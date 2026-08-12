from __future__ import annotations

from math import sqrt
from typing import Sequence


def audio_summary(samples: Sequence[float], sample_rate: float) -> dict[str, float]:
    """Dependency-free numeric audio summary for local sensor adapters."""
    if sample_rate <= 0:
        raise ValueError("sample_rate must be positive")
    if not samples:
        return {"rms": 0.0, "zero_crossing_rate": 0.0, "duration": 0.0}
    values = [float(v) for v in samples]
    rms = sqrt(sum(v * v for v in values) / len(values))
    crossings = sum(1 for a, b in zip(values, values[1:]) if (a < 0 <= b) or (a >= 0 > b))
    return {
        "rms": rms,
        "zero_crossing_rate": crossings / max(1, len(values) - 1),
        "duration": len(values) / float(sample_rate),
    }
