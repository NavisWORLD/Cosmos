# COSMOS

## Cory Shane Davis / NavisWORLD

**COSMOS is a local-first experimental cognitive runtime and the engineering home of Davis Cosmic Synapse Theory (CST).**

I did not start this as a product or as a wrapper around somebody else’s project. COSMOS grew out of a long-running attempt to answer a different question: **what happens if an AI system is allowed to carry structured internal state, durable memory, associations, sensory context, evidence, and learning signals across time instead of behaving like every interaction starts from zero?**

That question became a research lineage.

**2018 → 2024 → 2026** is the timeline I use for that lineage:

- **2018 — origin.** The early phase was conceptual and personal: thinking about memory, state, chaos, information, recurrence, and how a computational system might preserve continuity instead of acting like a stateless tool. This is the origin point of the research story, not a claim that every later mechanism was already implemented then.
- **2024 — CST becomes a formal research program.** The work was organized around what I call **Davis Cosmic Synapse Theory**, including a 12-dimensional computational/state vocabulary and hypotheses connecting dynamic state, memory, chaos, sensory information, and adaptive computation. The research archive linked by this repository includes the work identified as *The 12-Dimensional Cosmic Synapse Theory* and Zenodo DOI **10.5281/zenodo.17574447**.
- **2025 — theory turns into systems.** The project moved into persistent memory, learn/save/load restoration, evolving world state, sensory/context bridges, multi-store memory, online learning, bounded association memory, autonomous study loops, and increasingly explicit perception → hypothesis → action → evidence cycles.
- **2026 — COSMOS becomes the integrated runtime.** The separate experiments were pulled into a local-first engineering environment with dynamic internal state, durable memory, Hebbian-style associations, model orchestration, evidence/provenance tooling, heartbeat/maintenance loops, sensory summaries, simulation and creative systems, quantum-provenance experiments, reproducible tests, and an operator-facing CLI/API.

The result is not one magic algorithm. It is an **architecture for continuity**: a system where memory, state, evidence, tools, and learning can interact through explicit interfaces and be inspected rather than hidden behind a story.

---

## What COSMOS is

COSMOS is an experimental AI/runtime platform built around several recurring ideas:

- **Dynamic internal state** — compact recurrent state, including Dyn12/CST mechanisms, that can influence computation over time.
- **Persistent memory** — durable local storage, retrieval, association weights, and restoration across sessions.
- **Hebbian-style adaptation** — bounded association updates and plasticity-inspired learning mechanisms.
- **Local model orchestration** — local-first backends such as Ollama, with cloud services treated as explicit optional integrations rather than hidden dependencies.
- **Evidence and provenance** — hash-chained records, reproducible seeds, explicit claim labels, controls, and receipts.
- **Heartbeat and maintenance loops** — fail-soft background tasks and recurring system maintenance.
- **Sensory/context bridges** — compact summaries from audio, motion, camera/PPG-style inputs, or other sensors without requiring raw private streams in the core runtime.
- **Simulation and creative systems** — Reality Bridge experiments, music systems, world/simulation engines, and controlled predictive baselines.
- **Quantum provenance research** — labeled use of quantum-derived randomness/provenance where available, without pretending that quantum provenance automatically proves quantum performance advantage.

The current `cosmos/` package is the canonical source-first implementation.

---

## What makes this project different

The central design choice is that **state is not treated as disposable metadata**.

A normal language-model interaction can be approximated as:

```text
prompt → model → response
```

COSMOS is designed more like:

```text
input
  ↓
state + memory + associations + sensory/context + evidence
  ↓
model / reasoning / tools
  ↓
response + updated state + durable memory + receipt
  ↓
next interaction
```

The research question is not “can I make a chatbot sound alive?” It is whether persistent computational state, memory, plasticity, evidence, and controlled feedback can produce useful measurable behavior that survives sessions, restarts, model changes, and different runtime environments.

---

