from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import random
from typing import Iterable, Sequence

from .evidence import canonical_json, lock_snapshot


@dataclass(frozen=True, slots=True)
class Forecast:
    model: str
    seed: str
    values: tuple[float, ...]
    receipt: dict


def seeded_rng(seed: str) -> random.Random:
    digest = sha256(seed.encode("utf-8")).digest()
    return random.Random(int.from_bytes(digest, "big"))


def persistence_baseline(series: Sequence[float]) -> float:
    if not series:
        raise ValueError("series cannot be empty")
    return float(series[-1])


def moving_average(series: Sequence[float], window: int = 5) -> float:
    if not series:
        raise ValueError("series cannot be empty")
    window = max(1, min(window, len(series)))
    return sum(series[-window:]) / window


def lottery_random_baseline(low: int, high: int, count: int, seed: str) -> tuple[int, ...]:
    if count <= 0 or high < low or count > high - low + 1:
        raise ValueError("invalid lottery schema")
    rng = seeded_rng(seed)
    return tuple(sorted(rng.sample(range(low, high + 1), count)))


def make_forecast(model: str, seed: str, values: Iterable[float], metadata: dict | None = None) -> Forecast:
    vals = tuple(float(v) for v in values)
    payload = {"model": model, "seed": seed, "values": vals, "metadata": metadata or {}}
    return Forecast(model=model, seed=seed, values=vals, receipt=lock_snapshot(payload))
