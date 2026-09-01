#!/usr/bin/env python3
"""Complete finite falsifier for local area-ascent claims on F_N.

For each state in the (known single) minimal connected Hurwitz orbit F_N, the
script computes the maximum Dyck-area gain obtainable by one exact
same-product window replacement of length 3, 4, or 5.  Dynamic programming on
the all-transposition Cayley graph computes the optimum without enumerating a
conditional fiber per state.

Universal claim tested: every non-maximum-area word in F_N has a legal
r<=5 heat-bath outcome of strictly larger prefix-cycle area.  Finite success
cannot prove this claim; a zero-gain nonmaximum word refutes it.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import subprocess
import sys
import time
from collections import Counter, deque
from pathlib import Path


Perm = tuple[int, ...]
Edge = tuple[int, int]


def compose(p: Perm, q: Perm) -> Perm:
    """p after q: (pq)(x)=p(q(x))."""
    return tuple(p[q[i]] for i in range(len(p)))


def transposition(n: int, i: int, j: int) -> Perm:
    p = list(range(n))
    p[i], p[j] = p[j], p[i]
    return tuple(p)


def rank(p: Perm) -> int:
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


def apply_edge(e: Edge, x: int) -> int:
    a, b = e
    return b if x == a else a if x == b else x


def conjugate(a: Edge, by: Edge) -> Edge:
    x, y = apply_edge(by, a[0]), apply_edge(by, a[1])
    return (x, y) if x < y else (y, x)


def optimum_internal_sums(n: int, ts: list[Perm]) -> dict[tuple[Perm, int, Perm], int]:
    """max sum of ranks at r-1 internal times, keyed by (start,r,product)."""
    identity = tuple(range(n))
    out: dict[tuple[Perm, int, Perm], int] = {}
    for x in itertools.permutations(range(n)):
        # full[s][p] maximizes sum of ranks after each of s factors.
        full: dict[Perm, int] = {identity: 0}
        for s in range(1, 6):
            nxt: dict[Perm, int] = {}
            for p, value in full.items():
                for t in ts:
                    q = compose(p, t)
                    candidate = value + rank(compose(x, q))
                    if candidate > nxt.get(q, -1):
                        nxt[q] = candidate
            full = nxt
            if s >= 2:
                for p, value in full.items():
                    out[(x, s, p)] = value - rank(compose(x, p))
    return out


def enumerate_orbit(n: int) -> dict[str, object]:
    es = [(i, j) for i in range(n) for j in range(i + 1, n)]
    ts = [transposition(n, *e) for e in es]
    m = 2 * n - 2
    base = len(es)
    powers = [base**i for i in range(m)]
    edge_to_i = {e: i for i, e in enumerate(es)}
    conj = [[edge_to_i[conjugate(es[a], es[b])] for b in range(base)] for a in range(base)]
    optimal = optimum_internal_sums(n, ts)

    start_word: list[int] = []
    for v in range(1, n):
        e = edge_to_i[(0, v)]
        start_word.extend((e, e))
    start = sum(d * powers[i] for i, d in enumerate(start_word))

    seen = {start}
    queue = deque([start])
    area_counts: Counter[int] = Counter()
    dyck_path_counts: Counter[str] = Counter()
    zero_gain_by_area: Counter[int] = Counter()
    gain_counts: Counter[int] = Counter()
    pair_gain_counts: Counter[int] = Counter()
    pair_zero_gain_by_area: Counter[int] = Counter()
    first_nonmaximum_zero_gain: dict[str, object] | None = None
    first_zero_gain: dict[str, object] | None = None
    first_nonmaximum_pair_zero_gain: dict[str, object] | None = None
    maximum_possible_area = (n - 1) ** 2
    identity = tuple(range(n))
    t0 = time.time()

    while queue:
        code = queue.popleft()
        tmp = code
        word = [0] * m
        for i in range(m):
            word[i], tmp = tmp % base, tmp // base

        prefixes = [identity]
        heights = [0]
        for idx in word:
            prefixes.append(compose(prefixes[-1], ts[idx]))
            heights.append(rank(prefixes[-1]))
        if prefixes[-1] != identity:
            raise AssertionError("orbit word does not evaluate to identity")
        area = sum(heights)
        area_counts[area] += 1
        dyck_path = "".join(
            "U" if heights[j + 1] == heights[j] + 1 else "D"
            for j in range(m)
        )
        dyck_path_counts[dyck_path] += 1

        pair_max_gain = 0
        for i in range(m - 1):
            product = compose(ts[word[i]], ts[word[i + 1]])
            old_internal = heights[i + 1]
            gain = optimal[(prefixes[i], 2, product)] - old_internal
            pair_max_gain = max(pair_max_gain, gain)
        pair_gain_counts[pair_max_gain] += 1
        if pair_max_gain == 0:
            pair_zero_gain_by_area[area] += 1
            if area < maximum_possible_area and first_nonmaximum_pair_zero_gain is None:
                first_nonmaximum_pair_zero_gain = {
                    "edges": [list(es[idx]) for idx in word],
                    "area": area,
                    "heights": heights,
                    "maximum_possible_area": maximum_possible_area,
                }

        max_gain = 0
        best: dict[str, object] | None = None
        for r in (3, 4, 5):
            for i in range(m - r + 1):
                product = identity
                for j in range(i, i + r):
                    product = compose(product, ts[word[j]])
                old_internal = sum(heights[i + 1 : i + r])
                new_internal = optimal[(prefixes[i], r, product)]
                gain = new_internal - old_internal
                if gain > max_gain:
                    max_gain = gain
                    best = {"r": r, "window_start_zero_based": i, "gain": gain}
        gain_counts[max_gain] += 1
        if max_gain == 0:
            zero_gain_by_area[area] += 1
            witness = {
                "edges": [list(es[idx]) for idx in word],
                "area": area,
                "heights": heights,
                "maximum_possible_area": maximum_possible_area,
            }
            if first_zero_gain is None:
                first_zero_gain = witness
            if area < maximum_possible_area and first_nonmaximum_zero_gain is None:
                first_nonmaximum_zero_gain = witness

        for i in range(m - 1):
            a, b = word[i], word[i + 1]
            u, v = b, conj[a][b]
            nxt = code + (u - a) * powers[i] + (v - b) * powers[i + 1]
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
            u, v = conj[b][a], a
            nxt = code + (u - a) * powers[i] + (v - b) * powers[i + 1]
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)

    expected = math.factorial(m) * n ** (n - 3)
    if len(seen) != expected:
        raise AssertionError(f"orbit size {len(seen)} != exact {expected}")

    support = sorted(area_counts)
    cdf = 0
    admissible_quantiles = []
    for area in support:
        cdf += area_counts[area]
        if expected / 4 <= cdf <= expected / 2:
            admissible_quantiles.append(
                {"q": area, "lower_tail_count": cdf, "conditional_mass": [cdf, expected]}
            )

    return {
        "N": n,
        "m": m,
        "orbit_size": len(seen),
        "expected_orbit_size": expected,
        "maximum_possible_area": maximum_possible_area,
        "area_counts": dict(sorted(area_counts.items())),
        "dyck_path_counts": dict(sorted(dyck_path_counts.items())),
        "admissible_quarter_to_half_quantiles": admissible_quantiles,
        "maximum_one_window_gain_counts": dict(sorted(gain_counts.items())),
        "zero_gain_counts_by_area": dict(sorted(zero_gain_by_area.items())),
        "maximum_adjacent_pair_gain_counts": dict(sorted(pair_gain_counts.items())),
        "adjacent_pair_zero_gain_counts_by_area": dict(sorted(pair_zero_gain_by_area.items())),
        "first_zero_gain_witness": first_zero_gain,
        "first_nonmaximum_zero_gain_witness": first_nonmaximum_zero_gain,
        "first_nonmaximum_adjacent_pair_zero_gain_witness": first_nonmaximum_pair_zero_gain,
        "elapsed_seconds": time.time() - t0,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=5)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        commit = "unavailable"
    result = {
        "purpose": "Complete finite falsifier only; no finite-to-universal inference.",
        "claim_tested": (
            "Every nonmaximum-area state of F_N has a strictly area-increasing "
            "same-product heat-bath outcome in some r=3,4,5 window."
        ),
        "composition": "(pq)(x)=p(q(x)); word products left-to-right",
        "seed": None,
        "python": platform.python_version(),
        "repository_commit": commit,
        "argv": sys.argv,
        "result": enumerate_orbit(args.N),
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
