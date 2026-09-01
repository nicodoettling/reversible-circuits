#!/usr/bin/env python3
"""Exact combinatorial audit of the M113/M118 local incidence chain A_d.

This script does not enumerate transposition words.  It constructs every
realizable key from the connected-unicycle criterion, evaluates the exact
genus-zero side counts, and constructs adjacent stationary flows from the
Cartesian overlap formula.  All combinatorial counts and cut ratios are exact;
only the reported eigenvalues use floating sparse diagonalization.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import subprocess
import time
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh


Key = tuple[int, tuple[int, ...], tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]]


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return p*q under (p q)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    ans = [0] * len(p)
    for x, y in enumerate(p):
        ans[y] = x
    return tuple(ans)


def transposition_perm(d: int, edge: tuple[int, int]) -> tuple[int, ...]:
    ans = list(range(d))
    a, b = edge
    ans[a], ans[b] = ans[b], ans[a]
    return tuple(ans)


def cycles(p: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    seen: set[int] = set()
    out: list[tuple[int, ...]] = []
    for x in range(len(p)):
        if x in seen:
            continue
        cyc = []
        y = x
        while y not in seen:
            seen.add(y)
            cyc.append(y)
            y = p[y]
        out.append(tuple(sorted(cyc)))
    return tuple(sorted(out, key=lambda z: (z[0], len(z), z)))


def set_partitions(n: int) -> tuple[tuple[tuple[int, ...], ...], ...]:
    out: list[tuple[tuple[int, ...], ...]] = []

    def rec(i: int, blocks: list[list[int]]) -> None:
        if i == n:
            out.append(tuple(tuple(block) for block in blocks))
            return
        for block in blocks:
            block.append(i)
            rec(i + 1, blocks)
            block.pop()
        blocks.append([i])
        rec(i + 1, blocks)
        blocks.pop()

    rec(0, [])
    return tuple(out)


def atom_partition_to_labels(
    part: tuple[tuple[int, ...], ...], cyc: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, ...], ...]:
    blocks = [tuple(sorted(x for i in atom_block for x in cyc[i])) for atom_block in part]
    return tuple(sorted(blocks, key=lambda z: z[0]))


def incidence_connected(
    cyc: tuple[tuple[int, ...], ...],
    ql: tuple[tuple[int, ...], ...],
    qr: tuple[tuple[int, ...], ...],
) -> bool:
    nl = len(ql)
    adj = [[] for _ in range(nl + len(qr))]
    for atom in cyc:
        x = atom[0]
        li = next(i for i, block in enumerate(ql) if x in block)
        ri = next(i for i, block in enumerate(qr) if x in block)
        adj[li].append(nl + ri)
        adj[nl + ri].append(li)
    seen = {0}
    todo = [0]
    while todo:
        u = todo.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                todo.append(v)
    return len(seen) == len(adj)


def all_keys(d: int) -> list[Key]:
    out: set[Key] = set()
    partition_cache = {c: set_partitions(c) for c in range(1, d + 1)}
    for raw_p in itertools.permutations(range(d)):
        p = tuple(raw_p)
        cyc = cycles(p)
        label_parts = [atom_partition_to_labels(part, cyc) for part in partition_cache[len(cyc)]]
        for ql in label_parts:
            for qr in label_parts:
                if len(ql) + len(qr) != len(cyc):
                    continue
                if incidence_connected(cyc, ql, qr):
                    out.add((d + len(qr) - len(ql), p, ql, qr))
    return sorted(out)


def join_partition(
    part: tuple[tuple[int, ...], ...], edge: tuple[int, int]
) -> tuple[tuple[int, ...], ...]:
    a, b = edge
    ia = next(i for i, block in enumerate(part) if a in block)
    ib = next(i for i, block in enumerate(part) if b in block)
    if ia == ib:
        return part
    merged = tuple(sorted(part[ia] + part[ib]))
    ans = [block for i, block in enumerate(part) if i not in (ia, ib)] + [merged]
    return tuple(sorted(ans, key=lambda z: z[0]))


def transposition_support(p: tuple[int, ...]) -> tuple[int, int] | None:
    moved = [x for x, y in enumerate(p) if x != y]
    if len(moved) == 2 and p[moved[0]] == moved[1] and p[moved[1]] == moved[0]:
        return (moved[0], moved[1])
    return None


def compatible(low: Key, high: Key) -> tuple[int, int] | None:
    j, p, ql, qr = low
    j2, p2, ql2, qr2 = high
    if j2 != j + 1:
        return None
    edge = transposition_support(compose(inverse(p), p2))
    if edge is None:
        return None
    if join_partition(ql, edge) != ql2 or join_partition(qr2, edge) != qr:
        return None
    return edge


def side_count(
    d: int,
    p: tuple[int, ...],
    part: tuple[tuple[int, ...], ...],
    length: int,
) -> int:
    cyc = cycles(p)
    ans = Fraction(math.factorial(length), 1)
    for block in part:
        block_set = set(block)
        c_b = sum(set(atom) <= block_set for atom in cyc)
        ans *= Fraction(len(block), 1) ** (c_b - 3)
    for atom in cyc:
        a = len(atom)
        ans *= Fraction(a**a, math.factorial(a - 1))
    if ans.denominator != 1:
        raise AssertionError((d, p, part, length, ans))
    return ans.numerator


def key_counts(d: int, key: Key) -> tuple[int, int, int]:
    j, p, ql, qr = key
    u = side_count(d, p, ql, j)
    v = side_count(d, p, qr, 2 * d - j)
    return u, v, u * v


def is_singleton_split(low: Key, high: Key) -> bool:
    if high[0] != low[0] + 1 or high[2] != low[2]:
        return False
    old = [frozenset(x) for x in cycles(low[1])]
    new = [frozenset(x) for x in cycles(high[1])]
    if len(new) != len(old) + 1:
        return False
    for singleton in new:
        if len(singleton) != 1:
            continue
        for residual in new:
            if residual == singleton or singleton | residual not in old:
                continue
            old_rest = sorted((x for x in old if x != singleton | residual), key=lambda x: tuple(sorted(x)))
            new_rest = sorted((x for x in new if x not in (singleton, residual)), key=lambda x: tuple(sorted(x)))
            if old_rest == new_rest:
                return True
    return False


def reverse_key(key: Key, d: int) -> Key:
    j, p, ql, qr = key
    return (2 * d - j, inverse(p), qr, ql)


def singleton_or_reverse(low: Key, high: Key, d: int) -> bool:
    return is_singleton_split(low, high) or is_singleton_split(
        reverse_key(high, d), reverse_key(low, d)
    )


def block_of(part: tuple[tuple[int, ...], ...], x: int) -> tuple[int, ...]:
    return next(block for block in part if x in block)


def statistic_record(key: Key) -> dict[str, int]:
    j, p, ql, qr = key
    cyc = cycles(p)
    degrees = []
    for block in ql + qr:
        bs = set(block)
        degrees.append(sum(set(atom) <= bs for atom in cyc))
    incidence_edges = []
    for atom in cyc:
        x = atom[0]
        li = next(i for i, block in enumerate(ql) if x in block)
        ri = next(i for i, block in enumerate(qr) if x in block)
        incidence_edges.append((li, len(ql) + ri))
    nvertices = len(ql) + len(qr)
    active_vertices = set(range(nvertices))
    active_edges = set(range(len(incidence_edges)))
    changed = True
    while changed:
        changed = False
        deg = {v: 0 for v in active_vertices}
        for ei in active_edges:
            a, b = incidence_edges[ei]
            if a in active_vertices and b in active_vertices:
                deg[a] += 1
                deg[b] += 1
        leaves = [v for v, value in deg.items() if value <= 1]
        if leaves:
            changed = True
            remove = set(leaves)
            active_vertices -= remove
            active_edges = {
                ei for ei in active_edges
                if incidence_edges[ei][0] not in remove and incidence_edges[ei][1] not in remove
            }
    return {
        "j": j,
        "cycles": len(cyc),
        "max_cycle": max(map(len, cyc)),
        "left_blocks": len(ql),
        "right_blocks": len(qr),
        "cut_imbalance": abs(j - len(p)),
        "max_label_block": max(map(len, ql + qr)),
        "max_incidence_degree": max(degrees),
        "leaf_vertices": sum(value == 1 for value in degrees),
        "core_edges": len(active_edges),
        "identity": int(p == tuple(range(len(p)))),
    }


def fraction_json(x: Fraction) -> dict:
    return {"numerator": x.numerator, "denominator": x.denominator, "float": float(x)}


def key_json(key: Key) -> dict:
    return {
        "j": key[0],
        "p": list(key[1]),
        "Q_L": [list(x) for x in key[2]],
        "Q_R": [list(x) for x in key[3]],
    }


def scan_threshold_cuts(
    values: list[int], weights: list[int], edges: list[tuple[int, int, int]]
) -> dict | None:
    total = sum(weights)
    best = None
    for threshold in sorted(set(values))[:-1]:
        inside = [value <= threshold for value in values]
        mass = sum(w for w, yes in zip(weights, inside) if yes)
        if mass == 0 or mass == total:
            continue
        boundary_twice = sum(overlap for a, b, overlap in edges if inside[a] != inside[b])
        phi = Fraction(boundary_twice, 2 * min(mass, total - mass))
        if best is None or phi < best[0]:
            best = (phi, threshold, mass)
    if best is None:
        return None
    phi, threshold, mass = best
    return {
        "threshold_for_stat_leq": threshold,
        "mass": fraction_json(Fraction(mass, total)),
        "conductance": fraction_json(phi),
    }


def canonical_singleton_edge(d: int, key: Key) -> tuple[Key, Fraction, str]:
    """Return one certified singleton split/reverse neighbor and its lower formula."""
    j, p, ql, qr = key
    ident = tuple(range(d))
    cyc = cycles(p)
    if p != ident:
        atom = next(atom for atom in cyc if len(atom) >= 2)
        x = atom[0]
        edge = tuple(sorted((x, inverse(p)[x])))
        p2 = compose(p, transposition_perm(d, edge))
        old = block_of(qr, x)
        rest = tuple(y for y in old if y != x)
        qr2 = tuple(sorted([b for b in qr if b != old] + [(x,), rest], key=lambda z: z[0]))
        target: Key = (j + 1, p2, ql, qr2)
        a = len(atom)
        b = len(old)
        s = sum(set(c) <= set(old) for c in cyc)
        ratio = Fraction(1, 2 * (2 * d - j))
        ratio *= Fraction((a - 1) ** a, a**a)
        ratio *= Fraction(b - 1, b) ** (s - 3)
        return target, ratio, "nonidentity_right_singleton_split"

    for block in ql:
        for x, y in itertools.combinations(block, 2):
            if block_of(qr, x) == block_of(qr, y):
                continue
            edge = (x, y)
            p0 = transposition_perm(d, edge)
            qr0 = join_partition(qr, edge)
            target = (j - 1, p0, ql, qr0)
            return target, Fraction(2, j * len(block)), "identity_left_reverse"
    for block in qr:
        for x, y in itertools.combinations(block, 2):
            if block_of(ql, x) == block_of(ql, y):
                continue
            edge = (x, y)
            p2 = transposition_perm(d, edge)
            ql2 = join_partition(ql, edge)
            target = (j + 1, p2, ql2, qr)
            return target, Fraction(2, (2 * d - j) * len(block)), "identity_right_reverse"
    raise AssertionError("d>=3 connected unicycle must have a nonparallel adjacent pair")


def atom_factor(a: int) -> Fraction:
    return Fraction(a**a, math.factorial(a - 1))


def canonical_join_edge(d: int, key: Key) -> tuple[Key, Fraction, str]:
    """One join edge increasing defect when the seam has >=3 cycles."""
    j, p, ql, qr = key
    cyc = cycles(p)
    if len(cyc) < 3:
        raise ValueError("top defect level has no required upward join")

    def atom_block(part: tuple[tuple[int, ...], ...], atom: tuple[int, ...]) -> tuple[int, ...]:
        return block_of(part, atom[0])

    # Two atom-edges at one right incidence vertex with distinct left ends:
    # shift the cut right, join the atoms, and merge those left blocks.
    for block in qr:
        incident = [atom for atom in cyc if set(atom) <= set(block)]
        for first, second in itertools.combinations(incident, 2):
            if atom_block(ql, first) == atom_block(ql, second):
                continue
            edge = tuple(sorted((first[0], second[0])))
            p2 = compose(p, transposition_perm(d, edge))
            target: Key = (j + 1, p2, join_partition(ql, edge), qr)
            ratio = atom_factor(len(first) + len(second)) / (
                atom_factor(len(first)) * atom_factor(len(second))
            )
            return target, ratio / (2 * (2 * d - j) * len(block)), "right_join"

    # Color-reversed case: shift the cut left and merge the right blocks.
    for block in ql:
        incident = [atom for atom in cyc if set(atom) <= set(block)]
        for first, second in itertools.combinations(incident, 2):
            if atom_block(qr, first) == atom_block(qr, second):
                continue
            edge = tuple(sorted((first[0], second[0])))
            p0 = compose(p, transposition_perm(d, edge))
            target = (j - 1, p0, ql, join_partition(qr, edge))
            ratio = atom_factor(len(first) + len(second)) / (
                atom_factor(len(first)) * atom_factor(len(second))
            )
            return target, ratio / (2 * j * len(block)), "left_join"

    raise AssertionError("connected incidence graph on >=3 vertices has a branching simple neighbor")


def run_case(d: int) -> dict:
    started = time.time()
    keys = all_keys(d)
    index = {key: i for i, key in enumerate(keys)}
    counts = [key_counts(d, key) for key in keys]
    weights = [x[2] for x in counts]
    total_weight = sum(weights)
    by_j: dict[int, list[int]] = defaultdict(list)
    for i, key in enumerate(keys):
        by_j[key[0]].append(i)

    edge_rows: list[tuple[int, int, int]] = []
    singleton_edge_rows: list[tuple[int, int, int]] = []
    neighbors: dict[tuple[int, int], int] = {}
    singleton_rates = [Fraction(0) for _ in keys]
    move_rates = [Fraction(0) for _ in keys]
    parent = list(range(len(keys)))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    for j, lows in by_j.items():
        for a in lows:
            for b in by_j.get(j + 1, []):
                if compatible(keys[a], keys[b]) is None:
                    continue
                overlap = counts[a][0] * counts[b][1]
                edge_rows.append((a, b, overlap))
                neighbors[(a, b)] = overlap
                neighbors[(b, a)] = overlap
                union(a, b)
                pa = Fraction(overlap, 2 * weights[a])
                pb = Fraction(overlap, 2 * weights[b])
                move_rates[a] += pa
                move_rates[b] += pb
                if singleton_or_reverse(keys[a], keys[b], d):
                    singleton_edge_rows.append((a, b, overlap))
                    singleton_rates[a] += pa
                    singleton_rates[b] += pb

    row_failures = [i for i, value in enumerate(move_rates) if value > 1]
    components = len({find(i) for i in range(len(keys))})

    canonical_failures = []
    canonical_ratios = []
    join_failures = []
    join_ratios = []
    if d >= 3:
        for i, key in enumerate(keys):
            target, formula, kind = canonical_singleton_edge(d, key)
            target_i = index.get(target)
            if target_i is None or (i, target_i) not in neighbors:
                canonical_failures.append({"source": key_json(key), "target": key_json(target), "kind": kind})
                continue
            actual = Fraction(neighbors[(i, target_i)], 2 * weights[i])
            if actual != formula or not singleton_or_reverse(
                keys[min(i, target_i, key=lambda z: keys[z][0])],
                keys[max(i, target_i, key=lambda z: keys[z][0])], d
            ):
                canonical_failures.append({
                    "source": key_json(key), "target": key_json(target),
                    "kind": kind, "actual": str(actual), "formula": str(formula),
                })
            canonical_ratios.append(actual)
            if len(cycles(key[1])) >= 3:
                join_target, join_formula, join_kind = canonical_join_edge(d, key)
                join_i = index.get(join_target)
                if join_i is None or (i, join_i) not in neighbors:
                    join_failures.append({
                        "source": key_json(key), "target": key_json(join_target),
                        "kind": join_kind,
                    })
                    continue
                join_actual = Fraction(neighbors[(i, join_i)], 2 * weights[i])
                if join_actual != join_formula:
                    join_failures.append({
                        "source": key_json(key), "target": key_json(join_target),
                        "kind": join_kind, "actual": str(join_actual),
                        "formula": str(join_formula),
                    })
                join_ratios.append(join_actual)

    # Reversible symmetrization; Z cancels from every entry.  The second
    # matrix retains only singleton-cycle split edges and holds the rest.
    def spectral_record(
        selected_edges: list[tuple[int, int, int]], rates: list[Fraction]
    ) -> tuple[float, np.ndarray, float, int]:
        rows: list[int] = []
        cols: list[int] = []
        data: list[float] = []
        skeleton_parent = list(range(len(keys)))

        def skeleton_find(x: int) -> int:
            while skeleton_parent[x] != x:
                skeleton_parent[x] = skeleton_parent[skeleton_parent[x]]
                x = skeleton_parent[x]
            return x

        for a, b, overlap in selected_edges:
            ra, rb = skeleton_find(a), skeleton_find(b)
            if ra != rb:
                skeleton_parent[rb] = ra
            value = overlap / (2.0 * math.sqrt(weights[a] * weights[b]))
            rows.extend((a, b))
            cols.extend((b, a))
            data.extend((value, value))
        for i, rate in enumerate(rates):
            rows.append(i)
            cols.append(i)
            data.append(float(1 - rate))
        matrix = sparse.csr_matrix((data, (rows, cols)), shape=(len(keys), len(keys)))
        component_count = len({skeleton_find(i) for i in range(len(keys))})
        if len(keys) == 1:
            return 1.0, np.array([1.0]), 0.0, component_count
        k = min(6, len(keys) - 1)
        eigenvalues = np.sort(
            eigsh(matrix, k=k, which="LA", return_eigenvectors=False, tol=1e-12)
        )
        spectral_gap = 0.0 if component_count > 1 else float(1.0 - eigenvalues[-2])
        root_weights = np.sqrt(np.asarray(weights, dtype=float))
        residual = float(np.max(np.abs(matrix @ root_weights - root_weights)))
        return spectral_gap, eigenvalues, residual, component_count

    gap, eig, eigen_residual, spectral_components = spectral_record(edge_rows, move_rates)
    singleton_gap, singleton_eig, singleton_eigen_residual, singleton_components = spectral_record(
        singleton_edge_rows, singleton_rates
    )

    stat = [statistic_record(key) for key in keys]
    statistic_names = tuple(stat[0])
    scans = {
        name: scan_threshold_cuts([row[name] for row in stat], weights, edge_rows)
        for name in statistic_names
    }
    min_move_i = min(range(len(keys)), key=lambda i: move_rates[i])
    min_singleton_i = min(range(len(keys)), key=lambda i: singleton_rates[i])
    identity_indices = [i for i, key in enumerate(keys) if key[1] == tuple(range(d))]
    nonidentity_indices = [i for i in range(len(keys)) if i not in set(identity_indices)]

    level_weight: dict[int, int] = defaultdict(int)
    level_edge_overlap: dict[tuple[int, int], int] = defaultdict(int)
    for i, key in enumerate(keys):
        level_weight[d - len(cycles(key[1]))] += weights[i]
    for a, b, overlap in edge_rows:
        ra = d - len(cycles(keys[a][1]))
        rb = d - len(cycles(keys[b][1]))
        if abs(ra - rb) != 1:
            raise AssertionError("every transposition changes cycle defect by one")
        level_edge_overlap[tuple(sorted((ra, rb)))] += overlap
    level_sequence = [level_weight[r] for r in range(d - 1)]
    modes = [r for r, value in enumerate(level_sequence) if value == max(level_sequence)]
    first_mode, last_mode = min(modes), max(modes)
    level_unimodal = (
        all(level_sequence[r] <= level_sequence[r + 1] for r in range(first_mode))
        and all(level_sequence[r] == max(level_sequence) for r in range(first_mode, last_mode + 1))
        and all(level_sequence[r] >= level_sequence[r + 1] for r in range(last_mode, len(level_sequence) - 1))
    )
    level_log_concave = all(
        level_sequence[r] ** 2 >= level_sequence[r - 1] * level_sequence[r + 1]
        for r in range(1, len(level_sequence) - 1)
    )
    level_records = []
    for r, value in enumerate(level_sequence):
        down = None if r == 0 else Fraction(level_edge_overlap[(r - 1, r)], 2 * value)
        up = None if r == d - 2 else Fraction(level_edge_overlap[(r, r + 1)], 2 * value)
        level_records.append({
            "defect": r,
            "stationary_mass": fraction_json(Fraction(value, total_weight)),
            "down_probability": None if down is None else fraction_json(down),
            "up_probability": None if up is None else fraction_json(up),
        })

    def min_on(indices: list[int], values: list[Fraction]) -> dict | None:
        if not indices:
            return None
        i = min(indices, key=lambda z: values[z])
        return {"value": fraction_json(values[i]), "key": key_json(keys[i])}

    return {
        "d": d,
        "keys": len(keys),
        "undirected_edges": len(edge_rows),
        "components": components,
        "exact_row_failures": row_failures,
        "stationary_weight_total": total_weight,
        "gap_A_numeric": gap,
        "largest_eigenvalues": [float(x) for x in eig],
        "stationary_eigenvector_residual": eigen_residual,
        "spectral_components": spectral_components,
        "singleton_skeleton": {
            "undirected_edges": len(singleton_edge_rows),
            "components": singleton_components,
            "gap_numeric": singleton_gap,
            "largest_eigenvalues": [float(x) for x in singleton_eig],
            "stationary_eigenvector_residual": singleton_eigen_residual,
        },
        "minimum_all_move_rate": {"value": fraction_json(move_rates[min_move_i]), "key": key_json(keys[min_move_i])},
        "minimum_singleton_split_or_reverse_rate": {
            "value": fraction_json(singleton_rates[min_singleton_i]),
            "key": key_json(keys[min_singleton_i]),
        },
        "minimum_singleton_rate_identity": min_on(identity_indices, singleton_rates),
        "minimum_singleton_rate_nonidentity": min_on(nonidentity_indices, singleton_rates),
        "canonical_edge_formula_failures": canonical_failures,
        "minimum_canonical_edge_rate": None if not canonical_ratios else fraction_json(min(canonical_ratios)),
        "canonical_join_formula_failures": join_failures,
        "minimum_canonical_join_rate": None if not join_ratios else fraction_json(min(join_ratios)),
        "proved_coarse_bound_checked": None if d < 3 else {
            "bound": fraction_json(Fraction(1, 64 * d * d)),
            "all_singleton_rates_meet_bound": all(x >= Fraction(1, 64 * d * d) for x in singleton_rates),
            "all_canonical_rates_meet_bound": all(x >= Fraction(1, 64 * d * d) for x in canonical_ratios),
            "all_join_rates_meet_d_cubed_bound": all(x >= Fraction(1, d**3) for x in join_ratios),
        },
        "threshold_cut_scans": scans,
        "defect_projection": {
            "levels": level_records,
            "unimodal_finite_check": level_unimodal,
            "log_concave_finite_check": level_log_concave,
        },
        "elapsed_seconds": time.time() - started,
    }


def git_commit() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unavailable"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", nargs="+", type=int, default=[2, 3, 4, 5])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if any(d < 2 or d > 5 for d in args.d):
        raise SystemExit("exact audit is restricted to 2<=d<=5")
    payload = {
        "claim_scope": "exact finite combinatorics; numerical spectra are finite diagnostics only",
        "target": "rho(kappa)=|C_kappa|/sum_lambda |C_lambda| on realizable connected-unicycle keys",
        "kernel": "A_d with Q_A(kappa,lambda)=|C_kappa intersect C_lambda|/(2 Z_inc) and unused row mass held",
        "convention": "(p q)(x)=p(q(x)); factors multiply left-to-right",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": __import__("scipy").__version__,
        "seed": None,
        "arguments": vars(args) | {"output": str(args.output)},
        "cases": [run_case(d) for d in args.d],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
