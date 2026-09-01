#!/usr/bin/env python3
"""Exact bounded audit of right-spine root-split support and rates."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import platform
import subprocess
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def load_m50():
    repo = Path(__file__).resolve().parents[4]
    path = (
        repo
        / "experiments/20260811-polynomial-mixing-resolution"
        / "cycle-12/mission-M50-full-parking-flow"
        / "root_composition_audit.py"
    )
    spec = importlib.util.spec_from_file_location("m50_spine", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def change_degree(macro, removed: int, added: int):
    counts = Counter(macro)
    counts[removed] -= 1
    counts[added] += 1
    return tuple(
        label for label in range(len(macro)) for _ in range(counts[label])
    )


def subtree_sizes(children):
    sizes = [0] * len(children)

    def visit(v):
        sizes[v] = 1 + sum(visit(u) for u in children[v])
        return sizes[v]

    visit(0)
    return sizes


def run(r: int, m50) -> dict:
    macros, adjacency, capacities, _ = m50.exact_instance(r + 1)
    orbit_weight = m50.M41.BASE.orbit_weight
    rates = {
        edge: Fraction(capacity, orbit_weight(edge[0]))
        for edge, capacity in capacities.items()
    }
    alpha = Fraction(2, 3 * r * (r - 1))
    support_failures = []
    unexpected_target_failures = []
    ratio_rows = defaultdict(set)
    all_positive_ratios = set()
    minimum_witness = None
    maximum_witness = None

    for source in sorted(macros):
        comp = m50.root_composition(source)
        children = m50.children(source)
        sizes = subtree_sizes(children)
        degree = m50.degrees(source)
        for branch_index, branch_root in enumerate(children[0]):
            c = comp[branch_index]
            cut_by_size = {}
            parent = branch_root
            while children[parent]:
                child = children[parent][-1]
                cut_by_size[sizes[child]] = parent
                parent = child
            for b_size in range(1, c):
                a_size = c - b_size
                refined = (
                    comp[:branch_index]
                    + (a_size, b_size)
                    + comp[branch_index + 1 :]
                )
                actual_targets = [
                    target
                    for target in adjacency[source]
                    if m50.root_composition(target) == refined
                ]
                observed = sum(
                    (rates[source, target] for target in actual_targets),
                    Fraction(),
                )
                predicted_positive = b_size in cut_by_size
                if (observed > 0) != predicted_positive:
                    support_failures.append(
                        {
                            "source": list(source),
                            "composition": list(comp),
                            "branch_index": branch_index,
                            "split": [a_size, b_size],
                            "observed": str(observed),
                            "right_spine_sizes": sorted(cut_by_size),
                        }
                    )
                    continue
                if not predicted_positive:
                    continue
                cut_parent = cut_by_size[b_size]
                predicted_target = change_degree(source, cut_parent, 0)
                if actual_targets != [predicted_target]:
                    unexpected_target_failures.append(
                        {
                            "source": list(source),
                            "composition": list(comp),
                            "branch_index": branch_index,
                            "split": [a_size, b_size],
                            "parent": cut_parent,
                            "actual_targets": [
                                list(target) for target in actual_targets
                            ],
                            "predicted_target": list(predicted_target),
                        }
                    )
                ratio = observed / alpha
                all_positive_ratios.add(ratio)
                witness = {
                    "source": list(source),
                    "composition": list(comp),
                    "branch_index": branch_index,
                    "split": [a_size, b_size],
                    "cut_parent": cut_parent,
                    "cut_parent_degree": degree[cut_parent],
                    "target": list(predicted_target),
                    "rate": str(observed),
                    "rate_over_alpha": str(ratio),
                }
                if (
                    minimum_witness is None
                    or ratio < Fraction(minimum_witness["rate_over_alpha"])
                ):
                    minimum_witness = witness
                if (
                    maximum_witness is None
                    or ratio > Fraction(maximum_witness["rate_over_alpha"])
                ):
                    maximum_witness = witness
                ratio_rows[
                    (
                        c,
                        a_size,
                        b_size,
                        degree[cut_parent],
                        len(children[cut_parent]),
                    )
                ].add(ratio)

    path_family = []
    for z in range(1, r):
        # z root branches: z-1 singleton branches followed by a path of
        # size r-z+1. Split the final leaf from that path.
        source = tuple([0] * z + list(range(z, r)))
        target = change_degree(source, r - 1, 0)
        observed = rates.get((source, target), Fraction())
        expected_ratio = Fraction(1, math.comb(r - 1, z))
        path_family.append(
            {
                "z": z,
                "source": list(source),
                "composition": list(m50.root_composition(source)),
                "target": list(target),
                "rate": str(observed),
                "rate_over_alpha": str(observed / alpha),
                "expected_rate_over_alpha": str(expected_ratio),
                "matches": observed / alpha == expected_ratio,
            }
        )

    return {
        "r": r,
        "macro_count": len(macros),
        "right_spine_support_failures": support_failures,
        "unique_cut_target_failures": unexpected_target_failures,
        "positive_rate_over_alpha_values": sorted(
            (str(value) for value in all_positive_ratios)
        ),
        "minimum_positive_witness": minimum_witness,
        "maximum_positive_witness": maximum_witness,
        "same_coarse_parameters_rate_variation": [
            {
                "branch_size": key[0],
                "left_size": key[1],
                "right_size": key[2],
                "cut_parent_degree": key[3],
                "cut_parent_child_count": key[4],
                "rate_over_alpha_values": sorted(str(x) for x in values),
            }
            for key, values in ratio_rows.items()
            if len(values) > 1
        ],
        "path_family": path_family,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-max", type=int, default=7)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 2 <= args.r_max <= 7:
        raise SystemExit("bounded exact range is 2 <= r-max <= 7")
    m50 = load_m50()
    result = {
        "claim_tested": (
            "A split of one coarse root branch into (A,B) is positive "
            "exactly when B is a suffix-subtree size on that branch's "
            "rightmost spine, with a unique degree-macro target."
        ),
        "universal_scope": (
            "A failure refutes the support/uniqueness statement.  A finite "
            "pass does not prove its universal plane-tree surgery proof."
        ),
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "seed": None,
        "python": platform.python_version(),
        "git_commit": git_commit(),
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-12/mission-M54-root-mean-lift-referee/"
            "spine_split_audit.py "
            f"--r-max {args.r_max} --output {args.output}"
        ),
        "records": [run(r, m50) for r in range(2, args.r_max + 1)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
