#!/usr/bin/env python3
"""Exact topology/voltage checks supporting the W_L zero-row theorem."""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
from collections import Counter, deque
from pathlib import Path


sys.dont_write_bytecode = True

BASE_WORD = (
    (3, 5), (3, 4), (1, 5), (2, 5),
    (1, 6), (0, 4), (3, 7), (2, 7),
    (0, 5), (3, 6), (1, 4), (1, 7),
    (0, 6), (2, 4), (2, 6), (0, 7),
)
VX = (-1, -1, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
VY = (-1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)


def rotation_faces(word, n: int):
    darts = tuple((i, side) for i in range(len(word)) for side in range(2))
    dart_id = {dart: index for index, dart in enumerate(darts)}
    alpha = {}
    for i in range(len(word)):
        alpha[dart_id[(i, 0)]] = dart_id[(i, 1)]
        alpha[dart_id[(i, 1)]] = dart_id[(i, 0)]
    sigma = {}
    for vertex in range(n):
        incident = [
            dart_id[(i, side)]
            for i, edge in enumerate(word)
            for side, endpoint in enumerate(edge)
            if endpoint == vertex
        ]
        for j, dart in enumerate(incident):
            sigma[dart] = incident[(j + 1) % len(incident)]
    face_map = {dart: sigma[alpha[dart]] for dart in range(len(darts))}
    seen = set()
    faces = []
    for dart in range(len(darts)):
        if dart in seen:
            continue
        face = []
        current = dart
        while current not in seen:
            seen.add(current)
            factor, side = darts[current]
            face.append((factor, side))
            current = face_map[current]
        faces.append(tuple(face))
    return tuple(faces)


def signed_face_voltage(face):
    total = [0, 0]
    for factor, side in face:
        # BASE_WORD is oriented from its smaller (left-part) endpoint to the
        # larger (right-part) endpoint. alpha crosses from `side` to 1-side
        # before sigma, so this dart contributes the opposite of its endpoint
        # orientation when side=0 and the positive orientation when side=1.
        sign = -1 if side == 0 else 1
        total[0] += sign * VX[factor]
        total[1] += sign * VY[factor]
    return tuple(total)


def cycle_voltage(vertices):
    index = {edge: i for i, edge in enumerate(BASE_WORD)}
    total = [0, 0]
    for a, b in zip(vertices, vertices[1:] + vertices[:1]):
        edge = tuple(sorted((a, b)))
        factor = index[edge]
        sign = 1 if a < b else -1
        total[0] += sign * VX[factor]
        total[1] += sign * VY[factor]
    return tuple(total)


def lifted_word(L: int):
    def label(vertex: int, x: int, y: int) -> int:
        return (vertex * L + x) * L + y

    word = []
    for (a, b), dx, dy in zip(BASE_WORD, VX, VY):
        for x in range(L):
            for y in range(L):
                word.append(tuple(sorted((
                    label(a, x, y),
                    label(b, (x + dx) % L, (y + dy) % L),
                ))))
    return tuple(word)


def connected(word, n: int):
    adjacency = [[] for _ in range(n)]
    for a, b in word:
        adjacency[a].append(b)
        adjacency[b].append(a)
    seen = {0}
    queue = deque([0])
    while queue:
        x = queue.popleft()
        for y in adjacency[x]:
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return len(seen) == n


def identity(word, n: int):
    permutation = list(range(n))
    for a, b in word:
        permutation[a], permutation[b] = permutation[b], permutation[a]
    return permutation == list(range(n))


def hurwitz(a, b):
    p, q = b

    def act(x):
        return q if x == p else p if x == q else x

    return b, tuple(sorted((act(a[0]), act(a[1]))))


def move_right_factor_left_across_pair(p, c):
    word = [p, p, c]
    word[1], word[2] = hurwitz(word[1], word[2])
    word[0], word[1] = hurwitz(word[0], word[1])
    return tuple(word)


def move_pair_right_across_left_factor(c, p):
    word = [c, p, p]
    word[0], word[1] = hurwitz(word[0], word[1])
    word[1], word[2] = hurwitz(word[1], word[2])
    return tuple(word)


def local_pair_transparency():
    edges = tuple((a, b) for a in range(5) for b in range(a + 1, 5))
    failures = []
    for p in edges:
        for c in edges:
            left = move_right_factor_left_across_pair(p, c)
            right = move_pair_right_across_left_factor(c, p)
            if not (left[1] == left[2] and left[0] == c):
                failures.append([list(p), list(c), "right-factor-left", left])
            if not (right[0] == right[1] and right[2] == c):
                failures.append([list(p), list(c), "pair-right", right])
    return {"tested_pairs": len(edges) ** 2, "failure_count": len(failures), "failures": failures}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--L", nargs="+", type=int, default=[1, 2, 3, 11])
    args = parser.parse_args()
    base_faces = rotation_faces(BASE_WORD, 8)
    base = {
        "vertices": 8,
        "edges": 16,
        "faces": len(base_faces),
        "euler_characteristic": 8 - 16 + len(base_faces),
        "genus": (2 - (8 - 16 + len(base_faces))) // 2,
        "face_lengths": [len(face) for face in base_faces],
        "face_integer_voltages": [list(signed_face_voltage(face)) for face in base_faces],
        "all_face_voltages_zero": all(signed_face_voltage(face) == (0, 0) for face in base_faces),
        "basis_cycle_x_vertices": [0, 7, 2, 6],
        "basis_cycle_x_voltage": list(cycle_voltage((0, 7, 2, 6))),
        "basis_cycle_y_vertices": [0, 7, 1, 6],
        "basis_cycle_y_voltage": list(cycle_voltage((0, 7, 1, 6))),
        "basis_voltage_determinant": -1,
        "nonzero_x_blocks": [i for i, value in enumerate(VX) if value],
        "nonzero_y_blocks": [i for i, value in enumerate(VY) if value],
        "coordinate_bound": {
            "endpoint_paths": "2 paths * at most 1 matching edge per nonzero block",
            "closing_edges": 2,
            "x": 2 * sum(value != 0 for value in VX) + 2,
            "y": 2 * sum(value != 0 for value in VY) + 2,
        },
    }
    lifts = []
    for L in args.L:
        word = lifted_word(L)
        n = 8 * L * L
        faces = rotation_faces(word, n)
        chi = n - len(word) + len(faces)
        lifts.append({
            "L": L,
            "vertices": n,
            "edges": len(word),
            "faces": len(faces),
            "expected_faces": 8 * L * L,
            "face_length_histogram": dict(sorted(Counter(map(len, faces)).items())),
            "connected": connected(word, n),
            "identity": identity(word, n),
            "euler_characteristic": chi,
            "genus": (2 - chi) // 2,
        })
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "argv": sys.argv,
        "commit": commit,
        "python": platform.python_version(),
        "seed": None,
        "nonstandard_dependencies": {},
        "method": (
            "Exact dart permutations for chronological ribbon faces, exact "
            "integer face/cycle voltages, exact lifted word checks, and "
            "exhaustive local null-pair Hurwitz identities in S_5."
        ),
        "scope_warning": (
            "Finite lift checks corroborate but do not replace the symbolic "
            "all-L surface-cover and coordinate-bound proof."
        ),
        "base": base,
        "lifts": lifts,
        "local_null_pair_transparency": local_pair_transparency(),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
