from __future__ import annotations


def calibrated_language(confidence: float) -> str:
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must be in [0, 1]")
    if confidence >= 0.9:
        return "high confidence"
    if confidence >= 0.65:
        return "moderate confidence"
    if confidence >= 0.4:
        return "low confidence"
    return "speculative"
