#!/usr/bin/env python3
"""Exact full-K conductance of N=5 midpoint transposition-length shells."""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SIG = load("m64_signature", HERE / "exact_n5_signature_closure.py")


def decode_prefix(code, length=4):
    answer = []
    for _ in range(length):
        code, digit = divmod(code, SIG.M)
        answer.append(digit)
    return tuple(answer)


def transposition_length(p):
    seen = [False] * len(p)
    cycles = 0
    for start in range(len(p)):
        if seen[start]:
            continue
        cycles += 1
        x = start
        while not seen[x]:
            seen[x] = True
            x = p[x]
    return len(p) - cycles


def flow_by_window(total_counts, cut_counts):
    result = {}
    for r, i in SIG.WINDOWS:
        numerator_by_size = Counter()
        totals = total_counts[(r, i)]
        for key, inside in cut_counts[(r, i)].items():
            total = totals[key]
            numerator_by_size[total] += inside * (total - inside)
        value = Fraction(0)
        for fiber_size, numerator in numerator_by_size.items():
            value += Fraction(numerator, 6 * (SIG.LENGTH - r + 1) * fiber_size)
        result[(r, i)] = value
    return result


def fraction_text(x):
    return f"{x.numerator}/{x.denominator}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    all_edges = SIG.M59.edges(SIG.N)
    all_codes, exterior = SIG.identity_words(all_edges)
    del exterior
    total_counts = SIG.group_counts(all_codes)
    endpoint_length = {}
    for code in all_codes:
        prefix = decode_prefix(code)
        endpoint = SIG.M59.evaluate(SIG.N, all_edges, prefix)
        endpoint_length[code] = transposition_length(endpoint)

    results = []
    omega = len(all_codes)
    midpoint = 4
    for q in (0, 2):
        cut = [code for code in all_codes if endpoint_length[code] <= q]
        cut_counts = SIG.group_counts(cut)
        by_window = flow_by_window(total_counts, cut_counts)
        for (r, i), value in by_window.items():
            crosses = i < midpoint < i + r
            if not crosses and value:
                raise AssertionError((q, r, i, value))
        by_r = {
            r: sum((value for (rr, _i), value in by_window.items() if rr == r), Fraction(0))
            for r in (3, 4, 5)
        }
        boundary = sum(by_r.values(), Fraction(0))
        smaller = min(len(cut), omega - len(cut))
        conductance = boundary / smaller
        results.append({
            "q": q,
            "cut_size": len(cut),
            "complement_size": omega - len(cut),
            "smaller_side": "cut" if len(cut) <= omega - len(cut) else "complement",
            "stationary_mass": fraction_text(Fraction(len(cut), omega)),
            "boundary_unnormalized_sum": fraction_text(boundary),
            "boundary_by_r": {str(r): fraction_text(by_r[r]) for r in (3, 4, 5)},
            "boundary_by_crossing_window": [
                {"r": r, "i_zero_based": i, "value": fraction_text(value)}
                for (r, i), value in sorted(by_window.items()) if value
            ],
            "conductance": fraction_text(conductance),
            "conductance_float": float(conductance),
        })

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
        "convention": "(pq)(x)=p(q(x)); midpoint prefix has four factors",
        "kernel": "literal lazy K via outside-window conditional-fiber cliques",
        "claim_tested": "At N=5, the thick midpoint transposition-length shells have exactly the reported global mass and full H3/H4/H5 conductance, and only midpoint-crossing windows contribute.",
        "scope_warning": "Finite N=5 conductance can falsify a universal local formula but cannot prove asymptotic shell expansion.",
        "N": SIG.N,
        "m": SIG.LENGTH,
        "omega": omega,
        "results": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(results, sort_keys=True))


if __name__ == "__main__":
    main()
