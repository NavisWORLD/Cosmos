from __future__ import annotations

from hashlib import blake2b
from typing import Mapping


def project_to_dyn12(features: Mapping[str, float]) -> tuple[float, ...]:
    """Deterministically project named numeric features into a bounded 12-scalar control vector."""
    out = [0.0] * 12
    for key, value in sorted(features.items()):
        digest = blake2b(key.encode("utf-8"), digest_size=16).digest()
        index = int.from_bytes(digest[:4], "big") % 12
        sign = 1.0 if digest[4] & 1 else -1.0
        out[index] += sign * float(value)
    scale = max(1.0, max((abs(v) for v in out), default=1.0))
    return tuple(v / scale for v in out)
