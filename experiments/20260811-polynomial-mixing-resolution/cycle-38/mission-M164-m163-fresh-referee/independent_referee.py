#!/usr/bin/env python3
"""Clean-room finite referee for frozen M163.

This script reads the M163 payload only to verify hashes.  It imports and
executes no predecessor code.  All permutation, Hurwitz, quotient, voltage,
orbit, and S4/V4 projection primitives below are independent.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import platform
import subprocess
from collections import Counter, defaultdict, deque
from pathlib import Path


EXPECTED_M163 = {
    "report.md": "ff5f33859a3ff57d6e60bac3a1efaf535c2420839400bea4061916de812e3a7a",
    "proof.md": "c151e4b4d986472f46b2a5b32598b665d30496fc7e8df31764b6b2695269b79e",
    "stabilizer_voltage_audit.py": "ebae09e2065627687468e89388b5768d1bc3320fb927a4936755c406be746614",
    "results.json": "01026b59612f1ec27394a5c068aded3ad35456b548af8d8a445b98b5f6fbab2e",
    "freeze_manifest.md": "128dc9a5ad79764c0556b4928586f8f896bfca9ac6a8e23253ee18b44ac8b95e",
    "SHA256SUMS": "7a235dd5246182375166fc63ab067728c8129191e86640a411156709f55de62a",
}


def identity(n):
    return tuple(range(n))


def compose(p, q):
    """Return pq, so (pq)(x)=p(q(x))."""
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p):
    out = [0] * len(p)
    for i, x in enumerate(p):
        out[x] = i
    return tuple(out)


def perm_sign_bit(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2


def transposition(n, edge):
    p = list(range(n))
    a, b = edge
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def edge_relabel(edge, rho):
    return tuple(sorted((rho[edge[0]], rho[edge[1]])))


def word_relabel(word, rho):
    return tuple(edge_relabel(edge, rho) for edge in word)


def eval_word(word, n):
    value = identity(n)
    for edge in word:
        value = compose(value, transposition(n, edge))
    return value


def connected(word, n):
    adjacency = [set() for _ in range(n)]
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
    return len(seen) == n


def conjugate_edge(edge, by_edge):
    by = transposition(max(max(edge), max(by_edge)) + 1, by_edge)
    return edge_relabel(edge, by)


def hurwitz(word, slot, direction):
    out = list(word)
    a, b = out[slot], out[slot + 1]
    if direction == 1:
        out[slot], out[slot + 1] = b, conjugate_edge(a, b)
    else:
        out[slot], out[slot + 1] = conjugate_edge(b, a), a
    return tuple(out)


def canonical(word, relabelings):
    return min(word_relabel(word, rho) for rho in relabelings)


def enumerate_quotient(d):
    edges = tuple(itertools.combinations(range(d), 2))
    relabelings = tuple(itertools.permutations(range(d)))
    physical = []
    quotient = set()
    for word in itertools.product(edges, repeat=2 * d - 2):
        if eval_word(word, d) == identity(d) and connected(word, d):
            physical.append(word)
            quotient.add(canonical(word, relabelings))
    states = tuple(sorted(quotient))
    assert len(physical) == len(states) * len(relabelings)
    for state in states:
        stabilizers = [rho for rho in relabelings if word_relabel(state, rho) == state]
        assert stabilizers == [identity(d)]
    return tuple(physical), states, relabelings


def unique_transporter(target, raw, relabelings):
    found = [rho for rho in relabelings if word_relabel(target, rho) == raw]
    assert len(found) == 1
    return found[0]


def signed_quotient_action(d, states, relabelings):
    index = {state: i for i, state in enumerate(states)}
    generators = tuple(
        (slot, direction)
        for slot in range(2 * d - 3)
        for direction in (1, -1)
    )
    actions = []
    voltages = []
    for slot, direction in generators:
        action = []
        voltage = []
        for state in states:
            raw = hurwitz(state, slot, direction)
            assert eval_word(raw, d) == identity(d) and connected(raw, d)
            target = canonical(raw, relabelings)
            rho = unique_transporter(target, raw, relabelings)
            action.append(index[target])
            voltage.append(perm_sign_bit(rho))
        actions.append(tuple(action))
        voltages.append(tuple(voltage))

    inverse_failures = 0
    for slot in range(2 * d - 3):
        pos, neg = 2 * slot, 2 * slot + 1
        for q in range(len(states)):
            r = actions[pos][q]
            inverse_failures += actions[neg][r] != q
            inverse_failures += voltages[neg][r] != voltages[pos][q]
    assert inverse_failures == 0

    cocycle_pair_failures = 0
    for g1, (slot1, direction1) in enumerate(generators):
        for g2, (slot2, direction2) in enumerate(generators):
            for q, state in enumerate(states):
                raw = hurwitz(hurwitz(state, slot1, direction1), slot2, direction2)
                q1 = actions[g1][q]
                q2 = actions[g2][q1]
                assert canonical(raw, relabelings) == states[q2]
                rho = unique_transporter(states[q2], raw, relabelings)
                expected = voltages[g1][q] ^ voltages[g2][q1]
                cocycle_pair_failures += perm_sign_bit(rho) != expected
    assert cocycle_pair_failures == 0
    return generators, tuple(actions), tuple(voltages), {
        "inverse_edge_failures": inverse_failures,
        "two_generator_cocycle_failures": cocycle_pair_failures,
    }


def relative_mask(bits):
    return sum((bits[i] ^ bits[0]) << (i - 1) for i in range(1, len(bits)))


def augmented_orbit(seed, actions, voltages):
    start = (tuple(seed), 0)
    seen = {start}
    todo = deque([start])
    while todo:
        point, mask = todo.popleft()
        for action, voltage in zip(actions, voltages):
            bits = tuple(voltage[q] for q in point)
            nxt = (
                tuple(action[q] for q in point),
                mask ^ relative_mask(bits),
            )
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return seen


def permutation_group_closure(generators):
    degree = len(generators[0])
    one = identity(degree)
    seen = {one}
    todo = deque([one])
    while todo:
        g = todo.popleft()
        for h in generators:
            gh = compose(g, h)
            if gh not in seen:
                seen.add(gh)
                todo.append(gh)
    return seen


def d3_audit():
    physical, states, relabelings = enumerate_quotient(3)
    generators, actions, voltages, action_checks = signed_quotient_action(
        3, states, relabelings
    )
    positive_actions = tuple(actions[2 * slot] for slot in range(3))
    quotient_group = permutation_group_closure(positive_actions)
    rows = []
    for width in range(1, 5):
        histogram = Counter()
        quotient_orbit_sizes = Counter()
        for point in itertools.product(range(len(states)), repeat=width):
            orbit = augmented_orbit(point, actions, voltages)
            vstab = frozenset(mask for endpoint, mask in orbit if endpoint == point)
            assert vstab == {0}
            quotient_size = len({endpoint for endpoint, _ in orbit})
            assert len(orbit) == quotient_size
            histogram[str(tuple(sorted(vstab)))] += 1
            quotient_orbit_sizes[quotient_size] += 1
        rows.append(
            {
                "width": width,
                "tuples_exhausted": len(states) ** width,
                "vstab_histogram": dict(sorted(histogram.items())),
                "quotient_orbit_size_histogram": {
                    str(k): v for k, v in sorted(quotient_orbit_sizes.items())
                },
            }
        )
    return {
        "physical_Z3_size": len(physical),
        "quotient_Q3_size": len(states),
        "global_action_free": True,
        "signed_generator_count": len(generators),
        "quotient_positive_image_order": len(quotient_group),
        "positive_generators_even": all(perm_sign_bit(g) == 0 for g in positive_actions),
        "action_checks": action_checks,
        "all_tuple_rows": rows,
        "conclusion": "every d=3 quotient tuple of width 1..4 has V_stab={0}",
    }


MATCHINGS4 = (
    frozenset((frozenset((0, 1)), frozenset((2, 3)))),
    frozenset((frozenset((0, 2)), frozenset((1, 3)))),
    frozenset((frozenset((0, 3)), frozenset((1, 2)))),
)


def matching_relabel(matching, rho):
    return frozenset(
        frozenset((rho[min(edge)], rho[max(edge)])) for edge in matching
    )


def project_edge_s4_to_s3(edge):
    rho = transposition(4, edge)
    action = tuple(MATCHINGS4.index(matching_relabel(matching, rho)) for matching in MATCHINGS4)
    moved = tuple(i for i in range(3) if action[i] != i)
    assert len(moved) == 2
    return moved


def project_word(word):
    return tuple(project_edge_s4_to_s3(edge) for edge in word)


def paired_subgroup_order(words):
    d = 4
    generators = tuple(
        (transposition(d, words[0][i]), transposition(d, words[1][i]))
        for i in range(len(words[0]))
    )
    one = (identity(d), identity(d))
    seen = {one}
    todo = deque([one])
    while todo:
        g1, g2 = todo.popleft()
        for h1, h2 in generators:
            product = (compose(g1, h1), compose(g2, h2))
            if product not in seen:
                seen.add(product)
                todo.append(product)
    return len(seen)


def d4_audit():
    physical, states, relabelings = enumerate_quotient(4)
    generators, actions, voltages, action_checks = signed_quotient_action(
        4, states, relabelings
    )
    index = {state: i for i, state in enumerate(states)}
    relabelings3 = tuple(itertools.permutations(range(3)))

    phi = []
    for state in states:
        projected = project_word(state)
        assert eval_word(projected, 3) == identity(3)
        assert connected(projected, 3)
        phi.append(canonical(projected, relabelings3))
    fibers = defaultdict(list)
    for i, label in enumerate(phi):
        fibers[label].append(i)
    assert len(fibers) == 40
    assert set(map(len, fibers.values())) == {3}

    block_failures = 0
    for action in actions:
        for fiber in fibers.values():
            block_failures += len({phi[action[q]] for q in fiber}) != 1
    assert block_failures == 0

    A, B, C, D, E = (0, 1), (0, 2), (2, 3), (1, 2), (1, 3)
    sources = ((A, B, B, A, C, C), (A, B, B, C, A, C))
    targets = ((A, D, B, E, D, C), (A, D, B, C, E, C))
    for word in sources + targets:
        assert eval_word(word, 4) == identity(4) and connected(word, 4)
    source = tuple(index[canonical(word, relabelings)] for word in sources)
    target = tuple(index[canonical(word, relabelings)] for word in targets)

    source_orbit = augmented_orbit(source, actions, voltages)
    target_orbit = augmented_orbit(target, actions, voltages)
    source_vstab = sorted(mask for point, mask in source_orbit if point == source)
    target_vstab = sorted(mask for point, mask in target_orbit if point == target)
    route_voltages = sorted(mask for point, mask in source_orbit if point == target)
    source_qsize = len({point for point, _ in source_orbit})
    target_qsize = len({point for point, _ in target_orbit})
    assert source_vstab == [0] and target_vstab == [0]
    assert len(source_orbit) == source_qsize == 240
    assert len(target_orbit) == target_qsize == 9720
    assert route_voltages == []
    assert phi[source[0]] == phi[source[1]]
    assert phi[target[0]] != phi[target[1]]

    source_group_order = paired_subgroup_order(sources)
    target_group_order = paired_subgroup_order(targets)
    assert (source_group_order, target_group_order) == (96, 288)
    return {
        "physical_Z4_size": len(physical),
        "quotient_Q4_size": len(states),
        "global_action_free": True,
        "signed_generator_count": len(generators),
        "action_checks": action_checks,
        "S4_over_V4_block": {
            "fiber_count": len(fibers),
            "fiber_sizes": sorted(Counter(map(len, fibers.values())).items()),
            "signed_action_block_failures": block_failures,
        },
        "accepted_witness": {
            "clean_room_lexicographic_source_indices": list(source),
            "clean_room_lexicographic_target_indices": list(target),
            "source_quotient_orbit_size": source_qsize,
            "source_augmented_orbit_size": len(source_orbit),
            "source_vstab_masks": source_vstab,
            "target_quotient_orbit_size": target_qsize,
            "target_augmented_orbit_size": len(target_orbit),
            "target_vstab_masks": target_vstab,
            "source_to_target_voltage_masks": route_voltages,
            "source_same_block": phi[source[0]] == phi[source[1]],
            "target_same_block": phi[target[0]] == phi[target[1]],
            "paired_subgroup_orders": {
                "source": source_group_order,
                "target": target_group_order,
            },
        },
        "conclusion": (
            "both accepted d=4 endpoint stabilizer voltages are trivial; "
            "the endpoints are in different quotient-tuple orbits by the "
            "S4/V4 block invariant"
        ),
    }


def verify_frozen_hashes(root):
    base = root / (
        "experiments/20260811-polynomial-mixing-resolution/cycle-37/"
        "mission-M163-quotient-stabilizer-voltage"
    )
    observed = {
        name: hashlib.sha256((base / name).read_bytes()).hexdigest()
        for name in EXPECTED_M163
    }
    assert observed == EXPECTED_M163
    return observed


def main():
    here = Path(__file__).resolve().parent
    root = here.parents[3]
    payload = {
        "experiment": "M164 fresh immutable referee of M163",
        "target": "quotient stabilizer-voltage lifting criterion; not a sampler or gap",
        "composition_convention": (
            "(pq)(x)=p(q(x)); displayed factors left-to-right; "
            "R_j(a,b)=(b,b^-1*a*b)"
        ),
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True
        ).strip(),
        "python": platform.python_version(),
        "seed": None,
        "command": "python3 -B independent_referee.py",
        "frozen_m163_hashes": verify_frozen_hashes(root),
        "imports_or_executes_predecessor_code": False,
        "d3": d3_audit(),
        "d4": d4_audit(),
        "scope": "exact d=3 and accepted d=4 witness/block only; no d>=5 inference",
    }
    (here / "independent_results.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
