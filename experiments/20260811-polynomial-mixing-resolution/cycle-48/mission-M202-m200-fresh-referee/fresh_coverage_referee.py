#!/usr/bin/env python3
"""Clean-room exact referee of M200's d=5 incidence/coverage theorem.

This imports no M200 or predecessor Python.  It reconstructs the finite Q5
action and rooted DPS targets from definitions, then replays all M196 routes.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from array import array
from collections import Counter, defaultdict, deque
from functools import cache
from pathlib import Path


D = 5
N = 8400
SYMBOLS = tuple(range(1, 8)) + tuple(range(-1, -8, -1))
LABELINGS = tuple(itertools.permutations(range(D)))
IDENTITY = tuple(range(D))


def ordered_edge(a, b):
    return (a, b) if a < b else (b, a)


def relabel_word(word, permutation):
    return tuple(ordered_edge(permutation[a], permutation[b]) for a, b in word)


@cache
def canonical(word):
    return min(relabel_word(word, permutation) for permutation in LABELINGS)


def conjugate_by_edge(target, acting):
    x, y = acting

    def image(label):
        return y if label == x else x if label == y else label

    return ordered_edge(image(target[0]), image(target[1]))


def hurwitz(word, symbol):
    position = abs(symbol) - 1
    left, right = word[position], word[position + 1]
    output = list(word)
    if symbol > 0:
        output[position : position + 2] = (
            right, conjugate_by_edge(left, right)
        )
    else:
        output[position : position + 2] = (
            conjugate_by_edge(right, left), left
        )
    return tuple(output)


def q5_reconstruction():
    # M181 order: pattern 0 gives V, pattern 1 gives U.
    pattern_zero = (
        (0, 1), (0, 1), (0, 2), (0, 2),
        (1, 3), (1, 3), (0, 4), (0, 4),
    )
    pattern_one = (
        (0, 1), (0, 1), (0, 2), (0, 2),
        (0, 3), (0, 3), (0, 4), (0, 4),
    )
    sources = canonical(pattern_zero), canonical(pattern_one)
    reached = {sources[0]}
    queue = deque([sources[0]])
    while queue:
        word = queue.popleft()
        for symbol in SYMBOLS:
            neighbor = canonical(hurwitz(word, symbol))
            if neighbor not in reached:
                reached.add(neighbor)
                queue.append(neighbor)
    states = tuple(sorted(reached))
    index = {word: state_id for state_id, word in enumerate(states)}
    action_rows = [array("H", (
        index[canonical(hurwitz(word, symbol))] for word in states
    )) for symbol in SYMBOLS]
    return sources, states, index, action_rows


def prufer_trees():
    for code in itertools.product(range(1, D + 1), repeat=D - 2):
        degrees = [0] + [1] * D
        for vertex in code:
            degrees[vertex] += 1
        edges = []
        for vertex in code:
            leaf = min(x for x in range(1, D + 1) if degrees[x] == 1)
            edges.append(ordered_edge(leaf, vertex))
            degrees[leaf] -= 1
            degrees[vertex] -= 1
        last = [x for x in range(1, D + 1) if degrees[x] == 1]
        edges.append(ordered_edge(*last))
        yield frozenset(edges)


def rooted_parents(tree):
    adjacency = {vertex: [] for vertex in range(1, D + 1)}
    for a, b in tree:
        adjacency[a].append(b)
        adjacency[b].append(a)
    parent = {D: 0}
    stack = [D]
    while stack:
        vertex = stack.pop()
        for neighbor in adjacency[vertex]:
            if neighbor not in parent:
                parent[neighbor] = vertex
                stack.append(neighbor)
    assert len(parent) == D
    return parent


def dps_boundary(tree, ordering):
    parent = rooted_parents(tree)
    incidence = defaultdict(dict)
    first_black = {}
    for child in range(1, D):
        labels = ordering[2 * child - 2 : 2 * child]
        black = ("b", child)
        for label, white_id in ((labels[0], child), (labels[1], parent[child])):
            white = ("w", white_id)
            incidence[black][label] = white
            incidence[white][label] = black
            first_black[label] = child

    modulus = 2 * D - 2
    start = (("w", 1), 1)
    state = start
    visited = set()
    tokens = []
    while state not in visited:
        visited.add(state)
        vertex, incoming = state
        direction = 1 if vertex[0] == "w" else -1
        label = 1 + ((incoming - 1 + direction) % modulus)
        if label in incidence[vertex]:
            tokens.append(("side",))
            state = (incidence[vertex][label], label)
        else:
            tokens.append(("half", vertex[0], vertex[1], label))
            state = (vertex, label)
    assert state == start and len(tokens) == (2 * D - 1) * modulus
    return tokens, first_black


def dps_close(tokens):
    tokens = list(tokens)
    second_black = {}
    while True:
        positions = [j for j, token in enumerate(tokens) if token[0] == "half"]
        pair = None
        for offset, white_position in enumerate(positions):
            black_position = positions[(offset + 1) % len(positions)]
            if (
                tokens[white_position][1] == "w"
                and tokens[black_position][1] == "b"
            ):
                pair = white_position, black_position
                break
        if pair is None:
            break
        white_position, black_position = pair
        tokens = tokens[white_position:] + tokens[:white_position]
        black_position = (black_position - white_position) % len(tokens)
        white, black = tokens[0], tokens[black_position]
        assert white[3] == black[3]
        separation = sum(token[0] == "side" for token in tokens[1:black_position])
        assert separation in (1, 3)
        if separation == 3:
            second_black[white[3]] = black[2]
        tokens = [("side",)] + tokens[black_position + 1 :]
    residue = [token for token in tokens if token[0] == "half"]
    assert len(residue) == 2 * D - 2
    assert all(token[1] == "w" for token in residue)
    return second_black


def dps_word(tree, ordering):
    tokens, first_black = dps_boundary(tree, ordering)
    second_black = dps_close(tokens)
    result = []
    for label in range(1, 2 * D - 1):
        left = first_black[label]
        right = second_black.get(label, D)
        assert left != right
        result.append(ordered_edge(left - 1, right - 1))
    return tuple(result)


def compatible_orderings(word):
    root = D - 1
    choices = [tuple(label for label in edge if label != root) for edge in word]
    for assigned in itertools.product(*choices):
        if any(assigned.count(vertex) != 2 for vertex in range(D - 1)):
            continue
        slots = {
            vertex: [position + 1 for position, value in enumerate(assigned)
                     if value == vertex]
            for vertex in range(D - 1)
        }
        for orientations in itertools.product((0, 1), repeat=D - 1):
            ordering = []
            for vertex in range(D - 1):
                pair = slots[vertex]
                ordering.extend(pair if orientations[vertex] == 0 else reversed(pair))
            yield tuple(ordering)


def inverse_dps(word, trees):
    for ordering in compatible_orderings(word):
        for tree in trees:
            if dps_word(tree, ordering) == word:
                return tree, ordering
    raise AssertionError("rooted DPS inverse failed")


def swap_values(ordering, edit):
    return tuple(
        edit + 1 if value == edit
        else edit if value == edit + 1
        else value
        for value in ordering
    )


def root_swap(root):
    permutation = list(IDENTITY)
    permutation[root], permutation[D - 1] = (
        permutation[D - 1], permutation[root]
    )
    return tuple(permutation)


def rebuild_incidences(sources, index):
    trees = tuple(prufer_trees())
    descriptors = {}
    for coordinate, source in enumerate(sources):
        for root in range(D):
            physical = relabel_word(source, root_swap(root))
            descriptors[coordinate, root] = inverse_dps(physical, trees)

    coordinate_targets = {}
    for edit in range(1, 8):
        for coordinate in range(2):
            for root in range(D):
                tree, ordering = descriptors[coordinate, root]
                target = canonical(dps_word(tree, swap_values(ordering, edit)))
                coordinate_targets[edit, coordinate, root] = index[target]

    occurrences = defaultdict(list)
    for edit in range(1, 8):
        for root_zero in range(D):
            for root_one in range(D):
                target_ids = (
                    coordinate_targets[edit, 0, root_zero],
                    coordinate_targets[edit, 1, root_one],
                )
                assert target_ids[0] != target_ids[1]
                occurrences[target_ids].append({
                    "edit": edit,
                    "roots": [root_zero, root_one],
                })
    sorted_rows = []
    for target_id, (target_ids, rows) in enumerate(sorted(occurrences.items())):
        sorted_rows.append({
            "target_id": target_id,
            "target_ids": list(target_ids),
            "occurrences": sorted(rows, key=lambda row: (row["edit"], row["roots"])),
        })
    return descriptors, coordinate_targets, sorted_rows


def apply_pair(pair, word, action):
    first, second = pair
    for symbol in word:
        row = action[symbol]
        first, second = row[first], row[second]
    return [first, second]


def route_digest(word):
    return hashlib.sha256(
        json.dumps(word, separators=(",", ":")).encode()
    ).hexdigest()


def audit(args):
    objections = []

    def require(condition, text):
        if not condition:
            objections.append(text)

    q5_bytes = args.q5_action.read_bytes()
    q5 = json.loads(q5_bytes)
    m181 = json.loads(args.m181_results.read_text())
    m196_bytes = args.m196_results.read_bytes()
    m196 = json.loads(m196_bytes)
    frozen_m200_bytes = args.m200_table.read_bytes()
    frozen_m200 = json.loads(frozen_m200_bytes)

    sources, states, index, action_rows = q5_reconstruction()
    action = dict(zip(SYMBOLS, action_rows))
    source_ids = [index[source] for source in sources]
    action_digest = hashlib.sha256(
        b"".join(row.tobytes() for row in action_rows)
    ).hexdigest()
    stored_rows = [array("H", row) for row in q5["action_rows"]]
    require(len(states) == N, "O01: clean Q5 orbit size is not 8400")
    require(source_ids == [16, 0] == q5["source_ids"],
            "O02: M181 pattern source IDs do not equal (16,0)")
    require(all(left == right for left, right in zip(action_rows, stored_rows)),
            "O03: clean action rows differ from frozen Q5")
    require(action_digest == q5["action_sha256"] == m196["action_sha256"],
            "O04: action digest mismatch")
    inverse_pairs = all(
        action[-symbol][action[symbol][point]] == point
        and action[symbol][action[-symbol][point]] == point
        for symbol in range(1, 8) for point in range(N)
    )
    require(inverse_pairs, "O05: signed generator inverse failure")

    descriptors, coordinate_targets, target_rows = rebuild_incidences(sources, index)
    require(len(descriptors) == 10, "O06: rooted descriptor count is not 10")
    require(len(coordinate_targets) == 70, "O07: root-edge row count is not 70")
    require(len(target_rows) == 54, "O08: deduplicated target count is not 54")
    occurrence_count = sum(len(row["occurrences"]) for row in target_rows)
    require(occurrence_count == 175, "O09: root-pair occurrence count is not 175")
    expected_keys = {
        (edit, root_zero, root_one)
        for edit in range(1, 8)
        for root_zero in range(5)
        for root_one in range(5)
    }
    key_lookup = {}
    for row in target_rows:
        for occurrence in row["occurrences"]:
            key = (occurrence["edit"], *occurrence["roots"])
            require(key not in key_lookup, f"O10: duplicate occurrence key {key}")
            key_lookup[key] = (row["target_id"], row["target_ids"])
    require(set(key_lookup) == expected_keys, "O11: occurrence-key inventory mismatch")
    require(target_rows == q5["target_rows"],
            "O12: clean target rows differ from frozen Q5 inventory")

    # Independent full route replay, one certificate per deduplicated class.
    certificate_by_id = {}
    route_lengths = []
    route_digests = {}
    for certificate in m196["original_target_certificates"]:
        target_id = certificate["target_id"]
        require(target_id not in certificate_by_id,
                f"O13: duplicate route target ID {target_id}")
        certificate_by_id[target_id] = certificate
        require(certificate["status"] == "positive",
                f"O14: target {target_id} is not positive")
        require(certificate["target_ids"] == target_rows[target_id]["target_ids"],
                f"O15: target IDs mismatch for target {target_id}")
        require(apply_pair(source_ids, certificate["full_word"], action)
                == certificate["target_ids"],
                f"O16: route replay fails for target {target_id}")
        route_lengths.append(len(certificate["full_word"]))
        route_digests[target_id] = route_digest(certificate["full_word"])
    require(set(certificate_by_id) == set(range(54)),
            "O17: route certificate inventory is not exactly 0..53")
    require(max(route_lengths, default=-1) == 22,
            "O18: maximum quotient certificate length is not 22")

    # Reconstruct the 70 and 175 comparison rows independently.
    clean_edge_rows = []
    for edit in range(1, 8):
        for coordinate in range(2):
            for root in range(5):
                clean_edge_rows.append({
                    "edit": edit,
                    "coordinate": coordinate,
                    "left_source_q5_id": source_ids[coordinate],
                    "h_orbit_root": root,
                    "matched_target_q5_id": coordinate_targets[edit, coordinate, root],
                })
    require(clean_edge_rows == frozen_m200["root_edge_rows"],
            "O19: M200 root-edge rows differ from clean reconstruction")

    clean_pair_rows = []
    for edit, root_zero, root_one in sorted(expected_keys):
        target_id, target_ids = key_lookup[edit, root_zero, root_one]
        clean_pair_rows.append({
            "edit": edit,
            "source_q5_ids": source_ids,
            "selected_h_orbit_roots": [root_zero, root_one],
            "matched_target_q5_ids": target_ids,
            "m196_target_id": target_id,
            "target_class_occurrences": len(target_rows[target_id]["occurrences"]),
            "covered_by_m196_theorem": True,
            "route_certificate_target_id": target_id,
            "route_length": len(certificate_by_id[target_id]["full_word"]),
            "route_word_sha256": route_digests[target_id],
        })
    require(clean_pair_rows == frozen_m200["root_pair_rows"],
            "O20: M200 simultaneous root-pair rows differ from reconstruction")

    # Every edit/color after normalization has one fixed first root and any
    # of five second roots; an actual coloring chooses a permutation.
    clean_color_rows = []
    for edit in range(1, 8):
        for color in range(5):
            possibilities = []
            for second_root in range(5):
                target_id, target_ids = key_lookup[edit, color, second_root]
                possibilities.append({
                    "second_source_root": second_root,
                    "matched_target_q5_ids": target_ids,
                    "m196_target_id": target_id,
                    "route_length": len(certificate_by_id[target_id]["full_word"]),
                })
            clean_color_rows.append({
                "edit": edit,
                "normalized_color": color,
                "first_source_root": color,
                "second_source_root": "sigma_edit(color)",
                "sigma_edit_constraint": "permutation of 0..4",
                "all_possible_matched_targets": possibilities,
                "all_possibilities_covered": True,
                "full_voltage_source": True,
            })
    require(clean_color_rows == frozen_m200["normalized_color_rows"],
            "O21: M200 normalized arbitrary-color rows mismatch")

    # Audit the exact M181 source row, including the even-width quotient.
    d5_rows = [row for row in m181["family_rows"] if row["d"] == 5]
    require(len(d5_rows) == 1, "O22: M181 has no unique d=5 family row")
    d5_row = d5_rows[0] if d5_rows else {}
    require(d5_row.get("patterns") == [[0], [1]]
            and d5_row.get("width") == 2
            and d5_row.get("voltage_basis_representatives") == [[0, 1]],
            "O23: M181 d=5 width-two source/voltage data mismatch")
    # W2=F2^2/<(1,1)> has dimension one; (0,1) is not diagonal.
    voltage_is_full = [0, 1] not in ([0, 0], [1, 1])
    require(voltage_is_full, "O24: M181 voltage representative is zero in W2")

    counts = frozen_m200["counts"]
    require(counts == {
        "colors_per_edit": 5,
        "covered_root_pair_incidences": 175,
        "distinct_m196_target_classes": 54,
        "edits": 7,
        "normalized_color_rows": 35,
        "relevant_left_source_orbits": 2,
        "root_edge_rows": 70,
        "root_pair_incidences": 175,
        "uncovered_root_pair_incidences": 0,
    }, "O25: M200 aggregate incidence counts mismatch")
    require(frozen_m200["uncovered_target_classes"] == [],
            "O26: M200 records an uncovered target class")
    theorem = frozen_m200["exact_theorem"]
    require(theorem.get("every_d5_matching_color_has_full_voltage_source_pair") is True,
            "O27: full-voltage color theorem field false")
    require(theorem.get("every_matched_quotient_target_pair_is_m196_reachable") is True,
            "O28: quotient reachability theorem field false")
    require(theorem.get("m181_conditional_endpoint_hypothesis_discharged") is True,
            "O29: conditional endpoint hypothesis not marked discharged")
    require(theorem.get("qualitative_zero_relative_voltage_endpoint_route_exists") is True,
            "O30: qualitative endpoint theorem field false")
    require(theorem.get("quantitative_zero_voltage_route_length_claim") is False,
            "O31: M200 improperly asserts quantitative corrected-route length")

    result_digest = hashlib.sha256(m196_bytes).hexdigest()
    require(result_digest ==
            "e40c220ea10798b82d7225cbde54daec751f25e581028c926e2a11ba3e33a4b2",
            "O32: M196 route result digest mismatch")
    require(hashlib.sha256(frozen_m200_bytes).hexdigest() ==
            "48b37502a45be316efe39728cee5cb3125c4cc3196b547cf3e90c923e87187f1",
            "O33: frozen M200 incidence table digest mismatch")

    output = {
        "verdict": "ACCEPT" if not objections else "REJECT",
        "numbered_objections": objections,
        "m200_manifest_sha256":
            "6561e28aa199fc1d463881f399f116bd3c05222d6d26e9f54992ff1b542f2045",
        "m200_incidence_table_sha256": hashlib.sha256(frozen_m200_bytes).hexdigest(),
        "m196_results_sha256": result_digest,
        "q5_action_file_sha256": hashlib.sha256(q5_bytes).hexdigest(),
        "q5_action_packed_sha256": action_digest,
        "q5": {
            "states": len(states),
            "source_ids": source_ids,
            "action_rows_exact_match": all(
                left == right for left, right in zip(action_rows, stored_rows)
            ),
            "signed_inverse_pairs": inverse_pairs,
        },
        "independent_incidence": {
            "m181_patterns": d5_row.get("patterns"),
            "m181_voltage_basis": d5_row.get("voltage_basis_representatives"),
            "v_stab_equals_w2": voltage_is_full,
            "rooted_descriptors": len(descriptors),
            "root_edge_rows": len(coordinate_targets),
            "root_pair_rows": occurrence_count,
            "deduplicated_target_classes": len(target_rows),
            "normalized_color_rows": len(clean_color_rows),
            "uncovered": 0,
        },
        "route_replay": {
            "certificates": len(certificate_by_id),
            "all_replayed": not any(
                objection.startswith("O16") for objection in objections
            ),
            "maximum_quotient_certificate_length": max(route_lengths),
            "quotient_words_asserted_zero_voltage": False,
            "voltage_correction_length_claim": None,
            "corrected_total_length_claim": None,
        },
        "logic_audit": {
            "arbitrary_color_selects_one_of_25_pairs_per_edit": True,
            "pair_coverage_is_simultaneous_not_coordinatewise": True,
            "full_voltage_plus_quotient_reachability_invokes_m175_affine_criterion": True,
            "zero_voltage_endpoint_route_conclusion": "qualitative existence only",
        },
        "scope": (
            "exact finite d=5 M181 width-two matching colors only; no all-d, "
            "arbitrary-subfamily, polynomial-length, gap, mixing, or Terminal inference"
        ),
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True))
    if objections:
        raise SystemExit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--q5-action", type=Path, required=True)
    parser.add_argument("--m181-results", type=Path, required=True)
    parser.add_argument("--m196-results", type=Path, required=True)
    parser.add_argument("--m200-table", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("referee_results.json"))
    audit(parser.parse_args())


if __name__ == "__main__":
    main()
