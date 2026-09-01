#!/usr/bin/env python3
"""Exhaustive local algebra audit for M86's signed rectangle case split."""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import subprocess
import time
from pathlib import Path


def edge(a: int, b: int) -> tuple[int, int]:
    return (a, b) if a < b else (b, a)


def conj(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    x, y = b
    u, v = a
    u = y if u == x else x if u == y else u
    v = y if v == x else x if v == y else v
    return edge(u, v)


def right(left, right_factor):
    # R swaps occurrence strands and conjugates the left occurrence.
    la, a = left
    lb, b = right_factor
    return ((lb, b), (la, conj(a, b)))


def inverse(left, right_factor):
    # R^-1 swaps occurrence strands and conjugates the right occurrence.
    la, a = left
    lb, b = right_factor
    return ((lb, conj(b, a)), (la, a))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", nargs="+", type=int, default=[3, 4, 5, 6])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    records = []
    for n in args.N:
        edges = [edge(a, b) for a, b in itertools.combinations(range(n), 2)]
        cases = inverse_failures = occurrence_failures = endpoint_bound_failures = 0
        endpoint_move_hist = {0: 0, 1: 0, 2: 0}
        both_marked_max = 0
        for a in edges:
            for b in edges:
                cases += 1
                original = (("A", a), ("B", b))
                rw = right(*original)
                back = inverse(*rw)
                if back != (("A", a), ("B", b)):
                    inverse_failures += 1
                if sorted(x[0] for x in rw) != ["A", "B"]:
                    occurrence_failures += 1
                changed = sum(1 for x in a if (b[1] if x == b[0] else b[0] if x == b[1] else x) != x)
                endpoint_move_hist[changed] += 1
                if changed > 2:
                    endpoint_bound_failures += 1
                # Even when both factor occurrences are declared tracked,
                # R conjugates only occurrence A; R^-1 only occurrence B.
                both_marked_max = max(both_marked_max, changed)
                iw = inverse(*original)
                fwd = right(*iw)
                if fwd != (("A", a), ("B", b)):
                    inverse_failures += 1
                changed_inv = sum(1 for x in b if (a[1] if x == a[0] else a[0] if x == a[1] else x) != x)
                endpoint_move_hist[changed_inv] += 1
                if changed_inv > 2:
                    endpoint_bound_failures += 1
                both_marked_max = max(both_marked_max, changed_inv)
        records.append({
            "N": n,
            "ordered_edge_pairs": cases,
            "signed_cases": 2 * cases,
            "inverse_failures": inverse_failures,
            "occurrence_label_failures": occurrence_failures,
            "endpoint_bound_failures": endpoint_bound_failures,
            "endpoint_moves_histogram": endpoint_move_hist,
            "max_endpoint_tracks_changed_when_both_occurrences_marked": both_marked_max,
        })
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "schema": "m86-local-signed-rectangle-v1",
        "claim_status": "exact finite audit of the universal transposition case split",
        "scope_warning": "The enumeration checks local signed algebra; the all-length voltage bound additionally uses the proved occurrence-band pullback induction.",
        "convention": "R(a,b)=(b,bab); R^-1(a,b)=(aba,a)",
        "commit": commit,
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "argv": [str(x) for x in __import__("sys").argv],
        "elapsed_seconds": time.time() - started,
        "records": records,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
