#!/usr/bin/env python3
"""Exact raw marked-leaf projection flow for d<=4.

Fix the missing label v=d-1 and restrict P_(0,d) by holding proposals which
lose the leaf mark.  Partition by z=Del_v(w).  This script compares each
oriented off-diagonal base generator with all physical proposals deleting to
that exact oriented move, both before and after stationary-flow normalization.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent


def load_local():
    path = HERE / "marked_leaf_audit.py"
    spec = importlib.util.spec_from_file_location("m112_marked_flow", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


A = load_local()


def word_json(word):
    return [list(e) for e in word]


def audit_d(d: int) -> dict:
    started = time.perf_counter()
    v = d - 1
    states = A.enumerate_z(d)
    state_set = set(states)
    fibers = defaultdict(list)
    for w in states:
        if v in A.leaves(d, A.join_tree(d, w)):
            z, _ = A.delete_strand(d, w, v)
            fibers[z].append(w)
    q = d - 1
    base_states = A.enumerate_z(q)
    if set(fibers) != set(base_states):
        raise AssertionError(("projection not onto", d, len(fibers), len(base_states)))

    # Demand keys retain site and orientation, not merely the resulting pair.
    demands = []
    by_target = defaultdict(list)
    for z in base_states:
        for site, orientation, zp in A.proposals(z):
            if zp != z:
                key = (z, site, orientation, zp)
                demands.append(key)
                by_target[(z, zp)].append((site, orientation))

    lift_counts = Counter()
    retained_identity = 0
    retained_base_move = 0
    mark_lost = 0
    bad_images = []
    physical_directed = 0
    for z, ws in fibers.items():
        for w in ws:
            for _physical_site, _physical_orientation, wp in A.proposals(w):
                physical_directed += 1
                if wp not in state_set:
                    raise AssertionError("proposal left Z_d")
                if v not in A.leaves(d, A.join_tree(d, wp)):
                    mark_lost += 1
                    continue
                zp, _ = A.delete_strand(d, wp, v)
                if zp == z:
                    retained_identity += 1
                    continue
                matches = by_target.get((z, zp), [])
                if not matches:
                    if len(bad_images) < 5:
                        bad_images.append({"z": word_json(z), "zp": word_json(zp), "w": word_json(w), "wp": word_json(wp)})
                    continue
                retained_base_move += 1
                # For off-diagonal signed Hurwitz moves the requested
                # (site,orientation) is unique in all audited cases.  If not,
                # count the physical edge for every identical generator
                # commodity and report the ambiguity.
                for site, orientation in matches:
                    lift_counts[(z, site, orientation, zp)] += 1

    if bad_images:
        raise AssertionError(bad_images[0])

    sizes = {z: len(ws) for z, ws in fibers.items()}
    total_marked = sum(sizes.values())
    base_total = len(base_states)
    physical_sites = 2 * d - 3
    base_sites = max(1, 2 * q - 3)
    rows = []
    zero_demands = 0
    for z, site, orientation, zp in demands:
        count = lift_counts[(z, site, orientation, zp)]
        if count == 0:
            zero_demands += 1
        # Ratio of raw projection stationary flow to the uniform base
        # oriented-generator stationary flow.  Both 1/4 factors cancel.
        normalized_ratio = count * base_total * base_sites / (total_marked * physical_sites)
        rows.append((normalized_ratio, count, sizes[z], z, site, orientation, zp))
    rows.sort(key=lambda x: x[0])
    minrow = rows[0] if rows else None
    maxrow = rows[-1] if rows else None
    per_state_fractions = [count / size for _ratio, count, size, *_rest in rows]

    # Aggregate parallel generator commodities by ordered base state pair.
    pair_counts = Counter()
    pair_base_mult = Counter()
    for z, site, orientation, zp in demands:
        pair_counts[(z, zp)] += lift_counts[(z, site, orientation, zp)]
        pair_base_mult[(z, zp)] += 1
    pair_ratios = []
    for (z, zp), count in pair_counts.items():
        ratio = count * base_total * base_sites / (pair_base_mult[(z, zp)] * total_marked * physical_sites)
        pair_ratios.append((ratio, count, pair_base_mult[(z, zp)], z, zp))
    pair_ratios.sort(key=lambda x: x[0])

    def record(row):
        if row is None:
            return None
        ratio, count, size, z, site, orientation, zp = row
        return {
            "normalized_flow_ratio": ratio,
            "physical_lift_count": count,
            "source_fiber_size": size,
            "source": word_json(z),
            "base_site": site,
            "base_orientation": orientation,
            "target": word_json(zp),
        }

    return {
        "d": d,
        "fixed_leaf_label": v,
        "upstairs_states": len(states),
        "marked_restriction_states": total_marked,
        "base_states": base_total,
        "base_oriented_offdiagonal_demands": len(demands),
        "zero_aggregate_lift_demands": zero_demands,
        "source_fiber_size_histogram": dict(sorted(Counter(sizes.values()).items())),
        "physical_directed_proposals": physical_directed,
        "retained_identity": retained_identity,
        "retained_base_move": retained_base_move,
        "mark_lost": mark_lost,
        "mark_loss_fraction": mark_lost / physical_directed,
        "lift_count_histogram": dict(sorted(Counter(lift_counts.values()).items())),
        "per_source_state_lift_fraction_min": min(per_state_fractions, default=None),
        "per_source_state_lift_fraction_max": max(per_state_fractions, default=None),
        "minimum_oriented_demand": record(minrow),
        "maximum_oriented_demand": record(maxrow),
        "minimum_parallel_pair_normalized_flow_ratio": pair_ratios[0][0] if pair_ratios else None,
        "maximum_parallel_pair_normalized_flow_ratio": pair_ratios[-1][0] if pair_ratios else None,
        "elapsed_seconds": time.perf_counter() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", type=int, nargs="+", default=[3, 4])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if any(d < 3 or d > 4 for d in args.d):
        raise SystemExit("exact audit is intentionally restricted to 3<=d<=4")
    started = time.perf_counter()
    rows = [audit_d(d) for d in args.d]
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
        "claim_tested": "The raw fixed-leaf stationary-flow projection aggregate-dominates the uniform P_(0,d-1) base edge flow.",
        "scope_warning": "Finite normalized ratios can falsify zero aggregate lifting but do not prove a universal comparison.",
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
