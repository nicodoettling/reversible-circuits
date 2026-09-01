#!/usr/bin/env python3
"""Independent exact audit for M119.

This file deliberately imports no project experiment module.  It implements
the permutation, Hurwitz, strand-deletion, transfer-matrix, and DPS closure
logic directly from the definitions and the three cited primary sources.
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
from pathlib import Path


Perm = tuple[int, ...]
Trans = tuple[int, int]
Word = tuple[Trans, ...]


def identity(n: int) -> Perm:
    return tuple(range(n))


def compose(p: Perm, q: Perm) -> Perm:
    """Return p*q, meaning p after q: (p*q)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    ans = [0] * len(p)
    for x, y in enumerate(p):
        ans[y] = x
    return tuple(ans)


def transposition_perm(n: int, edge: Trans) -> Perm:
    a, b = edge
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def conjugate_transposition(a: Trans, b: Trans) -> Trans:
    """Return b*a*b for transpositions a,b."""
    bp = transposition_perm(max(max(a), max(b)) + 1, b)
    x, y = sorted((bp[a[0]], bp[a[1]]))
    return (x, y)


def eval_word(n: int, w: Word) -> Perm:
    p = identity(n)
    for e in w:
        p = compose(p, transposition_perm(n, e))
    return p


def hurwitz(w: Word, i: int, sign: int) -> Word:
    a, b = w[i], w[i + 1]
    out = list(w)
    if sign == 1:
        out[i], out[i + 1] = b, conjugate_transposition(a, b)
    elif sign == -1:
        out[i], out[i + 1] = conjugate_transposition(b, a), a
    else:
        raise ValueError(sign)
    return tuple(out)


def transpositions(n: int) -> tuple[Trans, ...]:
    return tuple(itertools.combinations(range(n), 2))


def connected_support(n: int, w: Word) -> bool:
    if n <= 1:
        return True
    adj = [[] for _ in range(n)]
    for a, b in w:
        adj[a].append(b)
        adj[b].append(a)
    seen = {0}
    stack = [0]
    while stack:
        x = stack.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return len(seen) == n


def enumerate_z(n: int) -> tuple[Word, ...]:
    if n == 1:
        return ((),)
    m = 2 * n - 2
    return tuple(
        w
        for w in itertools.product(transpositions(n), repeat=m)
        if eval_word(n, w) == identity(n) and connected_support(n, w)
    )


class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        self.p[y] = x
        return True


def join_data(n: int, w: Word) -> tuple[tuple[bool, ...], frozenset[Trans]]:
    dsu = DSU(n)
    flags: list[bool] = []
    tree: set[Trans] = set()
    for e in w:
        a, b = e
        is_join = dsu.union(a, b)
        flags.append(is_join)
        if is_join:
            tree.add(tuple(sorted(e)))
    return tuple(flags), frozenset(tree)


def tree_leaves(n: int, tree: frozenset[Trans]) -> tuple[int, ...]:
    deg = [0] * n
    for a, b in tree:
        deg[a] += 1
        deg[b] += 1
    return tuple(i for i, d in enumerate(deg) if d == 1)


def erase_label(p: Perm, v: int) -> Perm:
    comp = [x for x in range(len(p)) if x != v]
    rank = {x: i for i, x in enumerate(comp)}
    out = []
    for x in comp:
        y = p[x]
        if y == v:
            y = p[v]
        out.append(rank[y])
    return tuple(out)


def permutation_to_increment(p: Perm) -> Trans | None:
    moved = [i for i, x in enumerate(p) if i != x]
    if not moved:
        return None
    if len(moved) == 2 and p[moved[0]] == moved[1] and p[moved[1]] == moved[0]:
        return tuple(moved)  # type: ignore[return-value]
    raise AssertionError(f"not identity/transposition: {p}")


def delete_strand(n: int, w: Word, v: int) -> tuple[Word, tuple[int, ...]]:
    old = identity(n)
    erased_old = erase_label(old, v)
    projected: list[Trans] = []
    null_positions: list[int] = []
    for j, e in enumerate(w):
        old = compose(old, transposition_perm(n, e))
        erased_new = erase_label(old, v)
        inc = compose(inverse(erased_old), erased_new)
        t = permutation_to_increment(inc)
        if t is None:
            null_positions.append(j)
        else:
            projected.append(t)
        erased_old = erased_new
    return tuple(projected), tuple(null_positions)


