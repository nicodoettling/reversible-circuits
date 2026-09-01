#!/usr/bin/env python3
"""Exact insertion-coordinate transfer for marked leaf-strand lifts.

For z in Z_q, the transfer recurrence counts lifts to Z_(q+1) with one
specified new label v as a prefix-join-tree leaf.  The script independently
checks the recurrence against direct fibers through d=4 and evaluates it on
all 2,880 bases in Z_4, thereby counting d=5 fibers without enumerating Z_5.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent


def load_local():
    path = HERE / "marked_leaf_audit.py"
    spec = importlib.util.spec_from_file_location("m112_marked", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


A = load_local()


def join_flags(q: int, z: A.Word) -> tuple[bool, ...]:
    dsu = A.DSU(q)
    flags = []
    for x, y in z:
        flags.append(dsu.find(x) != dsu.find(y))
        dsu.union(x, y)
    if sum(flags) != q - 1:
        raise AssertionError((q, z, flags))
    return tuple(flags)


def step_vector(vec: tuple[int, ...], edge: A.Edge, is_join: bool) -> tuple[int, ...]:
    x, y = edge
    out = list(vec)
    if is_join:
        out[x], out[y] = vec[y], vec[x]
    else:
        out[x] = vec[x] + vec[y]
        out[y] = vec[x] + vec[y]
    return tuple(out)


def step_matrix(mat: tuple[tuple[int, ...], ...], edge: A.Edge, is_join: bool):
    # Rows index the opening coordinate; columns the current coordinate.
    return tuple(step_vector(row, edge, is_join) for row in mat)


def transfer_count(q: int, z: A.Word) -> dict:
    flags = join_flags(q, z)
    L = len(z)
    total = 0
    interval_masses = Counter()
    maximum_entry = 0
    maximum_row_support = 0
    for i in range(L + 1):
        mat = tuple(tuple(int(a == b) for b in range(q)) for a in range(q))
        mass = q
        total += mass  # empty interval i=j
        interval_masses[mass] += 1
        for j in range(i, L):
            mat = step_matrix(mat, z[j], flags[j])
            mass = sum(sum(row) for row in mat)
            total += mass
            interval_masses[mass] += 1
            maximum_entry = max(maximum_entry, *(max(row) for row in mat))
            maximum_row_support = max(maximum_row_support, *(sum(x != 0 for x in row) for row in mat))
    expected_intervals = (L + 1) * (L + 2) // 2
    if sum(interval_masses.values()) != expected_intervals:
        raise AssertionError((sum(interval_masses.values()), expected_intervals))
    return {
        "count": total,
        "interval_mass_histogram": dict(sorted(interval_masses.items())),
        "maximum_transfer_entry": maximum_entry,
        "maximum_row_support": maximum_row_support,
    }


def direct_sizes(d: int):
    states = A.enumerate_z(d)
    ans = {}
    for w in states:
        for v in A.leaves(d, A.join_tree(d, w)):
            z, _ = A.delete_strand(d, w, v)
            ans[(v, z)] = ans.get((v, z), 0) + 1
    return states, ans


def concatenated_distinct_squares(z: A.Word) -> bool:
    if len(z) != 4:
        return False
    return z[0] == z[1] and z[2] == z[3] and z[0] != z[2]


def audit(q_values: list[int]) -> dict:
    rows = []
    for q in q_values:
        started = time.perf_counter()
        bases = A.enumerate_z(q)
        counts = Counter()
        max_entry = 0
        max_support = 0
        special = Counter()
        for z in bases:
            result = transfer_count(q, z)
            counts[result["count"]] += 1
            max_entry = max(max_entry, result["maximum_transfer_entry"])
            max_support = max(max_support, result["maximum_row_support"])
            if q == 3:
                special[(concatenated_distinct_squares(z), result["count"])] += 1

        direct_check = None
        if q + 1 <= 4:
            _upstairs, direct = direct_sizes(q + 1)
            mismatches = []
            # Standardize the downstairs labels after deleting v.  The
            # recurrence is label-equivariant, so only the standardized z
            # and its count matter.
            for (v, z), size in direct.items():
                predicted = transfer_count(q, z)["count"]
                if size != predicted and len(mismatches) < 5:
                    mismatches.append({"v": v, "z": A.word_json(z), "direct": size, "predicted": predicted})
            direct_check = {
                "fibers": len(direct),
                "mismatch_count_recorded": len(mismatches),
                "mismatch_examples": mismatches,
                "direct_histogram": dict(sorted(Counter(direct.values()).items())),
            }
            if mismatches:
                raise AssertionError(mismatches[0])

        rows.append({
            "base_q": q,
            "upstairs_d": q + 1,
            "base_states": len(bases),
            "fiber_count_histogram_per_missing_label": dict(sorted(counts.items())),
            "fiber_min": min(counts),
            "fiber_max": max(counts),
            "fiber_max_over_min": max(counts) / min(counts),
            "maximum_transfer_entry": max_entry,
            "maximum_row_support": max_support,
            "q3_square_correlation": {str(k): v for k, v in sorted(special.items())},
            "direct_check": direct_check,
            "elapsed_seconds": time.perf_counter() - started,
        })
    return {"rows": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-q", type=int, nargs="+", default=[1, 2, 3, 4])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if any(q < 1 or q > 4 for q in args.base_q):
        raise SystemExit("audit intentionally supports 1<=base-q<=4")
    started = time.perf_counter()
    data = audit(args.base_q)
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "argv": sys.argv,
        "commit": commit,
        "python": platform.python_version(),
        "seed": None,
        "nonstandard_dependencies": {},
        "claim_tested": "The insertion-coordinate transfer recurrence exactly counts each fixed missing-label marked-leaf fiber.",
        "scope_warning": "Exact agreement through d=4 and evaluation over Z_4 are finite; the recurrence's universal validity requires its separate bijective proof.",
        **data,
        "elapsed_seconds": time.perf_counter() - started,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"rows": payload["rows"], "elapsed_seconds": payload["elapsed_seconds"]}, sort_keys=True))


if __name__ == "__main__":
    main()
