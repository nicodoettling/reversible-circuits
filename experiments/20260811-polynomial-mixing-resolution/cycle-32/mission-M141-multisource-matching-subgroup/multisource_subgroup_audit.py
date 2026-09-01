#!/usr/bin/env python3
"""Deterministic exceptional-rank audit for M141.

The universal d>=5 theorem is proved in ``multisource_subgroup_theorem.md``.
This script tests the accepted M135 matching construction at d=3 and gives
the smallest abstract warning showing why nonabelian simplicity is essential.

The DPS reconstruction is loaded from the frozen, independently accepted
M137 checker after verifying its SHA-256 digest.  No frozen file is modified.
"""

from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import math
import platform
import subprocess
import sys
import time
from collections import Counter, defaultdict, deque
from pathlib import Path


Permutation = tuple[int, ...]
ProductElement = tuple[Permutation, ...]

M137_CHECKER_SHA256 = "bb62d449c7cad72a448389f9f7dd7ee76618e8c71b68189db20e19f4e2244341"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def repository_root() -> Path:
    return Path(__file__).resolve().parents[4]


def load_frozen_m137():
    path = (
        repository_root()
        / "experiments/20260811-polynomial-mixing-resolution/cycle-31"
        / "mission-M137-m135-fresh-referee/independent_referee.py"
    )
    observed = sha256(path)
    assert observed == M137_CHECKER_SHA256, (observed, M137_CHECKER_SHA256)
    spec = importlib.util.spec_from_file_location("frozen_m137_checker", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module, path, observed


def product_multiply(ref, left: ProductElement, right: ProductElement) -> ProductElement:
    return tuple(ref.multiply(a, b) for a, b in zip(left, right))


def generated_multi_group(ref, d: int, words) -> frozenset[ProductElement]:
    width = len(words)
    identity = tuple(range(d))
    one = tuple(identity for _ in range(width))
    generators = tuple(
        tuple(ref.edge_map(d, word[position]) for word in words)
        for position in range(len(words[0]))
    )
    reached = {one}
    queue = deque([one])
    while queue:
        current = queue.popleft()
        for generator in generators:
            nxt = product_multiply(ref, current, generator)
            if nxt not in reached:
                reached.add(nxt)
                queue.append(nxt)
    return frozenset(reached)


def expected_common_parity_size(d: int, width: int) -> int:
    if width == 1:
        return math.factorial(d)
    return 2 * (math.factorial(d) // 2) ** width


def common_parity(ref, element: ProductElement) -> bool:
    return len({ref.sign(p) for p in element}) == 1


def subset_audit(ref, d: int, indices, words) -> dict:
    failures = []
    size_histogram: dict[int, Counter] = defaultdict(Counter)
    for width in range(1, len(indices) + 1):
        expected = expected_common_parity_size(d, width)
        for subset in itertools.combinations(indices, width):
            group = generated_multi_group(ref, d, [words[j] for j in subset])
            size_histogram[width][len(group)] += 1
            if len(group) != expected or not all(common_parity(ref, x) for x in group):
                failures.append(
                    {
                        "subset": list(subset),
                        "observed_order": len(group),
                        "expected_order": expected,
                    }
                )
    return {
        "all_nonempty_subsets_checked": 2 ** len(indices) - 1,
        "order_histogram_by_width": {
            str(width): {str(order): count for order, count in sorted(hist.items())}
            for width, hist in sorted(size_histogram.items())
        },
        "common_parity_group_failures": failures,
    }


def aligned_source_target_comparison(ref, d: int, source_indices, target_indices, words) -> dict:
    assert len(source_indices) == len(target_indices)
    rows = {}
    for width in range(1, len(source_indices) + 1):
        equal = 0
        total = 0
        order_pair_histogram = Counter()
        for positions in itertools.combinations(range(len(source_indices)), width):
            source_group = generated_multi_group(
                ref, d, [words[source_indices[j]] for j in positions]
            )
            target_group = generated_multi_group(
                ref, d, [words[target_indices[j]] for j in positions]
            )
            total += 1
            equal += source_group == target_group
            order_pair_histogram[(len(source_group), len(target_group))] += 1
        rows[str(width)] = {
            "equal_literal_subgroups": equal,
            "subsets": total,
            "order_pair_histogram": {
                f"{a},{b}": count
                for (a, b), count in sorted(order_pair_histogram.items())
            },
        }
    return rows


def audit_actual_rank_three(ref) -> list[dict]:
    d = 3
    words, _index, _fibers, tau = ref.reconstruct_rank(d)
    permutations = tuple(itertools.permutations(range(d)))
    root_group = tuple(p for p in permutations if p[d - 1] == d - 1)
    global_blocks = ref.orbit_blocks(words, permutations)
    root_blocks = ref.orbit_blocks(words, root_group)
    global_key = {
        source: ref.canonical(word, permutations) for source, word in enumerate(words)
    }
    root_key = {
        source: ref.canonical(word, root_group) for source, word in enumerate(words)
    }

    rows = []
    for adjacent_index, target in tau.items():
        edge_rows = []
        representatives = []
        for _hkey, block in sorted(root_blocks.items()):
            target_hkeys = {root_key[target[source]] for source in block}
            assert len(target_hkeys) == 1
            representative = block[0]
            edge_rows.append(
                (global_key[representative], global_key[target[representative]])
            )
            representatives.append(representative)

        colors, left_vertices, right_vertices = ref.decompose_regular_bipartite(
            edge_rows, d
        )
        row = {
            "adjacent_index": adjacent_index + 1,
            "global_orbits": len(global_blocks),
            "matching_colors": [],
        }
        for color in range(d):
            edge_ids = tuple(sorted(edge for edge, c in colors.items() if c == color))
            source_indices = tuple(representatives[edge] for edge in edge_ids)
            target_indices = tuple(target[source] for source in source_indices)
            source_left = [global_key[source] for source in source_indices]
            target_right = [global_key[source] for source in target_indices]
            assert len(source_indices) == len(left_vertices) == len(right_vertices) == 4
            assert len(set(source_left)) == len(source_left)
            assert len(set(target_right)) == len(target_right)

            source_audit = subset_audit(ref, d, source_indices, words)
            target_audit = subset_audit(ref, d, target_indices, words)
            aligned_comparison = aligned_source_target_comparison(
                ref, d, source_indices, target_indices, words
            )
            row["matching_colors"].append(
                {
                    "color": color,
                    "edges": len(edge_ids),
                    "distinct_source_global_orbits": len(set(source_left)),
                    "distinct_target_global_orbits": len(set(target_right)),
                    "source": source_audit,
                    "target": target_audit,
                    "aligned_source_target_comparison_by_width": aligned_comparison,
                }
            )
        rows.append(row)
    return rows


def abstract_rank_three_counterexample(ref) -> dict:
    """Build C_3^(r-1) semidirect common parity for the smallest r=3."""
    d = 3
    r = 3
    permutations = tuple(itertools.permutations(range(d)))
    alternating = tuple(p for p in permutations if ref.sign(p) == 1)
    identity = tuple(range(d))
    transposition = ref.edge_map(d, (0, 1))

    even_kernel = {
        triple
        for triple in itertools.product(alternating, repeat=r)
        if ref.multiply(ref.multiply(triple[0], triple[1]), triple[2]) == identity
    }
    odd_coset = {
        tuple(ref.multiply(a, transposition) for a in triple)
        for triple in even_kernel
    }
    subgroup = frozenset(even_kernel | odd_coset)
    assert len(even_kernel) == 3 ** (r - 1)
    assert len(subgroup) == 2 * 3 ** (r - 1)

    for left in subgroup:
        for right in subgroup:
            assert product_multiply(ref, left, right) in subgroup

    pair_projection_sizes = {}
    for a, b in itertools.combinations(range(r), 2):
        projection = {(element[a], element[b]) for element in subgroup}
        pair_projection_sizes[f"{a + 1},{b + 1}"] = len(projection)

    expected_pair = expected_common_parity_size(d, 2)
    expected_full = expected_common_parity_size(d, r)
    assert set(pair_projection_sizes.values()) == {expected_pair}
    assert len(subgroup) < expected_full
    return {
        "d": d,
        "r": r,
        "description": "kernel x1*x2*x3=id in A3^3, extended by one simultaneous odd tuple",
        "subgroup_order": len(subgroup),
        "common_parity_group_order": expected_full,
        "pair_projection_orders": pair_projection_sizes,
        "common_parity_pair_order": expected_pair,
        "proper_with_all_pair_projections_full": True,
        "smallest_possible_arity": 3,
    }


def main() -> None:
    started = time.perf_counter()
    ref, dependency_path, dependency_hash = load_frozen_m137()
    actual_rows = audit_actual_rank_three(ref)
    abstract_counterexample = abstract_rank_three_counterexample(ref)
    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repository_root(),
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    payload = {
        "experiment": "M141 multisource matching subgroup exceptional-rank audit",
        "repository_commit": commit,
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "command": "python3 -B multisource_subgroup_audit.py",
        "composition_convention": "(pq)(x)=p(q(x)); displayed factors multiply left-to-right",
        "frozen_read_only_dependency": {
            "path": str(dependency_path.relative_to(repository_root())),
            "sha256": dependency_hash,
        },
        "universal_claim": "proved separately for d>=5; finite data are exception audits only",
        "actual_d3_matching_rows": actual_rows,
        "abstract_d3_pairwise_full_counterexample": abstract_counterexample,
    }
    assert all(
        not any(
            len(failure["subset"]) <= 2
            for failure in color[side]["common_parity_group_failures"]
        )
        for row in actual_rows
        for color in row["matching_colors"]
        for side in ("source", "target")
    )
    assert all(
        color["aligned_source_target_comparison_by_width"]["2"][
            "equal_literal_subgroups"
        ]
        == 6
        and color["aligned_source_target_comparison_by_width"]["4"][
            "equal_literal_subgroups"
        ]
        == 0
        for row in actual_rows
        for color in row["matching_colors"]
    )
    output = Path(__file__).with_name("results.json")
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    elapsed_seconds = time.perf_counter() - started
    print(
        json.dumps(
            {
                "actual_d3_rows": len(actual_rows),
                "elapsed_seconds": elapsed_seconds,
                "output": str(output),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
