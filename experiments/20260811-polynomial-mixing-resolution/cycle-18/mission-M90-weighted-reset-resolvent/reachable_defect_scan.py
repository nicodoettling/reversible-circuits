#!/usr/bin/env python3
"""Exact reachable-context scan of the weighted one-step defect.

This is a falsifier for the proposed boundary-layer condition
``r_U=U-A-QU>=0`` away from the fresh context ``(K,R)=(1,0)``.  It
enumerates the accepted reachable closure ``{(1,0)} union {K>R>=1}`` and
retains every attachment rank ``j>=1``.  Finite survival proves no theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import time
from fractions import Fraction
from pathlib import Path

import exact_weighted_resolvent as EXACT
from boundary_layer_scan import U, children, defect, record


def scan(s_max: int, k_max: int) -> dict[str, object]:
    negatives = []
    negative_nonfresh = []
    minimum = None
    minimum_nonfresh = None
    contexts = 0
    for s in range(2, s_max + 1):
        for K in range(1, k_max + 1):
            for R in range(K):
                if R == 0 and K > 1:
                    continue
                for B in range(1, s + 1):
                    x = (s, K, R, B)
                    contexts += 1
                    value = defect(x)
                    normalized = value / U(x)
                    row = {
                        "context": list(x),
                        "U": record(U(x)),
                        "reset_budget": record(EXACT.reset_budget(*x)),
                        "deep_U": record(sum(
                            (weight * U(child) for weight, child in children(x)),
                            Fraction(),
                        )),
                        "defect": record(value),
                        "normalized_defect": record(normalized),
                        "fresh": (K, R) == (1, 0),
                    }
                    if minimum is None or normalized < minimum[0]:
                        minimum = (normalized, row)
                    if (K, R) != (1, 0):
                        if minimum_nonfresh is None or normalized < minimum_nonfresh[0]:
                            minimum_nonfresh = (normalized, row)
                    if value < 0:
                        negatives.append(row)
                        if (K, R) != (1, 0):
                            negative_nonfresh.append(row)
    return {
        "contexts": contexts,
        "negative_defect_count": len(negatives),
        "negative_nonfresh_defect_count": len(negative_nonfresh),
        "all_negative_defects": negatives,
        "first_negative_nonfresh_defects": negative_nonfresh[:3],
        "minimum_normalized_defect": {
            "value": record(minimum[0]),
            "row": minimum[1],
        },
        "minimum_normalized_nonfresh_defect": {
            "value": record(minimum_nonfresh[0]),
            "row": minimum_nonfresh[1],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=12)
    parser.add_argument("--k-max", type=int, default=32)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    result = scan(args.s_max, args.k_max)
    payload = {
        "claim_tested": "r_U>=0 on every reachable nonfresh context",
        "finite_scope_warning": "Exact bounded survival proves no universal inequality.",
        "arithmetic": "fractions.Fraction exact grouped recurrences",
        "normalization": "Q=rho*nu for every j>=1; U=q(1-q)K/(R+1)",
        "strict_phase": "P=s+K-R decreases on every retained deep child",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "parameters": {"s_max": args.s_max, "k_max": args.k_max},
        "elapsed_seconds": time.time() - started,
        "result": result,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "elapsed_seconds": payload["elapsed_seconds"],
        "contexts": result["contexts"],
        "negative_defect_count": result["negative_defect_count"],
        "negative_nonfresh_defect_count": result["negative_nonfresh_defect_count"],
        "all_negative_defects": result["all_negative_defects"],
        "minimum_normalized_nonfresh_defect": result["minimum_normalized_nonfresh_defect"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
