from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PatchProposal:
    path: str
    rationale: str
    replacement: str


def propose(path: str, replacement: str, rationale: str) -> PatchProposal:
    """Create a proposal object only. Applying changes remains an explicit reviewed action."""
    if not path.strip() or not rationale.strip():
        raise ValueError("path and rationale are required")
    return PatchProposal(path.strip(), rationale.strip(), replacement)
