from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True, slots=True)
class Event:
    topic: str
    payload: dict[str, Any]
    timestamp: str


class Nexus:
    """Small synchronous event bus for explicit runtime coordination."""

    def __init__(self) -> None:
        self._subscribers: dict[str, list[Callable[[Event], None]]] = defaultdict(list)

    def subscribe(self, topic: str, callback: Callable[[Event], None]) -> Callable[[], None]:
        self._subscribers[topic].append(callback)

        def unsubscribe() -> None:
            if callback in self._subscribers.get(topic, []):
                self._subscribers[topic].remove(callback)

        return unsubscribe

    def publish(self, topic: str, payload: dict[str, Any] | None = None) -> Event:
        event = Event(topic, dict(payload or {}), datetime.now(timezone.utc).isoformat())
        for callback in tuple(self._subscribers.get(topic, ())):
            callback(event)
        return event
