#!/usr/bin/env python3
"""Exact character falsifier for a perfect-matching endpoint square mode.

For even l, set N=2l and let h have cycle type 2^l.  The script computes the
correlation of 1{p(X_i)=e} under the length-l raw-microincrement bridge using
Murnaghan--Nakayama and the central class-sum formula.  A growing additive
Gram Rayleigh quotient could refute a universal O(1/l) correlation claim.
Finite values cannot prove such a claim.
"""

from __future__ import annotations

import argparse
import functools
import json
import math
import platform
from fractions import Fraction
from pathlib import Path

Shape = tuple[int, ...]


def partitions(n: int, maximum: int | None = None):
    if n == 0:
        yield ()
        return
    maximum = n if maximum is None else min(maximum, n)
    for first in range(maximum, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def dimension_content(shape: Shape) -> tuple[int, int]:
    n = sum(shape)
    hooks = 1
    content = 0
    for i, row_len in enumerate(shape):
        for j in range(row_len):
            below = sum(lower > j for lower in shape[i + 1 :])
            hooks *= row_len - j + below
            content += j - i
    return math.factorial(n) // hooks, content


def subpartitions_of_size(shape: Shape, target: int):
    rows = len(shape)

    def rec(i: int, previous: int, remaining: int, prefix: list[int]):
        if i == rows:
            if remaining == 0:
                while prefix and prefix[-1] == 0:
                    prefix.pop()
                yield tuple(prefix)
            return
        maximum = min(shape[i], previous, remaining)
        tail_capacity = sum(min(shape[j], maximum) for j in range(i + 1, rows))
        minimum = max(0, remaining - tail_capacity)
        for value in range(maximum, minimum - 1, -1):
            yield from rec(i + 1, value, remaining - value, prefix + [value])

    yield from rec(0, shape[0] if shape else 0, target, [])


def border_strip(shape: Shape, lower: Shape, size: int) -> int | None:
    padded = lower + (0,) * (len(shape) - len(lower))
    cells = {
        (i, j)
        for i, row_len in enumerate(shape)
        for j in range(padded[i], row_len)
    }
    if len(cells) != size or not cells:
        return None
    seen = {next(iter(cells))}
    frontier = list(seen)
    while frontier:
        i, j = frontier.pop()
        for neighbor in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if neighbor in cells and neighbor not in seen:
                seen.add(neighbor)
                frontier.append(neighbor)
    if seen != cells:
        return None
    for i, j in cells:
        if {(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)} <= cells:
            return None
    return len({i for i, _j in cells})


@functools.cache
def character(shape: Shape, cycles: tuple[int, ...]) -> int:
    if not cycles:
        return int(not shape)
    size = cycles[0]
    target = sum(shape) - size
    total = 0
    for lower in subpartitions_of_size(shape, target):
        height = border_strip(shape, lower, size)
        if height is not None:
            total += (-1) ** (height - 1) * character(lower, cycles[1:])
    return total


def scaled_completion(n: int, steps: int, endpoint_cycles: tuple[int, ...]) -> int:
    # Returns n! [h] W^steps. The common n! cancels from all probabilities.
    return sum(
        dimension * character(shape, endpoint_cycles) * content ** (2 * steps)
        for shape in partitions(n)
        for dimension, content in [dimension_content(shape)]
    )


def decimal(q: Fraction) -> float:
    return q.numerator / q.denominator


def record(length: int) -> dict:
    n = 2 * length
    endpoint_cycles = (2,) * length
    s_l = scaled_completion(n, length, endpoint_cycles)
    s_1 = scaled_completion(n, length - 1, endpoint_cycles)
    s_2 = scaled_completion(n, length - 2, endpoint_cycles)
    assert s_l > 0
    m = n * (n - 1) // 2
    p = Fraction(m * s_1, s_l)
    p_pair = Fraction(m * m * s_2, s_l)
    kappa = (p_pair - p * p) / (p * (1 - p))
    additive_rayleigh = Fraction(1 + (length - 1) * kappa, length)
    return {
        "N": n,
        "length": length,
        "endpoint_cycle_type": list(endpoint_cycles),
        "partition_count": sum(1 for _ in partitions(n)),
        "square_probability": str(p),
        "square_pair_probability": str(p_pair),
        "square_correlation": str(kappa),
        "square_correlation_decimal": decimal(kappa),
        "additive_gram_rayleigh": str(additive_rayleigh),
        "additive_gram_rayleigh_decimal": decimal(additive_rayleigh),
        "length_times_rayleigh_decimal": length * decimal(additive_rayleigh),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lengths", default="4,6,8,10,12")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    lengths = [int(x) for x in args.lengths.split(",") if x]
    assert all(length >= 4 and length % 2 == 0 for length in lengths)
    payload = {
        "status": "complete",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "composition": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "formula": "N! [h]W^r=sum_lambda d_lambda chi_lambda(h)c_lambda^(2r)",
        "claim_falsifier": (
            "If l times the additive Gram Rayleigh quotient diverges, then "
            "the universal mu_l(h)<=A/l claim is false."
        ),
        "scope_warning": (
            "Exact finite character values can refute, but cannot prove, a "
            "uniform asymptotic correlation bound."
        ),
        "records": [record(length) for length in lengths],
    }
    Path(args.output).write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
