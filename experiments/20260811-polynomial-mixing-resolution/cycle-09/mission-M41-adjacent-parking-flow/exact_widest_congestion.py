#!/usr/bin/env python3
"""Exact simultaneous-load audit for a named adjacent parking flow.

For each adjacent-value ideal commodity, choose a deterministic
capacity-maximizing path in the actual parking-macro projection.  This can
falsify that named routing rule.  Finite success is not a universal flow
theorem.
"""

from __future__ import annotations

import argparse
import heapq
import importlib.util
import itertools
import json
import platform
import subprocess
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


Macro = tuple[int, ...]


def load_base():
    repo = Path(__file__).resolve().parents[4]
    path = (
        repo
        / "experiments/20260811-polynomial-mixing-resolution"
        / "cycle-08/mission-M35-general-parking-flow"
        / "adjacent_bypass_probe.py"
    )
    spec = importlib.util.spec_from_file_location("m35_adjacent_base", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE = load_base()


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def ideal_rate(source: Macro, target: Macro, macros: set[Macro]) -> Fraction:
    """Exact M36 delete/reinsert rate for one off-diagonal macro edge."""
    r = len(source)
    source_counts = Counter(source)
    target_counts = Counter(target)
    removed = [i for i in range(r) if source_counts[i] > target_counts[i]]
    added = [i for i in range(r) if target_counts[i] > source_counts[i]]
    if len(removed) != 1 or len(added) != 1:
        raise AssertionError("not a unit exchange")
    i = removed[0]
    residual = list(source)
    residual.remove(i)
    feasible = 0
    for j in range(r):
        proposal = tuple(sorted(residual + [j]))
        feasible += proposal in macros
    if not feasible:
        raise AssertionError("no feasible reinsertion")
    return Fraction(source_counts[i], r * feasible)


def build_instance(n: int):
    """Build the exact projected actual chain, reusing M35's audited maps."""
    r = n - 1
    identity = tuple(range(n))
    cycle = tuple(list(range(1, n)) + [0])
    edges = [(a, b) for a in range(n) for b in range(a + 1, n)]
    edge_index = {edge: i for i, edge in enumerate(edges)}
    perms = [BASE.transposition(n, edge) for edge in edges]

    pair_fibers = defaultdict(list)
    for i, p in enumerate(perms):
        for j, q in enumerate(perms):
            pair_fibers[BASE.compose(p, q)].append((i, j))

    macro_words = defaultdict(list)
    seen_words = set()
    for labels in itertools.product(range(r), repeat=r):
        if not BASE.is_parking_word(labels):
            continue
        word_edges = BASE.factor_word(BASE.inverse_chain(labels))
        word = tuple(edge_index[edge] for edge in word_edges)
        product = identity
        for index in word:
            product = BASE.compose(product, perms[index])
        if product != cycle:
            raise AssertionError("wrong endpoint")
        if tuple(edge[0] for edge in word_edges) != labels:
            raise AssertionError("wrong Stanley labels")
        if word in seen_words:
            raise AssertionError("inverse map not injective")
        seen_words.add(word)
        macro_words[tuple(sorted(labels))].append(word)

    if len(seen_words) != n ** (n - 2):
        raise AssertionError("Dénes count mismatch")
    for macro, words in macro_words.items():
        if len(words) != BASE.orbit_weight(macro):
            raise AssertionError("orbit-weight mismatch")

    rates = defaultdict(Fraction)
    for source, words in macro_words.items():
        total = defaultdict(Fraction)
        for word in words:
            for pos in range(r - 1):
                product = BASE.compose(perms[word[pos]], perms[word[pos + 1]])
                fiber = pair_fibers[product]
                increment = Fraction(1, (r - 1) * len(fiber))
                for first, second in fiber:
                    target_word = word[:pos] + (first, second) + word[pos + 2 :]
                    target = tuple(
                        sorted(edges[index][0] for index in target_word)
                    )
                    if not BASE.is_macro(target):
                        raise AssertionError("infeasible target macro")
                    total[target] += increment
        for target, value in total.items():
            rates[source, target] = value / len(words)

    macros = set(macro_words)
    adjacency = {macro: [] for macro in macros}
    capacities = {}
    for (source, target), rate in rates.items():
        if source == target or not rate:
            continue
        capacity = BASE.orbit_weight(source) * rate
        reverse = BASE.orbit_weight(target) * rates[target, source]
        if capacity != reverse:
            raise AssertionError("projected detailed balance failure")
        capacities[source, target] = capacity
        adjacency[source].append(target)
    for source in adjacency:
        adjacency[source].sort()
    return macros, adjacency, capacities, len(seen_words)


def widest_tree(source: Macro, adjacency, capacities):
    upper = sum(capacities.values(), Fraction()) + 1
    best = {source: upper}
    parent: dict[Macro, Macro | None] = {source: None}
    heap = [(-upper, source)]
    while heap:
        negative, here = heapq.heappop(heap)
        value = -negative
        if best.get(here) != value:
            continue
        for there in adjacency[here]:
            candidate = min(value, capacities[here, there])
            if candidate > best.get(there, Fraction()):
                best[there] = candidate
                parent[there] = here
                heapq.heappush(heap, (-candidate, there))
    return best, parent


def recover_path(source: Macro, target: Macro, parent):
    path = []
    cursor: Macro | None = target
    while cursor is not None:
        path.append(cursor)
        cursor = parent[cursor]
    path.reverse()
    if not path or path[0] != source:
        raise AssertionError("path recovery failed")
    return path


def duplicate_buffer_candidates(
    source: Macro, target: Macro, capacities
) -> list[tuple[int, list[Macro]]]:
    """All positive borrow--move--return paths for one adjacent exchange."""
    r = len(source)
    source_counts = Counter(source)
    target_counts = Counter(target)
    removed = next(
        i for i in range(r) if source_counts[i] > target_counts[i]
    )
    added = next(
        i for i in range(r) if target_counts[i] > source_counts[i]
    )
    reverse = added < removed
    right_source = target if reverse else source
    right_target = source if reverse else target
    i = min(removed, added)
    counts = Counter(right_source)
    answer = []
    for h in range(i + 1):
        if counts[h] < 2:
            continue
        if h == i:
            path = [right_source, right_target]
        else:
            z_list = list(right_source)
            z_list.remove(h)
            z_list.append(i)
            z = tuple(sorted(z_list))
            w_list = list(z)
            w_list.remove(i)
            w_list.append(i + 1)
            w = tuple(sorted(w_list))
            path = [right_source, z, w, right_target]
        if reverse:
            path = path[::-1]
        if all(edge in capacities for edge in zip(path, path[1:])):
            answer.append((h, path))
    return answer


def run(n: int) -> dict:
    r = n - 1
    macros, adjacency, capacities, raw_count = build_instance(n)
    ideal_edges = BASE.adjacent_ideal_edges(macros)
    trees = {source: widest_tree(source, adjacency, capacities)
             for source in {edge[0] for edge in ideal_edges}}

    edge_load = defaultdict(Fraction)
    records = []
    minimum_ratio = None
    maximum_length = 0
    for source, target in ideal_edges:
        rate = ideal_rate(source, target, macros)
        flow = BASE.orbit_weight(source) * rate
        best, parent = trees[source]
        path = recover_path(source, target, parent)
        length = len(path) - 1
        maximum_length = max(maximum_length, length)
        bottleneck = min(
            capacities[path[k], path[k + 1]] for k in range(length)
        )
        ratio = bottleneck / flow
        if minimum_ratio is None or ratio < minimum_ratio:
            minimum_ratio = ratio
        for k in range(length):
            edge_load[path[k], path[k + 1]] += flow * length
        records.append(
            {
                "source": list(source),
                "target": list(target),
                "ideal_rate": str(rate),
                "ideal_flow_scaled": str(flow),
                "path": [list(item) for item in path],
                "path_length": length,
                "bottleneck_over_ideal_flow": str(ratio),
            }
        )

    congestions = {
        edge: load / capacities[edge] for edge, load in edge_load.items()
    }
    worst_edge = max(congestions, key=congestions.get)
    worst = congestions[worst_edge]
    warning_records = []
    for a in range(2, r):
        b = r - a - 1
        if b < 1:
            continue
        source = (0,) * a + (1,) + (2,) * b
        target = (0,) * a + (2,) * (b + 1)
        match = next(
            (
                record for record in records
                if record["source"] == list(source)
                and record["target"] == list(target)
            ),
            None,
        )
        if match is not None:
            warning_records.append({"a": a, "b": b, **match})

    duplicate_load = defaultdict(Fraction)
    duplicate_missing = []
    duplicate_minimum_ratio = None
    duplicate_maximum_length = 0
    for source, target in ideal_edges:
        rate = ideal_rate(source, target, macros)
        flow = BASE.orbit_weight(source) * rate
        candidates = duplicate_buffer_candidates(source, target, capacities)
        if not candidates:
            duplicate_missing.append([list(source), list(target)])
            continue
        scored = []
        for h, path in candidates:
            bottleneck = min(
                capacities[edge] for edge in zip(path, path[1:])
            )
            scored.append((bottleneck / flow, -h, path))
        ratio, _, path = max(scored)
        if duplicate_minimum_ratio is None or ratio < duplicate_minimum_ratio:
            duplicate_minimum_ratio = ratio
        length = len(path) - 1
        duplicate_maximum_length = max(duplicate_maximum_length, length)
        for edge in zip(path, path[1:]):
            duplicate_load[edge] += flow * length
    if duplicate_load:
        duplicate_congestions = {
            edge: load / capacities[edge]
            for edge, load in duplicate_load.items()
        }
        duplicate_worst_edge = max(
            duplicate_congestions, key=duplicate_congestions.get
        )
        duplicate_worst = duplicate_congestions[duplicate_worst_edge]
    else:
        duplicate_worst_edge = None
        duplicate_worst = Fraction()

    return {
        "n": n,
        "r": r,
        "raw_factorization_count": raw_count,
        "macro_count": len(macros),
        "actual_directed_edge_count": len(capacities),
        "adjacent_ideal_directed_edge_count": len(ideal_edges),
        "maximum_widest_path_length": maximum_length,
        "minimum_individual_widest_capacity_ratio": str(minimum_ratio),
        "deterministic_widest_path_total_congestion": str(worst),
        "worst_loaded_directed_edge": [
            list(worst_edge[0]),
            list(worst_edge[1]),
        ],
        "warning_family_records": warning_records,
        "duplicate_buffer_missing_edges": duplicate_missing,
        "duplicate_buffer_minimum_capacity_ratio": str(
            duplicate_minimum_ratio
        ),
        "duplicate_buffer_maximum_path_length": duplicate_maximum_length,
        "duplicate_buffer_total_congestion": str(duplicate_worst),
        "duplicate_buffer_worst_loaded_edge": (
            [
                list(duplicate_worst_edge[0]),
                list(duplicate_worst_edge[1]),
            ]
            if duplicate_worst_edge is not None
            else None
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 3 <= args.n_max <= 8:
        raise SystemExit("exact range is 3<=n-max<=8")
    result = {
        "claim_tested": (
            "Deterministically chosen capacity-maximizing paths for every "
            "adjacent-value ideal edge have polynomial simultaneous load; "
            "and every adjacent edge has a three-step duplicate-buffer path."
        ),
        "finite_scope_warning": (
            "A large exact load can refute this named routing rule. Finite "
            "polynomial-looking load cannot prove a universal flow theorem."
        ),
        "convention": "(pq)(x)=p(q(x)); tuple product left-to-right",
        "stationary_scale": (
            "all capacities omit the common factor (r+1)^(-(r-1))"
        ),
        "seed": None,
        "python": platform.python_version(),
        "repository_commit": git_commit(),
        "records": [run(n) for n in range(3, args.n_max + 1)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
