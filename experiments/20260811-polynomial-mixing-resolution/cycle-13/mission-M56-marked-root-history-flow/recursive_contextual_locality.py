#!/usr/bin/env python3
"""Exact falsifier for recursive contextual suffix locality.

For every ambient root-split context through r_max, first form the exact
contextual function on the macro of the branch being split.  Decompose that
local macro at its own root.  A suffix cut of size B must then be zero if the
last root branch is smaller than B, constant on the whole root-composition
fiber if that branch has size B, and depend only on the last branch macro if
that branch is larger than B.  A finite pass proves none of these universal
claims; one collision refutes the corresponding claim.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def load_context_module():
    path = Path(__file__).with_name("split_context_locality.py")
    spec = importlib.util.spec_from_file_location("m56_context", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CTX = load_context_module()
M50 = CTX.M50


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def split_at(comp, index, left):
    part = comp[index]
    return comp[:index] + (left, part - left) + comp[index + 1 :]


def contextual_tables(r):
    macros, adjacency, rates, raw_count = CTX.instance_rates(r)
    alpha = Fraction(2, 3 * r * (r - 1))
    by_comp = defaultdict(list)
    for macro in macros:
        by_comp[M50.root_composition(macro)].append(macro)

    contexts = []
    for coarse, sources in sorted(by_comp.items()):
        intervals_by_source = {
            source: M50.root_intervals(source) for source in sources
        }
        for index, part in enumerate(coarse):
            if part <= 1:
                continue
            for left in range(1, part):
                refined = split_at(coarse, index, left)
                values_by_local = defaultdict(set)
                for source in sources:
                    rate = sum(
                        (
                            rates[source, target]
                            for target in adjacency[source]
                            if M50.root_composition(target) == refined
                        ),
                        Fraction(),
                    )
                    local = M50.local_macro(
                        source, intervals_by_source[source][index]
                    )
                    values_by_local[local].add(rate / alpha)
                contexts.append(
                    {
                        "coarse": coarse,
                        "refined": refined,
                        "branch_index": index,
                        "branch_size": part,
                        "suffix_size": part - left,
                        "values_by_local": values_by_local,
                    }
                )
    return contexts, len(macros), raw_count


def run(r):
    contexts, macro_count, raw_count = contextual_tables(r)
    initial_locality_failures = []
    too_small_support_failures = []
    top_constancy_failures = []
    deep_last_branch_failures = []
    top_groups = 0
    deep_groups = 0

    for context in contexts:
        suffix = context["suffix_size"]
        coarse = context["coarse"]
        refined = context["refined"]
        index = context["branch_index"]
        deep = defaultdict(set)
        top = defaultdict(set)
        for local, values in context["values_by_local"].items():
            if len(values) != 1:
                initial_locality_failures.append(
                    {
                        "coarse": list(coarse),
                        "refined": list(refined),
                        "branch_index": index,
                        "local_macro": list(local),
                        "values": sorted(str(value) for value in values),
                    }
                )
                continue
            value = next(iter(values))
            inner_comp = M50.root_composition(local)
            last_size = inner_comp[-1]
            if last_size < suffix:
                if value:
                    too_small_support_failures.append(
                        {
                            "coarse": list(coarse),
                            "refined": list(refined),
                            "branch_index": index,
                            "local_macro": list(local),
                            "inner_composition": list(inner_comp),
                            "value_over_alpha_r": str(value),
                        }
                    )
            elif last_size == suffix:
                top[inner_comp].add(value)
            else:
                last_interval = M50.root_intervals(local)[-1]
                last_local = M50.local_macro(local, last_interval)
                deep[(inner_comp, last_local)].add(value)

        top_groups += len(top)
        deep_groups += len(deep)
        for inner_comp, values in sorted(top.items()):
            if len(values) > 1:
                top_constancy_failures.append(
                    {
                        "coarse": list(coarse),
                        "refined": list(refined),
                        "branch_index": index,
                        "inner_composition": list(inner_comp),
                        "values_over_alpha_r": sorted(
                            str(value) for value in values
                        ),
                    }
                )
        for (inner_comp, last_local), values in sorted(deep.items()):
            if len(values) > 1:
                deep_last_branch_failures.append(
                    {
                        "coarse": list(coarse),
                        "refined": list(refined),
                        "branch_index": index,
                        "inner_composition": list(inner_comp),
                        "last_branch_macro": list(last_local),
                        "values_over_alpha_r": sorted(
                            str(value) for value in values
                        ),
                    }
                )

    return {
        "r": r,
        "macro_count": macro_count,
        "raw_factorization_count": raw_count,
        "context_count": len(contexts),
        "top_group_count": top_groups,
        "deep_group_count": deep_groups,
        "initial_contextual_locality_failures": initial_locality_failures,
        "too_small_suffix_support_failures": too_small_support_failures,
        "top_cut_constancy_failures": top_constancy_failures,
        "deep_last_branch_locality_failures": deep_last_branch_failures,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-max", type=int, default=7)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 2 <= args.r_max <= 7:
        raise SystemExit("bounded exact range is 2 <= r-max <= 7")
    result = {
        "claim_tested": (
            "Every contextual suffix-cut function recursively depends only "
            "on the last root branch; at equality it is constant on the "
            "fixed root-composition fiber, and below support it vanishes."
        ),
        "finite_scope_warning": (
            "One listed failure refutes its named universal statement. "
            "Finite empty failure lists prove no universal theorem."
        ),
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "python": platform.python_version(),
        "git_commit": git_commit(),
        "seed": None,
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-13/mission-M56-marked-root-history-flow/"
            f"recursive_contextual_locality.py --r-max {args.r_max} "
            f"--output {args.output}"
        ),
        "records": [run(r) for r in range(2, args.r_max + 1)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
