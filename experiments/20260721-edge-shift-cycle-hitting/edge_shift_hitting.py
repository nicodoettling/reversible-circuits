#!/usr/bin/env python3
"""Monte Carlo hitting times for the graph edge-shift walk.

The pre-hit state is a finite simple undirected graph.  One step chooses an
ordered wedge (a,b,c), meaning distinct vertices with edges ab and bc,
uniformly from all ordered wedges.  If ac is already an edge, the proposed
shift would create a parallel copy of ac and the walk hits its target.
Otherwise, delete ab and add ac.

The initial graph must have every vertex on at least one simple cycle.  This
condition is deliberately *not* imposed after time zero: an edge shift can
create bridges and pendant vertices.  The vertex set, edge count, connected
component partition, and cycle rank remain invariant before absorption.

This file is self-contained and uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import multiprocessing as mp
import os
import random
import statistics
import sys
import time
from collections import Counter, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Iterator, Mapping, Sequence


Edge = tuple[int, int]
Adjacency = list[set[int]]


def canonical_edge(u: int, v: int) -> Edge:
    if u == v:
        raise ValueError("self-loops are not allowed")
    return (u, v) if u < v else (v, u)


def adjacency_from_edges(n: int, edges: Iterable[Sequence[int]]) -> Adjacency:
    if n < 1:
        raise ValueError("n must be positive")
    adjacency: Adjacency = [set() for _ in range(n)]
    seen: set[Edge] = set()
    for raw_edge in edges:
        if len(raw_edge) != 2:
            raise ValueError(f"edge must have two endpoints: {raw_edge!r}")
        u, v = int(raw_edge[0]), int(raw_edge[1])
        if not (0 <= u < n and 0 <= v < n):
            raise ValueError(f"edge {(u, v)} is outside vertex range 0..{n - 1}")
        edge = canonical_edge(u, v)
        if edge in seen:
            raise ValueError(f"duplicate edge in simple input graph: {edge}")
        seen.add(edge)
        adjacency[u].add(v)
        adjacency[v].add(u)
    return adjacency


def copy_adjacency(adjacency: Adjacency) -> Adjacency:
    return [set(neighbors) for neighbors in adjacency]


def edges_of(adjacency: Adjacency) -> list[Edge]:
    return [(u, v) for u, neighbors in enumerate(adjacency) for v in neighbors if u < v]


def edge_count(adjacency: Adjacency) -> int:
    return sum(len(neighbors) for neighbors in adjacency) // 2


def component_count(adjacency: Adjacency) -> int:
    unseen = set(range(len(adjacency)))
    count = 0
    while unseen:
        count += 1
        start = unseen.pop()
        stack = [start]
        while stack:
            vertex = stack.pop()
            for neighbor in adjacency[vertex]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    stack.append(neighbor)
    return count


def bridge_edges(adjacency: Adjacency) -> set[Edge]:
    """Return all bridges using Tarjan's DFS algorithm."""

    n = len(adjacency)
    discovery = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    bridges: set[Edge] = set()
    clock = 0

    def dfs(vertex: int) -> None:
        nonlocal clock
        discovery[vertex] = low[vertex] = clock
        clock += 1
        for neighbor in adjacency[vertex]:
            if discovery[neighbor] < 0:
                parent[neighbor] = vertex
                dfs(neighbor)
                low[vertex] = min(low[vertex], low[neighbor])
                if low[neighbor] > discovery[vertex]:
                    bridges.add(canonical_edge(vertex, neighbor))
            elif neighbor != parent[vertex]:
                low[vertex] = min(low[vertex], discovery[neighbor])

    for vertex in range(n):
        if discovery[vertex] < 0:
            dfs(vertex)
    return bridges


def vertices_on_cycles(adjacency: Adjacency) -> set[int]:
    """A vertex is on a cycle iff it touches at least one non-bridge edge."""

    bridges = bridge_edges(adjacency)
    covered: set[int] = set()
    for u, v in edges_of(adjacency):
        if (u, v) not in bridges:
            covered.add(u)
            covered.add(v)
    return covered


