#!/usr/bin/env python3
"""No-predecessor-import guard for the frozen M278 fixed-edit formulas."""

from __future__ import annotations

import heapq
import itertools
import json
import platform
from collections import Counter, defaultdict, deque
from pathlib import Path


OUTPUT = Path(__file__).with_name("guard_results.json")


def edge(left: int, right: int) -> tuple[int, int]:
    assert left != right
    return (left, right) if left < right else (right, left)


def decode_prufer(vertices: tuple[int, ...], code: tuple[int, ...]):
    degree = Counter({vertex: 1 for vertex in vertices})
    degree.update(code)
    leaves = [vertex for vertex in vertices if degree[vertex] == 1]
    heapq.heapify(leaves)
    result = []
    for vertex in code:
        leaf = heapq.heappop(leaves)
        result.append(edge(leaf, vertex))
        degree[leaf] -= 1
        degree[vertex] -= 1
        if degree[vertex] == 1:
            heapq.heappush(leaves, vertex)
    result.append(edge(heapq.heappop(leaves), heapq.heappop(leaves)))
    return frozenset(result)


def root_leaf_templates(d: int):
    base = tuple(range(1, d))
    for code in itertools.product(base, repeat=d - 3):
        yield decode_prufer(base, code) | {edge(1, d)}


def parent_map(tree, root: int):
    adjacency = {vertex: [] for vertex in range(1, root + 1)}
    for left, right in tree:
        adjacency[left].append(right)
        adjacency[right].append(left)
    parent = {root: None}
    queue = deque([root])
    while queue:
        vertex = queue.popleft()
        for neighbor in sorted(adjacency[vertex]):
            if neighbor not in parent:
                parent[neighbor] = vertex
                queue.append(neighbor)
    assert len(parent) == root
    return parent


def trace_tokens(tree, order: tuple[int, ...], rank: int):
    parent = parent_map(tree, rank)
    ports = defaultdict(dict)
    first_black = {}
    for child in range(1, rank):
        black = ("b", child)
        left, right = order[2 * child - 2 : 2 * child]
        for label, white_id in ((left, child), (right, parent[child])):
            white = ("w", white_id)
            ports[black][label] = white
            ports[white][label] = black
            first_black[label] = child

    modulus = 2 * rank - 2
    initial = (("w", 1), 1)
    state = initial
    seen = set()
    trace = []
    while state not in seen:
        seen.add(state)
        node, incoming = state
        step = 1 if node[0] == "w" else -1
        label = 1 + ((incoming - 1 + step) % modulus)
        if label in ports[node]:
            trace.append(("side",))
            state = ports[node][label], label
        else:
            trace.append(("open", node[0], node[1], label))
            state = node, label
    assert state == initial
    assert len(trace) == (2 * rank - 1) * modulus
    return trace, first_black


def close_lifo(trace, rank: int):
    trace = list(trace)
    second_black = {}
    while True:
        opens = [index for index, item in enumerate(trace) if item[0] == "open"]
        selected = None
        for offset, white_index in enumerate(opens):
            black_index = opens[(offset + 1) % len(opens)]
            if (
                trace[white_index][1] == "w"
                and trace[black_index][1] == "b"
            ):
                selected = white_index, black_index
                break
        if selected is None:
            break
        white_index, black_index = selected
        trace = trace[white_index:] + trace[:white_index]
        black_index = (black_index - white_index) % len(trace)
        white, black = trace[0], trace[black_index]
        assert white[3] == black[3]
        side_count = sum(item[0] == "side" for item in trace[1:black_index])
        assert side_count in (1, 3)
        if side_count == 3:
            second_black[white[3]] = black[2]
        trace = [("side",)] + trace[black_index + 1 :]

    residue = [item for item in trace if item[0] == "open"]
    assert len(residue) == 2 * rank - 2
    assert all(item[1] == "w" for item in residue)
    return second_black


def dps_data(tree, order: tuple[int, ...], rank: int):
    trace, first_black = trace_tokens(tree, order, rank)
    second_black = close_lifo(trace, rank)
    word = tuple(
        edge(first_black[label] - 1, second_black.get(label, rank) - 1)
        for label in range(1, 2 * rank - 1)
    )
    return word, first_black, second_black


def canonical_order(rank: int):
    return (2 * rank - 3, 2 * rank - 2) + tuple(range(1, 2 * rank - 3))


def edited_order(order: tuple[int, ...], edit: int):
    return tuple(
        edit + 1 if label == edit else edit if label == edit + 1 else label
        for label in order
    )


def conjugate(transposition, by):
    left, right = by

    def image(vertex):
        return right if vertex == left else left if vertex == right else vertex

    return edge(image(transposition[0]), image(transposition[1]))


def hurwitz(word, signed_generator: int):
    position = abs(signed_generator) - 1
    left, right = word[position : position + 2]
    result = list(word)
    if signed_generator > 0:
        result[position : position + 2] = (
            right,
            conjugate(left, right),
        )
    else:
        result[position : position + 2] = (
            conjugate(right, left),
            left,
        )
    return tuple(result)


def act(word, route):
    for signed_generator in route:
        word = hurwitz(word, signed_generator)
    return word


def endpoint_data(tree, d: int, edit: int):
    old_order = edited_order(canonical_order(d), edit)
    old_word, old_first, old_second = dps_data(tree, old_order, d)
    k = edge(0, d)
    old_padded = old_word + (k, k)

    extension = tree | {edge(1, d + 1)}
    new_order = edited_order(canonical_order(d + 1), edit)
    new_word, new_first, new_second = dps_data(extension, new_order, d + 1)
    return {
        "old": old_padded,
        "new": new_word,
        "old_first": old_first,
        "old_second": old_second,
        "new_first": new_first,
        "new_second": new_second,
    }


