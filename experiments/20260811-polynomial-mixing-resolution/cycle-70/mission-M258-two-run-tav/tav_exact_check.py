#!/usr/bin/env python3
"""Restricted exact falsifier for M258 TAV, only k=3,5,7."""

from __future__ import annotations

import argparse
import json
import math
import platform
from collections import Counter
from fractions import Fraction
from math import factorial
from pathlib import Path


def b(m: int) -> Fraction:
    # The common exp(-m) factor cancels from every K ratio.
    return Fraction(m ** (m - 1), factorial(m))


def kernel(k: int, r: int, t: int) -> Fraction:
    return b(t) * b(r - t) / ((2 * k - 3) * b(r))


def h(k: int, r: int) -> Fraction:
    if r <= 1:
        return Fraction(0)
    return Fraction((r - 1) * (r - 2), r * (2 * k - 3))


def retained(D: int, r: int, t: int, a: int) -> set[int]:
    return set(range(0, a)) | set(range(a + r - t, r))


def overlap(k: int, r: int, t: int, a: int) -> int:
    D = 2 * k - 1
    E = retained(D, r, t, a)
    return sum(1 for x in E if (x + k) % D in E)


def J(k: int, r: int, t: int) -> int:
    if not (2 <= t <= r - 1):
        return 0
    return sum(overlap(k, r, t, a) for a in range(1, t))


def indicator(value: bool) -> int:
    return int(value)


def qcoef(k: int, ell: int, t: int) -> Fraction:
    D = 2 * k - 1
    return Fraction(
        (D - 2 * t) * indicator(t <= ell)
        + t * indicator(t <= ell - 1)
        + t * indicator(t <= ell - k),
        D,
    )


def placement_formula(k: int, ell: int, r: int, t: int, a: int) -> Fraction:
    D = 2 * k - 1
    j = overlap(k, r, t, a)
    numerator = (
        (D - 2 * t + j) * indicator(t <= ell)
        + (t - j) * indicator(t <= ell - 1)
        + (t - j) * indicator(t <= ell - k)
        + j * indicator(t <= ell - k - 1)
    )
    return Fraction(numerator, D)


def placement_literal(k: int, ell: int, r: int, t: int, a: int) -> Fraction:
    D = 2 * k - 1
    E0 = retained(D, r, t, a)
    qualifying = 0
    for i in range(D):
        E = {(i + x) % D for x in E0}
        y = t + k * indicator(0 in E) + indicator(k in E)
        qualifying += indicator(2 <= y <= ell)
    return Fraction(qualifying, D)


def placement_sum_formula(k: int, ell: int, r: int, t: int) -> Fraction:
    D = 2 * k - 1
    return (t - 1) * qcoef(k, ell, t) + Fraction(
        J(k, r, t)
        * (indicator(t == ell) - indicator(t == ell - k)),
        D,
    )


def T_formula(k: int, ell: int, r: int) -> Fraction:
    return sum(
        (
            kernel(k, r, t) * placement_sum_formula(k, ell, r, t)
            for t in range(2, r)
        ),
        Fraction(0),
    )


def T_literal(k: int, ell: int, r: int) -> Fraction:
    D = 2 * k - 1
    total = Fraction(0)
    for t in range(2, r):
        for a in range(1, t):
            total += kernel(k, r, t) * placement_literal(k, ell, r, t, a)
    return total


def wtilde(k: int, r: int, values) -> Fraction:
    return sum(
        (kernel(k, r, t) * (t - 1) * values(t) for t in range(2, r)),
        Fraction(0),
    )


def spike(k: int, r: int, t: int) -> Fraction:
    if not (2 <= t <= r - 1):
        return Fraction(0)
    return kernel(k, r, t) * Fraction(J(k, r, t), 2 * k - 1)


def theta(k: int, ell: int, s: int, literal: bool = False) -> Fraction:
    D = 2 * k - 1
    H = h(k, s) + h(k, D - s)
    fun = T_literal if literal else T_formula
    return (fun(k, ell, s) + fun(k, ell, D - s)) / H


