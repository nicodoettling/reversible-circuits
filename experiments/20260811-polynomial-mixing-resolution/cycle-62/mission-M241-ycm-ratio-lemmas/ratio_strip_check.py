#!/usr/bin/env python3
"""Compact certified-interval falsifier for M241 R1--R3.

Finite checks do not prove the lemmas.  All transcendental dependence is
enclosed using rational lower/upper bounds for Euler's number.
"""

from fractions import Fraction
from math import factorial
import json


def e_interval(terms=50):
    lo = sum((Fraction(1, factorial(n)) for n in range(terms + 1)), Fraction())
    # Tail after terms: first omitted term times a geometric majorant whose
    # subsequent ratios are at most 1/(terms+2).
    first = Fraction(1, factorial(terms + 1))
    hi = lo + first * Fraction(terms + 2, terms + 1)
    return lo, hi


E_LO, E_HI = e_interval()


def core(n):
    """b_n = exp(-n) * core(n), with exact rational core."""
    return Fraction(n ** (n - 1), factorial(n))


def b_ratio_interval(numer, denom):
    """Certified interval for b_numer / b_denom."""
    c = core(numer) / core(denom)
    exponent = denom - numer
    if exponent >= 0:
        return c * E_LO**exponent, c * E_HI**exponent
    exponent = -exponent
    return c / E_HI**exponent, c / E_LO**exponent


def q(k, s):
    # Exponents cancel exactly.
    return Fraction(k, k - 1) * core(s) * core(k - s) / core(k)


def a_interval(r, x, R):
    lo, hi = b_ratio_interval(r - x, r)
    factor = Fraction(r - x - 1, R)
    return factor * lo, factor * hi


def abs_interval_diff_upper(lo, hi, value):
    return max(abs(lo - value), abs(hi - value))


def run():
    max_k = 31
    checked_r1 = checked_r2 = checked_r3 = 0
    worst = {
        "r1_over_36": Fraction(),
        "r2_over_rhs": Fraction(),
        "r3_comparison_squared_over_rhs_squared": Fraction(),
        "r3_actual_squared_over_rhs_squared": Fraction(),
    }

    for k in range(3, max_k + 1, 2):
        j, D, R, L = (k - 1) // 2, 2 * k - 1, 2 * k - 3, (3 * k - 1) // 2
        assert sum((q(k, s) for s in range(1, j + 1)), Fraction()) == 1

        for x in range(j, L):
            for s in range(1, min(j, D - x - 2) + 1):
                lo1, hi1 = b_ratio_interval(x, k)
                lo2, hi2 = b_ratio_interval(k - s, D - s)
                upper = hi1 * hi2
                assert upper <= 36
                worst["r1_over_36"] = max(worst["r1_over_36"], upper / 36)
                checked_r1 += 1

        for x in range(1, k // 4 + 1):
            smooth = Fraction()
            for s in range(1, j + 1):
                lo, hi = a_interval(D - s, x, R)
                smooth += q(k, s) * abs_interval_diff_upper(
                    lo, hi, Fraction(D - s, R)
                )
            for s in range(2 * x, j + 1):
                lo, hi = a_interval(s, x, R)
                smooth += q(k, s) * abs_interval_diff_upper(
                    lo, hi, Fraction(s, R)
                )
            rhs = Fraction(34 * (x + 1), k)
            assert smooth <= rhs
            worst["r2_over_rhs"] = max(worst["r2_over_rhs"], smooth / rhs)
            checked_r2 += 1

            comp = sum(
                (q(k, s) * Fraction(s, R) for s in range(x + 1, min(2 * x, j + 1))),
                Fraction(),
            )
            actual_hi = sum(
                (
                    q(k, s) * a_interval(s, x, R)[1]
                    for s in range(x + 1, min(2 * x, j + 1))
                ),
                Fraction(),
            )
            assert comp * comp * R * R <= 42 * 42 * x
            assert actual_hi * actual_hi * R * R <= 28 * 28 * x
            worst["r3_comparison_squared_over_rhs_squared"] = max(
                worst["r3_comparison_squared_over_rhs_squared"],
                comp * comp * R * R / (42 * 42 * x),
            )
            worst["r3_actual_squared_over_rhs_squared"] = max(
                worst["r3_actual_squared_over_rhs_squared"],
                actual_hi * actual_hi * R * R / (28 * 28 * x),
            )
            checked_r3 += 1

    def encode(frac):
        return {
            "decimal": float(frac),
            "numerator_bits": frac.numerator.bit_length(),
            "denominator_bits": frac.denominator.bit_length(),
        }

    return {
        "status": "pass",
        "role": "finite certified-interval falsification only",
        "odd_k": [3, max_k],
        "e_interval_terms": 50,
        "e_interval": {
            "lower_decimal": float(E_LO),
            "upper_decimal": float(E_HI),
            "width_decimal": float(E_HI - E_LO),
        },
        "counts": {"r1_tuples": checked_r1, "r2_cases": checked_r2, "r3_cases": checked_r3},
        "worst_normalized": {name: encode(value) for name, value in worst.items()},
        "seed": None,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
