from __future__ import annotations

from dataclasses import dataclass
import json
import socket
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


@dataclass(frozen=True, slots=True)
class ServiceStatus:
    name: str
    endpoint: str
    ok: bool
    detail: str


def probe_http(name: str, endpoint: str, timeout: float = 1.5) -> ServiceStatus:
    try:
        with urlopen(endpoint, timeout=timeout) as response:
            return ServiceStatus(name, endpoint, 200 <= response.status < 500, f"HTTP {response.status}")
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        return ServiceStatus(name, endpoint, False, str(exc))


def probe_tcp(name: str, host: str, port: int, timeout: float = 1.0) -> ServiceStatus:
    endpoint = f"tcp://{host}:{port}"
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return ServiceStatus(name, endpoint, True, "reachable")
    except OSError as exc:
        return ServiceStatus(name, endpoint, False, str(exc))


class OllamaClient:
    """Tiny stdlib Ollama adapter. No cloud fallback is performed."""

    def __init__(self, base_url: str, model: str, timeout: float = 120.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout

    def generate(self, prompt: str, system: str = "") -> str:
        payload: dict[str, Any] = {"model": self.model, "prompt": prompt, "stream": False}
        if system:
            payload["system"] = system
        request = Request(
            f"{self.base_url}/api/generate",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(request, timeout=self.timeout) as response:
            data = json.loads(response.read().decode("utf-8"))
        return str(data.get("response", "")).strip()
