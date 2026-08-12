from __future__ import annotations

from pathlib import Path


def validate_adapter_path(path: str | Path) -> Path:
    """Validate an external LoRA adapter path without loading or mutating model weights."""
    resolved = Path(path).expanduser().resolve()
    if not resolved.exists():
        raise FileNotFoundError(resolved)
    return resolved