def validate_initial_graph(adjacency: Adjacency) -> None:
    if not adjacency:
        raise ValueError("the graph has no vertices")
    if any(not neighbors for neighbors in adjacency):
        raise ValueError("the graph has an isolated vertex")
    covered = vertices_on_cycles(adjacency)
    if len(covered) != len(adjacency):
        missing = sorted(set(range(len(adjacency))) - covered)
        raise ValueError(f"every initial vertex must lie on a cycle; missing={missing}")


def wedge_count(adjacency: Adjacency) -> int:
    return sum(len(neighbors) * (len(neighbors) - 1) for neighbors in adjacency)


def triangle_count(adjacency: Adjacency) -> int:
    total = 0
    for u, neighbors in enumerate(adjacency):
        for v in neighbors:
            if u < v:
                total += len(adjacency[u] & adjacency[v])
    return total // 3


def girth(adjacency: Adjacency) -> int | None:
    """Return the shortest simple-cycle length, or None for a forest."""

    best = math.inf
    n = len(adjacency)
    for start in range(n):
        distance = [-1] * n
        parent = [-1] * n
        distance[start] = 0
        queue: deque[int] = deque([start])
        while queue:
            vertex = queue.popleft()
            if 2 * distance[vertex] + 1 >= best:
                continue
            for neighbor in adjacency[vertex]:
                if distance[neighbor] < 0:
                    distance[neighbor] = distance[vertex] + 1
                    parent[neighbor] = vertex
                    queue.append(neighbor)
                elif parent[vertex] != neighbor:
                    best = min(best, distance[vertex] + distance[neighbor] + 1)
    return None if best == math.inf else int(best)


def fundamental_cycle_basis(adjacency: Adjacency) -> tuple[list[Edge], list[int]]:
    """Return sorted edges and a deterministic fundamental cycle basis as bitsets."""

    n = len(adjacency)
    all_edges = sorted(edges_of(adjacency))
    edge_index = {edge: index for index, edge in enumerate(all_edges)}
    parent = [-1] * n
    depth = [0] * n
    tree_edges: set[Edge] = set()
    seen = [False] * n

    for root in range(n):
        if seen[root]:
            continue
        seen[root] = True
        queue: deque[int] = deque([root])
        while queue:
            vertex = queue.popleft()
            for neighbor in sorted(adjacency[vertex]):
                if not seen[neighbor]:
                    seen[neighbor] = True
                    parent[neighbor] = vertex
                    depth[neighbor] = depth[vertex] + 1
                    tree_edges.add(canonical_edge(vertex, neighbor))
                    queue.append(neighbor)

    basis: list[int] = []
    for chord in all_edges:
        if chord in tree_edges:
            continue
        u, v = chord
        mask = 1 << edge_index[chord]
        left, right = u, v
        while depth[left] > depth[right]:
            edge = canonical_edge(left, parent[left])
            mask |= 1 << edge_index[edge]
            left = parent[left]
        while depth[right] > depth[left]:
            edge = canonical_edge(right, parent[right])
            mask |= 1 << edge_index[edge]
            right = parent[right]
        while left != right:
            left_edge = canonical_edge(left, parent[left])
            right_edge = canonical_edge(right, parent[right])
            mask |= 1 << edge_index[left_edge]
            mask |= 1 << edge_index[right_edge]
            left = parent[left]
            right = parent[right]
        basis.append(mask)

    expected_rank = len(all_edges) - n + component_count(adjacency)
    if len(basis) != expected_rank:
        raise AssertionError(f"basis rank {len(basis)} != cycle rank {expected_rank}")
    return all_edges, basis


