#!/usr/bin/env python3
"""Clean-room exact falsification checks for the strict PBV reduction.

The script is standard-library only and reads/imports no M261 code or data.
It reconstructs the source pair laws directly from minimal-factorization
counts, including ordered triangle/double lifts and the M91 J channels.
Finite k=3,5 checks are used only to falsify algebraic or indexing errors.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import factorial


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return pq with (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    ans = [0] * len(p)
    for x, y in enumerate(p):
        ans[y] = x
    return tuple(ans)


def cycle_perm(n: int, cyc: tuple[int, ...]) -> tuple[int, ...]:
    p = list(range(n))
    for x, y in zip(cyc, cyc[1:] + cyc[:1]):
        p[x] = y
    return tuple(p)


def transposition(n: int, a: int, b: int) -> tuple[int, ...]:
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def cycles(p: tuple[int, ...]) -> list[tuple[int, ...]]:
    seen: set[int] = set()
    out: list[tuple[int, ...]] = []
    for start in range(len(p)):
        if start in seen:
            continue
        cyc = []
        x = start
        while x not in seen:
            seen.add(x)
            cyc.append(x)
            x = p[x]
        out.append(tuple(cyc))
    return out


def transposition_rank(p: tuple[int, ...]) -> int:
    return len(p) - len(cycles(p))


def tau(d: int) -> Fraction:
    if d < 1:
        return Fraction(0)
    if d == 1:
        return Fraction(1)
    return Fraction(d ** (d - 2), factorial(d - 1))


def minimal_count(p: tuple[int, ...], expected_rank: int) -> int:
    if transposition_rank(p) != expected_rank:
        return 0
    ans = Fraction(factorial(expected_rank))
    for cyc in cycles(p):
        ans *= tau(len(cyc))
    assert ans.denominator == 1
    return ans.numerator


def add_scaled(dst: dict, src: dict, scale: Fraction) -> None:
    for key, value in src.items():
        dst[key] += scale * value


def normalized(measure: dict, mass: Fraction) -> dict:
    assert mass > 0
    return {key: value / mass for key, value in measure.items() if value}


def measure_difference(a: dict, b: dict) -> dict:
    out = defaultdict(Fraction)
    add_scaled(out, a, Fraction(1))
    add_scaled(out, b, Fraction(-1))
    return {key: value for key, value in out.items() if value}


def assert_measures_equal(a: dict, b: dict) -> None:
    keys = set(a) | set(b)
    assert all(a.get(key, 0) == b.get(key, 0) for key in keys)


def expectation(measure: dict, observable: dict) -> Fraction:
    return sum((weight * observable[key] for key, weight in measure.items()), Fraction())


def smaller_split(edge: tuple[int, int], source_cycles: list[tuple[int, ...]]) -> int:
    a, b = edge
    for cyc in source_cycles:
        support = set(cyc)
        if a in support and b in support:
            pos = {x: i for i, x in enumerate(cyc)}
            distance = (pos[b] - pos[a]) % len(cyc)
            return min(distance, len(cyc) - distance)
    raise AssertionError("non-internal transposition in a nonzero completion")


def chord_split_law(d: int) -> dict[int, Fraction]:
    law = {}
    for split in range(1, (d - 1) // 2 + 1):
        single_chord = Fraction(
            factorial(d - 2) * tau(split) * tau(d - split),
            d ** (d - 2),
        )
        law[split] = d * single_chord
    assert sum(law.values(), Fraction()) == 1
    return law


def cyclic_run_count(n: int, support: set[int]) -> int:
    if len(support) == n:
        return 1
    return sum(x in support and (x - 1) % n not in support for x in range(n))


def nontrivial_cycle_text(p: tuple[int, ...]) -> str:
    return "".join(
        "(" + ",".join(map(str, cyc)) + ")" for cyc in cycles(p) if len(cyc) > 1
    )


def source_pair_data(n: int, k: int, g: tuple[int, ...], h: tuple[int, ...]):
    qg = compose(inverse(g), h)
    source_cycles = cycles(qg)
    middle = set(range(k, 2 * k))
    a_g = minimal_count(qg, n - 3)
    edges = [(a, b, transposition(n, a, b)) for a in range(n) for b in range(a + 1, n)]

    law = defaultdict(Fraction)
    channel = {j: defaultdict(Fraction) for j in range(3)}
    group = {j: defaultdict(lambda: defaultdict(Fraction)) for j in (1, 2)}
    lift_kinds = defaultdict(int)

    for a, b, ep in edges:
        for c, d, fp in edges:
            s = compose(ep, fp)
            if transposition_rank(s) != 2:
                continue
            residual = compose(inverse(compose(g, s)), h)
            completion = minimal_count(residual, n - 5)
            if not completion:
                continue
            weight = Fraction(completion, a_g)
            law[s] += weight

            pair = ((a, b), (c, d))
            exterior_flags = []
            for edge in pair:
                x, y = edge
                internal_middle = x in middle and y in middle
                internal_cycle = any(x in cyc and y in cyc for cyc in source_cycles)
                assert internal_cycle
                exterior_flags.append(0 if internal_middle else 1)
            j = sum(exterior_flags)
            channel[j][s] += weight

            if j in (1, 2):
                if j == 1:
                    exterior_edge = pair[exterior_flags.index(1)]
                else:
                    exterior_edge = pair[0]
                split = smaller_split(exterior_edge, source_cycles)
                group[j][split][s] += weight

            support_size = sum(s[x] != x for x in range(n))
            kind = "T" if support_size == 3 else "D"
            assert support_size in (3, 4)
            lift_kinds[(s, kind)] += 1

    assert sum(law.values(), Fraction()) == 1
    return {
        "q": qg,
        "cycles": source_cycles,
        "A": a_g,
        "law": dict(law),
        "channel": {j: dict(m) for j, m in channel.items()},
        "group": {j: {u: dict(m) for u, m in groups.items()} for j, groups in group.items()},
        "lift_kinds": lift_kinds,
    }


def product_profile(n: int, s: tuple[int, ...], h: tuple[int, ...], edge_perms):
    q = compose(inverse(s), h)
    residual_cycles = cycles(q)
    assert len(residual_cycles) == 3
    d = [len(cyc) for cyc in residual_cycles]
    owner = {}
    for i, cyc in enumerate(residual_cycles):
        for x in cyc:
            owner[x] = i

    chi = [[0] * n for _ in range(3)]
    for r in range(n):
        if s[(r + 1) % n] == (r + 1) % n:
            chi[owner[r]][r] = 1

    kappa = [[Fraction() for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if i == j:
                kappa[i][j] = tau(d[i] - 2) / tau(d[i])
            else:
                kappa[i][j] = tau(d[i] - 1) * tau(d[j] - 1) / (tau(d[i]) * tau(d[j]))

    a_s = minimal_count(q, n - 3)
    normalizer = (n - 3) * (n - 4)
    response = {}
    endpoints = {}
    csum = {}

    for ell in range(2, n - 1):
        raw = Fraction()
        for r in range(n):
            altered = compose(edge_perms[r], compose(edge_perms[(r + ell) % n], q))
            raw += Fraction(minimal_count(altered, n - 5), a_s)

        weighted_correlation = Fraction()
        total_correlation = 0
        for i in range(3):
            for j in range(3):
                cij = sum(chi[i][r] * chi[j][(r + ell) % n] for r in range(n))
                total_correlation += cij
                weighted_correlation += kappa[i][j] * cij
        formula = weighted_correlation / normalizer
        assert raw == formula
        response[ell] = formula
        csum[ell] = total_correlation

    jump_count = sum(
        tuple(chi[i][x] for i in range(3))
        != tuple(chi[i][(x + 1) % n] for i in range(3))
        for x in range(n)
    )
    support_size = sum(s[x] != x for x in range(n))
    assert jump_count <= (6 if support_size == 3 else 8)

    b = [1 - sum(chi[i][r] for i in range(3)) for r in range(n)]
    assert sum(b) == support_size
    for ell in range(2, n - 1):
        incidence = sum(b[r] * b[(r + ell) % n] for r in range(n))
        affine = n - 8 + 2 * (support_size == 3) + incidence
        assert csum[ell] == affine

    for ell in range(2, n - 2):
        endpoint = Fraction()
        for x in range(n):
            for i in range(3):
                if not chi[i][(x - ell) % n]:
                    continue
                for j in range(3):
                    endpoint += kappa[i][j] * (
                        chi[j][(x + 1) % n] - chi[j][x]
                    )
        assert response[ell + 1] - response[ell] == endpoint / normalizer
        assert abs(endpoint) <= 8
        endpoints[ell] = endpoint

    run_profile = tuple(
        sorted((len(cyc), cyclic_run_count(n, set(cyc))) for cyc in residual_cycles)
    )
    return {
        "response": response,
        "endpoint": endpoints,
        "support_size": support_size,
        "jump_count": jump_count,
        "run_profile": run_profile,
    }


def audit_k(k: int) -> list[str]:
    n = 3 * k
    h = cycle_perm(n, tuple(range(n)))
    a_source = cycle_perm(n, (0, k, 2 * k))
    b_source = compose(transposition(n, 0, 1), transposition(n, k, 2 * k))
    edge_perms = [transposition(n, r, (r + 1) % n) for r in range(n)]

    source_a = source_pair_data(n, k, a_source, h)
    source_b = source_pair_data(n, k, b_source, h)
    m = k - 1
    denom = 3 * m * (3 * m - 1)
    alpha = {
        0: Fraction(m * (m - 1), denom),
        1: Fraction(4 * m * m, denom),
        2: Fraction(2 * m * (2 * m - 1), denom),
    }
    assert sum(alpha.values(), Fraction()) == 1
    for src in (source_a, source_b):
        for j in range(3):
            assert sum(src["channel"][j].values(), Fraction()) == alpha[j]

    h_a = {j: normalized(source_a["channel"][j], alpha[j]) for j in range(3)}
    h_b = {j: normalized(source_b["channel"][j], alpha[j]) for j in range(3)}
    assert_measures_equal(h_a[0], h_b[0])

    eta = measure_difference(source_b["law"], source_a["law"])
    eta_channels = defaultdict(Fraction)
    for j in (1, 2):
        add_scaled(eta_channels, measure_difference(h_b[j], h_a[j]), alpha[j])
    assert_measures_equal(eta, eta_channels)

    p = chord_split_law(2 * k - 1)
    q = chord_split_law(k)
    phi = {1: {}, 2: {}}
    psi = {1: {}, 2: {}}
    for j in (1, 2):
        for u, group in source_b["group"][j].items():
            mass = sum(group.values(), Fraction())
            assert mass == alpha[j] * p[u]
            phi[j][u] = normalized(group, mass)
        for u, group in source_a["group"][j].items():
            mass = sum(group.values(), Fraction())
            assert mass == alpha[j] * q[u]
            psi[j][u] = normalized(group, mass)

        d_u = {}
        cumulative = Fraction()
        for u in range(1, k):
            cumulative += p.get(u, 0) - q.get(u, 0)
            d_u[u] = cumulative
        assert d_u[k - 1] == 0

        abel = defaultdict(Fraction)
        for u in range(1, k - 1):
            add_scaled(abel, phi[j][u], d_u[u])
            add_scaled(abel, phi[j][u + 1], -d_u[u])
        for u in range(1, (k - 1) // 2 + 1):
            add_scaled(abel, phi[j][u], q[u])
            add_scaled(abel, psi[j][u], -q[u])
        assert_measures_equal(measure_difference(h_b[j], h_a[j]), abel)

    all_products = set(source_a["law"]) | set(source_b["law"])
    profiles = {s: product_profile(n, s, h, edge_perms) for s in all_products}
    max_endpoint = max(
        (abs(value) for profile in profiles.values() for value in profile["endpoint"].values()),
        default=Fraction(),
    )
    max_jumps_t = max(
        profile["jump_count"] for profile in profiles.values() if profile["support_size"] == 3
    )
    max_jumps_d = max(
        profile["jump_count"] for profile in profiles.values() if profile["support_size"] == 4
    )

    # Exhibit the information loss in the X_D/Y_D interface: the complete
    # component-size/run-count profile can agree while literal endpoint data differ.
    j2_products = set(source_a["channel"][2]) | set(source_b["channel"][2])
    by_run_profile = defaultdict(list)
    for s in j2_products:
        profile = profiles[s]
        by_run_profile[profile["run_profile"]].append(s)
    xy_witness = None
    for run_profile, states in by_run_profile.items():
        for left in states:
            left_e = tuple(profiles[left]["endpoint"].values())
            for right in states:
                if tuple(profiles[right]["endpoint"].values()) != left_e:
                    xy_witness = (run_profile, left, right)
                    break
            if xy_witness:
                break
        if xy_witness:
            break
    assert xy_witness is not None
    witness_profile, witness_left, witness_right = xy_witness
    witness_ell = next(
        ell
        for ell in range(2, n - 2)
        if profiles[witness_left]["endpoint"][ell]
        != profiles[witness_right]["endpoint"][ell]
    )
    witness_values = (
        profiles[witness_left]["endpoint"][witness_ell],
        profiles[witness_right]["endpoint"][witness_ell],
    )

    # Check the Abel evaluation of every endpoint observable channel by channel.
    for ell in range(2, n - 2):
        observable = {s: profiles[s]["endpoint"][ell] for s in all_products}
        direct_eta = expectation(eta, observable)
        channel_eta = Fraction()
        for j in (1, 2):
            channel_eta += alpha[j] * expectation(measure_difference(h_b[j], h_a[j]), observable)
        assert direct_eta == channel_eta

    f_t = (n - 2) ** (n - 4)
    lam = Fraction(n ** (n - 3), f_t)
    normalizer = (n - 3) * (n - 4)
    z = []
    for ell in range(2, n - 1):
        observable = {s: profiles[s]["response"][ell] for s in all_products}
        z.append(lam * expectation(eta, observable))
    pbv_values = []
    for ell in range(2, n - 2):
        observable = {s: profiles[s]["endpoint"][ell] for s in all_products}
        pbv_values.append(expectation(eta, observable))
    variation_z = sum((abs(z[i + 1] - z[i]) for i in range(len(z) - 1)), Fraction())
    pbv_l1 = sum((abs(value) for value in pbv_values), Fraction())
    assert variation_z == lam * pbv_l1 / normalizer

    eta_t = sum(
        weight for s, weight in eta.items() if sum(s[x] != x for x in range(n)) == 3
    )
    eta_t_formula = Fraction(12 * (k - 1), 3 * k * (3 * k - 4) * (2 * k - 1))
    assert eta_t == eta_t_formula

    scale = Fraction(k * k) * lam / normalizer
    lines = [
        f"k={k} n={n}",
        f"  accessible_products_A={len(source_a['law'])} B={len(source_b['law'])}",
        f"  alpha_0={alpha[0]} alpha_1={alpha[1]} alpha_2={alpha[2]}",
        f"  circular_rows_checked={len(all_products) * (n - 3)}",
        f"  endpoint_rows_checked={len(all_products) * (n - 4)}",
        f"  max_jump_count_triangle={max_jumps_t} double={max_jumps_d}",
        f"  max_abs_endpoint={float(max_endpoint):.12g}",
        f"  same_XY_profile_distinct_E={witness_profile}",
        f"    witness_left={nontrivial_cycle_text(witness_left)}",
        f"    witness_right={nontrivial_cycle_text(witness_right)}",
        f"    ell={witness_ell} E_left={witness_values[0]} E_right={witness_values[1]}",
        f"  n_times_pbv_l1={float(n * pbv_l1):.12g}",
        f"  k2_times_Vz={float(k * k * variation_z):.12g}",
        f"  k2_Lambda_over_R={float(scale):.12g} ratio_to_n={float(scale / n):.12g}",
        f"  eta_triangle={eta_t}",
        "  status=all exact identities passed; finite falsification only",
    ]
    return lines


def main() -> None:
    print("M264 clean-room PBV reduction checks")
    print("reads_M261=false imports_M261=false seed=null arithmetic=Fraction")
    print("e2_affine_split=verified_symbolically_via_sum_C=n-8+2*1_T+I")
    for k in (3, 5):
        for line in audit_k(k):
            print(line)
    print("scope=no PBV/sign/FCL1/gap/mixing/Terminal inference")


if __name__ == "__main__":
    main()
