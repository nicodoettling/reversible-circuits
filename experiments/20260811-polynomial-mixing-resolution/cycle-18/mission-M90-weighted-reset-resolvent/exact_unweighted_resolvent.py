#!/usr/bin/env python3
"""Exact transformed unweighted reset resolvent and multitype budget scan.

For ``h(x)=q_x[(I-D)^(-1)J_can 1](x)``, cancellation of parent and child
split masses gives

    h(x)=A0(x)+sum_(k,t,j>=1) rho_s(k,t) nu(j) h(y),
    A0(x)=sum_e theta_e^2/Q_G(e).

On a right-heavy seed, ``h<=q(1-q)`` is exactly
``K_reset 1<=1-q`` and implies the assigned weighted inequality because
every reset target is right-heavy and ``W(y)=1-q_y<=1``.  The broader
multitype candidate budget is ``U0=q(1-q)(K-R)``.  Every attachment rank
``j>=1`` is retained.  Finite survival proves no theorem.
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

import exact_weighted_resolvent as EXACT


def fraction_record(value: Fraction) -> dict[str, object]:
    return {
        "decimal": float(value),
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


@functools.lru_cache(maxsize=None)
def reset_unweighted_budget(s: int, K: int, R: int, B: int) -> Fraction:
    """Return ``A0=sum_e theta_e^2/Q_G(e)`` exactly."""
    q_parent = EXACT.q_split(s, B)
    answer = Fraction(0)
    scalar_cache: dict[tuple[int, int, int], Fraction] = {}

    def basin_scalar(A: int, ell: int, last: int) -> Fraction:
        key = (A, ell, last)
        if key not in scalar_cache:
            value = Fraction(0)
            for p in range(1, A + 1):
                coefficient = EXACT.cayley(A, p)
                if coefficient:
                    value += coefficient * (
                        EXACT.contextual_value(p + ell, last, K, R, B)
                        - q_parent
                    ) / math.factorial(p + ell)
            scalar_cache[key] = value
        return scalar_cache[key]

    for ell in range(1, s):
        tail_parts = ell - 1
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
                    tail_rows = ((b, EXACT.w(b)),)
                else:
                    rows = []
                    for last in range(1, tail_total + 1):
                        prefix = EXACT.cayley(tail_total - last, tail_parts - 1)
                        if prefix:
                            rows.append(
                                (last, EXACT.w(b) * prefix * EXACT.w(last))
                            )
                    tail_rows = tuple(rows)
                for last, suffix_weight in tail_rows:
                    scalar = basin_scalar(A, ell, last)
                    answer += (
                        suffix_weight
                        * math.factorial(ell)
                        * scalar
                        * scalar
                        / (EXACT.w(A) * EXACT.w(s + 1))
                    )
    return answer


def deep_children(x: tuple[int, int, int, int]):
    s, K, R, B = x
    rows = []
    parent_phase = s + K - R
    for k, t, mass in EXACT.groups(s):
        if t <= B or t - 1 < 2:
            continue
        for j in range(1, k + 1):
            probability = EXACT.nu(K, R, k, j)
            if probability:
                child = (t - 1, K + k, R + j, B)
                if child[0] + child[1] - child[2] >= parent_phase:
                    raise AssertionError(("phase", x, child))
                rows.append((mass * probability, child))
    return tuple(rows)


class ExactUnweighted:
    def __init__(self) -> None:
        self.contexts = 0

    @functools.lru_cache(maxsize=None)
    def h(self, s: int, K: int, R: int, B: int) -> Fraction:
        if s <= 1:
            return Fraction(0)
        self.contexts += 1
        x = (s, K, R, B)
        return reset_unweighted_budget(*x) + sum(
            (weight * self.h(*child) for weight, child in deep_children(x)),
            Fraction(),
        )

    @functools.lru_cache(maxsize=None)
    def defect_depth(self, x: tuple[int, int, int, int]):
        s, K, R, B = x
        q = EXACT.q_split(s, B)
        budget = q * (1 - q) * (K - R)
        children = deep_children(x)
        child_budget = sum(
            (
                weight
                * EXACT.q_split(child[0], child[3])
                * (1 - EXACT.q_split(child[0], child[3]))
                * (child[1] - child[2])
                for weight, child in children
            ),
            Fraction(),
        )
        profile = [budget - reset_unweighted_budget(*x) - child_budget]
        for weight, child in children:
            child_profile = self.defect_depth(child)
            while len(profile) < len(child_profile) + 1:
                profile.append(Fraction(0))
            for depth, value in enumerate(child_profile, start=1):
                profile[depth] += weight * value
        return tuple(profile)


def scan(s_values: list[int], K_values: list[int]) -> dict[str, object]:
    solver = ExactUnweighted()
    rows = []
    failures = []
    local_negative = []
    positive_depth_negative = []
    maximum = None
    minimum_local = None
    minimum_tail = None
    for s in s_values:
        rank_worst = None
        for K in K_values:
            for B in range(1, s + 1):
                x = (s, K, K - 1, B)
                q = EXACT.q_split(s, B)
                target = q * (1 - q)
                value = solver.h(*x)
                ratio = value / target
                profile = solver.defect_depth(x)
                if sum(profile, Fraction()) != target - value:
                    raise AssertionError(("telescoping", x))
                row = {
                    "context": list(x),
                    "q": fraction_record(q),
                    "transformed_unweighted_resolvent": fraction_record(value),
                    "target_variance": fraction_record(target),
                    "ratio": fraction_record(ratio),
                    "margin": fraction_record(target - value),
                    "local_multitype_defect": fraction_record(profile[0]),
                }
                if rank_worst is None or ratio > rank_worst[0]:
                    rank_worst = (ratio, row)
                if maximum is None or ratio > maximum[0]:
                    maximum = (ratio, row)
                normalized_local = profile[0] / target
                if minimum_local is None or normalized_local < minimum_local[0]:
                    minimum_local = (normalized_local, row)
                if value > target:
                    failures.append(row)
                if profile[0] < 0:
                    local_negative.append(row)
                tail = Fraction(0)
                for depth in range(len(profile) - 1, 0, -1):
                    tail += profile[depth]
                    tail_row = dict(row)
                    tail_row.update({
                        "depth": depth,
                        "depth_contribution": fraction_record(profile[depth]),
                        "reverse_tail": fraction_record(tail),
                    })
                    normalized_tail = tail / target
                    if minimum_tail is None or normalized_tail < minimum_tail[0]:
                        minimum_tail = (normalized_tail, tail_row)
                    if profile[depth] < 0:
                        positive_depth_negative.append(tail_row)
        rows.append({"s": s, "worst": rank_worst[1]})
        print(json.dumps(rows[-1], sort_keys=True), flush=True)
    return {
        "rank_worst_rows": rows,
        "overall_worst": maximum[1],
        "failure_count": len(failures),
        "first_failures": failures[:3],
        "negative_local_multitype_defect_count": len(local_negative),
        "first_negative_local_multitype_defects": local_negative[:3],
        "negative_positive_depth_contribution_count": len(positive_depth_negative),
        "first_negative_positive_depth_contributions": positive_depth_negative[:3],
        "minimum_normalized_local_defect": {
            "value": fraction_record(minimum_local[0]),
            "row": minimum_local[1],
        },
        "minimum_normalized_positive_depth_reverse_tail": {
            "value": fraction_record(minimum_tail[0]),
            "row": minimum_tail[1],
        },
        "memoized_contexts": solver.contexts,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-values", type=int, nargs="+", required=True)
    parser.add_argument("--K-values", type=int, nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    result = scan(args.s_values, args.K_values)
    payload = {
        "claim_tested": (
            "right-heavy K_reset 1<=1-q, sufficient for K_reset W<=W"
        ),
        "finite_scope_warning": "Exact bounded survival proves no universal inequality.",
        "arithmetic": "fractions.Fraction exact grouped Cayley recurrence",
        "normalization": (
            "h=q*(I-D)^-1*J_can*1; Q=rho*nu for every j>=1; "
            "A0=sum theta^2/Q_G"
        ),
        "strict_phase": "P=s+K-R decreases on every retained deep child",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "parameters": {"s_values": args.s_values, "K_values": args.K_values},
        "elapsed_seconds": time.time() - started,
        "result": result,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "elapsed_seconds": payload["elapsed_seconds"],
        "overall_worst": result["overall_worst"],
        "failure_count": result["failure_count"],
        "negative_local_multitype_defect_count": (
            result["negative_local_multitype_defect_count"]
        ),
        "negative_positive_depth_contribution_count": (
            result["negative_positive_depth_contribution_count"]
        ),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
