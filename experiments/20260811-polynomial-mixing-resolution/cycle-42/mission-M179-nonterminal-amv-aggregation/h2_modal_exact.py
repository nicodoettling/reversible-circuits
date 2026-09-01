#!/usr/bin/env python3
"""Compact exact audit for M179's fresh h=2 affine-sector theorem."""

from __future__ import annotations

import argparse
import json
import math
import platform
from fractions import Fraction as Q
from pathlib import Path


Poly = tuple[Q, ...]


def trim(values: list[Q] | tuple[Q, ...]) -> Poly:
    out = list(values)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def multiply(left: Poly, right: Poly) -> Poly:
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return trim(out)


def rising(x: int, n: int) -> int:
    return math.prod(range(x, x + n)) if n else 1


def beta_moment(alpha: int, beta: int, degree: int) -> Q:
    return Q(rising(alpha, degree), rising(alpha + beta, degree))


def expectation(poly: Poly, alpha: int, beta: int) -> Q:
    return sum(
        (coefficient * beta_moment(alpha, beta, i) for i, coefficient in enumerate(poly)),
        Q(0),
    )


def likelihood(d: int, a: int) -> Poly:
    out = [Q(0)] * (d + 1)
    for j in range(d - a + 1):
        out[a + j] += Q(math.comb(d, a) * math.comb(d - a, j) * (-1) ** j)
    return trim(out)


def w(n: int) -> Q:
    return Q(n ** (n - 1), math.factorial(n))


def cayley(n: int, r: int) -> Q:
    if (n, r) == (0, 0) or r == n:
        return Q(1)
    return Q(r * n ** (n - r - 1), math.factorial(n - r))


def exterior(n: int, r: int) -> Q:
    return cayley(n, r) / (math.factorial(r + 1) * w(n + 3))


def exterior_from_root_and_splits(B: int, n: int, r: int) -> Q:
    """Direct eta=m_group*q_child/q_parent for h=2, L=n+2."""
    degree = r + 1
    total = B + n + 2
    last = B + 2
    group_mass = w(last) * cayley(n, r) / (math.factorial(degree) * w(total + 1))
    child_split = w(2) * w(B) / w(B + 2)
    parent_split = w(n + 3) * w(B) / w(total + 1)
    return group_mass * child_split / parent_split


def record(value: Q) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def posterior_data(d: int, a: int, trace_override: Q | None = None) -> dict[str, Q]:
    alpha = a + 1
    beta = d - a + 1
    total = d + 2
    p = Q(alpha, total)
    variance = Q(alpha * beta, total * total * (total + 1))
    delta = p - Q(1, 2)
    second_p = Q(2 * a + 1, 2 * (d + 1))
    second_variance = Q(
        (2 * a + 1) * (2 * d - 2 * a + 1),
        (2 * d + 2) ** 2 * (2 * d + 3),
    )
    trace = (
        Q(d + 1, 2 * d + 1)
        * Q(math.comb(d, a) ** 2, math.comb(2 * d, 2 * a))
        if trace_override is None
        else trace_override
    )
    shift = second_p - p
    lambda1 = trace * shift
    lambda2 = trace * (second_variance + shift * shift)
    pi = Q(1, d + 1)
    q00 = trace - 12 * pi * delta * delta
    q01_numerator = lambda1 - 12 * pi * delta * variance
    q01_squared = q01_numerator * q01_numerator / variance
    q11 = lambda2 / variance - 12 * pi * variance
    return {
        "p": p,
        "variance": variance,
        "delta": delta,
        "trace": trace,
        "lambda1": lambda1,
        "lambda2": lambda2,
        "q00": q00,
        "q01_squared": q01_squared,
        "q11": q11,
    }


def loewner_slack(d: int, a: int, constant: Q, upper_trace: bool) -> tuple[Q, Q, Q]:
    trace = Q(d + 1, 2 * d + 1) if upper_trace else None
    data = posterior_data(d, a, trace)
    s00 = constant - data["q00"]
    s11 = constant - data["q11"]
    determinant = s00 * s11 - data["q01_squared"]
    return s00, s11, determinant


