#!/usr/bin/env python3
"""Exact finite checks for the projected-star flat-completion lift.

These checks can falsify the orientation, projected count collapse, branch
normalization, or finite pointwise spectral inequalities.  They do not prove
the asymptotic retained-length tail theorem in report.md.
"""

from __future__ import annotations

import json
import math
import platform
from fractions import Fraction
from itertools import permutations


Perm = tuple[int, ...]


def compose(p: Perm, q: Perm) -> Perm:
    """Map product p*q, so (p*q)(x)=p(q(x))."""

    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    result = [0] * len(p)
    for i, value in enumerate(p):
        result[value] = i
    return tuple(result)


def transposition(n: int, i: int, j: int) -> Perm:
    result = list(range(n))
    result[i], result[j] = result[j], result[i]
    return tuple(result)


def all_transpositions(n: int) -> list[Perm]:
    return [transposition(n, i, j) for i in range(n) for j in range(i + 1, n)]


def star_transpositions(n: int) -> list[Perm]:
    return [transposition(n, i, n - 1) for i in range(n - 1)]


def endpoint_table(n: int, generators: list[Perm], max_length: int):
    identity = tuple(range(n))
    tables = [{identity: 1}]
    for _ in range(max_length):
        next_table: dict[Perm, int] = {}
        for endpoint, count in tables[-1].items():
            for generator in generators:
                new_endpoint = compose(endpoint, generator)
                next_table[new_endpoint] = next_table.get(new_endpoint, 0) + count
        tables.append(next_table)
    return tables


def embed(p: Perm, n: int) -> Perm:
    assert len(p) == n - 1
    return p + (n - 1,)


def z_formula(n: int, k: int, x: int) -> int:
    s = n - 1
    if x == n - 1:
        return (s**k + s * ((-1) ** k)) // n
    return (s**k - ((-1) ** k)) // n


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def projection_checks(max_n: int = 5, max_k: int = 6):
    cases = 0
    orientation_cases = 0
    recurrence_cases = 0
    selected = []
    for n in range(2, max_n + 1):
        stars = star_transpositions(n)
        star_tables = endpoint_table(n, stars, max_k)
        stabilizer = [embed(p, n) for p in permutations(range(n - 1))]
        all_perms = list(permutations(range(n)))
        for k in range(max_k + 1):
            endpoint_counts = star_tables[k]
            brute_projection = [0] * n
            for q, count in endpoint_counts.items():
                brute_projection[inverse(q)[n - 1]] += count
            for x in range(n):
                assert brute_projection[x] == z_formula(n, k, x)
                recurrence_cases += 1
                if k:
                    rhs = sum(
                        z_formula(n, k - 1, star[x]) for star in stars
                    )
                    assert rhs == z_formula(n, k, x)

            for g in all_perms:
                x = inverse(g)[n - 1]
                convolution = 0
                for h in stabilizer:
                    q = compose(inverse(h), g)
                    convolution += endpoint_counts.get(q, 0)
                assert convolution == z_formula(n, k, x)
                cases += 1

                for q in endpoint_counts:
                    h = compose(g, inverse(q))
                    fixes_pivot = h[n - 1] == n - 1
                    projected = inverse(q)[n - 1] == x
                    assert fixes_pivot == projected
                    orientation_cases += 1
            if n in (3, 4, 5) and k in (0, 1, 2, 5, 6):
                selected.append(
                    {
                        "N": n,
                        "k": k,
                        "center_count": z_formula(n, k, n - 1),
                        "each_leaf_count": z_formula(n, k, 0),
                        "total": z_formula(n, k, n - 1)
                        + (n - 1) * z_formula(n, k, 0),
                        "expected_total": (n - 1) ** k,
                    }
                )
    return {
        "stabilizer_convolution_equalities": cases,
        "orientation_equivalences": orientation_cases,
        "projected_formula_and_backward_recurrence_equalities": recurrence_cases,
        "selected": selected,
    }


