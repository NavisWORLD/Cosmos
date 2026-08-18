from __future__ import annotations

import random
from typing import Sequence, TypeVar

T = TypeVar("T")


def mutate_choice(options: Sequence[T], *, seed: int | str | bytes | None = None) -> T:
    if not options:
        raise ValueError("options cannot be empty")
    return random.Random(seed).choice(list(options))
