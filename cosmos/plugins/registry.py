from __future__ import annotations

from collections.abc import Callable
from typing import Any


class PluginRegistry:
    def __init__(self) -> None:
        self._plugins: dict[str, Callable[..., Any]] = {}

    def register(self, name: str, plugin: Callable[..., Any]) -> None:
        if not name or name in self._plugins:
            raise ValueError("plugin name must be non-empty and unique")
        self._plugins[name] = plugin

    def invoke(self, name: str, *args: Any, **kwargs: Any) -> Any:
        return self._plugins[name](*args, **kwargs)

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._plugins))
