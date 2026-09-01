#!/usr/bin/env python3
"""List exact raw witnesses for the 0/1/2 two-hop obstruction family."""

from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict
from pathlib import Path

import adjacent_bypass_probe as base


def run(a: int, b: int) -> dict:
    r = a + b + 1
    n = r + 1
    identity = tuple(range(n))
    cycle = tuple(list(range(1, n)) + [0])
    edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
    edge_index = {edge: i for i, edge in enumerate(edges)}
    perms = [base.transposition(n, edge) for edge in edges]
    fibers = defaultdict(list)
    for i, p in enumerate(perms):
        for j, q in enumerate(perms):
            fibers[base.compose(p, q)].append((i, j))

    x = (0,) * a + (1,) + (2,) * b
    y = (0,) * a + (2,) * (b + 1)
    delta = (0,) * (a + 1) + (2,) * b
    zeta = (0,) * (a - 1) + (1,) + (2,) * (b + 1)
    wanted = {(x, delta), (delta, y), (x, zeta), (zeta, y)}
    witnesses = {f"{source}->{target}": [] for source, target in wanted}

    for labels in itertools.product(range(r), repeat=r):
        if tuple(sorted(labels)) not in {x, delta, zeta}:
            continue
        word_edges = base.factor_word(base.inverse_chain(labels))
        word = tuple(edge_index[edge] for edge in word_edges)
        product = identity
        for index in word:
            product = base.compose(product, perms[index])
        if product != cycle:
            raise AssertionError("wrong endpoint")
        source = tuple(sorted(labels))
        for pos in range(r - 1):
            pair_product = base.compose(perms[word[pos]], perms[word[pos + 1]])
            for first, second in fibers[pair_product]:
                target_word = word[:pos] + (first, second) + word[pos + 2 :]
                target_edges = tuple(edges[index] for index in target_word)
                target = tuple(sorted(edge[0] for edge in target_edges))
                if (source, target) not in wanted or target == source:
                    continue
                key = f"{source}->{target}"
                witnesses[key].append(
                    {
                        "source_labels": list(labels),
                        "source_edges": [list(edge) for edge in word_edges],
                        "position": pos,
                        "source_pair": [list(word_edges[pos]), list(word_edges[pos + 1])],
                        "target_pair": [list(edges[first]), list(edges[second])],
                    }
                )

    return {
        "a": a,
        "b": b,
        "r": r,
        "convention": "(pq)(x)=p(q(x)); tuple product left-to-right",
        "witnesses": witnesses,
        "counts": {key: len(value) for key, value in witnesses.items()},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", type=int, required=True)
    parser.add_argument("--b", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.a, args.b)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["counts"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
