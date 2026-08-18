# Reality Bridge Prediction & Evidence Manual

## Prime directive
**Replace claims with instrumentation.**

## Forecast lifecycle
`data snapshot → validation → config+seed → prediction → LOCK → hash/receipt → future outcome → resolution → score vs baseline → evidence event`

A forecast editable after the outcome is not evidence.

## Determinism
Record an experiment/universe seed. Same data/version/config/seed should reproduce the same stochastic forecast.

## Baselines
Market: persistence, zero-change, moving average, momentum, linear trend. Lottery: exact-schema uniform random plus simple declared heuristics. Report proper metrics and repeated/walk-forward results.

## Walk-forward
For outcome `n`, use only observations `< n`; predict, score, advance.

## Lottery as an adversarial test
Enforce exact schema; reject malformed history visibly; lock before draw; compare seeded random baseline; report misses as visibly as hits; never auto-buy; never promise guaranteed winners. A single partial hit is not stable predictive skill.

## Evidence ledger
Record forecast open/lock, win/miss/partial/null, model/data changes, and anomalies. A hash chain makes mutation detectable; it does not make a forecast accurate.

## Live market data
Record provider, symbol, timestamp, latency/staleness, interval, missing-data behavior. Never silently label stale data live.

## Boundary
The engine measures prediction. Skill must be demonstrated prospectively or with correct walk-forward tests against baselines.

## Tech
- [Reality Bridge processor](../../cosmos/tools/reality_bridge_processor.py)
- [Evidence processor](../../cosmos/tools/cosmos_evidence_processor.py)
