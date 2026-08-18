from tempfile import TemporaryDirectory
from pathlib import Path

from cosmos.config import CosmosConfig
from cosmos.runtime import CosmosRuntime

with TemporaryDirectory() as tmp:
    cfg = CosmosConfig(data_dir=Path(tmp), backend="echo")
    with CosmosRuntime(cfg) as runtime:
        result = runtime.process_turn("COSMOS smoke test")
        assert len(result.state) == 12
        assert runtime.status()["evidence"]["ok"]
print("COSMOS smoke test: OK")
