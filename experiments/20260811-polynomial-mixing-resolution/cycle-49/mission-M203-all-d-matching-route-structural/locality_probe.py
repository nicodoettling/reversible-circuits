#!/usr/bin/env python3
"""Bounded exact locality probes for M181's embedded DPS targets.

No quotient Q_d is enumerated.  For d=5,6,7 this script inverts only the
explicit rooted words (and their root relabelings), applies all DPS edits, and
tests whether target factors outside the active adjacent-label positions stay
equal to the source.  It also records support leakage outside each M181 block.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import time
from collections import Counter, defaultdict
from pathlib import Path


def edge(a, b):
    return (a, b) if a < b else (b, a)


def relabel(word, permutation):
    return tuple(edge(permutation[a], permutation[b]) for a, b in word)


def prufer_trees(d):
    for code in itertools.product(range(1, d + 1), repeat=d - 2):
        degree = [0] + [1] * d
        for vertex in code:
            degree[vertex] += 1
        result = []
        for vertex in code:
            leaf = min(x for x in range(1, d + 1) if degree[x] == 1)
            result.append(edge(leaf, vertex))
            degree[leaf] -= 1
            degree[vertex] -= 1
        last = [x for x in range(1, d + 1) if degree[x] == 1]
        result.append(edge(*last))
        yield frozenset(result)


def parents(tree, d):
    adjacency = {vertex: [] for vertex in range(1, d + 1)}
    for a, b in tree:
        adjacency[a].append(b)
        adjacency[b].append(a)
    parent = {d: 0}
    stack = [d]
    while stack:
        vertex = stack.pop()
        for neighbor in adjacency[vertex]:
            if neighbor not in parent:
                parent[neighbor] = vertex
                stack.append(neighbor)
    assert len(parent) == d
    return parent


def boundary(tree, ordering, d):
    parent = parents(tree, d)
    incidence = defaultdict(dict)
    first_black = {}
    for child in range(1, d):
        labels = ordering[2 * child - 2 : 2 * child]
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
            state = (incidence[vertex][label], label)
        else:
            tokens.append(("half", vertex[0], vertex[1], label))
            state = (vertex, label)
    assert state == start and len(tokens) == (2 * d - 1) * m
    return tokens, first_black


def close(tokens, d):
    tokens = list(tokens)
    second_black = {}
    while True:
        positions = [index for index, token in enumerate(tokens) if token[0] == "half"]
        pair = None
        for offset, white_pos in enumerate(positions):
            black_pos = positions[(offset + 1) % len(positions)]
            if tokens[white_pos][1] == "w" and tokens[black_pos][1] == "b":
                pair = white_pos, black_pos
                break
        if pair is None:
            break
        white_pos, black_pos = pair
        tokens = tokens[white_pos:] + tokens[:white_pos]
        black_pos = (black_pos - white_pos) % len(tokens)
        white, black = tokens[0], tokens[black_pos]
        assert white[3] == black[3]
        distance = sum(token[0] == "side" for token in tokens[1:black_pos])
        assert distance in (1, 3)
        if distance == 3:
            second_black[white[3]] = black[2]
        tokens = [("side",)] + tokens[black_pos + 1 :]
    residue = [token for token in tokens if token[0] == "half"]
    assert len(residue) == 2 * d - 2
    assert all(token[1] == "w" for token in residue)
    return second_black


def dps_word(tree, ordering, d):
    tokens, first_black = boundary(tree, ordering, d)
    second_black = close(tokens, d)
    output = []
    for label in range(1, 2 * d - 1):
        a = first_black[label]
        b = second_black.get(label, d)
        assert a != b
        output.append(edge(a - 1, b - 1))
    return tuple(output)


def compatible_orderings(word, d):
    root = d - 1
    choices = [tuple(label for label in pair if label != root) for pair in word]
    for assigned in itertools.product(*choices):
        if any(assigned.count(vertex) != 2 for vertex in range(d - 1)):
            continue
        positions = {
            vertex: [index + 1 for index, value in enumerate(assigned) if value == vertex]
            for vertex in range(d - 1)
        }
        for flips in itertools.product((0, 1), repeat=d - 1):
            ordering = []
            for vertex in range(d - 1):
                pair = positions[vertex]
                ordering.extend(pair if flips[vertex] == 0 else reversed(pair))
            yield tuple(ordering)


def inverse_dps(word, trees, d):
    trials = 0
    for ordering in compatible_orderings(word, d):
        for tree in trees:
            trials += 1
            if dps_word(tree, ordering, d) == word:
                return tree, ordering, trials
    raise AssertionError("DPS inverse not found")


def swap_values(ordering, edit):
    return tuple(
        edit + 1 if value == edit
        else edit if value == edit + 1
        else value
        for value in ordering
    )


def constructed_word(d, pattern):
    r = (d - 1) // 3
    assert len(pattern) == r
    factors = []
    for block_index, bit in enumerate(pattern):
        a, b, c = 3 * block_index + 1, 3 * block_index + 2, 3 * block_index + 3
        triples = ((0, a), (0, b), (0, c)) if bit else ((0, a), (0, b), (a, c))
        for pair in triples:
            factors.extend((pair, pair))
    for label in range(3 * r + 1, d):
        factors.extend(((0, label), (0, label)))
    return tuple(factors)


def root_swap(d, root):
    permutation = list(range(d))
    permutation[root], permutation[d - 1] = permutation[d - 1], permutation[root]
    return tuple(permutation)


def canonical_digest(word, d):
    representative = min(relabel(word, permutation) for permutation in itertools.permutations(range(d)))
    return hashlib.sha256(json.dumps(representative).encode()).hexdigest()


def audit():
    started = time.perf_counter()
    rows = []
    first_failure = None
    for d in (5, 6, 7):
        r = (d - 1) // 3
        patterns = [tuple(0 for _ in range(r))]
        patterns.extend(tuple(int(index == active) for index in range(r)) for active in range(r))
        roots = range(d) if d <= 6 else (d - 1,)
        trees = tuple(prufer_trees(d))
        for pattern_id, pattern in enumerate(patterns):
            literal = constructed_word(d, pattern)
            for root in roots:
                source = relabel(literal, root_swap(d, root))
                tree, ordering, trials = inverse_dps(source, trees, d)
                for edit in range(1, 2 * d - 2):
                    target = dps_word(tree, swap_values(ordering, edit), d)
                    changed_positions = [
                        position for position, (before, after) in enumerate(zip(source, target), 1)
                        if before != after
                    ]
                    # The swapped DPS values edit and edit+1 name factor
                    # positions, so literal factor-locality would allow only
                    # those two positions to change.
                    outside_edit_changes = [
                        position for position in changed_positions
                        if position not in (edit, edit + 1)
                    ]
                    block_size = 6
                    active_block = (edit - 1) // block_size
                    block_start = active_block * block_size + 1
                    block_end = min(block_start + block_size - 1, 2 * d - 2)
                    outside_block_changes = [
                        position for position in changed_positions
                        if not block_start <= position <= block_end
                    ]
                    source_support = set(label for pair in source for label in pair)
                    target_support = set(label for pair in target for label in pair)
                    row = {
                        "d": d,
                        "pattern_id": pattern_id,
                        "pattern": list(pattern),
                        "root": root,
                        "edit": edit,
                        "inverse_trials": trials,
                        "source": [list(pair) for pair in source],
                        "target": [list(pair) for pair in target],
                        "changed_positions": changed_positions,
                        "outside_adjacent_edit_positions": outside_edit_changes,
                        "nominal_six_factor_region": [block_start, block_end],
                        "outside_nominal_block_positions": outside_block_changes,
                        "source_support": sorted(source_support),
                        "target_support": sorted(target_support),
                        "target_canonical_sha256": canonical_digest(target, d),
                        "literal_adjacent_factor_locality": not outside_edit_changes,
                        "literal_six_factor_block_locality": not outside_block_changes,
                    }
                    rows.append(row)
                    if first_failure is None and outside_block_changes:
                        first_failure = row

    assert first_failure is not None
    summary = {
        "experiment": "M203 bounded embedded-DPS locality probe",
        "scope": "explicit M181 words only; no Q_d enumeration",
        "d_values": [5, 6, 7],
        "d7_roots": [6],
        "rows": len(rows),
        "literal_adjacent_factor_locality_failures": sum(
            not row["literal_adjacent_factor_locality"] for row in rows
        ),
        "literal_six_factor_block_locality_failures": sum(
            not row["literal_six_factor_block_locality"] for row in rows
        ),
        "failure_histogram_by_d": dict(sorted(Counter(
            row["d"] for row in rows if not row["literal_six_factor_block_locality"]
        ).items())),
        "first_block_locality_failure": first_failure,
        "elapsed_seconds": time.perf_counter() - started,
        "rows_detail": rows,
    }
    Path("locality_results.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: summary[key] for key in (
        "rows", "literal_adjacent_factor_locality_failures",
        "literal_six_factor_block_locality_failures", "failure_histogram_by_d",
        "first_block_locality_failure", "elapsed_seconds"
    )}, indent=2, sort_keys=True))


if __name__ == "__main__":
    audit()
