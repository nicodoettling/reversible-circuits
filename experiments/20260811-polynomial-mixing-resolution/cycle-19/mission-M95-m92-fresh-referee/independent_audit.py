#!/usr/bin/env python3
"""Independent exact checks for the frozen M92 reduction.

This script imports no M92 or predecessor code.  Its finite checks can
falsify the claimed pointwise lump, shuttle word, explicit unmarked family,
and metadata witnesses.  They do not prove an asymptotic Hurwitz gap or a
marked hitting-time bound.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import subprocess
import sys
import time
from collections import Counter, deque
from fractions import Fraction
from pathlib import Path


sys.dont_write_bytecode = True


Edge = tuple[int, int]
Word = tuple[Edge, ...]


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return pq, so (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def transposition(n: int, edge: Edge) -> tuple[int, ...]:
    a, b = edge
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def evaluate(word: Word, n: int) -> tuple[int, ...]:
    value = tuple(range(n))
    for edge in word:
        value = compose(value, transposition(n, edge))
    return value


def conjugate_edge(conjugator: Edge, edge: Edge) -> Edge:
    a, b = edge
    c, d = conjugator

    def image(x: int) -> int:
        if x == c:
            return d
        if x == d:
            return c
        return x

    return tuple(sorted((image(a), image(b))))


def hurwitz_pair(first: Edge, second: Edge, sign: int) -> tuple[Edge, Edge]:
    if sign == 1:
        return second, conjugate_edge(second, first)
    if sign == -1:
        return conjugate_edge(first, second), first
    raise ValueError(sign)


def hurwitz_word(word: Word, index: int, sign: int) -> Word:
    pair = hurwitz_pair(word[index], word[index + 1], sign)
    return word[:index] + pair + word[index + 2 :]


def connected_on(word: Word, vertices: tuple[int, ...]) -> bool:
    if len(vertices) <= 1:
        return True
    adjacency = {v: set() for v in vertices}
    for a, b in word:
        if a in adjacency and b in adjacency:
            adjacency[a].add(b)
            adjacency[b].add(a)
    seen = {vertices[0]}
    stack = [vertices[0]]
    while stack:
        a = stack.pop()
        for b in adjacency[a]:
            if b not in seen:
                seen.add(b)
                stack.append(b)
    return seen == set(vertices)


def marked_internal_positions(word: Word, vertices: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        i
        for i in range(len(word) - 1)
        if word[i] == word[i + 1]
        and connected_on(word[:i] + word[i + 2 :], vertices)
    )


def enumerate_connected_identity(vertices: tuple[int, ...], length: int, n: int) -> tuple[Word, ...]:
    edges = tuple(itertools.combinations(vertices, 2))
    identity = tuple(range(n))
    return tuple(
        word
        for word in itertools.product(edges, repeat=length)
        if evaluate(word, n) == identity and connected_on(word, vertices)
    )


def color_words(k_u: int, k_v: int) -> tuple[tuple[str, ...], ...]:
    answer = []
    for u_positions in itertools.combinations(range(k_u + k_v), k_u):
        u_set = set(u_positions)
        answer.append(tuple("U" if i in u_set else "V" for i in range(k_u + k_v)))
    return tuple(answer)


def interleave(colors: tuple[str, ...], u: Word, v: Word) -> Word:
    answer = []
    iu = iv = 0
    for color in colors:
        if color == "U":
            answer.append(u[iu])
            iu += 1
        else:
            answer.append(v[iv])
            iv += 1
    assert iu == len(u) and iv == len(v)
    return tuple(answer)


def split_word(word: Word, u_vertices: frozenset[int]) -> tuple[tuple[str, ...], Word, Word]:
    colors = []
    u = []
    v = []
    for edge in word:
        if set(edge) <= u_vertices:
            colors.append("U")
            u.append(edge)
        elif set(edge).isdisjoint(u_vertices):
            colors.append("V")
            v.append(edge)
        else:
            raise AssertionError(("cross-component factor", edge))
    return tuple(colors), tuple(u), tuple(v)


def projected_generator(
    state: tuple[tuple[str, ...], Word], index: int, sign: int
) -> tuple[tuple[str, ...], Word]:
    colors, u = state
    left, right = colors[index], colors[index + 1]
    if left == right == "U":
        internal_index = sum(color == "U" for color in colors[:index])
        return colors, hurwitz_word(u, internal_index, sign)
    if left != right:
        changed = list(colors)
        changed[index], changed[index + 1] = changed[index + 1], changed[index]
        return tuple(changed), u
    return state


def projected_mark(state: tuple[tuple[str, ...], Word], u_vertices: tuple[int, ...]) -> bool:
    colors, u = state
    rank = 0
    for i in range(len(colors) - 1):
        if colors[i] == colors[i + 1] == "U":
            if u[rank] == u[rank + 1] and connected_on(u[:rank] + u[rank + 2 :], u_vertices):
                return True
        if colors[i] == "U":
            rank += 1
    return False


def full_mark(word: Word, u_vertices: tuple[int, ...]) -> bool:
    u_set = frozenset(u_vertices)
    for i in range(len(word) - 1):
        if word[i] != word[i + 1] or not set(word[i]) <= u_set:
            continue
        u_without = tuple(
            edge
            for j, edge in enumerate(word)
            if set(edge) <= u_set and j not in (i, i + 1)
        )
        if connected_on(u_without, u_vertices):
            return True
    return False


def apply_projected_path(
    state: tuple[tuple[str, ...], Word],
    first: int,
    second: int,
    sign: int,
) -> tuple[tuple[str, ...], Word]:
    path = [(i, 1) for i in range(first, second - 1)]
    path.append((second - 1, sign))
    path.extend((i, 1) for i in range(second - 2, first - 1, -1))
    current = state
    for index, orientation in path:
        current = projected_generator(current, index, orientation)
    return current


def strong_lump_and_shuttle_check() -> dict:
    n = 6
    u_vertices = (0, 1, 2)
    v_vertices = (3, 4, 5)
    u_words = enumerate_connected_identity(u_vertices, 6, n)
    v_words = enumerate_connected_identity(v_vertices, 4, n)
    colors_all = color_words(6, 4)
    assert len(u_words) == 240 and len(v_words) == 24 and len(colors_all) == 210

    # Each labeled projected proposal is a bijection.  Check this on the full
    # projected state space, independently of full-word coordinates.
    projected_states = tuple((colors, u) for colors in colors_all for u in u_words)
    projected_state_set = set(projected_states)
    bijection_checks = 0
    for index in range(9):
        for sign in (1, -1):
            images = {projected_generator(state, index, sign) for state in projected_states}
            assert images == projected_state_set
            bijection_checks += 1

    # Check the pointwise formula against actual full Hurwitz moves for two
    # very different omitted V words at every projected state and proposal.
    omitted_samples = (v_words[0], v_words[-1])
    pointwise_checks = 0
    omitted_independence_checks = 0
    marked_projection_count = 0
    marked_full_checks = 0
    for colors, u in projected_states:
        expected_mark = projected_mark((colors, u), u_vertices)
        if expected_mark:
            marked_projection_count += 1
        prior_rows = None
        for v in omitted_samples:
            full = interleave(colors, u, v)
            assert full_mark(full, u_vertices) == expected_mark
            marked_full_checks += 1
            row = Counter()
            for index in range(9):
                for sign in (1, -1):
                    moved = hurwitz_word(full, index, sign)
                    new_colors, new_u, _new_v = split_word(moved, frozenset(u_vertices))
                    actual = (new_colors, new_u)
                    expected = projected_generator((colors, u), index, sign)
                    assert actual == expected
                    row[actual] += 1
                    pointwise_checks += 1
            if prior_rows is not None:
                assert row == prior_rows
                omitted_independence_checks += 1
            prior_rows = row

    # Exhaust every requested internal generator and every color interleaving.
    shuttle_checks = 0
    max_shuttle_length = 0
    for colors, u in projected_states:
        positions = [i for i, color in enumerate(colors) if color == "U"]
        for internal_index in range(5):
            first, second = positions[internal_index], positions[internal_index + 1]
            length = 2 * (second - first - 1) + 1
            max_shuttle_length = max(max_shuttle_length, length)
            for sign in (1, -1):
                actual = apply_projected_path((colors, u), first, second, sign)
                expected = (colors, hurwitz_word(u, internal_index, sign))
                assert actual == expected
                shuttle_checks += 1

    total_projected = len(projected_states)
    marked_fraction = Fraction(marked_projection_count, total_projected)
    zeta = Fraction(3, n * 10 * 9)
    assert marked_fraction >= zeta
    return {
        "ambient_N": n,
        "ambient_m": 10,
        "U_fiber_size": len(u_words),
        "V_fiber_size": len(v_words),
        "color_interleavings": len(colors_all),
        "projected_states": total_projected,
        "full_macro_size": total_projected * len(v_words),
        "constant_projection_fiber_size": len(v_words),
        "labeled_projected_bijections_checked": bijection_checks,
        "pointwise_full_to_projected_proposals_checked": pointwise_checks,
        "omitted_word_row_equalities_checked": omitted_independence_checks,
        "mark_measurability_checks": marked_full_checks,
        "marked_projected_states": marked_projection_count,
        "marked_fraction": str(marked_fraction),
        "zeta_lower_bound": str(zeta),
        "shuttle_instances_checked": shuttle_checks,
        "maximum_shuttle_length_seen": max_shuttle_length,
        "theoretical_strict_bound": 20,
    }


def prufer_tree(sequence: tuple[int, ...], d: int) -> tuple[Edge, ...]:
    degree = [1] * d
    for vertex in sequence:
        degree[vertex] += 1
    edges = []
    for vertex in sequence:
        leaf = min(i for i, value in enumerate(degree) if value == 1)
        edges.append(tuple(sorted((leaf, vertex))))
        degree[leaf] -= 1
        degree[vertex] -= 1
    last = [i for i, value in enumerate(degree) if value == 1]
    edges.append(tuple(sorted(last)))
    return tuple(sorted(edges))


def unmarked_tree_word(tree: tuple[Edge, ...]) -> Word:
    incident = next(
        (pair for pair in itertools.combinations(tree, 2) if set(pair[0]) & set(pair[1])),
        None,
    )
    assert incident is not None
    a, b = incident
    tail = tuple(edge for edge in tree if edge not in (a, b))
    return (a, b, a, b, a, b) + tuple(edge for edge in tail for _ in range(2))


def unmarked_family_check(d_max: int = 6) -> list[dict]:
    result = []
    for d in range(3, d_max + 1):
        seen = set()
        count = 0
        for sequence in itertools.product(range(d), repeat=d - 2):
            tree = prufer_tree(sequence, d)
            seen.add(tree)
            word = unmarked_tree_word(tree)
            assert len(word) == 2 * d
            assert evaluate(word, d) == tuple(range(d))
            assert connected_on(word, tuple(range(d)))
            assert set(word) == set(tree)
            assert not marked_internal_positions(word, tuple(range(d)))
            count += 1
        assert count == len(seen) == d ** (d - 2)
        result.append({"d": d, "trees_checked": count, "expected": d ** (d - 2)})
    return result


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        self.parent[b] = a
        return True


def face_data(word: Word, n: int) -> tuple[tuple[tuple[int, int], ...], dict[tuple[int, int], int]]:
    darts = tuple((edge, side) for edge in range(len(word)) for side in (0, 1))
    dart_id = {dart: i for i, dart in enumerate(darts)}
    alpha = [0] * len(darts)
    for edge in range(len(word)):
        alpha[dart_id[(edge, 0)]] = dart_id[(edge, 1)]
        alpha[dart_id[(edge, 1)]] = dart_id[(edge, 0)]
    sigma = [0] * len(darts)
    for vertex in range(n):
        incident = [
            dart_id[(edge, side)]
            for edge, endpoints in enumerate(word)
            for side, endpoint in enumerate(endpoints)
            if endpoint == vertex
        ]
        for j, dart in enumerate(incident):
            sigma[dart] = incident[(j + 1) % len(incident)]
    phi = [sigma[alpha[dart]] for dart in range(len(darts))]
    seen = set()
    faces = []
    dart_face = {}
    for root in range(len(darts)):
        if root in seen:
            continue
        face = []
        current = root
        face_id = len(faces)
        while current not in seen:
            seen.add(current)
            dart_face[darts[current]] = face_id
            face.append(darts[current])
            current = phi[current]
        faces.append(tuple(face))
    return tuple(faces), dart_face


def tree_path(tree_positions: tuple[int, ...], word: Word, start: int, end: int) -> tuple[int, ...]:
    adjacency = {v: [] for v in set(x for edge in word for x in edge)}
    for position in tree_positions:
        a, b = word[position]
        adjacency[a].append((b, position))
        adjacency[b].append((a, position))
    queue = deque([start])
    predecessor: dict[int, tuple[int, int] | None] = {start: None}
    while queue:
        a = queue.popleft()
        for b, position in sorted(adjacency[a], key=lambda item: item[1]):
            if b not in predecessor:
                predecessor[b] = (a, position)
                queue.append(b)
    assert end in predecessor
    answer = []
    current = end
    while predecessor[current] is not None:
        previous, position = predecessor[current]
        answer.append(position)
        current = previous
    return tuple(reversed(answer))


def tree_cotree_signature(word: Word, n: int) -> dict:
    primal = UnionFind(n)
    tree = []
    for position, (a, b) in enumerate(word):
        if primal.union(a, b):
            tree.append(position)
    assert len(tree) == n - 1
    faces, dart_face = face_data(word, n)
    assert len(faces) == n
    tree_set = set(tree)
    dual = UnionFind(len(faces))
    cotree = []
    for position in range(len(word)):
        if position in tree_set:
            continue
        left = dart_face[(position, 0)]
        right = dart_face[(position, 1)]
        if dual.union(left, right):
            cotree.append(position)
    assert len(cotree) == n - 1
    used = tree_set | set(cotree)
    leftovers = tuple(i for i in range(len(word)) if i not in used)
    assert len(leftovers) == 2
    return {
        "tree": tree,
        "cotree": cotree,
        "leftovers": list(leftovers),
        "leftover_edges": [list(word[i]) for i in leftovers],
        "paths": [list(tree_path(tuple(tree), word, *word[i])) for i in leftovers],
        "faces": len(faces),
    }


def metadata_witness_check() -> dict:
    first: Word = (
        (0, 1), (0, 1), (0, 1), (0, 2),
        (0, 1), (2, 3), (1, 2), (1, 3),
    )
    second: Word = (
        (0, 1), (0, 1), (0, 1), (0, 2),
        (0, 2), (0, 3), (0, 1), (1, 3),
    )
    signatures = []
    for word in (first, second):
        assert evaluate(word, 4) == tuple(range(4))
        assert connected_on(word, tuple(range(4)))
        signatures.append(tree_cotree_signature(word, 4))
    one, two = signatures
    for field in ("tree", "cotree", "leftovers", "leftover_edges", "faces"):
        assert one[field] == two[field]
    assert one["paths"] != two["paths"]
    assert one["tree"] == [0, 3, 5]
    assert one["cotree"] == [1, 4, 6]
    assert one["leftovers"] == [2, 7]
    assert one["leftover_edges"] == [[0, 1], [1, 3]]
    assert one["paths"] == [[0], [0, 3, 5]]
    assert two["paths"] == [[0], [0, 5]]
    return {"first": one, "second": two, "identity_and_connected": True}


def toy_random_time_check(T: int = 6) -> dict:
    # Z/4Z with hold, +1, -1 probabilities 1/2,1/4,1/4.  This is a
    # state-independent bijective-proposal walk, exactly matching the abstract
    # structure of M92 Theorem 1.1.
    n = 4
    transition = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for x in range(n):
        transition[x][x] += Fraction(1, 2)
        transition[x][(x + 1) % n] += Fraction(1, 4)
        transition[x][(x - 1) % n] += Fraction(1, 4)

    def step(row: list[Fraction]) -> list[Fraction]:
        return [sum(row[x] * transition[x][y] for x in range(n)) for y in range(n)]

    checks = []
    for source in range(n):
        row = [Fraction(int(x == source)) for x in range(n)]
        occupation = Fraction(0)
        for _time in range(T + 1):
            occupation += row[0]
            row = step(row)
        endpoint_average = occupation / (T + 1)

        # Killed-chain dynamic program for avoiding mark {0} through T.
        if source == 0:
            hit = Fraction(1)
        else:
            alive = [Fraction(int(x == source)) for x in range(n)]
            alive[0] = 0
            for _time in range(T):
                next_alive = step(alive)
                next_alive[0] = 0
                alive = next_alive
            hit = 1 - sum(alive)
        assert endpoint_average >= hit / (T + 1)
        checks.append({
            "source": source,
            "hit_by_T": str(hit),
            "random_time_endpoint_mark": str(endpoint_average),
            "lower_bound": str(hit / (T + 1)),
        })
    return {
        "T": T,
        "expected_emitted_length": str(Fraction(T, 4)),
        "sources": checks,
    }


def normalization_check() -> dict:
    N, m, T, t = 6, 10, 8, 137
    M = math.comb(N, 2)
    p_h = Fraction(1, 6 * (m - 2) * M * M)
    random_time_markov_bound = p_h * Fraction(1, 2) / (T + 1) / Fraction(T, 4)
    assert random_time_markov_bound == Fraction(2, 1) * p_h / (T * (T + 1))
    zeta = Fraction(3, N * m * (m - 1))
    fixed_time_endpoint_bound = p_h * (zeta / 2) / Fraction(t, 2)
    displayed = Fraction(1, 2 * N * m * (m - 1) * (m - 2) * M * M * t)
    assert fixed_time_endpoint_bound == displayed
    return {
        "N": N,
        "m": m,
        "M": M,
        "p_H": str(p_h),
        "random_time_T": T,
        "random_time_markov_coarea": str(random_time_markov_bound),
        "fixed_time_t": t,
        "zeta": str(zeta),
        "fixed_time_coarea": str(fixed_time_endpoint_bound),
        "displayed_formula": str(displayed),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "claim_tested": (
            "M92's scoped random-time/coarea normalization, pointwise strong lump, "
            "projected shuttle, explicit unmarked family, and metadata witnesses"
        ),
        "scope_warning": (
            "Finite checks do not prove gamma_1, uniform marked hitting, an arbitrary-"
            "macro cover, a full heat-bath gap, or either Terminal."
        ),
        "convention": "(pq)(x)=p(q(x)); tuple factors multiply left-to-right",
        "commit": commit,
        "python": platform.python_version(),
        "seed": None,
        "nonstandard_dependencies": {},
        "argv": sys.argv,
        "random_time_toy": toy_random_time_check(),
        "coarea_normalizations": normalization_check(),
        "projected_lump_and_shuttle": strong_lump_and_shuttle_check(),
        "unmarked_cayley_trees": unmarked_family_check(),
        "tree_cotree_metadata_witness": metadata_witness_check(),
        "elapsed_seconds": time.perf_counter() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
