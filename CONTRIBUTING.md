# Contributing to COSMOS

COSMOS welcomes engineering, reproducibility, documentation, benchmark, and safety improvements.

## Ground rules

1. Keep claims no broader than evidence.
2. Preserve null/negative results.
3. Never commit credentials, private conversations, raw health data, or raw camera/mic captures.
4. Keep local-first behavior as the default; external services must be explicit.
5. Autonomous code changes use `proposal → branch/sandbox → tests → review → merge`.

## Development

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e '.[dev]'
pytest
python -m compileall -q cosmos
```

Use focused PRs with tests. If a result is empirical, include the dataset/config/seed/code identifiers required to reproduce it.
