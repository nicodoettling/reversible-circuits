#!/usr/bin/env python3
"""Exact audit of M225's two predeclared child-contour candidates.

The script reconstructs the complete d=6 root-leaf tree template and all nine
edited endpoint pairs, then literally replays Candidate A and Candidate B.
There is no route search, quotient enumeration, or predecessor import/data
read.  Candidate definitions are transcribed from candidate_descriptors.md.
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
OUTPUT = HERE / "child_contour_results.json"


def edge(a: int, b: int):
    assert a != b
    return (a, b) if a < b else (b, a)


def prufer_trees(vertices):
    vertices = tuple(vertices)
    for code in itertools.product(vertices, repeat=len(vertices) - 2):
        degree = {vertex: 1 for vertex in vertices}
        for vertex in code:
            degree[vertex] += 1
        result = []
        for vertex in code:
            leaf = min(item for item in vertices if degree[item] == 1)
            result.append(edge(leaf, vertex))
            degree[leaf] -= 1
            degree[vertex] -= 1
        leaves = [item for item in vertices if degree[item] == 1]
        assert len(leaves) == 2
        result.append(edge(*leaves))
        yield frozenset(result)


def template(d: int):
    direct = {tree | {(1, d)} for tree in prufer_trees(range(1, d))}
    ordered = [
        tree
        for tree in prufer_trees(range(1, d + 1))
        if (1, d) in tree and sum(d in item for item in tree) == 1
    ]
    assert set(ordered) == direct
    assert len(ordered) == (d - 1) ** (d - 3)
    return ordered


def parents(tree, root: int):
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
        labels = order[2 * child - 2 : 2 * child]
        black = ("b", child)
        for label, white_id in ((labels[0], child), (labels[1], parent[child])):
            white = ("w", white_id)
            incidence[black][label] = white
            incidence[white][label] = black
            first_black[label] = child
    modulus = 2 * d - 2
    start = (("w", 1), 1)
    state = start
    seen = set()
    tokens = []
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        direction = 1 if vertex[0] == "w" else -1
        label = 1 + ((incoming - 1 + direction) % modulus)
        if label in incidence[vertex]:
            tokens.append(("side",))
            state = incidence[vertex][label], label
        else:
            tokens.append(("half", vertex[0], vertex[1], label))
            state = vertex, label
    assert state == start
    assert len(tokens) == (2 * d - 1) * modulus
    return tokens, first_black


def close_boundary(tokens, d: int):
    tokens = list(tokens)
    second_black = {}
    while True:
        half = [index for index, token in enumerate(tokens) if token[0] == "half"]
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
    assert len(residue) == 2 * d - 2
    assert all(token[1] == "w" for token in residue)
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
    a, b = by

    def image(vertex):
        return b if vertex == a else a if vertex == b else vertex

    return edge(image(transposition[0]), image(transposition[1]))


def hurwitz(word, symbol: int):
    position = abs(symbol) - 1
    left, right = word[position : position + 2]
    result = list(word)
    if symbol > 0:
        result[position : position + 2] = (right, conjugate(left, right))
    else:
        result[position : position + 2] = (conjugate(right, left), left)
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
        permutation = tuple(transposition[permutation[index]] for index in range(d))
    return permutation


def stopped_path(parent, vertex: int):
    result = [vertex]
    while result[-1] != 1:
        next_vertex = parent[result[-1]]
        assert next_vertex is not None
        result.append(next_vertex)
    return tuple(result)


def child_signs(bits):
    bits = tuple(bits)
    if not bits:
        return ()
    signs = [-1 if bits[0] else 1]
    for bit in bits[1:]:
        signs.append(-1 if bit else -signs[-1])
    return tuple(signs)


def ordinary_data(tree, d: int, edit: int):
    vertex = (edit + 3) // 2
    parent = parents(tree, d)
    path = stopped_path(parent, vertex)
    late = any(item > vertex for item in path[1:-1])
    bits = tuple(parent[label] == vertex for label in range(vertex + 1, d))
    forward_path = (vertex,) + tuple(range(2, vertex)) + (1,)
    forward_exception = vertex >= 4 and path == forward_path
    internal = path[1:-1]
    ascent = any(left < right for left, right in zip(internal, internal[1:]))
    offpath = []
    path_set = set(path)
    for path_vertex in path:
        offpath.append(tuple(
            label
            for label in range(1, d)
            if parent.get(label) == path_vertex and label not in path_set
        ))
    return {
        "vertex": vertex,
        "path": path,
        "late": late,
        "child_bits": bits,
        "child_signs": child_signs(bits),
        "forward_exception": forward_exception,
        "ascent": ascent,
        "offpath_children": tuple(offpath),
    }


def carrier_word(d: int, data):
    vertex = data["vertex"]
    q = []
    for offset, sign in enumerate(data["child_signs"]):
        generator = 2 * (vertex + offset) - 2
        q.extend((sign * generator, sign * (generator + 1)))
    p = 2 * d - 4
    carrier = (-p, p + 1, -(p + 2), -(p + 1), -p)
    q = tuple(q)
    return q + carrier + inverse_route(q)


def candidate_route(tree, d: int, edit: int, candidate: str):
    if edit % 2 == 1 and edit <= 2 * d - 5:
        data = ordinary_data(tree, d, edit)
        if candidate == "A":
            identity_case = data["late"] or data["forward_exception"]
            descriptor = (
                "odd_A",
                data["vertex"],
                data["late"],
                data["child_bits"],
                data["forward_exception"],
            )
        else:
            assert candidate == "B"
            identity_case = data["late"] or data["ascent"]
            descriptor = (
                "odd_B",
                data["vertex"],
                data["late"],
                data["child_bits"],
                data["forward_exception"],
                data["path"],
                data["offpath_children"],
            )
        route = () if identity_case else carrier_word(d, data)
        details = {
            key: list(value) if isinstance(value, tuple) else value
            for key, value in data.items()
        }
        details["offpath_children"] = [list(value) for value in data["offpath_children"]]
        return route, descriptor, details

    if edit % 2 == 0 and edit <= 2 * d - 6:
        return (), ("internal_even",), {"kind": "internal_even"}
    if edit == 2 * d - 4:
        generator = 2 * d - 5
        return (-generator, -generator), ("cross_boundary",), {
            "kind": "cross_boundary"
        }
    assert edit == 2 * d - 3
    return (-(2 * d - 2),), ("old_high_pair",), {"kind": "old_high_pair"}


def json_tree(tree):
    return [list(item) for item in sorted(tree)]


def json_word(word):
    return [list(item) for item in word]


def json_route(route):
    return [[abs(symbol), 1 if symbol > 0 else -1] for symbol in route]


def jsonable(value):
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    return value


def compact_digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def audit_candidate(candidate: str, d: int, trees, endpoint_rows):
    rows = []
    identity = tuple(range(d + 1))
    for endpoint in endpoint_rows:
        route, descriptor, details = candidate_route(
            endpoint["tree_raw"], d, endpoint["edit"], candidate
        )
        replay = act(endpoint["naive_raw"], route)
        assert product(replay, d + 1) == identity
        mismatches = [
            position + 1
            for position, pair in enumerate(zip(replay, endpoint["actual_raw"]))
            if pair[0] != pair[1]
        ]
        rows.append({
            "tree_id": endpoint["tree_id"],
            "tree": endpoint["tree"],
            "edit": endpoint["edit"],
            "descriptor": jsonable(descriptor),
            "details": details,
            "route": json_route(route),
            "route_length": len(route),
            "naive": endpoint["naive"],
            "actual": endpoint["actual"],
            "replay": json_word(replay),
            "pass": replay == endpoint["actual_raw"],
            "naive_equals_actual": endpoint["naive_raw"] == endpoint["actual_raw"],
            "mismatch_positions": mismatches,
        })

    groups = defaultdict(list)
    for row in rows:
        groups[json.dumps(row["descriptor"], separators=(",", ":"))].append(row)
    class_summary = []
    for descriptor in sorted(groups):
        group = groups[descriptor]
        routes = {
            json.dumps(row["route"], separators=(",", ":")) for row in group
        }
        assert len(routes) == 1
        class_summary.append({
            "descriptor": json.loads(descriptor),
            "size": len(group),
            "passes": sum(row["pass"] for row in group),
            "failures": sum(not row["pass"] for row in group),
            "route": json.loads(next(iter(routes))),
            "route_length": group[0]["route_length"],
        })
    first_collision = None
    for descriptor in sorted(groups):
        group = groups[descriptor]
        for left_index, left in enumerate(group):
            for right in group[left_index + 1:]:
                if left["pass"] != right["pass"]:
                    first_collision = {
                        "descriptor": json.loads(descriptor),
                        "left": left,
                        "right": right,
                    }
                    break
            if first_collision:
                break
        if first_collision:
            break

    pass_counts = [
        sum(row["pass"] for row in rows if row["edit"] == edit)
        for edit in range(1, 2 * d - 2)
    ]
    lengths = [row["route_length"] for row in rows]
    length_histogram = {
        str(length): sum(value == length for value in lengths)
        for length in sorted(set(lengths))
    }
    distinct_routes = {
        json.dumps(row["route"], separators=(",", ":")) for row in rows
    }
    return {
        "candidate": candidate,
        "row_count": len(rows),
        "passes": sum(row["pass"] for row in rows),
        "failures": sum(not row["pass"] for row in rows),
        "pass_counts_by_edit": pass_counts,
        "failure_counts_by_edit": [len(trees) - count for count in pass_counts],
        "class_count": len(groups),
        "class_summary": class_summary,
        "distinct_route_count": len(distinct_routes),
        "identity_route_rows": sum(not row["route"] for row in rows),
        "route_length_histogram": length_histogram,
        "maximum_route_length": max(lengths),
        "complete_rows_digest": compact_digest(rows),
        "first_failure": next((row for row in rows if not row["pass"]), None),
        "first_same_descriptor_pass_failure": first_collision,
    }


def build_endpoints(d: int, trees):
    order = canonical_order(d)
    next_order = canonical_order(d + 1)
    leaf_pair = ((0, d), (0, d))
    identity = tuple(range(d + 1))
    endpoints = []
    for tree_id, tree in enumerate(trees):
        extension = tree | {(1, d + 1)}
        assert dps_word(extension, next_order, d + 1) == dps_word(tree, order, d) + leaf_pair
        for edit in range(1, 2 * d - 2):
            naive = dps_word(tree, swap_values(order, edit), d) + leaf_pair
            actual = dps_word(extension, swap_values(next_order, edit), d + 1)
            assert product(naive, d + 1) == product(actual, d + 1) == identity
            endpoints.append({
                "tree_id": tree_id,
                "tree_raw": tree,
                "tree": json_tree(tree),
                "edit": edit,
                "naive_raw": naive,
                "actual_raw": actual,
                "naive": json_word(naive),
                "actual": json_word(actual),
            })
    return endpoints


def verify_formal_carrier():
    count = 0
    for x, y, z, n in itertools.permutations(range(7), 4):
        source = (edge(x, y), edge(z, x), edge(z, y), edge(z, n))
        target = (edge(x, n), edge(z, y), edge(z, y), edge(z, x))
        assert act(source, (-1, 2, -3, -2, -1)) == target
        count += 1
    return count


def main():
    carrier_checks = verify_formal_carrier()
    trees = template(6)
    assert len(trees) == 125
    endpoints = build_endpoints(6, trees)
    assert len(endpoints) == 1125

    candidate_a = audit_candidate("A", 6, trees, endpoints)
    candidate_b = audit_candidate("B", 6, trees, endpoints)

    result = {
        "experiment": "M225 two predeclared full child-contour candidates",
        "target": "deterministic chronological signed-Hurwitz endpoint correction",
        "method": {
            "candidate_order": ["A", "B"],
            "candidates_predeclared": True,
            "third_candidate_allowed": False,
            "route_search": False,
            "quotient_enumeration": False,
            "predecessor_imports": False,
            "predecessor_data_reads": False,
        },
        "formal_carrier_checks": carrier_checks,
        "tree_count": len(trees),
        "edit_count": 9,
        "endpoint_row_count": len(endpoints),
        "candidate_A": candidate_a,
        "candidate_B": candidate_b,
        "environment": {
            "python": platform.python_version(),
            "nonstandard_dependencies": {},
            "seed": None,
        },
        "scope": (
            "Exact finite d6->7 only; failure refutes only the displayed formula; "
            "success supplies no all-rank induction or mixing conclusion."
        ),
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "carrier_checks": carrier_checks,
        "tree_count": len(trees),
        "rows": len(endpoints),
        "candidate_A": {
            key: candidate_a[key]
            for key in (
                "passes", "failures", "pass_counts_by_edit",
                "maximum_route_length", "complete_rows_digest"
            )
        },
        "candidate_B": {
            key: candidate_b[key]
            for key in (
                "passes", "failures", "pass_counts_by_edit",
                "maximum_route_length", "complete_rows_digest"
            )
        },
        "A_has_collision": candidate_a["first_same_descriptor_pass_failure"] is not None,
        "B_has_collision": candidate_b["first_same_descriptor_pass_failure"] is not None,
        "output": str(OUTPUT),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
