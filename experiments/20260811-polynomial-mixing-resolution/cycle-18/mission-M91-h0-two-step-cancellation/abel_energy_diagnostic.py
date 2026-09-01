#!/usr/bin/env python3
"""Finite floating diagnostic for a weighted Abel/Fisher sufficient route.

The exact conditional measures are constructed over ``Fraction`` and then
embedded into the floating quotient kernel.  Values are finite falsification
diagnostics only; they do not prove asymptotic bounds.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


A = load_module("balanced_abel", HERE / "balanced_abel_audit.py")
M = A.M


def as_array(vector) -> np.ndarray:
    return np.array([float(value) for value in vector], dtype=float)


def l2_image(vector: np.ndarray, kernel: np.ndarray, pi: np.ndarray) -> float:
    image = vector @ kernel
    return float(np.sum(image * image / pi))


def mixture(masses, conditionals, dimension: int) -> np.ndarray:
    out = np.zeros(dimension, dtype=float)
    for split, probability in masses.items():
        out += float(probability) * as_array(conditionals[split])
    return out


def analyze(k: int) -> dict[str, object]:
    if k < 3 or k % 2 == 0:
        raise ValueError("k must be odd and at least three")
    n = 3 * k
    h, orbits, kernel, squared, pi, _ = M.build(n, False)
    qdim = len(orbits)
    oid = {state: index for index, orbit in enumerate(orbits) for state in orbit}

    source_a = A.oriented_cycle(n, (0, k, 2 * k))
    source_b = M.mul(M.edge_perm(n, 0, 1), M.edge_perm(n, k, 2 * k))
    ai, bi = oid[source_a], oid[source_b]
    residual_a = M.mul(M.inv(source_a), h)
    residual_b = M.mul(M.inv(source_b), h)
    components_a = M.cycles(residual_a)
    components_b = M.cycles(residual_b)
    cminus = next(c for c in components_a if 0 in c)
    middle = next(c for c in components_a if k in c)
    cplus = next(c for c in components_a if 2 * k in c)
    long_cycle = next(c for c in components_b if len(c) == 2 * k - 1)

    nu_minus = A.first_edge_distribution(n, cminus)
    nu_middle = A.first_edge_distribution(n, middle)
    nu_plus = A.first_edge_distribution(n, cplus)
    nu_long = A.first_edge_distribution(n, long_cycle)

    p1, phi1 = A.mixture_conditionals(
        [long_cycle], [nu_long], nu_middle, oid, qdim
    )
    q1, psi1 = A.mixture_conditionals(
        [cminus, cplus], [nu_minus, nu_plus], nu_middle, oid, qdim
    )
    p2, phi2 = A.pair_law_conditioned_on_first_split(
        n, A.cycle_perm(n, long_cycle), [long_cycle], oid, qdim
    )
    q2, psi2 = A.pair_law_conditioned_on_first_split(
        n,
        M.mul(A.cycle_perm(n, cminus), A.cycle_perm(n, cplus)),
        [cminus, cplus],
        oid,
        qdim,
    )
    assert p1 == p2 and q1 == q2
    p, qmass = p1, q1

    m = k - 1
    denominator = 3 * m * (3 * m - 1)
    alpha1 = Fraction(4 * m * m, denominator)
    alpha2 = Fraction(2 * m * (2 * m - 1), denominator)

    cumulative = []
    running = Fraction(0)
    for split in range(1, k):
        running += p.get(split, Fraction(0)) - qmass.get(split, Fraction(0))
        cumulative.append(running)
    assert cumulative[-1] == 0

    gradient_energy = 0.0
    gradient_weight = 0.0
    gradient_rows = []
    for split in range(1, k - 1):
        d = cumulative[split - 1]
        x = (
            float(alpha1) * (as_array(phi1[split]) - as_array(phi1[split + 1]))
            + float(alpha2) * (as_array(phi2[split]) - as_array(phi2[split + 1]))
        )
        energy = l2_image(x, kernel, pi)
        weight = abs(float(d))
        gradient_weight += weight
        gradient_energy += weight * energy
        gradient_rows.append({
            "split": split,
            "D": str(d),
            "image_L2_squared": energy,
            "weighted_contribution": weight * energy,
        })

    embedding_energy = 0.0
    embedding_rows = []
    for split, probability in sorted(qmass.items()):
        y = (
            float(alpha1) * (as_array(phi1[split]) - as_array(psi1[split]))
            + float(alpha2) * (as_array(phi2[split]) - as_array(psi2[split]))
        )
        energy = l2_image(y, kernel, pi)
        weight = float(probability)
        embedding_energy += weight * energy
        embedding_rows.append({
            "split": split,
            "q": str(probability),
            "image_L2_squared": energy,
            "weighted_contribution": weight * energy,
        })

    eta = kernel[bi] - kernel[ai]
    image = eta @ kernel
    actual_l2 = float(np.sum(image * image / pi))
    actual_tv = 0.5 * float(np.sum(np.abs(image)))

    channel1 = mixture(p, phi1, qdim) - mixture(qmass, psi1, qdim)
    channel2 = mixture(p, phi2, qdim) - mixture(qmass, psi2, qdim)
    channel1_image = channel1 @ kernel
    channel2_image = channel2 @ kernel
    channel1_l2 = float(np.sum(channel1_image * channel1_image / pi))
    channel2_l2 = float(np.sum(channel2_image * channel2_image / pi))
    channel_cross = float(np.sum(channel1_image * channel2_image / pi))
    channel_reconstruction = (
        float(alpha1) ** 2 * channel1_l2
        + float(alpha2) ** 2 * channel2_l2
        + 2.0 * float(alpha1) * float(alpha2) * channel_cross
    )
    if not np.isclose(channel_reconstruction, actual_l2, rtol=2e-9, atol=2e-12):
        raise AssertionError("two-channel L2 reconstruction failed")
    fisher_bound = 2.0 * gradient_weight * gradient_energy + 2.0 * embedding_energy
    if actual_l2 > fisher_bound + 1e-10:
        raise AssertionError("weighted Cauchy bound failed")

    return {
        "k": k,
        "n": n,
        "quotient_states": qdim,
        "actual_two_step_TV": actual_tv,
        "k_squared_actual_two_step_TV": k * k * actual_tv,
        "actual_BA2_L2": actual_l2,
        "k_fourth_actual_BA2_L2": k ** 4 * actual_l2,
        "two_channel_L2": {
            "alpha1_squared_channel1": float(alpha1) ** 2 * channel1_l2,
            "alpha2_squared_channel2": float(alpha2) ** 2 * channel2_l2,
            "twice_alpha1_alpha2_cross": (
                2.0 * float(alpha1) * float(alpha2) * channel_cross
            ),
            "unweighted_cross": channel_cross,
            "correlation": channel_cross / np.sqrt(channel1_l2 * channel2_l2),
            "reconstructed": channel_reconstruction,
        },
        "sum_abs_D": gradient_weight,
        "sum_abs_D_over_sqrt_k": gradient_weight / np.sqrt(k),
        "gradient_energy": gradient_energy,
        "k_to_9_over_2_gradient_energy": k ** 4.5 * gradient_energy,
        "embedding_energy": embedding_energy,
        "k_fourth_embedding_energy": k ** 4 * embedding_energy,
        "weighted_Cauchy_bound": fisher_bound,
        "k_fourth_weighted_Cauchy_bound": k ** 4 * fisher_bound,
        "gradient_rows": gradient_rows,
        "embedding_rows": embedding_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", nargs="+", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "status": "finite_floating_falsification_diagnostic_only",
        "target": "balanced Abel collision BA2 and weighted Fisher sufficient route",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
        "results": [analyze(k) for k in args.k],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
