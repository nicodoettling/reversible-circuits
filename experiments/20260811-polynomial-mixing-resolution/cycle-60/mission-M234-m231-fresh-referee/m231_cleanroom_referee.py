#!/usr/bin/env python3
"""Clean-room finite referee for M231.

No predecessor implementation or result file is imported or read.  This
script reconstructs the rooted DPS closure and the declared descriptor map
directly from the frozen mathematical specification.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import platform
import sys
from collections import Counter, defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "cleanroom_results.json"


def canonical_hash(obj) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def edge(a: int, b: int) -> tuple[int, int]:
    assert a != b
    return (a, b) if a < b else (b, a)


def conjugate_transposition(t: tuple[int, int], by: tuple[int, int]):
    def act(x: int) -> int:
        if x == by[0]:
            return by[1]
        if x == by[1]:
            return by[0]
        return x

    return edge(act(t[0]), act(t[1]))


def hurwitz_step(word, position: int, sign: int):
    """Apply chronological right Hurwitz R_position^(sign), 1-based."""
    assert sign in (-1, 1)
    j = position - 1
    assert 0 <= j < len(word) - 1
    out = list(word)
    a, b = out[j], out[j + 1]
    if sign == 1:
        out[j : j + 2] = (b, conjugate_transposition(a, b))
    else:
        out[j : j + 2] = (conjugate_transposition(b, a), a)
    return tuple(out)


def replay(word, actions):
    state = tuple(word)
    for position, sign in actions:
        state = hurwitz_step(state, position, sign)
    return state


def evaluate_identity(word, degree: int) -> bool:
    image = list(range(degree))
    for a, b in word:
        image[a], image[b] = image[b], image[a]
    return image == list(range(degree))


def prufer_decode(vertices, code):
    vertices = tuple(vertices)
    degree = {v: 1 for v in vertices}
    for x in code:
        degree[x] += 1
    edges = []
    for x in code:
        leaf = min(v for v in vertices if degree[v] == 1)
        edges.append(edge(leaf, x))
        degree[leaf] -= 1
        degree[x] -= 1
    leaves = [v for v in vertices if degree[v] == 1]
    assert len(leaves) == 2
    edges.append(edge(*leaves))
    return tuple(sorted(edges))


def base_trees():
    """The 125 trees on [6] with leaf root 6 adjacent to 1."""
    from_five = {
        tuple(sorted((*prufer_decode(range(1, 6), code), (1, 6))))
        for code in itertools.product(range(1, 6), repeat=3)
    }
    direct = {
        tree
        for code in itertools.product(range(1, 7), repeat=4)
        for tree in (prufer_decode(range(1, 7), code),)
        if sum(6 in e for e in tree) == 1 and (1, 6) in tree
    }
    assert from_five == direct
    assert len(from_five) == 125
    return tuple(sorted(from_five))


def rooted_parent(tree, root: int):
    adjacency = defaultdict(list)
    for a, b in tree:
        adjacency[a].append(b)
        adjacency[b].append(a)
    parent = {root: None}
    stack = [root]
    while stack:
        u = stack.pop()
        for v in adjacency[u]:
            if v not in parent:
                parent[v] = u
                stack.append(v)
    assert len(parent) == root
    return parent


def canonical_pi(d: int):
    return (2 * d - 3, 2 * d - 2, *range(1, 2 * d - 3))


def swap_values(pi, i: int):
    assert i >= 1
    return tuple(i + 1 if x == i else i if x == i + 1 else x for x in pi)


def dps_factorization(tree, pi, d: int):
    """Independent + mirror implementation of DPS hairy-tree closure."""
    assert len(pi) == 2 * d - 2
    parent = rooted_parent(tree, d)
    incidence = defaultdict(dict)
    black_for_label = {}
    for black in range(1, d):
        labels = pi[2 * black - 2 : 2 * black]
        for label, white in ((labels[0], black), (labels[1], parent[black])):
            bv = ("B", black)
            wv = ("W", white)
            incidence[bv][label] = wv
            incidence[wv][label] = bv
            black_for_label[label] = black

    # Trace the unique outer contour: white rotations increase, black
    # rotations decrease.  Tokens are half-edges H or physical/closure sides S.
    m = 2 * d - 2
    start = (("W", 1), 1)
    state = start
    seen = set()
    boundary = []
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        direction = 1 if vertex[0] == "W" else -1
        label = 1 + ((incoming - 1 + direction) % m)
        if label in incidence[vertex]:
            boundary.append(("S", "tree"))
            state = (incidence[vertex][label], label)
        else:
            boundary.append(("H", vertex[0], vertex[1], label))
            state = (vertex, label)
    assert state == start
    assert len(boundary) == (2 * d - 1) * m

    tokens = list(boundary)
    other_black = {}
    while True:
        half_positions = [j for j, tok in enumerate(tokens) if tok[0] == "H"]
        pair = None
        for k, left in enumerate(half_positions):
            right = half_positions[(k + 1) % len(half_positions)]
            if tokens[left][1] == "W" and tokens[right][1] == "B":
                pair = (left, right)
                break
        if pair is None:
            break
        left, right = pair
        tokens = tokens[left:] + tokens[:left]
        right = (right - left) % len(tokens)
        white, black = tokens[0], tokens[right]
        assert white[3] == black[3]
        distance = sum(tok[0] == "S" for tok in tokens[1:right])
        assert distance in (1, 3)
        if distance == 3:
            assert white[3] not in other_black
            other_black[white[3]] = black[2]
        tokens = [("S", "closure"), *tokens[right + 1 :]]

    remaining = [tok for tok in tokens if tok[0] == "H"]
    assert len(remaining) == m
    assert all(tok[1] == "W" for tok in remaining)
    assert sorted(tok[3] for tok in remaining) == list(range(1, m + 1))

    factors = []
    for label in range(1, m + 1):
        a = black_for_label[label]
        b = other_black.get(label, d)
        assert a != b
        factors.append(edge(a - 1, b - 1))
    word = tuple(factors)
    assert evaluate_identity(word, d)
    return word


def sign_automaton(bits):
    if not bits:
        return ()
    signs = [-1 if bits[0] else 1]
    for bit in bits[1:]:
        signs.append(-1 if bit else -signs[-1])
    return tuple(signs)


def carrier(d: int):
    return (
        (2 * d - 4, -1),
        (2 * d - 3, 1),
        (2 * d - 2, -1),
        (2 * d - 3, -1),
        (2 * d - 4, -1),
    )


def formula_word(d: int, v: int, late: bool, ascent: bool, epsilon):
    if late or ascent:
        return ()
    transport = []
    for t, sign in enumerate(epsilon):
        transport.extend(((2 * (v + t) - 2, sign), (2 * (v + t) - 1, sign)))
    inverse = tuple((position, -sign) for position, sign in reversed(transport))
    return tuple(transport) + carrier(d) + inverse


def descriptors(tree, v: int, d: int):
    parent = rooted_parent(tree, d)
    path = [v]
    while path[-1] != 1:
        path.append(parent[path[-1]])
    path = tuple(path)
    internal = path[1:-1]
    late = any(u > v for u in internal)
    ascent = any(a < b for a, b in zip(internal, internal[1:]))
    forward = v >= 4 and path == (v, *range(2, v), 1)
    L = d - v - 1
    child_bits = tuple(parent[v + t + 1] == v for t in range(L))
    epsilon = sign_automaton(child_bits)
    path_set = set(path)
    offpath = tuple(
        tuple(sorted(w for w in range(1, d) if parent[w] == u and w not in path_set))
        for u in path
    )
    d_a = (v, late, child_bits, forward)
    d_b = (d_a, path, offpath)
    z1 = (v, late, ascent, epsilon)
    z2 = ("closed",) if late or ascent else ("open", v, epsilon)
    actions = formula_word(d, v, late, ascent, epsilon)
    return {
        "path": path,
        "late": late,
        "ascent": ascent,
        "forward": forward,
        "child_bits": child_bits,
        "epsilon": epsilon,
        "offpath": offpath,
        "d_b": d_b,
        "z1": z1,
        "z2": z2,
        "actions": actions,
    }


def jsonable(x):
    if isinstance(x, tuple):
        return [jsonable(y) for y in x]
    if isinstance(x, list):
        return [jsonable(y) for y in x]
    if isinstance(x, dict):
        return {str(k): jsonable(v) for k, v in x.items()}
    return x


def symbolic_kernel_audit(z2_to_words):
    # Forward direction: the formula is visibly a function of Z2.  Converse is
    # audited syntactically: identity is empty; open v is encoded by length
    # 4L+5; at fixed v the first unequal epsilon produces the first unequal
    # signed generator pair.
    keys = sorted(z2_to_words, key=repr)
    for key in keys:
        assert len(z2_to_words[key]) == 1
        word = next(iter(z2_to_words[key]))
        if key == ("closed",):
            assert word == ()
            continue
        _, v, eps = key
        assert len(word) == 4 * len(eps) + 5
        for t, sign in enumerate(eps):
            assert word[2 * t] == (2 * (v + t) - 2, sign)
            assert word[2 * t + 1] == (2 * (v + t) - 1, sign)
    word_to_key = {}
    for key in keys:
        word = next(iter(z2_to_words[key]))
        assert word not in word_to_key
        word_to_key[word] = key
    return {
        "forward_functional": True,
        "identity_distinguished_by_length_zero": True,
        "open_v_distinguished_by_length_4L_plus_5": True,
        "epsilon_distinguished_by_first_signed_pair": True,
        "iff_on_occurring_values": True,
    }


def m231_normalized_certificates(rows):
    """Serialize independent objects using M231's published normalization.

    This is a compatibility layer only.  It was added after the independent
    table, counts, census, and native hashes had been fixed in checkpoint.md.
    It reads no predecessor file and changes no mathematical object.
    """
    row_map = {(row["tree"], row["edit"]): row for row in rows}
    direct_order = []
    for code in itertools.product(range(1, 7), repeat=4):
        tree = prufer_decode(range(1, 7), code)
        if sum(6 in item for item in tree) == 1 and (1, 6) in tree:
            direct_order.append(tree)
    assert len(direct_order) == 125
    assert set(direct_order) == set(base_trees())

    normalized = []
    for tree_id, tree in enumerate(direct_order):
        for edit in (1, 3, 5, 7):
            row = row_map[(tree, edit)]
            full = (
                "odd_B",
                row["v"],
                row["late"],
                row["child_bits"],
                row["forward"],
                row["path"],
                row["offpath"],
            )
            q1 = (
                "Q1",
                row["v"],
                row["late"],
                row["ascent"],
                row["epsilon"],
            )
            q2 = row["z2"]
            route = [[position, sign] for position, sign in row["actions"]]
            replayed = replay(row["naive"], row["actions"])
            normalized.append(
                {
                    "tree_id": tree_id,
                    "tree": [list(item) for item in tree],
                    "edit": edit,
                    "full_descriptor": jsonable(full),
                    "q1": jsonable(q1),
                    "q2": jsonable(q2),
                    "route": route,
                    "route_length": len(route),
                    "naive": jsonable(row["naive"]),
                    "actual": jsonable(row["actual"]),
                    "replay": jsonable(replayed),
                    "pass": replayed == row["actual"],
                    "naive_equals_actual": row["naive"] == row["actual"],
                    "mismatch_positions": [
                        position
                        for position, pair in enumerate(
                            zip(replayed, row["actual"]), start=1
                        )
                        if pair[0] != pair[1]
                    ],
                }
            )

    def class_digest(field):
        groups = defaultdict(list)
        for row in normalized:
            key = json.dumps(row[field], separators=(",", ":"))
            groups[key].append(row)
        summaries = []
        for key in sorted(groups):
            group = groups[key]
            routes = {
                json.dumps(row["route"], separators=(",", ":")) for row in group
            }
            summaries.append(
                {
                    "quotient": json.loads(key),
                    "size": len(group),
                    "route_count": len(routes),
                    "passes": sum(row["pass"] for row in group),
                    "failures": sum(not row["pass"] for row in group),
                    "route": json.loads(next(iter(routes))) if len(routes) == 1 else None,
                }
            )
        return canonical_hash(summaries)

    observed = {
        "rows": canonical_hash(normalized),
        "z1": class_digest("q1"),
        "z2": class_digest("q2"),
    }
    published = {
        "rows": "43f9171c42c7b99be6de5b154a34cfc1cee0cee67c1db24743900df2f5d51ad3",
        "z1": "50e4027978e590b6794c608a7d181d6c7bb9171d4f711baf624be6c56e31f2c2",
        "z2": "fdf2836fee0b96d78a0bcf8c29b06a1a99b5209bcd8ac8e0c069efab34c8c512",
    }
    assert observed == published
    return {
        "observed": observed,
        "published": published,
        "all_match": True,
        "independent_table_fixed_before_normalizer_inspection": True,
    }


def main():
    # Formal carrier identity: 7P4 ordered distinct symbol assignments.
    carrier_checks = 0
    B = ((1, -1), (2, 1), (3, -1), (2, -1), (1, -1))
    for x, y, z, n in itertools.permutations(range(7), 4):
        source = (edge(x, y), edge(z, x), edge(z, y), edge(z, n))
        target = (edge(x, n), edge(z, y), edge(z, y), edge(z, x))
        assert replay(source, B) == target
        carrier_checks += 1
    assert carrier_checks == 840

    # Initial-run specialization check, L=0,...,5 and r=0,...,L.
    sign_checks = 0
    for L in range(6):
        for r in range(L + 1):
            bits = (True,) * r + (False,) * (L - r)
            expected = tuple(
                -1 if t < r else (1 if (t - r) % 2 == 0 else -1)
                for t in range(L)
            )
            assert sign_automaton(bits) == expected
            sign_checks += 1
    assert sign_checks == 21

    trees = base_trees()
    rows = []
    d_b_by_edit = defaultdict(set)
    z1_by_edit = defaultdict(set)
    z2_by_edit = defaultdict(set)
    z1_to_words = defaultdict(set)
    z2_to_words = defaultdict(set)
    z1_to_pass = defaultdict(set)
    z2_to_pass = defaultdict(set)
    odd_words = set()

    for tree in trees:
        actual_tree = tuple(sorted((*tree, (1, 7))))
        for edit in (1, 3, 5, 7):
            v = (edit + 3) // 2
            desc = descriptors(tree, v, 6)

            # Descriptor and formula word are complete before endpoints exist.
            d_b = desc["d_b"]
            z1 = desc["z1"]
            z2 = desc["z2"]
            actions = desc["actions"]

            naive = dps_factorization(tree, swap_values(canonical_pi(6), edit), 6)
            naive = naive + (edge(0, 6), edge(0, 6))
            actual = dps_factorization(
                actual_tree, swap_values(canonical_pi(7), edit), 7
            )
            passed = replay(naive, actions) == actual
            assert evaluate_identity(naive, 7)
            assert evaluate_identity(actual, 7)

            d_b_by_edit[edit].add(d_b)
            z1_by_edit[edit].add(z1)
            z2_by_edit[edit].add(z2)
            z1_to_words[z1].add(actions)
            z2_to_words[z2].add(actions)
            z1_to_pass[z1].add(passed)
            z2_to_pass[z2].add(passed)
            odd_words.add(actions)
            rows.append(
                {
                    "tree": tree,
                    "edit": edit,
                    "v": v,
                    **desc,
                    "naive": naive,
                    "actual": actual,
                    "passed": passed,
                }
            )

    assert len(rows) == 500
    assert all(row["passed"] for row in rows)
    assert [len(d_b_by_edit[i]) for i in (1, 3, 5, 7)] == [101] * 4
    assert [len(z1_by_edit[i]) for i in (1, 3, 5, 7)] == [12, 7, 6, 2]
    assert [len(z2_by_edit[i]) for i in (1, 3, 5, 7)] == [6, 4, 3, 2]
    assert len(set().union(*d_b_by_edit.values())) == 404
    assert len(set().union(*z1_by_edit.values())) == 27
    assert len(set().union(*z2_by_edit.values())) == 12
    assert all(len(words) == 1 for words in z1_to_words.values())
    assert all(len(words) == 1 for words in z2_to_words.values())
    assert all(flags == {True} for flags in z1_to_pass.values())
    assert all(flags == {True} for flags in z2_to_pass.values())
    assert len(odd_words) == 12

    kernel = symbolic_kernel_audit(z2_to_words)
    z2_sizes = Counter(row["z2"] for row in rows)
    closed_size = z2_sizes[("closed",)]
    assert closed_size == 193
    closed_by_edit = [
        sum(row["edit"] == edit and row["z2"] == ("closed",) for row in rows)
        for edit in (1, 3, 5, 7)
    ]
    assert closed_by_edit == [75, 60, 41, 17]
    open_census = {
        repr(key): value
        for key, value in sorted(z2_sizes.items(), key=lambda item: repr(item[0]))
        if key != ("closed",)
    }

    boundary_words = {
        ((7, -1), (7, -1)),
        ((10, -1),),
    }
    full_words = odd_words | boundary_words
    assert len(boundary_words) == 2
    assert len(full_words) == 14

    # Native clean-room certificates.  A later, quarantined serializer audit
    # may additionally compare these independent rows to M231's declared
    # normalization, but these tables never depend on predecessor data.
    row_certificate = [
        {
            "tree": row["tree"],
            "edit": row["edit"],
            "d_b": row["d_b"],
            "z1": row["z1"],
            "z2": row["z2"],
            "actions": row["actions"],
            "naive": row["naive"],
            "actual": row["actual"],
            "passed": row["passed"],
        }
        for row in rows
    ]
    z1_certificate = [
        (key, next(iter(z1_to_words[key])), len(z1_to_words[key]), len(z1_to_pass[key]))
        for key in sorted(z1_to_words, key=repr)
    ]
    z2_certificate = [
        (key, next(iter(z2_to_words[key])), z2_sizes[key])
        for key in sorted(z2_to_words, key=repr)
    ]

    result = {
        "mission": "M234",
        "target": "fresh immutable referee of frozen M231",
        "scope": "exact finite d=6->7 ordinary odd-edit formula compression only",
        "environment": {
            "python": platform.python_version(),
            "dependencies": {},
            "seed": None,
            "command": "python3 -B m231_cleanroom_referee.py",
        },
        "independence": {
            "predecessor_code_imported": False,
            "predecessor_data_read_by_checker": False,
            "route_search": False,
            "endpoint_built_after_descriptor_and_word": True,
        },
        "carrier_checks": carrier_checks,
        "initial_run_sign_checks": sign_checks,
        "tree_count": len(trees),
        "odd_edits": [1, 3, 5, 7],
        "row_count": len(rows),
        "passes": sum(row["passed"] for row in rows),
        "failures": sum(not row["passed"] for row in rows),
        "d_b_classes_by_edit": [len(d_b_by_edit[i]) for i in (1, 3, 5, 7)],
        "d_b_classes_global": len(set().union(*d_b_by_edit.values())),
        "z1_classes_by_edit": [len(z1_by_edit[i]) for i in (1, 3, 5, 7)],
        "z1_classes_global": len(set().union(*z1_by_edit.values())),
        "z2_classes_by_edit": [len(z2_by_edit[i]) for i in (1, 3, 5, 7)],
        "z2_classes_global": len(set().union(*z2_by_edit.values())),
        "closed_class_size": closed_size,
        "closed_rows_by_edit": closed_by_edit,
        "open_class_census": open_census,
        "odd_formula_words": len(odd_words),
        "odd_word_inventory": jsonable(sorted(odd_words, key=repr)),
        "boundary_nonidentity_words": len(boundary_words),
        "boundary_word_inventory": jsonable(sorted(boundary_words, key=repr)),
        "full_table_formula_words": len(full_words),
        "symbolic_z2_kernel": kernel,
        "native_digests": {
            "rows": canonical_hash(jsonable(row_certificate)),
            "z1": canonical_hash(jsonable(z1_certificate)),
            "z2": canonical_hash(jsonable(z2_certificate)),
        },
        "m231_normalization_audit": m231_normalized_certificates(rows),
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
