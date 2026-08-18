from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from time import sleep
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class Attempt(Generic[T]):
    ok: bool
    value: T | None = None
    error: str | None = None
    attempts: int = 0


def retry(call: Callable[[], T], *, attempts: int = 3, delay: float = 0.0) -> Attempt[T]:
    """Run a bounded retry loop and return an inspectable result instead of hiding failure."""
    if attempts < 1:
        raise ValueError("attempts must be >= 1")
    last_error: Exception | None = None
    for number in range(1, attempts + 1):
        try:
            return Attempt(ok=True, value=call(), attempts=number)
        except Exception as exc:  # explicit fail-soft boundary
            last_error = exc
            if delay > 0 and number < attempts:
                sleep(delay)
    return Attempt(ok=False, error=str(last_error), attempts=attempts)
