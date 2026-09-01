#!/usr/bin/env python3
"""No-import fresh replay of the four M250 rows and token schemas.

This reconstructs the plus-mirror DPS hairy-tree contour from Proposition 3
and closes it with a cycle-lemma rotation followed by the RandomQuad LIFO
stack.  It neither imports nor reads any predecessor code or data.  The four
rank-seven rows are exactly the predeclared M250 rows; there is no census.
"""

from __future__ import annotations

import hashlib
import json
import platform
from collections import defaultdict, deque
from pathlib import Path
from typing import Iterable


HERE = Path(__file__).resolve().parent
OUT = HERE / "cleanroom_results.json"
EXPECTED_M250_ROWS_DIGEST = (
    "d285b53ae1646d9ab241c17f51c92a55d563ad5de2095d9f77dfdfc133e59c59"
)


def edge(a: int, b: int) -> tuple[int, int]:
    if a == b:
        raise AssertionError("a transposition needs two distinct endpoints")
    return (a, b) if a < b else (b, a)


def root_parent(
    tree: tuple[tuple[int, int], ...], root: int
) -> dict[int, int | None]:
    neighbors: dict[int, list[int]] = defaultdict(list)
    for u, w in tree:
        neighbors[u].append(w)
        neighbors[w].append(u)
    parent: dict[int, int | None] = {root: None}
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for w in neighbors[u]:
            if w not in parent:
                parent[w] = u
                queue.append(w)
    if set(parent) != set(range(1, root + 1)):
        raise AssertionError("the declared edge set is not a tree on [rank]")
    return parent


def pi(rank: int) -> tuple[int, ...]:
    return (2 * rank - 3, 2 * rank - 2, *range(1, 2 * rank - 3))


def adjacent_value_edit(order: tuple[int, ...], left: int) -> tuple[int, ...]:
    replacement = {left: left + 1, left + 1: left}
    return tuple(replacement.get(q, q) for q in order)


def hairy_contour(
    tree: tuple[tuple[int, int], ...], order: tuple[int, ...], rank: int
) -> tuple[list[tuple], dict[int, int]]:
    """Build the literal outer contour using opposite cyclic rotations."""

    parent = root_parent(tree, rank)
    incidence: dict[tuple[str, int], dict[int, tuple[str, int]]] = defaultdict(dict)
    first_black: dict[int, int] = {}

    for a in range(1, rank):
        left, right = order[2 * a - 2 : 2 * a]
        black = ("B", a)
        assignments = ((left, a), (right, parent[a]))
        for label, white_index in assignments:
            if white_index is None:
                raise AssertionError("only the white root has no parent")
            white = ("W", white_index)
            incidence[black][label] = white
            incidence[white][label] = black
            first_black[label] = a

    modulus = 2 * rank - 2
    # The canonical root edge x_1--y_rank has label `modulus`; starting here
    # differs from M250's chosen contour corner but describes the same cycle.
    start = (("W", rank), modulus)
    if modulus not in incidence[start[0]]:
        raise AssertionError("root-edge start is not an actual incidence")

    contour: list[tuple] = []
    state = start
    seen: set[tuple[tuple[str, int], int]] = set()
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        direction = 1 if vertex[0] == "W" else -1
        nxt_label = 1 + ((incoming - 1 + direction) % modulus)
        neighbor = incidence[vertex].get(nxt_label)
        if neighbor is None:
            contour.append(("H", vertex[0], vertex[1], nxt_label))
            state = (vertex, nxt_label)
        else:
            contour.append(("S", vertex, neighbor, nxt_label))
            state = (neighbor, nxt_label)
    if state != start:
        raise AssertionError("contour did not return to the chosen corner")
    return contour, first_black


def cycle_lemma_rotation(tokens: list[tuple]) -> list[tuple]:
    """Rotate so every black half-edge has an earlier unmatched white one."""

    balance = 0
    minimum = 0
    last_minimum_index = -1
    for i, token in enumerate(tokens):
        if token[0] == "H":
            balance += 1 if token[1] == "W" else -1
        if balance <= minimum:
            minimum = balance
            last_minimum_index = i
    cut = (last_minimum_index + 1) % len(tokens)
    return tokens[cut:] + tokens[:cut]


