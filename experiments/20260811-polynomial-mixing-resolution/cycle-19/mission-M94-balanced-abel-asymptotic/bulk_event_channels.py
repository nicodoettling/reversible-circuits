#!/usr/bin/env python3
"""Finite channel/Abel decomposition of the central double bulk defect."""

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
ROOT = HERE.parents[3]
M91 = (
    ROOT
    / "experiments/20260811-polynomial-mixing-resolution/cycle-18/"
      "mission-M91-h0-two-step-cancellation/balanced_abel_audit.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


A = load_module("balanced_abel", M91)
M = A.M


def array(vector):
    return np.array([float(value) for value in vector], dtype=float)


def mixture(masses, conditionals, dimension: int):
    out = np.zeros(dimension, dtype=float)
    for split, probability in masses.items():
        out += float(probability) * array(conditionals[split])
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
    residual_a = M.mul(M.inv(source_a), h)
    residual_b = M.mul(M.inv(source_b), h)
    ca = M.cycles(residual_a)
    cb = M.cycles(residual_b)
    cminus = next(c for c in ca if 0 in c)
    middle = next(c for c in ca if k in c)
    cplus = next(c for c in ca if 2 * k in c)
    long_cycle = next(c for c in cb if len(c) == 2 * k - 1)

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

    channel1 = mixture(p, phi1, qdim) - mixture(qmass, psi1, qdim)
    channel2 = mixture(p, phi2, qdim) - mixture(qmass, psi2, qdim)

    cumulative = {}
    running = Fraction(0)
    for split in range(1, k):
        running += p.get(split, Fraction(0)) - qmass.get(split, Fraction(0))
        cumulative[split] = running
    assert cumulative[k - 1] == 0

    gradient1 = np.zeros(qdim)
    gradient2 = np.zeros(qdim)
    for split in range(1, k - 1):
        gradient1 += float(cumulative[split]) * (
            array(phi1[split]) - array(phi1[split + 1])
        )
        gradient2 += float(cumulative[split]) * (
            array(phi2[split]) - array(phi2[split + 1])
        )
    embedding1 = np.zeros(qdim)
    embedding2 = np.zeros(qdim)
    for split, probability in qmass.items():
        embedding1 += float(probability) * (array(phi1[split]) - array(psi1[split]))
        embedding2 += float(probability) * (array(phi2[split]) - array(psi2[split]))
    if not np.allclose(channel1, gradient1 + embedding1, rtol=2e-10, atol=2e-12):
        raise AssertionError("channel one Abel reconstruction failed")
    if not np.allclose(channel2, gradient2 + embedding2, rtol=2e-10, atol=2e-12):
        raise AssertionError("channel two Abel reconstruction failed")

    threshold = (k + 1) // 2
    event = []
    for index, orbit in enumerate(orbits):
        representative = orbit[0]
        if M.kind(representative) == "D" and min(M.descriptor(representative, h)["support_gaps"]) >= threshold:
            event.append(index)

    def event_image(vector):
        return float(np.sum((vector @ kernel)[event]))

    gradient_rows = []
    for split in range(1, k - 1):
        one = float(alpha1) * float(cumulative[split]) * event_image(
            array(phi1[split]) - array(phi1[split + 1])
        )
        two = float(alpha2) * float(cumulative[split]) * event_image(
            array(phi2[split]) - array(phi2[split + 1])
        )
        gradient_rows.append({
            "split": split,
            "D": str(cumulative[split]),
            "alpha1_contribution": one,
            "alpha2_contribution": two,
            "combined": one + two,
            "k_squared_combined": k * k * (one + two),
        })
    embedding_rows = []
    for split, probability in sorted(qmass.items()):
        one = float(alpha1) * float(probability) * event_image(
            array(phi1[split]) - array(psi1[split])
        )
        two = float(alpha2) * float(probability) * event_image(
            array(phi2[split]) - array(psi2[split])
        )
        embedding_rows.append({
            "split": split,
            "q": str(probability),
            "alpha1_contribution": one,
            "alpha2_contribution": two,
            "combined": one + two,
            "k_squared_combined": k * k * (one + two),
        })

    parts = {
        "alpha1_channel1": float(alpha1) * event_image(channel1),
        "alpha2_channel2": float(alpha2) * event_image(channel2),
        "alpha1_gradient1": float(alpha1) * event_image(gradient1),
        "alpha2_gradient2": float(alpha2) * event_image(gradient2),
        "alpha1_embedding1": float(alpha1) * event_image(embedding1),
        "alpha2_embedding2": float(alpha2) * event_image(embedding2),
    }
    parts["complete"] = parts["alpha1_channel1"] + parts["alpha2_channel2"]
    parts["gradient_combined"] = parts["alpha1_gradient1"] + parts["alpha2_gradient2"]
    parts["embedding_combined"] = parts["alpha1_embedding1"] + parts["alpha2_embedding2"]
    direct = float(np.sum((squared[oid[source_b]] - squared[oid[source_a]])[event]))
    if not np.isclose(parts["complete"], direct, rtol=2e-9, atol=2e-12):
        raise AssertionError("direct central event reconstruction failed")

    return {
        "k": k,
        "n": n,
        "quotient_states": qdim,
        "event_orbits": len(event),
        "event_stationary_mass": float(np.sum(pi[event])),
        "k_times_event_stationary_mass": k * float(np.sum(pi[event])),
        "parts": parts,
        "k_squared_parts": {name: k * k * value for name, value in parts.items()},
        "gradient_rows": gradient_rows,
        "embedding_rows": embedding_rows,
        "reconstruction_verified": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", nargs="+", required=True, type=int)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    payload = {
        "status": "finite_floating_falsification_diagnostic_only",
        "target": "two-channel and Abel decomposition of central double bulk defect",
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
