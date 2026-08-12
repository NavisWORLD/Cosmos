# Changelog

All notable public repository changes are documented here.

## [3.0.0] - 2026-08-12

### Repository reconstruction
- Removed the unrelated Farnsworth Python package, Farnsworth package metadata, Farnsworth Node/MCP bridge, Farnsworth build artifacts, foreign Farnsworth license, and Farnsworth documentation from the current COSMOS tree.
- Removed tracked `node_modules`, Python bytecode/cache directories, generated scanner/test output, runtime logs, and local/private archival state.
- Preserved the pre-cleanup repository at branch `backup/pre-cosmos-cleanup-2026-08-12` and in Git history.
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
