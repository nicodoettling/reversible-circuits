#!/usr/bin/env python3
"""Exact finite audit for the leaf-count threshold theorem.

For r balls in n=r+1 boxes, the number of allocations with exactly ell
empty boxes is (n)_(n-ell) S(r,n-ell).  The script checks every threshold
whose two stationary sides have mass at least 1/4.  It tests the exact
deterministic/M35 lower bound

    P(L=ell) * 2(r+1-2ell) / [3r(r-1)]

against 1/[60(r+1)(r-1)].  This bounded calculation is used only for
2 <= r <= 127; the report proves r >= 128 analytically.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import factorial
from pathlib import Path


def stirling_row(r: int) -> list[int]:
    row = [1]
    for a in range(1, r + 1):
        nxt = [0] * (a + 1)
        for k in range(1, a + 1):
            nxt[k] = (row[k - 1] if k - 1 < len(row) else 0) + (
                k * row[k] if k < len(row) else 0
            )
        row = nxt
    return row


def falling(n: int, k: int) -> int:
    return factorial(n) // factorial(n - k)


def audit(r_min: int, r_max: int) -> dict:
    checked = 0
    worst: tuple[Fraction, int, int, int, int] | None = None
    rows = []
    for r in range(r_min, r_max + 1):
        n = r + 1
        s = stirling_row(r)
        den = n**r
        counts = {
            n - k: falling(n, k) * s[k]
            for k in range(1, r + 1)
        }
        assert sum(counts.values()) == den
        cumulative = 0
        balanced = []
        for ell in sorted(counts):
            cumulative += counts[ell]
            tail = den - cumulative
            if 4 * cumulative >= den and 4 * tail >= den:
                checked += 1
                unary_lower = r + 1 - 2 * ell
                assert unary_lower > 0
                flow_lower = Fraction(counts[ell], den) * Fraction(
                    2 * unary_lower, 3 * r * (r - 1)
                )
                target = Fraction(1, 60 * (r + 1) * (r - 1))
                assert flow_lower >= target
                scaled = flow_lower * (r + 1) * (r - 1)
                if worst is None or scaled < worst[0]:
                    worst = (scaled, r, ell, counts[ell], den)
                balanced.append(
                    {
                        "ell": ell,
                        "level_numerator": counts[ell],
                        "unary_lower": unary_lower,
                    }
                )
        rows.append({"r": r, "balanced_thresholds": balanced})
    assert worst is not None
    return {
        "claim_tested": (
            "For every 2<=r<=127 and every ell with both leaf-count "
            "threshold sides at least 1/4, the proved level-flow lower "
            "bound is at least 1/[60(r+1)(r-1)]."
        ),
        "exact_arithmetic": True,
        "r_min": r_min,
        "r_max": r_max,
        "thresholds_checked": checked,
        "minimum_scaled_flow": {
            "numerator": worst[0].numerator,
            "denominator": worst[0].denominator,
            "r": worst[1],
            "ell": worst[2],
            "level_numerator": worst[3],
            "occupancy_denominator": worst[4],
        },
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-min", type=int, default=2)
    parser.add_argument("--r-max", type=int, default=127)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = audit(args.r_min, args.r_max)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result["minimum_scaled_flow"], sort_keys=True))


if __name__ == "__main__":
    main()
