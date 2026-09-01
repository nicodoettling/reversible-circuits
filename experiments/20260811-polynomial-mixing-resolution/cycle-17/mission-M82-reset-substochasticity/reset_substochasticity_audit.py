#!/usr/bin/env python3
"""Exact bounded audit of eliminated canonical reset potentials.

The kernel implementation is the frozen, independently refereed M79
``fractions.Fraction`` implementation.  This wrapper evaluates new M82
potentials and records exact extrema; bounded success is a falsifier only.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import platform
from fractions import Fraction
from pathlib import Path


def load_m79():
    path = Path(__file__).resolve().parents[1] / (
        "mission-M79-m76-referee-resolvent/independent_audit.py"
    )
    spec = importlib.util.spec_from_file_location("m79_exact", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M79 = load_m79()


def record(value: Fraction, context: tuple[int, int, int, int]) -> dict:
    return {
        "context": list(context),
        "decimal": float(value),
        "exact": f"{value.numerator}/{value.denominator}",
    }


def scan(s_max: int, k_max: int) -> dict:
    maxima = {
        "unweighted_eliminated_row": (Fraction(-1), None),
        "right_heavy_unweighted_eliminated_row": (Fraction(-1), None),
        "row_over_u_one_minus_q": (Fraction(-1), None),
        "eliminated_W_over_W": (Fraction(-1), None),
    }
    failures = {key: [] for key in maxima}
    raw_constant_first = None
    contexts = 0
    for s in range(2, s_max + 1):
        for K in range(1, k_max + 1):
            for R in range(K):
                # Exact reachable closure after canonical resets.
                if R == 0 and K > 1:
                    continue
                for B in range(1, s + 1):
                    x = (s, K, R, B)
                    contexts += 1
                    q = M79.q_split(s, B)
                    _, deep, reset, _ = M79.split(*x)
                    raw = sum(deep.values(), Fraction()) + sum(
                        reset.values(), Fraction()
                    )
                    if raw > 1 and raw_constant_first is None:
                        raw_constant_first = {
                            "context": list(x),
                            "raw_row": f"{raw.numerator}/{raw.denominator}",
                            "deep_row": str(sum(deep.values(), Fraction())),
                            "reset_row": str(sum(reset.values(), Fraction())),
                        }

                    eliminated = M79.eliminated(*x)[1]
                    row = sum(eliminated.values(), Fraction())
                    u_bound = (K - R) * (1 - q)
                    W_parent = (1 - q) * Fraction(K, R + 1)
                    W_child_sum = sum(
                        coefficient
                        * (1 - M79.q_split(child[0], child[3]))
                        * Fraction(child[1], child[2] + 1)
                        for child, coefficient in eliminated.items()
                    )
                    values = {
                        "unweighted_eliminated_row": row,
                        "row_over_u_one_minus_q": row / u_bound,
                        "eliminated_W_over_W": W_child_sum / W_parent,
                    }
                    if R == K - 1:
                        values["right_heavy_unweighted_eliminated_row"] = row
                    for key, value in values.items():
                        if value > maxima[key][0]:
                            maxima[key] = (value, x)
                        if value > 1:
                            failures[key].append({
                                "context": list(x),
                                "ratio": f"{value.numerator}/{value.denominator}",
                            })
    return {
        "contexts": contexts,
        "reachable_closure": "(K,R)=(1,0) or K>R>=1",
        "maxima": {
            key: record(value, context)
            for key, (value, context) in maxima.items()
        },
        "failure_counts": {key: len(value) for key, value in failures.items()},
        "first_failures": {key: value[:3] for key, value in failures.items()},
        "raw_constant_first_failure": raw_constant_first,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=8)
    parser.add_argument("--k-max", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "claim_tested": (
            "Exact bounded eliminated reset substochasticity and "
            "W=(1-q)K/(R+1) superharmonicity"
        ),
        "finite_scope_warning": "No bounded scan proves a universal inequality.",
        "arithmetic": "fractions.Fraction",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "parameters": {"s_max": args.s_max, "k_max": args.k_max},
        "result": scan(args.s_max, args.k_max),
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "result": result["result"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
