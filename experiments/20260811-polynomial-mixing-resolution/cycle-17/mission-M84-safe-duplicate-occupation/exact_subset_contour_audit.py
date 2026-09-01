#!/usr/bin/env python3
"""Exhaustive subset/contour audit for the 16-factor base word W_1.

Every one of the 2^16 selected-label subsets and every unselected pair is
checked.  This is a finite validation of the static subset formula and the
collision-contour safety criterion; it is not the all-L proof.
"""

from __future__ import annotations

import argparse
import functools
import itertools
import json
import math
import platform
import subprocess
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

from collision_contour_audit import contour_record
from subset_tail_audit import connected, lifted_word, stable_residual


sys.dont_write_bytecode = True


def components(edges, n: int):
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        aa, bb = find(a), find(b)
        if aa != bb:
            parent[bb] = aa
    blocks = defaultdict(list)
    for x in range(n):
        blocks[find(x)].append(x)
    return tuple(sorted(tuple(block) for block in blocks.values()))


def audit():
    L = 1
    word = lifted_word(L)
    n = 8
    k = len(word)
    full_mask = (1 << k) - 1
    residuals = {}
    selected_components = {}
    started = time.perf_counter()
    for mask in range(1 << k):
        selected = frozenset(i for i in range(k) if mask >> i & 1)
        residuals[mask] = stable_residual(word, selected, n)
        selected_components[mask] = components(
            (word[i] for i in selected), n
        )

    duplicate_count = 0
    safe_count = 0
    equivalence_failures = []
    residual_formula_failures = []
    outside_safety = defaultdict(set)
    homology_histogram = Counter()
    path_length_histogram = Counter()
    max_abs_voltage = 0
    safe_pair_masks = defaultdict(set)

    # Independently check that each residual has the advertised component
    # partition invariance under two opposite extraction orders.
    def conjugate(edge, pivot):
        p, q = pivot

        def act(x):
            return q if x == p else p if x == q else x

        return tuple(sorted((act(edge[0]), act(edge[1]))))

    def eliminate(order):
        values = list(word)
        labels = list(range(k))
        outputs = []
        for wanted in order:
            position = labels.index(wanted)
            pivot = values[position]
            outputs.append(pivot)
            values = (
                [conjugate(edge, pivot) for edge in values[:position]]
                + values[position + 1 :]
            )
            labels = labels[:position] + labels[position + 1 :]
        return tuple(outputs), dict(zip(labels, values))

    for mask in range(1 << k):
        selected_tuple = tuple(i for i in range(k) if mask >> i & 1)
        if len(selected_tuple) <= 8:  # 39203 subsets; both orders checked.
            for order in (selected_tuple, tuple(reversed(selected_tuple))):
                outputs, residual = eliminate(order)
                if residual != residuals[mask]:
                    residual_formula_failures.append({
                        "mask": mask,
                        "order": list(order),
                        "kind": "residual",
                    })
                    break
                if components(outputs, n) != selected_components[mask]:
                    residual_formula_failures.append({
                        "mask": mask,
                        "order": list(order),
                        "kind": "prefix-components",
                    })
                    break

        residual = residuals[mask]
        unselected = tuple(i for i in range(k) if not (mask >> i & 1))
        for i, j in itertools.combinations(unselected, 2):
            if residual[i] != residual[j]:
                continue
            duplicate_count += 1
            enlarged_mask = mask | (1 << i) | (1 << j)
            remaining_edges = itertools.chain(
                (word[label] for label in range(k) if mask >> label & 1),
                residuals[enlarged_mask].values(),
            )
            is_safe = connected(remaining_edges, n)
            safe_count += is_safe
            if is_safe:
                safe_pair_masks[mask].add((i, j))
            record = contour_record(
                1,
                tuple(label for label in range(k) if mask >> label & 1),
                (i, j),
            )
            homology = tuple(record["contour_homology"])
            homology_histogram[str(homology)] += 1
            lengths = tuple(record["path_lengths"])
            path_length_histogram[str(lengths)] += 1
            max_abs_voltage = max(
                max_abs_voltage,
                *(abs(x) for x in record["contour_integer_voltage"]),
            )
            if is_safe != (homology != (0, 0)) and len(equivalence_failures) < 100:
                equivalence_failures.append({
                    "mask": mask,
                    "pair": [i, j],
                    "safe": is_safe,
                    "record": record,
                })
            between_mask = sum(
                1 << label
                for label in range(i + 1, j)
                if mask >> label & 1
            )
            outside_safety[(i, j, between_mask)].add(is_safe)

    outside_invariance_failures = [
        {
            "pair": [key[0], key[1]],
            "between_mask": key[2],
            "safe_values": sorted(values),
        }
        for key, values in outside_safety.items()
        if len(values) != 1
    ]

    @functools.lru_cache(maxsize=None)
    def hit_count(mask: int, last: int) -> int:
        remaining_count = k - mask.bit_count()
        if remaining_count == 0:
            return 0
        total = 0
        preliminary = mask ^ (1 << last) if last >= 0 else None
        for label in range(k):
            if mask >> label & 1:
                continue
            if last >= 0 and tuple(sorted((last, label))) in safe_pair_masks[preliminary]:
                total += math.factorial(remaining_count - 1)
            else:
                total += hit_count(mask | (1 << label), label)
        return total

    exact_hits = hit_count(0, -1)
    return {
        "L": 1,
        "n": n,
        "k": k,
        "selected_subset_count": 1 << k,
        "duplicate_subset_pair_count": duplicate_count,
        "safe_subset_pair_count": safe_count,
        "homology_histogram": dict(sorted(homology_histogram.items())),
        "path_length_histogram": dict(sorted(path_length_histogram.items())),
        "maximum_absolute_contour_voltage_coordinate": max_abs_voltage,
        "safe_iff_nonzero_homology_failure_count": len(equivalence_failures),
        "safe_iff_nonzero_homology_failures": equivalence_failures,
        "outside_selection_invariance_failure_count": len(outside_invariance_failures),
        "outside_selection_invariance_failures": outside_invariance_failures[:100],
        "residual_and_prefix_partition_check_subset_scope": "all masks of size <=8; increasing and decreasing orders",
        "residual_or_prefix_partition_failure_count": len(residual_formula_failures),
        "residual_or_prefix_partition_failures": residual_formula_failures[:100],
        "exact_full_order_hit_count": exact_hits,
        "exact_full_order_count": math.factorial(k),
        "exact_full_order_hit_probability": exact_hits / math.factorial(k),
        "hit_count_cache": hit_count.cache_info()._asdict(),
        "elapsed_seconds": time.perf_counter() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "argv": sys.argv,
        "commit": commit,
        "python": platform.python_version(),
        "seed": None,
        "nonstandard_dependencies": {},
        "method": (
            "Exhaustive all-subset/all-unselected-pair audit on W_1, plus "
            "exact memoized counting of full elimination orders."
        ),
        "scope_warning": (
            "Finite exhaustive validation of the base word does not replace "
            "the all-L collision-contour and voltage proof."
        ),
        "result": audit(),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["result"], sort_keys=True))


if __name__ == "__main__":
    main()
