#!/usr/bin/env python3
"""Exact finite moments for a Fourier coefficient in a minimal long-cycle bridge.

For odd n, sample a uniform minimal transposition factorization of the long
cycle h=(0 1 ... n-1).  This computes the variance of
    a(t)=sum_v omega^{-(v+t(v))}=-(omega^-p-omega^-q)^2
and its forward correlation between the first two transpositions.  Completion
counts use the elementary minimal-factorization formula.  Final cyclotomic
sums are floating point; this is a falsifier and formula-discovery aid only.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
import platform
from fractions import Fraction
from pathlib import Path

Perm = tuple[int, ...]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for i, image in enumerate(p):
        out[image] = i
    return tuple(out)


def transpositions(n: int) -> list[tuple[tuple[int, int], Perm]]:
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            p = list(range(n))
            p[i], p[j] = p[j], p[i]
            out.append(((i, j), tuple(p)))
    return out


def cycle_type(p: Perm) -> tuple[int, ...]:
    seen = [False] * len(p)
    parts = []
    for start in range(len(p)):
        if seen[start]:
            continue
        x = start
        size = 0
        while not seen[x]:
            seen[x] = True
            size += 1
            x = p[x]
        parts.append(size)
    return tuple(sorted(parts, reverse=True))


def minimal_completion_count(ctype: tuple[int, ...]) -> int:
    rank = sum(size - 1 for size in ctype)
    value = Fraction(math.factorial(rank), 1)
    for size in ctype:
        if size >= 2:
            value *= Fraction(size ** (size - 2), math.factorial(size - 1))
    assert value.denominator == 1
    return value.numerator


def record(n: int) -> dict:
    assert n >= 7 and n % 2 == 1
    h = tuple((i + 1) % n for i in range(n))
    hinv = inverse(h)
    edges = transpositions(n)
    omega = cmath.exp(2j * cmath.pi / n)
    feature = {
        e: -(omega ** (-a) - omega ** (-b)) ** 2
        for (a, b), e in edges
    }
    total = n ** (n - 2)
    marginal_count = {}
    variance_numerator = 0j
    for _, e in edges:
        residual = compose(inverse(e), h)
        count = minimal_completion_count(cycle_type(residual))
        marginal_count[e] = count
        variance_numerator += count * abs(feature[e]) ** 2
    assert sum(marginal_count.values()) == total
    covariance_numerator = 0j
    feasible_pairs = 0
    for _, e in edges:
        for _, f in edges:
            residual = compose(inverse(compose(e, f)), h)
            if sum(size - 1 for size in cycle_type(residual)) != n - 3:
                continue
            count = minimal_completion_count(cycle_type(residual))
            feasible_pairs += 1
            covariance_numerator += count * feature[e].conjugate() * feature[f]
    variance = variance_numerator.real / total
    covariance = covariance_numerator / total
    kappa = covariance / variance
    return {
        "n": n,
        "bridge_length": n - 1,
        "variance": variance,
        "covariance_real": covariance.real,
        "covariance_imag": covariance.imag,
        "kappa_real": kappa.real,
        "kappa_imag": kappa.imag,
        "kappa_abs": abs(kappa),
        "sqrt_n_times_kappa_abs": math.sqrt(n) * abs(kappa),
        "feasible_ordered_first_pairs": feasible_pairs,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-values", default="7,9,11,13,15,17,19,21")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    ns = [int(x) for x in args.n_values.split(",") if x]
    payload = {
        "status": "complete",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "composition": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "scope_warning": "Exact counts but floating cyclotomic sums; finite values are not asymptotic proof.",
        "records": [record(n) for n in ns],
    }
    Path(args.output).write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
