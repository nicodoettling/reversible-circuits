#!/usr/bin/env python3
"""Exact bounded audit of contextual conditional-mean quotient energy.

For every ambient split context through r_max, localize its rate to the
affected branch, condition that local observable on the branch's own root
composition, and compute the exact electrical energy on the accepted
root-composition quotient.  This tests the coefficient that multiplies
recursively generated fine target biases in a naive quotient
disintegration.  Finite values do not establish an asymptotic bound.
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

import numpy as np
from scipy.linalg import eigh


def load_recursive():
    path = Path(__file__).with_name("recursive_contextual_locality.py")
    spec = importlib.util.spec_from_file_location("m56_recursive", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


REC = load_recursive()
M50 = REC.M50


def git_commit() -> str:
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


def rho_unnormalized(comp):
    answer = Fraction(1, math.factorial(len(comp)))
    for part in comp:
        answer *= w(part)
    return answer


def merge_at(comp, index):
    return (
        comp[:index]
        + (comp[index] + comp[index + 1],)
        + comp[index + 2 :]
    )


def quotient_laplacian(s):
    comps = list(compositions(s))
    index = {comp: i for i, comp in enumerate(comps)}
    weights = [rho_unnormalized(comp) for comp in comps]
    total = sum(weights, Fraction())
    rho = np.array([float(value / total) for value in weights])
    # Divide all rates by alpha_s.  A fixed merge boundary then has rate k.
    laplacian = np.zeros((len(comps), len(comps)))
    for comp in comps:
        k = len(comp)
        if k < 2:
            continue
        i = index[comp]
        for boundary in range(k - 1):
            merged = merge_at(comp, boundary)
            j = index[merged]
            capacity = float(Fraction(weights[i], total) * k)
            laplacian[i, i] += capacity
            laplacian[j, j] += capacity
            laplacian[i, j] -= capacity
            laplacian[j, i] -= capacity
    return comps, index, rho, laplacian


def hminus(laplacian, linear, tolerance=1e-11):
    values, vectors = eigh(laplacian)
    answer = 0.0
    residual = 0.0
    for value, vector in zip(values, vectors.T):
        projection = float(vector @ linear)
        if value <= tolerance:
            residual = max(residual, abs(projection))
        else:
            answer += projection * projection / float(value)
    return answer, residual


def run(ambient_r):
    contexts, macro_count, raw_count = REC.contextual_tables(ambient_r)
    quotient_cache = {}
    rows = []
    maximum = None
    for context in contexts:
        s = context["branch_size"] - 1
        if s < 2:
            continue
        if s not in quotient_cache:
            quotient_cache[s] = quotient_laplacian(s)
        comps, comp_index, rho, laplacian = quotient_cache[s]
        weighted = defaultdict(lambda: [Fraction(), Fraction()])
        for local, values in context["values_by_local"].items():
            if len(values) != 1:
                raise AssertionError("contextual locality collision")
            comp = M50.root_composition(local)
            weight = Fraction(M50.M41.BASE.orbit_weight(local))
            weighted[comp][0] += weight * next(iter(values))
            weighted[comp][1] += weight
        means = np.zeros(len(comps))
        for comp, (numerator, denominator) in weighted.items():
            means[comp_index[comp]] = float(numerator / denominator)
        mean = float(rho @ means)
        continuation_mass = float(
            sum(
                rho[comp_index[comp]] * means[comp_index[comp]]
                for comp in comps
                if comp[-1] > context["suffix_size"]
            )
        )
        continuation_fraction = (
            continuation_mass / mean if mean > 0 else 0.0
        )
        variance = float(rho @ ((means - mean) ** 2))
        linear = rho * (means - mean)
        norm, residual = hminus(laplacian, linear)
        # The physical observable is alpha_s*phi and the physical quotient
        # is alpha_s times the normalized quotient.  Both alpha_s factors
        # cancel, leaving norm/mean.
        coefficient = norm / mean if mean > 0 else 0.0
        row = {
            "ambient_r": ambient_r,
            "local_s": s,
            "coarse": list(context["coarse"]),
            "refined": list(context["refined"]),
            "branch_index": context["branch_index"],
            "suffix_size": context["suffix_size"],
            "conditional_mean_over_alpha": mean,
            "conditional_mean_variance": variance,
            "deep_continuation_fraction": continuation_fraction,
            "normalized_quotient_energy_over_mean": coefficient,
            "continuation_plus_quotient_coefficient": (
                continuation_fraction + coefficient
            ),
            "nullspace_residual": residual,
        }
        rows.append(row)
        if maximum is None or coefficient > maximum[
            "normalized_quotient_energy_over_mean"
        ]:
            maximum = row
    return {
        "ambient_r": ambient_r,
        "macro_count": macro_count,
        "raw_factorization_count": raw_count,
        "context_count_with_local_s_at_least_2": len(rows),
        "maximum": maximum,
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
            "The root-composition conditional mean of every contextual "
            "split has controlled quotient electrical energy; this is the "
            "coefficient that weights fine target-bias recursion."
        ),
        "finite_scope_warning": (
            "A nullspace residual would refute routability on the quotient. "
            "Finite bounded coefficients prove no universal or additive "
            "occupation inequality."
        ),
        "normalization": (
            "Rates and Laplacian are divided by alpha_s; the reported "
            "energy/mean equals the physical coefficient because the "
            "alpha_s factors cancel."
        ),
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "python": platform.python_version(),
        "numpy": np.__version__,
        "git_commit": git_commit(),
        "seed": None,
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-13/mission-M56-marked-root-history-flow/"
            f"contextual_macro_energy.py --r-max {args.r_max} "
            f"--output {args.output}"
        ),
        "records": [run(r) for r in range(3, args.r_max + 1)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
