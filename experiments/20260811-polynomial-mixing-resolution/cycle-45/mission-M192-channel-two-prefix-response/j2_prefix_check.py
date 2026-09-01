#!/usr/bin/env python3
"""Compact exact k=3,5,7 checker for the M192 J=2 reduction.

This standard-library script builds only the exterior first-factor and
ordered-pair laws.  It verifies the closed shared-endpoint coefficient,
triangle masses, disjoint scalar weights, the nonzero Abel endpoint, and the
exact disjoint-prefix decomposition for both PCR prefix observables.

Convention: (pq)(x)=p(q(x)); displayed factors multiply left-to-right.
Finite diagnostics imply no universal bound or sign.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path


Perm = tuple[int, ...]
Key = tuple[int, int]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def cycle_perm(n: int, vertices: tuple[int, ...]) -> Perm:
    out = list(range(n))
    for x, y in zip(vertices, vertices[1:] + vertices[:1]):
        out[x] = y
    return tuple(out)


def transposition(n: int, x: int, y: int) -> Perm:
    return cycle_perm(n, (x, y))


def cycles(p: Perm) -> list[tuple[int, ...]]:
    seen: set[int] = set()
    out: list[tuple[int, ...]] = []
    for start in range(len(p)):
        if start in seen:
            continue
        part: list[int] = []
        x = start
        while x not in seen:
            seen.add(x)
            part.append(x)
            x = p[x]
        out.append(tuple(part))
    return out


def rank(p: Perm) -> int:
    return len(p) - len(cycles(p))


def tau(d: int) -> Fraction:
    return Fraction(d ** (d - 1), math.factorial(d))


def completion(p: Perm, length: int) -> Fraction:
    if rank(p) != length:
        return Fraction()
    out = Fraction(math.factorial(length))
    for part in cycles(p):
        out *= tau(len(part))
    return out


def internal_edges(p: Perm) -> list[Perm]:
    return [
        transposition(len(p), x, y)
        for part in cycles(p)
        for x, y in combinations(part, 2)
    ]


def edge_vertices(e: Perm) -> tuple[int, int]:
    moved = [x for x in range(len(e)) if e[x] != x]
    assert len(moved) == 2
    return tuple(sorted(moved))  # type: ignore[return-value]


def on_parts(n: int, parts: list[tuple[int, ...]]) -> Perm:
    out = list(range(n))
    for part in parts:
        for x, y in zip(part, part[1:] + part[:1]):
            out[x] = y
    return tuple(out)


def source(k: int, side: str) -> tuple[Perm, Perm, list[tuple[int, ...]]]:
    n = 3 * k
    h = cycle_perm(n, tuple(range(n)))
    if side == "A":
        g = cycle_perm(n, (0, k, 2 * k))
    else:
        g = compose(transposition(n, 0, 1), transposition(n, k, 2 * k))
    parts = cycles(compose(inverse(g), h))
    middle = next(part for part in parts if set(part) == set(range(k, 2 * k)))
    exterior = [part for part in parts if part != middle and len(part) > 1]
    return h, on_parts(n, exterior), exterior


def first_law(q: Perm) -> dict[Perm, Fraction]:
    r = rank(q)
    denominator = completion(q, r)
    out = {e: completion(compose(e, q), r - 1) / denominator for e in internal_edges(q)}
    assert sum(out.values(), Fraction()) == 1
    return out


def pair_law(q: Perm) -> dict[tuple[Perm, Perm], Fraction]:
    r = rank(q)
    denominator = completion(q, r)
    out: dict[tuple[Perm, Perm], Fraction] = {}
    for e in internal_edges(q):
        q1 = compose(e, q)
        for f in internal_edges(q1):
            out[(e, f)] = completion(compose(f, q1), r - 2) / denominator
    assert all(out.values())
    assert sum(out.values(), Fraction()) == 1
    return out


def smaller_split(e: Perm, original: list[tuple[int, ...]]) -> int:
    x, y = edge_vertices(e)
    part = next(part for part in original if x in part)
    positions = {z: i for i, z in enumerate(part)}
    gap = (positions[y] - positions[x]) % len(part)
    return min(gap, len(part) - gap)


def ambient_runs(part: tuple[int, ...], n: int) -> tuple[int, ...]:
    support = set(part)
    starts = [x for x in support if (x - 1) % n not in support]
    assert starts
    lengths: list[int] = []
    for start in starts:
        length = 0
        while (start + length) % n in support:
            length += 1
        lengths.append(length)
    assert sum(lengths) == len(part)
    return tuple(sorted(lengths))


def component_profile(product: Perm, h: Perm) -> dict[Key, int]:
    residual = compose(inverse(product), h)
    parts = cycles(residual)
    assert len(parts) == 3
    out: defaultdict[Key, int] = defaultdict(int)
    for part in parts:
        runs = ambient_runs(part, len(h))
        assert len(runs) in (1, 2)
        out[(len(runs), len(part))] += 1
    return dict(out)


def gamma(k: int, side: str, split: int) -> Fraction:
    other = (2 * k - 1 - split) if side == "B" else (k - split)
    return Fraction(2, 2 * k - 3) * (
        2 - Fraction(1, split) - Fraction(1, other)
    )


def observable(profile: dict[Key, Fraction], cutoff: int, one_only: bool) -> Fraction:
    return sum(
        value
        for (run_type, size), value in profile.items()
        if 2 <= size <= cutoff and (not one_only or run_type == 1)
    )


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def analyze(k: int) -> dict[str, object]:
    n = 3 * k
    data: dict[str, dict[str, object]] = {}
    collision_events = 0
    for side in ("A", "B"):
        h, exterior, original = source(k, side)
        first = first_law(exterior)
        pairs = pair_law(exterior)
        split_law: defaultdict[int, Fraction] = defaultdict(Fraction)
        triangle_mass: defaultdict[int, Fraction] = defaultdict(Fraction)
        double_mass: defaultdict[int, Fraction] = defaultdict(Fraction)
        double_profile_raw: dict[int, defaultdict[Key, Fraction]] = defaultdict(lambda: defaultdict(Fraction))
        for e, weight in first.items():
            split_law[smaller_split(e, original)] += weight
        for (e, f), weight in pairs.items():
            split = smaller_split(e, original)
            shared = bool(set(edge_vertices(e)) & set(edge_vertices(f)))
            profile = component_profile(compose(e, f), h)
            if shared:
                assert all(run_type == 1 for run_type, _ in profile)
                triangle_mass[split] += weight
            else:
                assert sum(count for (run_type, _), count in profile.items() if run_type == 2) == 1
                double_mass[split] += weight
                for key, count in profile.items():
                    double_profile_raw[split][key] += weight * count
                if any(count > 1 for count in profile.values()):
                    collision_events += 1
        for split, mass in split_law.items():
            assert triangle_mass[split] / mass == gamma(k, side, split)
            assert double_mass[split] == mass * (1 - gamma(k, side, split))
        normalized = {
            split: {key: value / double_mass[split] for key, value in profile.items()}
            for split, profile in double_profile_raw.items()
        }
        data[side] = {
            "split_law": dict(split_law),
            "triangle_mass": dict(triangle_mass),
            "double_mass": dict(double_mass),
            "double_profiles": normalized,
        }

    p = data["B"]["split_law"]
    q = data["A"]["split_law"]
    phat = data["B"]["double_mass"]
    qhat = data["A"]["double_mass"]
    phi = data["B"]["double_profiles"]
    psi = data["A"]["double_profiles"]
    assert isinstance(p, dict) and isinstance(q, dict)
    assert isinstance(phat, dict) and isinstance(qhat, dict)
    assert isinstance(phi, dict) and isinstance(psi, dict)

    triangle_b = sum(data["B"]["triangle_mass"].values(), Fraction())  # type: ignore[union-attr]
    triangle_a = sum(data["A"]["triangle_mass"].values(), Fraction())  # type: ignore[union-attr]
    assert triangle_b == Fraction(3, 2 * k - 1)
    assert triangle_a == Fraction(3 * (k - 2), k * (2 * k - 3))

    cumulative: dict[int, Fraction] = {}
    running = Fraction()
    for split in range(1, k):
        running += phat.get(split, Fraction()) - qhat.get(split, Fraction())
        cumulative[split] = running
    endpoint = -Fraction(6 * (k - 1), k * (2 * k - 1) * (2 * k - 3))
    assert cumulative[k - 1] == endpoint

    diagnostics = {"all_types": [], "one_run": []}
    for one_only, name in ((False, "all_types"), (True, "one_run")):
        for cutoff in range(2, n // 2 + 1):
            phi_value = {split: observable(profile, cutoff, one_only) for split, profile in phi.items()}
            psi_value = {split: observable(profile, cutoff, one_only) for split, profile in psi.items()}
            direct = sum(phat[split] * phi_value[split] for split in phat) - sum(
                qhat[split] * psi_value[split] for split in qhat
            )
            scalar = endpoint * phi_value[k - 1] + sum(
                cumulative[u] * (phi_value[u] - phi_value[u + 1]) for u in range(1, k - 1)
            )
            embedding = sum(
                qhat[split] * (phi_value[split] - psi_value[split]) for split in qhat
            )
            assert direct == scalar + embedding
            variation = sum(
                math.sqrt(u) * abs(float(phi_value[u] - phi_value[u + 1]))
                for u in range(1, k - 1)
            )
            diagnostics[name].append({
                "cutoff": cutoff,
                "direct_double_prefix": qstr(direct),
                "scalar_Abel_part": qstr(scalar),
                "signed_embedding_part": qstr(embedding),
                "scaled_abs_direct_k_over_sqrt_cutoff": k * abs(float(direct)) / math.sqrt(cutoff),
                "weighted_variation_over_sqrt_cutoff": variation / math.sqrt(cutoff),
                "scaled_abs_embedding_k_over_sqrt_cutoff": k * abs(float(embedding)) / math.sqrt(cutoff),
            })

    return {
        "k": k,
        "n": n,
        "triangle_mass_B": qstr(triangle_b),
        "triangle_mass_A": qstr(triangle_a),
        "double_mass_difference_endpoint": qstr(endpoint),
        "max_scaled_cumulative_abs_k_over_sqrt_u": max(
            k * abs(float(cumulative[u])) / math.sqrt(u) for u in cumulative
        ),
        "shared_endpoint_gamma_exact": True,
        "disjoint_Abel_decomposition_exact": True,
        "collision_events_retained": collision_events,
        "finite_only_diagnostics": diagnostics,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    payload = {
        "mission": "M192",
        "status": "all exact k=3,5,7 J=2 reduction assertions passed; DV/DE/PCR unresolved",
        "composition": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "parameters": {"k": [3, 5, 7], "seed": None},
        "python": platform.python_version(),
        "standard_library_only": True,
        "finite_asymptotic_or_sign_inference": False,
        "results": [analyze(k) for k in (3, 5, 7)],
    }
    Path(args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": payload["status"], "output": args.output}, sort_keys=True))


if __name__ == "__main__":
    main()
