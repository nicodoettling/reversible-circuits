#!/usr/bin/env python3
"""Fixed-seed probe of collision-contour homology versus deletion safety.

This is empirical except for each individual replayed state, whose duplicate,
connectivity, and integer voltage are computed exactly.
"""

from __future__ import annotations

import argparse
import json
import platform
import random
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

from collision_contour_audit import contour_record
from subset_tail_audit import lifted_word, safe_pairs_static, stable_residual


sys.dont_write_bytecode = True


def run_case(L: int, trials: int, seed: int):
    word = lifted_word(L)
    k = len(word)
    n = 8 * L * L
    rng = random.Random(seed)
    collisions = 0
    safe = 0
    equivalence_failures = []
    homology_histogram = Counter()
    path_length_histogram = Counter()
    examples = []
    started = time.perf_counter()
    for trial_index in range(trials):
        order = list(range(k))
        rng.shuffle(order)
        selected: set[int] = set()
        residual = stable_residual(word, frozenset(), n)
        previous = None
        previous_label = None
        for depth, label in enumerate(order):
            current = residual[label]
            if previous is not None and current == previous:
                preliminary = frozenset(selected - {previous_label})
                pair = tuple(sorted((previous_label, label)))
                record = contour_record(L, tuple(preliminary), pair)
                pairs = safe_pairs_static(word, preliminary, n)
                is_safe = pair in pairs
                homology = tuple(record["contour_homology"])
                nonzero = homology != (0, 0)
                collisions += 1
                safe += is_safe
                homology_histogram[str(homology)] += 1
                path_length_histogram[str(tuple(record["path_lengths"]))] += 1
                if is_safe != nonzero and len(equivalence_failures) < 20:
                    equivalence_failures.append({
                        "trial": trial_index,
                        "depth": depth - 1,
                        "preliminary_selected": sorted(preliminary),
                        "pair": list(pair),
                        "safe": is_safe,
                        "record": record,
                    })
                if len(examples) < 12:
                    examples.append({
                        "trial": trial_index,
                        "depth": depth - 1,
                        "pair": list(pair),
                        "safe": is_safe,
                        "homology": list(homology),
                    })
            selected.add(label)
            residual = stable_residual(word, frozenset(selected), n)
            previous = current
            previous_label = label
    return {
        "L": L,
        "n": n,
        "k": k,
        "trials": trials,
        "seed": seed,
        "collision_prefixes": collisions,
        "safe_prefixes": safe,
        "homology_histogram": dict(sorted(homology_histogram.items())),
        "path_length_histogram": dict(sorted(path_length_histogram.items())),
        "safe_iff_nonzero_homology_failures": equivalence_failures,
        "examples": examples,
        "elapsed_seconds": time.perf_counter() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--seed", type=int, default=840084)
    parser.add_argument("--case", nargs=2, action="append", metavar=("L", "TRIALS"))
    args = parser.parse_args()
    cases = [(int(L), int(trials)) for L, trials in (args.case or [(1, 5000), (2, 10000)])]
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
        "nonstandard_dependencies": {},
        "method": (
            "Uniform random full label orders; exact subset-state residual; "
            "exact collision contour voltage and exact deletion connectivity."
        ),
        "scope_warning": (
            "The absence of a mismatch in fixed-seed trials is empirical and "
            "does not prove a topological equivalence."
        ),
        "results": [
            run_case(L, trials, args.seed + 1000003 * index)
            for index, (L, trials) in enumerate(cases)
        ],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], sort_keys=True))


if __name__ == "__main__":
    main()