def lifo_close(
    contour: list[tuple], first_black: dict[int, int], rank: int
) -> tuple[tuple[int, int], ...]:
    """Run RandomQuad's LIFO stack after a cycle-lemma contour rotation."""

    stream = cycle_lemma_rotation(contour)
    reduced: list[tuple] = []
    second_black: dict[int, int] = {}

    for token in stream:
        if token[0] != "H" or token[1] == "W":
            reduced.append(token)
            continue

        white_pos = next(
            (i for i in range(len(reduced) - 1, -1, -1) if reduced[i][0] == "H"),
            None,
        )
        if white_pos is None:
            raise AssertionError("cycle-lemma rotation left an unmatched black")
        white = reduced[white_pos]
        if white[1] != "W" or white[3] != token[3]:
            raise AssertionError("LIFO pair violates the same-label rule")
        interior = reduced[white_pos + 1 :]
        if any(item[0] != "S" for item in interior):
            raise AssertionError("a nested half-edge survived inside a LIFO pair")
        distance = len(interior)
        if distance not in (1, 3):
            raise AssertionError(f"DPS side distance {distance} is not 1 or 3")
        if distance == 3:
            if white[3] in second_black:
                raise AssertionError("a label acquired two distance-three closures")
            second_black[white[3]] = token[2]
        # The whole complete nested interval is replaced by its closure side.
        reduced[white_pos:] = [("S", "closure", white[3])]

    remaining = [t for t in reduced if t[0] == "H"]
    modulus = 2 * rank - 2
    if len(remaining) != modulus or any(t[1] != "W" for t in remaining):
        raise AssertionError("RandomQuad did not leave exactly the root whites")
    if sorted(t[3] for t in remaining) != list(range(1, modulus + 1)):
        raise AssertionError("the remaining root labels are not a permutation")

    return tuple(
        edge(first_black[q] - 1, second_black.get(q, rank) - 1)
        for q in range(1, modulus + 1)
    )


def dps_word(
    tree: tuple[tuple[int, int], ...], order: tuple[int, ...], rank: int
) -> tuple[tuple[int, int], ...]:
    contour, first_black = hairy_contour(tree, order, rank)
    return lifo_close(contour, first_black, rank)


def close_schema(tokens: Iterable[tuple], label: str) -> tuple[list[tuple], int]:
    """Close one explicitly named consecutive symbolic W/B pair."""

    word = list(tokens)
    wi = next(i for i, t in enumerate(word) if t == ("W", label))
    bi = next(i for i, t in enumerate(word) if i > wi and t == ("B", label))
    if any(t[0] in {"W", "B"} for t in word[wi + 1 : bi]):
        raise AssertionError("symbolic closure interval is not complete")
    distance = sum(t[0] == "S" for t in word[wi + 1 :bi])
    if distance not in (1, 3):
        raise AssertionError("symbolic row has an illegal DPS distance")
    word[wi : bi + 1] = [("S", f"closed-{label}")]
    return word, distance


