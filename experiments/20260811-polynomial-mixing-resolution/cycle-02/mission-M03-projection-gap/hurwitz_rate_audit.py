#!/usr/bin/env python3
"""Finite exact audit of the connected-Hurwitz zero-range rate sequence.

For support size v and k=2(v-1)+2g, let C(v,k) count connected identity
transposition words and a_v(g)=C(v,k)/k!.  The fixed-support-partition square
chain has zero-range expulsion rates proportional to

    rho_v(g)=a_v(g-1)/a_v(g)
            =k(k-1) C(v,k-2)/C(v,k),  g>=1.

Caputo's uniformly-increasing-rate criterion would require quantitative
control of rho_v(g+1)-rho_v(g).  Gaudilliere--Reygner's first theorem would
require ultra-log-concavity of a_v, equivalently

    g rho_v(g+1) >= (g+1) rho_v(g).

This script can falsify either property in the smallest cases; passing is not
a proof.  Composition is p after q.
"""

from __future__ import annotations

import argparse
import json
import platform
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def compose(p, q):
    return tuple(p[q[x]] for x in range(len(p)))


def transpositions(v):
    out = []
    for a in range(v):
        for b in range(a + 1, v):
            p = list(range(v))
            p[a], p[b] = p[b], p[a]
            out.append((tuple(p), a, b))
    return out


def mask_connected(mask, edges, v):
    adjacency = [set() for _ in range(v)]
    for bit, (_, a, b) in enumerate(edges):
        if mask & (1 << bit):
            adjacency[a].add(b)
            adjacency[b].add(a)
    seen = {0}
    todo = [0]
    while todo:
        x = todo.pop()
        for y in adjacency[x] - seen:
            seen.add(y)
            todo.append(y)
    return len(seen) == v


def connected_counts(v, max_g):
    edges = transpositions(v)
    identity = tuple(range(v))
    max_k = 2 * (v - 1) + 2 * max_g
    dp = {(identity, 0): 1}
    counts = {}
    connected_masks = {
        mask for mask in range(1 << len(edges)) if mask_connected(mask, edges, v)
    }
    for k in range(1, max_k + 1):
        nxt = defaultdict(int)
        for (perm, mask), count in dp.items():
            for bit, (t, _, _) in enumerate(edges):
                nxt[(compose(perm, t), mask | (1 << bit))] += count
        dp = nxt
        if k >= 2 * (v - 1) and k % 2 == 0:
            counts[k] = sum(
                count
                for (perm, mask), count in dp.items()
                if perm == identity and mask in connected_masks
            )
    return counts, len(dp)


def fs(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def audit_v(v, max_g):
    counts, final_dp_states = connected_counts(v, max_g)
    base = 2 * (v - 1)
    rho = {}
    for g in range(1, max_g + 1):
        k = base + 2 * g
        rho[g] = Fraction(k * (k - 1) * counts[k - 2], counts[k])
    increments = {g: rho[g + 1] - rho[g] for g in range(1, max_g)}
    ulc_margins = {
        g: g * rho[g + 1] - (g + 1) * rho[g] for g in range(1, max_g)
    }
    ratio_floor = Fraction(12, v**3)
    return {
        "v": v,
        "max_g": max_g,
        "connected_counts": {str(k): value for k, value in sorted(counts.items())},
        "rho": {str(g): fs(value) for g, value in rho.items()},
        "rho_increments": {str(g): fs(value) for g, value in increments.items()},
        "all_tested_increments_positive": all(value > 0 for value in increments.values()),
        "minimum_tested_increment": fs(min(increments.values())) if increments else None,
        "ultra_log_concavity_margins": {
            str(g): fs(value) for g, value in ulc_margins.items()
        },
        "all_tested_ultra_log_concavity_inequalities_hold": all(
            value >= 0 for value in ulc_margins.values()
        ),
        "first_tested_ultra_log_concavity_failure": next(
            (
                {"g": g, "margin": fs(value)}
                for g, value in ulc_margins.items()
                if value < 0
            ),
            None,
        ),
        "M12_ratio_floor": fs(ratio_floor),
        "all_tested_rho_at_least_M12_ratio_floor": all(
            value >= ratio_floor for value in rho.values()
        ),
        "final_dynamic_program_state_count": final_dp_states,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-v", type=int, default=5)
    parser.add_argument("--max-g", type=int, default=6)
    parser.add_argument("--output", default="hurwitz_rate_results.json")
    args = parser.parse_args()
    result = {
        "python": platform.python_version(),
        "randomness": "none",
        "composition": "compose(p,q)[x]=p[q[x]]; word product t1...tk",
        "claims_tested": [
            "rho_v(g+1)>rho_v(g) for connected identity factorizations",
            "ultra-log-concavity: g*rho_v(g+1)>=(g+1)*rho_v(g)",
            "M12 proved floor rho_v(g)>=12/v^3",
        ],
        "scope_warning": (
            "finite falsification only; passing does not prove uniform monotonicity "
            "or the all-genus ratio floor"
        ),
        "cases": [audit_v(v, args.max_g) for v in range(2, args.max_v + 1)],
    }
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
