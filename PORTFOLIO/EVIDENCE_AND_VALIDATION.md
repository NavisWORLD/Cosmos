# Evidence & Validation Policy

This file is the epistemic contract of the portfolio.

## Evidence labels
- **IMPLEMENTED** — code/artifact exists; does not alone prove improvement.
- **OBSERVED** — runtime evidence shows execution in the documented environment.
- **MEASURED** — a defined metric was produced under a described/reproducible benchmark.
- **NULL** — the test did not meet its success criterion; nulls remain first-class evidence.
- **HYPOTHESIS** — a falsifiable proposition still requiring evidence.
- **METAPHOR / MODEL** — conceptual design language, not literal physics/biology unless independently demonstrated.

## Current bounded claims

### Dynamic state / dyn12
Published controlled small-model tests report dyn12 as the strongest mechanism rung in the cited frozen-corpus state ladder. The useful public wording is narrow: a compact evolving state modulating attention improved that tested character-level architecture relative to its no-state baseline and did so with low parameter overhead.

Do not convert this into “12D is always better,” “54D is always better,” or “CST universally beats transformers.”

### Parameter efficiency
Published larger-scale comparisons report an increasing parameter-efficiency ratio for dyn12 relative to static54 at several tested sizes. Static54 may still have lower absolute loss in some comparisons. Efficiency and absolute performance are separate metrics.

### Quantum provenance
The project has evidence for auditable quantum-derived provenance in specific model-birth / entropy pipelines. This is different from performance advantage.

### Quantum accuracy advantage
Matched tests reported **NULL** for the claim that quantum randomness made the tested models more accurate.

### Paired sensory/internal-state conditioning
The aligned-state arm beat some destroyed-pairing conditioned controls but did not beat plain attention in the cited benchmark. The preregistered result is therefore **NULL** for predictive improvement over the plain baseline.

### Consciousness
Not established. Persistent memory, self-monitoring, autonomous tasks, model self-description, sensory input, or lower loss are not measurements of machine consciousness.

## Mechanism preflight
Before accepting a state-kernel benchmark:
- Ω must vary where expected.
- State must vary.
- State-affinity kernel must not collapse to identity or all-ones.
- Gate gradients must flow.
- Learned couplings should be checked for movement.
- Dataset/corpus snapshot and hash must be fixed.
- Telemetry schema must be versioned.

## Research record requirements
Preserve exact lineage, code hash, dataset hash, seeds, hyperparameters, liveness diagnostics, per-seed results, success criterion, null/failure status, hardware/simulator provenance, and limitations.

See [Technical Index](TECHNICAL_INDEX.md).
