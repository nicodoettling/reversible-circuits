#!/usr/bin/env python3
"""Emit the stable clean-room M171 audit payload for exactly k=3,5."""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
from pathlib import Path

from independent_phase_audit import analyze


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--frozen-m168", type=Path, required=True)
    args = parser.parse_args()

    # Both exact reconstructions finish before the frozen output is consulted.
    results = [analyze(3), analyze(5)]
    for row in results:
        row.pop("runtime_seconds")
        pair_checks = row.pop("completion_size_checks")
        row["completion_support_checks"] = pair_checks
        row["nonzero_completion_size_checks"] = sum(
            row["topology_nonzero_counts"].values()
        )

    frozen = json.loads(args.frozen_m168.read_text())
    frozen_by_k = {row["k"]: row for row in frozen["results"]}
    comparisons = []
    for row in results:
        if row["signed_sum_exact"] != frozen_by_k[row["k"]]["signed_sum_exact"]:
            raise AssertionError((row, frozen_by_k[row["k"]]))
        comparisons.append({"k": row["k"], "signed_sum_exact_match": True})

    payload = {
        "status": "fresh exact finite referee; no asymptotic inference",
        "target": "M168 fixed first physical cell of the M73 nonlazy cyclic rank-two quotient",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "scope_cap": [3, 5],
        "raw_pair_reconstruction": True,
        "imports_m168_code": False,
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "frozen_m168_comparisons": comparisons,
        "results": results,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

