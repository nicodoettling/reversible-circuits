#!/usr/bin/env python3
"""Independent immutable referee for M208's finite d5->d6 theorem.

No M208 code is imported.  The checker independently implements the rooted
DPS closure and signed Hurwitz action, completes its named/template results,
and only then reads frozen M208 JSON for comparison.  No Q6 graph or route
search is constructed.
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
RUN_ROOT = HERE.parent.parent
M208 = RUN_ROOT / "cycle-51" / "mission-M208-all-d-route-rooted-recursion"
M196 = RUN_ROOT / "cycle-46" / "mission-M196-q5-target-pair-direct-orbits"
M200 = RUN_ROOT / "cycle-47" / "mission-M200-d5-perfect-matching-route-coverage"


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


def parents(tree, root):
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
    assert len(parent) == root
    return parent


def boundary_trace(tree, order, d):
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
        half_positions = [i for i, token in enumerate(tokens) if token[0] == "half"]
        chosen = None
        for offset, white_position in enumerate(half_positions):
            black_position = half_positions[(offset + 1) % len(half_positions)]
            if tokens[white_position][1] == "w" and tokens[black_position][1] == "b":
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
            second_black[white[3]] = black[2]
        tokens = [("side",)] + tokens[black_position + 1 :]
    residue = [token for token in tokens if token[0] == "half"]
    assert len(residue) == 2 * d - 2 and all(token[1] == "w" for token in residue)
    return second_black


def dps_word(tree, order, d):
    tokens, first_black = boundary_trace(tree, order, d)
    second_black = close_boundary(tokens, d)
    return tuple(
        edge(first_black[label] - 1, second_black.get(label, d) - 1)
        for label in range(1, 2 * d - 1)
    )


def swap_values(order, edit):
    return tuple(
        edit + 1 if value == edit
        else edit if value == edit + 1
        else value
        for value in order
    )


def explicit_source(d, pattern):
    third = (1, 3) if pattern == 0 else (0, 3)
    result = tuple(item for item in ((0, 1), (0, 2), third) for _ in range(2))
    return result + tuple((0, label) for label in range(4, d) for _ in range(2))


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


def act_signed_symbols(word, symbols):
    for symbol in symbols:
        word = hurwitz(word, abs(symbol) - 1, 1 if symbol > 0 else -1)
    return word


def permutation_product(word, d):
    permutation = list(range(d))
    for a, b in word:
        permutation[a], permutation[b] = permutation[b], permutation[a]
    return tuple(permutation)


def relabel(word, permutation):
    return tuple(edge(permutation[a], permutation[b]) for a, b in word)


def canonical(word, d):
    return min(relabel(word, permutation) for permutation in itertools.permutations(range(d)))


def json_word(word):
    return [list(item) for item in word]


def json_route(route):
    return [[position + 1, sign] for position, sign in route]


def digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


ROUTES = {
    1: (
        (1, 1), (2, 1), (3, -1), (4, -1),
        (5, -1), (6, 1), (7, -1), (6, -1), (5, -1),
        (4, 1), (3, 1), (2, -1), (1, -1),
    ),
    2: (),
    3: (
        (3, 1), (4, 1), (5, -1), (6, 1), (7, -1),
        (6, -1), (5, -1), (4, -1), (3, -1),
    ),
    4: (),
    5: ((5, -1), (6, 1), (7, -1), (6, -1), (5, -1)),
    6: ((4, -1), (4, -1)),
    7: ((7, -1),),
}


def main():
    pi5 = (7, 8, 1, 2, 3, 4, 5, 6)
    pi6 = (9, 10, 1, 2, 3, 4, 5, 6, 7, 8)
    trees5 = {
        0: frozenset({(1, 2), (1, 3), (1, 5), (2, 4)}),
        1: frozenset({(1, 2), (1, 3), (1, 4), (1, 5)}),
    }
    trees6 = {pattern: tree | {(1, 6)} for pattern, tree in trees5.items()}

    descriptors = []
    for pattern in (0, 1):
        source5 = dps_word(trees5[pattern], pi5, 5)
        source6 = dps_word(trees6[pattern], pi6, 6)
        assert source5 == explicit_source(5, pattern)
        assert source6 == explicit_source(6, pattern) == source5 + ((0, 5), (0, 5))
        assert permutation_product(source5, 5) == tuple(range(5))
        assert permutation_product(source6, 6) == tuple(range(6))
        descriptors.append({
            "pattern": pattern,
            "tree5": [list(item) for item in sorted(trees5[pattern])],
            "tree6": [list(item) for item in sorted(trees6[pattern])],
            "pi5": list(pi5),
            "pi6": list(pi6),
        })

    targets5 = {}
    targets6 = {}
    certificates = []
    for edit in range(1, 8):
        pattern_rows = []
        for pattern in (0, 1):
            target5 = dps_word(trees5[pattern], swap_values(pi5, edit), 5)
            target6 = dps_word(trees6[pattern], swap_values(pi6, edit), 6)
            naive = target5 + ((0, 5), (0, 5))
            replay = act(naive, ROUTES[edit])
            assert replay == target6
            assert permutation_product(target5, 5) == tuple(range(5))
            assert permutation_product(target6, 6) == tuple(range(6))
            targets5[pattern, edit] = target5
            targets6[pattern, edit] = target6
            pattern_rows.append({
                "pattern": pattern,
                "naive_target": json_word(naive),
                "actual_target": json_word(target6),
                "exact_replay": True,
            })
        certificates.append({
            "edit": edit,
            "chronological_route": json_route(ROUTES[edit]),
            "route_length": len(ROUTES[edit]),
            "generator_support": sorted({position + 1 for position, _ in ROUTES[edit]}),
            "patterns": pattern_rows,
        })

    certificate_digest = digest(certificates)
    route_lengths = [len(ROUTES[edit]) for edit in range(1, 8)]

    template_trees = [
        tree for tree in prufer_trees(5)
        if (1, 5) in tree and sum(5 in item for item in tree) == 1
    ]
    assert len(template_trees) == 16
    failures = []
    failures_by_edit = Counter()
    for tree_index, tree5 in enumerate(template_trees):
        tree6 = tree5 | {(1, 6)}
        for edit in range(1, 8):
            naive = dps_word(tree5, swap_values(pi5, edit), 5) + ((0, 5), (0, 5))
            actual = dps_word(tree6, swap_values(pi6, edit), 6)
            output = act(naive, ROUTES[edit])
            if output != actual:
                failures_by_edit[edit] += 1
                failures.append({
                    "tree_index": tree_index,
                    "tree5": [list(item) for item in sorted(tree5)],
                    "edit": edit,
                    "naive_target": json_word(naive),
                    "actual_target": json_word(actual),
                    "route_output": json_word(output),
                })
    assert failures

    # Independent d5 quotient-certificate replay and composition audit.
    m200 = json.loads((M200 / "incidence_table.json").read_text())
    selected_rows = sorted(
        (row for row in m200["root_pair_rows"] if row["selected_h_orbit_roots"] == [4, 4]),
        key=lambda row: row["edit"],
    )
    assert [row["edit"] for row in selected_rows] == list(range(1, 8))
    assert all(row["covered_by_m196_theorem"] for row in selected_rows)
    m196 = json.loads((M196 / "targeted_results.json").read_text())
    route_by_id = {row["target_id"]: row for row in m196["original_target_certificates"]}
    composition_rows = []
    exact_stored_physical_edits = []
    quotient_only_stored_edits = []
    sources5 = [explicit_source(5, pattern) for pattern in (0, 1)]
    sources6 = [explicit_source(6, pattern) for pattern in (0, 1)]
    for incidence in selected_rows:
        edit = incidence["edit"]
        stored = route_by_id[incidence["m196_target_id"]]
        assert stored["full_word"] is not None
        reached5 = [act_signed_symbols(source, stored["full_word"]) for source in sources5]
        wanted5 = [targets5[pattern, edit] for pattern in (0, 1)]
        quotient_hits = [canonical(reached5[p], 5) == canonical(wanted5[p], 5) for p in (0, 1)]
        assert all(quotient_hits)
        exact_physical = reached5 == wanted5
        if exact_physical:
            exact_stored_physical_edits.append(edit)
            reached6_naive = [act_signed_symbols(source, stored["full_word"]) for source in sources6]
            assert reached6_naive == [wanted + ((0, 5), (0, 5)) for wanted in wanted5]
            composite = [act(word, ROUTES[edit]) for word in reached6_naive]
            assert composite == [targets6[pattern, edit] for pattern in (0, 1)]
        else:
            quotient_only_stored_edits.append(edit)
        composition_rows.append({
            "edit": edit,
            "m196_target_id": incidence["m196_target_id"],
            "stored_quotient_word": stored["full_word"],
            "stored_quotient_length": len(stored["full_word"]),
            "stored_word_hits_both_target_quotient_classes": all(quotient_hits),
            "stored_word_hits_fixed_physical_targets": exact_physical,
            "literal_stored_word_plus_correction_replay": exact_physical,
        })

    # Only now compare with frozen M208 result data.
    frozen = json.loads((M208 / "rooted_extension_results.json").read_text())
    our_first = failures[0]
    frozen_template = frozen["template_falsification"]
    comparison = {
        "route_lengths": route_lengths == frozen["named_pattern_route_lengths"],
        "maximum_correction_length": max(route_lengths) == frozen["maximum_correction_length"],
        "certificate_digest": certificate_digest == frozen["named_certificate_digest"],
        "certificate_rows": certificates == frozen["named_pattern_certificates"],
        "descriptor_extension": descriptors == frozen["descriptor_extension"],
        "template_tree_count": len(template_trees) == frozen_template["trees"],
        "template_check_count": len(template_trees) * 7 == frozen_template["tree_edit_checks"],
        "template_failure_count": len(failures) == frozen_template["known_route_failures"],
        "template_failure_histogram": {
            str(key): value for key, value in sorted(failures_by_edit.items())
        } == frozen_template["known_route_failures_by_edit"],
        "first_template_failure": our_first == frozen_template["first_failure"],
    }

    result = {
        "experiment": "M212 fresh immutable referee of M208",
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "scope": "finite named d5->d6 correction; no M208 imports and no Q6 enumeration",
        "descriptor_extension": descriptors,
        "route_lengths": route_lengths,
        "certificate_digest": certificate_digest,
        "all_fourteen_named_replays": all(
            row["exact_replay"] for certificate in certificates for row in certificate["patterns"]
        ),
        "template_audit": {
            "trees": len(template_trees),
            "checks": len(template_trees) * 7,
            "known_route_failures": len(failures),
            "failure_histogram": {
                str(key): value for key, value in sorted(failures_by_edit.items())
            },
            "first_failure": our_first,
        },
        "d5_composition_audit": {
            "distinguished_incidence_rows": len(selected_rows),
            "all_stored_words_hit_target_quotient_classes": all(
                row["stored_word_hits_both_target_quotient_classes"] for row in composition_rows
            ),
            "stored_words_hit_fixed_physical_targets_edits": exact_stored_physical_edits,
            "stored_words_need_fixed_endpoint_voltage_correction_edits": quotient_only_stored_edits,
            "rows": composition_rows,
            "formal_composition": (
                "For any accepted fixed-physical-endpoint d5 braid B_i, its generators "
                "act on positions 1..8 and leave the appended square fixed; C_i then "
                "reaches the actual d6 endpoint. M200/M202 supply existence of B_i "
                "qualitatively via full voltage, without a corrected length."
            ),
        },
        "frozen_comparison": comparison,
        "numbered_objections": [],
        "verdict": "ACCEPT M208 AS FROZEN",
        "scope_boundary": (
            "Finite two-pattern d5->d6 correction only. The 21 failures refute only "
            "the archived schedule table's universality; no general d6, every-color, "
            "all-d, voltage-length, polynomial, gap, mixing, or Terminal claim follows."
        ),
    }
    assert result["all_fourteen_named_replays"]
    assert all(comparison.values())
    assert result["template_audit"]["known_route_failures"] == 21
    assert result["template_audit"]["failure_histogram"] == {"1": 11, "3": 9, "5": 1}
    assert exact_stored_physical_edits == [1, 2, 4, 6]
    assert quotient_only_stored_edits == [3, 5, 7]

    (HERE / "referee_results.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps({
        "verdict": result["verdict"],
        "route_lengths": route_lengths,
        "certificate_digest": certificate_digest,
        "all_fourteen_named_replays": result["all_fourteen_named_replays"],
        "template_audit": result["template_audit"],
        "d5_composition_audit": result["d5_composition_audit"],
        "frozen_comparison": comparison,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

