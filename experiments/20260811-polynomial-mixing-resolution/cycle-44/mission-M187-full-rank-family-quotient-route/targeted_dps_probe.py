#!/usr/bin/env python3
"""Targeted DPS audit for the d=5 M181 source pair.

This reconstructs rooted descriptors only for the ten physical words obtained
from the two M181 patterns and their five possible distinguished roots.  It
does not enumerate Z_5, Q_5, an action group, or a quotient component.
"""

from __future__ import annotations

import itertools
import json
import platform
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path


Edge = tuple[int, int]
Word = tuple[Edge, ...]
Tree = frozenset[tuple[int, int]]
Perm = tuple[int, ...]


@dataclass(frozen=True)
class Half:
    color: str
    vertex: int
    label: int


@dataclass(frozen=True)
class Side:
    kind: str


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    q = [0] * len(p)
    for x, y in enumerate(p):
        q[y] = x
    return tuple(q)


def relabel_edge(p: Perm, edge: Edge) -> Edge:
    return tuple(sorted((p[edge[0]], p[edge[1]])))


def relabel_word(p: Perm, word: Word) -> Word:
    return tuple(relabel_edge(p, edge) for edge in word)


def swap_perm(d: int, a: int, b: int) -> Perm:
    p = list(range(d))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def canonical(word: Word, d: int) -> Word:
    return min(relabel_word(p, word) for p in itertools.permutations(range(d)))


def conjugate_edge(edge: Edge, by: Edge) -> Edge:
    a, b = edge
    x, y = by
    image = lambda z: y if z == x else x if z == y else z
    return tuple(sorted((image(a), image(b))))


def hurwitz(word: Word, letter: int) -> Word:
    slot = abs(letter) - 1
    a, b = word[slot], word[slot + 1]
    out = list(word)
    if letter > 0:
        out[slot : slot + 2] = [b, conjugate_edge(a, b)]
    else:
        out[slot : slot + 2] = [conjugate_edge(b, a), a]
    return tuple(out)


def cayley_trees(d: int):
    if d == 2:
        yield frozenset({(1, 2)})
        return
    for code in itertools.product(range(1, d + 1), repeat=d - 2):
        degree = [0] + [1] * d
        for x in code:
            degree[x] += 1
        edges = []
        for x in code:
            leaf = next(v for v in range(1, d + 1) if degree[v] == 1)
            edges.append(tuple(sorted((leaf, x))))
            degree[leaf] -= 1
            degree[x] -= 1
        remaining = [v for v in range(1, d + 1) if degree[v] == 1]
        edges.append(tuple(sorted(remaining)))
        yield frozenset(edges)


def rooted_parent(tree: Tree, d: int) -> dict[int, int]:
    adj = {v: [] for v in range(1, d + 1)}
    for a, b in tree:
        adj[a].append(b)
        adj[b].append(a)
    parent = {d: 0}
    todo = [d]
    while todo:
        a = todo.pop()
        for b in adj[a]:
            if b not in parent:
                parent[b] = a
                todo.append(b)
    return parent


def hairy_incidence(tree: Tree, pi: tuple[int, ...], d: int):
    parent = rooted_parent(tree, d)
    incidence: dict[tuple[str, int], dict[int, tuple[str, int]]] = defaultdict(dict)
    first_black: dict[int, int] = {}
    for i in range(1, d):
        p = parent[i]
        labels = pi[2 * i - 2 : 2 * i]
        for label, white in ((labels[0], i), (labels[1], p)):
            black = ("b", i)
            white_vertex = ("w", white)
            incidence[black][label] = white_vertex
            incidence[white_vertex][label] = black
            first_black[label] = i
    return incidence, first_black


def hairy_boundary(incidence, d: int) -> list[Half | Side]:
    m = 2 * d - 2
    start = (("w", 1), 1)
    state = start
    seen = set()
    out: list[Half | Side] = []
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        step = 1 if vertex[0] == "w" else -1
        label = 1 + ((incoming - 1 + step) % m)
        if label in incidence[vertex]:
            out.append(Side("tree"))
            state = (incidence[vertex][label], label)
        else:
            out.append(Half(vertex[0], vertex[1], label))
            state = (vertex, label)
    assert state == start and len(out) == (2 * d - 1) * m
    return out


def close_hairy(tokens: list[Half | Side], d: int) -> dict[int, int]:
    tokens = list(tokens)
    second_black: dict[int, int] = {}
    while True:
        positions = [j for j, token in enumerate(tokens) if isinstance(token, Half)]
        pair = None
        for k, white_pos in enumerate(positions):
            black_pos = positions[(k + 1) % len(positions)]
            white, black = tokens[white_pos], tokens[black_pos]
            if white.color == "w" and black.color == "b":
                pair = white_pos, black_pos
                break
        if pair is None:
            break
        white_pos, black_pos = pair
        tokens = tokens[white_pos:] + tokens[:white_pos]
        black_pos = (black_pos - white_pos) % len(tokens)
        white, black = tokens[0], tokens[black_pos]
        assert white.label == black.label
        distance = sum(isinstance(token, Side) for token in tokens[1:black_pos])
        assert distance in (1, 3)
        if distance == 3:
            assert white.label not in second_black
            second_black[white.label] = black.vertex
        tokens = [Side("closure")] + tokens[black_pos + 1 :]
    remaining = [token for token in tokens if isinstance(token, Half)]
    assert len(remaining) == 2 * d - 2
    assert all(token.color == "w" for token in remaining)
    return second_black


