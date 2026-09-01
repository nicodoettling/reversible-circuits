#!/usr/bin/env python3
"""Exact C_n-equivariance audit for two primary-source Dénes bijections.

The endpoint/factor convention is the accepted M70 convention:
``(p q)(x)=p(q(x))`` and tuple factors multiply left-to-right.  M70's
endpoint is h=(0 1 ... n-1).  Goulden--Yong use the usual right-to-left
permutation action.  Apostolakis--Ojakian reverse both the action convention
and the written endpoint; hence the *same ordered sequence* represents the
same Goulden--Yong input in their Definition 6.2.

Maps tested:

* ``moszkowski_tree`` is the map identified in Goulden--Yong, p. 114:
  draw the (noncrossing) factor chords, label chord i by factor rank i,
  root at original vertex 0, and push each edge label away from the root.
  Thus a non-root vertex gets the label of its parent edge, shifted by one
  because factor ranks here are 0-based.  Original vertex labels are erased.

* ``goulden_yong_tree`` implements Definition 2.9 and Definition 6.2 of
  Apostolakis--Ojakian (arXiv:1704.03085), proved there to equal the
  Goulden--Yong planar-dual bijection.  Compute the mind-body dual of the
  unchanged ordered factor sequence and push its edge ranks away from 0.

* ``goulden_pepper_images`` implements Algorithm 3 of Goulden--Pepper
  (Discrete Math. 113 (1993), pp. 264--266) from every Prüfer-coded tree and
  reverses the resulting exact dictionary.

Finite checks can refute equivariance/locality claims, but do not prove a
spectral-gap bound.
"""

from __future__ import annotations

import argparse
import collections
import itertools
import json
import platform
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
M70 = HERE.parent / "mission-M70-long-cycle-exceptional-closure-gap"
sys.path.insert(0, str(M70))

from n7_exceptional_krylov import Edge, minimal_words, transpositions  # noqa: E402


Tree = tuple[Edge, ...]


def rooted_push_tree(n: int, ranked_edges: tuple[Edge, ...]) -> Tree:
    """Erase original labels; give each nonroot vertex its parent-edge rank+1."""
    adjacency: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for rank, (a, b) in enumerate(ranked_edges):
        adjacency[a].append((b, rank + 1))
        adjacency[b].append((a, rank + 1))
    parent = [-2] * n
    pushed = [-1] * n
    parent[0] = -1
    pushed[0] = 0
    stack = [0]
    while stack:
        u = stack.pop()
        for v, rank_label in adjacency[u]:
            if v == parent[u]:
                continue
            if parent[v] != -2:
                raise AssertionError("raw edge set is not a tree")
            parent[v] = u
            pushed[v] = rank_label
            stack.append(v)
    if sorted(pushed) != list(range(n)):
        raise AssertionError("pushed vertex labels are not a permutation")
    return tuple(
        sorted(tuple(sorted((pushed[a], pushed[b]))) for a, b in ranked_edges)
    )


def moszkowski_tree(n: int, raw_edges: tuple[Edge, ...]) -> Tree:
    return rooted_push_tree(n, raw_edges)


def mind_body_dual(raw_edges: tuple[Edge, ...]) -> tuple[Edge, ...]:
    """Apostolakis--Ojakian Def. 2.9, with bodies indexed by vertices."""
    mind_in_body = list(range(len(raw_edges) + 1))
    dual: list[Edge] = []
    for a, b in raw_edges:
        dual.append(tuple(sorted((mind_in_body[a], mind_in_body[b]))))
        mind_in_body[a], mind_in_body[b] = mind_in_body[b], mind_in_body[a]
    return tuple(dual)


def goulden_yong_tree(n: int, raw_edges: tuple[Edge, ...]) -> Tree:
    # AO reverse both GY's action convention and displayed endpoint, so the
    # ordered transposition sequence itself is unchanged (AO pp. 22--23).
    dual = mind_body_dual(raw_edges)
    return rooted_push_tree(n, dual)


def prufer_tree(n: int, code: tuple[int, ...]) -> Tree:
    degree = [1] * n
    for value in code:
        degree[value] += 1
    answer: list[Edge] = []
    for value in code:
        leaf = next(i for i in range(n) if degree[i] == 1)
        answer.append(tuple(sorted((leaf, value))))
        degree[leaf] -= 1
        degree[value] -= 1
    remaining = [i for i in range(n) if degree[i] == 1]
    answer.append(tuple(sorted(remaining)))
    return tuple(sorted(answer))


