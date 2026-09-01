#!/usr/bin/env python3
"""Exact finite audit of the M51 leaf-threshold count inequalities.

Reads the exact weighted prefix-join-tree layers produced by M47.  A failure
would falsify the displayed universal counting consequence; a pass is not an
asymptotic proof.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
import sys
from pathlib import Path


def layers(path: Path, statistic: str) -> dict[int, int]:
    data = json.loads(path.read_text())["result"]["layers"][statistic]
    return dict(zip(data["support"], data["counts"], strict=True))


def tail(counts: dict[int, int], q: int) -> int:
    return sum(value for leaves, value in counts.items() if leaves >= q)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    all_layers: dict[int, dict[int, int]] = {3: {2: 24}}
    all_max_degree: dict[int, dict[int, int]] = {3: {2: 24}}
    for n in range(4, 9):
        source = args.source_dir / f"tree-dp-N{n}.json"
        all_layers[n] = layers(source, "leaf_count")
        all_max_degree[n] = layers(source, "max_degree")
    rows = []
    for n in range(4, 9):
        m = 2 * n - 2
        deletion_fiber = math.comb(m, 2) * (n - 1) ** 2
        for q in range(2, n):
            actual = tail(all_layers[n], q)
            base = tail(all_layers[n - 1], q - 1)
            upper = n * deletion_fiber * base
            sources = (n - q) * (m - 1) * base
            row = {
                "N": n,
                "q": q,
                "J_N_q": actual,
                "J_N_minus_1_q_minus_1": base,
                "deletion_upper": upper,
                "insertion_source_lower": sources,
                "deletion_inequality_holds": actual <= upper,
                "source_positive": sources > 0,
            }
            if not row["deletion_inequality_holds"] or not row["source_positive"]:
                raise AssertionError(row)
            rows.append(row)
    degree_rows = []
    for n in range(4, 9):
        m = 2 * n - 2
        deletion_fiber = math.comb(m, 2) * (n - 1) ** 2
        for q in range(2, n):
            actual = tail(all_max_degree[n], q)
            base = tail(all_max_degree[n - 1], q - 1)
            upper = n * deletion_fiber * base
            sources = (m - 1) * base
            row = {
                "N": n,
                "q": q,
                "D_N_q": actual,
                "D_N_minus_1_q_minus_1": base,
                "deletion_upper": upper,
                "insertion_source_lower": sources,
                "deletion_inequality_holds": actual <= upper,
                "source_positive": sources > 0,
            }
            if not row["deletion_inequality_holds"] or not row["source_positive"]:
                raise AssertionError(row)
            degree_rows.append(row)
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
        "convention": "(pq)(x)=p(q(x)); imported layers count literal ordered words",
        "claims_tested": [
            "For every leaf threshold, J_N(q)<=N*binom(2N-2,2)*(N-1)^2*J_(N-1)(q-1), and the certified insertion reservoir is nonempty.",
            "The analogous maximum-degree threshold inequality and one-attachment reservoir hold.",
        ],
        "scope_warning": "Exact N<=8 passes can falsify but cannot prove the universal theorem.",
        "source_artifacts": [str(args.source_dir / f"tree-dp-N{n}.json") for n in range(4, 9)],
        "rows": rows,
        "maximum_degree_rows": degree_rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"leaf_rows": len(rows), "degree_rows": len(degree_rows), "all_pass": True}, sort_keys=True))


if __name__ == "__main__":
    main()
