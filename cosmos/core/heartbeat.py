from __future__ import annotations

from dataclasses import dataclass
from time import monotonic
from typing import Callable, Any


@dataclass(slots=True)
class Task:
    name: str
    interval: float
    callback: Callable[[], Any]
    last_run: float = 0.0


class Heartbeat:
    """Fail-soft scheduler for consolidation, reflection, health and curiosity jobs."""

    def __init__(self, clock: Callable[[], float] = monotonic) -> None:
        self._clock = clock
        self._tasks: dict[str, Task] = {}

    def register(self, name: str, interval: float, callback: Callable[[], Any]) -> None:
        if interval <= 0:
            raise ValueError("interval must be positive")
        self._tasks[name] = Task(name=name, interval=float(interval), callback=callback)

    def run_due(self) -> list[dict[str, Any]]:
        now = self._clock()
        results: list[dict[str, Any]] = []
        for task in self._tasks.values():
            if task.last_run and now - task.last_run < task.interval:
                continue
            try:
                value = task.callback()
                results.append({"task": task.name, "ok": True, "result": value})
            except Exception as exc:  # fail-soft by design
                results.append({"task": task.name, "ok": False, "error": str(exc)})
            finally:
                task.last_run = now
        return results
