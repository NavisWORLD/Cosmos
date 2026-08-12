from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path


@dataclass(slots=True)
class TrustWeight:
    value: float = 1.0
    updates: int = 0


class PlasticityStore:
    """Persistent, bounded model/domain trust weights with simple Hebbian-style updates."""

    def __init__(self, path: str | Path, learning_rate: float = 0.05, minimum: float = 0.05, maximum: float = 5.0) -> None:
        self.path = Path(path)
        self.learning_rate = float(learning_rate)
        self.minimum = float(minimum)
        self.maximum = float(maximum)
        self.weights: dict[str, TrustWeight] = {}
        self.load()

    def update(self, key: str, reward: float) -> float:
        item = self.weights.setdefault(key, TrustWeight())
        target = 1.0 + float(reward)
        item.value += self.learning_rate * (target - item.value)
        item.value = min(self.maximum, max(self.minimum, item.value))
        item.updates += 1
        self.save()
        return item.value

    def get(self, key: str, default: float = 1.0) -> float:
        return self.weights.get(key, TrustWeight(default)).value

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = {key: {"value": item.value, "updates": item.updates} for key, item in self.weights.items()}
        self.path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

    def load(self) -> None:
        if not self.path.exists():
            return
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        self.weights = {key: TrustWeight(float(item["value"]), int(item["updates"])) for key, item in raw.items()}
