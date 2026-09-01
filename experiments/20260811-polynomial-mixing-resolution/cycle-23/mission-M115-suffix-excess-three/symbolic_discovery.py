#!/usr/bin/env python3
"""SymPy discovery for the cleared L=3 large-s slack polynomial.

This file is derivational aid only.  The final certificate is independently
checked with standard-library exact rational arithmetic in ``l3_exact.py``.
"""

import itertools
import json
import math

import sympy as sp


def main() -> None:
    r, u, v, y, z = sp.symbols("r u v y z", positive=True)
    a = u * v * y
    b = v * y
    c = sp.Rational(3, 2) * a
    q = sp.Rational(8, 3) * r * a
    d = 2 * z**2 / (1 + z)
    e = 6 * z**3 / ((1 + z) * (1 + 2 * z))
    exceptional = sp.Rational(37, 64) + sp.Rational(5, 16) / y + sp.Rational(3, 16) / (v * y)
    reset = (
        q * (1 - q * exceptional)
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

    def f1(p):
        return b * (1 - b / 2) + (2 * p - b) ** 2 / 4 + (1 - p) * (1 - y)

    descendants = (
        (3 * (1 - d) + (1 - e)) * (1 - y) / 16
        + sp.Rational(3, 16) * (nu1 * f1(p1) + nu2 * f1(p2))
        + sp.Rational(9, 16) * (1 - z) * (1 - c)
    )
    slack = sp.factor(1 - q - reset - descendants)
    numerator, denominator = map(sp.factor, sp.together(slack).as_numer_denom())
    poly = sp.Poly(numerator, r, u, v, y, z)
    variables = (r, u, v, y, z)
    lefts = (sp.Rational(1, 3),) * 4 + (sp.Rational(0),)
    rights = (sp.Rational(2, 5),) * 4 + (sp.Rational(1, 2),)
    tvars = sp.symbols("tr tu tv ty tz")
    mapped = sp.Poly(sp.expand(numerator.subs({
        variable: left + (right - left) * tvar
        for variable, left, right, tvar in zip(
            variables, lefts, rights, tvars, strict=True
        )
    })), *tvars)
    degrees = mapped.degree_list()
    power = dict(mapped.terms())
    bernstein = {}
    for index in itertools.product(*(range(degree + 1) for degree in degrees)):
        value = sp.Rational(0)
        for exponent, coefficient in power.items():
            if all(i <= k for i, k in zip(exponent, index, strict=True)):
                weight = sp.prod(
                    sp.Rational(math.comb(k, i), math.comb(degree, i))
                    for i, k, degree in zip(
                        exponent, index, degrees, strict=True
                    )
                )
                value += coefficient * weight
        bernstein[index] = sp.factor(value)
    minimum_index, minimum = min(bernstein.items(), key=lambda item: item[1])
    payload = {
        "sympy": sp.__version__,
        "denominator": str(denominator),
        "degrees": list(poly.degree_list()),
        "term_count": len(poly.terms()),
        "numerator": str(numerator),
        "box": [
            [str(left), str(right)]
            for left, right in zip(lefts, rights, strict=True)
        ],
        "bernstein_count": len(bernstein),
        "bernstein_nonpositive_count": sum(
            int(bool(value <= 0)) for value in bernstein.values()
        ),
        "bernstein_minimum_index": list(minimum_index),
        "bernstein_minimum": str(minimum),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
