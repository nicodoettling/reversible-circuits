#!/usr/bin/env python3
"""One-row clean-room check of the literal M244 RSMI formulation.

This script imports no mission code or data.  It reconstructs the accepted
plus-mirror DPS contour and LIFO closure directly from DPS Proposition 3,
Lemma 2, and RandomQuad.  It checks one predeclared boundary configuration:
a nondecreasing stopped path which nevertheless has a larger direct child.
It is not a census and cannot prove an all-rank statement.
"""

from __future__ import annotations

import hashlib
import json
import platform
from collections import defaultdict, deque
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "cleanroom_token_results.json"


def canonical_order(rank: int) -> tuple[int, ...]:
    return (2 * rank - 3, 2 * rank - 2, *range(1, 2 * rank - 3))


def swap_values(order: tuple[int, ...], left: int) -> tuple[int, ...]:
    return tuple(left + 1 if x == left else left if x == left + 1 else x for x in order)


def parent_map(tree: tuple[tuple[int, int], ...], root: int) -> dict[int, int | None]:
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


def dps_word(
    tree: tuple[tuple[int, int], ...], order: tuple[int, ...], rank: int
) -> tuple[tuple[int, int], ...]:
    """Return zero-based physical factors under the accepted plus mirror."""
    parent = parent_map(tree, rank)
    incidence: dict[tuple[str, int], dict[int, tuple[str, int]]] = defaultdict(dict)
    first_black: dict[int, int] = {}

    for a in range(1, rank):
        left, right = order[2 * a - 2 : 2 * a]
        modulus = 2 * rank - 2
        assert (right - left) % modulus in (1, modulus - 1)
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
    assert len(contour) == (2 * rank - 1) * modulus

    tokens = contour
    second_black: dict[int, int] = {}
    while True:
        half_positions = [i for i, token in enumerate(tokens) if token[0] == "H"]
        chosen = None
        for k, white_pos in enumerate(half_positions):
            black_pos = half_positions[(k + 1) % len(half_positions)]
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
        tuple(sorted((first_black[label] - 1, second_black.get(label, rank) - 1)))
        for label in range(1, modulus + 1)
    )


def main() -> None:
    # Root 7.  For v=4, P(v)=(4,2,3,1) has the internal ascent 2<3.
    # Vertex 5 is simultaneously a larger direct child of v.
    rank = 7
    v = 4
    larger_child = 5
    tree = tuple(sorted(((1, 7), (1, 3), (1, 6), (2, 3), (2, 4), (4, 5))))
    parent = parent_map(tree, rank)
    path = [v]
    while path[-1] != 1:
        next_vertex = parent[path[-1]]
        assert next_vertex is not None
        path.append(next_vertex)
    decreasing = all(a > b for a, b in zip(path, path[1:]))
    assert path == [4, 2, 3, 1]
    assert not decreasing
    assert larger_child > v and parent[larger_child] == v

    edit = 2 * v - 3
    old = dps_word(tree, swap_values(canonical_order(rank), edit), rank)
    naive = old + ((0, rank), (0, rank))
    extended_tree = tuple(sorted((*tree, (1, rank + 1))))
    actual = dps_word(
        extended_tree,
        swap_values(canonical_order(rank + 1), edit),
        rank + 1,
    )

    slot_positions = (2 * larger_child - 3, 2 * larger_child - 2)
    old_slot = tuple(naive[position - 1] for position in slot_positions)
    actual_slot = tuple(actual[position - 1] for position in slot_positions)
    item2_old_prediction = ((larger_child - 1, rank - 1),) * 2
    item2_new_prediction = ((larger_child - 1, rank),) * 2

    result = {
        "mission": "M247 one-row clean-room token/rewrite check",
        "status": "exact finite falsification of literal unqualified RSMI(2) only",
        "rank": rank,
        "tree": tree,
        "edited_vertex": v,
        "edit": edit,
        "path": path,
        "path_strictly_decreasing": decreasing,
        "larger_direct_child": larger_child,
        "slot_positions_one_based": slot_positions,
        "naive_equals_actual": naive == actual,
        "actual_old_slot": old_slot,
        "actual_new_slot": actual_slot,
        "literal_rsmi_item2_old_prediction": item2_old_prediction,
        "literal_rsmi_item2_new_prediction": item2_new_prediction,
        "literal_rsmi_item2_holds": (
            old_slot == item2_old_prediction and actual_slot == item2_new_prediction
        ),
        "word_pair_digest": hashlib.sha256(
            json.dumps([naive, actual], separators=(",", ":")).encode()
        ).hexdigest(),
        "environment": {
            "python": platform.python_version(),
            "nonstandard_dependencies": {},
            "seed": None,
        },
        "scope": {
            "rows": 1,
            "proves_pruning": False,
            "proves_or_refutes_repaired_rsmi": False,
            "proves_idl": False,
            "gap_or_mixing": False,
        },
    }
    assert result["naive_equals_actual"]
    assert not result["literal_rsmi_item2_holds"]
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
