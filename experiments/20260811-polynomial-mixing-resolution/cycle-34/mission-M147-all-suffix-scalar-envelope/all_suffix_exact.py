#!/usr/bin/env python3
"""Exact audits for M147's all-suffix recurrence and scalar nonclosure.

Standard-library only.  This script imports no predecessor source or output.
All theorem-critical arithmetic uses fractions.Fraction.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import platform
from fractions import Fraction as F
from pathlib import Path


def rec(x: F) -> dict[str, str | float]:
    return {
        "numerator": str(x.numerator),
        "denominator": str(x.denominator),
        "decimal": float(x),
    }


@functools.lru_cache(None)
def w(n: int) -> F:
    assert n >= 1
    return F(n ** (n - 1), math.factorial(n))


@functools.lru_cache(None)
def comps(n: int) -> tuple[tuple[int, ...], ...]:
    if n == 0:
        return ((),)
    return tuple((a,) + tail for a in range(1, n + 1) for tail in comps(n - a))


@functools.lru_cache(None)
def cayley(n: int, p: int) -> F:
    if (n, p) == (0, 0):
        return F(1)
    if not 1 <= p <= n:
        return F(0)
    return F(p * n ** (n - p), n * math.factorial(n - p))


def rise(x: int, n: int) -> int:
    return math.prod(range(x, x + n))


def fall(x: int, n: int) -> int:
    return math.prod(range(x - n + 1, x + 1))


@functools.lru_cache(None)
def lam(first: int, degree: int) -> F:
    return math.factorial(degree - 1) * sum(
        (
            F(p * fall(first, p), math.factorial(p + degree - 1) * first**p)
            for p in range(1, first + 1)
        ),
        F(0),
    )


@functools.lru_cache(None)
def scalar_c(s: int) -> F:
    return sum(
        (
            w(first)
            * cayley(s - first, degree - 1)
            / (math.factorial(degree - 1) * w(s + 1))
            * lam(first, degree) ** 2
            for degree in range(2, s + 1)
            for first in range(1, s - degree + 2)
        ),
        F(0),
    )


def qsplit(s: int, bottom: int) -> F:
    return w(s + 1 - bottom) * w(bottom) / w(s + 1)


def attachment(kappa: int, deficit: int, degree: int, j: int) -> F:
    assert 0 <= j <= degree
    return (
        F(math.comb(degree, j))
        * rise(deficit, degree - j)
        * rise(kappa - deficit, j)
        / rise(kappa, degree)
    )


def contextual(degree: int, last: int, kappa: int, deficit: int, bottom: int) -> F:
    if last < bottom:
        return F(0)
    if last == bottom:
        return F(degree) * rise(deficit, degree - 1) / rise(kappa, degree - 1)
    return qsplit(last - 1, bottom) * (
        1 - F(rise(deficit, degree), rise(kappa, degree))
    )


@functools.lru_cache(None)
def root_groups(s: int) -> tuple[tuple[int, int, F], ...]:
    rows = []
    for degree in range(1, s + 1):
        for last in range(1, s + 1):
            mass = w(last) * cayley(s - last, degree - 1) / (
                math.factorial(degree) * w(s + 1)
            )
            if mass:
                rows.append((degree, last, mass))
    assert sum((mass for _, _, mass in rows), F(0)) == 1
    return tuple(rows)


def in_basin(source: tuple[int, ...], endpoint: tuple[int, ...]) -> bool:
    return any(
        sum(source[:cut]) == endpoint[0] and source[cut:] == endpoint[1:]
        for cut in range(1, len(source) + 1)
    )


@functools.lru_cache(None)
def basin_structure(s: int):
    sources = comps(s)
    endpoints = sorted(
        {
            (sum(source[:cut]),) + source[cut:]
            for source in sources
            if len(source) >= 2
            for cut in range(1, len(source))
            if sum(source[:cut]) + source[cut] - 1 >= 2
        },
        key=lambda x: (len(x), x),
    )
    return tuple(
        (endpoint, tuple(source for source in sources if in_basin(source, endpoint)))
        for endpoint in endpoints
    )


@functools.lru_cache(None)
def reset(s: int, kappa: int, deficit: int, bottom: int) -> F:
    q = qsplit(s, bottom)
    mass = {
        source: math.prod(w(a) for a in source)
        / (math.factorial(len(source)) * w(s + 1))
        for source in comps(s)
    }
    ans = F(0)
    for endpoint, sources in basin_structure(s):
        theta = sum(
            (
                mass[source]
                * (contextual(len(source), source[-1], kappa, deficit, bottom) - q)
                for source in sources
            ),
            F(0),
        )
        capacity = len(endpoint) * mass[endpoint]
        ans += theta * theta / capacity
    return ans


@functools.lru_cache(None)
def children(s: int, kappa: int, deficit: int, bottom: int):
    rows = []
    for degree, last, mass in root_groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        assert sum(
            (attachment(kappa, deficit, degree, j) for j in range(degree + 1)),
            F(0),
        ) == 1
        for j in range(1, degree + 1):
            nu = attachment(kappa, deficit, degree, j)
            if nu:
                rows.append(
                    (
                        mass * nu,
                        (last - 1, kappa + degree, deficit + degree - j, bottom),
                        degree,
                        last,
                        j,
                    )
                )
    return tuple(rows)


@functools.lru_cache(None)
def H(s: int, kappa: int, deficit: int, bottom: int) -> F:
    return reset(s, kappa, deficit, bottom) + sum(
        (mass * H(*child) for mass, child, _, _, _ in children(s, kappa, deficit, bottom)),
        F(0),
    )


def normalized_rhs(s: int, kappa: int, deficit: int, bottom: int) -> F:
    q = qsplit(s, bottom)
    answer = reset(s, kappa, deficit, bottom) / q
    for mass, child, _, _, _ in children(s, kappa, deficit, bottom):
        child_q = qsplit(child[0], bottom)
        answer += mass / q * child_q * (H(*child) / child_q)
    return answer


def suffix_rows(bottom: int, excess: int, kappa: int, deficit: int):
    ratios = tuple(w(bottom + excess - i) / w(bottom + excess - i + 1) for i in range(excess + 1))
    q = w(excess + 1) * math.prod(ratios)
    rows = []
    for h in range(excess + 1):
        product = math.prod(ratios[-h:]) if h else F(1)
        for prefix in comps(excess - h):
            degree = len(prefix) + 1
            mass = math.prod(w(a) for a in prefix) / (
                math.factorial(degree) * w(excess + 1) * product
            )
            mean = contextual(degree, bottom + h, kappa, deficit, bottom)
            source = prefix + (bottom + h,)
            literal_mass = (
                math.prod(w(a) for a in source)
                / (math.factorial(degree) * w(bottom + excess + 1))
                / q
            )
            assert mass == literal_mass
            rows.append((h, prefix, degree, mass, mean))
    assert len(rows) == 2**excess
    assert q == qsplit(bottom + excess, bottom)
    assert sum((mass * mean for _, _, _, mass, mean in rows), F(0)) == 1
    for h in range(excess + 1):
        product = math.prod(ratios[-h:]) if h else F(1)
        for degree in range(1, excess - h + 2):
            grouped = sum(
                (mass for hh, _, dd, mass, _ in rows if hh == h and dd == degree),
                F(0),
            )
            formula = cayley(excess - h, degree - 1) / (
                math.factorial(degree) * w(excess + 1) * product
            )
            assert grouped == formula
    return tuple(rows), q


def l1_formula(kappa: int, deficit: int) -> F:
    q = F(3, 8)
    p = F(deficit, kappa)
    return F(1, 16) + (2 * p - q) ** 2 / 4


def moment_pair(r: int, kappa: int):
    n = r + 1
    den = 2 ** (n - 1)
    even = {1 + i: F(math.comb(n, i), den) for i in range(n + 1) if i % 2 == 0}
    odd = {1 + i: F(math.comb(n, i), den) for i in range(n + 1) if i % 2 == 1}
    assert sum(even.values(), F(0)) == sum(odd.values(), F(0)) == 1

    def expect(mu, fn):
        return sum((mass * fn(d) for d, mass in mu.items()), F(0))

    equal = []
    for power in range(r + 1):
        a = expect(even, lambda d, power=power: d**power)
        b = expect(odd, lambda d, power=power: d**power)
        equal.append(a == b)
    high_a = expect(even, lambda d: rise(d, n))
    high_b = expect(odd, lambda d: rise(d, n))
    killed_a = high_a / rise(kappa, n)
    killed_b = high_b / rise(kappa, n)
    expected_difference = F((-1) ** n * math.factorial(n), 2 ** (n - 1))
    assert high_a - high_b == expected_difference
    return {
        "r": r,
        "kappa": kappa,
        "support": [1, r + 2],
        "low_moments_equal": all(equal),
        "high_rising_difference": rec(high_a - high_b),
        "expected_high_difference": rec(expected_difference),
        "killed_mass_difference": rec(killed_a - killed_b),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    failures = []

    attachment_rows = []
    for kappa in (2, 5, 11, 35):
        for deficit in range(1, kappa - 1):
            for degree in range(1, 7):
                total = sum(
                    (attachment(kappa, deficit, degree, j) for j in range(degree + 1)),
                    F(0),
                )
                if total != 1:
                    failures.append({"kind": "attachment-sum", "state": [kappa, deficit, degree]})
                attachment_rows.append((kappa, deficit, degree))

    suffix_audits = []
    for bottom, excess, kappa, deficit in (
        (1, 1, 33, 31),
        (1, 3, 65, 63),
        (1, 4, 4097, 4095),
        (2, 1, 33, 31),
        (2, 2, 7, 3),
        (2, 3, 6, 1),
        (3, 3, 9, 4),
        (2, 4, 3, 1),
    ):
        rows, q = suffix_rows(bottom, excess, kappa, deficit)
        s = bottom + excess
        rhs = normalized_rhs(s, kappa, deficit, bottom)
        lhs = H(s, kappa, deficit, bottom) / q
        if lhs != rhs:
            failures.append({"kind": "normalized-recurrence", "state": [s, kappa, deficit, bottom]})
        suffix_audits.append(
            {
                "state_s_kappa_D_B": [s, kappa, deficit, bottom],
                "support_count": len(rows),
                "q": rec(q),
                "H_over_q": rec(lhs),
                "rhs": rec(rhs),
            }
        )

    boundary_rows = []
    for K in (1, 2, 31, 32, 64, 4096):
        for label, deficit in (("right-heavy", 1), ("R=1", K - 1)):
            if deficit < 1:
                continue
            kappa = K + 1
            actual = H(3, kappa, deficit, 2) / F(3, 8)
            formula = l1_formula(kappa, deficit)
            if actual != formula:
                failures.append({"kind": "l1-formula", "K": K, "label": label})
            boundary_rows.append(
                {
                    "K": K,
                    "label": label,
                    "deficit": deficit,
                    "p": rec(F(deficit, kappa)),
                    "H_over_q": rec(actual),
                    "formula": rec(formula),
                    "margin_over_local_budget": rec(actual - F(5, 8)),
                }
            )

    if l1_formula(32 + 1, 31) != F(175033, 278784):
        failures.append({"kind": "first-witness-normalized"})
    if scalar_c(3) != F(9, 32):
        failures.append({"kind": "scalar-C3"})
    if H(3, 33, 31, 2) != F(175033, 743424):
        failures.append({"kind": "first-witness-absolute"})
    if H(3, 33, 1, 2) != F(24313, 743424):
        failures.append({"kind": "paired-right-heavy"})
    if H(3, 33, 31, 2) - F(15, 64) != F(793, 743424):
        failures.append({"kind": "first-witness-margin"})
    if len(basin_structure(3)) != 2:
        failures.append({"kind": "first-witness-basin-count"})
    if any(reset(*child) != 0 for _, child, _, _, _ in children(3, 33, 31, 2)):
        failures.append({"kind": "first-witness-child-reset"})
    if l1_formula(32, 30) != F(5, 8):
        failures.append({"kind": "threshold-equality-K31"})

    reachability = []
    for K in (32, 64, 4096):
        degree = K - 1
        parent = (K + 2, 2, 1, 2)  # (s,kappa,D,B), fresh K=1,R=0.
        child = (3, parent[1] + degree, parent[2] + degree - 1, 2)
        probability = attachment(2, 1, degree, 1)
        expected = (3, K + 1, K - 1, 2)
        if child != expected or probability != F(1, K):
            failures.append({"kind": "reachability", "K": K})
        reachability.append(
            {
                "K": K,
                "parent_s_kappa_D_B": list(parent),
                "degree": degree,
                "last_part": 4,
                "rank_j": 1,
                "attachment_probability": rec(probability),
                "child_s_kappa_D_B": list(child),
            }
        )

    moments = [moment_pair(r, r + 4) for r in range(0, 9)]
    if not all(row["low_moments_equal"] for row in moments):
        failures.append({"kind": "moment-cancellation"})

    payload = {
        "claim": "all-suffix functional recurrence and deficit-blind scalar nonclosure",
        "scope": "auxiliary full unweighted nonlazy reset excursion only",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "parameters": {
            "attachment_kappa": [2, 5, 11, 35],
            "attachment_degree_max": 6,
            "suffix_cases": len(suffix_audits),
            "boundary_K": [1, 2, 31, 32, 64, 4096],
            "moment_r": [0, 8],
        },
        "attachment_normalization_rows": len(attachment_rows),
        "suffix_recurrence_audits": suffix_audits,
        "boundary_rows": boundary_rows,
        "first_witness": {
            "bad_state_s_K_R_B": [3, 32, 1, 2],
            "C_3": rec(scalar_c(3)),
            "bad_H": rec(F(175033, 743424)),
            "right_heavy_state_s_K_R_B": [3, 32, 31, 2],
            "right_heavy_H": rec(F(24313, 743424)),
            "budget": rec(F(15, 64)),
            "bad_margin": rec(F(793, 743424)),
            "threshold": "R=1 family equals budget at K=31 and exceeds it iff K>=32",
            "identical_recorded_data": ["L", "B", "s", "q", "C_s", "all Cayley ratios", "K", "z"],
            "missing_coordinate": "D=K-R (equivalently p=D/(K+1))",
        },
        "reachability": reachability,
        "moment_obstructions": moments,
        "failure_count": len(failures),
        "failures": failures,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
                "failure_count": len(failures),
                "attachment_rows": len(attachment_rows),
                "suffix_cases": len(suffix_audits),
                "boundary_rows": len(boundary_rows),
                "moment_rows": len(moments),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
