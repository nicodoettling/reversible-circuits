#!/usr/bin/env python3
"""Exact coefficient diagnostic for the endpoint-matched matching reference.

For a Dyck path P of semilength n, let p(P) be the number of perfect
matchings with opener/closer path P, namely the product of the pre-down-step
heights.  The reference area coefficient is

    G_n(a)=sum_{Area(P)=a} p(P).

It is computed by an exact height/area transfer.  The exponential tilt

    q_n=[(n+1)^(n-1)/n!]^(1/[n(n-1)])

matches exactly the bottom-to-mountain density ratio of the connected
minimal-identity path law.  Floating logs are used only to normalize the
tilted probabilities; all unnormalized G_n(a) are exact integers.

Finite output can falsify, but never prove, the proposed universal reference
quartile or polynomial comparison to the connected law.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, Mapping


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return "unavailable"


def matching_area_counts(n: int) -> Dict[int, int]:
    dp: Dict[tuple[int, int], int] = {(0, 0): 1}
    for _ in range(2 * n):
        nxt: Dict[tuple[int, int], int] = defaultdict(int)
        for (height, area), count in dp.items():
            if height < n:
                nxt[(height + 1, area + height + 1)] += count
            if height:
                # Choose which of the height open endpoints is closed.
                nxt[(height - 1, area + height - 1)] += height * count
        dp = dict(nxt)
    answer = {a: v for (h, a), v in sorted(dp.items()) if h == 0}
    if sum(answer.values()) != math.prod(range(1, 2 * n, 2)):
        raise AssertionError((n, sum(answer.values())))
    return answer


def log_q(n: int) -> float:
    if n <= 1:
        return 0.0
    return ((n - 1) * math.log(n + 1) - math.lgamma(n + 1)) / (n * (n - 1))


def normalized_log_masses(counts: Mapping[int, int], logq: float) -> Dict[int, float]:
    raw = {a: math.log(v) + a * logq for a, v in counts.items()}
    peak = max(raw.values())
    logz = peak + math.log(sum(math.exp(x - peak) for x in raw.values()))
    return {a: x - logz for a, x in raw.items()}


def quartile(logmass: Mapping[int, float]) -> Dict[str, float | int | bool]:
    cumulative = 0.0
    layers = []
    for area in sorted(logmass):
        mass = math.exp(logmass[area])
        cumulative += mass
        layers.append((area, mass, cumulative))
    first = next(x for x in layers if x[2] >= 0.25 - 1e-14)
    lower_half = [x for x in layers if x[2] <= 0.5 + 1e-14]
    monotone = all(
        lower_half[i][1] <= lower_half[i + 1][1] * (1 + 1e-12)
        for i in range(len(lower_half) - 1)
    )
    return {
        "area": first[0],
        "cdf": first[2],
        "layer_over_cdf": first[1] / first[2],
        "cdf_at_most_half": first[2] <= 0.5 + 1e-12,
        "lower_half_monotone_float_check": monotone,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--actual", type=Path, required=True)
    parser.add_argument("--reference-max-n", type=int, default=60)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    actual_payload = json.loads(args.actual.read_text())
    actual_by_n = {
        int(r["N"]) - 1: r for r in actual_payload["records"]
    }
    records = []
    any_quartile_failure = False
    any_actual_threshold_disagreement = False
    for n in range(2, args.reference_max_n + 1):
        counts = matching_area_counts(n)
        lq = log_q(n)
        ref_logs = normalized_log_masses(counts, lq)
        ref_quartile = quartile(ref_logs)
        any_quartile_failure |= not bool(ref_quartile["cdf_at_most_half"])
        record: Dict[str, object] = {
            "n": n,
            "N": n + 1,
            "area_layer_count": len(counts),
            "matching_total": sum(counts.values()),
            "log_q": lq,
            "q_float": math.exp(lq),
            "reference_quartile": ref_quartile,
        }
        if n in actual_by_n:
            raw = actual_by_n[n]
            actual_counts = {int(a): int(v) for a, v in raw["area_counts"].items()}
            actual_total = int(raw["hurwitz_total"])
            actual_logs = {
                a: math.log(v) - math.log(actual_total)
                for a, v in actual_counts.items()
            }
            actual_quartile = quartile(actual_logs)
            ratios = [
                math.exp(actual_logs[a] - ref_logs[a])
                for a in sorted(actual_logs)
            ]
            same_threshold = actual_quartile["area"] == ref_quartile["area"]
            any_actual_threshold_disagreement |= not same_threshold
            record["actual_comparison"] = {
                "actual_quartile": actual_quartile,
                "same_first_quartile_area": same_threshold,
                "min_normalized_density_ratio": min(ratios),
                "max_normalized_density_ratio": max(ratios),
                "density_distortion": max(ratios) / min(ratios),
                "total_variation_float": 0.5 * sum(
                    abs(math.exp(actual_logs[a]) - math.exp(ref_logs[a]))
                    for a in actual_logs
                ),
            }
        records.append(record)

    output = {
        "metadata": {
            "command": " ".join(sys.argv),
            "repository_commit": git_commit(),
            "python": sys.version,
            "platform": platform.platform(),
            "deterministic": True,
            "seed": None,
            "nonstandard_dependencies": [],
        },
        "claims_tested": [
            "Every endpoint-matched q-tilted matching reference has a first quartile with CDF at most 1/2.",
            "The actual and reference first-quartile areas agree for every N (one finite disagreement refutes this exact conjecture).",
            "Finite density distortions are diagnostics only; they do not prove polynomial comparison.",
        ],
        "reference_quartile_failure_found": any_quartile_failure,
        "actual_threshold_disagreement_found": any_actual_threshold_disagreement,
        "records": records,
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "reference_quartile_failure_found": any_quartile_failure,
        "actual_threshold_disagreement_found": any_actual_threshold_disagreement,
        "max_n": args.reference_max_n,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
