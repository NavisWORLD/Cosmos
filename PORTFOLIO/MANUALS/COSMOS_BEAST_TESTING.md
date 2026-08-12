# COSMOS Beast Testing Manual

“Beast testing” means integration/stress testing of the whole runtime, not evidence that surprising behavior automatically has a surprising cause.

## Stress domains
Local model availability/latency, memory recovery, state-kernel liveness, service lifecycle, port ownership, sensory freshness, quantum backend failure, telemetry schema, file locks, autonomous proposal lanes, CPU/RAM pressure, optional dependency failure.

## Phases
0. Snapshot commit/environment/checkpoints/corpus/services.
1. Static compile/import/config preflight.
2. Service health and process ownership.
3. Mechanism liveness: Ω/state/kernel/gates/couplings.
4. Persistence across restart.
5. Deliberate subsystem degradation.
6. Long-run/load test.
7. Export evidence package with logs/hashes/metrics/nulls/anomalies.

## Known failure classes
Stale model process; port collision; missing optional audio; absent WebSocket support; scientific-Python DLL/import conflict; file lock; syntax/import regression; telemetry drop/reorder; quantum refill failure; corpus drift.

## Causal discipline
A good result says what ran, for how long, under what version/configuration, and what failed. An unrelated hardware failure after a run is not automatically caused by the software; causal claims require instrumentation.

## Tech
- [Evidence processor](../../cosmos/tools/cosmos_evidence_processor.py)
- [Tools](../../cosmos/tools/)
