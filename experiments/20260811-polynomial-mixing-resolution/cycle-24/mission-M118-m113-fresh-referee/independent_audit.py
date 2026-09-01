#!/usr/bin/env python3
"""Independent finite and algebraic audit for frozen M113.

This file deliberately imports no predecessor mission code.  It exhausts the
auxiliary connected genus-one word spaces only for d <= 4, constructs the
three projected kernels from their definitions, and separately checks the
Higgs-basis and Hessian claims.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import time
from collections import Counter, defaultdict, deque
from fractions import Fraction
from pathlib import Path

import numpy as np


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return p*q under (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    ans = [0] * len(p)
    for x, y in enumerate(p):
        ans[y] = x
    return tuple(ans)


def transposition_perm(d: int, edge: tuple[int, int]) -> tuple[int, ...]:
    a, b = edge
    p = list(range(d))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def permutation_cycles(p: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
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


def edge_partition(
    d: int, word: tuple[int, ...], edges: tuple[tuple[int, int], ...]
) -> tuple[tuple[int, ...], ...]:
    parent = list(range(d))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    for idx in word:
        union(*edges[idx])
    blocks: dict[int, list[int]] = defaultdict(list)
    for x in range(d):
        blocks[find(x)].append(x)
    return tuple(sorted((tuple(v) for v in blocks.values()), key=lambda z: z[0]))


def eval_word(
    word: tuple[int, ...], trans_perms: tuple[tuple[int, ...], ...]
) -> tuple[int, ...]:
    p = tuple(range(len(trans_perms[0])))
    for idx in word:
        p = compose(p, trans_perms[idx])
    return p


def join_partition(
    partition: tuple[tuple[int, ...], ...], edge: tuple[int, int]
) -> tuple[tuple[int, ...], ...]:
    a, b = edge
    ia = next(i for i, block in enumerate(partition) if a in block)
    ib = next(i for i, block in enumerate(partition) if b in block)
    if ia == ib:
        return partition
    merged = tuple(sorted(partition[ia] + partition[ib]))
    blocks = [block for i, block in enumerate(partition) if i not in (ia, ib)]
    blocks.append(merged)
    return tuple(sorted(blocks, key=lambda z: z[0]))


def is_transposition(p: tuple[int, ...]) -> tuple[int, int] | None:
    moved = [x for x, y in enumerate(p) if x != y]
    if len(moved) == 2 and p[moved[0]] == moved[1] and p[moved[1]] == moved[0]:
        return (moved[0], moved[1])
    return None


def set_partitions(n: int) -> tuple[tuple[tuple[int, ...], ...], ...]:
    if n == 0:
        return ((),)
    ans: list[tuple[tuple[int, ...], ...]] = []

    def rec(i: int, blocks: list[list[int]]) -> None:
        if i == n:
            ans.append(tuple(tuple(block) for block in blocks))
            return
        for k in range(len(blocks)):
            blocks[k].append(i)
            rec(i + 1, blocks)
            blocks[k].pop()
        blocks.append([i])
        rec(i + 1, blocks)
        blocks.pop()

    rec(0, [])
    return tuple(ans)


def atom_partition_to_labels(
    atom_partition: tuple[tuple[int, ...], ...],
    cycles: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    blocks = []
    for atom_block in atom_partition:
        labels = sorted(x for atom in atom_block for x in cycles[atom])
        blocks.append(tuple(labels))
    return tuple(sorted(blocks, key=lambda z: z[0]))


def incidence_connected(
    cycles: tuple[tuple[int, ...], ...],
    ql: tuple[tuple[int, ...], ...],
    qr: tuple[tuple[int, ...], ...],
) -> bool:
    nleft, nright = len(ql), len(qr)
    adj = [[] for _ in range(nleft + nright)]
    for cyc in cycles:
        x = cyc[0]
        li = next(i for i, block in enumerate(ql) if x in block)
        ri = next(i for i, block in enumerate(qr) if x in block)
        adj[li].append(nleft + ri)
        adj[nleft + ri].append(li)
    seen = {0}
    todo = [0]
    while todo:
        u = todo.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                todo.append(v)
    return len(seen) == nleft + nright


def combinatorial_keys(d: int) -> set[tuple]:
    keys: set[tuple] = set()
    for p in itertools.permutations(range(d)):
        p = tuple(p)
        cycles = permutation_cycles(p)
        atom_parts = set_partitions(len(cycles))
        label_parts = [atom_partition_to_labels(part, cycles) for part in atom_parts]
        for ql in label_parts:
            for qr in label_parts:
                if len(cycles) != len(ql) + len(qr):
                    continue
                if not incidence_connected(cycles, ql, qr):
                    continue
                j = d + len(qr) - len(ql)
                if 0 <= j <= 2 * d:
                    keys.add((j, p, ql, qr))
    return keys


def cell_formula(d: int, key: tuple) -> Fraction:
    j, p, ql, qr = key
    cycles = permutation_cycles(p)
    ans = Fraction(math.factorial(j) * math.factorial(2 * d - j), 1)
    for block in ql + qr:
        block_set = set(block)
        c_b = sum(set(cyc) <= block_set for cyc in cycles)
        exponent = c_b - 3
        if exponent >= 0:
            ans *= len(block) ** exponent
        else:
            ans /= len(block) ** (-exponent)
    for cyc in cycles:
        length = len(cyc)
        factor = Fraction(length**length, math.factorial(length - 1))
        ans *= factor * factor
    return ans


def key_compatibility(low: tuple, high: tuple) -> tuple[int, int] | None:
    j, p, ql, qr = low
    j2, p2, ql2, qr2 = high
    if j2 != j + 1:
        return None
    tperm = compose(inverse(p), p2)
    edge = is_transposition(tperm)
    if edge is None:
        return None
    if join_partition(ql, edge) != ql2:
        return None
    if join_partition(qr2, edge) != qr:
        return None
    return edge


def is_singleton_cycle_split(low: tuple, high: tuple) -> bool:
    """A rightward adjacent shift splits one p-cycle into singleton+residual."""
    if high[0] != low[0] + 1 or high[2] != low[2]:
        return False
    source = [frozenset(cyc) for cyc in permutation_cycles(low[1])]
    target = [frozenset(cyc) for cyc in permutation_cycles(high[1])]
    if len(target) != len(source) + 1:
        return False
    for singleton in target:
        if len(singleton) != 1:
            continue
        for residual in target:
            if residual == singleton:
                continue
            merged = singleton | residual
            if merged not in source:
                continue
            source_rest = sorted((x for x in source if x != merged), key=lambda x: tuple(sorted(x)))
            target_rest = sorted((x for x in target if x not in (singleton, residual)), key=lambda x: tuple(sorted(x)))
            if source_rest == target_rest:
                return True
    return False


def reverse_key(key: tuple, d: int) -> tuple:
    j, p, ql, qr = key
    return (2 * d - j, inverse(p), qr, ql)


def is_singleton_split_or_reversal(low: tuple, high: tuple, d: int) -> bool:
    return is_singleton_cycle_split(low, high) or is_singleton_cycle_split(
        reverse_key(high, d), reverse_key(low, d)
    )


def graph_components(n: int, undirected_edges: list[tuple[int, int]]) -> int:
    adj = [[] for _ in range(n)]
    for a, b in undirected_edges:
        adj[a].append(b)
        adj[b].append(a)
    seen: set[int] = set()
    count = 0
    for root in range(n):
        if root in seen:
            continue
        count += 1
        seen.add(root)
        todo = [root]
        while todo:
            u = todo.pop()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    todo.append(v)
    return count


def gap_from_flow(flow: np.ndarray, stationary: np.ndarray) -> tuple[float, list[float]]:
    if len(stationary) == 1:
        return 1.0, [1.0]
    sym = flow / np.sqrt(np.outer(stationary, stationary))
    sym = (sym + sym.T) / 2
    eig = np.linalg.eigvalsh(sym)
    return float(1.0 - eig[-2]), [float(x) for x in eig]


def enumerate_word_audit(d: int, include_full_projection: bool) -> dict:
    start = time.time()
    edges = tuple(itertools.combinations(range(d), 2))
    trans_perms = tuple(transposition_perm(d, edge) for edge in edges)
    identity = tuple(range(d))
    m = 2 * d
    D = 2 * d - 1

    words: list[tuple[int, ...]] = []
    for word in itertools.product(range(len(edges)), repeat=m):
        p = identity
        for edge_idx in word:
            p = compose(p, trans_perms[edge_idx])
        if p != identity:
            continue
        if len(edge_partition(d, word, edges)) == 1:
            words.append(tuple(word))

    word_index = {word: i for i, word in enumerate(words)}
    key_index: dict[tuple, int] = {}
    keys: list[tuple] = []
    cell_count: list[int] = []
    prefixes: list[set[tuple[int, ...]]] = []
    suffixes: list[set[tuple[int, ...]]] = []
    word_key_ids: list[list[int]] = []
    word_key_tuples: list[list[tuple]] = []
    genus_integrality_failures = 0
    central_interval_failures = 0

    for word in words:
        prefix_p = identity
        local_keys: list[tuple] = []
        for j in range(m + 1):
            if j > 0:
                prefix_p = compose(prefix_p, trans_perms[word[j - 1]])
            ql = edge_partition(d, word[:j], edges)
            qr = edge_partition(d, word[j:], edges)
            c = len(permutation_cycles(prefix_p))
            numer_l = j - d - c + 2 * len(ql)
            numer_r = (m - j) - d - c + 2 * len(qr)
            if numer_l % 2 or numer_r % 2:
                genus_integrality_failures += 1
                continue
            if numer_l == 0 and numer_r == 0:
                local_keys.append((j, prefix_p, ql, qr))
        js = [key[0] for key in local_keys]
        if not js or js != list(range(min(js), max(js) + 1)):
            central_interval_failures += 1
        ids = []
        for key in local_keys:
            if key not in key_index:
                key_index[key] = len(keys)
                keys.append(key)
                cell_count.append(0)
                prefixes.append(set())
                suffixes.append(set())
            kid = key_index[key]
            ids.append(kid)
            j = key[0]
            cell_count[kid] += 1
            prefixes[kid].add(word[:j])
            suffixes[kid].add(word[j:])
        word_key_ids.append(ids)
        word_key_tuples.append(local_keys)

    nwords = len(words)
    nkeys = len(keys)
    ell_hist = Counter(len(ids) for ids in word_key_ids)
    Z_inc = sum(len(ids) for ids in word_key_ids)

    combin_keys = combinatorial_keys(d)
    observed_keys = set(keys)
    formula_failures = []
    cartesian_failures = []
    for kid, key in enumerate(keys):
        value = cell_formula(d, key)
        if value.denominator != 1 or value.numerator != cell_count[kid]:
            formula_failures.append((kid, str(value), cell_count[kid]))
        if len(prefixes[kid]) * len(suffixes[kid]) != cell_count[kid]:
            cartesian_failures.append(
                (kid, len(prefixes[kid]), len(suffixes[kid]), cell_count[kid])
            )

    adjacent_counts: Counter[tuple[int, int]] = Counter()
    for ids in word_key_ids:
        for a, b in zip(ids, ids[1:]):
            if keys[b][0] != keys[a][0] + 1:
                central_interval_failures += 1
            adjacent_counts[(a, b)] += 1

    compatible: dict[tuple[int, int], tuple[int, int]] = {}
    overlap_failures = []
    move_type_failures = []
    keys_by_j: dict[int, list[int]] = defaultdict(list)
    for kid, key in enumerate(keys):
        keys_by_j[key[0]].append(kid)
    for j, lows in keys_by_j.items():
        for a in lows:
            for b in keys_by_j.get(j + 1, []):
                edge = key_compatibility(keys[a], keys[b])
                if edge is None:
                    continue
                compatible[(a, b)] = edge
                expected = len(prefixes[a]) * len(suffixes[b])
                observed = adjacent_counts.get((a, b), 0)
                if observed != expected:
                    overlap_failures.append((a, b, observed, expected))
                ca = len(permutation_cycles(keys[a][1]))
                cb = len(permutation_cycles(keys[b][1]))
                qla, qra = keys[a][2], keys[a][3]
                qlb, qrb = keys[b][2], keys[b][3]
                join_ok = (
                    cb == ca - 1
                    and len(qlb) == len(qla) - 1
                    and qrb == qra
                )
                split_ok = (
                    cb == ca + 1
                    and qlb == qla
                    and len(qrb) == len(qra) + 1
                )
                if not (join_ok or split_ok):
                    move_type_failures.append((a, b, ca, cb))
    for pair, observed in adjacent_counts.items():
        if pair not in compatible:
            overlap_failures.append((pair[0], pair[1], observed, "incompatible"))

    undirected_edges = list(compatible)
    component_count = graph_components(nkeys, undirected_edges)

    bar_pi = np.zeros(nkeys)
    qg = np.zeros((nkeys, nkeys))
    for ids in word_key_ids:
        ell = len(ids)
        for a in ids:
            bar_pi[a] += 1.0 / (nwords * ell)
        amount = 1.0 / (nwords * ell * ell)
        for a in ids:
            for b in ids:
                qg[a, b] += amount

    rho = np.array(cell_count, dtype=float) / Z_inc
    qa = np.zeros((nkeys, nkeys))
    for (a, b), count in adjacent_counts.items():
        amount = count / (2.0 * Z_inc)
        qa[a, b] += amount
        qa[b, a] += amount
    for a in range(nkeys):
        qa[a, a] = rho[a] - float(np.sum(qa[a]))

    singleton_split_rates = np.zeros(nkeys)
    for (a, b), edge in compatible.items():
        if not is_singleton_split_or_reversal(keys[a], keys[b], d):
            continue
        singleton_split_rates[a] += qa[a, b] / rho[a]
        singleton_split_rates[b] += qa[b, a] / rho[b]

    qbar = None
    beta_gap = None
    beta_eig = None
    proposal_target_failures = 0
    qbar_symmetry_residual = None
    qbar_row_residual = None
    if include_full_projection:
        conjugate = [[0] * len(edges) for _ in edges]
        edge_to_idx = {edge: i for i, edge in enumerate(edges)}
        for b_idx, b_perm in enumerate(trans_perms):
            for a_idx, a_edge in enumerate(edges):
                mapped = tuple(sorted((b_perm[a_edge[0]], b_perm[a_edge[1]])))
                conjugate[b_idx][a_idx] = edge_to_idx[mapped]
        qbar = 0.5 * qg
        for wid, word in enumerate(words):
            source_ids = word_key_ids[wid]
            ell_source = len(source_ids)
            targets: Counter[int] = Counter()
            for i in range(D):
                a, b = word[i], word[i + 1]
                right = word[:i] + (b, conjugate[b][a]) + word[i + 2 :]
                left = word[:i] + (conjugate[a][b], a) + word[i + 2 :]
                for target_word in (right, left):
                    target_id = word_index.get(target_word)
                    if target_id is None:
                        proposal_target_failures += 1
                    else:
                        targets[target_id] += 1
            for target_id, multiplicity in targets.items():
                target_ids = word_key_ids[target_id]
                amount = multiplicity / (
                    nwords * ell_source * 4.0 * D * len(target_ids)
                )
                for a in source_ids:
                    for b in target_ids:
                        qbar[a, b] += amount
        qbar_symmetry_residual = float(np.max(np.abs(qbar - qbar.T)))
        qbar_row_residual = float(np.max(np.abs(np.sum(qbar, axis=1) - bar_pi)))
        beta_gap, beta_eig = gap_from_flow(qbar, bar_pi)

    gap_g, eig_g = gap_from_flow(qg, bar_pi)
    gap_a, eig_a = gap_from_flow(qa, rho)

    qg_symmetry_residual = float(np.max(np.abs(qg - qg.T)))
    qa_symmetry_residual = float(np.max(np.abs(qa - qa.T)))
    qg_row_residual = float(np.max(np.abs(np.sum(qg, axis=1) - bar_pi)))
    qa_row_residual = float(np.max(np.abs(np.sum(qa, axis=1) - rho)))
    measure_ratio = bar_pi / rho
    flow_ratios = []
    for a, b in adjacent_counts:
        if qa[a, b] > 0:
            flow_ratios.append(qg[a, b] / qa[a, b])

    rho_j = defaultdict(float)
    rho_cycle_type = defaultdict(float)
    for kid, key in enumerate(keys):
        rho_j[str(key[0])] += float(rho[kid])
        lengths = sorted((len(c) for c in permutation_cycles(key[1])), reverse=True)
        rho_cycle_type[",".join(map(str, lengths))] += float(rho[kid])

    return {
        "d": d,
        "candidate_words": len(edges) ** m,
        "states": nwords,
        "lifted_incidences": Z_inc,
        "keys": nkeys,
        "ell_histogram": {str(k): v for k, v in sorted(ell_hist.items())},
        "central_interval_failures": central_interval_failures,
        "genus_integrality_failures": genus_integrality_failures,
        "combinatorial_key_count": len(combin_keys),
        "missing_observed_keys": len(combin_keys - observed_keys),
        "extra_observed_keys": len(observed_keys - combin_keys),
        "cell_formula_failures": formula_failures[:20],
        "cartesian_cell_failures": cartesian_failures[:20],
        "compatible_adjacent_pairs": len(compatible),
        "observed_adjacent_pairs": len(adjacent_counts),
        "overlap_failures": overlap_failures[:20],
        "move_type_failures": move_type_failures[:20],
        "key_graph_components": component_count,
        "gap_A": gap_a,
        "gap_G": gap_g,
        "gap_beta": beta_gap,
        "comparison_lower_bound_G": 2.0 * gap_a / (D**3),
        "comparison_lower_bound_beta": gap_a / (D**3),
        "beta_vs_half_G_margin": None if beta_gap is None else beta_gap - gap_g / 2,
        "stationary_measure_ratio_min": float(np.min(measure_ratio)),
        "stationary_measure_ratio_max": float(np.max(measure_ratio)),
        "G_to_A_flow_ratio_min": min(flow_ratios) if flow_ratios else None,
        "required_G_to_A_flow_ratio": 2.0 / (D**2),
        "A_min_diagonal": float(np.min(np.diag(qa))),
        "singleton_split_or_reverse_rate_min": float(np.min(singleton_split_rates)),
        "singleton_split_or_reverse_zero_keys": int(np.sum(singleton_split_rates == 0)),
        "G_min_diagonal": float(np.min(np.diag(qg) / bar_pi)),
        "proposal_target_failures": proposal_target_failures,
        "residuals": {
            "A_symmetry": qa_symmetry_residual,
            "A_rows": qa_row_residual,
            "G_symmetry": qg_symmetry_residual,
            "G_rows": qg_row_residual,
            "beta_symmetry": qbar_symmetry_residual,
            "beta_rows": qbar_row_residual,
        },
        "rho_by_j": dict(sorted(rho_j.items(), key=lambda item: int(item[0]))),
        "rho_by_cycle_type": dict(sorted(rho_cycle_type.items())),
        "second_eigenvalues": {
            "A": None if len(eig_a) == 1 else eig_a[-2],
            "G": None if len(eig_g) == 1 else eig_g[-2],
            "beta": None if beta_eig is None or len(beta_eig) == 1 else beta_eig[-2],
        },
        "elapsed_seconds": time.time() - start,
    }


def forest_components(c: int, edge_set: tuple[tuple[str, int, int], ...], color: str):
    parent = list(range(c))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> bool:
        a, b = find(a), find(b)
        if a == b:
            return False
        parent[b] = a
        return True

    acyclic = True
    for col, a, b in edge_set:
        if col == color and not union(a, b):
            acyclic = False
    blocks: dict[int, list[int]] = defaultdict(list)
    for x in range(c):
        blocks[find(x)].append(x)
    part = tuple(sorted((tuple(v) for v in blocks.values()), key=lambda z: z[0]))
    return acyclic, part


def uncolored_connected(c: int, edge_set: tuple[tuple[str, int, int], ...]) -> bool:
    adj = [[] for _ in range(c)]
    for _, a, b in edge_set:
        adj[a].append(b)
        adj[b].append(a)
    seen = {0}
    todo = [0]
    while todo:
        u = todo.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                todo.append(v)
    return len(seen) == c


def higgs_basis_audit(max_c: int) -> dict:
    out = {}
    for c in range(2, max_c + 1):
        ground = tuple(
            (color, a, b)
            for color in ("r", "b")
            for a, b in itertools.combinations(range(c), 2)
        )
        bases = 0
        incidence_failures = 0
        key_multiplicity: Counter[tuple] = Counter()
        for chosen in itertools.combinations(ground, c):
            red_forest, ql = forest_components(c, chosen, "r")
            blue_forest, qr = forest_components(c, chosen, "b")
            if not (red_forest and blue_forest and uncolored_connected(c, chosen)):
                continue
            bases += 1
            cycles = tuple((x,) for x in range(c))
            if len(ql) + len(qr) != c or not incidence_connected(cycles, ql, qr):
                incidence_failures += 1
            key_multiplicity[(ql, qr)] += 1
        out[str(c)] = {
            "ground_size": len(ground),
            "rank_c_subsets": math.comb(len(ground), c),
            "higgs_bases": bases,
            "incidence_failures": incidence_failures,
            "incidence_keys": len(key_multiplicity),
        }
    return out


def determinant_fraction(matrix: list[list[Fraction]]) -> Fraction:
    a = [row[:] for row in matrix]
    det = Fraction(1)
    n = len(a)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det *= -1
        pivot_value = a[col][col]
        det *= pivot_value
        for j in range(col, n):
            a[col][j] /= pivot_value
        for r in range(col + 1, n):
            factor = a[r][col]
            if factor:
                for j in range(col, n):
                    a[r][j] -= factor * a[col][j]
    return det


def basis_coefficient(
    c: int,
    edge_set: tuple[tuple[str, int, int], ...],
    factorial_tilt: bool,
) -> Fraction:
    red_forest, ql = forest_components(c, edge_set, "r")
    blue_forest, qr = forest_components(c, edge_set, "b")
    if not (red_forest and blue_forest and uncolored_connected(c, edge_set)):
        return Fraction(0)
    denominator = math.prod(len(block) for block in ql + qr)
    if not factorial_tilt:
        return Fraction(1, denominator)
    r = sum(edge[0] == "r" for edge in edge_set)
    return Fraction(math.factorial(2 * r) * math.factorial(2 * c - 2 * r), denominator)


def lorentzian_audit() -> dict:
    fixed = (("r", 0, 1), ("r", 0, 2))
    variables = (("r", 0, 3), ("b", 0, 1), ("b", 0, 2), ("b", 1, 3))
    outputs = {}
    for name, factorial_tilt in (("weighted", True), ("untilted", False)):
        matrix = [[Fraction(0) for _ in variables] for _ in variables]
        for i in range(len(variables)):
            for j in range(i + 1, len(variables)):
                coeff = basis_coefficient(4, fixed + (variables[i], variables[j]), factorial_tilt)
                matrix[i][j] = matrix[j][i] = coeff
        det = determinant_fraction(matrix)
        numeric = np.array([[float(x) for x in row] for row in matrix])
        eig = np.linalg.eigvalsh(numeric)
        outputs[name] = {
            "matrix": [[str(x) for x in row] for row in matrix],
            "determinant": str(det),
            "trace": str(sum(matrix[i][i] for i in range(4))),
            "inertia_numeric": {
                "positive": int(np.sum(eig > 1e-10)),
                "negative": int(np.sum(eig < -1e-10)),
                "zero": int(np.sum(np.abs(eig) <= 1e-10)),
            },
            "eigenvalues": [float(x) for x in eig],
        }
    return outputs


def balanced_split_audit(max_even_d: int) -> dict:
    rows = []
    failures = 0
    for d in range(6, max_even_d + 1, 2):
        a = d // 2
        raw = Fraction(a ** (a - 3) * a ** (a - 3), 8 * (2 * d - 3) * d ** (d - 4))
        simplified = Fraction(1, 2 ** (d - 3) * (2 * d - 3) * d * d)
        multiplicity = math.comb(d - 2, a - 1)
        aggregate = multiplicity * raw
        lower = Fraction(2, (d - 1) * (2 * d - 3) * d * d)
        if raw != simplified or aggregate < lower:
            failures += 1
        rows.append(
            {
                "d": d,
                "point_probability": str(raw),
                "multiplicity": multiplicity,
                "aggregate_probability": str(aggregate),
                "claimed_lower_bound": str(lower),
                "aggregate_to_bound_ratio": float(aggregate / lower),
            }
        )
    return {"failures": failures, "rows": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", nargs="+", type=int, default=[2, 3, 4])
    parser.add_argument("--max-higgs-c", type=int, default=4)
    parser.add_argument("--max-balanced-d", type=int, default=30)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    total_start = time.time()
    finite = []
    for d in args.d:
        finite.append(enumerate_word_audit(d, include_full_projection=True))
    result = {
        "metadata": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "seed": None,
            "command_scope": {"d": args.d},
        },
        "finite": finite,
        "higgs": higgs_basis_audit(args.max_higgs_c),
        "lorentzian": lorentzian_audit(),
        "balanced_split": balanced_split_audit(args.max_balanced_d),
        "total_elapsed_seconds": time.time() - total_start,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
