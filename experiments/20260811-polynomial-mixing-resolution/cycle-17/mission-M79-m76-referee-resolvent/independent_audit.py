#!/usr/bin/env python3
"""Independent exact audit of the frozen M76 renewal claims.

This implementation intentionally imports no predecessor experiment code.
It uses ``Fraction`` throughout the bounded composition enumeration.  The
only floating conversions are for compact human-readable diagnostics.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import platform
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def compositions(total: int):
    if total == 0:
        yield ()
        return
    for mask in range(1 << (total - 1)):
        answer = []
        start = 0
        for position in range(total - 1):
            if mask & (1 << position):
                answer.append(position + 1 - start)
                start = position + 1
        answer.append(total - start)
        yield tuple(answer)


@functools.lru_cache(maxsize=None)
def w(a: int) -> Fraction:
    if a < 1:
        raise ValueError(a)
    return Fraction(a ** (a - 1), math.factorial(a))


def rho(s: int, comp: tuple[int, ...]) -> Fraction:
    value = Fraction(1, math.factorial(len(comp)) * w(s + 1))
    for part in comp:
        value *= w(part)
    return value


def q_split(s: int, B: int) -> Fraction:
    return w(s + 1 - B) * w(B) / w(s + 1)


def comb_ratio(n1: int, k1: int, n2: int, k2: int) -> Fraction:
    if not (0 <= k1 <= n1 and 0 <= k2 <= n2):
        return Fraction(0)
    return Fraction(math.comb(n1, k1), math.comb(n2, k2))


def contextual_value(k: int, t: int, K: int, R: int, B: int) -> Fraction:
    if t < B:
        return Fraction(0)
    if t == B:
        return K * comb_ratio(
            k + K - R - 2,
            K - R - 1,
            k + K - 1,
            K - 1,
        )
    local = w(t - B) * w(B) / w(t)
    bad = comb_ratio(K, R + 1, K + k, R + 1)
    return local * (1 - bad)


def negative_hypergeometric(K: int, R: int, k: int, j: int) -> Fraction:
    return Fraction(
        math.comb(R + j, j)
        * math.comb(K - R - 1 + k - j, k - j),
        math.comb(K + k, k),
    )


@functools.lru_cache(maxsize=None)
def rank_data(s: int):
    comps = tuple(compositions(s))
    masses = tuple(rho(s, comp) for comp in comps)
    assert sum(masses, Fraction(0)) == 1
    return comps, masses


@functools.lru_cache(maxsize=None)
def split(s: int, K: int, R: int, B: int):
    comps, masses = rank_data(s)
    values = tuple(
        contextual_value(len(comp), comp[-1], K, R, B) for comp in comps
    )
    mean = sum((mass * value for mass, value in zip(masses, values)), Fraction(0))
    assert mean == q_split(s, B), (s, K, R, B, mean, q_split(s, B))

    reset = defaultdict(Fraction)
    reset_rows = []
    base = Fraction(0)
    for refined, refined_mass in zip(comps, masses):
        k = len(refined)
        if k < 2:
            continue
        A, right = refined[0], refined[1]
        suffix = refined[1:]
        basin_current = Fraction(0)
        for comp, mass, value in zip(comps, masses, values):
            if (
                len(comp) >= len(suffix) + 1
                and comp[-len(suffix):] == suffix
                and sum(comp[:-len(suffix)]) == A
            ):
                basin_current += mass * (value - mean)
        capacity = refined_mass * k
        energy = basin_current * basin_current / (capacity * mean)
        base += energy
        child = (A + right - 1, k - 1, k - 2, right)
        reset_rows.append((refined, child, energy))
        if child[0] >= 2:
            reset[child] += energy

    deep = defaultdict(Fraction)
    for comp, mass in zip(comps, masses):
        k, t = len(comp), comp[-1]
        if t <= B:
            continue
        child_q = w(t - B) * w(B) / w(t)
        for j in range(1, k + 1):
            coefficient = (
                mass * child_q * negative_hypergeometric(K, R, k, j) / mean
            )
            child = (t - 1, K + k, R + j, B)
            if child[0] >= 2:
                deep[child] += coefficient
    return base, dict(deep), dict(reset), tuple(reset_rows)


@functools.lru_cache(maxsize=None)
def eliminated(s: int, K: int, R: int, B: int):
    if s <= 1:
        return Fraction(0), {}
    base, deep, reset, _ = split(s, K, R, B)
    total_base = base
    total_reset = defaultdict(Fraction, reset)
    for child, coefficient in deep.items():
        child_base, child_reset = eliminated(*child)
        total_base += coefficient * child_base
        for target, weight in child_reset.items():
            total_reset[target] += coefficient * weight
    return total_base, dict(total_reset)


def coefficient_A(a: int) -> Fraction:
    answer = Fraction(0)
    for comp in compositions(a):
        product = Fraction(1)
        for part in comp:
            product *= w(part)
        answer += product / math.factorial(len(comp) + 1)
    return answer


def coefficient_C(a: int) -> Fraction:
    answer = Fraction(0)
    for comp in compositions(a):
        product = Fraction(1)
        for part in comp:
            product *= w(part)
        p = len(comp)
        answer += Fraction(p + 1, math.factorial(p + 2)) * product
    return answer


def seed_formula(s: int, B: int, t: int) -> Fraction:
    q = q_split(s, B)
    p_t = w(t) * coefficient_A(s - t) / w(s + 1)
    if t < B:
        marked = Fraction(0)
    elif t == B:
        marked = w(B) * coefficient_A(s - B) / w(s + 1)
    else:
        marked = w(t - B) * w(B) * coefficient_C(s - t) / w(s + 1)
    capacity = w(s - t) * w(t) / w(s + 1)
    return (marked - q * p_t) ** 2 / (capacity * q)


def direct_seed_entry(s: int, B: int, t: int) -> Fraction:
    _, _, _, rows = split(s, 1, 0, B)
    target = (s - 1, 1, 0, t)
    return sum(
        (energy for refined, child, energy in rows if child == target),
        Fraction(0),
    )


def p_counter(s: int) -> Fraction:
    # Sum over an arbitrary prefix composition of s-1.  Lagrange inversion
    # gives C(a,p)=[z^a]T(z)^p=p*a^(a-p-1)/(a-p)!.
    a = s - 1
    A = Fraction(0)
    for p in range(1, a + 1):
        coefficient = Fraction(
            p * a ** (a - p), a * math.factorial(a - p)
        )
        A += coefficient / math.factorial(p + 1)
    return A / w(s + 1)


def audit(s_max: int, k_max: int) -> dict:
    mean_checks = 0
    descent_checks = 0
    reset_right_heavy_checks = 0
    worst_raw = None
    worst_eliminated = None
    seed_checks = 0
    seed_max_error = Fraction(0)
    finite_rows = []

    for s in range(2, s_max + 1):
        rank_worst_raw = None
        rank_worst_eliminated = None
        for K in range(1, k_max + 1):
            R = K - 1
            for B in range(1, s + 1):
                context = (s, K, R, B)
                parent_P = s + K - R
                base, deep, reset, _ = split(*context)
                mean_checks += 1
                for child in deep:
                    assert child[0] + child[1] - child[2] < parent_P
                    descent_checks += 1
                for child in reset:
                    assert child[1] - child[2] == 1
                    assert child[0] + child[1] - child[2] < parent_P
                    descent_checks += 1
                    reset_right_heavy_checks += 1

                parent_h = 1 / q_split(s, B)
                raw_h = sum(
                    (weight / q_split(child[0], child[3]) for child, weight in deep.items()),
                    Fraction(0),
                ) + sum(
                    (weight / q_split(child[0], child[3]) for child, weight in reset.items()),
                    Fraction(0),
                )
                raw_ratio = raw_h / parent_h
                _, reset_eliminated = eliminated(*context)
                eliminated_h = sum(
                    (
                        weight / q_split(child[0], child[3])
                        for child, weight in reset_eliminated.items()
                    ),
                    Fraction(0),
                )
                eliminated_ratio = eliminated_h / parent_h
                row = {
                    "s": s,
                    "K": K,
                    "R": R,
                    "B": B,
                    "raw_ratio": float(raw_ratio),
                    "eliminated_ratio": float(eliminated_ratio),
                    "raw_ratio_exact": f"{raw_ratio.numerator}/{raw_ratio.denominator}",
                    "eliminated_ratio_exact": (
                        f"{eliminated_ratio.numerator}/{eliminated_ratio.denominator}"
                    ),
                    "base": float(base),
                }
                if rank_worst_raw is None or raw_ratio > rank_worst_raw[0]:
                    rank_worst_raw = (raw_ratio, row)
                if rank_worst_eliminated is None or eliminated_ratio > rank_worst_eliminated[0]:
                    rank_worst_eliminated = (eliminated_ratio, row)
                if worst_raw is None or raw_ratio > worst_raw[0]:
                    worst_raw = (raw_ratio, row)
                if worst_eliminated is None or eliminated_ratio > worst_eliminated[0]:
                    worst_eliminated = (eliminated_ratio, row)
        finite_rows.append(
            {
                "s": s,
                "worst_raw": rank_worst_raw[1],
                "worst_eliminated": rank_worst_eliminated[1],
            }
        )

        for B in range(1, s + 1):
            for t in range(1, s):
                left = seed_formula(s, B, t)
                right = direct_seed_entry(s, B, t)
                seed_max_error = max(seed_max_error, abs(left - right))
                assert left == right, (s, B, t, left, right)
                seed_checks += 1

    counter_rows = []
    for s in (4, 8, 16, 32, 64, 128):
        K = s * s
        p = p_counter(s)
        deep = Fraction(K, K + 1)
        plain_core = deep + p * p
        log_core = deep + p * p * (1.0 + math.log(s - 1))
        counter_rows.append(
            {
                "s": s,
                "p_last_one": float(p),
                "p_lower_single_composition": float(w(s - 1) / (2 * w(s + 1))),
                "plain_core": float(plain_core),
                "plain_d2_ratio": float(Fraction(s, s + 1) ** 2 * plain_core),
                "log_d2_lower_ratio": (
                    (s / (s + 1)) ** 2
                    * log_core
                    / (1.0 + math.log(2.0))
                ),
            }
        )

    # Exact closure of mark pairs under reset-to-right-heavy and a deep step.
    reachable_constructive = []
    for K in range(2, 12):
        for R in range(1, K):
            k, j = K - 1, R
            assert 1 <= j <= k
            assert (1 + k, j) == (K, R)
            reachable_constructive.append([K, R, k, j])

    return {
        "arithmetic": "fractions.Fraction exact rational enumeration",
        "parameters": {"s_max": s_max, "k_max": k_max},
        "mean_identity_checks": mean_checks,
        "strict_P_descent_checks": descent_checks,
        "reset_right_heavy_checks": reset_right_heavy_checks,
        "seed_formula_checks": seed_checks,
        "seed_formula_max_exact_error": str(seed_max_error),
        "reachable_constructive_checks": reachable_constructive,
        "finite_inverse_q_rows": finite_rows,
        "global_worst_raw": worst_raw[1],
        "global_worst_eliminated": worst_eliminated[1],
        "counterfamily": counter_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=7)
    parser.add_argument("--k-max", type=int, default=6)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "claim_tested": "Independent exact referee audit of frozen M76",
        "finite_scope_warning": (
            "Bounded rows can refute but cannot prove the universal resolvent inequality."
        ),
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "result": audit(args.s_max, args.k_max),
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "summary": result["result"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
