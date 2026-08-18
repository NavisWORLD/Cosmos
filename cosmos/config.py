from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os


@dataclass(slots=True)
class CosmosConfig:
    """Runtime configuration loaded from explicit values or environment variables."""

    data_dir: Path = Path("var")
    host: str = "127.0.0.1"
    port: int = 8081
    ollama_url: str = "http://127.0.0.1:11434"
    ollama_model: str = "qwen2.5:1.5b"
    backend: str = "echo"
    memory_limit: int = 8

    @classmethod
    def from_env(cls) -> "CosmosConfig":
        return cls(
            data_dir=Path(os.getenv("COSMOS_DATA_DIR", "var")),
            host=os.getenv("COSMOS_HOST", "127.0.0.1"),
            port=int(os.getenv("COSMOS_PORT", "8081")),
            ollama_url=os.getenv("COSMOS_OLLAMA_URL", "http://127.0.0.1:11434"),
            ollama_model=os.getenv("COSMOS_OLLAMA_MODEL", "qwen2.5:1.5b"),
            backend=os.getenv("COSMOS_BACKEND", "echo").lower(),
            memory_limit=max(1, int(os.getenv("COSMOS_MEMORY_LIMIT", "8"))),
        )

    def ensure_dirs(self) -> None:
        self.data_dir.mkdir(parents=True, exist_ok=True)
