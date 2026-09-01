#!/usr/bin/env python3
"""Exact class recurrence for a named buffer-count hypothesis.

For each N, W_k(lambda) is the number of length-k transposition words ending
at one fixed permutation of cycle type lambda.  At the minimum number
2*r_N of micro-transpositions needed to represent every even permutation,
we compute the largest ratio W_k(mu)/W_k(lambda) over feasible even types
whose representatives can differ by four right transpositions.  This is the
class-level necessary count-ratio test for a buffer shift
d -> p(Y)^(-1)d p(X).

Finite output can refute a proposed numerical bound; it cannot prove a
uniform polynomial bound.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
from collections import defaultdict
from pathlib import Path


def partitions(n: int, cap: int | None = None):
    if n == 0:
        yield ()
        return
    if cap is None or cap > n:
        cap = n
    for first in range(cap, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def representative(part: tuple[int, ...]) -> tuple[int, ...]:
    n = sum(part)
    p = list(range(n))
    start = 0
    for size in part:
        cyc = list(range(start, start + size))
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            p[a] = b
        start += size
    return tuple(p)


def right_transpose(p: tuple[int, ...], a: int, b: int) -> tuple[int, ...]:
    # p*t means apply t first, then p.
    out = list(p)
    out[a], out[b] = p[b], p[a]
    return tuple(out)


def cycle_type(p: tuple[int, ...]) -> tuple[int, ...]:
    seen = [False] * len(p)
    sizes = []
    for i in range(len(p)):
        if not seen[i]:
            j = i
            size = 0
            while not seen[j]:
                seen[j] = True
                size += 1
                j = p[j]
            sizes.append(size)
    return tuple(sorted(sizes, reverse=True))


def transposition_class_graph(n: int):
    parts = list(partitions(n))
    index = {part: i for i, part in enumerate(parts)}
    counts: list[dict[int, int]] = []
    neighbors: list[set[int]] = []
    for part in parts:
        p = representative(part)
        row: dict[int, int] = defaultdict(int)
        for a in range(n):
            for b in range(a + 1, n):
                row[index[cycle_type(right_transpose(p, a, b))]] += 1
        counts.append(dict(row))
        neighbors.append(set(row))
    return parts, index, counts, neighbors


def four_hop(neighbors: list[set[int]], start: int) -> set[int]:
    cur = {start}
    for _ in range(4):
        cur = {v for u in cur for v in neighbors[u]}
    return cur


def run_one(n: int):
    parts, index, counts, neighbors = transposition_class_graph(n)
    identity = (1,) * n
    r = (n - 1) // 2
    k = 2 * r
    w = [0] * len(parts)
    w[index[identity]] = 1
    for _ in range(k):
        w = [sum(mult * w[j] for j, mult in row.items()) for row in counts]

    feasible = [i for i, val in enumerate(w) if val]
    global_min_i = min(feasible, key=lambda i: w[i])
    global_max_i = max(feasible, key=lambda i: w[i])
    global_ratio = w[global_max_i] / w[global_min_i]
    max_num = 1
    max_den = 1
    arg = None
    for i in feasible:
        for j in four_hop(neighbors, i):
            if w[j] and w[j] * max_den > max_num * w[i]:
                max_num, max_den = w[j], w[i]
                arg = (parts[i], parts[j])
    ratio_float = max_num / max_den
    exponent = math.log(ratio_float) / math.log(n) if ratio_float > 1 else 0.0
    return {
        "N": n,
        "r": r,
        "micro_length": k,
        "partition_count": len(parts),
        "feasible_type_count": len(feasible),
        "global_max_min_ratio_float": global_ratio,
        "global_effective_N_exponent": (
            math.log(global_ratio) / math.log(n) if global_ratio > 1 else 0.0
        ),
        "global_min_type": list(parts[global_min_i]),
        "global_max_type": list(parts[global_max_i]),
        "global_min_count": str(w[global_min_i]),
        "global_max_count": str(w[global_max_i]),
        "max_ratio_numerator": str(max_num),
        "max_ratio_denominator": str(max_den),
        "max_ratio_float": ratio_float,
        "effective_N_exponent": exponent,
        "source_type": list(arg[0]) if arg else None,
        "target_type": list(arg[1]) if arg else None,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-min", type=int, default=3)
    ap.add_argument("--n-max", type=int, default=18)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    rows = [run_one(n) for n in range(args.n_min, args.n_max + 1)]
    payload = {
        "claim_tested": (
            "At r=floor((N-1)/2), (a) neighboring feasible buffer-fiber "
            "counts F_r(d')/F_r(d), for d'=p(Y)^(-1)d p(X), and (b) the "
            "global max/min feasible endpoint count ratio are bounded by "
            "N^C for a universal C. Four-transposition class adjacency is "
            "the class-level test for (a); complementary-buffer switching "
            "can require the arbitrary endpoint ratio (b)."
        ),
        "logical_scope": "Finite exact falsification only; no asymptotic proof.",
        "python": platform.python_version(),
        "command": (
            "python3 bridge_count_ratio.py --n-min "
            f"{args.n_min} --n-max {args.n_max} --output {args.output.name}"
        ),
        "rows": rows,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
