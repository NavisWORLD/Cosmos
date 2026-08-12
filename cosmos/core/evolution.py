from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
from typing import Iterable


class EvolutionEngine:
    """Small persistent pattern/cycle counter for explicit, inspectable adaptation."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.patterns: Counter[str] = Counter()
        self.cycles = 0
        self.load()

    def learn(self, patterns: Iterable[str]) -> int:
        for pattern in patterns:
            cleaned = pattern.strip().lower()
            if cleaned:
                self.patterns[cleaned] += 1
        self.cycles += 1
        self.save()
        return self.cycles

    def top(self, limit: int = 20) -> list[tuple[str, int]]:
        return self.patterns.most_common(limit)

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps({"cycles": self.cycles, "patterns": dict(self.patterns)}, indent=2, sort_keys=True), encoding="utf-8")

    def load(self) -> None:
        if not self.path.exists():
            return
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        self.cycles = int(raw.get("cycles", 0))
        self.patterns = Counter({str(k): int(v) for k, v in raw.get("patterns", {}).items()})
