#!/usr/bin/env python3
"""Independent exact falsification audit for the frozen M84 theorem.

This file deliberately imports no code from M84 or any predecessor mission.
It checks finite interfaces of the proof.  The all-L theorem still requires
the topological argument audited in report.md.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import subprocess
import sys
import time
from collections import Counter, defaultdict, deque
from pathlib import Path


sys.dont_write_bytecode = True

BASE = (
    (3, 5), (3, 4), (1, 5), (2, 5),
    (1, 6), (0, 4), (3, 7), (2, 7),
    (0, 5), (3, 6), (1, 4), (1, 7),
    (0, 6), (2, 4), (2, 6), (0, 7),
)
VX = (-1, -1, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
VY = (-1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)


def swap_point(x: int, edge: tuple[int, int]) -> int:
    a, b = edge
    return b if x == a else a if x == b else x


def conjugate(edge: tuple[int, int], pivot: tuple[int, int]) -> tuple[int, int]:
    return tuple(sorted((swap_point(edge[0], pivot), swap_point(edge[1], pivot))))


def evaluate(word: tuple[tuple[int, int], ...], n: int) -> tuple[int, ...]:
    # Left-to-right tuple product; tokens are updated chronologically.
    p = list(range(n))
    for a, b in word:
        p[a], p[b] = p[b], p[a]
    return tuple(p)


def components(edges, n: int) -> tuple[tuple[int, ...], ...]:
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        aa, bb = find(a), find(b)
        if aa != bb:
            parent[bb] = aa
    blocks: dict[int, list[int]] = defaultdict(list)
    for x in range(n):
        blocks[find(x)].append(x)
    return tuple(sorted(tuple(block) for block in blocks.values()))


def connected(edges, n: int) -> bool:
    return len(components(edges, n)) == 1


def eliminate(word, order):
    labels = list(range(len(word)))
    values = list(word)
    outputs = []
    for wanted in order:
        pos = labels.index(wanted)
        pivot = values[pos]
        outputs.append(pivot)
        values = [conjugate(edge, pivot) for edge in values[:pos]] + values[pos + 1 :]
        labels = labels[:pos] + labels[pos + 1 :]
    return tuple(outputs), dict(zip(labels, values))


def formula_residual(word, selected):
    answer = {}
    selected = set(selected)
    for j, edge in enumerate(word):
        if j in selected:
            continue
        # Endpoints of H_j^{-1} t_j H_j are moved by H_j^{-1}; under the
        # stated convention that applies selected factors >j increasingly.
        a, b = edge
        for s in sorted(x for x in selected if x > j):
            a = swap_point(a, word[s])
            b = swap_point(b, word[s])
        answer[j] = tuple(sorted((a, b)))
    return answer


def faces(word, n: int):
    darts = tuple((e, side) for e in range(len(word)) for side in (0, 1))
    dart_id = {d: q for q, d in enumerate(darts)}
    alpha = [0] * len(darts)
    for e in range(len(word)):
        alpha[dart_id[(e, 0)]] = dart_id[(e, 1)]
        alpha[dart_id[(e, 1)]] = dart_id[(e, 0)]
    sigma = [0] * len(darts)
    for v in range(n):
        incident = [
            dart_id[(e, side)]
            for e, edge in enumerate(word)
            for side, endpoint in enumerate(edge)
            if endpoint == v
        ]
        if not incident:
            continue
        for q, dart in enumerate(incident):
            sigma[dart] = incident[(q + 1) % len(incident)]
    phi = [sigma[alpha[d]] for d in range(len(darts))]
    seen = set()
    answer = []
    for root in range(len(darts)):
        if root in seen:
            continue
        cycle = []
        d = root
        while d not in seen:
            seen.add(d)
            cycle.append(darts[d])
            d = phi[d]
        answer.append(tuple(cycle))
    return tuple(answer)


def face_mask(face) -> int:
    mask = 0
    for edge, _side in face:
        mask ^= 1 << edge
    return mask


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


def in_span(value: int, basis) -> bool:
    x = value
    while x:
        pivot = x.bit_length() - 1
        if pivot not in basis:
            return False
        x ^= basis[pivot]
    return True


def directed_voltage(start: int, end: int, label: int) -> tuple[int, int]:
    a, b = BASE[label]
    if (start, end) == (a, b):
        return VX[label], VY[label]
    if (start, end) == (b, a):
        return -VX[label], -VY[label]
    raise AssertionError((start, end, label, BASE[label]))


def contour(word, selected, i: int, j: int, with_voltage: bool):
    between = tuple(s for s in sorted(selected) if i < s < j)
    c, d = word[j]
    paths = []
    for start in (c, d):
        pos = start
        traversals = []
        for label in reversed(between):
            new = swap_point(pos, word[label])
            if new != pos:
                traversals.append((label, pos, new))
            pos = new
        paths.append((pos, traversals))
    if set((paths[0][0], paths[1][0])) != set(word[i]):
        raise AssertionError("contour requested for a nonduplicate")

    # Orient c --B--> B(c) --i--> B(d) --B^-1--> d --j--> c.
    end_c, path_c = paths[0]
    end_d, path_d = paths[1]
    if word[i] != tuple(sorted((end_c, end_d))):
        raise AssertionError("endpoint mismatch")
    mask = (1 << i) ^ (1 << j)
    for label, _a, _b in path_c:
        mask ^= 1 << label
    for label, _a, _b in path_d:
        mask ^= 1 << label

    voltage = [0, 0]
    if with_voltage:
        for label, a, b in path_c:
            dx, dy = directed_voltage(a, b, label)
            voltage[0] += dx
            voltage[1] += dy
        dx, dy = directed_voltage(end_c, end_d, i)
        voltage[0] += dx
        voltage[1] += dy
        for label, a, b in reversed(path_d):
            dx, dy = directed_voltage(b, a, label)
            voltage[0] += dx
            voltage[1] += dy
        dx, dy = directed_voltage(d, c, j)
        voltage[0] += dx
        voltage[1] += dy
    return mask, tuple(voltage), (len(path_c), len(path_d))


def mask_is_cycle(mask: int, word, n: int) -> bool:
    parity = [0] * n
    for i, (a, b) in enumerate(word):
        if mask >> i & 1:
            parity[a] ^= 1
            parity[b] ^= 1
    return not any(parity)


def deletion_safety(word, selected, i: int, j: int, n: int):
    order = tuple(sorted(selected)) + (i, j)
    outputs, residual = eliminate(word, order)
    if outputs[-1] != outputs[-2]:
        raise AssertionError("not a duplicate after extraction")
    deletion = outputs[:-2] + tuple(residual[label] for label in sorted(residual))
    return connected(deletion, n), components(deletion, n)


def audit_base():
    n = 8
    k = len(BASE)
    fs = faces(BASE, n)
    boundary_basis = xor_basis(face_mask(f) for f in fs)
    formula_failures = []
    order_failures = []
    prefix_component_failures = []
    outside_failures = []
    homology_failures = []
    contour_cycle_failures = []
    duplicate_pairs = 0
    safe_pairs = 0
    max_voltage = 0
    voltage_hist = Counter()
    path_hist = Counter()

    for mask in range(1 << k):
        selected = tuple(i for i in range(k) if mask >> i & 1)
        expected = formula_residual(BASE, selected)
        out_inc, res_inc = eliminate(BASE, selected)
        out_dec, res_dec = eliminate(BASE, tuple(reversed(selected)))
        if res_inc != expected and len(formula_failures) < 20:
            formula_failures.append(mask)
        if res_dec != expected and len(order_failures) < 20:
            order_failures.append(mask)
        original_components = components((BASE[i] for i in selected), n)
        if components(out_inc, n) != original_components and len(prefix_component_failures) < 20:
            prefix_component_failures.append((mask, "increasing"))
        if components(out_dec, n) != original_components and len(prefix_component_failures) < 20:
            prefix_component_failures.append((mask, "decreasing"))

        unselected = tuple(i for i in range(k) if not (mask >> i & 1))
        for i, j in itertools.combinations(unselected, 2):
            if expected[i] != expected[j]:
                continue
            duplicate_pairs += 1
            safe, _parts = deletion_safety(BASE, selected, i, j, n)
            safe_pairs += int(safe)
            between = tuple(s for s in selected if i < s < j)
            safe_between, _ = deletion_safety(BASE, between, i, j, n)
            if safe != safe_between and len(outside_failures) < 20:
                outside_failures.append((mask, i, j, safe, safe_between))
            chain, voltage, path_lengths = contour(BASE, selected, i, j, True)
            if not mask_is_cycle(chain, BASE, n) and len(contour_cycle_failures) < 20:
                contour_cycle_failures.append((mask, i, j, chain))
            nonzero_homology = not in_span(chain, boundary_basis)
            if safe != nonzero_homology and len(homology_failures) < 20:
                homology_failures.append((mask, i, j, safe, chain))
            max_voltage = max(max_voltage, abs(voltage[0]), abs(voltage[1]))
            voltage_hist[str(voltage)] += 1
            path_hist[str(path_lengths)] += 1

    face_voltages = []
    for f in fs:
        total = [0, 0]
        for label, side in f:
            sign = -1 if side == 0 else 1
            total[0] += sign * VX[label]
            total[1] += sign * VY[label]
        face_voltages.append(tuple(total))

    def cycle_voltage(vertices):
        lookup = {edge: i for i, edge in enumerate(BASE)}
        total = [0, 0]
        for a, b in zip(vertices, vertices[1:] + vertices[:1]):
            label = lookup[tuple(sorted((a, b)))]
            dx, dy = directed_voltage(a, b, label)
            total[0] += dx
            total[1] += dy
        return tuple(total)

    return {
        "identity": evaluate(BASE, n) == tuple(range(n)),
        "connected": connected(BASE, n),
        "face_count": len(fs),
        "face_lengths": sorted(map(len, fs)),
        "euler_characteristic": n - k + len(fs),
        "face_voltages": face_voltages,
        "basis_cycle_voltages": [
            cycle_voltage((0, 7, 2, 6)),
            cycle_voltage((0, 7, 1, 6)),
        ],
        "subsets_checked": 1 << k,
        "formula_failure_count": len(formula_failures),
        "formula_failures": formula_failures,
        "reverse_order_failure_count": len(order_failures),
        "reverse_order_failures": order_failures,
        "prefix_component_failure_count": len(prefix_component_failures),
        "prefix_component_failures": prefix_component_failures,
        "duplicate_subset_pairs": duplicate_pairs,
        "safe_subset_pairs": safe_pairs,
        "outside_selection_failure_count": len(outside_failures),
        "outside_selection_failures": outside_failures,
        "contour_cycle_failure_count": len(contour_cycle_failures),
        "contour_cycle_failures": contour_cycle_failures,
        "safe_homology_failure_count": len(homology_failures),
        "safe_homology_failures": homology_failures,
        "maximum_absolute_contour_voltage": max_voltage,
        "voltage_histogram": dict(sorted(voltage_hist.items())),
        "path_length_histogram": dict(sorted(path_hist.items())),
    }


def lift_word(L: int):
    def vertex(base: int, x: int, y: int) -> int:
        return (base * L + x) * L + y

    word = []
    blocks = []
    for q, ((a, b), dx, dy) in enumerate(zip(BASE, VX, VY)):
        block = []
        for x in range(L):
            for y in range(L):
                edge = tuple(sorted((
                    vertex(a, x, y),
                    vertex(b, (x + dx) % L, (y + dy) % L),
                )))
                word.append(edge)
                block.append(edge)
        blocks.append(tuple(block))
    return tuple(word), tuple(blocks)


def audit_lift(L: int):
    word, blocks = lift_word(L)
    n = 8 * L * L
    fs = faces(word, n)
    block_matching_failures = 0
    for block in blocks:
        degree = Counter(x for edge in block for x in edge)
        if len(degree) != n or set(degree.values()) != {1}:
            # A base matching meets every lifted vertex over its two base
            # endpoints, not all n vertices.  Check precisely that scope.
            expected = 2 * L * L
            if len(degree) != expected or set(degree.values()) != {1}:
                block_matching_failures += 1
    return {
        "L": L,
        "vertices": n,
        "factors": len(word),
        "identity": evaluate(word, n) == tuple(range(n)),
        "connected": connected(word, n),
        "simple_support": len(set(word)) == len(word),
        "bipartite": all(a // (L * L) < 4 <= b // (L * L) for a, b in word),
        "faces": len(fs),
        "face_lengths": dict(sorted(Counter(map(len, fs)).items())),
        "euler_characteristic": n - len(word) + len(fs),
        "block_matching_failures": block_matching_failures,
    }


def null_pair_transparency():
    edges = tuple(itertools.combinations(range(5), 2))
    failures = []

    def right_move(a, b):
        return b, conjugate(a, b)

    for p in edges:
        for c in edges:
            x = [p, p, c]
            x[1], x[2] = right_move(x[1], x[2])
            x[0], x[1] = right_move(x[0], x[1])
            y = [c, p, p]
            y[0], y[1] = right_move(y[0], y[1])
            y[1], y[2] = right_move(y[1], y[2])
            if not (x[0] == c and x[1] == x[2]):
                failures.append((p, c, "left", tuple(x)))
            if not (y[0] == y[1] and y[2] == c):
                failures.append((p, c, "right", tuple(y)))
    return {"cases": len(edges) ** 2, "failure_count": len(failures), "failures": failures[:20]}


def audit_generic_s3():
    n = 3
    edges = tuple(itertools.combinations(range(n), 2))
    words = 0
    duplicate_pairs = 0
    safe_pairs = 0
    outside_failures = []
    contour_failures = []
    homology_failures = []
    for indices in itertools.product(range(3), repeat=6):
        word = tuple(edges[i] for i in indices)
        if evaluate(word, n) != tuple(range(n)) or not connected(word, n):
            continue
        words += 1
        boundary_basis = xor_basis(face_mask(f) for f in faces(word, n))
        for mask in range(1 << 6):
            selected = tuple(i for i in range(6) if mask >> i & 1)
            residual = formula_residual(word, selected)
            unselected = tuple(sorted(residual))
            for i, j in itertools.combinations(unselected, 2):
                if residual[i] != residual[j]:
                    continue
                duplicate_pairs += 1
                safe, _ = deletion_safety(word, selected, i, j, n)
                safe_pairs += int(safe)
                between = tuple(s for s in selected if i < s < j)
                safe_between, _ = deletion_safety(word, between, i, j, n)
                if safe != safe_between and len(outside_failures) < 20:
                    outside_failures.append((indices, mask, i, j))
                chain, _voltage, _lengths = contour(word, selected, i, j, False)
                if not mask_is_cycle(chain, word, n) and len(contour_failures) < 20:
                    contour_failures.append((indices, mask, i, j, chain))
                nonzero_homology = not in_span(chain, boundary_basis)
                if safe != nonzero_homology and len(homology_failures) < 20:
                    homology_failures.append((indices, mask, i, j, safe, chain))
    return {
        "connected_genus_one_identity_words": words,
        "duplicate_subset_pairs": duplicate_pairs,
        "safe_subset_pairs": safe_pairs,
        "outside_selection_failure_count": len(outside_failures),
        "outside_selection_failures": outside_failures,
        "contour_cycle_failure_count": len(contour_failures),
        "contour_cycle_failures": contour_failures,
        "safe_homology_failure_count": len(homology_failures),
        "safe_homology_failures": homology_failures,
    }


def ambient_record(L: int):
    d = 8 * L * L
    k = 16 * L * L
    N = d + 2
    m = k + 2
    return {
        "L": L,
        "genus_one_component_vertices": d,
        "genus_one_component_factors": k,
        "genus_zero_component_vertices": 2,
        "genus_zero_component_factors": 2,
        "ambient_N": N,
        "ambient_m": m,
        "minimal_identity": m == 2 * N - 2,
        "both_components_nontrivial": True,
        "component_genera": [1, 0],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        commit = "unavailable"
    results = {
        "base": audit_base(),
        "local_null_pair_transparency": null_pair_transparency(),
        "generic_s3": audit_generic_s3(),
        "lifts": [audit_lift(2), audit_lift(11)],
        "coordinate_bound": {
            "nonzero_x_blocks": sum(v != 0 for v in VX),
            "nonzero_y_blocks": sum(v != 0 for v in VY),
            "two_endpoint_paths_plus_two_closing_edges": 10,
        },
        "ambient_L11": ambient_record(11),
    }
    payload = {
        "argv": sys.argv,
        "commit": commit,
        "python": platform.python_version(),
        "seed": None,
        "nonstandard_dependencies": {},
        "method": "Independent standard-library reconstruction; no imports from M84 or predecessor missions.",
        "scope_warning": "Finite exact checks are falsification only and do not replace the all-L proof audit.",
        "elapsed_seconds": time.perf_counter() - started,
        "results": results,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(results, sort_keys=True))


if __name__ == "__main__":
    main()
