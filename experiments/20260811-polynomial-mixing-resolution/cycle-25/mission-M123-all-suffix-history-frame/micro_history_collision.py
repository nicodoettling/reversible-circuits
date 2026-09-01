#!/usr/bin/env python3
"""Literal word/scan/outcome witness for the M123 reset-category collision.

The witness is the fresh right-heavy contextual state ``(s,K,R,B)=(4,1,0,1)``.
It is realized in the ambient rank-five parking projection by the coarse root
composition ``(5)`` and refinement ``(4,1)``.  This script reconstructs every
parking factor word, every scan site, and every same-product rank-two outcome
for the unique relevant source macro.  It then records the favourable marked
outcomes and the two active canonical basins which contain their standardized
local source composition ``(1,1,1,1)``.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import platform
from collections import Counter, defaultdict
from fractions import Fraction as F
from pathlib import Path


Perm = tuple[int, ...]
Partition = tuple[tuple[int, ...], ...]
Edge = tuple[int, int]
Macro = tuple[int, ...]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, image in enumerate(p):
        out[image] = x
    return tuple(out)


def transposition(n: int, edge: Edge) -> Perm:
    out = list(range(n))
    a, b = edge
    out[a], out[b] = out[b], out[a]
    return tuple(out)


def partition_perm(partition: Partition) -> Perm:
    n = sum(len(block) for block in partition)
    out = list(range(n))
    for block in partition:
        if len(block) > 1:
            for x, image in zip(block, block[1:] + block[:1]):
                out[x] = image
    return tuple(out)


def normalize(blocks: list[set[int]]) -> Partition:
    return tuple(sorted(tuple(sorted(block)) for block in blocks))


def inverse_chain(labels: tuple[int, ...]) -> tuple[Partition, ...]:
    r = len(labels)
    if r == 0:
        return (((0,),),)
    largest = max(labels)
    position = max(i for i, value in enumerate(labels) if value == largest)
    smaller = inverse_chain(labels[:position] + labels[position + 1 :])
    new_vertex = largest + 1

    def relabel(partition: Partition) -> list[set[int]]:
        return [
            {x if x <= largest else x + 1 for x in block}
            for block in partition
        ]

    chain = []
    for rank in range(r + 1):
        if rank <= position:
            blocks = relabel(smaller[rank])
            blocks.append({new_vertex})
        else:
            blocks = relabel(smaller[rank - 1])
            target = next(i for i, block in enumerate(blocks) if largest in block)
            blocks[target].add(new_vertex)
        chain.append(normalize(blocks))
    return tuple(chain)


def factor_word(chain: tuple[Partition, ...]) -> tuple[Edge, ...]:
    word = []
    for rank in range(1, len(chain)):
        before = [set(block) for block in chain[rank - 1]]
        after = [set(block) for block in chain[rank]]
        merged = next(block for block in after if not any(block == old for old in before))
        pieces = [block for block in before if block < merged]
        if len(pieces) != 2 or pieces[0] | pieces[1] != merged:
            raise AssertionError("invalid chain cover")
        quotient = compose(inverse(partition_perm(chain[rank - 1])), partition_perm(chain[rank]))
        moved = [x for x, image in enumerate(quotient) if x != image]
        if len(moved) != 2:
            raise AssertionError("non-transposition cover")
        word.append(tuple(moved))
    return tuple(word)


def is_parking(labels: tuple[int, ...]) -> bool:
    return all(value <= index for index, value in enumerate(sorted(labels)))


def degrees(macro: Macro) -> list[int]:
    return [macro.count(i) for i in range(len(macro))] + [0]


def children(macro: Macro) -> list[list[int]]:
    d = degrees(macro)
    out = [[] for _ in d]
    stack = [[0, d[0]]]
    for vertex in range(1, len(d)):
        while stack and stack[-1][1] == 0:
            stack.pop()
        parent = stack[-1][0]
        out[parent].append(vertex)
        stack[-1][1] -= 1
        stack.append([vertex, d[vertex]])
    return out


def root_composition(macro: Macro) -> tuple[int, ...]:
    child_rows = children(macro)

    def size(vertex: int) -> int:
        return 1 + sum(size(child) for child in child_rows[vertex])

    return tuple(size(child) for child in child_rows[0])


def root_intervals(macro: Macro) -> list[tuple[int, int]]:
    d = degrees(macro)
    out = []
    start = 1
    for _ in range(d[0]):
        balance = 0
        for vertex in range(start, len(d)):
            balance += d[vertex] - 1
            if balance == -1:
                out.append((start, vertex))
                start = vertex + 1
                break
    return out


def local_macro(macro: Macro, interval: tuple[int, int]) -> Macro:
    d = degrees(macro)
    first, last = interval
    return tuple(
        local
        for local in range(last - first)
        for _ in range(d[first + local])
    )


def main() -> None:
    n = 6
    r = n - 1
    source_macro = (0, 1, 1, 1, 1)
    coarse = (5,)
    refined = (4, 1)
    edges = tuple((a, b) for a in range(n) for b in range(a + 1, n))
    edge_index = {edge: index for index, edge in enumerate(edges)}
    perms = tuple(transposition(n, edge) for edge in edges)
    fibers: dict[Perm, list[tuple[int, int]]] = defaultdict(list)
    for i, left in enumerate(perms):
        for j, right in enumerate(perms):
            fibers[compose(left, right)].append((i, j))

    words = []
    for labels in itertools.product(range(r), repeat=r):
        if not is_parking(labels) or tuple(sorted(labels)) != source_macro:
            continue
        word_edges = factor_word(inverse_chain(labels))
        words.append((labels, tuple(edge_index[edge] for edge in word_edges), word_edges))

    if len(words) != math.factorial(r) // math.factorial(4):
        raise AssertionError("source orbit size")
    if root_composition(source_macro) != coarse:
        raise AssertionError("coarse composition")
    interval = root_intervals(source_macro)[0]
    local = local_macro(source_macro, interval)
    if local != (0, 0, 0, 0) or root_composition(local) != (1, 1, 1, 1):
        raise AssertionError("local star")

    marked = []
    all_fiber_sizes = set()
    favourable_rate = F(0)
    for labels, word, word_edges in words:
        for scan in range(r - 1):
            product = compose(perms[word[scan]], perms[word[scan + 1]])
            fiber = fibers[product]
            all_fiber_sizes.add(len(fiber))
            for outcome, (first, second) in enumerate(fiber):
                target_word = word[:scan] + (first, second) + word[scan + 2 :]
                target_macro = tuple(sorted(edges[index][0] for index in target_word))
                if root_composition(target_macro) == refined:
                    favourable_rate += F(1, len(words) * (r - 1) * len(fiber))
                    marked.append(
                        {
                            "labels": list(labels),
                            "source_word_edges": [list(edge) for edge in word_edges],
                            "scan_index": scan,
                            "old_pair": [list(edges[word[scan]]), list(edges[word[scan + 1]])],
                            "fiber_outcome_index": outcome,
                            "pair_fiber_size": len(fiber),
                            "new_pair": [list(edges[first]), list(edges[second])],
                            "target_macro": list(target_macro),
                        }
                    )

    alpha = F(2, 3 * r * (r - 1))
    # Pair fibers can have size two or three; keep the actual denominator.
    if favourable_rate != alpha:
        raise AssertionError((favourable_rate, alpha))

    payload = {
        "claim_tested": (
            "literal hidden word/scan/outcome atoms at x=(4,1,0,1) are "
            "favourable and nevertheless lie in two active canonical basins"
        ),
        "convention": "(pq)(x)=p(q(x)); factors displayed left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "ambient": {"n": n, "r": r, "coarse": list(coarse), "refined": list(refined)},
        "context": [4, 1, 0, 1],
        "source_macro": list(source_macro),
        "local_macro": list(local),
        "local_root_composition": [1, 1, 1, 1],
        "source_word_count": len(words),
        "scan_count_per_word": r - 1,
        "all_pair_fiber_sizes": sorted(all_fiber_sizes),
        "favourable_rate": {"numerator": str(favourable_rate.numerator), "denominator": str(favourable_rate.denominator)},
        "alpha_r": {"numerator": str(alpha.numerator), "denominator": str(alpha.denominator)},
        "favourable_mark_count": len(marked),
        "normalized_contextual_value_phi": 1,
        "active_canonical_endpoints_containing_every_mark": [[2, 1, 1], [3, 1]],
        "favourable_marks": marked,
    }
    output = Path(__file__).with_name("micro_collision.json")
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    output.write_text(encoded)
    print(json.dumps({"output": str(output), "sha256": hashlib.sha256(encoded.encode()).hexdigest(), "favourable_mark_count": len(marked)}, sort_keys=True))


if __name__ == "__main__":
    main()

