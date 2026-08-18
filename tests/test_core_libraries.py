from cosmos.core.cns import CNS
from cosmos.core.evolution import EvolutionEngine
from cosmos.core.internal_monologue import InternalMonologue
from cosmos.core.organism import Organism
from cosmos.core.plasticity import PlasticityStore
from cosmos.core.provenance import QuantumRecord
from cosmos.core.quantum_bridge import QuantumBridge


def test_persistent_support_libraries(tmp_path):
    plastic = PlasticityStore(tmp_path / "plastic.json")
    assert plastic.update("local", 1.0) > 1.0
    assert PlasticityStore(tmp_path / "plastic.json").get("local") > 1.0

    thoughts = InternalMonologue(tmp_path / "thoughts.jsonl", max_items=3)
    thoughts.add("health check", "heartbeat")
    assert thoughts.recent(1)[0].text == "health check"

    organism = Organism(tmp_path / "organism.json")
    organism.observe(0.5)
    organism.advance_generation()
    assert Organism(tmp_path / "organism.json").state.generation == 1

    evolution = EvolutionEngine(tmp_path / "evolution.json")
    evolution.learn(["memory", "memory", "state"])
    assert evolution.top(1)[0] == ("memory", 2)

    bridge = QuantumBridge()
    bridge.ingest(QuantumRecord("ibm", "backend", ("01", "10"), "hardware", "job"))
    assert bridge.status()["source_kind"] == "hardware"
    assert len(bridge.seed()) == 64

    cns = CNS()
    cns.report("quantum", enabled=True, healthy=True, detail="archive")
    assert cns.snapshot()["quantum"]["enabled"] is True


def test_nexus_fcp_and_plugin_registry():
    from cosmos.core import Nexus, project_to_dyn12
    from cosmos.plugins import PluginRegistry
    seen = []
    bus = Nexus()
    bus.subscribe("x", lambda event: seen.append(event.payload["v"]))
    bus.publish("x", {"v": 3})
    assert seen == [3]
    assert len(project_to_dyn12({"audio": 0.2, "motion": 0.1})) == 12
    registry = PluginRegistry()
    registry.register("double", lambda value: value * 2)
    assert registry.invoke("double", 4) == 8


def test_audio_and_ppg_helpers():
    from math import sin, pi
    from cosmos.integration import audio_summary, estimate_bpm
    samples = [sin(2 * pi * 2 * i / 100) for i in range(100)]
    summary = audio_summary(samples, 100)
    assert summary["rms"] > 0
    # synthetic narrow pulses at 60 BPM, 100 Hz
    ppg = [0.0] * 401
    for i in (50, 150, 250, 350):
        ppg[i] = 1.0
    bpm = estimate_bpm(ppg, 100)
    assert bpm is not None and abs(bpm - 60.0) < 1e-6
