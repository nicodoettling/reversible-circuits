#!/usr/bin/env python3
"""Four predeclared exact guards for the M273 root-seam formulas.

The cases were frozen in checkpoint.md before this file was created.  This
script imports no predecessor code or data.  It reconstructs the plus-mirror
DPS hairy contour from Proposition 3 and executes the cyclic LIFO closure of
Lemma 2/RandomQuad.  Four cases are finite calibration, never an all-rank
proof.
"""

from __future__ import annotations

import hashlib
import json
import platform
from collections import defaultdict, deque
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "root_seam_guard_results.json"


def edge(a: int, b: int) -> tuple[int, int]:
    if a == b:
        raise AssertionError("loop is not a transposition")
    return (a, b) if a < b else (b, a)


def parents(tree: tuple[tuple[int, int], ...], root: int) -> dict[int, int | None]:
    graph: dict[int, list[int]] = defaultdict(list)
    for a, b in tree:
        graph[a].append(b)
        graph[b].append(a)
    parent: dict[int, int | None] = {root: None}
    queue = deque([root])
    while queue:
        a = queue.popleft()
        for b in graph[a]:
            if b not in parent:
                parent[b] = a
                queue.append(b)
    if set(parent) != set(range(1, root + 1)) or len(tree) != root - 1:
        raise AssertionError("edge set is not a tree on the declared rank")
    return parent


def canonical_order(rank: int) -> tuple[int, ...]:
    return (2 * rank - 3, 2 * rank - 2, *range(1, 2 * rank - 3))


def odd_edit(order: tuple[int, ...], v: int) -> tuple[int, ...]:
    left = 2 * v - 3
    return tuple(left + 1 if q == left else left if q == left + 1 else q for q in order)


def contour(
    tree: tuple[tuple[int, int], ...], rank: int, v: int
) -> tuple[list[tuple], dict[int, int]]:
    """Literal plus-mirror hairy contour and first black endpoint by label."""

    parent = parents(tree, rank)
    order = odd_edit(canonical_order(rank), v)
    incidence: dict[tuple[str, int], dict[int, tuple[str, int]]] = defaultdict(dict)
    first_black: dict[int, int] = {}
    for a in range(1, rank):
        left, right = order[2 * a - 2 : 2 * a]
        black = ("B", a)
        for label, white_index in ((left, a), (right, parent[a])):
            if white_index is None:
                raise AssertionError("a nonroot slot points outside the tree")
            white = ("W", white_index)
            incidence[black][label] = white
            incidence[white][label] = black
            first_black[label] = a

    modulus = 2 * rank - 2
    start = (("W", rank), modulus)
    if modulus not in incidence[start[0]]:
        raise AssertionError("the chosen root corner is not an incidence")

    tokens: list[tuple] = []
    state = start
    seen: set[tuple[tuple[str, int], int]] = set()
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        step = 1 if vertex[0] == "W" else -1
        label = 1 + ((incoming - 1 + step) % modulus)
        neighbor = incidence[vertex].get(label)
        if neighbor is None:
            tokens.append(("H", vertex[0], vertex[1], label))
            state = (vertex, label)
        else:
            tokens.append(("S", vertex, neighbor, label))
            state = (neighbor, label)
    if state != start:
        raise AssertionError("contour failed to return to its start corner")
    return tokens, first_black


def cycle_rotation(tokens: list[tuple]) -> list[tuple]:
    balance = 0
    minimum = 0
    last_minimum = -1
    for j, token in enumerate(tokens):
        if token[0] == "H":
            balance += 1 if token[1] == "W" else -1
        if balance <= minimum:
            minimum = balance
            last_minimum = j
    cut = (last_minimum + 1) % len(tokens)
    return tokens[cut:] + tokens[:cut]


