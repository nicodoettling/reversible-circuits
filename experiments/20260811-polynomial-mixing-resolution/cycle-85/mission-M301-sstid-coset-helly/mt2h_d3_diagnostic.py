#!/usr/bin/env python3
"""One exact finite diagnostic for M301's pre-registered MT2H candidate.

The accepted, SHA-gated M135 implementation supplies the DPS map and basic
permutation/Hurwitz routines.  This script independently constructs the
finite signed-Hurwitz action image, actual H-orbit incidence edges, every
perfect matching, and the exact action-fiber intersections at d=3.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import platform
import subprocess
import sys
import time
from collections import Counter, defaultdict, deque
from pathlib import Path


M135_TOP_SHA = "8d7ca3afbab24be7b1552b433e9f0f0260efbbb658af4bd66cccd676452a5358"
M135_SCRIPT_SHA = "79ed378ae7fd7543c16bf12a1fa51e0144b817a938c91de196be960a2e6ad540"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_m135(repo: Path):
    directory = (
        repo
        / "experiments/20260811-polynomial-mixing-resolution/cycle-30"
        / "mission-M135-conflict-coloring-realization"
    )
    manifest = directory / "SHA256SUMS"
    script = directory / "conflict_coloring_audit.py"
    observed = {"manifest": sha256(manifest), "script": sha256(script)}
    expected = {"manifest": M135_TOP_SHA, "script": M135_SCRIPT_SHA}
    if observed != expected:
        raise AssertionError(("M135 SHA gate failed", expected, observed))
    spec = importlib.util.spec_from_file_location("m135_frozen", script)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module, observed


def all_actions(module, words, index):
    generators = []
    for position in range(len(words[0]) - 1):
        for sign in (1, -1):
            generators.append(
                tuple(index[module.hurwitz(word, position, sign)] for word in words)
            )
    identity = tuple(range(len(words)))
    actions = {identity}
    queue = deque([identity])
    while queue:
        action = queue.popleft()
        for generator in generators:
            new = module.compose_action(generator, action)
            if new not in actions:
                actions.add(new)
                queue.append(new)
    return tuple(sorted(actions))


def enumerate_matchings(edge_endpoints, left_count):
    by_left = defaultdict(list)
    for edge_id, (left, _right) in enumerate(edge_endpoints):
        by_left[left].append(edge_id)
    matchings = []
    for selected in itertools.product(*(by_left[left] for left in range(left_count))):
        rights = [edge_endpoints[edge_id][1] for edge_id in selected]
        if len(set(rights)) == left_count:
            matchings.append(tuple(selected))
    return tuple(sorted(set(matchings)))


def intersection_size(fibers, subset):
    common = set(fibers[subset[0]])
    for edge_id in subset[1:]:
        common.intersection_update(fibers[edge_id])
    return len(common)


def serialize_word(module, word):
    return module.serialize_word(word)


def run(repo: Path):
    module, dependency_hashes = load_m135(repo)
    d = 3
    words, index, _preimages, target_maps = module.build_rank(d)
    actions = all_actions(module, words, index)
    all_perms = tuple(itertools.permutations(range(d)))
    root_stabilizer = tuple(rho for rho in all_perms if rho[d - 1] == d - 1)
    global_keys = tuple(module.canonical(word, all_perms) for word in words)
    root_keys = tuple(module.canonical(word, root_stabilizer) for word in words)
    global_key_order = tuple(sorted(set(global_keys)))
    global_id = {key: j for j, key in enumerate(global_key_order)}
    root_blocks = defaultdict(list)
    for source, key in enumerate(root_keys):
        root_blocks[key].append(source)
    root_key_order = tuple(sorted(root_blocks))

    adjacent_rows = []
    first_full_witness = None
    first_subfamily_witness = None
    for adjacent_index, target in sorted(target_maps.items()):
        edge_rows = []
        for root_key in root_key_order:
            representative = root_blocks[root_key][0]
            targets = {root_keys[target[source]] for source in root_blocks[root_key]}
            if len(targets) != 1:
                raise AssertionError("tau_i did not descend to H-orbits")
            edge_rows.append(
                {
                    "source": representative,
                    "source_word": serialize_word(module, words[representative]),
                    "left": global_id[global_keys[representative]],
                    "right": global_id[global_keys[target[representative]]],
                    "target": target[representative],
                    "target_word": serialize_word(module, words[target[representative]]),
                }
            )
        endpoints = tuple((row["left"], row["right"]) for row in edge_rows)
        matchings = enumerate_matchings(endpoints, len(global_key_order))
        fibers = tuple(
            frozenset(
                action_id
                for action_id, action in enumerate(actions)
                if action[row["source"]] == row["target"]
            )
            for row in edge_rows
        )
        if set(map(len, fibers)) != {9}:
            raise AssertionError(("unexpected d=3 point-fiber sizes", set(map(len, fibers))))

        minimum_empty_histogram = Counter()
        pairwise_full_count = 0
        pairwise_full_empty_count = 0
        subfamily_counterexamples = []
        full_counterexamples = []
        matching_rows = []
        for matching_id, matching in enumerate(matchings):
            subset_rows = []
            minimum_empty = None
            for size in range(1, len(matching) + 1):
                for subset in itertools.combinations(matching, size):
                    common_size = intersection_size(fibers, subset)
                    subset_rows.append((subset, common_size))
                    if common_size == 0 and minimum_empty is None:
                        minimum_empty = size
                    if size >= 3 and common_size == 0:
                        pair_actions = {
                            tuple(pair): sorted(fibers[pair[0]] & fibers[pair[1]])
                            for pair in itertools.combinations(subset, 2)
                        }
                        pair_sizes = {pair: len(ids) for pair, ids in pair_actions.items()}
                        if min(pair_sizes.values()) > 0:
                            witness = {
                                "adjacent_index": adjacent_index,
                                "matching_id": matching_id,
                                "matching_edges": list(matching),
                                "subfamily_edges": list(subset),
                                "pair_intersection_sizes": {
                                    ",".join(map(str, pair)): value
                                    for pair, value in pair_sizes.items()
                                },
                                "pair_intersection_action_ids": {
                                    ",".join(map(str, pair)): ids
                                    for pair, ids in pair_actions.items()
                                },
                                "total_intersection_size": 0,
                                "edge_rows": [edge_rows[edge_id] for edge_id in subset],
                            }
                            subfamily_counterexamples.append(witness)
            minimum_empty_histogram[minimum_empty or 0] += 1
            pair_sizes_full = [
                intersection_size(fibers, pair)
                for pair in itertools.combinations(matching, 2)
            ]
            total_size = intersection_size(fibers, matching)
            pairwise = min(pair_sizes_full) > 0
            pairwise_full_count += int(pairwise)
            pairwise_full_empty_count += int(pairwise and total_size == 0)
            if pairwise and total_size == 0:
                full_counterexamples.append(
                    {
                        "adjacent_index": adjacent_index,
                        "matching_id": matching_id,
                        "matching_edges": list(matching),
                        "pair_intersection_sizes": pair_sizes_full,
                        "total_intersection_size": total_size,
                        "edge_rows": [edge_rows[edge_id] for edge_id in matching],
                    }
                )
            matching_rows.append(
                {
                    "matching_id": matching_id,
                    "edges": list(matching),
                    "pairwise_compatible": pairwise,
                    "pair_intersection_size_histogram": dict(
                        sorted(Counter(pair_sizes_full).items())
                    ),
                    "total_intersection_size": total_size,
                    "minimum_empty_subfamily_size": minimum_empty,
                }
            )
        if full_counterexamples and first_full_witness is None:
            first_full_witness = full_counterexamples[0]
        if subfamily_counterexamples and first_subfamily_witness is None:
            first_subfamily_witness = subfamily_counterexamples[0]
        adjacent_rows.append(
            {
                "adjacent_index": adjacent_index,
                "actual_h_orbit_edges": len(edge_rows),
                "perfect_matchings": len(matchings),
                "point_fiber_size_histogram": dict(sorted(Counter(map(len, fibers)).items())),
                "pairwise_compatible_perfect_matchings": pairwise_full_count,
                "pairwise_compatible_but_empty_perfect_matchings": pairwise_full_empty_count,
                "minimum_empty_subfamily_size_histogram": {
                    str(key): value for key, value in sorted(minimum_empty_histogram.items())
                },
                "pairwise_compatible_empty_subfamilies": len(subfamily_counterexamples),
                "matching_rows": matching_rows,
            }
        )

    return {
        "experiment": "M301 pre-registered MT2H exact d=3 diagnostic",
        "status": "exact finite",
        "target": "actual M135 H-orbit edges in the minimal connected sector Z_3",
        "candidate": (
            "MT2H: on an actual perfect matching, pairwise nonempty finite "
            "action fibers imply a nonempty total intersection"
        ),
        "composition_convention": "(pq)(x)=p(q(x)); chronological signed right-Hurwitz action",
        "d": d,
        "m": 2 * d - 2,
        "z_size": len(words),
        "finite_action_image_order": len(actions),
        "global_orbits": len(global_key_order),
        "h_orbits": len(root_key_order),
        "dependency_hashes": dependency_hashes,
        "adjacent_rows": adjacent_rows,
        "first_full_mt2h_counterexample": first_full_witness,
        "first_matching_subfamily_2helly_counterexample": first_subfamily_witness,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("results.json"))
    args = parser.parse_args()
    start = time.perf_counter()
    repo = Path(__file__).resolve().parents[4]
    payload = run(repo)
    payload.update(
        {
            "seed": None,
            "python": platform.python_version(),
            "dependencies": {},
            "repository_commit": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=repo, text=True
            ).strip(),
            "command": "python3 -B mt2h_d3_diagnostic.py --output results.json",
            "elapsed_seconds": time.perf_counter() - start,
        }
    )
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "full_counterexample": payload["first_full_mt2h_counterexample"] is not None,
                "subfamily_counterexample": payload[
                    "first_matching_subfamily_2helly_counterexample"
                ]
                is not None,
                "elapsed_seconds": payload["elapsed_seconds"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
