#!/usr/bin/env python3
"""Exact/floating diagnostics for M83 endpoint-sharing influence.

The kernel is exact through construction; output probabilities are converted
to float unless ``--exact`` is requested.  Convention: (pq)(x)=p(q(x));
factor tuples multiply left-to-right.  This is a finite diagnostic only.
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import platform
import subprocess
import sys
from fractions import Fraction
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


def cycles(p: Perm) -> list[list[int]]:
    seen: set[int] = set()
    out: list[list[int]] = []
    for start in range(len(p)):
        if start in seen:
            continue
        c: list[int] = []
        x = start
        while x not in seen:
            seen.add(x)
            c.append(x)
            x = p[x]
        out.append(c)
    return out


def cycle_sizes(p: Perm) -> list[int]:
    return sorted((len(c) for c in cycles(p)), reverse=True)


def count_minimal(p: Perm, r: int) -> int:
    sizes = cycle_sizes(p)
    if len(p) - len(sizes) != r:
        return 0
    out = math.factorial(r)
    for d in sizes:
        if d > 1:
            out = out * d ** (d - 2) // math.factorial(d - 1)
    return out


def theta(p: Perm, h: Perm, hi: Perm) -> Perm:
    return mul(hi, mul(p, h))


def kind(p: Perm) -> str:
    cs = sorted(len(c) for c in cycles(p) if len(c) > 1)
    if cs == [3]:
        return "3"
    if cs == [2, 2]:
        return "D"
    raise AssertionError(cs)


def descriptor(p: Perm, h: Perm) -> dict[str, object]:
    moved = sorted(i for i, j in enumerate(p) if i != j)
    gaps = [
        (moved[(i + 1) % len(moved)] - moved[i]) % len(p)
        for i in range(len(moved))
    ]
    residual = cycle_sizes(mul(inv(p), h))
    return {
        "kind": kind(p),
        "cycles": [c for c in cycles(p) if len(c) > 1],
        "support_gaps": gaps,
        "residual_sizes": residual,
        "harmonic_residual_sum": sum(1.0 / d for d in residual),
        "minimum_residual_size": min(residual),
    }


def exact_string(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else str(x)


def build(n: int, exact: bool):
    if n < 7 or n % 2 == 0:
        raise ValueError("n must be odd and at least seven")
    h = tuple((i + 1) % n for i in range(n))
    hi = inv(h)
    gates = [edge_perm(n, i, j) for i in range(n) for j in range(i + 1, n)]
    edge = {g: edge_of(g) for g in gates}
    lifts: list[tuple[Perm, Perm, Perm]] = []
    multiplicity: collections.Counter[Perm] = collections.Counter()
    for a in gates:
        for b in gates:
            g = mul(a, b)
            multiplicity[g] += 1
            lifts.append((a, b, g))
    marginal: dict[Perm, int] = {}
    for g, ag in multiplicity.items():
        c = ag * count_minimal(mul(inv(g), h), n - 3)
        if c:
            marginal[g] = c

    oid: dict[Perm, int] = {}
    orbits: list[list[Perm]] = []
    for g in sorted(marginal):
        if g in oid:
            continue
        orbit: list[Perm] = []
        x = g
        while x not in orbit:
            orbit.append(x)
            x = theta(x, h, hi)
        j = len(orbits)
        for x in orbit:
            oid[x] = j
        orbits.append(orbit)
    q = len(orbits)

    if exact:
        kernel = [[Fraction(0) for _ in range(q)] for _ in range(q)]
    else:
        kernel = np.zeros((q, q), dtype=float)
    for i, orbit in enumerate(orbits):
        g = orbit[0]
        den = count_minimal(mul(inv(g), h), n - 3)
        for s in marginal:
            num = multiplicity[s] * count_minimal(mul(inv(mul(g, s)), h), n - 5)
            if num:
                if exact:
                    kernel[i][oid[s]] += Fraction(num, den)
                else:
                    kernel[i, oid[s]] += num / den
    if exact:
        squared = [
            [sum((kernel[i][k] * kernel[k][j] for k in range(q)), Fraction(0))
             for j in range(q)]
            for i in range(q)
        ]
        pi = [Fraction(len(o) * marginal[o[0]], n ** (n - 2)) for o in orbits]
    else:
        squared = kernel @ kernel
        pi = np.array(
            [len(o) * marginal[o[0]] / n ** (n - 2) for o in orbits],
            dtype=float,
        )

    # Record an explicit endpoint-sharing witness for every quotient edge.
    tokens: dict[tuple[int, Perm], list[tuple[Perm, int, tuple[Perm, Perm]]]] = (
        collections.defaultdict(list)
    )
    for a, b, g in lifts:
        if g not in oid:
            continue
        tokens[(0, a)].append((b, oid[g], (a, b)))
        tokens[(1, b)].append((a, oid[g], (a, b)))
    witnesses: dict[tuple[int, int], tuple[Perm, Perm, Perm, int]] = {}
    for (coordinate, common), records in tokens.items():
        unique = {(other, source): lift for other, source, lift in records}
        entries = sorted((other, source, lift) for (other, source), lift in unique.items())
        for pos, (b, i, _) in enumerate(entries):
            for c, j, _ in entries[pos + 1:]:
                if i == j or len(edge[b] & edge[c]) != 1:
                    continue
                pair = tuple(sorted((i, j)))
                witnesses.setdefault(pair, (common, b, c, coordinate))
    return h, orbits, kernel, squared, pi, witnesses


def analyze(n: int, exact: bool) -> dict[str, object]:
    h, orbits, kernel, squared, pi, witnesses = build(n, exact)
    q = len(orbits)
    best = None
    best_one = None
    kind_max: dict[str, tuple[object, tuple[int, int]]] = {}
    unit_max = None
    unit_edges = 0
    for pair in witnesses:
        i, j = pair
        if exact:
            tv1 = sum((abs(kernel[i][t] - kernel[j][t]) for t in range(q)), Fraction(0)) / 2
            tv2 = sum((abs(squared[i][t] - squared[j][t]) for t in range(q)), Fraction(0)) / 2
        else:
            tv1 = 0.5 * float(np.sum(np.abs(kernel[i] - kernel[j])))
            tv2 = 0.5 * float(np.sum(np.abs(squared[i] - squared[j])))
        pair_kind = "".join(sorted((kind(orbits[i][0]), kind(orbits[j][0]))))
        if pair_kind not in kind_max or tv2 > kind_max[pair_kind][0]:
            kind_max[pair_kind] = (tv2, pair)
        if best is None or tv2 > best[0]:
            best = (tv2, tv1, pair)
        if best_one is None or tv1 > best_one[0]:
            best_one = (tv1, tv2, pair)
        _, b_edge, c_edge, _ = witnesses[pair]
        changed = sorted(edge_of(b_edge) ^ edge_of(c_edge))
        if len(changed) == 2 and (changed[0] - changed[1]) % n in (1, n - 1):
            unit_edges += 1
            if unit_max is None or tv1 > unit_max[0]:
                unit_max = (tv1, tv2, pair)
    assert best is not None
    tv2, tv1, (i, j) = best
    common, b, c, coordinate = witnesses[(i, j)]
    source_support = set(edge_of(common)) | set(edge_of(b)) | set(edge_of(c))

    if exact:
        eta = [kernel[i][t] - kernel[j][t] for t in range(q)]
        delta = [squared[i][t] - squared[j][t] for t in range(q)]
    else:
        eta = kernel[i] - kernel[j]
        delta = squared[i] - squared[j]

    # Cancellation by intermediate kind and residual minimum.  Each layer is
    # the signed measure sum_s eta(s) K(s,.), before the final absolute value.
    layers: dict[tuple[str, int], object] = {}
    for s in range(q):
        ds = descriptor(orbits[s][0], h)
        key = (str(ds["kind"]), int(ds["minimum_residual_size"]))
        if exact:
            vec = layers.setdefault(key, [Fraction(0) for _ in range(q)])
            for t in range(q):
                vec[t] += eta[s] * kernel[s][t]
        else:
            vec = layers.setdefault(key, np.zeros(q, dtype=float))
            vec += eta[s] * kernel[s]

    layer_rows = []
    triangle_total = 0
    for key, vec in sorted(layers.items()):
        l1 = sum((abs(x) for x in vec), Fraction(0)) if exact else float(np.sum(np.abs(vec)))
        mass = sum(vec, Fraction(0)) if exact else float(np.sum(vec))
        triangle_total += l1
        layer_rows.append({
            "intermediate_kind": key[0],
            "intermediate_minimum_residual_size": key[1],
            "signed_mass": exact_string(mass) if exact else mass,
            "TV_seminorm": exact_string(l1 / 2) if exact else l1 / 2,
        })

    target_layers: dict[tuple[str, int], dict[str, object]] = {}
    first_step_support_layers: dict[tuple[str, bool], object] = {}
    first_step_kind_layers: dict[str, object] = {}
    disjoint_positive_ratios = []
    for t, value in enumerate(delta):
        dt = descriptor(orbits[t][0], h)
        key = (str(dt["kind"]), int(dt["minimum_residual_size"]))
        row = target_layers.setdefault(key, {"signed": Fraction(0) if exact else 0.0,
                                             "absolute": Fraction(0) if exact else 0.0})
        row["signed"] += value
        row["absolute"] += abs(value)
    for t in range(q):
        target_support = {
            x for cyc in cycles(orbits[t][0]) if len(cyc) > 1 for x in cyc
        }
        key = (kind(orbits[t][0]), bool(target_support & source_support))
        difference = kernel[i][t] - kernel[j][t]
        target_kind = kind(orbits[t][0])
        first_step_kind_layers[target_kind] = (
            first_step_kind_layers.get(target_kind, Fraction(0) if exact else 0.0)
            + abs(difference) / 2
        )
        first_step_support_layers[key] = (
            first_step_support_layers.get(key, Fraction(0) if exact else 0.0)
            + abs(difference) / 2
        )
        if not (target_support & source_support) and kernel[j][t] != 0:
            disjoint_positive_ratios.append(kernel[i][t] / kernel[j][t])

    def show(x):
        return exact_string(x) if exact else float(x)

    return {
        "n": n,
        "arithmetic": "exact_rational" if exact else "floating",
        "quotient_states": q,
        "localized_edges": len(witnesses),
        "unit_slide_edges": unit_edges,
        "maximum_edge_TV_K": show(best_one[0]),
        "n_times_maximum_edge_TV_K": show(n * best_one[0]),
        "edge_K_maximizing_orbits": list(best_one[2]),
        "maximum_edge_TV_K2": show(tv2),
        "n_squared_times_maximum_edge_TV_K2": show(n * n * tv2),
        "witness_orbits": [i, j],
        "witness_descriptors": [descriptor(orbits[i][0], h), descriptor(orbits[j][0], h)],
        "witness_lift": {
            "common_coordinate": coordinate,
            "common_chord": sorted(edge_of(common)),
            "differing_chords": [sorted(edge_of(b)), sorted(edge_of(c))],
        },
        "one_to_two_step_contraction_ratio": show(tv2 / tv1),
        "maximum_unit_slide_TV_K": show(unit_max[0]),
        "n_squared_times_maximum_unit_slide_TV_K": show(n * n * unit_max[0]),
        "maximum_unit_slide_TV_K2": show(unit_max[1]),
        "n_squared_times_corresponding_unit_slide_TV_K2": show(
            n * n * unit_max[1]
        ),
        "unit_slide_K_maximizing_orbits": list(unit_max[2]),
        "intermediate_layer_triangle_TV": show(triangle_total / 2),
        "triangle_loss_over_actual_TV": show((triangle_total / 2) / tv2),
        "intermediate_layers": layer_rows,
        "target_layers": [
            {"target_kind": key[0],
             "target_minimum_residual_size": key[1],
             "signed_mass": show(row["signed"]),
             "absolute_mass": show(row["absolute"])}
            for key, row in sorted(target_layers.items())
        ],
        # This representative-level split is deliberately labeled noninvariant:
        # target orbits contain other rotations with different intersections.
        "noninvariant_representative_support_split": [
            {"target_kind": key[0], "intersects_perturbed_source_support": key[1],
             "TV_contribution": show(value)}
            for key, value in sorted(first_step_support_layers.items())
        ],
        "first_step_TV_by_target_kind": {
            key: show(value) for key, value in sorted(first_step_kind_layers.items())
        },
        "representative_disjoint_positive_row_ratio_minimum": (
            show(min(disjoint_positive_ratios)) if disjoint_positive_ratios else None
        ),
        "representative_disjoint_positive_row_ratio_maximum": (
            show(max(disjoint_positive_ratios)) if disjoint_positive_ratios else None
        ),
        "disjoint_positive_row_ratio_distinct_exact": (
            len(set(disjoint_positive_ratios)) if exact else None
        ),
        "maxima_by_source_kind": {
            key: {"TV_K2": show(value[0]), "orbits": list(value[1])}
            for key, value in sorted(kind_max.items())
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", nargs="+", type=int, required=True)
    parser.add_argument("--exact-through", type=int, default=9)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "status": "finite_diagnostic_only",
        "claim_tested": "Endpoint-sharing K^2 influence and signed layer cancellation",
        "convention": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
        "results": [analyze(n, n <= args.exact_through) for n in args.n],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
