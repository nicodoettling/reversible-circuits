#!/usr/bin/env python3
"""Exact two-beta signed-current audit for M157.

Standard-library only.  The implementation is standalone and imports no
predecessor experiment source or data.  The theorem-critical arithmetic uses
fractions.Fraction throughout.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import platform
from fractions import Fraction as Q
from pathlib import Path


UPoly = tuple[Q, ...]
BPoly = dict[tuple[int, int], Q]


def trim(a: list[Q] | tuple[Q, ...]) -> UPoly:
    b = list(a)
    while len(b) > 1 and not b[-1]:
        b.pop()
    return tuple(b)


def uadd(a: UPoly, b: UPoly) -> UPoly:
    out = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)


def uscale(a: UPoly, c: Q) -> UPoly:
    return trim([c * x for x in a])


def umul(a: UPoly, b: UPoly) -> UPoly:
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def umonomial(n: int, c: Q = Q(1)) -> UPoly:
    return tuple([Q(0)] * n + [c])


def ueval(a: UPoly, x: Q) -> Q:
    ans = Q(0)
    for c in reversed(a):
        ans = ans * x + c
    return ans


def bclean(a: BPoly) -> BPoly:
    return {ij: c for ij, c in a.items() if c}


def badd(a: BPoly, b: BPoly) -> BPoly:
    out = dict(a)
    for ij, c in b.items():
        out[ij] = out.get(ij, Q(0)) + c
    return bclean(out)


def bscale(a: BPoly, c: Q) -> BPoly:
    return bclean({ij: c * x for ij, x in a.items()})


def bouter(a: UPoly, b: UPoly) -> BPoly:
    return bclean({(i, j): x * y for i, x in enumerate(a) for j, y in enumerate(b)})


def bmul_separable(a: BPoly, left: UPoly, right: UPoly) -> BPoly:
    out: BPoly = {}
    for (i, j), c in a.items():
        for r, x in enumerate(left):
            if not x:
                continue
            for t, y in enumerate(right):
                if not y:
                    continue
                key = (i + r, j + t)
                out[key] = out.get(key, Q(0)) + c * x * y
    return bclean(out)


def beval(a: BPoly, u: Q, v: Q) -> Q:
    up = [Q(1)]
    vp = [Q(1)]
    if a:
        for _ in range(max(i for i, _ in a)):
            up.append(up[-1] * u)
        for _ in range(max(j for _, j in a)):
            vp.append(vp[-1] * v)
    return sum((c * up[i] * vp[j] for (i, j), c in a.items()), Q(0))


def rise(x: int, n: int) -> int:
    return math.prod(range(x, x + n))


def beta_moment(kappa: int, deficit: int, n: int) -> Q:
    assert 1 <= deficit < kappa
    return Q(rise(deficit, n), rise(kappa, n))


def beta_expectation(a: UPoly, kappa: int, deficit: int) -> Q:
    return sum((c * beta_moment(kappa, deficit, n) for n, c in enumerate(a)), Q(0))


def double_beta_expectation(a: BPoly, kappa: int, deficit: int) -> Q:
    return sum(
        (
            c
            * beta_moment(kappa, deficit, i)
            * beta_moment(kappa, deficit, j)
            for (i, j), c in a.items()
        ),
        Q(0),
    )


def diagonal_beta_expectation(a: BPoly, kappa: int, deficit: int) -> Q:
    return sum(
        (c * beta_moment(kappa, deficit, i + j) for (i, j), c in a.items()),
        Q(0),
    )


@functools.lru_cache(None)
def w(n: int) -> Q:
    assert n >= 1
    return Q(n ** (n - 1), math.factorial(n))


@functools.lru_cache(None)
def comps(n: int) -> tuple[tuple[int, ...], ...]:
    if n == 0:
        return ((),)
    return tuple((a,) + tail for a in range(1, n + 1) for tail in comps(n - a))


@functools.lru_cache(None)
def cayley(n: int, p: int) -> Q:
    if (n, p) == (0, 0):
        return Q(1)
    if not 1 <= p <= n:
        return Q(0)
    return Q(p * n ** (n - p), n * math.factorial(n - p))


def qsplit(s: int, bottom: int) -> Q:
    return w(s + 1 - bottom) * w(bottom) / w(s + 1)


def rho(source: tuple[int, ...]) -> Q:
    return math.prod(w(a) for a in source) / (
        math.factorial(len(source)) * w(sum(source) + 1)
    )


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


def point_context(source: tuple[int, ...], bottom: int) -> UPoly:
    degree = len(source)
    last = source[-1]
    if last < bottom:
        return (Q(0),)
    if last == bottom:
        return umonomial(degree - 1, Q(degree))
    out = [Q(0)] * (degree + 1)
    out[0] = qsplit(last - 1, bottom)
    out[degree] = -out[0]
    return trim(out)


@functools.lru_cache(None)
def basin_currents(s: int, bottom: int) -> tuple[tuple[tuple[int, ...], UPoly, Q], ...]:
    q = qsplit(s, bottom)
    rows = []
    for endpoint, sources in basin_structure(s):
        current: UPoly = (Q(0),)
        for source in sources:
            centered = uadd(point_context(source, bottom), (Q(-q),))
            current = uadd(current, uscale(centered, rho(source)))
        capacity = Q(len(endpoint)) * rho(endpoint)
        rows.append((endpoint, current, capacity))
    return tuple(rows)


@functools.lru_cache(None)
def reset_kernel(s: int, bottom: int) -> BPoly:
    q = qsplit(s, bottom)
    ans: BPoly = {}
    for _, current, capacity in basin_currents(s, bottom):
        ans = badd(ans, bscale(bouter(current, current), Q(1) / (q * capacity)))
    return ans


@functools.lru_cache(None)
def reset_diagonal(s: int, bottom: int) -> UPoly:
    q = qsplit(s, bottom)
    ans: UPoly = (Q(0),)
    for _, current, capacity in basin_currents(s, bottom):
        ans = uadd(ans, uscale(umul(current, current), Q(1) / (q * capacity)))
    return ans


@functools.lru_cache(None)
def root_groups(s: int) -> tuple[tuple[int, int, Q], ...]:
    rows = []
    for degree in range(1, s + 1):
        for last in range(1, s + 1):
            mass = w(last) * cayley(s - last, degree - 1) / (
                math.factorial(degree) * w(s + 1)
            )
            if mass:
                rows.append((degree, last, mass))
    assert sum((mass for _, _, mass in rows), Q(0)) == 1
    return tuple(rows)


def attachment(kappa: int, deficit: int, degree: int, x: int) -> Q:
    assert 0 <= x <= degree
    return (
        Q(math.comb(degree, x))
        * rise(deficit, x)
        * rise(kappa - deficit, degree - x)
        / rise(kappa, degree)
    )


def likelihood(degree: int, x: int) -> UPoly:
    out = [Q(0)] * (degree + 1)
    for r in range(degree - x + 1):
        out[x + r] += Q(
            math.comb(degree, x) * math.comb(degree - x, r) * ((-1) ** r)
        )
    return trim(out)


def contextual(
    degree: int, last: int, kappa: int, deficit: int, bottom: int
) -> Q:
    if last < bottom:
        return Q(0)
    if last == bottom:
        return Q(degree) * beta_moment(kappa, deficit, degree - 1)
    return qsplit(last - 1, bottom) * (
        1 - beta_moment(kappa, deficit, degree)
    )


@functools.lru_cache(None)
def exact_reset(s: int, kappa: int, deficit: int, bottom: int) -> Q:
    ans = Q(0)
    for _, current, capacity in basin_currents(s, bottom):
        mean = beta_expectation(current, kappa, deficit)
        ans += mean * mean / capacity
    return ans


@functools.lru_cache(None)
def exact_h(s: int, kappa: int, deficit: int, bottom: int) -> Q:
    ans = exact_reset(s, kappa, deficit, bottom)
    for degree, last, mass in root_groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        for x in range(degree):
            ans += (
                mass
                * attachment(kappa, deficit, degree, x)
                * exact_h(last - 1, kappa + degree, deficit + x, bottom)
            )
    return ans


@functools.lru_cache(None)
def polarized_majorant(s: int, kappa: int, deficit: int, bottom: int) -> Q:
    """Pointwise polarization; exactly the M152 Jensen value."""
    q = qsplit(s, bottom)
    ans = beta_expectation(reset_diagonal(s, bottom), kappa, deficit)
    for degree, last, mass in root_groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        child_q = qsplit(last - 1, bottom)
        for x in range(degree):
            ans += (
                mass
                * child_q
                / q
                * attachment(kappa, deficit, degree, x)
                * polarized_majorant(last - 1, kappa + degree, deficit + x, bottom)
            )
    return ans


_KERNEL_CACHE: dict[tuple[int, int, int, int], BPoly] = {}


def signed_kernel(s: int, kappa: int, deficit: int, bottom: int) -> BPoly:
    """Exact finite two-copy Bellman kernel for F=H/q."""
    key = (s, kappa, deficit, bottom)
    if key in _KERNEL_CACHE:
        return _KERNEL_CACHE[key]
    q = qsplit(s, bottom)
    ans = dict(reset_kernel(s, bottom))
    for degree, last, mass in root_groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        child_q = qsplit(last - 1, bottom)
        coefficient = mass * child_q / q
        for x in range(degree):
            probability = attachment(kappa, deficit, degree, x)
            child = signed_kernel(last - 1, kappa + degree, deficit + x, bottom)
            like = likelihood(degree, x)
            term = bmul_separable(child, like, like)
            ans = badd(ans, bscale(term, coefficient / probability))
    ans = bclean(ans)
    _KERNEL_CACHE[key] = ans
    return ans


def rec(x: Q) -> dict[str, str | float]:
    return {
        "numerator": str(x.numerator),
        "denominator": str(x.denominator),
        "decimal": float(x),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-B", type=int, default=3)
    parser.add_argument("--max-excess", type=int, default=6)
    parser.add_argument("--max-kappa", type=int, default=16)
    args = parser.parse_args()
    assert 1 <= args.max_B <= 3
    assert 0 <= args.max_excess <= 6
    assert 2 <= args.max_kappa <= 16
    failures: list[dict[str, object]] = []

    # Shared-X two-posterior RN identity, including the killed x=d term.
    transfer_rows = 0
    killed_rows = 0
    for kappa in range(2, args.max_kappa + 1):
        for deficit in range(1, kappa):
            for degree in range(1, 7):
                full_mass = Q(0)
                retained_mass = Q(0)
                for x in range(degree + 1):
                    probability = attachment(kappa, deficit, degree, x)
                    like = likelihood(degree, x)
                    term_mass = (
                        beta_expectation(like, kappa, deficit) ** 2 / probability
                    )
                    full_mass += term_mass
                    if x < degree:
                        retained_mass += term_mass
                    for left_power in range(4):
                        for right_power in range(4):
                            left_like = umul(like, umonomial(left_power))
                            right_like = umul(like, umonomial(right_power))
                            rhs = (
                                beta_expectation(left_like, kappa, deficit)
                                * beta_expectation(right_like, kappa, deficit)
                                / probability
                            )
                            lhs = (
                                probability
                                * beta_moment(kappa + degree, deficit + x, left_power)
                                * beta_moment(kappa + degree, deficit + x, right_power)
                            )
                            if lhs != rhs:
                                failures.append(
                                    {
                                        "kind": "shared-X-transfer",
                                        "state": [kappa, deficit, degree, x],
                                        "powers": [left_power, right_power],
                                    }
                                )
                            transfer_rows += 1
                killed_probability = attachment(kappa, deficit, degree, degree)
                if (
                    full_mass != 1
                    or retained_mass != 1 - killed_probability
                    or beta_expectation(likelihood(degree, degree), kappa, deficit)
                    != killed_probability
                ):
                    failures.append(
                        {"kind": "transfer-mass", "state": [kappa, deficit, degree]}
                    )
                killed_rows += 1

    # The RN kernel is genuinely state-dependent already for d=1.
    d1_a = Q(2, 1)  # (kappa,D)=(2,1): kappa/(kappa-D)
    d1_b = Q(3, 2)  # (kappa,D)=(3,1)
    if d1_a == d1_b:
        failures.append({"kind": "state-dependence"})

    # Exact reset equality under two independent beta copies.
    reset_rows = 0
    for bottom in range(1, args.max_B + 1):
        for excess in range(args.max_excess + 1):
            s = bottom + excess
            q = qsplit(s, bottom)
            kernel = reset_kernel(s, bottom)
            for kappa in range(2, args.max_kappa + 1):
                for deficit in range(1, kappa):
                    lhs = double_beta_expectation(kernel, kappa, deficit)
                    rhs = exact_reset(s, kappa, deficit, bottom) / q
                    if lhs != rhs:
                        failures.append(
                            {
                                "kind": "reset-two-copy",
                                "state": [s, kappa, deficit, bottom],
                            }
                        )
                    reset_rows += 1

    # Simplest exact pointwise-sign obstruction.  Every shared-X transfer
    # vanishes at (u,v)=(0,1), so descendants cannot repair this sign.
    sign_s, sign_kappa, sign_deficit, sign_bottom = (3, 2, 1, 1)
    sign_reset = beval(reset_kernel(sign_s, sign_bottom), Q(0), Q(1))
    sign_full = beval(
        signed_kernel(sign_s, sign_kappa, sign_deficit, sign_bottom), Q(0), Q(1)
    )
    expected_sign = Q(-165, 512)
    if sign_reset != expected_sign or sign_full != expected_sign:
        failures.append({"kind": "signed-point-witness"})

    # Exact signed-recursion equality at fresh states and the M152 witness.
    selected_states = [
        (1, 0, 2, 1),
        (1, 1, 2, 1),
        (1, 2, 2, 1),
        (2, 1, 3, 1),
        (2, 3, 5, 2),
        (3, 2, 4, 3),
        (3, 6, 2, 1),
    ]
    equality_rows = []
    for bottom, excess, kappa, deficit in selected_states:
        s = bottom + excess
        q = qsplit(s, bottom)
        kernel = signed_kernel(s, kappa, deficit, bottom)
        represented = double_beta_expectation(kernel, kappa, deficit)
        direct = exact_h(s, kappa, deficit, bottom) / q
        kernel_encoding = ";".join(
            f"{i},{j}:{c.numerator}/{c.denominator}"
            for (i, j), c in sorted(kernel.items())
        ).encode()
        if represented != direct:
            failures.append(
                {"kind": "signed-recursion", "state": [s, kappa, deficit, bottom]}
            )
        equality_rows.append(
            {
                "state_s_kappa_D_B": [s, kappa, deficit, bottom],
                "suffix_excess": excess,
                "kernel_terms": len(kernel),
                "kernel_max_bidegrees": [
                    max((i for i, _ in kernel), default=0),
                    max((j for _, j in kernel), default=0),
                ],
                "kernel_coefficient_sha256": hashlib.sha256(
                    kernel_encoding
                ).hexdigest(),
                "represented_H_over_q": rec(represented),
                "direct_H_over_q": rec(direct),
                "budget_1_minus_q": rec(1 - q),
                "budget_slack": rec(1 - q - direct),
            }
        )

    # All 21 smallest fresh right-heavy states under the assigned B,L cap.
    fresh_rows = []
    first_trace_failure = None
    for bottom in range(1, args.max_B + 1):
        for excess in range(args.max_excess + 1):
            s = bottom + excess
            q = qsplit(s, bottom)
            value = exact_h(s, 2, 1, bottom) / q
            kernel = signed_kernel(s, 2, 1, bottom)
            trace_value = diagonal_beta_expectation(kernel, 2, 1)
            trace_margin = trace_value - (1 - q)
            if trace_margin > 0 and first_trace_failure is None:
                first_trace_failure = (bottom, excess, trace_value, trace_margin)
            fresh_rows.append(
                {
                    "bottom": bottom,
                    "excess": excess,
                    "H_over_q": rec(value),
                    "budget": rec(1 - q),
                    "slack": rec(1 - q - value),
                    "passes": value <= 1 - q,
                    "actual_kernel_diagonal_trace": rec(trace_value),
                    "trace_budget_margin": rec(trace_margin),
                    "trace_passes": trace_margin <= 0,
                }
            )

    expected_trace_state = (2, 6)
    expected_trace_value = Q(
        10304304880412164262179965176912695056497059,
        12663621893778357952841743000389707366400000,
    )
    expected_trace_margin = Q(
        132628808872888410508233058471582685297059,
        12663621893778357952841743000389707366400000,
    )
    if (
        first_trace_failure is None
        or first_trace_failure[:2] != expected_trace_state
        or first_trace_failure[2] != expected_trace_value
        or first_trace_failure[3] != expected_trace_margin
    ):
        failures.append({"kind": "first-diagonal-trace-failure"})

    # Natural pointwise polarization is a valid nonnegative supersolution,
    # but its beta integral is exactly the already-refuted M152 Jensen value.
    witness_bottom, witness_excess, witness_kappa, witness_deficit = (3, 6, 2, 1)
    witness_s = witness_bottom + witness_excess
    witness_q = qsplit(witness_s, witness_bottom)
    witness_signed = exact_h(
        witness_s, witness_kappa, witness_deficit, witness_bottom
    ) / witness_q
    witness_polarized = polarized_majorant(
        witness_s, witness_kappa, witness_deficit, witness_bottom
    )
    expected_q = Q(3176523, 25000000)
    expected_signed = Q(
        884793664847325174104678035065147237189087444781,
        1562205337586660322231315333120000000000000000000,
    )
    expected_polarized = Q(
        200725034388752880197118033887607702918039504603683,
        223395363274892426079078092636160000000000000000000,
    )
    if (
        witness_q != expected_q
        or witness_signed != expected_signed
        or witness_polarized != expected_polarized
        or witness_signed > 1 - witness_q
        or witness_polarized <= 1 - witness_q
    ):
        failures.append({"kind": "M152-witness-reproduction"})

    payload = {
        "claim": "exact shared-X two-beta signed-current representation",
        "scope": "auxiliary normalized full unweighted reset excursion only",
        "python": platform.python_version(),
        "seed": None,
        "parameters": {
            "max_B": args.max_B,
            "max_excess": args.max_excess,
            "max_kappa": args.max_kappa,
            "max_transfer_degree": 6,
            "max_transfer_monomial_power": 3,
        },
        "shared_X_transfer": {
            "monomial_rows": transfer_rows,
            "mass_rows": killed_rows,
            "d1_retained_coefficients_for_states_2_1_and_3_1": [
                rec(d1_a),
                rec(d1_b),
            ],
        },
        "reset_two_copy_rows": reset_rows,
        "pointwise_sign_counterexample": {
            "state_s_kappa_D_B": [
                sign_s,
                sign_kappa,
                sign_deficit,
                sign_bottom,
            ],
            "point_u_v": ["0", "1"],
            "reset_kernel": rec(sign_reset),
            "full_kernel": rec(sign_full),
            "descendant_transfer_at_point": rec(Q(0)),
        },
        "signed_recursion_equalities": equality_rows,
        "fresh_right_heavy_rows": fresh_rows,
        "fresh_failure_count": sum(not row["passes"] for row in fresh_rows),
        "first_actual_kernel_diagonal_trace_failure": None
        if first_trace_failure is None
        else {
            "bottom": first_trace_failure[0],
            "excess": first_trace_failure[1],
            "state_s_kappa_D_B": [
                first_trace_failure[0] + first_trace_failure[1],
                2,
                1,
                first_trace_failure[0],
            ],
            "trace_value": rec(first_trace_failure[2]),
            "positive_budget_margin": rec(first_trace_failure[3]),
        },
        "M152_witness": {
            "state_s_kappa_D_B": [
                witness_s,
                witness_kappa,
                witness_deficit,
                witness_bottom,
            ],
            "q": rec(witness_q),
            "budget": rec(1 - witness_q),
            "exact_signed_H_over_q": rec(witness_signed),
            "exact_signed_budget_slack": rec(1 - witness_q - witness_signed),
            "polarized_two_copy_majorant": rec(witness_polarized),
            "polarized_budget_margin": rec(witness_polarized - (1 - witness_q)),
        },
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
                "transfer_rows": transfer_rows,
                "reset_rows": reset_rows,
                "signed_equality_rows": len(equality_rows),
                "kernel_cache_states": len(_KERNEL_CACHE),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