def matmul_row(v: list[int], a: list[list[int]]) -> list[int]:
    return [sum(v[i] * a[i][j] for i in range(len(v))) for j in range(len(v))]


def transfer_matrices(q: int, z: Word) -> tuple[list[list[int]], ...]:
    joins, _ = join_data(q, z)
    mats = []
    for is_join, (x, y) in zip(joins, z):
        a = [[0] * q for _ in range(q)]
        if is_join:
            for c in range(q):
                a[c][y if c == x else x if c == y else c] = 1
        else:
            for c in range(q):
                if c not in (x, y):
                    a[c][c] = 1
            for c in (x, y):
                a[c][x] = a[c][y] = 1
        mats.append(a)
    return tuple(mats)


def transfer_interval_counts(q: int, z: Word) -> dict[tuple[int, int], int]:
    mats = transfer_matrices(q, z)
    L = len(z)
    ans = {}
    for a in range(L + 1):
        row = [1] * q
        ans[(a, a)] = sum(row)
        for b in range(a + 1, L + 1):
            row = matmul_row(row, mats[b - 1])
            ans[(a, b)] = sum(row)
    return ans


def word_neighbors(w: Word) -> tuple[Word, ...]:
    return tuple(hurwitz(w, i, s) for i in range(len(w) - 1) for s in (1, -1))


def hurwitz_distance(adjacency: dict[Word, tuple[Word, ...]], source: Word, target: Word) -> int:
    if source == target:
        return 0
    seen = {source}
    frontier = [source]
    dist = 0
    while frontier:
        dist += 1
        nxt = []
        for x in frontier:
            for y in adjacency[x]:
                if y == target:
                    return dist
                if y not in seen:
                    seen.add(y)
                    nxt.append(y)
        frontier = nxt
    raise AssertionError("disconnected Hurwitz graph")


def all_pair_distances(states: tuple[Word, ...]) -> dict[Word, dict[Word, int]]:
    state_set = set(states)
    adj = {w: tuple({x for x in word_neighbors(w) if x != w and x in state_set}) for w in states}
    ans: dict[Word, dict[Word, int]] = {}
    for source in states:
        d = {source: 0}
        queue = deque([source])
        while queue:
            x = queue.popleft()
            for y in adj[x]:
                if y not in d:
                    d[y] = d[x] + 1
                    queue.append(y)
        if len(d) != len(states):
            raise AssertionError((len(d), len(states)))
        ans[source] = d
    return ans


def cayley_trees(n: int) -> tuple[frozenset[Trans], ...]:
    edges = transpositions(n)
    out = []
    for comb in itertools.combinations(edges, n - 1):
        dsu = DSU(n)
        if all(dsu.union(*e) for e in comb):
            out.append(frozenset(comb))
    return tuple(out)


