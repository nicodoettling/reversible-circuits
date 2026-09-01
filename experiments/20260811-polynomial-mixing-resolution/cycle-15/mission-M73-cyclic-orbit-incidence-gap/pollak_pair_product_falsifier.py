#!/usr/bin/env python3
"""Exact falsifier for local Pollak-coordinate determination of pair products.

Stanley's labels of a reduced long-cycle factorization are its raw lower
transposition endpoints and form a zero-based parking function.  This script
tests whether increasingly strong local data from a paired label coordinate
determine the theta orbit of the pair product.

Convention: (pq)(x)=p(q(x)); factor tuples multiply left-to-right.
"""

from __future__ import annotations

import argparse
import collections
import json
import platform
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
M70 = HERE.parent / "mission-M70-long-cycle-exceptional-closure-gap"
sys.path.insert(0, str(M70))

from n7_exceptional_krylov import (  # noqa: E402
    compose,
    evaluate,
    long_cycle,
    minimal_words,
    transpositions,
)


Perm = tuple[int, ...]


def inverse(p: Perm) -> Perm:
    answer = [0] * len(p)
    for x, y in enumerate(p):
        answer[y] = x
    return tuple(answer)


def theta(p: Perm, h: Perm, h_inverse: Perm) -> Perm:
    return compose(h_inverse, compose(p, h))


def canonical_theta_orbit(p: Perm, h: Perm, h_inverse: Perm) -> Perm:
    orbit = []
    current = p
    while current not in orbit:
        orbit.append(current)
        current = theta(current, h, h_inverse)
    if current != p:
        raise AssertionError("theta trajectory did not close at its source")
    return min(orbit)


def cyclic_conjugate_word(
    word: tuple[int, ...], edges: list[tuple[int, int]], edge_index: dict[tuple[int, int], int], n: int
) -> tuple[int, ...]:
    return tuple(
        edge_index[tuple(sorted(((edges[index][0] - 1) % n, (edges[index][1] - 1) % n)))]
        for index in word
    )


def first_collision(
    observations: list[dict[str, object]], key_name: str
) -> tuple[dict[str, object] | None, int, int]:
    first: dict[object, tuple[object, dict[str, object]]] = {}
    ambiguous_keys = set()
    orbit_sets: dict[object, set[object]] = collections.defaultdict(set)
    witness = None
    for observation in observations:
        key = observation[key_name]
        target = observation["product_theta_orbit"]
        orbit_sets[key].add(target)
        if key not in first:
            first[key] = (target, observation)
        elif first[key][0] != target and witness is None:
            witness = {
                "metadata_key": key,
                "first": first[key][1],
                "second": observation,
            }
        if len(orbit_sets[key]) > 1:
            ambiguous_keys.add(key)
    return witness, len(ambiguous_keys), max(map(len, orbit_sets.values()))


