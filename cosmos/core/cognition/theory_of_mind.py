from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class IntentHypothesis:
    label: str
    confidence: float
    evidence: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be in [0, 1]")


def rank_hypotheses(items: list[IntentHypothesis]) -> list[IntentHypothesis]:
    """Rank declared intent hypotheses without claiming access to another mind."""
    return sorted(items, key=lambda item: item.confidence, reverse=True)
