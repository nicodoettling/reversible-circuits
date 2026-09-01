#!/usr/bin/env python3
"""Clean-room exact checks for the frozen M167 formulas.

Standard library only.  This script deliberately evaluates only the smallest
and a few diagnostic parameter values; it is not a finite scan and is not
evidence for the unresolved actual-history boundary.
"""

from fractions import Fraction as F
from math import comb, factorial
import json
import platform


def beta1_moment(b: int, k: int) -> F:
    """E[U^k] for U ~ Beta(1,b)."""
    return F(factorial(k) * factorial(b), factorial(b + k))


def poly_mul(x: list[F], y: list[F]) -> list[F]:
    out = [F(0) for _ in range(len(x) + len(y) - 1)]
    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            out[i + j] += xi * yj
    return out


def beta1_expect_poly(b: int, p: list[F]) -> F:
    return sum((coefficient * beta1_moment(b, degree)
                for degree, coefficient in enumerate(p)), F(0))


def leakage_row(b: int) -> dict[str, F]:
    # f is the monic first mode for the child Beta(1,b+1).  We represent
    # h=(1-u)f; g=h/sqrt(pi_0), so every quadratic quantity for g is the
    # corresponding quantity for h divided by pi_0.
    f = [F(-1, b + 2), F(1)]
    h = poly_mul([F(1), F(-1)], f)
    pi0 = F(b, b + 1)
    p_parent = F(1, b + 1)
    var_parent = F(b, (b + 1) ** 2 * (b + 2))

    h_norm_sq = beta1_expect_poly(b, poly_mul(h, h))
    centered_h = beta1_expect_poly(
        b, poly_mul([F(-p_parent), F(1)], h)
    )
    q_parent_g = h_norm_sq / pi0 - centered_h**2 / (pi0 * var_parent)

    child_norm = beta1_expect_poly(b + 1, poly_mul(f, f))
    p_child = F(1, b + 2)
    var_child = F(b + 1, (b + 2) ** 2 * (b + 3))
    centered_f = beta1_expect_poly(
        b + 1, poly_mul([F(-p_child), F(1)], f)
    )
    q_child_f = child_norm - centered_f**2 / var_child

    q_formula = F(4 * (b + 1), (b + 2) ** 2 * (b + 3) ** 2 * (b + 4))
    norm_formula = F(b + 1, (b + 2) ** 2 * (b + 3))
    ratio_formula = F(4, (b + 3) * (b + 4))

    assert beta1_expect_poly(b, h) == 0
    assert q_child_f == 0
    assert q_parent_g == q_formula
    assert child_norm == norm_formula
    assert q_parent_g / child_norm == ratio_formula
    return {
        "b": F(b),
        "pi_0": pi0,
        "child_T1": q_child_f,
        "parent_degree_two_tail": q_parent_g,
        "child_first_mode_norm": child_norm,
        "normalized_leakage": q_parent_g / child_norm,
    }


def q_uniform_bernstein(d: int, a: int) -> F:
    trace = F(d + 1, 2 * d + 1) * F(comb(d, a) ** 2, comb(2 * d, 2 * a))
    first = F(3 * (2 * a - d) ** 2, (d + 1) * (d + 2) ** 2)
    return trace - first


def retained_row(d: int) -> dict[str, F]:
    direct = sum((q_uniform_bernstein(d, a) for a in range(d)), F(0))
    convolution = sum(
        (F(comb(d, a) ** 2, comb(2 * d, 2 * a)) for a in range(d + 1)),
        F(0),
    )
    closed = (
        F(d + 1, 2 * d + 1) * (F(4**d, comb(2 * d, d)) - 1)
        - F(d, d + 2)
        + F(3 * d * d, (d + 1) * (d + 2) ** 2)
    )
    constant = F(d, d + 1)
    killed = F(1, d + 1)
    assert convolution == F(4**d, comb(2 * d, d))
    assert direct == closed
    assert direct >= constant
    return {
        "d": F(d),
        "R_d": direct,
        "retained_constant_energy": constant,
        "genuine_degree_at_least_two_tail": direct - constant,
        "killed_mass": killed,
        "tail_over_killed_mass": (direct - constant) / killed,
    }


def cayley_w(k: int) -> F:
    return F(k ** (k - 1), factorial(k))


def cayley_c(n: int, r: int) -> F:
    if (n, r) == (0, 0):
        return F(1)
    if not (n >= 1 and 1 <= r <= n):
        raise ValueError("requires (n,r)=(0,0) or 1<=r<=n")
    return F(r, factorial(n - r)) * F(n) ** (n - r - 1)


def eta_row(n: int, r: int) -> dict[str, F | bool]:
    eta = cayley_c(n, r) / (factorial(r + 1) * cayley_w(n + 2))
    if (n, r) == (0, 0):
        return {"n": F(n), "r": F(r), "eta": eta, "obstruction_tail_zero": True}
    closed = (
        F(r, factorial(n - r) * factorial(r + 1))
        * F(n) ** (n - r - 1)
        * F(factorial(n + 2), (n + 2) ** (n + 1))
    )
    majorant = F(r, factorial(r + 1))
    assert eta == closed
    assert eta <= majorant
    return {
        "n": F(n),
        "r": F(r),
        "eta": eta,
        "factorial_majorant": majorant,
        "is_boundary_r_equals_n": r == n,
    }


def stringify(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {key: stringify(item) for key, item in value.items()}
    if isinstance(value, list):
        return [stringify(item) for item in value]
    return value


def main() -> None:
    result = {
        "method": "standard-library Fraction; selected exact boundary rows only",
        "python": platform.python_version(),
        "random_seed": None,
        "leakage": [leakage_row(b) for b in (1, 2, 5)],
        "retained_constant_child": [retained_row(d) for d in (1, 2, 3, 4)],
        "terminal_eta": [
            eta_row(n, r)
            for n, r in ((0, 0), (1, 1), (2, 1), (2, 2), (3, 1), (3, 3))
        ],
        "all_assertions_pass": True,
    }
    print(json.dumps(stringify(result), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
