# Memory & Persistence Manual

“Forever memory” does **not** mean infinite context. It means durable retained records plus a mechanism capable of retrieving old relevant information into a finite current context.

## Memory layers
1. **Dialogue persistence** — turns survive process/session boundaries.
2. **Semantic recall** — retrieval by meaning, not only recency.
3. **Hebbian association memory** — concept co-occurrence/salience; separate from transformer weights and attention kernel.
4. **Consolidated/dream-derived records** — higher-level derived records that should point to primary sources.
5. **Routing/model plasticity** — slower model-trust/routing state, not dialogue memory.

## Loop
```text
new experience
 ├─ durable record
 ├─ embedding/index
 ├─ association + salience update
 └─ timestamp/hash
later query → semantic search → similarity/recency/confidence filter
→ compact memory context → response → store new experience ↺
```

## Why retrieval is the hard part
Writing JSON forever is not useful memory by itself. Measure whether the embedding/ranking system finds the genuinely relevant item above distractors; test thresholds, recency, deduplication, privacy, and consolidation lineage.

## Heartbeat
Background maintenance can trigger consolidation, reflection telemetry, health snapshots, and curiosity/research queueing. “Heartbeat” is a scheduler pattern, not a literal biological heartbeat.

## Test suite
Store distractors + one known relevant memory; retrieve semantically; restart; retrieve again; verify consolidation does not overwrite primary records; verify deletion/privacy policy and bounded context assembly.

## Tech
- [COSMOS core](../../cosmos/core/)
- [Memory tree](../../cosmos/core/memory/)
