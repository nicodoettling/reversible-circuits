#!/usr/bin/env python3
"""Fixed-seed exact-witness search for a locally unbreakable F_N state.

Each sampled state is obtained from a paired spanning-tree identity word by
exact project Hurwitz bijections.  Hence any reported witness is rigorously
in F_N.  It has zero one-step probability of leaving connected support under
the full r<=5 heat bath if deleting every interval of at most five factors
leaves a connected support graph.  Failure to find a witness is empirical.
"""

from __future__ import annotations

import argparse
import json
import platform
import random
from pathlib import Path


def edges(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def conj(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    def move(x: int) -> int:
        return b[1] if x == b[0] else b[0] if x == b[1] else x
    x, y = move(a[0]), move(a[1])
    return (x, y) if x < y else (y, x)


def connected_after_deleting(word: list[int], es: list[tuple[int, int]], n: int, lo: int, hi: int) -> bool:
    parent = list(range(n))
    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for pos, idx in enumerate(word):
        if lo <= pos < hi:
            continue
        a, b = map(find, es[idx])
        if a != b:
            parent[b] = a
    return len({find(v) for v in range(n)}) == 1


def locally_unbreakable(word: list[int], es: list[tuple[int, int]], n: int) -> bool:
    m = len(word)
    # If a shorter interval contains every edge of some cut, extending it to
    # a legal interval of length min(5,m) still contains every such edge.
    r = min(5, m)
    return all(connected_after_deleting(word, es, n, i, i + r) for i in range(m - r + 1))


def word_product(word: list[int], es: list[tuple[int, int]], n: int) -> list[int]:
    # Current permutation p represents the left-to-right product read so far;
    # appending transposition t gives p after t.
    p = list(range(n))
    for idx in word:
        a, b = es[idx]
        p[a], p[b] = p[b], p[a]
    return p


def search(n: int, steps: int, seed: int) -> dict:
    es = edges(n)
    index = {e: i for i, e in enumerate(es)}
    conjugates = [[index[conj(a, b)] for b in es] for a in es]
    word = []
    for v in range(1, n):
        e = index[(0, v)]
        word.extend((e, e))
    rng = random.Random(seed)
    for step in range(steps + 1):
        if locally_unbreakable(word, es, n):
            product = word_product(word, es, n)
            support_connected = connected_after_deleting(word, es, n, 0, 0)
            if product != list(range(n)) or not support_connected:
                raise AssertionError("Hurwitz-generated witness left F_N")
            return {
                "found": True,
                "step": step,
                "word_edge_indices": word,
                "word_edges": [list(es[i]) for i in word],
                "all_length_5_complements_connected": True,
                "identity_product_verified": True,
                "full_support_verified": True,
                "zero_macro_exit_implication": (
                    "Every r<=5 window is contained in a length-5 interval; "
                    "the unchanged complement already connects all labels."
                ),
            }
        i = rng.randrange(len(word) - 1)
        a, b = word[i], word[i + 1]
        if rng.randrange(2) == 0:
            word[i], word[i + 1] = b, conjugates[a][b]
        else:
            word[i], word[i + 1] = conjugates[b][a], a
    return {"found": False, "steps": steps}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--N", type=int, required=True)
    p.add_argument("--steps", type=int, default=100000)
    p.add_argument("--seed", type=int, default=290729)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    out = {
        "purpose": "Exact witness search; nonfinding is empirical only.",
        "claim_tested": "Every w in F_N has a positive one-step r<=5 macro exit.",
        "convention": "(pq)(x)=p(q(x)); R(a,b)=(b,bab)",
        "python": platform.python_version(),
        "N": a.N,
        "m": 2 * a.N - 2,
        "steps": a.steps,
        "seed": a.seed,
        "result": search(a.N, a.steps, a.seed),
    }
    a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