def dps_word(n: int, tree: frozenset[Trans], pi: tuple[int, ...], mirror: int = 1) -> Word:
    """Implement DPS Proposition 3 followed by the Theorem 5 closure.

    The implementation uses the noncrossing stack closure of the hairy-tree
    outer contour.  Labels are zero based.  ``mirror`` reverses every vertex
    rotation; either choice is a global mirror convention.
    """
    m = 2 * n - 2
    assert sorted(pi) == list(range(m))

    # Root the Cayley tree at y_(n-1).
    nbr = [[] for _ in range(n)]
    for a, b in tree:
        nbr[a].append(b)
        nbr[b].append(a)
    parent = [-1] * n
    parent[n - 1] = n - 1
    queue = deque([n - 1])
    while queue:
        x = queue.popleft()
        for y in nbr[x]:
            if parent[y] == -1:
                parent[y] = x
                queue.append(y)

    # Original vertices are ('w',i) and ('b',i), i<n-1.  An item is either
    # one dart of an actual tree edge or a loose stub.  Each vertex has one
    # item of every label, ordered by the required cyclic label order.
    rotations: dict[tuple[str, int], list[tuple[str, int]]] = {}
    item_vertex: dict[tuple[str, int], tuple[str, int]] = {}
    item_label: dict[tuple[str, int], int] = {}
    alpha: dict[tuple[str, int], tuple[str, int]] = {}
    is_stub: set[tuple[str, int]] = set()
    item_id = 0

    def new_item(kind: str, vertex: tuple[str, int], label: int) -> tuple[str, int]:
        nonlocal item_id
        ans = (kind, item_id)
        item_id += 1
        item_vertex[ans] = vertex
        item_label[ans] = label
        return ans

    actual_at: dict[tuple[tuple[str, int], int], tuple[str, int]] = {}
    for i in range(n - 1):
        bvertex = ('b', i)
        wchild = ('w', i)
        wparent = ('w', parent[i])
        d1 = new_item('d', wchild, pi[2 * i])
        e1 = new_item('d', bvertex, pi[2 * i])
        d2 = new_item('d', wparent, pi[2 * i + 1])
        e2 = new_item('d', bvertex, pi[2 * i + 1])
        alpha[d1] = e1
        alpha[e1] = d1
        alpha[d2] = e2
        alpha[e2] = d2
        actual_at[(wchild, pi[2 * i])] = d1
        actual_at[(wparent, pi[2 * i + 1])] = d2
        actual_at[(bvertex, pi[2 * i])] = e1
        actual_at[(bvertex, pi[2 * i + 1])] = e2

    vertices = [('w', i) for i in range(n)] + [('b', i) for i in range(n - 1)]
    for vertex in vertices:
        by_label = {}
        for label in range(m):
            item = actual_at.get((vertex, label))
            if item is None:
                item = new_item('h', vertex, label)
                alpha[item] = item
                is_stub.add(item)
            by_label[label] = item
        labels = list(range(m))
        # White vertices increase clockwise and black vertices decrease;
        # mirroring reverses both rotations.
        if vertex[0] == 'b':
            labels.reverse()
        if mirror == -1:
            labels.reverse()
        rotations[vertex] = [by_label[label] for label in labels]

    sigma: dict[tuple[str, int], tuple[str, int]] = {}
    for rot in rotations.values():
        for a, b in zip(rot, rot[1:] + rot[:1]):
            sigma[a] = b

    # The hairy tree has one outer-face contour.  Treat a loose stub as a
    # fixed point of alpha; it is encountered once at its tip.
    first = next(iter(item_vertex))
    contour = []
    seen = set()
    x = first
    while x not in seen:
        seen.add(x)
        contour.append(x)
        x = sigma[alpha[x]]
    if x != first or len(seen) != len(item_vertex):
        raise AssertionError((len(seen), len(item_vertex), x, first))
    stubs = [x for x in contour if x in is_stub]

    # Choose a cyclic starting point after a global minimum of the white(+1)
    # / black(-1) walk.  This is the stack closure performed around the outer
    # face, with exactly m unmatched white half-edges left for the new x_n.
    prefix = 0
    min_prefix = 0
    min_after = -1
    for idx, h in enumerate(stubs):
        prefix += 1 if item_vertex[h][0] == 'w' else -1
        if prefix < min_prefix:
            min_prefix = prefix
            min_after = idx
    stubs = stubs[min_after + 1 :] + stubs[: min_after + 1]
    stack: list[tuple[str, int]] = []
    paired: list[tuple[tuple[str, int], tuple[str, int]]] = []
    for h in stubs:
        if item_vertex[h][0] == 'w':
            stack.append(h)
        else:
            if not stack:
                raise AssertionError("cyclic stack underflow")
            paired.append((stack.pop(), h))
    if len(stack) != m:
        raise AssertionError((len(stack), m))
    if sorted(item_label[h] for h in stack) != list(range(m)):
        raise AssertionError("unmatched white labels are not a permutation")

    # Replace paired stubs by closure-edge darts, preserving their slots.
    final_alpha = dict(alpha)
    for wh, bh in paired:
        final_alpha[wh] = bh
        final_alpha[bh] = wh

    # The remaining white stubs connect to the new black x_(n-1).  Its
    # cyclic order is prescribed by the full label cycle at a black vertex.
    new_black = ('b', n - 1)
    new_darts = {}
    for wh in stack:
        label = item_label[wh]
        bh = new_item('d', new_black, label)
        new_darts[label] = bh
        final_alpha[wh] = bh
        final_alpha[bh] = wh
    labels = list(reversed(range(m)))
    if mirror == -1:
        labels.reverse()
    rotations[new_black] = [new_darts[label] for label in labels]

    final_sigma = {}
    for rot in rotations.values():
        for a, b in zip(rot, rot[1:] + rot[:1]):
            final_sigma[a] = b

    # Traverse faces.  The pre-map has only digons and quadrangles.  A
    # quadrangle's two black vertices give the transposition attached to its
    # common face label.
    face_seen = set()
    by_face_label: dict[int, Trans] = {}
    for dart in final_sigma:
        if dart in face_seen:
            continue
        face = []
        x = dart
        while x not in face_seen:
            face_seen.add(x)
            face.append(x)
            x = final_sigma[final_alpha[x]]
        if x != dart:
            raise AssertionError("face walk merged cycles")
        if len(face) not in (2, 4):
            raise AssertionError(("face degree", len(face)))
        if len(face) == 2:
            continue
        black_vertices = sorted({item_vertex[x][1] for x in face if item_vertex[x][0] == 'b'})
        if len(black_vertices) != 2:
            raise AssertionError(("black vertices", black_vertices, face))
        # With phi=sigma*alpha, a dart from black to white traverses this face
        # in the chosen orientation.  Its static label is the face label.
        labels_here = []
        for x in face:
            mate = final_alpha[x]
            if item_vertex[x][0] == 'b' and item_vertex[mate][0] == 'w':
                labels_here.append(item_label[x])
        if len(set(labels_here)) != 1:
            raise AssertionError(("face labels", labels_here, face))
        label = labels_here[0]
        by_face_label[label] = (black_vertices[0], black_vertices[1])
    if sorted(by_face_label) != list(range(m)):
        raise AssertionError(("missing quadrangles", sorted(by_face_label), m))
    return tuple(by_face_label[i] for i in range(m))


