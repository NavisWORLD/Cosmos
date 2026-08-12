# COSMOS Architecture

## Closed loop

```text
input
  ↓
retrieve durable relevant memory
  ↓
read latest compact sensory summary (optional)
  ↓
update 12-scalar dynamic state
  ↓
construct bounded context
  ↓
local response backend (echo baseline or Ollama)
  ↓
persist user/response records
  ↓
append evidence event
  ↓
heartbeat maintenance jobs
  ↺
```

The implementation deliberately separates ordinary systems services from experimental neural/research ideas.

## Modules

### `cosmos.core.state`
Implements a recurrent 12-scalar state, distance-calibrated Gaussian affinity kernel, attention mixing primitive, and preflight liveness checks. It operationalizes one computational interpretation of CST; it does not assert literal physical dimensions.

### `cosmos.core.memory`
SQLite-backed persistence with a deterministic hashing-retrieval baseline and pairwise Hebbian-style association weights. The baseline is intentionally transparent and replaceable by a dedicated embedding adapter.

### `cosmos.runtime`
Connects memory, dynamic state, latest sensory summary, response backend, persistence, heartbeat, and evidence. The core does not silently call cloud AI.

### `cosmos.tools.evidence`
Hash-chained JSONL events with explicit epistemic labels. A hash chain protects record integrity; it does not prove a claim true.

### `cosmos.core.provenance`
Validates labeled bitstring records and derives deterministic hashes/seeds. This is provenance plumbing, not a quantum-advantage claim.

### `cosmos.web.server`
A dependency-free local HTTP interface. It uses numeric sensory packets and does not record raw media.

## Extension boundary

Heavy or hardware-dependent capabilities belong behind adapters/extras: local LLMs, embedding models, Torch transformers, quantum providers, microphone/camera, HealthKit/native bridges. Their absence must not prevent the core package from importing, testing, or running its local demo.
