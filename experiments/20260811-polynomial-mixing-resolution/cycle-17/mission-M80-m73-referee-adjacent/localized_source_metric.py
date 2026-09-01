#!/usr/bin/env python3
"""Finite diagnostic for localized refinements of M73's source metric.

The proposed proof route replaces an arbitrary second chord inside a
shared-factor clique by endpoint-slide moves. This script tests connectivity,
diameter, and two-step TV scaling. Results are finite numeric evidence only.
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import platform
import subprocess
import sys
from pathlib import Path

import numpy as np


Perm = tuple[int, ...]


def mul(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[i]] for i in range(len(p)))


def inv(p: Perm) -> Perm:
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def edge_perm(n: int, i: int, j: int) -> Perm:
    p = list(range(n))
    p[i], p[j] = p[j], p[i]
    return tuple(p)


def edge_of(p: Perm) -> frozenset[int]:
    return frozenset(i for i, j in enumerate(p) if i != j)


def cycle_sizes(p: Perm) -> list[int]:
    seen: set[int] = set()
    answer: list[int] = []
    for start in range(len(p)):
        if start in seen:
            continue
        x = start
        size = 0
        while x not in seen:
            seen.add(x)
            size += 1
            x = p[x]
        answer.append(size)
    return answer


def nontrivial_cycles(p: Perm) -> list[list[int]]:
    seen: set[int] = set()
    answer: list[list[int]] = []
    for start in range(len(p)):
        if start in seen:
            continue
        cycle: list[int] = []
        x = start
        while x not in seen:
            seen.add(x)
            cycle.append(x)
            x = p[x]
        if len(cycle) > 1:
            answer.append(cycle)
    return answer


def descriptor(p: Perm, h: Perm) -> dict[str, object]:
    moved = sorted(i for i, j in enumerate(p) if i != j)
    gaps = [
        (moved[(offset + 1) % len(moved)] - moved[offset]) % len(p)
        for offset in range(len(moved))
    ]
    return {
        "cycles": nontrivial_cycles(p),
        "support_gaps": gaps,
        "residual_sizes": sorted(cycle_sizes(mul(inv(p), h)), reverse=True),
    }


def count_minimal(p: Perm, r: int) -> int:
    sizes = cycle_sizes(p)
    if len(p) - len(sizes) != r:
        return 0
    answer = math.factorial(r)
    for d in sizes:
        if d > 1:
            answer = answer * d ** (d - 2) // math.factorial(d - 1)
    return answer


def theta(p: Perm, h: Perm, h_inv: Perm) -> Perm:
    return mul(h_inv, mul(p, h))


def graph_stats(adjacency: list[set[int]]) -> tuple[bool, int | None]:
    q = len(adjacency)
    diameter = 0
    for source in range(q):
        distances = [-1] * q
        distances[source] = 0
        queue = collections.deque([source])
        while queue:
            i = queue.popleft()
            for j in adjacency[i]:
                if distances[j] < 0:
                    distances[j] = distances[i] + 1
                    queue.append(j)
        if -1 in distances:
            return False, None
        diameter = max(diameter, max(distances))
    return True, diameter


def analyze(n: int) -> dict[str, object]:
    h = tuple((i + 1) % n for i in range(n))
    h_inv = inv(h)
    gates = [edge_perm(n, i, j) for i in range(n) for j in range(i + 1, n)]
    edges = {g: edge_of(g) for g in gates}
    pair_lifts: list[tuple[Perm, Perm, Perm]] = []
    multiplicity: collections.Counter[Perm] = collections.Counter()
    for a in gates:
        for b in gates:
            product = mul(a, b)
            multiplicity[product] += 1
            pair_lifts.append((a, b, product))

    marginal: dict[Perm, int] = {}
    for g, a_g in multiplicity.items():
        value = a_g * count_minimal(mul(inv(g), h), n - 3)
        if value:
            marginal[g] = value

    orbit_of: dict[Perm, int] = {}
    orbits: list[list[Perm]] = []
    for g in sorted(marginal):
        if g in orbit_of:
            continue
        orbit = []
        x = g
        while x not in orbit:
            orbit.append(x)
            x = theta(x, h, h_inv)
        oid = len(orbits)
        for x in orbit:
            orbit_of[x] = oid
        orbits.append(orbit)
    q = len(orbits)

    kernel = np.zeros((q, q), dtype=float)
    for source, orbit in enumerate(orbits):
        g = orbit[0]
        denominator = count_minimal(mul(inv(g), h), n - 3)
        for s in marginal:
            kernel[source, orbit_of[s]] += (
                multiplicity[s]
                * count_minimal(mul(inv(mul(g, s)), h), n - 5)
                / denominator
            )
    squared = kernel @ kernel

    # For each literal shared coordinate token, retain the differing chord.
    token_records: dict[tuple[int, Perm], list[tuple[Perm, int]]] = (
        collections.defaultdict(list)
    )
    for a, b, product in pair_lifts:
        source = orbit_of.get(product)
        if source is None:
            continue
        token_records[(0, a)].append((b, source))
        token_records[(1, b)].append((a, source))

    metric_edges: dict[str, set[tuple[int, int]]] = {
        "arbitrary_replacement": set(),
        "differing_chords_share_endpoint": set(),
        "unit_endpoint_slide": set(),
        "unit_slide_same_product_kind": set(),
        "unit_slide_changes_product_kind": set(),
    }
    source_kind = [
        "3" if len(nontrivial_cycles(orbit[0])) == 1 else "D"
        for orbit in orbits
    ]
    for records in token_records.values():
        # Deduplicate a repeated (other chord, quotient orbit) record.
        records = sorted(set(records))
        for offset, (b, source) in enumerate(records):
            eb = edges[b]
            for bp, target in records[offset + 1:]:
                if source == target:
                    continue
                pair = tuple(sorted((source, target)))
                metric_edges["arbitrary_replacement"].add(pair)
                ebp = edges[bp]
                intersection = eb & ebp
                if len(intersection) != 1:
                    continue
                metric_edges["differing_chords_share_endpoint"].add(pair)
                changed = list(eb ^ ebp)
                if len(changed) == 2 and (
                    (changed[0] - changed[1]) % n in (1, n - 1)
                ):
                    metric_edges["unit_endpoint_slide"].add(pair)
                    if source_kind[source] == source_kind[target]:
                        metric_edges["unit_slide_same_product_kind"].add(pair)
                    else:
                        metric_edges["unit_slide_changes_product_kind"].add(pair)

    records = []
    for name, edge_set in metric_edges.items():
        adjacency = [set() for _ in range(q)]
        maximum = 0.0
        witness = None
        for i, j in edge_set:
            adjacency[i].add(j)
            adjacency[j].add(i)
            distance = 0.5 * float(np.sum(np.abs(squared[i] - squared[j])))
            if distance > maximum:
                maximum = distance
                witness = (i, j)
        connected, diameter = graph_stats(adjacency)
        target_layer_breakdown = None
        top_target_differences = None
        if witness is not None:
            difference = squared[witness[0]] - squared[witness[1]]
            layers: dict[tuple[str, int], dict[str, float | int]] = {}
            for target, value in enumerate(difference):
                target_residual = cycle_sizes(mul(inv(orbits[target][0]), h))
                key = (source_kind[target], min(target_residual))
                layer = layers.setdefault(key, {
                    "target_orbits": 0,
                    "signed_difference": 0.0,
                    "absolute_difference": 0.0,
                })
                layer["target_orbits"] += 1
                layer["signed_difference"] += float(value)
                layer["absolute_difference"] += abs(float(value))
            target_layer_breakdown = [
                {
                    "target_kind": key[0],
                    "minimum_target_residual_size": key[1],
                    **value,
                    "n_squared_times_absolute_difference": (
                        n ** 2 * value["absolute_difference"]
                    ),
                }
                for key, value in sorted(layers.items())
            ]
            top_targets = sorted(
                range(q), key=lambda target: abs(difference[target]), reverse=True
            )[:10]
            top_target_differences = [
                {
                    "target_orbit": target,
                    "signed_difference": float(difference[target]),
                    "n_squared_times_signed_difference": (
                        n ** 2 * float(difference[target])
                    ),
                    "descriptor": descriptor(orbits[target][0], h),
                }
                for target in top_targets
            ]
        records.append({
            "metric": name,
            "edges": len(edge_set),
            "connected": connected,
            "diameter": diameter,
            "maximum_edge_TV_K2": maximum,
            "n_squared_times_maximum": n ** 2 * maximum,
            "n_cubed_times_maximum": n ** 3 * maximum,
            "diameter_times_maximum": (
                diameter * maximum if diameter is not None else None
            ),
            "n_squared_times_diameter_times_maximum": (
                n ** 2 * diameter * maximum if diameter is not None else None
            ),
            "witness_orbits": list(witness) if witness is not None else None,
            "witness_descriptors": (
                [descriptor(orbits[i][0], h) for i in witness]
                if witness is not None else None
            ),
            "witness_target_layer_breakdown": target_layer_breakdown,
            "witness_top_target_differences": top_target_differences,
        })
    return {"n": n, "quotient_states": q, "metrics": records}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", nargs="+", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "status": "finite_numeric_diagnostic_only",
        "claim_tested": (
            "Endpoint-slide refinement of shared-factor adjacency has a "
            "polynomial diameter and a sharper per-edge K^2 influence."
        ),
        "convention": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
        "results": [analyze(n) for n in args.n],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
