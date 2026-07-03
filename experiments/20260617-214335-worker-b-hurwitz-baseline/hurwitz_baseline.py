#!/usr/bin/env python3
"""Pure Hurwitz baseline for small identity transposition words.

This script is intentionally self-contained for the Worker B experiment.  It
enumerates exact small spaces Omega(N,m), computes Hurwitz components, records
the weighted support-component invariant, and runs a lazy pure-Hurwitz walk to
show that the sampler remains trapped in its starting component.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
import time
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Deque, Dict, Iterable, Iterator, List, Sequence, Tuple

Edge = Tuple[int, int]
Word = Tuple[int, ...]
InvariantKey = Tuple[Tuple[Tuple[int, ...], int], ...]

EXPECTED = {
    (3, 4): {"identity_words": 27, "component_count": 4},
    (4, 4): {"identity_words": 120, "component_count": 13},
    (4, 6): {"identity_words": 3936, "component_count": 17},
}


def transpositions(n: int) -> List[Edge]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def edge_map(edges: Sequence[Edge]) -> Dict[Edge, int]:
    return {edge: idx for idx, edge in enumerate(edges)}


def apply_edge_to_point(point: int, edge: Edge) -> int:
    a, b = edge
    if point == a:
        return b
    if point == b:
        return a
    return point


def conjugate_edge(edge_id: int, by_edge_id: int, edges: Sequence[Edge], edge_to_id: Dict[Edge, int]) -> int:
    """Return by_edge^{-1} edge by_edge, still encoded as an edge id.

    For transpositions the inverse equals itself, so this relabels both
    endpoints of ``edge`` by ``by_edge``.
    """

    u, v = edges[edge_id]
    by_edge = edges[by_edge_id]
    cu = apply_edge_to_point(u, by_edge)
    cv = apply_edge_to_point(v, by_edge)
    if cu == cv:
        raise AssertionError("conjugating a transposition collapsed its endpoints")
    return edge_to_id[tuple(sorted((cu, cv)))]


def right_hurwitz(word: Word, pos: int, edges: Sequence[Edge], edge_to_id: Dict[Edge, int]) -> Word:
    """Apply (a,b) -> (b, b^{-1} a b) at adjacent position ``pos``."""

    a = word[pos]
    b = word[pos + 1]
    replacement = (b, conjugate_edge(a, b, edges, edge_to_id))
    return word[:pos] + replacement + word[pos + 2 :]


def inverse_hurwitz(word: Word, pos: int, edges: Sequence[Edge], edge_to_id: Dict[Edge, int]) -> Word:
    """Apply the inverse move (a,b) -> (a b a^{-1}, a)."""

    a = word[pos]
    b = word[pos + 1]
    replacement = (conjugate_edge(b, a, edges, edge_to_id), a)
    return word[:pos] + replacement + word[pos + 2 :]


def hurwitz_neighbors(word: Word, edges: Sequence[Edge], edge_to_id: Dict[Edge, int]) -> Iterator[Word]:
    seen = set()
    for pos in range(len(word) - 1):
        for move in (right_hurwitz, inverse_hurwitz):
            neighbor = move(word, pos, edges, edge_to_id)
            if neighbor not in seen:
                seen.add(neighbor)
                yield neighbor


def eval_word(word: Word, n: int, edges: Sequence[Edge]) -> Tuple[int, ...]:
    """Evaluate a word by applying factors from left to right."""

    image = list(range(n))
    for edge_id in word:
        a, b = edges[edge_id]
        for idx, value in enumerate(image):
            if value == a:
                image[idx] = b
            elif value == b:
                image[idx] = a
    return tuple(image)


def enumerate_identity_words(n: int, m: int, edges: Sequence[Edge]) -> List[Word]:
    identity = tuple(range(n))
    words = []
    for word in itertools.product(range(len(edges)), repeat=m):
        if eval_word(word, n, edges) == identity:
            words.append(word)
    return words


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))

    def find(self, value: int) -> int:
        parent = self.parent[value]
        if parent != value:
            parent = self.find(parent)
            self.parent[value] = parent
        return parent

    def union(self, left: int, right: int) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root != right_root:
            if right_root < left_root:
                left_root, right_root = right_root, left_root
            self.parent[right_root] = left_root


def weighted_support_invariant(word: Word, n: int, edges: Sequence[Edge]) -> InvariantKey:
    dsu = DSU(n)
    for edge_id in word:
        a, b = edges[edge_id]
        dsu.union(a, b)

    vertices_by_root: Dict[int, List[int]] = defaultdict(list)
    for vertex in range(n):
        vertices_by_root[dsu.find(vertex)].append(vertex)

    factor_counts: Counter[int] = Counter()
    for edge_id in word:
        a, _ = edges[edge_id]
        factor_counts[dsu.find(a)] += 1

    records = []
    for root, vertices in vertices_by_root.items():
        count = factor_counts[root]
        if count:
            records.append((tuple(vertices), count))
    return tuple(sorted(records))


def invariant_to_json(key: InvariantKey) -> List[Dict[str, object]]:
    return [{"vertices": list(vertices), "factor_count": count} for vertices, count in key]


def word_to_edges(word: Word, edges: Sequence[Edge]) -> List[List[int]]:
    return [[edges[edge_id][0], edges[edge_id][1]] for edge_id in word]


def compute_components(
    words: Sequence[Word],
    n: int,
    edges: Sequence[Edge],
    edge_to_id: Dict[Edge, int],
) -> Tuple[List[List[int]], List[int], int]:
    word_to_idx = {word: idx for idx, word in enumerate(words)}
    component_id = [-1] * len(words)
    components: List[List[int]] = []
    identity = tuple(range(n))
    product_failures = 0

    for start_idx, start_word in enumerate(words):
        if component_id[start_idx] >= 0:
            continue
        cid = len(components)
        component: List[int] = []
        queue: Deque[int] = deque([start_idx])
        component_id[start_idx] = cid

        while queue:
            idx = queue.popleft()
            word = words[idx]
            component.append(idx)

            for neighbor in hurwitz_neighbors(word, edges, edge_to_id):
                if eval_word(neighbor, n, edges) != identity:
                    product_failures += 1
                neighbor_idx = word_to_idx.get(neighbor)
                if neighbor_idx is None:
                    raise AssertionError("Hurwitz move left the enumerated identity space")
                if component_id[neighbor_idx] < 0:
                    component_id[neighbor_idx] = cid
                    queue.append(neighbor_idx)

        components.append(component)

    return components, component_id, product_failures


def run_walk(
    *,
    seed_word: Word,
    n: int,
    edges: Sequence[Edge],
    edge_to_id: Dict[Edge, int],
    word_to_idx: Dict[Word, int],
    component_id: Sequence[int],
    steps: int,
    lazy_probability: float,
    rng: random.Random,
) -> Dict[str, object]:
    current = seed_word
    identity = tuple(range(n))
    seed_invariant = weighted_support_invariant(seed_word, n, edges)
    visited_words = {current}
    visited_components = {component_id[word_to_idx[current]]}
    identity_failures = 0
    invariant_changed = False

    for _ in range(steps):
        if rng.random() >= lazy_probability:
            pos = rng.randrange(len(current) - 1)
            if rng.randrange(2):
                current = right_hurwitz(current, pos, edges, edge_to_id)
            else:
                current = inverse_hurwitz(current, pos, edges, edge_to_id)

        if eval_word(current, n, edges) != identity:
            identity_failures += 1
        if weighted_support_invariant(current, n, edges) != seed_invariant:
            invariant_changed = True

        visited_words.add(current)
        visited_components.add(component_id[word_to_idx[current]])

    return {
        "steps": steps,
        "lazy_probability": lazy_probability,
        "unique_words_seen": len(visited_words),
        "visited_component_ids": sorted(visited_components),
        "visited_component_count": len(visited_components),
        "identity_failures": identity_failures,
        "invariant_changed": invariant_changed,
        "final_word_edges": word_to_edges(current, edges),
    }


def summarize_case(n: int, m: int, steps: int, seed: int) -> List[Dict[str, object]]:
    started = time.perf_counter()
    edges = transpositions(n)
    edge_to_id = edge_map(edges)
    words = enumerate_identity_words(n, m, edges)
    components, component_id, product_failures = compute_components(words, n, edges, edge_to_id)
    word_to_idx = {word: idx for idx, word in enumerate(words)}

    invariant_by_word = [weighted_support_invariant(word, n, edges) for word in words]
    invariants_by_component: List[InvariantKey] = []
    mixed_invariant_components = 0
    for component in components:
        component_invariants = {invariant_by_word[idx] for idx in component}
        if len(component_invariants) != 1:
            mixed_invariant_components += 1
        invariants_by_component.append(sorted(component_invariants)[0])

    invariant_class_sizes: Counter[InvariantKey] = Counter(invariant_by_word)
    components_by_invariant: Dict[InvariantKey, List[int]] = defaultdict(list)
    for cid, key in enumerate(invariants_by_component):
        components_by_invariant[key].append(cid)

    component_sizes = [len(component) for component in components]
    sorted_component_ids = sorted(range(len(components)), key=lambda cid: (-component_sizes[cid], cid))
    largest_component_id = sorted_component_ids[0]
    first_word = words[0]
    largest_seed_word = words[components[largest_component_id][0]]
    expected = EXPECTED.get((n, m))
    expected_check = None
    if expected:
        expected_check = {
            "identity_words_expected": expected["identity_words"],
            "component_count_expected": expected["component_count"],
            "identity_words_match": len(words) == expected["identity_words"],
            "component_count_match": len(components) == expected["component_count"],
        }

    records: List[Dict[str, object]] = [
        {
            "record_type": "case_summary",
            "N": n,
            "m": m,
            "target_distribution": "uniform fixed-length identity transposition words",
            "sampler_distribution": "lazy pure Hurwitz walk, uniform only within its starting component when mixed",
            "transposition_count": len(edges),
            "total_words": len(edges) ** m,
            "identity_words": len(words),
            "component_count": len(components),
            "component_sizes_desc": sorted(component_sizes, reverse=True),
            "largest_component_size": component_sizes[largest_component_id],
            "largest_component_id": largest_component_id,
            "best_possible_pure_hurwitz_tv_lower_bound_vs_global_uniform": 1.0
            - (component_sizes[largest_component_id] / len(words)),
            "weighted_invariant_class_count": len(invariant_class_sizes),
            "weighted_invariant_sizes_desc": sorted(invariant_class_sizes.values(), reverse=True),
            "max_components_sharing_one_weighted_invariant": max(
                len(ids) for ids in components_by_invariant.values()
            ),
            "mixed_invariant_components": mixed_invariant_components,
            "hurwitz_product_failures_in_component_build": product_failures,
            "expected_check": expected_check,
            "elapsed_seconds": round(time.perf_counter() - started, 6),
        }
    ]

    for cid, component in enumerate(components):
        invariant = invariants_by_component[cid]
        records.append(
            {
                "record_type": "component_summary",
                "N": n,
                "m": m,
                "component_id": cid,
                "component_size": len(component),
                "weighted_support_invariant": invariant_to_json(invariant),
                "representative_word_edges": word_to_edges(words[component[0]], edges),
            }
        )

    rng = random.Random(seed + 1000 * n + m)
    for seed_strategy, seed_word in (
        ("lexicographic_first", first_word),
        ("largest_component_representative", largest_seed_word),
    ):
        seed_component = component_id[word_to_idx[seed_word]]
        walk_record = run_walk(
            seed_word=seed_word,
            n=n,
            edges=edges,
            edge_to_id=edge_to_id,
            word_to_idx=word_to_idx,
            component_id=component_id,
            steps=steps,
            lazy_probability=0.5,
            rng=rng,
        )
        records.append(
            {
                "record_type": "hurwitz_walk",
                "N": n,
                "m": m,
                "seed_strategy": seed_strategy,
                "seed": seed,
                "seed_word_edges": word_to_edges(seed_word, edges),
                "seed_component_id": seed_component,
                "seed_component_size": component_sizes[seed_component],
                "outside_seed_component_words": len(words) - component_sizes[seed_component],
                "tv_lower_bound_vs_global_uniform": 1.0 - (component_sizes[seed_component] / len(words)),
                **walk_record,
            }
        )

    return records


def parse_case(value: str) -> Tuple[int, int]:
    parts = value.split(",")
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("cases must have form N,m")
    return int(parts[0]), int(parts[1])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--case",
        action="append",
        type=parse_case,
        dest="cases",
        help="case as N,m; may be repeated",
    )
    parser.add_argument("--steps", type=int, default=20000, help="Hurwitz walk steps per seed")
    parser.add_argument("--seed", type=int, default=214335, help="base RNG seed")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("results.jsonl"),
        help="JSONL output path",
    )
    args = parser.parse_args()

    cases = args.cases or [(3, 4), (4, 4), (4, 6)]
    all_records: List[Dict[str, object]] = []
    for n, m in cases:
        all_records.extend(summarize_case(n, m, args.steps, args.seed))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        for record in all_records:
            handle.write(json.dumps(record, sort_keys=True) + "\n")

    failed_checks = [
        record
        for record in all_records
        if record.get("record_type") == "case_summary"
        and record.get("expected_check")
        and not (
            record["expected_check"]["identity_words_match"]
            and record["expected_check"]["component_count_match"]
        )
    ]
    if failed_checks:
        raise SystemExit(f"expected-count check failed for {failed_checks!r}")


if __name__ == "__main__":
    main()
