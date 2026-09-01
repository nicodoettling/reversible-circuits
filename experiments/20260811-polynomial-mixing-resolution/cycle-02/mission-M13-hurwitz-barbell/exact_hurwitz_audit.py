#!/usr/bin/env python3
"""Exact falsification harness for named minimal Hurwitz-orbit claims.

This is not a spectral-grid experiment.  It enumerates only the calibration
cases S_3,m=4; S_4,m=4; S_4,m=6 and tests:

* whether prefix join edges always form a spanning tree;
* whether the labeled join tree is uniformly distributed (finite falsifier);
* whether Dyck-path or join-tree statistics are exact Markov lumpings;
* whether one Hurwitz generator changes only one Dyck height and at most one
  join-tree edge;
* exact P_H stationary mass and full oriented-generator boundary flow for
  named Dyck/tree/Pruefer cuts.

Convention: p*q is p after q, (p*q)(x)=p(q(x)); a word is t_1*...*t_m.
The kernel is P_H=I/2+[1/(4(m-1))]sum_i(R_i+R_i^{-1}).
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import random
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable


Permutation = tuple[int, ...]
Word = tuple[int, ...]

EXPECTED = {
    (3, 4): (27, 24),
    (4, 4): (120, 0),
    (4, 6): (3936, 2880),
}


def all_transpositions(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def identity(n: int) -> Permutation:
    return tuple(range(n))


def right_multiply_transposition(p: Permutation, edge: tuple[int, int]) -> Permutation:
    """Return p*t, i.e. p after the transposition t."""
    a, b = edge
    q = list(p)
    q[a], q[b] = p[b], p[a]
    return tuple(q)


def eval_word(n: int, edges: list[tuple[int, int]], word: Iterable[int]) -> Permutation:
    p = identity(n)
    for edge_index in word:
        p = right_multiply_transposition(p, edges[edge_index])
    return p


def cycle_count(p: Permutation) -> int:
    seen = [False] * len(p)
    count = 0
    for start in range(len(p)):
        if seen[start]:
            continue
        count += 1
        x = start
        while not seen[x]:
            seen[x] = True
            x = p[x]
    return count


def is_full_support(n: int, edges: list[tuple[int, int]], word: Word) -> bool:
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for edge_index in word:
        union(*edges[edge_index])
    return len({find(v) for v in range(n)}) == 1


def enumerate_identity_words(n: int, m: int, edges: list[tuple[int, int]]) -> list[Word]:
    target = identity(n)
    return [
        word
        for word in itertools.product(range(len(edges)), repeat=m)
        if eval_word(n, edges, word) == target
    ]


def conjugate_edge_index(
    edges: list[tuple[int, int]],
    edge_to_index: dict[tuple[int, int], int],
    target_index: int,
    conjugator_index: int,
) -> int:
    """Index of b*a*b where a is target and b is conjugator."""
    a0, a1 = edges[target_index]
    b0, b1 = edges[conjugator_index]

    def apply_b(v: int) -> int:
        if v == b0:
            return b1
        if v == b1:
            return b0
        return v

    image = tuple(sorted((apply_b(a0), apply_b(a1))))
    return edge_to_index[image]


def hurwitz_right(
    word: Word,
    position: int,
    edges: list[tuple[int, int]],
    edge_to_index: dict[tuple[int, int], int],
) -> Word:
    a, b = word[position], word[position + 1]
    c = conjugate_edge_index(edges, edge_to_index, a, b)
    return word[:position] + (b, c) + word[position + 2 :]


def hurwitz_inverse(
    word: Word,
    position: int,
    edges: list[tuple[int, int]],
    edge_to_index: dict[tuple[int, int], int],
) -> Word:
    a, b = word[position], word[position + 1]
    c = conjugate_edge_index(edges, edge_to_index, b, a)
    return word[:position] + (c, a) + word[position + 2 :]


def prefix_heights(n: int, edges: list[tuple[int, int]], word: Word) -> tuple[int, ...]:
    p = identity(n)
    heights = [0]
    for edge_index in word:
        p = right_multiply_transposition(p, edges[edge_index])
        heights.append(n - cycle_count(p))
    return tuple(heights)


def tree_degrees(n: int, tree: tuple[int, ...], edges: list[tuple[int, int]]) -> tuple[int, ...]:
    degrees = [0] * n
    for edge_index in tree:
        a, b = edges[edge_index]
        degrees[a] += 1
        degrees[b] += 1
    return tuple(degrees)


def is_spanning_tree(n: int, tree: tuple[int, ...], edges: list[tuple[int, int]]) -> bool:
    if len(tree) != n - 1 or len(set(tree)) != n - 1:
        return False
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for edge_index in tree:
        a, b = edges[edge_index]
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra
    return len({find(v) for v in range(n)}) == 1


def prufer_code(n: int, tree: tuple[int, ...], edges: list[tuple[int, int]]) -> tuple[int, ...]:
    adjacency = [set() for _ in range(n)]
    for edge_index in tree:
        a, b = edges[edge_index]
        adjacency[a].add(b)
        adjacency[b].add(a)
    code: list[int] = []
    for _ in range(n - 2):
        leaf = min(v for v in range(n) if len(adjacency[v]) == 1)
        neighbor = next(iter(adjacency[leaf]))
        code.append(neighbor)
        adjacency[neighbor].remove(leaf)
        adjacency[leaf].clear()
    return tuple(code)


def statistics(n: int, edges: list[tuple[int, int]], word: Word) -> dict[str, object]:
    heights = prefix_heights(n, edges, word)
    steps = tuple(heights[j + 1] - heights[j] for j in range(len(word)))
    assert all(step in (-1, 1) for step in steps)
    assert min(heights) >= 0 and heights[-1] == 0
    join_positions = tuple(j for j, step in enumerate(steps) if step == 1)
    join_tree = tuple(sorted(word[j] for j in join_positions))
    minimal_full = len(word) == 2 * (n - 1) and is_full_support(n, edges, word)
    if minimal_full:
        assert len(join_positions) == n - 1
        assert is_spanning_tree(n, join_tree, edges)
    degrees = tree_degrees(n, join_tree, edges)
    prufer = prufer_code(n, join_tree, edges) if minimal_full else ()
    dyck_word = "".join("J" if step == 1 else "C" for step in steps)
    return {
        "heights": heights,
        "dyck_word": dyck_word,
        "dyck_area": sum(heights[:-1]),
        "dyck_max": max(heights),
        "dyck_peaks": sum(
            steps[j] == 1 and steps[j + 1] == -1 for j in range(len(steps) - 1)
        ),
        "join_positions": join_positions,
        "join_tree": join_tree,
        "join_degrees": degrees,
        "join_degree_profile": tuple(sorted(degrees, reverse=True)),
        "join_max_degree": max(degrees),
        "join_leaves": sum(degree == 1 for degree in degrees),
        "join_tree_star": max(degrees) == n - 1,
        "join_tree_path": max(degrees) <= 2,
        "prufer": prufer,
        "prufer_first": prufer[0] if prufer else -1,
        "fixed_join_edge_12": edges.index((0, 1)) in join_tree,
    }


def fraction_record(value: Fraction) -> dict[str, object]:
    return {"exact": f"{value.numerator}/{value.denominator}", "decimal": float(value)}


def tree_label(tree: tuple[int, ...], edges: list[tuple[int, int]]) -> str:
    return " ".join(f"{edges[e][0]+1}-{edges[e][1]+1}" for e in tree)


def stat_serial(value: object, edges: list[tuple[int, int]]) -> object:
    if isinstance(value, tuple):
        return list(value)
    return value


def named_cuts(
    n: int, stat_cache: dict[Word, dict[str, object]]
) -> list[tuple[str, Callable[[dict[str, object]], bool]]]:
    cuts: list[tuple[str, Callable[[dict[str, object]], bool]]] = []
    for name in ("dyck_area", "dyck_max", "dyck_peaks", "join_max_degree", "join_leaves"):
        values = sorted({int(stat[name]) for stat in stat_cache.values()})
        for threshold in values[:-1]:
            cuts.append(
                (
                    f"{name}_le_{threshold}",
                    lambda stat, name=name, threshold=threshold: int(stat[name]) <= threshold,
                )
            )
    cuts.extend(
        [
            ("join_tree_star", lambda stat: bool(stat["join_tree_star"])),
            ("join_tree_path", lambda stat: bool(stat["join_tree_path"])),
            ("fixed_join_edge_12", lambda stat: bool(stat["fixed_join_edge_12"])),
            (
                "prufer_first_in_first_half",
                lambda stat, n=n: int(stat["prufer_first"]) < n // 2,
            ),
        ]
    )
    return cuts


def transition_signature(
    word: Word,
    stat_name: str,
    transitions: dict[Word, tuple[Word, ...]],
    stat_cache: dict[Word, dict[str, object]],
) -> tuple[tuple[str, int], ...]:
    counts = Counter(repr(stat_cache[new_word][stat_name]) for new_word in transitions[word])
    return tuple(sorted(counts.items()))


def audit_case(n: int, m: int) -> dict[str, object]:
    edges = all_transpositions(n)
    edge_to_index = {edge: index for index, edge in enumerate(edges)}
    words = enumerate_identity_words(n, m, edges)
    full_words = [word for word in words if is_full_support(n, edges, word)]
    expected_total, expected_full = EXPECTED[(n, m)]
    assert len(words) == expected_total
    assert len(full_words) == expected_full
    result: dict[str, object] = {
        "N": n,
        "m": m,
        "M": len(edges),
        "identity_words": len(words),
        "minimal_full_support_words": len(full_words),
    }
    if not full_words:
        result["note"] = "Full support is infeasible because m<2(N-1)."
        return result

    full_set = set(full_words)
    stat_cache = {word: statistics(n, edges, word) for word in full_words}
    tree_counts = Counter(stat["join_tree"] for stat in stat_cache.values())
    dyck_counts = Counter(str(stat["dyck_word"]) for stat in stat_cache.values())
    shape_counts = Counter(stat["join_degree_profile"] for stat in stat_cache.values())
    prufer_first_counts = Counter(int(stat["prufer_first"]) for stat in stat_cache.values())

    transitions: dict[Word, tuple[Word, ...]] = {}
    identity_violations = 0
    fiber_violations = 0
    inverse_violations = 0
    height_locality_violations = 0
    height_change_values: Counter[int] = Counter()
    max_tree_symmetric_difference = 0
    tree_one_exchange_violations = 0
    explicit_local_witness: dict[str, object] | None = None

    for word in full_words:
        destinations: list[Word] = []
        old_stat = stat_cache[word]
        old_heights = old_stat["heights"]
        old_tree = set(old_stat["join_tree"])
        for position in range(m - 1):
            right = hurwitz_right(word, position, edges, edge_to_index)
            inverse = hurwitz_inverse(word, position, edges, edge_to_index)
            if hurwitz_inverse(right, position, edges, edge_to_index) != word:
                inverse_violations += 1
            if hurwitz_right(inverse, position, edges, edge_to_index) != word:
                inverse_violations += 1
            for direction, new_word in (("R", right), ("Rinv", inverse)):
                destinations.append(new_word)
                if eval_word(n, edges, new_word) != identity(n):
                    identity_violations += 1
                if new_word not in full_set:
                    fiber_violations += 1
                    continue
                new_stat = stat_cache[new_word]
                changed_height_indices = [
                    j
                    for j, (old, new) in enumerate(zip(old_heights, new_stat["heights"]))
                    if old != new
                ]
                if any(j != position + 1 for j in changed_height_indices):
                    height_locality_violations += 1
                middle_change = int(new_stat["heights"][position + 1]) - int(
                    old_heights[position + 1]
                )
                height_change_values[middle_change] += 1
                new_tree = set(new_stat["join_tree"])
                symmetric_difference = len(old_tree.symmetric_difference(new_tree))
                max_tree_symmetric_difference = max(
                    max_tree_symmetric_difference, symmetric_difference
                )
                if symmetric_difference > 2:
                    tree_one_exchange_violations += 1
                if middle_change and explicit_local_witness is None:
                    explicit_local_witness = {
                        "old_word_edge_indices": list(word),
                        "new_word_edge_indices": list(new_word),
                        "old_word_edges": [
                            [edges[e][0] + 1, edges[e][1] + 1] for e in word
                        ],
                        "new_word_edges": [
                            [edges[e][0] + 1, edges[e][1] + 1] for e in new_word
                        ],
                        "position_1_based": position + 1,
                        "direction": direction,
                        "old_dyck_word": old_stat["dyck_word"],
                        "new_dyck_word": new_stat["dyck_word"],
                        "middle_height_change": middle_change,
                        "old_join_tree": tree_label(tuple(sorted(old_tree)), edges),
                        "new_join_tree": tree_label(tuple(sorted(new_tree)), edges),
                    }
        transitions[word] = tuple(destinations)

    assert identity_violations == 0
    assert fiber_violations == 0
    assert inverse_violations == 0
    assert height_locality_violations == 0
    assert set(height_change_values).issubset({-2, 0, 2})
    assert tree_one_exchange_violations == 0

    lumpability: dict[str, object] = {}
    for stat_name in ("dyck_word", "join_tree", "join_degree_profile", "prufer_first"):
        grouped: dict[str, list[tuple[tuple[str, int], ...]]] = defaultdict(list)
        grouped_words: dict[str, list[Word]] = defaultdict(list)
        for word in full_words:
            key = repr(stat_cache[word][stat_name])
            grouped[key].append(
                transition_signature(word, stat_name, transitions, stat_cache)
            )
            grouped_words[key].append(word)
        witness = None
        for key, signatures in grouped.items():
            first = signatures[0]
            for index, signature in enumerate(signatures[1:], start=1):
                if signature != first:
                    witness = {
                        "source_statistic": key,
                        "word_1_edge_indices": list(grouped_words[key][0]),
                        "word_2_edge_indices": list(grouped_words[key][index]),
                        "generator_destination_counts_1": [list(item) for item in first],
                        "generator_destination_counts_2": [list(item) for item in signature],
                    }
                    break
            if witness is not None:
                break
        lumpability[stat_name] = {
            "is_exact_markov_lumping_in_this_case": witness is None,
            "counterexample": witness,
        }

    cuts = named_cuts(n, stat_cache)
    cut_records: list[dict[str, object]] = []
    for cut_name, predicate in cuts:
        membership = {word: predicate(stat_cache[word]) for word in full_words}
        size_a = sum(membership.values())
        size_b = len(full_words) - size_a
        if size_a == 0 or size_b == 0:
            continue
        cross_a_to_b = 0
        cross_b_to_a = 0
        boundary_sources_a = 0
        outward_counts_a: list[int] = []
        for word in full_words:
            outward = 0
            for new_word in transitions[word]:
                if membership[word] and not membership[new_word]:
                    cross_a_to_b += 1
                    outward += 1
                elif not membership[word] and membership[new_word]:
                    cross_b_to_a += 1
            if membership[word]:
                outward_counts_a.append(outward)
                if outward:
                    boundary_sources_a += 1
        assert cross_a_to_b == cross_b_to_a
        denominator = 4 * (m - 1)
        flow = Fraction(cross_a_to_b, len(full_words) * denominator)
        conductance = Fraction(cross_a_to_b, denominator * min(size_a, size_b))
        rayleigh = Fraction(
            cross_a_to_b * len(full_words), denominator * size_a * size_b
        )
        cut_records.append(
            {
                "cut": cut_name,
                "size_A": size_a,
                "size_Ac": size_b,
                "pi_A": fraction_record(Fraction(size_a, len(full_words))),
                "oriented_generator_crossings_A_to_Ac": cross_a_to_b,
                "oriented_generator_crossings_Ac_to_A": cross_b_to_a,
                "P_H_stationary_boundary_flow": fraction_record(flow),
                "conductance_using_smaller_side": fraction_record(conductance),
                "indicator_rayleigh_quotient": fraction_record(rayleigh),
                "boundary_sources_in_A": boundary_sources_a,
                "minimum_outward_generator_count_over_A": min(outward_counts_a),
                "maximum_outward_generator_count_over_A": max(outward_counts_a),
                "single_oriented_generator_probability": fraction_record(
                    Fraction(1, denominator)
                ),
            }
        )

    tree_count_values = list(tree_counts.values())
    result.update(
        {
            "kernel": {
                "holding_coefficient": "1/2",
                "oriented_generator_probability": f"1/{4*(m-1)}",
                "oriented_generators_per_state": 2 * (m - 1),
            },
            "join_tree_check": {
                "all_join_sets_are_spanning_trees": True,
                "number_distinct_labeled_trees": len(tree_counts),
                "cayley_tree_count": n ** (n - 2),
                "minimum_words_per_labeled_tree": min(tree_count_values),
                "maximum_words_per_labeled_tree": max(tree_count_values),
                "uniform_labeled_join_tree_in_this_case": len(set(tree_count_values)) == 1,
                "counts": {
                    tree_label(tree, edges): count
                    for tree, count in sorted(
                        tree_counts.items(), key=lambda item: tree_label(item[0], edges)
                    )
                },
            },
            "tree_shape_distribution": {
                repr(profile): count for profile, count in sorted(shape_counts.items())
            },
            "prufer_first_distribution": {
                str(value + 1): count for value, count in sorted(prufer_first_counts.items())
            },
            "dyck_word_distribution": dict(sorted(dyck_counts.items())),
            "local_move_check": {
                "identity_violations": identity_violations,
                "full_support_fiber_violations": fiber_violations,
                "inverse_violations": inverse_violations,
                "height_locality_violations": height_locality_violations,
                "middle_height_change_counts": {
                    str(value): count for value, count in sorted(height_change_values.items())
                },
                "maximum_join_tree_symmetric_difference": max_tree_symmetric_difference,
                "one_tree_edge_exchange_violations": tree_one_exchange_violations,
                "explicit_peak_valley_witness": explicit_local_witness,
            },
            "lumpability_tests": lumpability,
            "candidate_cut_flows": cut_records,
        }
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=130113)
    parser.add_argument(
        "--commit", default="502a6f031c6d5a4bc0064ee5b370a4fa3914f993"
    )
    args = parser.parse_args()
    random.seed(args.seed)
    result = {
        "purpose": (
            "Exact finite falsification of named minimal Hurwitz join-tree/Dyck "
            "claims; never an asymptotic gap inference."
        ),
        "target": "uniform minimal full-support identity-transposition Hurwitz orbit",
        "kernel": "P_H=I/2+[1/(4(m-1))]sum_i(R_i+R_i^{-1})",
        "permutation_convention": "pq=p after q; word=t_1...t_m",
        "reproduction_command": (
            "python3 exact_hurwitz_audit.py --output results.json --seed 130113"
        ),
        "repository_commit": args.commit,
        "seed": args.seed,
        "stochastic": False,
        "python_version": sys.version,
        "platform": platform.platform(),
        "nonstandard_dependencies": [],
        "claim_map": {
            "join_tree_check": (
                "Could falsify the universal join-edge spanning-tree lemma and "
                "the conjecture that the labeled join tree is uniform."
            ),
            "local_move_check": (
                "Could falsify the universal one-middle-height and one-tree-edge "
                "locality lemmas."
            ),
            "lumpability_tests": (
                "A displayed counterexample rigorously refutes exact Markov "
                "lumpability for that statistic in the stated finite case."
            ),
            "candidate_cut_flows": (
                "Audits every P_H coefficient and full boundary in calibration "
                "cases only; it proves no asymptotic conductance bound."
            ),
        },
        "cases": [audit_case(3, 4), audit_case(4, 4), audit_case(4, 6)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
