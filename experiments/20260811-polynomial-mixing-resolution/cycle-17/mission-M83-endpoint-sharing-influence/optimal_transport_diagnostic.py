#!/usr/bin/env python3
"""Finite optimal transport bound for (K_A-K_B)K in the balanced family.

The Jordan positive and negative parts of eta=K_A-K_B have equal mass.  A
coupling gamma gives ||eta K||_TV <= sum gamma(s,t) TV(K_s,K_t).  This script
solves that transport problem numerically and records its largest arcs.  It is
diagnostic only; the direct signed mixture may cancel beyond every coupling.
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
from scipy.optimize import linprog
from scipy.sparse import lil_matrix


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("m83", HERE / "influence_diagnostic.py")
assert SPEC is not None and SPEC.loader is not None
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def oriented_cycle(n, entries):
    p = list(range(n))
    for a, b in zip(entries, entries[1:] + entries[:1]):
        p[a] = b
    return tuple(p)


def analyze(n: int, tolerance: float):
    if n % 6 != 3 or n < 9:
        raise ValueError("requires n=3 mod 6, n>=9")
    k = n // 3
    h, orbits, kernel, _, _, witnesses = M.build(n, False)
    A = oriented_cycle(n, (0, k, 2 * k))
    B = M.mul(M.edge_perm(n, 0, 1), M.edge_perm(n, k, 2 * k))
    ai = next(i for i, orbit in enumerate(orbits) if A in orbit)
    bi = next(i for i, orbit in enumerate(orbits) if B in orbit)
    eta = kernel[ai] - kernel[bi]
    positive = np.flatnonzero(eta > tolerance)
    negative = np.flatnonzero(eta < -tolerance)
    supply = eta[positive]
    demand = -eta[negative]
    mass = float(np.sum(supply))
    costs = 0.5 * np.sum(np.abs(
        kernel[positive, None, :] - kernel[None, negative, :]
    ), axis=2)
    p, q = costs.shape
    variables = p * q
    Aeq = lil_matrix((p + q, variables), dtype=float)
    for i in range(p):
        Aeq[i, i * q:(i + 1) * q] = 1.0
    for j in range(q):
        Aeq[p + j, j::q] = 1.0
    beq = np.concatenate([supply, demand])
    # Drop one redundant demand constraint to avoid a rank warning.
    result = linprog(
        costs.ravel(), A_eq=Aeq[:-1].tocsr(), b_eq=beq[:-1],
        bounds=(0, None), method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)
    flow = result.x.reshape((p, q))
    arcs = []
    lambda_edges = set(witnesses)
    for ii, jj in zip(*np.nonzero(flow > tolerance)):
        source, target = int(positive[ii]), int(negative[jj])
        arcs.append({
            "mass": float(flow[ii, jj]),
            "cost_TV_K_rows": float(costs[ii, jj]),
            "weighted_cost": float(flow[ii, jj] * costs[ii, jj]),
            "source_orbits": [source, target],
            "is_Lambda_edge": tuple(sorted((source, target))) in lambda_edges,
            "source_descriptors": [M.descriptor(orbits[x][0], h) for x in (source, target)],
        })
    arcs.sort(key=lambda row: row["weighted_cost"], reverse=True)
    direct = 0.5 * float(np.sum(np.abs(eta @ kernel)))
    optimum = float(result.fun)
    return {
        "n": n,
        "quotient_states": len(orbits),
        "positive_support": len(positive),
        "negative_support": len(negative),
        "Jordan_mass": mass,
        "direct_TV_eta_K": direct,
        "optimal_coupling_upper_bound": optimum,
        "coupling_over_direct_ratio": optimum / direct,
        "n_squared_times_optimal_bound": n * n * optimum,
        "positive_transport_arcs": len(arcs),
        "Lambda_edge_transport_mass_fraction": (
            sum(row["mass"] for row in arcs if row["is_Lambda_edge"]) / mass
        ),
        "top_transport_arcs": arcs[:30],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", nargs="+", type=int, required=True)
    parser.add_argument("--tolerance", type=float, default=1e-11)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "status": "finite_floating_optimal_transport_only",
        "claim_tested": "coupling the Jordan parts of K_A-K_B before the second K step",
        "convention": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "deterministic": True,
        "seed": None,
        "tolerance": args.tolerance,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": __import__("scipy").__version__,
        "repository_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": " ".join(sys.argv),
        "results": [analyze(n, args.tolerance) for n in args.n],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps([{k: v for k, v in row.items() if k != "top_transport_arcs"}
                      for row in payload["results"]], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
