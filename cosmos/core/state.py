from __future__ import annotations

from dataclasses import dataclass, field
from math import exp, sqrt
from statistics import median
from typing import Iterable, Sequence


DEFAULT_DIMS = 12


def _as_vector(values: float | Sequence[float], dims: int) -> list[float]:
    if isinstance(values, (int, float)):
        return [float(values)] * dims
    vec = [float(v) for v in values]
    if len(vec) != dims:
        raise ValueError(f"expected {dims} values, got {len(vec)}")
    return vec


@dataclass(slots=True)
class Dyn12State:
    """Compact recurrent control state used as a testable CST state primitive.

    This is an engineering representation, not a claim about physical dimensions.
    """

    leak: float = 0.85
    gain: float = 0.15
    values: list[float] = field(default_factory=lambda: [0.0] * DEFAULT_DIMS)

    def __post_init__(self) -> None:
        if len(self.values) != DEFAULT_DIMS:
            raise ValueError("Dyn12State requires exactly 12 scalars")
        if not 0.0 <= self.leak <= 1.0:
            raise ValueError("leak must be in [0, 1]")

    def update(self, omega: float | Sequence[float]) -> tuple[float, ...]:
        drive = _as_vector(omega, DEFAULT_DIMS)
        self.values = [
            self.leak * old + self.gain * incoming
            for old, incoming in zip(self.values, drive, strict=True)
        ]
        return self.snapshot()

    def snapshot(self) -> tuple[float, ...]:
        return tuple(self.values)



def euclidean(a: Sequence[float], b: Sequence[float]) -> float:
    if len(a) != len(b):
        raise ValueError("state vectors must have equal length")
    return sqrt(sum((x - y) ** 2 for x, y in zip(a, b, strict=True)))


@dataclass(slots=True)
class GaussianStateKernel:
    bandwidth: float | None = None
    minimum_bandwidth: float = 1e-6

    def calibrate(self, states: Sequence[Sequence[float]]) -> float:
        distances: list[float] = []
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                d = euclidean(states[i], states[j])
                if d > 0:
                    distances.append(d)
        candidate = median(distances) if distances else 1.0
        self.bandwidth = max(float(candidate), self.minimum_bandwidth)
        return self.bandwidth

    def matrix(self, states: Sequence[Sequence[float]]) -> list[list[float]]:
        if not states:
            return []
        sigma = self.bandwidth or self.calibrate(states)
        denom = 2.0 * sigma * sigma
        return [
            [exp(-(euclidean(a, b) ** 2) / denom) for b in states]
            for a in states
        ]


def mix_attention(
    standard: Sequence[Sequence[float]],
    state_kernel: Sequence[Sequence[float]],
    gate: float,
) -> list[list[float]]:
    if not 0.0 <= gate <= 1.0:
        raise ValueError("gate must be in [0, 1]")
    if len(standard) != len(state_kernel):
        raise ValueError("attention matrices must have equal size")
    out: list[list[float]] = []
    for base_row, state_row in zip(standard, state_kernel, strict=True):
        if len(base_row) != len(state_row):
            raise ValueError("attention matrices must have equal shape")
        out.append([
            (1.0 - gate) * base + gate * state
            for base, state in zip(base_row, state_row, strict=True)
        ])
    return out


def preflight(states: Sequence[Sequence[float]], kernel: Sequence[Sequence[float]]) -> dict[str, float | bool]:
    """Mechanism-liveness checks that should precede benchmark claims."""
    if len(states) < 2 or len(kernel) < 2:
        return {"state_varies": False, "kernel_not_identity": False, "kernel_not_all_ones": False}
    flat_states = [value for state in states for value in state]
    state_varies = max(flat_states) - min(flat_states) > 1e-12
    off_diag = [kernel[i][j] for i in range(len(kernel)) for j in range(len(kernel[i])) if i != j]
    kernel_not_identity = any(abs(v) > 1e-9 for v in off_diag)
    all_values = [v for row in kernel for v in row]
    kernel_not_all_ones = any(abs(v - 1.0) > 1e-9 for v in all_values)
    return {
        "state_varies": state_varies,
        "kernel_not_identity": kernel_not_identity,
        "kernel_not_all_ones": kernel_not_all_ones,
    }
