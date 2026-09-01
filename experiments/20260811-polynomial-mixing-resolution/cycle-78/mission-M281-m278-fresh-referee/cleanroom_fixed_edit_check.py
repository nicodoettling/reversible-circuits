#!/usr/bin/env python3
"""Clean-room falsifier for the M281 audit of frozen M278.

This script imports no M278 or predecessor code/data.  It directly builds the
DPS hairy-tree contour, rotates it by the cycle lemma, executes the LIFO
distance-one/distance-three closure, and checks only the prescribed d=5,6
fixed-edit cases.  It performs no route search and is not the all-rank proof.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import platform
from collections import Counter, defaultdict, deque
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "cleanroom_results.json"


def edge(a: int, b: int) -> tuple[int, int]:
    assert a != b
    return (a, b) if a < b else (b, a)


def prufer_decode(vertices: tuple[int, ...], code: tuple[int, ...]):
    degree = {v: 1 for v in vertices}
    for v in code:
        degree[v] += 1
    result = []
    for v in code:
        leaf = min(x for x in vertices if degree[x] == 1)
        result.append(edge(leaf, v))
        degree[leaf] -= 1
        degree[v] -= 1
    leaves = [x for x in vertices if degree[x] == 1]
    assert len(leaves) == 2
    result.append(edge(*leaves))
    return tuple(sorted(result))


def rooted_leaf_trees(d: int):
    base = tuple(range(1, d))
    for code in itertools.product(base, repeat=d - 3):
        yield tuple(sorted((*prufer_decode(base, code), edge(1, d))))


def parents(tree: tuple[tuple[int, int], ...], root: int):
    graph = defaultdict(list)
    for a, b in tree:
        graph[a].append(b)
        graph[b].append(a)
    parent: dict[int, int | None] = {root: None}
    todo = deque([root])
    while todo:
        a = todo.popleft()
        for b in sorted(graph[a]):
            if b not in parent:
                parent[b] = a
                todo.append(b)
    assert set(parent) == set(range(1, root + 1))
    assert len(tree) == root - 1
    return parent


def canonical_order(rank: int) -> tuple[int, ...]:
    modulus = 2 * rank - 2
    return (modulus - 1, modulus, *range(1, modulus - 1))


def swap_values(order: tuple[int, ...], edit: int) -> tuple[int, ...]:
    return tuple(
        edit + 1 if q == edit else edit if q == edit + 1 else q
        for q in order
    )


def contour(
    tree: tuple[tuple[int, int], ...],
    rank: int,
    order,
    start_state=None,
):
    """Emit one full clockwise boundary cycle of the hairy Hurwitz tree."""

    parent = parents(tree, rank)
    incidence = defaultdict(dict)
    first_black = {}
    for child in range(1, rank):
        left, right = order[2 * child - 2 : 2 * child]
        black = ("B", child)
        for label, white_id in ((left, child), (right, parent[child])):
            assert white_id is not None
            white = ("W", white_id)
            incidence[black][label] = white
            incidence[white][label] = black
            first_black[label] = child

    # Start just after a literal tree side.  This remains valid when an edit
    # moves the largest label away from the old root edge.
    starts = [
        (node, label)
        for node, by_label in incidence.items()
        if node[0] == "W"
        for label in by_label
    ]
    state = min(starts) if start_state is None else start_state
    assert state in starts
    initial = state
    seen = set()
    tokens = []
    side_serial = 0
    modulus = 2 * rank - 2
    while state not in seen:
        seen.add(state)
        node, incoming = state
        step = 1 if node[0] == "W" else -1
        label = 1 + ((incoming - 1 + step) % modulus)
        other = incidence[node].get(label)
        if other is None:
            tokens.append(("H", node[0], node[1], label))
            state = node, label
        else:
            tokens.append(("S", side_serial))
            side_serial += 1
            state = other, label
    assert state == initial
    assert len(tokens) == (2 * rank - 1) * modulus
    assert set(first_black) == set(range(1, modulus + 1))
    return tokens, first_black


def is_half(token) -> bool:
    return token[0] == "H"


def is_side(token) -> bool:
    return token[0] in ("S", "C")


def cycle_rotate(tokens):
    """Rotate after the last minimum of white-minus-black half-edge balance."""

    balance = 0
    minimum = 0
    cut_after = -1
    for i, token in enumerate(tokens):
        if is_half(token):
            balance += 1 if token[1] == "W" else -1
        if balance <= minimum:
            minimum = balance
            cut_after = i
    cut = (cut_after + 1) % len(tokens)
    return tokens[cut:] + tokens[:cut]


def close(tree, rank: int, order, start_state=None):
    raw, first_black = contour(tree, rank, order, start_state)
    linear = cycle_rotate(raw)
    reduced = []
    second_black = {}
    rows = []
    for token in linear:
        if not is_half(token) or token[1] == "W":
            reduced.append(token)
            continue

        white_index = max(i for i, prior in enumerate(reduced) if is_half(prior))
        white = reduced[white_index]
        assert white[1] == "W"
        assert white[3] == token[3]
        inside = reduced[white_index + 1 :]
        assert all(is_side(x) for x in inside)
        distance = len(inside)
        assert distance in (1, 3)
        row = (token[3], white[2], token[2], distance)
        rows.append(row)
        if distance == 3:
            assert token[3] not in second_black
            second_black[token[3]] = token[2]
        reduced[white_index:] = [("C", len(rows) - 1)]

    residue = [x for x in reduced if is_half(x)]
    modulus = 2 * rank - 2
    assert len(residue) == modulus
    assert all(x[1] == "W" for x in residue)
    assert sorted(x[3] for x in residue) == list(range(1, modulus + 1))
    endpoints = {
        q: second_black.get(q, rank) for q in range(1, modulus + 1)
    }
    word = tuple(
        edge(first_black[q] - 1, endpoints[q] - 1)
        for q in range(1, modulus + 1)
    )
    return {
        "word": word,
        "first": first_black,
        "second": second_black,
        "endpoints": endpoints,
        "rows": rows,
    }


def conjugate(x, by):
    a, b = by

    def image(v):
        return b if v == a else a if v == b else v

    return edge(image(x[0]), image(x[1]))


def move(word, signed_position: int):
    pos = abs(signed_position) - 1
    x, y = word[pos : pos + 2]
    result = list(word)
    if signed_position > 0:
        result[pos : pos + 2] = y, conjugate(x, y)
    else:
        result[pos : pos + 2] = conjugate(y, x), x
    return tuple(result)


def act(word, route):
    for generator in route:
        word = move(word, generator)
    return word


def evaluates_to_identity(word, rank: int) -> bool:
    image = list(range(rank))
    for a, b in word:
        image[a], image[b] = image[b], image[a]
    return image == list(range(rank))


def endpoints(tree, d: int, edit: int):
    old = close(tree, d, swap_values(canonical_order(d), edit))
    k = edge(0, d)
    old_padded = old["word"] + (k, k)
    new_tree = tuple(sorted((*tree, edge(1, d + 1))))
    new = close(new_tree, d + 1, swap_values(canonical_order(d + 1), edit))
    assert evaluates_to_identity(old_padded, d + 1)
    assert evaluates_to_identity(new["word"], d + 1)
    return old, old_padded, new


def expected_internal(parent, v: int):
    e = edge(v - 1, parent[v] - 1)
    f = edge(v, parent[v + 1] - 1)
    if parent[v] == parent[v + 1]:
        case = "common_parent"
        factors = (e, f, conjugate(e, f), f)
        seconds = (parent[v], parent[v], v + 1, parent[v])
    elif parent[v + 1] == v:
        case = "next_child"
        factors = (e, conjugate(f, e), e, f)
        seconds = (parent[v], parent[v], parent[v], v)
    elif parent[v] == v + 1:
        case = "previous_child"
        c = conjugate(e, f)
        assert c == conjugate(f, e)
        factors = (c, e, c, f)
        seconds = (parent[v + 1], v, parent[v + 1], parent[v + 1])
    else:
        case = "disjoint"
        assert set(e).isdisjoint(f)
        factors = (e, f, e, f)
        seconds = (parent[v], parent[v + 1], parent[v], parent[v + 1])
    return case, factors, seconds


def audit_rank(d: int):
    trees = tuple(rooted_leaf_trees(d))
    assert len(trees) == (d - 1) ** (d - 3)
    incidence_counts = Counter()
    boundary_counts = Counter()
    chronology_counts = Counter()
    internal_rows = cross_rows = last_rows = 0

    for tree in trees:
        parent = parents(tree, d)
        base_old_data = close(tree, d, canonical_order(d))
        k = edge(0, d)
        base_old = base_old_data["word"] + (k, k)
        new_tree = tuple(sorted((*tree, edge(1, d + 1))))
        base_new = close(new_tree, d + 1, canonical_order(d + 1))["word"]
        assert base_old == base_new

        for edit in range(2, 2 * d - 5, 2):
            old, old_word, new = endpoints(tree, d, edit)
            v = (edit + 2) // 2
            case, factors, seconds = expected_internal(parent, v)
            labels = tuple(range(edit - 1, edit + 3))
            sl = slice(edit - 2, edit + 2)
            assert old_word[sl] == factors == new["word"][sl]
            assert tuple(old["first"][q] for q in labels) == (v, v + 1, v, v + 1)
            assert tuple(new["first"][q] for q in labels) == (v, v + 1, v, v + 1)
            assert tuple(old["second"][q] for q in labels) == seconds
            assert tuple(new["second"][q] for q in labels) == seconds
            mask = set(range(edit - 2, edit + 2))
            assert all(
                x == base_old[pos]
                for pos, x in enumerate(old_word)
                if pos not in mask
            )
            assert all(
                x == base_new[pos]
                for pos, x in enumerate(new["word"])
                if pos not in mask
            )
            assert old_word == new["word"]
            incidence_counts[case] += 1
            internal_rows += 1

        m = 2 * d - 2
        lam, mu, alpha, beta, gamma, delta = (
            m - 3,
            m - 2,
            m - 1,
            m,
            m + 1,
            m + 2,
        )
        h = edge(d - 2, parent[d - 1] - 1)
        g = edge(0, d - 1)
        a = conjugate(h, g)
        b = conjugate(g, a)

        old, old_word, new = endpoints(tree, d, m - 2)
        expected_old = (a, b, a, g, k, k)
        expected_new = (h, g, a, g, k, k)
        assert old_word[lam - 1 :] == expected_old
        assert new["word"][lam - 1 :] == expected_new
        assert old_word[: lam - 1] == new["word"][: lam - 1]
        after_one = move(old_word, -lam)
        assert after_one[lam - 1 : lam + 2] == (g, a, a)
        assert move(after_one, -lam) == new["word"]
        assert act(new["word"], (lam, lam)) == old_word
        assert tuple(old["first"][q] for q in (lam, mu, alpha, beta)) == (
            d - 1,
            1,
            d - 1,
            1,
        )
        r = parent[d - 1]
        if r == 1:
            assert lam not in old["second"]
            assert old["second"][mu] == d - 1
            assert alpha not in old["second"]
            boundary_counts["parent_one"] += 1
        else:
            assert old["second"][lam] == r
            assert mu not in old["second"]
            assert old["second"][alpha] == r
            boundary_counts["parent_not_one"] += 1
        assert beta not in old["second"]
        assert tuple(new["first"][q] for q in (lam, mu, alpha, beta, gamma, delta)) == (
            d - 1,
            d,
            d - 1,
            d,
            1,
            1,
        )
        assert new["second"][lam] == r
        assert new["second"][mu] == 1
        assert new["second"][alpha] == (d if r == 1 else r)
        assert new["second"][beta] == 1
        assert gamma not in new["second"] and delta not in new["second"]
        cross_rows += 1

        old, old_word, new = endpoints(tree, d, m - 1)
        assert old_word[alpha - 1 :] == (g, g, k, k)
        assert new["word"][alpha - 1 :] == (
            g,
            conjugate(k, g),
            g,
            k,
        )
        assert old_word[: alpha - 1] == new["word"][: alpha - 1]
        assert act(old_word, (-beta,)) == new["word"]
        assert act(new["word"], (beta,)) == old_word
        assert tuple(old["first"][q] for q in (alpha, beta)) == (1, 1)
        assert alpha not in old["second"] and beta not in old["second"]
        assert tuple(new["first"][q] for q in (alpha, beta, gamma, delta)) == (
            d,
            d,
            1,
            1,
        )
        assert new["second"][alpha] == 1
        assert beta not in new["second"]
        assert new["second"][gamma] == d
        assert delta not in new["second"]
        seam_order = tuple(
            q
            for q, _white, _black, distance in new["rows"]
            if distance == 3 and q in (alpha, gamma)
        )
        assert seam_order == (alpha, gamma)
        chronology_counts["-".join(map(str, seam_order))] += 1

        root_side_cut = (("W", d + 1), 2 * (d + 1) - 2)
        alternate = close(
            new_tree,
            d + 1,
            swap_values(canonical_order(d + 1), m - 1),
            start_state=root_side_cut,
        )
        assert alternate["word"] == new["word"]
        alternate_order = tuple(
            q
            for q, _white, _black, distance in alternate["rows"]
            if distance == 3 and q in (alpha, gamma)
        )
        assert alternate_order == (gamma, alpha)
        chronology_counts["root_cut_" + "-".join(map(str, alternate_order))] += 1
        last_rows += 1

    ordinary = set(range(1, 2 * d - 4, 2))
    internal = set(range(2, 2 * d - 5, 2))
    cross = {2 * d - 4}
    last = {2 * d - 3}
    families = (ordinary, internal, cross, last)
    assert set().union(*families) == set(range(1, 2 * d - 2))
    assert sum(len(x) for x in families) == 2 * d - 3
    max_route = max(
        [4 * (d - v - 1) + 5 for v in range(2, d)] + [0, 2, 1]
    )
    assert max_route == 4 * d - 7

    return {
        "d": d,
        "trees": len(trees),
        "internal_rows": internal_rows,
        "cross_rows": cross_rows,
        "last_rows": last_rows,
        "incidence_counts": dict(sorted(incidence_counts.items())),
        "boundary_counts": dict(sorted(boundary_counts.items())),
        "last_seam_chronology": dict(sorted(chronology_counts.items())),
        "all_edit_indices_partition": True,
        "maximum_local_route_length": max_route,
        "pass": True,
    }


def normalized_digest(rows) -> str:
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


def main() -> None:
    ranks = [audit_rank(d) for d in (5, 6)]
    result = {
        "mission": "M281",
        "purpose": "clean-room fixed-edit endpoint and route falsifier",
        "imports_m278_or_predecessor": False,
        "route_search": False,
        "tested_ranks": [5, 6],
        "python": platform.python_version(),
        "ranks": ranks,
        "totals": {
            "trees": sum(x["trees"] for x in ranks),
            "internal_rows": sum(x["internal_rows"] for x in ranks),
            "cross_rows": sum(x["cross_rows"] for x in ranks),
            "last_rows": sum(x["last_rows"] for x in ranks),
        },
        "m278_nonmaterial_chronology_correction": (
            "the two seam closures and their endpoints are invariant, but "
            "their execution order depends on the allowed cyclic start; "
            "M278 states one order without fixing that start"
        ),
        "pass": all(x["pass"] for x in ranks),
    }
    result["normalized_rank_digest"] = normalized_digest(ranks)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
