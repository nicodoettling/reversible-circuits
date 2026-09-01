#!/usr/bin/env python3
"""Exact finite checker for the M272 channel-two collision reduction.

This checker disintegrates the literal ordered first-two-factor laws by
first split and by shared/disjoint support.  It checks the vector-valued
disjoint Abel identity before taking lag-l1 norms.  Its finite profile
constants do not prove either remaining uniform estimate.
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
PROBE = HERE / "phase_incidence_probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("m272_phase_probe", PROBE)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load M272 phase probe")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


P = load_probe()


def zero(n: int):
    return [Fraction() for _ in range(n)]


def add(out, row, scale=Fraction(1)):
    for i, value in enumerate(row):
        out[i] += scale * value


def scaled(row, scale):
    return [scale * value for value in row]


def difference(left, right):
    return [x - y for x, y in zip(left, right)]


def l1(row):
    return sum((abs(value) for value in row), Fraction())


def qstr(value):
    return (
        str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}"
    )


def cycle_position(parts):
    return {
        vertex: (part_index, position, len(part))
        for part_index, part in enumerate(parts)
        for position, vertex in enumerate(part)
    }


def smaller_split(edge, positions):
    x, y = tuple(P.transposition_endpoints(edge))
    px, ix, length = positions[x]
    py, iy, other_length = positions[y]
    assert px == py and length == other_length
    gap = (iy - ix) % length
    return min(gap, length - gap)


def source_data(k, side):
    n = 3 * k
    if side == "A":
        parts = (
            tuple(range(0, k)),
            tuple(range(2 * k, 3 * k)),
        )
        residual = P.M.mul(
            P.M.cyc(n, parts[0]),
            P.M.cyc(n, parts[1]),
        )
    else:
        parts = (tuple(range(1, k)) + tuple(range(2 * k, 3 * k)),)
        residual = P.M.cyc(n, parts[0])
    return residual, cycle_position(parts)


def summarize(row, k):
    value = l1(row)
    return {
        "l1_exact": qstr(value),
        "l1_float": float(value),
        "k_times_l1_float": float(k * value),
    }


def analyze(k):
    if k < 3 or k % 2 == 0:
        raise ValueError("k must be odd and at least 3")
    n = 3 * k
    length = n - 4
    raw = {}
    for side in ("A", "B"):
        residual, positions = source_data(k, side)
        pairs = P.pair_law(n, residual)
        split_mass = defaultdict(Fraction)
        triangle_mass = defaultdict(Fraction)
        double_mass = defaultdict(Fraction)
        triangle_raw = defaultdict(lambda: zero(length))
        double_raw = defaultdict(lambda: zero(length))
        for (edge, second), weight in pairs.items():
            split = smaller_split(edge, positions)
            split_mass[split] += weight
            product = P.M.mul(edge, second)
            response = P.M.collision_delta_vector(n, product)
            shared = bool(
                P.transposition_endpoints(edge)
                & P.transposition_endpoints(second)
            )
            if shared:
                triangle_mass[split] += weight
                add(triangle_raw[split], response, weight)
            else:
                double_mass[split] += weight
                add(double_raw[split], response, weight)
        assert sum(split_mass.values(), Fraction()) == 1
        for split, mass in split_mass.items():
            other = 2 * k - 1 - split if side == "B" else k - split
            gamma = Fraction(2, 2 * k - 3) * (
                2 - Fraction(1, split) - Fraction(1, other)
            )
            assert triangle_mass[split] == mass * gamma
            assert triangle_mass[split] + double_mass[split] == mass
        raw[side] = {
            "split_mass": split_mass,
            "triangle_mass": triangle_mass,
            "double_mass": double_mass,
            "triangle_raw": triangle_raw,
            "double_raw": double_raw,
        }

    p_hat = raw["B"]["double_mass"]
    q_hat = raw["A"]["double_mass"]
    phi = {
        split: scaled(row, Fraction(1, p_hat[split]))
        for split, row in raw["B"]["double_raw"].items()
    }
    psi = {
        split: scaled(row, Fraction(1, q_hat[split]))
        for split, row in raw["A"]["double_raw"].items()
    }

    direct_double = zero(length)
    direct_triangle = zero(length)
    for side, sign in (("B", Fraction(1)), ("A", Fraction(-1))):
        for row in raw[side]["double_raw"].values():
            add(direct_double, row, sign)
        for row in raw[side]["triangle_raw"].values():
            add(direct_triangle, row, sign)

    cumulative = {}
    running = Fraction()
    for split in range(1, k):
        running += p_hat.get(split, Fraction()) - q_hat.get(split, Fraction())
        cumulative[split] = running
    endpoint = -Fraction(
        6 * (k - 1), k * (2 * k - 1) * (2 * k - 3)
    )
    assert cumulative[k - 1] == endpoint

    scalar = scaled(phi[k - 1], endpoint)
    for split in range(1, k - 1):
        add(
            scalar,
            difference(phi[split], phi[split + 1]),
            cumulative[split],
        )
    embedding = zero(length)
    for split, mass in q_hat.items():
        add(embedding, difference(phi[split], psi[split]), mass)
    assert direct_double == [
        scalar[i] + embedding[i] for i in range(length)
    ]

    weighted_adjacent_variation = sum(
        math.sqrt(split)
        * float(l1(difference(phi[split], phi[split + 1])))
        for split in range(1, k - 1)
    )
    total = [
        direct_double[i] + direct_triangle[i] for i in range(length)
    ]
    triangle_mass_a = sum(raw["A"]["triangle_mass"].values(), Fraction())
    triangle_mass_b = sum(raw["B"]["triangle_mass"].values(), Fraction())
    assert triangle_mass_b == Fraction(3, 2 * k - 1)
    assert triangle_mass_a == Fraction(3 * (k - 2), k * (2 * k - 3))
    assert l1(direct_triangle) <= 12 * (
        triangle_mass_a + triangle_mass_b
    )

    return {
        "k": k,
        "n": n,
        "triangle_mass_A_exact": qstr(triangle_mass_a),
        "triangle_mass_B_exact": qstr(triangle_mass_b),
        "double_mass_difference_endpoint_exact": qstr(endpoint),
        "shared_endpoint_gamma_exact": True,
        "vector_disjoint_Abel_identity_exact": True,
        "triangle_crude_l1_bound_exact": True,
        "signed_triangle": summarize(direct_triangle, k),
        "signed_double": summarize(direct_double, k),
        "signed_total_channel_two": summarize(total, k),
        "scalar_Abel_part": summarize(scalar, k),
        "signed_embedding_part": summarize(embedding, k),
        "collision_DV_lhs_float": weighted_adjacent_variation,
        "collision_DE_scaled_k_float": float(k * l1(embedding)),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", nargs="+", type=int, default=[3, 5, 7])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "status": (
            "exact finite channel-two collision reduction only; "
            "no CDV/CDE/SET/PBV inference"
        ),
        "target": "conditional J=2 signed collision derivative lag-l1",
        "convention": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(__import__("sys").argv),
        "results": [analyze(k) for k in args.k],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
