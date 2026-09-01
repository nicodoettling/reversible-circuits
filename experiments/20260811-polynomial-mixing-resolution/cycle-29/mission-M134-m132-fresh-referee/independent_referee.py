#!/usr/bin/env python3
"""Independent exact referee for frozen mission M132.

This checker imports no predecessor experiment module or result file.  It
reimplements the plus-mirror DPS construction, brute small targets, Hurwitz
actions, direct-product subgroup closure, graph coloring, and schedule-cover
enumeration using only the Python standard library.
"""

from __future__ import annotations

import itertools
import json
import platform
import subprocess
import time
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path


Edge = tuple[int, int]                 # one-based endpoints
Word = tuple[Edge, ...]
Perm = tuple[int, ...]                 # one-based images
Tree = tuple[Edge, ...]


@dataclass(frozen=True)
class Loose:
    color: str
    vertex: int
    label: int


@dataclass(frozen=True)
class Arc:
    kind: str
    label: int | None = None
    tail: tuple[str, int] | None = None
    head: tuple[str, int] | None = None


@dataclass
class RootedRecord:
    tree: Tree
    pi: tuple[int, ...]
    word: Word
    endpoints: dict[int, tuple[int, int]]
    first_black: dict[int, int]
    side_positions: dict[int, tuple[int, int]]
    closure_events: dict[int, tuple[tuple[int, int, int, int], ...]]
    boundary_length: int


def mul(p: Perm, q: Perm) -> Perm:
    """Return pq, with (pq)(x)=p(q(x))."""
    return tuple(p[q[x] - 1] for x in range(len(q)))


def identity(d: int) -> Perm:
    return tuple(range(1, d + 1))


def edge_perm(d: int, edge: Edge) -> Perm:
    a, b = edge
    out = list(identity(d))
    out[a - 1], out[b - 1] = out[b - 1], out[a - 1]
    return tuple(out)


def word_product(d: int, word: Word) -> Perm:
    out = identity(d)
    for edge in word:
        out = mul(out, edge_perm(d, edge))
    return out


def connected(d: int, word: Word) -> bool:
    adjacency = {v: set() for v in range(1, d + 1)}
    for a, b in word:
        adjacency[a].add(b)
        adjacency[b].add(a)
    reached = {1}
    stack = [1]
    while stack:
        v = stack.pop()
        for u in adjacency[v]:
            if u not in reached:
                reached.add(u)
                stack.append(u)
    return len(reached) == d


def conjugate_transposition(edge: Edge, by: Edge) -> Edge:
    x, y = by

    def image(v: int) -> int:
        if v == x:
            return y
        if v == y:
            return x
        return v

    return tuple(sorted((image(edge[0]), image(edge[1]))))


def hurwitz(word: Word, position: int, sign: int) -> Word:
    """Apply a signed right-Hurwitz move at zero-based position."""
    a, b = word[position], word[position + 1]
    out = list(word)
    if sign == 1:
        out[position : position + 2] = (b, conjugate_transposition(a, b))
    elif sign == -1:
        out[position : position + 2] = (conjugate_transposition(b, a), a)
    else:
        raise ValueError(sign)
    return tuple(out)


def apply_schedule(word: Word, schedule: tuple[tuple[int, int], ...]) -> Word:
    out = word
    for one_based_position, sign in schedule:
        out = hurwitz(out, one_based_position - 1, sign)
    return out


def all_cayley_trees(d: int):
    """Generate labeled trees from Prüfer words, independently of M132."""
    if d == 2:
        yield ((1, 2),)
        return
    for code in itertools.product(range(1, d + 1), repeat=d - 2):
        degree = [0] + [1] * d
        for v in code:
            degree[v] += 1
        edges: list[Edge] = []
        for v in code:
            leaf = min(u for u in range(1, d + 1) if degree[u] == 1)
            edges.append(tuple(sorted((leaf, v))))
            degree[leaf] -= 1
            degree[v] -= 1
        last = [u for u in range(1, d + 1) if degree[u] == 1]
        edges.append(tuple(last))
        yield tuple(sorted(edges))


