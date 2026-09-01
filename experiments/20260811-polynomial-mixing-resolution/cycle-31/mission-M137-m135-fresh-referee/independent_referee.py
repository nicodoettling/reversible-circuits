#!/usr/bin/env python3
"""Fresh exact referee checks for frozen M135.

No M135/predecessor module or JSON output is imported.  This file independently
implements the accepted plus-mirror DPS closure, brute targets, orbit
incidence, paired subgroup closure, and the complete rank-three braid action.
The all-rank group argument is audited in ``report.md``; finite rows here fix
conventions and test the exceptional cases.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import platform
import subprocess
import time
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path


Permutation = tuple[int, ...]
Transposition = tuple[int, int]
Word = tuple[Transposition, ...]
Tree = frozenset[Transposition]


@dataclass(frozen=True)
class Stub:
    side: str
    vertex: int
    label: int


@dataclass(frozen=True)
class Arc:
    kind: str
    label: int | None = None


def multiply(p: Permutation, q: Permutation) -> Permutation:
    """Return pq with (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Permutation) -> Permutation:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def edge_map(d: int, edge: Transposition) -> Permutation:
    out = list(range(d))
    a, b = edge
    out[a], out[b] = out[b], out[a]
    return tuple(out)


def evaluate(d: int, word: Word) -> Permutation:
    value = tuple(range(d))
    for edge in word:
        value = multiply(value, edge_map(d, edge))
    return value


def relabel_edge(edge: Transposition, rho: Permutation) -> Transposition:
    return tuple(sorted((rho[edge[0]], rho[edge[1]])))


def relabel_word(word: Word, rho: Permutation) -> Word:
    return tuple(relabel_edge(edge, rho) for edge in word)


def conjugate_edge(edge: Transposition, by: Transposition) -> Transposition:
    a, b = edge
    x, y = by

    def image(z: int) -> int:
        if z == x:
            return y
        if z == y:
            return x
        return z

    return tuple(sorted((image(a), image(b))))


def signed_hurwitz(word: Word, slot: int, direction: int) -> Word:
    a, b = word[slot : slot + 2]
    out = list(word)
    if direction == 1:
        out[slot : slot + 2] = (b, conjugate_edge(a, b))
    elif direction == -1:
        out[slot : slot + 2] = (conjugate_edge(b, a), a)
    else:
        raise ValueError(direction)
    return tuple(out)


def is_connected(d: int, word: Word) -> bool:
    adjacency = [set() for _ in range(d)]
    for a, b in word:
        adjacency[a].add(b)
        adjacency[b].add(a)
    reached = {0}
    stack = [0]
    while stack:
        v = stack.pop()
        for u in adjacency[v] - reached:
            reached.add(u)
            stack.append(u)
    return len(reached) == d


def brute_target(d: int) -> tuple[Word, ...]:
    edges = tuple(itertools.combinations(range(d), 2))
    identity = tuple(range(d))
    m = 2 * d - 2
    return tuple(
        word
        for word in itertools.product(edges, repeat=m)
        if evaluate(d, word) == identity and is_connected(d, word)
    )


def prufer_trees(d: int):
    if d == 2:
        yield frozenset({(0, 1)})
        return
    for code in itertools.product(range(d), repeat=d - 2):
        degree = [1] * d
        for v in code:
            degree[v] += 1
        edges: list[Transposition] = []
        for v in code:
            leaf = next(x for x in range(d) if degree[x] == 1)
            edges.append(tuple(sorted((leaf, v))))
            degree[leaf] -= 1
            degree[v] -= 1
        edges.append(tuple(x for x in range(d) if degree[x] == 1))
        yield frozenset(edges)


def parents_toward_root(tree: Tree, root: int) -> dict[int, int]:
    adjacency = {v: [] for v in range(root + 1)}
    for a, b in tree:
        adjacency[a].append(b)
        adjacency[b].append(a)
    parent = {root: -1}
    stack = [root]
    while stack:
        v = stack.pop()
        for u in adjacency[v]:
            if u not in parent:
                parent[u] = v
                stack.append(u)
    return parent


def hairy_tree(tree: Tree, order: tuple[int, ...], d: int):
    """Return label incidences and the first black endpoint of each label."""
    root = d - 1
    parent = parents_toward_root(tree, root)
    incidence: dict[tuple[str, int], dict[int, tuple[str, int]]] = defaultdict(dict)
    first_black: dict[int, int] = {}
    for black in range(root):
        labels = order[2 * black : 2 * black + 2]
        for label, white in ((labels[0], black), (labels[1], parent[black])):
            bnode = ("b", black)
            wnode = ("w", white)
            incidence[bnode][label] = wnode
            incidence[wnode][label] = bnode
            first_black[label] = black
    return incidence, first_black


