#!/usr/bin/env python3
"""Exact inversion of Stanley labels for a named UST-basis locality test.

The recursive inverse is the construction in the proof of Stanley's Theorem
3.1.  It enumerates parking functions (not transposition words), maps their
maximal chains to Stanley labelled trees, and tests how many parking-multiset
entries one spanning-tree basis exchange can change.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
from pathlib import Path


Partition = tuple[tuple[int, ...], ...]
Tree = tuple[tuple[int, int], ...]


def normalize(blocks: list[set[int]]) -> Partition:
    return tuple(sorted(tuple(sorted(block)) for block in blocks))


def inverse_chain(a: tuple[int, ...]) -> tuple[Partition, ...]:
    """Maximal NC chain with Stanley labels a, using zero-based values."""
    r = len(a)
    if r == 0:
        return (((0,),),)
    largest = max(a)
    s = max(i for i, value in enumerate(a) if value == largest)
    smaller = inverse_chain(a[:s] + a[s + 1 :])
    new_vertex = largest + 1

    def relabel_partition(partition: Partition) -> list[set[int]]:
        return [
            {x if x <= largest else x + 1 for x in block}
            for block in partition
        ]

    chain: list[Partition] = []
    for new_rank in range(r + 1):
        if new_rank <= s:
            blocks = relabel_partition(smaller[new_rank])
            blocks.append({new_vertex})
        else:
            blocks = relabel_partition(smaller[new_rank - 1])
            target = next(i for i, block in enumerate(blocks) if largest in block)
            blocks[target].add(new_vertex)
        chain.append(normalize(blocks))
    return tuple(chain)


def stanley_tree_from_chain(chain: tuple[Partition, ...]) -> Tree:
    n = len(chain)
    gamma: list[tuple[int, int, int]] = []
    for rank in range(1, n):
        before = [set(block) for block in chain[rank - 1]]
        after = [set(block) for block in chain[rank]]
        merged = next(block for block in after if not any(block == old for old in before))
        pieces = [block for block in before if block < merged]
        if len(pieces) != 2 or pieces[0] | pieces[1] != merged:
            raise AssertionError("Recursive chain does not have a two-block cover")
        B, Bp = pieces
        if min(B) > min(Bp):
            B, Bp = Bp, B
        min_bp = min(Bp)
        label = max(x for x in B if x < min_bp)
        gamma.append((label, min_bp, rank))

    adjacency: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for u, v, rank in gamma:
        adjacency[u].append((v, rank))
        adjacency[v].append((u, rank))
    parent = [-2] * n
    parent[0] = -1
    vertex_label = [-1] * n
    vertex_label[0] = 0
    stack = [0]
    while stack:
        u = stack.pop()
        for v, rank in adjacency[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            vertex_label[v] = rank
            stack.append(v)
    return tuple(sorted(tuple(sorted((vertex_label[u], vertex_label[v]))) for u, v, _ in gamma))


def sorted_parking(r: int):
    for b in itertools.combinations_with_replacement(range(r), r):
        if all(value <= i for i, value in enumerate(b)):
            yield b


def all_parking(r: int):
    for b in sorted_parking(r):
        yield from set(itertools.permutations(b))


def target_trees(n: int) -> tuple[Tree, Tree]:
    # The finite maximizers suggest this double-star family.
    t1 = {(0, 1), (1, 2), (1, 3)}
    t1.update((2, j) for j in range(4, n))
    t2 = set(t1)
    t2.remove((2, 4))
    t2.add((0, 4))
    return tuple(sorted(t1)), tuple(sorted(t2))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = []
    for n in range(5, args.n_max + 1):
        target1, target2 = target_trees(n)
        found: dict[Tree, tuple[int, ...]] = {}
        count = 0
        for a in all_parking(n - 1):
            count += 1
            tree = stanley_tree_from_chain(inverse_chain(a))
            if tree in (target1, target2):
                found[tree] = a
        if count != n ** (n - 2) or len(found) != 2:
            raise AssertionError("Parking/tree enumeration incomplete")
        a, b = found[target1], found[target2]
        ca = [a.count(v) for v in range(n - 1)]
        cb = [b.count(v) for v in range(n - 1)]
        rows.append(
            {
                "n": n,
                "parking_1": a,
                "parking_2": b,
                "multiset_replacements": sum(abs(x - y) for x, y in zip(ca, cb)) // 2,
                "tree_1": target1,
                "tree_2": target2,
            }
        )
    result = {
        "claim_tested": (
            "A single spanning-tree basis exchange changes only a bounded "
            "number of parking-multiset entries under Stanley's bijection."
        ),
        "universal_implication": (
            "The finite sequence can falsify any specified numerical bound; "
            "an asymptotic refutation still requires a proved closed form."
        ),
        "seed": None,
        "python": platform.python_version(),
        "n_max": args.n_max,
        "rows": rows,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
