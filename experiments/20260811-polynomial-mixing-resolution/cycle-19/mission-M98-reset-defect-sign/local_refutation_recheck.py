#!/usr/bin/env python3
"""Exact independent recheck of local proof-template refutations.

This imports only the owned M98 exact core, never a predecessor experiment.
The mixed-moment recurrence is M65's all-attachment-rank pointwise
inheritance applied twice on the same descendant macro.
"""

from __future__ import annotations

import functools
import hashlib
import json
import platform
import time
from fractions import Fraction
from pathlib import Path

import defect_counterexample as core


def ordered(a: tuple[int, int], b: tuple[int, int]):
    return (a, b) if a <= b else (b, a)


def mixed_moment(
    s: int, a: tuple[int, int], b: tuple[int, int], B: int
) -> Fraction:
    a, b = ordered(a, b)
    return _mixed_moment(s, a[0], a[1], b[0], b[1], B)


@functools.lru_cache(maxsize=None)
def _mixed_moment(
    s: int, K: int, R: int, L: int, S: int, B: int
) -> Fraction:
    if s == 1:
        if B != 1:
            raise AssertionError((s, K, R, L, S, B))
        return Fraction(1)
    answer = Fraction(0)
    for k, t, mass in core.groups(s):
        if t < B:
            continue
        if t == B:
            answer += (
                mass
                * core.contextual_value(k, t, K, R, B)
                * core.contextual_value(k, t, L, S, B)
            )
            continue
        for j in range(1, k + 1):
            left = core.attachment_probability(K, R, k, j)
            for ell in range(1, k + 1):
                right = core.attachment_probability(L, S, k, ell)
                answer += (
                    mass
                    * left
                    * right
                    * mixed_moment(
                        t - 1,
                        (K + k, R + j),
                        (L + k, S + ell),
                        B,
                    )
                )
    return answer


@functools.lru_cache(maxsize=None)
def variance(x: tuple[int, int, int, int]) -> Fraction:
    s, K, R, B = x
    q = core.q_split(s, B)
    return mixed_moment(s, (K, R), (K, R), B) - q * q


def root_mean_variance(x: tuple[int, int, int, int]) -> Fraction:
    s, K, R, B = x
    q = core.q_split(s, B)
    return sum(
        (
            mass * (core.contextual_value(k, t, K, R, B) - q) ** 2
            for k, t, mass in core.groups(s)
        ),
        Fraction(),
    )


def Q_value(x: tuple[int, int, int, int], value) -> Fraction:
    return sum(
        (mass * value(child) for mass, child in core.transformed_children(*x)),
        Fraction(),
    )


def coefficient(name: str, x: tuple[int, int, int, int]) -> Fraction:
    s, K, R, _ = x
    P = s + K - R
    if name.startswith("rank_s_over_s_plus_"):
        c = int(name.rsplit("_", 1)[1])
        return Fraction(s, s + c)
    if name.startswith("phase_P_over_P_plus_"):
        c = int(name.rsplit("_", 1)[1])
        return Fraction(P, P + c)
    if name == "rank_one_minus_inverse_square":
        return 1 - Fraction(1, s * s)
    if name == "phase_one_minus_inverse_square":
        return 1 - Fraction(1, P * P)
    raise KeyError(name)


def interpolant(name: str, x: tuple[int, int, int, int]) -> Fraction:
    V = variance(x)
    return V + coefficient(name, x) * (core.U(*x) - V)


def rec(value: Fraction) -> dict[str, object]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


def main() -> None:
    started = time.time()

    variance_x = (6, 2, 1, 2)
    variance_defect = (
        variance(variance_x)
        - core.reset_energy(*variance_x, True)
        - Q_value(variance_x, variance)
    )
    expected_variance_defect = Fraction(
        -21394206021215, 36917038301316768
    )
    if variance_defect != expected_variance_defect:
        raise AssertionError((variance_defect, expected_variance_defect))

    bessel_x = (8, 1, 0, 3)
    bessel_excess = core.unweighted_resolvent(*bessel_x) - variance(bessel_x)
    if bessel_excess <= 0:
        raise AssertionError("direct h<=V witness did not reproduce")

    root_x = (11, 1, 0, 4)
    root_excess = core.reset_energy(*root_x, False) - root_mean_variance(root_x)
    if root_excess <= 0:
        raise AssertionError("direct A0<=Var(H) witness did not reproduce")

    names = [
        *(f"rank_s_over_s_plus_{c}" for c in (1, 2, 4)),
        *(f"phase_P_over_P_plus_{c}" for c in (1, 2, 4)),
        "rank_one_minus_inverse_square",
        "phase_one_minus_inverse_square",
    ]
    interpolant_rows = []
    for name in names:
        local_defect = (
            interpolant(name, root_x)
            - core.reset_energy(*root_x, True)
            - Q_value(root_x, lambda child, name=name: interpolant(name, child))
        )
        if local_defect >= 0:
            raise AssertionError((name, local_defect))
        interpolant_rows.append({"name": name, "raw_defect": rec(local_defect)})

    nonprobability = core.contextual_value(6, 4, 32, 5, 4)
    if nonprobability != Fraction(16182, 6919) or nonprobability <= 1:
        raise AssertionError(("nonprobability witness", nonprobability))

    payload = {
        "purpose": "preserve accepted local variance/Bessel/compensator refutations",
        "scope": "auxiliary nonlazy minimal-long-cycle Pbar reset operator only",
        "normalization": "all attachment ranks retained; exact q-scaled Q recurrence",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "arithmetic": "fractions.Fraction exact",
        "python": platform.python_version(),
        "seed": None,
        "elapsed_seconds": time.time() - started,
        "raw_variance_supersolution": {
            "context": list(variance_x),
            "defect": rec(variance_defect),
            "matches_frozen_exact_fraction": True,
        },
        "direct_full_unweighted_Bessel": {
            "context": list(bessel_x),
            "h_minus_variance": rec(bessel_excess),
        },
        "direct_reset_Bessel": {
            "context": list(root_x),
            "A0_minus_root_mean_variance": rec(root_excess),
        },
        "scalar_interpolants": interpolant_rows,
        "contextual_statistic_not_probability": {
            "context": [12, 32, 5, 4],
            "root_group": [6, 4],
            "value": rec(nonprobability),
        },
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    output = Path(__file__).with_name("local_refutation_recheck.json")
    output.write_text(encoded)
    print(json.dumps({
        "output": str(output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "elapsed_seconds": payload["elapsed_seconds"],
        "variance_defect": payload["raw_variance_supersolution"]["defect"],
        "negative_interpolants": len(interpolant_rows),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