def contour(incidence, d: int) -> list[Stub | Arc]:
    """Walk the cyclic hairy boundary from the conventional root gap."""
    m = 2 * d - 2
    start = (("w", 0), 0)
    state = start
    visited = set()
    tokens: list[Stub | Arc] = []
    while state not in visited:
        visited.add(state)
        vertex, incoming = state
        step = 1 if vertex[0] == "w" else -1
        label = (incoming + step) % m
        if label in incidence[vertex]:
            neighbor = incidence[vertex][label]
            tokens.append(Arc("tree", label))
            state = (neighbor, label)
        else:
            tokens.append(Stub(vertex[0], vertex[1], label))
            state = (vertex, label)
    assert state == start
    assert len(tokens) == (2 * d - 1) * m
    return tokens


def close_contour(tokens: list[Stub | Arc], d: int) -> dict[int, int]:
    """Perform the intrinsic noncrossing white-black closure."""
    work = list(tokens)
    second_black: dict[int, int] = {}
    while True:
        stubs = [j for j, token in enumerate(work) if isinstance(token, Stub)]
        chosen = None
        for k, white_pos in enumerate(stubs):
            black_pos = stubs[(k + 1) % len(stubs)]
            if work[white_pos].side == "w" and work[black_pos].side == "b":
                chosen = (white_pos, black_pos)
                break
        if chosen is None:
            break
        white_pos, black_pos = chosen
        work = work[white_pos:] + work[:white_pos]
        black_pos = (black_pos - white_pos) % len(work)
        white = work[0]
        black = work[black_pos]
        assert isinstance(white, Stub) and isinstance(black, Stub)
        assert white.label == black.label
        distance = sum(isinstance(token, Arc) for token in work[1:black_pos])
        assert distance in (1, 3)
        if distance == 3:
            assert white.label not in second_black
            second_black[white.label] = black.vertex
        work = [Arc("closure")] + work[black_pos + 1 :]
    survivors = [token for token in work if isinstance(token, Stub)]
    assert len(survivors) == 2 * d - 2
    assert all(stub.side == "w" for stub in survivors)
    return second_black


def dps_image(tree: Tree, order: tuple[int, ...], d: int) -> Word:
    incidence, first_black = hairy_tree(tree, order, d)
    second_black = close_contour(contour(incidence, d), d)
    root = d - 1
    word = []
    for label in range(2 * d - 2):
        edge = tuple(sorted((first_black[label], second_black.get(label, root))))
        assert edge[0] != edge[1]
        word.append(edge)
    return tuple(word)


def adjacent_value_swap(order: tuple[int, ...], i: int) -> tuple[int, ...]:
    return tuple(i + 1 if x == i else i if x == i + 1 else x for x in order)


def reconstruct_rank(d: int):
    m = 2 * d - 2
    fibers: dict[Word, list[tuple[Tree, tuple[int, ...]]]] = defaultdict(list)
    for tree in prufer_trees(d):
        for order in itertools.permutations(range(m)):
            word = dps_image(tree, order, d)
            assert evaluate(d, word) == tuple(range(d))
            assert is_connected(d, word)
            fibers[word].append((tree, order))
    brute = brute_target(d)
    assert set(brute) == set(fibers)
    assert set(map(len, fibers.values())) == {d}
    words = tuple(sorted(brute))
    index = {word: j for j, word in enumerate(words)}
    tau: dict[int, tuple[int, ...]] = {}
    for i in range(m - 1):
        image = []
        for word in words:
            targets = {
                dps_image(tree, adjacent_value_swap(order, i), d)
                for tree, order in fibers[word]
            }
            assert len(targets) == 1
            image.append(index[next(iter(targets))])
        assert len(set(image)) == len(words)
        assert all(image[image[j]] == j for j in range(len(words)))
        tau[i] = tuple(image)
    return words, index, fibers, tau


def canonical(word: Word, group: tuple[Permutation, ...]) -> Word:
    return min(relabel_word(word, rho) for rho in group)


def orbit_blocks(words: tuple[Word, ...], group: tuple[Permutation, ...]):
    blocks: dict[Word, list[int]] = defaultdict(list)
    for j, word in enumerate(words):
        blocks[canonical(word, group)].append(j)
    return blocks


