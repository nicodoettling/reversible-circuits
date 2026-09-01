#!/usr/bin/env python3
"""Deterministic checks for the M146 tuple-conjugacy theorem.

The universal d>=5 statement is proved in ``tuple_conjugacy_theorem.md``.
Finite calculations here test the exact class-splitting formula at bounded
rank and calibrate the accepted M135 matchings at d=3.  The DPS reconstruction
is loaded read-only from the frozen M137 fresh checker after a SHA-256 check.
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
from collections import Counter, defaultdict, deque
from pathlib import Path


Permutation = tuple[int, ...]
ProductElement = tuple[Permutation, ...]

M137_CHECKER_SHA256 = "bb62d449c7cad72a448389f9f7dd7ee76618e8c71b68189db20e19f4e2244341"


def repository_root() -> Path:
    return Path(__file__).resolve().parents[4]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_frozen_m137():
    path = (
        repository_root()
        / "experiments/20260811-polynomial-mixing-resolution/cycle-31"
        / "mission-M137-m135-fresh-referee/independent_referee.py"
    )
    observed = sha256(path)
    assert observed == M137_CHECKER_SHA256, (observed, M137_CHECKER_SHA256)
    spec = importlib.util.spec_from_file_location("frozen_m137_checker_m146", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module, path, observed


def inverse(p: Permutation) -> Permutation:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def cycle_type(p: Permutation) -> tuple[int, ...]:
    seen = set()
    lengths = []
    for start in range(len(p)):
        if start in seen:
            continue
        length = 0
        x = start
        while x not in seen:
            seen.add(x)
            length += 1
            x = p[x]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def distinct_odd_cycle_type(kind: tuple[int, ...]) -> bool:
    return all(part % 2 == 1 for part in kind) and len(set(kind)) == len(kind)


def conjugate(ref, h: Permutation, x: Permutation) -> Permutation:
    return ref.multiply(ref.multiply(h, x), inverse(h))


def product_conjugate(ref, h: ProductElement, x: ProductElement) -> ProductElement:
    return tuple(conjugate(ref, a, b) for a, b in zip(h, x))


def product_multiply(ref, left: ProductElement, right: ProductElement) -> ProductElement:
    return tuple(ref.multiply(a, b) for a, b in zip(left, right))


def centralizer_parity_audit(ref, max_d: int = 7) -> list[dict]:
    """Test one representative of every cycle type through rank max_d."""
    rows = []
    for d in range(2, max_d + 1):
        permutations = tuple(itertools.permutations(range(d)))
        representatives = {}
        for p in permutations:
            representatives.setdefault(cycle_type(p), p)
        failures = []
        details = []
        for kind, p in sorted(representatives.items()):
            centralizer = tuple(
                g
                for g in permutations
                if ref.multiply(g, p) == ref.multiply(p, g)
            )
            has_odd = any(ref.sign(g) == -1 for g in centralizer)
            predicted = not distinct_odd_cycle_type(kind)
            details.append(
                {
                    "cycle_type": list(kind),
                    "centralizer_order": len(centralizer),
                    "has_odd_centralizer": has_odd,
                    "predicted_has_odd": predicted,
                }
            )
            if has_odd != predicted:
                failures.append(list(kind))
        rows.append(
            {
                "d": d,
                "cycle_types_checked": len(details),
                "failures": failures,
                "details": details,
            }
        )
    return rows


def common_parity_elements(ref, permutations, width: int) -> tuple[ProductElement, ...]:
    return tuple(
        x
        for x in itertools.product(permutations, repeat=width)
        if len({ref.sign(p) for p in x}) == 1
    )


def common_parity_conjugation_generators(ref, d: int, width: int):
    permutations = tuple(itertools.permutations(range(d)))
    identity = tuple(range(d))
    even = tuple(p for p in permutations if ref.sign(p) == 1)
    generators = []
    for coordinate in range(width):
        for p in even:
            if p == identity:
                continue
            element = [identity] * width
            element[coordinate] = p
            generators.append(tuple(element))
    transposition = ref.edge_map(d, (0, 1))
    generators.append(tuple(transposition for _ in range(width)))
    return tuple(generators)


def direct_class_splitting_audit(ref, max_d: int = 4, max_width: int = 3) -> list[dict]:
    """Enumerate P_(d,s)-conjugacy orbits and compare the splitting count."""
    rows = []
    for d in range(2, max_d + 1):
        permutations = tuple(itertools.permutations(range(d)))
        for width in range(1, max_width + 1):
            elements = common_parity_elements(ref, permutations, width)
            remaining = set(elements)
            generators = common_parity_conjugation_generators(ref, d, width)
            actual_by_ambient = Counter()
            while remaining:
                seed = min(remaining)
                orbit = {seed}
                queue = deque([seed])
                while queue:
                    x = queue.popleft()
                    for h in generators:
                        y = product_conjugate(ref, h, x)
                        if y not in orbit:
                            orbit.add(y)
                            queue.append(y)
                assert orbit <= remaining
                remaining -= orbit
                ambient = tuple(cycle_type(p) for p in seed)
                assert all(tuple(cycle_type(p) for p in x) == ambient for x in orbit)
                actual_by_ambient[ambient] += 1

            expected_by_ambient = {}
            for x in elements:
                ambient = tuple(cycle_type(p) for p in x)
                if ambient in expected_by_ambient:
                    continue
                rigid = sum(distinct_odd_cycle_type(kind) for kind in ambient)
                expected_by_ambient[ambient] = 2 ** max(rigid - 1, 0)
            failures = []
            for ambient, expected in expected_by_ambient.items():
                actual = actual_by_ambient[ambient]
                if actual != expected:
                    failures.append(
                        {
                            "ambient_cycle_types": [list(kind) for kind in ambient],
                            "actual": actual,
                            "expected": expected,
                        }
                    )
            transposition_kind = cycle_type(ref.edge_map(d, (0, 1)))
            all_transposition_ambient = tuple(transposition_kind for _ in range(width))
            rows.append(
                {
                    "d": d,
                    "width": width,
                    "group_order": len(elements),
                    "conjugacy_classes": sum(actual_by_ambient.values()),
                    "ambient_classes": len(actual_by_ambient),
                    "formula_failures": failures,
                    "all_transposition_class_count": actual_by_ambient[
                        all_transposition_ambient
                    ],
                }
            )
    return rows


def generated_group(ref, d: int, words) -> frozenset[ProductElement]:
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


def factor_tuples(ref, d: int, words) -> tuple[ProductElement, ...]:
    return tuple(
        tuple(ref.edge_map(d, word[position]) for word in words)
        for position in range(len(words[0]))
    )


def class_multiset(ref, group, factors) -> Counter:
    def class_key(x):
        return min(product_conjugate(ref, h, x) for h in group)

    return Counter(class_key(x) for x in factors)


def matching_data_rank_three(ref):
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
    witnesses = []
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
        assert len(left_vertices) == len(right_vertices) == len(global_blocks) == 4
        for color in range(d):
            edge_ids = tuple(sorted(edge for edge, c in colors.items() if c == color))
            source_indices = tuple(representatives[edge] for edge in edge_ids)
            target_indices = tuple(target[source] for source in source_indices)
            assert len(source_indices) == 4
            by_width = {}
            for width in range(1, 5):
                counters = Counter()
                for positions in itertools.combinations(range(4), width):
                    source_words = tuple(words[source_indices[j]] for j in positions)
                    target_words = tuple(words[target_indices[j]] for j in positions)
                    source_group = generated_group(ref, d, source_words)
                    target_group = generated_group(ref, d, target_words)
                    if source_group != target_group:
                        counters["literal_group_changed"] += 1
                        continue
                    source_classes = class_multiset(
                        ref, source_group, factor_tuples(ref, d, source_words)
                    )
                    target_classes = class_multiset(
                        ref, target_group, factor_tuples(ref, d, target_words)
                    )
                    if source_classes == target_classes:
                        counters["class_multiset_equal"] += 1
                    else:
                        counters["class_multiset_changed"] += 1
                        witnesses.append(
                            {
                                "adjacent_index": adjacent_index + 1,
                                "color": color,
                                "width": width,
                                "positions": [j + 1 for j in positions],
                                "source_indices": [source_indices[j] for j in positions],
                                "target_indices": [target_indices[j] for j in positions],
                                "group_order": len(source_group),
                                "source_words": [
                                    [list(edge) for edge in word] for word in source_words
                                ],
                                "target_words": [
                                    [list(edge) for edge in word] for word in target_words
                                ],
                                "source_class_sizes": sorted(source_classes.values()),
                                "target_class_sizes": sorted(target_classes.values()),
                            }
                        )
                by_width[str(width)] = dict(sorted(counters.items()))
            rows.append(
                {
                    "adjacent_index": adjacent_index + 1,
                    "color": color,
                    "matching_edges": len(edge_ids),
                    "subfamily_outcomes_by_width": by_width,
                }
            )
    return rows, witnesses


def explicit_even_conjugator_for_transpositions(d: int, source, target):
    """Return an even conjugator, using the odd centralizer of target."""
    permutations = tuple(itertools.permutations(range(d)))
    transporter = next(
        g for g in permutations if conjugate_dummy(g, source) == target
    )
    if permutation_sign(transporter) == 1:
        return transporter
    # Left multiplication by target centralizes target and flips parity.
    return compose_dummy(target, transporter)


def compose_dummy(p, q):
    return tuple(p[q[x]] for x in range(len(p)))


def conjugate_dummy(h, x):
    return compose_dummy(compose_dummy(h, x), inverse(h))


def permutation_sign(p):
    inversions = sum(
        p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))
    )
    return -1 if inversions % 2 else 1


def all_transposition_explicit_transport_audit(max_d: int = 7) -> list[dict]:
    rows = []
    for d in range(2, max_d + 1):
        transpositions = []
        for edge in itertools.combinations(range(d), 2):
            p = list(range(d))
            p[edge[0]], p[edge[1]] = p[edge[1]], p[edge[0]]
            transpositions.append(tuple(p))
        failures = []
        for source in transpositions:
            for target in transpositions:
                g = explicit_even_conjugator_for_transpositions(d, source, target)
                if permutation_sign(g) != 1 or conjugate_dummy(g, source) != target:
                    failures.append([source, target, g])
        rows.append(
            {
                "d": d,
                "ordered_transposition_pairs": len(transpositions) ** 2,
                "failures": failures,
            }
        )
    return rows


def main() -> None:
    ref, dependency_path, dependency_hash = load_frozen_m137()
    centralizer_rows = centralizer_parity_audit(ref, max_d=7)
    splitting_rows = direct_class_splitting_audit(ref, max_d=4, max_width=3)
    transport_rows = all_transposition_explicit_transport_audit(max_d=7)
    matching_rows, matching_witnesses = matching_data_rank_three(ref)

    assert all(not row["failures"] for row in centralizer_rows)
    assert all(not row["formula_failures"] for row in splitting_rows)
    assert all(row["all_transposition_class_count"] == 1 for row in splitting_rows)
    assert all(not row["failures"] for row in transport_rows)

    aggregate = {}
    for width in range(1, 5):
        total = Counter()
        for row in matching_rows:
            total.update(row["subfamily_outcomes_by_width"][str(width)])
        aggregate[str(width)] = dict(sorted(total.items()))

    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repository_root(),
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    payload = {
        "experiment": "M146 DPS aligned tuple-conjugacy invariant audit",
        "repository_commit": commit,
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "command": "python3 -B tuple_conjugacy_audit.py",
        "composition_convention": "(pq)(x)=p(q(x)); displayed factors multiply left-to-right",
        "frozen_read_only_dependency": {
            "path": str(dependency_path.relative_to(repository_root())),
            "sha256": dependency_hash,
        },
        "caps": {
            "centralizer_cycle_types": "one representative of every S_d cycle type, 2<=d<=7",
            "direct_class_orbits": "all elements of P_(d,s), 2<=d<=4 and 1<=s<=3",
            "explicit_transposition_transporters": "all ordered transposition pairs, 2<=d<=7",
            "d3_matching_calibration": "all 9 deterministic M137 matchings and all 15 nonempty subfamilies",
            "d5_matching_enumeration": "not run: universal theorem makes it unnecessary",
        },
        "universal_claim": "proved separately; finite checks are theorem stress tests and d=3 calibration",
        "centralizer_parity_audit": centralizer_rows,
        "direct_class_splitting_audit": splitting_rows,
        "explicit_even_transposition_transporters": transport_rows,
        "d3_matching_rows": matching_rows,
        "d3_aggregate_by_width": aggregate,
        "d3_class_multiset_change_witnesses": matching_witnesses,
    }
    output = Path(__file__).with_name("results.json")
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "centralizer_rows": len(centralizer_rows),
                "splitting_rows": len(splitting_rows),
                "d3_matchings": len(matching_rows),
                "d3_class_change_witnesses": len(matching_witnesses),
                "output": str(output),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
