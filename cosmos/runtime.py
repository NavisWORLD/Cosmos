from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, asdict
from hashlib import blake2b
from pathlib import Path
from typing import Any

from .config import CosmosConfig
from .core.heartbeat import Heartbeat
from .core.memory import SQLiteMemoryStore
from .core.state import Dyn12State
from .integration import OllamaClient
from .tools.evidence import EvidenceLedger

Responder = Callable[[str, str], str]


@dataclass(frozen=True, slots=True)
class TurnResult:
    response: str
    state: tuple[float, ...]
    memories: tuple[str, ...]
    backend: str


class CosmosRuntime:
    """Owner-controlled local runtime connecting state, memory, response and evidence."""

    def __init__(self, config: CosmosConfig | None = None, responder: Responder | None = None) -> None:
        self.config = config or CosmosConfig.from_env()
        self.config.ensure_dirs()
        self.memory = SQLiteMemoryStore(self.config.data_dir / "memory.sqlite3")
        self.evidence = EvidenceLedger(self.config.data_dir / "evidence.jsonl")
        self.state = Dyn12State()
        self.sensory: dict[str, float] = {}
        self.heartbeat = Heartbeat()
        self._responder = responder or self._build_responder()
        self.heartbeat.register("memory_health", 60.0, lambda: {"memories": self.memory.count()})
        self.heartbeat.register("evidence_health", 60.0, self._evidence_health)

    def close(self) -> None:
        self.memory.close()

    def __enter__(self) -> "CosmosRuntime":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def ingest_sensory(self, packet: dict[str, float]) -> dict[str, float]:
        clean: dict[str, float] = {}
        for key, value in packet.items():
            numeric = float(value)
            if numeric != numeric or numeric in (float("inf"), float("-inf")):
                raise ValueError(f"invalid sensory value for {key}")
            clean[str(key)] = numeric
        self.sensory = clean
        return dict(self.sensory)

    def process_turn(self, message: str) -> TurnResult:
        message = message.strip()
        if not message:
            raise ValueError("message cannot be empty")
        recalled = self.memory.recall(message, limit=self.config.memory_limit)
        memory_texts = tuple(item.text for item in recalled if item.score > 0.05)
        state = self.state.update(self._omega(message))
        context = self._context(memory_texts, state)
        response = self._responder(message, context)
        self.memory.remember(f"USER: {message}", tags=("dialogue", "user"), importance=0.55)
        self.memory.remember(f"COSMOS: {response}", tags=("dialogue", "assistant"), importance=0.5)
        self.evidence.append(
            "TURN_COMPLETED",
            "OBSERVED",
            {"backend": self.config.backend, "state": state, "memory_count": len(memory_texts)},
        )
        return TurnResult(response=response, state=state, memories=memory_texts, backend=self.config.backend)

    def status(self) -> dict[str, Any]:
        ledger_ok, events, error = self.evidence.verify()
        return {
            "version": "3.0.0",
            "backend": self.config.backend,
            "memory_count": self.memory.count(),
            "state": self.state.snapshot(),
            "sensory": dict(self.sensory),
            "evidence": {"ok": ledger_ok, "events": events, "error": error},
        }

    def _build_responder(self) -> Responder:
        if self.config.backend == "ollama":
            client = OllamaClient(self.config.ollama_url, self.config.ollama_model)
            return lambda message, context: client.generate(f"{context}\n\nUSER:\n{message}", system="You are COSMOS. Use retrieved memory only when relevant. Do not invent sensor readings or evidence.")
        if self.config.backend != "echo":
            raise ValueError(f"unsupported backend: {self.config.backend}")
        return lambda message, context: f"COSMOS local loop received: {message}"

    def _omega(self, message: str) -> list[float]:
        digest = blake2b(message.encode("utf-8"), digest_size=24).digest()
        values = []
        sensory_values = list(self.sensory.values())
        sensory_mean = sum(sensory_values) / len(sensory_values) if sensory_values else 0.0
        for i in range(12):
            raw = int.from_bytes(digest[i * 2 : i * 2 + 2], "big") / 65535.0
            values.append((raw * 2.0 - 1.0) + 0.05 * sensory_mean)
        return values

    def _context(self, memories: tuple[str, ...], state: tuple[float, ...]) -> str:
        memory_block = "\n".join(f"- {item}" for item in memories[: self.config.memory_limit]) or "- none"
        sensory_block = ", ".join(f"{k}={v:.4g}" for k, v in sorted(self.sensory.items())) or "none"
        state_block = ", ".join(f"{value:.4f}" for value in state)
        return f"RETRIEVED MEMORY:\n{memory_block}\nSENSORY SUMMARY: {sensory_block}\nDYN12 STATE: [{state_block}]"

    def _evidence_health(self) -> dict[str, Any]:
        ok, events, error = self.evidence.verify()
        return {"ok": ok, "events": events, "error": error}
