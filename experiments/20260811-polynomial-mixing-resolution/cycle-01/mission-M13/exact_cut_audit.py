#!/usr/bin/env python3
"""Exact falsification audit for named full-support statistics.

This is deliberately not a spectral-grid program.  It enumerates the three
project smoke cases, restricts the exact K_{N,m} kernel to the all-label
connected-support fiber, and computes exact stationary flow only for named
candidate cuts:

* midpoint transposition distance;
* maximum prefix distance;
* number of distinct support edges;
* number of adjacent repeats;
* the adjacent-doubled-tree normal-form family;
* the minimal-bridge midpoint-N-cycle ("mountain") family.

Permutation convention: p*q is p after q, (p*q)(x)=p(q(x)).  A word is
evaluated as t_1*...*t_m by repeated right multiplication.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
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


def right_multiply_transposition(p: Permutation, t: tuple[int, int]) -> Permutation:
    """Return p*t, i.e. p after t."""
    a, b = t
    q = list(p)
    q[a], q[b] = p[b], p[a]
    return tuple(q)


def eval_word(n: int, transpositions: list[tuple[int, int]], word: Iterable[int]) -> Permutation:
    p = identity(n)
    for edge_index in word:
        p = right_multiply_transposition(p, transpositions[edge_index])
    return p


def transposition_distance(p: Permutation) -> int:
    seen = [False] * len(p)
    cycles = 0
    for start in range(len(p)):
        if seen[start]:
            continue
        cycles += 1
        x = start
        while not seen[x]:
            seen[x] = True
            x = p[x]
    return len(p) - cycles


def is_full_support(n: int, transpositions: list[tuple[int, int]], word: Word) -> bool:
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
        union(*transpositions[edge_index])
    return len({find(v) for v in range(n)}) == 1


def prefix_distances(n: int, transpositions: list[tuple[int, int]], word: Word) -> list[int]:
    p = identity(n)
    result = [0]
    for edge_index in word:
        p = right_multiply_transposition(p, transpositions[edge_index])
        result.append(transposition_distance(p))
    return result


def aligned_doubled_tree(n: int, transpositions: list[tuple[int, int]], word: Word) -> bool:
    if len(word) != 2 * (n - 1):
        return False
    paired = [word[2 * j] for j in range(n - 1)]
    if any(word[2 * j] != word[2 * j + 1] for j in range(n - 1)):
        return False
    return len(set(paired)) == n - 1 and is_full_support(n, transpositions, word)


def statistics(n: int, transpositions: list[tuple[int, int]], word: Word) -> dict[str, object]:
    distances = prefix_distances(n, transpositions, word)
    counts = Counter(word)
    edge_parity = tuple(sorted(edge for edge, multiplicity in counts.items() if multiplicity % 2))
    degrees = [0] * n
    for edge_index, multiplicity in counts.items():
        a, b = transpositions[edge_index]
        degrees[a] += multiplicity
        degrees[b] += multiplicity
    degree_parity = tuple(v for v, degree in enumerate(degrees) if degree % 2)
    midpoint_distance = distances[len(word) // 2]
    return {
        "midpoint_distance": midpoint_distance,
        "max_prefix_distance": max(distances),
        "distinct_edges": len(counts),
        "adjacent_repeats": sum(word[j] == word[j + 1] for j in range(len(word) - 1)),
        "aligned_doubled_tree": aligned_doubled_tree(n, transpositions, word),
        "mountain": len(word) == 2 * (n - 1) and midpoint_distance == n - 1,
        "edge_parity": edge_parity,
        "degree_parity": degree_parity,
    }


def enumerate_identity_words(n: int, m: int, transpositions: list[tuple[int, int]]) -> list[Word]:
    target = identity(n)
    return [
        word
        for word in itertools.product(range(len(transpositions)), repeat=m)
        if eval_word(n, transpositions, word) == target
    ]


def block_fibers(
    n: int, transpositions: list[tuple[int, int]], block_lengths: Iterable[int]
) -> dict[int, dict[Permutation, tuple[Word, ...]]]:
    answer: dict[int, dict[Permutation, tuple[Word, ...]]] = {}
    for r in block_lengths:
        temporary: dict[Permutation, list[Word]] = defaultdict(list)
        for block in itertools.product(range(len(transpositions)), repeat=r):
            temporary[eval_word(n, transpositions, block)].append(block)
        answer[r] = {product: tuple(words) for product, words in temporary.items()}
    return answer


def fraction_record(value: Fraction) -> dict[str, object]:
    return {
        "exact": f"{value.numerator}/{value.denominator}",
        "decimal": float(value),
    }


def word_labels(word: Word, transpositions: list[tuple[int, int]]) -> list[list[int]]:
    return [[transpositions[index][0] + 1, transpositions[index][1] + 1] for index in word]


def crossing_window_count(m: int, r: int, cut: int) -> int:
    """Positions and cut are 1-based: window i..i+r-1 crosses cut k|k+1."""
    lo = max(1, cut - r + 2)
    hi = min(cut, m - r + 1)
    return max(0, hi - lo + 1)


def audit_case(n: int, m: int) -> dict[str, object]:
    transpositions = all_transpositions(n)
    M = len(transpositions)
    R = tuple(r for r in (3, 4, 5) if r <= m)
    words = enumerate_identity_words(n, m, transpositions)
    full_words = [word for word in words if is_full_support(n, transpositions, word)]
    expected_total, expected_full = EXPECTED[(n, m)]
    assert len(words) == expected_total
    assert len(full_words) == expected_full

    base: dict[str, object] = {
        "N": n,
        "m": m,
        "M": M,
        "R_m": list(R),
        "identity_words": len(words),
        "full_support_words": len(full_words),
    }
    if not full_words:
        base["note"] = "The all-label connected-support fiber is empty by m < 2(N-1)."
        return base

    fibers = block_fibers(n, transpositions, R)
    fiber_sizes = {
        str(r): {
            "minimum": min(len(options) for options in fibers[r].values()),
            "maximum": max(len(options) for options in fibers[r].values()),
            "product_count": len(fibers[r]),
            "prefix_bound_M_power_r_minus_1": M ** (r - 1),
        }
        for r in R
    }

    full_set = set(full_words)
    stat_cache = {word: statistics(n, transpositions, word) for word in full_words}
    scalar_names = (
        "midpoint_distance",
        "max_prefix_distance",
        "distinct_edges",
        "adjacent_repeats",
    )
    distributions = {
        name: dict(
            sorted(
                Counter(str(stat_cache[word][name]) for word in full_words).items(),
                key=lambda item: int(item[0]),
            )
        )
        for name in scalar_names
    }
    distributions["aligned_doubled_tree"] = dict(
        sorted(Counter(str(stat_cache[word]["aligned_doubled_tree"]).lower() for word in full_words).items())
    )
    distributions["mountain"] = dict(
        sorted(Counter(str(stat_cache[word]["mountain"]).lower() for word in full_words).items())
    )

    cuts: list[tuple[str, Callable[[dict[str, object]], bool]]] = []
    for name in scalar_names:
        values = sorted({int(stat_cache[word][name]) for word in full_words})
        for threshold in values[:-1]:
            cuts.append(
                (
                    f"{name}_le_{threshold}",
                    lambda stat, name=name, threshold=threshold: int(stat[name]) <= threshold,
                )
            )
    cuts.append(("aligned_doubled_tree", lambda stat: bool(stat["aligned_doubled_tree"])))
    cuts.append(("mountain", lambda stat: bool(stat["mountain"])))
    cut_membership = {
        name: {word: predicate(stat_cache[word]) for word in full_words}
        for name, predicate in cuts
    }
    cut_sizes = {
        name: sum(membership.values()) for name, membership in cut_membership.items()
    }

    # Boundary terms are grouped by their exact one-step denominator to avoid
    # doing millions of Fraction additions in the inner loop.
    boundary_a_to_b: dict[str, Counter[int]] = {name: Counter() for name, _ in cuts}
    boundary_b_to_a: dict[str, Counter[int]] = {name: Counter() for name, _ in cuts}
    exit_terms_by_word: dict[Word, Counter[int]] = {word: Counter() for word in full_words}
    prefix_cut = m // 2
    prefix_locality_violations = 0
    transition_checks = 0
    witnesses: dict[str, dict[str, object]] = {}

    for word in full_words:
        old_stat = stat_cache[word]
        old_prefix = eval_word(n, transpositions, word[:prefix_cut])
        for r in R:
            window_count = m - r + 1
            for start0 in range(window_count):
                old_block = word[start0 : start0 + r]
                product = eval_word(n, transpositions, old_block)
                options = fibers[r][product]
                denominator = 2 * len(R) * window_count * len(options)
                crosses_prefix = start0 < prefix_cut < start0 + r
                for new_block in options:
                    transition_checks += 1
                    new_word = word[:start0] + new_block + word[start0 + r :]
                    new_prefix = eval_word(n, transpositions, new_word[:prefix_cut])
                    if new_prefix != old_prefix and not crosses_prefix:
                        prefix_locality_violations += 1
                    if new_word not in full_set:
                        # This transition becomes holding mass in the restricted
                        # full-support kernel.
                        exit_terms_by_word[word][denominator] += 1
                        continue
                    new_stat = stat_cache[new_word]
                    for cut_name, _ in cuts:
                        old_side = cut_membership[cut_name][word]
                        new_side = cut_membership[cut_name][new_word]
                        if old_side and not new_side:
                            boundary_a_to_b[cut_name][denominator] += 1
                        elif not old_side and new_side:
                            boundary_b_to_a[cut_name][denominator] += 1

                    candidate_changes = {
                        "midpoint_distance_changes": old_stat["midpoint_distance"]
                        != new_stat["midpoint_distance"],
                        "distinct_edge_count_changes": old_stat["distinct_edges"]
                        != new_stat["distinct_edges"],
                        "edge_multiplicity_parity_changes": old_stat["edge_parity"]
                        != new_stat["edge_parity"],
                        "vertex_degree_parity_changes": old_stat["degree_parity"]
                        != new_stat["degree_parity"],
                        "leaves_aligned_doubled_tree": bool(old_stat["aligned_doubled_tree"])
                        and not bool(new_stat["aligned_doubled_tree"]),
                    }
                    for witness_name, changed in candidate_changes.items():
                        if changed and witness_name not in witnesses:
                            witnesses[witness_name] = {
                                "old_word": word_labels(word, transpositions),
                                "new_word": word_labels(new_word, transpositions),
                                "block_length": r,
                                "window_start_1_based": start0 + 1,
                                "single_option_probability_contribution": fraction_record(
                                    Fraction(1, denominator)
                                ),
                                "old_stat": {
                                    key: list(value) if isinstance(value, tuple) else value
                                    for key, value in old_stat.items()
                                },
                                "new_stat": {
                                    key: list(value) if isinstance(value, tuple) else value
                                    for key, value in new_stat.items()
                                },
                            }

    assert prefix_locality_violations == 0
    cut_records = []
    for cut_name, _ in cuts:
        size_a = cut_sizes[cut_name]
        size_b = len(full_words) - size_a
        if size_a == 0 or size_b == 0:
            continue
        flow_sum_a = sum(
            (Fraction(count, denominator) for denominator, count in boundary_a_to_b[cut_name].items()),
            Fraction(0),
        )
        flow_sum_b = sum(
            (Fraction(count, denominator) for denominator, count in boundary_b_to_a[cut_name].items()),
            Fraction(0),
        )
        assert flow_sum_a == flow_sum_b, (cut_name, flow_sum_a, flow_sum_b)
        stationary_flow = flow_sum_a / len(full_words)
        conductance = flow_sum_a / min(size_a, size_b)
        rayleigh = flow_sum_a * len(full_words) / (size_a * size_b)
        cut_records.append(
            {
                "cut": cut_name,
                "size_A": size_a,
                "size_Ac": size_b,
                "pi_A": fraction_record(Fraction(size_a, len(full_words))),
                "stationary_boundary_flow": fraction_record(stationary_flow),
                "conductance_using_smaller_side": fraction_record(conductance),
                "indicator_rayleigh_quotient": fraction_record(rayleigh),
            }
        )

    crossing_counts = {str(r): crossing_window_count(m, r, prefix_cut) for r in R}
    selected_crossing_probability = sum(
        (
            Fraction(crossing_counts[str(r)], 2 * len(R) * (m - r + 1))
            for r in R
        ),
        Fraction(0),
    )
    first_position_refresh_probability = sum(
        (Fraction(1, 2 * len(R) * (m - r + 1)) for r in R),
        Fraction(0),
    )

    # Stress-test the unqualified q_lift=1 inequality.  Let b(x) be the
    # one-step probability of exiting the full-support fiber.  On that fiber
    # put h(x)=mean_F(b)-b(x), and put h=0 off the fiber.  Then h has zero
    # mean on every macro-fiber.  For f_0=1_F, the projected energy of the
    # fiber means is Q(F,F^c), whereas E(f_0+theta*h) is a quadratic whose
    # derivative at zero is -2*pi(F)*Var_F(b).  A nonconstant b therefore
    # gives an explicit strict counterexample to q_lift=1.
    exit_probability = {
        word: sum(
            (Fraction(count, denominator) for denominator, count in terms.items()),
            Fraction(0),
        )
        for word, terms in exit_terms_by_word.items()
    }
    mean_exit = sum(exit_probability.values(), Fraction(0)) / len(full_words)
    h_value = {word: mean_exit - exit_probability[word] for word in full_words}
    exit_variance = sum((value - mean_exit) ** 2 for value in exit_probability.values()) / len(
        full_words
    )
    internal_energy_terms: Counter[tuple[int, Fraction]] = Counter()
    for word in full_words:
        for r in R:
            window_count = m - r + 1
            for start0 in range(window_count):
                old_block = word[start0 : start0 + r]
                product = eval_word(n, transpositions, old_block)
                options = fibers[r][product]
                denominator = 2 * len(R) * window_count * len(options)
                for new_block in options:
                    new_word = word[:start0] + new_block + word[start0 + r :]
                    if new_word in full_set:
                        difference = h_value[word] - h_value[new_word]
                        if difference:
                            internal_energy_terms[(denominator, difference)] += 1
    internal_oriented_sum = sum(
        (
            Fraction(count, denominator) * difference * difference
            for (denominator, difference), count in internal_energy_terms.items()
        ),
        Fraction(0),
    )
    # All following energies omit the common global factor 1/|Omega|.
    indicator_energy_scaled = sum(exit_probability.values(), Fraction(0))
    bilinear_scaled = sum(
        exit_probability[word] * h_value[word] for word in full_words
    )
    h_energy_scaled = sum(
        exit_probability[word] * h_value[word] * h_value[word] for word in full_words
    ) + Fraction(1, 2) * internal_oriented_sum
    assert bilinear_scaled == -len(full_words) * exit_variance
    if h_energy_scaled and bilinear_scaled:
        optimal_theta = -bilinear_scaled / h_energy_scaled
        optimized_energy_scaled = (
            indicator_energy_scaled
            - bilinear_scaled * bilinear_scaled / h_energy_scaled
        )
        lift_ratio = indicator_energy_scaled / optimized_energy_scaled
    else:
        optimal_theta = Fraction(0)
        optimized_energy_scaled = indicator_energy_scaled
        lift_ratio = Fraction(1)
    exit_distribution = Counter(
        f"{value.numerator}/{value.denominator}" for value in exit_probability.values()
    )
    mean_lift_stress_test = {
        "function": "f=1_full+theta*(mean_full_exit-exit_probability) on full support; f=0 otherwise",
        "full_support_mass": fraction_record(Fraction(len(full_words), len(words))),
        "distinct_exit_probabilities": len(exit_distribution),
        "exit_probability_distribution": dict(sorted(exit_distribution.items())),
        "mean_exit_probability": fraction_record(mean_exit),
        "exit_probability_variance": fraction_record(exit_variance),
        "optimal_theta": fraction_record(optimal_theta),
        "projected_energy_scaled_by_identity_word_count": fraction_record(
            indicator_energy_scaled
        ),
        "optimized_full_energy_scaled_by_identity_word_count": fraction_record(
            optimized_energy_scaled
        ),
        "projected_to_full_energy_ratio": fraction_record(lift_ratio),
        "interpretation": (
            "A ratio above one rigorously refutes only the naive q_lift=1 inequality. "
            "It does not refute the requested polynomial-factor mean-lift bound."
        ),
    }

    base.update(
        {
            "conditional_fiber_sizes": fiber_sizes,
            "statistic_distributions": distributions,
            "prefix_cut_1_based": prefix_cut,
            "crossing_window_counts": crossing_counts,
            "selected_crossing_probability": fraction_record(selected_crossing_probability),
            "selected_first_position_refresh_probability": fraction_record(
                first_position_refresh_probability
            ),
            "prefix_locality_transition_checks": transition_checks,
            "prefix_locality_violations": prefix_locality_violations,
            "candidate_cut_flows": cut_records,
            "explicit_one_step_witnesses": witnesses,
            "mean_lift_stress_test": mean_lift_stress_test,
        }
    )
    return base


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=130013)
    parser.add_argument("--commit", default="502a6f031c6d5a4bc0064ee5b370a4fa3914f993")
    args = parser.parse_args()
    random.seed(args.seed)
    result = {
        "purpose": "Exact falsification of named M13 full-support candidate statistics; no asymptotic inference.",
        "target": "uniform fixed-length identity bridge, restricted to all-label connected support for cut tests",
        "kernel": "exact lazy {3,4,5} same-product heat bath with GOAL_SPEC normalization",
        "permutation_convention": "pq=p after q; word=t_1...t_m",
        "repository_commit": args.commit,
        "seed": args.seed,
        "stochastic": False,
        "python_version": sys.version,
        "platform": platform.platform(),
        "nonstandard_dependencies": [],
        "cases": [audit_case(3, 4), audit_case(4, 4), audit_case(4, 6)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
