#!/usr/bin/env python3
"""Run the exact quotient UST-to-Hurwitz audit under primary Dénes maps.

This reuses ``quotient_basis_exchange.analyze`` after replacing only its
factorization-to-Cayley-tree bijection.  The quotient kernels, exact rates,
paths, and recovery audit are therefore identical to the Stanley run.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import subprocess
import sys
from pathlib import Path

import equivariant_bijections as eb
import quotient_basis_exchange as qb


def goulden_pepper_map():
    cache: dict[int, dict[tuple[eb.Edge, ...], eb.Tree]] = {}

    def map_word(n: int, raw_edges: tuple[eb.Edge, ...]) -> eb.Tree:
        if n not in cache:
            lookup: dict[tuple[eb.Edge, ...], eb.Tree] = {}
            codes = [()] if n == 2 else itertools.product(range(n), repeat=n - 2)
            for code in codes:
                tree = eb.prufer_tree(n, tuple(code))
                # Translate GP left-to-right application to project functional
                # composition exactly as in equivariant_bijections.py.
                word = tuple(reversed(eb.goulden_pepper_word(n, tree)))
                if word in lookup:
                    raise AssertionError("Goulden--Pepper map collision")
                lookup[word] = tree
            cache[n] = lookup
        return cache[n][raw_edges]

    return map_word


MAPS = {
    "moszkowski": eb.moszkowski_tree,
    "goulden_yong": eb.goulden_yong_tree,
    "goulden_pepper": goulden_pepper_map(),
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--bijection", choices=sorted(MAPS), action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    results = []
    for name in args.bijection:
        qb.stanley_tree = MAPS[name]
        row = qb.analyze(args.n)
        row["bijection"] = name
        results.append(row)
    payload = {
        "claim_tested": (
            "Primary-source Dénes bijections improve finite quotient UST basis-exchange "
            "routing through the adjacent Hurwitz heat-bath graph."
        ),
        "scope_warning": (
            "Finite congestion and path length are calibrations only.  Recovery metadata "
            "fields named Stanley in the reused harness mean the selected Cayley map here."
        ),
        "convention": "(p q)(x)=p(q(x)); tuple products left-to-right",
        "n": args.n,
        "bijections": args.bijection,
        "results": results,
        "python": platform.python_version(),
        "seed": None,
        "deterministic": True,
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": " ".join(sys.argv),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            [
                {
                    "bijection": row["bijection"],
                    "one_bubble_coverage_fraction": row["one_bubble_coverage_fraction"],
                    "maximum_shortest_path_length": row["maximum_shortest_path_length"],
                    "comparison_congestion": row[
                        "lexicographic_shortest_path_comparison_congestion"
                    ],
                    "maximum_recovery_multiplicity": row[
                        "lexicographic_recovery_metadata_audit"
                    ]["maximum_distinct_micro_sources_per_key"],
                }
                for row in results
            ],
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
