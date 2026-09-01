#!/usr/bin/env python3
"""Exact depth/terminal-rank profile of weighted resolvent slack.

For the transformed deep kernel ``Q(x,y)=rho_s(k,t) nu(j)`` and reset
reward ``A``, write ``g=(I-Q)^(-1)A``.  This script records the exact
depth contributions to ``g`` and to the defects of two candidate budgets:

    r_U = U-A-Q U,  U=q(1-q)K/(R+1),
    r_V = V-A-Q V,  V=Var(Phi).

Although either one-step defect can be negative, nilpotence gives the exact
whole-excursion identities ``U-g=sum_d Q^d r_U`` and
``V-g=sum_d Q^d r_V``.  Reset rewards are also grouped by the rank of the
right-heavy reset target.  These identities diagnose telescoping; they do
not prove positivity outside the evaluated context.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import platform
import time
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import contextual_second_moment as MOMENT
import exact_weighted_resolvent as EXACT


def record(value: Fraction) -> dict[str, object]:
    return {
        "decimal": float(value),
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


@functools.lru_cache(maxsize=None)
def reset_by_rank(s: int, K: int, R: int, B: int):
    q_parent = EXACT.q_split(s, B)
    answer = defaultdict(Fraction)
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
                q_child = EXACT.q_split(child_rank, b)
                for last, suffix_weight in tail_rows:
                    scalar = basin_scalar(A, ell, last)
                    energy = (
                        suffix_weight
                        * math.factorial(ell)
                        * scalar
                        * scalar
                        / (EXACT.w(A) * EXACT.w(s + 1))
                    )
                    answer[child_rank] += energy * (1 - q_child)
    total = sum(answer.values(), Fraction())
    if total != EXACT.reset_budget(s, K, R, B):
        raise AssertionError((s, K, R, B, total, EXACT.reset_budget(s, K, R, B)))
    return tuple(sorted(answer.items()))


def deep_children(x: tuple[int, int, int, int]):
    s, K, R, B = x
    rows = []
    for k, t, mass in EXACT.groups(s):
        if t <= B or t - 1 < 2:
            continue
        for j in range(1, k + 1):
            probability = EXACT.nu(K, R, k, j)
            if probability:
                rows.append((mass * probability, (t - 1, K + k, R + j, B)))
    return tuple(rows)


class Profiler:
    def __init__(self) -> None:
        self.moments = MOMENT.SecondMoment()

    def U(self, x: tuple[int, int, int, int]) -> Fraction:
        s, K, R, B = x
        q = EXACT.q_split(s, B)
        return q * (1 - q) * Fraction(K, R + 1)

    def V(self, x: tuple[int, int, int, int]) -> Fraction:
        return self.moments.variance(*x)

    @functools.lru_cache(maxsize=None)
    def reset_depth(self, x: tuple[int, int, int, int]):
        profile = [EXACT.reset_budget(*x)]
        for weight, child in deep_children(x):
            child_profile = self.reset_depth(child)
            while len(profile) < len(child_profile) + 1:
                profile.append(Fraction(0))
            for depth, value in enumerate(child_profile, start=1):
                profile[depth] += weight * value
        return tuple(profile)

    @functools.lru_cache(maxsize=None)
    def defect_depth(self, kind: str, x: tuple[int, int, int, int]):
        budget = self.U if kind == "U" else self.V
        children = deep_children(x)
        local = budget(x) - EXACT.reset_budget(*x) - sum(
            (weight * budget(child) for weight, child in children),
            Fraction(),
        )
        profile = [local]
        for weight, child in children:
            child_profile = self.defect_depth(kind, child)
            while len(profile) < len(child_profile) + 1:
                profile.append(Fraction(0))
            for depth, value in enumerate(child_profile, start=1):
                profile[depth] += weight * value
        return tuple(profile)

    @functools.lru_cache(maxsize=None)
    def reset_terminal_rank(self, x: tuple[int, int, int, int]):
        answer = defaultdict(Fraction, dict(reset_by_rank(*x)))
        for weight, child in deep_children(x):
            for rank, value in self.reset_terminal_rank(child):
                answer[rank] += weight * value
        return tuple(sorted(answer.items()))


def profile(x: tuple[int, int, int, int]) -> dict[str, object]:
    profiler = Profiler()
    U = profiler.U(x)
    V = profiler.V(x)
    reset_depth = profiler.reset_depth(x)
    u_defect = profiler.defect_depth("U", x)
    v_defect = profiler.defect_depth("V", x)
    terminal = profiler.reset_terminal_rank(x)
    g = sum(reset_depth, Fraction())
    if sum(u_defect, Fraction()) != U - g:
        raise AssertionError("U telescoping failure")
    if sum(v_defect, Fraction()) != V - g:
        raise AssertionError("V telescoping failure")
    if sum((value for _, value in terminal), Fraction()) != g:
        raise AssertionError("terminal-rank grouping failure")

    def depth_rows(values: tuple[Fraction, ...]):
        cumulative = Fraction(0)
        rows = []
        for depth, value in enumerate(values):
            cumulative += value
            rows.append({
                "depth": depth,
                "contribution": record(value),
                "cumulative": record(cumulative),
            })
        tail = Fraction(0)
        for row, value in zip(reversed(rows), reversed(values)):
            tail += value
            row["reverse_tail"] = record(tail)
        return rows

    ascending = []
    cumulative = Fraction(0)
    for rank, value in terminal:
        cumulative += value
        ascending.append({
            "reset_target_rank": rank,
            "contribution": record(value),
            "cumulative_reset": record(cumulative),
            "V_minus_cumulative": record(V - cumulative),
            "U_minus_cumulative": record(U - cumulative),
        })
    descending = []
    cumulative = Fraction(0)
    for rank, value in reversed(terminal):
        cumulative += value
        descending.append({
            "reset_target_rank": rank,
            "contribution": record(value),
            "cumulative_reset": record(cumulative),
            "V_minus_cumulative": record(V - cumulative),
            "U_minus_cumulative": record(U - cumulative),
        })

    return {
        "context": list(x),
        "q": record(EXACT.q_split(x[0], x[3])),
        "U": record(U),
        "V": record(V),
        "g": record(g),
        "U_minus_g": record(U - g),
        "V_minus_g": record(V - g),
        "reset_by_depth": depth_rows(reset_depth),
        "U_defect_by_depth": depth_rows(u_defect),
        "V_defect_by_depth": depth_rows(v_defect),
        "reset_by_terminal_rank_ascending": ascending,
        "reset_by_terminal_rank_descending": descending,
        "memoized_mixed_moment_contexts": profiler.moments.calls,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s", type=int, required=True)
    parser.add_argument("--K", type=int, required=True)
    parser.add_argument("--R", type=int, required=True)
    parser.add_argument("--B", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    result = profile((args.s, args.K, args.R, args.B))
    payload = {
        "claim_tested": "exact whole-excursion slack telescoping by depth and reset rank",
        "arithmetic": "fractions.Fraction exact grouped recurrences",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "elapsed_seconds": time.time() - started,
        "result": result,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "elapsed_seconds": payload["elapsed_seconds"],
        "summary": {
            key: result[key]
            for key in ("context", "U_minus_g", "V_minus_g")
        },
    }, sort_keys=True))


if __name__ == "__main__":
    main()
