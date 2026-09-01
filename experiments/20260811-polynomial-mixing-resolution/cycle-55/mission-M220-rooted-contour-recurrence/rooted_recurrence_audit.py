#!/usr/bin/env python3
"""Exact compact audit of M220's proposed one-leaf recurrence.

The checker reconstructs the rooted plus-mirror DPS closure, validates that
the closed recurrence specializes to all 112 accepted d=5 rows, and then
tests exactly the 125*9 declared d=6->7 rows.  It imports no predecessor code
or data, performs no route search, and enumerates no Hurwitz quotient graph.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import platform
import sys
from collections import defaultdict
from pathlib import Path


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "rooted_recurrence_results.json"


def edge(a: int, b: int) -> tuple[int, int]:
    assert a != b
    return (a, b) if a < b else (b, a)


def prufer_trees(vertices: tuple[int, ...]):
    n = len(vertices)
    assert n >= 2
    for code in itertools.product(vertices, repeat=n - 2):
        degree = {vertex: 1 for vertex in vertices}
        for vertex in code:
            degree[vertex] += 1
        tree = []
        for vertex in code:
            leaf = min(item for item in vertices if degree[item] == 1)
            tree.append(edge(leaf, vertex))
            degree[leaf] -= 1
            degree[vertex] -= 1
        leaves = [item for item in vertices if degree[item] == 1]
        assert len(leaves) == 2
        tree.append(edge(*leaves))
        yield frozenset(tree)


def rooted_tree_template(d: int):
    """Trees on [d] with root d a leaf adjacent to attachment vertex 1."""
    direct = {
        tree | {(1, d)}
        for tree in prufer_trees(tuple(range(1, d)))
    }
    filtered = [
        tree
        for tree in prufer_trees(tuple(range(1, d + 1)))
        if (1, d) in tree and sum(d in item for item in tree) == 1
    ]
    assert set(filtered) == direct
    assert len(filtered) == (d - 1) ** (d - 3)
    return filtered


def parents(tree: frozenset[tuple[int, int]], root: int):
    adjacency = {vertex: [] for vertex in range(1, root + 1)}
    for a, b in tree:
        adjacency[a].append(b)
        adjacency[b].append(a)
    parent = {root: None}
    stack = [root]
    while stack:
        vertex = stack.pop()
        for neighbor in sorted(adjacency[vertex], reverse=True):
            if neighbor not in parent:
                parent[neighbor] = vertex
                stack.append(neighbor)
    assert len(parent) == root
    return parent


def boundary_trace(tree, order, d: int):
    parent = parents(tree, d)
    incidence = defaultdict(dict)
    first_black = {}
    for child in range(1, d):
        label_a, label_b = order[2 * child - 2 : 2 * child]
        black = ("black", child)
        for label, white_id in ((label_a, child), (label_b, parent[child])):
            white = ("white", white_id)
            incidence[black][label] = white
            incidence[white][label] = black
            first_black[label] = child

    label_count = 2 * d - 2
    start = (("white", 1), 1)
    state = start
    seen = set()
    tokens = []
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        direction = 1 if vertex[0] == "white" else -1
        label = 1 + ((incoming - 1 + direction) % label_count)
        if label in incidence[vertex]:
            tokens.append(("side",))
            state = incidence[vertex][label], label
        else:
            tokens.append(("half", vertex[0], vertex[1], label))
            state = vertex, label
    assert state == start
    assert len(tokens) == (2 * d - 1) * label_count
    return tokens, first_black


def close_boundary(tokens, d: int):
    tokens = list(tokens)
    second_black = {}
    while True:
        half_positions = [
            index for index, token in enumerate(tokens) if token[0] == "half"
        ]
        chosen = None
        for offset, white_position in enumerate(half_positions):
            black_position = half_positions[(offset + 1) % len(half_positions)]
            if (
                tokens[white_position][1] == "white"
                and tokens[black_position][1] == "black"
            ):
                chosen = white_position, black_position
                break
        if chosen is None:
            break
        white_position, black_position = chosen
        tokens = tokens[white_position:] + tokens[:white_position]
        black_position = (black_position - white_position) % len(tokens)
        white, black = tokens[0], tokens[black_position]
        assert white[3] == black[3]
        distance = sum(token[0] == "side" for token in tokens[1:black_position])
        assert distance in (1, 3)
        if distance == 3:
            assert white[3] not in second_black
            second_black[white[3]] = black[2]
        tokens = [("side",)] + tokens[black_position + 1 :]
    residue = [token for token in tokens if token[0] == "half"]
    assert len(residue) == 2 * d - 2
    assert all(token[1] == "white" for token in residue)
    return second_black


def dps_word(tree, order, d: int):
    tokens, first_black = boundary_trace(tree, order, d)
    second_black = close_boundary(tokens, d)
    return tuple(
        edge(first_black[label] - 1, second_black.get(label, d) - 1)
        for label in range(1, 2 * d - 1)
    )


def canonical_order(d: int):
    return (2 * d - 3, 2 * d - 2) + tuple(range(1, 2 * d - 3))


def swap_values(order, edit: int):
    return tuple(
        edit + 1
        if value == edit
        else edit
        if value == edit + 1
        else value
        for value in order
    )


def conjugate(transposition, by):
    x, y = by

    def image(vertex):
        return y if vertex == x else x if vertex == y else vertex

    return edge(image(transposition[0]), image(transposition[1]))


def hurwitz(word, symbol: int):
    assert symbol
    position = abs(symbol) - 1
    a, b = word[position : position + 2]
    result = list(word)
    if symbol > 0:
        result[position : position + 2] = (b, conjugate(a, b))
    else:
        result[position : position + 2] = (conjugate(b, a), a)
    return tuple(result)


def act(word, route):
    for symbol in route:
        word = hurwitz(word, symbol)
    return word


def inverse_route(route):
    return tuple(-symbol for symbol in reversed(route))


def product(word, d: int):
    permutation = tuple(range(d))
    for a, b in word:
        transposition = list(range(d))
        transposition[a], transposition[b] = transposition[b], transposition[a]
        permutation = tuple(transposition[permutation[x]] for x in range(d))
    return permutation


def stopped_path(parent, vertex: int):
    result = [vertex]
    while result[-1] != 1:
        result.append(parent[result[-1]])
        assert result[-1] is not None
    return tuple(result)


def proposed_route_and_key(tree, d: int, edit: int):
    assert 1 <= edit <= 2 * d - 3
    parent = parents(tree, d)

    if edit % 2 == 1 and edit <= 2 * d - 5:
        vertex = (edit + 3) // 2
        path = stopped_path(parent, vertex)
        late = any(item > vertex for item in path[1:-1])
        run = 0
        for child in range(vertex + 1, d):
            if parent[child] != vertex:
                break
            run += 1
        exceptional_path = (vertex,) + tuple(range(2, vertex)) + (1,)
        exceptional = vertex >= 4 and path == exceptional_path
        key = {
            "kind": "ordinary_odd",
            "vertex": vertex,
            "path": list(path),
            "late_ancestor": late,
            "direct_child_run": run,
            "forward_chain_exception": exceptional,
            "proposed_class": [
                "ordinary_odd",
                vertex,
                late,
                run,
                exceptional,
            ],
        }
        if late or exceptional:
            return (), key

        length = d - vertex - 1
        q = []
        for offset in range(length):
            if offset < run:
                sign = -1
            else:
                sign = 1 if (offset - run) % 2 == 0 else -1
            first = 2 * (vertex + offset) - 2
            q.extend((sign * first, sign * (first + 1)))
        p = 2 * d - 4
        carrier = (-p, p + 1, -(p + 2), -(p + 1), -p)
        q = tuple(q)
        return q + carrier + inverse_route(q), key

    if edit % 2 == 0 and edit <= 2 * d - 6:
        return (), {
            "kind": "internal_even",
            "proposed_class": ["internal_even"],
        }

    if edit == 2 * d - 4:
        position = 2 * d - 5
        return (-position, -position), {
            "kind": "cross_boundary_even",
            "proposed_class": ["cross_boundary_even"],
        }

    assert edit == 2 * d - 3
    return (-(2 * d - 2),), {
        "kind": "old_high_pair",
        "proposed_class": ["old_high_pair"],
    }


def json_tree(tree):
    return [list(item) for item in sorted(tree)]


def json_word(word):
    return [list(item) for item in word]


def json_route(route):
    return [[abs(symbol), 1 if symbol > 0 else -1] for symbol in route]


def compact_digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def compact_row(row):
    return {
        "tree_id": row["tree_id"],
        "tree": row["tree"],
        "edit": row["edit"],
        "proposed_class": row["key"]["proposed_class"],
        "descriptor": row["key"],
        "route": row["route"],
        "naive": row["naive"],
        "actual": row["actual"],
        "replay": row["replay"],
        "pass": row["pass"],
        "naive_equals_actual": row["naive_equals_actual"],
        "mismatch_positions": row["mismatch_positions"],
    }


def audit_rank(d: int):
    trees = rooted_tree_template(d)
    order_d = canonical_order(d)
    order_next = canonical_order(d + 1)
    leaf_pair = ((0, d), (0, d))
    identity_d = tuple(range(d))
    identity_next = tuple(range(d + 1))
    rows = []

    for tree_id, tree in enumerate(trees):
        extension = tree | {(1, d + 1)}
        source = dps_word(tree, order_d, d)
        extended_source = dps_word(extension, order_next, d + 1)
        assert source + leaf_pair == extended_source
        assert product(source, d) == identity_d
        assert product(extended_source, d + 1) == identity_next

        for edit in range(1, 2 * d - 2):
            route, key = proposed_route_and_key(tree, d, edit)
            naive = dps_word(tree, swap_values(order_d, edit), d) + leaf_pair
            actual = dps_word(
                extension, swap_values(order_next, edit), d + 1
            )
            replay = act(naive, route)
            assert product(naive, d + 1) == identity_next
            assert product(actual, d + 1) == identity_next
            assert product(replay, d + 1) == identity_next
            mismatch_positions = [
                index + 1
                for index, (left, right) in enumerate(zip(replay, actual))
                if left != right
            ]
            rows.append(
                {
                    "tree_id": tree_id,
                    "tree": json_tree(tree),
                    "edit": edit,
                    "key": key,
                    "route": json_route(route),
                    "route_length": len(route),
                    "naive": json_word(naive),
                    "actual": json_word(actual),
                    "replay": json_word(replay),
                    "pass": replay == actual,
                    "naive_equals_actual": naive == actual,
                    "mismatch_positions": mismatch_positions,
                }
            )

    return trees, rows


def paired_witness(rows, predicate):
    by_key = defaultdict(list)
    for row in rows:
        key = json.dumps(row["key"]["proposed_class"], separators=(",", ":"))
        by_key[key].append(row)
    for key in sorted(by_key):
        group = by_key[key]
        for left_index, left in enumerate(group):
            for right in group[left_index + 1 :]:
                if predicate(left, right):
                    return {
                        "proposed_class": json.loads(key),
                        "left": compact_row(left),
                        "right": compact_row(right),
                    }
    return None


def rank_summary(d: int, trees, rows):
    by_edit = []
    for edit in range(1, 2 * d - 2):
        group = [row for row in rows if row["edit"] == edit]
        by_edit.append(
            {
                "edit": edit,
                "rows": len(group),
                "passes": sum(row["pass"] for row in group),
                "failures": sum(not row["pass"] for row in group),
                "naive_equals_actual": sum(
                    row["naive_equals_actual"] for row in group
                ),
            }
        )

    by_class = []
    groups = defaultdict(list)
    for row in rows:
        key = json.dumps(row["key"]["proposed_class"], separators=(",", ":"))
        groups[key].append(row)
    for key in sorted(groups):
        group = groups[key]
        routes = {json.dumps(row["route"], separators=(",", ":")) for row in group}
        assert len(routes) == 1
        by_class.append(
            {
                "proposed_class": json.loads(key),
                "rows": len(group),
                "passes": sum(row["pass"] for row in group),
                "failures": sum(not row["pass"] for row in group),
                "naive_equals_actual": sum(
                    row["naive_equals_actual"] for row in group
                ),
                "route": json.loads(next(iter(routes))),
                "route_length": group[0]["route_length"],
            }
        )

    normalized = [compact_row(row) for row in rows]
    return {
        "old_rank": d,
        "new_rank": d + 1,
        "tree_count": len(trees),
        "edit_count": 2 * d - 3,
        "row_count": len(rows),
        "passes": sum(row["pass"] for row in rows),
        "failures": sum(not row["pass"] for row in rows),
        "by_edit": by_edit,
        "by_proposed_class": by_class,
        "complete_rows_digest": compact_digest(normalized),
        "first_failure": next(
            (compact_row(row) for row in rows if not row["pass"]), None
        ),
        "same_key_pass_failure_pair": paired_witness(
            rows, lambda left, right: left["pass"] != right["pass"]
        ),
        "same_key_identity_nonidentity_pair": paired_witness(
            rows,
            lambda left, right: left["naive_equals_actual"]
            != right["naive_equals_actual"],
        ),
    }


def verify_formal_identities():
    carrier_input = ((0, 1), (0, 2), (1, 2), (2, 3))
    carrier_route = (-1, 2, -3, -2, -1)
    carrier_expected = ((0, 3), (1, 2), (1, 2), (0, 2))
    assert act(carrier_input, carrier_route) == carrier_expected

    square_input = ((0, 1), (0, 2), (0, 1))
    square_expected = ((0, 2), (1, 2), (0, 1))
    assert act(square_input, (-1, -1)) == square_expected

    inverse_input = ((0, 1), (0, 2))
    inverse_expected = ((1, 2), (0, 1))
    assert act(inverse_input, (-1,)) == inverse_expected
    return {
        "four_factor_carrier": True,
        "double_inverse_boundary": True,
        "single_inverse_boundary": True,
    }


def main():
    formal = verify_formal_identities()
    trees5, rows5 = audit_rank(5)
    summary5 = rank_summary(5, trees5, rows5)
    assert summary5["tree_count"] == 16
    assert summary5["row_count"] == 112
    assert summary5["failures"] == 0

    trees6, rows6 = audit_rank(6)
    summary6 = rank_summary(6, trees6, rows6)
    assert summary6["tree_count"] == 125
    assert summary6["row_count"] == 1125

    result = {
        "experiment": "M220 explicit rooted-contour recurrence audit",
        "target": "deterministic signed-Hurwitz endpoint correction",
        "formal_identities": formal,
        "method": {
            "predecessor_imports": False,
            "predecessor_data_reads": False,
            "route_search": False,
            "q6_enumeration": False,
            "q7_enumeration": False,
            "tree_generation": "two exact Pruefer constructions",
            "action_order": "chronological",
        },
        "d5_to_d6_reproduction": summary5,
        "d6_to_d7_test": summary6,
        "environment": {
            "python": platform.python_version(),
            "nonstandard_dependencies": {},
            "seed": None,
        },
        "scope": (
            "Tests only the explicit recurrence in symbolic_transport.md; "
            "no negative claim about richer descriptors or alternative routes."
        ),
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "d5_rows": summary5["row_count"],
        "d5_failures": summary5["failures"],
        "d6_trees": summary6["tree_count"],
        "d6_rows": summary6["row_count"],
        "d6_passes": summary6["passes"],
        "d6_failures": summary6["failures"],
        "first_failure": summary6["first_failure"],
        "has_same_key_pass_failure_pair": (
            summary6["same_key_pass_failure_pair"] is not None
        ),
        "has_same_key_identity_nonidentity_pair": (
            summary6["same_key_identity_nonidentity_pair"] is not None
        ),
        "output": str(OUTPUT),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
