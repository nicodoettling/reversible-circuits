#!/usr/bin/env python3
"""Exact small-rank audit of the rooted Duchi--Poulalhon--Schaeffer encoding.

This is a direct implementation of the quadratic ``hairy tree'' closure
algorithm in DuPoSc Proposition 3 / Theorem 5.  It is intentionally limited
to d <= 4: its purpose is to falsify named local-comparison lemmas, not to
serve as an asymptotic sampler.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import sys
import time
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path

from marked_leaf_audit import enumerate_z, evaluate, proposals


@dataclass(frozen=True)
class Half:
    color: str
    vertex: int
    label: int


@dataclass(frozen=True)
class Side:
    kind: str


def cayley_trees(d: int):
    """Enumerate labeled Cayley trees by Prüfer sequences."""
    if d == 1:
        yield frozenset()
        return
    if d == 2:
        yield frozenset({(1, 2)})
        return
    for code in itertools.product(range(1, d + 1), repeat=d - 2):
        deg = [0] + [1] * d
        for x in code:
            deg[x] += 1
        edges = []
        for x in code:
            leaf = next(i for i in range(1, d + 1) if deg[i] == 1)
            edges.append(tuple(sorted((leaf, x))))
            deg[leaf] -= 1
            deg[x] -= 1
        rem = [i for i in range(1, d + 1) if deg[i] == 1]
        edges.append(tuple(sorted(rem)))
        yield frozenset(edges)


def rooted_parent(tree, d):
    adj = {i: [] for i in range(1, d + 1)}
    for u, v in tree:
        adj[u].append(v)
        adj[v].append(u)
    parent = {d: 0}
    todo = [d]
    while todo:
        u = todo.pop()
        for v in adj[u]:
            if v not in parent:
                parent[v] = u
                todo.append(v)
    return parent


def hurwitz_tree(tree, pi, d):
    """Return incidence maps for Proposition 3's rooted Hurwitz tree."""
    parent = rooted_parent(tree, d)
    # Vertices are ('w',i), 1<=i<=d, and ('b',i), 1<=i<d.
    incidence = defaultdict(dict)
    black_of_label = {}
    for i in range(1, d):
        p = parent[i]
        labels = pi[2 * i - 2 : 2 * i]
        for lab, white in ((labels[0], i), (labels[1], p)):
            b = ("b", i)
            w = ("w", white)
            incidence[b][lab] = w
            incidence[w][lab] = b
            black_of_label[lab] = i
    return incidence, black_of_label


def hairy_boundary(incidence, d, trace_sign):
    """Build the unique outer-face contour of the embedded hairy tree.

    At whites the clockwise label order is increasing; at blacks it is
    decreasing.  ``trace_sign`` chooses one of the two face orientations;
    the source algorithm determines the valid one by its local-closure
    assertions, which we audit rather than assume.
    """
    m = 2 * d - 2
    start = (("w", 1), 1)
    state = start
    out = []
    seen = set()
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        color, idx = vertex
        clockwise_step = 1 if color == "w" else -1
        lab = 1 + ((incoming - 1 + trace_sign * clockwise_step) % m)
        if lab in incidence[vertex]:
            neighbor = incidence[vertex][lab]
            out.append(Side("tree"))
            state = (neighbor, lab)
        else:
            out.append(Half(color, idx, lab))
            state = (vertex, lab)
    if state != start:
        raise AssertionError("hairy contour did not close")
    expected = (2 * d - 1) * m
    if len(out) != expected:
        raise AssertionError((len(out), expected))
    return out


def close_hairy(tokens, d):
    """Perform all local white--black closures on a cyclic boundary word."""
    tokens = list(tokens)
    quadrangle_black = {}
    closure_counts = Counter()
    while True:
        half_positions = [i for i, x in enumerate(tokens) if isinstance(x, Half)]
        if not half_positions:
            raise AssertionError("no half-edges remain")
        pair = None
        for k, wi in enumerate(half_positions):
            w = tokens[wi]
            bj = half_positions[(k + 1) % len(half_positions)]
            b = tokens[bj]
            if w.color == "w" and b.color == "b":
                pair = (wi, bj)
                break
        if pair is None:
            break
        wi, bj = pair
        # Rotate so the selected white half-edge is first and its black mate
        # occurs later in the linear representation.
        tokens = tokens[wi:] + tokens[:wi]
        bj = (bj - wi) % len(tokens)
        w = tokens[0]
        b = tokens[bj]
        if w.label != b.label:
            raise AssertionError(("unequal closure labels", w, b))
        distance = sum(isinstance(x, Side) for x in tokens[1:bj])
        if distance not in (1, 3):
            raise AssertionError(("bad closure distance", distance, w, b))
        closure_counts[(w.label, distance)] += 1
        if distance == 3:
            if w.label in quadrangle_black:
                raise AssertionError(("two quadrangles with label", w.label))
            quadrangle_black[w.label] = b.vertex
        tokens = [Side("closure")] + tokens[bj + 1 :]

    remaining = [x for x in tokens if isinstance(x, Half)]
    if len(remaining) != 2 * d - 2 or any(x.color != "w" for x in remaining):
        raise AssertionError(("bad final half-edge set", len(remaining)))
    if sorted(x.label for x in remaining) != list(range(1, 2 * d - 1)):
        raise AssertionError("final white half-edge labels are not a permutation")
    return quadrangle_black, closure_counts


