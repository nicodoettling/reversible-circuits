#!/usr/bin/env python3
"""Independent bounded convention check for frozen M175.

The clean-room closure is exactly all ordered quotient pairs at d=3.  At
d=4 it replays only M175's displayed four-positive-move physical certificate;
it does not enumerate Q_4 or its pair components.
"""

from __future__ import annotations

import itertools
import json
from collections import deque
from pathlib import Path


Edge = tuple[int, int]
Word = tuple[Edge, ...]
Perm = tuple[int, ...]


def compose(p: Perm, q: Perm) -> Perm:
    """Return p q, with (p q)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def sign_bit(p: Perm) -> int:
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) & 1


def edge_perm(d: int, e: Edge) -> Perm:
    p = list(range(d))
    p[e[0]], p[e[1]] = p[e[1]], p[e[0]]
    return tuple(p)


def rename(w: Word, p: Perm) -> Word:
    return tuple(tuple(sorted((p[a], p[b]))) for a, b in w)


def evaluate(w: Word, d: int) -> Perm:
    ans = tuple(range(d))
    for e in w:
        ans = compose(ans, edge_perm(d, e))
    return ans


def connected(w: Word, d: int) -> bool:
    adj = [set() for _ in range(d)]
    for a, b in w:
        adj[a].add(b)
        adj[b].add(a)
    seen = {0}
    todo = [0]
    while todo:
        a = todo.pop()
        for b in adj[a] - seen:
            seen.add(b)
            todo.append(b)
    return len(seen) == d


def conjugate_edge(e: Edge, by: Edge, d: int) -> Edge:
    return tuple(sorted(edge_perm(d, by)[x] for x in e))


def move(w: Word, j: int, direction: int, d: int) -> Word:
    """Apply signed right Hurwitz move R_j; j is one-based."""
    out = list(w)
    a, b = out[j - 1], out[j]
    if direction == 1:
        out[j - 1], out[j] = b, conjugate_edge(a, b, d)
    elif direction == -1:
        out[j - 1], out[j] = conjugate_edge(b, a, d), a
    else:
        raise ValueError(direction)
    return tuple(out)


def canonical(w: Word, perms: tuple[Perm, ...]) -> Word:
    return min(rename(w, p) for p in perms)


def unique_transporter(target_section: Word, raw: Word, perms: tuple[Perm, ...]) -> Perm:
    hits = [p for p in perms if rename(target_section, p) == raw]
    assert len(hits) == 1
    return hits[0]


def d3_pair_closure() -> dict:
    d = 3
    perms = tuple(itertools.permutations(range(d)))
    edges = tuple(itertools.combinations(range(d), 2))
    ident = tuple(range(d))
    physical = [
        w
        for w in itertools.product(edges, repeat=4)
        if evaluate(w, d) == ident and connected(w, d)
    ]
    reps = tuple(sorted({canonical(w, perms) for w in physical}))
    index = {w: i for i, w in enumerate(reps)}
    assert len(physical) == 24 and len(reps) == 4

    generators = tuple((j, s) for j in range(1, 4) for s in (1, -1))
    actions: list[tuple[int, ...]] = []
    labels: list[tuple[int, ...]] = []
    for j, direction in generators:
        this_action = []
        this_label = []
        for section_word in reps:
            raw = move(section_word, j, direction, d)
            target = canonical(raw, perms)
            rho = unique_transporter(target, raw, perms)
            this_action.append(index[target])
            this_label.append(sign_bit(rho))
        actions.append(tuple(this_action))
        labels.append(tuple(this_label))

    inverse_checks = 0
    for j in range(3):
        pos, neg = 2 * j, 2 * j + 1
        for a in range(len(reps)):
            b = actions[pos][a]
            assert actions[neg][b] == a
            assert labels[neg][b] == labels[pos][a]
            inverse_checks += 1

    unseen = {(a, b) for a in range(4) for b in range(4)}
    rows = []
    while unseen:
        root = min(unseen)
        potential = {root: 0}
        todo = deque([root])
        chord_bits = []
        while todo:
            x = todo.popleft()
            for action, label in zip(actions, labels):
                y = (action[x[0]], action[x[1]])
                gain = label[x[0]] ^ label[x[1]]
                if y not in potential:
                    potential[y] = potential[x] ^ gain
                    todo.append(y)
                else:
                    chord_bits.append(potential[x] ^ gain ^ potential[y])

        component = set(potential)
        unseen -= component
        rank = int(any(chord_bits))

        lifted = {(root, 0)}
        lifted_todo = deque([(root, 0)])
        while lifted_todo:
            x, v = lifted_todo.popleft()
            for action, label in zip(actions, labels):
                y = (action[x[0]], action[x[1]])
                gain = label[x[0]] ^ label[x[1]]
                state = (y, v ^ gain)
                if state not in lifted:
                    lifted.add(state)
                    lifted_todo.append(state)
        root_voltages = sorted(v for x, v in lifted if x == root)
        assert root_voltages == ([0] if rank == 0 else [0, 1])
        assert len(lifted) == len(component) * (1 << rank)
        rows.append({
            "root": list(root),
            "base_size": len(component),
            "chord_rank": rank,
            "root_voltages": root_voltages,
        })

    rows.sort(key=lambda row: row["base_size"])
    assert [(row["base_size"], row["chord_rank"]) for row in rows] == [(4, 0), (12, 0)]
    return {
        "physical_words": len(physical),
        "quotient_states": len(reps),
        "signed_inverse_edge_checks": inverse_checks,
        "ordered_pair_components": rows,
    }


def quotient_route_labels(source: Word, moves: tuple[int, ...], d: int) -> tuple[Word, list[int]]:
    perms = tuple(itertools.permutations(range(d)))
    assert canonical(source, perms) == source
    section_word = source
    local_bits = []
    for symbol in moves:
        raw = move(section_word, abs(symbol), 1 if symbol > 0 else -1, d)
        target = canonical(raw, perms)
        local_bits.append(sign_bit(unique_transporter(target, raw, perms)))
        section_word = target
    return section_word, local_bits


def d4_literal_certificate() -> dict:
    d = 4
    perms = tuple(itertools.permutations(range(d)))
    u: Word = ((0, 1), (0, 1), (0, 2), (0, 2), (0, 3), (0, 3))
    v: Word = ((0, 1), (0, 1), (0, 2), (0, 2), (1, 3), (1, 3))
    chronological = (4, 3, 5, 4)
    assert evaluate(u, d) == tuple(range(d)) and connected(u, d)
    assert evaluate(v, d) == tuple(range(d)) and connected(v, d)

    physical_rows = []
    relative = 0
    for source in (u, v):
        raw = source
        for symbol in chronological:
            raw = move(raw, symbol, 1, d)
        rho = unique_transporter(source, raw, perms)
        endpoint_section, local_bits = quotient_route_labels(source, chronological, d)
        assert endpoint_section == source
        assert (sum(local_bits) & 1) == sign_bit(rho)
        relative ^= sign_bit(rho)
        physical_rows.append({
            "source": [list(e) for e in source],
            "raw_endpoint": [list(e) for e in raw],
            "transporter_images": list(rho),
            "transporter_sign": sign_bit(rho),
            "local_canonicalization_signs": local_bits,
        })

    assert [row["transporter_images"] for row in physical_rows] == [
        [0, 1, 3, 2], [1, 0, 3, 2]
    ]
    assert [row["transporter_sign"] for row in physical_rows] == [1, 0]
    assert relative == 1
    return {
        "chronological_positive_word": list(chronological),
        "coordinates": physical_rows,
        "relative_voltage": relative,
        "quotient_pair_closes": True,
    }


def main() -> None:
    result = {
        "scope": "clean-room all d=3 ordered pairs plus literal d=4 certificate only; no Q4 closure or d=5 enumeration",
        "composition": "(p q)(x)=p(q(x)); chronological move list applied left-to-right",
        "d3": d3_pair_closure(),
        "d4_certificate": d4_literal_certificate(),
        "seed": None,
        "dependencies": {},
    }
    Path("independent_results.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
