#!/usr/bin/env python3
"""Independent exact guard for the M275 root-seam referee.

This script was written after cleanroom_derivation.md was frozen.  It imports
no M273 code or data.  It reconstructs the plus-mirror hairy contour directly,
performs a cycle-lemma linearization and LIFO closure, and checks targeted
root-input schemas plus the complete d=5,6 tree census.  Finite success is
calibration, not the arbitrary-rank proof.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import platform
from collections import Counter, defaultdict, deque
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "guard_results.json"


def edge(a: int, b: int) -> tuple[int, int]:
    assert a != b
    return (a, b) if a < b else (b, a)


def get_parents(tree: tuple[tuple[int, int], ...], root: int) -> dict[int, int | None]:
    graph: dict[int, list[int]] = defaultdict(list)
    for a, b in tree:
        graph[a].append(b)
        graph[b].append(a)
    parent: dict[int, int | None] = {root: None}
    queue = deque([root])
    while queue:
        a = queue.popleft()
        for b in graph[a]:
            if b not in parent:
                parent[b] = a
                queue.append(b)
    assert set(parent) == set(range(1, root + 1))
    assert len(tree) == root - 1
    return parent


def base_order(rank: int) -> tuple[int, ...]:
    return (2 * rank - 3, 2 * rank - 2, *range(1, 2 * rank - 3))


def edited_order(rank: int, v: int) -> tuple[int, ...]:
    left = 2 * v - 3
    return tuple(
        left + 1 if q == left else left if q == left + 1 else q
        for q in base_order(rank)
    )


def raw_contour(
    tree: tuple[tuple[int, int], ...], rank: int, v: int
) -> tuple[list[tuple], dict[int, int]]:
    """Emit the literal cyclic plus-mirror contour from the incidence map."""

    parent = get_parents(tree, rank)
    incidence: dict[tuple[str, int], dict[int, tuple[str, int]]] = defaultdict(dict)
    first_black: dict[int, int] = {}
    order = edited_order(rank, v)
    for a in range(1, rank):
        left, right = order[2 * a - 2 : 2 * a]
        black = ("B", a)
        for label, white_number in ((left, a), (right, parent[a])):
            assert white_number is not None
            white = ("W", white_number)
            incidence[black][label] = white
            incidence[white][label] = black
            first_black[label] = a

    modulus = 2 * rank - 2
    start = (("W", rank), modulus)
    assert modulus in incidence[start[0]]
    state = start
    seen: set[tuple[tuple[str, int], int]] = set()
    tokens: list[tuple] = []
    serial = 0
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        direction = 1 if vertex[0] == "W" else -1
        label = 1 + ((incoming - 1 + direction) % modulus)
        neighbor = incidence[vertex].get(label)
        if neighbor is None:
            tokens.append(("H", vertex[0], vertex[1], label))
            state = (vertex, label)
        else:
            tokens.append(("S", serial, vertex, neighbor, label))
            serial += 1
            state = (neighbor, label)
    assert state == start
    return tokens, first_black


def is_half(token: tuple) -> bool:
    return token[0] == "H"


def is_side(token: tuple) -> bool:
    return token[0] in ("S", "C")


def cycle_lemma(tokens: list[tuple]) -> list[tuple]:
    balance = 0
    minimum = 0
    last_minimum = -1
    for j, token in enumerate(tokens):
        if is_half(token):
            balance += 1 if token[1] == "W" else -1
        if balance <= minimum:
            minimum = balance
            last_minimum = j
    cut = (last_minimum + 1) % len(tokens)
    return tokens[cut:] + tokens[:cut]


def expand(token: tuple) -> list[tuple]:
    if token[0] != "C":
        return [token]
    answer: list[tuple] = []
    for child in token[2]:
        answer.extend(expand(child))
    return answer


def close(tree: tuple[tuple[int, int], ...], rank: int, v: int) -> dict:
    original, first_black = raw_contour(tree, rank, v)
    linear = cycle_lemma(original)
    reduced: list[tuple] = []
    second_black: dict[int, int] = {}
    rows: list[dict] = []

    for token in linear:
        if not is_half(token) or token[1] == "W":
            reduced.append(token)
            continue

        white_pos = max(j for j, item in enumerate(reduced) if is_half(item))
        white = reduced[white_pos]
        assert white[1] == "W"
        assert white[3] == token[3]
        interior = reduced[white_pos + 1 :]
        assert all(is_side(item) for item in interior)
        distance = len(interior)
        assert distance in (1, 3)
        row = {
            "index": len(rows),
            "label": white[3],
            "white": white[2],
            "black": token[2],
            "distance": distance,
        }
        rows.append(row)
        if distance == 3:
            assert white[3] not in second_black
            second_black[white[3]] = token[2]
        segment = tuple((*reduced[white_pos:], token))
        reduced[white_pos:] = [("C", len(rows) - 1, segment)]

    reconstructed: list[tuple] = []
    for token in reduced:
        reconstructed.extend(expand(token))
    assert reconstructed == linear

    modulus = 2 * rank - 2
    remaining = [token for token in reduced if is_half(token)]
    assert len(remaining) == modulus
    assert all(token[1] == "W" for token in remaining)
    assert sorted(token[3] for token in remaining) == list(range(1, modulus + 1))
    remaining_white = {token[3]: token[2] for token in remaining}
    endpoints = {q: second_black.get(q, rank) for q in range(1, modulus + 1)}
    word = tuple(
        edge(first_black[q] - 1, endpoints[q] - 1)
        for q in range(1, modulus + 1)
    )
    return {
        "rows": rows,
        "second_black": second_black,
        "remaining_white": remaining_white,
        "endpoints": endpoints,
        "word": word,
        "inverse_ok": reconstructed == linear,
    }


def stopped_path(parent: dict[int, int | None], v: int) -> tuple[int, ...]:
    path = [v]
    while path[-1] != 1:
        nxt = parent[path[-1]]
        assert nxt is not None
        path.append(nxt)
    return tuple(path)


def width(rank: int, v: int, a: int) -> int:
    modulus = 2 * rank - 2
    right_v = 2 * v - 2
    right_a = modulus if a == 1 else 2 * a - 2
    answer = (right_a - right_v) % modulus
    assert answer
    return answer


def root_input_class(parent: dict[int, int | None], rank: int, v: int) -> str:
    path = stopped_path(parent, v)
    if path == (v, 1):
        return "direct_root_reversed_base"

    current = path[1]
    sealed = False
    for nxt in path[2:-1]:
        if width(rank, v, nxt) > width(rank, v, current):
            sealed = True
            break
        current = nxt
    if sealed:
        return "C"
    return (
        "F_contraction"
        if width(rank, v, 1) < width(rank, v, current)
        else "F_expansion"
    )


def unique_row(data: dict, label: int, white: int, black: int, distance: int) -> dict:
    matches = [
        row
        for row in data["rows"]
        if (row["label"], row["white"], row["black"], row["distance"])
        == (label, white, black, distance)
    ]
    assert len(matches) == 1
    return matches[0]


def audit(
    tree_input,
    d: int,
    v: int,
    expected_class: str | None = None,
    expected_ports: dict[int, int | str] | None = None,
) -> dict:
    tree = tuple(sorted(edge(*e) for e in tree_input))
    parent = get_parents(tree, d)
    path = stopped_path(parent, v)
    open_path = all(a > b for a, b in zip(path, path[1:]))
    input_class = root_input_class(parent, d, v)
    if expected_class is not None:
        assert input_class == expected_class

    old = close(tree, d, v)
    new_tree = tuple(sorted((*tree, edge(1, d + 1))))
    new = close(new_tree, d + 1, v)
    assert old["inverse_ok"] and new["inverse_ok"]

    m = 2 * d - 2
    alpha, beta, gamma, delta = m - 1, m, m + 1, m + 2
    if open_path:
        assert {q: old["endpoints"][q] for q in (alpha, beta)} == {
            alpha: v,
            beta: d,
        }
        assert {q: new["endpoints"][q] for q in (alpha, beta, gamma, delta)} == {
            alpha: 1,
            beta: 1,
            gamma: v,
            delta: d + 1,
        }
        unique_row(old, alpha, d, v, 3)
        unique_row(new, gamma, d + 1, v, 3)
    else:
        assert {q: old["endpoints"][q] for q in (alpha, beta)} == {
            alpha: d,
            beta: d,
        }
        assert {q: new["endpoints"][q] for q in (alpha, beta, gamma, delta)} == {
            alpha: 1,
            beta: 1,
            gamma: d + 1,
            delta: d + 1,
        }

    seam_beta = unique_row(new, beta, d, 1, 3)
    seam_alpha = unique_row(new, alpha, 1, 1, 3)
    assert seam_beta["index"] + 1 == seam_alpha["index"]

    exposed = {2 * v - 2}
    exposed.update(
        q
        for h in range(v + 1, d)
        if parent[h] == v
        for q in (2 * h - 3, 2 * h - 2)
    )
    endpoint_pairs = []
    for q in range(1, m - 1):
        pair = old["endpoints"][q], new["endpoints"][q]
        wanted = (d, d + 1) if open_path and q in exposed else (pair[0], pair[0])
        assert pair == wanted
        endpoint_pairs.append((q, *pair))

    if open_path:
        # R_v=q_0 lies outside A_v and is supplied by the root complement.
        assert old["remaining_white"][2 * v - 2] == d
        assert new["remaining_white"][2 * v - 2] == d + 1
        for h in range(v + 1, d):
            if parent[h] == v:
                left, right = 2 * h - 3, 2 * h - 2
                assert old["remaining_white"][left] == v
                assert old["remaining_white"][right] == h
                assert new["remaining_white"][left] == v
                assert new["remaining_white"][right] == h

    port_rows = []
    for h, expected in (expected_ports or {}).items():
        assert parent[h] == v
        left, right = 2 * h - 3, 2 * h - 2
        if expected == "root":
            assert (old["endpoints"][left], old["endpoints"][right]) == (d, d)
            assert (new["endpoints"][left], new["endpoints"][right]) == (d + 1, d + 1)
            assert left not in old["second_black"] and right not in old["second_black"]
            assert left not in new["second_black"] and right not in new["second_black"]
            port_rows.append((h, "persistent", d, d + 1))
        else:
            assert isinstance(expected, int)
            for data in (old, new):
                row_r = unique_row(data, right, h, expected, 3)
                row_l = unique_row(data, left, v, expected, 3)
                assert row_r["index"] + 1 == row_l["index"]
                assert data["endpoints"][left] == data["endpoints"][right] == expected
            port_rows.append((h, "discharged", expected))

    return {
        "d": d,
        "v": v,
        "tree": tree,
        "path": path,
        "root_input": input_class,
        "open": open_path,
        "exposed": sorted(exposed),
        "endpoint_pairs": endpoint_pairs,
        "seam_order": (seam_beta["index"], seam_alpha["index"]),
        "port_rows": port_rows,
        "old_word_hash": hashlib.sha256(repr(old["word"]).encode()).hexdigest(),
        "new_word_hash": hashlib.sha256(repr(new["word"]).encode()).hexdigest(),
        "inverse_ok": True,
    }


def prufer_tree(vertices: tuple[int, ...], code: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    degree = {a: 1 for a in vertices}
    for a in code:
        degree[a] += 1
    answer = []
    for a in code:
        leaf = min(b for b in vertices if degree[b] == 1)
        answer.append(edge(leaf, a))
        degree[leaf] -= 1
        degree[a] -= 1
    leaves = [a for a in vertices if degree[a] == 1]
    answer.append(edge(*leaves))
    return tuple(sorted(answer))


def rooted_leaf_trees(d: int):
    vertices = tuple(range(1, d))
    for code in itertools.product(vertices, repeat=d - 3):
        yield tuple(sorted((*prufer_tree(vertices, code), edge(1, d))))


def main() -> None:
    targeted_specs = (
        {
            "name": "direct_boundary",
            "d": 7,
            "v": 6,
            "kind": "direct_root_reversed_base",
            "tree": ((1, 7), (1, 6), (1, 2), (1, 3), (1, 4), (1, 5)),
        },
        {
            "name": "direct_with_both_port_sides",
            "d": 8,
            "v": 4,
            "kind": "direct_root_reversed_base",
            "tree": ((1, 8), (1, 4), (4, 5), (4, 3), (1, 2), (1, 6), (1, 7)),
            "ports": {5: "root", 3: 1},
        },
        {
            "name": "root_contraction_and_nonroot_port_crossing",
            "d": 9,
            "v": 6,
            "kind": "F_contraction",
            "tree": ((1, 9), (1, 3), (3, 5), (5, 6), (6, 7), (6, 4), (1, 2), (1, 8)),
            "ports": {7: "root", 4: 3},
        },
        {
            "name": "root_expansion",
            "d": 8,
            "v": 4,
            "kind": "F_expansion",
            "tree": ((1, 8), (1, 6), (6, 4), (4, 5), (1, 2), (1, 3), (1, 7)),
            "ports": {5: 1},
        },
        {
            "name": "already_sealed_C",
            "d": 8,
            "v": 4,
            "kind": "C",
            "tree": ((1, 8), (1, 2), (2, 5), (5, 3), (3, 4), (1, 6), (1, 7)),
        },
    )

    targeted = []
    for spec in targeted_specs:
        row = audit(
            spec["tree"], spec["d"], spec["v"], spec["kind"], spec.get("ports")
        )
        row["name"] = spec["name"]
        targeted.append(row)

    census_rows = []
    class_counts: Counter[str] = Counter()
    open_count = 0
    for d in (5, 6):
        trees = list(rooted_leaf_trees(d))
        assert len(trees) == (d - 1) ** (d - 3)
        for tree in trees:
            for v in range(2, d):
                row = audit(tree, d, v)
                class_counts[row["root_input"]] += 1
                open_count += int(row["open"])
                census_rows.append(
                    (d, v, row["tree"], row["path"], row["root_input"], row["open"])
                )

    result = {
        "mission": "M275 independent decorated-root-seam referee guard",
        "status": "exact finite calibration only",
        "predecessor_imports": False,
        "m273_imports": False,
        "seed": None,
        "targeted": targeted,
        "targeted_digest": hashlib.sha256(
            json.dumps(targeted, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
        "census": {
            "ranks": [5, 6],
            "trees": {"5": 16, "6": 125},
            "rows": len(census_rows),
            "open": open_count,
            "closed": len(census_rows) - open_count,
            "root_input_counts": dict(sorted(class_counts.items())),
            "digest": hashlib.sha256(
                json.dumps(census_rows, sort_keys=True, separators=(",", ":")).encode()
            ).hexdigest(),
        },
        "failures": [],
        "environment": {
            "python": platform.python_version(),
            "nonstandard_dependencies": {},
        },
        "scope": {
            "proves_all_rank": False,
            "proves_idl_without_the_analytic_chain": False,
            "fixed_edits": False,
            "every_color": False,
            "gap_or_mixing": False,
        },
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