def check_all() -> dict:
    assertions = 0
    max_ratios = {
        "q_weighted_variation_over_sqrt_ell": 0.0,
        "reflected_head_response_over_sqrt_u": 0.0,
        "spike_mass_over_sqrt_t_over_k": 0.0,
        "spike_response_over_sqrt_t": 0.0,
        "tav_over_sqrt_ell": 0.0,
    }
    rows = []

    def check(condition: bool, message: str) -> None:
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(message)

    for k in (3, 5, 7):
        D = 2 * k - 1
        R = 2 * k - 3
        ell_max = (3 * k - 1) // 2

        # Exact overlap domain, four seam patterns, and coefficient identity.
        for r in range(2, D):
            for t in range(2, r):
                for a in range(1, t):
                    E0 = retained(D, r, t, a)
                    patterns = Counter()
                    for i in range(D):
                        E = {(i + x) % D for x in E0}
                        patterns[(0 in E, k in E)] += 1
                    j = overlap(k, r, t, a)
                    check(patterns[(False, False)] == D - 2 * t + j,
                          f"neither pattern k={k},r={r},t={t},a={a}")
                    check(patterns[(False, True)] == t - j,
                          f"small-only pattern k={k},r={r},t={t},a={a}")
                    check(patterns[(True, False)] == t - j,
                          f"large-only pattern k={k},r={r},t={t},a={a}")
                    check(patterns[(True, True)] == j,
                          f"both pattern k={k},r={r},t={t},a={a}")
                    for ell in range(2, ell_max + 1):
                        check(
                            placement_literal(k, ell, r, t, a)
                            == placement_formula(k, ell, r, t, a),
                            f"placement coefficient k={k},ell={ell},r={r},t={t},a={a}",
                        )

                check(J(k, r, t) <= t * (t - 1),
                      f"J universal bound k={k},r={r},t={t}")
                if r <= k - 1:
                    check(J(k, r, t) == 0,
                          f"short J support k={k},r={r},t={t}")
                if r >= k:
                    c = r - k
                    ambient = [x for x in range(r) if (x + k) % D < r]
                    listed = list(range(0, c)) + list(range(k - 1, k + c))
                    check(ambient == listed,
                          f"ambient pair list k={k},r={r}")
                    if t <= c:
                        check(J(k, r, t) == 0,
                              f"long J cutoff k={k},r={r},t={t}")
                    check(J(k, r, t) <= (t - 1) * (2 * c + 1),
                          f"long J pair bound k={k},r={r},t={t}")

                for ell in range(2, ell_max + 1):
                    check(
                        sum(
                            (placement_literal(k, ell, r, t, a)
                             for a in range(1, t)),
                            Fraction(0),
                        )
                        == placement_sum_formula(k, ell, r, t),
                        f"placement sum k={k},ell={ell},r={r},t={t}",
                    )

        # Reflected constant identity and exact T/decomposition.
        for r in range(1, D):
            check(wtilde(k, r, lambda _t: Fraction(1)) == h(k, r),
                  f"constant identity k={k},r={r}")
        for ell in range(2, ell_max + 1):
            for r in range(1, D):
                check(T_formula(k, ell, r) == T_literal(k, ell, r),
                      f"T identity k={k},ell={ell},r={r}")
            for s in range(1, k):
                q = D - s
                H = h(k, s) + h(k, q)
                base = (
                    wtilde(k, s, lambda t: qcoef(k, ell, t))
                    + wtilde(k, q, lambda t: qcoef(k, ell, t))
                ) / H
                z_hi = (spike(k, s, ell) + spike(k, q, ell)) / H
                low_t = ell - k
                z_lo = (spike(k, s, low_t) + spike(k, q, low_t)) / H
                check(theta(k, ell, s) == base + z_hi - z_lo,
                      f"Theta decomposition k={k},ell={ell},s={s}")
                check(theta(k, ell, s) == theta(k, ell, s, literal=True),
                      f"Theta literal k={k},ell={ell},s={s}")

            qvar = sum(
                math.sqrt(u)
                * abs(float(qcoef(k, ell, u + 1) - qcoef(k, ell, u)))
                for u in range(1, D - 2)
            )
            qratio = qvar / math.sqrt(ell)
            max_ratios["q_weighted_variation_over_sqrt_ell"] = max(
                max_ratios["q_weighted_variation_over_sqrt_ell"], qratio
            )
            check(qratio <= 4.0 + 1e-12,
                  f"Q variation k={k},ell={ell},ratio={qratio}")

            tav = sum(
                math.sqrt(s) * abs(float(theta(k, ell, s + 1) - theta(k, ell, s)))
                for s in range(1, k - 1)
            )
            tav_ratio = tav / math.sqrt(ell)
            max_ratios["tav_over_sqrt_ell"] = max(
                max_ratios["tav_over_sqrt_ell"], tav_ratio
            )
            check(tav_ratio <= 500.0 + 1e-12,
                  f"TAV k={k},ell={ell},ratio={tav_ratio}")
            rows.append({"k": k, "ell": ell, "tav_ratio": tav_ratio})

        # Exact reflected-head shape and finite response bound.
        for u in range(1, ell_max + 1):
            seq = [wtilde(k, r, lambda t, u=u: Fraction(t <= u))
                   for r in range(1, D)]
            peak = min(u + 1, D - 1)
            for r in range(1, peak):
                check(seq[r] >= seq[r - 1],
                      f"head increasing k={k},u={u},r={r}")
            for r in range(peak, D - 1):
                check(seq[r] <= seq[r - 1],
                      f"head decreasing k={k},u={u},r={r}")
            tv = sum(abs(seq[r] - seq[r - 1]) for r in range(1, D - 1))
            check(tv <= Fraction(2 * u, R),
                  f"head TV k={k},u={u}")

            def head_profile(s: int) -> Fraction:
                q = D - s
                H = h(k, s) + h(k, q)
                return (
                    wtilde(k, s, lambda t: Fraction(t <= u))
                    + wtilde(k, q, lambda t: Fraction(t <= u))
                ) / H

            response = sum(
                math.sqrt(s)
                * abs(float(head_profile(s + 1) - head_profile(s)))
                for s in range(1, k - 1)
            )
            ratio = response / math.sqrt(u)
            max_ratios["reflected_head_response_over_sqrt_u"] = max(
                max_ratios["reflected_head_response_over_sqrt_u"], ratio
            )
            check(ratio <= 26.0 + 1e-12,
                  f"head response k={k},u={u},ratio={ratio}")

        # Spike mass and normalized response.
        for t in range(2, ell_max + 1):
            mass = sum((spike(k, r, t) for r in range(t + 1, D)), Fraction(0))
            mass_ratio = float(mass) / math.sqrt(t / k)
            max_ratios["spike_mass_over_sqrt_t_over_k"] = max(
                max_ratios["spike_mass_over_sqrt_t_over_k"], mass_ratio
            )
            check(mass_ratio <= 16.0 + 1e-12,
                  f"spike mass k={k},t={t},ratio={mass_ratio}")

            def spike_profile(s: int) -> Fraction:
                q = D - s
                H = h(k, s) + h(k, q)
                return (spike(k, s, t) + spike(k, q, t)) / H

            response = sum(
                math.sqrt(s)
                * abs(float(spike_profile(s + 1) - spike_profile(s)))
                for s in range(1, k - 1)
            )
            ratio = response / math.sqrt(t)
            max_ratios["spike_response_over_sqrt_t"] = max(
                max_ratios["spike_response_over_sqrt_t"], ratio
            )
            check(ratio <= 160.0 + 1e-12,
                  f"spike response k={k},t={t},ratio={ratio}")

    return {
        "status": "pass",
        "scope": "finite falsification only; k=3,5,7",
        "assertions": assertions,
        "max_ratios": max_ratios,
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = {
        "metadata": {
            "python": platform.python_version(),
            "seed": None,
            "parameters": {"k": [3, 5, 7]},
            "command": (
                "python3 tav_exact_check.py --output tav_exact_results.json"
            ),
            "dependencies": "Python standard library only",
        },
        "certificate": check_all(),
    }
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
