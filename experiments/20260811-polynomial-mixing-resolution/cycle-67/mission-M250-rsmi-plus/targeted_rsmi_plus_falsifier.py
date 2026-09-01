#!/usr/bin/env python3
"""Four predeclared adversarial rows for the repaired RSMI+ package.

This is not a rank census.  The four rank-seven rows were fixed in
checkpoint.md before this script was written or run.  The implementation is a
clean direct replay of DPS Proposition 3 plus Lemma 2/RandomQuad under the
accepted plus-mirror convention.  Finite success is calibration only.
"""

from __future__ import annotations

import hashlib
import json
import platform
from collections import defaultdict, deque
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "targeted_rsmi_plus_results.json"


def edge(a: int, b: int) -> tuple[int, int]:
    assert a != b
    return (a, b) if a < b else (b, a)


def parent_map(
    tree: tuple[tuple[int, int], ...], root: int
) -> dict[int, int | None]:
    adjacency: dict[int, list[int]] = defaultdict(list)
    for a, b in tree:
        adjacency[a].append(b)
        adjacency[b].append(a)
    parent: dict[int, int | None] = {root: None}
    todo = deque([root])
    while todo:
        a = todo.popleft()
        for b in adjacency[a]:
            if b not in parent:
                parent[b] = a
                todo.append(b)
    assert len(parent) == root
    return parent


def canonical_order(rank: int) -> tuple[int, ...]:
    return (2 * rank - 3, 2 * rank - 2, *range(1, 2 * rank - 3))


def swap_values(order: tuple[int, ...], left: int) -> tuple[int, ...]:
    return tuple(
        left + 1 if value == left else left if value == left + 1 else value
        for value in order
    )


def dps_word(
    tree: tuple[tuple[int, int], ...], order: tuple[int, ...], rank: int
) -> tuple[tuple[int, int], ...]:
    parent = parent_map(tree, rank)
    incidence: dict[tuple[str, int], dict[int, tuple[str, int]]] = defaultdict(dict)
    first_black: dict[int, int] = {}
    for a in range(1, rank):
        left, right = order[2 * a - 2 : 2 * a]
        black = ("B", a)
        for label, white_index in ((left, a), (right, parent[a])):
            assert white_index is not None
            white = ("W", white_index)
            incidence[black][label] = white
            incidence[white][label] = black
            first_black[label] = a

    modulus = 2 * rank - 2
    start = (("W", 1), 1)
    state = start
    visited: set[tuple[tuple[str, int], int]] = set()
    contour: list[tuple] = []
    while state not in visited:
        visited.add(state)
        vertex, incoming = state
        step = 1 if vertex[0] == "W" else -1
        label = 1 + ((incoming - 1 + step) % modulus)
        neighbor = incidence[vertex].get(label)
        if neighbor is None:
            contour.append(("H", vertex[0], vertex[1], label))
            state = (vertex, label)
        else:
            contour.append(("S",))
            state = (neighbor, label)
    assert state == start

    tokens = contour
    second_black: dict[int, int] = {}
    while True:
        halves = [i for i, token in enumerate(tokens) if token[0] == "H"]
        chosen = None
        for j, white_pos in enumerate(halves):
            black_pos = halves[(j + 1) % len(halves)]
            if tokens[white_pos][1] == "W" and tokens[black_pos][1] == "B":
                chosen = white_pos, black_pos
                break
        if chosen is None:
            break
        white_pos, black_pos = chosen
        tokens = tokens[white_pos:] + tokens[:white_pos]
        black_pos = (black_pos - white_pos) % len(tokens)
        white, black = tokens[0], tokens[black_pos]
        assert white[3] == black[3]
        distance = sum(token[0] == "S" for token in tokens[1:black_pos])
        assert distance in (1, 3)
        if distance == 3:
            assert white[3] not in second_black
            second_black[white[3]] = black[2]
        tokens = [("S",), *tokens[black_pos + 1 :]]

    remaining = [token for token in tokens if token[0] == "H"]
    assert len(remaining) == modulus
    assert all(token[1] == "W" for token in remaining)
    assert sorted(token[3] for token in remaining) == list(range(1, modulus + 1))
    return tuple(
        edge(first_black[label] - 1, second_black.get(label, rank) - 1)
        for label in range(1, modulus + 1)
    )


