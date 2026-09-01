#!/usr/bin/env python3
"""Exact finite probe for scalar compensators between variance and W budget.

Let ``U=q(1-q)K/(R+1)`` and ``V=Var(Phi)``.  For a coefficient
``0<=a(x)<=1`` define ``M=V+a(U-V)``.  If ``M>=A+D M`` universally, then
the full resolvent is bounded by ``M``; on right-heavy seeds ``M<=U``.
This script tests several phase/rank coefficients exactly.  Finite success
would still require an analytic proof; failures reject only the named forms.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import time
from fractions import Fraction
from pathlib import Path

import contextual_second_moment as MOMENT
import exact_weighted_resolvent as EXACT


def coefficients(s: int, K: int, R: int) -> dict[str, Fraction]:
    P = s + K - R
    return {
        "rank_s_over_s_plus_1": Fraction(s, s + 1),
        "rank_s_over_s_plus_2": Fraction(s, s + 2),
        "rank_s_over_s_plus_4": Fraction(s, s + 4),
        "phase_P_over_P_plus_1": Fraction(P, P + 1),
        "phase_P_over_P_plus_2": Fraction(P, P + 2),
        "phase_P_over_P_plus_4": Fraction(P, P + 4),
        "rank_one_minus_inverse_square": 1 - Fraction(1, s * s),
        "phase_one_minus_inverse_square": 1 - Fraction(1, P * P),
    }


def fraction_record(value: Fraction) -> dict[str, object]:
    return {
        "decimal": float(value),
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def scan(s_max: int, k_max: int) -> dict[str, object]:
    moments = MOMENT.SecondMoment()
    names = tuple(coefficients(2, 1, 0))
    failures = {name: [] for name in names}
    minima: dict[str, tuple[Fraction, dict[str, object]] | None] = {
        name: None for name in names
    }
    contexts = 0

    def U(s: int, K: int, R: int, B: int) -> Fraction:
        q = EXACT.q_split(s, B)
        return q * (1 - q) * Fraction(K, R + 1)

    def M(name: str, s: int, K: int, R: int, B: int) -> Fraction:
        variance = moments.variance(s, K, R, B)
        envelope = U(s, K, R, B)
        a = coefficients(s, K, R)[name]
        return variance + a * (envelope - variance)

    for s in range(2, s_max + 1):
        for K in range(1, k_max + 1):
            for R in range(K):
                if R == 0 and K > 1:
                    continue
                for B in range(1, s + 1):
                    contexts += 1
                    x = (s, K, R, B)
                    reset = EXACT.reset_budget(*x)
                    deep_children = []
                    for k, t, mass in EXACT.groups(s):
                        if t <= B or t - 1 < 2:
                            continue
                        for j in range(1, k + 1):
                            probability = EXACT.nu(K, R, k, j)
                            if probability:
                                deep_children.append(
                                    (mass * probability, (t - 1, K + k, R + j, B))
                                )
                    for name in names:
                        parent = M(name, *x)
                        child_sum = sum(
                            (weight * M(name, *child) for weight, child in deep_children),
                            Fraction(),
                        )
                        defect = parent - reset - child_sum
                        scale = parent if parent else Fraction(1)
                        normalized = defect / scale
                        row = {
                            "context": list(x),
                            "coefficient": fraction_record(coefficients(s, K, R)[name]),
                            "parent_M": fraction_record(parent),
                            "reset_budget": fraction_record(reset),
                            "deep_M": fraction_record(child_sum),
                            "defect": fraction_record(defect),
                            "normalized_defect": fraction_record(normalized),
                            "right_heavy": R == K - 1,
                        }
                        current = minima[name]
                        if current is None or normalized < current[0]:
                            minima[name] = (normalized, row)
                        if defect < 0:
                            failures[name].append(row)

    return {
        "contexts": contexts,
        "failure_counts": {name: len(rows) for name, rows in failures.items()},
        "first_failures": {name: rows[:3] for name, rows in failures.items()},
        "minimum_normalized_defects": {
            name: {"value": fraction_record(item[0]), "row": item[1]}
            for name, item in minima.items()
        },
        "memoized_mixed_moment_contexts": moments.calls,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=8)
    parser.add_argument("--k-max", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    result = scan(args.s_max, args.k_max)
    payload = {
        "claim_tested": "named scalar compensators M=V+a(U-V) satisfy M>=A+D M",
        "finite_scope_warning": (
            "A failure refutes only its named compensator. Finite survival "
            "would not prove a universal supersolution."
        ),
        "arithmetic": "fractions.Fraction exact grouped recurrences",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "parameters": {"s_max": args.s_max, "k_max": args.k_max},
        "elapsed_seconds": time.time() - started,
        "result": result,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "elapsed_seconds": payload["elapsed_seconds"],
        "failure_counts": result["failure_counts"],
        "minimum_normalized_defects": result["minimum_normalized_defects"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
