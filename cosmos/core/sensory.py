from __future__ import annotations

from dataclasses import dataclass, field
from time import monotonic


@dataclass(slots=True)
class SensorySummary:
    freshness_seconds: float = 2.0
    values: dict[str, float] = field(default_factory=dict)
    updated_at: float = 0.0

    def update(self, values: dict[str, float]) -> None:
        clean: dict[str, float] = {}
        for key, value in values.items():
            numeric = float(value)
            if numeric != numeric or abs(numeric) == float("inf"):
                raise ValueError(f"invalid sensory value for {key}")
            clean[str(key)] = numeric
        self.values = clean
        self.updated_at = monotonic()

    def current(self) -> dict[str, float]:
        if not self.updated_at or monotonic() - self.updated_at > self.freshness_seconds:
            return {}
        return dict(self.values)
