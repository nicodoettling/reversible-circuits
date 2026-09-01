#!/usr/bin/env python3
"""Falsify a proposed suffix-trajectory inverse for leaf contraction.

For a canonical macro leaf rotation (parent i, leaf j), lift every reduced
factorization after deleting j.  Inserting (i,j) after position q gives the
long cycle exactly when the suffix after q sends j-1 to i.  The proposed
strong form says there is exactly one such q whose preceding factor is
(i,k) with k>j; this q is then the inverse of leaf contraction.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict
from pathlib import Path

import adjacent_bypass_probe as base
from leaf_rotation_probe import counts_from_macro, leaf_rotations


def contracted_macro(source: tuple[int, ...], parent: int, leaf: int) -> tuple[int, ...]:
    degrees = list(counts_from_macro(source))
    degrees[parent] -= 1
    del degrees[leaf]
    return tuple(value for value, multiplicity in enumerate(degrees) for _ in range(multiplicity))


def lift_edge(edge: tuple[int, int], leaf: int) -> tuple[int, int]:
    return tuple(value if value < leaf else value + 1 for value in edge)


def product(n: int, edges: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    answer = tuple(range(n))
    for edge in edges:
        answer = base.compose(answer, base.transposition(n, edge))
    return answer


def run(n: int) -> dict:
    r = n - 1
    macros = defaultdict(list)
    for labels in itertools.product(range(r), repeat=r):
        if base.is_parking_word(labels):
            macros[tuple(sorted(labels))].append(base.factor_word(base.inverse_chain(labels)))

    reduced = defaultdict(list)
    for labels in itertools.product(range(r - 1), repeat=r - 1):
        if base.is_parking_word(labels):
            reduced[tuple(sorted(labels))].append(base.factor_word(base.inverse_chain(labels)))

    failures = []
    records = []
    full_cycle = tuple(list(range(1, n)) + [0])
    for source in sorted(macros):
        for parent, leaf, target in leaf_rotations(source):
            reduced_macro = contracted_macro(source, parent, leaf)
            multiplicities = []
            for reduced_word in reduced[reduced_macro]:
                lifted = tuple(lift_edge(edge, leaf) for edge in reduced_word)
                candidates = []
                algebraic = []
                for q, edge in enumerate(lifted):
                    suffix = product(n, lifted[q + 1 :])
                    if suffix[leaf - 1] == parent:
                        algebraic.append(q)
                        if edge[0] == parent and edge[1] > leaf:
                            candidates.append(q)
                            inserted = lifted[: q + 1] + ((parent, leaf),) + lifted[q + 1 :]
                            if product(n, inserted) != full_cycle:
                                failures.append({
                                    "kind": "suffix equation does not imply endpoint",
                                    "source": list(source),
                                    "parent": parent,
                                    "leaf": leaf,
                                    "reduced_word": [list(e) for e in reduced_word],
                                    "q": q,
                                })
                multiplicities.append(len(candidates))
                if len(candidates) != 1:
                    failures.append({
                        "kind": "candidate multiplicity",
                        "source": list(source),
                        "parent": parent,
                        "leaf": leaf,
                        "reduced_macro": list(reduced_macro),
                        "reduced_word": [list(e) for e in reduced_word],
                        "lifted": [list(e) for e in lifted],
                        "algebraic_positions": algebraic,
                        "special_positions": candidates,
                    })
            records.append({
                "source": list(source),
                "parent": parent,
                "leaf": leaf,
                "target": list(target),
                "reduced_macro": list(reduced_macro),
                "reduced_factorizations": len(multiplicities),
                "candidate_multiplicities": sorted(set(multiplicities)),
            })
    return {
        "n": n,
        "r": r,
        "claim_tested": "Every reduced factorization has a unique suffix-trajectory insertion site.",
        "universal_scope_warning": "Finite enumeration is a falsifier only.",
        "leaf_rotations": len(records),
        "failures": failures,
        "records": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.n)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "n": result["n"],
        "leaf_rotations": result["leaf_rotations"],
        "failure_count": len(result["failures"]),
        "first_failures": result["failures"][:3],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
