#!/usr/bin/env python3
"""Exact harmonicity/superharmonicity falsifier for contextual means.

The accepted root-composition quotient is divided by alpha_s.  For each
contextual suffix observable inherited from M56, this script computes exact
conditional means on compositions and the off-diagonal generator defect
G_0 h(C)=sum_D r_0(C,D)(h(D)-h(C)) on the deep region last(C)>B.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import platform
import subprocess
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]


def load_recursive():
    path = (
        REPO
        / "experiments/20260811-polynomial-mixing-resolution"
        / "cycle-13/mission-M56-marked-root-history-flow"
        / "recursive_contextual_locality.py"
    )
    spec = importlib.util.spec_from_file_location("m65_m56", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


REC = load_recursive()
M50 = REC.M50


def git_commit():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def compositions(total):
    if total == 0:
        yield ()
        return
    for first in range(1, total + 1):
        if first == total:
            yield (first,)
        else:
            for rest in compositions(total - first):
                yield (first,) + rest


def w(a):
    return Fraction(a ** (a - 1), math.factorial(a))


def normalized_neighbors(comp):
    """Off-diagonal R_s/alpha_s rates, with duplicate targets summed."""
    rates = defaultdict(Fraction)
    k = len(comp)
    for index in range(k - 1):
        merged = (
            comp[:index]
            + (comp[index] + comp[index + 1],)
            + comp[index + 2 :]
        )
        rates[merged] += k
    for index, part in enumerate(comp):
        for left in range(1, part):
            right = part - left
            refined = comp[:index] + (left, right) + comp[index + 1 :]
            rates[refined] += w(left) * w(right) / w(part)
    return rates


def conditional_means(context):
    weighted = defaultdict(lambda: [Fraction(), Fraction()])
    for local, values in context["values_by_local"].items():
        if len(values) != 1:
            raise AssertionError("contextual locality collision")
        comp = M50.root_composition(local)
        mass = Fraction(M50.M41.BASE.orbit_weight(local))
        weighted[comp][0] += mass * next(iter(values))
        weighted[comp][1] += mass
    return {
        comp: numerator / denominator
        for comp, (numerator, denominator) in weighted.items()
    }


def defect_parts(comp, means):
    current = means[comp]
    merge = Fraction()
    split = Fraction()
    k = len(comp)
    for target, rate in normalized_neighbors(comp).items():
        term = rate * (means[target] - current)
        if len(target) < k:
            merge += term
        else:
            split += term
    return merge, split


def sign_class(values):
    if not values or all(value == 0 for value in values):
        return "harmonic"
    if all(value <= 0 for value in values):
        return "superharmonic_G_le_0"
    if all(value >= 0 for value in values):
        return "subharmonic_G_ge_0"
    return "mixed_sign"


def row_for_context(ambient_r, context):
    s = context["branch_size"] - 1
    if s < 2:
        return None
    means = conditional_means(context)
    suffix = context["suffix_size"]
    deep_rows = []
    for comp in sorted(means):
        if comp[-1] <= suffix:
            continue
        merge, split = defect_parts(comp, means)
        deep_rows.append(
            {
                "composition": list(comp),
                "h_over_alpha": str(means[comp]),
                "merge_defect": str(merge),
                "split_defect": str(split),
                "total_defect": str(merge + split),
            }
        )
    defects = [Fraction(row["total_defect"]) for row in deep_rows]
    top_values = sorted(
        {means[comp] for comp in means if comp[-1] == suffix}
    )
    below_nonzero = [
        (comp, means[comp])
        for comp in means
        if comp[-1] < suffix and means[comp] != 0
    ]
    return {
        "ambient_r": ambient_r,
        "local_s": s,
        "coarse": list(context["coarse"]),
        "refined": list(context["refined"]),
        "branch_index": context["branch_index"],
        "suffix_size": suffix,
        "classification_on_deep_region": sign_class(defects),
        "top_values_over_alpha": [str(value) for value in top_values],
        "below_support_nonzero": [
            {"composition": list(comp), "value": str(value)}
            for comp, value in below_nonzero
        ],
        "deep_rows": deep_rows,
    }


def run(ambient_r):
    contexts, macro_count, raw_count = REC.contextual_tables(ambient_r)
    rows = [
        row
        for context in contexts
        if (row := row_for_context(ambient_r, context)) is not None
    ]
    classes = defaultdict(int)
    for row in rows:
        classes[row["classification_on_deep_region"]] += 1
    return {
        "ambient_r": ambient_r,
        "macro_count": macro_count,
        "raw_factorization_count": raw_count,
        "context_count": len(rows),
        "classification_counts": dict(sorted(classes.items())),
        "rows": rows,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-max", type=int, default=7)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 3 <= args.r_max <= 7:
        raise SystemExit("bounded exact range is 3 <= r-max <= 7")
    result = {
        "claim_tested": (
            "Every contextual conditional mean is harmonic, superharmonic, "
            "or a committor on the deep last-branch region for the accepted "
            "root-composition generator."
        ),
        "sign_convention": (
            "G_0 h=sum R/alpha*(h(target)-h(source)); superharmonic means "
            "G_0 h<=0."
        ),
        "finite_scope_warning": (
            "One nonzero or wrong-sign defect refutes the named literal "
            "identity. Finite agreement proves no universal inequality."
        ),
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-14/mission-M65-contextual-quotient-absorption/"
            f"generator_defect.py --r-max {args.r_max} --output {args.output}"
        ),
        "records": [run(r) for r in range(3, args.r_max + 1)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            [
                {
                    "ambient_r": record["ambient_r"],
                    "context_count": record["context_count"],
                    "classification_counts": record[
                        "classification_counts"
                    ],
                }
                for record in result["records"]
            ],
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
