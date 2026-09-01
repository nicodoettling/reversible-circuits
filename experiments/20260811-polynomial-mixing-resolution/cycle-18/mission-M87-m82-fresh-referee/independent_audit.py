#!/usr/bin/env python3
"""Independent exact referee audit of the frozen M82 reset report.

This file imports no predecessor experiment.  It reconstructs the contextual
composition operator and the grouped Cayley sums directly from the formulas
stated in the frozen report.  Every promoted comparison uses Fraction; floats
are emitted only as readable annotations.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import platform
import subprocess
import time
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


@functools.lru_cache(maxsize=None)
def ordered_compositions(total: int) -> tuple[tuple[int, ...], ...]:
    if total == 0:
        return ((),)
    rows: list[tuple[int, ...]] = []
    for cuts in range(1 << (total - 1)):
        left = 0
        comp: list[int] = []
        for site in range(1, total):
            if cuts & (1 << (site - 1)):
                comp.append(site - left)
                left = site
        comp.append(total - left)
        rows.append(tuple(comp))
    return tuple(rows)


@functools.lru_cache(maxsize=None)
def tree_weight(size: int) -> Fraction:
    if size < 1:
        raise ValueError(size)
    return Fraction(size ** (size - 1), math.factorial(size))


def root_mass(rank: int, comp: tuple[int, ...]) -> Fraction:
    answer = Fraction(1, math.factorial(len(comp)) * tree_weight(rank + 1))
    for part in comp:
        answer *= tree_weight(part)
    return answer


@functools.lru_cache(maxsize=None)
def root_rows(rank: int) -> tuple[tuple[tuple[int, ...], Fraction], ...]:
    rows = tuple((c, root_mass(rank, c)) for c in ordered_compositions(rank))
    assert sum((mass for _, mass in rows), Fraction()) == 1
    return rows


def split_mass(rank: int, boundary: int) -> Fraction:
    return (
        tree_weight(rank + 1 - boundary)
        * tree_weight(boundary)
        / tree_weight(rank + 1)
    )


def choose_ratio(numerator_n: int, numerator_k: int, denominator_n: int, denominator_k: int) -> Fraction:
    if not (
        0 <= numerator_k <= numerator_n
        and 0 <= denominator_k <= denominator_n
    ):
        return Fraction()
    return Fraction(
        math.comb(numerator_n, numerator_k),
        math.comb(denominator_n, denominator_k),
    )


def contextual_mean_value(parts: int, last: int, K: int, R: int, boundary: int) -> Fraction:
    if last < boundary:
        return Fraction()
    if last == boundary:
        return K * choose_ratio(
            parts + K - R - 2,
            K - R - 1,
            parts + K - 1,
            K - 1,
        )
    local_split = (
        tree_weight(last - boundary)
        * tree_weight(boundary)
        / tree_weight(last)
    )
    already_bad = choose_ratio(K, R + 1, K + parts, R + 1)
    return local_split * (1 - already_bad)


def inherited_rank_probability(K: int, R: int, parts: int, rank: int) -> Fraction:
    return Fraction(
        math.comb(R + rank, rank)
        * math.comb(K - R - 1 + parts - rank, parts - rank),
        math.comb(K + parts, parts),
    )


@functools.lru_cache(maxsize=None)
def direct_split(rank: int, K: int, R: int, boundary: int):
    """Return direct canonical ``D`` and ``J`` maps with exact normalization."""
    rows = root_rows(rank)
    values = {
        comp: contextual_mean_value(len(comp), comp[-1], K, R, boundary)
        for comp, _ in rows
    }
    q_parent = split_mass(rank, boundary)
    observed_mean = sum(
        (mass * values[comp] for comp, mass in rows), Fraction()
    )
    assert observed_mean == q_parent

    deep: defaultdict[tuple[int, int, int, int], Fraction] = defaultdict(Fraction)
    for comp, mass in rows:
        parts = len(comp)
        last = comp[-1]
        if last <= boundary:
            continue
        child_local_rank = last - 1
        if child_local_rank < 2:
            continue
        q_child = split_mass(child_local_rank, boundary)
        for inherited_rank in range(1, parts + 1):
            nu = inherited_rank_probability(K, R, parts, inherited_rank)
            if not nu:
                continue
            child = (
                child_local_rank,
                K + parts,
                R + inherited_rank,
                boundary,
            )
            deep[child] += mass * q_child * nu / q_parent

    reset: defaultdict[tuple[int, int, int, int], Fraction] = defaultdict(Fraction)
    for endpoint, endpoint_mass in rows:
        endpoint_degree = len(endpoint)
        if endpoint_degree < 2:
            continue
        first, second = endpoint[0], endpoint[1]
        suffix = endpoint[1:]
        current = Fraction()
        for comp, mass in rows:
            if len(comp) < len(suffix) + 1:
                continue
            if comp[-len(suffix):] != suffix:
                continue
            if sum(comp[:-len(suffix)]) != first:
                continue
            current += mass * (values[comp] - q_parent)
        capacity = endpoint_mass * endpoint_degree
        coefficient = current * current / (capacity * q_parent)
        child = (
            first + second - 1,
            endpoint_degree - 1,
            endpoint_degree - 2,
            second,
        )
        if child[0] >= 2:
            reset[child] += coefficient

    parent_phase = rank + K - R
    for child in (*deep.keys(), *reset.keys()):
        assert child[0] + child[1] - child[2] < parent_phase
    for child in reset:
        assert child[1] - child[2] == 1
    return dict(deep), dict(reset)


@functools.lru_cache(maxsize=None)
def eliminated_reset(rank: int, K: int, R: int, boundary: int):
    if rank < 2:
        return {}
    deep, reset = direct_split(rank, K, R, boundary)
    answer: defaultdict[tuple[int, int, int, int], Fraction] = defaultdict(Fraction)
    for child, coefficient in reset.items():
        answer[child] += coefficient
    for child, coefficient in deep.items():
        for target, continuation in eliminated_reset(*child).items():
            answer[target] += coefficient * continuation
    return dict(answer)


def phase_potential(context: tuple[int, int, int, int], exponent: int) -> Fraction:
    rank, K, R, boundary = context
    phase = rank + K - R
    return (
        phase**exponent
        * (1 - split_mass(rank, boundary))
        * Fraction(K, R + 1)
    )


def direct_weighted_row(context: tuple[int, int, int, int], exponent: int):
    deep, reset = direct_split(*context)
    deep_value = sum(
        (coefficient * phase_potential(child, exponent) for child, coefficient in deep.items()),
        Fraction(),
    )
    reset_value = sum(
        (coefficient * phase_potential(child, exponent) for child, coefficient in reset.items()),
        Fraction(),
    )
    return deep_value, reset_value


@functools.lru_cache(maxsize=None)
def cayley_sum(total: int, parts: int) -> Fraction:
    """Product-weight sum over ordered positive ``parts``-compositions."""
    if parts == 0:
        return Fraction(int(total == 0))
    if not (1 <= parts <= total):
        return Fraction()
    # [z^total] T(z)^parts = parts*total^(total-parts-1)/(total-parts)!.
    return Fraction(
        parts * total ** (total - parts),
        total * math.factorial(total - parts),
    )


def grouped_deep(
    context: tuple[int, int, int, int],
    exponent: int,
    floor_scale: int | None = None,
):
    rank, K, R, boundary = context
    q_parent = split_mass(rank, boundary)
    exact = Fraction()
    floor_integer = 0
    term_count = 0
    for parts in range(1, rank + 1):
        for last in range(boundary + 1, rank + 1):
            mass = (
                tree_weight(last)
                * cayley_sum(rank - last, parts - 1)
                / (math.factorial(parts) * tree_weight(rank + 1))
            )
            if not mass or last - 1 < 2:
                continue
            q_child = split_mass(last - 1, boundary)
            for inherited_rank in range(1, parts + 1):
                nu = inherited_rank_probability(K, R, parts, inherited_rank)
                if not nu:
                    continue
                child = (last - 1, K + parts, R + inherited_rank, boundary)
                term = mass * q_child * nu / q_parent * phase_potential(child, exponent)
                assert term >= 0
                if floor_scale is None:
                    exact += term
                else:
                    floor_integer += term.numerator * floor_scale // term.denominator
                    term_count += 1
    if floor_scale is None:
        return exact
    return floor_integer, term_count


def grouped_reset(
    context: tuple[int, int, int, int],
    exponent: int,
    floor_scale: int | None = None,
):
    rank, K, R, boundary = context
    q_parent = split_mass(rank, boundary)
    scalar_cache: dict[tuple[int, int, int], Fraction] = {}
    exact = Fraction()
    floor_integer = 0
    term_count = 0

    def scalar(first: int, suffix_parts: int, last: int) -> Fraction:
        key = (first, suffix_parts, last)
        if key not in scalar_cache:
            value = Fraction()
            for prefix_parts in range(1, first + 1):
                value += (
                    cayley_sum(first, prefix_parts)
                    * (
                        contextual_mean_value(
                            prefix_parts + suffix_parts,
                            last,
                            K,
                            R,
                            boundary,
                        )
                        - q_parent
                    )
                    / math.factorial(prefix_parts + suffix_parts)
                )
            scalar_cache[key] = value
        return scalar_cache[key]

    # Endpoint is (first, second, middle..., last); suffix_parts counts all
    # parts after ``first``.
    for suffix_parts in range(1, rank):
        middle_and_last_parts = suffix_parts - 1
        for first in range(1, rank + 1):
            max_second = rank - first - middle_and_last_parts
            for second in range(1, max_second + 1):
                remaining_total = rank - first - second
                child = (first + second - 1, suffix_parts, suffix_parts - 1, second)
                if child[0] < 2:
                    continue
                child_value = phase_potential(child, exponent)
                if middle_and_last_parts == 0:
                    if remaining_total != 0:
                        continue
                    tails = ((second, tree_weight(second)),)
                else:
                    tail_rows: list[tuple[int, Fraction]] = []
                    for last in range(1, remaining_total + 1):
                        middle_weight = cayley_sum(
                            remaining_total - last,
                            middle_and_last_parts - 1,
                        )
                        if middle_weight:
                            tail_rows.append(
                                (last, tree_weight(second) * middle_weight * tree_weight(last))
                            )
                    tails = tuple(tail_rows)
                for last, suffix_weight in tails:
                    current_scalar = scalar(first, suffix_parts, last)
                    energy = (
                        suffix_weight
                        * math.factorial(suffix_parts)
                        * current_scalar
                        * current_scalar
                        / (tree_weight(first) * tree_weight(rank + 1) * q_parent)
                    )
                    term = energy * child_value
                    assert term >= 0
                    if floor_scale is None:
                        exact += term
                    else:
                        floor_integer += term.numerator * floor_scale // term.denominator
                        term_count += 1
    if floor_scale is None:
        return exact
    return floor_integer, term_count


def fraction_record(value: Fraction) -> dict[str, object]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


def audit_split_bound(limit: int = 80) -> dict[str, object]:
    largest = (Fraction(-1), None)
    for a in range(1, limit + 1):
        for b in range(1, limit + 1):
            if a + b < 3:
                continue
            q = tree_weight(a) * tree_weight(b) / tree_weight(a + b)
            assert q <= Fraction(2, 3)
            if q > largest[0]:
                largest = (q, (a, b))
    return {
        "finite_limit_each_part": limit,
        "maximum": fraction_record(largest[0]),
        "maximizers_include": list(largest[1]),
        "excluded_pair_q": fraction_record(tree_weight(1) ** 2 / tree_weight(2)),
        "analytic_proof": (
            "For a+b=n, q=p*n/(ab), where p is the Bin(n,a/n) mass at a. "
            "If one part is 1, q=(1-1/n)^(n-2), decreasing from 2/3. "
            "If both parts are at least 2, the adjacent/central mass ratios "
            "are b/(b+1) and a/(a+1), hence p<=3/7 and n/(ab)<=1."
        ),
    }


def audit_grouped_direct() -> dict[str, object]:
    contexts = 0
    equality_checks = 0
    for rank in range(2, 8):
        for K in range(1, 5):
            for R in range(K):
                for boundary in range(1, rank + 1):
                    for exponent in range(3):
                        context = (rank, K, R, boundary)
                        direct_d, direct_j = direct_weighted_row(context, exponent)
                        grouped_d = grouped_deep(context, exponent)
                        grouped_j = grouped_reset(context, exponent)
                        assert direct_d == grouped_d, (context, exponent, "D")
                        assert direct_j == grouped_j, (context, exponent, "J")
                        contexts += 1
                        equality_checks += 2
    return {
        "scope": "2<=s<=7, 1<=K<=4, 0<=R<K, every B, d in {0,1,2}",
        "contexts": contexts,
        "exact_equalities": equality_checks,
        "failures": 0,
    }


def audit_reachability() -> dict[str, object]:
    constructions = []
    for K in range(2, 31):
        for R in range(1, K):
            parts = K - 1
            inherited_rank = R
            assert 1 <= inherited_rank <= parts
            assert (1 + parts, inherited_rank) == (K, R)
            constructions.append((K, R))
    return {
        "reset_targets_right_heavy": True,
        "constructive_pairs_checked": len(constructions),
        "closure": "{(1,0)} union {(K,R): K>R>=1}",
        "argument": (
            "Every reset has (K,R)=(k-1,k-2). A deep child preserves K>R "
            "and has R>=1. Conversely, from (1,0), choose k=K-1 and j=R."
        ),
    }


def audit_eliminated_rows() -> dict[str, object]:
    first_failure = None
    right_heavy_max = (Fraction(-1), None)
    contexts = 0
    for rank in range(2, 7):
        for K in range(1, 9):
            for R in range(K):
                if R == 0 and K > 1:
                    continue
                for boundary in range(1, rank + 1):
                    context = (rank, K, R, boundary)
                    row = sum(eliminated_reset(*context).values(), Fraction())
                    contexts += 1
                    if K - R == 1 and row > right_heavy_max[0]:
                        right_heavy_max = (row, context)
                    if row > 1 and first_failure is None:
                        first_failure = (row, context)
    assert first_failure is not None
    witness_context = (6, 8, 1, 2)
    witness = sum(eliminated_reset(*witness_context).values(), Fraction())
    assert first_failure == (witness, witness_context)
    assert witness > 1
    return {
        "scan_scope": "2<=s<=6, 1<=K<=8, exact reachable mark closure, every B",
        "contexts": contexts,
        "lexicographic_first_failure": {
            "context": list(witness_context),
            "row": fraction_record(witness),
            "right_heavy": False,
        },
        "right_heavy_maximum_in_scan": {
            "context": list(right_heavy_max[1]),
            "row": fraction_record(right_heavy_max[0]),
        },
    }


def raw_and_power_counterexamples(include_d2: bool) -> dict[str, object]:
    raw_context = (3, 13, 12, 2)
    raw_d, raw_j = direct_split(*raw_context)
    raw_d_sum = sum(raw_d.values(), Fraction())
    raw_j_sum = sum(raw_j.values(), Fraction())
    assert raw_d_sum == Fraction(13, 14)
    assert raw_j_sum == Fraction(953, 12544)
    assert raw_d_sum + raw_j_sum == Fraction(12601, 12544) > 1

    power_rows: dict[str, object] = {}
    for label, context, exponent in (
        ("d0", (11, 1, 0, 4), 0),
        ("d1", (44, 1, 0, 30), 1),
    ):
        parent = phase_potential(context, exponent)
        deep = grouped_deep(context, exponent)
        reset = grouped_reset(context, exponent)
        total = deep + reset
        assert total > parent
        power_rows[label] = {
            "context": list(context),
            "exponent": exponent,
            "parent": fraction_record(parent),
            "deep": fraction_record(deep),
            "reset": fraction_record(reset),
            "ratio": fraction_record(total / parent),
            "strict_refutation": True,
        }

    d2: dict[str, object] = {"executed": False}
    if include_d2:
        context = (120, 1, 0, 102)
        exponent = 2
        scale = 10**30
        parent = phase_potential(context, exponent)
        deep_floor, deep_terms = grouped_deep(context, exponent, scale)
        reset_floor, reset_terms = grouped_reset(context, exponent, scale)
        total_floor = deep_floor + reset_floor
        lower = Fraction(total_floor, scale)
        assert lower > parent
        d2 = {
            "executed": True,
            "context": list(context),
            "exponent": exponent,
            "scale": str(scale),
            "deep_floor_integer": str(deep_floor),
            "reset_floor_integer": str(reset_floor),
            "deep_term_count": deep_terms,
            "reset_term_count": reset_terms,
            "parent": fraction_record(parent),
            "rigorous_lower_bound": fraction_record(lower),
            "lower_minus_parent": fraction_record(lower - parent),
            "floor_direction": (
                "Every summand is nonnegative and floor(scale*term)/scale <= term; "
                "therefore the summed floor is a rigorous lower bound."
            ),
            "strict_refutation": True,
        }

    return {
        "raw_constant": {
            "context": list(raw_context),
            "D1": fraction_record(raw_d_sum),
            "J1": fraction_record(raw_j_sum),
            "total": fraction_record(raw_d_sum + raw_j_sum),
            "strict_refutation": True,
        },
        "phase_power_rows": power_rows,
        "d2_floor_certificate": d2,
    }


def implication_audit() -> dict[str, object]:
    return {
        "status": "valid conditional implication; antecedent unresolved",
        "antecedent": "K_reset W <= W on every active right-heavy seed",
        "weight": "W=(1-q)K/(R+1)",
        "reset_target_bounds": "1/3 <= W(y)=1-q_y <= 1",
        "epoch_mass": (
            "mu_n 1 <= 3 mu_n W <= 3 W(x) <= 3 for right-heavy x"
        ),
        "descent": "mu_n=0 for n>=P(x)",
        "occupation": (
            "sum_{n<P} mu_n b <= P*3*e*P^2*(1+log P) "
            "=3eP^3(1+log P)"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--include-d2", action="store_true")
    args = parser.parse_args()
    started = time.time()
    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()
    result = {
        "claim_tested": "Fresh exact referee audit of frozen M82",
        "operator_scope": (
            "full nonlazy stationary-flow parking-degree projection in the "
            "minimal long-cycle sector; not the original heat-bath chain"
        ),
        "convention": "(pq)(x)=p(q(x)); factors displayed left-to-right",
        "arithmetic": "fractions.Fraction exact; decimal fields are annotations",
        "python": platform.python_version(),
        "repository_commit": commit,
        "seed": None,
        "imports_predecessor_code": False,
        "normalization_checks": {
            "root_mass_sums": {
                str(rank): fraction_record(sum((m for _, m in root_rows(rank)), Fraction()))
                for rank in range(2, 12)
            },
            "mean_identity_checked_by_every_direct_split_call": True,
            "D_coefficient": "rho*q_child*nu/q_parent",
            "J_coefficient": "theta^2/(Q_G*q_parent)",
            "strict_phase_descent_checked_by_every_direct_split_call": True,
        },
        "split_mass_bound": audit_split_bound(),
        "reachability": audit_reachability(),
        "grouped_vs_direct": audit_grouped_direct(),
        "eliminated_rows": audit_eliminated_rows(),
        "bellman_counterexamples": raw_and_power_counterexamples(args.include_d2),
        "conditional_occupation_implication": implication_audit(),
        "elapsed_seconds": time.time() - started,
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "elapsed_seconds": result["elapsed_seconds"],
        "d2": result["bellman_counterexamples"]["d2_floor_certificate"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
