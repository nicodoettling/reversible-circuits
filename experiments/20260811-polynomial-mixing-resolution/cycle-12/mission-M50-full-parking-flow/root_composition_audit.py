#!/usr/bin/env python3
"""Bounded falsifier for the full-Pbar root-composition theorem.

The universal theorem is proved in root_composition_projection.md.  This
script only checks its structural and normalization claims through n <= 8.
It imports the already-audited exact long-cycle projection constructor from
M41, so it enumerates all parking functions and all exact rank-two fibers.
"""

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


Macro = tuple[int, ...]
Composition = tuple[int, ...]


def load_m41():
    repo = Path(__file__).resolve().parents[4]
    path = (
        repo
        / "experiments/20260811-polynomial-mixing-resolution"
        / "cycle-09/mission-M41-adjacent-parking-flow"
        / "exact_widest_congestion.py"
    )
    spec = importlib.util.spec_from_file_location("m41_exact", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M41 = load_m41()
INSTANCE_CACHE = {}


def exact_instance(n: int):
    if n not in INSTANCE_CACHE:
        INSTANCE_CACHE[n] = M41.build_instance(n)
    return INSTANCE_CACHE[n]


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def degrees(macro: Macro) -> list[int]:
    r = len(macro)
    return [macro.count(i) for i in range(r)] + [0]


def children(macro: Macro) -> list[list[int]]:
    """Children of the unique preorder plane tree with this degree word."""
    d = degrees(macro)
    answer = [[] for _ in d]
    stack = [[0, d[0]]]
    for vertex in range(1, len(d)):
        while stack and stack[-1][1] == 0:
            stack.pop()
        if not stack:
            raise AssertionError("invalid Lukasiewicz degree word")
        parent = stack[-1][0]
        answer[parent].append(vertex)
        stack[-1][1] -= 1
        stack.append([vertex, d[vertex]])
    return answer


def root_composition(macro: Macro) -> Composition:
    ch = children(macro)

    def subtree_size(v: int) -> int:
        return 1 + sum(subtree_size(u) for u in ch[v])

    return tuple(subtree_size(v) for v in ch[0])


def root_intervals(macro: Macro) -> list[tuple[int, int]]:
    """Closed preorder intervals of the root branches."""
    d = degrees(macro)
    answer = []
    start = 1
    for _ in range(d[0]):
        balance = 0
        for vertex in range(start, len(d)):
            balance += d[vertex] - 1
            if balance == -1:
                answer.append((start, vertex))
                start = vertex + 1
                break
    return answer


def local_macro(macro: Macro, interval: tuple[int, int]) -> Macro:
    """Standardized parking macro of one root-child subtree."""
    d = degrees(macro)
    first, last = interval
    return tuple(
        local
        for local in range(last - first)
        for _ in range(d[first + local])
    )


def unit_exchange(source: Macro, target: Macro) -> tuple[int, int]:
    r = len(source)
    a = Counter(source)
    b = Counter(target)
    removed = [i for i in range(r) if a[i] > b[i]]
    added = [i for i in range(r) if a[i] < b[i]]
    if len(removed) != 1 or len(added) != 1:
        raise AssertionError("off-diagonal macro edge is not a unit exchange")
    return removed[0], added[0]


def target_after_exchange(source: Macro, h: int, j: int) -> Macro:
    c = Counter(source)
    c[h] -= 1
    c[j] += 1
    return tuple(i for i in range(len(source)) for _ in range(c[i]))


def w(a: int) -> Fraction:
    if a < 1:
        raise ValueError("branch size must be positive")
    return Fraction(a ** (a - 1), math.factorial(a))


def z(edges: int) -> Fraction:
    if edges == 0:
        return Fraction(1)
    return Fraction((edges + 1) ** (edges - 1), math.factorial(edges))


def composition_weight(comp: Composition) -> Fraction:
    answer = Fraction(1, math.factorial(len(comp)))
    for part in comp:
        answer *= w(part)
    return answer


def refinement_coefficient(total: int, parts: int) -> Fraction:
    """[u^total] T(u)^parts for T=u exp(T)."""
    if not 1 <= parts <= total:
        return Fraction()
    return Fraction(
        parts * total ** (total - parts),
        total * math.factorial(total - parts),
    )


def basin_ratio(first_part: int, suffix_length: int) -> Fraction:
    numerator = Fraction()
    for p in range(1, first_part + 1):
        numerator += Fraction(
            math.factorial(suffix_length + 1),
            math.factorial(p + suffix_length),
        ) * refinement_coefficient(first_part, p)
    return numerator / w(first_part)


def run(n: int) -> dict:
    r = n - 1
    macros, adjacency, capacities, raw_count = exact_instance(n)
    orbit_weight = M41.BASE.orbit_weight
    rates = {
        edge: capacity / orbit_weight(edge[0])
        for edge, capacity in capacities.items()
    }

    upward_support_failures = []
    boundary_rate_failures = []
    root_merge_failures = []
    reverse_split_lumpability_witness = None
    internal_product_scaling_failures = []

    for source in sorted(macros):
        d = degrees(source)
        ch = children(source)
        actual_up = defaultdict(dict)
        for target in adjacency[source]:
            h, j = unit_exchange(source, target)
            if h < j:
                actual_up[h][j] = rates[source, target]

        allowed = defaultdict(set)
        for h, child_roots in enumerate(ch):
            for child_root in child_roots[:-1]:
                j = child_root
                while True:
                    allowed[h].add(j)
                    if not ch[j]:
                        break
                    j = ch[j][-1]
        for h, destinations in actual_up.items():
            extras = set(destinations) - allowed[h]
            if extras:
                upward_support_failures.append(
                    {
                        "source": list(source),
                        "h": h,
                        "extra_destinations": sorted(extras),
                    }
                )

        for h, child_roots in enumerate(ch):
            for child_root in child_roots[:-1]:
                spine = []
                j = child_root
                while True:
                    spine.append(j)
                    if not ch[j]:
                        break
                    j = ch[j][-1]
                observed = sum(
                    (
                        rates.get(
                            (source, target_after_exchange(source, h, j)),
                            Fraction(),
                        )
                        for j in spine
                    ),
                    Fraction(),
                )
                expected = Fraction(2 * d[h], 3 * r * (r - 1))
                if observed != expected:
                    boundary_rate_failures.append(
                        {
                            "source": list(source),
                            "h": h,
                            "child_root": child_root,
                            "spine": spine,
                            "observed": str(observed),
                            "expected": str(expected),
                        }
                    )

    # A root-composition restriction must be the exact weighted product of
    # smaller full projections.  This is checked edge by edge.
    for (source, target), observed in sorted(rates.items()):
        if root_composition(source) != root_composition(target):
            continue
        source_intervals = root_intervals(source)
        target_intervals = root_intervals(target)
        if source_intervals != target_intervals:
            internal_product_scaling_failures.append(
                {
                    "source": list(source),
                    "target": list(target),
                    "reason": "same composition but unequal intervals",
                }
            )
            continue
        changed = [
            interval
            for interval in source_intervals
            if local_macro(source, interval) != local_macro(target, interval)
        ]
        if len(changed) != 1:
            internal_product_scaling_failures.append(
                {
                    "source": list(source),
                    "target": list(target),
                    "reason": f"changed branch count {len(changed)}",
                }
            )
            continue
        interval = changed[0]
        local_source = local_macro(source, interval)
        local_target = local_macro(target, interval)
        s = len(local_source)
        if s < 2:
            internal_product_scaling_failures.append(
                {
                    "source": list(source),
                    "target": list(target),
                    "reason": "nontrivial update in singleton branch",
                }
            )
            continue
        _, _, local_capacities, _ = exact_instance(s + 1)
        local_capacity = local_capacities.get((local_source, local_target))
        if local_capacity is None:
            expected = Fraction()
        else:
            expected = (
                Fraction(local_capacity, orbit_weight(local_source))
                * Fraction(s * (s - 1), r * (r - 1))
            )
        if observed != expected:
            internal_product_scaling_failures.append(
                {
                    "source": list(source),
                    "target": list(target),
                    "branch_interval": list(interval),
                    "observed": str(observed),
                    "expected": str(expected),
                }
            )

    by_comp = defaultdict(list)
    for macro in macros:
        by_comp[root_composition(macro)].append(macro)

    quotient_flow = defaultdict(Fraction)
    comp_mass = {
        comp: sum(
            (Fraction(orbit_weight(m), raw_count) for m in states),
            Fraction(),
        )
        for comp, states in by_comp.items()
    }
    for (source, target), capacity in capacities.items():
        a = root_composition(source)
        b = root_composition(target)
        if a != b:
            quotient_flow[a, b] += Fraction(capacity, raw_count)

    for comp in sorted(by_comp):
        k = len(comp)
        for p in range(k - 1):
            merged = comp[:p] + (comp[p] + comp[p + 1],) + comp[p + 2 :]
            observed = quotient_flow[comp, merged] / comp_mass[comp]
            expected = Fraction(2 * k, 3 * r * (r - 1))
            reverse_observed = quotient_flow[merged, comp] / comp_mass[merged]
            reverse_expected = Fraction(2, 3 * r * (r - 1)) * (
                w(comp[p]) * w(comp[p + 1]) / w(comp[p] + comp[p + 1])
            )
            if observed != expected or reverse_observed != reverse_expected:
                root_merge_failures.append(
                    {
                        "source_composition": list(comp),
                        "target_composition": list(merged),
                        "forward_observed": str(observed),
                        "forward_expected": str(expected),
                        "reverse_observed": str(reverse_observed),
                        "reverse_expected": str(reverse_expected),
                    }
                )

    # Strong lumpability is not used.  Record the first exact reverse-split
    # witness where two shapes in one coarse composition have different exit
    # rates to the same refined composition.
    for coarse, states in sorted(by_comp.items()):
        targets = {
            root_composition(target)
            for source in states
            for target in adjacency[source]
            if len(root_composition(target)) == len(coarse) + 1
        }
        for refined in sorted(targets):
            values = []
            for source in sorted(states):
                value = sum(
                    (
                        rates[source, target]
                        for target in adjacency[source]
                        if root_composition(target) == refined
                    ),
                    Fraction(),
                )
                values.append((source, value))
            if len({value for _, value in values}) > 1:
                reverse_split_lumpability_witness = {
                    "coarse_composition": list(coarse),
                    "refined_composition": list(refined),
                    "shape_rates": [
                        {"macro": list(macro), "rate": str(value)}
                        for macro, value in values
                    ],
                }
                break
        if reverse_split_lumpability_witness is not None:
            break

    max_basin = Fraction()
    max_basin_parameters = None
    for first_part in range(1, r + 1):
        for suffix_length in range(0, r - first_part + 1):
            value = basin_ratio(first_part, suffix_length)
            if value > max_basin:
                max_basin = value
                max_basin_parameters = [first_part, suffix_length]

    return {
        "n": n,
        "r": r,
        "raw_factorization_count": raw_count,
        "macro_count": len(macros),
        "root_composition_count": len(by_comp),
        "upward_right_spine_support_failures": upward_support_failures,
        "per_boundary_rate_failures": boundary_rate_failures,
        "root_quotient_formula_failures": root_merge_failures,
        "internal_product_scaling_failures": (
            internal_product_scaling_failures
        ),
        "first_reverse_split_nonlumpability_witness": (
            reverse_split_lumpability_witness
        ),
        "maximum_left_merge_basin_ratio": str(max_basin),
        "maximum_left_merge_basin_parameters": max_basin_parameters,
        "basin_ratio_less_than_e": float(max_basin) < math.e,
        "r2_calibration": (
            {
                "merge": str(
                    quotient_flow.get(((1, 1), (2,)), Fraction())
                    / comp_mass.get((1, 1), Fraction(1))
                ),
                "split": str(
                    quotient_flow.get(((2,), (1, 1)), Fraction())
                    / comp_mass.get((2,), Fraction(1))
                ),
            }
            if r == 2
            else None
        ),
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
            "Exact right-spine support, per-child-boundary rate, and root "
            "composition quotient formulas for the full Pbar chain."
        ),
        "universal_scope": (
            "Failures refute the named theorem; finite passes do not prove it. "
            "The theorem is proved separately in root_composition_projection.md."
        ),
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "seed": None,
        "python": platform.python_version(),
        "git_commit": git_commit(),
        "command": (
            "python3 experiments/20260811-polynomial-mixing-resolution/"
            "cycle-12/mission-M50-full-parking-flow/root_composition_audit.py "
            f"--n-max {args.n_max} --output {args.output}"
        ),
        "records": [run(n) for n in range(3, args.n_max + 1)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