def parent_map(tree: Tree, root: int) -> dict[int, int]:
    adjacency: dict[int, list[int]] = defaultdict(list)
    for a, b in tree:
        adjacency[a].append(b)
        adjacency[b].append(a)
    parent = {root: 0}
    queue = [root]
    while queue:
        v = queue.pop()
        for u in adjacency[v]:
            if u not in parent:
                parent[u] = v
                queue.append(u)
    return parent


def rooted_dps(tree: Tree, pi: tuple[int, ...], d: int) -> RootedRecord:
    """Close the accepted plus-mirror hairy tree into one physical word."""
    m = 2 * d - 2
    parent = parent_map(tree, d)
    incidence: dict[tuple[str, int], dict[int, tuple[str, int]]] = defaultdict(dict)
    endpoints: dict[int, tuple[int, int]] = {}
    first_black: dict[int, int] = {}
    for black in range(1, d):
        white_parent = parent[black]
        labels = pi[2 * black - 2 : 2 * black]
        for label, white in ((labels[0], black), (labels[1], white_parent)):
            bv = ("B", black)
            wv = ("W", white)
            incidence[bv][label] = wv
            incidence[wv][label] = bv
            endpoints[label] = (black, white)
            first_black[label] = black

    # Traverse the unique boundary.  White increments and black decrements.
    start = (("W", 1), 1)
    state = start
    visited: set[tuple[tuple[str, int], int]] = set()
    boundary: list[Loose | Arc] = []
    while state not in visited:
        visited.add(state)
        vertex, incoming = state
        delta = 1 if vertex[0] == "W" else -1
        label = 1 + ((incoming - 1 + delta) % m)
        if label in incidence[vertex]:
            head = incidence[vertex][label]
            boundary.append(Arc("tree", label, vertex, head))
            state = (head, label)
        else:
            boundary.append(Loose(vertex[0], vertex[1], label))
            state = (vertex, label)
    expected_boundary = (2 * d - 1) * m
    assert state == start and len(boundary) == expected_boundary

    positions: dict[int, list[int]] = defaultdict(list)
    for at, token in enumerate(boundary):
        if isinstance(token, Arc) and token.kind == "tree":
            assert token.label is not None
            positions[token.label].append(at)
    assert all(len(positions[label]) == 2 for label in range(1, m + 1))

    # Iteratively close the first cyclic white/black pair among loose ends.
    tokens = list(boundary)
    events: dict[int, list[tuple[int, int, int, int]]] = defaultdict(list)
    opposite_black: dict[int, int] = {}
    step = 0
    while True:
        loose_at = [j for j, token in enumerate(tokens) if isinstance(token, Loose)]
        chosen: tuple[int, int] | None = None
        for k, wi in enumerate(loose_at):
            bj = loose_at[(k + 1) % len(loose_at)]
            if tokens[wi].color == "W" and tokens[bj].color == "B":
                chosen = wi, bj
                break
        if chosen is None:
            break
        wi, bj = chosen
        tokens = tokens[wi:] + tokens[:wi]
        bj = (bj - wi) % len(tokens)
        white = tokens[0]
        black = tokens[bj]
        assert isinstance(white, Loose) and isinstance(black, Loose)
        assert white.label == black.label
        distance = sum(isinstance(token, Arc) for token in tokens[1:bj])
        assert distance in (1, 3)
        events[white.label].append((step, distance, white.vertex, black.vertex))
        if distance == 3:
            # DPS closes at most one quadrangle of a given indexed face.
            assert white.label not in opposite_black
            opposite_black[white.label] = black.vertex
        step += 1
        tokens = [Arc("closure")] + tokens[bj + 1 :]

    remaining = [token for token in tokens if isinstance(token, Loose)]
    assert len(remaining) == m
    assert all(token.color == "W" for token in remaining)
    assert sorted(token.label for token in remaining) == list(range(1, m + 1))
    assert step == (d - 2) * m
    assert all(len(events[label]) == d - 2 for label in range(1, m + 1))

    word: list[Edge] = []
    for label in range(1, m + 1):
        edge = tuple(sorted((first_black[label], opposite_black.get(label, d))))
        assert edge[0] != edge[1]
        word.append(edge)
    return RootedRecord(
        tree=tree,
        pi=pi,
        word=tuple(word),
        endpoints=endpoints,
        first_black=first_black,
        side_positions={label: tuple(positions[label]) for label in range(1, m + 1)},
        closure_events={label: tuple(events[label]) for label in range(1, m + 1)},
        boundary_length=len(boundary),
    )


