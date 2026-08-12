from __future__ import annotations

from statistics import mean
from typing import Sequence


def estimate_bpm(samples: Sequence[float], sample_rate: float, *, min_bpm: float = 40.0, max_bpm: float = 220.0) -> float | None:
    """Simple local peak-interval BPM estimator for already-acquired PPG samples.

    This is a signal-processing helper, not a medical device and not a HealthKit acquisition layer.
    """
    if sample_rate <= 0 or len(samples) < 3:
        return None
    values = [float(v) for v in samples]
    center = mean(values)
    threshold = center + 0.25 * (max(values) - min(values))
    min_distance = max(1, int(sample_rate * 60.0 / max_bpm))
    max_distance = max(min_distance + 1, int(sample_rate * 60.0 / min_bpm))
    peaks: list[int] = []
    last = -max_distance
    for i in range(1, len(values) - 1):
        if values[i] >= threshold and values[i] > values[i - 1] and values[i] >= values[i + 1] and i - last >= min_distance:
            if peaks and i - peaks[-1] > max_distance:
                peaks = []
            peaks.append(i)
            last = i
    if len(peaks) < 2:
        return None
    intervals = [(b - a) / sample_rate for a, b in zip(peaks, peaks[1:])]
    valid = [interval for interval in intervals if 60.0 / max_bpm <= interval <= 60.0 / min_bpm]
    return 60.0 / mean(valid) if valid else None
