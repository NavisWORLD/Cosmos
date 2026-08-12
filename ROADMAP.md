# COSMOS Roadmap

This roadmap is deliberately split into **working core**, **next engineering work**, and **research validation**. Checked items describe the public source-first 3.0 foundation, not every historical local prototype.

## 3.0 — Repository reconstruction and professional core

- [x] Remove unrelated Farnsworth package, metadata, build products, node_modules, logs, and private runtime archive from the current tree.
- [x] Preserve a pre-cleanup Git branch for audit/recovery.
- [x] Replace compiled-only public COSMOS package with readable Python source.
- [x] Dependency-free local runtime and CLI.
- [x] SQLite persistent memory + deterministic retrieval baseline + association store.
- [x] Dyn12 recurrent state and calibrated Gaussian state-kernel preflight.
- [x] Hash-chained evidence ledger and forecast snapshot receipts.
- [x] Labeled quantum provenance primitives.
- [x] Fail-soft heartbeat, CNS registry, plasticity, organism/evolution aggregates, Nexus event bus.
- [x] Local Ollama adapter with no cloud fallback.
- [x] Dependency-free local JSON API.
- [x] Audio summary and already-acquired PPG signal helper.
- [x] Tests, smoke test, Dockerfile, CI, security/contribution docs.

## 3.1 — Retrieval and service hardening

- [ ] Add a purpose-built embedding adapter behind the existing memory interface and benchmark it against the hashing baseline.
- [ ] Add schema migrations/versioning for persistent stores.
- [ ] Add authenticated API mode before any non-loopback deployment.
- [ ] Add structured logging with privacy filters and configurable retention.
- [ ] Add service ownership/PID tracking for safe local start/stop workflows.
- [ ] Expand deterministic integration tests for Ollama using a mock HTTP service.

## 3.2 — Research architecture package

- [ ] Publish the exact PHOS/dyn12 training architecture as an installable optional ML package.
- [ ] Re-run state ladder on frozen, versioned datasets and publish machine-readable per-seed results.
- [ ] Keep kernel/Ω/gate/coupling preflight mandatory in benchmark harnesses.
- [ ] Add scaling harnesses for additional public corpora/models.

## 3.3 — Sensory and bio adapters

- [ ] Native iOS/Android bridge for permissioned sensor summaries.
- [ ] HealthKit/Health Connect adapters that expose explicit aggregates only.
- [ ] Camera/microphone feature adapters with freshness gates and opt-in retention.
- [ ] Timestamped paired-state research logger with aligned/shuffled/shifted controls.

## 3.4 — Quantum provenance adapters

- [ ] IBM/Azure provider adapters behind the provenance interface.
- [ ] Hardware/simulator labels enforced at ingestion.
- [ ] Archive manifest verification and shot/accounting tests.
- [ ] Continue matched classical controls; preserve null results.

## Creative / simulation projects

- [ ] Publish canonical Reality Bridge Alien Conductor browser artifact under `examples/`.
- [ ] Publish canonical Reality Bridge Prediction browser artifact under `examples/`.
- [ ] Publish Universe Simulation Engine C++/Python package with deterministic seed/export tests.
- [ ] Keep these projects linked through `PORTFOLIO/` and technical evidence pages.
