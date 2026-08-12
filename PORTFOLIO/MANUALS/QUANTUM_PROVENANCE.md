# Quantum Provenance Manual

## Two different questions
1. Can a model/control seed be audibly tied to measured quantum data? **Provenance.**
2. Does that source improve an ML objective over matched classical randomness? **Advantage.**

The first can be true while the second is null.

## Model-birth requirements
Identify exact source record; label provider/backend/hardware/simulator; deterministic mapping after source is fixed; same seed reproduces weights; altered seed changes initialization; manifest/hash attaches provenance to exact artifact.

## Public boundary
Published evidence supports auditable quantum-derived provenance for specific artifacts and validates parts of the mapping pipeline. Published matched tests do **not** support the stronger claim that quantum randomness improved model accuracy.

## Verification checklist
Manifest counts; shot conservation; backend labels; simulator separation; hashes; mapping statistics; exact model/seed linkage; matched classical control; null preservation.

## Links
- https://huggingface.co/phera-ra/QC67_cosmo/blob/main/benchmarks/verify_quantum_engine.py
- https://huggingface.co/phera-ra/QC67_cosmo/blob/main/data/quantum_measurements_manifest.json
- https://huggingface.co/phera-ra/QC67_cosmo/blob/main/FINDINGS.md
