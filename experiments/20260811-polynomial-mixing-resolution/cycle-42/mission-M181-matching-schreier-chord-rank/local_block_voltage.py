#!/usr/bin/env python3
"""Minimal symbolic audit for the M181 anchored voltage block.

This is not a quotient enumeration.  It checks one fixed B_6 relation, then
embeds shifted copies in explicit connected minimal words for small boundary
values of d and s.  The all-d result in the proof is symbolic.
"""

from __future__ import annotations

import json
import platform
from pathlib import Path


Edge = tuple[int, int]
Word = tuple[Edge, ...]
Perm = tuple[int, ...]
TupleWord = tuple[Word, ...]


def compose(p: Perm, q: Perm) -> Perm:
    """Return p q with (p q)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def sign_bit(p: Perm) -> int:
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) & 1


def transposition(d: int, a: int, b: int) -> Perm:
    p = list(range(d))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def relabel_edge(edge: Edge, p: Perm) -> Edge:
    return tuple(sorted((p[edge[0]], p[edge[1]])))


def relabel_word(word: Word, p: Perm) -> Word:
    return tuple(relabel_edge(edge, p) for edge in word)


def conjugate_edge(edge: Edge, by: Edge, d: int) -> Edge:
    return relabel_edge(edge, transposition(d, *by))


def hurwitz(word: Word, symbol: int, d: int) -> Word:
    """Apply one signed generator; abs(symbol) is one-based."""
    slot = abs(symbol) - 1
    direction = 1 if symbol > 0 else -1
    a, b = word[slot], word[slot + 1]
    out = list(word)
    if direction == 1:
        out[slot], out[slot + 1] = b, conjugate_edge(a, b, d)
    else:
        out[slot], out[slot + 1] = conjugate_edge(b, a, d), a
    return tuple(out)


def apply_braid(word: Word, chronological: tuple[int, ...], d: int) -> Word:
    out = word
    for symbol in chronological:
        out = hurwitz(out, symbol, d)
    return out


def evaluate(word: Word, d: int) -> Perm:
    out = tuple(range(d))
    for a, b in word:
        out = compose(out, transposition(d, a, b))
    return out


def connected(word: Word, d: int) -> bool:
    adj = [set() for _ in range(d)]
    for a, b in word:
        adj[a].add(b)
        adj[b].add(a)
    seen = {0}
    todo = [0]
    while todo:
        x = todo.pop()
        for y in adj[x] - seen:
            seen.add(y)
            todo.append(y)
    return len(seen) == d


def paired_factor_product(pair: TupleWord, indices: tuple[int, ...], d: int) -> tuple[Perm, ...]:
    out = [tuple(range(d)) for _ in pair]
    for index in indices:
        for coordinate, word in enumerate(pair):
            out[coordinate] = compose(out[coordinate], transposition(d, *word[index - 1]))
    return tuple(out)


def last_factor_loop(m: int) -> tuple[int, ...]:
    return tuple(range(m - 1, 0, -1)) + tuple(range(1, m))


def elementary_factor_conjugation(index: int, m: int) -> tuple[int, ...]:
    """Literal M154 word mapping X to x_index^{-1} X x_index."""
    transport = tuple(-j for j in range(index, m))
    undo = tuple(range(m - 1, index - 1, -1))
    return transport + last_factor_loop(m) + undo


def core_words() -> TupleWord:
    u: Word = ((0, 1), (0, 1), (0, 2), (0, 2), (0, 3), (0, 3))
    v: Word = ((0, 1), (0, 1), (0, 2), (0, 2), (1, 3), (1, 3))
    return u, v


def anchored_block_relation() -> dict:
    d = 4
    pair = core_words()
    base = (4, 3, 5, 4)
    rho = (
        (0, 1, 3, 2),
        (1, 0, 3, 2),
    )
    after_base = tuple(apply_braid(word, base, d) for word in pair)
    assert after_base == tuple(relabel_word(word, p) for word, p in zip(pair, rho))

    # A=(position 1), B=(position 3), C=(position 5).  In the aligned
    # factor group, (B C)^3=(id,(02)(13)); conjugating by A B A gives
    # p=(id,(01)(23)).
    p_expression = (1, 3, 1, 3, 5, 3, 5, 3, 5, 1, 3, 1)
    p = paired_factor_product(pair, p_expression, d)
    expected_p = (
        tuple(range(d)),
        compose(transposition(d, 0, 1), transposition(d, 2, 3)),
    )
    assert p == expected_p
    assert tuple(
        paired_factor_product(after_base, p_expression, d)[k] for k in range(2)
    ) == expected_p

    # Chronological elementary conjugations reverse the factor expression.
    correction = tuple(
        symbol
        for index in reversed(p_expression)
        for symbol in elementary_factor_conjugation(index, 6)
    )
    relation = base + correction
    endpoint = tuple(apply_braid(word, relation, d) for word in pair)
    delta = (
        transposition(d, 2, 3),
        tuple(range(d)),
    )
    expected_endpoint = tuple(relabel_word(word, p) for word, p in zip(pair, delta))
    assert endpoint == expected_endpoint

    # Directly test the universal elementary relation on this aligned pair.
    elementary_failures = []
    for index in (1, 3, 5):
        eword = elementary_factor_conjugation(index, 6)
        got = tuple(apply_braid(word, eword, d) for word in pair)
        factor_tuple = tuple(transposition(d, *word[index - 1]) for word in pair)
        want = tuple(
            relabel_word(word, inverse(factor))
            for word, factor in zip(pair, factor_tuple)
        )
        if got != want:
            elementary_failures.append(index)
    assert not elementary_failures

    return {
        "base_chronological": list(base),
        "base_transporters": [list(p) for p in rho],
        "p_factor_expression": list(p_expression),
        "p_images": [list(x) for x in p],
        "correction_length": len(correction),
        "relation_length": len(relation),
        "relation_chronological": list(relation),
        "final_transporters": [list(p) for p in delta],
        "final_signs": [sign_bit(p) for p in delta],
        "anchor_fixed": [p[0] == 0 for p in delta],
        "elementary_relation_failures": elementary_failures,
    }


def block(anchor: int, a: int, b: int, c: int, odd_pattern: bool) -> Word:
    del anchor  # The explicit construction always uses anchor 0.
    if odd_pattern:
        edges = ((0, a), (0, b), (0, c))
    else:
        edges = ((0, a), (0, b), (a, c))
    return tuple(edge for edge in edges for _ in range(2))


def constructed_word(d: int, r: int, pattern: tuple[int, ...]) -> Word:
    assert 3 * r <= d - 1 and len(pattern) == r
    out: list[Edge] = []
    for k, bit in enumerate(pattern):
        a, b, c = 3 * k + 1, 3 * k + 2, 3 * k + 3
        out.extend(block(0, a, b, c, bool(bit)))
    for vertex in range(3 * r + 1, d):
        out.extend(((0, vertex), (0, vertex)))
    word = tuple(out)
    assert len(word) == 2 * d - 2
    assert evaluate(word, d) == tuple(range(d))
    assert connected(word, d)
    return word


def shifted_relation(relation: tuple[int, ...], block_index: int) -> tuple[int, ...]:
    shift = 6 * block_index
    return tuple((1 if x > 0 else -1) * (abs(x) + shift) for x in relation)


def block_family_audit(relation: tuple[int, ...]) -> list[dict]:
    rows = []
    for d in range(5, 14):
        r = (d - 1) // 3
        patterns = [tuple(0 for _ in range(r))]
        patterns.extend(tuple(int(j == k) for j in range(r)) for k in range(r))
        words = [constructed_word(d, r, pattern) for pattern in patterns]
        gains = []
        transporter_rows = []
        for k in range(r):
            braid = shifted_relation(relation, k)
            this_gain = []
            this_transporters = []
            swap = transposition(d, 3 * k + 2, 3 * k + 3)
            identity = tuple(range(d))
            for pattern, word in zip(patterns, words):
                transporter = swap if pattern[k] else identity
                got = apply_braid(word, braid, d)
                assert got == relabel_word(word, transporter)
                this_gain.append(sign_bit(transporter))
                this_transporters.append(list(transporter))
            gains.append(this_gain)
            transporter_rows.append(this_transporters)
        expected = [
            [int(coordinate == k + 1) for coordinate in range(r + 1)]
            for k in range(r)
        ]
        assert gains == expected
        rows.append({
            "d": d,
            "blocks": r,
            "width": r + 1,
            "patterns": [list(x) for x in patterns],
            "voltage_basis_representatives": gains,
            "all_words_valid": True,
            "literal_shifted_relations_verified": r,
        })
    return rows


def main() -> None:
    core = anchored_block_relation()
    relation = tuple(core["relation_chronological"])
    rows = block_family_audit(relation)
    result = {
        "experiment": "M181 minimal anchored-block symbolic audit",
        "scope": "one explicit B6 relation and direct embeddings d=5..13; no quotient enumeration",
        "composition": "(p q)(x)=p(q(x)); braid lists applied chronologically left-to-right",
        "repository_base_commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
        "command": "python3 -B local_block_voltage.py",
        "parameters": {"d_min": 5, "d_max": 13},
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "core": core,
        "family_rows": rows,
    }
    Path("results.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
