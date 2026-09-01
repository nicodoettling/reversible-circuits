#!/usr/bin/env python3
"""Exact finite audit of two predeclared contour quotients.

No input files are read.  Formula words are assigned from tree/edit data
before endpoint construction.  There is no route search, quotient-state
enumeration, or predecessor import/data dependency.
"""

from __future__ import annotations

import hashlib
import heapq
import itertools
import json
import platform
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path


sys.dont_write_bytecode = True
OUTPUT = Path(__file__).with_name("compression_results.json")


def edge(a, b):
    assert a != b
    return (a, b) if a < b else (b, a)


def decode_prufer(vertices, code):
    vertices = tuple(sorted(vertices))
    degree = Counter({vertex: 1 for vertex in vertices})
    degree.update(code)
    leaves = [vertex for vertex in vertices if degree[vertex] == 1]
    heapq.heapify(leaves)
    result = []
    for vertex in code:
        leaf = heapq.heappop(leaves)
        result.append(edge(leaf, vertex))
        degree[leaf] -= 1
        degree[vertex] -= 1
        if degree[vertex] == 1:
            heapq.heappush(leaves, vertex)
    result.append(edge(heapq.heappop(leaves), heapq.heappop(leaves)))
    assert not leaves
    return frozenset(result)


def prufer_trees(vertices):
    vertices = tuple(sorted(vertices))
    for code in itertools.product(vertices, repeat=len(vertices) - 2):
        yield decode_prufer(vertices, code)


def root_leaf_template(d):
    direct = []
    for tree in prufer_trees(range(1, d + 1)):
        incident = [item for item in tree if d in item]
        if len(incident) == 1 and incident[0] == edge(1, d):
            direct.append(tree)
    extended = {
        tree | {edge(1, d)}
        for tree in prufer_trees(range(1, d))
    }
    assert set(direct) == extended
    assert len(direct) == (d - 1) ** (d - 3)
    return direct


def parents(tree, root):
    adjacency = {vertex: [] for vertex in range(1, root + 1)}
    for a, b in tree:
        adjacency[a].append(b)
        adjacency[b].append(a)
    parent = {root: None}
    queue = deque([root])
    while queue:
        vertex = queue.popleft()
        for neighbor in sorted(adjacency[vertex]):
            if neighbor not in parent:
                parent[neighbor] = vertex
                queue.append(neighbor)
    assert len(parent) == root
    return parent


def trace_boundary(tree, order, d):
    parent = parents(tree, d)
    ports = defaultdict(dict)
    first_black = {}
    for child in range(1, d):
        black = ("b", child)
        left, right = order[2 * child - 2 : 2 * child]
        for label, white_id in ((left, child), (right, parent[child])):
            white = ("w", white_id)
            ports[black][label] = white
            ports[white][label] = black
            first_black[label] = child

    modulus = 2 * d - 2
    initial = (("w", 1), 1)
    state = initial
    seen = set()
    trace = []
    while state not in seen:
        seen.add(state)
        node, incoming = state
        step = 1 if node[0] == "w" else -1
        label = 1 + ((incoming - 1 + step) % modulus)
        if label in ports[node]:
            trace.append(("side",))
            state = ports[node][label], label
        else:
            trace.append(("open", node[0], node[1], label))
            state = node, label
    assert state == initial
    assert len(trace) == (2 * d - 1) * modulus
    return trace, first_black


def close_trace(trace, d):
    trace = list(trace)
    second_black = {}
    while True:
        opens = [index for index, item in enumerate(trace) if item[0] == "open"]
        selected = None
        for offset, white_index in enumerate(opens):
            black_index = opens[(offset + 1) % len(opens)]
            if trace[white_index][1] == "w" and trace[black_index][1] == "b":
                selected = white_index, black_index
                break
        if selected is None:
            break
        white_index, black_index = selected
        trace = trace[white_index:] + trace[:white_index]
        black_index = (black_index - white_index) % len(trace)
        white, black = trace[0], trace[black_index]
        assert white[3] == black[3]
        side_count = sum(item[0] == "side" for item in trace[1:black_index])
        assert side_count in (1, 3)
        if side_count == 3:
            second_black[white[3]] = black[2]
        trace = [("side",)] + trace[black_index + 1 :]
    residue = [item for item in trace if item[0] == "open"]
    assert len(residue) == 2 * d - 2
    assert all(item[1] == "w" for item in residue)
    return second_black


