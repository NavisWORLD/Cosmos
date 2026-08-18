# Security, Privacy & Publication Policy

## Never commit
- API keys, tokens, passwords, private keys, wallet secrets, or `.env` values
- raw private conversations unless deliberately reviewed for public release
- raw camera/microphone recordings merely to prove sensing exists
- private health/biosignal records without an explicit publication decision
- third-party private identifiers
- weights/assets that cannot legally be redistributed

## Prefer publishing
Code, schemas, hashes/manifests, aggregate benchmark statistics, redacted logs, synthetic fixtures, reproduction instructions, simulator/hardware labels, and commit/dataset fingerprints.

## Sensory boundary
`raw local signal → local feature extraction → compact numeric summary → downstream state/control`

Raw media should not be retained by default simply because the runtime can sense it.

## Conversation archive boundary
A ChatGPT conversation may be linked only through its deliberate public share URL. The portfolio does not fabricate share links or silently publish private transcript text.

## Autonomous code boundary
Use `proposal → sandbox → tests → review/approval → apply → rollback path`.
