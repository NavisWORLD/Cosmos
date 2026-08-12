# COSMOS / REALITY BRIDGE
## Research, Engineering & Creative-Systems Portfolio

**Cory Shane Davis · 2018 → 2024 → 2026**

This is the public front door for a body of work that grew from speculative systems ideas into executable software, controlled ML experiments, persistent-memory systems, local-first cognitive-runtime engineering, simulations, browser instruments, evidence tooling, and creative AI experiments.

The purpose of this portfolio is not to make every historical idea look correct. It is to preserve the lineage and make it inspectable.

## One-sentence system definition

COSMOS is a local-first experimental cognitive runtime built around language-model inference, dynamic internal state, persistent/semantic memory, Hebbian-style association and routing, sensory summaries, autonomous maintenance loops, evidence/provenance tooling, and optional quantum-derived entropy/provenance paths.

## The rule of the repository

**Claims follow instrumentation.**

Every item is classified as one or more of:

- **IMPLEMENTED** — a code path or artifact exists.
- **OBSERVED** — runtime evidence shows it executed.
- **MEASURED** — a defined benchmark produced a result.
- **NULL** — a test did not support the proposed advantage.
- **HYPOTHESIS** — a falsifiable idea still requiring evidence.
- **METAPHOR / MODEL** — a conceptual design language, not a literal physical or biological claim.

## Portfolio map

| Area | What it covers | Manual / evidence | Technical anchor |
|---|---|---|---|
| COSMOS + CST | Lineage, 12D/42D/54D state, attention modulation | [Architecture Manual](MANUALS/COSMOS_CST_ARCHITECTURE.md) | [CosmicSynapse CST simulation](https://github.com/NavisWORLD/CosmicSynapse/blob/main/cst_simulation.py) |
| PHOS | Small-model dyn12 architecture and growth lineage | [PHOS Manual](MANUALS/PHOS_AND_TRANSFORMER.md) | [Public HF architecture](https://huggingface.co/phera-ra/QC67_cosmo/tree/main/architecture) |
| Memory | Cross-session persistence, semantic recall, associations, consolidation | [Memory Manual](MANUALS/MEMORY_AND_PERSISTENCE.md) | [COSMOS core](../cosmos/core/) |
| CNS / loops | Runtime routing, state, heartbeat, services | [Runtime Manual](MANUALS/CNS_RUNTIME_AND_LOOPS.md) | [COSMOS source tree](../cosmos/) |
| Quantum provenance | Entropy provenance and matched null controls | [Quantum Manual](MANUALS/QUANTUM_PROVENANCE.md) | [HF findings](https://huggingface.co/phera-ra/QC67_cosmo/blob/main/FINDINGS.md) |
| Universe engine | Deterministic worlds, orbital/surface simulation, data adapters | [Universe Manual](MANUALS/UNIVERSE_SIMULATION_ENGINE.md) | [Publication status](PUBLICATION_GAPS.md) |
| Music instruments | Audio engine, accompaniment, sensor-driven generative control | [Music Manual](MANUALS/MUSIC_AND_ALIEN_CONDUCTOR.md) | [12D audio demo](../12D_Cosmic_Synapse_Audio_Engine-demo.html) |
| Reality Bridge Prediction | Baselines, walk-forward tests, evidence ledger, lottery stress test | [Prediction Manual](MANUALS/REALITY_BRIDGE_PREDICTION.md) | [Reality Bridge processor](../cosmos/tools/reality_bridge_processor.py) |
| CLI / autonomous engineering | Local services, health, tools, proposal/test/apply workflow | [CLI Manual](MANUALS/AUTONOMOUS_ENGINEERING_CLI.md) | [Tools](../cosmos/tools/) |
| Origins × COSMOS | Cross-project prototype / interoperability study | [Origins Manual](MANUALS/ORIGINS_X_COSMOS.md) | [Publication status](PUBLICATION_GAPS.md) |
| Navier–Stokes | Mathematical exploration and proof-boundary discipline | [Research Labs](MANUALS/RESEARCH_AND_CREATIVE_LABS.md#navierstokes-research-conversations) | documentation/research only |
| Creative AI Lab | Album, film/writing, comedy, photography experiments | [Research Labs](MANUALS/RESEARCH_AND_CREATIVE_LABS.md#creative-ai-lab) | [Audio demo](../12D_Cosmic_Synapse_Audio_Engine-demo.html) |

## What is unusual here

The strongest through-line is not a single grand claim. It is the attempt to make several timescales of state coexist in one owner-controlled environment: per-token dynamic state, per-turn dialogue state, cross-session semantic memory, slower Hebbian association/routing, periodic consolidation, service health, and reproducible research snapshots.

The project also preserves negative evidence. Published tests include positive bounded architecture results for dyn12, but also null results for quantum-vs-classical accuracy advantage and for paired sensory-state conditioning versus plain attention. Those nulls are part of the portfolio rather than deleted from the story.

## Read this in order

1. [Project Atlas](PROJECT_ATLAS.md)
2. [Evidence & Validation](EVIDENCE_AND_VALIDATION.md)
3. [Technical Index](TECHNICAL_INDEX.md)
4. [ChatGPT Build-Log Index](CHATGPT_BUILD_LOG_INDEX.md)
5. [Manuals](MANUALS/)
6. [Security & Privacy](SECURITY_AND_PRIVACY.md)
7. [Publication Gaps](PUBLICATION_GAPS.md)

## Public anchors

- COSMOS repository: https://github.com/NavisWORLD/Cosmos
- Hugging Face release: https://huggingface.co/phera-ra/QC67_cosmo
- Zenodo CST deposit: https://doi.org/10.5281/zenodo.17574447
- Earlier CST repository: https://github.com/NavisWORLD/CosmicSynapse
- X public notebook: https://x.com/corebear667

This portfolio is deliberately written so another engineer can disagree with the theory and still reproduce, inspect, test, or reuse the engineering patterns.