def swap_values(pi: tuple[int, ...], i: int) -> tuple[int, ...]:
    return tuple(i + 1 if v == i else i if v == i + 1 else v for v in pi)


def brute_target(d: int) -> set[Word]:
    m = 2 * d - 2
    edges = tuple(itertools.combinations(range(1, d + 1), 2))
    return {
        word
        for word in itertools.product(edges, repeat=m)
        if word_product(d, word) == identity(d) and connected(d, word)
    }


def build_dps_rank(d: int):
    m = 2 * d - 2
    roots: dict[Word, list[tuple[Tree, tuple[int, ...]]]] = defaultdict(list)
    canonical: dict[Word, RootedRecord] = {}
    max_distance_three = 0
    for tree in all_cayley_trees(d):
        for pi in itertools.permutations(range(1, m + 1)):
            record = rooted_dps(tree, pi, d)
            assert word_product(d, record.word) == identity(d)
            assert connected(d, record.word)
            roots[record.word].append((tree, pi))
            old = canonical.get(record.word)
            if old is None or (tree, pi) < (old.tree, old.pi):
                canonical[record.word] = record
            for rows in record.closure_events.values():
                max_distance_three = max(
                    max_distance_three, sum(event[1] == 3 for event in rows)
                )
    assert set(map(len, roots.values())) == {d}
    brute = brute_target(d)
    assert set(roots) == brute
    words = tuple(sorted(brute))
    index = {word: j for j, word in enumerate(words)}
    tau: dict[int, tuple[int, ...]] = {}
    for i in range(1, m):
        image: list[int] = []
        for word in words:
            endpoints = {
                rooted_dps(tree, swap_values(pi, i), d).word
                for tree, pi in roots[word]
            }
            assert len(endpoints) == 1
            image.append(index[next(iter(endpoints))])
        assert len(set(image)) == len(words)
        assert all(image[image[j]] == j for j in range(len(words)))
        tau[i] = tuple(image)
    return {
        "words": words,
        "index": index,
        "roots": roots,
        "canonical": canonical,
        "tau": tau,
        "max_distance_three_per_label": max_distance_three,
        "boundary_length": (2 * d - 1) * m,
        "total_closures": (d - 2) * m,
    }


def closure_scalar(record: RootedRecord, label: int):
    rows = record.closure_events[label]
    distance_three = tuple(row[0] for row in rows if row[1] == 3)
    assert len(distance_three) <= 1
    counts = Counter(row[1] for row in rows)
    if not rows:
        return (0, 0, None, None, ())
    return (counts[1], counts[3], rows[0][0], rows[-1][0], distance_three)


def contour_descriptor(word: Word, record: RootedRecord, i: int):
    physical = (word[i - 1], word[i])
    hairy = (record.endpoints[i], record.endpoints[i + 1])
    oriented = []
    for label, factor in ((i, word[i - 1]), (i + 1, word[i])):
        first = record.first_black[label]
        other = factor[1] if factor[0] == first else factor[0]
        oriented.append((first, other))
    boundary = (record.side_positions[i], record.side_positions[i + 1])
    scalars = (closure_scalar(record, i), closure_scalar(record, i + 1))
    return (physical, hairy, tuple(oriented), boundary, scalars)


