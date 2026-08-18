from __future__ import annotations

from typing import Protocol
from dataclasses import dataclass

from ..integration.services import OllamaClient


class Backend(Protocol):
    name: str
    def generate(self, message: str, context: str = "") -> str: ...


@dataclass(slots=True)
class EchoBackend:
    name: str = "echo"

    def generate(self, message: str, context: str = "") -> str:
        return f"COSMOS local loop received: {message}"


@dataclass(slots=True)
class OllamaBackend:
    client: OllamaClient
    name: str = "ollama"

    def generate(self, message: str, context: str = "") -> str:
        prompt = f"{context}\n\nUSER:\n{message}" if context else message
        return self.client.generate(
            prompt,
            system="You are COSMOS. Use retrieved memory only when relevant. Do not invent sensor readings or evidence.",
        )
