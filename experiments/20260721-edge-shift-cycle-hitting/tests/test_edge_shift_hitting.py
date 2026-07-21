#!/usr/bin/env python3

from __future__ import annotations

import random
import json
import sys
import tempfile
import unittest
from pathlib import Path


EXPERIMENT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EXPERIMENT_ROOT))

from edge_shift_hitting import (  # noqa: E402
    apply_ordered_wedge,
    component_count,
    edge_count,
    graph_statistics,
    make_cycle_bouquet,
    make_cycle_with_chords,
    make_disjoint_cycles,
    make_theta,
    run_edge_shift_walk,
    sanitize_resume_file,
    validate_initial_graph,
)


def stats(adjacency):
    return graph_statistics(
        adjacency,
        exact_cycle_rank_cap=16,
        exact_cycle_element_cap=1_000_000,
    )


class GeneratorAndCycleStatisticTests(unittest.TestCase):
    def test_single_cycle(self) -> None:
        result = stats(make_disjoint_cycles([6]))
        self.assertEqual(result["cycle_rank"], 1)
        self.assertEqual(result["simple_cycle_count_exact"], 1)
        self.assertEqual(result["simple_cycle_lengths_exact"], [6])

    def test_bouquet_has_exactly_planted_cycles(self) -> None:
        result = stats(make_cycle_bouquet([3, 4, 5]))
        self.assertEqual(result["cycle_rank"], 3)
        self.assertEqual(result["simple_cycle_count_exact"], 3)
        self.assertEqual(result["simple_cycle_lengths_exact"], [3, 4, 5])
        self.assertTrue(result["all_vertices_cycle_covered"])

    def test_theta_has_three_cycles(self) -> None:
        result = stats(make_theta([2, 3, 4]))
        self.assertEqual(result["cycle_rank"], 2)
        self.assertEqual(result["simple_cycle_count_exact"], 3)
        self.assertEqual(result["simple_cycle_lengths_exact"], [5, 6, 7])

    def test_cycle_with_chords_has_requested_rank(self) -> None:
        graph = make_cycle_with_chords(20, 5, random.Random(7))
        validate_initial_graph(graph)
        self.assertEqual(stats(graph)["cycle_rank"], 5)


class EdgeShiftTests(unittest.TestCase):
    def test_non_hit_shift_preserves_basic_invariants(self) -> None:
        graph = make_disjoint_cycles([4])
        initial_edges = edge_count(graph)
        initial_components = component_count(graph)
        self.assertFalse(apply_ordered_wedge(graph, 0, 1, 2))
        self.assertEqual(edge_count(graph), initial_edges)
        self.assertEqual(component_count(graph), initial_components)
        self.assertEqual(stats(graph)["cycle_rank"], 1)

    def test_triangle_hits_in_one_step(self) -> None:
        graph = make_disjoint_cycles([3])
        for seed in range(10):
            result = run_edge_shift_walk(graph, rng=random.Random(seed), max_steps=100)
            self.assertTrue(result.hit)
            self.assertEqual(result.hit_step, 1)

    def test_reproducible_walk(self) -> None:
        graph = make_theta([3, 4, 5])
        left = run_edge_shift_walk(graph, rng=random.Random(1234), max_steps=10000)
        right = run_edge_shift_walk(graph, rng=random.Random(1234), max_steps=10000)
        self.assertEqual(left, right)


class ResumeTests(unittest.TestCase):
    def test_incomplete_graph_block_is_removed(self) -> None:
        digest = "test-digest"
        records = [
            {"record_type": "run_metadata", "config_digest": digest},
            {"record_type": "graph_summary", "config_digest": digest, "setting_id": "s", "graph_index": 0},
            {"record_type": "walk_trial", "config_digest": digest, "setting_id": "s", "graph_index": 0},
            {"record_type": "graph_summary", "config_digest": digest, "setting_id": "s", "graph_index": 1},
            {"record_type": "graph_complete", "config_digest": digest, "setting_id": "s", "graph_index": 1},
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "results.jsonl"
            with path.open("w", encoding="utf-8") as handle:
                for record in records:
                    handle.write(json.dumps(record) + "\n")
                handle.write('{"truncated":')
            completed = sanitize_resume_file(path, digest)
            self.assertEqual(completed, {("s", 1)})
            remaining = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
            self.assertFalse(any(record.get("graph_index") == 0 for record in remaining))
            self.assertTrue(any(record.get("graph_index") == 1 for record in remaining))


if __name__ == "__main__":
    unittest.main()
