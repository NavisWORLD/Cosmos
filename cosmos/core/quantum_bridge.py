from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Iterable

from .provenance import QuantumRecord, derive_seed, verify_record


@dataclass(slots=True)
class QuantumBridge:
    """Labeled entropy/provenance buffer. It never treats simulator data as hardware implicitly."""

    max_records: int = 128
    _records: deque[QuantumRecord] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._records = deque(maxlen=self.max_records)

    def ingest(self, record: QuantumRecord) -> dict[str, bool | int]:
        report = verify_record(record)
        if not all(report[key] for key in ("binary", "same_width", "labeled")):
            raise ValueError(f"invalid provenance record: {report}")
        self._records.append(record)
        return report

    def latest(self) -> QuantumRecord | None:
        return self._records[-1] if self._records else None

    def seed(self, bio_aggregates: Iterable[float] = ()) -> str:
        record = self.latest()
        if record is None:
            raise RuntimeError("no provenance record available")
        return derive_seed(record, bio_aggregates)

    def status(self) -> dict[str, object]:
        latest = self.latest()
        return {
            "records": len(self._records),
            "provider": latest.provider if latest else None,
            "backend": latest.backend if latest else None,
            "source_kind": latest.source_kind if latest else None,
        }
