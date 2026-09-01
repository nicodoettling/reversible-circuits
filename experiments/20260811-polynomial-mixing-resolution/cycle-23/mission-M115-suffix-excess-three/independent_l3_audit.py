#!/usr/bin/env python3
"""Second, literal-composition audit of the M115 L=3 envelope.

Unlike ``l3_exact.py``, this implementation does not group root compositions
by ``(k,t)`` and does not use the scalar reset formula.  It enumerates every
ordered composition, constructs each canonical basin literally by refining
its first part, computes the basin current and capacity, and recursively sums
every individual live attachment rank.
"""

from __future__ import annotations

import functools
import hashlib
import json
import math
import platform
from fractions import Fraction
from pathlib import Path


OUTPUT = Path("independent_l3_audit.json")


@functools.lru_cache(maxsize=None)
def w(n: int) -> Fraction:
    return Fraction(n ** (n - 1), math.factorial(n))


@functools.lru_cache(maxsize=None)
def compositions(n: int) -> tuple[tuple[int, ...], ...]:
    if n == 0:
        return ((),)
    return tuple(
        (first,) + tail
        for first in range(1, n + 1)
        for tail in compositions(n - first)
    )


def mass(parts: tuple[int, ...]) -> Fraction:
    return math.prod(w(part) for part in parts) / (
        math.factorial(len(parts)) * w(sum(parts) + 1)
    )


def split(rank: int, suffix: int) -> Fraction:
    return w(rank + 1 - suffix) * w(suffix) / w(rank + 1)


def choose_ratio(a: int, b: int, c: int, d: int) -> Fraction:
    if not (0 <= b <= a and 0 <= d <= c):
        return Fraction()
    return Fraction(math.comb(a, b), math.comb(c, d))


def mean(parts: tuple[int, ...], K: int, R: int, B: int) -> Fraction:
    k, t = len(parts), parts[-1]
    if t < B:
        return Fraction()
    if t == B:
        return K * choose_ratio(
            k + K - R - 2, K - R - 1, k + K - 1, K - 1
        )
    return split(t - 1, B) * (
        1 - choose_ratio(K, R + 1, K + k, R + 1)
    )


def attach(K: int, R: int, k: int, j: int) -> Fraction:
    return Fraction(
        math.comb(R + j, j)
        * math.comb(K - R - 1 + k - j, k - j),
        math.comb(K + k, k),
    )


@functools.lru_cache(maxsize=None)
def literal_reset(s: int, K: int, R: int, B: int) -> Fraction:
    q = split(s, B)
    answer = Fraction()
    for endpoint in compositions(s):
        if len(endpoint) < 2:
            continue
        A, b = endpoint[:2]
        if A + b - 1 < 2:
            continue
        theta = sum(
            (
                mass(refinement + endpoint[1:])
                * (mean(refinement + endpoint[1:], K, R, B) - q)
                for refinement in compositions(A)
            ),
            Fraction(),
        )
        answer += theta * theta / (len(endpoint) * mass(endpoint))
    return answer


@functools.lru_cache(maxsize=None)
def literal_resolvent(x: tuple[int, int, int, int]) -> Fraction:
    s, K, R, B = x
    answer = literal_reset(*x)
    for parts in compositions(s):
        t = parts[-1]
        if t <= B or t - 1 < 2:
            continue
        k = len(parts)
        for j in range(1, k + 1):
            coefficient = attach(K, R, k, j)
            if coefficient:
                answer += (
                    mass(parts)
                    * coefficient
                    * literal_resolvent((t - 1, K + k, R + j, B))
                )
    return answer


def envelope(s: int, K: int) -> tuple[Fraction, Fraction, Fraction]:
    B = s - 3
    r = w(s) / w(s + 1)
    u = w(s - 1) / w(s)
    v = w(s - 2) / w(s - 1)
    y = w(s - 3) / w(s - 2)
    a, b = u * v * y, v * y
    c = Fraction(3, 2) * a
    q = Fraction(8, 3) * r * a
    z = Fraction(1, K + 1)
    d = 2 * z * z / (1 + z)
    e = 6 * z ** 3 / ((1 + z) * (1 + 2 * z))
    hbar = Fraction(s - 1, s + 1)
    h1 = Fraction(s - 3, s - 1)
    reset_over_q = (
        q * (
            hbar - q * (
                Fraction(37, 64)
                + Fraction(5, 16) / y
                + Fraction(3, 16) / (v * y)
            )
        )
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

    def f1(p: Fraction) -> Fraction:
        return (
            b * (h1 - b / 2)
            + (2 * p - b) ** 2 / 4
            + (1 - p) * (1 - y)
        )

    descendant_over_q = (
        (3 * (1 - d) + (1 - e)) * (1 - y) / 16
        + Fraction(3, 16) * (nu1 * f1(p1) + nu2 * f1(p2))
        + Fraction(9, 16) * (1 - z) * (1 - c)
    )
    return q * reset_over_q, q * (reset_over_q + descendant_over_q), q * (1 - q)


def rec(value: Fraction) -> dict[str, str | float]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


def main() -> None:
    rows = []
    for s in range(4, 11):
        for K in range(1, 9):
            x = (s, K, K - 1, s - 3)
            reset = literal_reset(*x)
            total = literal_resolvent(x)
            reset_bound, total_bound, target = envelope(s, K)
            assert reset <= reset_bound
            assert total <= total_bound <= target
            rows.append({
                "context": list(x),
                "reset_ratio": rec(reset / reset_bound),
                "resolvent_ratio": rec(total / target),
                "envelope_ratio": rec(total_bound / target),
            })
    payload = {
        "claim_tested": (
            "literal ordered-composition/canonical-basin reconstruction of "
            "the L=3 reset and all-j resolvent versus the closed envelope"
        ),
        "scope": "auxiliary nonlazy minimal-long-cycle Pbar reset operator",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "parameters": {"s": [4, 10], "K": [1, 8], "R": "K-1"},
        "row_count": len(rows),
        "failure_count": 0,
        "rows": rows,
        "arithmetic": "fractions.Fraction exact",
        "python": platform.python_version(),
        "seed": None,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    OUTPUT.write_text(encoded)
    print(json.dumps({
        "output": str(OUTPUT),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "row_count": len(rows),
        "max_resolvent_ratio": max(
            row["resolvent_ratio"]["decimal"] for row in rows
        ),
        "max_envelope_ratio": max(
            row["envelope_ratio"]["decimal"] for row in rows
        ),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
