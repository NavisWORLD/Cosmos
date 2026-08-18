# API Reference

## Python

```python
from cosmos import CosmosConfig, CosmosRuntime

config = CosmosConfig(data_dir="var", backend="echo")
with CosmosRuntime(config) as runtime:
    runtime.ingest_sensory({"audio_energy": 0.2})
    result = runtime.process_turn("hello")
    print(result.response)
```

### State

```python
from cosmos.core.state import Dyn12State, GaussianStateKernel, preflight
```

`Dyn12State.update(omega)` accepts one scalar or exactly 12 scalars. `GaussianStateKernel` calibrates bandwidth from nonzero pairwise distances. `preflight()` reports whether state varies and whether the kernel avoided identity/all-ones collapse.

### Memory

```python
from cosmos.core.memory import SQLiteMemoryStore
```

`remember(text, tags=(), importance=0.5)` persists a memory. `recall(query, limit=5)` ranks all retained memories using a deterministic local vector baseline plus bounded importance/recency terms. `top_associations(term)` returns learned co-occurrence weights.

### Evidence

```python
from cosmos.tools.evidence import EvidenceLedger
```

`append(event_type, status, payload)` appends a hash-chained event. `verify()` checks JSON validity, previous-hash continuity, and each event digest.

## HTTP

Run `python -m cosmos web`.

- `GET /health`
- `GET /state`
- `POST /chat` body `{"message":"..."}`
- `POST /sensory` body `{"packet":{"audio_energy":0.2}}`

The HTTP server is local by default (`127.0.0.1`). Binding to `0.0.0.0` exposes it to the network; add an authenticated reverse proxy before using it on untrusted networks.
