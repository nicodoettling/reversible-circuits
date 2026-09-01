#!/usr/bin/env python3
"""Exact bounded falsifier for the proposed valley-to-peak upper diamond.

Universal claim tested: if x --a--> xa --b--> xab is a rank valley in the
all-transposition Cayley graph of S_N and rank(x)<N-1, then the same two-step
product ab has a factorization cd whose intermediate xc has rank(x)+1.
Finite success is not a proof; one counterexample refutes the claim.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import subprocess
from collections import Counter
from pathlib import Path


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """p after q: (pq)(x)=p(q(x))."""
    return tuple(p[q[i]] for i in range(len(p)))


def transposition(n: int, i: int, j: int) -> tuple[int, ...]:
    p = list(range(n))
    p[i], p[j] = p[j], p[i]
    return tuple(p)


def rank(p: tuple[int, ...]) -> int:
    n = len(p)
    seen = [False] * n
    cycles = 0
    for i in range(n):
        if not seen[i]:
            cycles += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j]
    return n - cycles


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-N", type=int, default=6)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    totals = Counter()
    no_lift = Counter()
    nonmax_totals = Counter()
    nonmax_no_lift = Counter()
    min_lifts: dict[str, int] = {}
    nonmax_min_lifts: dict[str, int] = {}
    witnesses: list[dict[str, object]] = []
    nonmax_witnesses: list[dict[str, object]] = []

    for n in range(2, args.max_N + 1):
        ts = [transposition(n, i, j) for i in range(n) for j in range(i + 1, n)]
        prod_factors: dict[tuple[int, ...], list[tuple[tuple[int, ...], tuple[int, ...]]]] = {}
        for c in ts:
            for d in ts:
                prod_factors.setdefault(compose(c, d), []).append((c, d))

        local_min = 10**9
        nonmax_local_min = 10**9
        for x in itertools.permutations(range(n)):
            hx = rank(x)
            for a in ts:
                xa = compose(x, a)
                if rank(xa) != hx - 1:
                    continue
                for b in ts:
                    xab = compose(xa, b)
                    if rank(xab) != hx:
                        continue
                    totals[str(n)] += 1
                    if hx < n - 1:
                        nonmax_totals[str(n)] += 1
                    p = compose(a, b)
                    lifts = [
                        (c, d)
                        for c, d in prod_factors[p]
                        if rank(compose(x, c)) == hx + 1
                    ]
                    local_min = min(local_min, len(lifts))
                    if hx < n - 1:
                        nonmax_local_min = min(nonmax_local_min, len(lifts))
                    if not lifts:
                        no_lift[str(n)] += 1
                        if hx < n - 1:
                            nonmax_no_lift[str(n)] += 1
                        witness = {
                            "N": n,
                            "x": x,
                            "rank_x": hx,
                            "a": a,
                            "b": b,
                            "endpoint": xab,
                            "rank_x_is_maximum": hx == n - 1,
                        }
                        if len(witnesses) < 25:
                            witnesses.append(witness)
                        if hx < n - 1 and len(nonmax_witnesses) < 25:
                            nonmax_witnesses.append(witness)
        min_lifts[str(n)] = 0 if local_min == 10**9 else local_min
        nonmax_min_lifts[str(n)] = (
            0 if nonmax_local_min == 10**9 else nonmax_local_min
        )

    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception:
        commit = "unavailable"
    result = {
        "claim_tested": (
            "Every transposition-Cayley rank valley based below maximum rank "
            "has a same-product two-factor upper diamond."
        ),
        "finite_scope": {"N_min": 2, "N_max": args.max_N},
        "composition": "(pq)(x)=p(q(x)); word products left-to-right",
        "deterministic_seed": None,
        "python": platform.python_version(),
        "repository_commit": commit,
        "valleys": dict(totals),
        "valleys_without_upper_lift": dict(no_lift),
        "nonmaximum_valleys": dict(nonmax_totals),
        "nonmaximum_valleys_without_upper_lift": dict(nonmax_no_lift),
        "minimum_number_of_upper_factorizations": min_lifts,
        "minimum_number_for_nonmaximum_valleys": nonmax_min_lifts,
        "first_witnesses": witnesses,
        "first_nonmaximum_witnesses": nonmax_witnesses,
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