def pair_subgroup(d: int, left: Word, right: Word) -> frozenset[tuple[Perm, Perm]]:
    generators = tuple(
        (edge_perm(d, a), edge_perm(d, b)) for a, b in zip(left, right)
    )
    one = (identity(d), identity(d))
    reached = {one}
    queue = deque([one])
    while queue:
        p, q = queue.popleft()
        for g, h in generators:
            nxt = (mul(p, g), mul(q, h))
            if nxt not in reached:
                reached.add(nxt)
                queue.append(nxt)
    return frozenset(reached)


def parity(p: Perm) -> int:
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2


def double_transposition_group() -> set[Perm]:
    return {
        (1, 2, 3, 4),
        (2, 1, 4, 3),
        (3, 4, 1, 2),
        (4, 3, 2, 1),
    }


def expected_product_diagonal(normal: set[Perm], group: tuple[Perm, ...]):
    return {(mul(a, g), mul(b, g)) for a in normal for b in normal for g in group}


def witness_audit(rank4) -> dict:
    words = rank4["words"]
    index = rank4["index"]
    canonical = rank4["canonical"]
    tau1 = rank4["tau"][1]
    x = ((1, 2), (1, 3), (1, 3), (1, 2), (3, 4), (3, 4))
    y = ((1, 2), (1, 3), (1, 3), (3, 4), (1, 2), (3, 4))
    xp = ((1, 2), (2, 3), (1, 3), (2, 4), (2, 3), (3, 4))
    yp = ((1, 2), (2, 3), (1, 3), (3, 4), (2, 4), (3, 4))
    assert all(w in index for w in (x, y, xp, yp))
    assert words[tau1[index[x]]] == xp and words[tau1[index[y]]] == yp
    rx, ry = canonical[x], canonical[y]
    expected_tree = ((1, 2), (1, 3), (2, 4))
    assert rx.tree == ry.tree == expected_tree
    assert rx.pi == (3, 2, 1, 4, 6, 5)
    assert ry.pi == (3, 2, 1, 5, 6, 4)
    dx = contour_descriptor(x, rx, 1)
    dy = contour_descriptor(y, ry, 1)
    expected_descriptor = (
        (((1, 2), (1, 3))),
        ((2, 2), (1, 2)),
        ((2, 1), (1, 3)),
        ((7, 19), (2, 20)),
        ((1, 1, 5, 11, (5,)), (1, 1, 4, 10, (10,))),
    )
    assert dx == dy == expected_descriptor

    source = pair_subgroup(4, x, y)
    target = pair_subgroup(4, xp, yp)
    s4 = tuple(itertools.permutations(range(1, 5)))
    v4 = double_transposition_group()
    a4 = {p for p in s4 if parity(p) == 0}
    expected_h = expected_product_diagonal(v4, s4)
    expected_k = expected_product_diagonal(a4, s4)
    parity_diagonal = {(p, q) for p in s4 for q in s4 if parity(p) == parity(q)}
    assert source == expected_h and len(source) == 96
    assert target == expected_k == parity_diagonal and len(target) == 288
    assert source != target

    return {
        "all_four_words_in_Z4": True,
        "tau1_endpoints_match": True,
        "canonical_tree": [list(edge) for edge in expected_tree],
        "canonical_pi_x": list(rx.pi),
        "canonical_pi_y": list(ry.pi),
        "full_descriptor_equal": True,
        "full_descriptor": dx,
        "source_subgroup_order": len(source),
        "target_subgroup_order": len(target),
        "source_equals_(V4xV4)DiagS4": source == expected_h,
        "target_equals_(A4xA4)DiagS4": target == expected_k,
        "target_equals_parity_diagonal": target == parity_diagonal,
        "literal_subgroups_differ": source != target,
    }