def _simple_cycle_length_from_mask(mask: int, edges: Sequence[Edge], n: int) -> int | None:
    if not mask:
        return None
    selected_adjacency: list[list[int]] = [[] for _ in range(n)]
    selected_edges = 0
    remaining = mask
    while remaining:
        low_bit = remaining & -remaining
        index = low_bit.bit_length() - 1
        u, v = edges[index]
        selected_adjacency[u].append(v)
        selected_adjacency[v].append(u)
        selected_edges += 1
        remaining ^= low_bit

    active = [vertex for vertex, neighbors in enumerate(selected_adjacency) if neighbors]
    if selected_edges < 3 or any(len(selected_adjacency[vertex]) != 2 for vertex in active):
        return None

    seen = {active[0]}
    stack = [active[0]]
    while stack:
        vertex = stack.pop()
        for neighbor in selected_adjacency[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    return selected_edges if len(seen) == len(active) else None


def exact_simple_cycle_lengths(
    adjacency: Adjacency,
    *,
    rank_cap: int,
    element_cap: int,
) -> tuple[list[int] | None, str | None]:
    """Enumerate cycle-space elements and retain those that are simple cycles.

    Every simple cycle is a nonzero element of the binary cycle space.  This
    method costs O(2^beta), so it is exact and useful when the cycle rank beta
    is moderate, independent of the number of vertices.
    """

    edges, basis = fundamental_cycle_basis(adjacency)
    rank = len(basis)
    element_count = (1 << rank) - 1
    if rank > rank_cap:
        return None, f"cycle_rank={rank} exceeds rank_cap={rank_cap}"
    if element_count > element_cap:
        return None, f"cycle_space_elements={element_count} exceeds element_cap={element_cap}"

    lengths: list[int] = []
    current_mask = 0
    previous_gray = 0
    for value in range(1, 1 << rank):
        gray = value ^ (value >> 1)
        changed = gray ^ previous_gray
        basis_index = (changed & -changed).bit_length() - 1
        current_mask ^= basis[basis_index]
        length = _simple_cycle_length_from_mask(current_mask, edges, len(adjacency))
        if length is not None:
            lengths.append(length)
        previous_gray = gray
    lengths.sort()
    return lengths, None


def _mean(values: Sequence[int | float]) -> float | None:
    return statistics.fmean(values) if values else None


def graph_statistics(
    adjacency: Adjacency,
    *,
    exact_cycle_rank_cap: int,
    exact_cycle_element_cap: int,
) -> dict[str, Any]:
    n = len(adjacency)
    m = edge_count(adjacency)
    components = component_count(adjacency)
    rank = m - n + components
    bridges = bridge_edges(adjacency)
    covered = vertices_on_cycles(adjacency)
    _, basis = fundamental_cycle_basis(adjacency)
    basis_lengths = sorted(mask.bit_count() for mask in basis)
    simple_lengths, skip_reason = exact_simple_cycle_lengths(
        adjacency,
        rank_cap=exact_cycle_rank_cap,
        element_cap=exact_cycle_element_cap,
    )
    degrees = [len(neighbors) for neighbors in adjacency]
    simple_histogram = None
    if simple_lengths is not None:
        simple_histogram = {str(length): count for length, count in sorted(Counter(simple_lengths).items())}

    return {
        "vertex_count": n,
        "edge_count": m,
        "component_count": components,
        "cycle_rank": rank,
        "bridge_count": len(bridges),
        "cycle_covered_vertex_count": len(covered),
        "all_vertices_cycle_covered": len(covered) == n,
        "min_degree": min(degrees),
        "max_degree": max(degrees),
        "mean_degree": statistics.fmean(degrees),
        "ordered_wedge_count": wedge_count(adjacency),
        "triangle_count": triangle_count(adjacency),
        "girth": girth(adjacency),
        "fundamental_cycle_basis_lengths": basis_lengths,
        "fundamental_cycle_basis_mean_length": _mean(basis_lengths),
        "fundamental_cycle_basis_min_length": min(basis_lengths) if basis_lengths else None,
        "fundamental_cycle_basis_max_length": max(basis_lengths) if basis_lengths else None,
        "simple_cycle_count_exact": len(simple_lengths) if simple_lengths is not None else None,
        "simple_cycle_lengths_exact": simple_lengths,
        "simple_cycle_length_histogram_exact": simple_histogram,
        "simple_cycle_mean_length_exact": _mean(simple_lengths or []),
        "simple_cycle_min_length_exact": min(simple_lengths) if simple_lengths else None,
        "simple_cycle_max_length_exact": max(simple_lengths) if simple_lengths else None,
        "simple_cycle_enumeration_skipped_reason": skip_reason,
    }


def _add_edge(adjacency: Adjacency, u: int, v: int) -> None:
    if u == v or v in adjacency[u]:
        raise ValueError(f"cannot add non-simple edge {(u, v)}")
    adjacency[u].add(v)
    adjacency[v].add(u)


def make_disjoint_cycles(lengths: Sequence[int]) -> Adjacency:
    if not lengths or any(length < 3 for length in lengths):
        raise ValueError("every cycle length must be at least 3")
    n = sum(lengths)
    adjacency: Adjacency = [set() for _ in range(n)]
    offset = 0
    for length in lengths:
        for index in range(length):
            _add_edge(adjacency, offset + index, offset + ((index + 1) % length))
        offset += length
    return adjacency


def make_cycle_bouquet(lengths: Sequence[int]) -> Adjacency:
    """Cycles share exactly one central vertex and no edges."""

    if not lengths or any(length < 3 for length in lengths):
        raise ValueError("every cycle length must be at least 3")
    n = 1 + sum(length - 1 for length in lengths)
    adjacency: Adjacency = [set() for _ in range(n)]
    next_vertex = 1
    for length in lengths:
        internal = list(range(next_vertex, next_vertex + length - 1))
        next_vertex += length - 1
        cycle = [0] + internal
        for index in range(length):
            _add_edge(adjacency, cycle[index], cycle[(index + 1) % length])
    return adjacency


def make_theta(path_lengths: Sequence[int]) -> Adjacency:
    """Three internally disjoint paths between vertices 0 and 1."""

    if len(path_lengths) != 3 or any(length < 1 for length in path_lengths):
        raise ValueError("theta requires three positive path lengths")
    if sum(length == 1 for length in path_lengths) > 1:
        raise ValueError("a simple theta graph cannot have two direct endpoint paths")
    n = sum(path_lengths) - 1
    adjacency: Adjacency = [set() for _ in range(n)]
    next_vertex = 2
    for length in path_lengths:
        internal = list(range(next_vertex, next_vertex + length - 1))
        next_vertex += length - 1
        path = [0] + internal + [1]
        for left, right in zip(path, path[1:]):
            _add_edge(adjacency, left, right)
    return adjacency


def make_cycle_with_chords(n: int, cycle_rank: int, rng: random.Random) -> Adjacency:
    if n < 3:
        raise ValueError("n must be at least 3")
    maximum_rank = n * (n - 1) // 2 - n + 1
    if not 1 <= cycle_rank <= maximum_rank:
        raise ValueError(f"cycle_rank must be in 1..{maximum_rank}")

    order = list(range(n))
    rng.shuffle(order)
    adjacency: Adjacency = [set() for _ in range(n)]
    for index, vertex in enumerate(order):
        _add_edge(adjacency, vertex, order[(index + 1) % n])

    candidates = [
        (u, v)
        for u in range(n)
        for v in range(u + 1, n)
        if v not in adjacency[u]
    ]
    for u, v in rng.sample(candidates, cycle_rank - 1):
        _add_edge(adjacency, u, v)
    return adjacency


def relabel_randomly(adjacency: Adjacency, rng: random.Random) -> Adjacency:
    permutation = list(range(len(adjacency)))
    rng.shuffle(permutation)
    return adjacency_from_edges(
        len(adjacency),
        [(permutation[u], permutation[v]) for u, v in edges_of(adjacency)],
    )


def build_graph(setting: Mapping[str, Any], seed: int) -> Adjacency:
    rng = random.Random(seed)
    generator = setting["generator"]
    if generator == "cycle_with_chords":
        adjacency = make_cycle_with_chords(int(setting["n"]), int(setting["cycle_rank"]), rng)
    elif generator == "disjoint_cycles":
        adjacency = make_disjoint_cycles([int(value) for value in setting["cycle_lengths"]])
    elif generator == "cycle_bouquet":
        adjacency = make_cycle_bouquet([int(value) for value in setting["cycle_lengths"]])
    elif generator == "theta":
        adjacency = make_theta([int(value) for value in setting["path_lengths"]])
    elif generator == "edge_list":
        adjacency = adjacency_from_edges(int(setting["n"]), setting["edges"])
    else:
        raise ValueError(f"unknown graph generator: {generator!r}")

    if setting.get("random_relabel", False) and generator != "cycle_with_chords":
        adjacency = relabel_randomly(adjacency, rng)
    validate_initial_graph(adjacency)
    return adjacency


class FenwickWeights:
    def __init__(self, values: Sequence[int]) -> None:
        self.n = len(values)
        self.values = list(values)
        self.tree = [0] * (self.n + 1)
        for index, value in enumerate(values):
            self._add(index, value)

    def _add(self, index: int, delta: int) -> None:
        position = index + 1
        while position <= self.n:
            self.tree[position] += delta
            position += position & -position

    def set(self, index: int, value: int) -> None:
        delta = value - self.values[index]
        self.values[index] = value
        self._add(index, delta)

    def total(self) -> int:
        total = 0
        position = self.n
        while position:
            total += self.tree[position]
            position -= position & -position
        return total

    def sample(self, rng: random.Random) -> int:
        total = self.total()
        if total <= 0:
            raise RuntimeError("graph has no ordered wedge")
        target = rng.randrange(1, total + 1)
        index = 0
        bit = 1 << (self.n.bit_length() - 1)
        while bit:
            candidate = index + bit
            if candidate <= self.n and self.tree[candidate] < target:
                target -= self.tree[candidate]
                index = candidate
            bit >>= 1
        return index


def apply_ordered_wedge(adjacency: Adjacency, a: int, b: int, c: int) -> bool:
    """Apply (a,b,c); return True instead when it would create a parallel edge."""

    if a == c or b not in adjacency[a] or c not in adjacency[b]:
        raise ValueError(f"{(a, b, c)} is not an ordered wedge")
    if c in adjacency[a]:
        return True
    adjacency[a].remove(b)
    adjacency[b].remove(a)
    adjacency[a].add(c)
    adjacency[c].add(a)
    return False


@dataclass(frozen=True)
class WalkResult:
    hit: bool
    observed_steps: int
    hit_step: int | None
    hit_wedge: tuple[int, int, int] | None
    pre_hit_ordered_wedges: int | None
    pre_hit_triangles: int | None
    final_max_degree: int


def run_edge_shift_walk(adjacency: Adjacency, *, rng: random.Random, max_steps: int) -> WalkResult:
    graph = copy_adjacency(adjacency)
    weights = [len(neighbors) * (len(neighbors) - 1) for neighbors in graph]
    centers = FenwickWeights(weights)

    for step in range(1, max_steps + 1):
        b = centers.sample(rng)
        neighbors = sorted(graph[b])
        first = rng.randrange(len(neighbors))
        second = rng.randrange(len(neighbors) - 1)
        if second >= first:
            second += 1
        a, c = neighbors[first], neighbors[second]

        if c in graph[a]:
            return WalkResult(
                hit=True,
                observed_steps=step,
                hit_step=step,
                hit_wedge=(a, b, c),
                pre_hit_ordered_wedges=centers.total(),
                pre_hit_triangles=triangle_count(graph),
                final_max_degree=max(len(neighbors_) for neighbors_ in graph),
            )

        old_degree_b = len(graph[b])
        old_degree_c = len(graph[c])
        was_hit = apply_ordered_wedge(graph, a, b, c)
        if was_hit:
            raise AssertionError("prechecked non-hitting wedge unexpectedly hit")
        new_degree_b = old_degree_b - 1
        new_degree_c = old_degree_c + 1
        centers.set(b, new_degree_b * (new_degree_b - 1))
        centers.set(c, new_degree_c * (new_degree_c - 1))

    return WalkResult(
        hit=False,
        observed_steps=max_steps,
        hit_step=None,
        hit_wedge=None,
        pre_hit_ordered_wedges=None,
        pre_hit_triangles=None,
        final_max_degree=max(len(neighbors) for neighbors in graph),
    )


def stable_seed(*parts: object) -> int:
    payload = "\x1f".join(str(part) for part in parts).encode("utf-8")
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big")


def _split_balanced(total: int) -> tuple[int, int, int]:
    quotient, remainder = divmod(total, 3)
    values = [quotient] * 3
    for index in range(remainder):
        values[index] += 1
    values.sort()
    return tuple(values)  # type: ignore[return-value]


def expand_config(config: Mapping[str, Any]) -> list[dict[str, Any]]:
    defaults = dict(config.get("defaults", {}))
    settings: list[dict[str, Any]] = []

    def add_setting(raw: Mapping[str, Any]) -> None:
        setting = {**defaults, **dict(raw)}
        required = {"id", "generator", "graphs_per_setting", "walks_per_graph", "max_steps"}
        missing = sorted(required - setting.keys())
        if missing:
            raise ValueError(f"setting is missing fields {missing}: {setting}")
        if any(existing["id"] == setting["id"] for existing in settings):
            raise ValueError(f"duplicate setting id: {setting['id']}")
        settings.append(setting)

    for raw in config.get("settings", []):
        add_setting(raw)

    for sweep in config.get("sweeps", []):
        kind = sweep["kind"]
        common = {key: value for key, value in sweep.items() if key not in {
            "kind", "id_prefix", "total_edges_values", "cycle_count_values", "topologies",
            "n_values", "cycle_rank_values", "shapes",
        }}
        prefix = sweep["id_prefix"]
        if kind == "equal_cycles":
            for total_edges in sweep["total_edges_values"]:
                for cycle_count in sweep["cycle_count_values"]:
                    if total_edges % cycle_count or total_edges // cycle_count < 3:
                        continue
                    length = total_edges // cycle_count
                    for topology in sweep["topologies"]:
                        generator = "disjoint_cycles" if topology == "disjoint" else "cycle_bouquet"
                        add_setting({
                            **common,
                            "id": f"{prefix}-{topology}-m{total_edges}-r{cycle_count}-l{length}",
                            "generator": generator,
                            "cycle_lengths": [length] * cycle_count,
                        })
        elif kind == "cycle_with_chords":
            for n in sweep["n_values"]:
                maximum_rank = n * (n - 1) // 2 - n + 1
                for rank in sweep["cycle_rank_values"]:
                    if rank <= maximum_rank:
                        add_setting({
                            **common,
                            "id": f"{prefix}-n{n}-beta{rank}",
                            "generator": "cycle_with_chords",
                            "n": n,
                            "cycle_rank": rank,
                        })
        elif kind == "theta":
            for total_edges in sweep["total_edges_values"]:
                for shape in sweep["shapes"]:
                    if shape == "balanced":
                        lengths = _split_balanced(total_edges)
                    elif shape == "skew":
                        left = (total_edges - 1) // 2
                        lengths = (1, left, total_edges - 1 - left)
                    elif shape == "near_triangle":
                        lengths = (1, 2, total_edges - 3)
                    else:
                        raise ValueError(f"unknown theta shape: {shape}")
                    add_setting({
                        **common,
                        "id": f"{prefix}-{shape}-m{total_edges}",
                        "generator": "theta",
                        "path_lengths": list(lengths),
                    })
        else:
            raise ValueError(f"unknown sweep kind: {kind!r}")
    return settings


def config_digest(config: Mapping[str, Any]) -> str:
    canonical = json.dumps(config, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def _graph_job(job: tuple[dict[str, Any], int, int, int, str]) -> list[dict[str, Any]]:
    setting, graph_index, global_seed, exact_cycle_rank_cap, digest = job
    graph_seed = stable_seed(global_seed, setting["id"], graph_index, "graph")
    adjacency = build_graph(setting, graph_seed)
    stats = graph_statistics(
        adjacency,
        exact_cycle_rank_cap=exact_cycle_rank_cap,
        exact_cycle_element_cap=int(setting.get("exact_cycle_element_cap", 1_000_000)),
    )
    if not stats["all_vertices_cycle_covered"]:
        raise AssertionError("generator produced an invalid initial graph")

    graph_id = f"{setting['id']}/graph-{graph_index:04d}"
    common = {
        "experiment": "edge_shift_cycle_hitting",
        "config_digest": digest,
        "setting_id": setting["id"],
        "graph_id": graph_id,
        "graph_index": graph_index,
        "generator": setting["generator"],
    }
    records: list[dict[str, Any]] = [{
        "record_type": "graph_summary",
        **common,
        "graph_seed": graph_seed,
        "generator_parameters": {
            key: value
            for key, value in setting.items()
            if key not in {"graphs_per_setting", "walks_per_graph", "max_steps", "exact_cycle_element_cap"}
        },
        **stats,
    }]

    initial_edges = stats["edge_count"]
    initial_components = stats["component_count"]
    initial_rank = stats["cycle_rank"]
    max_steps = int(setting["max_steps"])
    for trial_index in range(int(setting["walks_per_graph"])):
        walk_seed = stable_seed(global_seed, setting["id"], graph_index, trial_index, "walk")
        result = run_edge_shift_walk(adjacency, rng=random.Random(walk_seed), max_steps=max_steps)
        records.append({
            "record_type": "walk_trial",
            **common,
            "trial_index": trial_index,
            "walk_seed": walk_seed,
            "walk": "uniform_ordered_wedge_edge_shift",
            "target": "proposed_parallel_edge",
            "max_steps": max_steps,
            "hit": result.hit,
            "observed_steps": result.observed_steps,
            "hit_step": result.hit_step,
            "hit_wedge": list(result.hit_wedge) if result.hit_wedge else None,
            "pre_hit_ordered_wedge_count": result.pre_hit_ordered_wedges,
            "pre_hit_triangle_count": result.pre_hit_triangles,
            "final_max_degree": result.final_max_degree,
            "invariant_edge_count": initial_edges,
            "invariant_component_count": initial_components,
            "invariant_cycle_rank": initial_rank,
        })

    records.append({
        "record_type": "graph_complete",
        **common,
        "walks_completed": int(setting["walks_per_graph"]),
    })
    return records


def sanitize_resume_file(path: Path, digest: str) -> set[tuple[str, int]]:
    """Drop incomplete graph blocks and a possibly truncated final JSON line.

    A graph is resumable only after its trailing ``graph_complete`` record was
    flushed.  Removing every current-config record for incomplete graph keys
    prevents partial trials from being counted twice after a server failure.
    """

    if not path.exists():
        return set()

    valid_records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            try:
                valid_records.append(json.loads(line))
            except json.JSONDecodeError:
                # A killed process can leave only its final line truncated.
                continue

    completed: set[tuple[str, int]] = {
        (record["setting_id"], int(record["graph_index"]))
        for record in valid_records
        if record.get("record_type") == "graph_complete" and record.get("config_digest") == digest
    }

    def keep(record: Mapping[str, Any]) -> bool:
        if record.get("config_digest") != digest or "graph_index" not in record:
            return True
        key = (str(record.get("setting_id")), int(record["graph_index"]))
        return key in completed

    temporary = path.with_suffix(path.suffix + ".resume-tmp")
    with temporary.open("w", encoding="utf-8") as handle:
        write_records(handle, [record for record in valid_records if keep(record)])
    temporary.replace(path)
    return completed


def write_records(handle: Any, records: Sequence[Mapping[str, Any]]) -> None:
    for record in records:
        handle.write(json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n")
    handle.flush()


def run_experiment(args: argparse.Namespace) -> None:
    config_path = Path(args.config).resolve()
    config = json.loads(config_path.read_text(encoding="utf-8"))
    settings = expand_config(config)
    if not settings:
        raise ValueError("configuration expands to no settings")
    digest = config_digest(config)
    global_seed = int(config.get("seed", 20260721))
    exact_rank_cap = int(config.get("exact_cycle_rank_cap", 16))
    output_path = Path(args.output or config.get("output", "results.jsonl"))
    if not output_path.is_absolute():
        output_path = (config_path.parent.parent / output_path).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if output_path.exists() and not args.resume:
        output_path.unlink()
    completed = sanitize_resume_file(output_path, digest) if args.resume else set()
    jobs = [
        (setting, graph_index, global_seed, exact_rank_cap, digest)
        for setting in settings
        for graph_index in range(int(setting["graphs_per_setting"]))
        if (setting["id"], graph_index) not in completed
    ]

    workers = args.workers
    if workers is None:
        workers = int(os.environ.get("SLURM_CPUS_PER_TASK", "0") or 0)
    if not workers:
        workers = max(1, min(os.cpu_count() or 1, len(jobs) or 1))

    metadata = {
        "record_type": "run_metadata",
        "experiment": "edge_shift_cycle_hitting",
        "config_digest": digest,
        "config_path": str(config_path),
        "seed": global_seed,
        "setting_count": len(settings),
        "pending_graph_jobs": len(jobs),
        "workers": workers,
        "python": sys.version,
        "started_unix_time": time.time(),
        "process_definition": {
            "state": "simple undirected graph until absorption",
            "proposal": "uniform ordered wedge (a,b,c) with ab and bc present",
            "non_hit_move": "delete ab and add ac",
            "hit": "ac already present, so the proposal would create a parallel edge",
            "initial_condition": "every vertex lies on at least one simple cycle",
            "initial_condition_preserved": False,
        },
    }

    mode = "a" if args.resume and output_path.exists() else "w"
    with output_path.open(mode, encoding="utf-8") as handle:
        write_records(handle, [metadata])
        if workers == 1:
            for index, job in enumerate(jobs, start=1):
                write_records(handle, _graph_job(job))
                print(f"completed graph job {index}/{len(jobs)}", file=sys.stderr)
        else:
            context = mp.get_context("spawn")
            with context.Pool(processes=workers) as pool:
                for index, records in enumerate(pool.imap(_graph_job, jobs, chunksize=1), start=1):
                    write_records(handle, records)
                    print(f"completed graph job {index}/{len(jobs)}", file=sys.stderr)

    print(json.dumps({
        "output": str(output_path),
        "config_digest": digest,
        "settings": len(settings),
        "graph_jobs_completed_now": len(jobs),
        "graph_jobs_previously_completed": len(completed),
    }, indent=2))


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, help="JSON configuration file")
    parser.add_argument("--output", help="override JSONL output path")
    parser.add_argument("--workers", type=int, help="worker processes; defaults to SLURM_CPUS_PER_TASK/CPU count")
    parser.add_argument("--resume", action="store_true", help="append and skip graph jobs with graph_complete records")
    return parser.parse_args(argv)


if __name__ == "__main__":
    run_experiment(parse_args())
