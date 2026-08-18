from __future__ import annotations

from dataclasses import dataclass
from typing import Any


ORGANS = ("quantum", "dark_matter", "emeth", "plasticity", "awareness", "daemons", "surgeon")


@dataclass(slots=True)
class OrganStatus:
    enabled: bool = False
    healthy: bool = True
    detail: str = "deferred"
    state: dict[str, Any] | None = None


class CNS:
    """Seven-role runtime registry. Organ names are software architecture metaphors."""

    def __init__(self) -> None:
        self.organs = {name: OrganStatus() for name in ORGANS}

    def report(self, name: str, *, enabled: bool, healthy: bool, detail: str = "", state: dict[str, Any] | None = None) -> None:
        if name not in self.organs:
            raise KeyError(name)
        self.organs[name] = OrganStatus(enabled, healthy, detail, state)

    def snapshot(self) -> dict[str, dict[str, Any]]:
        return {
            name: {"enabled": item.enabled, "healthy": item.healthy, "detail": item.detail, "state": item.state or {}}
            for name, item in self.organs.items()
        }
