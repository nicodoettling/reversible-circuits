#!/usr/bin/env python3
"""Exact optimized falsifier for Lorentzian-to-heat-bath parking flow."""

from __future__ import annotations

import argparse
import heapq
import itertools
import json
import platform
import subprocess
from collections import Counter, defaultdict, deque
from fractions import Fraction
from functools import lru_cache
from pathlib import Path


Partition = tuple[tuple[int, ...], ...]
Macro = tuple[int, ...]


def normalize(blocks: list[set[int]]) -> Partition:
    return tuple(sorted(tuple(sorted(block)) for block in blocks))


@lru_cache(maxsize=None)
def inverse_chain(a: tuple[int, ...]) -> tuple[Partition, ...]:
    """Stanley's maximal NC chain for a zero-based parking function."""
    r = len(a)
    if r == 0:
        return (((0,),),)
    largest = max(a)
    s = max(i for i, value in enumerate(a) if value == largest)
    smaller = inverse_chain(a[:s] + a[s + 1 :])
    new_vertex = largest + 1

    def relabel(partition: Partition) -> list[set[int]]:
        return [
            {x if x <= largest else x + 1 for x in block}
            for block in partition
        ]

    chain: list[Partition] = []
    for new_rank in range(r + 1):
        if new_rank <= s:
            blocks = relabel(smaller[new_rank])
            blocks.append({new_vertex})
        else:
            blocks = relabel(smaller[new_rank - 1])
            target = next(i for i, block in enumerate(blocks) if largest in block)
            blocks[target].add(new_vertex)
        chain.append(normalize(blocks))
    return tuple(chain)


def cover_label(before: Partition, after: Partition) -> int:
    old = [set(block) for block in before]
    new = [set(block) for block in after]
    merged = next(
        block for block in new
        if sum(piece <= block for piece in old) == 2
    )
    pieces = [piece for piece in old if piece <= merged]
    if len(pieces) != 2 or pieces[0] | pieces[1] != merged:
        raise AssertionError("not a two-block cover")
    left, right = pieces
    if min(left) > min(right):
        left, right = right, left
    right_minimum = min(right)
    eligible = [x for x in left if x < right_minimum]
    if not eligible:
        raise AssertionError("Stanley cover label is undefined")
    return max(eligible)


def chain_labels(chain: tuple[Partition, ...]) -> tuple[int, ...]:
    return tuple(
        cover_label(chain[k - 1], chain[k])
        for k in range(1, len(chain))
    )


def is_noncrossing(partition: Partition) -> bool:
    block_of = {}
    for block_index, block in enumerate(partition):
        for vertex in block:
            block_of[vertex] = block_index
    vertices = sorted(block_of)
    for a, b, c, d in itertools.combinations(vertices, 4):
        if (
            block_of[a] == block_of[c]
            and block_of[b] == block_of[d]
            and block_of[a] != block_of[b]
        ):
            return False
    return True


def intermediate_partitions(lower: Partition, upper: Partition) -> tuple[Partition, ...]:
    blocks = [set(block) for block in lower]
    upper_blocks = [set(block) for block in upper]
    candidates: set[Partition] = set()
    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            merged = blocks[i] | blocks[j]
            if not any(merged <= block for block in upper_blocks):
                continue
            rest = [
                block
                for k, block in enumerate(blocks)
                if k not in (i, j)
            ]
            rest.append(merged)
            candidate = normalize(rest)
            if is_noncrossing(candidate):
                candidates.add(candidate)
    answer = tuple(sorted(candidates))
    if len(answer) not in (2, 3):
        raise AssertionError(f"rank-two NC interval has size {len(answer)}")
    return answer


def is_parking(a: tuple[int, ...]) -> bool:
    b = sorted(a)
    return all(value <= rank for rank, value in enumerate(b))


def parking_sequences(r: int):
    for a in itertools.product(range(r), repeat=r):
        if is_parking(a):
            yield a


def feasible_macros(r: int) -> list[Macro]:
    return [
        b
        for b in itertools.combinations_with_replacement(range(r), r)
        if all(value <= rank for rank, value in enumerate(b))
    ]


