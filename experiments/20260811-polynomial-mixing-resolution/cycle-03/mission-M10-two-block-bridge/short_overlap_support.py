#!/usr/bin/env python3
"""Exact support test for a two-block Q-bridge Gibbs sampler.

Named universal lemma tested: for every N, feasible fixed endpoint, and
positive tail/overlap lengths (t,s), the bipartite support of the boundary
pair (X_t,X_{t+s}) is connected.  A finite disconnected support proves that
the corresponding two-projection maximal correlation is one and refutes
that universal short-overlap angle lemma.  Failure to find one is finite
evidence only.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
from pathlib import Path


COMMIT = "502a6f031c6d5a4bc0064ee5b370a4fa3914f993"


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """p after q: (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    answer = [0] * len(p)
    for i, value in enumerate(p):
        answer[value] = i
    return tuple(answer)


def even(p: tuple[int, ...]) -> bool:
    inversions = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return inversions % 2 == 0


def transpositions(n: int) -> list[tuple[int, ...]]:
    answer = []
    for a in range(n):
        for b in range(a + 1, n):
            p = list(range(n))
            p[a], p[b] = p[b], p[a]
            answer.append(tuple(p))
    return answer


def support_power(
    one_step: set[tuple[int, ...]], exponent: int, identity: tuple[int, ...]
) -> set[tuple[int, ...]]:
    current = {identity}
    for _ in range(exponent):
        current = {compose(x, y) for x in current for y in one_step}
    return current


def cycles(p: tuple[int, ...]) -> list[list[int]]:
    seen = set()
    answer = []
    for start in range(len(p)):
        if start in seen or p[start] == start:
            continue
        cycle = []
        x = start
        while x not in seen:
            seen.add(x)
            cycle.append(x)
            x = p[x]
        answer.append(cycle)
    return answer


def component_sizes(
    left: set[tuple[int, ...]],
    right: set[tuple[int, ...]],
    middle_support: set[tuple[int, ...]],
) -> tuple[list[int], int]:
    adjacency: dict[tuple[str, tuple[int, ...]], set[tuple[str, tuple[int, ...]]]] = {}
    for x in left:
        lx = ("L", x)
        for increment in middle_support:
            y = compose(x, increment)
            if y not in right:
                continue
            ry = ("R", y)
            adjacency.setdefault(lx, set()).add(ry)
            adjacency.setdefault(ry, set()).add(lx)

    seen = set()
    sizes = []
    for node in adjacency:
        if node in seen:
            continue
        stack = [node]
        seen.add(node)
        size = 0
        while stack:
            current = stack.pop()
            size += 1
            for neighbor in adjacency[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        sizes.append(size)
    return sorted(sizes, reverse=True), sum(len(v) for key, v in adjacency.items() if key[0] == "L")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, required=True)
    parser.add_argument("--tail", type=int, default=1)
    parser.add_argument("--overlap", type=int, default=1)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    n, tail, overlap = args.N, args.tail, args.overlap
    identity = tuple(range(n))
    alternating = {p for p in itertools.permutations(range(n)) if even(p)}
    trans = transpositions(n)
    q_support = {compose(a, b) for a in trans for b in trans}
    tail_support = support_power(q_support, tail, identity)
    middle_support = support_power(q_support, overlap, identity)
    endpoint_support = support_power(q_support, 2 * tail + overlap, identity)

    disconnected = []
    component_histogram: dict[str, int] = {}
    for endpoint in sorted(endpoint_support):
        left = tail_support
        right = {compose(endpoint, inverse(z)) for z in tail_support}
        sizes, edge_count = component_sizes(left, right, middle_support)
        key = ",".join(map(str, sizes))
        component_histogram[key] = component_histogram.get(key, 0) + 1
        if len(sizes) > 1:
            disconnected.append(
                {
                    "endpoint": list(endpoint),
                    "endpoint_cycles": cycles(endpoint),
                    "component_sizes": sizes,
                    "positive_boundary_pairs": edge_count,
                }
            )

    payload = {
        "repository_commit": COMMIT,
        "claim_tested": (
            "For every N, feasible endpoint, and positive t,s, the boundary-pair "
            "support of the two-block Q-bridge sampler is connected. One finite "
            "failure forces maximal correlation one and refutes this universal "
            "short-overlap angle lemma; no finite success proves a gap."
        ),
        "convention": "(pq)(x)=p(q(x)); Q=P_transposition^2",
        "parameters": {"N": n, "tail": tail, "overlap": overlap},
        "deterministic": True,
        "random_seed": None,
        "environment": {"python": platform.python_version()},
        "alternating_group_size": len(alternating),
        "q_support_size": len(q_support),
        "tail_support_size": len(tail_support),
        "middle_support_size": len(middle_support),
        "feasible_endpoint_count": len(endpoint_support),
        "component_histogram": component_histogram,
        "disconnected_endpoint_count": len(disconnected),
        "first_disconnected_endpoints": disconnected[:10],
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
