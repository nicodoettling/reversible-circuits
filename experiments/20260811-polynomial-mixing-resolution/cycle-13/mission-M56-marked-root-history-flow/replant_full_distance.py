#!/usr/bin/env python3
"""Bounded geometry audit: leaf-replant neighbors versus full Pbar support.

Finite distances can refute a proposed universal short bound but cannot prove
polynomial mixing or congestion.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
from collections import deque
from pathlib import Path


def load_m50():
    repo = Path(__file__).resolve().parents[4]
    path = (
        repo
        / "experiments/20260811-polynomial-mixing-resolution"
        / "cycle-12/mission-M50-full-parking-flow"
        / "root_composition_audit.py"
    )
    spec = importlib.util.spec_from_file_location("m50_exact", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M50 = load_m50()
Tree = tuple
NodePath = tuple[int, ...]


def git_commit():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def macro_to_tree(macro):
    children = M50.children(macro)

    def build(vertex):
        return tuple(build(child) for child in children[vertex])

    return build(0)


def tree_to_macro(tree):
    degrees = []

    def visit(node):
        degrees.append(len(node))
        for child in node:
            visit(child)

    visit(tree)
    r = len(degrees) - 1
    return tuple(i for i in range(r) for _ in range(degrees[i]))


def vertex_paths(tree):
    answer = []

    def visit(node, path):
        answer.append((path, node))
        for index, child in enumerate(node):
            visit(child, path + (index,))

    visit(tree, ())
    return answer


def remove_at(tree, path):
    if len(path) == 1:
        index = path[0]
        return tree[:index] + tree[index + 1 :]
    index = path[0]
    child = remove_at(tree[index], path[1:])
    return tree[:index] + (child,) + tree[index + 1 :]


def insert_leaf(tree, parent_path, slot):
    if not parent_path:
        return tree[:slot] + ((),) + tree[slot:]
    index = parent_path[0]
    child = insert_leaf(tree[index], parent_path[1:], slot)
    return tree[:index] + (child,) + tree[index + 1 :]


def replant_neighbors(macro):
    tree = macro_to_tree(macro)
    answer = set()
    for leaf_path, node in vertex_paths(tree):
        if not leaf_path or node:
            continue
        base = remove_at(tree, leaf_path)
        for parent_path, parent in vertex_paths(base):
            for slot in range(len(parent) + 1):
                target = tree_to_macro(insert_leaf(base, parent_path, slot))
                if target != macro:
                    answer.add(target)
    return answer


def all_distances(source, adjacency):
    distance = {source: 0}
    queue = deque([source])
    while queue:
        state = queue.popleft()
        for target in adjacency[state]:
            if target not in distance:
                distance[target] = distance[state] + 1
                queue.append(target)
    return distance


def run(n):
    r = n - 1
    macros, adjacency, _capacities, raw_count = M50.exact_instance(n)
    y_neighbors = {macro: replant_neighbors(macro) for macro in macros}
    asymmetric = [
        [list(source), list(target)]
        for source in macros
        for target in y_neighbors[source]
        if source not in y_neighbors[target]
    ]
    missing = []
    max_distance = -1
    witness = None
    direct = 0
    directed_y_edges = 0
    for source in sorted(macros):
        distances = all_distances(source, adjacency)
        for target in sorted(y_neighbors[source]):
            directed_y_edges += 1
            if target in adjacency[source]:
                direct += 1
            if target not in distances:
                missing.append([list(source), list(target)])
                continue
            if distances[target] > max_distance:
                max_distance = distances[target]
                witness = [list(source), list(target)]
    return {
        "n": n,
        "r": r,
        "macro_count": len(macros),
        "raw_factorization_count": raw_count,
        "directed_distinct_replant_edges": directed_y_edges,
        "directed_replant_edges_already_actual": direct,
        "asymmetric_replant_support_failures": asymmetric,
        "actual_component_failures": missing,
        "maximum_shortest_actual_distance": max_distance,
        "maximum_distance_witness": witness,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 3 <= args.n_max <= 8:
        raise SystemExit("bounded exact range is 3 <= n-max <= 8")
    result = {
        "claim_tested": (
            "Every distinct plane-tree leaf-replanting neighbor lies in the "
            "same full-Pbar component, and bounded instances have the "
            "reported exact support distance."
        ),
        "universal_scope": (
            "A missing path refutes connectivity/comparison. Finite paths "
            "do not prove polynomial congestion or a universal diameter."
        ),
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "python": platform.python_version(),
        "git_commit": git_commit(),
        "seed": None,
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-13/mission-M56-marked-root-history-flow/"
            "replant_full_distance.py "
            f"--n-max {args.n_max} --output {args.output}"
        ),
        "records": [run(n) for n in range(3, args.n_max + 1)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