def symbolic_token_checks() -> dict:
    # Generic leaf suffix: close from right to left.  The number of ordinary
    # labels is immaterial to the induction; three names make nesting visible.
    leaf = [
        ("S", "left"),
        ("W", "R"),
        ("W", "a"),
        ("W", "b"),
        ("W", "c"),
        ("S", "middle"),
        ("B", "c"),
        ("B", "b"),
        ("B", "a"),
        ("S", "right"),
    ]
    leaf_distances = []
    for name in ("c", "b", "a"):
        leaf, distance = close_schema(leaf, name)
        leaf_distances.append(distance)
    leaf_shape = [token[0] for token in leaf]

    # A canonical child after its right suffix is one side.  The q row closes
    # first; its new side is the third side in the q-1 row.
    child = [
        ("W", "q-1"),
        ("S", "cross-parent-child"),
        ("S", "child-leading"),
        ("W", "q"),
        ("S", "child-suffix"),
        ("S", "child-return"),
        ("S", "processed-right-suffix"),
        ("B", "q"),
        ("B", "q-1"),
    ]
    child, q_distance = close_schema(child, "q")
    child, qm_distance = close_schema(child, "q-1")

    ordinary, ordinary_distance = close_schema(
        [("W", "t"), ("S", "suffix"), ("B", "t")], "t"
    )

    checks = {
        "leaf_residual_types": leaf_shape,
        "leaf_expected_types": ["S", "W", "S", "S"],
        "leaf_row_distances": leaf_distances,
        "child_final_types": [token[0] for token in child],
        "child_row_distances": [q_distance, qm_distance],
        "ordinary_final_types": [token[0] for token in ordinary],
        "ordinary_distance": ordinary_distance,
        "complete_intervals_only": True,
    }
    checks["holds"] = (
        checks["leaf_residual_types"] == checks["leaf_expected_types"]
        and leaf_distances == [1, 1, 1]
        and checks["child_final_types"] == ["S"]
        and checks["child_row_distances"] == [3, 3]
        and checks["ordinary_final_types"] == ["S"]
        and ordinary_distance == 1
    )
    return checks


def audit_row(name: str, raw_tree: tuple[tuple[int, int], ...], v: int) -> dict:
    rank = 7
    tree = tuple(sorted(tuple(sorted(pair)) for pair in raw_tree))
    parent = root_parent(tree, rank)
    path = [v]
    while path[-1] != 1:
        nxt = parent[path[-1]]
        if nxt is None:
            raise AssertionError("the stopped path missed white 1")
        path.append(nxt)
    is_open = all(a > b for a, b in zip(path, path[1:]))

    edit = 2 * v - 3
    old = dps_word(tree, adjacent_value_edit(pi(rank), edit), rank)
    naive = old + ((0, rank), (0, rank))
    extended = tuple(sorted((*tree, (1, rank + 1))))
    actual = dps_word(
        extended, adjacent_value_edit(pi(rank + 1), edit), rank + 1
    )

    clauses: dict[str, dict] = {}
    failures: list[dict] = []

    def check(clause: str, position: int, expected: tuple, got: tuple) -> None:
        item = {"position": position, "expected": expected, "got": got}
        clauses.setdefault(clause, {"checks": [], "holds": True})["checks"].append(item)
        if got != expected:
            clauses[clause]["holds"] = False
            failures.append({"clause": clause, **item})

    if not is_open:
        clauses["sealed_closed_equality"] = {
            "checks": [{"expected": True, "got": naive == actual}],
            "holds": naive == actual,
        }
        if naive != actual:
            failures.append(
                {
                    "clause": "sealed_closed_equality",
                    "first_differing_position": next(
                        j
                        for j, pair in enumerate(zip(naive, actual), start=1)
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
                if set(h) & {x, y, n}:
                    raise AssertionError("declared nonchild edge is not disjoint")
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
        "open": is_open,
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
    rows_digest = hashlib.sha256(
        json.dumps(audited, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    symbolic = symbolic_token_checks()
    result = {
        "mission": "M254 fresh no-import referee of M250",
        "status": "exact four-row calibration and symbolic token checks only",
        "predeclared_rows": 4,
        "rank_census": False,
        "rows": audited,
        "failures": failures,
        "rows_digest": rows_digest,
        "expected_m250_rows_digest": EXPECTED_M250_ROWS_DIGEST,
        "m250_rows_digest_matches": rows_digest == EXPECTED_M250_ROWS_DIGEST,
        "symbolic_token_checks": symbolic,
        "environment": {
            "python": platform.python_version(),
            "nonstandard_dependencies": {},
            "seed": None,
        },
        "scope": {
            "proves_rspt": False,
            "proves_rsmi_plus": False,
            "proves_idl": False,
            "downstream": False,
        },
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))
    if failures or not symbolic["holds"] or rows_digest != EXPECTED_M250_ROWS_DIGEST:
        raise AssertionError("fresh audit check failed")


if __name__ == "__main__":
    main()

