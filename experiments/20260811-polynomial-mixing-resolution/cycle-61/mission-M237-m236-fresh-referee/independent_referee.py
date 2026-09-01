#!/usr/bin/env python3
"""Clean-room exact referee for M236's finite d=7 -> 8 theorem.

This program reads no mission artifact and imports no project module.  It
constructs the finite tree universe, the predeclared Z2/formula, both DPS
endpoints, and the chronological signed-Hurwitz replay directly.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path
import platform
from typing import Iterable


HERE = Path(__file__).resolve().parent
OUT = HERE / "referee_results.json"

Edge = tuple[int, int]
Tree = tuple[Edge, ...]
Action = tuple[int, int]
Word = tuple[Edge, ...]


def edge(a: int, b: int) -> Edge:
    assert a != b
    return (a, b) if a < b else (b, a)


def canonical_hash(obj) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":"))
    return sha256(raw.encode("utf-8")).hexdigest()


def jsonable(obj):
    if isinstance(obj, tuple):
        return [jsonable(x) for x in obj]
    if isinstance(obj, list):
        return [jsonable(x) for x in obj]
    if isinstance(obj, dict):
        return {str(k): jsonable(v) for k, v in obj.items()}
    return obj


def decode_prufer(labels: tuple[int, ...], code: tuple[int, ...]) -> Tree:
    """Decode a Prüfer word by the lexicographically least-leaf rule."""
    degree = {v: 1 for v in labels}
    for v in code:
        degree[v] += 1
    out: list[Edge] = []
    for v in code:
        leaf = min(x for x in labels if degree[x] == 1)
        out.append(edge(leaf, v))
        degree[leaf] -= 1
        degree[v] -= 1
    final = [x for x in labels if degree[x] == 1]
    assert len(final) == 2
    out.append(edge(final[0], final[1]))
    return tuple(sorted(out))


def direct_root_leaf_trees() -> tuple[Tree, ...]:
    labels = tuple(range(1, 8))
    answer: list[Tree] = []
    for code in product(labels, repeat=5):
        tree = decode_prufer(labels, code)
        root_edges = [e for e in tree if 7 in e]
        if root_edges == [(1, 7)]:
            answer.append(tree)
    assert len(answer) == 1296
    assert len(set(answer)) == 1296
    return tuple(answer)


def attached_root_leaf_trees() -> tuple[Tree, ...]:
    labels = tuple(range(1, 7))
    answer = []
    for code in product(labels, repeat=4):
        base = decode_prufer(labels, code)
        answer.append(tuple(sorted(base + ((1, 7),))))
    assert len(answer) == 1296
    assert len(set(answer)) == 1296
    return tuple(answer)


def rooted_parent(tree: Tree, root: int) -> dict[int, int | None]:
    adjacency: dict[int, list[int]] = defaultdict(list)
    for a, b in tree:
        adjacency[a].append(b)
        adjacency[b].append(a)
    parent: dict[int, int | None] = {root: None}
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in sorted(adjacency[u]):
            if v not in parent:
                parent[v] = u
                queue.append(v)
    assert len(parent) == root
    return parent


def canonical_pi(d: int) -> tuple[int, ...]:
    return (2 * d - 3, 2 * d - 2, *range(1, 2 * d - 3))


def swap_values(order: tuple[int, ...], edit: int) -> tuple[int, ...]:
    return tuple(
        edit + 1 if x == edit else edit if x == edit + 1 else x
        for x in order
    )


def dps_factorization(tree: Tree, order: tuple[int, ...], d: int) -> Word:
    """Close the rooted plus-mirror hairy-tree boundary from its definition."""
    assert len(order) == 2 * d - 2
    parent = rooted_parent(tree, d)

    # White vertices are positive; the black vertex inserted below child c is
    # encoded as -c.  Each labelled hairy-tree edge appears in both incidence
    # maps, and its first black endpoint is recorded immediately.
    incidence: dict[int, dict[int, int]] = defaultdict(dict)
    first_black: dict[int, int] = {}
    for child in range(1, d):
        black = -child
        lo, hi = order[2 * child - 2 : 2 * child]
        for label, white in ((lo, child), (hi, parent[child])):
            assert white is not None
            incidence[black][label] = white
            incidence[white][label] = black
            first_black[label] = child

    modulus = 2 * d - 2
    state = (1, 1)
    initial = state
    visited: set[tuple[int, int]] = set()
    boundary: list[tuple] = []
    while state not in visited:
        visited.add(state)
        vertex, incoming = state
        delta = 1 if vertex > 0 else -1
        label = 1 + ((incoming - 1 + delta) % modulus)
        if label in incidence[vertex]:
            boundary.append(("side",))
            state = (incidence[vertex][label], label)
        else:
            boundary.append(
                ("half", "white" if vertex > 0 else "black", abs(vertex), label)
            )
            state = (vertex, label)
    assert state == initial
    assert len(boundary) == (2 * d - 1) * modulus

    second_black: dict[int, int] = {}
    while True:
        half_positions = [i for i, token in enumerate(boundary) if token[0] == "half"]
        chosen: tuple[int, int] | None = None
        for k, white_pos in enumerate(half_positions):
            black_pos = half_positions[(k + 1) % len(half_positions)]
            if boundary[white_pos][1] == "white" and boundary[black_pos][1] == "black":
                chosen = (white_pos, black_pos)
                break
        if chosen is None:
            break
        white_pos, black_pos = chosen
        boundary = boundary[white_pos:] + boundary[:white_pos]
        black_pos = (black_pos - white_pos) % len(boundary)
        white_half, black_half = boundary[0], boundary[black_pos]
        assert white_half[3] == black_half[3]
        side_distance = sum(x[0] == "side" for x in boundary[1:black_pos])
        assert side_distance in (1, 3)
        if side_distance == 3:
            assert white_half[3] not in second_black
            second_black[white_half[3]] = black_half[2]
        boundary = [("side",)] + boundary[black_pos + 1 :]

    leftovers = [x for x in boundary if x[0] == "half"]
    assert len(leftovers) == modulus
    assert all(x[1] == "white" for x in leftovers)

    answer = []
    for label in range(1, modulus + 1):
        a = first_black[label]
        b = second_black.get(label, d)
        assert a != b
        answer.append(edge(a - 1, b - 1))
    return tuple(answer)


def conjugate_transposition(a: Edge, by: Edge) -> Edge:
    x, y = by

    def image(z: int) -> int:
        if z == x:
            return y
        if z == y:
            return x
        return z

    return edge(image(a[0]), image(a[1]))


def hurwitz_step(word: Word, action: Action) -> Word:
    position, sign = action
    assert sign in (-1, 1)
    assert 1 <= position < len(word)
    i = position - 1
    a, b = word[i], word[i + 1]
    if sign == 1:
        pair = (b, conjugate_transposition(a, b))
    else:
        pair = (conjugate_transposition(b, a), a)
    return word[:i] + pair + word[i + 2 :]


def replay(word: Word, actions: tuple[Action, ...]) -> Word:
    current = word
    for action in actions:
        current = hurwitz_step(current, action)
    return current


def word_product(word: Word, n: int) -> tuple[int, ...]:
    # Functional convention: (pq)(x)=p(q(x)); append each displayed factor.
    current = tuple(range(n))
    for a, b in word:
        factor = list(range(n))
        factor[a], factor[b] = factor[b], factor[a]
        current = tuple(current[factor[x]] for x in range(n))
    return current


def identity_word(word: Word, n: int) -> bool:
    return word_product(word, n) == tuple(range(n))


def sign_automaton(bits: tuple[bool, ...]) -> tuple[int, ...]:
    if not bits:
        return ()
    signs = [-1 if bits[0] else 1]
    for bit in bits[1:]:
        signs.append(-1 if bit else -signs[-1])
    return tuple(signs)


def route_normal_data(tree: Tree, v: int, d: int) -> dict:
    """Compute only the predeclared tree-side descriptor data."""
    parent = rooted_parent(tree, d)
    path = [v]
    while path[-1] != 1:
        nxt = parent[path[-1]]
        assert nxt is not None
        path.append(nxt)
    path_t = tuple(path)
    internal = path_t[1:-1]
    late = any(x > v for x in internal)
    ascent = any(x < y for x, y in zip(internal, internal[1:]))
    L = d - v - 1
    bits = tuple(parent[v + t + 1] == v for t in range(L))
    epsilon = sign_automaton(bits)
    z2 = ("closed",) if late or ascent else ("open", v, epsilon)
    return {
        "path": path_t,
        "late": late,
        "ascent": ascent,
        "bits": bits,
        "epsilon": epsilon,
        "z2": z2,
    }


def carrier(d: int) -> tuple[Action, ...]:
    return (
        (2 * d - 4, -1),
        (2 * d - 3, 1),
        (2 * d - 2, -1),
        (2 * d - 3, -1),
        (2 * d - 4, -1),
    )


def route_normal_word(d: int, v: int, late: bool, ascent: bool,
                      epsilon: tuple[int, ...]) -> tuple[Action, ...]:
    if late or ascent:
        return ()
    q: list[Action] = []
    for t, sign in enumerate(epsilon):
        q.extend(((2 * (v + t) - 2, sign), (2 * (v + t) - 1, sign)))
    q_inv = [(position, -sign) for position, sign in reversed(q)]
    return tuple(q) + carrier(d) + tuple(q_inv)


def fixed_word(edit: int) -> tuple[Action, ...]:
    if edit in (2, 4, 6, 8):
        return ()
    if edit == 10:
        return ((9, -1), (9, -1))
    if edit == 11:
        return ((12, -1),)
    raise AssertionError(edit)


def endpoint_pair(tree: Tree, edit: int) -> tuple[Word, Word]:
    old_order = swap_values(canonical_pi(7), edit)
    naive = dps_factorization(tree, old_order, 7) + (edge(0, 7), edge(0, 7))
    extended = tuple(sorted(tree + ((1, 8),)))
    new_order = swap_values(canonical_pi(8), edit)
    actual = dps_factorization(extended, new_order, 8)
    return naive, actual


def class_certificate(rows: list[dict]) -> list[dict]:
    groups: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        groups[json.dumps(jsonable(row["z2"]), separators=(",", ":"))].append(row)
    answer = []
    for key in sorted(groups):
        group = groups[key]
        routes = {tuple(row["route"]) for row in group}
        outcomes = {row["pass"] for row in group}
        answer.append(
            {
                "z2": json.loads(key),
                "rows": len(group),
                "passes": sum(row["pass"] for row in group),
                "failures": sum(not row["pass"] for row in group),
                "route_count": len(routes),
                "outcome_count": len(outcomes),
                "route": jsonable(next(iter(routes))),
            }
        )
    return answer


def m236_compatibility_certificates(
    trees: tuple[Tree, ...], primary: list[dict], secondary: list[dict]
) -> dict:
    """Post-checkpoint serializer for M236's published normalized schema.

    The independent table, census, and native hashes were fixed in
    ``checkpoint.md`` before this compatibility layer was transcribed.  This
    function reads no M236 file and changes no mathematical object.
    """
    tree_order = tuple(sorted(trees))
    primary_map = {(row["tree"], row["edit"]): row for row in primary}
    secondary_map = {(row["tree"], row["edit"]): row for row in secondary}

    primary_rows = []
    secondary_rows = []
    for tree_id, tree in enumerate(tree_order):
        for edit in (1, 3, 5, 7, 9):
            row = primary_map[(tree, edit)]
            replayed = replay(row["naive"], row["route"])
            primary_rows.append(
                {
                    "row_index": len(primary_rows),
                    "tree_id": tree_id,
                    "tree": jsonable(tree),
                    "edit": edit,
                    "vertex": row["v"],
                    "path": jsonable(row["path"]),
                    "late": row["late"],
                    "ascent": row["ascent"],
                    "closed": row["late"] or row["ascent"],
                    "bits": jsonable(row["bits"]),
                    "epsilon": jsonable(row["epsilon"]),
                    "z2": jsonable(row["z2"]),
                    "route": jsonable(row["route"]),
                    "route_length": len(row["route"]),
                    "naive": jsonable(row["naive"]),
                    "actual": jsonable(row["actual"]),
                    "replay": jsonable(replayed),
                    "pass": replayed == row["actual"],
                    "naive_equals_actual": row["naive"] == row["actual"],
                    "mismatch_positions": [
                        position
                        for position, (left, right) in enumerate(
                            zip(replayed, row["actual"]), start=1
                        )
                        if left != right
                    ],
                }
            )
        for edit in (2, 4, 6, 8, 10, 11):
            row = secondary_map[(tree, edit)]
            replayed = replay(row["naive"], row["route"])
            secondary_rows.append(
                {
                    "row_index": len(secondary_rows),
                    "tree_id": tree_id,
                    "tree": jsonable(tree),
                    "edit": edit,
                    "family": (
                        "internal_even"
                        if edit <= 8
                        else "cross_boundary"
                        if edit == 10
                        else "old_high_pair"
                    ),
                    "route": jsonable(row["route"]),
                    "route_length": len(row["route"]),
                    "naive": jsonable(row["naive"]),
                    "actual": jsonable(row["actual"]),
                    "replay": jsonable(replayed),
                    "pass": replayed == row["actual"],
                    "naive_equals_actual": row["naive"] == row["actual"],
                    "mismatch_positions": [
                        position
                        for position, (left, right) in enumerate(
                            zip(replayed, row["actual"]), start=1
                        )
                        if left != right
                    ],
                }
            )

    groups: dict[str, list[dict]] = defaultdict(list)
    for row in primary_rows:
        groups[json.dumps(row["z2"], sort_keys=True, separators=(",", ":"))].append(row)
    classes = []
    for key in sorted(groups):
        group = groups[key]
        routes = sorted(
            {
                json.dumps(row["route"], sort_keys=True, separators=(",", ":"))
                for row in group
            }
        )
        classes.append(
            {
                "z2": json.loads(key),
                "size": len(group),
                "passes": sum(row["pass"] for row in group),
                "failures": sum(not row["pass"] for row in group),
                "route_count": len(routes),
                "route": json.loads(routes[0]) if len(routes) == 1 else None,
                "route_length": group[0]["route_length"] if len(routes) == 1 else None,
            }
        )

    primary_routes = sorted(
        {
            json.dumps(row["route"], sort_keys=True, separators=(",", ":"))
            for row in primary_rows
        }
    )
    secondary_routes = sorted(
        {
            json.dumps(row["route"], sort_keys=True, separators=(",", ":"))
            for row in secondary_rows
        }
    )
    full_routes = sorted(set(primary_routes) | set(secondary_routes))

    observed = {
        "tree_universe": canonical_hash([jsonable(tree) for tree in tree_order]),
        "primary_rows": canonical_hash(primary_rows),
        "z2_classes": canonical_hash(classes),
        "primary_words": canonical_hash([json.loads(route) for route in primary_routes]),
        "secondary_rows": canonical_hash(secondary_rows),
        "full_rows": canonical_hash(
            {"primary": primary_rows, "secondary": secondary_rows}
        ),
        "full_words": canonical_hash([json.loads(route) for route in full_routes]),
    }
    published = {
        "tree_universe": "4bedab1e9da7ba6dc4c657b1da435da53dc0e3d5114d5678209579774a476ed9",
        "primary_rows": "f1256098c2b86bf85504979ddb04a9f2c5afb0008c36233051a7e0a0859fdf53",
        "z2_classes": "30adb20d0458fae1829670233e6c0cdfdf599e76b5f39bf4a8f8b71c987bfaa1",
        "primary_words": "3bca6bd6407aa38e3cdc82c16f527f91fa5bda9ce6c75008bcdf89c3bb810608",
        "secondary_rows": "f7efdc9be6321543b784c71bffd18af2c2d7ec79adbcf7150867c5cbed5d1868",
        "full_rows": "114a70ed4fb006b25658a0cf7d49675b20b223b2504b8cca9ec462c31c05acf4",
        "full_words": "d6fdf8d908fee98bc866ab6201f585f187f3fee8771512ba2e2aa9cf208a821c",
    }
    assert observed == published
    return {
        "observed": observed,
        "published": published,
        "all_match": True,
        "independent_table_fixed_before_serializer_inspection": True,
        "runtime_m236_reads": False,
    }


def main() -> None:
    # Two complete constructions certify the finite tree universe.
    direct = direct_root_leaf_trees()
    attached = attached_root_leaf_trees()
    assert set(direct) == set(attached)

    # Source-extension identity is checked on every tree before edits.
    extension_identity_checks = 0
    for tree in direct:
        old = dps_factorization(tree, canonical_pi(7), 7)
        extended = tuple(sorted(tree + ((1, 8),)))
        new = dps_factorization(extended, canonical_pi(8), 8)
        assert new == old + (edge(0, 7), edge(0, 7))
        assert identity_word(old, 7)
        assert identity_word(new, 8)
        extension_identity_checks += 1

    # Formal five-move carrier: every ordered assignment of four distinct
    # symbols from [0,7].
    carrier_checks = 0
    local_carrier = ((1, -1), (2, 1), (3, -1), (2, -1), (1, -1))
    for x, y, z, n in permutations(range(8), 4):
        source = (edge(x, y), edge(z, x), edge(z, y), edge(z, n))
        target = (edge(x, n), edge(z, y), edge(z, y), edge(z, x))
        assert replay(source, local_carrier) == target
        carrier_checks += 1
    assert carrier_checks == 1680

    # Initial-direct-run specialization for L=0,...,6 and r=0,...,L.
    sign_checks = 0
    for L in range(7):
        for r in range(L + 1):
            bits = (True,) * r + (False,) * (L - r)
            expected = tuple(
                -1 if t < r else (1 if (t - r) % 2 == 0 else -1)
                for t in range(L)
            )
            assert sign_automaton(bits) == expected
            sign_checks += 1
    assert sign_checks == 28

    primary: list[dict] = []
    secondary: list[dict] = []
    first_failure = None
    first_secondary_failure = None

    for tree_index, tree in enumerate(direct):
        for edit in (1, 3, 5, 7, 9):
            v = (edit + 3) // 2

            # Mandatory anti-circularity order: tree descriptor and formula
            # word are complete before either endpoint is constructed.
            desc = route_normal_data(tree, v, 7)
            route = route_normal_word(
                7, v, desc["late"], desc["ascent"], desc["epsilon"]
            )
            frozen_descriptor = json.dumps(jsonable(desc), sort_keys=True)
            frozen_route = tuple(route)

            naive, actual = endpoint_pair(tree, edit)
            assert frozen_descriptor == json.dumps(jsonable(desc), sort_keys=True)
            assert frozen_route == route
            assert identity_word(naive, 8)
            assert identity_word(actual, 8)
            replayed = replay(naive, route)
            passed = replayed == actual
            row = {
                "tree_index": tree_index,
                "tree": tree,
                "edit": edit,
                "v": v,
                "path": desc["path"],
                "late": desc["late"],
                "ascent": desc["ascent"],
                "bits": desc["bits"],
                "epsilon": desc["epsilon"],
                "z2": desc["z2"],
                "route": route,
                "naive": naive,
                "actual": actual,
                "pass": passed,
                "naive_equals_actual": naive == actual,
                "first_mismatch": next(
                    (
                        j
                        for j, (a, b) in enumerate(zip(replayed, actual), start=1)
                        if a != b
                    ),
                    None,
                ),
            }
            primary.append(row)
            if not passed and first_failure is None:
                first_failure = jsonable(row)

        for edit in (2, 4, 6, 8, 10, 11):
            # The fixed family word is likewise selected before endpoints.
            route = fixed_word(edit)
            frozen_route = tuple(route)
            naive, actual = endpoint_pair(tree, edit)
            assert frozen_route == route
            assert identity_word(naive, 8)
            assert identity_word(actual, 8)
            replayed = replay(naive, route)
            passed = replayed == actual
            row = {
                "tree_index": tree_index,
                "tree": tree,
                "edit": edit,
                "route": route,
                "naive": naive,
                "actual": actual,
                "pass": passed,
                "naive_equals_actual": naive == actual,
                "first_mismatch": next(
                    (
                        j
                        for j, (a, b) in enumerate(zip(replayed, actual), start=1)
                        if a != b
                    ),
                    None,
                ),
            }
            secondary.append(row)
            if not passed and first_secondary_failure is None:
                first_secondary_failure = jsonable(row)

    assert len(primary) == 6480
    assert len(secondary) == 7776
    assert all(row["pass"] for row in primary)
    assert all(row["pass"] for row in secondary)

    edits = (1, 3, 5, 7, 9)
    z2_by_edit = {
        edit: {row["z2"] for row in primary if row["edit"] == edit}
        for edit in edits
    }
    z2_global = set().union(*z2_by_edit.values())
    z2_to_routes: dict[tuple, set[tuple[Action, ...]]] = defaultdict(set)
    z2_to_outcomes: dict[tuple, set[bool]] = defaultdict(set)
    for row in primary:
        z2_to_routes[row["z2"]].add(row["route"])
        z2_to_outcomes[row["z2"]].add(row["pass"])
    assert all(len(x) == 1 for x in z2_to_routes.values())
    assert all(x == {True} for x in z2_to_outcomes.values())

    primary_words = {row["route"] for row in primary}
    full_words = primary_words | {row["route"] for row in secondary}
    closed_by_edit = [
        sum(row["edit"] == edit and row["z2"] == ("closed",) for row in primary)
        for edit in edits
    ]
    open_by_edit = [1296 - x for x in closed_by_edit]
    primary_length_hist = Counter(len(row["route"]) for row in primary)
    full_length_hist = Counter(len(row["route"]) for row in primary + secondary)

    # Native, independently selected certificates.  These are intentionally
    # normalized from mathematical objects rather than a predecessor schema.
    tree_certificate = jsonable(list(direct))
    primary_certificate = [
        {
            "tree": jsonable(row["tree"]),
            "edit": row["edit"],
            "z2": jsonable(row["z2"]),
            "route": jsonable(row["route"]),
            "naive": jsonable(row["naive"]),
            "actual": jsonable(row["actual"]),
            "pass": row["pass"],
        }
        for row in primary
    ]
    secondary_certificate = [
        {
            "tree": jsonable(row["tree"]),
            "edit": row["edit"],
            "route": jsonable(row["route"]),
            "naive": jsonable(row["naive"]),
            "actual": jsonable(row["actual"]),
            "pass": row["pass"],
        }
        for row in secondary
    ]
    z2_certificate = class_certificate(primary)
    primary_word_certificate = sorted(jsonable(word) for word in primary_words)
    full_word_certificate = sorted(jsonable(word) for word in full_words)

    native_digests = {
        "tree_universe": canonical_hash(tree_certificate),
        "primary_rows": canonical_hash(primary_certificate),
        "z2_classes": canonical_hash(z2_certificate),
        "primary_words": canonical_hash(primary_word_certificate),
        "secondary_rows": canonical_hash(secondary_certificate),
        "full_rows": canonical_hash(primary_certificate + secondary_certificate),
        "full_words": canonical_hash(full_word_certificate),
    }

    m236_compatibility = m236_compatibility_certificates(
        direct, primary, secondary
    )

    result = {
        "mission": "M237",
        "target": "fresh immutable referee of frozen finite M236",
        "scope": "complete d=7 -> 8 one-leaf template only",
        "environment": {
            "python": platform.python_version(),
            "dependencies": {},
            "seed": None,
            "command": "python3 -B independent_referee.py",
        },
        "independence": {
            "reads_input_files": False,
            "imports_m236_code_or_data": False,
            "route_search": False,
            "endpoint_lookup": False,
            "descriptor_assigned_before_endpoints": True,
            "formula_assigned_before_endpoints": True,
        },
        "tree_count": len(direct),
        "tree_constructions_equal": True,
        "source_extension_identity_checks": extension_identity_checks,
        "carrier_checks": carrier_checks,
        "initial_run_sign_checks": sign_checks,
        "primary": {
            "edits": list(edits),
            "rows": len(primary),
            "passes": sum(row["pass"] for row in primary),
            "failures": sum(not row["pass"] for row in primary),
            "z2_classes_by_edit": [len(z2_by_edit[x]) for x in edits],
            "z2_classes_global": len(z2_global),
            "closed_rows_by_edit": closed_by_edit,
            "open_rows_by_edit": open_by_edit,
            "closed_rows": sum(closed_by_edit),
            "open_rows": sum(open_by_edit),
            "distinct_words": len(primary_words),
            "max_route_length": max(map(len, primary_words)),
            "length_histogram": {
                str(k): primary_length_hist[k] for k in sorted(primary_length_hist)
            },
            "first_failure": first_failure,
            "first_same_z2_behavior_collision": None,
        },
        "secondary": {
            "edits": [2, 4, 6, 8, 10, 11],
            "rows": len(secondary),
            "passes": sum(row["pass"] for row in secondary),
            "failures": sum(not row["pass"] for row in secondary),
            "first_failure": first_secondary_failure,
        },
        "full": {
            "rows": len(primary) + len(secondary),
            "passes": sum(row["pass"] for row in primary + secondary),
            "failures": sum(not row["pass"] for row in primary + secondary),
            "distinct_words": len(full_words),
            "length_histogram": {
                str(k): full_length_hist[k] for k in sorted(full_length_hist)
            },
        },
        "native_digests": native_digests,
        "m236_compatibility_digests": m236_compatibility,
    }

    # The exact finite substantive values are predeclared by the assignment.
    assert result["primary"]["z2_classes_by_edit"] == [9, 6, 4, 3, 2]
    assert result["primary"]["z2_classes_global"] == 20
    assert result["primary"]["closed_rows_by_edit"] == [864, 756, 624, 463, 267]
    assert result["primary"]["open_rows_by_edit"] == [432, 540, 672, 833, 1029]
    assert result["primary"]["closed_rows"] == 2974
    assert result["primary"]["open_rows"] == 3506
    assert result["primary"]["distinct_words"] == 20
    assert result["primary"]["max_route_length"] == 21
    assert result["full"]["distinct_words"] == 22

    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
