#!/usr/bin/env python3
"""Exact falsifier for the proposed h,h,j parking-word suffix lemma."""

from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict
from pathlib import Path

import adjacent_bypass_probe as base


def run(n: int) -> dict:
    r = n - 1
    edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
    edge_index = {edge: i for i, edge in enumerate(edges)}
    perms = [base.transposition(n, edge) for edge in edges]
    fibers = defaultdict(list)
    for first, p in enumerate(perms):
        for second, q in enumerate(perms):
            fibers[base.compose(p, q)].append((first, second))

    tests = 0
    failures = []
    for labels in itertools.product(range(r), repeat=r):
        if not base.is_parking_word(labels) or r < 3:
            continue
        h, duplicate, j = labels[-3:]
        if h != duplicate or not h < j:
            continue
        tests += 1
        word_edges = base.factor_word(base.inverse_chain(labels))
        word = tuple(edge_index[edge] for edge in word_edges)
        pos = r - 3
        product = base.compose(perms[word[pos]], perms[word[pos + 1]])
        source = tuple(sorted(labels))
        expected_counts = [source.count(k) for k in range(r)]
        expected_counts[h] -= 1
        expected_counts[j] += 1
        expected = tuple(
            value
            for value, multiplicity in enumerate(expected_counts)
            for _ in range(multiplicity)
        )
        target_outcomes = []
        for first, second in fibers[product]:
            target_word = word[:pos] + (first, second) + word[pos + 2 :]
            target = tuple(sorted(edges[index][0] for index in target_word))
            if target == expected:
                target_outcomes.append((edges[first], edges[second]))
        if len(target_outcomes) != 2:
            failures.append(
                {
                    "labels": list(labels),
                    "h": h,
                    "j": j,
                    "source_pair": [list(word_edges[pos]), list(word_edges[pos + 1])],
                    "expected": list(expected),
                    "target_outcomes": [
                        [list(first), list(second)] for first, second in target_outcomes
                    ],
                }
            )
            if len(failures) >= 20:
                break
    return {
        "n": n,
        "r": r,
        "claim_tested": (
            "If a parking word ends h,h,j with h<j, the rank-two heat bath "
            "at the two h coordinates has exactly two outcomes replacing h by j."
        ),
        "universal_scope_warning": "Finite enumeration is a falsifier only.",
        "tested_words": tests,
        "failures": failures,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.n)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
