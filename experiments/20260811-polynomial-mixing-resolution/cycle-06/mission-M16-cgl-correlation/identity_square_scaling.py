#!/usr/bin/env python3
"""Exact scalable identity-endpoint tests of two coordinate modes.

For W=(sum_{t in T_N} t)^2 and H_r(e)=[e]W^r, character theory gives

    H_r(e) = (1/N!) sum_{lambda |- N} d_lambda^2 c_lambda^(2r),

where d_lambda is the Specht dimension and c_lambda is the sum of the
contents of lambda.  This needs only partitions and integer arithmetic.

For the identity bridge, Y_i=1{p(X_i)=e} has exact pair correlation

    kappa = Corr(Y_1,Y_2),

computed from P(Y_1=1)=M H_{l-1}/H_l and
P(Y_1=Y_2=1)=M^2 H_{l-2}/H_l.  The script is a named falsifier for a
constant-correlation obstruction to the proposed O(1/l) maximal-correlation
bound.

It also treats the stronger fixed-label statistic Z_i=1{p(X_i) moves 0}.
If A is the transposition class sum in S_{N-1} (the stabilizer of 0), then
the weighted group-algebra element for this event is

    F = W - A^2 - (N-1)e.

On the S_{N-1}-summand mu inside an S_N irrep lambda, F has eigenvalue
c_lambda^2-c_mu^2-(N-1).  The multiplicity-free branching rule therefore
gives exact integer formulas for [e]FW^(l-1) and [e]F^2W^(l-2).

A finite grid cannot prove the uniform maximal-correlation bound.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
from fractions import Fraction
from pathlib import Path


def partitions(n: int, maximum: int | None = None):
    if n == 0:
        yield ()
        return
    if maximum is None or maximum > n:
        maximum = n
    for first in range(maximum, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def dimension_and_content(shape: tuple[int, ...]) -> tuple[int, int]:
    n = sum(shape)
    hook_product = 1
    content = 0
    for i, row_length in enumerate(shape):
        for j in range(row_length):
            below = sum(1 for lower in shape[i + 1 :] if lower > j)
            hook_product *= row_length - j + below
            content += j - i
    return math.factorial(n) // hook_product, content


def return_moment(data: list[tuple[int, int]], r: int) -> int:
    # This is N! H_r(e).  The common N! cancels from every ratio below.
    return sum(dimension * dimension * content ** (2 * r)
               for dimension, content in data)


def removable_shapes(shape: tuple[int, ...]):
    for i, row_length in enumerate(shape):
        next_length = shape[i + 1] if i + 1 < len(shape) else 0
        if row_length > next_length:
            reduced = list(shape)
            reduced[i] -= 1
            if reduced[i] == 0:
                reduced.pop(i)
            yield tuple(reduced)


def label_traces(
    shape: tuple[int, ...],
    dimension: int,
    content: int,
    lower_data: dict[tuple[int, ...], tuple[int, int]],
) -> tuple[int, int]:
    """Return Tr_lambda(F), Tr_lambda(F^2) by S_N down S_(N-1)."""
    n = sum(shape)
    trace = 0
    trace_square = 0
    branch_dimension = 0
    for lower_shape in removable_shapes(shape):
        lower_dimension, lower_content = lower_data[lower_shape]
        eigenvalue = content * content - lower_content * lower_content - (n - 1)
        trace += lower_dimension * eigenvalue
        trace_square += lower_dimension * eigenvalue * eigenvalue
        branch_dimension += lower_dimension
    assert branch_dimension == dimension
    return trace, trace_square


def fraction_decimal(value: Fraction) -> float:
    return value.numerator / value.denominator


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N-values", default="4,6,8,10,12,16,20,24,30,36,40")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    records = []
    for n in [int(x) for x in args.N_values.split(",") if x]:
        shapes = list(partitions(n))
        shape_data = {shape: dimension_and_content(shape) for shape in shapes}
        lower_data = {
            shape: dimension_and_content(shape) for shape in partitions(n - 1)
        }
        data = list(shape_data.values())
        traced_data = [
            (dimension, content, *label_traces(
                shape, dimension, content, lower_data
            ))
            for shape, (dimension, content) in shape_data.items()
        ]
        lengths = sorted(set(
            [3, 4, 5, max(3, n // 4), max(3, n // 2), max(3, n - 1),
             max(3, n), max(3, 2 * n),
             max(3, math.ceil(n * math.log(n + 1)))]
        ))
        moments = {r: return_moment(data, r)
                   for r in range(1, max(lengths) + 1)}
        m = n * (n - 1) // 2
        for length in lengths:
            s_l = moments[length]
            s_1 = moments[length - 1]
            s_2 = moments[length - 2]
            p = Fraction(m * s_1, s_l)
            p_pair = Fraction(m * m * s_2, s_l)
            if p in (0, 1):
                kappa = Fraction(0)
            else:
                kappa = (p_pair - p * p) / (p * (1 - p))
            label_numerator = sum(
                dimension * content ** (2 * (length - 1)) * trace
                for dimension, content, trace, _trace_square in traced_data
            )
            label_pair_numerator = sum(
                dimension * content ** (2 * (length - 2)) * trace_square
                for dimension, content, _trace, trace_square in traced_data
            )
            label_p = Fraction(label_numerator, s_l)
            label_pair_p = Fraction(label_pair_numerator, s_l)
            if label_p in (0, 1):
                label_kappa = Fraction(0)
            else:
                label_kappa = (
                    (label_pair_p - label_p * label_p)
                    / (label_p * (1 - label_p))
                )
            records.append({
                "N": n,
                "length": length,
                "partition_count": len(data),
                "square_probability_decimal": fraction_decimal(p),
                "square_pair_correlation_decimal": fraction_decimal(kappa),
                "length_times_correlation_decimal": fraction_decimal(length * kappa),
                "correlation_exact": f"{kappa.numerator}/{kappa.denominator}",
                "label_moved_probability_decimal": fraction_decimal(label_p),
                "label_moved_pair_correlation_decimal": fraction_decimal(label_kappa),
                "length_times_label_correlation_decimal": fraction_decimal(
                    length * label_kappa
                ),
                "label_correlation_exact": (
                    f"{label_kappa.numerator}/{label_kappa.denominator}"
                ),
            })

    payload = {
        "status": "complete",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "composition": "(pq)(x)=p(q(x)); tuple product left-to-right",
        "formula": "N! H_r(e)=sum_{lambda|-N} d_lambda^2 c_lambda^(2r)",
        "claim_falsifier": (
            "If either the square or fixed-label coordinate correlation stays "
            "bounded below along growing N,l, then the uniform O(1/l) "
            "maximal-correlation claim fails."
        ),
        "scope_warning": (
            "Exact finite class-function values can refute but cannot prove the "
            "uniform maximal-correlation bound."
        ),
        "records": records,
    }
    Path(args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
