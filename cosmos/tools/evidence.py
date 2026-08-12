from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
from typing import Any, Iterable


VALID_STATUSES = {"IMPLEMENTED", "OBSERVED", "MEASURED", "NULL", "HYPOTHESIS", "METAPHOR_MODEL"}


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


@dataclass(frozen=True, slots=True)
class EvidenceEvent:
    timestamp: str
    event_type: str
    status: str
    payload: dict[str, Any]
    previous_hash: str
    hash: str


class EvidenceLedger:
    """Append-only JSONL ledger with SHA-256 hash chaining."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, event_type: str, status: str, payload: dict[str, Any]) -> EvidenceEvent:
        status = status.upper()
        if status not in VALID_STATUSES:
            raise ValueError(f"unknown evidence status: {status}")
        previous_hash = self._last_hash()
        timestamp = datetime.now(timezone.utc).isoformat()
        body = {
            "timestamp": timestamp,
            "event_type": event_type,
            "status": status,
            "payload": payload,
            "previous_hash": previous_hash,
        }
        digest = sha256(canonical_json(body).encode("utf-8")).hexdigest()
        event = EvidenceEvent(hash=digest, **body)
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(canonical_json(asdict(event)) + "\n")
        return event

    def verify(self) -> tuple[bool, int, str | None]:
        previous = "0" * 64
        count = 0
        if not self.path.exists():
            return True, 0, None
        with self.path.open("r", encoding="utf-8") as handle:
            for number, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                try:
                    raw = json.loads(line)
                except json.JSONDecodeError:
                    return False, count, f"invalid JSON at line {number}"
                expected_prev = raw.pop("hash", None)
                body = raw
                if body.get("previous_hash") != previous:
                    return False, count, f"broken previous_hash at line {number}"
                calculated = sha256(canonical_json(body).encode("utf-8")).hexdigest()
                if calculated != expected_prev:
                    return False, count, f"hash mismatch at line {number}"
                previous = calculated
                count += 1
        return True, count, None

    def _last_hash(self) -> str:
        if not self.path.exists():
            return "0" * 64
        last = ""
        with self.path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    last = line
        if not last:
            return "0" * 64
        try:
            return str(json.loads(last)["hash"])
        except (json.JSONDecodeError, KeyError):
            raise ValueError("cannot append to an invalid evidence ledger")


def lock_snapshot(payload: dict[str, Any]) -> dict[str, Any]:
    """Create an immutable-style receipt for a forecast/config/data snapshot."""
    body = {"locked_at": datetime.now(timezone.utc).isoformat(), "payload": payload}
    body["sha256"] = sha256(canonical_json(body).encode("utf-8")).hexdigest()
    return body
