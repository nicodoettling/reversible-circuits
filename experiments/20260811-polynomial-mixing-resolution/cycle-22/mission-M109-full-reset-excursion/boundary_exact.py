#!/usr/bin/env python3
"""Independent exact checks for M109's full-excursion boundary theorems.

No predecessor module is imported.  ``Fraction`` arithmetic implements the
accepted all-j grouped recurrence.  The bounded checks only validate formulas;
the proofs in ``excursion_reduction.md`` are analytic.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import platform
import time
from fractions import Fraction
from pathlib import Path


@functools.lru_cache(maxsize=None)
def w(a: int) -> Fraction:
    return Fraction(a ** (a - 1), math.factorial(a))


@functools.lru_cache(maxsize=None)
def cayley(total: int, parts: int) -> Fraction:
    if parts == 0:
        return Fraction(int(total == 0))
    if not 1 <= parts <= total:
        return Fraction()
    return Fraction(parts * total ** (total - parts),
                    total * math.factorial(total - parts))


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
def reset_energy(s: int, K: int, R: int, B: int,
                 weighted: bool) -> Fraction:
    q_parent = q_split(s, B)
    answer = Fraction()
    scalar_cache: dict[tuple[int, int, int], Fraction] = {}

    def scalar(A: int, ell: int, last: int) -> Fraction:
        key = (A, ell, last)
        if key not in scalar_cache:
            scalar_cache[key] = sum((
                cayley(A, p)
                * (contextual(p + ell, last, K, R, B) - q_parent)
                / math.factorial(p + ell)
                for p in range(1, A + 1)
            ), Fraction())
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
                        (last, w(b) * cayley(tail_total - last,
                                             tail_parts - 1) * w(last))
                        for last in range(1, tail_total + 1)
                        if cayley(tail_total - last, tail_parts - 1)
                    )
                for last, suffix_weight in tail_rows:
                    current = scalar(A, ell, last)
                    energy = (
                        suffix_weight * math.factorial(ell) * current * current
                        / (w(A) * w(s + 1))
                    )
                    if weighted:
                        energy *= 1 - q_split(child_rank, b)
                    answer += energy
    return answer


@functools.lru_cache(maxsize=None)
def children(x: tuple[int, int, int, int]):
    s, K, R, B = x
    rows = []
    phase = s + K - R
    for k, t, mass in groups(s):
        if t <= B or t - 1 < 2:
            continue
        assert sum((attachment(K, R, k, j) for j in range(k + 1)),
                   Fraction()) == 1
        for j in range(1, k + 1):
            coefficient = attachment(K, R, k, j)
            if coefficient:
                child = (t - 1, K + k, R + j, B)
                assert child[0] + child[1] - child[2] < phase
                rows.append((mass * coefficient, child))
    return tuple(rows)


@functools.lru_cache(maxsize=None)
def resolvent(x: tuple[int, int, int, int], weighted: bool) -> Fraction:
    return reset_energy(*x, weighted) + sum((
        mass * resolvent(child, weighted) for mass, child in children(x)
    ), Fraction())


def record(value: Fraction) -> dict[str, str | float]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


def l2_envelope(s: int, K: int) -> tuple[Fraction, Fraction]:
    """Return (H upper bound, target) from the analytic L=2 proof."""
    B = s - 2
    r = w(s) / w(s + 1)
    u = w(s - 1) / w(s)
    v = w(B) / w(s - 1)
    a = u * v
    q = Fraction(3, 2) * r * a
    hbar = Fraction(s - 1, s + 1)
    z = Fraction(1, K + 1)
    d = 2 * z * z / (1 + z)
    E = (
        q * (hbar - 5 * q / 9 - q / (3 * v))
        + (3 * d - q) ** 2 / 27
        + (3 * d + 6 * z - 4 * q) ** 2 / 54
        + (v * (1 - d) - q) ** 2 / (6 * v)
        + (1 - d) * (1 - v) / 3
        + Fraction(2, 3) * (1 - z) * (1 - a)
    )
    return q * E, q * (1 - q)


def l2_slack_power_coefficients(s: int) -> list[Fraction]:
    """Power coefficients of 18v(1+z)^2 times the L=2 envelope slack."""
    B = s - 2
    r = w(s) / w(s + 1)
    u = w(s - 1) / w(s)
    v = w(B) / w(s - 1)
    a = u * v
    q = Fraction(3, 2) * r * a
    hbar = Fraction(s - 1, s + 1)
    return [
        12 * a * v - 18 * hbar * q * v + 4 * q * q * v
        + 3 * q * q - 12 * q * v + 3 * v * v,
        12 * a * v - 36 * hbar * q * v + 8 * q * q * v
        + 6 * q * q - 8 * q * v + 6 * v * v + 12 * v,
        -12 * a * v - 18 * hbar * q * v + 4 * q * q * v
        + 3 * q * q + 32 * q * v + 3 * v * v + 24 * v,
        -12 * a * v + 28 * q * v - 24 * v,
        -12 * v * v - 72 * v,
    ]


def bernstein_half(coefficients: list[Fraction]) -> list[Fraction]:
    """Bernstein coefficients on z in [0,1/2]."""
    degree = len(coefficients) - 1
    return [sum((
        coefficients[i]
        * Fraction(math.comb(k, i), math.comb(degree, i))
        * Fraction(1, 2) ** i
        for i in range(k + 1)
    ), Fraction()) for k in range(degree + 1)]


def bernstein_interval(coefficients: list[Fraction], left: Fraction,
                       right: Fraction) -> list[Fraction]:
    """Bernstein coefficients after mapping an arbitrary interval to [0,1]."""
    degree = len(coefficients) - 1
    span = right - left
    mapped = [sum((
        coefficients[i] * math.comb(i, j) * left ** (i - j) * span ** j
        for i in range(j, degree + 1)
    ), Fraction()) for j in range(degree + 1)]
    return [sum((
        mapped[j] * Fraction(math.comb(k, j), math.comb(degree, j))
        for j in range(k + 1)
    ), Fraction()) for k in range(degree + 1)]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=16)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()

    # Independent smallest frozen calibrations for the complete all-j core.
    calibrations = [
        ((8, 1, 0, 4), True, Fraction(
            198601672967024061529855442277847995017,
            454309761272791522761187983360000000000)),
        ((11, 1, 0, 5), True, Fraction(
            369415041873682908150614323148480891664502126021893041639180381877247723,
            685180503111588118552571661898695660247555243568148903962345472000000000)),
        ((8, 1, 0, 3), False, Fraction(
            253985287689718867427349453367883132399,
            408991211833242065204727055908864000000)),
        ((11, 1, 0, 4), False, Fraction(
            18615667628666856375237627759295775559821033754032171180303074993127,
            26795011170382144058688163148823729544343031644160000000000000000000)),
    ]
    calibration_rows = []
    for x, weighted, expected_ratio in calibrations:
        q = q_split(x[0], x[3])
        value = resolvent(x, weighted)
        ratio = value / (q * (1 - q))
        assert ratio == expected_ratio
        calibration_rows.append({
            "context": list(x), "weighted": weighted,
            "ratio": record(ratio), "exact_match": True,
        })

    # Exact direct checks of the two analytic boundary bounds.
    K_values = [1, 2, 5, 64]
    boundary_rows = []
    for s in range(2, args.s_max + 1):
        r = w(s) / w(s + 1)
        terminal_envelope = r * r * Fraction(s - 1, s + 1)
        for K in K_values:
            terminal = (s, K, K - 1, s)
            terminal_value = resolvent(terminal, False)
            terminal_target = r * (1 - r)
            assert terminal_value <= terminal_envelope <= terminal_target

            one = (s, K, K - 1, s - 1)
            one_value = resolvent(one, False)
            q = q_split(s, s - 1)
            one_target = q * (1 - q)
            assert one_value <= one_target
            boundary_rows.append({
                "s": s,
                "K": K,
                "terminal_ratio": record(terminal_value / terminal_target),
                "one_layer_ratio": record(one_value / one_target),
                "one_layer_margin": record(one_target - one_value),
            })

    # L=2 is certified analytically for all s.  These exact rows test the
    # finite formulas and give a machine-readable certificate for s=3,...,9;
    # the proof handles s>=10 by positive Bernstein polynomials in u.
    l2_rows = []
    finite_bernstein = []
    for s in range(3, max(args.s_max, 9) + 1):
        if s <= 9:
            coefficients = bernstein_half(l2_slack_power_coefficients(s))
            assert all(value > 0 for value in coefficients)
            finite_bernstein.append({
                "s": s,
                "coefficients": [record(value) for value in coefficients],
                "minimum": record(min(coefficients)),
            })
        if s <= args.s_max:
            for K in K_values:
                x = (s, K, K - 1, s - 2)
                value = resolvent(x, False)
                envelope, target = l2_envelope(s, K)
                assert value <= envelope <= target
                z = Fraction(1, K + 1)
                v = w(s - 2) / w(s - 1)
                q = q_split(s, s - 2)
                polynomial = sum((coefficient * z ** power for
                    power, coefficient in enumerate(
                        l2_slack_power_coefficients(s))), Fraction())
                assert polynomial == (
                    18 * v * (1 + z) ** 2 * (target - envelope) / q
                )
                l2_rows.append({
                    "s": s,
                    "K": K,
                    "actual_ratio": record(value / target),
                    "envelope_ratio": record(envelope / target),
                    "envelope_slack": record(target - envelope),
                })

    asymptotic_polynomials = {
        "p": [4, 16, -60, 0, 9, 12],
        "j": [32, 72, -360, 0, 81, 216],
        "m": [24, 32, 72, -360, 0, 81, 108],
    }
    asymptotic_bernstein = {}
    for name, coefficients in asymptotic_polynomials.items():
        values = bernstein_interval(
            [Fraction(value) for value in coefficients],
            Fraction(1, 3), Fraction(7, 16),
        )
        assert all(value > 0 for value in values)
        asymptotic_bernstein[name] = [record(value) for value in values]
    assert Fraction(9, 10) ** 8 < Fraction(7, 16)

    payload = {
        "claim_tested": (
            "exact formula audit for full unweighted/weighted all-j "
            "resolvent and analytic suffix-excess L<=1 theorems"
        ),
        "status": (
            "exact bounded validation only; universal L<=1 status comes "
            "from the analytic proof, not this scan"
        ),
        "scope": "auxiliary nonlazy minimal-long-cycle Pbar reset operator",
        "normalization": (
            "H=(I-Q)^-1 A0, G=(I-Q)^-1 A; every j=1,...,k retained; "
            "j=0 and inactive children killed"
        ),
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "parameters": {"s_max": args.s_max, "K_values": K_values},
        "calibrations": calibration_rows,
        "boundary_failure_count": 0,
        "boundary_rows": boundary_rows,
        "l2_rows": l2_rows,
        "l2_finite_bernstein_certificate": {
            "polynomial": (
                "18*v*(1+z)^2 times [1-q-E_s(z)], degree four, "
                "Bernstein basis on z in [0,1/2]"
            ),
            "range": "s=3,...,9",
            "rows": finite_bernstein,
        },
        "l2_asymptotic_bernstein_certificate": {
            "range": "u in [1/3,7/16] for s>=10",
            "b10": record(Fraction(9, 10) ** 8),
            "b10_below_7_over_16": True,
            "coefficients": asymptotic_bernstein,
        },
        "arithmetic": "fractions.Fraction exact",
        "python": platform.python_version(),
        "seed": None,
        "elapsed_seconds": time.time() - started,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "calibration_count": len(calibration_rows),
        "boundary_row_count": len(boundary_rows),
        "elapsed_seconds": payload["elapsed_seconds"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
