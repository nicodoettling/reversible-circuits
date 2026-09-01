#!/usr/bin/env python3
"""Exhaustive S_3 genus-one falsification of the collision-contour lemma."""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path


sys.dont_write_bytecode = True


def conjugate(edge, pivot):
    p, q = pivot

    def act(x):
        return q if x == p else p if x == q else x

    return tuple(sorted((act(edge[0]), act(edge[1]))))


def stable_residual(word, selected):
    values = list(word)
    labels = list(range(len(word)))
    for wanted in sorted(selected):
        position = labels.index(wanted)
        pivot = values[position]
        values = [conjugate(e, pivot) for e in values[:position]] + values[position + 1 :]
        labels = labels[:position] + labels[position + 1 :]
    return dict(zip(labels, values))


def connected(edges, n):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        aa, bb = find(a), find(b)
        if aa != bb:
            parent[bb] = aa
    return len({find(x) for x in range(n)}) == 1


def identity(word, n):
    p = list(range(n))
    for a, b in word:
        p[a], p[b] = p[b], p[a]
    return p == list(range(n))


def rotation_faces(word, n):
    darts = tuple((i, side) for i in range(len(word)) for side in range(2))
    dart_id = {dart: x for x, dart in enumerate(darts)}
    alpha = {dart_id[(i, side)]: dart_id[(i, 1 - side)] for i, side in darts}
    sigma = {}
    for vertex in range(n):
        incident = [
            dart_id[(i, side)]
            for i, edge in enumerate(word)
            for side, endpoint in enumerate(edge)
            if endpoint == vertex
        ]
        for x, dart in enumerate(incident):
            sigma[dart] = incident[(x + 1) % len(incident)]
    phi = {x: sigma[alpha[x]] for x in range(len(darts))}
    seen = set()
    faces = []
    for root in range(len(darts)):
        if root in seen:
            continue
        current = root
        mask = 0
        while current not in seen:
            seen.add(current)
            factor, _side = darts[current]
            mask ^= 1 << factor
            current = phi[current]
        faces.append(mask)
    return tuple(faces)


def xor_basis(vectors):
    basis = {}
    for value in vectors:
        x = value
        while x:
            pivot = x.bit_length() - 1
            if pivot in basis:
                x ^= basis[pivot]
            else:
                basis[pivot] = x
                break
    return basis


def in_span(value, basis):
    x = value
    while x:
        pivot = x.bit_length() - 1
        if pivot not in basis:
            return False
        x ^= basis[pivot]
    return True


def move(position, edge):
    a, b = edge
    return b if position == a else a if position == b else position


def contour_mask(word, selected, i, j):
    labels = tuple(x for x in range(i + 1, j) if x in selected)
    c, d = word[j]
    mask = (1 << i) ^ (1 << j)
    for start in (c, d):
        position = start
        for label in reversed(labels):
            new = move(position, word[label])
            if new != position:
                mask ^= 1 << label
            position = new
    return mask


def audit():
    n = 3
    edges = tuple(itertools.combinations(range(n), 2))
    words = 0
    duplicate_states = 0
    safe_states = 0
    mismatch = []
    contour_not_cycle = []
    face_histogram = Counter()
    started = time.perf_counter()
    for indices in itertools.product(range(len(edges)), repeat=2 * n):
        word = tuple(edges[x] for x in indices)
        if not identity(word, n) or not connected(word, n):
            continue
        words += 1
        faces = rotation_faces(word, n)
        face_histogram[str(tuple(sorted(mask.bit_count() for mask in faces)))] += 1
        basis = xor_basis(faces)
        for selected_mask in range(1 << len(word)):
            selected = frozenset(
                label for label in range(len(word)) if selected_mask >> label & 1
            )
            residual = stable_residual(word, selected)
            unselected = sorted(residual)
            for i, j in itertools.combinations(unselected, 2):
                if residual[i] != residual[j]:
                    continue
                duplicate_states += 1
                enlarged = selected | {i, j}
                after = stable_residual(word, enlarged)
                safe = connected(
                    itertools.chain(
                        (word[label] for label in selected),
                        after.values(),
                    ),
                    n,
                )
                safe_states += safe
                mask = contour_mask(word, selected, i, j)
                degree = [0] * n
                for label in range(len(word)):
                    if mask >> label & 1:
                        a, b = word[label]
                        degree[a] ^= 1
                        degree[b] ^= 1
                if any(degree) and len(contour_not_cycle) < 100:
                    contour_not_cycle.append({
                        "word": indices,
                        "selected_mask": selected_mask,
                        "pair": [i, j],
                        "contour_mask": mask,
                    })
                nonzero_homology = not in_span(mask, basis)
                if safe != nonzero_homology and len(mismatch) < 100:
                    mismatch.append({
                        "word": indices,
                        "selected_mask": selected_mask,
                        "pair": [i, j],
                        "safe": safe,
                        "contour_mask": mask,
                        "face_masks": faces,
                    })
    return {
        "n": n,
        "length": 2 * n,
        "connected_identity_words": words,
        "duplicate_subset_pairs": duplicate_states,
        "safe_subset_pairs": safe_states,
        "face_length_histogram": dict(sorted(face_histogram.items())),
        "contour_not_cycle_count": len(contour_not_cycle),
        "contour_not_cycle_examples": contour_not_cycle,
        "safe_iff_nonzero_mod2_homology_failure_count": len(mismatch),
        "safe_iff_nonzero_mod2_homology_failures": mismatch,
        "elapsed_seconds": time.perf_counter() - started,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
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
            "Exhaust all connected identity words in S_3 of genus one, all "
            "selected subsets, and all duplicate pairs; compute contour "
            "mod-2 homology in the literal chronological cell complex."
        ),
        "scope_warning": "Finite falsification only; not the general proof.",
        "result": audit(),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["result"], sort_keys=True))


if __name__ == "__main__":
    main()