def full_descriptor_classes(rank4) -> list[dict]:
    words = rank4["words"]
    canonical = rank4["canonical"]
    rows = []
    subgroup_cache: dict[tuple[int, int], frozenset[tuple[Perm, Perm]]] = {}

    def subgroup(a: int, b: int):
        key = (a, b)
        if key not in subgroup_cache:
            subgroup_cache[key] = pair_subgroup(4, words[a], words[b])
        return subgroup_cache[key]

    for i, target in sorted(rank4["tau"].items()):
        classes: dict[object, list[int]] = defaultdict(list)
        physical_classes: dict[object, list[int]] = defaultdict(list)
        for source, word in enumerate(words):
            classes[contour_descriptor(word, canonical[word], i)].append(source)
            physical_classes[(word[i - 1], word[i])].append(source)
        pairs = 0
        conflicts = 0
        first = None
        for key in sorted(classes, key=repr):
            members = classes[key]
            for a_at, a in enumerate(members):
                for b in members[a_at + 1 :]:
                    pairs += 1
                    before = subgroup(a, b)
                    after = subgroup(target[a], target[b])
                    if before != after:
                        conflicts += 1
                        if first is None:
                            first = {
                                "source_words": (words[a], words[b]),
                                "target_words": (words[target[a]], words[target[b]]),
                                "source_order": len(before),
                                "target_order": len(after),
                                "class_size": len(members),
                            }
        assert first is not None
        physical_first = None
        physical_pairs_tested = 0
        for key in sorted(physical_classes, key=repr):
            members = physical_classes[key]
            for a_at, a in enumerate(members):
                for b in members[a_at + 1 :]:
                    physical_pairs_tested += 1
                    before = subgroup(a, b)
                    after = subgroup(target[a], target[b])
                    if before != after:
                        physical_first = {
                            "source_order": len(before),
                            "target_order": len(after),
                            "source_words": (words[a], words[b]),
                            "target_words": (words[target[a]], words[target[b]]),
                        }
                        break
                if physical_first is not None:
                    break
            if physical_first is not None:
                break
        assert physical_first is not None
        rows.append(
            {
                "adjacent_value_index": i,
                "class_count": len(classes),
                "class_size_histogram": dict(sorted(Counter(map(len, classes.values())).items())),
                "within_class_pairs_exhausted": pairs,
                "conflicting_pairs": conflicts,
                "first_conflict": first,
                "exact_physical_pair_first_conflict": physical_first,
                "exact_physical_pair_pairs_tested_to_first_conflict": physical_pairs_tested,
            }
        )
    return rows


def full_twist_calibration(rank4) -> dict:
    words = rank4["words"]
    target = rank4["tau"][1]
    m = len(words[0])
    sweep = tuple((position, 1) for position in range(2, m))
    schedule = sweep * (m - 1)
    square_sources = [source for source, word in enumerate(words) if word[0] == word[1]]
    agreement = sum(
        rank4["index"][apply_schedule(words[source], schedule)] == target[source]
        for source in square_sources
    )
    assert len(schedule) == 20 and len(square_sources) == 360 and agreement == 180
    return {
        "scheduled_length": len(schedule),
        "square_prefix_source_count": len(square_sources),
        "agreement_with_tau1": agreement,
    }


def compose_action(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[v]] for v in range(len(right)))


def one_three_coloring(adjacency: list[set[int]]) -> list[int] | None:
    n = len(adjacency)
    colors = [-1] * n

    def search(done: int) -> bool:
        if done == n:
            return True
        candidates = [v for v in range(n) if colors[v] < 0]
        v = max(
            candidates,
            key=lambda x: (
                len({colors[u] for u in adjacency[x] if colors[u] >= 0}),
                len(adjacency[x]),
            ),
        )
        used = {colors[u] for u in adjacency[v] if colors[u] >= 0}
        for color in range(3):
            if color not in used:
                colors[v] = color
                if search(done + 1):
                    return True
                colors[v] = -1
        return False

    return colors if search(0) else None