def goulden_pepper_word(n: int, tree: Tree) -> tuple[Edge, ...]:
    """Goulden--Pepper Algorithm 3, translated from labels 1..n to 0..n-1."""
    output: list[Edge | None] = [None] * (n - 1)

    def recurse(vertices: frozenset[int], edges: frozenset[Edge], cycle: tuple[int, ...]) -> None:
        m = len(vertices)
        if m == 1:
            return
        ordered = sorted(vertices)
        largest, second = ordered[-1], ordered[-2]
        adjacency = {v: set() for v in vertices}
        for a, b in edges:
            adjacency[a].add(b)
            adjacency[b].add(a)
        parent = {largest: -1}
        queue = collections.deque([largest])
        while second not in parent:
            u = queue.popleft()
            for v in adjacency[u]:
                if v not in parent:
                    parent[v] = u
                    queue.append(v)
        j = second
        while parent[j] != largest:
            j = parent[j]
        cut = tuple(sorted((largest, j)))

        prime_vertices = {largest}
        stack = [largest]
        while stack:
            u = stack.pop()
            for v in adjacency[u]:
                if tuple(sorted((u, v))) == cut or v in prime_vertices:
                    continue
                prime_vertices.add(v)
                stack.append(v)
        double_vertices = set(vertices) - prime_vertices
        if second not in double_vertices or j not in double_vertices:
            raise AssertionError("Goulden--Pepper deletion components mistranslated")
        k = len(prime_vertices)
        rank = sorted(double_vertices).index(j)
        output[second] = tuple(sorted((cycle[rank], cycle[rank + k])))

        prime_edges = frozenset(e for e in edges if set(e) <= prime_vertices)
        double_edges = frozenset(e for e in edges if set(e) <= double_vertices)
        recurse(
            frozenset(prime_vertices),
            prime_edges,
            cycle[rank : rank + k],
        )
        recurse(
            frozenset(double_vertices),
            double_edges,
            cycle[rank + k :] + cycle[:rank],
        )

    recurse(frozenset(range(n)), frozenset(tree), tuple(range(n)))
    if any(edge is None for edge in output):
        raise AssertionError("Goulden--Pepper recursion left a factor undefined")
    return tuple(output)  # type: ignore[return-value]


def goulden_pepper_images(
    n: int, words: list[tuple[int, ...]], raw: dict[tuple[int, ...], tuple[Edge, ...]]
) -> dict[tuple[int, ...], Tree]:
    """Build the inverse Algorithm-3 dictionary exactly via all Prüfer codes."""
    word_to_tree: dict[tuple[Edge, ...], Tree] = {}
    if n == 2:
        codes = [()]
    else:
        import itertools

        codes = itertools.product(range(n), repeat=n - 2)
    for code in codes:
        tree = prufer_tree(n, tuple(code))
        # GP explicitly multiply by applying factors from left to right; the
        # project evaluator uses ordinary functional composition.  Reverse
        # their output sequence to represent the same displayed endpoint h.
        factorization = tuple(reversed(goulden_pepper_word(n, tree)))
        if factorization in word_to_tree:
            raise AssertionError("Goulden--Pepper Algorithm 3 was not injective")
        word_to_tree[factorization] = tree
    if set(word_to_tree) != set(raw.values()):
        missing = min(set(raw.values()) - set(word_to_tree))
        extra = min(set(word_to_tree) - set(raw.values()))
        raise AssertionError(f"Goulden--Pepper endpoint translation failed: {missing=}, {extra=}")
    return {word: word_to_tree[raw[word]] for word in words}


def shift_tree(tree: Tree, q: int, n: int) -> Tree:
    return tuple(sorted(tuple(sorted(((a + q) % n, (b + q) % n))) for a, b in tree))


def basis_distance(first: Tree, second: Tree) -> int:
    return len(set(first) ^ set(second)) // 2


def degree_profile(n: int, tree: Tree) -> tuple[int, ...]:
    degree = [0] * n
    for a, b in tree:
        degree[a] += 1
        degree[b] += 1
    return tuple(sorted(degree))