def dps_word(tree, order, d):
    trace, first_black = trace_boundary(tree, order, d)
    second_black = close_trace(trace, d)
    return tuple(
        edge(first_black[label] - 1, second_black.get(label, d) - 1)
        for label in range(1, 2 * d - 1)
    )


def canonical_order(d):
    return (2 * d - 3, 2 * d - 2) + tuple(range(1, 2 * d - 3))


def edited_order(order, edit):
    return tuple(
        edit + 1 if label == edit else edit if label == edit + 1 else label
        for label in order
    )


def conjugate(transposition, by):
    a, b = by

    def image(vertex):
        return b if vertex == a else a if vertex == b else vertex

    return edge(image(transposition[0]), image(transposition[1]))


def hurwitz(word, signed_generator):
    position = abs(signed_generator) - 1
    left, right = word[position : position + 2]
    result = list(word)
    if signed_generator > 0:
        result[position : position + 2] = (right, conjugate(left, right))
    else:
        result[position : position + 2] = (conjugate(right, left), left)
    return tuple(result)


def act(word, route):
    for signed_generator in route:
        word = hurwitz(word, signed_generator)
    return word


def product(word, degree):
    permutation = tuple(range(degree))
    for a, b in word:
        transposition = list(range(degree))
        transposition[a], transposition[b] = transposition[b], transposition[a]
        permutation = tuple(transposition[permutation[index]] for index in range(degree))
    return permutation


def stopped_path(parent, vertex):
    path = [vertex]
    while path[-1] != 1:
        path.append(parent[path[-1]])
    assert path[-1] == 1
    return tuple(path)


def sign_vector(bits):
    bits = tuple(bits)
    if not bits:
        return ()
    signs = [-1 if bits[0] else 1]
    for bit in bits[1:]:
        signs.append(-1 if bit else -signs[-1])
    return tuple(signs)


def descriptor_data(tree, d, edit):
    vertex = (edit + 3) // 2
    parent = parents(tree, d)
    path = stopped_path(parent, vertex)
    internal = path[1:-1]
    late = any(item > vertex for item in internal)
    ascent = any(left < right for left, right in zip(internal, internal[1:]))
    bits = tuple(parent[label] == vertex for label in range(vertex + 1, d))
    signs = sign_vector(bits)
    forward = vertex >= 4 and path == (
        (vertex,) + tuple(range(2, vertex)) + (1,)
    )
    path_set = set(path)
    offpath = tuple(
        tuple(
            label
            for label in range(1, d)
            if parent.get(label) == path_vertex and label not in path_set
        )
        for path_vertex in path
    )
    full = ("odd_B", vertex, late, bits, forward, path, offpath)
    q1 = ("Q1", vertex, late, ascent, signs)
    closed = late or ascent
    q2 = ("closed",) if closed else ("open", vertex, signs)
    return {
        "vertex": vertex,
        "late": late,
        "ascent": ascent,
        "closed": closed,
        "bits": bits,
        "signs": signs,
        "path": path,
        "offpath": offpath,
        "full_descriptor": full,
        "q1": q1,
        "q2": q2,
    }


def inverse_route(route):
    return tuple(-item for item in reversed(route))


def formula_route(d, data):
    if data["closed"]:
        return ()
    transport = []
    for offset, sign in enumerate(data["signs"]):
        first = 2 * (data["vertex"] + offset) - 2
        transport.extend((sign * first, sign * (first + 1)))
    transport = tuple(transport)
    base = 2 * d - 4
    carrier = (-base, base + 1, -(base + 2), -(base + 1), -base)
    return transport + carrier + inverse_route(transport)


