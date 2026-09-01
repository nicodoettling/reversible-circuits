#!/usr/bin/env python3
"""Exact finite check of the balanced-family far-singleton certificate.

For n=3k with odd k, compare

    A=(0,k,2k),             B=(0,1)(k,2k).

The event F consists of admissible double targets whose residual cycle sizes
are (1,u,n-1-u) with both nonsingleton sizes at least k.  The proof in the
M83 report shows K_A(F)=0.  A specified cross-cycle subset under B has the
closed probability computed by ``certificate_probability``.  This script
checks that formula against direct exact completion counts.  Every result is
a finite rational identity, not an asymptotic computation.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


Perm = tuple[int, ...]


def mul(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[i]] for i in range(len(p)))


def inv(p: Perm) -> Perm:
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def transposition(n: int, a: int, b: int) -> Perm:
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def cycle(n: int, entries: tuple[int, ...]) -> Perm:
    p = list(range(n))
    for a, b in zip(entries, entries[1:] + entries[:1]):
        p[a] = b
    return tuple(p)


def cycle_sizes(p: Perm) -> list[int]:
    seen: set[int] = set()
    out: list[int] = []
    for start in range(len(p)):
        if start in seen:
            continue
        size = 0
        x = start
        while x not in seen:
            seen.add(x)
            size += 1
            x = p[x]
        out.append(size)
    return sorted(out)


def count_minimal(p: Perm, length: int) -> int:
    sizes = cycle_sizes(p)
    if len(p) - len(sizes) != length:
        return 0
    value = math.factorial(length)
    for d in sizes:
        if d > 1:
            value = value * d ** (d - 2) // math.factorial(d - 1)
    return value


def tau(d: int) -> Fraction:
    return Fraction(d ** (d - 1), math.factorial(d))


def edge_weight(d: int, split: int) -> Fraction:
    """Probability of one specified chord under the local nu_d law."""

    return Fraction(math.factorial(d - 2), d ** (d - 2)) * tau(split) * tau(d - split)


def certificate_probability(k: int) -> Fraction:
    """Closed probability of the selected B cross-cycle target subset."""

    long_size = 2 * k - 1
    total_rank = 3 * k - 3
    cross_color = Fraction(
        2 * (long_size - 1) * (k - 1),
        total_rank * (total_rank - 1),
    )
    middle_boundary = (k - 1) * edge_weight(k, 1)
    long_cross = sum(
        (s * edge_weight(long_size, s) for s in range(1, k - 1)),
        Fraction(0),
    )
    long_cross += 2 * (k - 1) * edge_weight(long_size, k - 1)
    return cross_color * middle_boundary * long_cross


def analyze(k: int) -> dict[str, object]:
    if k < 3 or k % 2 == 0:
        raise ValueError("k must be odd and at least three")
    n = 3 * k
    h = tuple((x + 1) % n for x in range(n))
    source_a = cycle(n, (0, k, 2 * k))
    source_b = mul(transposition(n, 0, 1), transposition(n, k, 2 * k))
    den_a = count_minimal(mul(inv(source_a), h), n - 3)
    den_b = count_minimal(mul(inv(source_b), h), n - 3)

    selected: set[Perm] = set()
    for i in range(1, k):
        for j in range(2 * k, 3 * k):
            if not (k + 1 <= j - i <= 2 * k):
                continue
            long_edge = transposition(n, i, j)
            for m in range(k, 2 * k - 1):
                middle_edge = transposition(n, m, m + 1)
                selected.add(mul(long_edge, middle_edge))

    enumerated_a = Fraction(0)
    enumerated_b = Fraction(0)
    all_selected_have_far_singleton_residual = True
    for target in selected:
        sizes = cycle_sizes(mul(inv(target), h))
        all_selected_have_far_singleton_residual &= (
            sizes[0] == 1 and sizes[1] >= k
        )
        # Every selected product has exactly two ordered micro-lifts.
        enumerated_a += Fraction(
            2 * count_minimal(mul(inv(mul(source_a, target)), h), n - 5),
            den_a,
        )
        enumerated_b += Fraction(
            2 * count_minimal(mul(inv(mul(source_b, target)), h), n - 5),
            den_b,
        )

    formula = certificate_probability(k)
    return {
        "k": k,
        "n": n,
        "selected_raw_targets": len(selected),
        "all_selected_have_far_singleton_residual": (
            all_selected_have_far_singleton_residual
        ),
        "enumerated_A_probability": str(enumerated_a),
        "enumerated_B_probability": str(enumerated_b),
        "closed_formula_probability": str(formula),
        "formula_equals_enumeration": formula == enumerated_b,
        "sqrt_k_times_probability_numeric": math.sqrt(k) * float(formula),
        "proved_lower_bound_2_over_27e2sqrtk_numeric": (
            2 / (27 * math.e**2 * math.sqrt(k))
        ),
        "finite_probability_exceeds_proved_lower_bound": (
            float(formula) >= 2 / (27 * math.e**2 * math.sqrt(k))
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", nargs="+", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "status": "exact_finite_rational_certificate",
        "claim_checked": (
            "closed conditioned-Borel probability for a B-only subset of "
            "the far-singleton quotient event"
        ),
        "scope_warning": (
            "The script checks finite rational identities.  The asymptotic "
            "lower bound is a separate proof in report.md."
        ),
        "family": "n=3k, k odd: A=[k,k,k]_3, B=[1,k-1,k,k]_S",
        "convention": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
        "results": [analyze(k) for k in args.k],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
