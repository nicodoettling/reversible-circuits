#!/usr/bin/env python3
"""Bounded exact falsifier for M55 mixed-quadrant deletion/insertion lemmas."""

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
    x, y = blocked
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if (u == x and v == y) or (u == y and v == x) or v in seen:
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
                x = weight(records[n], lambda ell, bal: ell >= q and bal < r)
                y = total - x
                x_base = weight(
                    records[n - 1],
                    lambda ell, bal: ell >= q - 1 and bal < r,
                )
                y_base = weight(
                    records[n - 1],
                    lambda ell, bal: ell < q or bal >= r - 1,
                )
                row = {
                    "N": n,
                    "q": q,
                    "r": r,
                    "X_N": x,
                    "Y_N": y,
                    "X_base": x_base,
                    "Y_base": y_base,
                    "X_deletion_upper": n * lift * x_base,
                    "Y_deletion_upper": n * lift * y_base,
                    "X_deletion_holds": x <= n * lift * x_base,
                    "Y_deletion_holds": y <= n * lift * y_base,
                    "X_sources": (m - 1) * x_base,
                    "Y_sources": (m - 1) * y_base,
                }
                if not row["X_deletion_holds"] or not row["Y_deletion_holds"]:
                    raise AssertionError(row)
                if x and not x_base:
                    raise AssertionError(("missing X base", row))
                if y and not y_base:
                    raise AssertionError(("missing Y base", row))
                rows.append(row)

                if x:
                    checked = 0
                    for rec in records[n - 1]:
                        ell = rec["stats"]["leaf_count"]
                        bal = rec["stats"]["edge_balance"]
                        if ell < q - 1 or bal >= r:
                            continue
                        adj = adjacency(n - 1, rec["representative_edges"])
                        new_ell, new_bal = tree_stats(attach(adj, centroid(adj)))
                        if not (new_ell >= q and new_bal < r):
                            raise AssertionError(("X attachment failure", n, q, r, rec))
                        checked += 1
                    attachment_rows.append({
                        "kind": "X-centroid",
                        "N": n,
                        "q": q,
                        "r": r,
                        "base_shapes_checked": checked,
                    })

                if y:
                    checked = 0
                    for rec in records[n - 1]:
                        ell = rec["stats"]["leaf_count"]
                        bal = rec["stats"]["edge_balance"]
                        if ell >= q and bal < r - 1:
                            continue
                        adj = adjacency(n - 1, rec["representative_edges"])
                        if ell < q:
                            candidates = [
                                min(i for i, neighbors in enumerate(adj) if len(neighbors) == 1)
                            ]
                        elif bal >= r:
                            candidates = [0]
                        else:
                            candidates = list(range(n - 1))
                        possible = False
                        for u in candidates:
                            new_ell, new_bal = tree_stats(attach(adj, u))
                            if new_ell < q or new_bal >= r:
                                possible = True
                                break
                        if not possible:
                            raise AssertionError(("Y attachment failure", n, q, r, rec))
                        checked += 1
                    attachment_rows.append({
                        "kind": "Y-leaf-or-witness",
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
            "Mixed X deletion maps into {ell>=q-1,b<r} with M49 lift multiplicity.",
            "Mixed-complement deletion maps into {ell<q or b>=r-1}.",
            "Centroid attachment restores X and leaf/witness attachment restores its complement.",
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
