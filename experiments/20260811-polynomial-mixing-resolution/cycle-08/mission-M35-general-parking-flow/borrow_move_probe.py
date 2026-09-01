#!/usr/bin/env python3
"""Audit three-edge borrow--move--return routes for adjacent ideal edges.

Input is the exact projected-rate dump from ``adjacent_bypass_probe.py``.
For x -> y=x-e_i+e_(i+1), a candidate duplicated value h<=i gives

    z=x-e_h+e_i,  w=z-e_i+e_(i+1),  y=w-e_i+e_h.

The script checks exact actual-edge support and stationary capacities and
records plane-tree/prefix metadata that may characterize a universal h.
Finite output is a falsifier only.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path


Macro = tuple[int, ...]


def counts(macro: Macro) -> tuple[int, ...]:
    return tuple(macro.count(i) for i in range(len(macro)))


def macro(vector: tuple[int, ...]) -> Macro:
    return tuple(i for i, multiplicity in enumerate(vector) for _ in range(multiplicity))


def orbit(vector: tuple[int, ...]) -> int:
    answer = math.factorial(sum(vector))
    for multiplicity in vector:
        answer //= math.factorial(multiplicity)
    return answer


def parent_array(vector: tuple[int, ...]) -> tuple[int | None, ...]:
    degrees = vector + (0,)
    parents: list[int | None] = [None]
    stack: list[list[int]] = [[0, degrees[0]]]
    for vertex in range(1, len(degrees)):
        while stack and stack[-1][1] == 0:
            stack.pop()
        if not stack:
            raise AssertionError("invalid Lukasiewicz vector")
        parents.append(stack[-1][0])
        stack[-1][1] -= 1
        stack.append([vertex, degrees[vertex]])
    return tuple(parents)


def feasible(vector: tuple[int, ...]) -> bool:
    total = 0
    for i, multiplicity in enumerate(vector):
        total += multiplicity
        if total < i + 1:
            return False
    return total == len(vector)


def change(vector: tuple[int, ...], source: int, target: int) -> tuple[int, ...]:
    answer = list(vector)
    answer[source] -= 1
    answer[target] += 1
    return tuple(answer)


def run(path: Path) -> dict:
    wrapper = json.loads(path.read_text())
    data = wrapper["records"][-1] if "records" in wrapper else wrapper
    r = data["r"]
    capacity_counts = {}
    for row in data["projected_rates"]:
        source = tuple(row["source"])
        target = tuple(row["target"])
        capacity_counts[source, target] = Fraction(row["capacity_count"])

    records = []
    missing = []
    for row in data["ideal_edge_records"]:
        x = tuple(row["source"])
        y = tuple(row["target"])
        vx = counts(x)
        vy = counts(y)
        delta = [vy[k] - vx[k] for k in range(r)]
        if delta.count(-1) != 1 or delta.count(1) != 1:
            raise AssertionError("ideal edge is not a unit exchange")
        i = delta.index(-1)
        j = delta.index(1)
        if j != i + 1:
            continue

        prefix_surplus = []
        running = 0
        for k, multiplicity in enumerate(vx):
            running += multiplicity
            prefix_surplus.append(running - k - 1)
        parents = parent_array(vx)
        candidates = []
        for h in range(i + 1):
            if vx[h] < 2:
                continue
            vz = change(vx, h, i)
            vw = change(vz, i, j)
            if not (feasible(vz) and feasible(vw) and feasible(vy)):
                continue
            z = macro(vz)
            w = macro(vw)
            route = [x, z, w, y]
            nontrivial_edges = [
                (left, right) for left, right in zip(route, route[1:]) if left != right
            ]
            edge_counts = [capacity_counts.get(edge, Fraction(0)) for edge in nontrivial_edges]
            positive = all(edge_counts)
            # The common stationary normalization T cancels, while the raw
            # capacity count must still be divided by 3(r-1).  Compare each
            # actual stationary capacity to pi(x)/r^2, the universal lower
            # scale used for a positive ideal transition.
            source_orbit = orbit(vx)
            lower_demand_scaled = Fraction(source_orbit, r * r)
            bottleneck_ratio = (
                min(edge_counts) / (3 * (r - 1) * lower_demand_scaled)
                if positive
                else Fraction(0)
            )
            candidates.append(
                {
                    "h": h,
                    "h_is_parent_of_i": parents[i] == h if i else False,
                    "h_is_ancestor_of_i": (
                        h in _ancestors(parents, i) if i else False
                    ),
                    "prefix_surplus_at_h": prefix_surplus[h],
                    "prefix_surplus_before_i": prefix_surplus[i - 1] if i else None,
                    "states": [list(state) for state in route],
                    "edge_capacity_counts": [str(value) for value in edge_counts],
                    "all_edges_positive": positive,
                    "stationary_capacity_over_pi_x_r_minus_2": str(bottleneck_ratio),
                }
            )
        good = [candidate for candidate in candidates if candidate["all_edges_positive"]]
        if not good:
            missing.append({"source": list(x), "target": list(y), "i": i})
        records.append(
            {
                "source": list(x),
                "target": list(y),
                "counts": list(vx),
                "i": i,
                "parents": list(parents),
                "prefix_surplus": prefix_surplus,
                "candidates": candidates,
                "best_ratio": max(
                    (Fraction(candidate["stationary_capacity_over_pi_x_r_minus_2"]) for candidate in good),
                    default=Fraction(0),
                ).__str__(),
            }
        )

    positive_best = [Fraction(record["best_ratio"]) for record in records if Fraction(record["best_ratio"])]
    return {
        "input": str(path),
        "r": r,
        "claim_tested": (
            "Every right adjacent ideal exchange admits a positive actual "
            "borrow--move--return route through some duplicated h<=i."
        ),
        "universal_scope_warning": "Finite support/capacity checks cannot prove the claim.",
        "right_adjacent_edges": len(records),
        "missing_routes": missing,
        "minimum_best_stationary_capacity_ratio_to_pi_x_over_r2": (
            str(min(positive_best)) if positive_best else None
        ),
        "records": records,
    }


def _ancestors(parents: tuple[int | None, ...], vertex: int) -> tuple[int, ...]:
    answer = []
    parent = parents[vertex]
    while parent is not None:
        answer.append(parent)
        parent = parents[parent]
    return tuple(answer)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.input)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    summary = {key: value for key, value in result.items() if key != "records"}
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