def close(
    tree: tuple[tuple[int, int], ...], rank: int, v: int
) -> dict:
    tokens, first_black = contour(tree, rank, v)
    reduced: list[tuple] = []
    second_black: dict[int, int] = {}
    rows: list[dict] = []

    for token in cycle_rotation(tokens):
        if token[0] != "H" or token[1] == "W":
            reduced.append(token)
            continue

        white_pos = next(
            (j for j in range(len(reduced) - 1, -1, -1) if reduced[j][0] == "H"),
            None,
        )
        if white_pos is None:
            raise AssertionError("cycle rotation left an unmatched black")
        white = reduced[white_pos]
        if white[1] != "W" or white[3] != token[3]:
            raise AssertionError("LIFO pair violates the same-label rule")
        interior = reduced[white_pos + 1 :]
        if any(item[0] != "S" for item in interior):
            raise AssertionError("a half-edge remains inside a complete node")
        distance = len(interior)
        if distance not in (1, 3):
            raise AssertionError(f"illegal DPS side distance {distance}")
        row = {
            "label": white[3],
            "white": white[2],
            "black": token[2],
            "distance": distance,
        }
        rows.append(row)
        if distance == 3:
            if white[3] in second_black:
                raise AssertionError("a label acquired two distance-three rows")
            second_black[white[3]] = token[2]
        reduced[white_pos:] = [("S", "closure", white[3])]

    remaining = [token for token in reduced if token[0] == "H"]
    modulus = 2 * rank - 2
    if len(remaining) != modulus or any(token[1] != "W" for token in remaining):
        raise AssertionError("closure did not leave precisely the final-root whites")
    if sorted(token[3] for token in remaining) != list(range(1, modulus + 1)):
        raise AssertionError("final-root white labels are not a permutation")

    remaining_white = {token[3]: token[2] for token in remaining}
    endpoints = {q: second_black.get(q, rank) for q in range(1, modulus + 1)}
    word = tuple(
        edge(first_black[q] - 1, endpoints[q] - 1) for q in range(1, modulus + 1)
    )
    return {
        "rows": rows,
        "second_black": second_black,
        "endpoints": endpoints,
        "remaining_white": remaining_white,
        "word": word,
    }


def path_to_one(parent: dict[int, int | None], v: int) -> tuple[int, ...]:
    path = [v]
    while path[-1] != 1:
        nxt = parent[path[-1]]
        if nxt is None:
            raise AssertionError("stopped path reached the root before white 1")
        path.append(nxt)
    return tuple(path)


def matching_rows(data: dict, label: int, *, black: int, distance: int) -> list[dict]:
    return [
        row
        for row in data["rows"]
        if row["label"] == label
        and row["black"] == black
        and row["distance"] == distance
    ]


