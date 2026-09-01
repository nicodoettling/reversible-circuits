#!/usr/bin/env python3
"""Finite signed-layer analysis for the balanced/singleton source family.

This retains signs before applying the second K step.  It tests whether the
Theta(n^-1/2)-looking one-step boundary tail is separately smoothed or instead
cancels only against its complementary layers.  All reported values are
floating finite diagnostics.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import platform
import subprocess
import sys
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("m83", HERE / "influence_diagnostic.py")
assert SPEC is not None and SPEC.loader is not None
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def oriented_cycle(n: int, entries):
    p = list(range(n))
    for a, b in zip(entries, entries[1:] + entries[:1]):
        p[a] = b
    return tuple(p)


def analyze(n: int):
    if n < 9 or n % 6 != 3:
        raise ValueError("requires n=3 mod 6 and n>=9")
    k = n // 3
    h, orbits, kernel, squared, _, _ = M.build(n, False)
    A = oriented_cycle(n, (0, k, 2 * k))
    B = M.mul(M.edge_perm(n, 0, 1), M.edge_perm(n, k, 2 * k))
    ai = next(i for i, orbit in enumerate(orbits) if A in orbit)
    bi = next(i for i, orbit in enumerate(orbits) if B in orbit)
    eta = kernel[ai] - kernel[bi]
    image = eta @ kernel

    keys = []
    for orbit in orbits:
        representative = orbit[0]
        sizes = sorted(M.cycle_sizes(M.mul(M.inv(representative), h)))
        keys.append((M.kind(representative), tuple(sizes)))

    def stats(vector):
        output = vector @ kernel
        return {
            "signed_mass": float(np.sum(vector)),
            "TV_before_K": 0.5 * float(np.sum(np.abs(vector))),
            "TV_after_K": 0.5 * float(np.sum(np.abs(output))),
            "n_squared_times_TV_after_K": n * n * 0.5 * float(np.sum(np.abs(output))),
        }

    masks = {}
    masks["three_targets"] = np.array([key[0] == "3" for key in keys])
    masks["double_targets"] = np.array([key[0] == "D" for key in keys])
    masks["singleton_residual_double"] = np.array([
        key[0] == "D" and key[1][0] == 1 for key in keys
    ])
    masks["boundary_tail_u_le_k_minus_1"] = np.array([
        key[0] == "D" and key[1][0] == 1 and key[1][1] <= k - 1
        for key in keys
    ])
    masks["boundary_complement"] = ~masks["boundary_tail_u_le_k_minus_1"]

    groups = {}
    for name, mask in masks.items():
        vector = np.where(mask, eta, 0.0)
        groups[name] = stats(vector)

    singleton_u_layers = []
    for u in range(1, k + 1):
        mask = np.array([
            key[0] == "D" and key[1][0] == 1 and key[1][1] == u
            for key in keys
        ])
        singleton_u_layers.append({"u": u, **stats(np.where(mask, eta, 0.0))})

    # Abel partial sums of the u layers, measured after K.  If a
    # summation-by-parts argument is viable, these cumulative images should
    # be uniformly smaller than the sum of layer seminorms.
    cumulative = np.zeros_like(eta)
    abel_partial_sums = []
    for u in range(1, k + 1):
        mask = np.array([
            key[0] == "D" and key[1][0] == 1 and key[1][1] == u
            for key in keys
        ])
        cumulative += np.where(mask, eta, 0.0)
        abel_partial_sums.append({"u": u, **stats(cumulative)})

    return {
        "n": n,
        "k": k,
        "source_orbits": [ai, bi],
        "full_difference": stats(eta),
        "direct_TV_after_K": 0.5 * float(np.sum(np.abs(image))),
        "groups": groups,
        "singleton_u_layers": singleton_u_layers,
        "singleton_abel_partial_sums": abel_partial_sums,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", nargs="+", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "status": "finite_floating_signed_diagnostic_only",
        "claim_tested": "boundary-tail smoothing after the second K step",
        "convention": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "repository_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": " ".join(sys.argv),
        "results": [analyze(n) for n in args.n],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