def endpoint_pair(tree, d, edit):
    leaf_pair = ((0, d), (0, d))
    old = dps_word(tree, edited_order(canonical_order(d), edit), d) + leaf_pair
    extension = tree | {edge(1, d + 1)}
    new = dps_word(
        extension,
        edited_order(canonical_order(d + 1), edit),
        d + 1,
    )
    identity = tuple(range(d + 1))
    assert product(old, d + 1) == identity
    assert product(new, d + 1) == identity
    return old, new


def jsonable(value):
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    return value


def json_tree(tree):
    return [list(item) for item in sorted(tree)]


def json_word(word):
    return [list(item) for item in word]


def json_route(route):
    return [[abs(item), 1 if item > 0 else -1] for item in route]


def digest(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode()).hexdigest()


def first_collision(groups, field):
    for key in sorted(groups):
        group = groups[key]
        for left_index, left in enumerate(group):
            for right in group[left_index + 1 :]:
                if left[field] != right[field]:
                    return {
                        "quotient": json.loads(key),
                        "field": field,
                        "left": left,
                        "right": right,
                    }
    return None


def quotient_summary(rows, quotient_name, edits):
    field = quotient_name.lower()
    groups = defaultdict(list)
    for row in rows:
        groups[json.dumps(row[field], separators=(",", ":"))].append(row)
    word_collision = first_collision(groups, "route")
    behavior_collision = first_collision(groups, "pass")
    summaries = []
    for key in sorted(groups):
        group = groups[key]
        routes = {json.dumps(row["route"], separators=(",", ":")) for row in group}
        summaries.append({
            "quotient": json.loads(key),
            "size": len(group),
            "route_count": len(routes),
            "passes": sum(row["pass"] for row in group),
            "failures": sum(not row["pass"] for row in group),
            "route": json.loads(next(iter(routes))) if len(routes) == 1 else None,
        })
    per_edit = {}
    for edit in edits:
        edit_rows = [row for row in rows if row["edit"] == edit]
        keys = {json.dumps(row[field], separators=(",", ":")) for row in edit_rows}
        sizes = Counter(
            sum(json.dumps(row[field], separators=(",", ":")) == key for row in edit_rows)
            for key in keys
        )
        per_edit[str(edit)] = {
            "class_count": len(keys),
            "class_size_histogram": {str(size): count for size, count in sorted(sizes.items())},
        }
    return {
        "quotient": quotient_name,
        "class_count": len(groups),
        "classes_by_edit": per_edit,
        "word_homogeneous": word_collision is None,
        "endpoint_correct": all(row["pass"] for row in rows),
        "first_word_collision": word_collision,
        "first_behavior_collision": behavior_collision,
        "class_summary_digest": digest(summaries),
        "class_summaries": summaries,
    }


def formal_checks():
    carrier = (-1, 2, -3, -2, -1)
    carrier_checks = 0
    for x, y, z, n in itertools.permutations(range(7), 4):
        source = (edge(x, y), edge(z, x), edge(z, y), edge(z, n))
        target = (edge(x, n), edge(z, y), edge(z, y), edge(z, x))
        assert act(source, carrier) == target
        carrier_checks += 1
    sign_checks = 0
    for length in range(6):
        for run in range(length + 1):
            bits = (True,) * run + (False,) * (length - run)
            expected = (-1,) * run + tuple(
                1 if offset % 2 == 0 else -1
                for offset in range(length - run)
            )
            assert sign_vector(bits) == expected
            sign_checks += 1
    return carrier_checks, sign_checks


