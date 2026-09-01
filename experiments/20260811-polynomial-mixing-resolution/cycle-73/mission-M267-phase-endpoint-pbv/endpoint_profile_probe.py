#!/usr/bin/env python3
"""Finite falsification of M267's endpoint-profile identities.

The analytic profile target was fixed before this script was created.  This
script imports the frozen, checksum-validated M261 exact enumerator only for
its first-two-factor source law and basic permutation routines.  It does not
attempt to prove PBV, SET, or a sign theorem.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import platform
import subprocess
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


def qstr(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def jump_vector(n: int, h, s) -> tuple[Fraction, ...]:
    """Independent implementation of Proposition 1's owner-jump formula."""
    q = M.mul(M.inv(s), h)
    components = M.cycles(q)
    assert len(components) == 3
    vertex_owner = {x: i for i, component in enumerate(components) for x in component}
    sizes = [len(component) for component in components]
    owner = [-1] * n
    for r in range(n):
        if s[(r + 1) % n] == (r + 1) % n:
            owner[r] = vertex_owner[r]

    kappa = [[Fraction(0) for _ in components] for _ in components]
    for i in range(3):
        kappa[i][i] = M.tau_ratio_2(sizes[i])
        for j in range(3):
            if i != j:
                kappa[i][j] = M.tau_ratio_1(sizes[i]) * M.tau_ratio_1(sizes[j])

    values = []
    for ell in range(2, n - 2):
        value = Fraction(0)
        for x in range(n):
            source = owner[(x - ell) % n]
            if source < 0:
                continue
            before = owner[x]
            after = owner[(x + 1) % n]
            if after >= 0:
                value += kappa[source][after]
            if before >= 0:
                value -= kappa[source][before]
        values.append(value)
    return tuple(values)


def supported_products(n: int):
    h = M.cyc(n, tuple(range(n)))
    edges = [M.tr(n, x, y) for x in range(n) for y in range(x + 1, n)]
    products = set()
    for first in edges:
        for second in edges:
            if first == second:
                continue
            s = M.mul(first, second)
            support = sum(s[x] != x for x in range(n))
            if support not in (3, 4):
                continue
            q = M.mul(M.inv(s), h)
            if len(M.cycles(q)) == 3 and M.completion(q, n - 3):
                products.add(s)
    return h, products


def validate_pointwise(k: int) -> dict[str, object]:
    n = 3 * k
    h, products = supported_products(n)
    maximum_l1 = Fraction(0)
    for s in products:
        accepted = M.endpoint_vector(n, h, s)
        direct = jump_vector(n, h, s)
        assert direct == accepted
        assert all(direct[i] == -direct[-1 - i] for i in range(len(direct)))
        assert direct[len(direct) // 2] == 0
        maximum_l1 = max(maximum_l1, sum((abs(x) for x in direct), Fraction(0)))
        assert float(maximum_l1) <= 1232 / math.e**2
    return {
        "k": k,
        "supported_products": len(products),
        "jump_formula_exact": True,
        "reflection_exact": True,
        "central_zero_exact": True,
        "maximum_state_endpoint_l1_exact": qstr(maximum_l1),
        "maximum_state_endpoint_l1_float": float(maximum_l1),
        "proved_envelope_float": 1232 / math.e**2,
    }


def add_vectors(rows, length: int):
    return tuple(sum((row[i] for row in rows), Fraction(0)) for i in range(length))


def source_row(k: int) -> dict[str, object]:
    n = 3 * k
    length = n - 4
    a, _, _, _ = M.source_expectation(k, "A")
    b, _, _, _ = M.source_expectation(k, "B")
    zero = tuple(Fraction(0) for _ in range(length))
    keys = [(j, kind) for j in range(3) for kind in ("T", "D")]
    pieces = {
        key: tuple(b.get(key, zero)[i] - a.get(key, zero)[i] for i in range(length))
        for key in keys
    }
    combined = add_vectors([pieces[key] for key in keys], length)
    assert all(combined[i] == -combined[-1 - i] for i in range(length))
    assert combined[length // 2] == 0
    half = combined[: length // 2]
    signs = [(value > 0) - (value < 0) for value in half if value]
    sign_changes = sum(left != right for left, right in zip(signs, signs[1:]))
    threshold_candidate = all(
        (value <= 0 if ell < k - 1 else value >= 0)
        for ell, value in zip(range(2, 2 + len(half)), half)
    )
    return {
        "k": k,
        "n": n,
        "combined_reflection_exact": True,
        "combined_central_zero_exact": True,
        "n_times_combined_endpoint_l1": float(
            n * sum((abs(x) for x in combined), Fraction(0))
        ),
        "first_half_signs": signs,
        "first_half_sign_changes": sign_changes,
        "candidate_nonpositive_before_k_minus_1_nonnegative_after": threshold_candidate,
        "candidate_status": "exact finite falsification only; never a sign proof",
        "channel_kind_n_times_l1": {
            f"J{j}_{kind}": float(
                n * sum((abs(x) for x in pieces[(j, kind)]), Fraction(0))
            )
            for j, kind in keys
        },
    }


def witness() -> dict[str, object]:
    n = 9
    h = M.cyc(n, tuple(range(n)))
    s1 = M.mul(M.tr(n, 0, 2), M.tr(n, 6, 7))
    s2 = M.mul(M.tr(n, 1, 8), M.tr(n, 6, 7))
    e1 = jump_vector(n, h, s1)[0]
    e2 = jump_vector(n, h, s2)[0]
    assert e1 == Fraction(-625, 1296)
    assert e2 == Fraction(-20, 81)
    assert e1 != e2
    return {
        "k": 3,
        "same_size_run_profile_from_M264": "((1,1),(2,1),(6,2))",
        "E2_s1_exact": qstr(e1),
        "E2_s2_exact": qstr(e2),
        "distinct_literal_endpoint_profile": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "status": "exact finite falsification only; no PBV/SET/sign inference",
        "analytic_target_fixed_before_computation": True,
        "target": "M267 literal endpoint profile for M261 PBV",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "m261_dependency": str(M261_PATH.relative_to(ROOT)),
        "pointwise_checks": [validate_pointwise(k) for k in (3, 5)],
        "m264_firewall_witness": witness(),
        "source_checks": [source_row(k) for k in (3, 5, 7, 9)],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "pointwise": payload["pointwise_checks"],
        "source": payload["source_checks"],
        "witness": payload["m264_firewall_witness"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

