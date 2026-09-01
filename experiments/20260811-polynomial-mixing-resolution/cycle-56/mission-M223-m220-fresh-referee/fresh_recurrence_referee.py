#!/usr/bin/env python3
"""Clean-room exact referee for frozen M220.

No M220 code or result data are imported or read.  This script independently
reconstructs the formal Hurwitz identities, rooted DPS closure, explicit
recurrence, complete d=5 and d=6 templates, normalized digest, and first
same-key witness.  It performs no route search or quotient enumeration.
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
OUTPUT = HERE / "referee_results.json"

EXPECTED_M220_INVENTORY = (
    "0b953e9c517cfeb379d32abe04b32ea928dd2a83e67bc1ac40d61f87fccd1316"
)
EXPECTED_D6_DIGEST = (
    "f0deca809ef570f7d557a88a94d517e3885f971f0178ac7ef2938bad651341c0"
)
EXPECTED_PASSES = [114, 125, 125, 125, 125, 125, 109, 125, 125]


def normalized_edge(a: int, b: int):
    assert a != b
    return (a, b) if a < b else (b, a)


def all_prufer_trees(vertices: tuple[int, ...]):
    """Lexicographic Prüfer decoder using the least available leaf."""
    length = len(vertices) - 2
    for code in itertools.product(vertices, repeat=length):
        degree = {vertex: 1 for vertex in vertices}
        for vertex in code:
            degree[vertex] += 1
        edges = []
        for vertex in code:
            leaf = min(candidate for candidate in vertices if degree[candidate] == 1)
            edges.append(normalized_edge(leaf, vertex))
            degree[leaf] -= 1
            degree[vertex] -= 1
        leaves = [vertex for vertex in vertices if degree[vertex] == 1]
        assert len(leaves) == 2
        edges.append(normalized_edge(leaves[0], leaves[1]))
        yield frozenset(edges)


def complete_root_leaf_template(d: int):
    smaller = {
        tree | {(1, d)}
        for tree in all_prufer_trees(tuple(range(1, d)))
    }
    full_ordered = [
        tree
        for tree in all_prufer_trees(tuple(range(1, d + 1)))
        if (1, d) in tree and sum(d in edge for edge in tree) == 1
    ]
    assert set(full_ordered) == smaller
    assert len(full_ordered) == len(smaller) == (d - 1) ** (d - 3)
    return full_ordered


def parent_map(tree, root: int):
    neighbors = {vertex: [] for vertex in range(1, root + 1)}
    for a, b in tree:
        neighbors[a].append(b)
        neighbors[b].append(a)
    parent = {root: None}
    frontier = [root]
    while frontier:
        current = frontier.pop()
        for neighbor in sorted(neighbors[current], reverse=True):
            if neighbor not in parent:
                parent[neighbor] = current
                frontier.append(neighbor)
    assert len(parent) == root
    return parent


def trace_hairy_boundary(tree, order, d: int):
    parent = parent_map(tree, d)
    incident = defaultdict(dict)
    first_black = {}
    for child in range(1, d):
        labels = order[2 * child - 2 : 2 * child]
        black = ("b", child)
        for label, white_index in ((labels[0], child), (labels[1], parent[child])):
            white = ("w", white_index)
            incident[black][label] = white
            incident[white][label] = black
            first_black[label] = child

    modulus = 2 * d - 2
    initial = (("w", 1), 1)
    state = initial
    visited = set()
    boundary = []
    while state not in visited:
        visited.add(state)
        vertex, incoming = state
        direction = 1 if vertex[0] == "w" else -1
        label = 1 + ((incoming - 1 + direction) % modulus)
        if label in incident[vertex]:
            boundary.append(("side",))
            state = incident[vertex][label], label
        else:
            boundary.append(("half", vertex[0], vertex[1], label))
            state = vertex, label
    assert state == initial
    assert len(boundary) == (2 * d - 1) * modulus
    assert set(first_black) == set(range(1, modulus + 1))
    return boundary, first_black


def intrinsic_closure(boundary, d: int):
    boundary = list(boundary)
    second_black = {}
    while True:
        half = [index for index, token in enumerate(boundary) if token[0] == "half"]
        selected = None
        for offset, white_index in enumerate(half):
            black_index = half[(offset + 1) % len(half)]
            if boundary[white_index][1] == "w" and boundary[black_index][1] == "b":
                selected = white_index, black_index
                break
        if selected is None:
            break
        white_index, black_index = selected
        boundary = boundary[white_index:] + boundary[:white_index]
        black_index = (black_index - white_index) % len(boundary)
        white, black = boundary[0], boundary[black_index]
        assert white[3] == black[3]
        distance = sum(token[0] == "side" for token in boundary[1:black_index])
        assert distance in (1, 3)
        if distance == 3:
            assert white[3] not in second_black
            second_black[white[3]] = black[2]
        boundary = [("side",)] + boundary[black_index + 1 :]
    remainder = [token for token in boundary if token[0] == "half"]
    assert len(remainder) == 2 * d - 2
    assert all(token[1] == "w" for token in remainder)
    return second_black


def rooted_dps_word(tree, order, d: int):
    boundary, first_black = trace_hairy_boundary(tree, order, d)
    second_black = intrinsic_closure(boundary, d)
    return tuple(
        normalized_edge(first_black[label] - 1, second_black.get(label, d) - 1)
        for label in range(1, 2 * d - 1)
    )


def conjugated_edge(edge, conjugator):
    a, b = conjugator

    def image(vertex):
        if vertex == a:
            return b
        if vertex == b:
            return a
        return vertex

    return normalized_edge(image(edge[0]), image(edge[1]))


def signed_hurwitz(word, symbol: int):
    assert symbol != 0
    position = abs(symbol) - 1
    left, right = word[position : position + 2]
    result = list(word)
    if symbol > 0:
        result[position : position + 2] = (
            right,
            conjugated_edge(left, right),
        )
    else:
        result[position : position + 2] = (
            conjugated_edge(right, left),
            left,
        )
    return tuple(result)


def chronological_action(word, route):
    for symbol in route:
        word = signed_hurwitz(word, symbol)
    return word


def inverse_word(route):
    return tuple(-symbol for symbol in reversed(route))


def permutation_product(word, degree: int):
    permutation = tuple(range(degree))
    for a, b in word:
        transposition = list(range(degree))
        transposition[a], transposition[b] = transposition[b], transposition[a]
        permutation = tuple(transposition[permutation[index]] for index in range(degree))
    return permutation


def canonical_order(d: int):
    return (2 * d - 3, 2 * d - 2) + tuple(range(1, 2 * d - 3))


def adjacent_value_swap(order, edit: int):
    return tuple(
        edit + 1
        if value == edit
        else edit
        if value == edit + 1
        else value
        for value in order
    )


def path_to_attachment(parent, vertex: int):
    path = [vertex]
    while path[-1] != 1:
        next_vertex = parent[path[-1]]
        assert next_vertex is not None
        path.append(next_vertex)
    return tuple(path)


def displayed_recurrence(tree, d: int, edit: int):
    parent = parent_map(tree, d)
    if edit % 2 == 1 and edit <= 2 * d - 5:
        vertex = (edit + 3) // 2
        path = path_to_attachment(parent, vertex)
        late = any(item > vertex for item in path[1:-1])
        run = 0
        for child in range(vertex + 1, d):
            if parent[child] != vertex:
                break
            run += 1
        forward_path = (vertex,) + tuple(range(2, vertex)) + (1,)
        exceptional = vertex >= 4 and path == forward_path
        proposed_class = ["ordinary_odd", vertex, late, run, exceptional]
        descriptor = {
            "kind": "ordinary_odd",
            "vertex": vertex,
            "path": list(path),
            "late_ancestor": late,
            "direct_child_run": run,
            "forward_chain_exception": exceptional,
            "proposed_class": proposed_class,
        }
        if late or exceptional:
            return (), descriptor

        q = []
        for offset in range(d - vertex - 1):
            if offset < run:
                sign = -1
            else:
                sign = 1 if (offset - run) % 2 == 0 else -1
            generator = 2 * (vertex + offset) - 2
            q.extend((sign * generator, sign * (generator + 1)))
        p = 2 * d - 4
        carrier = (-p, p + 1, -(p + 2), -(p + 1), -p)
        q = tuple(q)
        return q + carrier + inverse_word(q), descriptor

    if edit % 2 == 0 and edit <= 2 * d - 6:
        return (), {
            "kind": "internal_even",
            "proposed_class": ["internal_even"],
        }
    if edit == 2 * d - 4:
        generator = 2 * d - 5
        return (-generator, -generator), {
            "kind": "cross_boundary_even",
            "proposed_class": ["cross_boundary_even"],
        }
    assert edit == 2 * d - 3
    return (-(2 * d - 2),), {
        "kind": "old_high_pair",
        "proposed_class": ["old_high_pair"],
    }


def json_tree(tree):
    return [list(edge) for edge in sorted(tree)]


def json_word(word):
    return [list(edge) for edge in word]


def json_route(route):
    return [[abs(symbol), 1 if symbol > 0 else -1] for symbol in route]


def compact_digest(value):
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def normalized_row(row):
    return {
        "tree_id": row["tree_id"],
        "tree": row["tree"],
        "edit": row["edit"],
        "proposed_class": row["descriptor"]["proposed_class"],
        "descriptor": row["descriptor"],
        "route": row["route"],
        "naive": row["naive"],
        "actual": row["actual"],
        "replay": row["replay"],
        "pass": row["pass"],
        "naive_equals_actual": row["naive_equals_actual"],
        "mismatch_positions": row["mismatch_positions"],
    }


def audit_rank(d: int):
    trees = complete_root_leaf_template(d)
    old_order = canonical_order(d)
    new_order = canonical_order(d + 1)
    appended = ((0, d), (0, d))
    old_identity = tuple(range(d))
    new_identity = tuple(range(d + 1))
    rows = []
    for tree_id, tree in enumerate(trees):
        extension = tree | {(1, d + 1)}
        old_source = rooted_dps_word(tree, old_order, d)
        new_source = rooted_dps_word(extension, new_order, d + 1)
        assert new_source == old_source + appended
        assert permutation_product(old_source, d) == old_identity
        assert permutation_product(new_source, d + 1) == new_identity
        for edit in range(1, 2 * d - 2):
            route, descriptor = displayed_recurrence(tree, d, edit)
            naive = rooted_dps_word(
                tree, adjacent_value_swap(old_order, edit), d
            ) + appended
            actual = rooted_dps_word(
                extension, adjacent_value_swap(new_order, edit), d + 1
            )
            replay = chronological_action(naive, route)
            assert permutation_product(naive, d + 1) == new_identity
            assert permutation_product(actual, d + 1) == new_identity
            assert permutation_product(replay, d + 1) == new_identity
            mismatches = [
                index + 1
                for index, pair in enumerate(zip(replay, actual))
                if pair[0] != pair[1]
            ]
            rows.append(
                {
                    "tree_id": tree_id,
                    "tree": json_tree(tree),
                    "edit": edit,
                    "descriptor": descriptor,
                    "route": json_route(route),
                    "naive": json_word(naive),
                    "actual": json_word(actual),
                    "replay": json_word(replay),
                    "pass": replay == actual,
                    "naive_equals_actual": naive == actual,
                    "mismatch_positions": mismatches,
                }
            )
    return trees, rows


def first_same_key_pass_failure(rows):
    groups = defaultdict(list)
    for row in rows:
        key = json.dumps(row["descriptor"]["proposed_class"], separators=(",", ":"))
        groups[key].append(row)
    for key in sorted(groups):
        group = groups[key]
        for left_index, left in enumerate(group):
            for right in group[left_index + 1 :]:
                if left["pass"] != right["pass"]:
                    return {
                        "proposed_class": json.loads(key),
                        "left": normalized_row(left),
                        "right": normalized_row(right),
                    }
    return None


def formal_identity_audit():
    carrier_checks = 0
    for x, y, z, n in itertools.permutations(range(7), 4):
        source = (
            normalized_edge(x, y),
            normalized_edge(z, x),
            normalized_edge(z, y),
            normalized_edge(z, n),
        )
        expected = (
            normalized_edge(x, n),
            normalized_edge(z, y),
            normalized_edge(z, y),
            normalized_edge(z, x),
        )
        assert chronological_action(source, (-1, 2, -3, -2, -1)) == expected
        carrier_checks += 1

    double_checks = 0
    for x, y, z in itertools.permutations(range(7), 3):
        a = normalized_edge(x, y)
        b = normalized_edge(z, x)
        c = normalized_edge(z, y)
        assert chronological_action((a, b, a), (-1, -1)) == (b, c, a)
        double_checks += 1

    all_edges = list(itertools.combinations(range(7), 2))
    single_checks = 0
    for a in all_edges:
        for b in all_edges:
            expected = (conjugated_edge(b, a), a)
            assert chronological_action((a, b), (-1,)) == expected
            single_checks += 1

    return {
        "carrier_distinct_assignments": carrier_checks,
        "double_inverse_distinct_assignments": double_checks,
        "single_inverse_edge_pairs": single_checks,
        "all_pass": True,
    }


def main():
    formal = formal_identity_audit()

    trees5, rows5 = audit_rank(5)
    assert len(trees5) == 16 and len(rows5) == 112
    assert all(row["pass"] for row in rows5)

    trees6, rows6 = audit_rank(6)
    assert len(trees6) == 125 and len(rows6) == 1125
    pass_counts = [
        sum(row["pass"] for row in rows6 if row["edit"] == edit)
        for edit in range(1, 10)
    ]
    assert pass_counts == EXPECTED_PASSES
    failure_counts = [125 - count for count in pass_counts]

    normalized = [normalized_row(row) for row in rows6]
    row_digest = compact_digest(normalized)
    assert row_digest == EXPECTED_D6_DIGEST

    witness = first_same_key_pass_failure(rows6)
    assert witness is not None
    expected_t0 = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6]]
    expected_t1 = [[1, 2], [1, 3], [1, 4], [1, 6], [2, 5]]
    assert witness["proposed_class"] == ["ordinary_odd", 2, False, 0, False]
    assert witness["left"]["tree"] == expected_t0
    assert witness["right"]["tree"] == expected_t1
    assert witness["left"]["descriptor"] == witness["right"]["descriptor"]
    assert witness["left"]["pass"] is True
    assert witness["right"]["pass"] is False
    assert witness["left"]["route"] == witness["right"]["route"]
    assert len(witness["left"]["route"]) == 17
    assert witness["right"]["mismatch_positions"] == [7, 8]
    assert witness["right"]["replay"][6:8] == [[4, 5], [4, 5]]
    assert witness["right"]["actual"][6:8] == [[4, 6], [4, 6]]

    result = {
        "experiment": "M223 clean-room referee of M220",
        "source_lock": {
            "expected_m220_sha256sums_digest": EXPECTED_M220_INVENTORY,
            "externally_verified_before_computation": True,
            "complete_inventory_ok": True,
        },
        "method": {
            "clean_room": True,
            "m220_imports": False,
            "m220_data_reads": False,
            "route_search": False,
            "q6_enumeration": False,
            "q7_enumeration": False,
            "action_order": "chronological",
        },
        "formal_identities": formal,
        "d5_to_d6": {
            "tree_count": len(trees5),
            "row_count": len(rows5),
            "passes": sum(row["pass"] for row in rows5),
            "failures": sum(not row["pass"] for row in rows5),
            "rows_digest": compact_digest([normalized_row(row) for row in rows5]),
        },
        "d6_to_d7": {
            "tree_count": len(trees6),
            "edit_count": 9,
            "row_count": len(rows6),
            "pass_counts_by_edit": pass_counts,
            "failure_counts_by_edit": failure_counts,
            "total_passes": sum(pass_counts),
            "total_failures": sum(failure_counts),
            "complete_rows_digest": row_digest,
            "digest_matches_expected": True,
            "first_same_key_witness": witness,
        },
        "logical_verdict": {
            "accept_m220": True,
            "refuted": "only the displayed key-to-word recurrence",
            "not_refuted": [
                "an alternative common braid",
                "a richer contour descriptor",
                "an all-rank theorem by another construction",
            ],
        },
        "environment": {
            "python": platform.python_version(),
            "nonstandard_dependencies": {},
            "seed": None,
        },
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "formal": formal,
        "d5_rows": len(rows5),
        "d5_failures": 0,
        "d6_rows": len(rows6),
        "pass_counts": pass_counts,
        "failure_counts": failure_counts,
        "row_digest": row_digest,
        "witness_trees": [witness["left"]["tree"], witness["right"]["tree"]],
        "witness_mismatches": witness["right"]["mismatch_positions"],
        "output": str(OUTPUT),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
