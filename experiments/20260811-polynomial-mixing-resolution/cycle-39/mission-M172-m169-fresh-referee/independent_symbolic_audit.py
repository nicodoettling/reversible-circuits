#!/usr/bin/env python3
"""Clean-room bounded convention audit for frozen M169.

This script uses only S_3.  It does not import predecessor code or attempt
any d=5 closure.  The universal conclusions in the referee report come from
proof audit; these finite checks only test quotient, inverse-monodromy,
relative-orientation, coboundary, and exact-sequence conventions.
"""

from __future__ import annotations

import itertools
import json
from collections import defaultdict, deque


Perm = tuple[int, ...]
Word = tuple[Perm, ...]


def compose(p: Perm, q: Perm) -> Perm:
    """p q, with (p q)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    ans = [0] * len(p)
    for x, y in enumerate(p):
        ans[y] = x
    return tuple(ans)


def sign_bit(p: Perm) -> int:
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2


def transposition(d: int, a: int, b: int) -> Perm:
    p = list(range(d))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def relabel(g: Perm, t: Perm) -> Perm:
    return compose(compose(g, t), inverse(g))


def relabel_word(g: Perm, w: Word) -> Word:
    return tuple(relabel(g, t) for t in w)


def word_product(w: Word) -> Perm:
    ans = tuple(range(len(w[0])))
    for t in w:
        ans = compose(ans, t)
    return ans


def edge_of_transposition(t: Perm) -> tuple[int, int]:
    moved = [x for x, y in enumerate(t) if x != y]
    assert len(moved) == 2
    return moved[0], moved[1]


def connected_support(w: Word) -> bool:
    d = len(w[0])
    adj = [set() for _ in range(d)]
    for t in w:
        a, b = edge_of_transposition(t)
        adj[a].add(b)
        adj[b].add(a)
    seen = {0}
    todo = [0]
    while todo:
        x = todo.pop()
        for y in adj[x] - seen:
            seen.add(y)
            todo.append(y)
    return len(seen) == d


def hurwitz(w: Word, j: int, direction: int) -> Word:
    a, b = w[j], w[j + 1]
    out = list(w)
    if direction == 1:
        out[j] = b
        out[j + 1] = compose(compose(inverse(b), a), b)
    elif direction == -1:
        out[j] = compose(compose(a, b), inverse(a))
        out[j + 1] = a
    else:
        raise ValueError(direction)
    return tuple(out)


def subgroup(generators: list[tuple[Perm, ...]], identity: tuple[Perm, ...]) -> set[tuple[Perm, ...]]:
    symmetric = generators + [tuple(inverse(p) for p in g) for g in generators]
    seen = {identity}
    todo = deque([identity])
    while todo:
        x = todo.popleft()
        for g in symmetric:
            y = tuple(compose(g[i], x[i]) for i in range(len(x)))
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return seen


def main() -> None:
    d = 3
    m = 2 * d - 2
    ident = tuple(range(d))
    perms = list(itertools.permutations(range(d)))
    trans = [transposition(d, a, b) for a in range(d) for b in range(a + 1, d)]
    words = sorted(
        w
        for w in itertools.product(trans, repeat=m)
        if word_product(w) == ident and connected_support(w)
    )
    assert len(words) == 24

    # Signed Hurwitz formulas are mutual inverses and preserve Z_3.
    hurwitz_inverse_checks = 0
    for w in words:
        for j in range(m - 1):
            assert hurwitz(hurwitz(w, j, 1), j, -1) == w
            assert hurwitz(hurwitz(w, j, -1), j, 1) == w
            assert hurwitz(w, j, 1) in words
            assert hurwitz(w, j, -1) in words
            hurwitz_inverse_checks += 2

    def global_canon(w: Word) -> Word:
        return min(relabel_word(g, w) for g in perms)

    reps = sorted({global_canon(w) for w in words})
    q_index = {w: i for i, w in enumerate(reps)}
    assert len(reps) == 4

    # Freeness and unique physical transporters.
    free_checks = 0
    for w in words:
        fixing = [g for g in perms if relabel_word(g, w) == w]
        assert fixing == [ident]
        free_checks += 1

    def transporter(u: Word, v: Word) -> Perm:
        hits = [g for g in perms if relabel_word(g, v) == u]
        assert len(hits) == 1
        return hits[0]

    # R_d=(Z_d x [d])/S_d and Z_d/H are the same 12-element B-set.
    root = d - 1
    H = [g for g in perms if g[root] == root]

    def h_canon(w: Word) -> Word:
        return min(relabel_word(h, w) for h in H)

    def rooted_canon(w: Word, a: int) -> tuple[Word, int]:
        return min((relabel_word(g, w), g[a]) for g in perms)

    h_orbits = {h_canon(w) for w in words}
    rooted_orbits = {rooted_canon(w, a) for w in words for a in range(d)}
    h_to_rooted = {hw: rooted_canon(hw, root) for hw in h_orbits}
    assert len(h_orbits) == 12
    assert len(rooted_orbits) == 12
    assert set(h_to_rooted.values()) == rooted_orbits

    # A signed generator edge on Q_d carries root monodromy rho^{-1}.
    edge = {}
    inverse_monodromy_checks = 0
    for qi, u in enumerate(reps):
        for j in range(m - 1):
            for direction in (-1, 1):
                bu = hurwitz(u, j, direction)
                v = global_canon(bu)
                qj = q_index[v]
                rho = transporter(bu, v)  # b.u = rho.v
                mu = inverse(rho)
                edge[(qi, j, direction)] = (qj, mu, rho)
                for a in range(d):
                    lhs = rooted_canon(bu, a)
                    rhs = rooted_canon(v, mu[a])
                    assert lhs == rhs
                    inverse_monodromy_checks += 1

    # Clean two-coordinate case using two distinct quotient points.
    q0 = (0, 1)
    aligned_generators = [(reps[0][j], reps[1][j]) for j in range(m)]
    pair_identity = (ident, ident)
    gamma = subgroup(aligned_generators, pair_identity)
    common_parity = {
        (g, h) for g in perms for h in perms if sign_bit(g) == sign_bit(h)
    }
    assert gamma == common_parity

    braid_generators = [(j, direction) for j in range(m - 1) for direction in (-1, 1)]

    # Simultaneous base and full root-monodromy closure.
    start_aug = (q0, pair_identity)
    aug_seen = {start_aug}
    aug_todo = deque([start_aug])
    while aug_todo:
        base, mus = aug_todo.popleft()
        for j, direction in braid_generators:
            e0 = edge[(base[0], j, direction)]
            e1 = edge[(base[1], j, direction)]
            new_base = (e0[0], e1[0])
            new_mus = (compose(e0[1], mus[0]), compose(e1[1], mus[1]))
            state = (new_base, new_mus)
            if state not in aug_seen:
                aug_seen.add(state)
                aug_todo.append(state)

    base_component = {base for base, _ in aug_seen}
    K_mon = {mus for base, mus in aug_seen if base == q0}
    assert len(base_component) == 12
    assert K_mon == common_parity
    v_stab = {sign_bit(g) ^ sign_bit(h) for g, h in K_mon}
    assert v_stab == {0}
    kernel = {(g, h) for g, h in K_mon if sign_bit(g) == sign_bit(h)}
    assert kernel == common_parity

    # Independent W_2 relative-orientation lift closure.
    orient_start = (q0, 0)
    orient_seen = {orient_start}
    orient_todo = deque([orient_start])
    while orient_todo:
        base, bit = orient_todo.popleft()
        for j, direction in braid_generators:
            e0 = edge[(base[0], j, direction)]
            e1 = edge[(base[1], j, direction)]
            edge_bit = sign_bit(e0[1]) ^ sign_bit(e1[1])
            state = ((e0[0], e1[0]), bit ^ edge_bit)
            if state not in orient_seen:
                orient_seen.add(state)
                orient_todo.append(state)

    projected_aug = {
        (base, sign_bit(mus[0]) ^ sign_bit(mus[1])) for base, mus in aug_seen
    }
    assert orient_seen == projected_aug
    stabilizer_bits = {bit for base, bit in orient_seen if base == q0}
    assert stabilizer_bits == v_stab

    # The other deck translate is a disjoint lifted orbit over the same base orbit.
    translated_orbit = {(base, bit ^ 1) for base, bit in orient_seen}
    assert orient_seen.isdisjoint(translated_orbit)
    assert orient_seen | translated_orbit == {
        (base, bit) for base in base_component for bit in (0, 1)
    }

    # Fixed physical endpoint criterion: at each target base, route voltage zero
    # iff the two canonical relative-orientation lifts share a lifted orbit.
    labels_by_base: dict[tuple[int, int], set[int]] = defaultdict(set)
    for base, mus in aug_seen:
        labels_by_base[base].add(sign_bit(mus[0]) ^ sign_bit(mus[1]))
    fixed_endpoint_checks = 0
    for base in base_component:
        zero_in_route_coset = 0 in labels_by_base[base]
        same_orientation_orbit = (base, 0) in orient_seen
        assert zero_in_route_coset == same_orientation_orbit
        fixed_endpoint_checks += 1

    # Endpoint representative changes translate the displayed relative label
    # by the source and target endpoint orientation changes (the coboundary).
    coboundary_checks = 0
    for base in itertools.product(range(len(reps)), repeat=2):
        for j, direction in braid_generators:
            data = [edge[(base[k], j, direction)] for k in range(2)]
            target = (data[0][0], data[1][0])
            rho = (data[0][2], data[1][2])
            old_bit = sign_bit(rho[0]) ^ sign_bit(rho[1])
            for alpha in itertools.product(perms, repeat=2):
                # A single nontrivial target choice per alpha is enough to test
                # both endpoint terms without an unnecessary 36-fold expansion.
                beta = (perms[(perms.index(alpha[1]) + 1) % len(perms)], alpha[0])
                new_rho = tuple(
                    compose(compose(alpha[k], rho[k]), inverse(beta[k]))
                    for k in range(2)
                )
                for k in range(2):
                    source_word = relabel_word(alpha[k], reps[base[k]])
                    target_word = relabel_word(beta[k], reps[target[k]])
                    assert hurwitz(source_word, j, direction) == relabel_word(
                        new_rho[k], target_word
                    )
                new_bit = sign_bit(new_rho[0]) ^ sign_bit(new_rho[1])
                alpha_bit = sign_bit(alpha[0]) ^ sign_bit(alpha[1])
                beta_bit = sign_bit(beta[0]) ^ sign_bit(beta[1])
                assert new_bit == old_bit ^ alpha_bit ^ beta_bit
                coboundary_checks += 1

    result = {
        "scope": "bounded clean-room S_3 convention audit; no d=5 closure",
        "seed": None,
        "counts": {
            "Z_3": len(words),
            "Q_3": len(reps),
            "H_orbits": len(h_orbits),
            "rooted_cover_points": len(rooted_orbits),
            "hurwitz_inverse_checks": hurwitz_inverse_checks,
            "free_action_checks": free_checks,
            "inverse_monodromy_root_checks": inverse_monodromy_checks,
            "ordered_distinct_base_component": len(base_component),
            "augmented_states": len(aug_seen),
            "K_mon_order": len(K_mon),
            "P_3_2_order": len(common_parity),
            "relative_orientation_orbit_size": len(orient_seen),
            "fixed_endpoint_checks": fixed_endpoint_checks,
            "coboundary_checks": coboundary_checks,
        },
        "assertions": {
            "Z_over_H_bijection_rooted_cover": True,
            "root_monodromy_is_inverse_transporter": True,
            "tuple_relative_sign_image_is_V_stab": True,
            "relative_orientation_orbits_are_W_mod_V_cosets": True,
            "fixed_physical_zero_coset_iff_orientation_orbit": True,
            "independent_endpoint_changes_are_coboundary": True,
            "actual_d3_distinct_pair_K_mon_equals_P": True,
            "actual_d3_exact_sequence_kernel_and_surjectivity": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
