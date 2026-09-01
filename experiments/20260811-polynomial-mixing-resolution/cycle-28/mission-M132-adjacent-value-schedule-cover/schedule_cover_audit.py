#!/usr/bin/env python3
"""Exact small-rank audit for DPS adjacent-value schedule metadata.

This file independently implements the accepted ``+`` DPS hairy-tree
closure, the descended physical maps tau_i, and signed right-Hurwitz moves.
It tests finite schedule libraries and, more importantly, searches for
paired-source subgroup obstructions inside natural polynomial-cardinality
metadata classes.  Finite rows are falsifiers/convention checks only.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
import subprocess
import time
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path


Edge = tuple[int, int]
Word = tuple[Edge, ...]
Tree = frozenset[tuple[int, int]]
Schedule = tuple[tuple[int, int], ...]  # one-based position, sign


@dataclass(frozen=True)
class Half:
    color: str
    vertex: int
    label: int


@dataclass(frozen=True)
class Side:
    kind: str
    label: int | None = None
    tail: tuple[str, int] | None = None
    head: tuple[str, int] | None = None


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return pq, so (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def transposition_perm(d: int, edge: Edge) -> tuple[int, ...]:
    a, b = edge
    out = list(range(d))
    out[a], out[b] = out[b], out[a]
    return tuple(out)


def evaluate(d: int, word: Word) -> tuple[int, ...]:
    out = tuple(range(d))
    for edge in word:
        out = compose(out, transposition_perm(d, edge))
    return out


def conjugate_edge(edge: Edge, by: Edge) -> Edge:
    a, b = edge
    x, y = by

    def image(z: int) -> int:
        return y if z == x else x if z == y else z

    return tuple(sorted((image(a), image(b))))


def hurwitz(word: Word, zero_position: int, sign: int) -> Word:
    a, b = word[zero_position], word[zero_position + 1]
    out = list(word)
    if sign == 1:
        out[zero_position : zero_position + 2] = [b, conjugate_edge(a, b)]
    elif sign == -1:
        out[zero_position : zero_position + 2] = [conjugate_edge(b, a), a]
    else:
        raise ValueError(sign)
    return tuple(out)


def apply_schedule(word: Word, schedule: Schedule) -> Word:
    out = word
    for one_position, sign in schedule:
        out = hurwitz(out, one_position - 1, sign)
    return out


def support_connected(d: int, word: Word) -> bool:
    adj = [[] for _ in range(d)]
    for a, b in word:
        adj[a].append(b)
        adj[b].append(a)
    seen = {0}
    todo = [0]
    while todo:
        x = todo.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return len(seen) == d


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
        x = todo.pop()
        for y in adj[x]:
            if y not in parent:
                parent[y] = x
                todo.append(y)
    return parent


def hairy_incidence(tree: Tree, pi: tuple[int, ...], d: int):
    parent = rooted_parent(tree, d)
    incidence: dict[tuple[str, int], dict[int, tuple[str, int]]] = defaultdict(dict)
    first_black: dict[int, int] = {}
    label_endpoints: dict[int, tuple[int, int]] = {}
    for black in range(1, d):
        white_parent = parent[black]
        pair = pi[2 * black - 2 : 2 * black]
        for label, white in ((pair[0], black), (pair[1], white_parent)):
            b_vertex = ("b", black)
            w_vertex = ("w", white)
            incidence[b_vertex][label] = w_vertex
            incidence[w_vertex][label] = b_vertex
            first_black[label] = black
            label_endpoints[label] = (black, white)
    return incidence, first_black, label_endpoints


def hairy_boundary(incidence, d: int) -> list[Half | Side]:
    m = 2 * d - 2
    start = (("w", 1), 1)
    state = start
    seen = set()
    out: list[Half | Side] = []
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        color, _ = vertex
        step = 1 if color == "w" else -1
        label = 1 + ((incoming - 1 + step) % m)
        if label in incidence[vertex]:
            head = incidence[vertex][label]
            out.append(Side("tree", label, vertex, head))
            state = (head, label)
        else:
            out.append(Half(color, vertex[1], label))
            state = (vertex, label)
    if state != start or len(out) != (2 * d - 1) * m:
        raise AssertionError("invalid hairy boundary")
    return out


def close_hairy(tokens: list[Half | Side], d: int):
    tokens = list(tokens)
    second_black: dict[int, int] = {}
    closure_distance: dict[int, int] = {}
    closure_events: dict[int, list[tuple[int, int, int, int]]] = defaultdict(list)
    closure_step = 0
    while True:
        positions = [j for j, token in enumerate(tokens) if isinstance(token, Half)]
        pair = None
        for k, white_position in enumerate(positions):
            black_position = positions[(k + 1) % len(positions)]
            white, black = tokens[white_position], tokens[black_position]
            if white.color == "w" and black.color == "b":
                pair = white_position, black_position
                break
        if pair is None:
            break
        white_position, black_position = pair
        tokens = tokens[white_position:] + tokens[:white_position]
        black_position = (black_position - white_position) % len(tokens)
        white, black = tokens[0], tokens[black_position]
        if white.label != black.label:
            raise AssertionError("unequal closure labels")
        distance = sum(isinstance(token, Side) for token in tokens[1:black_position])
        if distance not in (1, 3):
            raise AssertionError(("bad closure distance", distance))
        closure_distance[white.label] = distance
        closure_events[white.label].append(
            (closure_step, distance, white.vertex, black.vertex)
        )
        closure_step += 1
        if distance == 3:
            second_black[white.label] = black.vertex
        tokens = [Side("closure")] + tokens[black_position + 1 :]
    remaining = [token for token in tokens if isinstance(token, Half)]
    if len(remaining) != 2 * d - 2 or any(x.color != "w" for x in remaining):
        raise AssertionError("invalid final closure boundary")
    if sorted(x.label for x in remaining) != list(range(1, 2 * d - 1)):
        raise AssertionError("invalid final labels")
    return second_black, closure_distance, dict(closure_events)


def dps_record(tree: Tree, pi: tuple[int, ...], d: int):
    incidence, first_black, label_endpoints = hairy_incidence(tree, pi, d)
    boundary = hairy_boundary(incidence, d)
    side_positions: dict[int, list[int]] = defaultdict(list)
    for position, token in enumerate(boundary):
        if isinstance(token, Side) and token.kind == "tree":
            assert token.label is not None
            side_positions[token.label].append(position)
    if any(len(side_positions[label]) != 2 for label in range(1, 2 * d - 1)):
        raise AssertionError("each hairy edge should be traversed twice")
    second_black, closure_distance, closure_events = close_hairy(boundary, d)
    word = []
    for label in range(1, 2 * d - 1):
        a = first_black[label]
        b = second_black.get(label, d)
        if a == b:
            raise AssertionError("degenerate transposition")
        word.append(tuple(sorted((a - 1, b - 1))))
    contour = {
        "side_positions": {label: tuple(rows) for label, rows in side_positions.items()},
        "closure_events": closure_events,
    }
    return tuple(word), label_endpoints, closure_distance, first_black, contour


def swap_adjacent_values(pi: tuple[int, ...], i: int) -> tuple[int, ...]:
    return tuple(i + 1 if x == i else i if x == i + 1 else x for x in pi)


def shortest_schedule(
    words: tuple[Word, ...], index: dict[Word, int], source: int, target: int
) -> Schedule:
    if source == target:
        return ()
    m = len(words[0])
    parent: dict[int, tuple[int, tuple[int, int]]] = {}
    seen = {source}
    todo = deque([source])
    while todo:
        u = todo.popleft()
        for zero_position in range(m - 1):
            for sign in (1, -1):
                v = index[hurwitz(words[u], zero_position, sign)]
                if v in seen:
                    continue
                seen.add(v)
                parent[v] = (u, (zero_position + 1, sign))
                if v == target:
                    path = []
                    cursor = v
                    while cursor != source:
                        cursor, action = parent[cursor]
                        path.append(action)
                    path.reverse()
                    return tuple(path)
                todo.append(v)
    raise AssertionError("disconnected physical Hurwitz graph")


def pair_subgroup(d: int, left: Word, right: Word):
    identity = tuple(range(d))
    generators = tuple(
        (transposition_perm(d, a), transposition_perm(d, b))
        for a, b in zip(left, right)
    )
    seen = {(identity, identity)}
    todo = deque([(identity, identity)])
    while todo:
        p, q = todo.popleft()
        for g, h in generators:
            new = (compose(p, g), compose(q, h))
            if new not in seen:
                seen.add(new)
                todo.append(new)
    return frozenset(seen)


def relation_type(a: Edge, b: Edge) -> str:
    if a == b:
        return "equal"
    common = len(set(a) & set(b))
    return "incident" if common == 1 else "disjoint"


def serialize_word(word: Word):
    return [[a + 1, b + 1] for a, b in word]


def serialize_schedule(schedule: Schedule):
    return [[position, sign] for position, sign in schedule]


def full_twist_schedule(m: int) -> Schedule:
    # M122's C_L^(L+1) on positions 2,...,m, where L=m-2.
    sweep = tuple((position, 1) for position in range(2, m))
    return sweep * (m - 1)


def build_rank(d: int):
    m = 2 * d - 2
    preimages: dict[Word, list[tuple[Tree, tuple[int, ...], dict, dict, dict, dict]]] = defaultdict(list)
    for tree in cayley_trees(d):
        for pi in itertools.permutations(range(1, m + 1)):
            word, endpoints, closure, first_black, contour = dps_record(tree, pi, d)
            if evaluate(d, word) != tuple(range(d)) or not support_connected(d, word):
                raise AssertionError("DPS target failure")
            preimages[word].append((tree, pi, endpoints, closure, first_black, contour))
    if set(map(len, preimages.values())) != {d}:
        raise AssertionError("root quotient failure")
    words = tuple(sorted(preimages))
    index = {word: j for j, word in enumerate(words)}
    representatives = {word: min(rows, key=lambda x: (tuple(sorted(x[0])), x[1])) for word, rows in preimages.items()}
    target_maps: dict[int, tuple[int, ...]] = {}
    for i in range(1, m):
        image = []
        for word in words:
            targets = {
                dps_record(tree, swap_adjacent_values(pi, i), d)[0]
                for tree, pi, _endpoints, _closure, _first, _contour in preimages[word]
            }
            if len(targets) != 1:
                raise AssertionError("tau_i does not descend")
            image.append(index[next(iter(targets))])
        if len(set(image)) != len(words) or any(image[image[x]] != x for x in range(len(words))):
            raise AssertionError("tau_i is not an involutive permutation")
        target_maps[i] = tuple(image)
    return words, index, preimages, representatives, target_maps


def metadata_keys(
    word: Word,
    representative,
    adjacent_index: int,
):
    tree, pi, endpoints, closure, first_black, contour = representative
    i = adjacent_index
    physical_pair = (word[i - 1], word[i])
    hairy_pair = (endpoints[i], endpoints[i + 1])
    oriented_factor_pair = (
        (first_black[i] - 1, next(x for x in word[i - 1] if x != first_black[i] - 1)),
        (first_black[i + 1] - 1, next(x for x in word[i] if x != first_black[i + 1] - 1)),
    )

    def closure_scalar(label: int):
        events = contour["closure_events"][label]
        distance_counts = Counter(event[1] for event in events)
        distance_three_steps = tuple(event[0] for event in events if event[1] == 3)
        return (
            distance_counts[1],
            distance_counts[3],
            events[0][0],
            events[-1][0],
            distance_three_steps,
        )

    boundary_positions = (
        contour["side_positions"][i],
        contour["side_positions"][i + 1],
    )
    closure_scalars = (closure_scalar(i), closure_scalar(i + 1))
    return {
        "pair_relation": (relation_type(*physical_pair),),
        "exact_physical_pair": physical_pair,
        "hairy_edge_endpoints": hairy_pair,
        "oriented_factor_pair": oriented_factor_pair,
        "endpoints_plus_closure": (hairy_pair, closure[i], closure[i + 1]),
        "all_two_label_local_data": (
            physical_pair,
            hairy_pair,
            oriented_factor_pair,
            closure[i],
            closure[i + 1],
        ),
        "boundary_positions": boundary_positions,
        "closure_scalar_history": closure_scalars,
        "polynomial_contour_summary": (
            physical_pair,
            hairy_pair,
            oriented_factor_pair,
            boundary_positions,
            closure_scalars,
        ),
    }


def first_metadata_obstruction(
    d: int,
    words: tuple[Word, ...],
    target: tuple[int, ...],
    keys: list[object],
    max_pairs: int | None,
    subgroup_cache: dict[tuple[int, int], frozenset],
):
    classes: dict[object, list[int]] = defaultdict(list)
    for source, key in enumerate(keys):
        classes[key].append(source)
    tested = 0
    for key in sorted(classes, key=repr):
        sources = classes[key]
        for left_offset, left in enumerate(sources):
            for right in sources[left_offset + 1 :]:
                tested += 1
                if max_pairs is not None and tested > max_pairs:
                    return None, Counter(map(len, classes.values())), tested - 1, False
                source_key = (left, right)
                target_key = (target[left], target[right])
                if source_key not in subgroup_cache:
                    subgroup_cache[source_key] = pair_subgroup(
                        d, words[left], words[right]
                    )
                if target_key not in subgroup_cache:
                    subgroup_cache[target_key] = pair_subgroup(
                        d, words[target[left]], words[target[right]]
                    )
                before = subgroup_cache[source_key]
                after = subgroup_cache[target_key]
                if before != after:
                    return {
                        "metadata_key": repr(key),
                        "class_size": len(sources),
                        "pairs_tested_to_first_obstruction": tested,
                        "source_indices": [left, right],
                        "source_subgroup_order": len(before),
                        "target_subgroup_order": len(after),
                        "source_words": [serialize_word(words[left]), serialize_word(words[right])],
                        "target_words": [serialize_word(words[target[left]]), serialize_word(words[target[right]])],
                    }, Counter(map(len, classes.values())), tested, False
    return None, Counter(map(len, classes.values())), tested, True


def compose_action(left: tuple[int, ...], right: tuple[int, ...]):
    """Return the action table for left after right."""
    return tuple(left[right[x]] for x in range(len(right)))


def maximum_clique_bitset(adjacency: list[int]) -> list[int]:
    best: list[int] = []

    def visit(chosen: list[int], candidates: int, excluded: int) -> None:
        nonlocal best
        if not candidates and not excluded:
            if len(chosen) > len(best):
                best = chosen[:]
            return
        if len(chosen) + candidates.bit_count() <= len(best):
            return
        union = candidates | excluded
        pivot = max(
            (v for v in range(len(adjacency)) if (union >> v) & 1),
            key=lambda v: (adjacency[v] & candidates).bit_count(),
            default=0,
        )
        branch = candidates & ~adjacency[pivot]
        while branch:
            bit = branch & -branch
            vertex = bit.bit_length() - 1
            visit(
                chosen + [vertex],
                candidates & adjacency[vertex],
                excluded & adjacency[vertex],
            )
            candidates ^= bit
            excluded |= bit
            branch ^= bit

    visit([], (1 << len(adjacency)) - 1, 0)
    return best


def exact_chromatic_number(adjacency: list[int]):
    """Exact DSATUR branch-and-bound; used only on the 24 d=3 vertices."""
    n = len(adjacency)
    degrees = [row.bit_count() for row in adjacency]
    greedy_colors = [-1] * n
    for vertex in sorted(range(n), key=lambda v: -degrees[v]):
        forbidden = {
            greedy_colors[u]
            for u in range(n)
            if (adjacency[vertex] >> u) & 1 and greedy_colors[u] >= 0
        }
        color = 0
        while color in forbidden:
            color += 1
        greedy_colors[vertex] = color
    best = max(greedy_colors) + 1
    best_colors = greedy_colors[:]
    colors = [-1] * n

    def search(colored: int, used: int) -> None:
        nonlocal best, best_colors
        if colored == n:
            if used < best:
                best = used
                best_colors = colors[:]
            return
        if used >= best:
            return
        uncolored = [v for v in range(n) if colors[v] < 0]
        vertex = max(
            uncolored,
            key=lambda v: (
                len(
                    {
                        colors[u]
                        for u in range(n)
                        if (adjacency[v] >> u) & 1 and colors[u] >= 0
                    }
                ),
                degrees[v],
            ),
        )
        forbidden = {
            colors[u]
            for u in range(n)
            if (adjacency[vertex] >> u) & 1 and colors[u] >= 0
        }
        # Existing colors, plus one new color only if it can beat best.
        choices = list(range(used))
        if used + 1 < best:
            choices.append(used)
        for color in choices:
            if color in forbidden:
                continue
            colors[vertex] = color
            search(colored + 1, max(used, color + 1))
            colors[vertex] = -1

    search(0, 0)
    return best, best_colors


def exact_d3_action_and_conflict(
    words: tuple[Word, ...],
    index: dict[Word, int],
    representatives,
    target_maps: dict[int, tuple[int, ...]],
):
    if len(words) != 24 or len(words[0]) != 4:
        raise AssertionError("this complete audit is specific to d=3")
    generator_descriptors = tuple(
        (position, sign) for position in range(3) for sign in (1, -1)
    )
    generators = tuple(
        tuple(index[hurwitz(word, position, sign)] for word in words)
        for position, sign in generator_descriptors
    )
    identity = tuple(range(len(words)))
    parent: dict[tuple[int, ...], tuple[tuple[int, ...], int] | None] = {
        identity: None
    }
    todo = deque([identity])
    while todo:
        action = todo.popleft()
        for generator_index, generator in enumerate(generators):
            new_action = compose_action(generator, action)
            if new_action not in parent:
                parent[new_action] = (action, generator_index)
                todo.append(new_action)

    def shortest_word(action: tuple[int, ...]) -> Schedule:
        out = []
        cursor = action
        while parent[cursor] is not None:
            previous, generator_index = parent[cursor]
            position, sign = generator_descriptors[generator_index]
            out.append((position + 1, sign))
            cursor = previous
        out.reverse()
        return tuple(out)

    rows = []
    full_mask = (1 << len(words)) - 1
    for adjacent_index, target in sorted(target_maps.items()):
        agreement: dict[int, Schedule] = {}
        for action in parent:
            mask = sum(
                (action[source] == target[source]) << source
                for source in range(len(words))
            )
            if mask:
                schedule = shortest_word(action)
                if mask not in agreement or len(schedule) < len(agreement[mask]):
                    agreement[mask] = schedule
        frontier = {0}
        minimum_cover = None
        for depth in range(1, len(words) + 1):
            frontier = {covered | mask for covered in frontier for mask in agreement}
            if full_mask in frontier:
                minimum_cover = depth
                break
        if minimum_cover is None:
            raise AssertionError("transitivity should supply a finite cover")

        metadata = [
            metadata_keys(word, representatives[word], adjacent_index) for word in words
        ]
        realizability = {}
        for name in metadata[0]:
            classes: dict[object, int] = defaultdict(int)
            for source, item in enumerate(metadata):
                classes[item[name]] |= 1 << source
            unrealized = [
                key
                for key, class_mask in classes.items()
                if not any(class_mask & ~agreement_mask == 0 for agreement_mask in agreement)
            ]
            realizability[name] = {
                "class_count": len(classes),
                "every_class_contained_in_one_agreement_set": not unrealized,
                "unrealized_class_count": len(unrealized),
                "first_unrealized_key": repr(sorted(unrealized, key=repr)[0]) if unrealized else None,
            }

        conflict = [0] * len(words)
        edge_count = 0
        for left in range(len(words)):
            for right in range(left + 1, len(words)):
                if pair_subgroup(3, words[left], words[right]) != pair_subgroup(
                    3, words[target[left]], words[target[right]]
                ):
                    conflict[left] |= 1 << right
                    conflict[right] |= 1 << left
                    edge_count += 1
        clique = maximum_clique_bitset(conflict)
        chromatic, coloring = exact_chromatic_number(conflict)
        rows.append(
            {
                "adjacent_value_index": adjacent_index,
                "action_image_order": len(parent),
                "distinct_nonempty_agreement_masks": len(agreement),
                "maximum_one_schedule_agreement": max(mask.bit_count() for mask in agreement),
                "exact_minimum_schedule_cover": minimum_cover,
                "metadata_one_schedule_realizability": realizability,
                "schedule_conflict_graph": {
                    "vertices": len(words),
                    "edges": edge_count,
                    "maximum_clique_size": len(clique),
                    "one_maximum_clique_sources": [serialize_word(words[x]) for x in clique],
                    "chromatic_number": chromatic,
                    "color_class_size_histogram": dict(
                        sorted(Counter(Counter(coloring).values()).items())
                    ),
                    "interpretation": (
                        "Every fixed-schedule agreement set is independent, so the "
                        "chromatic number is a schedule-cover lower bound. The converse "
                        "need not hold because an arbitrary independent set need not be "
                        "simultaneously realizable by one braid."
                    ),
                },
            }
        )
    return {"complete": True, "rows": rows}


def audit_rank(d: int, do_paths: bool, max_metadata_pairs: int | None) -> dict:
    words, index, preimages, representatives, target_maps = build_rank(d)
    m = 2 * d - 2
    row = {
        "d": d,
        "m": m,
        "z_size": len(words),
        "rooted_pairs": sum(map(len, preimages.values())),
        "root_fiber_histogram": dict(sorted(Counter(map(len, preimages.values())).items())),
        "identity_and_connected_failures": 0,
        "adjacent_rows": [],
    }
    subgroup_cache: dict[tuple[int, int], frozenset] = {}
    if d == 3:
        row["complete_d3_action_and_conflict"] = exact_d3_action_and_conflict(
            words, index, representatives, target_maps
        )
    for adjacent_index, target in sorted(target_maps.items()):
        metadata = [metadata_keys(word, representatives[word], adjacent_index) for word in words]
        metadata_rows = {}
        for name in metadata[0]:
            obstruction, class_sizes, tested, exhaustive = first_metadata_obstruction(
                d,
                words,
                target,
                [item[name] for item in metadata],
                max_metadata_pairs,
                subgroup_cache,
            )
            metadata_rows[name] = {
                "number_of_classes": len(set(item[name] for item in metadata)),
                "class_size_histogram": dict(sorted(class_sizes.items())),
                "source_pairs_tested": tested,
                "search_exhaustive": exhaustive,
                "paired_source_obstruction": obstruction,
            }
            if obstruction is not None:
                certificates = []
                for source in obstruction["source_indices"]:
                    tree, pi, _endpoints, _closure, _first, _contour = representatives[
                        words[source]
                    ]
                    certificates.append(
                        {
                            "tree": [list(edge) for edge in sorted(tree)],
                            "pi": list(pi),
                            "swapped_pi": list(
                                swap_adjacent_values(pi, adjacent_index)
                            ),
                        }
                    )
                obstruction["canonical_dps_certificates"] = certificates
        adjacent_row = {
            "adjacent_value_index": adjacent_index,
            "physical_source_count": len(words),
            "metadata_audits": metadata_rows,
            "single_action_agreement_counts": {},
        }
        for zero_position in range(m - 1):
            for sign in (1, -1):
                schedule = ((zero_position + 1, sign),)
                count = sum(index[apply_schedule(word, schedule)] == target[s] for s, word in enumerate(words))
                if count:
                    adjacent_row["single_action_agreement_counts"][f"R{zero_position + 1}^{sign}"] = count
        twist = full_twist_schedule(m)
        twist_sources = [
            s for s, word in enumerate(words)
            if word[0] == word[1] and index[apply_schedule(word, twist)] == target[s]
        ]
        square_prefix_sources = sum(word[0] == word[1] for word in words)
        adjacent_row["square_prefix_full_twist"] = {
            "scheduled_length": len(twist),
            "square_prefix_source_count": square_prefix_sources,
            "agreement_within_square_prefix": len(twist_sources),
        }
        if do_paths:
            schedules = []
            distance_histogram = Counter()
            for source, endpoint in enumerate(target):
                schedule = shortest_schedule(words, index, source, endpoint)
                schedules.append(schedule)
                distance_histogram[len(schedule)] += 1
            library = tuple(sorted(set(schedules), key=lambda x: (len(x), x)))
            masks = []
            for schedule in library:
                mask = frozenset(
                    source
                    for source, word in enumerate(words)
                    if index[apply_schedule(word, schedule)] == target[source]
                )
                if mask:
                    masks.append((schedule, mask))
            uncovered = set(range(len(words)))
            greedy = []
            while uncovered:
                schedule, mask = max(
                    masks,
                    key=lambda item: (len(item[1] & uncovered), -len(item[0]), item[0]),
                )
                newly = mask & uncovered
                if not newly:
                    raise AssertionError("canonical library failed to cover")
                greedy.append((schedule, len(mask), len(newly)))
                uncovered -= newly
            adjacent_row["canonical_shortest_schedule_library"] = {
                "distance_histogram": dict(sorted(distance_histogram.items())),
                "distinct_schedules": len(library),
                "maximum_agreement_of_library_member": max(len(mask) for _schedule, mask in masks),
                "greedy_cover_class_count": len(greedy),
                "greedy_cover_max_schedule_length": max(len(schedule) for schedule, _a, _n in greedy),
                "greedy_cover": [
                    {
                        "schedule": serialize_schedule(schedule),
                        "total_agreement": total,
                        "newly_assigned": newly,
                    }
                    for schedule, total, newly in greedy
                ],
            }
        row["adjacent_rows"].append(adjacent_row)
    return row


def git_commit() -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"], text=True, capture_output=True, check=True
    ).stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", nargs="+", type=int, default=[3, 4])
    parser.add_argument("--paths-through-d", type=int, default=4)
    parser.add_argument("--max-metadata-pairs", type=int, default=5000)
    parser.add_argument("--output", type=Path, default=Path("results.json"))
    args = parser.parse_args()
    start = time.time()
    rows = [
        audit_rank(
            d,
            d <= args.paths_through_d,
            None if args.max_metadata_pairs < 0 else args.max_metadata_pairs,
        )
        for d in args.d
    ]
    payload = {
        "experiment": "M132 adjacent-value schedule metadata audit",
        "claim_tested": (
            "Natural polynomial-cardinality two-label metadata supports one fixed "
            "signed braid schedule per class; canonical finite covers calibrate d=3,4."
        ),
        "verdict": (
            "REFUTE_ONE_SCHEDULE_PER_TESTED_POLYNOMIAL_CONTOUR_KEY; "
            "GENERAL_ADJACENT_VALUE_POLYNOMIAL_SCHEDULE_COVER_UNRESOLVED"
        ),
        "tested_metadata_range_bound": (
            "E^2 [d(d-1)]^4 B^4 (S+1)^10 = O(d^40), "
            "E=binom(d,2), B=(2d-1)(2d-2), S=(d-2)(2d-2)"
        ),
        "target": "uniform physical Z_d via the constant-d rooted DPS lift",
        "composition_convention": "(pq)(x)=p(q(x)); displayed factors multiply left-to-right",
        "hurwitz_convention": "R_j(a,b)=(b,bab), R_j^-1(a,b)=(aba,a)",
        "commit": git_commit(),
        "python": platform.python_version(),
        "nonstandard_dependencies": {},
        "seed": None,
        "deterministic": True,
        "argv": list(__import__("sys").argv),
        "elapsed_seconds": time.time() - start,
        "rows": rows,
        "scope_warning": (
            "Finite d=3,4 covers are not asymptotic. A paired-source obstruction "
            "refutes only the named metadata class, not every polynomial schedule cover."
        ),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