def pointwise_mixing_checks(max_n: int = 5, max_a: int = 12):
    cases = 0
    max_relative_by_n: dict[str, float] = {}
    for n in range(3, max_n + 1):
        generators = all_transpositions(n)
        d = len(generators)
        tables = endpoint_table(n, generators, max_a)
        rho = Fraction(n - 3, n - 1)
        largest_relative = Fraction(0)
        for a, table in enumerate(tables):
            flat_probability = Fraction(2, math.factorial(n))
            for h in permutations(range(n)):
                # A reachable endpoint automatically has the parity of a;
                # testing only that coset avoids comparing against zero target mass.
                count = table.get(h, 0)
                if count == 0:
                    # It may still be parity-compatible but too far away.  Infer
                    # parity from inversion count.
                    inversions = sum(
                        h[i] > h[j] for i in range(n) for j in range(i + 1, n)
                    )
                    if inversions % 2 != a % 2:
                        continue
                probability = Fraction(count, d**a)
                absolute_error = abs(probability - flat_probability)
                spectral_bound = rho**a if not (rho == 0 and a == 0) else Fraction(1)
                assert absolute_error <= spectral_bound
                relative_error = absolute_error / flat_probability
                largest_relative = max(largest_relative, relative_error)
                cases += 1
        max_relative_by_n[str(n)] = float(largest_relative)
    return {
        "exact_kernel_entry_inequalities": cases,
        "largest_relative_error_seen_by_N": max_relative_by_n,
    }


def branch_tv_checks(max_n: int = 5, max_l: int = 6):
    coefficient_equalities = 0
    rank_three_flat_exact = 0
    selected = []
    for n in range(3, max_n + 1):
        full_generators = all_transpositions(n)
        old_generators_small = all_transpositions(n - 1)
        old_generators = [embed(t, n) for t in old_generators_small]
        stars = star_transpositions(n)
        full_tables = endpoint_table(n, full_generators, max_l)
        old_tables = endpoint_table(n, old_generators, max_l)
        star_tables = endpoint_table(n, stars, max_l)
        d = len(old_generators)
        all_perms = list(permutations(range(n)))
        for length in range(max_l + 1):
            for g in all_perms:
                exact_entries: list[int] = []
                flat_entries: list[int] = []
                for k in range(length + 1):
                    a = length - k
                    for q, star_count in star_tables[k].items():
                        h = compose(g, inverse(q))
                        if h[n - 1] != n - 1:
                            continue
                        old_count = old_tables[a].get(h, 0)
                        pattern_count = math.comb(length, k)
                        exact_entries.append(pattern_count * old_count * star_count)
                        flat_entries.append(pattern_count * (d**a) * star_count)
                exact_total = sum(exact_entries)
                flat_total = sum(flat_entries)
                assert exact_total == full_tables[length].get(g, 0)
                coefficient_equalities += 1
                if exact_total == 0:
                    continue
                assert flat_total > 0
                tv = sum(
                    abs(Fraction(x, exact_total) - Fraction(y, flat_total))
                    for x, y in zip(exact_entries, flat_entries)
                ) / 2
                if n == 3:
                    assert tv == 0
                    rank_three_flat_exact += 1
                if (n, length) in ((3, 4), (4, 4), (4, 6), (5, 6)) and g == tuple(range(n)):
                    selected.append(
                        {
                            "N": n,
                            "L": length,
                            "endpoint": "identity",
                            "exact_count": str(exact_total),
                            "flat_branch_TV": fraction_text(tv),
                            "flat_branch_TV_float": float(tv),
                        }
                    )
    return {
        "disintegration_coefficient_equalities": coefficient_equalities,
        "rank_three_exact_flat_cases": rank_three_flat_exact,
        "selected": selected,
    }


def main():
    result = {
        "schema": "r4-r5-flat-projection-check-v1",
        "python": platform.python_version(),
        "deterministic": True,
        "random_seed": None,
        "universal_claim_falsifiable": (
            "Finite instances of h=gq^{-1}, the stabilizer/projection "
            "equivalence, the Z recurrence, the flat positive branch "
            "collapse, and the pointwise mixing inequality."
        ),
        "projection": projection_checks(),
        "pointwise_mixing": pointwise_mixing_checks(),
        "branch_tv": branch_tv_checks(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
