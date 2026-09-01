#!/usr/bin/env python3
"""Clean-room finite referee for the two frozen child-contour formulae.

This program has no input files.  In particular it neither imports nor reads
the frozen mission's checker or machine data.  It generates trees, DPS words,
formula routes, replays, descriptors, and normalized row digests from scratch.
No quotient graph, route search, or route-output lookup is implemented.
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
OUTPUT = Path(__file__).with_name("referee_results.json")


def undirected(a: int, b: int) -> tuple[int, int]:
    if a == b:
        raise ValueError("a transposition/tree edge needs distinct endpoints")
    return (a, b) if a < b else (b, a)


def decode_prufer(labels, code) -> frozenset[tuple[int, int]]:
    """Decode a Prüfer word using a leaf heap (independent completeness path)."""

    labels = tuple(sorted(labels))
    degree = Counter({label: 1 for label in labels})
    degree.update(code)
    leaves = [label for label in labels if degree[label] == 1]
    heapq.heapify(leaves)
    edges = []
    for parent in code:
        leaf = heapq.heappop(leaves)
        edges.append(undirected(leaf, parent))
        degree[leaf] -= 1
        degree[parent] -= 1
        if degree[parent] == 1:
            heapq.heappush(leaves, parent)
    a = heapq.heappop(leaves)
    b = heapq.heappop(leaves)
    edges.append(undirected(a, b))
    assert not leaves and len(edges) == len(labels) - 1
    return frozenset(edges)


def all_labeled_trees(labels):
    labels = tuple(sorted(labels))
    for code in itertools.product(labels, repeat=len(labels) - 2):
        yield decode_prufer(labels, code)


def complete_root_leaf_template(d: int):
    """Return direct Prüfer order and cross-check an extension construction."""

    direct = []
    for tree in all_labeled_trees(range(1, d + 1)):
        root_edges = [item for item in tree if d in item]
        if root_edges == [undirected(1, d)]:
            direct.append(tree)
    extended = {
        tree | {undirected(1, d)}
        for tree in all_labeled_trees(range(1, d))
    }
    assert set(direct) == extended
    assert len(direct) == (d - 1) ** (d - 3)
    return direct


def rooted_parents(tree, root: int) -> dict[int, int | None]:
    neighbors = {vertex: [] for vertex in range(1, root + 1)}
    for a, b in tree:
        neighbors[a].append(b)
        neighbors[b].append(a)
    result = {root: None}
    queue = deque([root])
    while queue:
        vertex = queue.popleft()
        for neighbor in sorted(neighbors[vertex]):
            if neighbor not in result:
                result[neighbor] = vertex
                queue.append(neighbor)
    assert len(result) == root
    return result


def raw_boundary_walk(tree, paired_labels, d: int):
    """Trace the white/black rotation system before noncrossing closure."""

    parent = rooted_parents(tree, d)
    incidence = defaultdict(dict)
    first_black = {}
    for child in range(1, d):
        lo, hi = paired_labels[2 * child - 2 : 2 * child]
        black = ("black", child)
        for label, white_id in ((lo, child), (hi, parent[child])):
            white = ("white", white_id)
            incidence[black][label] = white
            incidence[white][label] = black
            first_black[label] = child

    modulus = 2 * d - 2
    initial = (("white", 1), 1)
    state = initial
    visited = set()
    events = []
    while state not in visited:
        visited.add(state)
        node, incoming = state
        delta = 1 if node[0] == "white" else -1
        label = 1 + ((incoming - 1 + delta) % modulus)
        if label in incidence[node]:
            events.append(("side",))
            state = incidence[node][label], label
        else:
            events.append(("open", node[0], node[1], label))
            state = node, label
    assert state == initial
    assert len(events) == (2 * d - 1) * modulus
    return events, first_black


def noncrossing_close(events, d: int):
    """Eliminate cyclic adjacent white/black opens and record depth-three mates."""

    events = list(events)
    second_black = {}
    while True:
        open_positions = [
            index for index, event in enumerate(events) if event[0] == "open"
        ]
        chosen = None
        for offset, white_index in enumerate(open_positions):
            black_index = open_positions[(offset + 1) % len(open_positions)]
            if (
                events[white_index][1] == "white"
                and events[black_index][1] == "black"
            ):
                chosen = white_index, black_index
                break
        if chosen is None:
            break

        white_index, black_index = chosen
        events = events[white_index:] + events[:white_index]
        black_index = (black_index - white_index) % len(events)
        white_event = events[0]
        black_event = events[black_index]
        assert white_event[3] == black_event[3]
        side_count = sum(event[0] == "side" for event in events[1:black_index])
        assert side_count in (1, 3)
        if side_count == 3:
            second_black[white_event[3]] = black_event[2]
        events = [("side",)] + events[black_index + 1 :]

    residue = [event for event in events if event[0] == "open"]
    assert len(residue) == 2 * d - 2
    assert all(event[1] == "white" for event in residue)
    return second_black


def dps_factorization(tree, paired_labels, d: int):
    events, first_black = raw_boundary_walk(tree, paired_labels, d)
    second_black = noncrossing_close(events, d)
    return tuple(
        undirected(first_black[label] - 1, second_black.get(label, d) - 1)
        for label in range(1, 2 * d - 1)
    )


def canonical_order(d: int):
    return (2 * d - 3, 2 * d - 2) + tuple(range(1, 2 * d - 3))


def adjacent_label_edit(order, edit: int):
    replacement = {edit: edit + 1, edit + 1: edit}
    return tuple(replacement.get(label, label) for label in order)


def conjugate_transposition(transposition, by):
    a, b = by
    return undirected(
        b if transposition[0] == a else a if transposition[0] == b else transposition[0],
        b if transposition[1] == a else a if transposition[1] == b else transposition[1],
    )


def signed_hurwitz(word, signed_generator: int):
    position = abs(signed_generator) - 1
    left, right = word[position : position + 2]
    result = list(word)
    if signed_generator > 0:
        result[position : position + 2] = (
            right,
            conjugate_transposition(left, right),
        )
    else:
        result[position : position + 2] = (
            conjugate_transposition(right, left),
            left,
        )
    return tuple(result)


def chronological_action(word, route):
    current = tuple(word)
    for signed_generator in route:
        current = signed_hurwitz(current, signed_generator)
    return current


def word_product(word, degree: int):
    permutation = tuple(range(degree))
    for a, b in word:
        transposition = list(range(degree))
        transposition[a], transposition[b] = transposition[b], transposition[a]
        permutation = tuple(transposition[permutation[index]] for index in range(degree))
    return permutation


def path_to_attachment(parent, vertex: int):
    path = [vertex]
    while path[-1] != 1:
        next_vertex = parent[path[-1]]
        assert next_vertex is not None
        path.append(next_vertex)
    return tuple(path)


def sign_automaton(child_bits):
    child_bits = tuple(child_bits)
    if not child_bits:
        return ()
    signs = [-1 if child_bits[0] else 1]
    for bit in child_bits[1:]:
        signs.append(-1 if bit else -signs[-1])
    return tuple(signs)


def contour_data(tree, d: int, edit: int):
    vertex = (edit + 3) // 2
    parent = rooted_parents(tree, d)
    path = path_to_attachment(parent, vertex)
    internal = path[1:-1]
    late = any(item > vertex for item in internal)
    child_bits = tuple(parent[label] == vertex for label in range(vertex + 1, d))
    forward_path = (vertex,) + tuple(range(2, vertex)) + (1,)
    forward_exception = vertex >= 4 and path == forward_path
    ascent = any(left < right for left, right in zip(internal, internal[1:]))
    path_vertices = set(path)
    offpath_children = tuple(
        tuple(
            label
            for label in range(1, d)
            if parent.get(label) == path_vertex and label not in path_vertices
        )
        for path_vertex in path
    )
    return {
        "vertex": vertex,
        "path": path,
        "late": late,
        "child_bits": child_bits,
        "child_signs": sign_automaton(child_bits),
        "forward_exception": forward_exception,
        "ascent": ascent,
        "offpath_children": offpath_children,
    }


def reverse_route(route):
    return tuple(-item for item in reversed(route))


def transported_carrier(d: int, data):
    vertex = data["vertex"]
    transport = []
    for offset, sign in enumerate(data["child_signs"]):
        first = 2 * (vertex + offset) - 2
        transport.extend((sign * first, sign * (first + 1)))
    base = 2 * d - 4
    carrier = (-base, base + 1, -(base + 2), -(base + 1), -base)
    transport = tuple(transport)
    return transport + carrier + reverse_route(transport)


def formula_assignment(tree, d: int, edit: int, candidate: str):
    """Assign from tree/edit only; no endpoint word is accepted as an argument."""

    if edit % 2 == 1 and edit <= 2 * d - 5:
        data = contour_data(tree, d, edit)
        if candidate == "A":
            descriptor = (
                "odd_A",
                data["vertex"],
                data["late"],
                data["child_bits"],
                data["forward_exception"],
            )
            closes = data["late"] or data["forward_exception"]
        elif candidate == "B":
            descriptor = (
                "odd_B",
                data["vertex"],
                data["late"],
                data["child_bits"],
                data["forward_exception"],
                data["path"],
                data["offpath_children"],
            )
            closes = data["late"] or data["ascent"]
        else:
            raise ValueError(candidate)
        route = () if closes else transported_carrier(d, data)
        details = {
            key: list(value) if isinstance(value, tuple) else value
            for key, value in data.items()
        }
        details["offpath_children"] = [
            list(children) for children in data["offpath_children"]
        ]
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
    return [[abs(item), 1 if item > 0 else -1] for item in route]


def json_value(value):
    if isinstance(value, tuple):
        return [json_value(item) for item in value]
    return value


def normalized_digest(value):
    serialization = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialization.encode()).hexdigest()


def endpoint_pair(tree, d: int, edit: int):
    old_order = adjacent_label_edit(canonical_order(d), edit)
    new_order = adjacent_label_edit(canonical_order(d + 1), edit)
    extension = tree | {undirected(1, d + 1)}
    repeated_leaf = ((0, d), (0, d))
    naive = dps_factorization(tree, old_order, d) + repeated_leaf
    actual = dps_factorization(extension, new_order, d + 1)
    identity = tuple(range(d + 1))
    assert word_product(naive, d + 1) == identity
    assert word_product(actual, d + 1) == identity
    return naive, actual


def audit_formula(candidate: str, trees, d: int):
    rows = []
    for tree_id, tree in enumerate(trees):
        for edit in range(1, 2 * d - 2):
            # Decisive anti-lookup order: assign route before endpoints exist.
            route, descriptor, details = formula_assignment(tree, d, edit, candidate)
            naive, actual = endpoint_pair(tree, d, edit)
            replay = chronological_action(naive, route)
            mismatch_positions = [
                position
                for position, (left, right) in enumerate(zip(replay, actual), start=1)
                if left != right
            ]
            rows.append({
                "tree_id": tree_id,
                "tree": json_tree(tree),
                "edit": edit,
                "descriptor": json_value(descriptor),
                "details": details,
                "route": json_route(route),
                "route_length": len(route),
                "naive": json_word(naive),
                "actual": json_word(actual),
                "replay": json_word(replay),
                "pass": replay == actual,
                "naive_equals_actual": naive == actual,
                "mismatch_positions": mismatch_positions,
            })

    grouped = defaultdict(list)
    for row in rows:
        grouped[json.dumps(row["descriptor"], separators=(",", ":"))].append(row)

    class_summaries = []
    for key in sorted(grouped):
        group = grouped[key]
        assigned_words = {
            json.dumps(row["route"], separators=(",", ":")) for row in group
        }
        assert len(assigned_words) == 1
        class_summaries.append({
            "descriptor": json.loads(key),
            "size": len(group),
            "passes": sum(row["pass"] for row in group),
            "failures": sum(not row["pass"] for row in group),
            "route": json.loads(next(iter(assigned_words))),
            "route_length": group[0]["route_length"],
        })

    collision = None
    for key in sorted(grouped):
        group = grouped[key]
        for left_index, left in enumerate(group):
            for right in group[left_index + 1 :]:
                if left["pass"] != right["pass"]:
                    collision = {
                        "descriptor": json.loads(key),
                        "left": left,
                        "right": right,
                    }
                    break
            if collision is not None:
                break
        if collision is not None:
            break

    pass_counts = [
        sum(row["pass"] for row in rows if row["edit"] == edit)
        for edit in range(1, 2 * d - 2)
    ]
    lengths = [row["route_length"] for row in rows]
    length_histogram = {
        str(length): sum(item == length for item in lengths)
        for length in sorted(set(lengths))
    }
    routes = {
        json.dumps(row["route"], separators=(",", ":")) for row in rows
    }
    return {
        "candidate": candidate,
        "row_count": len(rows),
        "passes": sum(row["pass"] for row in rows),
        "failures": sum(not row["pass"] for row in rows),
        "pass_counts_by_edit": pass_counts,
        "failure_counts_by_edit": [len(trees) - count for count in pass_counts],
        "class_count": len(grouped),
        "class_summary": class_summaries,
        "distinct_route_count": len(routes),
        "identity_route_rows": sum(not row["route"] for row in rows),
        "route_length_histogram": length_histogram,
        "maximum_route_length": max(lengths),
        "complete_rows_digest": normalized_digest(rows),
        "first_failure": next((row for row in rows if not row["pass"]), None),
        "first_same_descriptor_pass_failure": collision,
    }


def formal_carrier_audit():
    route = (-1, 2, -3, -2, -1)
    checks = 0
    for x, y, z, n in itertools.permutations(range(7), 4):
        source = (
            undirected(x, y),
            undirected(z, x),
            undirected(z, y),
            undirected(z, n),
        )
        target = (
            undirected(x, n),
            undirected(z, y),
            undirected(z, y),
            undirected(z, x),
        )
        assert chronological_action(source, route) == target
        checks += 1
    return checks


def sign_automaton_audit():
    checks = 0
    for length in range(6):
        for run in range(length + 1):
            bits = (True,) * run + (False,) * (length - run)
            expected = (-1,) * run + tuple(
                1 if offset % 2 == 0 else -1
                for offset in range(length - run)
            )
            assert sign_automaton(bits) == expected
            checks += 1
    assert sign_automaton((False, False, False)) == (1, -1, 1)
    assert sign_automaton((False, False, True)) == (1, -1, -1)
    return checks


def main():
    carrier_checks = formal_carrier_audit()
    sign_checks = sign_automaton_audit()
    d = 6
    trees = complete_root_leaf_template(d)
    assert len(trees) == 125

    unedited_extension_checks = 0
    for tree in trees:
        extension = tree | {undirected(1, d + 1)}
        assert dps_factorization(
            extension, canonical_order(d + 1), d + 1
        ) == dps_factorization(tree, canonical_order(d), d) + ((0, d), (0, d))
        unedited_extension_checks += 1

    candidate_a = audit_formula("A", trees, d)
    candidate_b = audit_formula("B", trees, d)

    # Expected certificates are terminal assertions only.  They play no role
    # in tree generation, endpoint construction, or formula assignment.
    assert candidate_a["passes"] == 1109
    assert candidate_a["failures"] == 16
    assert candidate_a["pass_counts_by_edit"] == [125] * 6 + [109, 125, 125]
    assert candidate_a["complete_rows_digest"] == (
        "85b01dc81f7175b8df32d198181e7b898507ec71d0862ca963c431695f0a15f6"
    )
    assert candidate_b["passes"] == 1125
    assert candidate_b["failures"] == 0
    assert candidate_b["pass_counts_by_edit"] == [125] * 9
    assert candidate_b["class_count"] == 407
    assert candidate_b["distinct_route_count"] == 14
    assert candidate_b["maximum_route_length"] == 17
    assert candidate_b["complete_rows_digest"] == (
        "80ba2016f66f6f8bd9d6cb8a53b276c0ee4403a4ec6747fdd85568299817f78e"
    )

    result = {
        "experiment": "M228 clean-room immutable referee of finite child-contour formulae",
        "verdict": "ACCEPT",
        "target": "deterministic chronological signed-Hurwitz endpoint correction",
        "method": {
            "input_files": [],
            "predecessor_imports": False,
            "predecessor_data_reads": False,
            "route_search": False,
            "quotient_enumeration": False,
            "route_output_lookup": False,
            "assignment_inputs": ["tree", "d", "edit", "candidate"],
            "assignment_precedes_endpoint_construction": True,
            "expected_certificates_used_only_as_terminal_assertions": True,
        },
        "formal_carrier_checks": carrier_checks,
        "sign_initial_run_checks": sign_checks,
        "unedited_extension_checks": unedited_extension_checks,
        "tree_count": len(trees),
        "edit_count": 9,
        "endpoint_row_count": 1125,
        "candidate_A": candidate_a,
        "candidate_B": candidate_b,
        "source_order_caveat": (
            "Frozen text and filesystem mtimes support predeclaration, but the "
            "inventory itself is not a cryptographic timestamp of that chronology."
        ),
        "descriptor_scope": (
            "Candidate B nearly records a complete root contour; finite success "
            "does not prove intrinsic or all-rank descriptor sufficiency."
        ),
        "environment": {
            "python": platform.python_version(),
            "nonstandard_dependencies": {},
            "seed": None,
        },
        "scope": (
            "Exact finite d6->7 only; no all-d, every-color, total-length, gap, "
            "mixing, or Terminal inference."
        ),
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": result["verdict"],
        "carrier_checks": carrier_checks,
        "sign_checks": sign_checks,
        "tree_count": len(trees),
        "rows": 1125,
        "candidate_A": {
            key: candidate_a[key]
            for key in (
                "passes", "failures", "pass_counts_by_edit", "class_count",
                "distinct_route_count", "maximum_route_length", "complete_rows_digest"
            )
        },
        "candidate_B": {
            key: candidate_b[key]
            for key in (
                "passes", "failures", "pass_counts_by_edit", "class_count",
                "distinct_route_count", "maximum_route_length", "complete_rows_digest"
            )
        },
        "output": str(OUTPUT),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
