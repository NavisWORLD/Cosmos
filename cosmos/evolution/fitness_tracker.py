from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class FitnessTracker:
    total: float = 0.0
    count: int = 0

    def add(self, score: float) -> float:
        self.total += float(score)
        self.count += 1
        return self.mean

    @property
    def mean(self) -> float:
        return self.total / self.count if self.count else 0.0
