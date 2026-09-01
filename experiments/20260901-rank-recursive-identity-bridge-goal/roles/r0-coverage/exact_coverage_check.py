#!/usr/bin/env python3
"""Deterministic exact checks for the R0 deleted-generator proof.

The checks can falsify the finite instances of the return-count identity,
the trace bounds, the union bound, or the spectral constant.  They cannot
prove the quantified theorem, whose proof is in report.md.
"""

from __future__ import annotations

import json
import math
import platform
from fractions import Fraction
from itertools import permutations


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return p*q as maps: (p*q)(x) = p(q(x))."""

    return tuple(p[q[x]] for x in range(len(p)))


def transpositions(n: int) -> list[tuple[int, ...]]:
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            t = list(range(n))
            t[i], t[j] = t[j], t[i]
            result.append(tuple(t))
    return result


def cayley_data(n: int):
    states = list(permutations(range(n)))
    state_index = {p: i for i, p in enumerate(states)}
    generators = transpositions(n)
    transitions = [
        [state_index[compose(p, t)] for t in generators] for p in states
    ]
    return states, generators, transitions


def return_snapshots(n: int, lengths: list[int], excluded: int | None = None):
    states, generators, transitions = cayley_data(n)
    allowed = [j for j in range(len(generators)) if j != excluded]
    wanted = set(lengths)
    counts = [0] * len(states)
    counts[0] = 1
    snapshots = {0: counts[0]} if 0 in wanted else {}
    for step in range(1, max(lengths, default=0) + 1):
        next_counts = [0] * len(states)
        for state, count in enumerate(counts):
            if count:
                for generator in allowed:
                    next_counts[transitions[state][generator]] += count
        counts = next_counts
        if step in wanted:
            snapshots[step] = counts[0]
    return snapshots


def coverage_counts(n: int, length: int) -> tuple[int, int]:
    """Return (identity words, full-support identity words) exactly."""

    states, generators, transitions = cayley_data(n)
    dp = {(0, 0): 1}
    for _ in range(length):
        next_dp: dict[tuple[int, int], int] = {}
        for (state, mask), count in dp.items():
            for generator in range(len(generators)):
                key = (transitions[state][generator], mask | (1 << generator))
                next_dp[key] = next_dp.get(key, 0) + count
        dp = next_dp
    full_mask = (1 << len(generators)) - 1
    total = sum(count for (state, _), count in dp.items() if state == 0)
    full = dp.get((0, full_mask), 0)
    return total, full


def partitions(n: int, ceiling: int | None = None):
    if n == 0:
        yield ()
        return
    if ceiling is None or ceiling > n:
        ceiling = n
    for first in range(ceiling, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def content_sum(partition: tuple[int, ...]) -> int:
    return sum(column - row for row, width in enumerate(partition, 1)
               for column in range(1, width + 1))


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def spectral_partition_checks():
    output = []
    for n in range(3, 13):
        m = math.comb(n, 2)
        nontrivial = [
            Fraction(content_sum(partition), m)
            for partition in partitions(n)
            if partition not in ((n,), (1,) * n)
        ]
        observed = max(abs(value) for value in nontrivial)
        expected = Fraction(m - n, m)
        assert observed == expected
        output.append(
            {
                "N": n,
                "max_nontrivial_absolute_character_ratio": fraction_text(observed),
                "expected_1_minus_N_over_M": fraction_text(expected),
                "equal": True,
            }
        )
    return output


def deleted_graph_constant_checks():
    output = []
    for n in range(3, 13):
        m = math.comb(n, 2)
        rho_exact = 1 - Fraction(n - 2, m - 1)
        rho_perturbative = 1 - Fraction(n - 2, m)
        alphabet_ratio = Fraction(m - 1, m)
        assert rho_exact <= rho_perturbative
        assert alphabet_ratio * rho_exact == Fraction(n - 2, n)
        output.append(
            {
                "N": n,
                "deleted_graph_laplacian_gap": n - 2,
                "exact_Q_absolute_radius": fraction_text(rho_exact),
                "perturbative_Q_absolute_bound": fraction_text(
                    rho_perturbative
                ),
                "exact_radius_no_larger_than_perturbative_bound": True,
                "alphabet_ratio_times_exact_radius": fraction_text(
                    alphabet_ratio * rho_exact
                ),
                "expected_1_minus_2_over_N": fraction_text(
                    Fraction(n - 2, n)
                ),
            }
        )
    return output


def return_count_checks():
    output = []
    cases = {
        3: [0, 2, 4, 6, 2 * 3**3],
        4: [0, 2, 4, 6, 2 * 4**3],
        5: [0, 2, 4, 6, 2 * 5**3],
    }
    for n, lengths in cases.items():
        m = math.comb(n, 2)
        full = return_snapshots(n, lengths)
        deleted_by_edge = [
            return_snapshots(n, lengths, excluded=edge)
            for edge in range(m)
        ]
        for length in lengths:
            assert full[length] > 0
            deleted_counts = [snapshots[length] for snapshots in deleted_by_edge]
            assert len(set(deleted_counts)) == 1
            deleted = deleted_counts[0]
            fixed_probability = Fraction(deleted, full[length])
            normalized_ratio = (
                Fraction(m - 1, m) ** length
                * Fraction(deleted, (m - 1) ** length)
                / Fraction(full[length], m**length)
            )
            assert fixed_probability == normalized_ratio

            rho = 1 - Fraction(n - 2, m - 1)
            q_return = Fraction(deleted, (m - 1) ** length)
            q_return_bound = Fraction(2, math.factorial(n)) + rho**length
            p_return = Fraction(full[length], m**length)
            p_return_floor = Fraction(2, math.factorial(n))
            theorem_fixed_bound = (
                Fraction(m - 1, m) ** length
                * (1 + Fraction(math.factorial(n), 2) * rho**length)
            )
            assert q_return <= q_return_bound
            assert p_return >= p_return_floor
            assert fixed_probability <= theorem_fixed_bound
            item = {
                "N": n,
                "L": length,
                "identity_word_count": str(full[length]),
                "deleted_edge_identity_word_count": str(deleted),
                "all_deleted_edges_same_count": True,
                "exact_deleted_ratio_identity": True,
                "q_even_return_bound": True,
                "p_even_return_floor": True,
                "fixed_edge_theorem_bound": True,
                "fixed_edge_probability_float": float(fixed_probability),
                "fixed_edge_bound_float": float(theorem_fixed_bound),
            }
            if length <= 6:
                item["fixed_edge_probability_exact"] = fraction_text(
                    fixed_probability
                )
                item["fixed_edge_bound_exact"] = fraction_text(
                    theorem_fixed_bound
                )
            output.append(item)
    return output


def exact_coverage_checks():
    output = []
    for n, length in [(2, 0), (2, 2), (3, 0), (3, 2), (3, 4), (3, 6),
                      (4, 0), (4, 2), (4, 4), (4, 6), (5, 6)]:
        total, full = coverage_counts(n, length)
        not_full = total - full
        item = {
            "N": n,
            "L": length,
            "identity_word_count": str(total),
            "full_support_identity_word_count": str(full),
            "not_full_identity_word_count": str(not_full),
            "not_full_probability_float": float(Fraction(not_full, total)),
        }
        if n >= 3:
            m = math.comb(n, 2)
            deleted = return_snapshots(n, [length], excluded=0)[length]
            union_numerator = m * deleted
            assert not_full <= union_numerator
            item["union_bound_verified_exactly"] = True
            item["union_bound_probability_float"] = float(
                Fraction(union_numerator, total)
            )
        output.append(item)
    return output


def boundary_checks():
    # For S_2 there is exactly one factor at every position.  Product parity
    # determines the endpoint, and every positive-length word has full support.
    return [
        {"N": 2, "L": 0, "endpoint": "e", "feasible": True,
         "full_support": False},
        {"N": 2, "L": 1, "endpoint": "(1 2)", "feasible": True,
         "full_support": True},
        {"N": 2, "L": 2, "endpoint": "e", "feasible": True,
         "full_support": True},
        {"N": 2, "L": 16, "endpoint": "e", "feasible": True,
         "full_support": True},
        {"N": 3, "L": 1, "endpoint": "e", "feasible": False,
         "reason": "sign parity"},
    ]


def main():
    result = {
        "schema": "r0-exact-coverage-check-v1",
        "python": platform.python_version(),
        "deterministic": True,
        "universal_claim_falsifiable": (
            "The finite instances of the deleted-generator return identity, "
            "the even-time return bounds, the union bound, and the claimed "
            "full-walk absolute spectral constant."
        ),
        "spectral_partition_checks": spectral_partition_checks(),
        "deleted_graph_constant_checks": deleted_graph_constant_checks(),
        "return_count_checks": return_count_checks(),
        "exact_coverage_checks": exact_coverage_checks(),
        "boundary_checks": boundary_checks(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
