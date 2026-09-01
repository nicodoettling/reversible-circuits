#!/usr/bin/env python3
"""Enumerate exact raw witnesses for one named parking-macro transition."""

from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict
from pathlib import Path

import adjacent_bypass_probe as base


def parse_macro(text: str) -> tuple[int, ...]:
    return tuple(int(value) for value in text.split(",") if value != "")


def run(source: tuple[int, ...], target: tuple[int, ...]) -> dict:
    r = len(source)
    n = r + 1
    if len(target) != r:
        raise ValueError("source and target lengths differ")
    identity = tuple(range(n))
    cycle = tuple(list(range(1, n)) + [0])
    edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
    edge_index = {edge: i for i, edge in enumerate(edges)}
    perms = [base.transposition(n, edge) for edge in edges]
    pair_fibers = defaultdict(list)
    for first, p in enumerate(perms):
        for second, q in enumerate(perms):
            pair_fibers[base.compose(p, q)].append((first, second))

    witnesses = []
    sources = 0
    for labels in sorted(set(itertools.permutations(source))):
        word_edges = base.factor_word(base.inverse_chain(labels))
        word = tuple(edge_index[edge] for edge in word_edges)
        product = identity
        for index in word:
            product = base.compose(product, perms[index])
        if product != cycle:
            raise AssertionError("wrong endpoint")
        sources += 1
        for pos in range(r - 1):
            pair_product = base.compose(perms[word[pos]], perms[word[pos + 1]])
            favorable = []
            for first, second in pair_fibers[pair_product]:
                new_word = word[:pos] + (first, second) + word[pos + 2 :]
                new_macro = tuple(sorted(edges[index][0] for index in new_word))
                if new_macro == target:
                    favorable.append((edges[first], edges[second]))
            if favorable:
                witnesses.append(
                    {
                        "labels": list(labels),
                        "position": pos,
                        "edges": [list(edge) for edge in word_edges],
                        "source_pair": [list(word_edges[pos]), list(word_edges[pos + 1])],
                        "target_pairs": [
                            [list(first), list(second)] for first, second in favorable
                        ],
                    }
                )
    return {
        "source": list(source),
        "target": list(target),
        "source_orbit": sources,
        "witness_positions": len(witnesses),
        "favorable_raw_outcomes": sum(len(row["target_pairs"]) for row in witnesses),
        "convention": "(pq)(x)=p(q(x)); tuple product left-to-right",
        "witnesses": witnesses,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(parse_macro(args.source), parse_macro(args.target))
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {key: value for key, value in result.items() if key != "witnesses"},
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
