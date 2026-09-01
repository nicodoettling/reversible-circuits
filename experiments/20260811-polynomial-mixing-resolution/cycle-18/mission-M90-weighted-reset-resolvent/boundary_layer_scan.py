#!/usr/bin/env python3
"""Exact audit of a two-step boundary-layer reduction for weighted slack.

Let ``Q(x,y)=rho_s(k,t)nu(j)``, ``g=(I-Q)^(-1)A``, and
``U=q(1-q)K/(R+1)``.  With ``r=U-A-QU``, nilpotence gives

    U-g = sum_(d>=0) Q^d r.

Every deep child of a fresh seed ``(s,1,0,B)`` is nonfresh.  Therefore the
two pointwise conditions

    r(z)>=0 on every reachable nonfresh z,
    r(x)+(Qr)(x)>=0 on every fresh x

would prove ``U>=g``: depths at least two are positive sums of nonfresh
defects.  This script audits those signs exactly on the full pure-deep
closure of the named fresh seeds.  It retains every attachment rank
``j>=1``.  Finite survival proves no universal condition.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import platform
import time
from fractions import Fraction
from pathlib import Path

import exact_weighted_resolvent as EXACT


def record(value: Fraction) -> dict[str, object]:
    return {
        "decimal": float(value),
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


@functools.lru_cache(maxsize=None)
def children(x: tuple[int, int, int, int]):
    s, K, R, B = x
    parent_phase = s + K - R
    rows = []
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


def U(x: tuple[int, int, int, int]) -> Fraction:
    s, K, R, B = x
    q = EXACT.q_split(s, B)
    return q * (1 - q) * Fraction(K, R + 1)


@functools.lru_cache(maxsize=None)
def defect(x: tuple[int, int, int, int]) -> Fraction:
    return U(x) - EXACT.reset_budget(*x) - sum(
        (weight * U(child) for weight, child in children(x)),
        Fraction(),
    )


@functools.lru_cache(maxsize=None)
def profile(x: tuple[int, int, int, int]):
    values = [defect(x)]
    for weight, child in children(x):
        child_values = profile(child)
        while len(values) < len(child_values) + 1:
            values.append(Fraction(0))
        for depth, value in enumerate(child_values, start=1):
            values[depth] += weight * value
    return tuple(values)


def scan(s_values: list[int]) -> dict[str, object]:
    solver = EXACT.ExactResolvent()
    visited: set[tuple[int, int, int, int]] = set()

    def visit(x: tuple[int, int, int, int]) -> None:
        if x in visited:
            return
        visited.add(x)
        for _, child in children(x):
            visit(child)

    seed_rows = []
    negative_two_step = []
    negative_positive_depth = []
    minimum_two_step = None
    minimum_main = None
    for s in s_values:
        rank_worst = None
        for B in range(1, s + 1):
            x = (s, 1, 0, B)
            visit(x)
            values = profile(x)
            g = solver.g(*x)
            if sum(values, Fraction()) != U(x) - g:
                raise AssertionError(("telescoping", x))
            q_r = values[1] if len(values) > 1 else Fraction(0)
            two_step = values[0] + q_r
            row = {
                "context": list(x),
                "U": record(U(x)),
                "g": record(g),
                "main_margin": record(U(x) - g),
                "main_ratio": record(g / U(x)),
                "r": record(values[0]),
                "Qr": record(q_r),
                "r_plus_Qr": record(two_step),
            }
            if rank_worst is None or g / U(x) > rank_worst[0]:
                rank_worst = (g / U(x), row)
            if minimum_main is None or (U(x) - g) / U(x) < minimum_main[0]:
                minimum_main = ((U(x) - g) / U(x), row)
            if minimum_two_step is None or two_step / U(x) < minimum_two_step[0]:
                minimum_two_step = (two_step / U(x), row)
            if two_step < 0:
                negative_two_step.append(row)
            for depth, value in enumerate(values[1:], start=1):
                if value < 0:
                    bad = dict(row)
                    bad.update({"depth": depth, "contribution": record(value)})
                    negative_positive_depth.append(bad)
        seed_rows.append({"s": s, "worst": rank_worst[1]})
        print(json.dumps(seed_rows[-1], sort_keys=True), flush=True)

    nonfresh = [x for x in visited if (x[1], x[2]) != (1, 0)]
    negative_nonfresh = []
    minimum_nonfresh = None
    for x in nonfresh:
        value = defect(x)
        normalized = value / U(x)
        row = {
            "context": list(x),
            "U": record(U(x)),
            "defect": record(value),
            "normalized_defect": record(normalized),
        }
        if minimum_nonfresh is None or normalized < minimum_nonfresh[0]:
            minimum_nonfresh = (normalized, row)
        if value < 0:
            negative_nonfresh.append(row)

    return {
        "fresh_seed_rows": seed_rows,
        "fresh_seed_count": sum(s_values),
        "reachable_context_count": len(visited),
        "reachable_nonfresh_context_count": len(nonfresh),
        "negative_nonfresh_defect_count": len(negative_nonfresh),
        "first_negative_nonfresh_defects": negative_nonfresh[:3],
        "negative_fresh_two_step_count": len(negative_two_step),
        "first_negative_fresh_two_steps": negative_two_step[:3],
        "negative_positive_depth_contribution_count": len(negative_positive_depth),
        "first_negative_positive_depth_contributions": negative_positive_depth[:3],
        "minimum_normalized_nonfresh_defect": {
            "value": record(minimum_nonfresh[0]),
            "row": minimum_nonfresh[1],
        },
        "minimum_normalized_fresh_two_step": {
            "value": record(minimum_two_step[0]),
            "row": minimum_two_step[1],
        },
        "minimum_normalized_main_margin": {
            "value": record(minimum_main[0]),
            "row": minimum_main[1],
        },
        "memoized_resolvent_contexts": solver.contexts,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-values", type=int, nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    result = scan(args.s_values)
    payload = {
        "claim_tested": (
            "weighted fresh-boundary two-step sufficient conditions on the "
            "full pure-deep closure"
        ),
        "finite_scope_warning": "Exact bounded survival proves no universal inequality.",
        "arithmetic": "fractions.Fraction exact grouped recurrences",
        "normalization": "Q=rho*nu for every j>=1; U=q(1-q)K/(R+1)",
        "strict_phase": "P=s+K-R decreases on every retained deep child",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "parameters": {"s_values": args.s_values},
        "elapsed_seconds": time.time() - started,
        "result": result,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "elapsed_seconds": payload["elapsed_seconds"],
        "negative_nonfresh_defect_count": result["negative_nonfresh_defect_count"],
        "negative_fresh_two_step_count": result["negative_fresh_two_step_count"],
        "negative_positive_depth_contribution_count": (
            result["negative_positive_depth_contribution_count"]
        ),
        "minimum_normalized_nonfresh_defect": (
            result["minimum_normalized_nonfresh_defect"]
        ),
        "minimum_normalized_fresh_two_step": (
            result["minimum_normalized_fresh_two_step"]
        ),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