def audit_case(spec: dict) -> dict:
    d = spec["d"]
    v = spec["v"]
    tree = tuple(sorted(edge(*pair) for pair in spec["tree"]))
    parent = parents(tree, d)
    path = path_to_one(parent, v)
    decreasing = all(a > b for a, b in zip(path, path[1:]))
    if decreasing != spec["open"]:
        raise AssertionError("declared open/sealed classification is wrong")

    old = close(tree, d, v)
    plus_tree = tuple(sorted((*tree, edge(1, d + 1))))
    new = close(plus_tree, d + 1, v)
    m = 2 * d - 2
    alpha, beta, gamma, delta = m - 1, m, m + 1, m + 2

    if decreasing:
        expected_old = {alpha: v, beta: d}
        expected_new = {alpha: 1, beta: 1, gamma: v, delta: d + 1}
    else:
        expected_old = {alpha: d, beta: d}
        expected_new = {alpha: 1, beta: 1, gamma: d + 1, delta: d + 1}
    got_old = {q: old["endpoints"][q] for q in expected_old}
    got_new = {q: new["endpoints"][q] for q in expected_new}
    if got_old != expected_old or got_new != expected_new:
        raise AssertionError("root endpoint table failed")

    # The new child d always contributes the seam macro beta then alpha,
    # both at distance three to current-parent black x_1.
    for q, white in ((beta, d), (alpha, 1)):
        rows = matching_rows(new, q, black=1, distance=3)
        if len(rows) != 1 or rows[0]["white"] != white:
            raise AssertionError("new-child seam macro row failed")

    if decreasing:
        old_top = matching_rows(old, alpha, black=v, distance=3)
        new_top = matching_rows(new, gamma, black=v, distance=3)
        if len(old_top) != 1 or old_top[0]["white"] != d:
            raise AssertionError("old top-lens row failed")
        if len(new_top) != 1 or new_top[0]["white"] != d + 1:
            raise AssertionError("new top-lens row failed")

    port_checks = []
    for port in spec.get("ports", ()):
        h = port["h"]
        labels = (2 * h - 3, 2 * h - 2)
        expected = port["endpoint"]
        got = {
            "old": [old["endpoints"][q] for q in labels],
            "new": [new["endpoints"][q] for q in labels],
        }
        if expected == "root":
            wanted = {"old": [d, d], "new": [d + 1, d + 1]}
            for q in labels:
                if q in old["second_black"] or q in new["second_black"]:
                    raise AssertionError("persistent port closed before final root")
        else:
            wanted = {"old": [expected, expected], "new": [expected, expected]}
        if got != wanted:
            raise AssertionError("individual port endpoint failed")
        port_checks.append({"h": h, "labels": labels, "expected": wanted, "got": got})

    # The full inherited low endpoint consequence is equality in the sealed
    # case and exactly E_v final-root transport in the open case.
    exposed = {2 * v - 2}
    exposed.update(
        q
        for h in range(v + 1, d)
        if parent[h] == v
        for q in (2 * h - 3, 2 * h - 2)
    )
    low_checks = []
    for q in range(1, m - 1):
        pair = (old["endpoints"][q], new["endpoints"][q])
        wanted = (d, d + 1) if decreasing and q in exposed else (pair[0], pair[0])
        if pair != wanted:
            raise AssertionError(f"inherited endpoint comparison failed at {q}")
        low_checks.append((q, pair))

    return {
        "name": spec["name"],
        "d": d,
        "v": v,
        "tree": tree,
        "path": path,
        "open": decreasing,
        "root_table_old": got_old,
        "root_table_new": got_new,
        "port_checks": port_checks,
        "exposed_labels": sorted(exposed),
        "low_endpoint_pairs": low_checks,
        "old_word_digest": hashlib.sha256(
            json.dumps(old["word"], separators=(",", ":")).encode()
        ).hexdigest(),
        "new_word_digest": hashlib.sha256(
            json.dumps(new["word"], separators=(",", ":")).encode()
        ).hexdigest(),
    }


def main() -> None:
    cases = (
        {
            "name": "direct_root_boundary_v_eq_d_minus_1",
            "d": 7,
            "v": 6,
            "tree": ((1, 7), (1, 6), (1, 2), (1, 3), (1, 4), (1, 5)),
            "open": True,
        },
        {
            "name": "decreasing_lens_persistent_and_crossing_ports",
            "d": 9,
            "v": 5,
            "tree": (
                (1, 9), (1, 2), (2, 4), (4, 5),
                (5, 7), (5, 3), (1, 6), (1, 8),
            ),
            "open": True,
            "ports": (
                {"h": 7, "endpoint": "root"},
                {"h": 3, "endpoint": 2},
            ),
        },
        {
            "name": "above_v_lens_expands_at_root",
            "d": 8,
            "v": 4,
            "tree": ((1, 8), (1, 6), (6, 4), (4, 5), (1, 2), (1, 3), (1, 7)),
            "open": False,
            "ports": ({"h": 5, "endpoint": 1},),
        },
        {
            "name": "canonical_input_sealed_before_root",
            "d": 8,
            "v": 5,
            "tree": ((1, 8), (1, 4), (4, 3), (3, 5), (1, 2), (1, 6), (1, 7)),
            "open": False,
        },
    )
    rows = [audit_case(spec) for spec in cases]
    result = {
        "mission": "M273 decorated root-seam four-schema guard",
        "status": "exact finite calibration only; analytic proof carries all ranks",
        "predeclared_cases": len(cases),
        "rank_census": False,
        "tree_census": False,
        "predecessor_imports": False,
        "rows": rows,
        "failures": [],
        "rows_digest": hashlib.sha256(
            json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
        "environment": {
            "python": platform.python_version(),
            "nonstandard_dependencies": {},
            "seed": None,
        },
        "scope": {
            "proves_all_rank": False,
            "proves_idl": False,
            "proves_route": False,
            "gap_or_mixing": False,
        },
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
