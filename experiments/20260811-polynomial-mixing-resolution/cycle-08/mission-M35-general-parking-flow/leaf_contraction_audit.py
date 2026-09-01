#!/usr/bin/env python3
"""Audit the proposed deletion bijection behind the leaf-rotation count.

For a preorder leaf rotation m -> m-e_i+e_j, delete vertex j and the
distinguished factor (i,j) from every favorable special-pair witness.  The
claim is that this gives each minimal long-cycle factorization with the
contracted parking macro exactly once.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path

import adjacent_bypass_probe as base
from leaf_rotation_probe import counts_from_macro, leaf_rotations


def relabel_after_deletion(edge: tuple[int, int], deleted: int) -> tuple[int, int]:
    if deleted in edge:
        raise ValueError("deleted vertex remains incident")
    return tuple(value if value < deleted else value - 1 for value in edge)


def contracted_macro(source: tuple[int, ...], parent: int, leaf: int) -> tuple[int, ...]:
    degrees = list(counts_from_macro(source))
    degrees[parent] -= 1
    del degrees[leaf]
    return tuple(value for value, multiplicity in enumerate(degrees) for _ in range(multiplicity))


def run(n: int) -> dict:
    r = n - 1
    identity = tuple(range(n))
    cycle = tuple(list(range(1, n)) + [0])
    edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
    edge_index = {edge: index for index, edge in enumerate(edges)}
    perms = [base.transposition(n, edge) for edge in edges]
    fibers = defaultdict(list)
    for first, p in enumerate(perms):
        for second, q in enumerate(perms):
            fibers[base.compose(p, q)].append((first, second))

    macro_words = defaultdict(list)
    for labels in itertools.product(range(r), repeat=r):
        if not base.is_parking_word(labels):
            continue
        word_edges = base.factor_word(base.inverse_chain(labels))
        macro_words[tuple(sorted(labels))].append((labels, word_edges))

    reduced_words_by_macro = defaultdict(set)
    if r >= 2:
        for labels in itertools.product(range(r - 1), repeat=r - 1):
            if not base.is_parking_word(labels):
                continue
            reduced_words_by_macro[tuple(sorted(labels))].add(
                base.factor_word(base.inverse_chain(labels))
            )

    failures = []
    records = []
    for source, rows in sorted(macro_words.items()):
        for parent, leaf, target in leaf_rotations(source):
            image_counter = Counter()
            witness_count = 0
            for labels, word_edges in rows:
                word = tuple(edge_index[edge] for edge in word_edges)
                product = identity
                for index in word:
                    product = base.compose(product, perms[index])
                if product != cycle:
                    raise AssertionError("wrong endpoint")
                for pos in range(r - 1):
                    pair_product = base.compose(perms[word[pos]], perms[word[pos + 1]])
                    favorable = 0
                    for first, second in fibers[pair_product]:
                        target_word = word[:pos] + (first, second) + word[pos + 2 :]
                        actual = tuple(sorted(edges[index][0] for index in target_word))
                        favorable += actual == target
                    if favorable != 2:
                        continue
                    witness_count += 1
                    expected_pair = ((parent, word_edges[pos][1]), (parent, leaf))
                    pair = (word_edges[pos], word_edges[pos + 1])
                    if (
                        pair[0][0] != parent
                        or pair[1] != (parent, leaf)
                        or pair[0][1] <= leaf
                    ):
                        failures.append(
                            {
                                "kind": "special-pair form",
                                "source": list(source),
                                "parent": parent,
                                "leaf": leaf,
                                "labels": list(labels),
                                "position": pos,
                                "pair": [list(edge) for edge in pair],
                                "expected_shape": [list(edge) for edge in expected_pair],
                            }
                        )
                        continue
                    incident = [edge for edge in word_edges if leaf in edge]
                    if incident != [(parent, leaf)]:
                        failures.append(
                            {
                                "kind": "raw vertex is not a leaf",
                                "source": list(source),
                                "parent": parent,
                                "leaf": leaf,
                                "labels": list(labels),
                                "incident_edges": [list(edge) for edge in incident],
                            }
                        )
                        continue
                    reduced = tuple(
                        relabel_after_deletion(edge, leaf)
                        for index, edge in enumerate(word_edges)
                        if index != pos + 1
                    )
                    image_counter[reduced] += 1

            reduced_macro = contracted_macro(source, parent, leaf)
            expected_images = reduced_words_by_macro[reduced_macro]
            bad_multiplicities = {
                str(word): multiplicity
                for word, multiplicity in image_counter.items()
                if multiplicity != 1
            }
            missing = expected_images - set(image_counter)
            extra = set(image_counter) - expected_images
            if bad_multiplicities or missing or extra:
                failures.append(
                    {
                        "kind": "deletion is not a bijection",
                        "source": list(source),
                        "parent": parent,
                        "leaf": leaf,
                        "target": list(target),
                        "reduced_macro": list(reduced_macro),
                        "bad_multiplicities": bad_multiplicities,
                        "missing": [[list(edge) for edge in word] for word in sorted(missing)[:10]],
                        "extra": [[list(edge) for edge in word] for word in sorted(extra)[:10]],
                    }
                )
            records.append(
                {
                    "source": list(source),
                    "parent": parent,
                    "leaf": leaf,
                    "target": list(target),
                    "reduced_macro": list(reduced_macro),
                    "witness_positions": witness_count,
                    "contracted_factorizations": len(image_counter),
                    "expected_contracted_factorizations": len(expected_images),
                }
            )

    return {
        "n": n,
        "r": r,
        "claim_tested": (
            "Deleting the distinguished leaf factor bijects leaf-rotation "
            "special-pair witnesses with the contracted macro fiber."
        ),
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
    print(
        json.dumps(
            {
                "n": result["n"],
                "r": result["r"],
                "leaf_rotations": result["leaf_rotations"],
                "failure_count": len(result["failures"]),
                "first_failures": result["failures"][:3],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
