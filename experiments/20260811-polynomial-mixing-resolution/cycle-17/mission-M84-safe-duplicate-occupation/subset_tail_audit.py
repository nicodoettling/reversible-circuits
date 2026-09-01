#!/usr/bin/env python3
"""Exact tail-level safe-duplicate audit for canonical elimination.

For a selected original-label set S, stable extraction in increasing label
order emits the original factors in S and leaves a residual tuple depending
only on S.  Consequently duplicate availability and deletion connectivity are
functions of S, not of the order by which S was reached.  This script audits
the exact static criterion at levels with a small unselected complement.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path


sys.dont_write_bytecode = True

BASE_WORD = (
    (3, 5), (3, 4), (1, 5), (2, 5),
    (1, 6), (0, 4), (3, 7), (2, 7),
    (0, 5), (3, 6), (1, 4), (1, 7),
    (0, 6), (2, 4), (2, 6), (0, 7),
)
VX = (-1, -1, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
VY = (-1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)


def lifted_word(L: int) -> tuple[tuple[int, int], ...]:
    def label(vertex: int, x: int, y: int) -> int:
        return (vertex * L + x) * L + y

    word = []
    for (a, b), dx, dy in zip(BASE_WORD, VX, VY):
        for x in range(L):
            for y in range(L):
                word.append(tuple(sorted((
                    label(a, x, y),
                    label(b, (x + dx) % L, (y + dy) % L),
                ))))
    return tuple(word)


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return pq under (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def edge_perm(edge: tuple[int, int], n: int) -> tuple[int, ...]:
    p = list(range(n))
    a, b = edge
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def conjugate_edge(
    edge: tuple[int, int], permutation: tuple[int, ...]
) -> tuple[int, int]:
    # permutation^{-1} edge permutation; endpoints move by permutation^{-1}.
    inverse = [0] * len(permutation)
    for x, image in enumerate(permutation):
        inverse[image] = x
    return tuple(sorted((inverse[edge[0]], inverse[edge[1]])))


def stable_residual(
    word: tuple[tuple[int, int], ...], selected: frozenset[int], n: int
) -> dict[int, tuple[int, int]]:
    """Residual after extracting selected labels in increasing original order."""
    suffix_product = tuple(range(n))
    residual: dict[int, tuple[int, int]] = {}
    for label in range(len(word) - 1, -1, -1):
        if label in selected:
            suffix_product = compose(edge_perm(word[label], n), suffix_product)
        else:
            residual[label] = conjugate_edge(word[label], suffix_product)
    return residual


def connected(edge_iterable, n: int) -> bool:
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edge_iterable:
        aa, bb = find(a), find(b)
        if aa != bb:
            parent[bb] = aa
    return len({find(x) for x in range(n)}) == 1


def safe_pairs_static(
    word: tuple[tuple[int, int], ...], selected: frozenset[int], n: int
) -> tuple[tuple[int, int], ...]:
    residual = stable_residual(word, selected, n)
    unselected = tuple(sorted(residual))
    answer = []
    for i, j in itertools.combinations(unselected, 2):
        if residual[i] != residual[j]:
            continue
        enlarged = selected | {i, j}
        after = stable_residual(word, enlarged, n)
        if connected(
            itertools.chain(
                (word[label] for label in selected),
                after.values(),
            ),
            n,
        ):
            answer.append((i, j))
    return tuple(answer)


def audit_tail(L: int, complement_sizes: tuple[int, ...]):
    word = lifted_word(L)
    n = 8 * L * L
    k = len(word)
    labels = frozenset(range(k))
    rows = []
    for c in complement_sizes:
        if c < 2 or c > k:
            continue
        safe_subset_count = 0
        safe_pair_total = 0
        safe_pair_histogram = Counter()
        examples = []
        started = time.perf_counter()
        for complement in itertools.combinations(range(k), c):
            selected = labels.difference(complement)
            pairs = safe_pairs_static(word, selected, n)
            safe_pair_histogram[len(pairs)] += 1
            if pairs:
                safe_subset_count += 1
                safe_pair_total += len(pairs)
                if len(examples) < 8:
                    examples.append({
                        "unselected_complement": list(complement),
                        "safe_pairs": [list(pair) for pair in pairs],
                    })
        subset_count = math.comb(k, c)
        denominator = subset_count * math.comb(c, 2)
        rows.append({
            "unselected_count": c,
            "selected_count": k - c,
            "subset_count": subset_count,
            "safe_subset_count": safe_subset_count,
            "safe_pair_total": safe_pair_total,
            "safe_pair_histogram": {
                str(a): count for a, count in sorted(safe_pair_histogram.items())
            },
            "one_level_safe_hit_probability_numerator": safe_pair_total,
            "one_level_safe_hit_probability_denominator": denominator,
            "examples": examples,
            "elapsed_seconds": time.perf_counter() - started,
        })
    return {"L": L, "n": n, "k": k, "tail_levels": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--case", nargs="+", action="append", metavar=("L", "C"))
    args = parser.parse_args()
    cases = args.case or [["1", "2", "3", "4"], ["2", "2", "3"]]
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "argv": sys.argv,
        "commit": commit,
        "python": platform.python_version(),
        "seed": None,
        "nonstandard_dependencies": {},
        "method": (
            "Literal enumeration of all selected subsets whose unselected "
            "complement has the requested size; exact stable-residual formula; "
            "exact duplicate and connectivity predicates."
        ),
        "claim_tested": (
            "Whether a fixed tail level alone supplies a safe-duplicate "
            "probability lower bound for W_L."
        ),
        "results": [
            audit_tail(int(case[0]), tuple(map(int, case[1:]))) for case in cases
        ],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], sort_keys=True))


if __name__ == "__main__":
    main()
