#!/usr/bin/env python3
"""Exact bounded probe for reverse root-split/right-spine geometry.

This script is a falsifier only.  It records every root split from a unary
root parking macro through n<=8, together with the rightmost-spine suffix
sizes of the source plane tree.  The universal claim under test is that a
positive split (A,B) is supported exactly when B is a proper suffix-subtree
size on that spine; finite agreement cannot prove the claim.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
from fractions import Fraction
from pathlib import Path


def load_m50():
    repo = Path(__file__).resolve().parents[4]
    path = (
        repo
        / "experiments/20260811-polynomial-mixing-resolution"
        / "cycle-12/mission-M50-full-parking-flow"
        / "root_composition_audit.py"
    )
    spec = importlib.util.spec_from_file_location("m50_root", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M50 = load_m50()


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def subtree_sizes(children: list[list[int]]) -> list[int]:
    answer = [0] * len(children)

    def visit(v: int) -> int:
        answer[v] = 1 + sum(visit(u) for u in children[v])
        return answer[v]

    visit(0)
    return answer


def right_spine_data(macro: tuple[int, ...]) -> list[dict]:
    children = M50.children(macro)
    sizes = subtree_sizes(children)
    if len(children[0]) != 1:
        raise AssertionError("source is not root-unary")
    data = []
    vertex = children[0][-1]
    first = True
    while True:
        if not first:
            parent = next(
                p for p, row in enumerate(children) if vertex in row
            )
            data.append(
                {
                    "vertex": vertex,
                    "parent": parent,
                    "suffix_size": sizes[vertex],
                    "parent_degree": len(children[parent]),
                    "vertex_degree": len(children[vertex]),
                }
            )
        first = False
        if not children[vertex]:
            break
        vertex = children[vertex][-1]
    return data


def run(n: int) -> dict:
    r = n - 1
    macros, adjacency, capacities, _ = M50.exact_instance(n)
    orbit_weight = M50.M41.BASE.orbit_weight
    alpha = Fraction(2, 3 * r * (r - 1))
    records = []
    failures = []
    for source in sorted(macros):
        if M50.root_composition(source) != (r,):
            continue
        spine = right_spine_data(source)
        suffixes = {row["suffix_size"] for row in spine}
        splits = []
        for target in adjacency[source]:
            comp = M50.root_composition(target)
            if len(comp) != 2:
                continue
            rate = Fraction(capacities[source, target], orbit_weight(source))
            row = {
                "target": list(target),
                "composition": list(comp),
                "rate": str(rate),
                "rate_over_alpha": str(rate / alpha),
                "right_size_on_spine": comp[1] in suffixes,
            }
            splits.append(row)
            if comp[1] not in suffixes:
                failures.append(
                    {
                        "source": list(source),
                        "spine_suffixes": sorted(suffixes),
                        **row,
                    }
                )
        supported = {tuple(row["composition"]) for row in splits}
        missing = [
            b for b in sorted(suffixes)
            if (r - b, b) not in supported
        ]
        if missing:
            failures.append(
                {
                    "source": list(source),
                    "missing_spine_suffix_splits": missing,
                }
            )
        records.append(
            {
                "source": list(source),
                "spine": spine,
                "splits": splits,
                "total_rate_over_alpha": str(
                    sum(
                        Fraction(row["rate_over_alpha"])
                        for row in splits
                    )
                ),
            }
        )
    return {
        "n": n,
        "r": r,
        "unary_macro_count": len(records),
        "support_failures": failures,
        "records": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 3 <= args.n_max <= 8:
        raise SystemExit("bounded exact range is 3 <= n-max <= 8")
    result = {
        "claim_tested": (
            "A unary-root split (A,B) is positive exactly when B is a "
            "proper right-spine suffix-subtree size."
        ),
        "finite_scope_warning": (
            "A failure refutes the support claim; finite success cannot "
            "prove the universal right-spine characterization."
        ),
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "records": [run(n) for n in range(3, args.n_max + 1)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
