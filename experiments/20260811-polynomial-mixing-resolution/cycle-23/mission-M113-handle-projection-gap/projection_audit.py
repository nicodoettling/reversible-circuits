#!/usr/bin/env python3
"""Exact finite falsification audit for the M113 handle-cell projection.

This exhausts only d <= 4.  It computes the word--central-key incidence Gibbs
chain extracted from the holding half of the M97 lift and, optionally, the
full stationary-flow projection.  Numerical spectra are finite diagnostics,
not asymptotic evidence.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import subprocess
import time
from collections import Counter, defaultdict, deque
from fractions import Fraction
from pathlib import Path

import numpy as np


def compose(p, q):
    """Return p q under (p q)(x) = p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def transpositions(d):
    return tuple((a, b) for a in range(d) for b in range(a + 1, d))


def edge_perm(d, edge):
    a, b = edge
    p = list(range(d))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def eval_word(d, word, edge_perms):
    p = tuple(range(d))
    for e in word:
        p = compose(p, edge_perms[e])
    return p


def cycle_blocks(p):
    seen = set()
    blocks = []
    for x in range(len(p)):
        if x in seen:
            continue
        block = []
        y = x
        while y not in seen:
            seen.add(y)
            block.append(y)
            y = p[y]
        blocks.append(tuple(sorted(block)))
    return tuple(sorted(blocks))


def cycle_count(p):
    return len(cycle_blocks(p))


def cycle_type(p):
    return tuple(sorted((len(block) for block in cycle_blocks(p)),
                        reverse=True))


def is_singleton_cycle_split(source_key, target_key):
    """Whether moving the cut right splits off a singleton p'-cycle."""
    j, p, ql, qr = source_key
    jp, pp, qlp, qrp = target_key
    if jp != j + 1 or qlp != ql:
        return False
    source_cycles = cycle_blocks(p)
    target_cycles = cycle_blocks(pp)
    if len(target_cycles) != len(source_cycles) + 1:
        return False
    source_sets = [set(x) for x in source_cycles]
    target_sets = [set(x) for x in target_cycles]
    for singleton in target_sets:
        if len(singleton) != 1:
            continue
        residual = None
        for block in target_sets:
            if block is not singleton and any(singleton | block == old
                                              for old in source_sets):
                residual = block
                break
        if residual is None:
            continue
        remaining_target = target_sets.copy()
        remaining_target.remove(singleton)
        remaining_target.remove(residual)
        merged = singleton | residual
        remaining_source = source_sets.copy()
        remaining_source.remove(merged)
        if sorted(map(sorted, remaining_target)) == sorted(map(sorted, remaining_source)):
            return True
    return False


def reverse_key(key, d):
    j, p, ql, qr = key
    inverse = [0] * d
    for x, y in enumerate(p):
        inverse[y] = x
    return (2 * d - j, tuple(inverse), qr, ql)


def is_singleton_split_either_cut_direction(source_key, target_key, d):
    return (
        is_singleton_cycle_split(source_key, target_key)
        or is_singleton_cycle_split(target_key, source_key)
        or is_singleton_cycle_split(reverse_key(source_key, d),
                                    reverse_key(target_key, d))
        or is_singleton_cycle_split(reverse_key(target_key, d),
                                    reverse_key(source_key, d))
    )


def support_partition(d, word, edges):
    parent = list(range(d))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    for e in word:
        union(*edges[e])
    blocks = defaultdict(list)
    for x in range(d):
        blocks[find(x)].append(x)
    return tuple(sorted(tuple(block) for block in blocks.values()))


def genus(d, word, edges, edge_perms):
    p = eval_word(d, word, edge_perms)
    q = len(support_partition(d, word, edges))
    numerator = len(word) - d - cycle_count(p) + 2 * q
    assert numerator % 2 == 0
    return numerator // 2


def central_cuts(d, word, edges, edge_perms):
    return tuple(
        j
        for j in range(1, 2 * d)
        if genus(d, word[:j], edges, edge_perms) == 0
        and genus(d, word[j:], edges, edge_perms) == 0
    )


def seam_key(d, word, j, edges, edge_perms):
    return (
        j,
        eval_word(d, word[:j], edge_perms),
        support_partition(d, word[:j], edges),
        support_partition(d, word[j:], edges),
    )


def conjugate_edge(e, by, edges, edge_to_index):
    a, b = edges[e]
    x, y = edges[by]

    def t(z):
        if z == x:
            return y
        if z == y:
            return x
        return z

    return edge_to_index[tuple(sorted((t(a), t(b))))]


