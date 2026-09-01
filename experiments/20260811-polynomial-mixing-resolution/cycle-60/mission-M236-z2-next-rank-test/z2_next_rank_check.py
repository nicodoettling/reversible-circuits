#!/usr/bin/env python3
"""Exact next-rank replay of the frozen M231 route-normal formula.

This checker reads no input files.  For every primary row it computes Z2 and
the literal formula word before constructing either DPS endpoint.  It performs
no route search, target lookup, quotient/group enumeration, or formula
adaptation.  The six fixed non-Z2 edit families are replayed separately.
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
OUTPUT = Path(__file__).with_name("z2_next_rank_results.json")


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


def tree_key(tree):
    return tuple(sorted(tree))


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
    return tuple(sorted(direct, key=tree_key))


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
        permutation = tuple(
            transposition[permutation[index]] for index in range(degree)
        )
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
    closed = late or ascent
    z2 = ("closed",) if closed else ("open", vertex, signs)
    return {
        "vertex": vertex,
        "path": path,
        "internal": internal,
        "late": late,
        "ascent": ascent,
        "closed": closed,
        "bits": bits,
        "signs": signs,
        "z2": z2,
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


def fixed_non_z2_route(d, edit):
    if edit % 2 == 0 and edit <= 2 * d - 6:
        return ()
    if edit == 2 * d - 4:
        return (-(2 * d - 5), -(2 * d - 5))
    if edit == 2 * d - 3:
        return (-(2 * d - 2),)
    raise AssertionError((d, edit))


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


def normalized_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest(value):
    return hashlib.sha256(normalized_json(value).encode()).hexdigest()


def mismatch_positions(left, right):
    return [
        position
        for position, pair in enumerate(zip(left, right), start=1)
        if pair[0] != pair[1]
    ]


def primary_row(tree_id, tree, d, edit, row_index):
    # Anti-lookup order: the frozen descriptor and route are computed before
    # either endpoint exists in this call.
    data = descriptor_data(tree, d, edit)
    route = formula_route(d, data)
    naive, actual = endpoint_pair(tree, d, edit)
    replay = act(naive, route)
    return {
        "row_index": row_index,
        "tree_id": tree_id,
        "tree": json_tree(tree),
        "edit": edit,
        "vertex": data["vertex"],
        "path": jsonable(data["path"]),
        "late": data["late"],
        "ascent": data["ascent"],
        "closed": data["closed"],
        "bits": jsonable(data["bits"]),
        "epsilon": jsonable(data["signs"]),
        "z2": jsonable(data["z2"]),
        "route": json_route(route),
        "route_length": len(route),
        "naive": json_word(naive),
        "actual": json_word(actual),
        "replay": json_word(replay),
        "pass": replay == actual,
        "naive_equals_actual": naive == actual,
        "mismatch_positions": mismatch_positions(replay, actual),
    }


def secondary_row(tree_id, tree, d, edit, row_index):
    route = fixed_non_z2_route(d, edit)
    naive, actual = endpoint_pair(tree, d, edit)
    replay = act(naive, route)
    return {
        "row_index": row_index,
        "tree_id": tree_id,
        "tree": json_tree(tree),
        "edit": edit,
        "family": (
            "internal_even"
            if edit <= 2 * d - 6
            else "cross_boundary"
            if edit == 2 * d - 4
            else "old_high_pair"
        ),
        "route": json_route(route),
        "route_length": len(route),
        "naive": json_word(naive),
        "actual": json_word(actual),
        "replay": json_word(replay),
        "pass": replay == actual,
        "naive_equals_actual": naive == actual,
        "mismatch_positions": mismatch_positions(replay, actual),
    }


def public_witness(row):
    return row if row is None else dict(row)


def first_behavior_collision(rows):
    seen = defaultdict(lambda: {True: [], False: []})
    for row in rows:
        key = normalized_json(row["z2"])
        opposite = seen[key][not row["pass"]]
        if opposite:
            return {
                "z2": row["z2"],
                "left": public_witness(opposite[0]),
                "right": public_witness(row),
            }
        seen[key][row["pass"]].append(row)
    return None


def z2_summary(rows, edits):
    groups = defaultdict(list)
    for row in rows:
        groups[normalized_json(row["z2"])].append(row)

    classes = []
    word_collision = None
    for key in sorted(groups):
        group = groups[key]
        routes = sorted({normalized_json(row["route"]) for row in group})
        if len(routes) != 1 and word_collision is None:
            word_collision = {
                "z2": json.loads(key),
                "routes": [json.loads(route) for route in routes],
            }
        classes.append({
            "z2": json.loads(key),
            "size": len(group),
            "passes": sum(row["pass"] for row in group),
            "failures": sum(not row["pass"] for row in group),
            "route_count": len(routes),
            "route": json.loads(routes[0]) if len(routes) == 1 else None,
            "route_length": group[0]["route_length"] if len(routes) == 1 else None,
        })

    by_edit = {}
    for edit in edits:
        edit_rows = [row for row in rows if row["edit"] == edit]
        edit_groups = defaultdict(list)
        for row in edit_rows:
            edit_groups[normalized_json(row["z2"])].append(row)
        by_edit[str(edit)] = {
            "rows": len(edit_rows),
            "passes": sum(row["pass"] for row in edit_rows),
            "failures": sum(not row["pass"] for row in edit_rows),
            "class_count": len(edit_groups),
            "closed_rows": sum(row["closed"] for row in edit_rows),
            "open_rows": sum(not row["closed"] for row in edit_rows),
            "late_rows": sum(row["late"] for row in edit_rows),
            "ascent_rows": sum(row["ascent"] for row in edit_rows),
            "class_size_histogram": {
                str(size): count
                for size, count in sorted(
                    Counter(len(group) for group in edit_groups.values()).items()
                )
            },
        }

    return {
        "class_count": len(groups),
        "classes_by_edit": by_edit,
        "word_homogeneous": word_collision is None,
        "first_word_collision": word_collision,
        "first_behavior_collision": first_behavior_collision(rows),
        "class_summary_digest": digest(classes),
        "class_summaries": classes,
    }


def per_edit_summary(rows, edits):
    return {
        str(edit): {
            "rows": sum(row["edit"] == edit for row in rows),
            "passes": sum(row["edit"] == edit and row["pass"] for row in rows),
            "failures": sum(
                row["edit"] == edit and not row["pass"] for row in rows
            ),
        }
        for edit in edits
    }


def formal_checks(d):
    carrier = (-1, 2, -3, -2, -1)
    carrier_checks = 0
    for x, y, z, n in itertools.permutations(range(d + 1), 4):
        source = (edge(x, y), edge(z, x), edge(z, y), edge(z, n))
        target = (edge(x, n), edge(z, y), edge(z, y), edge(z, x))
        assert act(source, carrier) == target
        carrier_checks += 1

    sign_initial_run_checks = 0
    for length in range(d):
        for run in range(length + 1):
            bits = (True,) * run + (False,) * (length - run)
            expected = (-1,) * run + tuple(
                1 if offset % 2 == 0 else -1
                for offset in range(length - run)
            )
            assert sign_vector(bits) == expected
            sign_initial_run_checks += 1
    return carrier_checks, sign_initial_run_checks


def main():
    d = 7
    odd_edits = (1, 3, 5, 7, 9)
    secondary_edits = (2, 4, 6, 8, 10, 11)
    all_edits = tuple(range(1, 2 * d - 2))
    assert tuple(sorted(odd_edits + secondary_edits)) == all_edits

    carrier_checks, sign_checks = formal_checks(d)
    trees = root_leaf_template(d)
    assert len(trees) == 6**4 == 1296

    primary_rows = []
    secondary_rows = []
    for tree_id, tree in enumerate(trees):
        for edit in odd_edits:
            primary_rows.append(
                primary_row(
                    tree_id,
                    tree,
                    d,
                    edit,
                    len(primary_rows),
                )
            )
        for edit in secondary_edits:
            secondary_rows.append(
                secondary_row(
                    tree_id,
                    tree,
                    d,
                    edit,
                    len(secondary_rows),
                )
            )

    assert len(primary_rows) == 6480
    assert len(secondary_rows) == 7776
    assert len(primary_rows) + len(secondary_rows) == 14256

    z2 = z2_summary(primary_rows, odd_edits)
    assert z2["word_homogeneous"]

    primary_failures = [row for row in primary_rows if not row["pass"]]
    secondary_failures = [row for row in secondary_rows if not row["pass"]]
    behavior_collision = z2["first_behavior_collision"]
    if not primary_failures:
        primary_verdict = "FINITE_PASS"
        failure_classification = None
    elif behavior_collision is not None:
        primary_verdict = "FINITE_OBSTRUCTION"
        failure_classification = "SAME_Z2_BEHAVIOR_COLLISION"
    else:
        primary_verdict = "FINITE_OBSTRUCTION"
        failure_classification = "PREDECLARED_WORD_FORMULA_FAILURE"

    secondary_verdict = (
        "FIXED_FAMILIES_PASS"
        if not secondary_failures
        else "FIXED_FAMILY_OBSTRUCTION"
    )

    primary_routes = sorted(
        {normalized_json(row["route"]) for row in primary_rows}
    )
    secondary_routes = sorted(
        {normalized_json(row["route"]) for row in secondary_rows}
    )
    full_routes = sorted(set(primary_routes) | set(secondary_routes))

    primary_length_histogram = {
        str(length): count
        for length, count in sorted(
            Counter(row["route_length"] for row in primary_rows).items()
        )
    }
    full_length_histogram = {
        str(length): count
        for length, count in sorted(
            Counter(
                row["route_length"] for row in primary_rows + secondary_rows
            ).items()
        )
    }

    result = {
        "experiment": "M236 exact d7->8 next-rank test of M231/M234 Z2",
        "target": "deterministic chronological signed-Hurwitz endpoint correction",
        "primary_verdict": primary_verdict,
        "failure_classification": failure_classification,
        "secondary_verdict": secondary_verdict,
        "method": {
            "input_files": [],
            "predecessor_imports": False,
            "predecessor_data_reads": False,
            "formula_change_from_M231": "rank d only",
            "assignment_precedes_endpoint_construction": True,
            "endpoint_derived_adaptation": False,
            "route_search": False,
            "target_word_lookup": False,
            "quotient_state_enumeration": False,
            "group_element_enumeration": False,
            "descriptor_class_census_only": True,
            "tree_order": "lexicographic sorted edge tuples",
            "row_order": "tree order, then increasing edit within scope",
        },
        "rank": {"old_d": d, "new_d": d + 1},
        "formal_carrier_checks": carrier_checks,
        "sign_initial_run_checks": sign_checks,
        "tree_count": len(trees),
        "tree_count_formula": "(d-1)^(d-3)=6^4",
        "tree_universe_digest": digest([json_tree(tree) for tree in trees]),
        "primary": {
            "scope": "Z2 ordinary odd edits",
            "edits": list(odd_edits),
            "row_count": len(primary_rows),
            "passes": len(primary_rows) - len(primary_failures),
            "failures": len(primary_failures),
            "by_edit": per_edit_summary(primary_rows, odd_edits),
            "closed_rows": sum(row["closed"] for row in primary_rows),
            "open_rows": sum(not row["closed"] for row in primary_rows),
            "late_rows": sum(row["late"] for row in primary_rows),
            "ascent_rows": sum(row["ascent"] for row in primary_rows),
            "distinct_formula_words": len(primary_routes),
            "route_length_histogram": primary_length_histogram,
            "maximum_route_length": max(row["route_length"] for row in primary_rows),
            "rows_digest": digest(primary_rows),
            "word_inventory_digest": digest(
                [json.loads(route) for route in primary_routes]
            ),
            "first_formula_failure": public_witness(
                primary_failures[0] if primary_failures else None
            ),
            "Z2": z2,
        },
        "secondary": {
            "scope": "fixed non-Z2 full-table reconciliation",
            "edits": list(secondary_edits),
            "row_count": len(secondary_rows),
            "passes": len(secondary_rows) - len(secondary_failures),
            "failures": len(secondary_failures),
            "by_edit": per_edit_summary(secondary_rows, secondary_edits),
            "distinct_formula_words": len(secondary_routes),
            "rows_digest": digest(secondary_rows),
            "first_failure": public_witness(
                secondary_failures[0] if secondary_failures else None
            ),
        },
        "full_table": {
            "edits": list(all_edits),
            "row_count": len(primary_rows) + len(secondary_rows),
            "passes": (
                len(primary_rows)
                + len(secondary_rows)
                - len(primary_failures)
                - len(secondary_failures)
            ),
            "failures": len(primary_failures) + len(secondary_failures),
            "distinct_formula_words": len(full_routes),
            "route_length_histogram": full_length_histogram,
            "rows_digest": digest({
                "primary": primary_rows,
                "secondary": secondary_rows,
            }),
            "word_inventory_digest": digest(
                [json.loads(route) for route in full_routes]
            ),
        },
        "environment": {
            "python": platform.python_version(),
            "nonstandard_dependencies": {},
            "seed": None,
        },
        "scope_boundary": (
            "Exact finite d7->8 template only; no all-d, every-color, "
            "polynomial-length, comparison, gap, mixing, or Terminal inference."
        ),
    }

    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "primary_verdict": primary_verdict,
        "failure_classification": failure_classification,
        "secondary_verdict": secondary_verdict,
        "trees": len(trees),
        "primary_rows": len(primary_rows),
        "primary_passes": len(primary_rows) - len(primary_failures),
        "primary_failures": len(primary_failures),
        "primary_by_edit": result["primary"]["by_edit"],
        "Z2_class_count": z2["class_count"],
        "Z2_classes_by_edit": z2["classes_by_edit"],
        "primary_words": len(primary_routes),
        "primary_maximum_route_length": result["primary"]["maximum_route_length"],
        "primary_rows_digest": result["primary"]["rows_digest"],
        "Z2_class_digest": z2["class_summary_digest"],
        "first_formula_failure": result["primary"]["first_formula_failure"],
        "first_behavior_collision": z2["first_behavior_collision"],
        "secondary_rows": len(secondary_rows),
        "secondary_failures": len(secondary_failures),
        "secondary_by_edit": result["secondary"]["by_edit"],
        "full_rows_digest": result["full_table"]["rows_digest"],
        "output": str(OUTPUT),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
