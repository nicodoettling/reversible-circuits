#!/usr/bin/env python3
"""Exact connectivity check for the aligned r=4 heat-bath subchain.

Convention: a tuple p stores p[x], and multiply(p,q)=p after q.  A word is
evaluated by right-multiplying its transpositions in displayed order.

Tested universal claim (falsification only): for every N>=3 and even m>=4,
the chain that heat-bath refreshes only aligned windows
(1..4),(3..6),... is irreducible on Omega(N,m).
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
from collections import Counter


def transpositions(n: int) -> list[tuple[int, int]]:
    return [(a, b) for a in range(n) for b in range(a + 1, n)]


def right_multiply(p: tuple[int, ...], t: tuple[int, int]) -> tuple[int, ...]:
    a, b = t
    out = list(p)
    out[a], out[b] = p[b], p[a]
    return tuple(out)


def evaluate(n: int, ts: list[tuple[int, int]], word: tuple[int, ...]) -> tuple[int, ...]:
    p = tuple(range(n))
    for letter in word:
        p = right_multiply(p, ts[letter])
    return p


class DSU:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1


def check_case(n: int, m: int) -> dict[str, object]:
    ts = transpositions(n)
    identity = tuple(range(n))
    words = [
        word
        for word in itertools.product(range(len(ts)), repeat=m)
        if evaluate(n, ts, word) == identity
    ]
    dsu = DSU(len(words))
    starts = list(range(0, m - 3, 2))

    for start in starts:
        fibers: dict[tuple[object, ...], list[int]] = {}
        for index, word in enumerate(words):
            block_product = evaluate(n, ts, word[start : start + 4])
            key = (word[:start], block_product, word[start + 4 :])
            fibers.setdefault(key, []).append(index)
        for fiber in fibers.values():
            first = fiber[0]
            for index in fiber[1:]:
                dsu.union(first, index)

    sizes = Counter(dsu.find(i) for i in range(len(words)))
    return {
        "N": n,
        "m": m,
        "identity_word_count": len(words),
        "aligned_zero_based_window_starts": starts,
        "component_count": len(sizes),
        "component_sizes_descending": sorted(sizes.values(), reverse=True),
        "irreducible": len(sizes) == 1,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", action="append", required=True, help="N,m")
    args = parser.parse_args()
    cases = []
    for raw in args.case:
        n, m = (int(piece) for piece in raw.split(","))
        cases.append(check_case(n, m))
    print(
        json.dumps(
            {
                "python": platform.python_version(),
                "deterministic": True,
                "permutation_convention": "(pq)(x)=p(q(x)); displayed word order",
                "tested_claim": (
                    "The aligned r=4 same-product heat-bath subchain is "
                    "irreducible for every N>=3 and even m>=4."
                ),
                "cases": cases,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
