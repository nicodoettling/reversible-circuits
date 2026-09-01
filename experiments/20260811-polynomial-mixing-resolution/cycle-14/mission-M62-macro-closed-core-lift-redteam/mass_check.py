#!/usr/bin/env python3
"""Exact arithmetic calibration for the N=5 macro-closed core lifts."""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    n = 5
    m = 8
    omega = 1_770_940
    full = 1_008_000
    exterior = omega - full
    path_fiber = 7_808
    components = [1068, 1068, 997, 997, 997, 997, 842, 842]
    selected = [1068, 997, 997, 842]
    a = sum(selected)
    if sum(components) != path_fiber or 2 * a != path_fiber:
        raise AssertionError((components, selected))

    s = exterior + a
    s_complement = full - a
    sprime = omega - a
    sprime_complement = a
    if s + s_complement != omega or sprime + sprime_complement != omega:
        raise AssertionError("side-size mismatch")

    block_lengths = 3
    M = n * (n - 1) // 2
    Lambda = (m * (m - 1) // 2) * (n - 1) ** 2
    constant = Fraction(1, 2 * block_lengths * n * (n - 1) * Lambda * (m - 2) * M**3)
    if constant != Fraction(1, 322_560_000):
        raise AssertionError(constant)

    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "argv": sys.argv,
        "commit": commit,
        "python": platform.python_version(),
        "seed": None,
        "nonstandard_dependencies": {},
        "claim_tested": "The exact N=5 balanced-union masses and inherited M60 constant are arithmetically consistent.",
        "scope_warning": "This bounded arithmetic check cannot prove the universal complement-symmetry theorem.",
        "N": n,
        "m": m,
        "omega": omega,
        "minimal_macro": full,
        "exterior": exterior,
        "path_fiber": path_fiber,
        "core_component_sizes": components,
        "balanced_selection": selected,
        "A_size": a,
        "S_sizes": [s, s_complement],
        "S_prime_sizes": [sprime, sprime_complement],
        "exact_M60_constant": f"{constant.numerator}/{constant.denominator}",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"A_size": a, "S_sizes": [s, s_complement], "S_prime_sizes": [sprime, sprime_complement], "constant": str(constant)}, sort_keys=True))


if __name__ == "__main__":
    main()
