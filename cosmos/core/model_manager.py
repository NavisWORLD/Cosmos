from __future__ import annotations

from dataclasses import dataclass

from ..config import CosmosConfig
from ..integration.services import ServiceStatus, probe_http
from .llm_backend import EchoBackend, OllamaBackend, Backend
from ..integration.services import OllamaClient


@dataclass(slots=True)
class ModelManager:
    """Construct and inspect explicitly configured local inference backends."""

    config: CosmosConfig

    def backend(self) -> Backend:
        if self.config.backend == "echo":
            return EchoBackend()
        if self.config.backend == "ollama":
            return OllamaBackend(OllamaClient(self.config.ollama_url, self.config.ollama_model))
        raise ValueError(f"unsupported backend: {self.config.backend}")

    def ollama_status(self, timeout: float = 1.0) -> ServiceStatus:
        return probe_http("ollama", f"{self.config.ollama_url.rstrip('/')}/api/tags", timeout=timeout)