def signed_move(word, i, orientation, edges, edge_to_index):
    a, b = word[i], word[i + 1]
    out = list(word)
    if orientation == 1:
        out[i:i + 2] = (b, conjugate_edge(a, b, edges, edge_to_index))
    else:
        out[i:i + 2] = (conjugate_edge(b, a, edges, edge_to_index), a)
    return tuple(out)


def components_from_flow(flow, tolerance=1e-15):
    n = flow.shape[0]
    unseen = set(range(n))
    sizes = []
    while unseen:
        root = unseen.pop()
        todo = [root]
        size = 0
        while todo:
            x = todo.pop()
            size += 1
            nbrs = np.flatnonzero(flow[x] > tolerance)
            for y in nbrs:
                y = int(y)
                if y != x and y in unseen:
                    unseen.remove(y)
                    todo.append(y)
        sizes.append(size)
    return sorted(sizes, reverse=True)


def spectrum_from_flow(flow, mass):
    sym = flow / np.sqrt(np.outer(mass, mass))
    residual = float(np.max(np.abs(sym - sym.T)))
    eig = np.linalg.eigvalsh((sym + sym.T) / 2.0)
    eig.sort()
    one_mult = int(np.sum(np.abs(eig - 1.0) <= 1e-9))
    gap = 0.0 if one_mult > 1 else float(1.0 - eig[-2]) if len(eig) > 1 else 1.0
    return {
        "gap": gap,
        "lambda_min": float(eig[0]),
        "lambda_second": float(eig[-2]) if len(eig) > 1 else None,
        "lambda_max": float(eig[-1]),
        "one_multiplicity": one_mult,
        "symmetry_residual": residual,
    }


def json_key(key):
    j, p, ql, qr = key
    return {"j": j, "p": list(p), "Q_L": [list(x) for x in ql],
            "Q_R": [list(x) for x in qr]}


def exact_cell_count(key, d):
    """Classical genus-zero Hurwitz formula after side interleaving."""
    j, p, ql, qr = key
    cycles = cycle_blocks(p)
    answer = Fraction(math.factorial(j) * math.factorial(2 * d - j), 1)
    for partition in (ql, qr):
        for block in partition:
            block_set = set(block)
            c_block = sum(set(cycle) <= block_set for cycle in cycles)
            answer *= Fraction(len(block), 1) ** (c_block - 3)
    for cycle in cycles:
        a = len(cycle)
        atom = Fraction(a ** a, math.factorial(a - 1))
        answer *= atom * atom
    if answer.denominator != 1:
        raise AssertionError("Hurwitz cell formula must be integral")
    return answer.numerator


