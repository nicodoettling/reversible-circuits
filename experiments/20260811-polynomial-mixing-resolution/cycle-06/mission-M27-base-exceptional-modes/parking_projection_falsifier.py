#!/usr/bin/env python3
"""Exact named falsifier for direct one-entry domination of orbit projection.

Under Stanley's parking labels, project the rank-two heat-bath graph for
reduced long-cycle factorizations onto sorted parking multisets.  Compare its
support with every feasible one-entry replacement of a sorted parking
function.  A missing edge refutes direct one-step domination of the latter
single-site chain (but not a path comparison).
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
from pathlib import Path


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[x]] for x in range(len(p)))


def transposition(n: int, a: int, b: int) -> tuple[int, ...]:
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def parking_labels(n: int, word_edges: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    blocks = [{i} for i in range(n)]
    labels = []
    for a, b in word_edges:
        ia = next(i for i, block in enumerate(blocks) if a in block)
        ib = next(i for i, block in enumerate(blocks) if b in block)
        B, Bp = blocks[ia], blocks[ib]
        if min(B) > min(Bp):
            B, Bp = Bp, B
            ia, ib = ib, ia
        min_bp = min(Bp)
        labels.append(max(x for x in B if x < min_bp))
        merged = B | Bp
        blocks = [block for j, block in enumerate(blocks) if j not in (ia, ib)]
        blocks.append(merged)
    return tuple(labels)


def feasible_sorted_parking(r: int) -> list[tuple[int, ...]]:
    return [
        b
        for b in itertools.combinations_with_replacement(range(r), r)
        if all(value <= i for i, value in enumerate(b))
    ]


def count_vector(b: tuple[int, ...], r: int) -> tuple[int, ...]:
    return tuple(b.count(v) for v in range(r))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=5)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    n = args.n
    r = n - 1
    edges = [(a, b) for a in range(n) for b in range(a + 1, n)]
    perms = [transposition(n, *e) for e in edges]
    identity = tuple(range(n))
    cycle = tuple(list(range(1, n)) + [0])

    words: list[tuple[int, ...]] = []
    labels: dict[tuple[int, ...], tuple[int, ...]] = {}
    for indices in itertools.product(range(len(edges)), repeat=r):
        product = identity
        for i in indices:
            product = compose(product, perms[i])
        if product != cycle:
            continue
        words.append(indices)
        labels[indices] = parking_labels(n, tuple(edges[i] for i in indices))

    observed_orbits = {tuple(sorted(a)) for a in labels.values()}
    feasible = set(feasible_sorted_parking(r))
    if observed_orbits != feasible:
        raise AssertionError("Stanley orbit set disagrees with sorted parking functions")

    projection_edges: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    for rank in range(r - 1):
        groups: dict[tuple[object, ...], list[tuple[int, ...]]] = {}
        for w in words:
            key = (w[:rank], compose(perms[w[rank]], perms[w[rank + 1]]), w[rank + 2 :])
            groups.setdefault(key, []).append(w)
        for group in groups.values():
            orbit_list = {tuple(sorted(labels[w])) for w in group}
            for x, y in itertools.combinations(sorted(orbit_list), 2):
                projection_edges.add((x, y))

    ideal_edges = set()
    feasible_list = sorted(feasible)
    vectors = {b: count_vector(b, r) for b in feasible_list}
    for i, x in enumerate(feasible_list):
        for y in feasible_list[i + 1 :]:
            if sum(abs(a - b) for a, b in zip(vectors[x], vectors[y])) == 2:
                ideal_edges.add((x, y))
    missing = sorted(ideal_edges - projection_edges)

    result = {
        "claim_tested": (
            "Every feasible one-entry replacement between sorted parking "
            "multisets is one stationary-flow projection edge of the local "
            "rank-two heat-bath."
        ),
        "universal_implication": (
            "A missing edge refutes direct one-step domination of a full "
            "single-entry heat-bath; it leaves polynomial path comparison open."
        ),
        "convention": "(pq)(x)=p(q(x)); tuple product left-to-right",
        "seed": None,
        "python": platform.python_version(),
        "n": n,
        "r": r,
        "factorizations": len(words),
        "parking_multisets": len(feasible),
        "projection_edges": len(projection_edges),
        "feasible_one_entry_edges": len(ideal_edges),
        "missing_edges": len(missing),
        "first_missing_edges": missing[:20],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