def generated_pair_group(d: int, first: Word, second: Word):
    identity = tuple(range(d))
    one = (identity, identity)
    generators = tuple(
        (edge_map(d, a), edge_map(d, b)) for a, b in zip(first, second)
    )
    reached = {one}
    queue = deque([one])
    while queue:
        p, q = queue.popleft()
        for a, b in generators:
            nxt = (multiply(p, a), multiply(q, b))
            if nxt not in reached:
                reached.add(nxt)
                queue.append(nxt)
    return frozenset(reached)


def sign(p: Permutation) -> int:
    inversions = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inversions % 2 else 1


def conjugation_graph(group: tuple[Permutation, ...], rho: Permutation):
    rho_inv = inverse(rho)
    return frozenset((p, multiply(multiply(rho, p), rho_inv)) for p in group)


def matching(edges, left_vertices, right_vertices, active):
    adjacency = {left: [] for left in left_vertices}
    for edge_id in active:
        left, right = edges[edge_id]
        adjacency[left].append((right, edge_id))
    occupied: dict[Word, tuple[Word, int]] = {}

    def augment(left, seen):
        for right, edge_id in adjacency[left]:
            if right in seen:
                continue
            seen.add(right)
            if right not in occupied or augment(occupied[right][0], seen):
                occupied[right] = (left, edge_id)
                return True
        return False

    assert all(augment(left, set()) for left in left_vertices)
    assert len(occupied) == len(right_vertices)
    return {edge_id for _left, edge_id in occupied.values()}


def decompose_regular_bipartite(edges, degree):
    left_vertices = tuple(sorted({left for left, _ in edges}))
    right_vertices = tuple(sorted({right for _, right in edges}))
    remaining = set(range(len(edges)))
    colors: dict[int, int] = {}
    for color in range(degree):
        chosen = matching(edges, left_vertices, right_vertices, remaining)
        for edge_id in chosen:
            colors[edge_id] = color
        remaining.difference_update(chosen)
    assert not remaining
    return colors, left_vertices, right_vertices


def compose_action(left: tuple[int, ...], right: tuple[int, ...]):
    return tuple(left[right[j]] for j in range(len(right)))


def rank_three_action(words, index, tau):
    generators = tuple(
        tuple(index[signed_hurwitz(word, slot, direction)] for word in words)
        for slot in range(len(words[0]) - 1)
        for direction in (1, -1)
    )
    identity = tuple(range(len(words)))
    actions = {identity}
    queue = deque([identity])
    while queue:
        action = queue.popleft()
        for generator in generators:
            nxt = compose_action(generator, action)
            if nxt not in actions:
                actions.add(nxt)
                queue.append(nxt)
    full = (1 << len(words)) - 1
    rows = []
    for i, target in tau.items():
        masks = {
            sum(1 << source for source in range(len(words)) if action[source] == target[source])
            for action in actions
        }
        masks.discard(0)
        frontier = {0}
        sizes = [1]
        minimum = None
        for depth in range(1, len(words) + 1):
            frontier = {old | mask for old in frontier for mask in masks}
            sizes.append(len(frontier))
            if full in frontier:
                minimum = depth
                break
        rows.append(
            {
                "adjacent_index": i + 1,
                "action_image_order": len(actions),
                "agreement_masks": len(masks),
                "maximum_agreement": max(mask.bit_count() for mask in masks),
                "minimum_schedule_cover": minimum,
                "union_frontier_sizes": sizes,
            }
        )
    return rows


