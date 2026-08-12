from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Callable
from typing import Any


@dataclass(frozen=True, slots=True)
class WorkerResult:
    worker: str
    ok: bool
    value: Any = None
    error: str | None = None


def run_workers(workers: dict[str, Callable[[], Any]]) -> list[WorkerResult]:
    results: list[WorkerResult] = []
    for name, worker in workers.items():
        try:
            results.append(WorkerResult(name, True, worker()))
        except Exception as exc:
            results.append(WorkerResult(name, False, error=str(exc)))
    return results
