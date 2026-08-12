# COSMOS CLI / Autonomous Engineering Manual

## Objective
Expose a complex local AI system through a small operator surface without destructively rewriting the core.

## Command families
`status` service/model/memory/Git health; `map` topology; `serve` ownership-safe lifecycle; `agent` bounded engineering task; `weights` metadata/hashes; `datasets` snapshots/schemas/hashes; `bench` reproducible tests; `evidence` normalize results.

## Non-destructive pattern
`CLI → probe existing services / read-only interfaces / explicit subprocesses / dedicated sandbox outputs / recorded promotion`

## Autonomous coding cycle
Task → inspect → proposal → branch/sandbox → tests → diff/evidence → approval policy → commit/apply → rollback point.

**Creative with proposals, paranoid with destruction.**

## Model adapters
New local models should plug into a provider boundary rather than being hard-coded into memory/state/evidence layers.

## Port discipline
Probe endpoint, identify process, verify expected response signature, start only if absent, stop only owned/approved processes.

## Tech
- [Tools](../../cosmos/tools/)
- [Evidence processor](../../cosmos/tools/cosmos_evidence_processor.py)
- [COSMOS package](../../cosmos/)