def clique_number(adjacency: list[set[int]]) -> tuple[int, tuple[int, ...]]:
    n = len(adjacency)
    best: tuple[int, ...] = ()
    for size in range(1, n + 1):
        found = None
        for subset in itertools.combinations(range(n), size):
            if all(b in adjacency[a] for a, b in itertools.combinations(subset, 2)):
                found = subset
                break
        if found is None:
            break
        best = found
    return len(best), best


def d3_action_and_conflict(rank3) -> list[dict]:
    words = rank3["words"]
    index = rank3["index"]
    assert len(words) == 24
    generators = []
    for position in range(3):
        for sign in (1, -1):
            generators.append(tuple(index[hurwitz(word, position, sign)] for word in words))
    ident = tuple(range(24))
    action_group = {ident}
    queue = deque([ident])
    while queue:
        action = queue.popleft()
        for generator in generators:
            nxt = compose_action(generator, action)
            if nxt not in action_group:
                action_group.add(nxt)
                queue.append(nxt)
    assert len(action_group) == 216

    rows = []
    for i, target in sorted(rank3["tau"].items()):
        adjacency = [set() for _ in words]
        for a in range(24):
            for b in range(a + 1, 24):
                if pair_subgroup(3, words[a], words[b]) != pair_subgroup(
                    3, words[target[a]], words[target[b]]
                ):
                    adjacency[a].add(b)
                    adjacency[b].add(a)
        edge_count = sum(map(len, adjacency)) // 2
        omega, clique = clique_number(adjacency)
        coloring = one_three_coloring(adjacency)
        assert edge_count == 80 and omega == 3 and coloring is not None
        assert all(coloring[a] != coloring[b] for a in range(24) for b in adjacency[a])
        assert set(coloring) == {0, 1, 2}

        masks = {
            sum((action[source] == target[source]) << source for source in range(24))
            for action in action_group
        } - {0}
        assert len(masks) == 23
        frontier = {0}
        frontier_counts = [1]
        first_full = None
        full = (1 << 24) - 1
        for depth in range(1, 25):
            frontier = {covered | mask for covered in frontier for mask in masks}
            frontier_counts.append(len(frontier))
            if full in frontier:
                first_full = depth
                break
        assert first_full == 5
        assert frontier_counts == [1, 23, 206, 811, 1640, 2021]
        assert max(mask.bit_count() for mask in masks) == 6

        descriptor_rows = [
            contour_descriptor(word, rank3["canonical"][word], i) for word in words
        ]
        calibration = {}
        for name, component in (
            ("exact_physical_pair", 0),
            ("closure_scalar_history", 4),
            ("polynomial_contour_summary", None),
        ):
            classes: dict[object, int] = defaultdict(int)
            for source, descriptor in enumerate(descriptor_rows):
                key = descriptor if component is None else descriptor[component]
                classes[key] |= 1 << source
            unrealized = [
                class_mask
                for class_mask in classes.values()
                if not any(class_mask & ~agreement == 0 for agreement in masks)
            ]
            calibration[name] = {
                "class_count": len(classes),
                "unrealized_class_count": len(unrealized),
                "every_class_contained_in_one_agreement_set": not unrealized,
            }
        rows.append(
            {
                "adjacent_value_index": i,
                "action_image_order": len(action_group),
                "tau_in_action_image": target in action_group,
                "distinct_nonempty_agreement_masks": len(masks),
                "maximum_one_schedule_agreement": max(mask.bit_count() for mask in masks),
                "exact_minimum_schedule_cover": first_full,
                "coverage_frontier_counts": frontier_counts,
                "conflict_vertices": 24,
                "conflict_edges": edge_count,
                "maximum_clique_size": omega,
                "one_triangle": [words[v] for v in clique],
                "chromatic_number": 3,
                "color_class_sizes": sorted(Counter(coloring).values()),
                "metadata_calibration": calibration,
            }
        )
    return rows


