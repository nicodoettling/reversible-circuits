#!/usr/bin/env python3
"""Exact finite falsification of a seam-phase endpoint decomposition.

The analytic split-path coupling in adjacent_transport.md was fixed before
this checker.  The checker retains the complete J=1/J=2 mixture and only
then partitions the designated first exterior chord according to whether it
crosses a splice seam (B) or is incident to the deleted vertex 0 (A).
Finite output is not an asymptotic SET or sign theorem.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import platform
import subprocess
import math as integer_math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
M261_PATH = ROOT / (
    "experiments/20260811-polynomial-mixing-resolution/cycle-71/"
    "mission-M261-fixed-cell-fd/pbv_exact.py"
)


def load_m261():
    spec = importlib.util.spec_from_file_location("m261_pbv_exact", M261_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load frozen M261 checker")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M = load_m261()


def rank(p) -> int:
    return sum(len(c) - 1 for c in M.cycles(p))


def nontrivial_components(p):
    return [c for c in M.cycles(p) if len(c) > 1]


def internal_edges(n: int, p):
    for c in nontrivial_components(p):
        yield from M.internal_edges(n, c)


def edge_law(n: int, residual):
    r = rank(residual)
    denominator = M.completion(residual, r)
    out = {}
    for e in internal_edges(n, residual):
        value = Fraction(M.completion(M.mul(e, residual), r - 1), denominator)
        if value:
            out[e] = value
    assert sum(out.values(), Fraction()) == 1
    return out


def pair_law(n: int, residual):
    r = rank(residual)
    denominator = M.completion(residual, r)
    out = {}
    for e in internal_edges(n, residual):
        after = M.mul(e, residual)
        for f in internal_edges(n, after):
            product = M.mul(e, f)
            value = Fraction(
                M.completion(M.mul(M.inv(product), residual), r - 2), denominator
            )
            if value:
                out[(e, f)] = value
    assert sum(out.values(), Fraction()) == 1
    return out


def transposition_endpoints(p):
    moved = [x for x in range(len(p)) if p[x] != x]
    assert len(moved) == 2
    return frozenset(moved)


def add_scaled(target, row, scale):
    for i, value in enumerate(row):
        target[i] += scale * value


def zero_vector(length: int):
    return [Fraction() for _ in range(length)]


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def summary(row, n: int):
    total = sum((abs(x) for x in row), Fraction())
    return {
        "l1_exact": qstr(total),
        "l1_float": float(total),
        "n_times_l1_float": float(n * total),
    }


def tau(d: int) -> Fraction:
    return Fraction(d ** (d - 1), integer_math.factorial(d))


def nu(d: int, a: int) -> Fraction:
    if not 1 <= a < d:
        return Fraction()
    return Fraction(integer_math.factorial(d - 2), d ** (d - 2)) * tau(a) * tau(d - a)


def channel_one_collision_formula(k: int):
    """Proposition 2 in phase_incidence_lemma.md, before alpha_1."""
    n = 3 * k
    d = 2 * k - 1
    rho_a = [Fraction() for _ in range(n)]
    rho_b = [Fraction() for _ in range(n)]
    for a in range(1, k):
        rho_a[a] = (k - a) * nu(k, a)
    for a in range(1, 2 * k):
        same = max(k - 1 - a, 0) + max(k - a, 0)
        cross = a - 1 if 2 <= a <= k else (2 * k - a if k < a <= 2 * k - 1 else 0)
        rho_b[a] = same * nu(d, a) + cross * nu(d, a - 1)
    assert sum(rho_a, Fraction()) == 1
    assert sum(rho_b, Fraction()) == 1
    delta_rho = [rho_b[a] - rho_a[a] for a in range(n)]

    first_block = set(range(1, k))
    second_block = set(range(2 * k, 3 * k))
    exterior_b = first_block | second_block
    exterior_a = {0} | exterior_b
    middle = set(range(k, 2 * k))
    delta_endpoint = [
        (Fraction(2, d) if v in exterior_b else Fraction())
        - (Fraction(1, k) if v in exterior_a else Fraction())
        for v in range(n)
    ]
    middle_endpoint = [Fraction(2, k) if v in middle else Fraction() for v in range(n)]
    assert sum(abs(x) for x in delta_endpoint) == Fraction(2, k)

    profile = []
    for ell in range(n):
        value = delta_rho[ell] + delta_rho[(n - ell) % n]
        value += sum(
            delta_endpoint[v] * middle_endpoint[(v + ell) % n]
            + middle_endpoint[v] * delta_endpoint[(v + ell) % n]
            for v in range(n)
        )
        profile.append(value)
    derivative = tuple(profile[ell + 1] - profile[ell] for ell in range(2, n - 2))
    variation_delta_rho = sum(
        abs(delta_rho[(a + 1) % n] - delta_rho[a]) for a in range(n)
    )
    return derivative, variation_delta_rho


def analyze(k: int):
    if k < 3 or k % 2 == 0:
        raise ValueError("k must be odd and at least 3")
    n = 3 * k
    h = M.cyc(n, tuple(range(n)))
    c_minus = M.cyc(n, tuple(range(0, k)))
    c_plus = M.cyc(n, tuple(range(2 * k, 3 * k)))
    exterior_a = M.mul(c_minus, c_plus)
    exterior_b = M.cyc(n, tuple(range(1, k)) + tuple(range(2 * k, 3 * k)))
    middle = M.cyc(n, tuple(range(k, 2 * k)))

    lambda_a = edge_law(n, exterior_a)
    lambda_b = edge_law(n, exterior_b)
    lambda_m = edge_law(n, middle)
    pair_a = pair_law(n, exterior_a)
    pair_b = pair_law(n, exterior_b)

    m = k - 1
    denominator = 3 * m * (3 * m - 1)
    alpha_1 = Fraction(4 * m * m, denominator)
    alpha_2 = Fraction(2 * m * (2 * m - 1), denominator)
    length = n - 4
    rows = defaultdict(lambda: zero_vector(length))
    collision_rows = defaultdict(lambda: zero_vector(length))
    cache = {}
    collision_cache = {}

    first_block = set(range(1, k))
    second_block = set(range(2 * k, 3 * k))

    def kind(product):
        return "T" if sum(product[x] != x for x in range(n)) == 3 else "D"

    def response(product):
        if product not in cache:
            cache[product] = M.endpoint_vector(n, h, product)
        return cache[product]

    def collision_response(product):
        if product not in collision_cache:
            collision_cache[product] = M.collision_delta_vector(n, product)
        return collision_cache[product]

    def record(key, product, scale):
        add_scaled(rows[key], response(product), scale)
        add_scaled(collision_rows[key], collision_response(product), scale)

    def category_b(e):
        endpoints = transposition_endpoints(e)
        return "B_cross" if endpoints & first_block and endpoints & second_block else "B_same"

    def category_a(e):
        return "A_zero" if 0 in transposition_endpoints(e) else "A_nonzero"

    for e, pe in lambda_b.items():
        category = category_b(e)
        for f, pf in lambda_m.items():
            product = M.mul(e, f)
            record((category, "J1", kind(product)), product, alpha_1 * pe * pf)
    for (e, f), probability in pair_b.items():
        product = M.mul(e, f)
        record((category_b(e), "J2", kind(product)), product, alpha_2 * probability)

    for e, pe in lambda_a.items():
        category = category_a(e)
        for f, pf in lambda_m.items():
            product = M.mul(e, f)
            record((category, "J1", kind(product)), product, -alpha_1 * pe * pf)
    for (e, f), probability in pair_a.items():
        product = M.mul(e, f)
        record((category_a(e), "J2", kind(product)), product, -alpha_2 * probability)

    keys = list(rows)
    total = zero_vector(length)
    interior = zero_vector(length)
    seam = zero_vector(length)
    by_channel = {j: zero_vector(length) for j in ("J1", "J2")}
    by_kind = {kind_: zero_vector(length) for kind_ in ("T", "D")}
    collision_total = zero_vector(length)
    collision_source = {
        source: zero_vector(length) for source in ("A", "B")
    }
    collision_source_channel = {
        (source, channel): zero_vector(length)
        for source in ("A", "B")
        for channel in ("J1", "J2")
    }
    collision_interior = zero_vector(length)
    collision_seam = zero_vector(length)
    collision_by_channel = {j: zero_vector(length) for j in ("J1", "J2")}
    collision_by_kind = {kind_: zero_vector(length) for kind_ in ("T", "D")}
    collision_by_channel_kind = {
        (channel, kind_): zero_vector(length)
        for channel in ("J1", "J2")
        for kind_ in ("T", "D")
    }
    for key in keys:
        category, channel, kind_ = key
        add_scaled(total, rows[key], Fraction(1))
        add_scaled(interior if category in ("B_same", "A_nonzero") else seam, rows[key], Fraction(1))
        add_scaled(by_channel[channel], rows[key], Fraction(1))
        add_scaled(by_kind[kind_], rows[key], Fraction(1))
        add_scaled(collision_total, collision_rows[key], Fraction(1))
        add_scaled(
            collision_interior if category in ("B_same", "A_nonzero") else collision_seam,
            collision_rows[key],
            Fraction(1),
        )
        add_scaled(collision_by_channel[channel], collision_rows[key], Fraction(1))
        add_scaled(collision_by_kind[kind_], collision_rows[key], Fraction(1))
        add_scaled(collision_by_channel_kind[(channel, kind_)], collision_rows[key], Fraction(1))

    for key in keys:
        category, channel, _ = key
        source = "B" if category.startswith("B_") else "A"
        sign = Fraction(1) if source == "B" else Fraction(-1)
        add_scaled(collision_source[source], collision_rows[key], sign)
        add_scaled(collision_source_channel[(source, channel)], collision_rows[key], sign)

    decorated_total = [math.e**2 * float(total[i]) - float(collision_total[i]) for i in range(length)]
    decorated_interior = [math.e**2 * float(interior[i]) - float(collision_interior[i]) for i in range(length)]
    decorated_seam = [math.e**2 * float(seam[i]) - float(collision_seam[i]) for i in range(length)]

    def float_summary(row):
        value = sum(abs(x) for x in row)
        return {"l1_float": value, "n_times_l1_float": n * value}

    assert all(total[i] == -total[-1 - i] for i in range(length))
    assert total[length // 2] == 0
    channel_one_formula, variation_delta_rho = channel_one_collision_formula(k)
    assert tuple(collision_by_channel["J1"]) == tuple(alpha_1 * x for x in channel_one_formula)
    return {
        "k": k,
        "n": n,
        "alpha_1_exact": qstr(alpha_1),
        "alpha_2_exact": qstr(alpha_2),
        "accessible_products": len(cache),
        "combined": summary(total, n),
        "first_exterior_phase_partition": {
            "same_nonzero_combined": summary(interior, n),
            "cross_zero_combined": summary(seam, n),
            "separate_sum_n_times_l1": summary(interior, n)["n_times_l1_float"]
            + summary(seam, n)["n_times_l1_float"],
        },
        "by_channel": {key: summary(value, n) for key, value in by_channel.items()},
        "by_kind": {key: summary(value, n) for key, value in by_kind.items()},
        "affine_split": {
            "collision_combined": summary(collision_total, n),
            "decorated_combined": float_summary(decorated_total),
            "collision_same_nonzero": summary(collision_interior, n),
            "collision_cross_zero": summary(collision_seam, n),
            "decorated_same_nonzero": float_summary(decorated_interior),
            "decorated_cross_zero": float_summary(decorated_seam),
            "collision_by_channel": {
                key: summary(value, n) for key, value in collision_by_channel.items()
            },
            "collision_by_kind": {
                key: summary(value, n) for key, value in collision_by_kind.items()
            },
            "collision_by_channel_kind": {
                f"{channel}/{kind_}": summary(value, n)
                for (channel, kind_), value in collision_by_channel_kind.items()
            },
            "collision_source_unsigned": {
                key: summary(value, n) for key, value in collision_source.items()
            },
            "collision_source_channel_unsigned": {
                f"{source}/{channel}": summary(value, n)
                for (source, channel), value in collision_source_channel.items()
            },
        },
        "atomic_groups": {
            "/".join(key): summary(value, n) for key, value in sorted(rows.items())
        },
        "reflection_exact": True,
        "channel_one_collision_formula_exact": True,
        "n_times_face_delta_variation_float": float(n * variation_delta_rho),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", nargs="+", type=int, default=[3, 5, 7])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "status": "exact finite falsification only; no SET/PBV/sign inference",
        "analytic_bad_phase_partition_fixed_before_computation": True,
        "target": "combined-channel endpoint response after D/q cancellation",
        "convention": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(__import__("sys").argv),
        "m261_dependency": str(M261_PATH.relative_to(ROOT)),
        "results": [analyze(k) for k in args.k],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
