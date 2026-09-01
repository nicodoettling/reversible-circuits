#!/usr/bin/env python3
"""Exact checks for M140's scalar Cayley lemma.

The universal proof is analytic.  This standalone standard-library checker
verifies every finite algebraic identity and rational margin used by it.  It
does not import predecessor experiment code.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import platform
from decimal import Decimal, getcontext
from fractions import Fraction as F
from pathlib import Path


def record(x: F) -> dict[str, str | float]:
    return {
        "numerator": str(x.numerator),
        "denominator": str(x.denominator),
        "decimal": float(x),
    }


@functools.lru_cache(None)
def weight(n: int) -> F:
    assert n >= 1
    return F(n ** (n - 1), math.factorial(n))


@functools.lru_cache(None)
def forest(n: int, p: int) -> F:
    """[z^n]T(z)^p for T=z exp(T)."""
    if (n, p) == (0, 0):
        return F(1)
    if not 1 <= p <= n:
        return F(0)
    return F(p * n ** (n - p), n * math.factorial(n - p))


def falling(a: int, p: int) -> int:
    return math.prod(range(a - p + 1, a + 1))


@functools.lru_cache(None)
def lam(a: int, k: int) -> F:
    assert a >= 1 and k >= 2
    return math.factorial(k - 1) * sum(
        (
            F(p * falling(a, p), math.factorial(p + k - 1) * a**p)
            for p in range(1, a + 1)
        ),
        F(0),
    )


def endpoint_weight(s: int, a: int, k: int) -> F:
    assert 2 <= k <= s and 1 <= a <= s - k + 1
    return (
        weight(a)
        * forest(s - a, k - 1)
        / (math.factorial(k - 1) * weight(s + 1))
    )


def binomial_tail(s: int, k: int) -> F:
    """P[Bin(s-1,1/(s+1)) >= k-1]."""
    return sum(
        (
            F(math.comb(s - 1, j) * s ** (s - 1 - j), (s + 1) ** (s - 1))
            for j in range(k - 1, s)
        ),
        F(0),
    )


def first_moment(s: int, k: int) -> F:
    return sum(
        (
            endpoint_weight(s, a, k) * lam(a, k)
            for a in range(1, s - k + 2)
        ),
        F(0),
    )


@functools.lru_cache(None)
def coefficient_c(s: int) -> F:
    return sum(
        (
            endpoint_weight(s, a, k) * lam(a, k) ** 2
            for k in range(2, s + 1)
            for a in range(1, s - k + 2)
        ),
        F(0),
    )


@functools.lru_cache(None)
def compositions(n: int) -> tuple[tuple[int, ...], ...]:
    if n == 0:
        return ((),)
    return tuple(
        (a,) + tail
        for a in range(1, n + 1)
        for tail in compositions(n - a)
    )


def rho_word(word: tuple[int, ...]) -> F:
    return math.prod(weight(a) for a in word) / (
        math.factorial(len(word)) * weight(sum(word) + 1)
    )


def basin_contains(source: tuple[int, ...], endpoint: tuple[int, ...]) -> bool:
    return any(
        sum(source[:cut]) == endpoint[0] and source[cut:] == endpoint[1:]
        for cut in range(1, len(source) + 1)
    )


def exceptional_occurrences(s: int):
    """The 31 supported L=5 prefix-basin occurrences."""
    bottom = s - 5
    rows = tuple(
        (h, prefix, prefix + (bottom + h,))
        for h in range(6)
        for prefix in compositions(5 - h)
    )
    occurrences = sorted(
        {
            (h, (sum(prefix[:cut]),) + prefix[cut:])
            for h, prefix, _ in rows
            for cut in range(1, len(prefix) + 1)
        },
        key=lambda item: (item[0], len(item[1]), item[1]),
    )
    return rows, occurrences


def poisson_one_tail(r: int) -> Decimal:
    """High-precision diagnostic only: P[Pois(1)>=r]."""
    if r <= 0:
        return Decimal(1)
    term = Decimal(1) / Decimal(math.factorial(r))
    total = term
    j = r
    threshold = Decimal(10) ** Decimal(-(getcontext().prec - 20))
    while term > threshold:
        j += 1
        term /= Decimal(j)
        total += term
    return (-Decimal(1)).exp() * total


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    failures: list[dict[str, object]] = []

    # Exact tree-EGF first moment versus the binomial tail.
    first_rows = []
    for s in range(2, 31):
        for k in range(2, s + 1):
            lhs = first_moment(s, k)
            rhs = binomial_tail(s, k)
            if lhs != rhs:
                failures.append({"kind": "first-moment", "s": s, "k": k})
            first_rows.append({"s": s, "k": k, "value": record(lhs)})

    # Self-attack the stochastic-order direction numerically.  The proof uses
    # the exact coupling Bern(p)=1[Poisson(-log(1-p))>=1], not this diagnostic.
    getcontext().prec = 420
    poisson_failures = 0
    minimum_poisson_slack: Decimal | None = None
    minimum_poisson_at = None
    for s in range(2, 121):
        assert F(s - 1, s) < 1  # (s-1)log(1+1/s)<(s-1)/s<1.
        for k in range(2, s + 1):
            lhs_f = binomial_tail(s, k)
            lhs = Decimal(lhs_f.numerator) / Decimal(lhs_f.denominator)
            rhs = poisson_one_tail(k - 1)
            slack = rhs - lhs
            if slack < 0:
                poisson_failures += 1
            if minimum_poisson_slack is None or slack < minimum_poisson_slack:
                minimum_poisson_slack = slack
                minimum_poisson_at = (s, k)
    if poisson_failures:
        failures.append({"kind": "poisson-tail-diagnostic", "count": poisson_failures})

    # Universal Pois(1) majorant U: seven exact terms plus a factorial tail.
    u_partial = sum(
        (F(2, n * (n + 2) * math.factorial(n)) for n in range(1, 8)),
        F(0),
    )
    u_tail_bound = F(1, 17920)
    u_bound = u_partial + u_tail_bound
    assert u_partial == F(10388003, 12700800)
    assert u_bound == F(41554847, 50803200) < F(409, 500)

    # Rational e upper bound used to replace exp(-(A+1)).
    e_partial = sum((F(1, math.factorial(n)) for n in range(7)), F(0))
    e_upper = e_partial + F(1, 4410)
    assert e_partial == F(1957, 720)
    assert e_upper == F(31967, 11760) < F(87, 32)

    # Uniform logarithmic bound for the selected finite correction.
    n0, u0, h0 = 96, 5, 2
    log_error = (
        F(u0**3, 3 * n0**2)
        + F(u0**3 * (u0 - 1), 3 * n0**3)
        + F(sum(r * r for r in range(1, u0 + 1)), 2 * n0**2)
        + sum((F(a * a, 2 * n0 * (n0 - a)) for a in range(1, h0 + 1)), F(0))
    )
    assert log_error == F(23612897, 2962759680) < F(1, 100)
    log_slack = F(1, 100) - log_error
    assert log_slack == F(30073499, 14813798400)
    linear_coefficients = {
        f"u={u},k={k}": F(3 * u - (k - 2) * (k - 1), 2)
        for u in range(2, 6)
        for k in range(2, 5)
    }
    assert min(linear_coefficients.values()) == 0

    selected = tuple(
        [(a, 2, F(1)) for a in range(1, 5)]
        + [(a, 3, F(9, 16)) for a in range(1, 5)]
        + [(1, 4, F(3, 8))]
    )
    l3_partial = math.factorial(2) * sum(
        (F(p, math.factorial(p + 2)) for p in range(1, 6)), F(0)
    )
    l4_partial = math.factorial(3) * sum(
        (F(p, math.factorial(p + 3)) for p in range(1, 6)), F(0)
    )
    assert l3_partial == F(473, 840) > F(9, 16)
    assert l4_partial == F(2557, 6720) > F(3, 8)

    correction_rows = []
    correction_inner = F(0)
    mass_failures = 0
    for a, k, lower_l in selected:
        u = a + 1
        lambda_ak = lam(a, k)
        assert lower_l > lambda_ak
        term = (
            weight(a)
            * F(32, 87) ** u
            / math.factorial(k - 2)
            * lambda_ak
            * (lower_l - lambda_ak)
        )
        correction_inner += term
        correction_rows.append(
            {
                "A": a,
                "k": k,
                "lambda": record(lambda_ak),
                "L_lower": record(lower_l),
                "inner_term": record(term),
            }
        )
        # Finite diagnostics for the universally proved mass lower bound.
        for s in (100, 101, 127, 200, 1000):
            lower_mass = F(99, 100) * weight(a) * F(32, 87) ** u / math.factorial(k - 2)
            if endpoint_weight(s, a, k) <= lower_mass:
                mass_failures += 1
    if mass_failures:
        failures.append({"kind": "selected-mass-diagnostic", "count": mass_failures})
    assert correction_inner == F(78988317872, 1121447071575) > F(69, 1000)
    correction_after_mass = F(99, 100) * correction_inner
    assert correction_after_mass == F(217217874148, 3115130754375)
    assert correction_after_mass > F(99, 100) * F(69, 1000)

    final_bound = F(409, 500) - F(99, 100) * F(69, 1000)
    assert final_bound == F(74969, 100000) < F(3, 4)

    # Exact normalization check for the corrected one-power exceptional
    # subtraction on the two literal small boundaries.
    subtraction_checks = []
    subtraction_failures = 0
    for s in (6, 7):
        all_words = compositions(s)
        rows, occurrences = exceptional_occurrences(s)
        assert len(rows) == 32 and len(occurrences) == 31
        for h, endpoint_prefix in occurrences:
            endpoint = endpoint_prefix + (s - 5 + h,)
            supported_sources = tuple(
                word
                for hh, prefix, word in rows
                if hh == h and basin_contains(prefix, endpoint_prefix)
            )
            full_sources = tuple(word for word in all_words if basin_contains(word, endpoint))
            a_mass = sum((rho_word(word) for word in supported_sources), F(0))
            b_mass = sum((rho_word(word) for word in full_sources), F(0))
            capacity = len(endpoint) * rho_word(endpoint)
            lambda_e = lam(endpoint[0], len(endpoint))
            ok = (
                a_mass <= b_mass
                and b_mass == capacity * lambda_e
                and b_mass * lambda_e - a_mass * lambda_e
                == (b_mass - a_mass) * lambda_e
                and b_mass * lambda_e - a_mass * lambda_e >= 0
            )
            if not ok:
                subtraction_failures += 1
        subtraction_checks.append(
            {"s": s, "occurrences": len(occurrences), "failures": subtraction_failures}
        )
    if subtraction_failures:
        failures.append({"kind": "corrected-subtraction", "count": subtraction_failures})

    c_values = {s: coefficient_c(s) for s in (6, 30, 99, 100)}
    if any(value >= F(3, 4) for value in c_values.values()):
        failures.append({"kind": "finite-C-diagnostic"})

    payload = {
        "claim": "standalone scalar Cayley bound C_s<3/4 for every s>=100",
        "scope": "auxiliary full nonlazy stationary-flow parking-degree projection only",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "first_moment": {
            "identity": "sum_A m_s(A,k)lambda(A,k)=P[Bin(s-1,1/(s+1))>=k-1]",
            "exact_row_count": len(first_rows),
            "failures": sum(1 for item in failures if item["kind"] == "first-moment"),
            "rows": first_rows,
        },
        "poisson_domination": {
            "proof": "couple each Bernoulli(p) as 1[Poisson(-log(1-p))>=1]; total Poisson parameter is (s-1)log(1+1/s)<(s-1)/s<1",
            "diagnostic_range": "2<=s<=120, 2<=k<=s",
            "diagnostic_failures": poisson_failures,
            "minimum_decimal_slack": str(minimum_poisson_slack),
            "minimum_at": list(minimum_poisson_at),
        },
        "universal_majorant": {
            "integral": "integral_0^1 (1-t^2)(exp(t)-1)/t dt",
            "series": "sum_(n>=1) 2/[n(n+2)n!]",
            "first_seven_terms": record(u_partial),
            "tail_bound": record(u_tail_bound),
            "rational_upper": record(u_bound),
            "coarse_upper": record(F(409, 500)),
        },
        "mass_lower_bound": {
            "statement": "m_s(A,k)>(99/100)w_A exp(-(A+1))/(k-2)! for s>=100 and selected pairs",
            "e_rational_upper": record(e_upper),
            "log_error_upper": record(log_error),
            "log_slack_to_1_over_100": record(log_slack),
            "linear_coefficients": {key: record(value) for key, value in linear_coefficients.items()},
            "finite_diagnostic_failures": mass_failures,
        },
        "finite_correction": {
            "selected_pairs": correction_rows,
            "L3_partial": record(l3_partial),
            "L4_partial": record(l4_partial),
            "inner_sum_D0": record(correction_inner),
            "inner_comparison": "D0>69/1000",
            "after_99_over_100_mass_factor": record(correction_after_mass),
        },
        "final_bound": {
            "calculation": "409/500-(99/100)(69/1000)",
            "value": record(final_bound),
            "strictly_below_three_quarters": final_bound < F(3, 4),
        },
        "corrected_subtraction": {
            "formula": "ordinary baseline q*b_E*lambda_E; safely subtract q*a_E*lambda_E because 0<=a_E<=b_E=c_E*lambda_E",
            "literal_checks": subtraction_checks,
            "failures": subtraction_failures,
            "rejected_formula_not_used": "a_E*lambda_E^2",
        },
        "finite_C_diagnostics": {str(s): record(value) for s, value in c_values.items()},
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
                "first_moment_rows": len(first_rows),
                "poisson_failures": poisson_failures,
                "mass_failures": mass_failures,
                "final_bound": record(final_bound),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
