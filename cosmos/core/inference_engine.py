from __future__ import annotations

from dataclasses import dataclass

from ..runtime import CosmosRuntime, TurnResult


@dataclass(slots=True)
class InferenceEngine:
    """Compatibility facade over the source-first COSMOS runtime."""

    runtime: CosmosRuntime

    def infer(self, message: str) -> TurnResult:
        return self.runtime.process_turn(message)
