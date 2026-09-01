#!/usr/bin/env python3
"""Independent exact d=4 quotient-block and DPS matching audit.

The code reconstructs the accepted rooted DPS closure from definitions.  It
does not import predecessor code or data.  It identifies the degree-120
Hurwitz quotient block system both by Schreier--Sims and by the exceptional
quotient S_4/V_4 ~= S_3, then tests the deterministic Hall matchings in the
M135 incidence multigraph against that block relation.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import platform
import subprocess
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path

from sympy.combinatorics import Permutation, PermutationGroup


PermutationTuple = tuple[int, ...]
Edge = tuple[int, int]
Word = tuple[Edge, ...]
Tree = frozenset[Edge]


@dataclass(frozen=True)
class Stub:
    side: str
    vertex: int
    label: int


@dataclass(frozen=True)
class Arc:
    kind: str
    label: int | None = None


def multiply(p: PermutationTuple, q: PermutationTuple) -> PermutationTuple:
    return tuple(p[q[x]] for x in range(len(p)))


def edge_map(d: int, edge: Edge) -> PermutationTuple:
    out = list(range(d))
    a, b = edge
    out[a], out[b] = out[b], out[a]
    return tuple(out)


def evaluate(d: int, word: Word) -> PermutationTuple:
    out = tuple(range(d))
    for edge in word:
        out = multiply(out, edge_map(d, edge))
    return out


def connected(d: int, word: Word) -> bool:
    adjacency = [set() for _ in range(d)]
    for a, b in word:
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen = {0}
    stack = [0]
    while stack:
        a = stack.pop()
        for b in adjacency[a] - seen:
            seen.add(b)
            stack.append(b)
    return len(seen) == d


def relabel_edge(edge: Edge, rho: PermutationTuple) -> Edge:
    return tuple(sorted((rho[edge[0]], rho[edge[1]])))


def relabel_word(word: Word, rho: PermutationTuple) -> Word:
    return tuple(relabel_edge(edge, rho) for edge in word)


def canonical(word: Word, group: tuple[PermutationTuple, ...]) -> Word:
    return min(relabel_word(word, rho) for rho in group)


def conjugate_edge(edge: Edge, by: Edge) -> Edge:
    a, b = edge
    x, y = by

    def image(z: int) -> int:
        return y if z == x else x if z == y else z

    return tuple(sorted((image(a), image(b))))


def hurwitz(word: Word, slot: int, direction: int = 1) -> Word:
    a, b = word[slot : slot + 2]
    out = list(word)
    if direction == 1:
        out[slot : slot + 2] = (b, conjugate_edge(a, b))
    elif direction == -1:
        out[slot : slot + 2] = (conjugate_edge(b, a), a)
    else:
        raise ValueError(direction)
    return tuple(out)


def brute_target(d: int) -> tuple[Word, ...]:
    edges = tuple(itertools.combinations(range(d), 2))
    identity = tuple(range(d))
    return tuple(
        word
        for word in itertools.product(edges, repeat=2 * d - 2)
        if evaluate(d, word) == identity and connected(d, word)
    )


def prufer_trees(d: int):
    for code in itertools.product(range(d), repeat=d - 2):
        degree = [1] * d
        for v in code:
            degree[v] += 1
        edges = []
        for v in code:
            leaf = next(x for x in range(d) if degree[x] == 1)
            edges.append(tuple(sorted((leaf, v))))
            degree[leaf] -= 1
            degree[v] -= 1
        edges.append(tuple(x for x in range(d) if degree[x] == 1))
        yield frozenset(edges)


def parents_toward_root(tree: Tree, root: int) -> dict[int, int]:
    adjacency = {v: [] for v in range(root + 1)}
    for a, b in tree:
        adjacency[a].append(b)
        adjacency[b].append(a)
    parent = {root: -1}
    stack = [root]
    while stack:
        a = stack.pop()
        for b in adjacency[a]:
            if b not in parent:
                parent[b] = a
                stack.append(b)
    return parent


def hairy_tree(tree: Tree, order: tuple[int, ...], d: int):
    root = d - 1
    parent = parents_toward_root(tree, root)
    incidence: dict[tuple[str, int], dict[int, tuple[str, int]]] = defaultdict(dict)
    first_black = {}
    for black in range(root):
        labels = order[2 * black : 2 * black + 2]
        for label, white in ((labels[0], black), (labels[1], parent[black])):
            bnode, wnode = ("b", black), ("w", white)
            incidence[bnode][label] = wnode
            incidence[wnode][label] = bnode
            first_black[label] = black
    return incidence, first_black


def contour(incidence, d: int) -> list[Stub | Arc]:
    m = 2 * d - 2
    start = (("w", 0), 0)
    state = start
    visited = set()
    tokens: list[Stub | Arc] = []
    while state not in visited:
        visited.add(state)
        vertex, incoming = state
        step = 1 if vertex[0] == "w" else -1
        label = (incoming + step) % m
        if label in incidence[vertex]:
            neighbor = incidence[vertex][label]
            tokens.append(Arc("tree", label))
            state = (neighbor, label)
        else:
            tokens.append(Stub(vertex[0], vertex[1], label))
            state = (vertex, label)
    assert state == start and len(tokens) == (2 * d - 1) * m
    return tokens


def close_contour(tokens: list[Stub | Arc], d: int) -> dict[int, int]:
    work = list(tokens)
    second_black = {}
    while True:
        stubs = [j for j, token in enumerate(work) if isinstance(token, Stub)]
        chosen = None
        for k, white_pos in enumerate(stubs):
            black_pos = stubs[(k + 1) % len(stubs)]
            if work[white_pos].side == "w" and work[black_pos].side == "b":
                chosen = white_pos, black_pos
                break
        if chosen is None:
            break
        white_pos, black_pos = chosen
        work = work[white_pos:] + work[:white_pos]
        black_pos = (black_pos - white_pos) % len(work)
        white, black = work[0], work[black_pos]
        assert isinstance(white, Stub) and isinstance(black, Stub) and white.label == black.label
        distance = sum(isinstance(token, Arc) for token in work[1:black_pos])
        assert distance in (1, 3)
        if distance == 3:
            second_black[white.label] = black.vertex
        work = [Arc("closure")] + work[black_pos + 1 :]
    survivors = [token for token in work if isinstance(token, Stub)]
    assert len(survivors) == 2 * d - 2 and all(token.side == "w" for token in survivors)
    return second_black


def dps_image(tree: Tree, order: tuple[int, ...], d: int) -> Word:
    incidence, first_black = hairy_tree(tree, order, d)
    second_black = close_contour(contour(incidence, d), d)
    root = d - 1
    return tuple(
        tuple(sorted((first_black[label], second_black.get(label, root))))
        for label in range(2 * d - 2)
    )


def adjacent_value_swap(order: tuple[int, ...], i: int) -> tuple[int, ...]:
    return tuple(i + 1 if x == i else i if x == i + 1 else x for x in order)


def reconstruct_dps(d: int):
    m = 2 * d - 2
    fibers: dict[Word, list[tuple[Tree, tuple[int, ...]]]] = defaultdict(list)
    for tree in prufer_trees(d):
        for order in itertools.permutations(range(m)):
            word = dps_image(tree, order, d)
            assert evaluate(d, word) == tuple(range(d)) and connected(d, word)
            fibers[word].append((tree, order))
    words = tuple(sorted(brute_target(d)))
    assert set(words) == set(fibers) and set(map(len, fibers.values())) == {d}
    index = {word: j for j, word in enumerate(words)}
    tau = {}
    for i in range(m - 1):
        image = []
        for word in words:
            targets = {
                dps_image(tree, adjacent_value_swap(order, i), d)
                for tree, order in fibers[word]
            }
            assert len(targets) == 1
            image.append(index[next(iter(targets))])
        assert len(set(image)) == len(words) and all(image[image[j]] == j for j in range(len(words)))
        tau[i] = tuple(image)
    return words, index, fibers, tau


def hall_matching(edges, left_vertices, active):
    adjacency = {left: [] for left in left_vertices}
    for edge_id in active:
        left, right = edges[edge_id]
        adjacency[left].append((right, edge_id))
    occupied = {}

    def augment(left, seen):
        for right, edge_id in adjacency[left]:
            if right in seen:
                continue
            seen.add(right)
            if right not in occupied or augment(occupied[right][0], seen):
                occupied[right] = (left, edge_id)
                return True
        return False

    assert all(augment(left, set()) for left in left_vertices)
    return {edge_id for _left, edge_id in occupied.values()}


def edge_coloring(edges, degree):
    left_vertices = tuple(sorted({left for left, _right in edges}))
    active = set(range(len(edges)))
    colors = {}
    for color in range(degree):
        chosen = hall_matching(edges, left_vertices, active)
        for edge_id in chosen:
            colors[edge_id] = color
        active.difference_update(chosen)
    assert not active
    return colors


def exceptional_projection_edge(edge: Edge) -> Edge:
    """Image of an S_4 transposition in its action on three perfect matchings."""
    matchings = (
        frozenset(((0, 1), (2, 3))),
        frozenset(((0, 2), (1, 3))),
        frozenset(((0, 3), (1, 2))),
    )
    rho = edge_map(4, edge)
    action = []
    for matching in matchings:
        image = frozenset(relabel_edge(e, rho) for e in matching)
        action.append(matchings.index(image))
    moved = tuple(j for j in range(3) if action[j] != j)
    assert len(moved) == 2
    return moved


def exceptional_block_key(word: Word, s3: tuple[PermutationTuple, ...]) -> Word:
    projected = tuple(exceptional_projection_edge(edge) for edge in word)
    assert evaluate(3, projected) == tuple(range(3)) and connected(3, projected)
    return canonical(projected, s3)


def quotient_action_and_blocks(qwords: tuple[Word, ...], s4, s3):
    qindex = {word: j for j, word in enumerate(qwords)}
    generators = [
        tuple(qindex[canonical(hurwitz(word, slot), s4)] for word in qwords)
        for slot in range(5)
    ]
    group = PermutationGroup([Permutation(list(action)) for action in generators])
    point_stabilizer = group.stabilizer(0)
    subdegrees = sorted(map(len, point_stabilizer.orbits()))
    sympy_labels = group.minimal_blocks(randomized=False)[0]
    sympy_blocks = defaultdict(set)
    for point, label in enumerate(sympy_labels):
        sympy_blocks[label].add(point)
    algebraic_blocks = defaultdict(set)
    for point, word in enumerate(qwords):
        algebraic_blocks[exceptional_block_key(word, s3)].add(point)
    sympy_partition = {frozenset(block) for block in sympy_blocks.values()}
    algebraic_partition = {frozenset(block) for block in algebraic_blocks.values()}
    return generators, group, subdegrees, sympy_partition, algebraic_partition


def matching_block_audit(words, tau, s4, root_group, qwords, qindex, block_of):
    global_key = {j: canonical(word, s4) for j, word in enumerate(words)}
    root_blocks = defaultdict(list)
    for j, word in enumerate(words):
        root_blocks[canonical(word, root_group)].append(j)
    rows = []
    for i, target in tau.items():
        edges = []
        edge_representatives = []
        edge_label_equal = 0
        for hkey in sorted(root_blocks):
            source = root_blocks[hkey][0]
            targets = {canonical(words[target[j]], s4) for j in root_blocks[hkey]}
            assert len(targets) == 1
            source_q = qindex[global_key[source]]
            target_q = qindex[next(iter(targets))]
            edges.append((source_q, target_q))
            edge_representatives.append(source)
            edge_label_equal += block_of[source_q] == block_of[target_q]
        colors = edge_coloring(edges, 4)
        color_rows = []
        for color in range(4):
            mapping = {edges[e][0]: edges[e][1] for e in colors if colors[e] == color}
            assert len(mapping) == len(qwords) and len(set(mapping.values())) == len(qwords)
            source_same = 0
            relation_preserved = 0
            relation_broken = 0
            relation_created = 0
            for a in range(len(qwords)):
                for b in range(a + 1, len(qwords)):
                    before = block_of[a] == block_of[b]
                    after = block_of[mapping[a]] == block_of[mapping[b]]
                    source_same += before
                    relation_preserved += before and after
                    relation_broken += before and not after
                    relation_created += not before and after
            color_rows.append(
                {
                    "color": color,
                    "mapping_is_block_system_automorphism": relation_broken == relation_created == 0,
                    "source_same_block_pairs": source_same,
                    "same_block_pairs_preserved": relation_preserved,
                    "same_block_pairs_broken": relation_broken,
                    "different_block_pairs_collapsed": relation_created,
                }
            )
        rows.append(
            {
                "adjacent_index": i + 1,
                "H_orbit_edges": len(edges),
                "edges_with_same_absolute_exceptional_block": edge_label_equal,
                "matching_colors": color_rows,
            }
        )
    return rows


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    mission = Path(__file__).resolve().parent
    d = 4
    s4 = tuple(itertools.permutations(range(4)))
    s3 = tuple(itertools.permutations(range(3)))
    root_group = tuple(rho for rho in s4 if rho[3] == 3)
    words, index, fibers, tau = reconstruct_dps(d)
    qwords = tuple(sorted({canonical(word, s4) for word in words}))
    qindex = {word: j for j, word in enumerate(qwords)}
    generators, group, subdegrees, sympy_partition, algebraic_partition = quotient_action_and_blocks(
        qwords, s4, s3
    )
    assert sympy_partition == algebraic_partition
    block_of = {}
    for block_id, block in enumerate(sorted(algebraic_partition, key=lambda b: min(b))):
        for point in block:
            block_of[point] = block_id
    matching_rows = matching_block_audit(
        words, tau, s4, root_group, qwords, qindex, block_of
    )
    A, B, C, D, E = (0, 1), (0, 2), (2, 3), (1, 2), (1, 3)
    witness_source = ((A, B, B, A, C, C), (A, B, B, C, A, C))
    witness_target = ((A, D, B, E, D, C), (A, D, B, C, E, C))
    witness_source_keys = [exceptional_block_key(word, s3) for word in witness_source]
    witness_target_keys = [exceptional_block_key(word, s3) for word in witness_target]
    payload = {
        "experiment": "M154 exact d4 exceptional quotient block and M135 matching audit",
        "target": "literal diagonal signed-Hurwitz action; no sampler or gap claim",
        "composition_convention": "(pq)(x)=p(q(x)); displayed factors multiply left-to-right",
        "repository_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "python": platform.python_version(),
        "dependencies": {"sympy": __import__("sympy").__version__},
        "seed": None,
        "command": "python3 -B d4_exceptional_block_audit.py",
        "d4": {
            "physical_words": len(words),
            "rooted_DPS_coordinates": sum(map(len, fibers.values())),
            "root_fiber_histogram": dict(sorted(Counter(map(len, fibers.values())).items())),
            "global_quotient_degree": len(qwords),
            "positive_hurwitz_generators": len(generators),
            "group_order": group.order(),
            "group_order_factorization": {str(p): e for p, e in __import__("sympy").factorint(group.order()).items()},
            "transitive": group.is_transitive(),
            "primitive": group.is_primitive(),
            "point_stabilizer_subdegrees": subdegrees,
            "minimal_blocks": len(sympy_partition),
            "minimal_block_size_histogram": dict(sorted(Counter(map(len, sympy_partition)).items())),
            "exceptional_quotient_blocks": len(algebraic_partition),
            "exceptional_block_size_histogram": dict(sorted(Counter(map(len, algebraic_partition)).items())),
            "sympy_blocks_equal_S4_mod_V4_fibers": sympy_partition == algebraic_partition,
            "accepted_M135_rank4_witness": {
                "source_same_exceptional_block": witness_source_keys[0] == witness_source_keys[1],
                "target_same_exceptional_block": witness_target_keys[0] == witness_target_keys[1],
                "therefore_common_literal_braid_obstructed":
                    (witness_source_keys[0] == witness_source_keys[1])
                    and (witness_target_keys[0] != witness_target_keys[1]),
            },
            "matching_rows": matching_rows,
        },
        "predecessor_read_only_hash": sha256(
            mission.parents[1] / "cycle-31" / "mission-M137-m135-fresh-referee" / "report.md"
        ),
    }
    assert len(words) == 2880 and sum(map(len, fibers.values())) == 11520
    assert len(qwords) == 120 and group.order() == 20652142670561646642588549120
    assert subdegrees == [1, 2, 36, 81]
    assert len(sympy_partition) == 40 and set(map(len, sympy_partition)) == {3}
    assert payload["d4"]["accepted_M135_rank4_witness"]["therefore_common_literal_braid_obstructed"]
    output = mission / "d4_results.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["d4"], sort_keys=True))


if __name__ == "__main__":
    main()
