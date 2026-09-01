#!/usr/bin/env python3
"""Clean-room referee replay of the narrow M187 d=5 claim.

The script reconstructs rooted DPS coordinates only for two named source
words and five roots each.  It then explores only the signed-Hurwitz ball of
radius five about their ordered quotient pair.  It imports no M187 code or
data and does not enumerate Z_5, Q_5, or a quotient component.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import platform
from collections import defaultdict, deque
from pathlib import Path


Edge = tuple[int, int]
Word = tuple[Edge, ...]
Tree = frozenset[tuple[int, int]]
State = tuple[Word, ...]


def vertex_transposition(d: int, a: int, b: int) -> tuple[int, ...]:
    p = list(range(d))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def rename_word(p: tuple[int, ...], word: Word) -> Word:
    return tuple(tuple(sorted((p[a], p[b]))) for a, b in word)


def canonical_word(word: Word, d: int) -> Word:
    return min(rename_word(p, word) for p in itertools.permutations(range(d)))


def conjugate_edge(edge: Edge, by: Edge) -> Edge:
    x, y = by

    def image(z: int) -> int:
        return y if z == x else x if z == y else z

    return tuple(sorted((image(edge[0]), image(edge[1]))))


def hurwitz(word: Word, symbol: int) -> Word:
    slot = abs(symbol) - 1
    a, b = word[slot], word[slot + 1]
    out = list(word)
    if symbol > 0:
        out[slot : slot + 2] = (b, conjugate_edge(a, b))
    else:
        out[slot : slot + 2] = (conjugate_edge(b, a), a)
    return tuple(out)


def apply_path(state: State, path: tuple[int, ...], d: int) -> State:
    current = state
    for symbol in path:
        current = tuple(canonical_word(hurwitz(word, symbol), d) for word in current)
    return current


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[x]] for x in range(len(p)))


def edge_perm(edge: Edge, d: int) -> tuple[int, ...]:
    return vertex_transposition(d, *edge)


def evaluates_to_identity(word: Word, d: int) -> bool:
    value = tuple(range(d))
    for edge in word:
        value = compose(value, edge_perm(edge, d))
    return value == tuple(range(d))


def connected_support(word: Word, d: int) -> bool:
    adj = [set() for _ in range(d)]
    for a, b in word:
        adj[a].add(b)
        adj[b].add(a)
    seen = {0}
    todo = [0]
    while todo:
        a = todo.pop()
        for b in adj[a]:
            if b not in seen:
                seen.add(b)
                todo.append(b)
    return len(seen) == d


def prufer_trees(d: int):
    """All Cayley trees on one-based vertices 1,...,d."""
    for code in itertools.product(range(1, d + 1), repeat=max(0, d - 2)):
        if d == 2:
            yield frozenset({(1, 2)})
            return
        degree = [0] + [1] * d
        for x in code:
            degree[x] += 1
        edges = []
        for x in code:
            leaf = min(v for v in range(1, d + 1) if degree[v] == 1)
            edges.append(tuple(sorted((leaf, x))))
            degree[leaf] -= 1
            degree[x] -= 1
        tail = [v for v in range(1, d + 1) if degree[v] == 1]
        edges.append(tuple(sorted(tail)))
        yield frozenset(edges)


def parent_map(tree: Tree, d: int) -> dict[int, int]:
    adj = {v: [] for v in range(1, d + 1)}
    for a, b in tree:
        adj[a].append(b)
        adj[b].append(a)
    parent = {d: 0}
    stack = [d]
    while stack:
        a = stack.pop()
        for b in adj[a]:
            if b not in parent:
                parent[b] = a
                stack.append(b)
    assert len(parent) == d
    return parent


def hairy_data(tree: Tree, pi: tuple[int, ...], d: int):
    parent = parent_map(tree, d)
    incidence: dict[tuple[str, int], dict[int, tuple[str, int]]] = defaultdict(dict)
    first_black: dict[int, int] = {}
    for child in range(1, d):
        labels = pi[2 * child - 2 : 2 * child]
        black = ("b", child)
        for label, white in ((labels[0], child), (labels[1], parent[child])):
            white_vertex = ("w", white)
            incidence[black][label] = white_vertex
            incidence[white_vertex][label] = black
            first_black[label] = child
    return incidence, first_black


def boundary_tokens(incidence, d: int):
    """Accepted plus-mirror boundary, encoded without predecessor classes."""
    m = 2 * d - 2
    state = (("w", 1), 1)
    start = state
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
    assert state == start
    assert len(tokens) == (2 * d - 1) * m
    return tokens


def noncrossing_close(tokens, d: int) -> dict[int, int]:
    tokens = list(tokens)
    second_black: dict[int, int] = {}
    while True:
        half_positions = [j for j, token in enumerate(tokens) if token[0] == "half"]
        chosen = None
        for k, white_pos in enumerate(half_positions):
            black_pos = half_positions[(k + 1) % len(half_positions)]
            if tokens[white_pos][1] == "w" and tokens[black_pos][1] == "b":
                chosen = white_pos, black_pos
                break
        if chosen is None:
            break
        white_pos, black_pos = chosen
        tokens = tokens[white_pos:] + tokens[:white_pos]
        black_pos = (black_pos - white_pos) % len(tokens)
        white, black = tokens[0], tokens[black_pos]
        assert white[4 - 1] == black[4 - 1]
        side_distance = sum(token[0] == "side" for token in tokens[1:black_pos])
        assert side_distance in (1, 3)
        if side_distance == 3:
            label = white[3]
            assert label not in second_black
            second_black[label] = black[2]
        tokens = [("side",)] + tokens[black_pos + 1 :]
    remainder = [token for token in tokens if token[0] == "half"]
    assert len(remainder) == 2 * d - 2
    assert all(token[1] == "w" for token in remainder)
    return second_black


def dps_close(tree: Tree, pi: tuple[int, ...], d: int) -> Word:
    incidence, first_black = hairy_data(tree, pi, d)
    second_black = noncrossing_close(boundary_tokens(incidence, d), d)
    word = []
    for label in range(1, 2 * d - 1):
        a = first_black[label]
        b = second_black.get(label, d)
        assert a != b
        word.append(tuple(sorted((a - 1, b - 1))))
    return tuple(word)


def compatible_pi(word: Word, d: int):
    """Only first-black assignments consistent with the displayed factors."""
    root = d - 1
    endpoint_choices = [tuple(x for x in edge if x != root) for edge in word]
    for assignment in itertools.product(*endpoint_choices):
        if any(assignment.count(v) != 2 for v in range(d - 1)):
            continue
        labels = {
            v: [position + 1 for position, x in enumerate(assignment) if x == v]
            for v in range(d - 1)
        }
        for flips in itertools.product((0, 1), repeat=d - 1):
            pi = []
            for v in range(d - 1):
                pair = labels[v]
                pi.extend(pair if flips[v] == 0 else reversed(pair))
            yield tuple(pi)


def rooted_inverse(word: Word, d: int, trees: tuple[Tree, ...]):
    trials = 0
    for pi in compatible_pi(word, d):
        for tree in trees:
            trials += 1
            if dps_close(tree, pi, d) == word:
                return tree, pi, trials
    raise AssertionError("targeted rooted inverse failed")


def swap_adjacent_values(pi: tuple[int, ...], index: int) -> tuple[int, ...]:
    return tuple(
        index + 1 if value == index else index if value == index + 1 else value
        for value in pi
    )


def source_pair() -> State:
    v = ((0, 1), (0, 1), (0, 2), (0, 2), (1, 3), (1, 3), (0, 4), (0, 4))
    u = ((0, 1), (0, 1), (0, 2), (0, 2), (0, 3), (0, 3), (0, 4), (0, 4))
    return v, u


def quotient_ball_routes(start: State, targets: set[State], d: int, radius: int):
    canonical_start = tuple(canonical_word(word, d) for word in start)
    parent: dict[State, tuple[State, int] | None] = {canonical_start: None}
    levels = {canonical_start: 0}
    queue = deque([canonical_start])
    found: dict[State, tuple[int, ...]] = {}
    while queue:
        state = queue.popleft()
        level = levels[state]
        if state in targets:
            path = []
            cursor = state
            while parent[cursor] is not None:
                previous, symbol = parent[cursor]
                path.append(symbol)
                cursor = previous
            found[state] = tuple(reversed(path))
        if level == radius:
            continue
        for slot in range(1, 2 * d - 2):
            for sign in (1, -1):
                symbol = sign * slot
                nxt = tuple(canonical_word(hurwitz(word, symbol), d) for word in state)
                if nxt not in parent:
                    parent[nxt] = state, symbol
                    levels[nxt] = level + 1
                    queue.append(nxt)
    return found, parent, levels


def word_json(word: Word):
    return [list(edge) for edge in word]


def state_json(state: State):
    return [word_json(word) for word in state]


def main() -> None:
    d = 5
    sources = source_pair()
    assert all(evaluates_to_identity(word, d) for word in sources)
    assert all(connected_support(word, d) for word in sources)
    trees = tuple(prufer_trees(d))
    assert len(trees) == d ** (d - 2)

    descriptors = {}
    descriptor_rows = []
    for coordinate, source in enumerate(sources):
        for root in range(d):
            relabel = vertex_transposition(d, root, d - 1)
            rooted_word = rename_word(relabel, source)
            tree, pi, trials = rooted_inverse(rooted_word, d, trees)
            assert dps_close(tree, pi, d) == rooted_word
            descriptors[coordinate, root] = tree, pi
            descriptor_rows.append({
                "coordinate": coordinate,
                "root": root,
                "pi": list(pi),
                "tree": [list(edge) for edge in sorted(tree)],
                "trials": trials,
            })

    occurrences: dict[State, list[dict[str, object]]] = defaultdict(list)
    occurrence_count = 0
    ineligible_count = 0
    target_word_checks = 0
    for edit in range(1, 2 * d - 2):
        coordinate_targets: list[list[Word]] = []
        for coordinate in range(2):
            root_targets = []
            for root in range(d):
                tree, pi = descriptors[coordinate, root]
                target = dps_close(tree, swap_adjacent_values(pi, edit), d)
                assert evaluates_to_identity(target, d)
                assert connected_support(target, d)
                target_word_checks += 1
                root_targets.append(canonical_word(target, d))
            coordinate_targets.append(root_targets)
        for root0 in range(d):
            for root1 in range(d):
                occurrence_count += 1
                target_state = (
                    coordinate_targets[0][root0],
                    coordinate_targets[1][root1],
                )
                if target_state[0] == target_state[1]:
                    ineligible_count += 1
                else:
                    occurrences[target_state].append({
                        "edit": edit,
                        "roots": [root0, root1],
                    })

    targets = set(occurrences)
    found, parent, levels = quotient_ball_routes(sources, targets, d, radius=5)
    canonical_source = tuple(canonical_word(word, d) for word in sources)
    routes = []
    for target, path in sorted(
        found.items(), key=lambda item: (len(item[1]), item[1], item[0])
    ):
        assert apply_path(canonical_source, path, d) == target
        routes.append({
            "length": len(path),
            "path": list(path),
            "occurrences": sorted(
                occurrences[target], key=lambda row: (row["edit"], row["roots"])
            ),
            "target": state_json(target),
        })

    anchored = {}
    for edit in range(1, 2 * d - 2):
        match = [
            route["path"]
            for route in routes
            if any(
                row["edit"] == edit and row["roots"] == [0, 0]
                for row in route["occurrences"]
            )
        ]
        anchored[str(edit)] = match[0] if match else None

    normalized = json.dumps(routes, sort_keys=True, separators=(",", ":")).encode()
    result = {
        "experiment": "M188 independent narrow M187 replay",
        "repository_base_commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
        "command": "python3 -B independent_replay.py",
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "scope": "two d=5 source words, ten rooted inversions, radius-five quotient ball",
        "broad_enumeration": False,
        "source_checks": {
            "identity": True,
            "connected_support": True,
            "canonical_sources": state_json(canonical_source),
        },
        "rooted_descriptors": descriptor_rows,
        "target_construction": {
            "raw_root_pair_occurrences": occurrence_count,
            "ineligible_equal_endpoint_occurrences": ineligible_count,
            "eligible_occurrences": occurrence_count - ineligible_count,
            "distinct_eligible_target_tuples": len(targets),
            "target_word_identity_connected_checks": target_word_checks,
        },
        "radius_five_ball": {
            "visited_states": len(parent),
            "states_by_level": {
                str(level): sum(value == level for value in levels.values())
                for level in range(6)
            },
            "positive_target_count": len(routes),
            "positive_path_lengths": [row["length"] for row in routes],
            "routes": routes,
            "routes_sha256": hashlib.sha256(normalized).hexdigest(),
            "anchored_root_pair_routes": anchored,
            "miss_interpretation": "none; bounded-radius misses are undecided",
        },
        "claim_match": {
            "distinct_targets_is_54": len(targets) == 54,
            "positive_targets_is_14": len(routes) == 14,
            "lengths_match": sorted(row["length"] for row in routes)
            == [0, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 5],
            "visited_states_is_4008": len(parent) == 4008,
        },
    }
    assert all(result["claim_match"].values())
    Path("independent_results.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps({
        "claim_match": result["claim_match"],
        "target_construction": result["target_construction"],
        "radius_five_summary": {
            key: result["radius_five_ball"][key]
            for key in (
                "visited_states",
                "states_by_level",
                "positive_target_count",
                "positive_path_lengths",
                "routes_sha256",
                "anchored_root_pair_routes",
                "miss_interpretation",
            )
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
