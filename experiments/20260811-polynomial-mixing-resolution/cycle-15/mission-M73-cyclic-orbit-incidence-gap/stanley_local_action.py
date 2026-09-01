#!/usr/bin/env python3
"""Exact audit of Stanley's local S_r action in factorization/tree coordinates."""

from __future__ import annotations

import argparse
import collections
import json
import platform
import subprocess
import sys
from pathlib import Path

from cyclic_tree_action import Edge, conjugate_edge, minimal_words, stanley_tree, transpositions


def parking_labels(n: int, raw_edges: tuple[Edge, ...]) -> tuple[int, ...]:
    blocks = [{i} for i in range(n)]
    labels = []
    for a, b in raw_edges:
        ia = next(i for i, block in enumerate(blocks) if a in block)
        ib = next(i for i, block in enumerate(blocks) if b in block)
        first, second = blocks[ia], blocks[ib]
        if min(first) > min(second):
            first, second = second, first
            ia, ib = ib, ia
        minimum_second = min(second)
        labels.append(max(x for x in first if x < minimum_second))
        merged = first | second
        blocks = [block for j, block in enumerate(blocks) if j not in (ia, ib)]
        blocks.append(merged)
    return tuple(labels)


def swap_tree_labels(tree: tuple[Edge, ...], first: int, second: int) -> tuple[Edge, ...]:
    def swap(value: int) -> int:
        return second if value == first else first if value == second else value

    return tuple(sorted(tuple(sorted((swap(a), swap(b)))) for a, b in tree))


def analyze(n: int) -> dict[str, object]:
    edges, gates = transpositions(n)
    edge_index = {edge: i for i, edge in enumerate(edges)}
    words = minimal_words(n, edges, gates)
    word_set = set(words)
    labels = {
        word: parking_labels(n, tuple(edges[index] for index in word))
        for word in words
    }
    trees = {
        word: stanley_tree(n, tuple(edges[index] for index in word))
        for word in words
    }

    def hurwitz(word: tuple[int, ...], i: int) -> tuple[int, ...]:
        changed = list(word)
        changed[i] = word[i + 1]
        changed[i + 1] = edge_index[
            conjugate_edge(edges[word[i]], edges[word[i + 1]])
        ]
        target = tuple(changed)
        if target not in word_set:
            raise AssertionError("Hurwitz move left state space")
        return target

    action_matches = 0
    action_total = 0
    fixed_special = 0
    swapped_nonspecial = 0
    first_action_failure = None
    heatbath_tree_distance = collections.Counter()
    special_to_nonspecial_distance = collections.Counter()
    nonspecial_swap_distance = collections.Counter()
    first_special_transition = None

    for word in words:
        for i in range(n - 2):
            fiber = []
            current = word
            while current not in fiber:
                fiber.append(current)
                current = hurwitz(current, i)
            source_labels = labels[word]
            swapped_labels = list(source_labels)
            swapped_labels[i], swapped_labels[i + 1] = swapped_labels[i + 1], swapped_labels[i]
            matches = [candidate for candidate in fiber if labels[candidate] == tuple(swapped_labels)]
            if len(matches) != 1:
                raise AssertionError("Stanley local action target was not unique")
            target = matches[0]
            predicted_tree = swap_tree_labels(trees[word], i + 1, i + 2)
            action_total += 1
            if trees[target] == predicted_tree:
                action_matches += 1
            elif first_action_failure is None:
                first_action_failure = {
                    "rank_zero_based": i,
                    "word": word,
                    "parking_labels": source_labels,
                    "action_target": target,
                    "source_tree": trees[word],
                    "target_tree": trees[target],
                    "predicted_label_swap_tree": predicted_tree,
                }
            if target == word:
                fixed_special += 1
            else:
                swapped_nonspecial += 1

            for candidate in fiber:
                if candidate == word:
                    continue
                distance = len(set(trees[word]) ^ set(trees[candidate])) // 2
                heatbath_tree_distance[distance] += 1
                if target == word:
                    special_to_nonspecial_distance[distance] += 1
                    if first_special_transition is None:
                        first_special_transition = {
                            "rank_zero_based": i,
                            "special_word": word,
                            "nonspecial_word": candidate,
                            "special_tree": trees[word],
                            "nonspecial_tree": trees[candidate],
                            "basis_distance": distance,
                        }
                elif candidate == target:
                    nonspecial_swap_distance[distance] += 1

    def serial(counter: collections.Counter[int]) -> dict[str, int]:
        return {str(key): counter[key] for key in sorted(counter)}

    return {
        "n": n,
        "states": len(words),
        "local_rank_sites": action_total,
        "Stanley_Sr_action_equals_swapping_tree_vertex_labels": action_matches == action_total,
        "action_match_count": action_matches,
        "fixed_special_count": fixed_special,
        "swapped_nonspecial_count": swapped_nonspecial,
        "first_action_failure": first_action_failure,
        "all_heatbath_tree_basis_distance": serial(heatbath_tree_distance),
        "special_to_nonspecial_tree_basis_distance": serial(special_to_nonspecial_distance),
        "nonspecial_action_swap_tree_basis_distance": serial(nonspecial_swap_distance),
        "first_special_transition": first_special_transition,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    parameters = sorted(set(args.n))
    payload = {
        "claim_tested": (
            "Stanley's local S_r action is ordinary swapping of the rank-labelled "
            "Cayley-tree vertices, and topology-changing heat-bath moves are local "
            "basis exchanges in these coordinates."
        ),
        "scope_warning": "Finite exact identities/failures do not establish an asymptotic gap.",
        "convention": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "parameters": parameters,
        "results": [analyze(n) for n in parameters],
        "python": platform.python_version(),
        "seed": None,
        "deterministic": True,
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": " ".join(sys.argv),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

