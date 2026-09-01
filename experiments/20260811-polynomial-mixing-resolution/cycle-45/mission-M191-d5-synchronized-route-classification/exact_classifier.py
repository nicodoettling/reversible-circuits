#!/usr/bin/env python3
"""Exact finite d=5 synchronized quotient-route classifier.

This independently reconstructs the 54 named M188 targets, enumerates the
single quotient Q_5, builds a Schreier tree for the first source, and reduces
diagonal membership to an exact orbit of its action stabilizer on the second
coordinate.  No radius cutoff decides membership and no Cartesian product is
enumerated.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
from array import array
from collections import defaultdict, deque
from pathlib import Path


Edge = tuple[int, int]
Word = tuple[Edge, ...]
Tree = frozenset[tuple[int, int]]
State = tuple[Word, ...]


def transposition_perm(d: int, a: int, b: int) -> tuple[int, ...]:
    p = list(range(d))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[x]] for x in range(len(p)))


def rename_word(p: tuple[int, ...], word: Word) -> Word:
    return tuple(tuple(sorted((p[a], p[b]))) for a, b in word)


ALL_LABEL_PERMS = tuple(itertools.permutations(range(5)))


def canonical_word(word: Word) -> Word:
    return min(rename_word(p, word) for p in ALL_LABEL_PERMS)


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


def apply_path(word: Word, path: tuple[int, ...]) -> Word:
    current = word
    for symbol in path:
        current = canonical_word(hurwitz(current, symbol))
    return current


def edge_perm(edge: Edge, d: int = 5) -> tuple[int, ...]:
    return transposition_perm(d, *edge)


def evaluates_to_identity(word: Word, d: int = 5) -> bool:
    value = tuple(range(d))
    for edge in word:
        value = compose(value, edge_perm(edge, d))
    return value == tuple(range(d))


def connected_support(word: Word, d: int = 5) -> bool:
    adj = [set() for _ in range(d)]
    for a, b in word:
        adj[a].add(b)
        adj[b].add(a)
    seen = {0}
    stack = [0]
    while stack:
        a = stack.pop()
        for b in adj[a]:
            if b not in seen:
                seen.add(b)
                stack.append(b)
    return len(seen) == d


def all_physical_z5_words():
    """Enumerate Z_5 by seven factors and the forced eighth factor."""
    d = 5
    identity = tuple(range(d))
    edges = tuple(itertools.combinations(range(d), 2))
    edge_to_perm = {edge: edge_perm(edge, d) for edge in edges}
    perm_to_edge = {perm: edge for edge, perm in edge_to_perm.items()}
    for prefix in itertools.product(edges, repeat=7):
        value = identity
        for edge in prefix:
            value = compose(value, edge_to_perm[edge])
        final_edge = perm_to_edge.get(value)
        if final_edge is None:
            continue
        word = prefix + (final_edge,)
        if connected_support(word, d):
            yield word


def enumerate_q5():
    representatives = set()
    physical_count = 0
    for word in all_physical_z5_words():
        physical_count += 1
        representatives.add(canonical_word(word))
    states = tuple(sorted(representatives))
    index = {word: i for i, word in enumerate(states)}
    return states, index, physical_count


def generator_action(states: tuple[Word, ...], index: dict[Word, int]):
    symbols = tuple(list(range(1, 8)) + list(range(-1, -8, -1)))
    actions = {}
    for symbol in symbols:
        image = array("H", (
            index[canonical_word(hurwitz(word, symbol))] for word in states
        ))
        assert len(set(image)) == len(states)
        actions[symbol] = image
    for slot in range(1, 8):
        plus, minus = actions[slot], actions[-slot]
        assert all(minus[plus[i]] == i and plus[minus[i]] == i for i in range(len(states)))
    return symbols, actions


def prufer_trees(d: int = 5):
    for code in itertools.product(range(1, d + 1), repeat=d - 2):
        degree = [0] + [1] * d
        for x in code:
            degree[x] += 1
        edges = []
        for x in code:
            leaf = min(v for v in range(1, d + 1) if degree[v] == 1)
            edges.append(tuple(sorted((leaf, x))))
            degree[leaf] -= 1
            degree[x] -= 1
        remaining = [v for v in range(1, d + 1) if degree[v] == 1]
        edges.append(tuple(sorted(remaining)))
        yield frozenset(edges)


def parent_map(tree: Tree, d: int = 5) -> dict[int, int]:
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


def hairy_incidence(tree: Tree, pi: tuple[int, ...], d: int = 5):
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


def boundary_tokens(incidence, d: int = 5):
    m = 2 * d - 2
    start = (("w", 1), 1)
    state = start
    seen = set()
    out = []
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        step = 1 if vertex[0] == "w" else -1
        label = 1 + ((incoming - 1 + step) % m)
        if label in incidence[vertex]:
            out.append(("side",))
            state = (incidence[vertex][label], label)
        else:
            out.append(("half", vertex[0], vertex[1], label))
            state = (vertex, label)
    assert state == start and len(out) == (2 * d - 1) * m
    return out


def close_hairy(tokens, d: int = 5) -> dict[int, int]:
    tokens = list(tokens)
    second_black = {}
    while True:
        positions = [j for j, token in enumerate(tokens) if token[0] == "half"]
        chosen = None
        for k, white_pos in enumerate(positions):
            black_pos = positions[(k + 1) % len(positions)]
            if tokens[white_pos][1] == "w" and tokens[black_pos][1] == "b":
                chosen = white_pos, black_pos
                break
        if chosen is None:
            break
        white_pos, black_pos = chosen
        tokens = tokens[white_pos:] + tokens[:white_pos]
        black_pos = (black_pos - white_pos) % len(tokens)
        white, black = tokens[0], tokens[black_pos]
        assert white[3] == black[3]
        distance = sum(token[0] == "side" for token in tokens[1:black_pos])
        assert distance in (1, 3)
        if distance == 3:
            second_black[white[3]] = black[2]
        tokens = [("side",)] + tokens[black_pos + 1 :]
    remaining = [token for token in tokens if token[0] == "half"]
    assert len(remaining) == 2 * d - 2
    assert all(token[1] == "w" for token in remaining)
    return second_black


def dps_word(tree: Tree, pi: tuple[int, ...], d: int = 5) -> Word:
    incidence, first_black = hairy_incidence(tree, pi, d)
    second_black = close_hairy(boundary_tokens(incidence, d), d)
    out = []
    for label in range(1, 2 * d - 1):
        a = first_black[label]
        b = second_black.get(label, d)
        assert a != b
        out.append(tuple(sorted((a - 1, b - 1))))
    return tuple(out)


def compatible_pi(word: Word, d: int = 5):
    root = d - 1
    choices = [tuple(x for x in edge if x != root) for edge in word]
    for assigned in itertools.product(*choices):
        if any(assigned.count(v) != 2 for v in range(d - 1)):
            continue
        labels = {
            v: [j + 1 for j, x in enumerate(assigned) if x == v]
            for v in range(d - 1)
        }
        for flips in itertools.product((0, 1), repeat=d - 1):
            pi = []
            for v in range(d - 1):
                pair = labels[v]
                pi.extend(pair if flips[v] == 0 else reversed(pair))
            yield tuple(pi)


def targeted_inverse(word: Word, trees: tuple[Tree, ...], d: int = 5):
    trials = 0
    for pi in compatible_pi(word, d):
        for tree in trees:
            trials += 1
            if dps_word(tree, pi, d) == word:
                return tree, pi, trials
    raise AssertionError("targeted DPS inverse failed")


def swap_values(pi: tuple[int, ...], i: int):
    return tuple(i + 1 if x == i else i if x == i + 1 else x for x in pi)


def sources() -> State:
    v = ((0, 1), (0, 1), (0, 2), (0, 2), (1, 3), (1, 3), (0, 4), (0, 4))
    u = ((0, 1), (0, 1), (0, 2), (0, 2), (0, 3), (0, 3), (0, 4), (0, 4))
    return canonical_word(v), canonical_word(u)


def named_targets():
    source = sources()
    trees = tuple(prufer_trees())
    descriptors = {}
    descriptor_rows = []
    for coordinate, word in enumerate(source):
        for root in range(5):
            relabel = transposition_perm(5, root, 4)
            physical = rename_word(relabel, word)
            tree, pi, trials = targeted_inverse(physical, trees)
            descriptors[coordinate, root] = tree, pi
            descriptor_rows.append({
                "coordinate": coordinate,
                "root": root,
                "tree": [list(edge) for edge in sorted(tree)],
                "pi": list(pi),
                "trials": trials,
            })
    occurrences: dict[State, list[dict[str, object]]] = defaultdict(list)
    for edit in range(1, 8):
        coordinate_targets = []
        for coordinate in range(2):
            root_targets = []
            for root in range(5):
                tree, pi = descriptors[coordinate, root]
                target = canonical_word(dps_word(tree, swap_values(pi, edit)))
                assert evaluates_to_identity(target) and connected_support(target)
                root_targets.append(target)
            coordinate_targets.append(root_targets)
        for root0 in range(5):
            for root1 in range(5):
                target = coordinate_targets[0][root0], coordinate_targets[1][root1]
                assert target[0] != target[1]
                occurrences[target].append({"edit": edit, "roots": [root0, root1]})
    assert len(occurrences) == 54
    return occurrences, descriptor_rows


def schreier_tree(start: int, symbols, actions):
    n = len(next(iter(actions.values())))
    parent = array("i", [-2]) * n
    parent_symbol = array("b", [0]) * n
    parent[start] = -1
    order = array("H", [start])
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        for symbol in symbols:
            nxt = actions[symbol][vertex]
            if parent[nxt] == -2:
                parent[nxt] = vertex
                parent_symbol[nxt] = symbol
                order.append(nxt)
                queue.append(nxt)
    assert len(order) == n
    return parent, parent_symbol, order


def tree_path(vertex: int, parent, parent_symbol) -> tuple[int, ...]:
    path = []
    while parent[vertex] != -1:
        path.append(parent_symbol[vertex])
        vertex = parent[vertex]
    return tuple(reversed(path))


def inverse_path(path: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(-symbol for symbol in reversed(path))


def apply_index(index: int, path: tuple[int, ...], actions) -> int:
    for symbol in path:
        index = actions[symbol][index]
    return index


def stabilizer_loops(start: int, symbols, actions, parent, parent_symbol, order):
    """All nontrivial Schreier fundamental loops at start."""
    paths = {vertex: tree_path(vertex, parent, parent_symbol) for vertex in order}
    loops = []
    seen_actions = set()
    for vertex in order:
        for symbol in symbols:
            nxt = actions[symbol][vertex]
            loop = paths[vertex] + (symbol,) + inverse_path(paths[nxt])
            assert apply_index(start, loop, actions) == start
            # Deduplicate by the induced permutation on Q5, not by word.
            action = bytes(apply_index(i, loop, actions) // 256 for i in ())
            key = tuple(apply_index(i, loop, actions) for i in range(len(order)))
            if key == tuple(range(len(order))) or key in seen_actions:
                continue
            seen_actions.add(key)
            loops.append(loop)
    return loops


def compact_stabilizer_generators(start, symbols, actions, parent, parent_symbol, order):
    """Greedily keep Schreier loops that enlarge the orbit of the second source."""
    tree_paths = {vertex: tree_path(vertex, parent, parent_symbol) for vertex in order}
    candidate_loops = []
    for vertex in order:
        for symbol in symbols:
            nxt = actions[symbol][vertex]
            # Tree edge in the discovery direction gives the empty loop.
            if parent[nxt] == vertex and parent_symbol[nxt] == symbol:
                continue
            loop = tree_paths[vertex] + (symbol,) + inverse_path(tree_paths[nxt])
            assert apply_index(start, loop, actions) == start
            candidate_loops.append(loop)
    return candidate_loops


def orbit_with_certificates(start: int, loop_words, actions):
    parent = {start: None}
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        for generator_id, loop in enumerate(loop_words):
            for orientation in (1, -1):
                word = loop if orientation == 1 else inverse_path(loop)
                nxt = apply_index(vertex, word, actions)
                if nxt not in parent:
                    parent[nxt] = vertex, generator_id, orientation
                    queue.append(nxt)
    return parent


def orbit_word(vertex: int, parent, loop_words):
    chunks = []
    while parent[vertex] is not None:
        previous, generator_id, orientation = parent[vertex]
        loop = loop_words[generator_id]
        chunks.append(loop if orientation == 1 else inverse_path(loop))
        vertex = previous
    return tuple(symbol for chunk in reversed(chunks) for symbol in chunk)


def classify(output: Path):
    states, index, physical_count = enumerate_q5()
    symbols, actions = generator_action(states, index)
    source_v, source_u = sources()
    source_v_id, source_u_id = index[source_v], index[source_u]
    parent, parent_symbol, order = schreier_tree(source_v_id, symbols, actions)
    assert len(order) == len(states)
    candidates = compact_stabilizer_generators(
        source_v_id, symbols, actions, parent, parent_symbol, order
    )

    # Incrementally add candidate Schreier loops until the second-source orbit
    # no longer grows through a full pass.  Retain only generators that enlarge it.
    retained = []
    orbit_parent = {source_u_id: None}
    for loop in candidates:
        before = len(orbit_parent)
        trial = orbit_with_certificates(source_u_id, retained + [loop], actions)
        if len(trial) > before:
            retained.append(loop)
            orbit_parent = trial
    # Exact closure and completeness audit under every Schreier generator.
    orbit_set = set(orbit_parent)
    failures = []
    for candidate_id, loop in enumerate(candidates):
        for vertex in orbit_set:
            if apply_index(vertex, loop, actions) not in orbit_set:
                failures.append((candidate_id, vertex))
                break
    assert not failures

    occurrences, descriptor_rows = named_targets()
    rows = []
    positives = 0
    negatives = 0
    for target_id, (target, target_occurrences) in enumerate(sorted(occurrences.items())):
        target_v, target_u = target
        target_v_id, target_u_id = index[target_v], index[target_u]
        alpha = tree_path(target_v_id, parent, parent_symbol)
        adjusted_u_id = apply_index(target_u_id, inverse_path(alpha), actions)
        if adjusted_u_id in orbit_parent:
            stabilizer_word = orbit_word(adjusted_u_id, orbit_parent, retained)
            route = stabilizer_word + alpha
            assert apply_index(source_v_id, route, actions) == target_v_id
            assert apply_index(source_u_id, route, actions) == target_u_id
            status = "reachable"
            positives += 1
        else:
            stabilizer_word = ()
            route = ()
            status = "unreachable"
            negatives += 1
        rows.append({
            "target_id": target_id,
            "status": status,
            "target_ids": [target_v_id, target_u_id],
            "occurrences": sorted(
                target_occurrences, key=lambda row: (row["edit"], row["roots"])
            ),
            "first_coordinate_tree_word": list(alpha),
            "adjusted_second_id": adjusted_u_id,
            "stabilizer_orbit_member": adjusted_u_id in orbit_set,
            "stabilizer_word": list(stabilizer_word),
            "route": list(route),
            "route_length": len(route) if status == "reachable" else None,
        })

    # Direct word replay, independent of index transition composition.
    replay_failures = []
    for row in rows:
        if row["status"] != "reachable":
            continue
        target_v_id, target_u_id = row["target_ids"]
        path = tuple(row["route"])
        if (
            index[apply_path(source_v, path)] != target_v_id
            or index[apply_path(source_u, path)] != target_u_id
        ):
            replay_failures.append(row["target_id"])
    assert not replay_failures

    orbit_bitmap = bytearray(len(states))
    for vertex in orbit_set:
        orbit_bitmap[vertex] = 1
    target_digest = hashlib.sha256(
        json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    result = {
        "experiment": "M191 exact d=5 synchronized quotient classification",
        "repository_base_commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
        "command": "python3 -B exact_classifier.py --output exact_results.json",
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "scope": "one exact Q5 action and 54 named width-two targets",
        "stale_m187_geometric_claims_used": False,
        "q5": {
            "physical_z5_words": physical_count,
            "quotient_size": len(states),
            "generator_count": len(symbols),
            "all_generator_bijections": True,
            "all_signed_inverse_pairs": True,
            "source_orbit_size": len(order),
        },
        "stabilizer": {
            "schreier_candidate_loops": len(candidates),
            "retained_orbit_generators": len(retained),
            "retained_generator_words": [list(loop) for loop in retained],
            "second_coordinate_orbit_size": len(orbit_set),
            "orbit_closed_under_all_schreier_loops": True,
            "orbit_bitmap_sha256": hashlib.sha256(orbit_bitmap).hexdigest(),
        },
        "named_targets": {
            "count": len(rows),
            "reachable": positives,
            "unreachable": negatives,
            "all_positive_routes_replayed": True,
            "classification_rows_sha256": target_digest,
            "rows": rows,
        },
        "certificate_logic": {
            "positive": "explicit chronological braid route directly replayed",
            "negative": (
                "inverse(first-coordinate tree word) sends target second ID "
                "outside exact source-stabilizer orbit; orbit closure checked "
                "under every Schreier fundamental loop"
            ),
        },
    }
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "q5": result["q5"],
        "stabilizer": {
            key: result["stabilizer"][key]
            for key in (
                "schreier_candidate_loops",
                "retained_orbit_generators",
                "second_coordinate_orbit_size",
                "orbit_closed_under_all_schreier_loops",
                "orbit_bitmap_sha256",
            )
        },
        "named_targets": {
            key: result["named_targets"][key]
            for key in (
                "count", "reachable", "unreachable",
                "all_positive_routes_replayed", "classification_rows_sha256"
            )
        },
    }, indent=2, sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("exact_results.json"))
    parser.add_argument("--gate-only", action="store_true")
    args = parser.parse_args()
    if args.gate_only:
        occurrences, descriptors = named_targets()
        print(json.dumps({
            "named_target_count": len(occurrences),
            "rooted_descriptor_count": len(descriptors),
            "criterion": (
                "target (v',u') reachable iff u' alpha(v')^-1 lies in "
                "Orb_Stab(v)(u), with alpha(v') the source-to-v' tree word"
            ),
            "next": "enumerate one Q5 quotient and its source stabilizer orbit",
        }, indent=2, sort_keys=True))
        return
    classify(args.output)


if __name__ == "__main__":
    main()
