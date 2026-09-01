#!/usr/bin/env python3
"""Exact audit of the proposed leaf-rotation subchain.

A parking macro is represented by its multiplicity/Łukasiewicz vector m.
For every leaf that is not the last child of its parent in the preorder
plane tree, the proposed rotation moves the next sibling subtree below the
leaf, changing m to m-e_parent+e_leaf.  The script enumerates the exact
rank-two heat-bath witnesses and tests the conjectured closed count.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from collections import defaultdict
from pathlib import Path

import adjacent_bypass_probe as base


def counts_from_macro(macro: tuple[int, ...]) -> tuple[int, ...]:
    r = len(macro)
    return tuple(macro.count(i) for i in range(r))


def macro_from_counts(counts: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(i for i, count in enumerate(counts) for _ in range(count))


def preorder_children(degrees: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    """Return children of the unique preorder plane tree with these degrees."""
    r = len(degrees)
    # There are r+1 tree vertices; the last degree is forced to be zero.
    all_degrees = degrees + (0,)
    children: list[list[int]] = [[] for _ in range(r + 1)]
    stack: list[list[int]] = [[0, all_degrees[0]]]
    for vertex in range(1, r + 1):
        while stack and stack[-1][1] == 0:
            stack.pop()
        if not stack:
            raise AssertionError("invalid Lukasiewicz degree sequence")
        parent = stack[-1][0]
        children[parent].append(vertex)
        stack[-1][1] -= 1
        stack.append([vertex, all_degrees[vertex]])
    while stack and stack[-1][1] == 0:
        stack.pop()
    if stack:
        raise AssertionError("unfilled child slots")
    return tuple(tuple(row) for row in children)


def leaf_rotations(macro: tuple[int, ...]) -> list[tuple[int, int, tuple[int, ...]]]:
    degrees = counts_from_macro(macro)
    children = preorder_children(degrees)
    answer = []
    for parent, row in enumerate(children):
        for leaf in row[:-1]:
            if degrees[leaf] != 0:
                continue
            target_degrees = list(degrees)
            target_degrees[parent] -= 1
            target_degrees[leaf] += 1
            answer.append((parent, leaf, macro_from_counts(tuple(target_degrees))))
    return answer


def run(n: int, dump_witnesses: bool) -> dict:
    r = n - 1
    identity = tuple(range(n))
    cycle = tuple(list(range(1, n)) + [0])
    edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
    edge_index = {edge: i for i, edge in enumerate(edges)}
    perms = [base.transposition(n, edge) for edge in edges]
    pair_fibers = defaultdict(list)
    for first, p in enumerate(perms):
        for second, q in enumerate(perms):
            pair_fibers[base.compose(p, q)].append((first, second))

    words = []
    macro_words = defaultdict(list)
    for labels in itertools.product(range(r), repeat=r):
        if not base.is_parking_word(labels):
            continue
        word_edges = base.factor_word(base.inverse_chain(labels))
        word = tuple(edge_index[edge] for edge in word_edges)
        product = identity
        for index in word:
            product = base.compose(product, perms[index])
        if product != cycle:
            raise AssertionError("wrong endpoint")
        macro = tuple(sorted(labels))
        record = (labels, word_edges, word)
        words.append(record)
        macro_words[macro].append(record)

    if len(words) != n ** (n - 2):
        raise AssertionError("Dénes count failed")

    records = []
    failures = []
    coordinate_characterizations = []
    for source, source_words in sorted(macro_words.items()):
        for parent, leaf, target in leaf_rotations(source):
            witness_rows = []
            source_positions = defaultdict(list)
            for labels, word_edges, word in source_words:
                for pos in range(r - 1):
                    product = base.compose(perms[word[pos]], perms[word[pos + 1]])
                    favorable = []
                    for first, second in pair_fibers[product]:
                        target_word = word[:pos] + (first, second) + word[pos + 2 :]
                        target_macro = tuple(sorted(edges[index][0] for index in target_word))
                        if target_macro == target:
                            favorable.append((edges[first], edges[second]))
                    if favorable:
                        source_positions[labels].append(pos)
                        if dump_witnesses:
                            witness_rows.append(
                                {
                                    "labels": list(labels),
                                    "position": pos,
                                    "source_pair": [list(word_edges[pos]), list(word_edges[pos + 1])],
                                    "target_pairs": [
                                        [list(first), list(second)] for first, second in favorable
                                    ],
                                }
                            )
            raw_outcomes = sum(
                2 * len(positions) for positions in source_positions.values()
            )
            orbit = base.orbit_weight(source)
            expected = 2 * counts_from_macro(source)[parent] * orbit // r
            if raw_outcomes != expected:
                failures.append(
                    {
                        "source": list(source),
                        "target": list(target),
                        "parent": parent,
                        "leaf": leaf,
                        "observed": raw_outcomes,
                        "expected": expected,
                    }
                )

            witness_labels = set(source_positions)
            matching_coordinates = []
            for coordinate in range(r):
                candidate = {
                    labels for labels, _, _ in source_words if labels[coordinate] == parent
                }
                if candidate == witness_labels and all(
                    len(source_positions[labels]) == 1 for labels in witness_labels
                ):
                    matching_coordinates.append(coordinate)
            coordinate_characterizations.append(
                {
                    "source": list(source),
                    "target": list(target),
                    "parent": parent,
                    "leaf": leaf,
                    "matching_coordinates": matching_coordinates,
                }
            )
            record = {
                "source": list(source),
                "target": list(target),
                "degrees": list(counts_from_macro(source)),
                "parent": parent,
                "leaf": leaf,
                "orbit": orbit,
                "witness_sources": len(witness_labels),
                "raw_outcomes": raw_outcomes,
                "expected_raw_outcomes": expected,
                "matching_coordinates": matching_coordinates,
            }
            if dump_witnesses:
                record["witnesses"] = witness_rows
            records.append(record)

    return {
        "n": n,
        "r": r,
        "convention": "(pq)(x)=p(q(x)); tuple product left-to-right",
        "claim_tested": (
            "Every preorder leaf rotation is an actual macro edge with raw "
            "favorable-outcome count 2*m_parent*|O_m|/r."
        ),
        "universal_scope_warning": (
            "Enumeration can refute but cannot prove the universal count or gap."
        ),
        "parking_words": len(words),
        "macros": len(macro_words),
        "leaf_rotations": len(records),
        "count_failures": failures,
        "all_have_single_coordinate_characterization": all(
            row["matching_coordinates"] for row in coordinate_characterizations
        ),
        "records": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--dump-witnesses", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.n, args.dump_witnesses)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    summary = {key: value for key, value in result.items() if key != "records"}
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