def audit_rank(d: int):
    words, index, fibers, tau = reconstruct_rank(d)
    permutations = tuple(itertools.permutations(range(d)))
    root_group = tuple(p for p in permutations if p[d - 1] == d - 1)
    global_blocks = orbit_blocks(words, permutations)
    root_blocks = orbit_blocks(words, root_group)
    global_key = {source: canonical(word, permutations) for source, word in enumerate(words)}
    root_key = {source: canonical(word, root_group) for source, word in enumerate(words)}

    free_global_failures = sum(
        relabel_word(word, rho) == word
        for word in words
        for rho in permutations
        if rho != tuple(range(d))
    )
    free_root_failures = sum(
        relabel_word(word, rho) == word
        for word in words
        for rho in root_group
        if rho != tuple(range(d))
    )
    h_orbits_per_g = Counter()
    for block in global_blocks.values():
        h_orbits_per_g[len({root_key[source] for source in block})] += 1

    row = {
        "d": d,
        "m": 2 * d - 2,
        "brute_z_size": len(words),
        "dps_image_equals_brute": True,
        "rooted_coordinates": sum(map(len, fibers.values())),
        "root_fiber_histogram": dict(sorted(Counter(map(len, fibers.values())).items())),
        "global_orbits": len(global_blocks),
        "global_orbit_size_histogram": dict(sorted(Counter(map(len, global_blocks.values())).items())),
        "root_stabilizer_orbits": len(root_blocks),
        "root_orbit_size_histogram": dict(sorted(Counter(map(len, root_blocks.values())).items())),
        "nontrivial_global_stabilizers": free_global_failures,
        "nontrivial_root_stabilizers": free_root_failures,
        "h_orbits_per_g_orbit_histogram": dict(sorted(h_orbits_per_g.items())),
        "adjacent_rows": [],
    }

    pair_group_cache = {}

    def pair_group(a, b):
        key = (a, b)
        if key not in pair_group_cache:
            pair_group_cache[key] = generated_pair_group(d, words[a], words[b])
        return pair_group_cache[key]

    for i, target in tau.items():
        h_failures = 0
        g_failures = 0
        for source, word in enumerate(words):
            for rho in permutations:
                conjugate_source = index[relabel_word(word, rho)]
                lhs = words[target[conjugate_source]]
                rhs = relabel_word(words[target[source]], rho)
                if lhs != rhs:
                    g_failures += 1
                    if rho in root_group:
                        h_failures += 1

        edge_rows = []
        edge_hkeys = []
        for hkey, block in root_blocks.items():
            target_hkeys = {root_key[target[source]] for source in block}
            assert len(target_hkeys) == 1
            representative = block[0]
            edge_rows.append((global_key[representative], global_key[target[representative]]))
            edge_hkeys.append(hkey)
        colors, left_vertices, right_vertices = decompose_regular_bipartite(edge_rows, d)
        left_degrees = Counter(left for left, _ in edge_rows)
        right_degrees = Counter(right for _, right in edge_rows)
        color_sources: dict[int, list[int]] = defaultdict(list)
        for edge_id, color in colors.items():
            color_sources[color].extend(root_blocks[edge_hkeys[edge_id]])

        adjacent = {
            "adjacent_index": i + 1,
            "root_stabilizer_equivariance_failures": h_failures,
            "full_group_equivariance_failures": g_failures,
            "incidence_edges": len(edge_rows),
            "left_vertices": len(left_vertices),
            "right_vertices": len(right_vertices),
            "left_degree_histogram": dict(sorted(Counter(left_degrees.values()).items())),
            "right_degree_histogram": dict(sorted(Counter(right_degrees.values()).items())),
            "edge_colors": len(set(colors.values())),
            "color_size_histogram": dict(sorted(Counter(map(len, color_sources.values())).items())),
        }

        if d == 3:
            color_conflicts = 0
            for sources in color_sources.values():
                for offset, a in enumerate(sources):
                    for b in sources[offset + 1 :]:
                        if pair_group(a, b) != pair_group(target[a], target[b]):
                            color_conflicts += 1

            conflict_adjacency = [set() for _ in words]
            dichotomy_failures = 0
            parity_diagonal = frozenset(
                (p, q) for p in permutations for q in permutations if sign(p) == sign(q)
            )
            for a in range(len(words)):
                for b in range(a + 1, len(words)):
                    before = pair_group(a, b)
                    after = pair_group(target[a], target[b])
                    if before != after:
                        conflict_adjacency[a].add(b)
                        conflict_adjacency[b].add(a)
                    conjugators = [
                        rho for rho in permutations if relabel_word(words[a], rho) == words[b]
                    ]
                    if conjugators:
                        expected = conjugation_graph(permutations, conjugators[0])
                    else:
                        expected = parity_diagonal
                    if before != expected:
                        dichotomy_failures += 1
            triangles = [
                (a, b, c)
                for a in range(len(words))
                for b in conflict_adjacency[a]
                if b > a
                for c in conflict_adjacency[a].intersection(conflict_adjacency[b])
                if c > b
            ]
            adjacent.update(
                {
                    "color_pair_conflicts": color_conflicts,
                    "conflict_edges": sum(map(len, conflict_adjacency)) // 2,
                    "conflict_triangle_found": bool(triangles),
                    "d3_goursat_dichotomy_failures": dichotomy_failures,
                    "matching_colors_automatically_realizable": False,
                }
            )
        row["adjacent_rows"].append(adjacent)

    if d == 3:
        row["complete_action_cover"] = rank_three_action(words, index, tau)
    if d == 4:
        A, B, C, D, E = (0, 1), (0, 2), (2, 3), (1, 2), (1, 3)
        x = (A, B, B, A, C, C)
        y = (A, B, B, C, A, C)
        xp = (A, D, B, E, D, C)
        yp = (A, D, B, C, E, C)
        source_group = generated_pair_group(4, x, y)
        target_group = generated_pair_group(4, xp, yp)
        identity = tuple(range(4))
        double_transpositions = (
            multiply(edge_map(4, (0, 1)), edge_map(4, (2, 3))),
            multiply(edge_map(4, (0, 2)), edge_map(4, (1, 3))),
            multiply(edge_map(4, (0, 3)), edge_map(4, (1, 2))),
        )
        v4 = (identity,) + double_transpositions
        v4_diagonal_product = frozenset(
            (multiply(n1, g), multiply(n2, g))
            for n1 in v4
            for n2 in v4
            for g in permutations
        )
        parity_diagonal = frozenset(
            (p, q) for p in permutations for q in permutations if sign(p) == sign(q)
        )
        row["rank_four_exception"] = {
            "all_words_in_brute_z4": all(word in index for word in (x, y, xp, yp)),
            "tau1_endpoints_match": words[tau[0][index[x]]] == xp and words[tau[0][index[y]]] == yp,
            "sources_globally_conjugate": canonical(x, permutations) == canonical(y, permutations),
            "targets_globally_conjugate": canonical(xp, permutations) == canonical(yp, permutations),
            "source_pair_group_order": len(source_group),
            "target_pair_group_order": len(target_group),
            "source_equals_v4_diagonal_product": source_group == v4_diagonal_product,
            "target_equals_parity_diagonal": target_group == parity_diagonal,
            "singleton_bound": len(words),
            "d_to_six": d**6,
            "singleton_patch_valid": len(words) < d**6,
        }
    return row


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    start = time.perf_counter()
    mission = Path(__file__).resolve().parent
    run_root = mission.parents[1]
    frozen = run_root / "cycle-30" / "mission-M135-conflict-coloring-realization"
    expected = {
        "report.md": "2d56c7e409b64f691309e950cc88aca471bfc68f84bc93f55d5d3a24b6974455",
        "orbit_incidence_reduction.md": "499fe5a0fd829f0fad88283e7592420e5ddbb3b0c8f89460a139f13928d4895c",
        "conflict_coloring_audit.py": "79ed378ae7fd7543c16bf12a1fa51e0144b817a938c91de196be960a2e6ad540",
        "results.json": "4a7c885629399f01805d49c96f99e65612f9d7c9fbf745becd285dd96c1c30b9",
        "freeze_manifest.md": "6428246337bd3c8ffc3228754e5aa6b2ee2b407d0f842421079d7798ade58541",
        "SHA256SUMS": "8d7ca3afbab24be7b1552b433e9f0f0260efbbb658af4bd66cccd676452a5358",
    }
    observed = {name: file_sha256(frozen / name) for name in expected}
    rows = [audit_rank(3), audit_rank(4)]
    payload = {
        "experiment": "M137 fresh independent referee of frozen M135",
        "target": "uniform physical Z_d; no Markov-chain gap claim",
        "composition_convention": "(pq)(x)=p(q(x)); displayed factors multiply left-to-right",
        "seed": None,
        "python": platform.python_version(),
        "dependencies": {},
        "repository_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": "python3 -B independent_referee.py",
        "frozen_hashes": {
            name: {"expected": expected[name], "observed": observed[name], "match": observed[name] == expected[name]}
            for name in expected
        },
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - start,
        "verdict": "ACCEPT",
        "material_numbered_objections": [],
    }
    assert all(row["match"] for row in payload["frozen_hashes"].values())
    d3, d4 = rows
    assert d3["brute_z_size"] == 24 and d4["brute_z_size"] == 2880
    assert all(row["root_stabilizer_equivariance_failures"] == 0 for rank in rows for row in rank["adjacent_rows"])
    assert all(row["color_pair_conflicts"] == 0 for row in d3["adjacent_rows"])
    assert all(row["conflict_edges"] == 80 and row["conflict_triangle_found"] for row in d3["adjacent_rows"])
    assert all(row["d3_goursat_dichotomy_failures"] == 0 for row in d3["adjacent_rows"])
    assert all(row["action_image_order"] == 216 for row in d3["complete_action_cover"])
    assert all(row["maximum_agreement"] == 6 and row["minimum_schedule_cover"] == 5 for row in d3["complete_action_cover"])
    assert d4["rank_four_exception"]["source_pair_group_order"] == 96
    assert d4["rank_four_exception"]["target_pair_group_order"] == 288
    assert d4["rank_four_exception"]["singleton_patch_valid"]
    output = mission / "independent_results.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"elapsed_seconds": payload["elapsed_seconds"], "output": str(output), "verdict": payload["verdict"]}, sort_keys=True))


if __name__ == "__main__":
    main()
