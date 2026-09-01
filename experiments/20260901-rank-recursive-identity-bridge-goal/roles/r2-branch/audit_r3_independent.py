#!/usr/bin/env python3
"""Independent exact audit of the R3 prescribed-endpoint star sampler.

This file deliberately does not import any code from roles/r3-star.  It uses
three separate constructions:

1. a direct labeled endpoint/support dynamic program;
2. an independent implementation of Feray's positive transitive formula;
3. an exact symbolic expansion of the proposed backward sampling kernel.

Permutations are tuples of zero-based images.  ``compose(p, q)`` is p o q,
so a displayed word t_1 ... t_k is evaluated rightmost-first as a map and is
built by repeatedly replacing the current product p by p o t_i.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import subprocess
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from pathlib import Path


FERAY_URL = "https://arxiv.org/html/0904.4854v2"


def identity(n: int) -> tuple[int, ...]:
    return tuple(range(n))


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return p o q, i.e. (p q)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def star(n: int, i: int) -> tuple[int, ...]:
    t = list(range(n))
    t[i], t[n - 1] = t[n - 1], t[i]
    return tuple(t)


def cycles(q: tuple[int, ...]) -> list[tuple[int, ...]]:
    seen: set[int] = set()
    answer: list[tuple[int, ...]] = []
    for x in range(len(q)):
        if x in seen:
            continue
        cyc: list[int] = []
        y = x
        while y not in seen:
            seen.add(y)
            cyc.append(y)
            y = q[y]
        answer.append(tuple(cyc))
    return answer


def endpoint_data(q: tuple[int, ...]) -> dict[str, object]:
    """Mandatory active type and optional fixed lower labels for q."""
    n = len(q)
    pivot = n - 1
    cs = cycles(q)
    pivot_cycle = next(c for c in cs if pivot in c)
    nonpivot_nontrivial = [c for c in cs if pivot not in c and len(c) > 1]
    optional = tuple(i for i in range(n - 1) if q[i] == i)
    mandatory = tuple(i for i in range(n - 1) if q[i] != i)
    parts = (len(pivot_cycle),) + tuple(len(c) for c in nonpivot_nontrivial)
    n0 = sum(parts)
    ell_star = n0 + len(parts) - 2
    mandatory_mask = sum(1 << i for i in mandatory)
    optional_mask = sum(1 << i for i in optional)
    return {
        "parts": parts,
        "n0": n0,
        "ell_star": ell_star,
        "mandatory": mandatory,
        "optional": optional,
        "mandatory_mask": mandatory_mask,
        "optional_mask": optional_mask,
    }


@lru_cache(maxsize=None)
def f_series(scale: int, degree: int) -> tuple[Fraction, ...]:
    """Coefficients through degree of F(scale*t)=2sinh(scale*t/2)/(scale*t)."""
    ans = [Fraction(0) for _ in range(degree + 1)]
    for d in range(0, degree + 1, 2):
        ans[d] = Fraction(scale**d, (2**d) * math.factorial(d + 1))
    return tuple(ans)


def multiply_truncated(
    p: tuple[Fraction, ...], q: tuple[Fraction, ...], degree: int
) -> tuple[Fraction, ...]:
    ans = [Fraction(0) for _ in range(degree + 1)]
    for i, a in enumerate(p):
        if a == 0:
            continue
        for j, b in enumerate(q[: degree - i + 1]):
            if b:
                ans[i + j] += a * b
    return tuple(ans)


@lru_cache(maxsize=None)
def transitive_count(parts: tuple[int, ...], k: int) -> int:
    """Feray Theorem 1.2, independently implemented from the displayed formula."""
    n_active = sum(parts)
    if n_active == 1:
        return int(parts == (1,) and k == 0)
    excess = k - (n_active + len(parts) - 2)
    if excess < 0:
        return 0
    poly: tuple[Fraction, ...] = (Fraction(1),) + (Fraction(0),) * excess
    scales = (1,) * (n_active - 2) + parts
    for scale in scales:
        poly = multiply_truncated(poly, f_series(scale, excess), excess)
    coefficient = poly[excess]
    prefactor = Fraction(
        math.factorial(k) * math.prod(parts), math.factorial(n_active)
    )
    value = prefactor * coefficient
    assert value.denominator == 1, (parts, k, value)
    return value.numerator


@lru_cache(maxsize=None)
def formula_count(n: int, k: int, q: tuple[int, ...]) -> int:
    if len(q) != n or k < 0:
        return 0
    if n == 1:
        return int(k == 0 and q == identity(1))
    data = endpoint_data(q)
    base = tuple(data["parts"])
    f = len(tuple(data["optional"]))
    return sum(
        math.comb(f, s) * transitive_count(base + (1,) * s, k)
        for s in range(f + 1)
    )


def exact_support_formula(q: tuple[int, ...], k: int, mask: int) -> int:
    """Formula for one specified exact lower-label support, not summed over choices."""
    data = endpoint_data(q)
    mandatory = int(data["mandatory_mask"])
    optional = int(data["optional_mask"])
    if mask & mandatory != mandatory or mask & ~(mandatory | optional):
        return 0
    s = (mask & optional).bit_count()
    return transitive_count(tuple(data["parts"]) + (1,) * s, k)


def direct_tables(
    n: int, max_k: int
) -> tuple[list[dict[tuple[int, ...], int]], list[dict[tuple[tuple[int, ...], int], int]]]:
    """Direct labeled walk DP, retaining exact used-support masks separately."""
    endpoints: list[dict[tuple[int, ...], int]] = []
    supports: list[dict[tuple[tuple[int, ...], int], int]] = []
    current_support: dict[tuple[tuple[int, ...], int], int] = {(identity(n), 0): 1}
    for k in range(max_k + 1):
        supports.append(dict(current_support))
        collapsed: defaultdict[tuple[int, ...], int] = defaultdict(int)
        for (q, _mask), count in current_support.items():
            collapsed[q] += count
        endpoints.append(dict(collapsed))
        if k == max_k:
            break
        nxt: defaultdict[tuple[tuple[int, ...], int], int] = defaultdict(int)
        for (q, mask), count in current_support.items():
            for i in range(n - 1):
                nxt[(compose(q, star(n, i)), mask | (1 << i))] += count
        current_support = dict(nxt)
    return endpoints, supports


def evaluate_word(n: int, word: tuple[int, ...]) -> tuple[int, ...]:
    q = identity(n)
    for i in word:
        q = compose(q, star(n, i))
    return q


@lru_cache(maxsize=None)
def exact_backward_distribution(
    n: int, k: int, q: tuple[int, ...]
) -> tuple[tuple[tuple[int, ...], Fraction], ...]:
    """Expand the backward kernel symbolically, returning exact word probabilities."""
    total = formula_count(n, k, q)
    if total == 0:
        return tuple()
    if k == 0:
        assert q == identity(n) and total == 1
        return ((tuple(), Fraction(1)),)
    output: list[tuple[tuple[int, ...], Fraction]] = []
    child_sum = 0
    for i in range(n - 1):
        # q = prefix * tau_i, hence prefix = q * tau_i.
        prefix_endpoint = compose(q, star(n, i))
        child_count = formula_count(n, k - 1, prefix_endpoint)
        child_sum += child_count
        if child_count == 0:
            continue
        branch_probability = Fraction(child_count, total)
        for prefix, probability in exact_backward_distribution(
            n, k - 1, prefix_endpoint
        ):
            output.append((prefix + (i,), branch_probability * probability))
    assert child_sum == total
    return tuple(output)


def partitions_up_to(n: int) -> list[int]:
    p = [0] * (n + 1)
    p[0] = 1
    for part in range(1, n + 1):
        for value in range(part, n + 1):
            p[value] += p[value - part]
    return p


def git_commit(repo: Path) -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()


def run_audit() -> dict[str, object]:
    endpoint_checks = 0
    support_cell_checks = 0
    recurrence_checks = 0
    sampler_fibers = 0
    sampler_words = 0
    feasibility_checks = 0
    total_mass_checks = 0
    direct: dict[int, tuple[list[dict], list[dict]]] = {}

    for n in range(1, 6):
        direct[n] = direct_tables(n, 6)

    # Every endpoint and every length through six for N <= 4; one complete
    # N=5 slice at k=6.  Include zero-count endpoints, not only reachable ones.
    test_pairs = [(n, k) for n in range(1, 5) for k in range(7)] + [(5, 6)]
    for n, k in test_pairs:
        endpoints, supports = direct[n]
        all_permutations = list(itertools.permutations(range(n)))
        for q in all_permutations:
            brute = endpoints[k].get(q, 0)
            formula = formula_count(n, k, q)
            assert formula == brute, ("endpoint", n, k, q, formula, brute)
            endpoint_checks += 1

            if n == 1:
                expected_feasible = k == 0 and q == identity(1)
            else:
                ell = int(endpoint_data(q)["ell_star"])
                expected_feasible = k >= ell and (k - ell) % 2 == 0
            assert (formula > 0) == expected_feasible, (
                "feasibility",
                n,
                k,
                q,
                formula,
                expected_feasible,
            )
            feasibility_checks += 1

            for mask in range(1 << max(0, n - 1)):
                brute_support = supports[k].get((q, mask), 0)
                support_formula = exact_support_formula(q, k, mask)
                assert support_formula == brute_support, (
                    "support",
                    n,
                    k,
                    q,
                    mask,
                    support_formula,
                    brute_support,
                )
                support_cell_checks += 1

            if formula:
                distribution = dict(exact_backward_distribution(n, k, q))
                assert len(distribution) == formula
                assert sum(distribution.values(), Fraction(0)) == 1
                expected_probability = Fraction(1, formula)
                assert all(p == expected_probability for p in distribution.values())
                assert all(evaluate_word(n, word) == q for word in distribution)
                sampler_fibers += 1
                sampler_words += len(distribution)

        assert sum(formula_count(n, k, q) for q in all_permutations) == (
            (n - 1) ** k
        )
        total_mass_checks += 1

    # Last-factor recurrence for all endpoints N<=4 and r=1..6, and N=5,r=6.
    recurrence_pairs = [(n, k) for n in range(1, 5) for k in range(1, 7)] + [
        (5, 6)
    ]
    orientation_witness = None
    for n, k in recurrence_pairs:
        for q in itertools.permutations(range(n)):
            right_children = [
                formula_count(n, k - 1, compose(q, star(n, i)))
                for i in range(n - 1)
            ]
            assert formula_count(n, k, q) == sum(right_children)
            recurrence_checks += 1
            if orientation_witness is None and n >= 3:
                left_children = [
                    formula_count(n, k - 1, compose(star(n, i), q))
                    for i in range(n - 1)
                ]
                if left_children != right_children:
                    orientation_witness = {
                        "n": n,
                        "k": k,
                        "q_zero_based_images": list(q),
                        "right_append_prefix_weights": right_children,
                        "left_prepend_suffix_weights": left_children,
                    }

    # Minimality, wrong parity, and pair-padding directly from the formula.
    minimal_padding_checks = 0
    for n in range(2, 6):
        for q in itertools.permutations(range(n)):
            ell = int(endpoint_data(q)["ell_star"])
            assert formula_count(n, ell, q) > 0
            assert formula_count(n, ell + 2, q) > 0
            if ell >= 1:
                assert formula_count(n, ell - 1, q) == 0
            if ell >= 2:
                assert formula_count(n, ell - 2, q) == 0
            minimal_padding_checks += 1

    # Explicit boundary facts for the degenerate alphabets.
    n1 = [formula_count(1, k, identity(1)) for k in range(7)]
    n2_identity = [formula_count(2, k, identity(2)) for k in range(7)]
    n2_swap = [formula_count(2, k, star(2, 0)) for k in range(7)]
    assert n1 == [1, 0, 0, 0, 0, 0, 0]
    assert n2_identity == [1, 0, 1, 0, 1, 0, 1]
    assert n2_swap == [0, 1, 0, 1, 0, 1, 0]

    # Secondary check of the pointed-orbit state count sum_{u<N} p(u).
    partition_values = partitions_up_to(99)
    pointed = {
        str(n): sum(partition_values[:n]) for n in (10, 20, 50, 100)
    }
    assert pointed == {
        "10": 97,
        "20": 2087,
        "50": 1091745,
        "100": 1452423276,
    }

    selected_counts = {}
    for n, k, q in [
        (2, 0, identity(2)),
        (2, 5, star(2, 0)),
        (3, 4, identity(3)),
        (4, 6, identity(4)),
        (5, 6, identity(5)),
        (5, 6, (1, 0, 3, 2, 4)),
    ]:
        selected_counts[f"N={n},k={k},q={list(q)}"] = formula_count(n, k, q)

    return {
        "audit_scope": {
            "formula_and_direct_dp": "every endpoint for N=1..4,k=0..6 and N=5,k=6",
            "support_dp": "every exact lower-label support in the same endpoint/length cases",
            "sampler": "exact symbolic probability of every word in every nonempty tested fiber",
            "implementation_independence": "does not import roles/r3-star code",
        },
        "primary_source": {
            "url": FERAY_URL,
            "proposition_1_1": "transitive star count is constant on ordinary conjugacy classes",
            "theorem_1_2": "r!/|lambda|! * product(lambda_i) * [t^g] F(t)^(|lambda|-2) product_i F(lambda_i t)",
            "excess": "g=r-(|lambda|+ell(lambda)-2)",
            "F": "2*sinh(t/2)/t",
            "lemma_3_1": "full partial-permutation support is equivalent to transitivity",
            "equation_12": "repeats the theorem normalization after coefficient extraction",
            "composition": "partial permutations multiply as sigma o sigma-prime, hence rightmost-first as maps",
        },
        "checks": {
            "endpoint_equalities": endpoint_checks,
            "exact_support_cell_equalities": support_cell_checks,
            "last_factor_recurrences": recurrence_checks,
            "feasibility_equalities": feasibility_checks,
            "total_walk_mass_equalities": total_mass_checks,
            "minimal_and_padding_endpoints": minimal_padding_checks,
            "symbolically_uniform_nonempty_fibers": sampler_fibers,
            "symbolically_enumerated_words": sampler_words,
        },
        "boundary_sequences": {
            "N=1_identity_k=0..6": n1,
            "N=2_identity_k=0..6": n2_identity,
            "N=2_swap_k=0..6": n2_swap,
        },
        "last_factor_orientation_witness": orientation_witness,
        "pointed_state_counts": pointed,
        "selected_counts": selected_counts,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run_audit()
    repo = Path(__file__).resolve().parents[4]
    result["environment"] = {
        "python": platform.python_version(),
        "implementation": platform.python_implementation(),
        "repository_commit": git_commit(repo),
        "command": (
            "python3 experiments/20260901-rank-recursive-identity-bridge-goal/"
            "roles/r2-branch/audit_r3_independent.py --output experiments/"
            "20260901-rank-recursive-identity-bridge-goal/roles/r2-branch/"
            "audit_r3_results.json"
        ),
        "nonstandard_dependencies": [],
        "determinism": "no randomness used",
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["checks"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