def direct_affine_charge(d: int, a: int, mean: Q, covariance: Q) -> Q:
    like = likelihood(d, a)
    alpha = a + 1
    beta = d - a + 1
    p = Q(alpha, d + 2)
    variance = Q(alpha * beta, (d + 2) ** 2 * (d + 3))
    phi = (mean - p * covariance / variance, covariance / variance)
    trace = expectation(multiply(like, multiply(phi, phi)), alpha, beta)
    delta = p - Q(1, 2)
    return trace - Q(12, d + 1) * (delta * mean + covariance) ** 2


def formula_affine_charge(d: int, a: int, mean: Q, covariance: Q) -> Q:
    data = posterior_data(d, a)
    variance = data["variance"]
    return (
        data["trace"] * mean * mean
        + 2 * data["lambda1"] * mean * covariance / variance
        + data["lambda2"] * covariance * covariance / (variance * variance)
        - Q(12, d + 1) * (data["delta"] * mean + covariance) ** 2
    )


def child_norm_envelope(B: int, d: int, a: int) -> Q:
    if B == 1:
        return Q(0)
    y = w(B) / w(B + 1)
    b = w(B) / w(B + 2)
    height = Q(B, B + 2)
    p = Q(a + 1, d + 2)
    z = Q(1, d + 3)
    variance = p * (1 - p) * z
    return (
        b * (height - b / 2)
        + (p - b / 2) ** 2
        + variance
        + (1 - p + p * z) * (1 - y)
    )


def determinant_polynomial(d: int, x: int) -> int:
    a0 = (d - 1) * (d + 2) ** 3 * (
        5 * d**4 + 24 * d**3 + 64 * d**2 + 72 * d + 18
    )
    a1 = (
        -5 * d**6
        + 43 * d**5
        + 480 * d**4
        + 1658 * d**3
        + 2729 * d**2
        + 2025 * d
        + 414
    )
    a2 = 90 * d**3 + 387 * d**2 + 603 * d + 216
    return a0 + a1 * x - a2 * x * x


