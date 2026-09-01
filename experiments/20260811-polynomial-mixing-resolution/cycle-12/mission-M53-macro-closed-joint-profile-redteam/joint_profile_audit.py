#!/usr/bin/env python3
"""Exact finite falsifier for the M53 joint-profile lemmas.

The universal proof is combinatorial.  This script only tests, through N=8,
the two weighted deletion inequalities and existence of one leaf attachment
which simultaneously restores the two tight profile constraints.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
import sys
from collections import defaultdict, deque
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
    answer, remainder = divmod(numerator, math.factorial(n))
    if remainder:
        raise AssertionError((n, m, remainder))
    return answer


def adjacency(n: int, edges: list[list[int]] | list[tuple[int, int]]):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return adj


def component_size(adj: list[set[int]], start: int, blocked: tuple[int, int]) -> int:
    seen = {start}
    queue = deque([start])
    x, y = blocked
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if (u == x and v == y) or (u == y and v == x) or v in seen:
                continue
            seen.add(v)
            queue.append(v)
    return len(seen)


def stats(adj: list[set[int]]) -> tuple[int, int]:
    n = len(adj)
    leaves = sum(len(neighbors) == 1 for neighbors in adj)
    balance = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                side = component_size(adj, u, (u, v))
                balance = max(balance, min(side, n - side))
    return leaves, balance


def attach(adj: list[set[int]], u: int) -> list[set[int]]:
    out = [set(neighbors) for neighbors in adj] + [set()]
    v = len(adj)
    out[u].add(v)
    out[v].add(u)
    return out


def centroid(adj: list[set[int]]) -> int:
    n = len(adj)
    scores = []
    for u in range(n):
        largest = 0
        for v in adj[u]:
            largest = max(largest, component_size(adj, v, (u, v)))
        scores.append((largest, u))
    return min(scores)[1]


def load_records(path: Path) -> list[dict]:
    data = json.loads(path.read_text())
    return data["result"]["shape_records"]


def joint_count(records: list[dict], q: int, r: int) -> int:
    return sum(
        rec["weighted_contribution"]
        for rec in records
        if rec["stats"]["leaf_count"] >= q
        and rec["stats"]["edge_balance"] >= r
    )


def fraction_text(a: int, b: int) -> str:
    value = Fraction(a, b)
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    records: dict[int, list[dict]] = {
        3: [{
            "representative_edges": [[0, 1], [1, 2]],
            "stats": {"leaf_count": 2, "edge_balance": 1},
            "weighted_contribution": 24,
        }]
    }
    for n in range(4, 9):
        records[n] = load_records(args.source_dir / f"tree-dp-N{n}.json")

    rows = []
    attachment_rows = []
    global_masses = []
    for n in range(4, 9):
        m = 2 * n - 2
        total = sum(rec["weighted_contribution"] for rec in records[n])
        expected = math.factorial(m) * n ** (n - 3)
        if total != expected:
            raise AssertionError((n, total, expected))
        omega = omega_count(n, m)
        global_masses.append({
            "N": n,
            "m": m,
            "Omega": omega,
            "F_N": total,
            "pi_F_exact": fraction_text(total, omega),
        })
        lift = math.comb(m, 2) * (n - 1) ** 2
        base_total = sum(rec["weighted_contribution"] for rec in records[n - 1])
        for q in range(2, n):
            for r in range(1, n // 2 + 1):
                high = joint_count(records[n], q, r)
                low = total - high
                high_base = joint_count(records[n - 1], q - 1, r - 1)
                low_base = base_total - joint_count(records[n - 1], q, r)
                high_upper = n * lift * high_base
                low_upper = n * lift * low_base
                row = {
                    "N": n,
                    "q": q,
                    "r": r,
                    "joint_high_N": high,
                    "joint_low_N": low,
                    "high_base_q_minus_1_r_minus_1": high_base,
                    "low_base_q_r": low_base,
                    "high_deletion_upper": high_upper,
                    "low_deletion_upper": low_upper,
                    "high_deletion_holds": high <= high_upper,
                    "low_deletion_holds": low <= low_upper,
                    "high_square_sources": (m - 1) * high_base,
                    "low_square_sources": (m - 1) * low_base,
                    "pi_A_plus_exact": fraction_text(omega - low, omega),
                    "pi_A_plus_complement_exact": fraction_text(low, omega),
                    "pi_A_minus_exact": fraction_text(omega - high, omega),
                    "pi_A_minus_complement_exact": fraction_text(high, omega),
                }
                if not row["high_deletion_holds"] or not row["low_deletion_holds"]:
                    raise AssertionError(row)
                if high and not high_base:
                    raise AssertionError(("missing high base", row))
                if low and not low_base:
                    raise AssertionError(("missing low base", row))
                rows.append(row)

                # Shape-level existence check for the high insertion.  The
                # universal proof supplies a canonical choice; exhaustive
                # attachment here can only falsify existence.
                if high:
                    checked = 0
                    for rec in records[n - 1]:
                        old_l = rec["stats"]["leaf_count"]
                        old_b = rec["stats"]["edge_balance"]
                        if old_l < q - 1 or old_b < r - 1:
                            continue
                        adj = adjacency(n - 1, rec["representative_edges"])
                        possible = [
                            u for u in range(n - 1)
                            if (lambda z: z[0] >= q and z[1] >= r)(stats(attach(adj, u)))
                        ]
                        if not possible:
                            raise AssertionError(("high attachment failure", n, q, r, rec))
                        checked += 1
                    attachment_rows.append({
                        "kind": "high",
                        "N": n,
                        "q": q,
                        "r": r,
                        "base_shapes_checked": checked,
                    })

                if low:
                    checked = 0
                    for rec in records[n - 1]:
                        old_l = rec["stats"]["leaf_count"]
                        old_b = rec["stats"]["edge_balance"]
                        if old_l >= q and old_b >= r:
                            continue
                        adj = adjacency(n - 1, rec["representative_edges"])
                        if old_l < q:
                            u = min(i for i, neighbors in enumerate(adj) if len(neighbors) == 1)
                        else:
                            u = centroid(adj)
                        new_l, new_b = stats(attach(adj, u))
                        if new_l >= q and new_b >= r:
                            raise AssertionError(("low attachment failure", n, q, r, rec, u))
                        checked += 1
                    attachment_rows.append({
                        "kind": "low",
                        "N": n,
                        "q": q,
                        "r": r,
                        "base_shapes_checked": checked,
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
        "convention": "(pq)(x)=p(q(x)); join tree from prefix cycle joins",
        "claims_tested": [
            "Joint-high deletion: H_N(q,r)<=N*binom(2N-2,2)*(N-1)^2*H_(N-1)(q-1,r-1).",
            "Joint-low deletion: C_N(q,r)<=N*binom(2N-2,2)*(N-1)^2*C_(N-1)(q,r).",
            "Every relevant base shape admits the claimed one-leaf high or low attachment.",
            "The character-content formula gives the literal global masses used for orientation.",
        ],
        "scope_warning": "Finite N<=8 success can falsify but cannot prove the universal theorem.",
        "global_masses": global_masses,
        "rows": rows,
        "attachment_rows": attachment_rows,
        "summary": {
            "threshold_rows": len(rows),
            "attachment_rows": len(attachment_rows),
            "all_pass": True,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
