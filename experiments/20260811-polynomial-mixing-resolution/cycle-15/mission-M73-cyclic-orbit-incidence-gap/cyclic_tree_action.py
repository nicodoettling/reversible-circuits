#!/usr/bin/env python3
"""Exact finite audit of the cyclic action under Stanley's tree bijection.

The state space is the set of reduced transposition factorizations of the
long cycle.  We use the accepted M70 Hurwitz-BFS enumerator and independently
reconstruct Stanley's labelled Cayley tree.  All reported claims are finite
falsifiers/calibrations, not asymptotic gap proofs.

Convention: (p q)(x)=p(q(x)); factor tuples multiply left-to-right.
"""

from __future__ import annotations

import argparse
import collections
import json
import platform
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
M70 = HERE.parent / "mission-M70-long-cycle-exceptional-closure-gap"
sys.path.insert(0, str(M70))

from n7_exceptional_krylov import (  # noqa: E402
    Edge,
    conjugate_edge,
    minimal_words,
    transpositions,
)


def stanley_tree(n: int, raw_edges: tuple[Edge, ...]) -> tuple[Edge, ...]:
    """Stanley's labelled tree, with rank labels 0,...,n-1."""
    blocks = [{i} for i in range(n)]
    gamma_edges: list[tuple[int, int, int]] = []
    for rank, (a, b) in enumerate(raw_edges, start=1):
        ia = next(i for i, block in enumerate(blocks) if a in block)
        ib = next(i for i, block in enumerate(blocks) if b in block)
        if ia == ib:
            raise AssertionError("reduced prefix did not merge two blocks")
        first, second = blocks[ia], blocks[ib]
        if min(first) > min(second):
            first, second = second, first
            ia, ib = ib, ia
        minimum_second = min(second)
        label = max(x for x in first if x < minimum_second)
        gamma_edges.append((label, minimum_second, rank))
        merged = first | second
        blocks = [block for j, block in enumerate(blocks) if j not in (ia, ib)]
        blocks.append(merged)

    adjacency: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for u, v, rank in gamma_edges:
        adjacency[u].append((v, rank))
        adjacency[v].append((u, rank))
    parent = [-2] * n
    parent[0] = -1
    rank_label = [-1] * n
    rank_label[0] = 0
    stack = [0]
    while stack:
        u = stack.pop()
        for v, rank in adjacency[u]:
            if v == parent[u]:
                continue
            if parent[v] != -2:
                raise AssertionError("Stanley intermediate graph is not a tree")
            parent[v] = u
            rank_label[v] = rank
            stack.append(v)
    if any(label < 0 for label in rank_label):
        raise AssertionError("Stanley intermediate graph is disconnected")
    return tuple(
        sorted(tuple(sorted((rank_label[u], rank_label[v]))) for u, v, _ in gamma_edges)
    )


def prufer_code(n: int, tree: tuple[Edge, ...]) -> tuple[int, ...]:
    adjacency = [set() for _ in range(n)]
    for u, v in tree:
        adjacency[u].add(v)
        adjacency[v].add(u)
    code: list[int] = []
    for _ in range(n - 2):
        leaf = min(i for i in range(n) if len(adjacency[i]) == 1)
        neighbor = next(iter(adjacency[leaf]))
        code.append(neighbor)
        adjacency[leaf].remove(neighbor)
        adjacency[neighbor].remove(leaf)
    return tuple(code)


def shift_tree(tree: tuple[Edge, ...], q: int, n: int) -> tuple[Edge, ...]:
    return tuple(sorted(tuple(sorted(((a + q) % n, (b + q) % n))) for a, b in tree))


