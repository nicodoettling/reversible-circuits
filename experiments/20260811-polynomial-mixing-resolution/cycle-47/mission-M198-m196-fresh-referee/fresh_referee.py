#!/usr/bin/env python3
"""Clean-room exact referee for frozen M196.

No M191/M196 Python module is imported.  This script reconstructs Q5 and the
named DPS targets from definitions, then audits M196's literal certificates.
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


def edge(a, b):
    return (a, b) if a < b else (b, a)


def rename(word, permutation):
    return tuple(edge(permutation[a], permutation[b]) for a, b in word)


@cache
def quotient_representative(word):
    return min(rename(word, permutation) for permutation in LABELINGS)


def conjugate_edge(target, conjugator):
    x, y = conjugator

    def image(label):
        if label == x:
            return y
        if label == y:
            return x
        return label

    return edge(image(target[0]), image(target[1]))


def hurwitz(word, symbol):
    slot = abs(symbol) - 1
    left, right = word[slot], word[slot + 1]
    moved = list(word)
    if symbol > 0:
        moved[slot : slot + 2] = (right, conjugate_edge(left, right))
    else:
        moved[slot : slot + 2] = (conjugate_edge(right, left), left)
    return tuple(moved)


def inverse_word(word):
    return tuple(-symbol for symbol in reversed(word))


def permutation_for_edge(pair):
    permutation = list(IDENTITY)
    a, b = pair
    permutation[a], permutation[b] = permutation[b], permutation[a]
    return tuple(permutation)


def compose(left, right):
    return tuple(left[right[x]] for x in range(D))


def identity_product(word):
    value = IDENTITY
    for pair in word:
        value = compose(value, permutation_for_edge(pair))
    return value == IDENTITY


def connected(word):
    adjacency = [set() for _ in range(D)]
    for a, b in word:
        adjacency[a].add(b)
        adjacency[b].add(a)
    reached = {0}
    queue = [0]
    while queue:
        vertex = queue.pop()
        for neighbor in adjacency[vertex]:
            if neighbor not in reached:
                reached.add(neighbor)
                queue.append(neighbor)
    return len(reached) == D


def source_words():
    first = (
        (0, 1), (0, 1), (0, 2), (0, 2),
        (1, 3), (1, 3), (0, 4), (0, 4),
    )
    second = (
        (0, 1), (0, 1), (0, 2), (0, 2),
        (0, 3), (0, 3), (0, 4), (0, 4),
    )
    return quotient_representative(first), quotient_representative(second)


def reconstruct_q5():
    first, _second = source_words()
    reached = {first}
    queue = deque([first])
    while queue:
        word = queue.popleft()
        for symbol in SYMBOLS:
            neighbor = quotient_representative(hurwitz(word, symbol))
            if neighbor not in reached:
                reached.add(neighbor)
                queue.append(neighbor)
    states = tuple(sorted(reached))
    index = {word: state_id for state_id, word in enumerate(states)}
    action_rows = []
    for symbol in SYMBOLS:
        action_rows.append(array("H", (
            index[quotient_representative(hurwitz(word, symbol))]
            for word in states
        )))
    return states, index, action_rows


def prufer_trees():
    for code in itertools.product(range(1, D + 1), repeat=D - 2):
        degrees = [0] + [1] * D
        for vertex in code:
            degrees[vertex] += 1
        tree_edges = []
        for vertex in code:
            leaf = min(x for x in range(1, D + 1) if degrees[x] == 1)
            tree_edges.append(edge(leaf, vertex))
            degrees[leaf] -= 1
            degrees[vertex] -= 1
        last = [x for x in range(1, D + 1) if degrees[x] == 1]
        tree_edges.append(edge(*last))
        yield frozenset(tree_edges)


def tree_parents(tree):
    adjacency = {vertex: [] for vertex in range(1, D + 1)}
    for a, b in tree:
        adjacency[a].append(b)
        adjacency[b].append(a)
    parents = {D: 0}
    stack = [D]
    while stack:
        vertex = stack.pop()
        for neighbor in adjacency[vertex]:
            if neighbor not in parents:
                parents[neighbor] = vertex
                stack.append(neighbor)
    assert len(parents) == D
    return parents


def hairy_boundary(tree, ordering):
    parents = tree_parents(tree)
    incidence = defaultdict(dict)
    first_black = {}
    for child in range(1, D):
        first_label, second_label = ordering[2 * child - 2 : 2 * child]
        black = ("b", child)
        for label, white_id in (
            (first_label, child), (second_label, parents[child])
        ):
            white = ("w", white_id)
            incidence[black][label] = white
            incidence[white][label] = black
            first_black[label] = child

    modulus = 2 * D - 2
    start = (("w", 1), 1)
    cursor = start
    visited = set()
    tokens = []
    while cursor not in visited:
        visited.add(cursor)
        vertex, incoming = cursor
        direction = 1 if vertex[0] == "w" else -1
        label = 1 + ((incoming - 1 + direction) % modulus)
        if label in incidence[vertex]:
            tokens.append(("side",))
            cursor = (incidence[vertex][label], label)
        else:
            tokens.append(("half", vertex[0], vertex[1], label))
            cursor = (vertex, label)
    assert cursor == start
    assert len(tokens) == (2 * D - 1) * modulus
    return tokens, first_black


def close_hairy(tokens):
    tokens = list(tokens)
    second_black = {}
    while True:
        half_positions = [
            position for position, token in enumerate(tokens)
            if token[0] == "half"
        ]
        closable = None
        for offset, white_position in enumerate(half_positions):
            black_position = half_positions[(offset + 1) % len(half_positions)]
            if (
                tokens[white_position][1] == "w"
                and tokens[black_position][1] == "b"
            ):
                closable = (white_position, black_position)
                break
        if closable is None:
            break
        white_position, black_position = closable
        tokens = tokens[white_position:] + tokens[:white_position]
        black_position = (black_position - white_position) % len(tokens)
        white_token, black_token = tokens[0], tokens[black_position]
        assert white_token[3] == black_token[3]
        separation = sum(
            token[0] == "side" for token in tokens[1:black_position]
        )
        assert separation in (1, 3)
        if separation == 3:
            second_black[white_token[3]] = black_token[2]
        tokens = [("side",)] + tokens[black_position + 1 :]
    residue = [token for token in tokens if token[0] == "half"]
    assert len(residue) == 2 * D - 2
    assert all(token[1] == "w" for token in residue)
    return second_black


def dps_word(tree, ordering):
    boundary, first_black = hairy_boundary(tree, ordering)
    second_black = close_hairy(boundary)
    word = []
    for label in range(1, 2 * D - 1):
        left = first_black[label]
        right = second_black.get(label, D)
        assert left != right
        word.append(edge(left - 1, right - 1))
    return tuple(word)


def compatible_orderings(word):
    root = D - 1
    endpoint_choices = [tuple(x for x in pair if x != root) for pair in word]
    for selected in itertools.product(*endpoint_choices):
        if any(selected.count(vertex) != 2 for vertex in range(D - 1)):
            continue
        positions = {
            vertex: [position + 1 for position, value in enumerate(selected)
                     if value == vertex]
            for vertex in range(D - 1)
        }
        for orientations in itertools.product((0, 1), repeat=D - 1):
            ordering = []
            for vertex in range(D - 1):
                pair = positions[vertex]
                ordering.extend(
                    pair if orientations[vertex] == 0 else reversed(pair)
                )
            yield tuple(ordering)


def inverse_dps(word, trees):
    trials = 0
    for ordering in compatible_orderings(word):
        for tree in trees:
            trials += 1
            if dps_word(tree, ordering) == word:
                return tree, ordering, trials
    raise AssertionError("no rooted DPS descriptor")


def swap_adjacent_values(ordering, position):
    return tuple(
        position + 1 if value == position
        else position if value == position + 1
        else value
        for value in ordering
    )


def reconstruct_named_targets():
    source = source_words()
    trees = tuple(prufer_trees())
    descriptors = {}
    descriptor_rows = []
    for coordinate, word in enumerate(source):
        for root in range(D):
            root_swap = list(IDENTITY)
            root_swap[root], root_swap[D - 1] = root_swap[D - 1], root_swap[root]
            physical = rename(word, tuple(root_swap))
            tree, ordering, trials = inverse_dps(physical, trees)
            descriptors[coordinate, root] = (tree, ordering)
            descriptor_rows.append({
                "coordinate": coordinate,
                "root": root,
                "tree": [list(pair) for pair in sorted(tree)],
                "pi": list(ordering),
                "trials": trials,
            })

    occurrences = defaultdict(list)
    for edit in range(1, 8):
        coordinate_targets = []
        for coordinate in range(2):
            root_targets = []
            for root in range(D):
                tree, ordering = descriptors[coordinate, root]
                edited = dps_word(tree, swap_adjacent_values(ordering, edit))
                target = quotient_representative(edited)
                assert identity_product(target)
                assert connected(target)
                root_targets.append(target)
            coordinate_targets.append(root_targets)
        for first_root in range(D):
            for second_root in range(D):
                target = (
                    coordinate_targets[0][first_root],
                    coordinate_targets[1][second_root],
                )
                assert target[0] != target[1]
                occurrences[target].append({
                    "edit": edit,
                    "roots": [first_root, second_root],
                })
    return occurrences, descriptor_rows


def apply_point(point, word, action):
    for symbol in word:
        point = action[symbol][point]
    return point


def apply_pair(pair, word, action):
    first, second = pair
    for symbol in word:
        row = action[symbol]
        first, second = row[first], row[second]
    return first, second


def one_coordinate_transversal(start, action):
    parent = [-2] * N
    parent_symbol = [0] * N
    depth = [-1] * N
    parent[start] = -1
    depth[start] = 0
    order = [start]
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        for symbol in SYMBOLS:
            neighbor = action[symbol][vertex]
            if parent[neighbor] == -2:
                parent[neighbor] = vertex
                parent_symbol[neighbor] = symbol
                depth[neighbor] = depth[vertex] + 1
                order.append(neighbor)
                queue.append(neighbor)
    return parent, parent_symbol, depth, order


def tree_word(vertex, parent, parent_symbol):
    reverse = []
    while parent[vertex] != -1:
        reverse.append(parent_symbol[vertex])
        vertex = parent[vertex]
    return tuple(reversed(reverse))


def pair_code(first, second):
    return first * N + second


def pair_decode(code):
    return divmod(code, N)


def product_forward_ball(source, action, radius):
    root = pair_code(*source)
    parent = {root: None}
    parent_symbol = {}
    distance = {root: 0}
    frontier = [root]
    levels = [1]
    for next_depth in range(1, radius + 1):
        next_frontier = []
        for code in frontier:
            first, second = pair_decode(code)
            for symbol in SYMBOLS:
                row = action[symbol]
                neighbor = pair_code(row[first], row[second])
                if neighbor not in parent:
                    parent[neighbor] = code
                    parent_symbol[neighbor] = symbol
                    distance[neighbor] = next_depth
                    next_frontier.append(neighbor)
        frontier = next_frontier
        levels.append(len(frontier))
    return parent, parent_symbol, distance, levels


def product_tree_word(code, root, parent, parent_symbol):
    reverse = []
    while code != root:
        reverse.append(parent_symbol[code])
        code = parent[code]
    return tuple(reversed(reverse))


def normalized_occurrences(rows):
    return sorted(rows, key=lambda row: (row["edit"], row["roots"]))


def audit(args):
    objections = []

    def require(condition, message):
        if not condition:
            objections.append(message)

    q5_bytes = args.q5_action.read_bytes()
    q5 = json.loads(q5_bytes)
    adjusted = json.loads(args.adjusted.read_text())
    result_bytes = args.results.read_bytes()
    results = json.loads(result_bytes)
    prior_verification = json.loads(args.prior_verification.read_text())

    states, state_index, rebuilt_rows = reconstruct_q5()
    require(len(states) == N, "O01: rebuilt Q5 orbit does not have 8400 states")
    require(all(identity_product(word) and connected(word) for word in states),
            "O02: a rebuilt Q5 state fails identity/connectedness")
    require(q5.get("q5_size") == N, "O03: frozen q5_size is not 8400")
    require(q5.get("physical_z5_count") == 5 ** 2 * 40320,
            "O04: physical Z5 count mismatch")
    require(q5.get("symbols") == list(SYMBOLS),
            "O05: frozen symbol order mismatch")

    stored_rows = [array("H", row) for row in q5["action_rows"]]
    require(len(stored_rows) == 14 and all(len(row) == N for row in stored_rows),
            "O06: action-row dimensions mismatch")
    require(all(stored == rebuilt for stored, rebuilt in zip(stored_rows, rebuilt_rows)),
            "O07: frozen action rows differ from clean-room reconstruction")
    all_bijections = all(len(set(row)) == N for row in rebuilt_rows)
    require(all_bijections, "O08: a rebuilt generator row is not bijective")
    inverse_pairs = all(
        rebuilt_rows[7 + slot][rebuilt_rows[slot][point]] == point
        and rebuilt_rows[slot][rebuilt_rows[7 + slot][point]] == point
        for slot in range(7) for point in range(N)
    )
    require(inverse_pairs, "O09: signed action rows are not mutual inverses")
    action_digest = hashlib.sha256(
        b"".join(row.tobytes() for row in rebuilt_rows)
    ).hexdigest()
    require(action_digest == q5.get("action_sha256"),
            "O10: packed action digest mismatch")
    action = dict(zip(SYMBOLS, rebuilt_rows))

    source_words_pair = source_words()
    rebuilt_source_ids = [state_index[word] for word in source_words_pair]
    require(rebuilt_source_ids == [16, 0] == q5.get("source_ids"),
            "O11: source IDs mismatch")
    source = tuple(rebuilt_source_ids)

    occurrences, descriptor_rows = reconstruct_named_targets()
    require(len(descriptor_rows) == 10,
            "O12: rooted descriptor count is not 10")
    require(descriptor_rows == q5.get("rooted_descriptors"),
            "O13: clean-room rooted descriptors differ")
    require(len(occurrences) == 54,
            "O14: reconstructed named target count is not 54")
    require(sum(map(len, occurrences.values())) == 175,
            "O15: named target occurrence multiplicity is not 175")
    rebuilt_target_rows = []
    for target_id, (target, rows) in enumerate(sorted(occurrences.items())):
        rebuilt_target_rows.append({
            "target_id": target_id,
            "target_ids": [state_index[target[0]], state_index[target[1]]],
            "occurrences": normalized_occurrences(rows),
        })
    require(rebuilt_target_rows == q5.get("target_rows"),
            "O16: frozen 54-row target inventory differs from reconstruction")

    parent, parent_symbol, depth, order = one_coordinate_transversal(source[0], action)
    require(len(order) == N, "O17: one-coordinate transversal is incomplete")
    require(max(depth) == 13, "O18: transversal maximum depth is not 13")
    all_tree_replays = all(
        apply_point(source[0], tree_word(vertex, parent, parent_symbol), action)
        == vertex for vertex in range(N)
    )
    require(all_tree_replays, "O19: a chronological tree word fails replay")

    expected_adjusted_rows = []
    classes = defaultdict(list)
    for target in rebuilt_target_rows:
        target_first, target_second = target["target_ids"]
        alpha = tree_word(target_first, parent, parent_symbol)
        adjusted_second = apply_point(target_second, inverse_word(alpha), action)
        classes[adjusted_second].append(target["target_id"])
        expected_adjusted_rows.append({
            "target_id": target["target_id"],
            "target_ids": target["target_ids"],
            "occurrences": target["occurrences"],
            "first_tree_word": list(alpha),
            "adjusted_second_id": adjusted_second,
        })
    expected_classes = [
        {"adjusted_second_id": adjusted_id, "target_ids": ids}
        for adjusted_id, ids in sorted(classes.items())
    ]
    require(len(classes) == 41, "O20: adjusted targets do not deduplicate to 41")
    require(adjusted.get("target_rows") == expected_adjusted_rows,
            "O21: M196 adjusted target rows differ from clean-room values")
    require(adjusted.get("adjusted_classes") == expected_classes,
            "O22: M196 adjusted target classes differ from clean-room values")
    require(adjusted.get("transversal_size") == N
            and adjusted.get("transversal_max_depth") == 13
            and adjusted.get("target_count") == 54
            and adjusted.get("distinct_adjusted_target_count") == 41,
            "O23: M196 adjusted summary fields mismatch")

    forward_parent, forward_symbol, forward_distance, forward_levels = (
        product_forward_ball(source, action, 8)
    )
    expected_levels = [1, 6, 40, 190, 795, 2976, 10416, 34256, 105713]
    require(forward_levels == expected_levels,
            "O24: independently rebuilt radius-eight level sizes mismatch")
    require(len(forward_parent) == 154393,
            "O25: independently rebuilt forward-ball size is not 154393")
    require(results.get("forward_level_sizes") == forward_levels
            and results.get("forward_visited") == len(forward_parent),
            "O26: stored forward-ball summary differs from reconstruction")
    require(results.get("forward_depth_cap") == 8
            and results.get("backward_depth_cap") == 8,
            "O27: stored MITM depth caps are not 8/8")

    searches = results.get("searches", [])
    require(len(searches) == 41, "O28: search certificate count is not 41")
    search_by_adjusted = {}
    meeting_checks = 0
    stabilizer_replays = 0
    direct_count = 0
    forward_lengths = []
    backward_lengths = []
    stabilizer_lengths = []
    for certificate in searches:
        adjusted_id = certificate.get("adjusted_second_id")
        require(adjusted_id not in search_by_adjusted,
                f"O29: duplicate search certificate for adjusted ID {adjusted_id}")
        search_by_adjusted[adjusted_id] = certificate
        require(certificate.get("status") == "positive",
                f"O30: adjusted ID {adjusted_id} is not positive")
        require(certificate.get("target_ids") == classes.get(adjusted_id),
                f"O31: adjusted ID {adjusted_id} target class mismatch")
        forward = tuple(certificate.get("forward_word", []))
        backward = tuple(certificate.get("backward_word", []))
        stabilizer = tuple(certificate.get("stabilizer_word", []))
        meeting = tuple(certificate.get("meeting_state", []))
        require(all(symbol in SYMBOLS for symbol in forward + backward + stabilizer),
                f"O32: invalid symbol in adjusted ID {adjusted_id} certificate")
        require(len(forward) <= 8 and len(backward) <= 8,
                f"O33: adjusted ID {adjusted_id} exceeds 8/8 MITM radius")
        require(apply_pair(source, forward, action) == meeting,
                f"O34: adjusted ID {adjusted_id} forward meeting replay fails")
        require(apply_pair((source[0], adjusted_id), backward, action) == meeting,
                f"O35: adjusted ID {adjusted_id} backward meeting replay fails")
        require(stabilizer == forward + inverse_word(backward),
                f"O36: adjusted ID {adjusted_id} inverse concatenation mismatch")
        require(apply_pair(source, stabilizer, action) == (source[0], adjusted_id),
                f"O37: adjusted ID {adjusted_id} stabilizer replay fails")
        meeting_code = pair_code(*meeting)
        require(meeting_code in forward_distance,
                f"O38: adjusted ID {adjusted_id} meeting is outside forward ball")
        if meeting_code in forward_distance:
            require(forward_distance[meeting_code] == len(forward),
                    f"O39: adjusted ID {adjusted_id} forward length is not BFS depth")
            canonical_forward = product_tree_word(
                meeting_code, pair_code(*source), forward_parent, forward_symbol
            )
            require(forward == canonical_forward,
                    f"O40: adjusted ID {adjusted_id} forward BFS word mismatch")
        meeting_checks += 1
        stabilizer_replays += 1
        direct_count += not backward
        forward_lengths.append(len(forward))
        backward_lengths.append(len(backward))
        stabilizer_lengths.append(len(stabilizer))

    require(set(search_by_adjusted) == set(classes),
            "O41: adjusted search-ID inventory mismatch")
    require(direct_count == 15 and len(searches) - direct_count == 26,
            "O42: direct/MITM split is not 15/26")

    originals = results.get("original_target_certificates", [])
    require(len(originals) == 54, "O43: full certificate count is not 54")
    original_by_id = {}
    adjustment_checks = 0
    full_replays = 0
    tree_lengths = []
    full_lengths = []
    for certificate in originals:
        target_id = certificate.get("target_id")
        require(target_id not in original_by_id,
                f"O44: duplicate original target ID {target_id}")
        original_by_id[target_id] = certificate
        if not isinstance(target_id, int) or not 0 <= target_id < 54:
            require(False, f"O45: invalid original target ID {target_id}")
            continue
        target = rebuilt_target_rows[target_id]
        target_ids = tuple(target["target_ids"])
        require(certificate.get("target_ids") == target["target_ids"],
                f"O46: target IDs mismatch for target {target_id}")
        alpha = tree_word(target_ids[0], parent, parent_symbol)
        adjusted_id = apply_point(target_ids[1], inverse_word(alpha), action)
        require(certificate.get("adjusted_second_id") == adjusted_id,
                f"O47: adjusted second mismatch for target {target_id}")
        require(tuple(certificate.get("first_tree_word", [])) == alpha,
                f"O48: tree word mismatch for target {target_id}")
        require(certificate.get("status") == "positive",
                f"O49: target {target_id} is not marked positive")
        stabilizer = tuple(certificate.get("stabilizer_word", []))
        full_word = tuple(certificate.get("full_word", []))
        expected_stabilizer = tuple(
            search_by_adjusted[adjusted_id].get("stabilizer_word", [])
        )
        require(stabilizer == expected_stabilizer,
                f"O50: stabilizer word mismatch for target {target_id}")
        require(full_word == stabilizer + alpha,
                f"O51: full concatenation mismatch for target {target_id}")
        require(apply_point(source[0], alpha, action) == target_ids[0]
                and apply_point(adjusted_id, alpha, action) == target_ids[1],
                f"O52: adjustment/tree relation fails for target {target_id}")
        require(apply_pair(source, full_word, action) == target_ids,
                f"O53: full endpoint replay fails for target {target_id}")
        adjustment_checks += 1
        full_replays += 1
        tree_lengths.append(len(alpha))
        full_lengths.append(len(full_word))

    require(set(original_by_id) == set(range(54)),
            "O54: original target-ID inventory is not exactly 0..53")
    require(max(forward_lengths, default=-1) == 8,
            "O55: maximum forward length is not 8")
    require(max(backward_lengths, default=-1) == 7,
            "O56: maximum backward length is not 7")
    require(max(stabilizer_lengths, default=-1) == 15,
            "O57: maximum stabilizer length is not 15")
    require(max(tree_lengths, default=-1) == 9,
            "O58: maximum named-target tree length is not 9")
    require(max(full_lengths, default=-1) == 22,
            "O59: maximum full endpoint-word length is not 22")

    aggregate_expectations = {
        "distinct_adjusted_targets": 41,
        "positive_adjusted_targets": 41,
        "undecided_adjusted_targets": 0,
        "original_targets": 54,
        "positive_original_targets": 54,
        "undecided_original_targets": 0,
        "complete_positive_classification": True,
        "negative_membership_claims": 0,
        "unresolved_statuses": [],
    }
    for key, value in aggregate_expectations.items():
        require(results.get(key) == value,
                f"O60: aggregate field {key} mismatch")

    result_digest = hashlib.sha256(result_bytes).hexdigest()
    require(result_digest == prior_verification.get("targeted_results_sha256"),
            "O61: result digest differs from frozen verification")
    require(action_digest == prior_verification.get("action_sha256"),
            "O62: action digest differs from frozen verification")
    require(result_digest ==
            "e40c220ea10798b82d7225cbde54daec751f25e581028c926e2a11ba3e33a4b2",
            "O63: stated result digest mismatch")
    require(action_digest ==
            "160bcae167e754af4ff55356a2ab25526bf53d03ebc23bd974938fb8370c67ae",
            "O64: stated action digest mismatch")

    summary = {
        "verdict": "ACCEPT" if not objections else "REJECT",
        "numbered_objections": objections,
        "m196_manifest_sha256":
            "7fa987c6c776e55990c00fcfaea85e34c1d7b0e6d3f97d57fdefba8bcb5bd913",
        "q5_action_file_sha256": hashlib.sha256(q5_bytes).hexdigest(),
        "action_sha256": action_digest,
        "targeted_results_sha256": result_digest,
        "q5": {
            "reconstructed_states": len(states),
            "all_states_identity_connected": True,
            "action_rows_exact_match": not any(
                objection.startswith("O07") for objection in objections
            ),
            "all_generator_bijections": all_bijections,
            "all_signed_inverse_pairs": inverse_pairs,
            "source_ids": list(source),
            "transversal_size": len(order),
            "transversal_max_depth": max(depth),
            "all_transversal_words_replayed": all_tree_replays,
        },
        "named_targets": {
            "rooted_descriptors": len(descriptor_rows),
            "distinct_rows": len(rebuilt_target_rows),
            "occurrences": sum(map(len, occurrences.values())),
            "adjusted_distinct": len(classes),
        },
        "forward_ball": {
            "radius": 8,
            "level_sizes": forward_levels,
            "states": len(forward_parent),
        },
        "certificates": {
            "adjusted": len(searches),
            "direct": direct_count,
            "nonempty_backward": len(searches) - direct_count,
            "meeting_checks": meeting_checks,
            "stabilizer_replays": stabilizer_replays,
            "original": len(originals),
            "adjustment_checks": adjustment_checks,
            "full_replays": full_replays,
            "max_forward_length": max(forward_lengths, default=None),
            "max_backward_length": max(backward_lengths, default=None),
            "max_stabilizer_length": max(stabilizer_lengths, default=None),
            "max_named_tree_length": max(tree_lengths, default=None),
            "max_full_length": max(full_lengths, default=None),
            "stabilizer_length_histogram": dict(sorted(Counter(stabilizer_lengths).items())),
            "full_length_histogram": dict(sorted(Counter(full_lengths).items())),
        },
        "scope": (
            "exact finite d=5 width-two named target list only; no every-color, "
            "all-d, polynomial-length, gap, mixing, or Terminal inference"
        ),
    }
    args.output.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))
    if objections:
        raise SystemExit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--q5-action", type=Path, required=True)
    parser.add_argument("--adjusted", type=Path, required=True)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--prior-verification", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("referee_results.json"))
    args = parser.parse_args()
    audit(args)


if __name__ == "__main__":
    main()