def swap_values(pi: tuple[int, ...], j: int) -> tuple[int, ...]:
    return tuple(j + 1 if x == j else j if x == j + 1 else x for x in pi)


def tree_exchanges(n: int, tree: frozenset[Trans]) -> tuple[frozenset[Trans], ...]:
    ans = []
    nonedges = set(transpositions(n)) - set(tree)
    for e in tree:
        for f in nonedges:
            t = frozenset((set(tree) - {e}) | {f})
            dsu = DSU(n)
            if all(dsu.union(*g) for g in t):
                ans.append(t)
    return tuple(ans)


def spectral_gap_path_random_scan(m: int) -> float:
    # CLR continuous path gap 2(1-cos(pi/m)); scale every edge rate by
    # 1/[2(m-1)] for the displayed half-lazy random-scan kernel.
    return (1.0 - math.cos(math.pi / m)) / (m - 1)


def audit_deletion(zs: dict[int, tuple[Word, ...]], max_d: int) -> dict[str, object]:
    direct_counts: dict[tuple[int, Word, int, int], int] = Counter()
    deletion_failures = Counter()
    equivariance_checked = 0
    statewise_requests = 0
    statewise_failures = 0
    marked_by_d = Counter()
    leaf_histograms = {}

    for d in range(2, max_d + 1):
        zset = set(zs[d - 1])
        leaves_hist = Counter()
        for w in zs[d]:
            _, tree = join_data(d, w)
            leaves = tree_leaves(d, tree)
            leaves_hist[len(leaves)] += 1
            for v in leaves:
                marked_by_d[d] += 1
                z, nulls = delete_strand(d, w, v)
                if len(nulls) != 2:
                    deletion_failures['null_count'] += 1
                    continue
                if z not in zset or eval_word(d - 1, z) != identity(d - 1) or not connected_support(d - 1, z):
                    deletion_failures['base_not_z'] += 1
                a, b = nulls[0], nulls[1] - 1
                direct_counts[(v, z, a, b)] += 1

                physical_deleted_targets = set()
                base_local_targets = set(word_neighbors(z))
                for wp in word_neighbors(w):
                    _, tp = join_data(d, wp)
                    if v not in tree_leaves(d, tp):
                        continue
                    zp, _ = delete_strand(d, wp, v)
                    physical_deleted_targets.add(zp)
                    equivariance_checked += 1
                    if zp != z and zp not in base_local_targets:
                        deletion_failures['equivariance'] += 1
                for zp in word_neighbors(z):
                    if zp == z:
                        continue
                    statewise_requests += 1
                    if zp not in physical_deleted_targets:
                        statewise_failures += 1
        leaf_histograms[str(d)] = {str(k): v for k, v in sorted(leaves_hist.items())}

    transfer_failures = 0
    direct_fiber_hist = {}
    interval_rows_checked = 0
    for q in range(1, max_d):
        per_base = Counter()
        for z in zs[q]:
            predicted = transfer_interval_counts(q, z)
            for v in range(q + 1):
                total = 0
                for (a, b), want in predicted.items():
                    got = direct_counts[(v, z, a, b)]
                    interval_rows_checked += 1
                    total += got
                    if got != want:
                        transfer_failures += 1
                per_base[(v, z)] = total
        hist = Counter(per_base.values())
        direct_fiber_hist[str(q)] = {str(k): v for k, v in sorted(hist.items())}

    predicted_q4 = Counter()
    if 4 in zs:
        for z in zs[4]:
            predicted_q4[sum(transfer_interval_counts(4, z).values())] += 1

    bounds = {}
    for q in range(1, max_d + 1):
        if q not in zs:
            continue
        C = math.comb(2 * q, 2)
        totals = [sum(transfer_interval_counts(q, z).values()) for z in zs[q]]
        bounds[str(q)] = {
            'interval_count': C,
            'minimum': min(totals),
            'maximum': max(totals),
            'lower_qC': q * C,
            'upper_q2C': q * q * C,
            'bound_failures': sum(not (q * C <= x <= q * q * C) for x in totals),
        }

    return {
        'marked_incidences': {str(k): v for k, v in sorted(marked_by_d.items())},
        'leaf_count_histogram': leaf_histograms,
        'deletion_failures': dict(deletion_failures),
        'equivariance_oriented_moves_checked': equivariance_checked,
        'statewise_nontrivial_base_requests': statewise_requests,
        'statewise_one_step_failures': statewise_failures,
        'transfer_interval_rows_checked': interval_rows_checked,
        'transfer_interval_failures': transfer_failures,
        'direct_fiber_histogram_including_missing_labels': direct_fiber_hist,
        'predicted_q4_base_histogram': {str(k): v for k, v in sorted(predicted_q4.items())},
        'universal_bound_small_case_check': bounds,
    }


