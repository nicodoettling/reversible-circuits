#!/usr/bin/env python3
"""Exact genus-zero support-component audit for matching endpoints.

This checks finite masses and records the universal block EGF calculation.
The latter proves that the genus-zero assembly conditioned to l/2 components
is beyond its finite-mean critical saddle. It does not determine the full
bridge, which also contains positive-genus components.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import platform
from fractions import Fraction
from pathlib import Path


def load_character_module():
    path = Path(__file__).with_name("perfect_matching_square_mode.py")
    spec = importlib.util.spec_from_file_location("matching_character", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CHAR = load_character_module()


def block_weight(k: int) -> Fraction:
    # F_k/(3k-2)! for a fixed product of cycle type 2^k.
    return Fraction(4**k) * Fraction(2 * k) ** (k - 3)


def coefficient_power(length: int, components: int) -> Fraction:
    # [z^length] B(z)^components/components!, B=sum b_k z^k/k!.
    atom = [Fraction(0)] * (length + 1)
    for k in range(1, length + 1):
        atom[k] = block_weight(k) / math.factorial(k)
    poly = [Fraction(0)] * (length + 1)
    poly[0] = Fraction(1)
    for _ in range(components):
        new = [Fraction(0)] * (length + 1)
        for i, value in enumerate(poly):
            if not value:
                continue
            for k in range(1, length - i + 1):
                new[i + k] += value * atom[k]
        poly = new
    return poly[length] / math.factorial(components)


def record(length: int) -> dict:
    n = 2 * length
    components = length // 2
    coefficient = coefficient_power(length, components)
    genus_zero_count = (
        math.factorial(2 * length) * math.factorial(length) * coefficient
    )
    assert genus_zero_count.denominator == 1
    scaled_total = CHAR.scaled_completion(n, length, (2,) * length)
    total_count = Fraction(scaled_total, math.factorial(n))
    assert total_count.denominator == 1
    ratio = genus_zero_count / total_count
    return {
        "N": n,
        "length": length,
        "genus_zero_component_count": components,
        "genus_zero_word_count": str(genus_zero_count),
        "total_word_count": str(total_count),
        "genus_zero_mass": str(ratio),
        "genus_zero_mass_decimal": float(ratio),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lengths", default="4,6,8,10,12")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    lengths = [int(x) for x in args.lengths.split(",") if x]
    assert all(length >= 4 and length % 2 == 0 for length in lengths)
    payload = {
        "status": "complete",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "composition": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "genus_zero_formula": (
            "F_k=(3k-2)! (2k)^(k-3) 4^k; "
            "B(z)=sum_k F_k/(3k-2)! z^k/k!"
        ),
        "tree_function_identity": (
            "B(z)=(1/8)(T-3T^2/4+T^3/6), T=8z exp(T)"
        ),
        "critical_values": {
            "rho": "1/(8e)",
            "B(rho)": "5/96",
            "rho_B_prime(rho)": "1/16",
            "critical_mean": "6/5",
            "conditioned_mean_for_l_over_2_components": "2",
        },
        "scope_warning": (
            "The critical-mean calculation is universal for the genus-zero "
            "sector. Finite masses do not prove its full-bridge asymptotic "
            "mass, condensation, or any spectral conclusion."
        ),
        "records": [record(length) for length in lengths],
    }
    Path(args.output).write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
