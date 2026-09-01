#!/usr/bin/env python3
"""Exact/seeded probe for signed-Hurwitz bypasses of the M84 voltage words.

The implementation is deliberately self-contained.  It records literal
generator indices and signs, so every reported path is a source-independent
bijection once its source family is declared.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import random
import subprocess
import time
from collections import deque
from pathlib import Path


BASE_EDGES = (
    (3, 5), (3, 4), (1, 5), (2, 5),
    (1, 6), (0, 4), (3, 7), (2, 7),
    (0, 5), (3, 6), (1, 4), (1, 7),
    (0, 6), (2, 4), (2, 6), (0, 7),
)
VX = (-1, -1, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
VY = (-1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)


Edge = tuple[int, int]
Word = tuple[Edge, ...]
Move = tuple[int, int]  # zero-based adjacent index, sign +1 (R) or -1


def edge(a: int, b: int) -> Edge:
    assert a != b
    return (a, b) if a < b else (b, a)


def vertex(base: int, r: int, s: int, L: int) -> int:
    return (base * L + r) * L + s


def voltage_word(L: int) -> Word:
    out: list[Edge] = []
    for i, (a, b) in enumerate(BASE_EDGES):
        for r in range(L):
            for s in range(L):
                u = vertex(a, r, s, L)
                v = vertex(b, (r + VX[i]) % L, (s + VY[i]) % L, L)
                out.append(edge(u, v))
    return tuple(out)


def conjugate_transposition(a: Edge, by: Edge) -> Edge:
    u, v = a
    x, y = by
    if u == x:
        u = y
    elif u == y:
        u = x
    if v == x:
        v = y
    elif v == y:
        v = x
    return edge(u, v)


def move(word: Word, i: int, sign: int) -> Word:
    a, b = word[i], word[i + 1]
    out = list(word)
    if sign == 1:
        out[i], out[i + 1] = b, conjugate_transposition(a, b)
    elif sign == -1:
        out[i], out[i + 1] = conjugate_transposition(b, a), a
    else:
        raise ValueError(sign)
    return tuple(out)


def apply_moves(word: Word, moves: list[Move]) -> Word:
    for i, sign in moves:
        word = move(word, i, sign)
    return word


def support_connected(word: Word, n: int) -> bool:
    if n <= 1:
        return True
    adj = [[] for _ in range(n)]
    for a, b in word:
        adj[a].append(b)
        adj[b].append(a)
    seen = {0}
    stack = [0]
    while stack:
        a = stack.pop()
        for b in adj[a]:
            if b not in seen:
                seen.add(b)
                stack.append(b)
    return len(seen) == n


def marked_positions(word: Word, n: int) -> list[int]:
    ans = []
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            continue
        reduced = word[:i] + word[i + 2 :]
        if support_connected(reduced, n):
            ans.append(i)
    return ans


def evaluate(word: Word, n: int) -> tuple[int, ...]:
    # Build the algebraic left-to-right product by left-composing each next
    # factor.  Identity is invariant under the equivalent token-time view.
    p = list(range(n))
    for a, b in reversed(word):
        p[a], p[b] = p[b], p[a]
    return tuple(p)


def cyclic_left_word(word: Word, amount: int) -> Word:
    amount %= len(word)
    return word[amount:] + word[:amount]


def cyclic_left_braid(k: int) -> list[Move]:
    return [(i, 1) for i in range(k - 1)]


def random_walk_hit(L: int, steps: int, seed: int, check_every: int) -> dict:
    rng = random.Random(seed)
    source = voltage_word(L)
    n, k = 8 * L * L, 16 * L * L
    assert len(source) == k and evaluate(source, n) == tuple(range(n))
    assert support_connected(source, n)
    word = source
    path: list[Move] = []
    hit = marked_positions(word, n)
    if hit:
        encoded = json.dumps(path, separators=(",", ":")).encode()
        return {
            "hit_step": 0,
            "marked_positions": hit,
            "moves_sha256": hashlib.sha256(encoded).hexdigest(),
            "moves_prefix": path,
            "moves_suffix": path,
        }
    for t in range(1, steps + 1):
        mv = (rng.randrange(k - 1), 1 if rng.randrange(2) else -1)
        word = move(word, *mv)
        path.append(mv)
        if t % check_every == 0:
            hit = marked_positions(word, n)
            if hit:
                assert evaluate(word, n) == tuple(range(n))
                assert apply_moves(source, path) == word
                inverse = [(i, -sign) for i, sign in reversed(path)]
                assert apply_moves(word, inverse) == source
                encoded = json.dumps(path, separators=(",", ":")).encode()
                return {
                    "hit_step": t,
                    "marked_positions": hit,
                    "moves_sha256": hashlib.sha256(encoded).hexdigest(),
                    "moves_prefix": path[:20],
                    "moves_suffix": path[-20:],
                    "endpoint_sha256": hashlib.sha256(repr(word).encode()).hexdigest(),
                }
    return {"hit_step": None, "marked_positions": []}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", action="append", nargs=3, metavar=("L", "STEPS", "SEED"), required=True)
    parser.add_argument("--check-every", type=int, default=1)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    cases = []
    for Ls, stepss, seeds in args.case:
        L, steps, seed = int(Ls), int(stepss), int(seeds)
        result = random_walk_hit(L, steps, seed, args.check_every)
        cases.append({"L": L, "steps": steps, "seed": seed, **result})
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "schema": "m86-signed-bypass-probe-v1",
        "status": "successful paths are exact certificates; failure is empirical only",
        "convention": "(pq)(x)=p(q(x)); R(a,b)=(b,bab)",
        "commit": commit,
        "python": platform.python_version(),
        "dependencies": {},
        "check_every": args.check_every,
        "elapsed_seconds": time.time() - started,
        "cases": cases,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
