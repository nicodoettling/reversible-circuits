#!/usr/bin/env python3
"""Complete finite falsifier for a full-block reverse area-action lemma.

The deliberately strong claim tested is that every nonminimum word in the
minimal connected macro F_N has *some* same-product r=3,4,5 window outcome of
smaller prefix-rank area.  The minimization below even allows outcomes that
leave F_N.  Thus a zero-decrease witness refutes both this strong claim and
the weaker proposed within-F_N descent action.  Finite success proves neither.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
import platform
import subprocess
import sys
import time
from collections import Counter, deque
from pathlib import Path


HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1] / "cycle-08" / "mission-M34-area-median-shell" / "exact_local_area_ascent.py"
SPEC = importlib.util.spec_from_file_location("m34_exact", BASE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot import {BASE}")
M34 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M34)


def minimum_internal_sums(
    n: int,
    ts: list[tuple[int, ...]],
    track_support: bool,
) -> tuple[
    dict[tuple[tuple[int, ...], int, tuple[int, ...]], int],
    dict[tuple[tuple[int, ...], int, tuple[int, ...]], dict[int, int]],
]:
    """Minimum internal sums, optionally resolved by replacement support."""
    identity = tuple(range(n))
    answer: dict[tuple[tuple[int, ...], int, tuple[int, ...]], int] = {}
    by_support: dict[
        tuple[tuple[int, ...], int, tuple[int, ...]], dict[int, int]
    ] = {}
    for start in itertools.permutations(range(n)):
        # full[p] is the minimum sum including the rank after the current
        # last factor.  Subtract the fixed endpoint rank before storing.
        full: dict[tuple[tuple[int, ...], int], int] = {(identity, 0): 0}
        for length in range(1, 6):
            nxt: dict[tuple[tuple[int, ...], int], int] = {}
            for (product, support), value in full.items():
                for edge_index, t in enumerate(ts):
                    target = M34.compose(product, t)
                    target_support = support | (1 << edge_index) if track_support else 0
                    candidate = value + M34.rank(M34.compose(start, target))
                    key = (target, target_support)
                    if candidate < nxt.get(key, 10**9):
                        nxt[key] = candidate
            full = nxt
            if length >= 3:
                for (product, support), value in full.items():
                    internal = value - M34.rank(M34.compose(start, product))
                    key = (start, length, product)
                    answer[key] = min(answer.get(key, 10**9), internal)
                    if track_support:
                        support_row = by_support.setdefault(key, {})
                        support_row[support] = min(
                            support_row.get(support, 10**9), internal
                        )
    return answer, by_support


def support_connected(n: int, edges: list[tuple[int, int]], mask: int) -> bool:
    adjacency = [[] for _ in range(n)]
    for index, (a, b) in enumerate(edges):
        if mask & (1 << index):
            adjacency[a].append(b)
            adjacency[b].append(a)
    seen = {0}
    stack = [0]
    while stack:
        vertex = stack.pop()
        for target in adjacency[vertex]:
            if target not in seen:
                seen.add(target)
                stack.append(target)
    return len(seen) == n


def enumerate_orbit(n: int, track_connected_targets: bool) -> dict[str, object]:
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    ts = [M34.transposition(n, *edge) for edge in edges]
    m = 2 * n - 2
    base = len(edges)
    powers = [base**i for i in range(m)]
    edge_to_index = {edge: i for i, edge in enumerate(edges)}
    conjugate = [
        [edge_to_index[M34.conjugate(edges[a], edges[b])] for b in range(base)]
        for a in range(base)
    ]
    minimum, minimum_by_support = minimum_internal_sums(
        n, ts, track_connected_targets
    )

    start_word: list[int] = []
    for vertex in range(1, n):
        edge = edge_to_index[(0, vertex)]
        start_word.extend((edge, edge))
    start_code = sum(digit * powers[i] for i, digit in enumerate(start_word))

    identity = tuple(range(n))
    seen = {start_code}
    queue = deque([start_code])
    area_counts: Counter[int] = Counter()
    best_decrease_counts: Counter[int] = Counter()
    zero_decrease_by_area: Counter[int] = Counter()
    connected_best_decrease_counts: Counter[int] = Counter()
    connected_zero_decrease_by_area: Counter[int] = Counter()
    first_nonminimum_zero: dict[str, object] | None = None
    first_nonminimum_connected_zero: dict[str, object] | None = None
    minimum_area = n - 1
    started = time.time()

    while queue:
        code = queue.popleft()
        tmp = code
        word = [0] * m
        for i in range(m):
            word[i], tmp = tmp % base, tmp // base

        prefixes = [identity]
        heights = [0]
        for index in word:
            prefixes.append(M34.compose(prefixes[-1], ts[index]))
            heights.append(M34.rank(prefixes[-1]))
        if prefixes[-1] != identity:
            raise AssertionError("nonbridge in Hurwitz orbit")
        area = sum(heights)
        area_counts[area] += 1

        best_decrease = 0
        best_connected_decrease = 0
        best_window: dict[str, int] | None = None
        for length in (3, 4, 5):
            if length > m:
                continue
            for i in range(m - length + 1):
                product = identity
                for j in range(i, i + length):
                    product = M34.compose(product, ts[word[j]])
                old_internal = sum(heights[i + 1 : i + length])
                new_internal = minimum[(prefixes[i], length, product)]
                decrease = old_internal - new_internal
                if decrease > best_decrease:
                    best_decrease = decrease
                    best_window = {
                        "r": length,
                        "window_start_zero_based": i,
                        "decrease": decrease,
                    }
                if track_connected_targets:
                    outside_support = 0
                    for position, edge_index in enumerate(word):
                        if not (i <= position < i + length):
                            outside_support |= 1 << edge_index
                    for replacement_support, candidate_internal in (
                        minimum_by_support[(prefixes[i], length, product)].items()
                    ):
                        if support_connected(
                            n, edges, outside_support | replacement_support
                        ):
                            best_connected_decrease = max(
                                best_connected_decrease,
                                old_internal - candidate_internal,
                            )
        best_decrease_counts[best_decrease] += 1
        if best_decrease == 0:
            zero_decrease_by_area[area] += 1
            if area > minimum_area and first_nonminimum_zero is None:
                first_nonminimum_zero = {
                    "edges": [list(edges[index]) for index in word],
                    "area": area,
                    "heights": heights,
                    "minimum_area": minimum_area,
                    "best_window": best_window,
                    "note": "No descent even when the target may leave F_N.",
                }
        if track_connected_targets:
            connected_best_decrease_counts[best_connected_decrease] += 1
            if best_connected_decrease == 0:
                connected_zero_decrease_by_area[area] += 1
                if area > minimum_area and first_nonminimum_connected_zero is None:
                    first_nonminimum_connected_zero = {
                        "edges": [list(edges[index]) for index in word],
                        "area": area,
                        "heights": heights,
                        "minimum_area": minimum_area,
                        "note": "No descent whose target remains in F_N.",
                    }

        # The minimal connected macro is the single Hurwitz orbit.  Generate
        # it by right and inverse adjacent Hurwitz moves.
        for i in range(m - 1):
            a, b = word[i], word[i + 1]
            u, v = b, conjugate[a][b]
            nxt = code + (u - a) * powers[i] + (v - b) * powers[i + 1]
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
            u, v = conjugate[b][a], a
            nxt = code + (u - a) * powers[i] + (v - b) * powers[i + 1]
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)

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
        "maximum_one_window_decrease_counts": dict(sorted(best_decrease_counts.items())),
        "zero_decrease_counts_by_area": dict(sorted(zero_decrease_by_area.items())),
        "first_nonminimum_zero_decrease_witness": first_nonminimum_zero,
        "connected_target_check_enabled": track_connected_targets,
        "maximum_connected_target_decrease_counts": dict(
            sorted(connected_best_decrease_counts.items())
        ),
        "connected_target_zero_decrease_counts_by_area": dict(
            sorted(connected_zero_decrease_by_area.items())
        ),
        "first_nonminimum_connected_target_zero_decrease_witness": (
            first_nonminimum_connected_zero
        ),
        "universal_claim_refuted": first_nonminimum_zero is not None,
        "within_F_claim_refuted": first_nonminimum_connected_zero is not None,
        "elapsed_seconds": time.time() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--within-connected",
        action="store_true",
        help="also resolve replacement support and require the target to stay in F_N",
    )
    args = parser.parse_args()
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "purpose": "Complete finite falsifier; no finite-to-universal inference.",
        "claim_tested": (
            "Every nonminimum F_N word has a smaller-area same-product outcome "
            "in some r=3,4,5 window, even if targets outside F_N are allowed."
        ),
        "composition": "(pq)(x)=p(q(x)); word products left-to-right",
        "seed": None,
        "deterministic": True,
        "python": sys.version,
        "platform": platform.platform(),
        "repository_commit": commit,
        "argv": sys.argv,
        "result": enumerate_orbit(args.N, args.within_connected),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "N": args.N,
        "refuted": payload["result"]["universal_claim_refuted"],
        "within_F_refuted": payload["result"]["within_F_claim_refuted"],
        "witness_area": (
            payload["result"]["first_nonminimum_zero_decrease_witness"] or {}
        ).get("area"),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
