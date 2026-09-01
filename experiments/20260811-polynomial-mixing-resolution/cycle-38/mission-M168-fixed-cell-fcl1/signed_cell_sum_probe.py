#!/usr/bin/env python3
"""Narrow exact/float probe for the *signed* M161 fixed-cell phase sum.

This does not build a quotient matrix and does not scan other cells or
shells.  It collapses the lag/phase sum before the intermediate-state sum.
For q=s^{-1}h, every nonzero boundary edge (r,r+1) is an actual adjacent
edge of one cycle of q.  Consequently the sum over all ordered disjoint
pairs is determined by the generic-edge counts in the three residual
cycles.  The script checks this collapsed formula against frozen M161 data
at k=3,5,7 and optionally evaluates further odd k.

Convention: (pq)(x)=p(q(x)); factors multiply left-to-right.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
import time
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path


def mul(p, q):
    return tuple(p[q[x]] for x in range(len(p)))


def inv(p):
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def cyc(n, entries):
    out = list(range(n))
    for x, y in zip(entries, entries[1:] + entries[:1]):
        out[x] = y
    return tuple(out)


def tr(n, x, y):
    return cyc(n, (x, y))


def cycle_list(p):
    seen, ans = set(), []
    for a in range(len(p)):
        if a in seen:
            continue
        c, x = [], a
        while x not in seen:
            seen.add(x)
            c.append(x)
            x = p[x]
        ans.append(tuple(c))
    return ans


@lru_cache(maxsize=None)
def completion_sizes(sizes, length):
    if sum(sizes) - len(sizes) != length:
        return 0
    ans = math.factorial(length)
    for d in sizes:
        if d > 1:
            ans = ans * d ** (d - 2) // math.factorial(d - 1)
    return ans


def completion(p, length):
    return completion_sizes(tuple(sorted(map(len, cycle_list(p)))), length)


def supported(n):
    for a, b, c in combinations(range(n), 3):
        yield cyc(n, (a, b, c)), "T", 3
    for a, b, c, d in combinations(range(n), 4):
        yield mul(tr(n, a, b), tr(n, c, d)), "D", 2
        yield mul(tr(n, a, d), tr(n, b, c)), "D", 2


def collapsed_target_completion_sum(n, s, q):
    """Sum F_{n-5}(t q) over ordered disjoint boundary-edge pairs t."""
    cs = cycle_list(q)
    owner = {}
    for i, c in enumerate(cs):
        for x in c:
            owner[x] = i
    sizes = [len(c) for c in cs]

    # q(r)=r+1 precisely when s fixes r+1.  These and only these boundary
    # edges can occur in a nonzero fixed-cell target completion.
    generic = [s[(r + 1) % n] == (r + 1) % n for r in range(n)]
    counts = [0] * len(cs)
    adjacent = [0] * len(cs)
    for r in range(n):
        if generic[r]:
            counts[owner[r]] += 1
        if generic[r] and generic[(r + 1) % n]:
            i = owner[r]
            assert owner[(r + 1) % n] == i
            adjacent[i] += 1

    total = 0
    for i, d in enumerate(sizes):
        ordered_disjoint = counts[i] * (counts[i] - 1) - 2 * adjacent[i]
        if ordered_disjoint:
            after = sizes[:i] + [1, 1, d - 2] + sizes[i + 1 :]
            total += ordered_disjoint * completion_sizes(tuple(sorted(after)), n - 5)
    for i in range(len(sizes)):
        for j in range(i + 1, len(sizes)):
            ordered = 2 * counts[i] * counts[j]
            if ordered:
                after = [d for a, d in enumerate(sizes) if a not in (i, j)]
                after += [1, sizes[i] - 1, 1, sizes[j] - 1]
                total += ordered * completion_sizes(tuple(sorted(after)), n - 5)
    return total, tuple(sorted(counts)), tuple(sorted(adjacent))


def qstr(x):
    if isinstance(x, Fraction):
        return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
    return None


def analyze(k, exact):
    if k < 3 or k % 2 == 0:
        raise ValueError("k must be odd and at least three")
    started = time.monotonic()
    n = 3 * k
    h = cyc(n, tuple(range(n)))
    A = cyc(n, (0, k, 2 * k))
    B = mul(tr(n, 0, 1), tr(n, k, 2 * k))
    fA = completion(mul(inv(A), h), n - 3)
    fB = completion(mul(inv(B), h), n - 3)
    t0 = mul(tr(n, 0, 1), tr(n, 2, 3))
    fT = completion(mul(inv(t0), h), n - 3)

    zero = Fraction(0) if exact else 0.0
    source = {"A": zero, "B": zero}
    by_kind = {"T": zero, "D": zero}
    states = 0
    for s, kind, lift in supported(n):
        q = mul(inv(s), h)
        fs = completion(q, n - 3)
        target_sum, _, _ = collapsed_target_completion_sum(n, s, q)
        f5A = completion(mul(inv(mul(A, s)), h), n - 5)
        f5B = completion(mul(inv(mul(B, s)), h), n - 5)
        if exact:
            ca = Fraction(lift * f5A, fA * fs)
            cb = Fraction(lift * f5B, fB * fs)
        else:
            ca = lift * (f5A / fA) * (target_sum / fs)
            cb = lift * (f5B / fB) * (target_sum / fs)
            # target_sum/fs was already included; avoid multiplying twice.
            source["A"] += ca
            source["B"] += cb
            by_kind[kind] += cb - ca
            states += 1
            continue
        source["A"] += ca * target_sum
        source["B"] += cb * target_sum
        by_kind[kind] += (cb - ca) * target_sum
        states += 1

    norm = Fraction(n ** (n - 2), n * fT) if exact else n ** (n - 2) / (n * fT)
    signed_sum = norm * (source["B"] - source["A"])
    pi_y = Fraction(2 * n * fT, n ** (n - 2)) if exact else 2 * n * fT / n ** (n - 2)
    # Each physical boundary-double orbit occurs twice in the colored y list.
    event_delta = pi_y * signed_sum / 2
    return {
        "k": k,
        "n": n,
        "exact": exact,
        "states": states,
        "signed_sum_exact": qstr(signed_sum),
        "signed_sum_float": float(signed_sum),
        "k_times_signed_sum": float(k * signed_sum),
        "event_delta_exact": qstr(event_delta),
        "event_delta_float": float(event_delta),
        "n_squared_event_delta": float(n * n * event_delta),
        "by_intermediate_kind_signed_sum": {
            kind: float(norm * value) for kind, value in by_kind.items()
        },
        "runtime_seconds": time.monotonic() - started,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, nargs="+", required=True)
    ap.add_argument("--exact-through", type=int, default=7)
    ap.add_argument("--frozen-m161", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    rows = [analyze(k, k <= args.exact_through) for k in args.k]
    frozen_checks = []
    if args.frozen_m161:
        frozen = json.loads(args.frozen_m161.read_text())
        by_k = {r["k"]: r for r in frozen["results"]}
        for row in rows:
            if row["k"] in by_k and row["signed_sum_exact"] is not None:
                expected = sum(
                    (Fraction(x["score_exact"]) for x in by_k[row["k"]]["rows"]),
                    Fraction(0),
                )
                assert Fraction(row["signed_sum_exact"]) == expected
                frozen_checks.append({"k": row["k"], "exact_match": True})
    payload = {
        "status": "narrow signed fixed-cell phase-sum probe; no sign or asymptotic inference",
        "target": "M161 FCL1 cell (a,b)=(1,1) only",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "frozen_m161_checks": frozen_checks,
        "results": rows,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(rows, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