def dps_word(tree, pi, d, trace_sign):
    incidence, black_of_label = hurwitz_tree(tree, pi, d)
    boundary = hairy_boundary(incidence, d, trace_sign)
    other_black, closure_counts = close_hairy(boundary, d)
    word = []
    for lab in range(1, 2 * d - 1):
        a = black_of_label[lab]
        b = other_black.get(lab, d)
        if a == b:
            raise AssertionError(("degenerate factor", lab, a))
        word.append(tuple(sorted((a - 1, b - 1))))
    return tuple(word), closure_counts


def word_key(word):
    return tuple(word)


def all_pairs(d):
    m = 2 * d - 2
    for tree in cayley_trees(d):
        for pi in itertools.permutations(range(1, m + 1)):
            yield tree, pi


def graph_distances(words, d):
    index = {w: i for i, w in enumerate(words)}
    adj = [[] for _ in words]
    for i, w in enumerate(words):
        for position, sign, nw in proposals(w):
            if nw != w:
                adj[i].append((index[nw], position, sign))
    return index, adj


def shortest_action_path(adj, source, target):
    if source == target:
        return ()
    seen = {source}
    parent = {}
    q = deque([source])
    while q:
        u = q.popleft()
        for v, position, sign in adj[u]:
            if v in seen:
                continue
            seen.add(v)
            parent[v] = (u, position, sign)
            if v == target:
                path = []
                x = v
                while x != source:
                    prev, pos, sgn = parent[x]
                    path.append((prev, x, pos, sgn))
                    x = prev
                path.reverse()
                return tuple(path)
            q.append(v)
    raise AssertionError("disconnected Hurwitz graph")


