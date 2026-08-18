# Contributing to COSMOS

COSMOS accepts engineering, reproducibility, documentation, benchmark, and safety improvements **by prior approval**.

Because the current repository revision is permission-only and the project is maintaining a clear ownership/provenance boundary, opening an issue or pull request does not grant anyone a license to the existing COSMOS codebase and does not automatically transfer ownership of a contributor’s material to Cory Shane Davis / NavisWORLD.

## Before contributing

Contact the repository owner and obtain approval for the proposed contribution scope before submitting substantial code, documentation, datasets, media, or other material.

A contribution may require a separate contributor agreement, assignment, or license identifying what rights the contributor grants and what rights the contributor retains. Do not assume a pull request alone settles those questions.

## Contributor representations

By submitting material, you must have the right to submit it. Do not contribute third-party code, confidential material, copied documentation, datasets, model outputs, credentials, personal data, or other content unless you have the necessary rights and the repository owner has approved the inclusion.

## Engineering ground rules

1. Keep claims no broader than evidence.
2. Preserve null/negative results.
3. Never commit credentials, private conversations, raw health data, or raw camera/mic captures.
4. Keep local-first behavior as the default; external services must be explicit.
5. Autonomous code changes use `proposal → branch/sandbox → tests → review → merge`.
6. Identify third-party dependencies and their licenses clearly.
7. Do not remove or weaken ownership, provenance, evidence, safety, or licensing notices without explicit owner approval.

## Development

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e '.[dev]'
pytest
python -m compileall -q cosmos
```

Use focused PRs with tests. If a result is empirical, include the dataset/config/seed/code identifiers required to reproduce it.

See `LICENSE`, `CORY_DAVIS_IP_AND_ACCESS_NOTICE.md`, `COMMERCIAL_RIGHTS.md`, and `ORIGIN_AND_PROVENANCE.md` before contributing.
