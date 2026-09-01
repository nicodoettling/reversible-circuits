#!/usr/bin/env python3
"""Complete finite falsifier for a reverse adjacent-Hurwitz action lemma.

Claim tested: every nonminimum-area word in F_N has an adjacent right or left
Hurwitz move that lowers prefix-rank area by two.  Such moves preserve the
generated subgroup, hence stay in F_N.  One finite witness refutes the
universal claim; finite success would not prove it.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import platform
import subprocess
import sys
import time
from collections import Counter, deque
from pathlib import Path


HERE = Path(__file__).resolve().parent
BASE_SCRIPT = HERE.parent / "mission-M34-area-median-shell" / "exact_local_area_ascent.py"
SPEC = importlib.util.spec_from_file_location("m34_exact", BASE_SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot import {BASE_SCRIPT}")
M34 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M34)


def enumerate_orbit(n: int) -> dict[str, object]:
    es = [(i, j) for i in range(n) for j in range(i + 1, n)]
    ts = [M34.transposition(n, *e) for e in es]
    m = 2 * n - 2
    base = len(es)
    powers = [base**i for i in range(m)]
    edge_to_i = {e: i for i, e in enumerate(es)}
    conj = [[edge_to_i[M34.conjugate(es[a], es[b])] for b in range(base)] for a in range(base)]

    start_word: list[int] = []
    for v in range(1, n):
        e = edge_to_i[(0, v)]
        start_word.extend((e, e))
    start = sum(d * powers[i] for i, d in enumerate(start_word))

    identity = tuple(range(n))
    seen = {start}
    queue = deque([start])
    area_counts: Counter[int] = Counter()
    no_decrease_counts: Counter[int] = Counter()
    best_decrease_counts: Counter[int] = Counter()
    first_nonminimum_no_decrease = None
    minimum_area = n - 1
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
            prefixes.append(M34.compose(prefixes[-1], ts[idx]))
            heights.append(M34.rank(prefixes[-1]))
        if prefixes[-1] != identity:
            raise AssertionError("nonbridge in Hurwitz orbit")
        area = sum(heights)
        area_counts[area] += 1

        best_decrease = 0
        for i in range(m - 1):
            a, b = word[i], word[i + 1]
            # Right Hurwitz: (a,b)->(b,bab).  Only the intermediate
            # prefix changes, so the area difference is exact.
            right_first = b
            right_height = M34.rank(M34.compose(prefixes[i], ts[right_first]))
            best_decrease = max(best_decrease, heights[i + 1] - right_height)

            # Inverse/left Hurwitz: (a,b)->(aba,a).
            left_first = conj[b][a]
            left_height = M34.rank(M34.compose(prefixes[i], ts[left_first]))
            best_decrease = max(best_decrease, heights[i + 1] - left_height)

            # Generate both orbit neighbors while this pair is in hand.
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

        best_decrease_counts[best_decrease] += 1
        if best_decrease == 0:
            no_decrease_counts[area] += 1
            if area > minimum_area and first_nonminimum_no_decrease is None:
                first_nonminimum_no_decrease = {
                    "edges": [list(es[idx]) for idx in word],
                    "area": area,
                    "heights": heights,
                    "minimum_area": minimum_area,
                }

    expected = math.factorial(m) * n ** (n - 3)
    if len(seen) != expected:
        raise AssertionError((len(seen), expected))
    return {
        "N": n,
        "m": m,
        "orbit_size": len(seen),
        "expected_orbit_size": expected,
        "minimum_area": minimum_area,
        "area_counts": dict(sorted(area_counts.items())),
        "best_adjacent_hurwitz_decrease_counts": dict(sorted(best_decrease_counts.items())),
        "no_adjacent_hurwitz_decrease_by_area": dict(sorted(no_decrease_counts.items())),
        "first_nonminimum_no_decrease_witness": first_nonminimum_no_decrease,
        "universal_claim_refuted": first_nonminimum_no_decrease is not None,
        "elapsed_seconds": time.time() - t0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "purpose": "Complete finite falsifier; no finite-to-universal inference.",
        "claim_tested": "Every nonminimum F_N word has an adjacent left/right Hurwitz move lowering area by two.",
        "composition": "(pq)(x)=p(q(x)); word products left-to-right",
        "seed": None,
        "python": platform.python_version(),
        "repository_commit": commit,
        "argv": sys.argv,
        "result": enumerate_orbit(args.N),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
