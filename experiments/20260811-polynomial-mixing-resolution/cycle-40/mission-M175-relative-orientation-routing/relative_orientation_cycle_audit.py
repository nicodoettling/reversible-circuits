#!/usr/bin/env python3
"""Bounded exact audit for the M175 relative-orientation cycle criterion.

Only d=3,4 are enumerated.  The script reconstructs the physical quotient,
the local signed root-orientation edge cocycle, a synchronized-coboundary
ansatz, and all ordered-pair diagonal components.  It imports no predecessor
module or result file.
"""

from __future__ import annotations

import itertools
import json
import platform
from collections import Counter, deque
from pathlib import Path


def identity(n: int) -> tuple[int, ...]:
    return tuple(range(n))


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return pq, so (pq)(x)=p(q(x))."""
    return tuple(p[q[i]] for i in range(len(p)))


def perm_sign_bit(p: tuple[int, ...]) -> int:
    return sum(
        p[i] > p[j]
        for i in range(len(p))
        for j in range(i + 1, len(p))
    ) & 1


def transposition(n: int, edge: tuple[int, int]) -> tuple[int, ...]:
    p = list(range(n))
    a, b = edge
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def relabel_edge(edge: tuple[int, int], rho: tuple[int, ...]) -> tuple[int, int]:
    return tuple(sorted((rho[edge[0]], rho[edge[1]])))


def relabel_word(
    word: tuple[tuple[int, int], ...], rho: tuple[int, ...]
) -> tuple[tuple[int, int], ...]:
    return tuple(relabel_edge(edge, rho) for edge in word)


def evaluate(word: tuple[tuple[int, int], ...], d: int) -> tuple[int, ...]:
    value = identity(d)
    for edge in word:
        value = compose(value, transposition(d, edge))
    return value


def connected(word: tuple[tuple[int, int], ...], d: int) -> bool:
    adjacency = [set() for _ in range(d)]
    for a, b in word:
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen = {0}
    todo = [0]
    while todo:
        u = todo.pop()
        for v in adjacency[u] - seen:
            seen.add(v)
            todo.append(v)
    return len(seen) == d


def conjugate_edge(
    edge: tuple[int, int], by_edge: tuple[int, int]
) -> tuple[int, int]:
    d = max(max(edge), max(by_edge)) + 1
    return relabel_edge(edge, transposition(d, by_edge))


def hurwitz(
    word: tuple[tuple[int, int], ...], slot: int, direction: int
) -> tuple[tuple[int, int], ...]:
    out = list(word)
    a, b = out[slot], out[slot + 1]
    if direction == 1:
        out[slot], out[slot + 1] = b, conjugate_edge(a, b)
    else:
        out[slot], out[slot + 1] = conjugate_edge(b, a), a
    return tuple(out)


def canonical(
    word: tuple[tuple[int, int], ...], relabelings: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, int], ...]:
    return min(relabel_word(word, rho) for rho in relabelings)


def quotient_and_local_cocycle(d: int):
    edges = tuple(itertools.combinations(range(d), 2))
    relabelings = tuple(itertools.permutations(range(d)))
    quotient = set()
    physical_count = 0
    for word in itertools.product(edges, repeat=2 * d - 2):
        if evaluate(word, d) == identity(d) and connected(word, d):
            physical_count += 1
            quotient.add(canonical(word, relabelings))
    states = tuple(sorted(quotient))
    assert physical_count == len(states) * len(relabelings)
    index = {word: i for i, word in enumerate(states)}

    generators = tuple(
        (slot, direction)
        for slot in range(2 * d - 3)
        for direction in (1, -1)
    )
    actions: list[tuple[int, ...]] = []
    labels: list[tuple[int, ...]] = []
    for slot, direction in generators:
        action = []
        label = []
        for state in states:
            raw = hurwitz(state, slot, direction)
            target = canonical(raw, relabelings)
            transports = [
                rho for rho in relabelings if relabel_word(target, rho) == raw
            ]
            assert len(transports) == 1
            action.append(index[target])
            label.append(perm_sign_bit(transports[0]))
        actions.append(tuple(action))
        labels.append(tuple(label))

    for slot in range(2 * d - 3):
        pos, neg = 2 * slot, 2 * slot + 1
        for q in range(len(states)):
            r = actions[pos][q]
            assert actions[neg][r] == q
            assert labels[neg][r] == labels[pos][q]
    return physical_count, states, generators, tuple(actions), tuple(labels)


def gf2_rank(rows: list[int]) -> int:
    pivots: dict[int, int] = {}
    for row in rows:
        x = row
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return len(pivots)


def gf2_consistent(equations: list[tuple[int, int]], variable_count: int):
    """Return consistency/rank for coefficient bitmask and rhs equations."""
    pivots: dict[int, tuple[int, int]] = {}
    for coeff, rhs in equations:
        x, b = coeff, rhs
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                y, c = pivots[p]
                x ^= y
                b ^= c
            else:
                pivots[p] = (x, b)
                break
        if x == 0 and b:
            return False, len(pivots)
    assert all(p < variable_count for p in pivots)
    return True, len(pivots)


def synchronized_coboundary_test(generators, actions, labels):
    """Test l_j(q)=theta(q)+theta(R_j q)+c_j over F_2."""
    n = len(actions[0])
    slot_count = max(slot for slot, _ in generators) + 1
    equations = []
    for (slot, _), action, label in zip(generators, actions, labels):
        for q, r in enumerate(action):
            coeff = (1 << q) ^ (1 << r) ^ (1 << (n + slot))
            equations.append((coeff, label[q]))
    ok, rank = gf2_consistent(equations, n + slot_count)
    return {
        "consistent": ok,
        "equations": len(equations),
        "variables": n + slot_count,
        "rank_before_contradiction_or_full_rank": rank,
        "meaning": "edge label is vertex coboundary plus a generator-only bit",
    }


def pair_component_audit(generators, actions, labels):
    """Exhaust base and relative-orientation components on ordered pairs."""
    n = len(actions[0])
    points = [(a, b) for a in range(n) for b in range(n)]
    unvisited = set(points)
    component_rows = []
    first_nonzero_cycle = None

    while unvisited:
        seed = min(unvisited)
        base_seen = {seed}
        parent: dict[tuple[int, int], tuple[tuple[int, int], int] | None] = {seed: None}
        potential = {seed: 0}
        todo = deque([seed])
        cycle_labels = []
        witness = None
        while todo:
            point = todo.popleft()
            for gen_index, (action, label) in enumerate(zip(actions, labels)):
                nxt = (action[point[0]], action[point[1]])
                edge_label = label[point[0]] ^ label[point[1]]
                if nxt not in base_seen:
                    base_seen.add(nxt)
                    parent[nxt] = (point, gen_index)
                    potential[nxt] = potential[point] ^ edge_label
                    todo.append(nxt)
                else:
                    cycle_voltage = potential[point] ^ edge_label ^ potential[nxt]
                    cycle_labels.append(cycle_voltage)
                    if cycle_voltage and witness is None:
                        witness = (point, gen_index, nxt)
        unvisited.difference_update(base_seen)
        rank = gf2_rank(cycle_labels)

        augmented_seen = {(seed, 0)}
        augmented_todo = deque([(seed, 0)])
        while augmented_todo:
            point, voltage = augmented_todo.popleft()
            for action, label in zip(actions, labels):
                nxt = (action[point[0]], action[point[1]])
                edge_label = label[point[0]] ^ label[point[1]]
                state = (nxt, voltage ^ edge_label)
                if state not in augmented_seen:
                    augmented_seen.add(state)
                    augmented_todo.append(state)
        augmented_base = {point for point, _ in augmented_seen}
        augmented_stabilizer = {
            voltage for point, voltage in augmented_seen if point == seed
        }
        assert augmented_base == base_seen
        assert len(augmented_stabilizer) == (1 << rank)
        assert len(augmented_seen) == len(base_seen) * (1 << rank)

        component_rows.append(
            {
                "seed": list(seed),
                "base_size": len(base_seen),
                "relative_voltage_rank": rank,
                "orientation_lift_component_size": len(augmented_seen),
                "augmented_bfs_cross_check": True,
            }
        )

        if witness is not None and first_nonzero_cycle is None:
            point, gen_index, nxt = witness

            def tree_word(vertex):
                out = []
                while parent[vertex] is not None:
                    prev, gen = parent[vertex]
                    slot, direction = generators[gen]
                    out.append(direction * (slot + 1))
                    vertex = prev
                return tuple(reversed(out))

            slot, direction = generators[gen_index]
            edge_symbol = direction * (slot + 1)
            closed_word = (
                tree_word(point)
                + (edge_symbol,)
                + tuple(-x for x in reversed(tree_word(nxt)))
            )

            replay_point = seed
            replay_voltage = 0
            generator_index = {
                direction * (slot + 1): i
                for i, (slot, direction) in enumerate(generators)
            }
            for symbol in closed_word:
                i = generator_index[symbol]
                replay_voltage ^= labels[i][replay_point[0]] ^ labels[i][replay_point[1]]
                replay_point = (actions[i][replay_point[0]], actions[i][replay_point[1]])
            assert replay_point == seed and replay_voltage == 1

            first_nonzero_cycle = {
                "component_seed": list(seed),
                "edge_from": list(point),
                "edge_generator": edge_symbol,
                "edge_to": list(nxt),
                "closed_signed_generator_word": list(closed_word),
                "direct_replay_endpoint": list(replay_point),
                "direct_replay_voltage": replay_voltage,
                "relative_voltage": 1,
            }

    hist = Counter((row["base_size"], row["relative_voltage_rank"]) for row in component_rows)
    return {
        "ordered_pairs": n * n,
        "component_count": len(component_rows),
        "augmented_bfs_cross_check_all": all(
            row["augmented_bfs_cross_check"] for row in component_rows
        ),
        "component_size_voltage_rank_histogram": [
            {"base_size": size, "rank": rank, "count": count}
            for (size, rank), count in sorted(hist.items())
        ],
        "all_pair_stabilizer_voltages_trivial": all(
            row["relative_voltage_rank"] == 0 for row in component_rows
        ),
        "first_nonzero_cycle_certificate": first_nonzero_cycle,
    }


def replay_pair_word(seed, word, generators, actions, labels):
    generator_index = {
        direction * (slot + 1): i
        for i, (slot, direction) in enumerate(generators)
    }
    point = seed
    voltage = 0
    for symbol in word:
        i = generator_index[symbol]
        voltage ^= labels[i][point[0]] ^ labels[i][point[1]]
        point = (actions[i][point[0]], actions[i][point[1]])
    return point, voltage


def main():
    rows = []
    for d in (3, 4):
        physical_count, states, generators, actions, labels = quotient_and_local_cocycle(d)
        pair_row = pair_component_audit(generators, actions, labels)
        if d == 4:
            seed = (0, 1)
            word = (4, 3, 5, 4)
            endpoint, voltage = replay_pair_word(
                seed, word, generators, actions, labels
            )
            assert endpoint == seed and voltage == 1
            relabelings = tuple(itertools.permutations(range(d)))
            transporters = []
            for index in seed:
                raw = states[index]
                for symbol in word:
                    raw = hurwitz(raw, abs(symbol) - 1, 1 if symbol > 0 else -1)
                found = [
                    rho
                    for rho in relabelings
                    if relabel_word(states[index], rho) == raw
                ]
                assert len(found) == 1
                transporters.append({
                    "permutation_images": list(found[0]),
                    "sign_bit": perm_sign_bit(found[0]),
                })
            assert [row["sign_bit"] for row in transporters] == [1, 0]
            pair_row["short_positive_certificate"] = {
                "source_quotient_indices": list(seed),
                "source_canonical_words": [
                    [list(edge) for edge in states[i]] for i in seed
                ],
                "chronological_positive_word": list(word),
                "endpoint_quotient_indices": list(endpoint),
                "literal_transporters": transporters,
                "relative_voltage": voltage,
            }
        rows.append({
            "d": d,
            "physical_count": physical_count,
            "quotient_count": len(states),
            "signed_generator_count": len(actions),
            "synchronized_coboundary": synchronized_coboundary_test(
                generators, actions, labels
            ),
            "ordered_pair_cycle_space": pair_row,
        })
    result = {
        "experiment": "M175 bounded relative-orientation cycle audit",
        "scope": "exact d=3,4 only; no d=5 quotient enumeration",
        "composition_convention": "(pq)(x)=p(q(x)); displayed factors multiply left-to-right",
        "hurwitz_convention": "R_j(a,b)=(b,b^{-1}ab)",
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "rows": rows,
    }
    Path("results.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
