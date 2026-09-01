#!/usr/bin/env python3
"""Clean-room exact certificate for the frozen M179 h=2 theorem.

Standard library only.  This file imports no predecessor code or data and
checks only named decisive algebra/boundary rows; it is not an enumeration.
"""

from __future__ import annotations

import argparse
import functools
import json
import math
import platform
from fractions import Fraction as Q
from pathlib import Path


Poly = tuple[Q, ...]


def trim(poly: list[Q] | tuple[Q, ...]) -> Poly:
    out = list(poly)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def add(left: Poly, right: Poly) -> Poly:
    out = [Q(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    return trim(out)


def scale(poly: Poly, scalar: Q) -> Poly:
    return trim([scalar * value for value in poly])


def multiply(left: Poly, right: Poly) -> Poly:
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return trim(out)


def monomial(degree: int, coefficient: Q = Q(1)) -> Poly:
    return tuple([Q(0)] * degree + [coefficient])


def rising(start: int, length: int) -> int:
    return math.prod(range(start, start + length)) if length else 1


def beta_moment(alpha: int, beta: int, degree: int) -> Q:
    return Q(rising(alpha, degree), rising(alpha + beta, degree))


def expectation(poly: Poly, alpha: int, beta: int) -> Q:
    return sum(
        (coefficient * beta_moment(alpha, beta, degree)
         for degree, coefficient in enumerate(poly)),
        Q(0),
    )


def likelihood(d: int, a: int) -> Poly:
    out = [Q(0)] * (d + 1)
    for extra in range(d - a + 1):
        out[a + extra] += Q(
            math.comb(d, a)
            * math.comb(d - a, extra)
            * (-1) ** extra
        )
    return trim(out)


def posterior(d: int, a: int, trace_override: Q | None = None) -> dict[str, Q]:
    p = Q(a + 1, d + 2)
    variance = Q((a + 1) * (d - a + 1), (d + 2) ** 2 * (d + 3))
    delta = p - Q(1, 2)
    second_mean = Q(2 * a + 1, 2 * (d + 1))
    second_variance = Q(
        (2 * a + 1) * (2 * d - 2 * a + 1),
        (2 * d + 2) ** 2 * (2 * d + 3),
    )
    lambda0 = (
        Q(d + 1, 2 * d + 1)
        * Q(math.comb(d, a) ** 2, math.comb(2 * d, 2 * a))
        if trace_override is None
        else trace_override
    )
    shift = second_mean - p
    lambda1 = lambda0 * shift
    lambda2 = lambda0 * (second_variance + shift * shift)
    pi = Q(1, d + 1)
    g00 = lambda0 - 12 * pi * delta * delta
    g01_squared = (lambda1 - 12 * pi * delta * variance) ** 2 / variance
    g11 = lambda2 / variance - 12 * pi * variance
    return {
        "p": p,
        "variance": variance,
        "delta": delta,
        "lambda0": lambda0,
        "lambda1": lambda1,
        "lambda2": lambda2,
        "g00": g00,
        "g01_squared": g01_squared,
        "g11": g11,
    }


def branch_direct(d: int, a: int, mean: Q, covariance: Q) -> Q:
    """Parent-uniform Q of L*Phi/sqrt(pi), with eta divided out."""
    child_p = Q(a + 1, d + 2)
    child_v = Q((a + 1) * (d - a + 1), (d + 2) ** 2 * (d + 3))
    phi = (mean - child_p * covariance / child_v, covariance / child_v)
    lifted = multiply(likelihood(d, a), phi)
    pi = Q(1, d + 1)
    centered = (Q(-1, 2), Q(1))
    trace = expectation(multiply(lifted, lifted), 1, 1) / pi
    first = expectation(multiply(centered, lifted), 1, 1)
    return trace - first * first / (pi * Q(1, 12))


def branch_formula(d: int, a: int, mean: Q, covariance: Q) -> Q:
    data = posterior(d, a)
    v = data["variance"]
    return (
        data["lambda0"] * mean * mean
        + 2 * data["lambda1"] * mean * covariance / v
        + data["lambda2"] * covariance * covariance / (v * v)
        - Q(12, d + 1) * (data["delta"] * mean + covariance) ** 2
    )


def determinant_polynomial(d: int, x: int) -> int:
    a0 = (d - 1) * (d + 2) ** 3 * (
        5 * d**4 + 24 * d**3 + 64 * d**2 + 72 * d + 18
    )
    a1 = (
        -5 * d**6 + 43 * d**5 + 480 * d**4 + 1658 * d**3
        + 2729 * d**2 + 2025 * d + 414
    )
    a2 = 90 * d**3 + 387 * d**2 + 603 * d + 216
    return a0 + a1 * x - a2 * x * x


def loewner_row(d: int, a: int) -> dict[str, Q]:
    upper_lambda0 = Q(d + 1, 2 * d + 1)
    data = posterior(d, a, upper_lambda0)
    s00 = Q(2, 3) - data["g00"]
    s11 = Q(2, 3) - data["g11"]
    determinant = s00 * s11 - data["g01_squared"]
    x = (2 * a - d) ** 2

    expected_s00 = Q(
        (d - 1) * (d + 1) * (d + 2) ** 2 + (18 * d + 9) * x,
        3 * (d + 1) * (d + 2) ** 2 * (2 * d + 1),
    )
    n11 = (
        5 * d**6 + 44 * d**5 + 180 * d**4 + 424 * d**3
        + 562 * d**2 + 360 * d + 72
        - (36 * d**2 + 72 * d + 27) * x
    )
    expected_s11 = Q(
        n11,
        3 * (d + 1) * (d + 2) ** 2 * (d + 3) * (2 * d + 1) * (2 * d + 3),
    )
    det_denominator = (
        9 * (d + 1) * (d + 2) * (d + 3)
        * (2 * d + 1) ** 2 * (2 * d + 3) * ((d + 2) ** 2 - x)
    )
    expected_det = Q(determinant_polynomial(d, x), det_denominator)
    return {
        "actual_lambda0": posterior(d, a)["lambda0"],
        "upper_lambda0": upper_lambda0,
        "s00": s00,
        "s11": s11,
        "determinant": determinant,
        "expected_s00": expected_s00,
        "expected_s11": expected_s11,
        "expected_determinant": expected_det,
    }


@functools.lru_cache(None)
def w(n: int) -> Q:
    return Q(n ** (n - 1), math.factorial(n))


@functools.lru_cache(None)
def compositions(total: int) -> tuple[tuple[int, ...], ...]:
    if total == 0:
        return ((),)
    return tuple(
        (head,) + tail
        for head in range(1, total + 1)
        for tail in compositions(total - head)
    )


def qsplit(s: int, bottom: int) -> Q:
    return w(s + 1 - bottom) * w(bottom) / w(s + 1)


def root_mass(source: tuple[int, ...]) -> Q:
    return math.prod(w(part) for part in source) / (
        math.factorial(len(source)) * w(sum(source) + 1)
    )


def active_endpoints(s: int) -> tuple[tuple[int, ...], ...]:
    endpoints: set[tuple[int, ...]] = set()
    for source in compositions(s):
        for cut in range(1, len(source)):
            if sum(source[:cut]) + source[cut] - 1 >= 2:
                endpoints.add((sum(source[:cut]),) + source[cut:])
    return tuple(sorted(endpoints, key=lambda e: (len(e), e)))


def in_basin(source: tuple[int, ...], endpoint: tuple[int, ...]) -> bool:
    return any(
        sum(source[:cut]) == endpoint[0] and source[cut:] == endpoint[1:]
        for cut in range(1, len(source) + 1)
    )


def point_context(source: tuple[int, ...], bottom: int) -> Poly:
    degree = len(source)
    last = source[-1]
    if last < bottom:
        return (Q(0),)
    if last == bottom:
        return monomial(degree - 1, Q(degree))
    split = qsplit(last - 1, bottom)
    return add((split,), monomial(degree, -split))


@functools.lru_cache(None)
def reset_rows(s: int, bottom: int) -> tuple[tuple[tuple[int, ...], Poly, Q, Q], ...]:
    q = qsplit(s, bottom)
    rows = []
    sources = compositions(s)
    for endpoint in active_endpoints(s):
        basin = tuple(source for source in sources if in_basin(source, endpoint))
        current: Poly = (Q(0),)
        for source in basin:
            centered = add(point_context(source, bottom), (Q(-q),))
            current = add(current, scale(centered, root_mass(source)))
        capacity = Q(len(endpoint)) * root_mass(endpoint)
        basin_mass = sum((root_mass(source) for source in basin), Q(0))
        rows.append((endpoint, current, capacity, basin_mass))
    return tuple(rows)


def reset_trace(s: int, bottom: int, alpha: int, beta: int) -> Q:
    q = qsplit(s, bottom)
    return sum(
        (expectation(multiply(current, current), alpha, beta) / (q * capacity)
         for _, current, capacity, _ in reset_rows(s, bottom)),
        Q(0),
    )


def child_trace_row(B: int, d: int, a: int) -> dict[str, Q | int]:
    if B == 1:
        assert reset_rows(2, 1) == ()
        return {
            "B": B,
            "d": d,
            "a": a,
            "reset_trace": Q(0),
            "ordinary_trace": Q(0),
            "envelope": Q(0),
            "target": Q(3, 4) if d == 1 else Q(1),
        }

    alpha = a + 1
    beta = d - a + 1
    p = Q(alpha, d + 2)
    z = Q(1, d + 3)
    variance = p * (1 - p) * z
    y = w(B) / w(B + 1)
    b = w(B) / w(B + 2)
    height = Q(B, B + 2)
    total_reset = reset_trace(B + 1, B, alpha, beta)

    exceptional = None
    for endpoint, current, capacity, basin_mass in reset_rows(B + 1, B):
        if endpoint == (1, B):
            assert capacity == b and basin_mass == b / 2
            assert current == scale((Q(-b, 2), Q(1)), b)
            exceptional = expectation(
                multiply((Q(-b, 2), Q(1)), (Q(-b, 2), Q(1))), alpha, beta
            )
            break
    assert exceptional is not None
    ordinary = total_reset - exceptional
    ordinary_bound = b * (height - b / 2)
    descendant_bound = (1 - p + p * z) * (1 - y)
    envelope = ordinary_bound + exceptional + descendant_bound
    target = Q(3, 4) if d == 1 else Q(1)
    return {
        "B": B,
        "d": d,
        "a": a,
        "reset_trace": total_reset,
        "ordinary_trace": ordinary,
        "ordinary_bound": ordinary_bound,
        "envelope": envelope,
        "target": target,
        "variance": variance,
    }


def cayley(n: int, r: int) -> Q:
    if (n, r) == (0, 0) or r == n:
        return Q(1)
    return Q(r * n ** (n - r - 1), math.factorial(n - r))


def eta_closed(n: int, r: int) -> Q:
    return cayley(n, r) / (math.factorial(r + 1) * w(n + 3))


def eta_direct(B: int, n: int, r: int) -> Q:
    degree = r + 1
    s = B + n + 2
    last = B + 2
    group = w(last) * cayley(n, r) / (math.factorial(degree) * w(s + 1))
    child_q = w(2) * w(B) / w(B + 2)
    parent_q = w(n + 3) * w(B) / w(s + 1)
    return group * child_q / parent_q


def record(value: Q) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def run() -> dict[str, object]:
    failures: list[str] = []

    # Different asymmetric specialization from the frozen checker.
    direct = branch_direct(5, 3, Q(-4, 7), Q(5, 13))
    formula = branch_formula(5, 3, Q(-4, 7), Q(5, 13))
    if direct != formula:
        failures.append("Bayes-normalized affine branch")

    d1 = posterior(1, 0)
    if (d1["g00"], d1["g01_squared"], d1["g11"]) != (
        Q(1, 2), Q(0), Q(1, 5)
    ):
        failures.append("d=1 retained matrix")

    matrix_rows: list[dict[str, object]] = []
    for d, observations in ((2, (0, 1)), (5, (0, 2, 4)), (11, (0, 5, 10))):
        p0 = determinant_polynomial(d, 0)
        pd2 = determinant_polynomial(d, d * d)
        expected_pd2 = (d + 1) * (2 * d + 1) * (
            d**5 + 152 * d**4 + 557 * d**3 + 658 * d**2 - 216 * d - 144
        )
        if p0 <= 0 or pd2 != expected_pd2 or pd2 <= 0:
            failures.append(f"determinant endpoints d={d}")
        for a in observations:
            row = loewner_row(d, a)
            if row["actual_lambda0"] > row["upper_lambda0"]:
                failures.append(f"Vandermonde Loewner increase d={d},a={a}")
            if (
                row["s00"] != row["expected_s00"]
                or row["s11"] != row["expected_s11"]
                or row["determinant"] != row["expected_determinant"]
                or min(row["s00"], row["s11"], row["determinant"]) <= 0
            ):
                failures.append(f"2/3 slack factorization d={d},a={a}")
            matrix_rows.append(
                {
                    "d": d,
                    "a": a,
                    "actual_lambda0": record(row["actual_lambda0"]),
                    "slack_determinant": record(row["determinant"]),
                }
            )

    trace_rows: list[dict[str, object]] = []
    for B, d, a in (
        (1, 1, 0),
        (2, 1, 0),
        (5, 1, 0),
        (2, 2, 0),
        (2, 2, 1),
        (4, 5, 0),
        (4, 5, 2),
        (4, 5, 4),
    ):
        row = child_trace_row(B, d, a)
        if row["ordinary_trace"] < 0:
            failures.append(f"negative ordinary history trace B={B},d={d},a={a}")
        if B >= 2 and row["ordinary_trace"] > row["ordinary_bound"]:
            failures.append(f"canonical ordinary bound B={B},d={d},a={a}")
        if row["envelope"] > row["target"]:
            failures.append(f"actual-history trace envelope B={B},d={d},a={a}")
        trace_rows.append(
            {
                "B": B,
                "d": d,
                "a": a,
                "reset_trace": record(row["reset_trace"]),
                "envelope": record(row["envelope"]),
                "target": record(row["target"]),
            }
        )

    eta_rows: list[dict[str, object]] = []
    for B, n, r in ((1, 0, 0), (3, 1, 1), (6, 4, 1), (6, 4, 2), (6, 4, 4)):
        direct_eta = eta_direct(B, n, r)
        closed_eta = eta_closed(n, r)
        if direct_eta != closed_eta:
            failures.append(f"eta cancellation B={B},n={n},r={r}")
        eta_rows.append(
            {"B": B, "n": n, "r": r, "eta": record(direct_eta)}
        )

    moment_rows: list[dict[str, object]] = []
    for n in (0, 1, 2, 4):
        rs = (0,) if n == 0 else range(1, n + 1)
        moment = sum(((r + 1) * eta_closed(n, r) for r in rs), Q(0))
        closed = Q(2, 3) if n == 0 else Q(
            (n + 1) ** n * (n + 2), (n + 3) ** (n + 1)
        )
        sector = Q(2, 3) * moment if n else Q(1, 2) * Q(3, 4) * moment
        if moment != closed or sector > Q(1, 4):
            failures.append(f"exterior first moment n={n}")
        moment_rows.append(
            {"n": n, "first_moment": record(moment), "sector_bound": record(sector)}
        )

    return {
        "claim_audited": "frozen M179 fresh actual-history h=2 charge <=1/4",
        "scope": "h=2 only; no reset, h>=3, total AMV, gap, or terminal",
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "environment": {
            "python": platform.python_version(),
            "dependencies": "Python standard library only",
            "seed": None,
            "imports_predecessor_code_or_data": False,
            "exact_command": "python3 -B independent_exact.py --output independent_results.json",
        },
        "bayes_affine_cross_term": {
            "degree": 5,
            "observation": 3,
            "direct": record(direct),
            "matrix_formula": record(formula),
        },
        "degree_one_matrix": {
            "g00": record(d1["g00"]),
            "g01_squared": record(d1["g01_squared"]),
            "g11": record(d1["g11"]),
        },
        "matrix_rows": matrix_rows,
        "actual_history_trace_rows": trace_rows,
        "eta_rows": eta_rows,
        "exterior_moment_rows": moment_rows,
        "counts": {
            "matrix_rows": len(matrix_rows),
            "actual_history_trace_rows": len(trace_rows),
            "eta_rows": len(eta_rows),
            "exterior_moment_rows": len(moment_rows),
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    args.output.write_text(payload, encoding="utf-8")
