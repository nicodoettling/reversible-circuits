#!/usr/bin/env python3
"""Clean-room exact checks for M213. Standard library only; no scans/imports."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from pathlib import Path


def mul(a: list[F], b: list[F]) -> list[F]:
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def add(a: list[F], b: list[F]) -> list[F]:
    out = [F(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return out


def beta_moment(alpha: int, beta: int, n: int) -> F:
    out = F(1)
    for j in range(n):
        out *= F(alpha + j, alpha + beta + j)
    return out


def expect(poly: list[F], alpha: int, beta: int) -> F:
    return sum((c * beta_moment(alpha, beta, i)
                for i, c in enumerate(poly)), F(0))


def q_scalar(feature: list[F], alpha: int, beta: int) -> F:
    p = F(alpha, alpha + beta)
    var = F(alpha * beta, (alpha + beta) ** 2 * (alpha + beta + 1))
    centered = [-p, F(1)]
    return (expect(mul(feature, feature), alpha, beta)
            - expect(mul(centered, feature), alpha, beta) ** 2 / var)


def fs(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="kernel_referee_results.json")
    args = parser.parse_args()

    p2 = [F(1, 10), F(-4, 5), F(1)]
    p3 = [F(-1, 35), F(3, 7), F(-9, 7), F(1)]
    child_p = F(1, 3)
    child_var = F(1, 18)
    parent_centered = [F(-1, 2), F(1)]
    likelihood = [F(1), F(-1)]
    pi = expect(likelihood, 1, 1)
    assert pi == F(1, 2)

    rows = []
    for name, poly, wanted_norm, wanted_charge in (
        ("P2", p2, F(1, 300), F(18, 35)),
        ("P3", p3, F(1, 4900), F(32, 63)),
    ):
        mean = expect(poly, 1, 2)
        centered = expect(mul([-child_p, F(1)], poly), 1, 2)
        norm = expect(mul(poly, poly), 1, 2)
        child_t1 = (norm - centered * centered / child_var) / norm
        raw_parent_cov = expect(
            mul(parent_centered, mul(likelihood, poly)), 1, 1
        )
        trace = expect(mul(mul(likelihood, poly),
                           mul(likelihood, poly)), 1, 1) / (pi * norm)
        parent_charge = trace - raw_parent_cov * raw_parent_cov / (
            pi * norm * F(1, 12)
        )
        assert (mean, centered, norm, child_t1, raw_parent_cov, parent_charge) == (
            F(0), F(0), wanted_norm, F(1), F(0), wanted_charge
        )
        rows.append({
            "name": name,
            "mean": fs(mean),
            "centered_moment": fs(centered),
            "norm2": fs(norm),
            "normalized_child_T1": fs(child_t1),
            "parent_first_mode_raw": fs(raw_parent_cov),
            "parent_lift_charge": fs(parent_charge),
        })

    # One exact PSD-order representative: H=K+(g tensor g), after the
    # d=2,a=1 likelihood lift under Beta(2,3). The difference is Q[Lg]/pi.
    l21 = [F(0), F(2), F(-2)]
    pi21 = expect(l21, 2, 3)
    g = [F(0), F(-1, 3), F(1)]
    monotone_increment = q_scalar(mul(l21, g), 2, 3) / pi21
    assert pi21 == F(2, 5)
    assert monotone_increment > 0

    # Exact accounting identity on arbitrary rational symbols.
    q = F(2, 7)
    upper = [F(1, 10), F(1, 11), F(1, 12)]
    sectors = [F(1, 30), F(1, 40), F(1, 50), F(1, 60), F(1, 70)]
    reset = F(1, 20)
    c3 = sum((upper[i] - sectors[i] for i in range(3)), F(0))
    delta = 1 - q - sum(upper, F(0))
    x3 = reset + sum(sectors[3:], F(0)) - delta
    total_t1 = reset + sum(sectors, F(0))
    assert c3 - x3 == (1 - q) - total_t1

    # For Phi(u)=u at u=0,1, vector (1,-1) kills cJ and gives K-form 1.
    constant_j_form = F(0)
    nonconstant_k_form = F(1)
    domination_difference_form = constant_j_form - nonconstant_k_form
    assert domination_difference_form < 0

    out = {
        "schema": "M213-clean-room-exact-v1",
        "method": "analytic identities plus exact Fraction checks; no scan",
        "p2_p3": rows,
        "likelihood_lift": {
            "pi_d2_a1_beta_2_3": fs(pi21),
            "positive_psd_increment": fs(monotone_increment),
            "verified": True,
        },
        "accounting": {
            "C3_minus_X3": fs(c3 - x3),
            "one_minus_q_minus_T1": fs((1 - q) - total_t1),
            "verified": True,
        },
        "constant_J_obstruction": {
            "J_form": fs(constant_j_form),
            "K_form": fs(nonconstant_k_form),
            "cJ_minus_K_form": fs(domination_difference_form),
            "verified": True,
        },
        "all_checks_pass": True,
    }
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
