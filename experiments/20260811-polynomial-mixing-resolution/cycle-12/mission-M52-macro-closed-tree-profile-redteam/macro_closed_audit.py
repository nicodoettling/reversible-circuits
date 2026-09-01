#!/usr/bin/env python3
"""Finite exact audit for M52 low-profile macro-closed cuts.

The script reads exact weighted join-tree layers, tests the strand-deletion
low-tail inequalities, and computes global bridge counts from the character
content formula.  Finite passes can falsify the named claims but cannot prove
the universal theorem.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


def partitions(n: int, top: int | None = None):
    if n == 0:
        yield ()
        return
    if top is None or top > n:
        top = n
    for first in range(top, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def dimension(shape: tuple[int, ...]) -> int:
    n = sum(shape)
    hooks = 1
    for i, row in enumerate(shape):
        for j in range(row):
            below = sum(1 for lower in shape[i + 1 :] if lower > j)
            hooks *= row - j + below
    return math.factorial(n) // hooks


def content_sum(shape: tuple[int, ...]) -> int:
    return sum(j - i for i, row in enumerate(shape) for j in range(row))


def omega_count(n: int, m: int) -> int:
    numerator = 0
    for shape in partitions(n):
        f = dimension(shape)
        numerator += f * f * content_sum(shape) ** m
    ans, rem = divmod(numerator, math.factorial(n))
    if rem:
        raise AssertionError((n, m, rem))
    return ans


def layer(path: Path, statistic: str) -> dict[int, int]:
    d = json.loads(path.read_text())["result"]["layers"][statistic]
    return dict(zip(d["support"], d["counts"], strict=True))


def low(counts: dict[int, int], q: int) -> int:
    return sum(value for value_of_stat, value in counts.items() if value_of_stat < q)


def fraction_text(a: int, b: int) -> str:
    z = Fraction(a, b)
    return f"{z.numerator}/{z.denominator}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    leaf = {3: {2: 24}}
    balance = {3: {1: 24}}
    for n in range(4, 9):
        source = args.source_dir / f"tree-dp-N{n}.json"
        leaf[n] = layer(source, "leaf_count")
        balance[n] = layer(source, "edge_balance")
    rows = []
    masses = []
    for n in range(4, 9):
        m = 2 * n - 2
        fiber = math.comb(m, 2) * (n - 1) ** 2
        z = omega_count(n, m)
        c0 = math.factorial(m) * n ** (n - 3)
        masses.append({
            "N": n,
            "m": m,
            "Omega": z,
            "F_N": c0,
            "pi_F_exact": fraction_text(c0, z),
        })
        for statistic, data, thresholds in (
            ("leaf_count", leaf, range(3, n)),
            ("edge_balance", balance, range(2, n // 2 + 1)),
        ):
            for q in thresholds:
                current = low(data[n], q)
                base = low(data[n - 1], q)
                upper = n * fiber * base
                source_count = (m - 1) * base
                row = {
                    "statistic": statistic,
                    "N": n,
                    "q": q,
                    "low_N": current,
                    "low_N_minus_1": base,
                    "deletion_upper": upper,
                    "source_count": source_count,
                    "deletion_inequality_holds": current <= upper,
                    "source_positive": source_count > 0,
                    "pi_A_plus_exact": fraction_text(z - current, z),
                    "pi_complement_exact": fraction_text(current, z),
                }
                if not row["deletion_inequality_holds"] or not row["source_positive"]:
                    raise AssertionError(row)
                rows.append(row)
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
        "convention": "(pq)(x)=p(q(x)); global Omega count uses central transposition content eigenvalues",
        "claims_tested": [
            "Every low leaf-count tail satisfies l_N(q)<=N*binom(2N-2,2)*(N-1)^2*l_(N-1)(q).",
            "The analogous low edge-balance inequality holds, and each new canonical source reservoir is nonempty.",
            "The character-content formula reproduces exact global masses used for orientation.",
        ],
        "scope_warning": "Finite N<=8 passes can falsify but cannot prove the universal theorem.",
        "global_masses": masses,
        "rows": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"rows": len(rows), "all_pass": True}, sort_keys=True))


if __name__ == "__main__":
    main()