def audit_dps(zs: dict[int, tuple[Word, ...]], max_d: int) -> dict[str, object]:
    coverage = {}
    product_maps = {}
    for d in range(2, max_d + 1):
        m = 2 * d - 2
        pmap = {}
        fibers = Counter()
        failures = Counter()
        for tree in cayley_trees(d):
            tree_key = tuple(sorted(tree))
            for pi in itertools.permutations(range(m)):
                w = dps_word(d, tree, pi, mirror=1)
                pmap[(tree_key, pi)] = w
                fibers[w] += 1
                if eval_word(d, w) != identity(d):
                    failures['identity'] += 1
                if not connected_support(d, w):
                    failures['support'] += 1
        if set(fibers) != set(zs[d]):
            failures['coverage_symmetric_difference'] = len(set(fibers) ^ set(zs[d]))
        coverage[str(d)] = {
            'rooted_pairs': len(pmap),
            'image_words': len(fibers),
            'preimage_histogram': {str(k): v for k, v in sorted(Counter(fibers.values()).items())},
            'failures': dict(failures),
        }
        product_maps[d] = pmap

    distances = {}
    for d in range(3, max_d + 1):
        m = 2 * d - 2
        pmap = product_maps[d]
        pi_demands: dict[Word, Counter[Word]] = defaultdict(Counter)
        tree_demands: dict[Word, Counter[Word]] = defaultdict(Counter)
        for (tree_key, pi), w in pmap.items():
            for j in range(m - 1):
                wp = pmap[(tree_key, swap_values(pi, j))]
                pi_demands[w][wp] += 1
            tree = frozenset(tree_key)
            for tp in tree_exchanges(d, tree):
                wp = pmap[(tuple(sorted(tp)), pi)]
                tree_demands[w][wp] += 1

        state_set = set(zs[d])
        adjacency = {w: tuple({x for x in word_neighbors(w) if x != w and x in state_set}) for w in zs[d]}
        pi_hist = Counter()
        tree_hist = Counter()
        for source in zs[d]:
            needed = set(pi_demands.get(source, ())) | set(tree_demands.get(source, ()))
            found = {source: 0}
            queue = deque([source])
            while queue and not needed.issubset(found):
                x = queue.popleft()
                for y in adjacency[x]:
                    if y not in found:
                        found[y] = found[x] + 1
                        queue.append(y)
            if not needed.issubset(found):
                raise AssertionError('DPS demand endpoints disconnected')
            for target, mult in pi_demands.get(source, {}).items():
                pi_hist[found[target]] += mult
            for target, mult in tree_demands.get(source, {}).items():
                tree_hist[found[target]] += mult
        distances[str(d)] = {
            'adjacent_value_histogram': {str(k): v for k, v in sorted(pi_hist.items())},
            'tree_exchange_histogram': {str(k): v for k, v in sorted(tree_hist.items())},
            'adjacent_value_max': max(pi_hist),
            'tree_exchange_max': max(tree_hist),
        }

    T = frozenset({(0, 1), (0, 2)})
    pi = (0, 2, 3, 1)
    wp = dps_word(3, T, pi, mirror=1)
    wq = dps_word(3, T, swap_values(pi, 0), mirror=1)
    adj3 = {w: tuple({x for x in word_neighbors(w) if x != w}) for w in zs[3]}
    witness_distance = hurwitz_distance(adj3, wp, wq)
    return {
        'coverage': coverage,
        'distances': distances,
        'stored_witness': {
            'tree': [list(e) for e in sorted(T)],
            'pi_zero_based': list(pi),
            'word': [list(e) for e in wp],
            'swapped_word': [list(e) for e in wq],
            'distance': witness_distance,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--max-d', type=int, default=4)
    args = parser.parse_args()
    started = time.time()
    zs = {d: enumerate_z(d) for d in range(1, args.max_d + 1)}
    results: dict[str, object] = {
        'metadata': {
            'python': platform.python_version(),
            'seed': None,
            'dependencies': {},
            'convention': '(pq)(x)=p(q(x)); displayed word factors multiply left-to-right',
            'imports_m112': False,
        },
        'z_counts': {str(d): len(zs[d]) for d in zs},
    }
    results['deletion_transfer'] = audit_deletion(zs, args.max_d)
    results['dps'] = audit_dps(zs, args.max_d)
    results['ideal_gap_normalizations'] = {
        str(d): {
            'ust_anari_lower_bound': (
                1.0
                if d == 2
                else 1.0 / (2 * (d - 1) * (math.comb(d, 2) - d + 1))
            ),
            'permutation_exact_gap_clr': spectral_gap_path_random_scan(2 * d - 2),
            'coordinate_mixture_gap_is_half_minimum': True,
        }
        for d in range(2, args.max_d + 1)
    }
    results['metadata']['elapsed_seconds'] = time.time() - started
    try:
        results['metadata']['repository_commit'] = subprocess.check_output(
            ['git', 'rev-parse', 'HEAD'], text=True
        ).strip()
    except Exception:
        results['metadata']['repository_commit'] = None
    args.output.write_text(json.dumps(results, indent=2, sort_keys=True) + '\n')
    print(json.dumps(results, indent=2, sort_keys=True))
    print(f'elapsed={time.time()-started:.6f}s')


if __name__ == '__main__':
    main()
