#!/usr/bin/env python3
"""Independent exact N=3 microstate check for the aligned length-eight chain."""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import shlex
import subprocess
import sys
from collections import defaultdict
from pathlib import Path


Permutation = tuple[int, ...]


def compose(p: Permutation, q: Permutation) -> Permutation:
    """Return p after q: (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def transpositions(n: int) -> list[Permutation]:
    answer = []
    for a in range(n):
        for b in range(a + 1, n):
            p = list(range(n))
            p[a], p[b] = p[b], p[a]
            answer.append(tuple(p))
    return answer


def product(factors: tuple[Permutation, ...], identity: Permutation) -> Permutation:
    answer = identity
    for factor in factors:
        answer = compose(answer, factor)
    return answer


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = bytearray(size)

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, first: int, second: int) -> None:
        first = self.find(first)
        second = self.find(second)
        if first == second:
            return
        if self.rank[first] < self.rank[second]:
            first, second = second, first
        self.parent[second] = first
        if self.rank[first] == self.rank[second]:
            self.rank[first] += 1


def cycle_type(p: Permutation) -> list[int]:
    seen: set[int] = set()
    lengths = []
    for start in range(len(p)):
        if start in seen:
            continue
        length = 0
        x = start
        while x not in seen:
            seen.add(x)
            length += 1
            x = p[x]
        lengths.append(length)
    return sorted(lengths, reverse=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    n = 3
    identity = tuple(range(n))
    gates = transpositions(n)
    endpoint_words: dict[Permutation, list[tuple[Permutation, ...]]] = defaultdict(list)
    for word in itertools.product(gates, repeat=8):
        endpoint_words[product(word, identity)].append(word)

    cases = []
    for endpoint, words in sorted(endpoint_words.items()):
        uf = UnionFind(len(words))
        for start in (0, 2, 4):
            first_by_key: dict[tuple[object, ...], int] = {}
            for state, word in enumerate(words):
                block = word[start : start + 4]
                outside = word[:start] + word[start + 4 :]
                key = (start, outside, product(block, identity))
                previous = first_by_key.setdefault(key, state)
                uf.union(state, previous)
        roots = {uf.find(state) for state in range(len(words))}
        cases.append(
            {
                "endpoint": list(endpoint),
                "endpoint_cycle_type": cycle_type(endpoint),
                "fiber_size": len(words),
                "micro_components": len(roots),
                "connected": len(roots) == 1,
            }
        )

    assert sum(case["fiber_size"] for case in cases) == len(gates) ** 8
    assert all(case["connected"] for case in cases)
    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"], check=True, capture_output=True, text=True
    ).stdout.strip()
    result = {
        "claim_tested": (
            "At N=3, every exact length-eight endpoint fiber is connected under "
            "the three aligned four-factor same-product heat-bath support graphs."
        ),
        "scope_warning": "Finite survival is calibration only, not a universal proof.",
        "convention": "compose(p,q)=p after q; displayed word product t1...t8",
        "kernel_support": "aligned windows start at zero-based positions 0,2,4",
        "N": n,
        "transpositions": len(gates),
        "total_words": len(gates) ** 8,
        "cases": cases,
        "all_connected": all(case["connected"] for case in cases),
        "command": shlex.join([sys.executable, *sys.argv]),
        "python": platform.python_version(),
        "seed": None,
        "commit": commit,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