def dps_word(tree: Tree, pi: tuple[int, ...], d: int) -> Word:
    incidence, first_black = hairy_incidence(tree, pi, d)
    second_black = close_hairy(hairy_boundary(incidence, d), d)
    out = []
    for label in range(1, 2 * d - 1):
        a = first_black[label]
        b = second_black.get(label, d)
        assert a != b
        out.append(tuple(sorted((a - 1, b - 1))))
    return tuple(out)


def adjacent_value_swap(pi: tuple[int, ...], i: int) -> tuple[int, ...]:
    return tuple(i + 1 if x == i else i if x == i + 1 else x for x in pi)


def candidate_pi(word: Word, d: int):
    """Enumerate only pairings compatible with first-black incidences."""
    choices = [tuple(x for x in edge if x != d - 1) for edge in word]
    for assigned in itertools.product(*choices):
        if any(assigned.count(v) != 2 for v in range(d - 1)):
            continue
        labels = {v: [j + 1 for j, x in enumerate(assigned) if x == v] for v in range(d - 1)}
        for flips in itertools.product((0, 1), repeat=d - 1):
            pi = []
            for v in range(d - 1):
                pair = labels[v]
                pi.extend(pair if flips[v] == 0 else reversed(pair))
            yield tuple(pi)


def invert_targeted(word: Word, d: int) -> tuple[Tree, tuple[int, ...], int]:
    trees = tuple(cayley_trees(d))
    trials = 0
    for pi in candidate_pi(word, d):
        for tree in trees:
            trials += 1
            if dps_word(tree, pi, d) == word:
                return tree, pi, trials
    raise AssertionError("targeted DPS inverse failed")


def source_patterns(d: int = 5) -> tuple[Word, Word]:
    assert d == 5
    v = ((0, 1), (0, 1), (0, 2), (0, 2), (1, 3), (1, 3), (0, 4), (0, 4))
    u = ((0, 1), (0, 1), (0, 2), (0, 2), (0, 3), (0, 3), (0, 4), (0, 4))
    return v, u


def quotient_bfs(source: tuple[Word, ...], targets: set[tuple[Word, ...]], d: int, depth: int):
    start = tuple(canonical(word, d) for word in source)
    found: dict[tuple[Word, ...], tuple[int, ...]] = {}
    parent: dict[tuple[Word, ...], tuple[tuple[Word, ...], int] | None] = {start: None}
    queue = deque([(start, 0)])
    while queue and len(found) < len(targets):
        state, level = queue.popleft()
        if state in targets and state not in found:
            path = []
            cursor = state
            while parent[cursor] is not None:
                previous, letter = parent[cursor]
                path.append(letter)
                cursor = previous
            found[state] = tuple(reversed(path))
        if level == depth:
            continue
        for slot in range(1, 2 * d - 2):
            for sign in (1, -1):
                letter = sign * slot
                nxt = tuple(canonical(hurwitz(word, letter), d) for word in state)
                if nxt not in parent:
                    parent[nxt] = state, letter
                    queue.append((nxt, level + 1))
    return found, len(parent), max((level for _, level in queue), default=depth)


def main() -> None:
    d = 5
    sources = source_patterns(d)
    target_rows = []
    target_keys: dict[tuple[Word, ...], list[dict]] = defaultdict(list)
    descriptors = {}
    for coordinate, source in enumerate(sources):
        for root in range(d):
            alpha = swap_perm(d, root, d - 1)
            physical = relabel_word(alpha, source)
            tree, pi, trials = invert_targeted(physical, d)
            assert dps_word(tree, pi, d) == physical
            descriptors[(coordinate, root)] = (tree, pi, physical, trials)

    for i in range(1, 2 * d - 2):
        per_coordinate = []
        for coordinate in range(2):
            rows = []
            for root in range(d):
                tree, pi, physical, trials = descriptors[(coordinate, root)]
                target = dps_word(tree, adjacent_value_swap(pi, i), d)
                rows.append({
                    "root": root,
                    "inverse_trials": trials,
                    "target_canonical": [list(e) for e in canonical(target, d)],
                })
            per_coordinate.append(rows)
        distinct_target_pairs = 0
        distinct_right_pairs = 0
        for root0 in range(d):
            for root1 in range(d):
                left = tuple(tuple(e) for e in per_coordinate[0][root0]["target_canonical"])
                right = tuple(tuple(e) for e in per_coordinate[1][root1]["target_canonical"])
                key = (left, right)
                distinct_target_pairs += key not in target_keys
                if left != right:
                    distinct_right_pairs += 1
                    target_keys[key].append({"i": i, "roots": [root0, root1]})
        target_rows.append({
            "i": i,
            "coordinate_rows": per_coordinate,
            "root_pairs_with_distinct_right_endpoints": distinct_right_pairs,
        })

    # Only a small-radius diagnostic around one ordered source pair.  Its
    # failure to find a route is never used as a nonreachability result.
    target_set = set(target_keys)
    found, visited, _ = quotient_bfs(sources, target_set, d, depth=5)
    result = {
        "experiment": "M187 targeted d=5 DPS/root audit",
        "scope": "two explicit source words, ten targeted rooted inversions, no Z5/Q5 enumeration",
        "repository_base_commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
        "command": "python3 -B targeted_dps_probe.py",
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "sources_canonical": [[list(e) for e in canonical(w, d)] for w in sources],
        "target_rows": target_rows,
        "eligible_distinct_target_tuple_count": len(target_set),
        "bounded_quotient_bfs": {
            "depth": 5,
            "visited_states": visited,
            "targets_found": len(found),
            "found_path_lengths": sorted(len(path) for path in found.values()),
            "interpretation": "positive certificates only; misses are not nonreachability",
        },
    }
    Path("targeted_results.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
