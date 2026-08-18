# Changelog

All notable public repository changes are documented here.

## [3.0.1] - 2026-08-18

### Provenance and ownership reset
- Rewrote the root README around Cory Shane Davis / NavisWORLD, the COSMOS/CST research story, the 2018 → 2024 → 2026 timeline, current engineering scope, evidence discipline, and ownership boundaries.
- Added `ORIGIN_AND_PROVENANCE.md` to separate personal origin, project chronology, public evidence, implementation, and legal conclusions.
- Replaced the current repository MIT license with a permission-only/all-rights-reserved copyright notice for Cory-owned Covered Original Material.
- Updated `CORY_DAVIS_IP_AND_ACCESS_NOTICE.md` and `COMMERCIAL_RIGHTS.md` so they match the current permission boundary while preserving valid earlier license grants for earlier copies/versions.
- Updated `CONTRIBUTING.md` to require prior approval and clearer contribution/provenance rights.
- Updated Python package metadata to `3.0.1` and changed the license classifier from MIT to `Other/Proprietary License`.
- Preserved third-party license boundaries and explicit limits on what copyright can protect.
- Preserved the scientific claim boundary: implementation, observation, measurement, null, hypothesis, and metaphor remain distinct.

### Repository lineage
- The canonical repository tree remains the reconstructed COSMOS-only source tree.
- The canonical branch ancestry was previously rebuilt from a clean root snapshot so discontinued mixed integration ancestry is not part of the supported `main` lineage.

## [3.0.0] - 2026-08-12

### Repository reconstruction
- Removed discontinued external integration packages, metadata, bridges, build artifacts, foreign package/license material, and related documentation from the current COSMOS tree.
- Removed tracked `node_modules`, Python bytecode/cache directories, generated scanner/test output, runtime logs, and local/private archival state.
- Replaced the compiled-bytecode-only public `cosmos/` tree with readable, testable source.

### Added
- Source-first `cosmos-cst` Python package and `cosmos` CLI.
- Dependency-free local closed-loop runtime.
- Dyn12 recurrent state, calibrated Gaussian state kernel, and mechanism-liveness preflight.
- SQLite durable memory, deterministic retrieval baseline, and Hebbian-style association store.
- Hash-chained evidence ledger and Reality Bridge forecast receipts/baselines.
- Labeled quantum provenance records and deterministic seed derivation.
- Heartbeat, Nexus, CNS registry, plasticity store, organism/evolution state, resilience utilities, and compatibility namespaces.
- Local Ollama adapter with explicit opt-in and no cloud fallback.
- Local JSON API with `/health`, `/state`, `/chat`, and `/sensory`.
- Dependency-free audio summary and already-acquired PPG BPM helper.
- Professional README, vision, roadmap, migration/library docs, security policy, contribution guide, Dockerfile, setup scripts, tests, smoke test, and GitHub Actions CI.

### Validation
- Core unit suite passes locally.
- Python source compiles successfully.
- CLI smoke/demo/state-preflight pass locally.
- Local HTTP server was exercised end-to-end for health, chat, sensory input, and state.
- Ollama, IBM/Azure quantum hardware, camera/microphone hardware, and mobile HealthKit/Health Connect acquisition remain optional environment-dependent integrations and are not represented as CI-validated hardware paths.

## [2.9.4] - 2026-03-01

Historical COSMOS development entry retained from the prior repository lineage. It documented work on swarm vision, acoustic feature ingestion, Hebbian plasticity, dynamic scaling, local model stability, port handling, quantum bridge initialization, and knowledge-graph entity resolution. The 3.0 reconstruction does not treat historical changelog prose as a substitute for reproducible source/tests.
