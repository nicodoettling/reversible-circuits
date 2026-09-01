#!/usr/bin/env python3
"""Compact clean-room convention guard for M288.

This file imports no M284 or predecessor implementation. It checks only the
finite algebraic schemas used in the fresh proof audit; it is not an all-rank
proof and performs no state-space or route search.
"""

from __future__ import annotations

import hashlib
import json
import platform


def ident(n: int) -> tuple[int, ...]:
    return tuple(range(n))


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return p*q with (p*q)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def transposition(n: int, a: int, b: int) -> tuple[int, ...]:
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def conjugate(b: tuple[int, ...], a: tuple[int, ...]) -> tuple[int, ...]:
    return compose(b, compose(a, b))


def evaluate(word: list[tuple[int, ...]]) -> tuple[int, ...]:
    out = ident(len(word[0]))
    for factor in word:
        out = compose(out, factor)
    return out


def hurwitz(word: list[tuple[int, ...]], j: int, sign: int) -> list[tuple[int, ...]]:
    """Apply one chronological signed right-Hurwitz move, with j one-based."""
    out = list(word)
    a, b = out[j - 1], out[j]
    if sign == 1:
        out[j - 1 : j + 1] = [b, conjugate(b, a)]
    elif sign == -1:
        out[j - 1 : j + 1] = [conjugate(a, b), a]
    else:
        raise ValueError(sign)
    return out


def act(word: list[tuple[int, ...]], schedule: list[tuple[int, int]]) -> list[tuple[int, ...]]:
    out = list(word)
    for j, sign in schedule:
        out = hurwitz(out, j, sign)
    return out


def edge(p: tuple[int, ...]) -> tuple[int, int]:
    moved = [i for i, x in enumerate(p) if i != x]
    assert len(moved) == 2 and p[moved[0]] == moved[1] and p[moved[1]] == moved[0]
    return moved[0], moved[1]


def connected(word: list[tuple[int, ...]]) -> bool:
    n = len(word[0])
    graph = [set() for _ in range(n)]
    for factor in word:
        a, b = edge(factor)
        graph[a].add(b)
        graph[b].add(a)
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in graph[u] - seen:
            seen.add(v)
            stack.append(v)
    return len(seen) == n


def main() -> None:
    v_rows = []
    seam_rows = []
    partition_rows = []
    embedding_rows = []

    for D in range(6, 13):
        es = [transposition(D, 0, r) for r in range(1, D)]
        U = [x for e in es for x in (e, e)]
        V = hurwitz(U, 2, 1)
        assert len(V) == 2 * D - 2
        assert evaluate(U) == ident(D) and evaluate(V) == ident(D)
        assert connected(V)
        assert all(U[2 * r] == U[2 * r + 1] for r in range(D - 1))
        assert V[0] != V[1]
        assert set(es).issubset(set(V))
        v_rows.append({"D": D, "length": len(V), "support_edges": len(set(map(edge, V)))})

    for d in range(5, 13):
        n = d + 1
        g = transposition(n, 0, d - 1)
        k = transposition(n, 0, d)
        for parent in range(1, d - 1):
            h = transposition(n, d - 2, parent - 1)
            a = conjugate(g, h)
            b = conjugate(a, g)
            N = [a, b, a, g, k, k]
            A = [h, g, a, g, k, k]
            assert act(N, [(1, -1), (1, -1)]) == A
            assert evaluate(N) == evaluate(A)
            seam_rows.append({"d": d, "parent": parent, "regime": "meet" if parent == 1 else "disjoint"})
        N_last = [g, g, k, k]
        A_last = [g, conjugate(g, k), g, k]
        assert act(N_last, [(2, -1)]) == A_last

        odd = list(range(1, 2 * d - 4, 2))
        even = list(range(2, 2 * d - 5, 2))
        cross, last = 2 * d - 4, 2 * d - 3
        assert sorted(odd + even + [cross, last]) == list(range(1, 2 * d - 2))
        lengths = [4 * (d - v - 1) + 5 for v in range(2, d)] + [0, 2, 1]
        assert max(lengths) == 4 * d - 7
        partition_rows.append({"d": d, "edits": 2 * d - 3, "max_length": max(lengths)})

    for d in range(5, 13):
        n = d + 1
        z, y, new = 0, d - 1, d
        for x in range(1, d - 1):
            candidates = [u for u in range(1, d - 1) if u != x]
            if not candidates:
                continue
            u = candidates[0]
            cy = transposition(n, x, y)
            cn = transposition(n, x, new)
            hy = transposition(n, u, y)
            hn = transposition(n, u, new)
            left = act([cy, hy, hy], [(1, -1), (2, -1)])
            right = act([cn, hn, hn], [(1, -1), (2, -1)])
            ux = transposition(n, u, x)
            assert left == [ux, ux, cy]
            assert right == [ux, ux, cn]

            spare = [r for r in range(n) if r not in {x, y, new}]
            if len(spare) >= 2:
                h = transposition(n, spare[0], spare[1])
                assert act([cy, h, h], [(1, -1), (2, -1)]) == [h, h, cy]
                assert act([cn, h, h], [(1, -1), (2, -1)]) == [h, h, cn]

            xy = transposition(n, x, y)
            zx = transposition(n, z, x)
            zy = transposition(n, z, y)
            zn = transposition(n, z, new)
            xn = transposition(n, x, new)
            carrier = [(1, -1), (2, 1), (3, -1), (2, -1), (1, -1)]
            assert act([xy, zx, zy, zn], carrier) == [xn, zy, zy, zx]

    for d in range(5, 9):
        n = d + 1
        es = [transposition(n, 0, r) for r in range(1, d)]
        lower = [x for e in es for x in (e, e)]
        beta = [(2, 1), (3, -1), (1, 1), (len(lower) - 1, -1)]
        pad = transposition(n, 0, d)
        embedded = act(lower + [pad, pad], beta)
        expected = act(lower, beta) + [pad, pad]
        assert embedded == expected
        embedding_rows.append({"d": d, "lower_length": len(lower), "beta_length": len(beta)})

    payload = {
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "checks": {
            "V_D": v_rows,
            "cross_seam_rows": len(seam_rows),
            "edit_partitions": partition_rows,
            "prefix_embeddings": embedding_rows,
            "all_negative_scan_and_carrier": "passed for d=5..12",
        },
    }
    normalized = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["normalized_sha256"] = hashlib.sha256(normalized.encode()).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