def audit(d):
    words = tuple(enumerate_z(d))
    word_set = set(words)
    valid_signs = []
    sign_rows = {}
    mappings = {}
    for sign in (1, -1):
        counter = Counter()
        failures = Counter()
        mapping = {}
        closure_hist = Counter()
        for tree, pi in all_pairs(d):
            try:
                word, closure_counts = dps_word(tree, pi, d, sign)
            except AssertionError as exc:
                failures[str(exc.args[0])] += 1
                continue
            mapping[(tree, pi)] = word
            counter[word] += 1
            closure_hist.update(closure_counts)
            if evaluate(d, word) != tuple(range(d)):
                failures["nonidentity"] += 1
            if word not in word_set:
                failures["not_Z_d"] += 1
        good = (
            not failures
            and len(counter) == len(words)
            and set(counter.values()) == {d}
        )
        sign_rows[str(sign)] = {
            "mapped_pairs": len(mapping),
            "distinct_words": len(counter),
            "preimage_histogram": dict(sorted(Counter(counter.values()).items())),
            "failures": dict(failures),
            "closure_histogram": {str(k): v for k, v in sorted(closure_hist.items())},
            "valid_d_to_1": good,
        }
        if good:
            valid_signs.append(sign)
            mappings[sign] = mapping

    row = {
        "d": d,
        "z_size": len(words),
        "pair_count": sum(1 for _ in all_pairs(d)),
        "orientation_audit": sign_rows,
        "valid_signs": valid_signs,
        "all_reconstructed_identity_connected_and_exactly_d_to_1": bool(valid_signs),
    }
    if not valid_signs or d < 3:
        return row

    # Reversing the sphere orientation gives the second equally valid mirror
    # convention.  Fix +1 when available; word-graph distances are invariant
    # under this mirror choice.
    chosen_sign = 1 if 1 in valid_signs else valid_signs[0]
    row["chosen_mirror_sign"] = chosen_sign
    mapping = mappings[chosen_sign]
    index, adj = graph_distances(words, d)
    m = 2 * d - 2
    pi_dist = Counter()
    tree_dist = Counter()
    pi_source_multiplicity = Counter()
    tree_source_multiplicity = Counter()
    pi_action_load = Counter()
    tree_action_load = Counter()
    pi_recovery_multiplicity = Counter()
    tree_recovery_multiplicity = Counter()
    path_cache = {}
    pi_nonlocal_witness = None

    def get_path(source, target):
        key = (source, target)
        if key not in path_cache:
            path_cache[key] = shortest_action_path(adj, source, target)
        return path_cache[key]
    # Each rooted ideal edge is tested.  Distances concern projected words;
    # the source multiplicities expose immediate many-to-one loss after root
    # forgetting, but are not a path-congestion certificate.
    for (tree, pi), word in mapping.items():
        for lab in range(1, m):
            swapped = tuple(
                lab + 1 if x == lab else lab if x == lab + 1 else x for x in pi
            )
            target = mapping[(tree, swapped)]
            path = get_path(index[word], index[target])
            pi_dist[len(path)] += 1
            if len(path) > 1:
                candidate = {
                    "tree_edges": [list(e) for e in sorted(tree)],
                    "pi": list(pi),
                    "swapped_adjacent_values": [lab, lab + 1],
                    "source_word": [list(e) for e in word],
                    "target_word": [list(e) for e in target],
                    "signed_hurwitz_distance": len(path),
                }
                witness_key = (
                    len(path),
                    tuple(sorted(tree)),
                    pi,
                    lab,
                )
                if pi_nonlocal_witness is None or witness_key < pi_nonlocal_witness[0]:
                    pi_nonlocal_witness = (witness_key, candidate)
            pi_source_multiplicity[(word, target, lab)] += 1
            for time, (source_id, _target_id, position, sign) in enumerate(path):
                action = (source_id, position, sign)
                pi_action_load[action] += 1
                pi_recovery_multiplicity[(action, time, lab)] += 1
        for add in sorted(set(itertools.combinations(range(1, d + 1), 2)) - set(tree)):
            u, v = add
            tadj = defaultdict(list)
            for a, b in tree:
                tadj[a].append(b)
                tadj[b].append(a)
            # unique u-v path; deleting any path edge gives a basis exchange
            parent = {u: 0}
            todo = [u]
            while todo:
                a = todo.pop()
                for b in tadj[a]:
                    if b not in parent:
                        parent[b] = a
                        todo.append(b)
            path = []
            x = v
            while x != u:
                path.append(tuple(sorted((x, parent[x]))))
                x = parent[x]
            for drop in path:
                target_tree = frozenset((set(tree) - {drop}) | {add})
                target = mapping[(target_tree, pi)]
                path = get_path(index[word], index[target])
                tree_dist[len(path)] += 1
                tree_source_multiplicity[(word, target, add, drop)] += 1
                descriptor = (add, drop)
                for time, (source_id, _target_id, position, sign) in enumerate(path):
                    action = (source_id, position, sign)
                    tree_action_load[action] += 1
                    tree_recovery_multiplicity[(action, time, descriptor)] += 1
    row["local_ideal_move_audit"] = {
        "pi_adjacent_value_swap_distance_histogram": dict(sorted(pi_dist.items())),
        "pi_adjacent_value_swap_smallest_nonlocal_witness": pi_nonlocal_witness[1],
        "pi_projected_edge_max_root_multiplicity": max(pi_source_multiplicity.values()),
        "pi_deterministic_shortest_path_max_action_load": max(pi_action_load.values()),
        "pi_max_source_multiplicity_given_action_time_descriptor": max(
            pi_recovery_multiplicity.values()
        ),
        "tree_basis_exchange_distance_histogram": dict(sorted(tree_dist.items())),
        "tree_projected_edge_max_root_multiplicity": max(tree_source_multiplicity.values()),
        "tree_deterministic_shortest_path_max_action_load": max(tree_action_load.values()),
        "tree_max_source_multiplicity_given_action_time_descriptor": max(
            tree_recovery_multiplicity.values()
        ),
        "warning": (
            "These are finite diagnostics for one arbitrary deterministic shortest-path rule. "
            "They neither prove an asymptotic source-recovery bound nor polynomial congestion."
        ),
    }
    return row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", nargs="+", type=int, default=[2, 3, 4])
    parser.add_argument("--output", type=Path, default=Path("dps_local_results.json"))
    args = parser.parse_args()
    started = time.perf_counter()
    rows = [audit(d) for d in args.d]
    payload = {
        "experiment": "M112 rooted DPS local-move audit",
        "claim_tested": (
            "The DPS rooted product map is exactly d-to-1 onto Z_d, and its "
            "adjacent-pi and basis-exchange moves intertwine in one Hurwitz step."
        ),
        "commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
        "argv": sys.argv,
        "python": platform.python_version(),
        "nonstandard_dependencies": {},
        "elapsed_seconds": time.perf_counter() - started,
        "deterministic": True,
        "seed": None,
        "scope_warning": (
            "Complete only for d<=4; distances and fixed shortest-path loads do not "
            "prove asymptotic path length, source recovery, or congestion."
        ),
        "rows": rows,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
