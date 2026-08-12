# PHOS & Dynamic-State Transformer Manual

PHOS names the flagship small-transformer lineage built around the corrected dyn12 mechanism on the intended φ-governed scaffold. It must be distinguished from other artifacts called COSMOS.

## Architecture
The documented line combines causal transformer modeling, RMS-style normalization, rotary positional encoding, φ-scaled feed-forward/init choices, recurrent 12-scalar state, calibrated state-similarity kernels, learned mixing with ordinary attention, and warm-start growth.

## Mechanism
Ordinary attention is augmented by a question: *were these token positions in similar evolving states?* State similarity becomes matrix `H`; a learned gate controls its contribution.

The mechanism is only meaningful if state varies, distances are correctly scaled, `H` is not identity/all-ones, gradients flow, and state projections/couplings receive optimizer pressure.

## Controlled ladder
Published comparisons included none, dyn12, dyn42, dyn54, static54, and coupled variants under frozen-data repeated-seed conditions. The cited result favored compact dyn12 among mechanism rungs; “more dimensions” was not monotonically better.

## Reproduction protocol
1. Freeze corpus/hash.
2. Fix seeds.
3. Train plain baseline.
4. Add dyn12.
5. Run mechanism preflight.
6. Record per-seed loss, gate/kernel diagnostics, parameter count, code hash.
7. Repeat controls.
8. Report absolute loss separately from parameter efficiency.
9. Preserve negative rungs.

## Links
- https://huggingface.co/phera-ra/QC67_cosmo/blob/main/architecture/cosmos_state_ladder.py
- https://huggingface.co/phera-ra/QC67_cosmo/blob/main/benchmarks/causality_probe.py
- https://huggingface.co/phera-ra/QC67_cosmo/blob/main/architecture/phos_grow.py
- https://huggingface.co/phera-ra/QC67_cosmo/blob/main/FINDINGS.md