def ideal_edges(macro: Macro) -> dict[Macro, Fraction]:
    r = len(macro)
    counts = Counter(macro)
    result: dict[Macro, Fraction] = defaultdict(Fraction)
    for source_type, multiplicity in counts.items():
        eta = list(macro)
        eta.remove(source_type)
        feasible = []
        for destination in range(r):
            target = tuple(sorted(eta + [destination]))
            if all(value <= rank for rank, value in enumerate(target)):
                feasible.append((destination, target))
        for destination, target in feasible:
            if target != macro:
                result[target] += Fraction(multiplicity, r * len(feasible))
    return dict(result)


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def run(n: int) -> dict:
    r = n - 1
    macros = feasible_macros(r)
    macro_sizes: Counter[Macro] = Counter()
    # Integer flow scale: interval size two contributes 3, size three 2.
    flow_weight: dict[Macro, Counter[Macro]] = defaultdict(Counter)
    raw_count = 0
    label_failures = []
    interval_histogram: Counter[int] = Counter()

    for a in parking_sequences(r):
        raw_count += 1
        chain = inverse_chain(a)
        recovered = chain_labels(chain)
        if recovered != a:
            label_failures.append([list(a), list(recovered)])
            if len(label_failures) >= 10:
                raise AssertionError("Stanley inverse label failure")
        source = tuple(sorted(a))
        macro_sizes[source] += 1
        for rank in range(1, r):
            candidates = intermediate_partitions(chain[rank - 1], chain[rank + 1])
            interval_histogram[len(candidates)] += 1
            weight = 6 // len(candidates)
            for middle in candidates:
                target_chain = chain[:rank] + (middle,) + chain[rank + 1 :]
                target = tuple(sorted(chain_labels(target_chain)))
                flow_weight[source][target] += weight

    expected = n ** (n - 2)
    if raw_count != expected:
        raise AssertionError((n, raw_count, expected))
    if set(macro_sizes) != set(macros):
        raise AssertionError("macro support mismatch")
    if label_failures:
        raise AssertionError("inverse labels did not reproduce parking functions")

    detailed_balance_failures = []
    adjacency: dict[Macro, set[Macro]] = {macro: set() for macro in macros}
    projected_rate: dict[tuple[Macro, Macro], Fraction] = {}
    for source in macros:
        row = Fraction()
        for target, weight in flow_weight[source].items():
            rate = Fraction(weight, 6 * (r - 1) * macro_sizes[source])
            projected_rate[(source, target)] = rate
            row += rate
            if source != target and rate:
                adjacency[source].add(target)
            if flow_weight[source][target] != flow_weight[target][source]:
                detailed_balance_failures.append(
                    [list(source), list(target), flow_weight[source][target],
                     flow_weight[target][source]]
                )
        if row != 1:
            raise AssertionError(("row sum", source, row))
    if detailed_balance_failures:
        raise AssertionError(
            f"stationary projected flow is not symmetric: "
            f"{detailed_balance_failures[:3]}"
        )

    def distances(source: Macro) -> dict[Macro, int]:
        dist = {source: 0}
        queue = deque([source])
        while queue:
            here = queue.popleft()
            for there in adjacency[here]:
                if there not in dist:
                    dist[there] = dist[here] + 1
                    queue.append(there)
        return dist

    distance_cache = {macro: distances(macro) for macro in macros}

    def widest_paths(source: Macro):
        upper = Fraction(raw_count + 1)
        best: dict[Macro, Fraction] = {source: upper}
        parent: dict[Macro, Macro | None] = {source: None}
        heap: list[tuple[Fraction, Macro]] = [(-upper, source)]
        while heap:
            negative_capacity, here = heapq.heappop(heap)
            capacity = -negative_capacity
            if capacity != best[here]:
                continue
            for there in adjacency[here]:
                edge_capacity = Fraction(
                    flow_weight[here][there], 6 * (r - 1)
                )
                candidate = min(capacity, edge_capacity)
                if candidate > best.get(there, Fraction()):
                    best[there] = candidate
                    parent[there] = here
                    heapq.heappush(heap, (-candidate, there))
        return best, parent

    widest_cache = {macro: widest_paths(macro) for macro in macros}
    ideal_balance_failures = []
    ideal_records = []
    worst_ratio: Fraction | None = None
    worst_record = None
    max_distance = 0
    max_widest_path_length = 0
    minimum_widest_ratio: Fraction | None = None
    worst_widest_record = None
    missing_two_hop = []
    for source in macros:
        for target, d_rate in ideal_edges(source).items():
            reverse = ideal_edges(target).get(source, Fraction())
            lhs = macro_sizes[source] * d_rate
            rhs = macro_sizes[target] * reverse
            if lhs != rhs:
                ideal_balance_failures.append(
                    [list(source), list(target), str(lhs), str(rhs)]
                )
            distance = distance_cache[source].get(target)
            if distance is None:
                raise AssertionError("actual projection disconnected")
            max_distance = max(max_distance, distance)
            ideal_flow_scaled = macro_sizes[source] * d_rate

            candidates: list[tuple[Fraction, Macro | None, int]] = []
            direct_weight = flow_weight[source][target]
            if direct_weight:
                actual_scaled = Fraction(direct_weight, 6 * (r - 1))
                candidates.append((actual_scaled / ideal_flow_scaled, None, 1))
            for middle in adjacency[source]:
                if target not in adjacency[middle]:
                    continue
                cap1 = Fraction(flow_weight[source][middle], 6 * (r - 1))
                cap2 = Fraction(flow_weight[middle][target], 6 * (r - 1))
                candidates.append((min(cap1, cap2) / ideal_flow_scaled, middle, 2))
            if not candidates:
                missing_two_hop.append([list(source), list(target), distance])
                best_ratio = Fraction(0)
                middle = None
                path_length = distance
            else:
                best_ratio, middle, path_length = max(candidates, key=lambda x: x[0])
            widest_capacities, widest_parents = widest_cache[source]
            widest_ratio = widest_capacities[target] / ideal_flow_scaled
            widest_path = []
            cursor: Macro | None = target
            while cursor is not None:
                widest_path.append(cursor)
                cursor = widest_parents[cursor]
            widest_path.reverse()
            widest_path_length = len(widest_path) - 1
            max_widest_path_length = max(
                max_widest_path_length, widest_path_length
            )
            record = {
                "source": list(source),
                "target": list(target),
                "ideal_rate": str(d_rate),
                "actual_graph_distance": distance,
                "best_route_length_at_most_two": path_length,
                "best_middle": list(middle) if middle is not None else None,
                "best_min_capacity_over_ideal_flow": str(best_ratio),
                "best_ratio_float": float(best_ratio),
                "widest_path": [list(item) for item in widest_path],
                "widest_path_length": widest_path_length,
                "widest_min_capacity_over_ideal_flow": str(widest_ratio),
                "widest_ratio_float": float(widest_ratio),
            }
            ideal_records.append(record)
            if worst_ratio is None or best_ratio < worst_ratio:
                worst_ratio = best_ratio
                worst_record = record
            if minimum_widest_ratio is None or widest_ratio < minimum_widest_ratio:
                minimum_widest_ratio = widest_ratio
                worst_widest_record = record

    if ideal_balance_failures:
        raise AssertionError("ideal chain detailed balance failed")

    ideal_records.sort(key=lambda row: row["best_ratio_float"])
    return {
        "n": n,
        "r": r,
        "raw_factorization_count": raw_count,
        "denes_expected": expected,
        "macro_count": len(macros),
        "inverse_label_failures": label_failures,
        "rank_two_interval_histogram": dict(sorted(interval_histogram.items())),
        "projected_detailed_balance_failures": detailed_balance_failures,
        "ideal_detailed_balance_failures": ideal_balance_failures,
        "ideal_directed_edge_count": len(ideal_records),
        "maximum_actual_distance_of_ideal_edge": max_distance,
        "missing_length_at_most_two_routes": missing_two_hop,
        "minimum_best_capacity_ratio": str(worst_ratio),
        "minimum_best_capacity_ratio_float": float(worst_ratio or 0),
        "worst_capacity_record": worst_record,
        "maximum_widest_path_length": max_widest_path_length,
        "minimum_widest_capacity_ratio": str(minimum_widest_ratio),
        "minimum_widest_capacity_ratio_float": float(
            minimum_widest_ratio or 0
        ),
        "worst_widest_capacity_record": worst_widest_record,
        "twenty_worst_capacity_records": ideal_records[:20],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()
    if not 3 <= args.n_max <= 8:
        raise SystemExit("exact range is 3<=n-max<=8")
    result = {
        "claim_tested": (
            "Every Lorentzian ideal parking edge has an actual projected "
            "route of length at most two with inverse-polynomial capacity loss."
        ),
        "finite_scope_warning": (
            "A missing route refutes the two-hop claim. Positive finite "
            "instances do not prove a universal path or congestion theorem."
        ),
        "convention": "(pq)(x)=p(q(x)); factor products left-to-right",
        "actual_kernel": (
            "nonlazy uniform scan of exact adjacent rank-two heat baths in "
            "minimal long-cycle factorizations"
        ),
        "ideal_kernel": (
            "delete a uniformly chosen coordinate and reinsert uniformly "
            "among feasible parking values"
        ),
        "seed": None,
        "python": platform.python_version(),
        "repository_commit": git_commit(),
        "records": [run(n) for n in range(3, args.n_max + 1)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not args.quiet:
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
