# COSMOS Roadmap

This roadmap is split into **working core**, **provenance/rights hardening**, **next engineering work**, and **research validation**. Checked items describe the current supported source-first COSMOS foundation, not every historical prototype.

## 3.0 — Repository reconstruction and professional core

- [x] Remove discontinued external integration material, generated build products, `node_modules`, logs, and private runtime archives from the current tree.
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

## 3.0.1 — Provenance, ownership, and rights hardening

- [x] Rebuild the canonical supported branch from a clean COSMOS root snapshot.
- [x] Re-anchor contaminated historical branches away from discontinued integration ancestry while preserving unrelated clean work where possible.
- [x] Rewrite the README around Cory Shane Davis / NavisWORLD and the 2018 → 2024 → 2026 COSMOS/CST story.
- [x] Add `ORIGIN_AND_PROVENANCE.md`.
- [x] Add `DISPUTED_PROVENANCE_AND_EVIDENCE_NOTICE.md`.
- [x] Replace the current-tree MIT license with a permission-only copyright notice while explicitly preserving valid prior grants for earlier copies/versions.
- [x] Align commercial-rights, contribution, package metadata, and portfolio language with the current permission boundary.
- [x] Preserve third-party license boundaries and avoid claiming ownership of generic prior art, public algorithms, or scientific concepts.
- [x] State that repository cleanup is not a waiver, release, abandonment, assignment, consent, or surrender of preserved evidence or claims.
- [ ] Obtain qualified IP counsel review of the provenance/evidence package before relying on it in a specific legal dispute.
- [ ] Maintain an offline, immutable evidence archive containing original files, hashes, exports, correspondence, platform timestamps, DOI records, and chain-of-custody notes.

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
