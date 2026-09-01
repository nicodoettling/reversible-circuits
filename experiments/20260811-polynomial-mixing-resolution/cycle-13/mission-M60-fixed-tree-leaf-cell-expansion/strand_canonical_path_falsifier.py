#!/usr/bin/env python3
"""Exact falsifier for the M60 strand-cell canonical H3 path lemma.

For every state in representative N=4/5 fixed-tree fibers and every tree
leaf, move the opening null increment right by product-preserving Hurwitz
swaps, refresh the adjacent square to the fixed tree leaf edge, then slide it
to the final gap.  Every pair swap is padded by one unchanged neighbor in an
actual length-three same-product update.
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


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


HERE = Path(__file__).resolve().parent
M59 = load_module(
    "m59_for_path",
    HERE.parent / "mission-M59-fixed-join-tree-internal-redteam" / "fixed_tree_dp_bucket_audit.py",
)
M60 = load_module("m60_cells", HERE / "leaf_cell_audit.py")


def conjugate_edge(conjugator, edge):
    a, b = edge
    x, y = conjugator

    def move(v):
        if v == x:
            return y
        if v == y:
            return x
        return v

    return tuple(sorted((move(a), move(b))))


def actual_join_tree(n: int, all_edges, word):
    dsu = M59.DSU(n)
    joins = []
    for idx in word:
        a, b = all_edges[idx]
        if dsu.find(a) != dsu.find(b):
            dsu.union(a, b)
            joins.append((a, b))
    return tuple(sorted(joins))


def assert_minimal_identity(n: int, all_edges, word):
    if M59.evaluate(n, all_edges, word) != tuple(range(n)):
        raise AssertionError(("not identity", word))
    tree = actual_join_tree(n, all_edges, word)
    if len(tree) != n - 1:
        raise AssertionError(("not full connected", tree, word))
    return tree


def pair_to_padded_triple(source, target, pair_position: int):
    """Return one source/target triple certifying an actual H3 outcome."""
    m = len(source)
    if pair_position + 2 < m:
        i = pair_position
    else:
        i = pair_position - 1
    return i, source[i : i + 3], target[i : i + 3]


def canonicalize(n: int, tree, all_edges, word, v: int):
    edge_index = {e: i for i, e in enumerate(all_edges)}
    incident = [e for e in tree if v in e]
    if len(incident) != 1:
        raise AssertionError((tree, v, incident))
    f_idx = edge_index[incident[0]]
    base, original_nulls = M60.delete_strand(word, all_edges, n, v)
    current = tuple(word)
    step_types = Counter()
    path_steps = 0

    while True:
        current_base, nulls = M60.delete_strand(current, all_edges, n, v)
        if current_base != base:
            raise AssertionError(("base changed", v, base, current_base))
        p, q = nulls
        if q == p + 1:
            break
        a_idx, b_idx = current[p], current[p + 1]
        a, b = all_edges[a_idx], all_edges[b_idx]
        candidates = [
            (b_idx, edge_index[conjugate_edge(b, a)], "right_hurwitz"),
            (edge_index[conjugate_edge(a, b)], a_idx, "inverse_hurwitz"),
        ]
        valid = []
        for x, y, kind in candidates:
            trial = current[:p] + (x, y) + current[p + 2 :]
            trial_base, trial_nulls = M60.delete_strand(trial, all_edges, n, v)
            if trial_base == base and trial_nulls == (p + 1, q):
                valid.append((trial, kind))
        if not valid:
            raise AssertionError(("no null swap", n, tree, word, v, current, nulls))
        trial, kind = valid[0]
        triple_i, old_triple, new_triple = pair_to_padded_triple(current, trial, p)
        if M59.evaluate(n, all_edges, old_triple) != M59.evaluate(n, all_edges, new_triple):
            raise AssertionError(("bad padded product", triple_i, old_triple, new_triple))
        assert_minimal_identity(n, all_edges, trial)
        current = trial
        step_types[kind] += 1
        path_steps += 1

    base_now, nulls = M60.delete_strand(current, all_edges, n, v)
    p, q = nulls
    if base_now != base or q != p + 1 or current[p] != current[q]:
        raise AssertionError(("not an adjacent square", current, nulls, base_now, base))

    # Refresh the square label to the actual leaf edge of T.
    trial = current[:p] + (f_idx, f_idx) + current[p + 2 :]
    if p > 0:
        old_triple, new_triple = current[p - 1 : p + 2], trial[p - 1 : p + 2]
    else:
        old_triple, new_triple = current[:3], trial[:3]
    if M59.evaluate(n, all_edges, old_triple) != M59.evaluate(n, all_edges, new_triple):
        raise AssertionError(("bad square refresh", old_triple, new_triple))
    if M60.delete_strand(trial, all_edges, n, v)[0] != base:
        raise AssertionError("refresh changed base")
    if assert_minimal_identity(n, all_edges, trial) != tuple(sorted(tree)):
        raise AssertionError(("refresh did not restore T", tree, trial))
    current = trial
    step_types["square_label_refresh"] += 1
    path_steps += 1

    # Slide f^2 right through the unchanged base sequence.
    p = M60.delete_strand(current, all_edges, n, v)[1][0]
    while p + 2 < len(current):
        c = current[p + 2]
        trial = current[:p] + (c, f_idx, f_idx) + current[p + 3 :]
        if M59.evaluate(n, all_edges, current[p : p + 3]) != M59.evaluate(n, all_edges, trial[p : p + 3]):
            raise AssertionError("bad square slide")
        if M60.delete_strand(trial, all_edges, n, v)[0] != base:
            raise AssertionError("slide changed base")
        if assert_minimal_identity(n, all_edges, trial) != tuple(sorted(tree)):
            raise AssertionError(("slide changed T", tree, trial))
        current = trial
        p += 1
        step_types["square_slide"] += 1
        path_steps += 1

    expected = tuple(base) + (f_idx, f_idx)
    # Re-embed compressed base edge indices onto the original label set.
    remaining = [x for x in range(n) if x != v]
    base_edges = M59.edges(n - 1)
    embedded = tuple(
        edge_index[tuple(sorted((remaining[base_edges[idx][0]], remaining[base_edges[idx][1]])))]
        for idx in base
    ) + (f_idx, f_idx)
    if current != embedded:
        raise AssertionError(("wrong canonical target", current, embedded, expected))
    return {
        "original_nulls": original_nulls,
        "path_steps": path_steps,
        "step_types": step_types,
    }


def trees_for_n(n: int):
    return M60.trees_for_n(n)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, choices=(4, 5), required=True)
    parser.add_argument("--shape", default="all")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    shapes = trees_for_n(args.N)
    names = list(shapes) if args.shape == "all" else [args.shape]
    rows = []
    for name in names:
        tree = shapes[name]
        all_edges = M59.edges(args.N)
        words, _cache = M59.enumerate_fixed_tree(args.N, tree, all_edges)
        leaves = M59.tree_leaves(args.N, tree)
        step_counts = Counter()
        path_lengths = Counter()
        checked = 0
        for word in words:
            for v in leaves:
                result = canonicalize(args.N, tree, all_edges, word, v)
                checked += 1
                path_lengths[result["path_steps"]] += 1
                step_counts.update(result["step_types"])
        rows.append({
            "shape": name,
            "tree_edges": [list(e) for e in tree],
            "fiber_size": len(words),
            "leaves": leaves,
            "state_leaf_pairs_checked": checked,
            "failures": 0,
            "maximum_path_steps": max(path_lengths),
            "path_length_distribution": dict(sorted(path_lengths.items())),
            "step_type_totals": dict(sorted(step_counts.items())),
        })
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
        "claim_tested": "Every leaf deletion cell admits the explicit <=2m-3 H3-supported canonical path preserving Del_v.",
        "scope_warning": "N<=5 exact success is a falsification check; the universal proof is separate.",
        "summary": {
            "N": args.N,
            "m": 2 * args.N - 2,
            "shapes": names,
            "state_leaf_pairs_checked": sum(row["state_leaf_pairs_checked"] for row in rows),
            "failures": 0,
            "maximum_path_steps": max(row["maximum_path_steps"] for row in rows),
            "elapsed_seconds_before_write": time.perf_counter() - started,
        },
        "trees": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