def main():
    carrier_checks, sign_checks = formal_checks()
    d = 6
    odd_edits = (1, 3, 5, 7)
    trees = root_leaf_template(d)
    assert len(trees) == 125

    rows = []
    for tree_id, tree in enumerate(trees):
        for edit in odd_edits:
            # Anti-lookup order: descriptor and literal formula word are fixed
            # before either endpoint is constructed.
            data = descriptor_data(tree, d, edit)
            route = formula_route(d, data)
            naive, actual = endpoint_pair(tree, d, edit)
            replay = act(naive, route)
            rows.append({
                "tree_id": tree_id,
                "tree": json_tree(tree),
                "edit": edit,
                "full_descriptor": jsonable(data["full_descriptor"]),
                "q1": jsonable(data["q1"]),
                "q2": jsonable(data["q2"]),
                "route": json_route(route),
                "route_length": len(route),
                "naive": json_word(naive),
                "actual": json_word(actual),
                "replay": json_word(replay),
                "pass": replay == actual,
                "naive_equals_actual": naive == actual,
                "mismatch_positions": [
                    position
                    for position, pair in enumerate(zip(replay, actual), start=1)
                    if pair[0] != pair[1]
                ],
            })

    assert len(rows) == 500
    full_classes_by_edit = {
        str(edit): len({
            json.dumps(row["full_descriptor"], separators=(",", ":"))
            for row in rows if row["edit"] == edit
        })
        for edit in odd_edits
    }
    q1 = quotient_summary(rows, "Q1", odd_edits)
    q2 = quotient_summary(rows, "Q2", odd_edits)

    odd_routes = {
        json.dumps(row["route"], separators=(",", ":")) for row in rows
    }
    internal_even = ()
    cross_boundary = (-(2 * d - 5), -(2 * d - 5))
    old_high_pair = (-(2 * d - 2),)
    full_routes = set(odd_routes)
    full_routes.update(
        json.dumps(json_route(route), separators=(",", ":"))
        for route in (internal_even, cross_boundary, old_high_pair)
    )

    # Terminal finite obligations; none participates in formula assignment.
    assert full_classes_by_edit == {"1": 101, "3": 101, "5": 101, "7": 101}
    assert q1["word_homogeneous"] and q1["endpoint_correct"]
    assert q2["word_homogeneous"] and q2["endpoint_correct"]
    assert len(odd_routes) == 12
    assert len(full_routes) == 14

    result = {
        "experiment": "M231 finite contour-descriptor compression",
        "verdict": "PROMOTE_EXACT_FINITE_COMPRESSION",
        "target": "deterministic chronological signed-Hurwitz endpoint correction",
        "method": {
            "input_files": [],
            "predecessor_imports": False,
            "predecessor_data_reads": False,
            "route_search": False,
            "quotient_state_enumeration": False,
            "route_output_lookup": False,
            "assignment_precedes_endpoint_construction": True,
            "predeclared_quotients": ["Q1", "Q2"],
            "third_quotient_allowed": False,
        },
        "formal_carrier_checks": carrier_checks,
        "sign_initial_run_checks": sign_checks,
        "tree_count": len(trees),
        "odd_edits": list(odd_edits),
        "odd_row_count": len(rows),
        "odd_passes": sum(row["pass"] for row in rows),
        "odd_failures": sum(not row["pass"] for row in rows),
        "full_descriptor_classes_by_edit": full_classes_by_edit,
        "odd_distinct_formula_words": len(odd_routes),
        "full_table_distinct_formula_words": len(full_routes),
        "odd_rows_digest": digest(rows),
        "Q1": q1,
        "Q2": q2,
        "environment": {
            "python": platform.python_version(),
            "nonstandard_dependencies": {},
            "seed": None,
        },
        "scope": (
            "Complete finite d6->7 odd-edit table only; no all-d, every-color, "
            "total-length, gap, mixing, or Terminal inference."
        ),
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": result["verdict"],
        "trees": result["tree_count"],
        "odd_rows": result["odd_row_count"],
        "odd_passes": result["odd_passes"],
        "odd_words": result["odd_distinct_formula_words"],
        "full_table_words": result["full_table_distinct_formula_words"],
        "full_classes_by_edit": full_classes_by_edit,
        "Q1_class_count": q1["class_count"],
        "Q1_classes_by_edit": q1["classes_by_edit"],
        "Q2_class_count": q2["class_count"],
        "Q2_classes_by_edit": q2["classes_by_edit"],
        "odd_rows_digest": result["odd_rows_digest"],
        "Q1_class_digest": q1["class_summary_digest"],
        "Q2_class_digest": q2["class_summary_digest"],
        "output": str(OUTPUT),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
