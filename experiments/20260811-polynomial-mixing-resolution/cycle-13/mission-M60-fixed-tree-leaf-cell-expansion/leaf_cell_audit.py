#!/usr/bin/env python3
"""Exact bounded leaf-deletion-cell audit for fixed N=4/5 tree fibers.

Connectivity, cells, and candidate-cut flows are exact.  Optional scipy
eigenvalues are numerical diagnostics and are never promoted to a universal
claim.  The script imports the already-frozen M59 exact automaton with bytecode
writing disabled.
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
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


sys.dont_write_bytecode = True


def load_m59():
    path = (
        Path(__file__).resolve().parent.parent
        / "mission-M59-fixed-join-tree-internal-redteam"
        / "fixed_tree_dp_bucket_audit.py"
    )
    spec = importlib.util.spec_from_file_location("m59_frozen", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M59 = load_m59()


class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))
        self.s = [1] * n

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a: int, b: int) -> None:
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if self.s[a] < self.s[b]:
            a, b = b, a
        self.p[b] = a
        self.s[a] += self.s[b]


def delete_strand(word, all_edges, n: int, v: int):
    base_labels = [x for x in range(n) if x != v]
    base_edges = M59.edges(n - 1)
    base_index = {e: i for i, e in enumerate(base_edges)}
    p = tuple(range(n))
    old = M59.erase_label(p, v)
    out = []
    nulls = []
    for j, idx in enumerate(word):
        p = M59.append_edge(p, all_edges[idx])
        new = M59.erase_label(p, v)
        delta = M59.compose(M59.inverse(old), new)
        moved = [x for x in range(n - 1) if delta[x] != x]
        if not moved:
            nulls.append(j)
        elif (
            len(moved) == 2
            and delta[moved[0]] == moved[1]
            and delta[moved[1]] == moved[0]
        ):
            out.append(base_index[tuple(sorted(moved))])
        else:
            raise AssertionError((word, v, j, delta))
        old = new
    if len(nulls) != 2 or len(out) != len(word) - 2:
        raise AssertionError((word, v, out, nulls))
    return tuple(out), tuple(nulls)


def delete_original_labels(word, n: int, labels_to_delete):
    """Sequential strand erasure, tracking compressed label coordinates."""
    current_word = tuple(word)
    current_labels = list(range(n))
    current_n = n
    for original_v in labels_to_delete:
        current_v = current_labels.index(original_v)
        current_edges = M59.edges(current_n)
        current_word, _nulls = delete_strand(current_word, current_edges, current_n, current_v)
        current_labels.pop(current_v)
        current_n -= 1
    return current_word


def inversion_parity(values) -> int:
    return sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values))) % 2


def all_statistics(n: int, tree, all_edges, word):
    base = M59.word_statistics(n, tree, all_edges, word)
    leaves = M59.tree_leaves(n, tree)
    separations = []
    for v in leaves:
        a, b = M59.strand_nulls(word, all_edges, n, v)
        separations.append(b - a)
    joins = M59.verify_join_tree(n, tree, all_edges, word)
    tree_index = {edge: k for k, edge in enumerate(sorted(tree))}
    order = [tree_index[edge] for edge, _position in joins]
    base.update({
        "sum_leaf_null_separation": sum(separations),
        "max_leaf_null_separation": max(separations),
        "min_leaf_null_separation": min(separations),
        "join_order_parity": inversion_parity(order),
    })
    return base


def fraction_text(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def cell_operator_gap(cells_by_leaf, number_words: int):
    """Numerical second eigenvalue of the average conditional projections."""
    import numpy as np
    from scipy.sparse.linalg import LinearOperator, eigsh

    leaves = sorted(cells_by_leaf)

    def matvec(x):
        y = np.zeros(number_words, dtype=float)
        for v in leaves:
            for members in cells_by_leaf[v].values():
                average = float(np.sum(x[list(members)])) / len(members)
                y[list(members)] += average / len(leaves)
        return y

    operator = LinearOperator((number_words, number_words), matvec=matvec, dtype=float)
    values = eigsh(operator, k=min(4, number_words - 1), which="LA", tol=1e-11, return_eigenvectors=False)
    values = sorted((float(x) for x in values), reverse=True)
    return {
        "largest_eigenvalues": values,
        "numerical_gap": 1.0 - values[1],
        "status": "numerical finite diagnostic only",
    }


def audit_shape(n: int, name: str, tree, do_spectrum: bool):
    m = 2 * n - 2
    all_edges = M59.edges(n)
    words, cache_info = M59.enumerate_fixed_tree(n, tree, all_edges)
    index = {word: i for i, word in enumerate(words)}
    leaves = M59.tree_leaves(n, tree)

    cells_by_leaf = {v: defaultdict(list) for v in leaves}
    deletion_nulls = {}
    for i, word in enumerate(words):
        for v in leaves:
            base, nulls = delete_strand(word, all_edges, n, v)
            cells_by_leaf[v][base].append(i)
            deletion_nulls[(i, v)] = nulls
    cells_by_leaf = {
        v: {base: tuple(members) for base, members in grouped.items()}
        for v, grouped in cells_by_leaf.items()
    }

    dsu = DSU(len(words))
    for grouped in cells_by_leaf.values():
        for members in grouped.values():
            for j in members[1:]:
                dsu.union(members[0], j)
    components = sorted(Counter(dsu.find(i) for i in range(len(words))).values(), reverse=True)

    # Every leaf-cell update preserves the word obtained after erasing all
    # original tree leaves.  This exact key diagnoses the path-tree split.
    deletion_order = tuple(sorted(leaves, reverse=True))
    core_key = {
        i: delete_original_labels(word, n, deletion_order)
        for i, word in enumerate(words)
    }

    statistics = {i: all_statistics(n, tree, all_edges, word) for i, word in enumerate(words)}

    global_fibers = {r: M59.product_counts(n, all_edges, r) for r in (3, 4, 5)}
    buckets = []
    for r in (3, 4, 5):
        for position in range(m - r + 1):
            grouped = defaultdict(list)
            for i, word in enumerate(words):
                product = M59.evaluate(n, all_edges, word[position : position + r])
                grouped[(word[:position], word[position + r :], product)].append(i)
            for key, members in grouped.items():
                buckets.append((r, key[2], tuple(members)))

    def flows(subset):
        subset = set(subset)
        leaf_boundary = Fraction(0)
        for grouped in cells_by_leaf.values():
            for members in grouped.values():
                a = sum(i in subset for i in members)
                leaf_boundary += Fraction(a * (len(members) - a), len(leaves) * len(members))
        full_by_r = {r: Fraction(0) for r in (3, 4, 5)}
        restriction_by_r = {r: Fraction(0) for r in (3, 4, 5)}
        for r, product, members in buckets:
            a = sum(i in subset for i in members)
            if not a:
                continue
            f = global_fibers[r][product]
            outer = Fraction(1, 6 * (m - r + 1))
            full_by_r[r] += outer * a * Fraction(f - a, f)
            restriction_by_r[r] += outer * a * Fraction(len(members) - a, f)
        denominator = len(subset)
        return {
            "P_leaf_escape": fraction_text(leaf_boundary / denominator),
            "full_K_escape": fraction_text(sum(full_by_r.values(), Fraction(0)) / denominator),
            "restriction_escape": fraction_text(sum(restriction_by_r.values(), Fraction(0)) / denominator),
            "full_by_r": {str(r): fraction_text(full_by_r[r] / denominator) for r in (3, 4, 5)},
            "restriction_by_r": {
                str(r): fraction_text(restriction_by_r[r] / denominator) for r in (3, 4, 5)
            },
        }

    candidates = []
    statistic_names = list(next(iter(statistics.values())))
    for stat in statistic_names:
        values = sorted({statistics[i][stat] for i in range(len(words))})
        # Thresholds and every contiguous middle band.  Orient to the smaller
        # conditional side for P_leaf; either side remains globally <=1/2.
        raw_sets = []
        for threshold in values[:-1]:
            raw_sets.append(("le", values[0], threshold, {i for i in range(len(words)) if statistics[i][stat] <= threshold}))
        if stat != "join_order_parity":
            for lo_index in range(1, len(values) - 1):
                for hi_index in range(lo_index, len(values) - 1):
                    lo, hi = values[lo_index], values[hi_index]
                    raw_sets.append(("band", lo, hi, {i for i in range(len(words)) if lo <= statistics[i][stat] <= hi}))
        for family, lo, hi, subset in raw_sets:
            orientation = "inside"
            if len(subset) > len(words) // 2:
                subset = set(range(len(words))) - subset
                orientation = "fixed_fiber_complement"
            if not subset:
                continue
            row = {
                "statistic": stat,
                "family": family,
                "lo": lo,
                "hi": hi,
                "orientation": orientation,
                "side_size": len(subset),
            }
            row.update(flows(subset))
            candidates.append(row)

    # Add the parity half explicitly.
    parity = {i for i in range(len(words)) if statistics[i]["join_order_parity"] == 0}
    if len(parity) > len(words) // 2:
        parity = set(range(len(words))) - parity
        parity_orientation = "odd"
    else:
        parity_orientation = "even"
    parity_row = {
        "statistic": "join_order_parity",
        "family": "parity",
        "orientation": parity_orientation,
        "side_size": len(parity),
    }
    parity_row.update(flows(parity))
    candidates.append(parity_row)

    components_by_root = defaultdict(list)
    for i in range(len(words)):
        components_by_root[dsu.find(i)].append(i)
    core_to_roots = defaultdict(set)
    component_rows = []
    for root, members in components_by_root.items():
        keys = {core_key[i] for i in members}
        for key in keys:
            core_to_roots[key].add(root)
        row = {
            "size": len(members),
            "core_keys": [list(key) for key in sorted(keys)],
        }
        row.update(flows(members))
        component_rows.append(row)
    component_rows.sort(key=lambda row: (-row["size"], row["core_keys"]))

    leaf_cell_sizes = [len(members) for grouped in cells_by_leaf.values() for members in grouped.values()]
    result = {
        "shape": name,
        "tree_edges": [list(e) for e in tree],
        "fiber_size": len(words),
        "leaves": leaves,
        "components": len(components),
        "component_sizes": components,
        "all_leaf_deletion_order": list(deletion_order),
        "all_leaf_core_distribution": [
            {"core_word": list(key), "count": count}
            for key, count in sorted(Counter(core_key.values()).items())
        ],
        "each_component_has_one_core_key": all(len(row["core_keys"]) == 1 for row in component_rows),
        "each_core_key_has_one_component": all(len(roots) == 1 for roots in core_to_roots.values()),
        "component_flows": component_rows,
        "cells": len(leaf_cell_sizes),
        "cell_size_distribution": dict(sorted(Counter(leaf_cell_sizes).items())),
        "maximum_cell_size": max(leaf_cell_sizes),
        "minimum_nontrivial_cell_size": min((x for x in leaf_cell_sizes if x > 1), default=None),
        "automaton_cache": {
            "hits": cache_info.hits,
            "misses": cache_info.misses,
            "currsize": cache_info.currsize,
        },
        "candidate_cuts": candidates,
        "minimum_candidate_P_leaf_escape": min(candidates, key=lambda row: Fraction(row["P_leaf_escape"])),
        "minimum_candidate_full_K_escape": min(candidates, key=lambda row: Fraction(row["full_K_escape"])),
        "minimum_candidate_restriction_escape": min(candidates, key=lambda row: Fraction(row["restriction_escape"])),
    }
    if do_spectrum:
        result["P_leaf_spectrum"] = cell_operator_gap(cells_by_leaf, len(words))
    return result


def trees_for_n(n: int):
    if n == 4:
        return {
            "star": ((0, 1), (0, 2), (0, 3)),
            "path": ((0, 1), (0, 2), (2, 3)),
        }
    if n == 5:
        return M59.tree_shapes()
    raise ValueError(n)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, choices=(4, 5), required=True)
    parser.add_argument("--shape", default="all")
    parser.add_argument("--spectrum", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    shapes = trees_for_n(args.N)
    names = list(shapes) if args.shape == "all" else [args.shape]
    rows = [audit_shape(args.N, name, shapes[name], args.spectrum) for name in names]
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "argv": sys.argv,
        "commit": commit,
        "python": platform.python_version(),
        "seed": None,
        "dependencies": {"scipy": "used only if --spectrum; numerical diagnostic"},
        "convention": "(pq)(x)=p(q(x)); right-appending swaps domain entries",
        "P_leaf": "uniform leaf choice followed by exact heat bath in current Del_v cell",
        "K": "literal lazy K; outcome weight 1/[6(m-r+1)|F_r(g)|] for N=4,5",
        "claims_tested": [
            "Universal leaf-cell irreducibility can be falsified by a disconnected tested fiber.",
            "Middle chronology bands or deletion-deck statistics can be falsified as zero/full-K bottlenecks.",
        ],
        "scope_warning": "Finite connectivity, flow, and numerical eigenvalues cannot prove polynomial asymptotic bounds.",
        "summary": {
            "N": args.N,
            "m": 2 * args.N - 2,
            "shapes": names,
            "all_connected": all(row["components"] == 1 for row in rows),
            "elapsed_seconds_before_write": time.perf_counter() - started,
        },
        "trees": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
