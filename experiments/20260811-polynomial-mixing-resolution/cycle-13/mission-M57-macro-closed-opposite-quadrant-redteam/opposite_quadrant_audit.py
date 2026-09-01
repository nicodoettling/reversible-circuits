#!/usr/bin/env python3
"""Bounded exact falsifier for M57 opposite-quadrant lemmas."""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
import sys
from collections import deque
from pathlib import Path


def adjacency(n: int, edges: list[list[int]]):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return adj


def component_size(adj: list[set[int]], start: int, blocked: tuple[int, int]) -> int:
    seen = {start}
    queue = deque([start])
    z, w = blocked
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if (u == z and v == w) or (u == w and v == z) or v in seen:
                continue
            seen.add(v)
            queue.append(v)
    return len(seen)


def tree_stats(adj: list[set[int]]) -> tuple[int, int]:
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
    scores = []
    for u in range(len(adj)):
        largest = max(
            (component_size(adj, v, (u, v)) for v in adj[u]),
            default=0,
        )
        scores.append((largest, u))
    return min(scores)[1]


def load_records(path: Path) -> list[dict]:
    return json.loads(path.read_text())["result"]["shape_records"]


def weight(records: list[dict], predicate) -> int:
    return sum(
        rec["weighted_contribution"]
        for rec in records
        if predicate(
            rec["stats"]["leaf_count"],
            rec["stats"]["edge_balance"],
        )
    )


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
    for n in range(4, 9):
        m = 2 * n - 2
        total = sum(rec["weighted_contribution"] for rec in records[n])
        expected = math.factorial(m) * n ** (n - 3)
        if total != expected:
            raise AssertionError((n, total, expected))
        base_total = sum(rec["weighted_contribution"] for rec in records[n - 1])
        lift = math.comb(m, 2) * (n - 1) ** 2
        for q in range(2, n):
            for r in range(1, n // 2 + 1):
                z = weight(records[n], lambda ell, bal: ell < q and bal >= r)
                w = total - z
                z_base = weight(
                    records[n - 1],
                    lambda ell, bal: ell < q and bal >= r - 1,
                )
                w_base = weight(
                    records[n - 1],
                    lambda ell, bal: ell >= q - 1 or bal < r,
                )
                row = {
                    "N": n,
                    "q": q,
                    "r": r,
                    "Z_N": z,
                    "W_N": w,
                    "Z_base": z_base,
                    "W_base": w_base,
                    "Z_deletion_upper": n * lift * z_base,
                    "W_deletion_upper": n * lift * w_base,
                    "Z_deletion_holds": z <= n * lift * z_base,
                    "W_deletion_holds": w <= n * lift * w_base,
                    "Z_sources": (m - 1) * z_base,
                    "W_sources": (m - 1) * w_base,
                }
                if not row["Z_deletion_holds"] or not row["W_deletion_holds"]:
                    raise AssertionError(row)
                if z and not z_base:
                    raise AssertionError(("missing Z base", row))
                if w and not w_base:
                    raise AssertionError(("missing W base", row))
                rows.append(row)

                if z:
                    checked = 0
                    for rec in records[n - 1]:
                        ell = rec["stats"]["leaf_count"]
                        bal = rec["stats"]["edge_balance"]
                        if ell >= q or bal < r - 1:
                            continue
                        adj = adjacency(n - 1, rec["representative_edges"])
                        leaves = [
                            u for u, neighbors in enumerate(adj) if len(neighbors) == 1
                        ]
                        possible = any(
                            (lambda pair: pair[0] < q and pair[1] >= r)(
                                tree_stats(attach(adj, u))
                            )
                            for u in leaves
                        )
                        if not possible:
                            raise AssertionError(("Z attachment failure", n, q, r, rec))
                        checked += 1
                    attachment_rows.append({
                        "kind": "Z-witness-leaf",
                        "N": n,
                        "q": q,
                        "r": r,
                        "base_shapes_checked": checked,
                    })

                if w:
                    checked = 0
                    for rec in records[n - 1]:
                        ell = rec["stats"]["leaf_count"]
                        bal = rec["stats"]["edge_balance"]
                        if ell < q - 1 and bal >= r:
                            continue
                        adj = adjacency(n - 1, rec["representative_edges"])
                        if bal < r:
                            candidates = [centroid(adj)]
                        else:
                            candidates = [
                                u for u, neighbors in enumerate(adj) if len(neighbors) > 1
                            ]
                        possible = any(
                            (lambda pair: pair[0] >= q or pair[1] < r)(
                                tree_stats(attach(adj, u))
                            )
                            for u in candidates
                        )
                        if not possible:
                            raise AssertionError(("W attachment failure", n, q, r, rec))
                        checked += 1
                    attachment_rows.append({
                        "kind": "W-centroid-or-nonleaf",
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
            "Opposite Z deletion maps into {ell<q,b>=r-1} with M49 lift multiplicity.",
            "Opposite-complement deletion maps into {ell>=q-1 or b<r}.",
            "Witness-side leaf attachment restores Z and centroid/nonleaf attachment restores its complement.",
        ],
        "scope_warning": "Finite N<=8 success can falsify but cannot prove the universal theorem.",
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
