from __future__ import annotations

from dataclasses import dataclass, asdict
import json
from pathlib import Path


@dataclass(slots=True)
class OrganismState:
    generation: int = 0
    experience_count: int = 0
    reward_total: float = 0.0


class Organism:
    """Persistent aggregate runtime state. The name is a software metaphor."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.state = OrganismState()
        self.load()

    def observe(self, reward: float = 0.0) -> OrganismState:
        self.state.experience_count += 1
        self.state.reward_total += float(reward)
        self.save()
        return self.state

    def advance_generation(self) -> int:
        self.state.generation += 1
        self.save()
        return self.state.generation

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(asdict(self.state), indent=2, sort_keys=True), encoding="utf-8")

    def load(self) -> None:
        if self.path.exists():
            self.state = OrganismState(**json.loads(self.path.read_text(encoding="utf-8")))