def run() -> dict[str, object]:
    failures: list[str] = []

    # One asymmetric exact specialization of all M,C cross terms.
    direct = direct_affine_charge(4, 1, Q(7, 5), Q(-2, 11))
    formula = formula_affine_charge(4, 1, Q(7, 5), Q(-2, 11))
    if direct != formula:
        failures.append("affine AMV specialization")

    d1 = posterior_data(1, 0)
    if (d1["q00"], d1["q01_squared"], d1["q11"]) != (
        Q(1, 2),
        Q(0),
        Q(1, 5),
    ):
        failures.append("degree-one operator matrix")

    matrix_rows: list[dict[str, object]] = []
    for d in (2, 3, 7, 20):
        observations = sorted({0, d // 2, d - 1})
        for a in observations:
            actual = posterior_data(d, a)
            upper_trace = Q(d + 1, 2 * d + 1)
            if actual["trace"] > upper_trace:
                failures.append(f"Vandermonde trace d={d},a={a}")
            s00, s11, determinant = loewner_slack(d, a, Q(2, 3), True)
            if min(s00, s11, determinant) < 0:
                failures.append(f"2/3 Loewner slack d={d},a={a}")
            x = (2 * a - d) ** 2
            denominator = (
                9
                * (d + 1)
                * (d + 2)
                * (d + 3)
                * (2 * d + 1) ** 2
                * (2 * d + 3)
                * ((d + 2) ** 2 - x)
            )
            if determinant != Q(determinant_polynomial(d, x), denominator):
                failures.append(f"determinant polynomial d={d},a={a}")
            matrix_rows.append(
                {
                    "d": d,
                    "a": a,
                    "actual_trace": record(actual["trace"]),
                    "upper_slack_determinant": record(determinant),
                }
            )
        p0 = determinant_polynomial(d, 0)
        pd2 = determinant_polynomial(d, d * d)
        expected0 = (d - 1) * (d + 2) ** 3 * (
            5 * d**4 + 24 * d**3 + 64 * d**2 + 72 * d + 18
        )
        expectedd2 = (d + 1) * (2 * d + 1) * (
            d**5 + 152 * d**4 + 557 * d**3 + 658 * d**2 - 216 * d - 144
        )
        if p0 != expected0 or pd2 != expectedd2 or min(p0, pd2) <= 0:
            failures.append(f"concave determinant endpoints d={d}")

    norm_rows: list[dict[str, object]] = []
    for B, d, a in (
        (1, 1, 0),
        (2, 1, 0),
        (8, 1, 0),
        (2, 2, 0),
        (2, 2, 1),
        (5, 5, 0),
        (5, 5, 4),
        (20, 9, 8),
    ):
        envelope = child_norm_envelope(B, d, a)
        target = Q(3, 4) if d == 1 else Q(1)
        if envelope > target:
            failures.append(f"affine child norm B={B},d={d},a={a}")
        norm_rows.append(
            {"B": B, "d": d, "a": a, "envelope": record(envelope), "target": record(target)}
        )

    exterior_rows: list[dict[str, object]] = []
    for n in (0, 1, 2, 5):
        rs = (0,) if n == 0 else range(1, n + 1)
        first_moment = sum(((r + 1) * exterior(n, r) for r in rs), Q(0))
        if n == 0:
            closed = Q(2, 3)
        else:
            closed = Q((n + 1) ** n * (n + 2), (n + 3) ** (n + 1))
        if first_moment != closed or (n >= 1 and first_moment > Q(3, 8)):
            failures.append(f"h2 exterior first moment n={n}")
        sector_bound = (
            exterior(0, 0) * Q(1, 2) * Q(3, 4)
            if n == 0
            else Q(2, 3) * first_moment
        )
        if sector_bound > Q(1, 4):
            failures.append(f"h2 quarter bound n={n}")
        exterior_rows.append(
            {
                "n": n,
                "first_moment": record(first_moment),
                "sector_envelope": record(sector_bound),
            }
        )

    eta_rows: list[dict[str, object]] = []
    for B, n, r in ((1, 0, 0), (2, 1, 1), (7, 5, 1), (7, 5, 3), (7, 5, 5)):
        direct_eta = exterior_from_root_and_splits(B, n, r)
        closed_eta = exterior(n, r)
        if direct_eta != closed_eta:
            failures.append(f"h2 eta cancellation B={B},n={n},r={r}")
        eta_rows.append(
            {
                "B": B,
                "n": n,
                "r": r,
                "direct_eta": record(direct_eta),
                "closed_eta": record(closed_eta),
            }
        )

    return {
        "claim": "fresh-parent actual-history h=2 descendant charge is at most one quarter",
        "claim_scope": "h=2 descendants only; no reset, h>=3, total budget, gap, or terminal",
        "comparison_denominator": "actual-history child diagonal trace S, not child T1 or F",
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "environment": {
            "python": platform.python_version(),
            "dependencies": "Python standard library only",
            "seed": None,
            "exact_command": "python3 -B h2_modal_exact.py --output h2_modal_exact.json",
        },
        "affine_cross_term_audit": {
            "degree": 4,
            "observation": 1,
            "direct": record(direct),
            "formula": record(formula),
        },
        "degree_one_matrix": {
            "q00": record(d1["q00"]),
            "q01_squared": record(d1["q01_squared"]),
            "q11": record(d1["q11"]),
        },
        "matrix_rows": matrix_rows,
        "child_norm_rows": norm_rows,
        "exterior_rows": exterior_rows,
        "eta_cancellation_rows": eta_rows,
        "counts": {
            "matrix_rows": len(matrix_rows),
            "child_norm_rows": len(norm_rows),
            "exterior_rows": len(exterior_rows),
            "eta_cancellation_rows": len(eta_rows),
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(payload, end="")
    else:
        args.output.write_text(payload, encoding="utf-8")
    raise SystemExit(0 if result["status"] == "pass" else 1)
