# COSMOS Library Map

The pre-3.0 public repository contained many Python **bytecode-only** modules (`.pyc`) without their corresponding readable `.py` source. The 3.0 pass does not pretend those binaries can be reconstructed byte-for-byte from filenames. Instead, it rebuilds their defensible public responsibilities as readable, tested modules and documents consolidation where names changed.

## Source-first core

| 3.0 module | Responsibility |
|---|---|
| `cosmos.runtime` | closed conversation/state/memory/evidence loop |
| `cosmos.core.state` | dyn12 state + Gaussian affinity kernel + preflight |
| `cosmos.core.memory` | durable SQLite memory + local retrieval + associations |
| `cosmos.core.nexus` | explicit event bus |
| `cosmos.core.model_manager` | configured local backend construction/health |
| `cosmos.core.model_swarm` | explicit multi-backend candidate collection |
| `cosmos.core.llm_backend` | backend protocol, echo, Ollama |
| `cosmos.core.resilience` | bounded retry/fail-soft result |
| `cosmos.core.fcp` | deterministic named-feature → 12-state projection |
| `cosmos.core.cns` | seven-role status registry |
| `cosmos.core.plasticity` | persisted bounded trust weights |
| `cosmos.core.organism` | persisted aggregate runtime state; software metaphor |
| `cosmos.core.evolution` | persistent pattern/cycle counter |
| `cosmos.core.internal_monologue` | bounded auditable event history, not hidden chain-of-thought |
| `cosmos.core.quantum_bridge` | labeled provenance buffer |
| `cosmos.tools.evidence` | evidence labels + hash-chain ledger |
| `cosmos.tools.reality_bridge_processor` | deterministic forecast baselines/receipts |
| `cosmos.integration.services` | local service probes/Ollama adapter |
| `cosmos.integration.audio` | numeric audio summary helper |
| `cosmos.integration.bio.ppg` | signal-only PPG BPM helper |
| `cosmos.web.server` | localhost JSON API |

## Compatibility/source namespaces restored

Readable public namespaces were restored for:

- `cosmos.core.cognition` — explicit plans, intent hypotheses, uncertainty labels.
- `cosmos.core.collective` — worker orchestration and reviewable code-patch proposals.
- `cosmos.memory` — compatibility exports for the memory API.
- `cosmos.health` — source health report.
- `cosmos.plugins` — minimal plugin registry.
- `cosmos.os_integration` — read-only system summary.
- `cosmos.p2p` — safe disabled-by-default namespace; no unauthenticated WAN relay is shipped.
- `cosmos.evolution` — deterministic mutation/selection/fitness helpers and external LoRA-path validation.

## Historical names consolidated rather than falsely copied

The old compiled tree exposed names such as `context_profiles`, `fcp`, `inference_engine`, `llm_backend`, `model_manager`, `model_swarm`, `nexus`, `quantum_bridge`, `resilience`, cognition modules, collective modules, evolution modules, and planetary-memory helpers. Where the precise source was unavailable, 3.0 implements the documented engineering role from scratch or records it as future work rather than claiming binary equivalence.

The pre-cleanup snapshot remains available on `backup/pre-cosmos-cleanup-2026-08-12` for provenance and forensic comparison.
