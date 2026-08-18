from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .llm_backend import Backend


@dataclass(frozen=True, slots=True)
class Candidate:
    backend: str
    text: str


class ModelSwarm:
    """Explicit multi-backend runner; it never silently treats consensus as truth."""

    def __init__(self, backends: Iterable[Backend]) -> None:
        self.backends = list(backends)

    def run(self, message: str, context: str = "") -> list[Candidate]:
        return [Candidate(getattr(backend, "name", type(backend).__name__), backend.generate(message, context)) for backend in self.backends]
