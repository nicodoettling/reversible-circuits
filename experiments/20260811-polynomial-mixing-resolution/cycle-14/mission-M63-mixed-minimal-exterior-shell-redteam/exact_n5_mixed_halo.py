#!/usr/bin/env python3
"""Exact N=5 full-K audit of the smallest mixed exterior halo."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import platform
import subprocess
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M59 = load(
    "m59_for_m63",
    HERE.parent.parent / "cycle-13" / "mission-M59-fixed-join-tree-internal-redteam" / "fixed_tree_dp_bucket_audit.py",
)
M60 = load(
    "m60_for_m63",
    HERE.parent.parent / "cycle-13" / "mission-M60-fixed-tree-leaf-cell-expansion" / "leaf_cell_audit.py",
)


def fraction_text(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def join_tree(n, all_edges, word):
    dsu = M59.DSU(n)
    joins = []
    for idx in word:
        a, b = all_edges[idx]
        if dsu.find(a) != dsu.find(b):
            dsu.union(a, b)
            joins.append((a, b))
    return tuple(sorted(joins))


def embed_base(base, n: int, v: int, all_edges):
    remaining = [x for x in range(n) if x != v]
    small_edges = M59.edges(n - 1)
    big_index = {e: i for i, e in enumerate(all_edges)}
    return tuple(
        big_index[tuple(sorted((remaining[small_edges[idx][0]], remaining[small_edges[idx][1]])))]
        for idx in base
    )


def block_fibers(n: int, all_edges):
    answer = {}
    for r in (3, 4, 5):
        grouped = defaultdict(list)
        for block in itertools.product(range(len(all_edges)), repeat=r):
            grouped[M59.evaluate(n, all_edges, block)].append(tuple(block))
        answer[r] = {g: tuple(values) for g, values in grouped.items()}
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    n = 5
    m = 8
    all_edges = M59.edges(n)
    edge_index = {e: i for i, e in enumerate(all_edges)}
    tree = M59.tree_shapes()["path"]
    words, _cache = M59.enumerate_fixed_tree(n, tree, all_edges)
    word_set = set(words)
    leaves = M59.tree_leaves(n, tree)
    if leaves != [3, 4]:
        raise AssertionError(leaves)

    core = {
        word: M60.delete_original_labels(word, n, tuple(sorted(leaves, reverse=True)))
        for word in words
    }
    core_counts = Counter(core.values())
    keys = sorted(core_counts)
    selected = None
    for subset in itertools.combinations(keys, 4):
        if sum(core_counts[key] for key in subset) == len(words) // 2:
            selected = tuple(subset)
            break
    if selected is None:
        raise AssertionError(core_counts)
    selected_set = set(selected)
    A = {word for word in words if core[word] in selected_set}
    if len(A) != 3904:
        raise AssertionError(len(A))

    v = leaves[0]
    f = next(edge for edge in tree if v in edge)
    u = f[0] if f[1] == v else f[1]
    f_idx = edge_index[f]
    remaining = [x for x in range(n) if x != v]
    s = tuple(remaining[:2])
    s_idx = edge_index[tuple(sorted(s))]

    cells = defaultdict(set)
    for word in words:
        base, _nulls = M60.delete_strand(word, all_edges, n, v)
        cells[base].add(word)
    Z = set()
    for base, cell in cells.items():
        hits = cell & A
        if hits and hits != cell:
            raise AssertionError(("core cut not cell saturated", base, len(hits), len(cell)))
        if hits:
            Z.add(base)

    E = set()
    hubs = set()
    alternate_targets = set()
    for base in Z:
        embedded = embed_base(base, n, v, all_edges)
        hub = embedded + (f_idx, f_idx)
        exterior = embedded + (s_idx, s_idx)
        if hub not in A or exterior in word_set:
            raise AssertionError((base, hub in A, exterior in word_set))
        if M59.evaluate(n, all_edges, exterior) != tuple(range(n)):
            raise AssertionError("exterior target not identity")
        hubs.add(hub)
        E.add(exterior)
        for a in remaining:
            if a == u:
                continue
            g_idx = edge_index[tuple(sorted((v, a)))]
            target = embedded + (g_idx, g_idx)
            if target in A or target in E:
                raise AssertionError(("alternate target absorbed", base, a))
            if join_tree(n, all_edges, target) == tuple(sorted(tree)):
                raise AssertionError(("alternate target kept path tree", base, a))
            alternate_targets.add(target)

    if len(E) != len(Z) or len(hubs) != len(Z) or len(alternate_targets) != (n - 2) * len(Z):
        raise AssertionError((len(Z), len(E), len(hubs), len(alternate_targets)))
    C = A | E
    if len(C) != len(A) + len(E):
        raise AssertionError("A/E overlap")

    fibers = block_fibers(n, all_edges)
    boundary_by_r = {r: Fraction(0) for r in (3, 4, 5)}
    boundary_category = defaultdict(lambda: Fraction(0))
    for word in C:
        for r in (3, 4, 5):
            outer = Fraction(1, 6 * (m - r + 1))
            for position in range(m - r + 1):
                product = M59.evaluate(n, all_edges, word[position : position + r])
                options = fibers[r][product]
                outcome_weight = outer / len(options)
                for block in options:
                    target = word[:position] + block + word[position + r :]
                    if target in C:
                        continue
                    boundary_by_r[r] += outcome_weight
                    target_tree = join_tree(n, all_edges, target)
                    if len(target_tree) == n - 1:
                        category = "minimal_full_support"
                    else:
                        support = set()
                        for idx in target:
                            support.update(all_edges[idx])
                        category = f"exterior_support_size_{len(support)}"
                    boundary_category[(r, category)] += outcome_weight

    omega = M59.identity_word_count(n, all_edges, m)
    total_boundary = sum(boundary_by_r.values(), Fraction(0))
    escape = total_boundary / len(C)
    stationary_mass = Fraction(len(C), omega)
    if 2 * len(C) > omega:
        raise AssertionError("unexpected mass orientation")

    D = (3 * n * n + n - 12) // 2
    Lambda = (m * (m - 1) // 2) * (n - 1) ** 2
    proved_bound = Fraction(n - 2, 6 * (m - 2) * D * (Lambda + 1))
    if escape < proved_bound:
        raise AssertionError((escape, proved_bound))

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
        "convention": "(pq)(x)=p(q(x)); append by swapping domain entries",
        "kernel": "literal lazy K; each outcome has weight 1/[6(m-r+1)|F_r(g)|]",
        "claim_tested": "The smallest specified-target halo is injective, proper, and its exact full-K escape exceeds the universal alternate-leaf-square lower bound.",
        "scope_warning": "This exact N=5 result can falsify the injection/normalization but cannot prove the universal theorem.",
        "N": n,
        "m": m,
        "omega": omega,
        "tree_edges": [list(edge) for edge in tree],
        "leaves": leaves,
        "chosen_leaf": v,
        "leaf_neighbor": u,
        "fixed_exterior_square": list(s),
        "core_distribution": [
            {"core_word": list(key), "count": core_counts[key], "selected": key in selected_set}
            for key in keys
        ],
        "A_size": len(A),
        "Z_size": len(Z),
        "cell_size_bound_Lambda": Lambda,
        "E_size": len(E),
        "C_size": len(C),
        "C_stationary_mass": fraction_text(stationary_mass),
        "alternate_full_support_targets": len(alternate_targets),
        "boundary_flow_over_pi_by_r": {
            str(r): fraction_text(boundary_by_r[r] / len(C)) for r in (3, 4, 5)
        },
        "boundary_flow_over_pi_by_category": [
            {"r": r, "category": category, "escape_contribution": fraction_text(value / len(C))}
            for (r, category), value in sorted(boundary_category.items())
        ],
        "exact_escape": fraction_text(escape),
        "universal_proved_bound_at_N5": fraction_text(proved_bound),
        "elapsed_seconds_before_write": time.perf_counter() - started,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "A": len(A),
        "Z": len(Z),
        "E": len(E),
        "C": len(C),
        "escape": fraction_text(escape),
        "bound": fraction_text(proved_bound),
        "elapsed": payload["elapsed_seconds_before_write"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