def analyze(n: int) -> dict[str, object]:
    edges, gates = transpositions(n)
    edge_index = {edge: i for i, edge in enumerate(edges)}
    words = minimal_words(n, edges, gates)
    word_set = set(words)
    trees = {
        word: stanley_tree(n, tuple(edges[index] for index in word))
        for word in words
    }
    if len(set(trees.values())) != len(words):
        raise AssertionError("Stanley tree map is not bijective")
    codes = {word: prufer_code(n, tree) for word, tree in trees.items()}

    def cyclic_conjugate(word: tuple[int, ...]) -> tuple[int, ...]:
        answer = []
        for index in word:
            a, b = edges[index]
            answer.append(edge_index[tuple(sorted(((a - 1) % n, (b - 1) % n)))])
        target = tuple(answer)
        if target not in word_set:
            raise AssertionError("cyclic conjugation left the state space")
        return target

    tree_shift_matches = collections.Counter()
    code_diagonal_matches = collections.Counter()
    action_tree_distance = collections.Counter()
    action_code_distance = collections.Counter()
    quotient_hurwitz_tree_distance = collections.Counter()
    quotient_hurwitz_code_distance = collections.Counter()
    max_tree_witness = None
    max_code_witness = None

    for word in words:
        target = cyclic_conjugate(word)
        source_tree, target_tree = trees[word], trees[target]
        source_code, target_code = codes[word], codes[target]
        matching_tree_shifts = [q for q in range(n) if shift_tree(source_tree, q, n) == target_tree]
        tree_shift_matches[len(matching_tree_shifts)] += 1
        matching_code_shifts = [
            q for q in range(n)
            if tuple((value + q) % n for value in source_code) == target_code
        ]
        code_diagonal_matches[len(matching_code_shifts)] += 1
        action_tree_distance[len(set(source_tree) ^ set(target_tree)) // 2] += 1
        action_code_distance[sum(a != b for a, b in zip(source_code, target_code))] += 1

        for i in range(n - 2):
            changed = list(word)
            changed[i] = word[i + 1]
            changed[i + 1] = edge_index[
                conjugate_edge(edges[word[i]], edges[word[i + 1]])
            ]
            neighbor = tuple(changed)
            orbit_trees = []
            orbit_codes = []
            current = neighbor
            for _ in range(n):
                orbit_trees.append(trees[current])
                orbit_codes.append(codes[current])
                current = cyclic_conjugate(current)
            if current != neighbor:
                raise AssertionError("cyclic action does not have order n")
            tree_distance = min(
                len(set(source_tree) ^ set(candidate)) // 2 for candidate in orbit_trees
            )
            code_distance = min(
                sum(a != b for a, b in zip(source_code, candidate))
                for candidate in orbit_codes
            )
            quotient_hurwitz_tree_distance[tree_distance] += 1
            quotient_hurwitz_code_distance[code_distance] += 1
            if max_tree_witness is None or tree_distance > max_tree_witness["distance"]:
                max_tree_witness = {
                    "distance": tree_distance,
                    "source_word": word,
                    "target_word": neighbor,
                    "source_tree": source_tree,
                    "target_tree": trees[neighbor],
                }
            if max_code_witness is None or code_distance > max_code_witness["distance"]:
                max_code_witness = {
                    "distance": code_distance,
                    "source_word": word,
                    "target_word": neighbor,
                    "source_code": source_code,
                    "target_code": codes[neighbor],
                }

    unseen = set(words)
    orbit_count = 0
    while unseen:
        start = min(unseen)
        current = start
        orbit = []
        for _ in range(n):
            if current in orbit:
                raise AssertionError("cyclic action is not free")
            orbit.append(current)
            current = cyclic_conjugate(current)
        if current != start:
            raise AssertionError("cyclic action order exceeds n")
        unseen.difference_update(orbit)
        orbit_count += 1

    def serial(counter: collections.Counter[int]) -> dict[str, int]:
        return {str(key): counter[key] for key in sorted(counter)}

    return {
        "n": n,
        "states": len(words),
        "expected_states": n ** (n - 2),
        "cyclic_orbits": orbit_count,
        "expected_cyclic_orbits": n ** (n - 3),
        "stanley_trees_distinct": len(set(trees.values())),
        "U_equals_a_global_cyclic_tree_label_shift_counts": serial(tree_shift_matches),
        "U_equals_a_diagonal_prufer_value_shift_counts": serial(code_diagonal_matches),
        "basis_exchange_distance_between_tree_and_U_tree": serial(action_tree_distance),
        "prufer_hamming_distance_between_code_and_U_code": serial(action_code_distance),
        "quotient_basis_distance_of_one_hurwitz_move": serial(quotient_hurwitz_tree_distance),
        "quotient_prufer_distance_of_one_hurwitz_move": serial(quotient_hurwitz_code_distance),
        "maximum_quotient_tree_distance_witness": max_tree_witness,
        "maximum_quotient_prufer_distance_witness": max_code_witness,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "claim_tested": (
            "Simultaneous endpoint conjugation is a simple global cyclic relabeling "
            "under Stanley's Cayley-tree/Pruefer bijection, or quotienting it makes "
            "one Hurwitz move local in those coordinates."
        ),
        "scope_warning": (
            "Finite distances can refute a proposed exact locality statement but cannot "
            "prove an asymptotic spectral gap or congestion bound."
        ),
        "convention": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "parameters": sorted(set(args.n)),
        "results": [analyze(n) for n in sorted(set(args.n))],
        "python": platform.python_version(),
        "seed": None,
        "deterministic": True,
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": " ".join(sys.argv),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

