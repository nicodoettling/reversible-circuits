#!/usr/bin/env python3
"""Deterministic falsification harness for the frozen M10 inequalities.

Finite survival is not a proof.  The tested universal statements are:
  * the endpoint-tilt density and maximal-correlation bounds at eps=1/16;
  * the two-projection principal-angle formula;
  * the affine recursion's integer/parity and stopping inequalities.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
from pathlib import Path

import numpy as np


EPSILON = 1.0 / 16.0
RHO_BOUND = 22.0 / 75.0
SEED = 20260811


def maximal_correlation(mu: np.ndarray) -> float:
    mx = mu.sum(axis=1)
    my = mu.sum(axis=0)
    keep_x = mx > 1e-15
    keep_y = my > 1e-15
    mu = mu[np.ix_(keep_x, keep_y)]
    mx = mu.sum(axis=1)
    my = mu.sum(axis=0)
    normalized = mu / np.sqrt(mx[:, None] * my[None, :])
    singular = np.linalg.svd(normalized, compute_uv=False)
    return float(singular[1]) if len(singular) > 1 else 0.0


def projection_gap(mu: np.ndarray) -> float:
    nx, ny = mu.shape
    weights = mu.reshape(-1)
    mx = mu.sum(axis=1)
    my = mu.sum(axis=0)
    ux = np.zeros((nx * ny, nx))
    uy = np.zeros((nx * ny, ny))
    for i in range(nx):
        for j in range(ny):
            state = i * ny + j
            ux[state, i] = math.sqrt(mu[i, j] / mx[i])
            uy[state, j] = math.sqrt(mu[i, j] / my[j])
    assert np.all(weights > 0)
    operator = 0.5 * (ux @ ux.T + uy @ uy.T)
    eigenvalues = np.linalg.eigvalsh(operator)[::-1]
    assert abs(eigenvalues[0] - 1.0) < 2e-10
    return float(1.0 - eigenvalues[1])


def random_probability(rng: np.random.Generator, size: int) -> np.ndarray:
    values = rng.exponential(size=size)
    # Include sparse endpoint tilts while retaining at least one support point.
    mask = rng.random(size) < 0.2
    values[mask] = 0.0
    if values.sum() == 0.0:
        values[rng.integers(size)] = 1.0
    return values / values.sum()


def audit_tilts(samples: int) -> dict:
    rng = np.random.default_rng(SEED)
    max_density_deviation = 0.0
    max_rho = 0.0
    max_angle_error = 0.0
    failures: list[dict] = []

    for sample in range(samples):
        nx = int(rng.integers(2, 6))
        ny = int(rng.integers(2, 6))
        alpha = random_probability(rng, nx)
        beta = random_probability(rng, ny)
        # Corners are the natural adversarial points for the pointwise bound.
        delta = EPSILON * rng.choice(np.array([-1.0, 1.0]), size=(nx, ny))
        unnormalized = alpha[:, None] * (1.0 + delta) * beta[None, :]
        mu = unnormalized / unnormalized.sum()
        mx = mu.sum(axis=1)
        my = mu.sum(axis=0)
        support = (mx[:, None] > 0) & (my[None, :] > 0)
        density = np.zeros_like(mu)
        density[support] = mu[support] / (
            (mx[:, None] * my[None, :])[support]
        )
        deviation = float(np.max(np.abs(density[support] - 1.0)))
        rho = maximal_correlation(mu)
        max_density_deviation = max(max_density_deviation, deviation)
        max_rho = max(max_rho, rho)
        if deviation > RHO_BOUND + 1e-12 or rho > RHO_BOUND + 1e-12:
            failures.append(
                {"sample": sample, "deviation": deviation, "rho": rho}
            )

        # Projection audit only on full-support marginal choices, so the
        # product support is one connected rectangle and constants are the
        # unique common range.
        if np.all(alpha > 0) and np.all(beta > 0):
            gap = projection_gap(mu)
            angle_error = abs(gap - (1.0 - rho) / 2.0)
            max_angle_error = max(max_angle_error, angle_error)
            if angle_error > 2e-10:
                failures.append(
                    {"sample": sample, "projection_angle_error": angle_error}
                )

    return {
        "samples": samples,
        "epsilon": EPSILON,
        "claimed_safe_bound": RHO_BOUND,
        "sharp_density_bound": 64.0 / 225.0,
        "max_density_deviation": max_density_deviation,
        "max_maximal_correlation": max_rho,
        "max_projection_formula_error": max_angle_error,
        "failures": failures,
    }


def audit_recursion(max_sstar: int, max_excess: int) -> dict:
    failures: list[dict] = []
    cases = 0
    max_levels_slack = 0
    for sstar in range(1, max_sstar + 1):
        b = sstar + 1
        for excess in range(2, max_excess + 1):
            n = b + excess
            s = sstar if (sstar - n) % 2 == 0 else sstar + 1
            t = (n - s) // 2
            length = t + s
            cases += 1
            local_ok = (
                (n - s) % 2 == 0
                and t >= 1
                and 2 <= length < n
                and length - b <= (n - b) / 2.0
            )
            sites = set(range(1, n))
            first = set(range(1, length))
            second = set(range(t + 1, n))
            local_ok = local_ok and first.union(second) == sites
            local_ok = local_ok and all(
                int(site in first) + int(site in second) <= 2 for site in sites
            )

            current = n
            levels = 0
            while current >= b + 2:
                overlap = sstar if (sstar - current) % 2 == 0 else sstar + 1
                tail = (current - overlap) // 2
                current = tail + overlap
                levels += 1
                if levels > 100:
                    local_ok = False
                    break
            ceiling = math.ceil(math.log2(n - b))
            local_ok = local_ok and 2 <= current <= b + 1
            local_ok = local_ok and levels <= ceiling
            local_ok = local_ok and 3.0 ** (-levels) + 1e-15 >= (
                (1.0 / 3.0) * (n - b) ** (-math.log2(3.0))
            )
            max_levels_slack = max(max_levels_slack, ceiling - levels)
            if not local_ok:
                failures.append(
                    {
                        "sstar": sstar,
                        "n": n,
                        "first_length": length,
                        "levels": levels,
                        "ceiling": ceiling,
                        "stopping_length": current,
                    }
                )

    return {
        "cases": cases,
        "max_sstar": max_sstar,
        "max_excess": max_excess,
        "max_levels_slack": max_levels_slack,
        "failures": failures,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=20000)
    parser.add_argument("--max-sstar", type=int, default=80)
    parser.add_argument("--max-excess", type=int, default=5000)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    result = {
        "claim_tested": (
            "M10 endpoint-tilt density/maximal-correlation bound, exact "
            "two-projection angle formula, and affine recursion arithmetic. "
            "A finite violation refutes the corresponding universal claim; "
            "finite survival proves none of them."
        ),
        "seed": SEED,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "tilt_audit": audit_tilts(args.samples),
        "recursion_audit": audit_recursion(args.max_sstar, args.max_excess),
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
