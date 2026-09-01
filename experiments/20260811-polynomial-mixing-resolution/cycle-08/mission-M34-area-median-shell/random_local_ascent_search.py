#!/usr/bin/env python3
"""Fixed-seed search for a nonmaximum r<=5 area local maximum.

Every state is reached by exact Hurwitz bijections from a paired spanning-tree
word, hence is rigorously in F_N.  Any emitted zero-gain state is checked by
exact dynamic programming over every same-product r=3,4,5 fiber.  Nonfinding
is empirical and is not evidence for the universal ascent lemma.
"""

from __future__ import annotations

import argparse
import json
import platform
import random
import subprocess
from pathlib import Path

from exact_local_area_ascent import (
    compose,
    conjugate,
    optimum_internal_sums,
    rank,
    transposition,
)


def analyze(word, ts, optimal, n):
    m = len(word)
    identity = tuple(range(n))
    prefixes = [identity]
    heights = [0]
    for idx in word:
        prefixes.append(compose(prefixes[-1], ts[idx]))
        heights.append(rank(prefixes[-1]))
    if prefixes[-1] != identity:
        raise AssertionError("Hurwitz state lost identity product")
    area = sum(heights)
    max_gain = 0
    best = None
    for r in (3, 4, 5):
        for i in range(m - r + 1):
            product = identity
            for j in range(i, i + r):
                product = compose(product, ts[word[j]])
            old_internal = sum(heights[i + 1 : i + r])
            gain = optimal[(prefixes[i], r, product)] - old_internal
            if gain > max_gain:
                max_gain = gain
                best = {"r": r, "window_start_zero_based": i, "gain": gain}
    return area, heights, max_gain, best


def search(n, steps, stride, seed):
    es = [(i, j) for i in range(n) for j in range(i + 1, n)]
    index = {e: i for i, e in enumerate(es)}
    ts = [transposition(n, *e) for e in es]
    conjugates = [[index[conjugate(a, b)] for b in es] for a in es]
    optimal = optimum_internal_sums(n, ts)
    word = []
    for v in range(1, n):
        e = index[(0, v)]
        word.extend((e, e))
    rng = random.Random(seed)
    checked = 0
    minimum_positive_gain = None
    first_by_gain = {}
    maximum_area = (n - 1) ** 2
    for step in range(steps + 1):
        if step % stride == 0:
            checked += 1
            area, heights, gain, best = analyze(word, ts, optimal, n)
            first_by_gain.setdefault(
                str(gain),
                {"step": step, "area": area, "heights": heights, "best": best},
            )
            if gain > 0 and (minimum_positive_gain is None or gain < minimum_positive_gain):
                minimum_positive_gain = gain
            if gain == 0 and area < maximum_area:
                return {
                    "found": True,
                    "step": step,
                    "checked_states": checked,
                    "word_edge_indices": word,
                    "word_edges": [list(es[i]) for i in word],
                    "area": area,
                    "heights": heights,
                    "maximum_possible_area": maximum_area,
                    "exact_maximum_one_window_gain": gain,
                    "identity_product_verified": True,
                    "full_support_verified": True,
                    "first_by_gain": first_by_gain,
                }
        i = rng.randrange(len(word) - 1)
        a, b = word[i], word[i + 1]
        if rng.randrange(2) == 0:
            word[i], word[i + 1] = b, conjugates[a][b]
        else:
            word[i], word[i + 1] = conjugates[b][a], a
    return {
        "found": False,
        "steps": steps,
        "stride": stride,
        "checked_states": checked,
        "minimum_positive_gain_seen": minimum_positive_gain,
        "first_by_gain": first_by_gain,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, required=True)
    ap.add_argument("--steps", type=int, default=200000)
    ap.add_argument("--stride", type=int, default=10)
    ap.add_argument("--seed", type=int, default=340031)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        commit = "unavailable"
    out = {
        "purpose": "Exact witness search; nonfinding is empirical only.",
        "claim_tested": (
            "Every nonmaximum-area state in F_N has a positive one-step "
            "same-product r<=5 area gain."
        ),
        "convention": "(pq)(x)=p(q(x)); R(a,b)=(b,bab)",
        "python": platform.python_version(),
        "repository_commit": commit,
        "N": args.N,
        "m": 2 * args.N - 2,
        "steps": args.steps,
        "stride": args.stride,
        "seed": args.seed,
        "result": search(args.N, args.steps, args.stride, args.seed),
    }
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