def relabel_tree(tree: Tree, permutation: tuple[int, ...]) -> Tree:
    return tuple(
        sorted(tuple(sorted((permutation[a], permutation[b]))) for a, b in tree)
    )


def all_n_cycles(n: int):
    """Every n-cycle exactly once, represented by its pointwise images."""
    for tail in itertools.permutations(range(1, n)):
        cycle_order = (0,) + tail
        permutation = [-1] * n
        for a, b in zip(cycle_order, cycle_order[1:] + cycle_order[:1]):
            permutation[a] = b
        yield tuple(permutation)


def analyze_map(
    n: int,
    words: list[tuple[int, ...]],
    raw: dict[tuple[int, ...], tuple[Edge, ...]],
    cyclic_conjugate,
    map_name: str,
    map_fn=None,
    images_override: dict[tuple[int, ...], Tree] | None = None,
) -> dict[str, object]:
    images = (
        images_override
        if images_override is not None
        else {word: map_fn(n, raw[word]) for word in words}
    )
    if len(set(images.values())) != len(words):
        counts = collections.Counter(images.values())
        collision = next((tree, count) for tree, count in counts.items() if count > 1)
        raise AssertionError(f"{map_name} not bijective: {collision}")

    # If U were any fixed relabeling of Cayley-tree vertices, its permutation
    # must be an n-cycle: U has exact order n and acts freely on trees for odd
    # n, while a smaller permutation order cannot induce a free order-n action.
    global_relabel_candidates = list(all_n_cycles(n))
    for word in words:
        source_tree = images[word]
        target_tree = images[cyclic_conjugate(word)]
        global_relabel_candidates = [
            permutation
            for permutation in global_relabel_candidates
            if relabel_tree(source_tree, permutation) == target_tree
        ]
        if not global_relabel_candidates:
            break

    exact_shift_counts: collections.Counter[int] = collections.Counter()
    shifts_when_unique: collections.Counter[int] = collections.Counter()
    min_shift_distance: collections.Counter[int] = collections.Counter()
    raw_action_distance: collections.Counter[int] = collections.Counter()
    shape_preserved = collections.Counter()
    first_failure = None
    first_shape_failure = None
    for word in words:
        target = cyclic_conjugate(word)
        source_tree, target_tree = images[word], images[target]
        matches = [q for q in range(n) if shift_tree(source_tree, q, n) == target_tree]
        exact_shift_counts[len(matches)] += 1
        if len(matches) == 1:
            shifts_when_unique[matches[0]] += 1
        else:
            distances = [basis_distance(shift_tree(source_tree, q, n), target_tree) for q in range(n)]
            min_shift_distance[min(distances)] += 1
            if first_failure is None:
                first_failure = {
                    "source_word": word,
                    "conjugate_word": target,
                    "source_tree": source_tree,
                    "conjugate_tree": target_tree,
                    "basis_distance_by_shift": distances,
                }
        raw_action_distance[basis_distance(source_tree, target_tree)] += 1
        preserves_shape = degree_profile(n, source_tree) == degree_profile(n, target_tree)
        shape_preserved[preserves_shape] += 1
        if not preserves_shape and first_shape_failure is None:
            first_shape_failure = {
                "source_word": word,
                "conjugate_word": target,
                "source_tree": source_tree,
                "conjugate_tree": target_tree,
                "source_degree_profile": degree_profile(n, source_tree),
                "conjugate_degree_profile": degree_profile(n, target_tree),
            }

    # A natural quotient UST chain would also follow if the transported U
    # action were an automorphism of the Cayley-tree basis-exchange graph.
    # Audit that weaker property directly, independently of how U acts on
    # labels.  Since `images` is onto all Cayley trees, membership is exact.
    tree_to_word = {tree: word for word, tree in images.items()}
    all_edges = tuple((a, b) for a in range(n) for b in range(a + 1, n))
    adjacency_distance: collections.Counter[int] = collections.Counter()
    first_adjacency_failure = None
    for source_tree, word in tree_to_word.items():
        source_set = set(source_tree)
        action_source = images[cyclic_conjugate(word)]
        for removed in source_tree:
            for added in all_edges:
                if added in source_set:
                    continue
                candidate = tuple(sorted((source_set - {removed}) | {added}))
                neighbor_word = tree_to_word.get(candidate)
                if neighbor_word is None:
                    continue
                action_neighbor = images[cyclic_conjugate(neighbor_word)]
                distance = basis_distance(action_source, action_neighbor)
                adjacency_distance[distance] += 1
                if distance != 1 and first_adjacency_failure is None:
                    first_adjacency_failure = {
                        "source_tree": source_tree,
                        "neighbor_tree": candidate,
                        "removed": removed,
                        "added": added,
                        "U_source_tree": action_source,
                        "U_neighbor_tree": action_neighbor,
                        "U_image_basis_distance": distance,
                    }

    def serial(counter: collections.Counter[int]) -> dict[str, int]:
        return {str(key): counter[key] for key in sorted(counter)}

    return {
        "name": map_name,
        "distinct_images": len(set(images.values())),
        "C_n_action_equals_some_global_tree_shift_count": serial(exact_shift_counts),
        "matching_shift_when_unique": serial(shifts_when_unique),
        "minimum_basis_distance_to_any_shift_on_failures": serial(min_shift_distance),
        "unshifted_basis_distance_under_C_n_action": serial(raw_action_distance),
        "degree_profile_preserved_under_C_n_action": {
            str(key).lower(): shape_preserved[key] for key in (False, True)
        },
        "first_shape_change_witness": first_shape_failure,
        "global_n_cycle_vertex_relabeling_candidates": [
            list(permutation) for permutation in global_relabel_candidates
        ],
        "UST_basis_exchange_distance_after_induced_U": serial(adjacency_distance),
        "first_UST_adjacency_failure": first_adjacency_failure,
        "first_non_equivariance_witness": first_failure,
    }


