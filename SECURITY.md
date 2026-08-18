# Security & Evidence Integrity Policy

## Secrets and private data

Do not commit secrets, API keys, wallet secrets, provider credentials, private conversations, raw health records, raw camera/microphone captures, private legal correspondence, or unredacted personal information.

The default web server binds to `127.0.0.1`. If COSMOS is exposed outside the local machine, place it behind authentication/TLS and review the threat model first.

## Provenance and evidence integrity

COSMOS provenance, ownership, and dispute records must be treated as integrity-sensitive material.

Do not silently alter, delete, rewrite, backdate, fabricate, or replace evidence records, hashes, provenance statements, authorship records, timestamps, benchmark results, null results, or archival references.

When a correction is necessary:

1. preserve the original artifact when lawful and appropriate;
2. create a new corrected record rather than pretending the earlier record never existed;
3. record what changed and why;
4. preserve hashes/checksums when available;
5. distinguish a platform timestamp from a user-authored date;
6. do not claim that a timestamp proves more than it actually proves.

Evidence relevant to a real-world dispute should be preserved outside the working repository as well, ideally in read-only or immutable storage with redundant copies and documented hashes. Do not publish private evidence merely to prove that it exists.

## Repository ownership controls

- Repository-wide ownership is declared through `.github/CODEOWNERS`.
- Current permission boundaries are defined in `LICENSE`, `CORY_DAVIS_IP_AND_ACCESS_NOTICE.md`, and `COMMERCIAL_RIGHTS.md`.
- Provenance/dispute records are documented in `ORIGIN_AND_PROVENANCE.md` and `DISPUTED_PROVENANCE_AND_EVIDENCE_NOTICE.md`.
- Changes that weaken ownership, licensing, provenance, or evidence-integrity controls require explicit owner approval.

## Reporting

Please report security issues privately to the repository owner rather than publishing exploitable credentials, private data, or sensitive evidence in an issue.
