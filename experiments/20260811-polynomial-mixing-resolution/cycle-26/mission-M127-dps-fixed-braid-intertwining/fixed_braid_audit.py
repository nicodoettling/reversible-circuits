#!/usr/bin/env python3
"""Exact constraints for a source-independent DPS adjacent-value braid.

This independently implements the + mirror of the DPS hairy-tree closure.
For every rooted product coordinate (T, pi), it compares F(T, pi) with
F(T, s_i pi).  A fixed signed Hurwitz word acts deterministically on the
unrooted factor tuple, so the edit must be constant on every d-element fiber
of F.  The script exhausts that necessary constraint at d=3,4.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
import subprocess
import sys
import time
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path


Edge = tuple[int, int]
Word = tuple[Edge, ...]
Tree = frozenset[tuple[int, int]]


@dataclass(frozen=True)
class Half:
    color: str
    vertex: int
    label: int


@dataclass(frozen=True)
class Side:
    kind: str


def transposition_perm(d: int, edge: Edge) -> tuple[int, ...]:
    a, b = edge
    p = list(range(d))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return pq, so (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def evaluate(d: int, word: Word) -> tuple[int, ...]:
    out = tuple(range(d))
    for edge in word:
        out = compose(out, transposition_perm(d, edge))
    return out


def conjugate_edge(edge: Edge, by: Edge) -> Edge:
    a, b = edge
    x, y = by
    image = lambda z: y if z == x else x if z == y else z
    return tuple(sorted((image(a), image(b))))


def hurwitz(word: Word, position: int, sign: int) -> Word:
    """Apply R_position^sign with zero-based position."""
    a, b = word[position], word[position + 1]
    out = list(word)
    if sign == 1:
        out[position : position + 2] = [b, conjugate_edge(a, b)]
    elif sign == -1:
        out[position : position + 2] = [conjugate_edge(b, a), a]
    else:
        raise ValueError(sign)
    return tuple(out)


def support_connected(d: int, word: Word) -> bool:
    adj = [[] for _ in range(d)]
    for a, b in word:
        adj[a].append(b)
        adj[b].append(a)
    seen = {0}
    todo = [0]
    while todo:
        a = todo.pop()
        for b in adj[a]:
            if b not in seen:
                seen.add(b)
                todo.append(b)
    return len(seen) == d


def cayley_trees(d: int):
    if d == 2:
        yield frozenset({(1, 2)})
        return
    for code in itertools.product(range(1, d + 1), repeat=d - 2):
        degree = [0] + [1] * d
        for x in code:
            degree[x] += 1
        edges = []
        for x in code:
            leaf = next(v for v in range(1, d + 1) if degree[v] == 1)
            edges.append(tuple(sorted((leaf, x))))
            degree[leaf] -= 1
            degree[x] -= 1
        remaining = [v for v in range(1, d + 1) if degree[v] == 1]
        edges.append(tuple(sorted(remaining)))
        yield frozenset(edges)


def rooted_parent(tree: Tree, d: int) -> dict[int, int]:
    adj = {v: [] for v in range(1, d + 1)}
    for a, b in tree:
        adj[a].append(b)
        adj[b].append(a)
    parent = {d: 0}
    todo = [d]
    while todo:
        a = todo.pop()
        for b in adj[a]:
            if b not in parent:
                parent[b] = a
                todo.append(b)
    return parent


def hairy_incidence(tree: Tree, pi: tuple[int, ...], d: int):
    parent = rooted_parent(tree, d)
    incidence: dict[tuple[str, int], dict[int, tuple[str, int]]] = defaultdict(dict)
    first_black: dict[int, int] = {}
    for i in range(1, d):
        p = parent[i]
        labels = pi[2 * i - 2 : 2 * i]
        for label, white in ((labels[0], i), (labels[1], p)):
            black_vertex = ("b", i)
            white_vertex = ("w", white)
            incidence[black_vertex][label] = white_vertex
            incidence[white_vertex][label] = black_vertex
            first_black[label] = i
    return incidence, first_black


def hairy_boundary(incidence, d: int) -> list[Half | Side]:
    """Trace the accepted + mirror: white labels increase, black decrease."""
    m = 2 * d - 2
    start = (("w", 1), 1)
    state = start
    seen = set()
    out: list[Half | Side] = []
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        color, _ = vertex
        step = 1 if color == "w" else -1
        label = 1 + ((incoming - 1 + step) % m)
        if label in incidence[vertex]:
            out.append(Side("tree"))
            state = (incidence[vertex][label], label)
        else:
            out.append(Half(color, vertex[1], label))
            state = (vertex, label)
    if state != start or len(out) != (2 * d - 1) * m:
        raise AssertionError("invalid hairy boundary")
    return out


def close_hairy(tokens: list[Half | Side], d: int) -> dict[int, int]:
    tokens = list(tokens)
    second_black: dict[int, int] = {}
    while True:
        positions = [j for j, token in enumerate(tokens) if isinstance(token, Half)]
        pair = None
        for k, white_position in enumerate(positions):
            black_position = positions[(k + 1) % len(positions)]
            white, black = tokens[white_position], tokens[black_position]
            if white.color == "w" and black.color == "b":
                pair = white_position, black_position
                break
        if pair is None:
            break
        white_position, black_position = pair
        tokens = tokens[white_position:] + tokens[:white_position]
        black_position = (black_position - white_position) % len(tokens)
        white, black = tokens[0], tokens[black_position]
        if white.label != black.label:
            raise AssertionError(("unequal labels", white, black))
        distance = sum(isinstance(token, Side) for token in tokens[1:black_position])
        if distance not in (1, 3):
            raise AssertionError(("bad closure distance", distance))
        if distance == 3:
            if white.label in second_black:
                raise AssertionError("duplicate quadrangle")
            second_black[white.label] = black.vertex
        tokens = [Side("closure")] + tokens[black_position + 1 :]
    remaining = [token for token in tokens if isinstance(token, Half)]
    if len(remaining) != 2 * d - 2:
        raise AssertionError("bad final half-edge count")
    if any(token.color != "w" for token in remaining):
        raise AssertionError("nonwhite final half-edge")
    if sorted(token.label for token in remaining) != list(range(1, 2 * d - 1)):
        raise AssertionError("bad final labels")
    return second_black


def dps_word(tree: Tree, pi: tuple[int, ...], d: int) -> Word:
    incidence, first_black = hairy_incidence(tree, pi, d)
    second_black = close_hairy(hairy_boundary(incidence, d), d)
    word = []
    for label in range(1, 2 * d - 1):
        a = first_black[label]
        b = second_black.get(label, d)
        if a == b:
            raise AssertionError("degenerate factor")
        word.append(tuple(sorted((a - 1, b - 1))))
    return tuple(word)


def swap_adjacent_values(pi: tuple[int, ...], i: int) -> tuple[int, ...]:
    return tuple(i + 1 if x == i else i if x == i + 1 else x for x in pi)


def serialize_tree(tree: Tree) -> list[list[int]]:
    return [list(edge) for edge in sorted(tree)]


def serialize_word(word: Word) -> list[list[int]]:
    return [[a + 1, b + 1] for a, b in word]


def descriptor_key(item):
    tree, pi, target = item
    return tuple(sorted(tree)), pi, target


def connected_components_from_actions(words: tuple[Word, ...]):
    """Optional audit: signed generators act as permutations of Z_d."""
    index = {word: k for k, word in enumerate(words)}
    m = len(words[0])
    generator_permutations = []
    for position in range(m - 1):
        for sign in (1, -1):
            image = tuple(index[hurwitz(word, position, sign)] for word in words)
            if len(set(image)) != len(words):
                raise AssertionError("Hurwitz generator not bijective")
            generator_permutations.append(
                {"position": position + 1, "sign": sign, "image_sha256": hashlib.sha256(json.dumps(image).encode()).hexdigest()}
            )
    seen = {0}
    todo = deque([0])
    while todo:
        a = todo.popleft()
        word = words[a]
        for position in range(m - 1):
            for sign in (1, -1):
                b = index[hurwitz(word, position, sign)]
                if b not in seen:
                    seen.add(b)
                    todo.append(b)
    return generator_permutations, len(seen)


def direct_product_subgroup(d: int, left: Word, right: Word):
    """Subgroup of S_d x S_d generated by coordinatewise factor pairs."""
    identity = tuple(range(d))
    generators = tuple(
        (transposition_perm(d, a), transposition_perm(d, b))
        for a, b in zip(left, right)
    )

    def multiply(x, y):
        return compose(x[0], y[0]), compose(x[1], y[1])

    subgroup = {(identity, identity)}
    todo = [(identity, identity)]
    while todo:
        x = todo.pop()
        for generator in generators:
            y = multiply(x, generator)
            if y not in subgroup:
                subgroup.add(y)
                todo.append(y)
    return frozenset(subgroup)


def rooted_descriptor(tree: Tree, pi: tuple[int, ...]) -> dict:
    return {"tree": serialize_tree(tree), "pi": list(pi)}


def find_subgroup_obstruction(
    d: int,
    words: tuple[Word, ...],
    representatives: dict[Word, tuple[Tree, tuple[int, ...]]],
    target: dict[Word, Word],
) -> dict | None:
    """Find the first pair whose S_d x S_d generated subgroup changes."""
    pairs_tested = 0
    for left in words:
        for right in words:
            pairs_tested += 1
            source_subgroup = direct_product_subgroup(d, left, right)
            target_subgroup = direct_product_subgroup(d, target[left], target[right])
            if source_subgroup == target_subgroup:
                continue
            left_tree, left_pi = representatives[left]
            right_tree, right_pi = representatives[right]
            return {
                "pairs_tested_until_witness": pairs_tested,
                "source_word_a": serialize_word(left),
                "source_word_b": serialize_word(right),
                "source_rooted_coordinate_a": rooted_descriptor(left_tree, left_pi),
                "source_rooted_coordinate_b": rooted_descriptor(right_tree, right_pi),
                "target_word_a": serialize_word(target[left]),
                "target_word_b": serialize_word(target[right]),
                "source_generated_subgroup_order": len(source_subgroup),
                "target_generated_subgroup_order": len(target_subgroup),
                "subgroup_intersection_order": len(source_subgroup & target_subgroup),
                "invariant": (
                    "A common signed Hurwitz word on the two sources is the ordinary "
                    "Hurwitz action on coordinatewise pairs in S_d x S_d and preserves "
                    "their generated subgroup exactly."
                ),
            }
    return None


def compose_action(left: tuple[int, ...], right: tuple[int, ...]):
    """Return left after right as action tables."""
    return tuple(left[right[x]] for x in range(len(right)))


def exact_action_image_and_cover(
    words: tuple[Word, ...], target_permutations: dict[int, tuple[int, ...]]
) -> dict:
    """Enumerate the d=3 Hurwitz action image and minimum schedule covers."""
    index = {word: k for k, word in enumerate(words)}
    m = len(words[0])
    generator_descriptors = tuple(
        (position, sign) for position in range(m - 1) for sign in (1, -1)
    )
    generators = tuple(
        tuple(index[hurwitz(word, position, sign)] for word in words)
        for position, sign in generator_descriptors
    )
    identity = tuple(range(len(words)))
    queue = deque([identity])
    parent: dict[tuple[int, ...], tuple[tuple[int, ...], int] | None] = {
        identity: None
    }
    while queue:
        action = queue.popleft()
        for generator_index, generator in enumerate(generators):
            new_action = compose_action(generator, action)
            if new_action not in parent:
                parent[new_action] = action, generator_index
                queue.append(new_action)

    def shortest_word(action: tuple[int, ...]):
        path = []
        cursor = action
        while parent[cursor] is not None:
            previous, generator_index = parent[cursor]
            position, sign = generator_descriptors[generator_index]
            path.append([position + 1, sign])
            cursor = previous
        path.reverse()
        return path

    def apply_schedule(word: Word, schedule: list[list[int]]) -> Word:
        out = word
        for one_based_position, sign in schedule:
            out = hurwitz(out, one_based_position - 1, sign)
        return out

    target_rows = []
    full_mask = (1 << len(words)) - 1
    for adjacent_index, target in sorted(target_permutations.items()):
        best_action_for_mask: dict[int, tuple[int, ...]] = {}
        best_word_for_mask: dict[int, list[list[int]]] = {}
        for action in parent:
            mask = sum(
                (action[source] == target[source]) << source
                for source in range(len(words))
            )
            if not mask:
                continue
            word = shortest_word(action)
            if mask not in best_word_for_mask or len(word) < len(best_word_for_mask[mask]):
                best_action_for_mask[mask] = action
                best_word_for_mask[mask] = word

        frontier: dict[int, list[int]] = {0: []}
        frontier_sizes = [1]
        cover_masks = None
        for _depth in range(1, len(words) + 1):
            next_frontier: dict[int, list[int]] = {}
            for covered, used_masks in frontier.items():
                for mask in best_action_for_mask:
                    new_covered = covered | mask
                    if new_covered not in next_frontier:
                        next_frontier[new_covered] = used_masks + [mask]
            frontier = next_frontier
            frontier_sizes.append(len(frontier))
            if full_mask in frontier:
                cover_masks = frontier[full_mask]
                break
        if cover_masks is None:
            raise AssertionError("transitivity should give a finite schedule cover")

        assigned = set()
        cover_rows = []
        for class_index, mask in enumerate(cover_masks, 1):
            newly_assigned = [
                source
                for source in range(len(words))
                if (mask >> source) & 1 and source not in assigned
            ]
            assigned.update(newly_assigned)
            schedule = best_word_for_mask[mask]
            for source in newly_assigned:
                endpoint = apply_schedule(words[source], schedule)
                if index[endpoint] != target[source]:
                    raise AssertionError("schedule-cover endpoint failure")
            cover_rows.append(
                {
                    "metadata_class": class_index,
                    "signed_hurwitz_word": schedule,
                    "total_agreement_count": mask.bit_count(),
                    "assigned_source_count": len(newly_assigned),
                    "assigned_source_words": [serialize_word(words[x]) for x in newly_assigned],
                }
            )
        if len(assigned) != len(words):
            raise AssertionError("bad cover assignment")
        target_rows.append(
            {
                "adjacent_value_index": adjacent_index,
                "target_is_bijection": len(set(target)) == len(words),
                "target_is_involution": compose_action(target, target) == identity,
                "target_in_signed_hurwitz_action_image": target in parent,
                "nonempty_distinct_agreement_masks": len(best_action_for_mask),
                "maximum_sources_served_by_one_fixed_braid": max(
                    mask.bit_count() for mask in best_action_for_mask
                ),
                "minimum_fixed_braid_schedule_classes": len(cover_masks),
                "set_cover_frontier_sizes_through_minimum": frontier_sizes,
                "one_minimum_schedule_cover": cover_rows,
            }
        )
    return {
        "action_image_order": len(parent),
        "generator_count": len(generators),
        "complete_closure_verified": True,
        "target_rows": target_rows,
    }


def audit_d(d: int, action_table_audit: bool) -> dict:
    m = 2 * d - 2
    rooted = []
    word_preimages: dict[Word, list[tuple[Tree, tuple[int, ...]]]] = defaultdict(list)
    identity_failures = 0
    support_failures = 0
    for tree in cayley_trees(d):
        for pi in itertools.permutations(range(1, m + 1)):
            word = dps_word(tree, pi, d)
            rooted.append((tree, pi, word))
            word_preimages[word].append((tree, pi))
            identity_failures += evaluate(d, word) != tuple(range(d))
            support_failures += not support_connected(d, word)
    fiber_histogram = Counter(len(preimages) for preimages in word_preimages.values())
    words = tuple(sorted(word_preimages))
    representatives = {word: word_preimages[word][0] for word in words}
    rows = []
    global_witness = None
    max_target_choices = 0
    target_maps = {}
    for i in range(1, m):
        target_cache = {
            (tree, pi): dps_word(tree, swap_adjacent_values(pi, i), d)
            for tree, pi, _ in rooted
        }
        choice_histogram = Counter()
        multiplicity_profile_histogram = Counter()
        collision_word_count = 0
        distinct_unrooted_directed_edges = set()
        witness = None
        all_target_sources = Counter()
        for source_word, preimages in word_preimages.items():
            target_groups: dict[Word, list[tuple[Tree, tuple[int, ...], Word]]] = defaultdict(list)
            for tree, pi in preimages:
                target = target_cache[(tree, pi)]
                target_groups[target].append((tree, pi, target))
                distinct_unrooted_directed_edges.add((source_word, target))
                all_target_sources[(source_word, target)] += 1
            choices = len(target_groups)
            max_target_choices = max(max_target_choices, choices)
            choice_histogram[choices] += 1
            multiplicity_profile_histogram[tuple(sorted(map(len, target_groups.values()), reverse=True))] += 1
            if choices > 1:
                collision_word_count += 1
                ordered_targets = sorted(target_groups)
                left = min(target_groups[ordered_targets[0]], key=descriptor_key)
                right = min(target_groups[ordered_targets[1]], key=descriptor_key)
                candidate_key = (source_word, descriptor_key(left), descriptor_key(right))
                candidate = {
                    "source_word": serialize_word(source_word),
                    "rooted_source_a": {
                        "tree": serialize_tree(left[0]),
                        "pi": list(left[1]),
                        "target_word": serialize_word(left[2]),
                    },
                    "rooted_source_b": {
                        "tree": serialize_tree(right[0]),
                        "pi": list(right[1]),
                        "target_word": serialize_word(right[2]),
                    },
                    "distinct_target_count_in_root_fiber": choices,
                    "target_multiplicities": sorted(map(len, target_groups.values()), reverse=True),
                }
                if witness is None or candidate_key < witness[0]:
                    witness = candidate_key, candidate
                global_key = (d, i, candidate_key)
                if global_witness is None or global_key < global_witness[0]:
                    global_witness = global_key, {"adjacent_value_index": i, **candidate}
        row = {
            "adjacent_value_index": i,
            "rooted_demands": len(rooted),
            "unrooted_source_words": len(word_preimages),
            "distinct_unrooted_directed_edges": len(distinct_unrooted_directed_edges),
            "target_choice_count_per_source_histogram": {
                str(k): v for k, v in sorted(choice_histogram.items())
            },
            "target_multiplicity_profile_histogram": {
                str(profile): count
                for profile, count in sorted(multiplicity_profile_histogram.items())
            },
            "collision_source_words": collision_word_count,
            "descends_to_unrooted_word_function": collision_word_count == 0,
            "fixed_braid_not_refuted_by_root_fiber_collision": collision_word_count == 0,
            "arbitrary_source_independent_unrooted_map_possible": collision_word_count == 0,
            "smallest_collision_witness": None if witness is None else witness[1],
            "max_rooted_sources_per_unrooted_directed_edge": max(all_target_sources.values()),
        }
        target_maps[i] = {
            source_word: target_cache[representatives[source_word]]
            for source_word in words
        }
        row["two_source_direct_product_subgroup_obstruction"] = (
            find_subgroup_obstruction(
                d, words, representatives, target_maps[i]
            )
        )
        rows.append(row)

    generator_rows = None
    orbit_size = None
    if action_table_audit:
        generator_rows, orbit_size = connected_components_from_actions(words)
    word_index = {word: k for k, word in enumerate(words)}
    target_permutations = {
        adjacent_index: tuple(word_index[target_map[word]] for word in words)
        for adjacent_index, target_map in target_maps.items()
    }
    complete_action_image = (
        exact_action_image_and_cover(words, target_permutations) if d == 3 else None
    )
    return {
        "d": d,
        "m": m,
        "cayley_tree_count": d ** (d - 2),
        "rooted_pair_count": len(rooted),
        "z_size": len(word_preimages),
        "root_fiber_size_histogram": {str(k): v for k, v in sorted(fiber_histogram.items())},
        "identity_failures": identity_failures,
        "connected_support_failures": support_failures,
        "all_adjacent_indices_have_root_fiber_collision": all(
            row["collision_source_words"] for row in rows
        ),
        "all_adjacent_indices_have_two_source_subgroup_obstruction": all(
            row["two_source_direct_product_subgroup_obstruction"] is not None
            for row in rows
        ),
        "maximum_distinct_targets_from_one_root_fiber": max_target_choices,
        "globally_smallest_collision_witness": None if global_witness is None else global_witness[1],
        "adjacent_index_rows": rows,
        "signed_hurwitz_generator_action_tables": generator_rows,
        "signed_hurwitz_orbit_size_from_first_word": orbit_size,
        "complete_signed_hurwitz_action_image": complete_action_image,
    }


def git_commit() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"], check=True, capture_output=True, text=True
    )
    return result.stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", nargs="+", type=int, default=[3, 4])
    parser.add_argument("--output", type=Path, default=Path("fixed_braid_results.json"))
    parser.add_argument(
        "--action-table-d",
        nargs="*",
        type=int,
        default=[3, 4],
        help="ranks for which to hash every signed Hurwitz generator table",
    )
    args = parser.parse_args()
    started = time.perf_counter()
    rows = [audit_d(d, d in args.action_table_d) for d in args.d]
    payload = {
        "experiment": "M127 exact DPS fixed-braid intertwining constraints",
        "claim_tested": (
            "For every d and adjacent value i, one signed Hurwitz action word "
            "beta_(d,i), independent of rooted DPS source, maps F(T,pi) to F(T,s_i pi)."
        ),
        "verdict": (
            "REFUTED at d=3 (indeed at every adjacent index for d=3 and d=4) "
            "by a two-source direct-product generated-subgroup invariant."
        ),
        "target": "uniform rooted minimal identity sector, projected to Z_d",
        "composition_convention": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "dps_convention": "+ mirror; Cayley tree rooted at y_d",
        "vertex_labels_in_serialized_words": "1-based",
        "commit": git_commit(),
        "argv": sys.argv,
        "python": platform.python_version(),
        "nonstandard_dependencies": {},
        "deterministic": True,
        "seed": None,
        "elapsed_seconds": time.perf_counter() - started,
        "logical_implication": (
            "A common signed braid on two source words is the Hurwitz action on "
            "their coordinatewise-pair tuple in S_d x S_d, whose generated subgroup "
            "is invariant. Different source/target generated subgroups refute every "
            "fixed braid word, regardless of its length."
        ),
        "scope_warning": (
            "Finite exhaustive constraints can refute the universal fixed-braid proposition. "
            "They prove no all-edge congestion, physical gap, Gamma_0 estimate, heat-bath gap, "
            "or terminal outcome."
        ),
        "rows": rows,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
