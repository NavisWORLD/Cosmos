from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
import sys

from ..config import CosmosConfig
from ..integration.services import probe_http


def health_report(config: CosmosConfig | None = None, timeout: float = 1.0) -> dict[str, object]:
    cfg = config or CosmosConfig.from_env()
    cfg.ensure_dirs()
    ollama = probe_http("ollama", f"{cfg.ollama_url.rstrip('/')}/api/tags", timeout=timeout)
    checks = [
        {"name": "python", "ok": sys.version_info >= (3, 10), "detail": sys.version.split()[0]},
        {"name": "data_dir", "ok": Path(cfg.data_dir).exists(), "detail": str(cfg.data_dir)},
        {**asdict(ollama), "optional": True},
    ]
    return {"ok": all(item["ok"] for item in checks if not item.get("optional")), "checks": checks}
