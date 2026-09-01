#!/usr/bin/env python3
"""Exact finite falsification audit for the frozen M02 projection formulas.

Composition is p after q: compose(p, q)[x] = p[q[x]].  All arithmetic used
for Markov probabilities is exact.  The run is deterministic and uses only
the Python standard library.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
from collections import Counter, defaultdict, deque
from fractions import Fraction
from pathlib import Path


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[x]] for x in range(len(p)))


def transpositions(n: int) -> list[tuple[int, ...]]:
    out = []
    for a in range(n):
        for b in range(a + 1, n):
            p = list(range(n))
            p[a], p[b] = p[b], p[a]
            out.append(tuple(p))
    return out


def endpoints(t: tuple[int, ...]) -> tuple[int, int]:
    moved = [x for x, y in enumerate(t) if x != y]
    assert len(moved) == 2
    return moved[0], moved[1]


def product(word: tuple[tuple[int, ...], ...], identity: tuple[int, ...]) -> tuple[int, ...]:
    g = identity
    for t in word:
        g = compose(g, t)
    return g


def macro(word: tuple[tuple[int, ...], ...]) -> tuple[tuple[tuple[int, ...], int], ...]:
    """Labeled nontrivial support components with word-position weights."""
    adjacency: dict[int, set[int]] = defaultdict(set)
    edge_list = []
    for t in word:
        a, b = endpoints(t)
        adjacency[a].add(b)
        adjacency[b].add(a)
        edge_list.append((a, b))
    unseen = set(adjacency)
    blocks = []
    while unseen:
        root = min(unseen)
        todo = [root]
        vertices = set()
        while todo:
            x = todo.pop()
            if x in vertices:
                continue
            vertices.add(x)
            todo.extend(adjacency[x] - vertices)
        unseen -= vertices
        weight = sum(a in vertices for a, _ in edge_list)
        blocks.append((tuple(sorted(vertices)), weight))
    return tuple(sorted(blocks))


def enumerate_identity_words(n: int, length: int):
    identity = tuple(range(n))
    trans = transpositions(n)
    words = [w for w in itertools.product(trans, repeat=length) if product(w, identity) == identity]
    return trans, words


def connected_identity_count(v: int, k: int) -> int:
    trans, words = enumerate_identity_words(v, k)
    wanted = tuple(range(v))
    del trans
    return sum(len(macro(w)) == 1 and macro(w)[0][0] == wanted for w in words)


def predicted_weight(alpha, m: int, connected_counts: dict[tuple[int, int], int]) -> int:
    numerator = math.factorial(m)
    for vertices, weight in alpha:
        numerator *= connected_counts[(len(vertices), weight)]
        numerator //= math.factorial(weight)
    return numerator


def fibers_by_product(n: int, max_r: int):
    identity = tuple(range(n))
    trans = transpositions(n)
    all_fibers = {}
    for r in range(3, max_r + 1):
        fibers = defaultdict(list)
        for block in itertools.product(trans, repeat=r):
            fibers[product(block, identity)].append(block)
        all_fibers[r] = dict(fibers)
    return all_fibers


def direct_projection_k(n: int, m: int, words, fibers, weights):
    rset = [r for r in (3, 4, 5) if r <= m]
    accum = defaultdict(Fraction)
    for w in words:
        a = macro(w)
        accum[(a, a)] += Fraction(1, 2)
        for r in rset:
            selection = Fraction(1, 2 * len(rset) * (m - r + 1))
            for i in range(m - r + 1):
                key = product(w[i : i + r], tuple(range(n)))
                candidates = fibers[r][key]
                target_counts = Counter(macro(w[:i] + block + w[i + r :]) for block in candidates)
                for b, count in target_counts.items():
                    accum[(a, b)] += selection * Fraction(count, len(candidates))
    projection = {(a, b): value / weights[a] for (a, b), value in accum.items()}
    return projection


def direct_projection_square(trans, words, weights):
    mcount = len(trans)
    accum = defaultdict(Fraction)
    for w in words:
        a = macro(w)
        if w[0] != w[1]:
            accum[(a, a)] += 1
        else:
            target_counts = Counter(macro((s, s) + w[2:]) for s in trans)
            for b, count in target_counts.items():
                accum[(a, b)] += Fraction(count, mcount)
    return {(a, b): value / weights[a] for (a, b), value in accum.items()}


def rational_rank(matrix):
    """Exact rank over Q for an integer/Fraction matrix."""
    if not matrix:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and a[r][col]:
                scale = a[r][col]
                a[r] = [x - scale * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def common_core_square_formula(n: int, m: int, trans, weights):
    _, core_words = enumerate_identity_words(n, m - 2)
    core_weights = Counter(macro(w) for w in core_words)
    representative = {}
    for w in core_words:
        representative.setdefault(macro(w), w)
    offdiag = defaultdict(Fraction)
    for gamma, core_weight in core_weights.items():
        d = Counter(macro((t, t) + representative[gamma]) for t in trans)
        for a, da in d.items():
            for b, db in d.items():
                if a != b:
                    offdiag[(a, b)] += Fraction(core_weight * da * db, len(trans) * weights[a])
    formula = dict(offdiag)
    for a in weights:
        formula[(a, a)] = 1 - sum(value for (x, y), value in offdiag.items() if x == a and y != a)
    top_states = list(weights)
    core_states = list(core_weights)
    incidence = []
    for a in top_states:
        row = []
        for gamma in core_states:
            d = sum(macro((t, t) + representative[gamma]) == a for t in trans)
            row.append(core_weights[gamma] * d)
        incidence.append(row)
    return formula, core_weights, rational_rank(incidence), (len(top_states), len(core_states))


def matrix_checks(matrix, weights):
    states = list(weights)
    row_errors = {}
    for a in states:
        row_sum = sum(matrix.get((a, b), Fraction(0)) for b in states)
        if row_sum != 1:
            row_errors[str(a)] = str(row_sum)
    balance_errors = []
    for a in states:
        for b in states:
            lhs = weights[a] * matrix.get((a, b), Fraction(0))
            rhs = weights[b] * matrix.get((b, a), Fraction(0))
            if lhs != rhs:
                balance_errors.append((str(a), str(b), str(lhs), str(rhs)))
    return row_errors, balance_errors


def matrix_equal(left, right, states):
    differences = []
    for a in states:
        for b in states:
            x = left.get((a, b), Fraction(0))
            y = right.get((a, b), Fraction(0))
            if x != y:
                differences.append((str(a), str(b), str(x), str(y)))
    return differences


def connected_from_matrix(matrix, states):
    if not states:
        return True, 0
    adjacency = {a: set() for a in states}
    for (a, b), value in matrix.items():
        if a != b and value > 0:
            adjacency[a].add(b)
            adjacency[b].add(a)
    seen = {states[0]}
    todo = [states[0]]
    while todo:
        x = todo.pop()
        for y in adjacency[x] - seen:
            seen.add(y)
            todo.append(y)
    return len(seen) == len(states), len(seen)


def component_count(alpha, n: int) -> int:
    active = sum(len(vertices) for vertices, _ in alpha)
    return n - active + len(alpha)


def same_level_components(matrix, states, n: int):
    result = {}
    levels = defaultdict(list)
    for a in states:
        levels[component_count(a, n)].append(a)
    for level, level_states in sorted(levels.items()):
        adjacency = {a: set() for a in level_states}
        for a in level_states:
            for b in level_states:
                if a != b and matrix.get((a, b), Fraction(0)) > 0:
                    adjacency[a].add(b)
        unseen = set(level_states)
        sizes = []
        while unseen:
            root = next(iter(unseen))
            seen = {root}
            todo = [root]
            while todo:
                x = todo.pop()
                for y in adjacency[x] - seen:
                    seen.add(y)
                    todo.append(y)
            unseen -= seen
            sizes.append(len(seen))
        result[str(level)] = sorted(sizes, reverse=True)
    return result


def b_connectivity(n: int, m: int, words, fibers):
    starts = list(range(0, m - 3, 2))
    word_set = set(words)
    seen = {words[0]}
    todo = deque([words[0]])
    identity = tuple(range(n))
    while todo:
        w = todo.popleft()
        for i in starts:
            key = product(w[i : i + 4], identity)
            for block in fibers[4][key]:
                candidate = w[:i] + block + w[i + 4 :]
                assert candidate in word_set
                if candidate not in seen:
                    seen.add(candidate)
                    todo.append(candidate)
    return len(seen) == len(words), len(seen), starts


def d_n_audit(n: int, trans):
    identity = tuple(range(n))
    counts = []
    for target in trans:
        count = sum(product(block, identity) == target for block in itertools.product(trans, repeat=3))
        counts.append(count)
    formula = (3 * n * n + n - 12) // 2
    return counts, formula


def frac_string(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def audit_case(n: int, m: int):
    trans, words = enumerate_identity_words(n, m)
    weights = Counter(macro(w) for w in words)
    needed_vk = {(len(vertices), weight) for a in weights for vertices, weight in a}
    connected_counts = {(v, k): connected_identity_count(v, k) for v, k in needed_vk}
    predicted = {a: predicted_weight(a, m, connected_counts) for a in weights}
    weight_errors = [(str(a), weights[a], predicted[a]) for a in weights if weights[a] != predicted[a]]

    fibers = fibers_by_product(n, min(5, m))
    bar_k = direct_projection_k(n, m, words, fibers, weights)
    k_row_errors, k_balance_errors = matrix_checks(bar_k, weights)

    direct_s = direct_projection_square(trans, words, weights)
    formula_s, core_weights, incidence_rank, incidence_shape = common_core_square_formula(n, m, trans, weights)
    s_differences = matrix_equal(direct_s, formula_s, list(weights))
    s_row_errors, s_balance_errors = matrix_checks(formula_s, weights)
    s_connected, s_reached = connected_from_matrix(formula_s, list(weights))
    s_level_components = same_level_components(formula_s, list(weights), n)

    d_counts, d_formula = d_n_audit(n, trans)
    rset = [r for r in (3, 4, 5) if r <= m]
    c_sq = Fraction(len(trans), 2 * len(rset) * (m - 2) * d_formula)
    comparison_errors = []
    min_positive_ratio = None
    for a in weights:
        for b in weights:
            if a == b:
                continue
            sval = formula_s.get((a, b), Fraction(0))
            kval = bar_k.get((a, b), Fraction(0))
            if sval > 0:
                ratio = kval / sval
                min_positive_ratio = ratio if min_positive_ratio is None else min(min_positive_ratio, ratio)
                if kval < c_sq * sval:
                    comparison_errors.append((str(a), str(b), frac_string(kval), frac_string(sval)))

    b_ok, b_reached, starts = b_connectivity(n, m, words, fibers)
    f4_sizes = [len(v) for v in fibers[4].values()]
    n_pairs = m // 2
    specified_lower = Fraction(1, (n_pairs - 1) * max(f4_sizes))
    claimed_crude_lower = Fraction(1, (n_pairs - 1) * len(trans) ** 3)

    known = {(3, 4): (27, 4), (4, 4): (120, 13), (4, 6): (3936, 17)}[(n, m)]
    return {
        "N": n,
        "m": m,
        "M": len(trans),
        "identity_word_count": len(words),
        "expected_identity_word_count": known[0],
        "macro_count": len(weights),
        "expected_macro_count": known[1],
        "macro_weight_formula_errors": weight_errors,
        "connected_counts_used": {f"v={v},k={k}": count for (v, k), count in sorted(connected_counts.items())},
        "K_row_errors": k_row_errors,
        "K_detailed_balance_errors": k_balance_errors,
        "S_common_core_differences": s_differences,
        "S_row_errors": s_row_errors,
        "S_detailed_balance_errors": s_balance_errors,
        "S_connected": s_connected,
        "S_reached_macros": s_reached,
        "S_same_component_count_restriction_component_sizes": s_level_components,
        "core_macro_count": len(core_weights),
        "common_core_incidence_shape": incidence_shape,
        "common_core_incidence_rank_over_Q": incidence_rank,
        "D_N_enumerated_by_target": d_counts,
        "D_N_formula": d_formula,
        "D_N_bound_4M": d_formula <= 4 * len(trans),
        "c_sq": frac_string(c_sq),
        "c_sq_at_least_1_over_24_m_minus_2": c_sq >= Fraction(1, 24 * (m - 2)),
        "barK_ge_cS_errors": comparison_errors,
        "minimum_positive_offdiagonal_barK_over_S": frac_string(min_positive_ratio) if min_positive_ratio else None,
        "B_aligned_window_starts_zero_based": starts,
        "B_connected": b_ok,
        "B_reached_words": b_reached,
        "F4_min": min(f4_sizes),
        "F4_max": max(f4_sizes),
        "F4_max_le_M_cubed": max(f4_sizes) <= len(trans) ** 3,
        "B_specified_outcome_exact_uniform_lower": frac_string(specified_lower),
        "B_claimed_crude_lower": frac_string(claimed_crude_lower),
        "B_exact_lower_ge_claimed": specified_lower >= claimed_crude_lower,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="results.json")
    args = parser.parse_args()
    cases = [audit_case(3, 4), audit_case(4, 4), audit_case(4, 6)]
    result = {
        "python": platform.python_version(),
        "randomness": "none",
        "composition": "compose(p,q)[x]=p[q[x]]; word product t1...tm",
        "cases": cases,
    }
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
