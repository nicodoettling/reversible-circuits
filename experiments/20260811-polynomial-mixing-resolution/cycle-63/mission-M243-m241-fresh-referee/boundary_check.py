#!/usr/bin/env python3
"""Clean-room boundary falsifier for frozen M241.

This script imports no predecessor module or data.  Exact rational arithmetic
is used except for a certified rational enclosure of Euler's number.  Passing
finite checks is not evidence for the universal statements.
"""

from fractions import Fraction
from math import factorial
import json


def e_bounds(order=56):
    lower = sum((Fraction(1, factorial(i)) for i in range(order + 1)), Fraction())
    first_missing = Fraction(1, factorial(order + 1))
    upper = lower + first_missing * Fraction(order + 2, order + 1)
    return lower, upper


E0, E1 = e_bounds()


def core(n):
    return Fraction(n ** (n - 1), factorial(n))


def b_ratio(a, c):
    """Certified interval for b_a/b_c."""
    rational = core(a) / core(c)
    power = c - a
    if power >= 0:
        return rational * E0**power, rational * E1**power
    power = -power
    return rational / E1**power, rational / E0**power


def abs_from_interval(lo, hi, center):
    return max(abs(lo - center), abs(hi - center))


def weight(k, s):
    return Fraction(k, k - 1) * core(s) * core(k - s) / core(k)


def shifted(parent, x, R):
    lo, hi = b_ratio(parent - x, parent)
    scale = Fraction(parent - x - 1, R)
    return scale * lo, scale * hi


def direct_g_exact(k, x):
    """Exact G_k(x); all exponential factors cancel termwise."""
    j, D, R = (k - 1) // 2, 2 * k - 1, 2 * k - 3
    M = D - x
    total = Fraction()
    if x <= j:
        total += weight(k, x) * Fraction((M - 1) * (M - 2), M * R)
    for s in range(x + 1, j + 1):
        total += (
            weight(k, s)
            * Fraction(s - x - 1, R)
            * core(x)
            * core(s - x)
            / core(s)
        )
    for s in range(1, min(j, M - 2) + 1):
        total += (
            weight(k, s)
            * Fraction(M - s - 1, R)
            * core(x)
            * core(M - s)
            / core(D - s)
        )
    return total


def check(max_k=35):
    counts = {
        "rho_steps": 0,
        "product_boundaries": 0,
        "r1_tuples": 0,
        "sg_cases": 0,
        "gg2_cases": 0,
    }
    margins = {
        "r1_over_36": Fraction(),
        "r2_over_bound": Fraction(),
        "r3_comparison_squared_over_bound": Fraction(),
        "r3_actual_squared_over_bound": Fraction(),
        "sg_squared_over_bound": Fraction(),
        "gg2_squared_over_bound": Fraction(),
    }

    # Euler factors cancel: this is an exact check that rho_n decreases.
    for n in range(2, 4 * max_k):
        f_n = Fraction(n - 1, n) ** (n - 2)
        f_next = Fraction(n, n + 1) ** (n - 1)
        assert f_next < f_n
        counts["rho_steps"] += 1

    for k in range(3, max_k + 1, 2):
        j, D, R, L = (k - 1) // 2, 2 * k - 1, 2 * k - 3, (3 * k - 1) // 2
        assert sum((weight(k, s) for s in range(1, j + 1)), Fraction()) == 1

        # Check the exact endpoints in the telescoping-product identity.
        for x in range(1, k // 4 + 1):
            for parent in {2 * x, k, D - 1, D - j}:
                if parent < 2 * x:
                    continue
                lhs = core(parent - x) / core(parent)
                rhs = Fraction(1)
                for n in range(parent - x + 1, parent + 1):
                    rhs *= Fraction(n - 1, n) ** (n - 2)
                assert lhs == rhs
                assert parent - x + 1 >= 2
                counts["product_boundaries"] += 1

        for x in range(j, L):
            M = D - x
            for s in range(1, min(j, M - 2) + 1):
                a0, a1 = b_ratio(x, k)
                c0, c1 = b_ratio(k - s, D - s)
                upper = a1 * c1
                assert upper <= 36
                margins["r1_over_36"] = max(margins["r1_over_36"], upper / 36)
                counts["r1_tuples"] += 1

            g = direct_g_exact(k, x)
            assert g * g * k * k * M <= 70 * 70
            margins["gg2_squared_over_bound"] = max(
                margins["gg2_squared_over_bound"], g * g * k * k * M / (70 * 70)
            )
            counts["gg2_cases"] += 1

        for x in range(1, k // 4 + 1):
            smooth = Fraction()
            for s in range(1, j + 1):
                lo, hi = shifted(D - s, x, R)
                smooth += weight(k, s) * abs_from_interval(lo, hi, Fraction(D - s, R))
            for s in range(2 * x, j + 1):
                lo, hi = shifted(s, x, R)
                smooth += weight(k, s) * abs_from_interval(lo, hi, Fraction(s, R))
            r2_bound = Fraction(34 * (x + 1), k)
            assert smooth <= r2_bound
            margins["r2_over_bound"] = max(margins["r2_over_bound"], smooth / r2_bound)

            comparison = Fraction()
            actual_lo = actual_hi = Fraction()
            for s in range(x + 1, min(2 * x, j + 1)):
                comparison += weight(k, s) * Fraction(s, R)
                lo, hi = shifted(s, x, R)
                actual_lo += weight(k, s) * lo
                actual_hi += weight(k, s) * hi
            assert comparison * comparison * R * R <= 42 * 42 * x
            assert actual_hi * actual_hi * R * R <= 28 * 28 * x
            margins["r3_comparison_squared_over_bound"] = max(
                margins["r3_comparison_squared_over_bound"],
                comparison * comparison * R * R / (42 * 42 * x),
            )
            margins["r3_actual_squared_over_bound"] = max(
                margins["r3_actual_squared_over_bound"],
                actual_hi * actual_hi * R * R / (28 * 28 * x),
            )

            P = Fraction(k, k - 1) * Fraction(D - x - 1, D - x) * Fraction(D - x - 2, R)
            assert abs(P - 1) <= Fraction(2 * (x + 1), k)
            assert P <= Fraction(5, 4)
            q0, q1 = b_ratio(k - x, k)
            assert abs_from_interval(P * q0, P * q1, Fraction(1)) <= Fraction(22 * (x + 1), k)

            # Direct normalized G interval, independent of the SG decomposition.
            u0, u1 = P * q0, P * q1
            f0 = f1 = Fraction()
            for s in range(1, j + 1):
                lo, hi = shifted(D - s, x, R)
                f0 += weight(k, s) * lo
                f1 += weight(k, s) * hi
            for s in range(x + 1, j + 1):
                lo, hi = shifted(s, x, R)
                f0 += weight(k, s) * lo
                f1 += weight(k, s) * hi
            error = abs_from_interval(u0 + f0, u1 + f1, Fraction(2))
            sg_bound = Fraction(128 * (x + 1), k)
            assert error <= sg_bound
            margins["sg_squared_over_bound"] = max(
                margins["sg_squared_over_bound"], error * error / (sg_bound * sg_bound)
            )
            counts["sg_cases"] += 1

    def show(value):
        return {"decimal": float(value), "numerator_bits": value.numerator.bit_length(), "denominator_bits": value.denominator.bit_length()}

    return {
        "status": "pass",
        "scope": "finite clean-room boundary falsification only",
        "odd_k": [3, max_k],
        "standard_library_only": True,
        "predecessor_imports": False,
        "seed": None,
        "counts": counts,
        "worst_normalized": {key: show(value) for key, value in margins.items()},
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2, sort_keys=True))