def analyze(n: int) -> dict[str, object]:
    edges, gates = transpositions(n)
    edge_index = {edge: i for i, edge in enumerate(edges)}
    words = minimal_words(n, edges, gates)
    word_set = set(words)
    raw = {word: tuple(edges[index] for index in word) for word in words}

    def cyclic_conjugate(word: tuple[int, ...]) -> tuple[int, ...]:
        target = tuple(
            edge_index[tuple(sorted(((edges[index][0] - 1) % n, (edges[index][1] - 1) % n)))]
            for index in word
        )
        if target not in word_set:
            raise AssertionError("cyclic conjugation left the endpoint fiber")
        return target

    gp_images = goulden_pepper_images(n, words, raw)
    return {
        "n": n,
        "states": len(words),
        "expected_states": n ** (n - 2),
        "maps": [
            analyze_map(n, words, raw, cyclic_conjugate, "Moszkowski_push", moszkowski_tree),
            analyze_map(
                n,
                words,
                raw,
                cyclic_conjugate,
                "Goulden_Yong_mind_body_dual",
                goulden_yong_tree,
            ),
            analyze_map(
                n,
                words,
                raw,
                cyclic_conjugate,
                "Goulden_Pepper_Algorithm_3",
                images_override=gp_images,
            ),
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    parameters = sorted(set(args.n))
    payload = {
        "claim_tested": (
            "The primary-source Moszkowski or Goulden--Yong Cayley-tree "
            "bijection intertwines endpoint-cycle conjugation with one fixed "
            "global cyclic relabeling of Cayley-tree vertices."
        ),
        "scope_warning": (
            "Finite exact enumeration refutes universal equivariance when a witness "
            "exists; it does not prove an asymptotic gap or congestion bound."
        ),
        "convention": "(p q)(x)=p(q(x)); tuple products left-to-right",
        "cyclic_action": "U maps every raw endpoint label x to x-1 modulo n",
        "source_translation": (
            "AO reverse both GY's permutation-action convention and displayed endpoint; "
            "the ordered transposition sequence is therefore unchanged.  GP Algorithm 3 "
            "uses left-to-right application, so its output is reversed for project composition."
        ),
        "parameters": parameters,
        "results": [analyze(n) for n in parameters],
        "python": platform.python_version(),
        "seed": None,
        "deterministic": True,
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": " ".join(sys.argv),
        "primary_sources": [
            "Goulden--Yong, JCTA 98 (2002), Secs. 2--3, esp. pp. 111--114",
            "Apostolakis--Ojakian, arXiv:1704.03085v1, Def. 2.9, Def. 6.2, Thm. 6.7",
            "Goulden--Pepper, Discrete Math. 113 (1993), Algorithm 3 and Theorem 4",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