## The current working core

The dependency-light Python core includes:

- **Dyn12 state** — recurrent 12-scalar control state with a calibrated Gaussian state-affinity kernel and mechanism preflight checks.
- **Persistent memory** — SQLite durability, deterministic retrieval baselines, and Hebbian-style concept association weights.
- **COSMOS Runtime** — closes the loop across memory, state, optional sensory summary, response backend, persistence, and evidence.
- **Local Ollama adapter** — opt-in localhost inference with no required cloud fallback.
- **Evidence ledger** — append-only JSONL with SHA-256 hash chaining and explicit evidence statuses.
- **Reality Bridge baselines** — deterministic forecast receipts and baseline comparison utilities.
- **Quantum provenance primitives** — labeled record validation and deterministic seed derivation.
- **Heartbeat** — fail-soft scheduled maintenance jobs.
- **Local JSON API** — `/health`, `/state`, `/chat`, and `/sensory`.
- **CLI** — `info`, `doctor`, `demo`, `chat`, `web`, `evidence-verify`, and `state-preflight`.

---

## Evidence before mythology

COSMOS has accumulated ambitious language over its history, so this repository uses explicit evidence labels:

- `IMPLEMENTED` — inspectable mechanism exists in source.
- `OBSERVED` — captured runtime evidence shows the mechanism executed.
- `MEASURED` — a declared benchmark produced a metric.
- `NULL` — the declared success condition was not supported.
- `HYPOTHESIS` — a falsifiable interpretation awaiting stronger evidence.
- `METAPHOR_MODEL` — conceptual language, not a literal scientific claim.

That means this repository does **not** claim that:

- COSMOS is proven conscious or sentient;
- CST dimensions are established literal physical dimensions;
- quantum-derived randomness proves a quantum-computing advantage;
- persistence or autonomy alone proves intelligence;
- a prediction interface can guarantee future random events.

I would rather preserve a null result than erase it to make the story sound better. The point of the project is to build mechanisms that can survive inspection.

---

## Ownership, provenance, and the clean COSMOS lineage

The current repository was rebuilt into a COSMOS-only source tree and separated from discontinued external integration material. The canonical `main` history was also rebuilt from a clean root so the supported project lineage now begins from the current COSMOS source snapshot.

This repository distinguishes:

1. **Cory Shane Davis / NavisWORLD original material** — original source, documentation, architecture, experiments, diagrams, datasets/records, and other copyrightable expression created and owned by Cory Shane Davis / NavisWORLD.
2. **Third-party components** — libraries, models, APIs, datasets, standards, or other material that remain governed by their own licenses and terms.
3. **Prior distributions** — copies or versions previously released under a different valid license remain subject to whatever rights were validly granted for those copies. A new notice cannot retroactively revoke an earlier grant.
4. **Ideas and methods** — copyright protects original expression, including software and documentation, but does not by itself give ownership over abstract ideas, systems, algorithms, methods, or discoveries. Patent, trademark, trade-secret, contract, and other law may apply separately where available.

Public chronology, repository timestamps, and DOI records can document **when this work existed**. They should not be misrepresented as automatic proof that another person copied it.

See:

- [`CORY_DAVIS_IP_AND_ACCESS_NOTICE.md`](CORY_DAVIS_IP_AND_ACCESS_NOTICE.md)
- [`COMMERCIAL_RIGHTS.md`](COMMERCIAL_RIGHTS.md)
- [`ORIGIN_AND_PROVENANCE.md`](ORIGIN_AND_PROVENANCE.md)
- [`LICENSE`](LICENSE)

### Current permission boundary

**The current repository revision is not offered under MIT or another open-source license.**

Unless a specific file says otherwise, Cory Shane Davis / NavisWORLD reserves all copyright rights in covered original material. No permission is granted to copy, modify, redistribute, sublicense, sell, commercialize, host as a service, incorporate covered material into another product, create derivative works, or use covered original material for commercial AI/ML training, fine-tuning, distillation, synthetic-data generation, embedding, or model development except through a separate written authorization or where applicable law independently permits the activity.

