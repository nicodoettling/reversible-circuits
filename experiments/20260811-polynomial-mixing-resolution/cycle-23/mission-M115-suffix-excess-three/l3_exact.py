#!/usr/bin/env python3
"""Exact formula audit for the M115 suffix-excess-three excursion.

This is a standalone standard-library ``Fraction`` implementation.  It
reconstructs the accepted all-j recurrence, the L=3 support/live-group table,
and the closed analytic envelope derived in ``suffix_excess_three.md``.
Bounded rows test formulas and search for a counterexample; they do not by
themselves prove a universal inequality.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import itertools
import math
import platform
import time
from fractions import Fraction
from pathlib import Path


@functools.lru_cache(maxsize=None)
def w(a: int) -> Fraction:
    assert a >= 1
    return Fraction(a ** (a - 1), math.factorial(a))


@functools.lru_cache(maxsize=None)
def cayley(total: int, parts: int) -> Fraction:
    if parts == 0:
        return Fraction(int(total == 0))
    if not 1 <= parts <= total:
        return Fraction()
    return Fraction(
        parts * total ** (total - parts),
        total * math.factorial(total - parts),
    )


def q_split(s: int, B: int) -> Fraction:
    return w(s + 1 - B) * w(B) / w(s + 1)


def comb_ratio(n1: int, k1: int, n2: int, k2: int) -> Fraction:
    if not (0 <= k1 <= n1 and 0 <= k2 <= n2):
        return Fraction()
    return Fraction(math.comb(n1, k1), math.comb(n2, k2))


def contextual(k: int, t: int, K: int, R: int, B: int) -> Fraction:
    if t < B:
        return Fraction()
    if t == B:
        return K * comb_ratio(
            k + K - R - 2, K - R - 1, k + K - 1, K - 1
        )
    return q_split(t - 1, B) * (
        1 - comb_ratio(K, R + 1, K + k, R + 1)
    )


def attachment(K: int, R: int, k: int, j: int) -> Fraction:
    return Fraction(
        math.comb(R + j, j)
        * math.comb(K - R - 1 + k - j, k - j),
        math.comb(K + k, k),
    )


@functools.lru_cache(maxsize=None)
def groups(s: int) -> tuple[tuple[int, int, Fraction], ...]:
    rows = []
    total = Fraction()
    for k in range(1, s + 1):
        for t in range(1, s + 1):
            mass = w(t) * cayley(s - t, k - 1) / (
                math.factorial(k) * w(s + 1)
            )
            if mass:
                rows.append((k, t, mass))
                total += mass
    assert total == 1
    return tuple(rows)


@functools.lru_cache(maxsize=None)
def reset_energy(s: int, K: int, R: int, B: int) -> Fraction:
    """Exact unweighted active canonical-reset energy A_0."""
    q_parent = q_split(s, B)
    answer = Fraction()
    scalar_cache: dict[tuple[int, int, int], Fraction] = {}

    def scalar(A: int, ell: int, last: int) -> Fraction:
        key = (A, ell, last)
        if key not in scalar_cache:
            scalar_cache[key] = sum(
                (
                    cayley(A, p)
                    * (contextual(p + ell, last, K, R, B) - q_parent)
                    / math.factorial(p + ell)
                    for p in range(1, A + 1)
                ),
                Fraction(),
            )
        return scalar_cache[key]

    for ell in range(1, s):
        tail_parts = ell - 1
        for A in range(1, s + 1):
            for b in range(1, s - A - tail_parts + 1):
                tail_total = s - A - b
                child_rank = A + b - 1
                if child_rank < 2:
                    continue
                if tail_parts == 0:
                    tail_rows = ((b, w(b)),) if tail_total == 0 else ()
                else:
                    tail_rows = tuple(
                        (
                            last,
                            w(b)
                            * cayley(tail_total - last, tail_parts - 1)
                            * w(last),
                        )
                        for last in range(1, tail_total + 1)
                        if cayley(tail_total - last, tail_parts - 1)
                    )
                for last, suffix_weight in tail_rows:
                    current = scalar(A, ell, last)
                    answer += (
                        suffix_weight
                        * math.factorial(ell)
                        * current
                        * current
                        / (w(A) * w(s + 1))
                    )
    return answer


@functools.lru_cache(maxsize=None)
def children(x: tuple[int, int, int, int]):
    s, K, R, B = x
    rows = []
    phase = s + K - R
    for k, t, mass in groups(s):
        if t <= B or t - 1 < 2:
            continue
        assert sum(
            (attachment(K, R, k, j) for j in range(k + 1)), Fraction()
        ) == 1
        for j in range(1, k + 1):
            coefficient = attachment(K, R, k, j)
            if coefficient:
                child = (t - 1, K + k, R + j, B)
                assert child[0] + child[1] - child[2] < phase
                rows.append((mass * coefficient, child, k, t, j))
    return tuple(rows)


@functools.lru_cache(maxsize=None)
def resolvent(x: tuple[int, int, int, int]) -> Fraction:
    return reset_energy(*x) + sum(
        (mass * resolvent(child) for mass, child, _, _, _ in children(x)),
        Fraction(),
    )


def l3_parameters(s: int, K: int) -> dict[str, Fraction]:
    assert s >= 4 and K >= 1
    r = w(s) / w(s + 1)
    u = w(s - 1) / w(s)
    v = w(s - 2) / w(s - 1)
    y = w(s - 3) / w(s - 2)
    a = u * v * y
    b = v * y
    c = Fraction(3, 2) * a
    q = Fraction(8, 3) * r * a
    z = Fraction(1, K + 1)
    d = 2 * z * z / (1 + z)
    e = 6 * z ** 3 / ((1 + z) * (1 + 2 * z))
    return {
        "r": r,
        "u": u,
        "v": v,
        "y": y,
        "a": a,
        "b": b,
        "c": c,
        "q": q,
        "z": z,
        "d": d,
        "e": e,
        "hbar": Fraction(s - 1, s + 1),
        "h1": Fraction(s - 3, s - 1),
    }


def support_table(s: int, K: int):
    """Expected L=3 supported compositions: (parts, mass, mean)."""
    p = l3_parameters(s, K)
    B = s - 3
    q, z, d, e = p["q"], p["z"], p["d"], p["e"]
    y, v, a = p["y"], p["v"], p["a"]
    return (
        ((3, B), Fraction(9, 32) * q, 2 * z),
        ((1, 2, B), Fraction(1, 16) * q, 3 * d),
        ((2, 1, B), Fraction(1, 16) * q, 3 * d),
        ((1, 1, 1, B), Fraction(1, 64) * q, 4 * e),
        ((2, s - 2), Fraction(3, 16) * q / y, y * (1 - d)),
        ((1, 1, s - 2), Fraction(1, 16) * q / y, y * (1 - e)),
        ((1, s - 1), Fraction(3, 16) * q / (v * y), v * y * (1 - d)),
        ((s,), p["r"], Fraction(3, 2) * a * (1 - z)),
    )


def l1_child_envelope(s: int, p_attach: Fraction) -> Fraction:
    """Bound on H/b for the L=1 child of an L=3 parent.

    Here the child has rank ``S=s-2``, split ``b=v*y``, terminal split ``y``,
    and ``p_attach=(K_child-R_child)/(K_child+1)``.
    """
    params = l3_parameters(s, 1)
    b, y, h1 = params["b"], params["y"], params["h1"]
    return (
        b * (h1 - b / 2)
        + (2 * p_attach - b) ** 2 / 4
        + (1 - p_attach) * (1 - y)
    )


def l3_reset_envelope_over_q(s: int, K: int) -> Fraction:
    """Closed ordinary-basin plus seven-exception reset bound A_0/q."""
    p = l3_parameters(s, K)
    q, z, d, e = p["q"], p["z"], p["d"], p["e"]
    y, v, hbar = p["y"], p["v"], p["hbar"]
    exceptional_height = (
        Fraction(37, 64) + Fraction(5, 16) / y + Fraction(3, 16) / (v * y)
    )
    return (
        q * (hbar - q * exceptional_height)
        + (4 * e - q) ** 2 / 256
        + (12 * d + 4 * e - 5 * q) ** 2 / 768
        + (3 * d - q) ** 2 / 48
        + (36 * z + 24 * d + 4 * e - 27 * q) ** 2 / 2304
        + (y * (1 - e) - q) ** 2 / (48 * y)
        + (4 * y - 3 * y * d - y * e - 4 * q) ** 2 / (96 * y)
        + 3 * (v * y * (1 - d) - q) ** 2 / (32 * v * y)
    )


def l3_descendant_envelope_over_q(s: int, K: int) -> Fraction:
    """All-j descendant charge divided by the parent q."""
    p = l3_parameters(s, K)
    z, d, e = p["z"], p["d"], p["e"]
    y, c = p["y"], p["c"]
    nu1 = 2 * z * (1 - z) / (1 + z)
    nu2 = (1 - z) / (1 + z)
    p1 = 2 * z / (1 + 2 * z)
    p2 = z / (1 + 2 * z)
    assert d + nu1 + nu2 == 1
    return (
        (3 * (1 - d) + (1 - e)) * (1 - y) / 16
        + Fraction(3, 16)
        * (
            nu1 * l1_child_envelope(s, p1)
            + nu2 * l1_child_envelope(s, p2)
        )
        + Fraction(9, 16) * (1 - z) * (1 - c)
    )


def l3_envelope(s: int, K: int) -> tuple[Fraction, Fraction]:
    p = l3_parameters(s, K)
    over_q = l3_reset_envelope_over_q(s, K) + l3_descendant_envelope_over_q(s, K)
    return p["q"] * over_q, p["q"] * (1 - p["q"])


def envelope_over_q_general(
    r: Fraction,
    u: Fraction,
    v: Fraction,
    y: Fraction,
    z: Fraction,
    hbar: Fraction,
    h1: Fraction,
) -> tuple[Fraction, Fraction]:
    """Return ``(E,q)`` for the closed L=3 bound ``H/q<=E``.

    The formula treats the four consecutive Cayley ratios as independent
    variables.  This is used for the large-s box certificate.
    """
    a = u * v * y
    b = v * y
    c = Fraction(3, 2) * a
    q = Fraction(8, 3) * r * a
    d = 2 * z * z / (1 + z)
    e = 6 * z ** 3 / ((1 + z) * (1 + 2 * z))
    exceptional_height = (
        Fraction(37, 64)
        + Fraction(5, 16) / y
        + Fraction(3, 16) / (v * y)
    )
    reset = (
        q * (hbar - q * exceptional_height)
        + (4 * e - q) ** 2 / 256
        + (12 * d + 4 * e - 5 * q) ** 2 / 768
        + (3 * d - q) ** 2 / 48
        + (36 * z + 24 * d + 4 * e - 27 * q) ** 2 / 2304
        + (y * (1 - e) - q) ** 2 / (48 * y)
        + (4 * y - 3 * y * d - y * e - 4 * q) ** 2 / (96 * y)
        + 3 * (v * y * (1 - d) - q) ** 2 / (32 * v * y)
    )
    nu1 = 2 * z * (1 - z) / (1 + z)
    nu2 = (1 - z) / (1 + z)
    p1 = 2 * z / (1 + 2 * z)
    p2 = z / (1 + 2 * z)

    def f1(p_attach: Fraction) -> Fraction:
        return (
            b * (h1 - b / 2)
            + (2 * p_attach - b) ** 2 / 4
            + (1 - p_attach) * (1 - y)
        )

    descendants = (
        (3 * (1 - d) + (1 - e)) * (1 - y) / 16
        + Fraction(3, 16) * (nu1 * f1(p1) + nu2 * f1(p2))
        + Fraction(9, 16) * (1 - z) * (1 - c)
    )
    return reset + descendants, q


def cleared_slack_general(
    r: Fraction,
    u: Fraction,
    v: Fraction,
    y: Fraction,
    z: Fraction,
    hbar: Fraction,
    h1: Fraction,
) -> Fraction:
    """Positive-denominator clearing of ``1-q-E``."""
    envelope, q = envelope_over_q_general(r, u, v, y, z, hbar, h1)
    return 1728 * (1 + z) ** 2 * (1 + 2 * z) ** 2 * (
        1 - q - envelope
    )


@functools.lru_cache(maxsize=None)
def lagrange_to_bernstein_matrix(degree: int):
    """Map values at integer nodes 0,...,degree to Bernstein coefficients."""
    lagrange = []
    for node in range(degree + 1):
        coefficients = [Fraction(1)]
        denominator = 1
        for other in range(degree + 1):
            if other == node:
                continue
            product = [Fraction()] * (len(coefficients) + 1)
            for power, coefficient in enumerate(coefficients):
                product[power] -= other * coefficient
                product[power + 1] += coefficient
            coefficients = product
            denominator *= node - other
        lagrange.append(tuple(value / denominator for value in coefficients))
    return tuple(
        tuple(
            sum(
                (
                    lagrange[node][power]
                    * Fraction(
                        math.comb(index, power),
                        math.comb(degree, power),
                    )
                    for power in range(index + 1)
                ),
                Fraction(),
            )
            for node in range(degree + 1)
        )
        for index in range(degree + 1)
    )


def tensor_bernstein(
    values: dict[tuple[int, ...], Fraction],
    degrees: tuple[int, ...],
) -> dict[tuple[int, ...], Fraction]:
    """Apply tensor interpolation/Bernstein transforms one axis at a time."""
    transformed = values
    ranges = tuple(range(degree + 1) for degree in degrees)
    for axis, degree in enumerate(degrees):
        matrix = lagrange_to_bernstein_matrix(degree)
        next_values = {}
        for output_index in itertools.product(*ranges):
            next_values[output_index] = sum(
                (
                    matrix[output_index[axis]][node]
                    * transformed[
                        output_index[:axis]
                        + (node,)
                        + output_index[axis + 1 :]
                    ]
                    for node in range(degree + 1)
                ),
                Fraction(),
            )
        transformed = next_values
    return transformed


def record(value: Fraction) -> dict[str, str | float]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=20)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()

    K_values = [1, 2, 5, 64]
    rows = []
    support_checks = []
    live_checks = []
    failures = []
    for s in range(4, args.s_max + 1):
        B = s - 3
        for K in K_values:
            p = l3_parameters(s, K)
            table = support_table(s, K)
            assert sum((mass * mean for _, mass, mean in table), Fraction()) == p["q"]
            for parts, expected_mass, expected_mean in table:
                k, t = len(parts), parts[-1]
                direct_mass = math.prod((w(part) for part in parts)) / (
                    math.factorial(k) * w(s + 1)
                )
                assert direct_mass == expected_mass
                assert contextual(k, t, K, K - 1, B) == expected_mean
            nonzero_pairs = tuple(
                (k, t)
                for k, t, _ in groups(s)
                if contextual(k, t, K, K - 1, B)
            )
            assert nonzero_pairs == (
                (1, s),
                (2, s - 3),
                (2, s - 2),
                (2, s - 1),
                (3, s - 3),
                (3, s - 2),
                (4, s - 3),
            )
            support_checks.append({
                "s": s,
                "K": K,
                "supported_composition_count": len(table),
                "supported_group_count": len(nonzero_pairs),
                "mean_identity": True,
            })

            live = children((s, K, K - 1, B))
            live_groups = tuple(sorted(set((k, t) for _, _, k, t, _ in live)))
            expected_groups = [(1, s), (2, s - 1)]
            if s >= 5:
                expected_groups.extend([(2, s - 2), (3, s - 2)])
            assert live_groups == tuple(sorted(expected_groups))
            assert all(j >= 1 for _, _, _, _, j in live)
            live_checks.append({
                "s": s,
                "K": K,
                "groups": [list(group) for group in live_groups],
                "retained_j": sorted(set(j for _, _, _, _, j in live)),
            })

            x = (s, K, K - 1, B)
            actual_reset = reset_energy(*x)
            reset_bound = p["q"] * l3_reset_envelope_over_q(s, K)
            envelope, target = l3_envelope(s, K)
            general_envelope, general_q = envelope_over_q_general(
                p["r"], p["u"], p["v"], p["y"], p["z"],
                p["hbar"], p["h1"],
            )
            assert general_q == p["q"]
            assert p["q"] * general_envelope == envelope
            actual = resolvent(x)
            if not (actual_reset <= reset_bound and actual <= envelope):
                failures.append({"s": s, "K": K, "kind": "formula-bound"})
            if envelope > target:
                failures.append({"s": s, "K": K, "kind": "envelope-sign"})
            rows.append({
                "s": s,
                "K": K,
                "actual_ratio": record(actual / target),
                "envelope_ratio": record(envelope / target),
                "reset_ratio_to_bound": record(actual_reset / reset_bound),
                "envelope_slack": record(target - envelope),
            })

    # The actual finite-rank slack has degree at most six after multiplication
    # by the displayed positive denominator.  Interpolate it at seven exact
    # nodes and convert to Bernstein form on z in [0,1/2].
    finite_certificates = []
    for s in range(4, 21):
        r = w(s) / w(s + 1)
        u = w(s - 1) / w(s)
        v = w(s - 2) / w(s - 1)
        y = w(s - 3) / w(s - 2)
        values = {
            (node,): cleared_slack_general(
                r, u, v, y, Fraction(node, 2),
                Fraction(s - 1, s + 1), Fraction(s - 3, s - 1),
            )
            for node in range(7)
        }
        coefficients = tensor_bernstein(values, (6,))
        assert all(value > 0 for value in coefficients.values())
        finite_certificates.append({
            "s": s,
            "coefficients": [
                record(coefficients[(index,)]) for index in range(7)
            ],
            "minimum": record(min(coefficients.values())),
        })

    # For s>=21, monotonicity of the Cayley ratios and b_18<2/5 put
    # r,u,v,y independently in [1/3,2/5].  Replacing hbar,h1 by one enlarges
    # the envelope.  The tensor Bernstein coefficients certify positivity on
    # that entire five-dimensional box, including z=0.
    degrees = (2, 2, 2, 2, 6)
    lefts = (Fraction(1, 3),) * 4 + (Fraction(),)
    spans = (Fraction(1, 15),) * 4 + (Fraction(1, 2),)
    ranges = tuple(range(degree + 1) for degree in degrees)
    box_values = {}
    for index in itertools.product(*ranges):
        r, u, v, y, z = tuple(
            left + span * node
            for left, span, node in zip(lefts, spans, index)
        )
        box_values[index] = cleared_slack_general(
            r, u, v, y, z, Fraction(1), Fraction(1)
        )
    box_coefficients = tensor_bernstein(box_values, degrees)
    box_minimum_index, box_minimum = min(
        box_coefficients.items(), key=lambda item: item[1]
    )
    assert all(value > 0 for value in box_coefficients.values())
    assert box_minimum == Fraction(682328, 28125)
    b18 = Fraction(18, 19) ** 17
    assert b18 < Fraction(2, 5)

    payload = {
        "claim_tested": (
            "exact L=3 support/live-group formulas, all-j resolvent, and "
            "closed-envelope domination/sign"
        ),
        "status": (
            "exact formula validation plus complete Bernstein certificates; "
            "the analytic proof supplies their interpretation"
        ),
        "scope": "auxiliary nonlazy minimal-long-cycle Pbar reset operator",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "parameters": {"s_min": 4, "s_max": args.s_max, "K_values": K_values},
        "arithmetic": "fractions.Fraction exact",
        "python": platform.python_version(),
        "seed": None,
        "support_checks": support_checks,
        "live_checks": live_checks,
        "rows": rows,
        "finite_bernstein_certificate": {
            "range": "s=4,...,20; z in [0,1/2]",
            "cleared_polynomial": (
                "1728*(1+z)^2*(1+2z)^2*[1-q-E_s(z)], degree <=6"
            ),
            "rows": finite_certificates,
        },
        "asymptotic_bernstein_certificate": {
            "range": (
                "r,u,v,y in [1/3,2/5], z in [0,1/2], hbar=h1=1; "
                "contains all s>=21"
            ),
            "degrees": list(degrees),
            "coefficient_count": len(box_coefficients),
            "minimum_index": list(box_minimum_index),
            "minimum": record(box_minimum),
            "b18": record(b18),
            "b18_below_two_fifths": True,
            "coefficients": [
                {"index": list(index), "value": record(value)}
                for index, value in sorted(box_coefficients.items())
            ],
        },
        "failure_count": len(failures),
        "failures": failures,
        "elapsed_seconds": time.time() - started,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "row_count": len(rows),
        "failure_count": len(failures),
        "max_actual_ratio": max(float(row["actual_ratio"]["decimal"]) for row in rows),
        "max_envelope_ratio": max(float(row["envelope_ratio"]["decimal"]) for row in rows),
        "elapsed_seconds": payload["elapsed_seconds"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