def run_case(d, full_projection):
    started = time.time()
    edges = transpositions(d)
    edge_to_index = {e: i for i, e in enumerate(edges)}
    edge_perms = tuple(edge_perm(d, e) for e in edges)
    ident = tuple(range(d))

    states = {}
    key_to_index = {}
    key_words = defaultdict(list)
    key_left = defaultdict(set)
    key_right = defaultdict(set)
    ell_histogram = Counter()
    for word in itertools.product(range(len(edges)), repeat=2 * d):
        if eval_word(d, word, edge_perms) != ident:
            continue
        if len(support_partition(d, word, edges)) != 1:
            continue
        cuts = central_cuts(d, word, edges, edge_perms)
        assert cuts
        keys = []
        for j in cuts:
            key = seam_key(d, word, j, edges, edge_perms)
            if key not in key_to_index:
                key_to_index[key] = len(key_to_index)
            idx = key_to_index[key]
            keys.append(idx)
            key_words[idx].append(word)
            key_left[idx].add(word[:j])
            key_right[idx].add(word[j:])
        states[word] = (cuts, tuple(keys))
        ell_histogram[len(cuts)] += 1

    nkeys = len(key_to_index)
    mass = np.zeros(nkeys, dtype=float)
    cut_flow = np.zeros((nkeys, nkeys), dtype=float)
    key_word_count = np.zeros(nkeys, dtype=int)
    for word, (cuts, keys) in states.items():
        ell = len(cuts)
        for k in keys:
            mass[k] += 1.0 / ell
            key_word_count[k] += 1
        contribution = 1.0 / (ell * ell)
        for k in keys:
            for l in keys:
                cut_flow[k, l] += contribution

    cut_row_residual = float(np.max(np.abs(cut_flow.sum(axis=1) - mass)))
    cut_components = components_from_flow(cut_flow)
    cut_spectrum = spectrum_from_flow(cut_flow, mass)

    inverse_keys = [None] * nkeys
    for key, idx in key_to_index.items():
        inverse_keys[idx] = key
    cell_formula_failures = []
    for i, key in enumerate(inverse_keys):
        expected = exact_cell_count(key, d)
        if expected != key_word_count[i]:
            cell_formula_failures.append({
                "key": json_key(key), "expected": expected,
                "observed": int(key_word_count[i]),
            })

    # Local raw-incidence chain.  From a key, sample a raw-uniform word in
    # its cell and attempt one of the two adjacent cut shifts.  A compatible
    # pair gets stationary flow |C_k intersect C_l|/(2 Z_inc).
    incidence_total = int(sum(len(keys) for _, keys in states.values()))
    raw_mass_count = np.array(
        [len(key_words[i]) for i in range(nkeys)], dtype=float)
    adjacent_count = np.zeros((nkeys, nkeys), dtype=float)
    for word, (cuts, keys) in states.items():
        for a in range(len(cuts) - 1):
            if cuts[a + 1] != cuts[a] + 1:
                raise AssertionError("central cuts must form an interval")
            k, l = keys[a], keys[a + 1]
            adjacent_count[k, l] += 1.0
            adjacent_count[l, k] += 1.0
    overlap_formula_failures = 0
    for k in range(nkeys):
        jk = inverse_keys[k][0]
        for l in np.flatnonzero(adjacent_count[k] > 0):
            l = int(l)
            jl = inverse_keys[l][0]
            if jl == jk + 1:
                expected = len(key_left[k]) * len(key_right[l])
                if int(adjacent_count[k, l]) != expected:
                    overlap_formula_failures += 1
            elif jk != jl + 1:
                overlap_formula_failures += 1
    raw_mass = raw_mass_count / incidence_total
    adjacent_flow = adjacent_count / (2.0 * incidence_total)
    for k in range(nkeys):
        adjacent_flow[k, k] = raw_mass[k] - float(adjacent_flow[k].sum())
        if adjacent_flow[k, k] < -1e-12:
            raise AssertionError("adjacent chain has negative holding mass")
        adjacent_flow[k, k] = max(adjacent_flow[k, k], 0.0)
    adjacent_positive = adjacent_count[adjacent_count > 0]
    adjacent_spectrum = spectrum_from_flow(adjacent_flow, raw_mass)
    singleton_split_probability = np.zeros(nkeys, dtype=float)
    all_adjacent_probability = np.zeros(nkeys, dtype=float)
    for k in range(nkeys):
        for l in np.flatnonzero(adjacent_count[k] > 0):
            l = int(l)
            all_adjacent_probability[k] += adjacent_flow[k, l] / raw_mass[k]
            if is_singleton_split_either_cut_direction(
                    inverse_keys[k], inverse_keys[l], d):
                singleton_split_probability[k] += adjacent_flow[k, l] / raw_mass[k]
    positive_singleton = singleton_split_probability[
        singleton_split_probability > 1e-15]
    raw_mass_by_j = defaultdict(Fraction)
    raw_mass_by_cycle_type = defaultdict(Fraction)
    raw_mass_by_j_cycle_type = defaultdict(Fraction)
    for i, key in enumerate(inverse_keys):
        j, p, _, _ = key
        weight = Fraction(int(raw_mass_count[i]), incidence_total)
        ctype = cycle_type(p)
        raw_mass_by_j[j] += weight
        raw_mass_by_cycle_type[ctype] += weight
        raw_mass_by_j_cycle_type[(j, ctype)] += weight

    def fraction_record(value):
        return {"numerator": value.numerator,
                "denominator": value.denominator, "float": float(value)}

    full_result = None
    if full_projection:
        D = 2 * d - 1
        full_flow = 0.5 * cut_flow
        proposal_scale = 1.0 / (4.0 * D)
        missing_targets = 0
        for word, (cuts, keys) in states.items():
            ell = len(cuts)
            for i in range(D):
                for orientation in (-1, 1):
                    target = signed_move(word, i, orientation, edges,
                                         edge_to_index)
                    target_record = states.get(target)
                    if target_record is None:
                        missing_targets += 1
                        continue
                    tcuts, tkeys = target_record
                    tell = len(tcuts)
                    contribution = proposal_scale / (ell * tell)
                    for k in keys:
                        for l in tkeys:
                            full_flow[k, l] += contribution
        full_row_residual = float(np.max(np.abs(full_flow.sum(axis=1) - mass)))
        full_result = {
            "components": components_from_flow(full_flow),
            "spectrum": spectrum_from_flow(full_flow, mass),
            "row_mass_residual": full_row_residual,
            "reversibility_residual": float(np.max(np.abs(full_flow-full_flow.T))),
            "missing_move_targets": missing_targets,
        }

    singleton_keys = [i for i in range(nkeys) if key_word_count[i] == 1]
    zero_offdiag_keys = [
        i for i in range(nkeys)
        if float(cut_flow[i].sum() - cut_flow[i, i]) <= 1e-15
    ]
    degree_histogram = Counter()
    for i in range(nkeys):
        degree_histogram[int(np.sum(cut_flow[i] > 1e-15) - 1)] += 1

    return {
        "d": d,
        "candidate_words": len(edges) ** (2 * d),
        "connected_genus_one_words": len(states),
        "central_key_count": nkeys,
        "ell_histogram": dict(sorted(ell_histogram.items())),
        "hurwitz_cell_formula_failures": cell_formula_failures,
        "cut_refresh": {
            "components": cut_components,
            "spectrum": cut_spectrum,
            "row_mass_residual": cut_row_residual,
            "reversibility_residual": float(np.max(np.abs(cut_flow-cut_flow.T))),
            "key_word_count_min": int(key_word_count.min()),
            "key_word_count_max": int(key_word_count.max()),
            "singleton_key_count": len(singleton_keys),
            "zero_offdiagonal_key_count": len(zero_offdiag_keys),
            "degree_histogram": dict(sorted(degree_histogram.items())),
            "first_zero_offdiagonal_key": (
                json_key(inverse_keys[zero_offdiag_keys[0]])
                if zero_offdiag_keys else None
            ),
        },
        "adjacent_raw_incidence": {
            "components": components_from_flow(adjacent_flow),
            "spectrum": adjacent_spectrum,
            "row_mass_residual": float(
                np.max(np.abs(adjacent_flow.sum(axis=1) - raw_mass))),
            "reversibility_residual": float(
                np.max(np.abs(adjacent_flow-adjacent_flow.T))),
            "incidence_total": incidence_total,
            "directed_compatible_pair_count": int(
                np.sum(adjacent_count > 0)),
            "minimum_positive_overlap": int(adjacent_positive.min())
                if adjacent_positive.size else None,
            "maximum_overlap": int(adjacent_positive.max())
                if adjacent_positive.size else None,
            "overlap_product_formula_failures": overlap_formula_failures,
            "all_adjacent_move_probability": {
                "minimum": float(all_adjacent_probability.min()),
                "maximum": float(all_adjacent_probability.max()),
                "argmin_key": json_key(inverse_keys[int(
                    np.argmin(all_adjacent_probability))]),
            },
            "singleton_split_or_reverse": {
                "zero_rate_key_count": int(np.sum(
                    singleton_split_probability <= 1e-15)),
                "minimum_positive_probability": (
                    float(positive_singleton.min())
                    if positive_singleton.size else None),
                "maximum_probability": float(
                    singleton_split_probability.max()),
                "first_zero_rate_key": (
                    json_key(inverse_keys[int(np.flatnonzero(
                        singleton_split_probability <= 1e-15)[0])])
                    if np.any(singleton_split_probability <= 1e-15)
                    else None),
            },
            "mass_by_j": {
                str(j): fraction_record(value)
                for j, value in sorted(raw_mass_by_j.items())
            },
            "mass_by_cycle_type": {
                ",".join(map(str, ctype)): fraction_record(value)
                for ctype, value in sorted(raw_mass_by_cycle_type.items(),
                                           reverse=True)
            },
            "mass_by_j_and_cycle_type": [
                {"j": j, "cycle_type": list(ctype),
                 "mass": fraction_record(value)}
                for (j, ctype), value in sorted(
                    raw_mass_by_j_cycle_type.items())
            ],
            "beta_lower_bound_from_comparison": (
                adjacent_spectrum["gap"] / ((2 * d - 1) ** 3)
            ),
        },
        "full_projection": full_result,
        "elapsed_seconds": time.time() - started,
    }


def git_commit():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unavailable"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", nargs="+", type=int, default=[2, 3, 4])
    parser.add_argument("--skip-full-projection", action="store_true")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    if any(d < 2 or d > 4 for d in args.d):
        raise SystemExit("this falsification audit is restricted to 2 <= d <= 4")
    payload = {
        "claim_scope": "exact finite diagnostics only; no asymptotic inference",
        "target": "uniform connected-support identity words of length 2d",
        "convention": "(p q)(x)=p(q(x)); word factors multiply left-to-right",
        "kernel": "M97 half-lazy signed adjacent-Hurwitz lift and M104 cell projection",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "seed": None,
        "arguments": vars(args),
        "cases": [run_case(d, not args.skip_full_projection) for d in args.d],
    }
    output = Path(args.output)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
