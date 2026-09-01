#!/usr/bin/env python3
"""Exact falsification harness for aligned length-four bridge resampling."""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import shlex
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return p after q."""
    return tuple(p[q[x]] for x in range(len(p)))


def transpositions(n: int) -> list[tuple[int, ...]]:
    out = []
    for a in range(n):
        for b in range(a + 1, n):
            p = list(range(n))
            p[a], p[b] = p[b], p[a]
            out.append(tuple(p))
    return out


def product(indices: tuple[int, ...], gates: list[tuple[int, ...]]) -> tuple[int, ...]:
    value = tuple(range(len(gates[0])))
    for index in indices:
        value = compose(value, gates[index])
    return value


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = bytearray(size)

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


def analyze(n: int, length: int) -> dict[str, object]:
    gates = transpositions(n)
    width = 2 * length
    count = len(gates) ** width
    uf = UnionFind(count)
    endpoints: list[tuple[int, ...]] = [()] * count
    clique_representative: dict[tuple[object, ...], int] = {}

    for state_id, word in enumerate(itertools.product(range(len(gates)), repeat=width)):
        endpoint = product(word, gates)
        endpoints[state_id] = endpoint
        for start in range(0, width - 3, 2):
            block_product = product(word[start : start + 4], gates)
            key = (start, word[:start], word[start + 4 :], block_product)
            representative = clique_representative.setdefault(key, state_id)
            uf.union(state_id, representative)

    endpoint_roots: dict[tuple[int, ...], set[int]] = defaultdict(set)
    endpoint_sizes: Counter[tuple[int, ...]] = Counter(endpoints)
    root_endpoint: dict[int, tuple[int, ...]] = {}
    for state_id, endpoint in enumerate(endpoints):
        root = uf.find(state_id)
        previous = root_endpoint.setdefault(root, endpoint)
        assert previous == endpoint, "aligned heat-bath union crossed endpoints"
        endpoint_roots[endpoint].add(root)

    component_histogram = Counter(len(roots) for roots in endpoint_roots.values())
    disconnected = [
        {
            "endpoint": list(endpoint),
            "fiber_size": endpoint_sizes[endpoint],
            "components": len(roots),
        }
        for endpoint, roots in endpoint_roots.items()
        if len(roots) != 1
    ]
    return {
        "N": n,
        "pair_length": length,
        "transposition_word_length": width,
        "transpositions": len(gates),
        "states": count,
        "feasible_endpoints": len(endpoint_roots),
        "component_count_histogram_over_endpoints": {
            str(key): value for key, value in sorted(component_histogram.items())
        },
        "minimum_fiber_size": min(endpoint_sizes.values()),
        "maximum_fiber_size": max(endpoint_sizes.values()),
        "disconnected_endpoints": disconnected,
        "all_endpoint_fibers_connected": not disconnected,
    }


def git_commit() -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", action="append", default=[], help="N,l")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cases = [(3, 2), (3, 3), (3, 4), (3, 5), (4, 2), (4, 3)]
    if args.case:
        cases = [tuple(map(int, item.split(","))) for item in args.case]
    result = {
        "claim_tested": (
            "every nonempty fixed-endpoint microfactorized Q-bridge fiber is "
            "connected under aligned length-four same-product heat baths"
        ),
        "scope_warning": "finite connectivity can refute but cannot prove the universal claim or a gap",
        "convention": "compose(p,q)=p after q; word product t1...tm",
        "command": shlex.join([sys.executable, *sys.argv]),
        "seed": None,
        "python": platform.python_version(),
        "commit": git_commit(),
        "cases": [analyze(n, length) for n, length in cases],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
