#!/usr/bin/env python3
"""Exact grouped audits for phase/beta-binomial Bellman potentials.

This script evaluates one raw marked-DAG row, not an eliminated resolvent.
It groups root compositions by their part count, first two parts, and last
part using the exact Cayley coefficient

    [z^a] T(z)^p = p a^(a-p-1)/(a-p)!.

All arithmetic is ``fractions.Fraction``.  Its intended use is exact
certification of candidate Lyapunov inequalities after a floating discovery
scan; a finite row below one proves no universal claim.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import platform
import time
from fractions import Fraction
from pathlib import Path


@functools.lru_cache(maxsize=None)
def w(a: int) -> Fraction:
    if a < 1:
        raise ValueError(a)
    return Fraction(a ** (a - 1), math.factorial(a))


@functools.lru_cache(maxsize=None)
def cayley(total: int, parts: int) -> Fraction:
    """Return the product-weight sum over positive ``parts``-compositions."""
    if parts == 0:
        return Fraction(int(total == 0))
    if not (1 <= parts <= total):
        return Fraction(0)
    return Fraction(
        parts * total ** (total - parts),
        total * math.factorial(total - parts),
    )


def q_split(s: int, B: int) -> Fraction:
    return w(s + 1 - B) * w(B) / w(s + 1)


def comb_ratio(n1: int, k1: int, n2: int, k2: int) -> Fraction:
    if not (0 <= k1 <= n1 and 0 <= k2 <= n2):
        return Fraction(0)
    return Fraction(math.comb(n1, k1), math.comb(n2, k2))


def contextual_value(k: int, t: int, K: int, R: int, B: int) -> Fraction:
    if t < B:
        return Fraction(0)
    if t == B:
        return K * comb_ratio(
            k + K - R - 2,
            K - R - 1,
            k + K - 1,
            K - 1,
        )
    local = w(t - B) * w(B) / w(t)
    bad = comb_ratio(K, R + 1, K + k, R + 1)
    return local * (1 - bad)


def negative_hypergeometric(K: int, R: int, k: int, j: int) -> Fraction:
    return Fraction(
        math.comb(R + j, j)
        * math.comb(K - R - 1 + k - j, k - j),
        math.comb(K + k, k),
    )


def potential(s: int, K: int, R: int, B: int, exponent: int) -> Fraction:
    P = s + K - R
    return (
        P**exponent
        * (1 - q_split(s, B))
        * Fraction(K, R + 1)
    )


def group_mass(s: int, k: int, t: int) -> Fraction:
    return w(t) * cayley(s - t, k - 1) / (math.factorial(k) * w(s + 1))


def deep_weighted(
    s: int,
    K: int,
    R: int,
    B: int,
    exponent: int,
    floor_scale: int | None = None,
) -> Fraction | tuple[int, int]:
    q_parent = q_split(s, B)
    answer: Fraction | int = Fraction(0) if floor_scale is None else 0
    term_count = 0
    for k in range(1, s + 1):
        for t in range(B + 1, s + 1):
            mass = group_mass(s, k, t)
            if not mass or t - 1 < 2:
                continue
            q_child = q_split(t - 1, B)
            for j in range(1, k + 1):
                nu = negative_hypergeometric(K, R, k, j)
                if nu:
                    term = (
                        mass
                        * q_child
                        * nu
                        / q_parent
                        * potential(t - 1, K + k, R + j, B, exponent)
                    )
                    if floor_scale is None:
                        answer += term
                    else:
                        answer += term.numerator * floor_scale // term.denominator
                        term_count += 1
    if floor_scale is None:
        return answer
    return int(answer), term_count


def reset_weighted(
    s: int,
    K: int,
    R: int,
    B: int,
    exponent: int,
    floor_scale: int | None = None,
) -> Fraction | tuple[int, int]:
    """Exact canonical first-boundary reset contribution ``J_can U``."""
    q_parent = q_split(s, B)
    answer: Fraction | int = Fraction(0) if floor_scale is None else 0
    term_count = 0
    scalar_cache: dict[tuple[int, int, int], Fraction] = {}

    def basin_scalar(A: int, l: int, last: int) -> Fraction:
        key = (A, l, last)
        if key not in scalar_cache:
            value = Fraction(0)
            for p in range(1, A + 1):
                coefficient = cayley(A, p)
                if coefficient:
                    value += (
                        coefficient
                        * (
                            contextual_value(p + l, last, K, R, B)
                            - q_parent
                        )
                        / math.factorial(p + l)
                    )
            scalar_cache[key] = value
        return scalar_cache[key]

    # Refined endpoint is (A,b,tail), with l suffix parts after A.
    for l in range(1, s):
        tail_parts = l - 1
        for A in range(1, s + 1):
            max_b = s - A - tail_parts
            for b in range(1, max_b + 1):
                tail_total = s - A - b
                child_rank = A + b - 1
                if child_rank < 2:
                    continue
                if tail_parts == 0:
                    if tail_total != 0:
                        continue
                    tail_rows = ((b, w(b)),)
                else:
                    rows = []
                    for last in range(1, tail_total + 1):
                        prefix_weight = cayley(
                            tail_total - last, tail_parts - 1
                        )
                        if prefix_weight:
                            rows.append((last, w(b) * prefix_weight * w(last)))
                    tail_rows = tuple(rows)

                child_U = potential(child_rank, l, l - 1, b, exponent)
                for last, suffix_weight in tail_rows:
                    scalar = basin_scalar(A, l, last)
                    energy = (
                        suffix_weight
                        * math.factorial(l)
                        * scalar
                        * scalar
                        / (w(A) * w(s + 1) * q_parent)
                    )
                    term = energy * child_U
                    if floor_scale is None:
                        answer += term
                    else:
                        answer += term.numerator * floor_scale // term.denominator
                        term_count += 1
    if floor_scale is None:
        return answer
    return int(answer), term_count


def fraction_record(value: Fraction) -> dict[str, object]:
    return {
        "decimal": float(value),
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def evaluate(
    s: int,
    K: int,
    R: int,
    B: int,
    exponent: int,
    lower_bound_digits: int | None,
) -> dict:
    started = time.time()
    parent = potential(s, K, R, B, exponent)
    if lower_bound_digits is not None:
        scale = 10**lower_bound_digits
        deep_floor, deep_terms = deep_weighted(
            s, K, R, B, exponent, floor_scale=scale
        )
        reset_floor, reset_terms = reset_weighted(
            s, K, R, B, exponent, floor_scale=scale
        )
        lower_floor = deep_floor + reset_floor
        lower = Fraction(lower_floor, scale)
        certified = lower > parent
        return {
            "context": {"s": s, "K": K, "R": R, "B": B},
            "exponent": exponent,
            "parent_potential": fraction_record(parent),
            "lower_bound_digits": lower_bound_digits,
            "deep_term_count": deep_terms,
            "reset_term_count": reset_terms,
            "deep_lower_floor_integer": str(deep_floor),
            "reset_lower_floor_integer": str(reset_floor),
            "total_lower_bound": fraction_record(lower),
            "lower_minus_parent": fraction_record(lower - parent),
            "certified_total_greater_than_parent": certified,
            "certificate_explanation": (
                "Each nonnegative exact rational summand was rounded down "
                "individually to the stated common decimal scale. Their sum "
                "is therefore a rigorous lower bound on the Bellman left side."
            ),
            "elapsed_seconds": time.time() - started,
        }
    deep = deep_weighted(s, K, R, B, exponent)
    reset = reset_weighted(s, K, R, B, exponent)
    total = deep + reset
    return {
        "context": {"s": s, "K": K, "R": R, "B": B},
        "exponent": exponent,
        "parent_potential": fraction_record(parent),
        "deep_weighted": fraction_record(deep),
        "reset_weighted": fraction_record(reset),
        "total_weighted": fraction_record(total),
        "ratio": fraction_record(total / parent),
        "total_minus_parent": fraction_record(total - parent),
        "elapsed_seconds": time.time() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s", type=int, required=True)
    parser.add_argument("--K", type=int, required=True)
    parser.add_argument("--R", type=int, required=True)
    parser.add_argument("--B", type=int, required=True)
    parser.add_argument("--exponent", type=int, required=True)
    parser.add_argument("--lower-bound-digits", type=int)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "claim_tested": (
            "Raw Bellman inequality for U=P^d(1-q)K/(R+1)"
        ),
        "arithmetic": "fractions.Fraction exact grouped Cayley sums",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "result": evaluate(
            args.s,
            args.K,
            args.R,
            args.B,
            args.exponent,
            args.lower_bound_digits,
        ),
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "result": result["result"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
