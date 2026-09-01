#!/usr/bin/env python3
"""Deterministic orbit audit for a two-weight bridge path coupling."""

from __future__ import annotations

import argparse
import json
import platform
from itertools import combinations

import numpy as np
import scipy
from scipy.optimize import linprog


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return p after q."""
    return tuple(p[q[i]] for i in range(len(p)))


def transposition_perm(n: int, edge: tuple[int, int]) -> tuple[int, ...]:
    p = list(range(n))
    a, b = edge
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def edge_type(a: tuple[int, int], b: tuple[int, int]) -> str:
    if a == b:
        return "E"
    return "C" if len(set(a) & set(b)) == 1 else "D"


def triple_orbit_key(
    p: tuple[int, int], t: tuple[int, int], tp: tuple[int, int]
) -> tuple[int, ...]:
    """Canonical colored-three-edge graph key under vertex relabeling."""
    best = None
    triples = (p, t, tp)
    for mask in range(8):
        sequence = []
        for index, edge in enumerate(triples):
            sequence.extend(edge if not (mask & (1 << index)) else edge[::-1])
        relabel: dict[int, int] = {}
        restricted = []
        for vertex in sequence:
            if vertex not in relabel:
                relabel[vertex] = len(relabel)
            restricted.append(relabel[vertex])
        key = tuple(restricted)
        if best is None or key < best:
            best = key
    assert best is not None
    return best


def midpoint_fiber(
    h: tuple[int, ...],
    edges: list[tuple[int, int]],
    perms: dict[tuple[int, int], tuple[int, ...]],
) -> list[tuple[int, int]]:
    transposition_perms = {value for value in perms.values()}
    return [r for r in edges if compose(perms[r], h) in transposition_perms]


def transport_cost(
    left: list[tuple[int, int]],
    right: list[tuple[int, int]],
    x: float,
) -> tuple[float, list[list[float]]]:
    nl, nr = len(left), len(right)
    costs = []
    for a in left:
        for b in right:
            typ = edge_type(a, b)
            costs.append(0.0 if typ == "E" else (1.0 if typ == "C" else x))

    aeq = []
    beq = []
    for i in range(nl):
        row = [0.0] * (nl * nr)
        for j in range(nr):
            row[i * nr + j] = 1.0
        aeq.append(row)
        beq.append(1.0 / nl)
    for j in range(nr):
        row = [0.0] * (nl * nr)
        for i in range(nl):
            row[i * nr + j] = 1.0
        aeq.append(row)
        beq.append(1.0 / nr)

    result = linprog(
        np.asarray(costs),
        A_eq=np.asarray(aeq),
        b_eq=np.asarray(beq),
        bounds=(0.0, None),
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)
    plan = result.x.reshape((nl, nr)).tolist()
    return float(result.fun), plan


def audit_n(n: int, grid: list[float]) -> dict:
    edges = list(combinations(range(n), 2))
    perms = {edge: transposition_perm(n, edge) for edge in edges}
    cases_by_orbit: dict[str, dict[tuple[int, ...], dict]] = {"C": {}, "D": {}}
    raw_case_counts = {"C": 0, "D": 0}

    for t in edges:
        for tp in edges:
            q = edge_type(t, tp)
            if q == "E":
                continue
            for p in edges:
                raw_case_counts[q] += 1
                orbit_key = triple_orbit_key(p, t, tp)
                if orbit_key in cases_by_orbit[q]:
                    continue
                h = compose(perms[p], perms[t])
                hp = compose(perms[p], perms[tp])
                left = midpoint_fiber(h, edges, perms)
                right = midpoint_fiber(hp, edges, perms)
                cases_by_orbit[q][orbit_key] = {
                    "p": p,
                    "t": t,
                    "tp": tp,
                    "left": left,
                    "right": right,
                    "orbit_key": orbit_key,
                }

    cases = {q: list(cases_by_orbit[q].values()) for q in ("C", "D")}

    grid_rows = []
    for x in grid:
        maxima = {}
        for q in ("C", "D"):
            if not cases[q]:
                maxima[q] = None
                continue
            best_cost = -1.0
            best_case = None
            best_plan = None
            for case in cases[q]:
                cost, plan = transport_cost(case["left"], case["right"], x)
                if cost > best_cost + 1e-10:
                    best_cost = cost
                    best_case = case
                    best_plan = plan
            assert best_case is not None
            maxima[q] = {
                "cost": best_cost,
                "p": list(best_case["p"]),
                "t": list(best_case["t"]),
                "tp": list(best_case["tp"]),
                "orbit_key": list(best_case["orbit_key"]),
                "left": [list(e) for e in best_case["left"]],
                "right": [list(e) for e in best_case["right"]],
                "plan": best_plan,
            }
        grid_rows.append(
            {
                "x": x,
                "A_C": maxima["C"],
                "A_D": maxima["D"],
                "margin_C": (
                    None if maxima["C"] is None else 1.0 - 2.0 * maxima["C"]["cost"]
                ),
                "margin_D": (
                    None if maxima["D"] is None else x - 2.0 * maxima["D"]["cost"]
                ),
            }
        )

    return {
        "N": n,
        "M": len(edges),
        "raw_case_counts": raw_case_counts,
        "orbit_case_counts": {q: len(cases[q]) for q in cases},
        "grid": grid_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="results.json")
    parser.add_argument("--n-min", type=int, default=3)
    parser.add_argument("--n-max", type=int, default=9)
    args = parser.parse_args()

    # A logarithmic/rationally recognizable grid; follow-up proof extracts
    # explicit witnesses rather than treating this scan as universal.
    grid = [
        0.05,
        0.1,
        0.2,
        1 / 3,
        0.5,
        2 / 3,
        0.8,
        1.0,
        1.25,
        1.5,
        2.0,
        3.0,
        5.0,
        10.0,
        20.0,
    ]
    payload = {
        "claim_tested": "existence of positive two-type weights satisfying 2 A_C<1 and 2 A_D<x",
        "seed": 0,
        "python": platform.python_version(),
        "scipy": scipy.__version__,
        "numpy": np.__version__,
        "convention": "compose(p,q)=p after q",
        "runs": [audit_n(n, grid) for n in range(args.n_min, args.n_max + 1)],
    }
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


if __name__ == "__main__":
    main()
