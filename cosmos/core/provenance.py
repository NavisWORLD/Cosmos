from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from typing import Iterable


@dataclass(frozen=True, slots=True)
class QuantumRecord:
    provider: str
    backend: str
    bitstrings: tuple[str, ...]
    source_kind: str  # hardware, simulator, archive, unknown
    job_id: str = ""

    def canonical_bytes(self) -> bytes:
        joined = "|".join((self.provider, self.backend, self.source_kind, self.job_id, *self.bitstrings))
        return joined.encode("utf-8")


def verify_record(record: QuantumRecord) -> dict[str, bool | int]:
    binary = all(bits and set(bits) <= {"0", "1"} for bits in record.bitstrings)
    same_width = len({len(bits) for bits in record.bitstrings}) <= 1 if record.bitstrings else False
    labeled = bool(record.provider and record.backend and record.source_kind)
    return {"binary": binary, "same_width": same_width, "labeled": labeled, "count": len(record.bitstrings)}


def derive_seed(record: QuantumRecord, bio_aggregates: Iterable[float] = ()) -> str:
    """Derive a reproducible seed from labeled measurement data and optional aggregates.

    This establishes provenance only; it does not imply an ML performance advantage.
    """
    h = sha256(record.canonical_bytes())
    for value in bio_aggregates:
        h.update(f"|{float(value):.12g}".encode("ascii"))
    return h.hexdigest()