def audit_row(name: str, tree: tuple[tuple[int, int], ...], v: int) -> dict:
    rank = 7
    tree = tuple(sorted(tuple(sorted(e)) for e in tree))
    parent = parent_map(tree, rank)
    path = [v]
    while path[-1] != 1:
        nxt = parent[path[-1]]
        assert nxt is not None
        path.append(nxt)
    open_state = all(a > b for a, b in zip(path, path[1:]))

    edit = 2 * v - 3
    old = dps_word(tree, swap_values(canonical_order(rank), edit), rank)
    naive = old + ((0, rank), (0, rank))
    extended_tree = tuple(sorted((*tree, (1, rank + 1))))
    actual = dps_word(
        extended_tree,
        swap_values(canonical_order(rank + 1), edit),
        rank + 1,
    )

    clauses: dict[str, dict] = {}
    failures: list[dict] = []

    def check(clause: str, position: int, expected: tuple, got: tuple) -> None:
        item = {"position": position, "expected": expected, "got": got}
        clauses.setdefault(clause, {"checks": [], "holds": True})["checks"].append(item)
        if got != expected:
            clauses[clause]["holds"] = False
            failures.append({"clause": clause, **item})

    if not open_state:
        clauses["sealed_closed_equality"] = {
            "checks": [{"expected": True, "got": naive == actual}],
            "holds": naive == actual,
        }
        if naive != actual:
            failures.append(
                {
                    "clause": "sealed_closed_equality",
                    "first_differing_position": next(
                        i
                        for i, pair in enumerate(zip(naive, actual), start=1)
                        if pair[0] != pair[1]
                    ),
                }
            )
    else:
        x, y, z, n = v - 1, rank - 1, 0, rank
        named: dict[int, tuple[tuple[int, int], tuple[int, int], str]] = {
            2 * v - 2: (edge(x, y), edge(x, n), "initial_edited_endpoint"),
            2 * rank - 3: (edge(z, x), edge(z, y), "open_root_four_block"),
            2 * rank - 2: (edge(z, y), edge(z, y), "open_root_four_block"),
            2 * rank - 1: (edge(z, n), edge(z, x), "open_root_four_block"),
            2 * rank: (edge(z, n), edge(z, n), "open_root_four_block"),
        }
        for r in range(v + 1, rank):
            if parent[r] == v:
                expected = (
                    edge(r - 1, y),
                    edge(r - 1, n),
                    "open_only_larger_child",
                )
            else:
                h = edge(r - 1, int(parent[r]) - 1)
                assert not set(h) & {x, y, n}
                expected = (h, h, "common_nonchild_endpoint")
            named[2 * r - 3] = expected
            named[2 * r - 2] = expected

        for position, (expected_old, expected_new, clause) in named.items():
            check(
                clause,
                position,
                (expected_old, expected_new),
                (naive[position - 1], actual[position - 1]),
            )
        for position in range(1, 2 * rank + 1):
            if position not in named:
                check(
                    "unnamed_coordinate_equality",
                    position,
                    (naive[position - 1], naive[position - 1]),
                    (naive[position - 1], actual[position - 1]),
                )

    return {
        "name": name,
        "rank": rank,
        "tree": tree,
        "v": v,
        "path": path,
        "open": open_state,
        "clauses": clauses,
        "failures": failures,
        "word_pair_digest": hashlib.sha256(
            json.dumps([naive, actual], separators=(",", ":")).encode()
        ).hexdigest(),
    }


def main() -> None:
    rows = (
        (
            "open_multilevel_direct_and_nonchild",
            ((1, 7), (1, 2), (2, 3), (3, 4), (4, 5), (3, 6)),
            4,
        ),
        (
            "open_empty_scan",
            ((1, 7), (1, 6), (1, 2), (2, 3), (3, 4), (4, 5)),
            6,
        ),
        (
            "closed_late_with_direct_child",
            ((1, 7), (1, 6), (6, 4), (4, 5), (1, 2), (2, 3)),
            4,
        ),
        (
            "closed_ascent_with_direct_child",
            ((1, 7), (1, 2), (2, 4), (4, 3), (3, 5), (5, 6)),
            5,
        ),
    )
    audited = [audit_row(*row) for row in rows]
    failures = [
        {"name": row["name"], "failures": row["failures"]}
        for row in audited
        if row["failures"]
    ]
    result = {
        "mission": "M250 four-row targeted RSMI+ falsifier",
        "status": "exact finite calibration only",
        "predeclared_rows": 4,
        "rows": audited,
        "failures": failures,
        "rows_digest": hashlib.sha256(
            json.dumps(audited, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
        "environment": {
            "python": platform.python_version(),
            "nonstandard_dependencies": {},
            "seed": None,
        },
        "scope": {
            "rank_census": False,
            "proves_rsmi_plus": False,
            "proves_idl": False,
            "downstream": False,
        },
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))
    assert not failures


if __name__ == "__main__":
    main()