def expected_internal(parent, v: int):
    e = edge(v - 1, parent[v] - 1)
    f = edge(v, parent[v + 1] - 1)
    if parent[v] == parent[v + 1]:
        return "common_parent", (e, f, conjugate(e, f), f)
    if parent[v + 1] == v:
        return "next_child", (e, conjugate(f, e), e, f)
    if parent[v] == v + 1:
        c = conjugate(e, f)
        assert c == conjugate(f, e)
        return "previous_child", (c, e, c, f)
    assert set(e).isdisjoint(f)
    return "disjoint", (e, f, e, f)


def check_rank(d: int):
    trees = tuple(root_leaf_templates(d))
    assert len(trees) == (d - 1) ** (d - 3)
    incidence = Counter()
    boundary = Counter()
    internal_rows = 0
    cross_rows = 0
    last_rows = 0

    for tree in trees:
        parent = parent_map(tree, d)
        base_old = dps_data(tree, canonical_order(d), d)[0] + (
            edge(0, d),
            edge(0, d),
        )
        extension = tree | {edge(1, d + 1)}
        base_new = dps_data(extension, canonical_order(d + 1), d + 1)[0]
        assert base_old == base_new

        for edit in range(2, 2 * d - 5, 2):
            data = endpoint_data(tree, d, edit)
            v = (edit + 2) // 2
            case, expected = expected_internal(parent, v)
            window = slice(edit - 2, edit + 2)
            assert data["old"][window] == expected
            assert data["new"][window] == expected
            mask = set(range(edit - 2, edit + 2))
            assert all(
                value == base_old[position]
                for position, value in enumerate(data["old"])
                if position not in mask
            )
            assert all(
                value == base_new[position]
                for position, value in enumerate(data["new"])
                if position not in mask
            )
            assert data["old"] == data["new"]
            incidence[case] += 1
            internal_rows += 1

        m = 2 * d - 2
        alpha, beta, gamma, delta = m - 1, m, m + 1, m + 2
        j = m - 3
        h = edge(d - 2, parent[d - 1] - 1)
        g = edge(0, d - 1)
        k = edge(0, d)
        a = conjugate(h, g)
        b = conjugate(g, a)

        cross = endpoint_data(tree, d, m - 2)
        assert cross["old"][j - 1 :] == (a, b, a, g, k, k)
        assert cross["new"][j - 1 :] == (h, g, a, g, k, k)
        assert cross["old"][: j - 1] == cross["new"][: j - 1]
        assert act(cross["old"], (-j, -j)) == cross["new"]

        r = parent[d - 1]
        old_first = cross["old_first"]
        old_second = cross["old_second"]
        new_first = cross["new_first"]
        new_second = cross["new_second"]
        assert tuple(old_first[q] for q in (j, j + 1, alpha, beta)) == (
            d - 1,
            1,
            d - 1,
            1,
        )
        if r == 1:
            assert j not in old_second
            assert old_second[j + 1] == d - 1
            assert alpha not in old_second
        else:
            assert old_second[j] == r
            assert j + 1 not in old_second
            assert old_second[alpha] == r
        assert beta not in old_second
        assert tuple(
            new_first[q] for q in (j, j + 1, alpha, beta, gamma, delta)
        ) == (d - 1, d, d - 1, d, 1, 1)
        assert new_second[j] == r
        assert new_second[j + 1] == 1
        assert new_second[alpha] == (d if r == 1 else r)
        assert new_second[beta] == 1
        assert gamma not in new_second and delta not in new_second
        boundary["parent_one" if r == 1 else "parent_not_one"] += 1
        cross_rows += 1

        last = endpoint_data(tree, d, m - 1)
        assert last["old"][alpha - 1 :] == (g, g, k, k)
        assert last["new"][alpha - 1 :] == (
            g,
            conjugate(k, g),
            g,
            k,
        )
        assert last["old"][: alpha - 1] == last["new"][: alpha - 1]
        assert act(last["old"], (-beta,)) == last["new"]

        assert tuple(last["old_first"][q] for q in (alpha, beta)) == (1, 1)
        assert alpha not in last["old_second"]
        assert beta not in last["old_second"]
        assert tuple(
            last["new_first"][q] for q in (alpha, beta, gamma, delta)
        ) == (d, d, 1, 1)
        assert last["new_second"][alpha] == 1
        assert beta not in last["new_second"]
        assert last["new_second"][gamma] == d
        assert delta not in last["new_second"]
        last_rows += 1

    return {
        "d": d,
        "tree_count": len(trees),
        "internal_rows": internal_rows,
        "cross_boundary_rows": cross_rows,
        "last_edit_rows": last_rows,
        "incidence_counts": dict(sorted(incidence.items())),
        "cross_boundary_counts": dict(sorted(boundary.items())),
        "pass": True,
    }


def main():
    ranks = [check_rank(d) for d in (5, 6)]
    result = {
        "mission": "M278",
        "purpose": "post-analytic-lock transcription and boundary guard",
        "predecessor_imports": [],
        "searched_routes": False,
        "tested_ranks": [5, 6],
        "python": platform.python_version(),
        "ranks": ranks,
        "totals": {
            "trees": sum(row["tree_count"] for row in ranks),
            "internal_rows": sum(row["internal_rows"] for row in ranks),
            "cross_boundary_rows": sum(
                row["cross_boundary_rows"] for row in ranks
            ),
            "last_edit_rows": sum(row["last_edit_rows"] for row in ranks),
        },
        "pass": all(row["pass"] for row in ranks),
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
