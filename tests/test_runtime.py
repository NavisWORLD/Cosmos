from cosmos.config import CosmosConfig
from cosmos.runtime import CosmosRuntime


def test_runtime_closes_loop_and_persists(tmp_path):
    cfg = CosmosConfig(data_dir=tmp_path, backend="echo", memory_limit=4)
    with CosmosRuntime(cfg) as runtime:
        runtime.ingest_sensory({"audio_energy": 0.25, "motion": 0.1})
        result = runtime.process_turn("hello cosmos")
        assert "hello cosmos" in result.response
        assert len(result.state) == 12
        assert runtime.memory.count() == 2
        assert runtime.status()["evidence"]["ok"] is True
    with CosmosRuntime(cfg) as runtime:
        assert runtime.memory.count() == 2
