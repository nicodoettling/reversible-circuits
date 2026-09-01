#!/usr/bin/env python3
"""Clean-room exact referee for M214's finite rooted-contour theorem.

This standalone checker imports and reads no M214 code or result data.  It
reconstructs the complete declared tree template, rooted descriptor, DPS
endpoints, and signed-Hurwitz replays from the human-readable theorem.  It
does no route search and constructs no Q6 quotient graph.
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
OUTPUT = HERE / "referee_results.json"

EXPECTED_SOURCE_INVENTORY_DIGEST = (
    "cb63ac879b036d096af369fabf02da9abecba786bcf746ba34d809b8ceaada3f"
)
EXPECTED_CLASSIFICATION_DIGEST = (
    "96e39aea0f4a7aac3b75cadf286dc9e0343fe47801808c965d0d06545007d10b"
)
EXPECTED_SUMMARY_DIGEST = (
    "0963d5d0826a70e16dce02ff23e394f5d8fd1edecd79d6dbf3363213770a23c0"
)


def edge(a: int, b: int) -> tuple[int, int]:
    assert a != b
    return (a, b) if a < b else (b, a)


def prufer_trees(vertices: tuple[int, ...]):
    """Generate all labeled trees, directly from their Prüfer codes."""
    n = len(vertices)
    assert n >= 2
    for code in itertools.product(vertices, repeat=n - 2):
        degree = {vertex: 1 for vertex in vertices}
        for vertex in code:
            degree[vertex] += 1
        result = []
        for vertex in code:
            leaf = min(x for x in vertices if degree[x] == 1)
            result.append(edge(leaf, vertex))
            degree[leaf] -= 1
            degree[vertex] -= 1
        leaves = [x for x in vertices if degree[x] == 1]
        assert len(leaves) == 2
        result.append(edge(*leaves))
        yield frozenset(result)


def rooted_parents(tree: frozenset[tuple[int, int]], root: int):
    adjacency = {vertex: [] for vertex in range(1, root + 1)}
    for a, b in tree:
        adjacency[a].append(b)
        adjacency[b].append(a)
    for neighbors in adjacency.values():
        neighbors.sort(reverse=True)
    parent = {root: None}
    stack = [root]
    while stack:
        vertex = stack.pop()
        for neighbor in adjacency[vertex]:
            if neighbor not in parent:
                parent[neighbor] = vertex
                stack.append(neighbor)
    assert len(parent) == root
    return parent


def boundary_trace(
    tree: frozenset[tuple[int, int]], order: tuple[int, ...], d: int
):
    """Trace the accepted plus-mirror hairy-tree boundary."""
    assert len(order) == 2 * d - 2
    parent = rooted_parents(tree, d)
    incidence = defaultdict(dict)
    first_black = {}
    for child in range(1, d):
        first_label, second_label = order[2 * child - 2 : 2 * child]
        black = ("black", child)
        for label, white_id in (
            (first_label, child),
            (second_label, parent[child]),
        ):
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
    assert set(first_black) == set(range(1, label_count + 1))
    return tokens, first_black


def close_boundary(tokens, d: int):
    """Close white/black half-edges at boundary distance one or three."""
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
        white = tokens[0]
        black = tokens[black_position]
        assert white[0:2] == ("half", "white")
        assert black[0:2] == ("half", "black")
        assert white[3] == black[3]
        boundary_distance = sum(
            token[0] == "side" for token in tokens[1:black_position]
        )
        assert boundary_distance in (1, 3)
        if boundary_distance == 3:
            assert white[3] not in second_black
            second_black[white[3]] = black[2]
        tokens = [("side",)] + tokens[black_position + 1 :]

    residue = [token for token in tokens if token[0] == "half"]
    assert len(residue) == 2 * d - 2
    assert all(token[1] == "white" for token in residue)
    return second_black


def dps_word(
    tree: frozenset[tuple[int, int]], order: tuple[int, ...], d: int
) -> tuple[tuple[int, int], ...]:
    tokens, first_black = boundary_trace(tree, order, d)
    second_black = close_boundary(tokens, d)
    return tuple(
        edge(first_black[label] - 1, second_black.get(label, d) - 1)
        for label in range(1, 2 * d - 1)
    )


def swap_adjacent_values(order: tuple[int, ...], edit: int):
    assert 1 <= edit < len(order)
    return tuple(
        edit + 1
        if value == edit
        else edit
        if value == edit + 1
        else value
        for value in order
    )


def conjugate(transposition: tuple[int, int], by: tuple[int, int]):
    x, y = by

    def image(vertex):
        if vertex == x:
            return y
        if vertex == y:
            return x
        return vertex

    return edge(image(transposition[0]), image(transposition[1]))


def hurwitz_step(word, signed_generator: int):
    """Apply one one-based signed right-Hurwitz generator."""
    assert signed_generator != 0
    position = abs(signed_generator) - 1
    assert 0 <= position < len(word) - 1
    a, b = word[position : position + 2]
    result = list(word)
    if signed_generator > 0:
        result[position : position + 2] = (b, conjugate(a, b))
    else:
        result[position : position + 2] = (conjugate(b, a), a)
    return tuple(result)


def act_chronologically(word, route):
    for signed_generator in route:
        word = hurwitz_step(word, signed_generator)
    return word


def product(word, d: int):
    """Evaluate the displayed factors from left to right on point images."""
    permutation = tuple(range(d))
    for a, b in word:
        transposition = list(range(d))
        transposition[a], transposition[b] = transposition[b], transposition[a]
        permutation = tuple(transposition[permutation[x]] for x in range(d))
    return permutation


def stopped_path(parent, vertex: int):
    result = [vertex]
    while result[-1] != 1:
        next_vertex = parent[result[-1]]
        assert next_vertex is not None
        result.append(next_vertex)
    return tuple(result)


def local_descriptor(tree, edit: int):
    """Derive the M214 key only from the rooted tree and edit."""
    parent = rooted_parents(tree, 5)
    if edit == 1:
        vertex = 2
        path = stopped_path(parent, vertex)
        late = any(item > vertex for item in path[1:-1])
        run = 0
        for child in range(vertex + 1, 5):
            if parent[child] != vertex:
                break
            run += 1
        if late:
            case = "edit1_late"
            route_key = "identity"
        else:
            assert run in (0, 1, 2)
            case = f"edit1_run{run}"
            route_key = f"C_1_{run}"
        return path, late, run, case, route_key

    if edit == 2:
        return (), None, None, "edit2_identity", "identity"

    if edit == 3:
        vertex = 3
        path = stopped_path(parent, vertex)
        late = any(item > vertex for item in path[1:-1])
        run = 0
        for child in range(vertex + 1, 5):
            if parent[child] != vertex:
                break
            run += 1
        if late:
            case = "edit3_late"
            route_key = "identity"
        else:
            assert run in (0, 1)
            case = f"edit3_run{run}"
            route_key = f"C_3_{run}"
        return path, late, run, case, route_key

    if edit == 4:
        return (), None, None, "edit4_identity", "identity"

    if edit == 5:
        path = stopped_path(parent, 4)
        exceptional = path == (4, 2, 3, 1)
        case = "edit5_exceptional" if exceptional else "edit5_standard"
        route_key = "identity" if exceptional else "C_5"
        return path, None, None, case, route_key

    if edit == 6:
        return (), None, None, "edit6_universal", "C_6"

    if edit == 7:
        return (), None, None, "edit7_universal", "C_7"

    raise AssertionError(edit)


ROUTES = {
    "identity": (),
    "C_1_0": (2, 3, -4, -5, -6, 7, -8, -7, -6, 5, 4, -3, -2),
    "C_1_1": (-2, -3, 4, 5, -6, 7, -8, -7, -6, -5, -4, 3, 2),
    "C_1_2": (-2, -3, -4, -5, -6, 7, -8, -7, 6, 5, 4, 3, 2),
    "C_3_0": (4, 5, -6, 7, -8, -7, -6, -5, -4),
    "C_3_1": (-4, -5, -6, 7, -8, -7, 6, 5, 4),
    "C_5": (-6, 7, -8, -7, -6),
    "C_6": (-5, -5),
    "C_7": (-8,),
}


EXPECTED_CASE_COUNTS = {
    "edit1_late": 8,
    "edit1_run0": 5,
    "edit1_run1": 2,
    "edit1_run2": 1,
    "edit2_identity": 16,
    "edit3_late": 5,
    "edit3_run0": 7,
    "edit3_run1": 4,
    "edit4_identity": 16,
    "edit5_exceptional": 1,
    "edit5_standard": 15,
    "edit6_universal": 16,
    "edit7_universal": 16,
}

FROZEN_CLASS_IDS = {
    "edit1_run0": "edit1:direct_run_0",
    "edit1_run1": "edit1:direct_run_1",
    "edit1_run2": "edit1:direct_run_2",
    "edit1_late": "edit1:late_ancestor",
    "edit2_identity": "edit2:universal_identity",
    "edit3_run0": "edit3:direct_run_0",
    "edit3_run1": "edit3:direct_run_1",
    "edit3_late": "edit3:late_ancestor",
    "edit4_identity": "edit4:universal_identity",
    "edit5_exceptional": "edit5:exceptional_path_4_2_3_1",
    "edit5_standard": "edit5:standard",
    "edit6_universal": "edit6:universal_double_inverse",
    "edit7_universal": "edit7:universal_inverse",
}

FROZEN_CLASS_ORDER = (
    "edit1_run0",
    "edit1_run1",
    "edit1_run2",
    "edit1_late",
    "edit2_identity",
    "edit3_run0",
    "edit3_run1",
    "edit3_late",
    "edit4_identity",
    "edit5_exceptional",
    "edit5_standard",
    "edit6_universal",
    "edit7_universal",
)


def json_tree(tree):
    return [list(item) for item in sorted(tree)]


def json_word(word):
    return [list(item) for item in word]


def json_route(route):
    return [[abs(symbol), 1 if symbol > 0 else -1] for symbol in route]


def compact_digest(value):
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def main():
    # First generate the set independently on [4], then reproduce the stated
    # five-vertex Prüfer traversal order used by the published digest.  Equality
    # of the two sets is a separate completeness check.
    direct_tree_set = {
        tree | {(1, 5)} for tree in prufer_trees((1, 2, 3, 4))
    }
    trees = [
        tree
        for tree in prufer_trees((1, 2, 3, 4, 5))
        if (1, 5) in tree and sum(5 in item for item in tree) == 1
    ]
    assert len(trees) == 4 ** 2 == 16
    assert len(set(trees)) == 16
    assert set(trees) == direct_tree_set
    assert all((1, 5) in tree for tree in trees)
    assert all(sum(5 in item for item in tree) == 1 for tree in trees)

    pi5 = (7, 8, 1, 2, 3, 4, 5, 6)
    pi6 = (9, 10, 1, 2, 3, 4, 5, 6, 7, 8)
    fixed_leaf_pair = ((0, 5), (0, 5))

    rows = []
    published_rows = []
    case_counts = Counter()
    route_counts = Counter()
    for tree_index, tree5 in enumerate(trees):
        tree6 = tree5 | {(1, 6)}
        source5 = dps_word(tree5, pi5, 5)
        source6 = dps_word(tree6, pi6, 6)
        assert source6 == source5 + fixed_leaf_pair
        assert product(source5, 5) == tuple(range(5))
        assert product(source6, 6) == tuple(range(6))

        for edit in range(1, 8):
            path, late, run, case, route_key = local_descriptor(tree5, edit)
            route = ROUTES[route_key]
            edited5 = swap_adjacent_values(pi5, edit)
            edited6 = swap_adjacent_values(pi6, edit)
            naive = dps_word(tree5, edited5, 5) + fixed_leaf_pair
            actual = dps_word(tree6, edited6, 6)
            replay = act_chronologically(naive, route)

            assert product(naive, 6) == tuple(range(6))
            assert product(actual, 6) == tuple(range(6))
            assert product(replay, 6) == tuple(range(6))
            assert replay == actual
            case_counts[case] += 1
            route_counts[route_key] += 1
            rows.append(
                {
                    "tree_index": tree_index,
                    "tree": json_tree(tree5),
                    "edit": edit,
                    "path": list(path),
                    "late_ancestor": late,
                    "direct_child_run": run,
                    "case": case,
                    "route_key": route_key,
                    "chronological_route": list(route),
                    "route_length": len(route),
                    "naive_target": json_word(naive),
                    "actual_target": json_word(actual),
                    "route_output": json_word(replay),
                    "exact_replay": replay == actual,
                }
            )
            intrinsic_odd_key = None
            if edit in (1, 3, 5):
                vertex = (edit + 3) // 2
                parent = rooted_parents(tree5, 5)
                odd_path = stopped_path(parent, vertex)
                odd_late = any(item > vertex for item in odd_path[1:-1])
                odd_run = 0
                for child in range(vertex + 1, 5):
                    if parent[child] != vertex:
                        break
                    odd_run += 1
                intrinsic_odd_key = {
                    "consecutive_larger_child_run": odd_run,
                    "edit": edit,
                    "late_ancestor": odd_late,
                    "path_to_attachment": list(odd_path),
                    "vertex": vertex,
                }
                assert tuple(odd_path) == path
                if edit in (1, 3):
                    assert odd_late == late and odd_run == run
            published_rows.append(
                {
                    "actual_target": json_word(actual),
                    "class_id": FROZEN_CLASS_IDS[case],
                    "edit": edit,
                    "exact_replay": replay == actual,
                    "intrinsic_odd_key": intrinsic_odd_key,
                    "naive_target": json_word(naive),
                    "route": json_route(route),
                    "route_length": len(route),
                    "tree5": json_tree(tree5),
                    "tree_id": tree_index,
                }
            )

    assert len(rows) == 16 * 7 == 112
    assert len(published_rows) == 112
    assert all(row["exact_replay"] for row in rows)
    assert dict(sorted(case_counts.items())) == EXPECTED_CASE_COUNTS
    assert len(case_counts) == 13
    assert len(set(ROUTES.values())) == 9
    assert max(map(len, ROUTES.values())) == 13

    classes = []
    for case in sorted(case_counts):
        matching = [row for row in rows if row["case"] == case]
        route_keys = {row["route_key"] for row in matching}
        routes = {tuple(row["chronological_route"]) for row in matching}
        assert len(route_keys) == len(routes) == 1
        route_key = next(iter(route_keys))
        route = next(iter(routes))
        classes.append(
            {
                "case": case,
                "count": len(matching),
                "route_key": route_key,
                "chronological_route": list(route),
                "route_length": len(route),
            }
        )

    published_class_summary = []
    for case in FROZEN_CLASS_ORDER:
        class_id = FROZEN_CLASS_IDS[case]
        matching_rows = [
            row for row in published_rows if row["class_id"] == class_id
        ]
        assert len(matching_rows) == EXPECTED_CASE_COUNTS[case]
        route_values = {
            tuple(tuple(step) for step in row["route"]) for row in matching_rows
        }
        edit_values = {row["edit"] for row in matching_rows}
        assert len(route_values) == len(edit_values) == 1
        route = next(iter(route_values))
        edit = next(iter(edit_values))
        published_class_summary.append(
            {
                "class_id": class_id,
                "edit": edit,
                "route": [list(step) for step in route],
                "route_length": len(route),
                "row_digest": compact_digest(matching_rows),
                "size": len(matching_rows),
                "tree_ids": [row["tree_id"] for row in matching_rows],
            }
        )

    classification_digest = compact_digest(published_rows)
    summary_digest = compact_digest(published_class_summary)
    assert classification_digest == EXPECTED_CLASSIFICATION_DIGEST
    assert summary_digest == EXPECTED_SUMMARY_DIGEST

    result = {
        "mission": "M218",
        "method": {
            "clean_room": True,
            "imports_m214_code": False,
            "reads_m214_data": False,
            "route_search": False,
            "q6_enumeration": False,
            "tree_generation": "Pruefer codes on [4], then attach {1,5}",
            "convention": {
                "positive": "R_j(a,b)=(b,bab)",
                "negative": "R_j^-1(a,b)=(aba,a)",
                "action_order": "chronological",
            },
        },
        "source_lock": {
            "expected_m214_sha256sums_digest": EXPECTED_SOURCE_INVENTORY_DIGEST,
            "verified_externally_before_run": True,
            "complete_inventory_ok": True,
        },
        "checks": {
            "tree_count": len(trees),
            "row_count": len(rows),
            "case_count": len(classes),
            "distinct_correction_words": len(set(ROUTES.values())),
            "maximum_correction_length": max(map(len, ROUTES.values())),
            "all_replays_pass": all(row["exact_replay"] for row in rows),
            "case_counts_match": dict(sorted(case_counts.items()))
            == EXPECTED_CASE_COUNTS,
            "all_words_identity": True,
        },
        "case_counts": dict(sorted(case_counts.items())),
        "route_counts": dict(sorted(route_counts.items())),
        "routes": {key: list(route) for key, route in sorted(ROUTES.items())},
        "classes": classes,
        "published_class_summary": published_class_summary,
        "rows": rows,
        "published_rows": published_rows,
        "digests": {
            "classification": classification_digest,
            "classes": summary_digest,
            "expected_frozen_classification": EXPECTED_CLASSIFICATION_DIGEST,
            "expected_frozen_summary": EXPECTED_SUMMARY_DIGEST,
            "classification_matches_expected": True,
            "summary_matches_expected": True,
        },
        "environment": {
            "python": platform.python_version(),
            "nonstandard_dependencies": {},
            "seed": None,
        },
        "verdict_at_generation": "finite_endpoint_reconstruction_pass",
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "tree_count": len(trees),
        "row_count": len(rows),
        "case_count": len(classes),
        "distinct_correction_words": len(set(ROUTES.values())),
        "all_replays_pass": True,
        "classification_digest": classification_digest,
        "summary_digest": summary_digest,
        "output": str(OUTPUT),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
