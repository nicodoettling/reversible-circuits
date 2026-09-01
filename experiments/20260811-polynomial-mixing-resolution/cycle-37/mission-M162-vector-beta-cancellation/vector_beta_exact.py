#!/usr/bin/env python3
"""Exact vector/Jacobi cancellation audit for M162.

This is a standalone, standard-library-only implementation.  Every
theorem-critical calculation uses fractions.Fraction.  It reconstructs the
accepted all-suffix signed kernel from definitions and then resolves its
actual history-feature energy into monic orthogonal polynomials for the
state's Beta(D,kappa-D) law.
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
    out = list(a)
    while len(out) > 1 and not out[-1]:
        out.pop()
    return tuple(out)


def uadd(a: UPoly, b: UPoly) -> UPoly:
    out = [Q(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return trim(out)


def uscale(a: UPoly, scalar: Q) -> UPoly:
    return trim([scalar * value for value in a])


def umul(a: UPoly, b: UPoly) -> UPoly:
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return trim(out)


def umonomial(degree: int, coefficient: Q = Q(1)) -> UPoly:
    return tuple([Q(0)] * degree + [coefficient])


def bclean(a: BPoly) -> BPoly:
    return {key: value for key, value in a.items() if value}


def badd(a: BPoly, b: BPoly) -> BPoly:
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, Q(0)) + value
    return bclean(out)


def bscale(a: BPoly, scalar: Q) -> BPoly:
    return bclean({key: scalar * value for key, value in a.items()})


def bouter(a: UPoly, b: UPoly) -> BPoly:
    return bclean(
        {(i, j): left * right for i, left in enumerate(a) for j, right in enumerate(b)}
    )


def bmul_separable(a: BPoly, left: UPoly, right: UPoly) -> BPoly:
    out: BPoly = {}
    for (i, j), coefficient in a.items():
        for r, left_value in enumerate(left):
            if not left_value:
                continue
            for t, right_value in enumerate(right):
                if not right_value:
                    continue
                key = (i + r, j + t)
                out[key] = out.get(key, Q(0)) + coefficient * left_value * right_value
    return bclean(out)


def rise(start: int, length: int) -> int:
    return math.prod(range(start, start + length))


def beta_moment(kappa: int, deficit: int, degree: int) -> Q:
    assert 1 <= deficit < kappa
    return Q(rise(deficit, degree), rise(kappa, degree))


def beta_expectation(poly: UPoly, kappa: int, deficit: int) -> Q:
    return sum(
        (coefficient * beta_moment(kappa, deficit, degree)
         for degree, coefficient in enumerate(poly)),
        Q(0),
    )


def double_beta_expectation(kernel: BPoly, kappa: int, deficit: int) -> Q:
    return sum(
        (coefficient * beta_moment(kappa, deficit, i)
         * beta_moment(kappa, deficit, j)
         for (i, j), coefficient in kernel.items()),
        Q(0),
    )


def diagonal_beta_expectation(kernel: BPoly, kappa: int, deficit: int) -> Q:
    return sum(
        (coefficient * beta_moment(kappa, deficit, i + j)
         for (i, j), coefficient in kernel.items()),
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
    return tuple((head,) + tail for head in range(1, n + 1) for tail in comps(n - head))


@functools.lru_cache(None)
def cayley(n: int, parts: int) -> Q:
    if (n, parts) == (0, 0):
        return Q(1)
    if not 1 <= parts <= n:
        return Q(0)
    return Q(parts * n ** (n - parts), n * math.factorial(n - parts))


def qsplit(s: int, bottom: int) -> Q:
    return w(s + 1 - bottom) * w(bottom) / w(s + 1)


def rho(source: tuple[int, ...]) -> Q:
    return math.prod(w(part) for part in source) / (
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
        key=lambda endpoint: (len(endpoint), endpoint),
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
    out: BPoly = {}
    for _, current, capacity in basin_currents(s, bottom):
        out = badd(out, bscale(bouter(current, current), Q(1) / (q * capacity)))
    return out


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


def attachment(kappa: int, deficit: int, degree: int, observed_x: int) -> Q:
    return (
        Q(math.comb(degree, observed_x))
        * rise(deficit, observed_x)
        * rise(kappa - deficit, degree - observed_x)
        / rise(kappa, degree)
    )


def likelihood(degree: int, observed_x: int) -> UPoly:
    """L_x(u)=binom(d,x)u^x(1-u)^(d-x)."""
    out = [Q(0)] * (degree + 1)
    for extra in range(degree - observed_x + 1):
        out[observed_x + extra] += Q(
            math.comb(degree, observed_x)
            * math.comb(degree - observed_x, extra)
            * ((-1) ** extra)
        )
    return trim(out)


@functools.lru_cache(None)
def exact_reset(s: int, kappa: int, deficit: int, bottom: int) -> Q:
    out = Q(0)
    for _, current, capacity in basin_currents(s, bottom):
        mean = beta_expectation(current, kappa, deficit)
        out += mean * mean / capacity
    return out


@functools.lru_cache(None)
def exact_h(s: int, kappa: int, deficit: int, bottom: int) -> Q:
    out = exact_reset(s, kappa, deficit, bottom)
    for degree, last, mass in root_groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        for observed_x in range(degree):
            out += (
                mass
                * attachment(kappa, deficit, degree, observed_x)
                * exact_h(last - 1, kappa + degree, deficit + observed_x, bottom)
            )
    return out


_KERNEL_CACHE: dict[tuple[int, int, int, int], BPoly] = {}


def signed_kernel(s: int, kappa: int, deficit: int, bottom: int) -> BPoly:
    """K_x for F=H/q, reconstructed without predecessor imports."""
    key = (s, kappa, deficit, bottom)
    if key in _KERNEL_CACHE:
        return _KERNEL_CACHE[key]
    q = qsplit(s, bottom)
    out = dict(reset_kernel(s, bottom))
    for degree, last, mass in root_groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        child_q = qsplit(last - 1, bottom)
        exterior = mass * child_q / q
        for observed_x in range(degree):
            probability = attachment(kappa, deficit, degree, observed_x)
            child = signed_kernel(
                last - 1, kappa + degree, deficit + observed_x, bottom
            )
            like = likelihood(degree, observed_x)
            lifted = bmul_separable(child, like, like)
            out = badd(out, bscale(lifted, exterior / probability))
    out = bclean(out)
    _KERNEL_CACHE[key] = out
    return out


def inner(a: UPoly, b: UPoly, kappa: int, deficit: int) -> Q:
    return beta_expectation(umul(a, b), kappa, deficit)


@functools.lru_cache(None)
def monic_beta_orthogonal(kappa: int, deficit: int, max_degree: int):
    """Monic shifted-Jacobi system by exact Gram--Schmidt.

    This convention avoids ambiguity in Jacobi parameter/order and keeps all
    coefficients and squared norms rational.
    """
    polys: list[UPoly] = []
    norms: list[Q] = []
    for degree in range(max_degree + 1):
        poly = umonomial(degree)
        for previous, norm in zip(polys, norms):
            coefficient = inner(poly, previous, kappa, deficit) / norm
            poly = uadd(poly, uscale(previous, -coefficient))
        norm = inner(poly, poly, kappa, deficit)
        assert norm > 0 and len(poly) == degree + 1 and poly[-1] == 1
        polys.append(poly)
        norms.append(norm)
    return tuple(polys), tuple(norms)


def jacobi_energy(
    kernel: BPoly, poly: UPoly, norm: Q, kappa: int, deficit: int
) -> Q:
    """||E[P(U) Phi(U)]||^2/E[P(U)^2], from K=<Phi,Phi>."""
    left_moments: dict[int, Q] = {}
    right_moments: dict[int, Q] = {}
    for i, _ in kernel:
        if i not in left_moments:
            left_moments[i] = beta_expectation(
                umul(umonomial(i), poly), kappa, deficit
            )
    for _, j in kernel:
        if j not in right_moments:
            right_moments[j] = beta_expectation(
                umul(umonomial(j), poly), kappa, deficit
            )
    value = sum(
        (coefficient * left_moments[i] * right_moments[j]
         for (i, j), coefficient in kernel.items()),
        Q(0),
    ) / norm
    return value


def kernel_bilinear(
    kernel: BPoly,
    left: UPoly,
    right: UPoly,
    kappa: int,
    deficit: int,
) -> Q:
    """<E[left(U)Phi(U)], E[right(U)Phi(U)]>."""
    left_moments: dict[int, Q] = {}
    right_moments: dict[int, Q] = {}
    for i, _ in kernel:
        if i not in left_moments:
            left_moments[i] = beta_expectation(
                umul(umonomial(i), left), kappa, deficit
            )
    for _, j in kernel:
        if j not in right_moments:
            right_moments[j] = beta_expectation(
                umul(umonomial(j), right), kappa, deficit
            )
    return sum(
        (coefficient * left_moments[i] * right_moments[j]
         for (i, j), coefficient in kernel.items()),
        Q(0),
    )


def rec(value: Q) -> dict[str, str | float]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


def poly_record(poly: UPoly, norm: Q) -> dict[str, object]:
    return {
        "coefficients_low_to_high": [f"{x.numerator}/{x.denominator}" for x in poly],
        "squared_norm": rec(norm),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-B", type=int, default=3)
    parser.add_argument("--max-excess", type=int, default=6)
    parser.add_argument("--max-kappa", type=int, default=8)
    args = parser.parse_args()
    assert 1 <= args.max_B <= 3
    assert 0 <= args.max_excess <= 6
    assert 2 <= args.max_kappa <= 8

    failures: list[dict[str, object]] = []

    # The shared-X vector identity is checked on arbitrary vector monomial
    # pairs.  Its scalar coordinates imply the Hilbert-valued statement.
    transfer_rows = 0
    killed_rows = 0
    for kappa in range(2, args.max_kappa + 1):
        for deficit in range(1, kappa):
            for degree in range(1, 7):
                retained_mass = Q(0)
                for observed_x in range(degree + 1):
                    probability = attachment(kappa, deficit, degree, observed_x)
                    like = likelihood(degree, observed_x)
                    joint_mass = beta_expectation(like, kappa, deficit) ** 2 / probability
                    if observed_x < degree:
                        retained_mass += joint_mass
                    for left_power in range(4):
                        for right_power in range(4):
                            right_side = (
                                beta_expectation(
                                    umul(like, umonomial(left_power)), kappa, deficit
                                )
                                * beta_expectation(
                                    umul(like, umonomial(right_power)), kappa, deficit
                                )
                                / probability
                            )
                            left_side = (
                                probability
                                * beta_moment(
                                    kappa + degree, deficit + observed_x, left_power
                                )
                                * beta_moment(
                                    kappa + degree, deficit + observed_x, right_power
                                )
                            )
                            if left_side != right_side:
                                failures.append(
                                    {
                                        "kind": "shared-X-vector-transfer",
                                        "state": [kappa, deficit, degree, observed_x],
                                        "powers": [left_power, right_power],
                                    }
                                )
                            transfer_rows += 1
                killed_probability = attachment(kappa, deficit, degree, degree)
                if retained_mass != 1 - killed_probability:
                    failures.append(
                        {"kind": "retained-killed-mass", "state": [kappa, deficit, degree]}
                    )
                killed_rows += 1

    right_heavy_rows = []
    first_r1_failure = None
    max_minimal_r = -1
    max_minimal_states: list[list[int]] = []
    exact_target_failures = 0
    total_energy_checks = 0
    first_mode_recursion_rows = 0
    first_mode_recursion_failures = 0

    for bottom in range(1, args.max_B + 1):
        for excess in range(args.max_excess + 1):
            s = bottom + excess
            q = qsplit(s, bottom)
            budget = 1 - q
            for kappa in range(2, args.max_kappa + 1):
                for deficit in range(1, kappa):
                    kernel = signed_kernel(s, kappa, deficit, bottom)
                    degree = max(
                        max((i for i, _ in kernel), default=0),
                        max((j for _, j in kernel), default=0),
                    )
                    polys, norms = monic_beta_orthogonal(kappa, deficit, degree)
                    energies = [
                        jacobi_energy(kernel, poly, norm, kappa, deficit)
                        for poly, norm in zip(polys, norms)
                    ]
                    total_energy_checks += len(energies)
                    trace = diagonal_beta_expectation(kernel, kappa, deficit)
                    exact = double_beta_expectation(kernel, kappa, deficit)
                    direct = exact_h(s, kappa, deficit, bottom) / q
                    if (
                        any(energy < 0 for energy in energies)
                        or sum(energies, Q(0)) != trace
                        or energies[0] != exact
                        or exact != direct
                    ):
                        failures.append(
                            {
                                "kind": "jacobi-parseval-or-exact-value",
                                "state": [s, kappa, deficit, bottom],
                            }
                        )

                    # Exact vector-valued one-step recursion for the first
                    # centered Jacobi energy.  With C_y=E[(U-p_y)Phi_y], a
                    # retained branch contributes
                    # ext*p_x/Var_parent * ||(p_y-p)M_y+C_y||^2.
                    # The x=d branch is absent, exactly matching killing.
                    parent_mean = Q(deficit, kappa)
                    parent_center = (Q(-parent_mean), Q(1))
                    parent_variance = beta_moment(kappa, deficit, 2) - parent_mean**2
                    reset_first = kernel_bilinear(
                        reset_kernel(s, bottom),
                        parent_center,
                        parent_center,
                        kappa,
                        deficit,
                    ) / parent_variance
                    recursive_first = reset_first
                    for branch_degree, last, mass in root_groups(s):
                        if last <= bottom or last - 1 < 2:
                            continue
                        child_q = qsplit(last - 1, bottom)
                        exterior = mass * child_q / q
                        for observed_x in range(branch_degree):
                            probability = attachment(
                                kappa, deficit, branch_degree, observed_x
                            )
                            child_kappa = kappa + branch_degree
                            child_deficit = deficit + observed_x
                            child_mean = Q(child_deficit, child_kappa)
                            delta = child_mean - parent_mean
                            child_center = (Q(-child_mean), Q(1))
                            child_kernel = signed_kernel(
                                last - 1, child_kappa, child_deficit, bottom
                            )
                            child_constant = double_beta_expectation(
                                child_kernel, child_kappa, child_deficit
                            )
                            child_mixed = kernel_bilinear(
                                child_kernel,
                                child_center,
                                (Q(1),),
                                child_kappa,
                                child_deficit,
                            )
                            child_centered_norm = kernel_bilinear(
                                child_kernel,
                                child_center,
                                child_center,
                                child_kappa,
                                child_deficit,
                            )
                            recursive_first += (
                                exterior
                                * probability
                                * (
                                    delta * delta * child_constant
                                    + 2 * delta * child_mixed
                                    + child_centered_norm
                                )
                                / parent_variance
                            )
                    direct_first = energies[1] if degree >= 1 else Q(0)
                    if recursive_first != direct_first:
                        first_mode_recursion_failures += 1
                        failures.append(
                            {
                                "kind": "first-jacobi-vector-recursion",
                                "state": [s, kappa, deficit, bottom],
                            }
                        )
                    first_mode_recursion_rows += 1
                    upper_bounds = []
                    removed = Q(0)
                    for truncation in range(degree + 1):
                        if truncation:
                            removed += energies[truncation]
                        bound = trace - removed
                        upper_bounds.append(bound)
                        if bound < exact:
                            failures.append(
                                {
                                    "kind": "truncated-bound-below-exact",
                                    "state": [s, kappa, deficit, bottom],
                                    "truncation": truncation,
                                }
                            )
                    if upper_bounds[-1] != exact:
                        failures.append(
                            {
                                "kind": "full-degree-not-exact",
                                "state": [s, kappa, deficit, bottom],
                            }
                        )
                    minimal_r = next(
                        (index for index, bound in enumerate(upper_bounds) if bound <= budget),
                        None,
                    )
                    if exact > budget:
                        exact_target_failures += 1
                    if deficit == 1:
                        r1 = upper_bounds[min(1, degree)]
                        row = {
                            "bottom": bottom,
                            "excess": excess,
                            "kappa": kappa,
                            "state_s_kappa_D_B": [s, kappa, deficit, bottom],
                            "degree": degree,
                            "q": rec(q),
                            "budget": rec(budget),
                            "exact_H_over_q": rec(exact),
                            "trace": rec(trace),
                            "degree_one_energy": rec(energies[1] if degree >= 1 else Q(0)),
                            "degree_one_bound": rec(r1),
                            "degree_one_margin": rec(r1 - budget),
                            "degree_one_passes": r1 <= budget,
                            "minimal_jacobi_truncation_for_budget": minimal_r,
                            "energies": [rec(value) for value in energies],
                        }
                        right_heavy_rows.append(row)
                        if r1 > budget and first_r1_failure is None:
                            first_r1_failure = row
                        if minimal_r is not None:
                            if minimal_r > max_minimal_r:
                                max_minimal_r = minimal_r
                                max_minimal_states = [[s, kappa, deficit, bottom]]
                            elif minimal_r == max_minimal_r:
                                max_minimal_states.append([s, kappa, deficit, bottom])

    # A state with a nonzero first Jacobi mode must strictly improve trace.
    strict_rows = sum(
        row["degree_one_energy"]["numerator"] != "0" for row in right_heavy_rows
    )
    if strict_rows == 0:
        failures.append({"kind": "no-strict-degree-one-improvement"})

    # Record the monic convention explicitly in two asymmetric beta laws;
    # this audits parameter order and changing state normalization.
    jacobi_examples = []
    for kappa, deficit in ((2, 1), (5, 1), (5, 4)):
        polys, norms = monic_beta_orthogonal(kappa, deficit, 3)
        jacobi_examples.append(
            {
                "state_kappa_D": [kappa, deficit],
                "polynomials": [poly_record(poly, norm) for poly, norm in zip(polys, norms)],
            }
        )

    first_failure_record = first_r1_failure
    repair_rows = [
        row for row in right_heavy_rows
        if row["minimal_jacobi_truncation_for_budget"] == 1
    ]
    nontrivial_rows = [row for row in right_heavy_rows if row["excess"] > 0]
    tightest_nontrivial = max(
        nontrivial_rows,
        key=lambda row: Q(
            int(row["degree_one_margin"]["numerator"]),
            int(row["degree_one_margin"]["denominator"]),
        ),
    )
    minimal_truncation_counts = {
        str(index): sum(
            row["minimal_jacobi_truncation_for_budget"] == index
            for row in right_heavy_rows
        )
        for index in range(args.max_excess + 1)
    }
    payload = {
        "claim": "actual-history vector beta/Jacobi cancellation decomposition",
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
        "shared_X_vector_transfer": {
            "monomial_pair_rows": transfer_rows,
            "retained_killed_mass_rows": killed_rows,
        },
        "jacobi_convention_examples": jacobi_examples,
        "state_count": first_mode_recursion_rows,
        "jacobi_energy_count": total_energy_checks,
        "first_jacobi_vector_recursion": {
            "checked_rows": first_mode_recursion_rows,
            "failure_count": first_mode_recursion_failures,
            "formula": "reset_E1 + sum_retained ext*p_x/Var_parent * ||(p_child-p_parent)M_child+C_child||^2",
            "killed_observation": "x=d omitted exactly",
        },
        "right_heavy_state_count": len(right_heavy_rows),
        "strict_degree_one_improvement_count": strict_rows,
        "first_degree_one_budget_failure": first_failure_record,
        "maximum_minimal_truncation_on_right_heavy_grid": max_minimal_r,
        "states_attaining_maximum_minimal_truncation": max_minimal_states,
        "minimal_truncation_counts_on_right_heavy_grid": minimal_truncation_counts,
        "degree_one_repair_rows": repair_rows,
        "tightest_nontrivial_degree_one_row": tightest_nontrivial,
        "exact_target_failure_count_on_full_grid": exact_target_failures,
        "kernel_cache_states": len(_KERNEL_CACHE),
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
                "state_count": first_mode_recursion_rows,
                "right_heavy_state_count": len(right_heavy_rows),
                "first_degree_one_failure_state": None
                if first_r1_failure is None
                else first_r1_failure["state_s_kappa_D_B"],
                "max_minimal_truncation": max_minimal_r,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
