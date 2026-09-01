#!/usr/bin/env python3
"""Independent consistency verifier for all frozen M14 l=3 JSON certificates."""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
import sys
from collections import Counter
from pathlib import Path


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[i]] for i in range(len(p)))


def edge_perm(n: int, edge: list[int]) -> tuple[int, ...]:
    a, b = edge
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def evaluate_edges(n: int, word: list[list[int]]) -> tuple[int, ...]:
    value = tuple(range(n))
    for edge in word:
        value = compose(value, edge_perm(n, edge))
    return value


def partitions(n: int, maximum: int | None = None):
    if n == 0:
        yield ()
        return
    if maximum is None or maximum > n:
        maximum = n
    for first in range(maximum, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def representative(cycle_type: tuple[int, ...]) -> tuple[int, ...]:
    n = sum(cycle_type)
    p = list(range(n))
    start = 0
    for length in cycle_type:
        labels = list(range(start, start + length))
        for i, label in enumerate(labels):
            p[label] = labels[(i + 1) % length]
        start += length
    return tuple(p)


def class_size(cycle_type: tuple[int, ...]) -> int:
    denominator = 1
    for length, count in Counter(cycle_type).items():
        denominator *= length**count * math.factorial(count)
    return math.factorial(sum(cycle_type)) // denominator


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("inputs", type=Path, nargs="+")
    args = parser.parse_args()

    cases: dict[int, dict[str, object]] = {}
    for path in args.inputs:
        payload = json.loads(path.read_text())
        for case in payload["cases"]:
            n = case["N"]
            assert n not in cases
            cases[n] = case

    assert sorted(cases) == list(range(3, 13))
    summaries = []
    for n, case in sorted(cases.items()):
        m = math.comb(n, 2)
        expected_types = [
            cycle_type
            for cycle_type in partitions(n)
            if (n - len(cycle_type)) % 2 == 0 and n - len(cycle_type) <= 6
        ]
        assert case["endpoint_cycle_types_tested"] == len(expected_types)
        assert case["all_endpoint_types_connected"]
        assert case["six_word_class_mass_check"] == m**6

        weighted_mass = 0
        seen_types = []
        witnesses = 0
        for endpoint in case["endpoints"]:
            cycle = tuple(endpoint["cycle_type"])
            seen_types.append(cycle)
            assert endpoint["components"] == 1
            assert endpoint["connected"]
            assert sum(endpoint["component_state_sizes"]) == endpoint["fiber_size"]
            assert endpoint["symmetric_group_class_size"] == class_size(cycle)
            weighted_mass += endpoint["symmetric_group_class_size"] * endpoint["fiber_size"]
            expected_endpoint = representative(cycle)
            reps = endpoint["representative_words_by_component"]
            assert len(reps) == endpoint["components"]
            for word in reps:
                assert len(word) == 6
                assert evaluate_edges(n, word) == expected_endpoint
                witnesses += 1
        assert sorted(seen_types, reverse=True) == sorted(expected_types, reverse=True)
        assert weighted_mass == m**6

        summaries.append(
            {
                "N": n,
                "endpoint_types": len(expected_types),
                "all_connected": True,
                "class_mass": weighted_mass,
                "representative_words_checked": witnesses,
            }
        )

    result = {
        "claim": (
            "All frozen M14 l=3 JSON files cover exactly N=3,...,12 and every "
            "feasible endpoint cycle type; all component, mass, and explicit "
            "representative-product fields pass independent checks."
        ),
        "python": platform.python_version(),
        "command": " ".join([sys.executable, *sys.argv]),
        "commit": subprocess.run(
            ["git", "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip(),
        "cases": summaries,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