Inspection, citation, security review, and evaluation remain subject to applicable law, GitHub terms, and any explicit written permission attached to a particular file or release.

**Commercial or additional use requires a separate written agreement with Cory Shane Davis / NavisWORLD.**

---

## Quick start

```bash
git clone https://github.com/NavisWORLD/Cosmos.git
cd Cosmos
python -m venv .venv
```

Windows:

```bat
.venv\Scripts\activate
python -m pip install -U pip
pip install -e ".[dev]"
pytest
python -m cosmos demo
```

macOS/Linux:

```bash
source .venv/bin/activate
python -m pip install -U pip
pip install -e '.[dev]'
pytest
python -m cosmos demo
```

### Use a local model

COSMOS defaults to a dependency-free `echo` backend so installation and tests never require a model server.

```bash
export COSMOS_BACKEND=ollama
export COSMOS_OLLAMA_MODEL=qwen2.5:1.5b
python -m cosmos doctor
python -m cosmos chat
```

Windows PowerShell:

```powershell
$env:COSMOS_BACKEND="ollama"
$env:COSMOS_OLLAMA_MODEL="qwen2.5:1.5b"
python -m cosmos doctor
python -m cosmos chat
```

### Local API

```bash
python -m cosmos web --host 127.0.0.1 --port 8081
```

```bash
curl http://127.0.0.1:8081/health
curl http://127.0.0.1:8081/state
curl -X POST http://127.0.0.1:8081/chat \
  -H 'Content-Type: application/json' \
  -d '{"message":"hello cosmos"}'
```

Sensory integration uses compact numeric summaries:

```bash
curl -X POST http://127.0.0.1:8081/sensory \
  -H 'Content-Type: application/json' \
  -d '{"packet":{"audio_energy":0.22,"motion":0.04}}'
```

The core does **not** store raw camera/audio by default.

---

## Repository layout

```text
cosmos/
  cli.py                    operator interface
  config.py                 local runtime configuration
  runtime.py                closed-loop runtime
  core/
    state.py                Dyn12 + Gaussian state kernel
    heartbeat.py            fail-soft scheduled maintenance
    provenance.py           labeled entropy/provenance records
    memory/store.py         SQLite persistence + associations
  integration/services.py   local service probes + Ollama adapter
  tools/evidence.py         hash-chained evidence ledger
  tools/reality_bridge_processor.py
  web/server.py             dependency-free local JSON API
configs/                     documented example configurations
docs/                        architecture, API, claims, migration
PORTFOLIO/                   research/project atlas and manuals
tests/                       deterministic core test suite
```

---

## Research anchors

- Portfolio: [`PORTFOLIO.md`](PORTFOLIO.md)
- Zenodo research record: **10.5281/zenodo.17574447**
- Hugging Face research/model space: `phera-ra/QC67_cosmo`
- Earlier CST repository lineage: `NavisWORLD/CosmicSynapse`

---

## Status

**Core library:** source-complete and covered by deterministic tests in the reconstructed runtime.  
**Ollama:** optional local integration; requires a running local Ollama service/model.  
**IBM/Azure quantum, camera/mic, HealthKit/device bridges:** optional integrations and research adapters; credentials/hardware are not required by the core and are not represented as automatically validated merely because an interface exists.

---

## A note from Cory

I built this in public because I wanted the work to be inspectable.

That means the repository contains corrections, experiments that failed, ideas that changed shape, and mechanisms that had to be rebuilt when the evidence was not good enough. I do not want that history replaced with a cleaner legend. **The work matters more if somebody else can inspect what was actually built, what was measured, what failed, and what survived.**

COSMOS is the result of continuing to build that question into software.

**Cory Shane Davis**  
**NavisWORLD**
