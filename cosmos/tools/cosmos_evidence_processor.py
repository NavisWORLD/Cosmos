"""Compatibility entry point for COSMOS evidence processing."""

from .evidence import EvidenceEvent, EvidenceLedger, VALID_STATUSES, canonical_json, lock_snapshot

__all__ = ["EvidenceEvent", "EvidenceLedger", "VALID_STATUSES", "canonical_json", "lock_snapshot"]
