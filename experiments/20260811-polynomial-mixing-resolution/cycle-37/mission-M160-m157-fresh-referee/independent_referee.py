#!/usr/bin/env python3
"""Compact clean-room exact referee for frozen M157.

Standard library only.  This file imports no experiment code or data.
All theorem-critical arithmetic is fractions.Fraction.
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


Poly = tuple[F, ...]
Kernel = dict[tuple[int, int], F]


def clean_poly(a: list[F] | tuple[F, ...]) -> Poly:
    z = list(a)
    while len(z) > 1 and z[-1] == 0:
        z.pop()
    return tuple(z)


def padd(a: Poly, b: Poly) -> Poly:
    z = [F(0)] * max(len(a), len(b))
    for i, c in enumerate(a):
        z[i] += c
    for i, c in enumerate(b):
        z[i] += c
    return clean_poly(z)


def pscale(a: Poly, c: F) -> Poly:
    return clean_poly([c * x for x in a])


def pmul(a: Poly, b: Poly) -> Poly:
    z = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z[i + j] += x * y
    return clean_poly(z)


def monomial(k: int) -> Poly:
    return tuple([F(0)] * k + [F(1)])


def peval(a: Poly, u: F) -> F:
    z = F(0)
    for c in reversed(a):
        z = z * u + c
    return z


def kadd(a: Kernel, b: Kernel) -> Kernel:
    z = dict(a)
    for ij, c in b.items():
        z[ij] = z.get(ij, F(0)) + c
    return {ij: c for ij, c in z.items() if c}


def kscale(a: Kernel, c: F) -> Kernel:
    return {ij: c * x for ij, x in a.items() if c * x}


def outer(a: Poly, b: Poly) -> Kernel:
    return {
        (i, j): x * y
        for i, x in enumerate(a)
        for j, y in enumerate(b)
        if x * y
    }


def schur_separable(a: Kernel, left: Poly, right: Poly) -> Kernel:
    z: Kernel = {}
    for (i, j), c in a.items():
        for r, x in enumerate(left):
            for t, y in enumerate(right):
                if c * x * y:
                    z[i + r, j + t] = z.get((i + r, j + t), F(0)) + c * x * y
    return {ij: c for ij, c in z.items() if c}


def keval(a: Kernel, u: F, v: F) -> F:
    return sum((c * u**i * v**j for (i, j), c in a.items()), F(0))


def rising(a: int, r: int) -> int:
    return math.prod(range(a, a + r))


def moment(kappa: int, deficit: int, r: int) -> F:
    return F(rising(deficit, r), rising(kappa, r))


def pmean(a: Poly, kappa: int, deficit: int) -> F:
    return sum((c * moment(kappa, deficit, i) for i, c in enumerate(a)), F(0))


def kmean(a: Kernel, kappa: int, deficit: int) -> F:
    return sum(
        (c * moment(kappa, deficit, i) * moment(kappa, deficit, j)
         for (i, j), c in a.items()),
        F(0),
    )


def trace_mean(a: Kernel, kappa: int, deficit: int) -> F:
    return sum((c * moment(kappa, deficit, i + j) for (i, j), c in a.items()), F(0))


@functools.lru_cache(None)
def tree_weight(n: int) -> F:
    return F(n ** (n - 1), math.factorial(n))


def split_mass(s: int, bottom: int) -> F:
    return tree_weight(s + 1 - bottom) * tree_weight(bottom) / tree_weight(s + 1)


@functools.lru_cache(None)
def compositions(n: int) -> tuple[tuple[int, ...], ...]:
    if n == 0:
        return ((),)
    return tuple((a,) + tail for a in range(1, n + 1) for tail in compositions(n - a))


def stationary(source: tuple[int, ...]) -> F:
    return math.prod(tree_weight(a) for a in source) / (
        math.factorial(len(source)) * tree_weight(sum(source) + 1)
    )


def refines_first(source: tuple[int, ...], endpoint: tuple[int, ...]) -> bool:
    return any(
        sum(source[:cut]) == endpoint[0] and source[cut:] == endpoint[1:]
        for cut in range(1, len(source) + 1)
    )


@functools.lru_cache(None)
def active_basins(s: int) -> tuple[tuple[tuple[int, ...], tuple[tuple[int, ...], ...]], ...]:
    sources = compositions(s)
    endpoints = sorted({
        (sum(source[:cut]),) + source[cut:]
        for source in sources
        for cut in range(1, len(source))
        if sum(source[:cut]) + source[cut] - 1 >= 2
    })
    return tuple((e, tuple(c for c in sources if refines_first(c, e))) for e in endpoints)


def point_context(source: tuple[int, ...], bottom: int) -> Poly:
    degree, last = len(source), source[-1]
    if last < bottom:
        return (F(0),)
    if last == bottom:
        return pscale(monomial(degree - 1), F(degree))
    q_child = split_mass(last - 1, bottom)
    z = [F(0)] * (degree + 1)
    z[0], z[degree] = q_child, -q_child
    return clean_poly(z)


@functools.lru_cache(None)
def currents(s: int, bottom: int) -> tuple[tuple[Poly, F], ...]:
    q = split_mass(s, bottom)
    ans = []
    for endpoint, basin in active_basins(s):
        cur: Poly = (F(0),)
        for source in basin:
            centered = padd(point_context(source, bottom), (F(-q),))
            cur = padd(cur, pscale(centered, stationary(source)))
        capacity = F(len(endpoint)) * stationary(endpoint)
        ans.append((cur, capacity))
    return tuple(ans)


@functools.lru_cache(None)
def reset_kernel(s: int, bottom: int) -> Kernel:
    q = split_mass(s, bottom)
    z: Kernel = {}
    for cur, capacity in currents(s, bottom):
        z = kadd(z, kscale(outer(cur, cur), F(1) / (q * capacity)))
    return z


def normalized_reset(s: int, kappa: int, deficit: int, bottom: int) -> F:
    q = split_mass(s, bottom)
    return sum(
        (pmean(cur, kappa, deficit) ** 2 / (q * capacity)
         for cur, capacity in currents(s, bottom)),
        F(0),
    )


def cayley_coefficient(n: int, p: int) -> F:
    if (n, p) == (0, 0):
        return F(1)
    if not 1 <= p <= n:
        return F(0)
    return F(p * n ** (n - p), n * math.factorial(n - p))


@functools.lru_cache(None)
def root_groups(s: int) -> tuple[tuple[int, int, F], ...]:
    rows = []
    for degree in range(1, s + 1):
        for last in range(1, s + 1):
            mass = tree_weight(last) * cayley_coefficient(s - last, degree - 1) / (
                math.factorial(degree) * tree_weight(s + 1)
            )
            if mass:
                rows.append((degree, last, mass))
    assert sum((r[2] for r in rows), F(0)) == 1
    return tuple(rows)


def branch_probability(kappa: int, deficit: int, degree: int, x: int) -> F:
    return F(math.comb(degree, x) * rising(deficit, x)
             * rising(kappa - deficit, degree - x), rising(kappa, degree))


def binomial_likelihood(degree: int, x: int) -> Poly:
    z = [F(0)] * (degree + 1)
    for r in range(degree - x + 1):
        z[x + r] += F(math.comb(degree, x) * math.comb(degree - x, r) * (-1) ** r)
    return clean_poly(z)


@functools.lru_cache(None)
def exact_value(s: int, kappa: int, deficit: int, bottom: int) -> F:
    """Direct normalized value F=H/q."""
    q = split_mass(s, bottom)
    ans = normalized_reset(s, kappa, deficit, bottom)
    for degree, last, mass in root_groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        q_child = split_mass(last - 1, bottom)
        for x in range(degree):
            ans += (mass * q_child / q
                    * branch_probability(kappa, deficit, degree, x)
                    * exact_value(last - 1, kappa + degree, deficit + x, bottom))
    return ans


@functools.lru_cache(None)
def exact_kernel(s: int, kappa: int, deficit: int, bottom: int) -> tuple[tuple[tuple[int, int], F], ...]:
    """Finite signed equality kernel, serialized for caching."""
    q = split_mass(s, bottom)
    z = dict(reset_kernel(s, bottom))
    for degree, last, mass in root_groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        coefficient = mass * split_mass(last - 1, bottom) / q
        for x in range(degree):
            probability = branch_probability(kappa, deficit, degree, x)
            child = dict(exact_kernel(last - 1, kappa + degree, deficit + x, bottom))
            likelihood = binomial_likelihood(degree, x)
            z = kadd(z, kscale(schur_separable(child, likelihood, likelihood), coefficient / probability))
    return tuple(sorted(z.items()))


@functools.lru_cache(None)
def polarized_value(s: int, kappa: int, deficit: int, bottom: int) -> F:
    """Local feature polarization followed by one-copy posterior transfer."""
    q = split_mass(s, bottom)
    ans = sum(
        (pmean(pmul(cur, cur), kappa, deficit) / (q * capacity)
         for cur, capacity in currents(s, bottom)),
        F(0),
    )
    for degree, last, mass in root_groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        coefficient = mass * split_mass(last - 1, bottom) / q
        for x in range(degree):
            ans += (coefficient * branch_probability(kappa, deficit, degree, x)
                    * polarized_value(last - 1, kappa + degree, deficit + x, bottom))
    return ans


def record(x: F) -> dict[str, str | float]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator), "decimal": float(x)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    failures: list[str] = []

    # Clean-room shared-X posterior identities on selected nontrivial states.
    posterior_rows = 0
    mass_rows = 0
    for kappa, deficit in ((2, 1), (3, 1), (5, 2), (7, 5)):
        for degree in range(1, 5):
            retained = F(0)
            killed = F(0)
            for x in range(degree + 1):
                p = branch_probability(kappa, deficit, degree, x)
                likelihood = binomial_likelihood(degree, x)
                kernel_mass = pmean(likelihood, kappa, deficit) ** 2 / p
                if x < degree:
                    retained += kernel_mass
                else:
                    killed += kernel_mass
                for a in range(3):
                    for b in range(3):
                        lhs = p * moment(kappa + degree, deficit + x, a) * moment(kappa + degree, deficit + x, b)
                        rhs = (pmean(pmul(likelihood, monomial(a)), kappa, deficit)
                               * pmean(pmul(likelihood, monomial(b)), kappa, deficit) / p)
                        if lhs != rhs:
                            failures.append("posterior-RN")
                        posterior_rows += 1
            p_kill = branch_probability(kappa, deficit, degree, degree)
            if retained != 1 - p_kill or killed != p_kill:
                failures.append("retained-killed-mass")
            mass_rows += 1

    d1_coefficients = [
        F(1) / branch_probability(2, 1, 1, 0),
        F(1) / branch_probability(3, 1, 1, 0),
    ]
    if d1_coefficients != [F(2), F(3, 2)]:
        failures.append("state-dependence")

    # Smallest-rank pointwise sign witness and exact displayed polynomial.
    expected_reset = {
        (0, 0): F(193, 1536), (1, 0): F(-1, 4), (0, 1): F(-1, 4),
        (2, 0): F(-19, 96), (0, 2): F(-19, 96), (1, 1): F(2, 3),
        (2, 1): F(1, 3), (1, 2): F(1, 3), (2, 2): F(1, 3),
    }
    small_zero = all(not reset_kernel(s, b) for s in (1, 2) for b in range(1, s + 1))
    sign_reset = keval(reset_kernel(3, 1), F(0), F(1))
    sign_full = keval(dict(exact_kernel(3, 2, 1, 1)), F(0), F(1))
    likelihood_endpoint_products_vanish = all(
        peval(binomial_likelihood(d, x), F(0)) * peval(binomial_likelihood(d, x), F(1)) == 0
        for d in range(1, 9) for x in range(d)
    )
    if (reset_kernel(3, 1) != expected_reset or not small_zero
            or sign_reset != F(-165, 512) or sign_full != sign_reset
            or not likelihood_endpoint_products_vanish):
        failures.append("smallest-sign-witness")

    # Selected exact reset and recursively propagated H/q identities.
    selected = ((3, 2, 1, 1), (8, 2, 1, 2), (9, 2, 1, 3))
    equality_rows = []
    for s, kappa, deficit, bottom in selected:
        kernel = dict(exact_kernel(s, kappa, deficit, bottom))
        represented = kmean(kernel, kappa, deficit)
        direct = exact_value(s, kappa, deficit, bottom)
        reset_two_copy = kmean(reset_kernel(s, bottom), kappa, deficit)
        reset_direct = normalized_reset(s, kappa, deficit, bottom)
        if represented != direct or reset_two_copy != reset_direct:
            failures.append("exact-recursion-or-reset")
        encoding = ";".join(
            f"{i},{j}:{c.numerator}/{c.denominator}" for (i, j), c in sorted(kernel.items())
        ).encode()
        equality_rows.append({
            "state_s_kappa_D_B": [s, kappa, deficit, bottom],
            "kernel_terms": len(kernel),
            "kernel_coefficient_sha256": hashlib.sha256(encoding).hexdigest(),
            "represented_H_over_q": record(represented),
            "direct_H_over_q": record(direct),
            "reset_two_copy": record(reset_two_copy),
            "reset_direct": record(reset_direct),
        })

    expected_digest = "771567a049b76b2a546874b32de3170b8d1be32b3c7293c1a36cd9d84dec28f4"
    if equality_rows[-1]["kernel_coefficient_sha256"] != expected_digest:
        failures.append("witness-kernel-digest")

    # Actual-history PSD diagonal trace is valid but exceeds the budget.
    trace_rows = []
    first_trace_failure = None
    for bottom in range(1, 4):
        for excess in range(7):
            s = bottom + excess
            q = split_mass(s, bottom)
            kernel = dict(exact_kernel(s, 2, 1, bottom))
            product = kmean(kernel, 2, 1)
            trace = trace_mean(kernel, 2, 1)
            if product > trace:
                failures.append("invalid-diagonal-trace")
            margin = trace - (1 - q)
            if margin > 0 and first_trace_failure is None:
                first_trace_failure = (s, 2, 1, bottom, trace, margin)
            trace_rows.append({
                "state_s_kappa_D_B": [s, 2, 1, bottom],
                "trace_minus_product_nonnegative": trace >= product,
                "trace_budget_margin": record(margin),
            })
    expected_trace = F(
        10304304880412164262179965176912695056497059,
        12663621893778357952841743000389707366400000,
    )
    expected_margin = F(
        132628808872888410508233058471582685297059,
        12663621893778357952841743000389707366400000,
    )
    if (first_trace_failure is None or first_trace_failure[:4] != (8, 2, 1, 2)
            or first_trace_failure[4] != expected_trace
            or first_trace_failure[5] != expected_margin):
        failures.append("trace-counterexample")

    # Local feature polarization reproduces the accepted M152 Jensen value.
    polarized = polarized_value(9, 2, 1, 3)
    expected_polarized = F(
        200725034388752880197118033887607702918039504603683,
        223395363274892426079078092636160000000000000000000,
    )
    q_witness = split_mass(9, 3)
    if polarized != expected_polarized or polarized <= 1 - q_witness:
        failures.append("M152-polarization")

    payload = {
        "claim": "fresh exact audit of frozen M157 two-beta representation",
        "scope": "auxiliary normalized full unweighted reset excursion only",
        "python": platform.python_version(),
        "seed": None,
        "posterior_RN_rows": posterior_rows,
        "retained_killed_mass_rows": mass_rows,
        "d1_state_dependent_coefficients": [record(x) for x in d1_coefficients],
        "smallest_sign_witness": {
            "lower_rank_reset_kernels_zero": small_zero,
            "state_s_kappa_D_B": [3, 2, 1, 1],
            "point": ["0", "1"],
            "reset_value": record(sign_reset),
            "full_value": record(sign_full),
            "all_retained_likelihood_products_vanish": likelihood_endpoint_products_vanish,
        },
        "exact_equality_rows": equality_rows,
        "diagonal_trace": {
            "checked_rows": len(trace_rows),
            "all_trace_inequalities_valid": all(r["trace_minus_product_nonnegative"] for r in trace_rows),
            "first_failure_state_s_kappa_D_B": list(first_trace_failure[:4]) if first_trace_failure else None,
            "first_failure_trace": record(first_trace_failure[4]) if first_trace_failure else None,
            "first_failure_positive_budget_margin": record(first_trace_failure[5]) if first_trace_failure else None,
        },
        "M152_local_polarization": {
            "state_s_kappa_D_B": [9, 2, 1, 3],
            "value": record(polarized),
            "positive_budget_margin": record(polarized - (1 - q_witness)),
        },
        "failure_count": len(failures),
        "failures": failures,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "failure_count": len(failures),
        "kernel_cache_states": exact_kernel.cache_info().currsize,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
