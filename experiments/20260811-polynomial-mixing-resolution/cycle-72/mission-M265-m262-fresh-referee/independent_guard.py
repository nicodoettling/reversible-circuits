#!/usr/bin/env python3
"""Independent two-rank guard for the M262 CPR counterfamily.

This checks only rho=8,9.  The universal statement is audited symbolically in
the referee report; these computations are not finite interpolation.
"""

from __future__ import annotations

import json
import platform
from collections import deque
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "independent_guard_results.json"


def cyclic_open(start: int, stop: int, step: int, modulus: int) -> list[int]:
    """Labels strictly after start and strictly before stop in cyclic order."""
    out: list[int] = []
    value = (start - 1 + step) % modulus + 1
    while value != stop:
        out.append(value)
        value = (value - 1 + step) % modulus + 1
    return out


def s(name: str) -> tuple[str, str]:
    return ("S", name)


def h(kind: str, vertex: int, label: int) -> tuple[str, int, int]:
    return (kind, vertex, label)


def rooted_family(rank: int) -> tuple[set[tuple[int, int]], dict[int, int]]:
    edges = {(1, rank), (1, 6), (4, 6)}
    edges |= {(1, r) for r in range(2, rank) if r not in {4, 6}}
    edges = {tuple(sorted(edge)) for edge in edges}

    adjacency = {v: set() for v in range(1, rank + 1)}
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    assert len(edges) == rank - 1

    parent: dict[int, int] = {}
    seen = {rank}
    queue = deque([rank])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if v in seen:
                continue
            seen.add(v)
            parent[v] = u
            queue.append(v)
    assert seen == set(range(1, rank + 1))
    return edges, parent


def cp5_base(modulus: int) -> list[tuple]:
    # v=4, L_4=5, R_4=6, with no rooted child.
    return [
        *(h("B", 4, q) for q in cyclic_open(5, 6, -1, modulus)),
        s("base-R-enter"),
        *(h("W", 4, q) for q in cyclic_open(6, 6, +1, modulus)),
        s("base-R-return"),
        s("base-L-return"),
    ]


def cp2_at_six(modulus: int) -> list[tuple]:
    # L_6=9, R_6=10, and the edited child incidence is kappa(4)=L_4=5.
    return [
        s("six-L-enter"),
        *(h("W", 6, q) for q in cyclic_open(9, 5, +1, modulus)),
        s("child-enter"),
        *cp5_base(modulus),
        *(h("W", 6, q) for q in cyclic_open(5, 9, +1, modulus)),
        s("six-L-return"),
        *(h("B", 6, q) for q in cyclic_open(9, 10, -1, modulus)),
        s("six-R-return"),
    ]


def delete_prescribed(
    word: list[tuple],
    kind_vertices: tuple[int, int],
    label: int,
    expected_distance: int,
    row_log: list[dict],
) -> None:
    white_vertex, black_vertex = kind_vertices
    white = h("W", white_vertex, label)
    black = h("B", black_vertex, label)
    left = word.index(white)
    right = word.index(black)
    assert left < right
    between = word[left + 1 : right]
    assert all(token[0] == "S" for token in between)
    assert len(between) == expected_distance
    row_log.append(
        {
            "label": label,
            "white": white_vertex,
            "black": black_vertex,
            "distance": len(between),
        }
    )
    word[left : right + 1] = [s(f"closed-{white_vertex}-{black_vertex}-{label}")]


def normalized(word: list[tuple]) -> list[str | list[int | str]]:
    return ["S" if token[0] == "S" else list(token) for token in word]


def guard_rank(rank: int) -> dict:
    modulus = 2 * rank - 2
    edges, parent = rooted_family(rank)
    assert [4, parent[4], parent[parent[4]]] == [4, 6, 1]
    assert parent[1] == rank
    assert rank >= 8 and 6 not in {1, rank}
    assert all(parent.get(r) != 4 for r in range(5, rank))
    exposed = {6} | {
        2 * r - 3
        for r in range(5, rank)
        if parent.get(r) == 4
    } | {
        2 * r - 2
        for r in range(5, rank)
        if parent.get(r) == 4
    }
    assert exposed == {6}

    word = cp2_at_six(modulus)
    rows: list[dict] = []
    left_labels = [4, 3, 2, 1] + list(range(modulus, 9, -1))
    for label in left_labels:
        delete_prescribed(word, (6, 4), label, 1, rows)
    for label in [8, 7, 6]:
        delete_prescribed(word, (6, 6), label, 1, rows)
    delete_prescribed(word, (4, 6), 5, 3, rows)
    tail_labels = [4, 3, 2, 1] + list(range(modulus, 10, -1))
    for label in tail_labels:
        delete_prescribed(word, (4, 6), label, 1, rows)

    expected = [
        "S",
        "S",
        ["B", 4, 9],
        ["B", 4, 8],
        ["B", 4, 7],
        "S",
        ["W", 4, 7],
        ["W", 4, 8],
        ["W", 4, 9],
        ["W", 4, 10],
        "S",
        "S",
    ]
    assert normalized(word) == expected
    label_six = [row for row in rows if row["label"] == 6]
    assert label_six == [
        {"label": 6, "white": 6, "black": 6, "distance": 1}
    ]
    return {
        "rank": rank,
        "modulus": modulus,
        "edge_count": len(edges),
        "stopped_path_prefix": [4, 6, 1],
        "root": rank,
        "exposed": sorted(exposed),
        "left_distance_one_labels": left_labels,
        "right_distance_one_prefix": [8, 7, 6],
        "distance_three_label": 5,
        "right_distance_one_tail": tail_labels,
        "label_six_rows": label_six,
        "residual": normalized(word),
    }


def main() -> None:
    checks = [guard_rank(8), guard_rank(9)]
    added = sorted(
        set(checks[1]["left_distance_one_labels"])
        - set(checks[0]["left_distance_one_labels"])
    )
    assert added == [15, 16]
    assert checks[0]["residual"] == checks[1]["residual"]
    result = {
        "mission": "M265 independent rho=8,9 guard",
        "scope": "finite guard only; universal claim audited analytically",
        "checks": checks,
        "rank_extension_added_labels": added,
        "rank_extension_residual_unchanged": True,
        "holds": True,
        "environment": {
            "python": platform.python_version(),
            "nonstandard_dependencies": {},
            "seed": None,
        },
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

