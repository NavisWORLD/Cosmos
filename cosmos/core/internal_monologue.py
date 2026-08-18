from __future__ import annotations

from collections import deque
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import json
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Thought:
    timestamp: str
    text: str
    source: str = "runtime"


class InternalMonologue:
    """Bounded auditable thought/event history; not hidden chain-of-thought inference."""

    def __init__(self, path: str | Path, max_items: int = 100) -> None:
        self.path = Path(path)
        self.items: deque[Thought] = deque(maxlen=max_items)
        self._load()

    def add(self, text: str, source: str = "runtime") -> Thought:
        thought = Thought(datetime.now(timezone.utc).isoformat(), text.strip(), source)
        if not thought.text:
            raise ValueError("thought text cannot be empty")
        self.items.append(thought)
        self._save()
        return thought

    def recent(self, limit: int = 10) -> tuple[Thought, ...]:
        return tuple(list(self.items)[-max(0, limit):])

    def _save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text("\n".join(json.dumps(asdict(item), ensure_ascii=False) for item in self.items) + ("\n" if self.items else ""), encoding="utf-8")

    def _load(self) -> None:
        if not self.path.exists():
            return
        for line in self.path.read_text(encoding="utf-8").splitlines()[-self.items.maxlen:]:
            if line.strip():
                self.items.append(Thought(**json.loads(line)))
