from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Callable
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class Scored(Generic[T]):
    candidate: T
    score: float


def select(candidates: list[T], fitness: Callable[[T], float], keep: int = 1) -> list[Scored[T]]:
    if keep < 1:
        raise ValueError("keep must be >= 1")
    ranked = [Scored(candidate, float(fitness(candidate))) for candidate in candidates]
    return sorted(ranked, key=lambda item: item.score, reverse=True)[:keep]
