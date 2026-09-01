#!/usr/bin/env python3
"""Exact falsifier for harmonicity under canonical quotient subgenerators."""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_main():
    path = HERE / "generator_defect.py"
    spec = importlib.util.spec_from_file_location("m65_generator", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


G = load_main()


def git_commit():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def merge(comp, index):
    return (
        comp[:index]
        + (comp[index] + comp[index + 1],)
        + comp[index + 2 :]
    )


def split(comp, index, left):
    part = comp[index]
    return comp[:index] + (left, part - left) + comp[index + 1 :]


def defect(comp, means, mode):
    current = means[comp]
    k = len(comp)
    answer = Fraction()
    if mode == "first_boundary":
        merge_indices = [0] if k >= 2 else []
        split_indices = [0]
    elif mode == "last_boundary":
        merge_indices = [k - 2] if k >= 2 else []
        split_indices = [k - 1]
    elif mode == "prefix_only":
        merge_indices = list(range(max(0, k - 2)))
        split_indices = list(range(max(0, k - 1)))
    elif mode == "last_part_only":
        merge_indices = [k - 2] if k >= 2 else []
        split_indices = [k - 1]
    else:
        raise ValueError(mode)
    for index in merge_indices:
        target = merge(comp, index)
        answer += k * (means[target] - current)
    for index in split_indices:
        part = comp[index]
        for left in range(1, part):
            target = split(comp, index, left)
            answer += (
                G.w(left)
                * G.w(part - left)
                / G.w(part)
                * (means[target] - current)
            )
    return answer


def row_for_context(ambient_r, context):
    s = context["branch_size"] - 1
    if s < 2:
        return None
    means = G.conditional_means(context)
    suffix = context["suffix_size"]
    modes = ["first_boundary", "last_boundary", "prefix_only"]
    mode_rows = {}
    for mode in modes:
        rows = []
        for comp in sorted(means):
            if comp[-1] <= suffix:
                continue
            value = defect(comp, means, mode)
            rows.append(
                {
                    "composition": list(comp),
                    "h_over_alpha": str(means[comp]),
                    "defect": str(value),
                }
            )
        mode_rows[mode] = {
            "classification": G.sign_class(
                [Fraction(row["defect"]) for row in rows]
            ),
            "deep_rows": rows,
        }
    return {
        "ambient_r": ambient_r,
        "local_s": s,
        "coarse": list(context["coarse"]),
        "refined": list(context["refined"]),
        "branch_index": context["branch_index"],
        "suffix_size": suffix,
        "modes": mode_rows,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-max", type=int, default=7)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 3 <= args.r_max <= 7:
        raise SystemExit("bounded exact range is 3 <= r-max <= 7")
    records = []
    for ambient_r in range(3, args.r_max + 1):
        contexts = G.REC.contextual_tables(ambient_r)[0]
        rows = [
            row
            for context in contexts
            if (row := row_for_context(ambient_r, context)) is not None
        ]
        counts = {}
        for mode in ("first_boundary", "last_boundary", "prefix_only"):
            mode_counts = {}
            for row in rows:
                cls = row["modes"][mode]["classification"]
                mode_counts[cls] = mode_counts.get(cls, 0) + 1
            counts[mode] = dict(sorted(mode_counts.items()))
        records.append(
            {
                "ambient_r": ambient_r,
                "classification_counts": counts,
                "rows": rows,
            }
        )
    result = {
        "claim_tested": (
            "Contextual conditional means are harmonic or one-sign under "
            "canonical first-boundary, last-boundary, or prefix quotient "
            "subgenerators on the deep region."
        ),
        "sign_convention": (
            "G h=sum normalized_rate*(h(target)-h(source)); "
            "superharmonic means G h<=0."
        ),
        "finite_scope_warning": (
            "A mixed/nonzero defect refutes the corresponding literal "
            "identity. Finite passes prove no universal comparison."
        ),
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-14/mission-M65-contextual-quotient-absorption/"
            f"subgenerator_probe.py --r-max {args.r_max} --output {args.output}"
        ),
        "records": records,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            [
                {
                    "ambient_r": row["ambient_r"],
                    "classification_counts": row["classification_counts"],
                }
                for row in records
            ],
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