def analyze(n: int) -> dict[str, object]:
    edges, gates = transpositions(n)
    edge_index = {edge: index for index, edge in enumerate(edges)}
    words = minimal_words(n, edges, gates)
    word_set = set(words)
    h = long_cycle(n)
    h_inverse = inverse(h)
    if any(evaluate(word, gates, n) != h for word in words):
        raise AssertionError("enumerator produced a wrong endpoint")

    diagonal_translation_matches = 0
    diagonal_translation_unique_shifts = collections.Counter()
    first_nontranslation = None
    for word in words:
        target = cyclic_conjugate_word(word, edges, edge_index, n)
        if target not in word_set:
            raise AssertionError("U left the fixed endpoint space")
        labels = tuple(edges[index][0] for index in word)
        target_labels = tuple(edges[index][0] for index in target)
        shifts = [
            shift
            for shift in range(n)
            if tuple((value + shift) % n for value in labels) == target_labels
        ]
        diagonal_translation_unique_shifts[len(shifts)] += 1
        if shifts:
            diagonal_translation_matches += 1
        elif first_nontranslation is None:
            first_nontranslation = {
                "source_word_edges": [edges[index] for index in word],
                "source_parking_labels": labels,
                "U_word_edges": [edges[index] for index in target],
                "U_parking_labels": target_labels,
            }

    pair_records = []
    for pair_position in range((n - 1) // 2):
        observations = []
        first_position = 2 * pair_position
        second_position = first_position + 1
        for word in words:
            labels = tuple(edges[index][0] for index in word)
            counts = collections.Counter(labels)
            first_label = labels[first_position]
            second_label = labels[second_position]
            first_occurrence_rank = 1 + sum(
                labels[position] == first_label for position in range(first_position)
            )
            second_occurrence_rank = 1 + sum(
                labels[position] == second_label for position in range(second_position)
            )
            product = compose(gates[word[first_position]], gates[word[second_position]])
            product_orbit = canonical_theta_orbit(product, h, h_inverse)
            multiplicity_vector = tuple(counts[value] for value in range(n))
            observation = {
                "word_edges": tuple(edges[index] for index in word),
                "parking_labels": labels,
                "pair_position": pair_position,
                "pair_edges": (
                    edges[word[first_position]],
                    edges[word[second_position]],
                ),
                "pair_product": product,
                "product_theta_orbit": product_orbit,
                # The orbit of an ordered pair under diagonal translation is
                # equivalent to its directed difference.
                "directed_difference_mod_n": (first_label - second_label) % n,
                "ordered_pair_mod_diagonal": (
                    0,
                    (second_label - first_label) % n,
                ),
                "ordered_pair_absolute": (first_label, second_label),
                "pair_plus_local_multiplicities": (
                    first_label,
                    second_label,
                    counts[first_label],
                    counts[second_label],
                ),
                "pair_plus_multiplicities_and_occurrence_ranks": (
                    first_label,
                    second_label,
                    counts[first_label],
                    counts[second_label],
                    first_occurrence_rank,
                    second_occurrence_rank,
                ),
                # This strictly strengthens every local multiplicity proposal:
                # retain the full parking multiplicity vector as well.
                "pair_plus_full_multiplicity_vector_and_occurrence_ranks": (
                    first_label,
                    second_label,
                    multiplicity_vector,
                    first_occurrence_rank,
                    second_occurrence_rank,
                ),
            }
            observations.append(observation)

        tests = []
        for key_name in (
            "directed_difference_mod_n",
            "ordered_pair_mod_diagonal",
            "ordered_pair_absolute",
            "pair_plus_local_multiplicities",
            "pair_plus_multiplicities_and_occurrence_ranks",
            "pair_plus_full_multiplicity_vector_and_occurrence_ranks",
        ):
            witness, ambiguous, maximum = first_collision(observations, key_name)
            tests.append({
                "metadata": key_name,
                "determines_product_theta_orbit": witness is None,
                "ambiguous_metadata_keys": ambiguous,
                "maximum_product_orbits_for_one_metadata_key": maximum,
                "first_collision": witness,
            })
        pair_records.append({
            "pair_position_zero_based": pair_position,
            "observations": len(observations),
            "tests": tests,
        })

    return {
        "n": n,
        "states": len(words),
        "expected_states": n ** (n - 2),
        "U_parking_labels_equal_some_diagonal_translation_count": (
            diagonal_translation_matches
        ),
        "U_parking_label_diagonal_translation_match_multiplicity": {
            str(key): value
            for key, value in sorted(diagonal_translation_unique_shifts.items())
        },
        "first_U_not_diagonal_translation_witness": first_nontranslation,
        "fixed_pair_position_tests": pair_records,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    parameters = sorted(set(args.n))
    payload = {
        "claim_tested": (
            "A pair-product theta orbit is determined by the two Stanley/Pollak "
            "lower-endpoint coordinates modulo diagonal translation, possibly "
            "augmented by multiplicities and occurrence ranks."
        ),
        "convention": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "scope_warning": (
            "One exact collision refutes a universal deterministic shortcut; "
            "finite collision frequencies are not asymptotic statements."
        ),
        "parameters": parameters,
        "results": [analyze(n) for n in parameters],
        "python": platform.python_version(),
        "seed": None,
        "deterministic": True,
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": " ".join(sys.argv),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    summary = []
    for result in payload["results"]:
        summary.append({
            "n": result["n"],
            "U_diagonal_translation_matches": (
                result["U_parking_labels_equal_some_diagonal_translation_count"]
            ),
            "pair_tests": [
                {
                    "pair_position": record["pair_position_zero_based"],
                    "determination": {
                        test["metadata"]: test["determines_product_theta_orbit"]
                        for test in record["tests"]
                    },
                }
                for record in result["fixed_pair_position_tests"]
            ],
        })
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
