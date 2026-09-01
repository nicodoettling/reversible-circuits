#!/usr/bin/env python3
"""Deterministic falsifier for a naive generic double/double bulk integral.

This evaluates only the *naive, unrenormalized* continuum coefficient derived
from M94's raw Borel convolution.  A bounded probe reveals a nonintegrable
collision-face singularity.  Thus its output is retained only as a falsifier;
it is not a candidate coefficient for ``k^2 Delta(E_k)``.

Convention: (pq)(x)=p(q(x)); tuple factors multiply left-to-right.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
import sys
from pathlib import Path

import numpy as np
from scipy.stats import qmc


RHO = 1.0 / 6.0
EXCESS = 1.0 - 4.0 * RHO
EPSILON = 2.0 ** -45


def double_map(prefix: str, kind: str) -> dict[str, str]:
    labels = [f"{prefix}{i}" for i in range(4)]
    if kind == "S":
        pairs = ((0, 1), (2, 3))
    elif kind == "N":
        pairs = ((0, 3), (1, 2))
    else:
        raise ValueError(kind)
    out = {label: label for label in labels}
    for i, j in pairs:
        out[labels[i]], out[labels[j]] = labels[j], labels[i]
    return out


def source_a() -> tuple[dict[str, float], dict[str, str]]:
    positions = {"a0": 0.0, "a1": 1.0 / 3.0, "a2": 2.0 / 3.0}
    perm = {"a0": "a1", "a1": "a2", "a2": "a0"}
    return positions, perm


def source_b() -> tuple[dict[str, float], dict[str, str]]:
    positions = {
        "b0": 0.0,
        "be": EPSILON,
        "b1": 1.0 / 3.0,
        "b2": 2.0 / 3.0,
    }
    perm = {"b0": "be", "be": "b0", "b1": "b2", "b2": "b1"}
    return positions, perm


def combine_positions(*parts: dict[str, float]) -> dict[str, float]:
    out: dict[str, float] = {}
    for part in parts:
        overlap = set(out) & set(part)
        if overlap:
            raise AssertionError(overlap)
        out.update(part)
    return out


def compose(
    first: dict[str, str], second: dict[str, str], labels: list[str]
) -> dict[str, str]:
    """Return first after second, extending both by fixed points."""
    return {
        label: first.get(second.get(label, label), second.get(label, label))
        for label in labels
    }


def residual_lengths(positions: dict[str, float], perm: dict[str, str]) -> list[float]:
    """Cycle lengths of perm^{-1}h as sums of circular support gaps."""
    labels = sorted(positions, key=positions.__getitem__)
    count = len(labels)
    if len({positions[label] for label in labels}) != count:
        raise AssertionError("support collision")
    inverse = {image: preimage for preimage, image in perm.items()}
    if set(inverse) != set(labels) or set(perm) != set(labels):
        raise AssertionError("permutation support mismatch")
    index = {label: i for i, label in enumerate(labels)}
    gaps = [
        (positions[labels[(i + 1) % count]] - positions[labels[i]]) % 1.0
        for i in range(count)
    ]
    transition = [
        index[inverse[labels[(i + 1) % count]]]
        for i in range(count)
    ]
    seen: set[int] = set()
    lengths: list[float] = []
    for start in range(count):
        if start in seen:
            continue
        current = start
        total = 0.0
        while current not in seen:
            seen.add(current)
            total += gaps[current]
            current = transition[current]
        lengths.append(total)
    return sorted(lengths)


def power(lengths: list[float]) -> float:
    if any(length <= 0.0 for length in lengths):
        return math.inf
    return math.prod(length ** -1.5 for length in lengths)


def state_positions(prefix: str, values: np.ndarray) -> dict[str, float]:
    return {f"{prefix}{i}": float(value) for i, value in enumerate(values)}


A_POS, A_PERM = source_a()
B_POS, B_PERM = source_b()
A_DEN = power([1.0 / 3.0] * 3)
B_DEN = power([1.0 / 3.0, 2.0 / 3.0])


def source_contrast(s_values: np.ndarray, s_kind: str) -> tuple[float, float]:
    s_pos = state_positions("s", s_values)
    s_perm = double_map("s", s_kind)

    a_pos = combine_positions(A_POS, s_pos)
    a_labels = list(a_pos)
    a_product = compose(A_PERM, s_perm, a_labels)
    a_lengths = residual_lengths(a_pos, a_product)
    a_value = power(a_lengths) / A_DEN if len(a_lengths) == 5 else 0.0

    b_pos = combine_positions(B_POS, s_pos)
    b_labels = list(b_pos)
    b_product = compose(B_PERM, s_perm, b_labels)
    b_lengths = residual_lengths(b_pos, b_product)
    if len(b_lengths) == 5 and b_lengths[0] < 1000.0 * EPSILON:
        b_value = power(b_lengths[1:]) / B_DEN
    else:
        b_value = 0.0

    s_lengths = residual_lengths(s_pos, s_perm)
    if len(s_lengths) != 3:
        raise AssertionError((s_kind, s_lengths))
    return b_value - a_value, power(s_lengths)


def joint_weight(
    s_values: np.ndarray, s_kind: str, t_values: np.ndarray, t_kind: str
) -> float:
    s_pos = state_positions("s", s_values)
    t_pos = state_positions("t", t_values)
    positions = combine_positions(s_pos, t_pos)
    labels = list(positions)
    product = compose(double_map("s", s_kind), double_map("t", t_kind), labels)
    lengths = residual_lengths(positions, product)
    return power(lengths) if len(lengths) == 5 else 0.0


def sample_value(row: np.ndarray) -> tuple[float, dict[str, float]]:
    s_values = np.sort(row[:4])
    cuts = np.sort(row[4:7])
    excess_gaps = np.array(
        [cuts[0], cuts[1] - cuts[0], cuts[2] - cuts[1], 1.0 - cuts[2]]
    )
    gaps = RHO + EXCESS * excess_gaps
    t0 = row[7] * gaps[3]
    t_values = np.array(
        [t0, t0 + gaps[0], t0 + gaps[0] + gaps[1], t0 + gaps[0] + gaps[1] + gaps[2]]
    )
    type_values: dict[str, float] = {}
    total = 0.0
    for s_kind in ("S", "N"):
        contrast, denominator = source_contrast(s_values, s_kind)
        for t_kind in ("S", "N"):
            value = contrast * joint_weight(s_values, s_kind, t_values, t_kind) / denominator
            type_values[f"{s_kind}{t_kind}"] = value
            total += value
    # Ordered s positions have volume 1/24.  The central t domain has gap
    # simplex volume EXCESS^3/6 and t0 interval length gaps[3].
    volume_weight = EXCESS ** 3 * gaps[3] / 144.0
    return volume_weight * total, {
        key: volume_weight * value for key, value in type_values.items()
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--power", type=int, default=17)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    engine = qmc.Sobol(d=8, scramble=True, seed=102)
    points = engine.random_base2(args.power)
    values = []
    channels = {key: [] for key in ("SS", "SN", "NS", "NN")}
    invalid = 0
    for row in points:
        try:
            value, pieces = sample_value(row)
        except (AssertionError, OverflowError, ZeroDivisionError):
            invalid += 1
            continue
        if not math.isfinite(value):
            invalid += 1
            continue
        values.append(value)
        for key in channels:
            channels[key].append(pieces[key])
    array = np.asarray(values)
    block_count = 32
    blocks = np.array_split(array, block_count)
    block_means = np.asarray([np.mean(block) for block in blocks])
    j_estimate = float(np.mean(array))
    coefficient = j_estimate / (9.0 * math.pi ** 2)
    payload = {
        "status": "deterministic_qmc_falsifier_naive_integral_nonintegrable",
        "claim_tested": "naive unrenormalized generic double/double bulk integral",
        "convention": "(pq)(x)=p(q(x)); tuple factors multiply left-to-right",
        "derivation_normalization": "formally k^2 Delta -> J/(9 pi^2), but J is nonintegrable and this transfer is refuted",
        "sobol_power": args.power,
        "points_requested": len(points),
        "points_used": len(values),
        "invalid_points": invalid,
        "scramble_seed": 102,
        "epsilon_for_adjacent_B_edge": EPSILON,
        "J_estimate": j_estimate,
        "candidate_k_squared_delta_limit": coefficient,
        "block_mean_standard_deviation": float(np.std(block_means, ddof=1)),
        "channel_J_estimates": {
            key: float(np.mean(np.asarray(channel))) for key, channel in channels.items()
        },
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": __import__("scipy").__version__,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
