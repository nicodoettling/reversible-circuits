#!/usr/bin/env python3
"""Clean-room symbolic referee for frozen M181.

No M181 module or data file is imported.  This reconstructs the stated core
relation from its formulas and checks only d=5,7,10 boundary embeddings; it
does not enumerate any quotient Schreier component.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import platform
from pathlib import Path


Edge = tuple[int, int]
Word = tuple[Edge, ...]
Perm = tuple[int, ...]


def mul(left: Perm, right: Perm) -> Perm:
    """Composition left*right, so (left*right)(x)=left(right(x))."""
    return tuple(left[right[x]] for x in range(len(left)))


def inv(p: Perm) -> Perm:
    q = [0] * len(p)
    for x, y in enumerate(p):
        q[y] = x
    return tuple(q)


def identity(d: int) -> Perm:
    return tuple(range(d))


def swap(d: int, a: int, b: int) -> Perm:
    p = list(range(d))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def parity(p: Perm) -> int:
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2


def act_edge(p: Perm, edge: Edge) -> Edge:
    return tuple(sorted((p[edge[0]], p[edge[1]])))


def act_word(p: Perm, word: Word) -> Word:
    return tuple(act_edge(p, edge) for edge in word)


def hurwitz_step(word: Word, letter: int, d: int) -> Word:
    slot = abs(letter) - 1
    left, right = word[slot], word[slot + 1]
    out = list(word)
    if letter > 0:
        out[slot] = right
        out[slot + 1] = act_edge(swap(d, *right), left)
    else:
        out[slot] = act_edge(swap(d, *left), right)
        out[slot + 1] = left
    return tuple(out)


def braid(word: Word, letters: tuple[int, ...], d: int) -> Word:
    current = word
    for letter in letters:
        current = hurwitz_step(current, letter, d)
    return current


def product(word: Word, d: int) -> Perm:
    value = identity(d)
    for edge in word:
        value = mul(value, swap(d, *edge))
    return value


def support_connected(word: Word, d: int) -> bool:
    neighbors = [set() for _ in range(d)]
    for a, b in word:
        neighbors[a].add(b)
        neighbors[b].add(a)
    reached = {0}
    frontier = [0]
    while frontier:
        x = frontier.pop()
        for y in neighbors[x] - reached:
            reached.add(y)
            frontier.append(y)
    return reached == set(range(d))


def unique_transporter(source: Word, target: Word, d: int) -> Perm:
    hits = [p for p in itertools.permutations(range(d)) if act_word(p, source) == target]
    assert len(hits) == 1
    return hits[0]


def last_loop(m: int) -> tuple[int, ...]:
    return tuple(range(m - 1, 0, -1)) + tuple(range(1, m))


def elementary(index: int, m: int) -> tuple[int, ...]:
    move_to_end = tuple(-j for j in range(index, m))
    undo = tuple(range(m - 1, index - 1, -1))
    return move_to_end + last_loop(m) + undo


def factor_product(word: Word, positions: tuple[int, ...], d: int) -> Perm:
    value = identity(d)
    for position in positions:
        value = mul(value, swap(d, *word[position - 1]))
    return value


def core_audit() -> tuple[dict, tuple[int, ...]]:
    d = 4
    u = ((0, 1), (0, 1), (0, 2), (0, 2), (0, 3), (0, 3))
    v = ((0, 1), (0, 1), (0, 2), (0, 2), (1, 3), (1, 3))
    original = (u, v)
    beta = (4, 3, 5, 4)
    after_beta = tuple(braid(w, beta, d) for w in original)
    rho = tuple(unique_transporter(w, z, d) for w, z in zip(original, after_beta))
    assert rho == (swap(d, 2, 3), mul(swap(d, 0, 1), swap(d, 2, 3)))

    expression = (1, 3, 1, 3, 5, 3, 5, 3, 5, 1, 3, 1)
    p = tuple(factor_product(w, expression, d) for w in after_beta)
    assert p == (identity(d), mul(swap(d, 0, 1), swap(d, 2, 3)))

    # Verify E_j itself at every possible factor position, not only the three
    # positions appearing in the correction expression.
    elementary_checks = 0
    for word in after_beta:
        for index in range(1, 7):
            factor = swap(d, *word[index - 1])
            expected = act_word(inv(factor), word)
            assert braid(word, elementary(index, 6), d) == expected
            elementary_checks += 1

    # Reverse expression order.  Track the original-factor product q and
    # verify after every elementary word that the state equals q^{-1}Xq.
    states = list(after_beta)
    accumulated = [identity(d), identity(d)]
    prefix_checks = 0
    correction: list[int] = []
    for index in reversed(expression):
        eword = elementary(index, 6)
        correction.extend(eword)
        for coordinate in range(2):
            accumulated[coordinate] = mul(
                swap(d, *after_beta[coordinate][index - 1]), accumulated[coordinate]
            )
            states[coordinate] = braid(states[coordinate], eword, d)
            assert states[coordinate] == act_word(inv(accumulated[coordinate]), after_beta[coordinate])
            prefix_checks += 1
    assert tuple(accumulated) == p

    relation = beta + tuple(correction)
    final = tuple(braid(w, relation, d) for w in original)
    delta = tuple(unique_transporter(w, z, d) for w, z in zip(original, final))
    assert delta == (swap(d, 2, 3), identity(d))
    assert all(x[0] == 0 for x in delta)

    relation_digest = hashlib.sha256(
        json.dumps(list(relation), separators=(",", ":")).encode()
    ).hexdigest()
    return {
        "base_transporters": [list(x) for x in rho],
        "base_signs": [parity(x) for x in rho],
        "expression_products_after_base": [list(x) for x in p],
        "elementary_checks": elementary_checks,
        "reverse_prefix_checks": prefix_checks,
        "correction_length": len(correction),
        "relation_length": len(relation),
        "relation_json_sha256": relation_digest,
        "final_transporters": [list(x) for x in delta],
        "final_signs": [parity(x) for x in delta],
        "anchor_fixed": [x[0] == 0 for x in delta],
    }, relation


def local_block(a: int, b: int, c: int, bit: int) -> Word:
    distinct = ((0, a), (0, b), (0, c)) if bit else ((0, a), (0, b), (a, c))
    return tuple(edge for edge in distinct for _ in range(2))


def family_word(d: int, pattern: tuple[int, ...]) -> Word:
    r = (d - 1) // 3
    assert len(pattern) == r
    factors: list[Edge] = []
    for k, bit in enumerate(pattern):
        a, b, c = 3 * k + 1, 3 * k + 2, 3 * k + 3
        factors.extend(local_block(a, b, c, bit))
    for x in range(3 * r + 1, d):
        factors.extend(((0, x), (0, x)))
    return tuple(factors)


def shifted(letters: tuple[int, ...], block_index: int) -> tuple[int, ...]:
    shift = 6 * block_index
    return tuple((1 if x > 0 else -1) * (abs(x) + shift) for x in letters)


def globally_conjugate(left: Word, right: Word, d: int) -> bool:
    return any(act_word(p, left) == right for p in itertools.permutations(range(d)))


def conjugate(p: Perm, q: Perm) -> Perm:
    return mul(mul(p, q), inv(p))


def cycle_perm(d: int, shift: int) -> Perm:
    return tuple((x + shift) % d for x in range(d))


def embedding_audit(relation: tuple[int, ...]) -> list[dict]:
    rows = []
    for d in (5, 7, 10):
        r = (d - 1) // 3
        patterns = [tuple(0 for _ in range(r))]
        patterns += [tuple(int(j == k) for j in range(r)) for k in range(r)]
        words = [family_word(d, pattern) for pattern in patterns]
        assert all(len(w) == 2 * d - 2 for w in words)
        assert all(product(w, d) == identity(d) for w in words)
        assert all(support_connected(w, d) for w in words)

        gains: list[list[int]] = []
        endpoint_checks = 0
        filler_fixed_checks = 0
        for k in range(r):
            h = shifted(relation, k)
            swap_k = swap(d, 3 * k + 2, 3 * k + 3)
            gain = []
            for pattern, word in zip(patterns, words):
                transporter = swap_k if pattern[k] else identity(d)
                assert braid(word, h, d) == act_word(transporter, word)
                gain.append(parity(transporter))
                endpoint_checks += 1
                outside = word[: 6 * k] + word[6 * k + 6 :]
                assert act_word(transporter, outside) == outside
                filler_fixed_checks += 1
            gains.append(gain)
        expected = [[int(c == k + 1) for c in range(r + 1)] for k in range(r)]
        assert gains == expected

        # Independent coordinatewise G-equivariance check with relabelers
        # that generally move the anchor and need not lie in H.
        equivariance_checks = 0
        alphas = [cycle_perm(d, c + 1) for c in range(len(words))]
        for k in range(r):
            h = shifted(relation, k)
            raw_swap = swap(d, 3 * k + 2, 3 * k + 3)
            for c, (pattern, word, alpha) in enumerate(zip(patterns, words, alphas)):
                physical = act_word(alpha, word)
                raw = raw_swap if pattern[k] else identity(d)
                transported = conjugate(alpha, raw)
                assert braid(physical, h, d) == act_word(transported, physical)
                assert parity(transported) == expected[k][c]
                equivariance_checks += 1

        # Exhaustive orbit separation is kept only at the two small boundary
        # ranks; the proof for all d is structural, not computational.
        orbit_pairs_checked = 0
        if d in (5, 7):
            for i in range(len(words)):
                for j in range(i + 1, len(words)):
                    assert not globally_conjugate(words[i], words[j], d)
                    orbit_pairs_checked += 1

        rows.append({
            "d": d,
            "blocks": r,
            "width": r + 1,
            "filler_pairs": d - 1 - 3 * r,
            "all_lengths": sorted({len(w) for w in words}),
            "identity_and_connected": True,
            "endpoint_checks": endpoint_checks,
            "outside_block_fixed_checks": filler_fixed_checks,
            "coordinatewise_G_equivariance_checks": equivariance_checks,
            "voltage_representatives": gains,
            "exhaustive_nonconjugate_pairs_checked": orbit_pairs_checked,
        })
    return rows


def binary_rank(rows: list[int]) -> int:
    basis: dict[int, int] = {}
    for value in rows:
        x = value
        while x:
            pivot = x.bit_length() - 1
            if pivot in basis:
                x ^= basis[pivot]
            else:
                basis[pivot] = x
                break
    return len(basis)


def quotient_normal_form(bits: int, s: int) -> int:
    return bits ^ ((1 << s) - 1) if bits & 1 else bits


def voltage_rank_audit() -> list[dict]:
    rows = []
    for s in range(2, 7):
        singletons = [quotient_normal_form(1 << k, s) for k in range(1, s)]
        path_edges = [quotient_normal_form((1 << k) | (1 << (k + 1)), s) for k in range(s - 1)]
        single_rank = binary_rank(singletons)
        edge_rank = binary_rank(path_edges)
        assert single_rank == s - 1
        assert edge_rank == (s - 1 if s % 2 else s - 2)
        rows.append({
            "s": s,
            "W_dimension": s - 1,
            "single_coordinate_class_rank": single_rank,
            "connected_path_edge_class_rank": edge_rank,
            "edge_rank_defect": (s - 1) - edge_rank,
        })
    return rows


def main() -> None:
    core, relation = core_audit()
    result = {
        "experiment": "M183 clean-room fresh referee of frozen M181",
        "scope": "core B6 replay; d=5,7,10 embeddings; no M181 import; no quotient enumeration",
        "repository_base_commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
        "command": "python3 -B independent_referee.py",
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "core": core,
        "embedding_rows": embedding_audit(relation),
        "voltage_quotient_rows": voltage_rank_audit(),
    }
    Path("independent_results.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
