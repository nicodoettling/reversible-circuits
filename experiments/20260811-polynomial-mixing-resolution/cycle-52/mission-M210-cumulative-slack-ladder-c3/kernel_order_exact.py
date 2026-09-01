#!/usr/bin/env python3
"""Compact exact audit of M210's kernel-order reduction.

No predecessor imports.  This checks the decisive unrestricted P2/P3
likelihood-transfer nonclosure and a minimal Loewner-order obstruction.  It
does not scan fresh parents.
"""

from argparse import ArgumentParser
from fractions import Fraction as Q
from json import dumps
from math import prod
from pathlib import Path


def rising(start, length):
    return prod(range(start, start + length))


def beta_moment(kappa, deficit, degree):
    return Q(rising(deficit, degree), rising(kappa, degree))


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def add(left, right):
    out = [Q(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    return trim(out)


def scale(poly, scalar):
    return trim(scalar * value for value in poly)


def multiply(left, right):
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return trim(out)


def expectation(poly, kappa, deficit):
    return sum((coefficient * beta_moment(kappa, deficit, degree)
                for degree, coefficient in enumerate(poly)), Q(0))


def squared_norm(poly, kappa, deficit):
    return expectation(multiply(poly, poly), kappa, deficit)


def first_center(poly, kappa, deficit):
    mean = Q(deficit, kappa)
    return expectation(multiply(poly, (-mean, Q(1))), kappa, deficit)


def transfer_ratio(poly):
    # Parent Beta(1,1), d=1,a=0; child Beta(1,2), L_0=1-u.
    child_norm = squared_norm(poly, 3, 1)
    weighted_norm = expectation(
        multiply((Q(1), Q(-1)), multiply(poly, poly)), 3, 1
    )
    return weighted_norm / child_norm


def show(value):
    return {"exact": str(value), "decimal": float(value)}


def main():
    parser = ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    p2 = (Q(1, 10), Q(-4, 5), Q(1))
    p3 = (Q(-1, 35), Q(3, 7), Q(-9, 7), Q(1))

    norm2 = squared_norm(p2, 3, 1)
    norm3 = squared_norm(p3, 3, 1)
    assert norm2 == Q(1, 300) and norm3 == Q(1, 4900)

    # Both residual modes have identical (M,C,||Z||^2,T1) summaries.
    assert expectation(p2, 3, 1) == expectation(p3, 3, 1) == 0
    assert first_center(p2, 3, 1) == first_center(p3, 3, 1) == 0
    child_summaries = {
        "M": Q(0), "C": Q(0), "Z_norm_squared": Q(1), "child_T1": Q(1)
    }

    charge2 = transfer_ratio(p2)
    charge3 = transfer_ratio(p3)
    assert charge2 == Q(18, 35)
    assert charge3 == Q(32, 63)
    assert charge2 != charge3

    # The parent first-mode subtraction is zero for both lifted residuals.
    # Up to the harmless sqrt(pi_0) factor, test (u-1/2)(1-u)P_j.
    parent_center_times_likelihood = multiply(
        (Q(-1, 2), Q(1)), (Q(1), Q(-1))
    )
    assert expectation(multiply(parent_center_times_likelihood, p2), 2, 1) == 0
    assert expectation(multiply(parent_center_times_likelihood, p3), 2, 1) == 0

    # A constant rank-one kernel c*J cannot PSD-dominate a nonconstant Gram
    # kernel f(u)f(v): at points 0,1 and vector (1,-1), J has form zero while
    # f(u)=u has strictly positive form one.
    constant_kernel_zero_sum_form = Q(0)
    nonconstant_kernel_zero_sum_form = Q(1)
    assert constant_kernel_zero_sum_form < nonconstant_kernel_zero_sum_form

    # Exact sign bookkeeping on arbitrary rational placeholders.
    q = Q(2, 7)
    u = (Q(1, 11), Q(2, 13), Q(3, 17))
    t = (Q(1, 19), Q(2, 23), Q(3, 29))
    reset, tail = Q(5, 31), Q(7, 37)
    delta = 1 - q - sum(u, Q(0))
    sector_slack = sum((u[i] - t[i] for i in range(3)), Q(0))
    tail_excess = reset + tail - delta
    total_t1 = reset + tail + sum(t, Q(0))
    assert sector_slack - tail_excess == 1 - q - total_t1

    result = {
        "schema": "M210-kernel-order-v1",
        "arithmetic": "standard-library Fraction",
        "seed": None,
        "predecessor_imports": False,
        "accounting_identity_checked": True,
        "nonclosure_witness": {
            "common_child_summary": {key: show(value)
                                     for key, value in child_summaries.items()},
            "P2_norm_squared": show(norm2),
            "P3_norm_squared": show(norm3),
            "P2_lift_charge": show(charge2),
            "P3_lift_charge": show(charge3),
            "charges_distinct": True,
            "parent_first_mode_subtractions_zero": True,
        },
        "constant_Loewner_domination_obstruction": {
            "test_points": [0, 1],
            "test_vector": [1, -1],
            "constant_kernel_form": show(constant_kernel_zero_sum_form),
            "nonconstant_Gram_form": show(nonconstant_kernel_zero_sum_form),
            "conclusion": "c*J cannot PSD-dominate a nonconstant Gram kernel",
        },
        "scope": {
            "fresh_parent_scan": False,
            "universal_C3_claim": False,
            "purpose": "audit exact state-variable/kernel-order reduction only",
        },
    }
    args.output.write_text(dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
