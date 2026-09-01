#!/usr/bin/env python3
"""Exact named falsifier for negative dependence of the raw-tree projection.

Claim tested: under the uniform reduced transposition factorizations of the
long cycle (1 2 ... n), the raw factorization-edge-set measure is pairwise
negatively correlated (a necessary consequence of strong Rayleighness).

Permutation convention: (p q)(x)=p(q(x)); tuple products are left-to-right.
The calculation is exhaustive and deterministic; seed is null.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
from collections import Counter
from pathlib import Path


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[x]] for x in range(len(p)))


def transposition(n: int, a: int, b: int) -> tuple[int, ...]:
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=6)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    n = args.n
    if not 3 <= n <= 7:
        raise SystemExit("This exhaustive falsifier is intended for 3<=n<=7")

    edges = [(a, b) for a in range(n) for b in range(a + 1, n)]
    perms = [transposition(n, *e) for e in edges]
    identity = tuple(range(n))
    cycle = tuple(list(range(1, n)) + [0])

    total = 0
    edge_marginal = Counter()
    pair_marginal = Counter()
    tree_weights = Counter()
    for indices in itertools.product(range(len(edges)), repeat=n - 1):
        product = identity
        for i in indices:
            product = compose(product, perms[i])
        if product != cycle:
            continue
        total += 1
        raw = frozenset(edges[i] for i in indices)
        if len(raw) != n - 1:
            raise AssertionError("A reduced long-cycle factorization repeated an edge")
        tree_weights[tuple(sorted(raw))] += 1
        for e in raw:
            edge_marginal[e] += 1
        for e, f in itertools.combinations(sorted(raw), 2):
            pair_marginal[(e, f)] += 1

    witnesses = []
    for (e, f), joint in pair_marginal.items():
        lhs = joint * total
        rhs = edge_marginal[e] * edge_marginal[f]
        if lhs > rhs:
            witnesses.append(
                {
                    "edge_e": e,
                    "edge_f": f,
                    "joint_count": joint,
                    "marginal_e_count": edge_marginal[e],
                    "marginal_f_count": edge_marginal[f],
                    "cross_multiplied_excess": lhs - rhs,
                    "joint_probability": joint / total,
                    "product_of_marginals":
                        edge_marginal[e] * edge_marginal[f] / total**2,
                }
            )
    witnesses.sort(key=lambda z: z["cross_multiplied_excess"], reverse=True)

    result = {
        "claim_tested": (
            "The raw edge-set projection of a uniform reduced long-cycle "
            "factorization has pairwise nonpositive edge correlations."
        ),
        "universal_implication": (
            "A positive witness refutes strong Rayleighness and direct use of "
            "the homogeneous-strongly-Rayleigh basis-exchange theorem for "
            "this raw projection."
        ),
        "convention": "(pq)(x)=p(q(x)); tuple product left-to-right",
        "seed": None,
        "python": platform.python_version(),
        "n": n,
        "endpoint": list(cycle),
        "total_factorizations": total,
        "denes_expected": n ** (n - 2),
        "distinct_raw_trees": len(tree_weights),
        "tree_weight_min": min(tree_weights.values()),
        "tree_weight_max": max(tree_weights.values()),
        "number_positive_pair_correlations": len(witnesses),
        "strongest_witnesses": witnesses[:20],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
