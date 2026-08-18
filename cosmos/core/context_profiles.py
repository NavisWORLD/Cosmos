from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ContextProfile:
    """Named context policy used to bound what enters a model prompt."""

    name: str = "default"
    memory_limit: int = 8
    include_state: bool = True
    include_sensory: bool = True
    system_notes: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if self.memory_limit < 0:
            raise ValueError("memory_limit must be non-negative")
