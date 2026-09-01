#!/usr/bin/env python3
"""Deterministic exact checker for M214's 16-tree contour classification.

No route search, no Q6 enumeration, and no predecessor imports.  The script
generates the complete declared tree template by Prüfer codes, derives each
intrinsic contour key from its rooted tree, and replays the archived signed
Hurwitz word on all 112 endpoints.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import platform
import sys
from collections import Counter, defaultdict
from pathlib import Path


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent


def edge(a, b):
    assert a != b
    return (a, b) if a < b else (b, a)


def prufer_trees(d):
    for code in itertools.product(range(1, d + 1), repeat=d - 2):
        degree = [0] + [1] * d
        for vertex in code:
            degree[vertex] += 1
        tree = []
        for vertex in code:
            leaf = next(x for x in range(1, d + 1) if degree[x] == 1)
            tree.append(edge(leaf, vertex))
            degree[leaf] -= 1
            degree[vertex] -= 1
        last = [x for x in range(1, d + 1) if degree[x] == 1]
        tree.append(edge(last[0], last[1]))
        yield frozenset(tree)


def rooted_structure(tree, root):
    adjacency = {vertex: [] for vertex in range(1, root + 1)}
    for a, b in tree:
        adjacency[a].append(b)
        adjacency[b].append(a)
    parent = {root: None}
    stack = [root]
    while stack:
        vertex = stack.pop()
        for neighbor in adjacency[vertex]:
            if neighbor not in parent:
                parent[neighbor] = vertex
                stack.append(neighbor)
    children = {vertex: [] for vertex in adjacency}
    for vertex, ancestor in parent.items():
        if ancestor is not None:
            children[ancestor].append(vertex)
    for values in children.values():
        values.sort()
    return parent, children


def boundary_trace(tree, order, d):
    parent, _ = rooted_structure(tree, d)
    incidence = defaultdict(dict)
    first_black = {}
    for child in range(1, d):
        labels = order[2 * child - 2 : 2 * child]
        black = ("b", child)
        for label, white_id in ((labels[0], child), (labels[1], parent[child])):
            white = ("w", white_id)
            incidence[black][label] = white
            incidence[white][label] = black
            first_black[label] = child
    m = 2 * d - 2
    start = (("w", 1), 1)
    state = start
    seen = set()
    tokens = []
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        direction = 1 if vertex[0] == "w" else -1
        label = 1 + ((incoming - 1 + direction) % m)
        if label in incidence[vertex]:
            tokens.append(("side",))
            state = incidence[vertex][label], label
        else:
            tokens.append(("half", vertex[0], vertex[1], label))
            state = vertex, label
    assert state == start and len(tokens) == (2 * d - 1) * m
    return tokens, first_black


def close_boundary(tokens, d):
    tokens = list(tokens)
    second_black = {}
    while True:
        half = [i for i, token in enumerate(tokens) if token[0] == "half"]
        selected = None
        for offset, white_position in enumerate(half):
            black_position = half[(offset + 1) % len(half)]
            if tokens[white_position][1] == "w" and tokens[black_position][1] == "b":
                selected = white_position, black_position
                break
        if selected is None:
            break
        white_position, black_position = selected
        tokens = tokens[white_position:] + tokens[:white_position]
        black_position = (black_position - white_position) % len(tokens)
        white, black = tokens[0], tokens[black_position]
        assert white[3] == black[3]
        distance = sum(token[0] == "side" for token in tokens[1:black_position])
        assert distance in (1, 3)
        if distance == 3:
            second_black[white[3]] = black[2]
        tokens = [("side",)] + tokens[black_position + 1 :]
    residue = [token for token in tokens if token[0] == "half"]
    assert len(residue) == 2 * d - 2 and all(token[1] == "w" for token in residue)
    return second_black


def dps_word(tree, order, d):
    tokens, first = boundary_trace(tree, order, d)
    second = close_boundary(tokens, d)
    return tuple(
        edge(first[label] - 1, second.get(label, d) - 1)
        for label in range(1, 2 * d - 1)
    )


def swap_values(order, edit):
    return tuple(
        edit + 1 if value == edit
        else edit if value == edit + 1
        else value
        for value in order
    )


def conjugate(transposition, by):
    x, y = by
    image = lambda z: y if z == x else x if z == y else z
    return edge(image(transposition[0]), image(transposition[1]))


def hurwitz(word, position, sign):
    a, b = word[position], word[position + 1]
    result = list(word)
    if sign == 1:
        result[position : position + 2] = (b, conjugate(a, b))
    else:
        result[position : position + 2] = (conjugate(b, a), a)
    return tuple(result)


def act(word, route):
    for position, sign in route:
        word = hurwitz(word, position, sign)
    return word


def json_word(word):
    return [list(item) for item in word]


def json_route(route):
    return [[position + 1, sign] for position, sign in route]


def digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


# Internal positions are zero-based. Each word acts chronologically.
IDENTITY = ()
EDIT1_RUN0 = (
    (1, 1), (2, 1), (3, -1), (4, -1),
    (5, -1), (6, 1), (7, -1), (6, -1), (5, -1),
    (4, 1), (3, 1), (2, -1), (1, -1),
)
EDIT1_RUN1 = (
    (1, -1), (2, -1), (3, 1), (4, 1),
    (5, -1), (6, 1), (7, -1), (6, -1), (5, -1),
    (4, -1), (3, -1), (2, 1), (1, 1),
)
EDIT1_RUN2 = (
    (1, -1), (2, -1), (3, -1), (4, -1),
    (5, -1), (6, 1), (7, -1), (6, -1), (5, 1),
    (4, 1), (3, 1), (2, 1), (1, 1),
)
EDIT3_RUN0 = (
    (3, 1), (4, 1), (5, -1), (6, 1), (7, -1),
    (6, -1), (5, -1), (4, -1), (3, -1),
)
EDIT3_RUN1 = (
    (3, -1), (4, -1), (5, -1), (6, 1), (7, -1),
    (6, -1), (5, 1), (4, 1), (3, 1),
)
EDIT5_STANDARD = ((5, -1), (6, 1), (7, -1), (6, -1), (5, -1))
EDIT6 = ((4, -1), (4, -1))
EDIT7 = ((7, -1),)


def path_to_attachment(parent, start, attachment=1):
    """Intrinsic parent path from a rooted-DPS vertex to the attachment."""
    path = [start]
    while path[-1] != attachment:
        ancestor = parent[path[-1]]
        if ancestor is None:
            raise AssertionError("attachment is not an ancestor")
        path.append(ancestor)
    return tuple(path)


def odd_edit_key(tree, edit):
    """Intrinsic finite key derived only from the rooted tree and edit.

    Here the declared one-leaf template roots the old tree at 5 and attaches
    the new root 6 at white vertex 1. For edit i=2v-3, v is the black-slot
    vertex whose two DPS edge labels are exchanged.
    """
    assert edit in (1, 3, 5)
    vertex = (edit + 3) // 2
    parent, children = rooted_structure(tree, 5)
    path = path_to_attachment(parent, vertex, 1)
    internal = path[1:-1]
    late_ancestor = any(label > vertex for label in internal)
    child_run = 0
    for label in range(vertex + 1, 5):
        if label in children[vertex]:
            child_run += 1
        else:
            break
    return {
        "edit": edit,
        "vertex": vertex,
        "path_to_attachment": list(path),
        "late_ancestor": late_ancestor,
        "consecutive_larger_child_run": child_run,
    }


def classification(tree, edit):
    if edit in (2, 4):
        return f"edit{edit}:universal_identity", IDENTITY, None
    if edit == 6:
        return "edit6:universal_double_inverse", EDIT6, None
    if edit == 7:
        return "edit7:universal_inverse", EDIT7, None

    key = odd_edit_key(tree, edit)
    path = tuple(key["path_to_attachment"])
    late = key["late_ancestor"]
    run = key["consecutive_larger_child_run"]
    if edit == 1:
        if late:
            return "edit1:late_ancestor", IDENTITY, key
        routes = {0: EDIT1_RUN0, 1: EDIT1_RUN1, 2: EDIT1_RUN2}
        assert run in routes
        return f"edit1:direct_run_{run}", routes[run], key
    if edit == 3:
        if late:
            return "edit3:late_ancestor", IDENTITY, key
        routes = {0: EDIT3_RUN0, 1: EDIT3_RUN1}
        assert run in routes
        return f"edit3:direct_run_{run}", routes[run], key
    assert edit == 5
    if path == (4, 2, 3, 1):
        return "edit5:exceptional_path_4_2_3_1", IDENTITY, key
    return "edit5:standard", EDIT5_STANDARD, key


def main():
    pi5 = (7, 8, 1, 2, 3, 4, 5, 6)
    pi6 = (9, 10, 1, 2, 3, 4, 5, 6, 7, 8)
    trees = [
        tree for tree in prufer_trees(5)
        if (1, 5) in tree and sum(5 in item for item in tree) == 1
    ]
    assert len(trees) == 16

    rows = []
    class_rows = defaultdict(list)
    route_by_class = {}
    for tree_id, tree5 in enumerate(trees):
        tree6 = tree5 | {(1, 6)}
        for edit in range(1, 8):
            class_id, route, key = classification(tree5, edit)
            naive = dps_word(tree5, swap_values(pi5, edit), 5) + ((0, 5), (0, 5))
            actual = dps_word(tree6, swap_values(pi6, edit), 6)
            output = act(naive, route)
            assert output == actual, (tree_id, edit, class_id)
            assert class_id not in route_by_class or route_by_class[class_id] == route
            route_by_class[class_id] = route
            row = {
                "tree_id": tree_id,
                "tree5": [list(item) for item in sorted(tree5)],
                "edit": edit,
                "class_id": class_id,
                "intrinsic_odd_key": key,
                "route": json_route(route),
                "route_length": len(route),
                "naive_target": json_word(naive),
                "actual_target": json_word(actual),
                "exact_replay": True,
            }
            rows.append(row)
            class_rows[class_id].append(row)

    classes = []
    for class_id in sorted(class_rows):
        members = class_rows[class_id]
        route = route_by_class[class_id]
        classes.append({
            "class_id": class_id,
            "edit": members[0]["edit"],
            "tree_ids": [row["tree_id"] for row in members],
            "size": len(members),
            "route": json_route(route),
            "route_length": len(route),
            "row_digest": digest(members),
        })

    distinct_route_encodings = sorted({
        tuple(tuple(step) for step in item["route"]) for item in classes
    })
    assert len(rows) == 112
    assert len(classes) == 13
    assert len(distinct_route_encodings) == 9
    expected_sizes = {
        "edit1:direct_run_0": 5,
        "edit1:direct_run_1": 2,
        "edit1:direct_run_2": 1,
        "edit1:late_ancestor": 8,
        "edit2:universal_identity": 16,
        "edit3:direct_run_0": 7,
        "edit3:direct_run_1": 4,
        "edit3:late_ancestor": 5,
        "edit4:universal_identity": 16,
        "edit5:exceptional_path_4_2_3_1": 1,
        "edit5:standard": 15,
        "edit6:universal_double_inverse": 16,
        "edit7:universal_inverse": 16,
    }
    assert {item["class_id"]: item["size"] for item in classes} == expected_sizes

    payload = {
        "experiment": "M214 exact 16-tree rooted-contour correction classification",
        "scope": (
            "complete declared d5 one-leaf template: root 5 leaf at attachment "
            "1, common pi5/pi6, inherited edits 1..7; no Q6 enumeration"
        ),
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "tree_template_count": len(trees),
        "row_count": len(rows),
        "case_count": len(classes),
        "distinct_correction_words": len(distinct_route_encodings),
        "maximum_correction_length": max(item["route_length"] for item in classes),
        "all_replays_pass": all(row["exact_replay"] for row in rows),
        "class_summary": classes,
        "classification_digest": digest(rows),
        "classes_digest": digest(classes),
        "rows": rows,
        "proof_boundary": (
            "Exhaustive completeness is only for the 16-tree d5 template. "
            "The intrinsic key is defined for this template; no general-d "
            "sufficiency is asserted."
        ),
    }
    (HERE / "contour_classification_results.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps({
        key: payload[key] for key in (
            "tree_template_count", "row_count", "case_count",
            "distinct_correction_words", "maximum_correction_length",
            "all_replays_pass", "classification_digest", "classes_digest",
            "class_summary", "proof_boundary",
        )
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

