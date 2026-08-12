from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Step:
    index: int
    action: str


def plan(actions: list[str]) -> tuple[Step, ...]:
    """Create an explicit user-visible action plan; this is not hidden chain-of-thought."""
    return tuple(Step(i + 1, action.strip()) for i, action in enumerate(actions) if action.strip())
