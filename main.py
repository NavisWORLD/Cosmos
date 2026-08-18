"""Compatibility launcher: prefer `python -m cosmos` or the `cosmos` console command."""
from cosmos.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