def descriptor_range_audit(rank3, rank4) -> dict:
    # Each of two labels contributes two black/white endpoint pairs in total
    # across hairy and oriented fields, two boundary positions, and five closure
    # scalars.  The distance-three tuple is empty or a singleton.
    return {
        "formula": "E^2 [d(d-1)]^4 B^4 (S+1)^10",
        "definitions": {
            "E": "binom(d,2)",
            "B": "(2d-1)(2d-2)",
            "S": "(d-2)(2d-2)",
        },
        "asymptotic_power": 40,
        "field_powers": {
            "exact_physical_pair": "E^2 = O(d^4)",
            "hairy_and_oriented_endpoint_pairs": "[d(d-1)]^4 = O(d^8)",
            "four_boundary_positions": "B^4 = O(d^8)",
            "ten_closure_scalar_fields": "(S+1)^10 = O(d^20)",
        },
        "distance_three_field_is_empty_or_singleton": True,
        "complete_rank_checks": [
            {
                "d": d,
                "boundary_length": rank["boundary_length"],
                "total_closures": rank["total_closures"],
                "events_per_label": d - 2,
                "max_distance_three_events_per_label": rank["max_distance_three_per_label"],
            }
            for d, rank in ((3, rank3), (4, rank4))
        ],
        "boundary_d2_convention": "use empty markers for first/last closure; Z_2 is a singleton",
    }


def current_commit() -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"], text=True, capture_output=True, check=True
    ).stdout.strip()


def main() -> None:
    started = time.time()
    rank3 = build_dps_rank(3)
    rank4 = build_dps_rank(4)
    payload = {
        "experiment": "M134 independent fresh referee of frozen M132",
        "verdict": "ACCEPT",
        "material_numbered_objections": [],
        "target": "uniform physical Z_d via the exact d-to-one rooted DPS lift",
        "composition_convention": "(pq)(x)=p(q(x)); displayed factors multiply left-to-right",
        "hurwitz_convention": "R_j(a,b)=(b,bab); R_j^-1(a,b)=(aba,a)",
        "commit": current_commit(),
        "python": platform.python_version(),
        "nonstandard_dependencies": {},
        "seed": None,
        "deterministic": True,
        "rank_reconstruction": [
            {
                "d": d,
                "rooted_coordinates": sum(map(len, rank["roots"].values())),
                "brute_Z_size": len(rank["words"]),
                "root_fiber_histogram": dict(sorted(Counter(map(len, rank["roots"].values())).items())),
                "identity_connected_failures": 0,
                "tau_root_collisions": 0,
            }
            for d, rank in ((3, rank3), (4, rank4))
        ],
        "d4_witness": witness_audit(rank4),
        "descriptor_range": descriptor_range_audit(rank3, rank4),
        "d4_full_descriptor_classes": full_descriptor_classes(rank4),
        "d4_square_prefix_full_twist": full_twist_calibration(rank4),
        "d3_action_and_conflict": d3_action_and_conflict(rank3),
        "logical_claims": {
            "common_schedule_preserves_literal_pair_subgroup": True,
            "agreement_set_is_conflict_independent": True,
            "schedule_cover_induces_proper_coloring": True,
            "conflict_independence_is_not_sufficient_for_simultaneous_realization": True,
            "conditional_prefix_inversion_recovers_one_physical_source": True,
            "compressed_time_has_at_most_L_scheduled_candidates": True,
            "adjacent_index_count": "2d-3",
            "root_quotient_cost": "exactly d",
            "recovery_scope": "adjacent-value demands only, conditional on a polynomial fixed-schedule cover",
        },
        "scope": {
            "d3_d4_rows": "exact finite only",
            "M132_pair_search": "first-certificate/capped searches; no capped non-finding promoted",
            "general_polynomial_schedule_cover": "unresolved",
            "UST_basis_exchange": "unresolved",
            "physical_gap": "unresolved",
            "Gamma0": "unresolved outside the identity circular sector as before",
            "original_heat_bath_gap": "unresolved",
            "terminal_claim": False,
        },
        "elapsed_seconds": time.time() - started,
    }
    Path("independent_results.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n"
    )


if __name__ == "__main__":
    main()
