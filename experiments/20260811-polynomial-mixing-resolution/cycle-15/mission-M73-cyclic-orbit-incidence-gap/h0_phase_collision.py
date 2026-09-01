#!/usr/bin/env python3
"""Cyclic-phase autocorrelation expansion of the H0 trace-two quantity.

This is a floating diagnostic built from exact integer completion counts.  It
checks the identity

  Tr((K_H0-Pi)^2) = n^{-1} sum_d E[(R(G,S)-1)(R(G,theta^d S)-1)],

where G,S are independent one-coordinate product increments and R is the raw
two-coordinate likelihood ratio.  The identity itself is algebraic; the
reported decimal separation contributions are diagnostics only.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
import sys
from pathlib import Path

import numpy as np


def load_kernel_module():
    path = Path(__file__).with_name("h0_coordinate_correlation.py")
    spec = importlib.util.spec_from_file_location("m73_h0_kernel", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


H0 = load_kernel_module()


def analyze(n: int) -> dict:
    if n < 5 or n % 2 == 0:
        raise ValueError("expected odd n>=5")
    l = (n - 1) // 2
    h = tuple((x + 1) % n for x in range(n))
    h_inverse = H0.inverse(h)
    pair_counts = H0.pair_product_multiplicities(n)
    completions = {
        g: H0.minimal_factorization_count(H0.compose(H0.inverse(g), h), n - 3)
        for g in pair_counts
    }
    support = sorted(g for g, count in completions.items() if count)
    location = {g: index for index, g in enumerate(support)}
    total = n ** (n - 2)
    stationary = np.array([
        pair_counts[g] * completions[g] / total for g in support
    ], dtype=float)
    if abs(float(stationary.sum()) - 1) > 1e-12:
        raise AssertionError("marginal did not normalize")

    likelihood = np.zeros((len(support), len(support)), dtype=float)
    for i, g in enumerate(support):
        for j, s in enumerate(support):
            completion = H0.minimal_factorization_count(
                H0.compose(H0.inverse(H0.compose(g, s)), h), n - 5
            )
            if completion:
                likelihood[i, j] = total * completion / (
                    completions[g] * completions[s]
                )

    theta_index = np.array([
        location[H0.theta(s, h, h_inverse)] for s in support
    ], dtype=int)
    support_sets = [
        frozenset(x for x in range(n) if g[x] != x)
        for g in support
    ]
    current = np.arange(len(support), dtype=int)
    separation_covariances = []
    separation_overlap_contributions = []
    weighted_rows = stationary[:, None] * stationary[None, :]
    centered = likelihood - 1.0
    for separation in range(n):
        summand = weighted_rows * centered * centered[:, current]
        covariance = float(np.sum(summand))
        separation_covariances.append(covariance)
        overlap_contributions: dict[str, float] = {}
        # Classify by |supp(S) intersect supp(theta^d S)|.  This is the
        # phase-overlap statistic suggested by M67.  The sum is exact up to
        # final floating accumulation; no lumpability is assumed.
        for second, shifted_second in enumerate(current):
            overlap = len(support_sets[second] & support_sets[shifted_second])
            key = str(overlap)
            overlap_contributions[key] = (
                overlap_contributions.get(key, 0.0)
                + float(np.sum(summand[:, second]))
            )
        separation_overlap_contributions.append(overlap_contributions)
        current = theta_index[current]
    quotient_trace_two = float(sum(separation_covariances) / n)
    rotation_averaged_overlap_contributions: dict[str, float] = {}
    for record in separation_overlap_contributions:
        for overlap, value in record.items():
            rotation_averaged_overlap_contributions[overlap] = (
                rotation_averaged_overlap_contributions.get(overlap, 0.0)
                + value / n
            )
    if abs(float(np.sum(stationary[:, None] * stationary[None, :] * likelihood)) - 1) > 1e-10:
        raise AssertionError("raw likelihood did not normalize")
    return {
        "n": n,
        "l": l,
        "support_size": len(support),
        "raw_joint_chi_square_numeric": separation_covariances[0],
        "rotation_separation_centered_covariance_numeric": separation_covariances,
        "rotation_separation_support_overlap_contribution_numeric": (
            separation_overlap_contributions
        ),
        "rotation_averaged_support_overlap_contribution_numeric": (
            rotation_averaged_overlap_contributions
        ),
        "rotation_average_equals_H0_centered_trace_two_numeric": quotient_trace_two,
        "l_squared_times_H0_centered_trace_two_numeric": l * l * quotient_trace_two,
        "sum_absolute_rotation_covariances_divided_by_n_numeric": (
            sum(abs(value) for value in separation_covariances) / n
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "status": "complete",
        "claim_checked": "cyclic phase expansion of the H0 centered trace two",
        "scope_warning": "separation values are floating diagnostics, not asymptotic bounds",
        "convention": "(p q)(x)=p(q(x)); tuple products left-to-right",
        "records": [analyze(n) for n in sorted(set(args.n))],
        "python": platform.python_version(),
        "numpy": np.__version__,
        "seed": None,
        "deterministic": True,
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": " ".join(sys.argv),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["records"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
