#!/usr/bin/env python3
"""Clean-room exact checks for the frozen M272 identities.

This file is self-contained.  It imports no project module and reads no
predecessor or M272 artifact.  It rebuilds the relevant minimal-factorization
laws directly from cycle decompositions.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from pathlib import Path


Perm = tuple[int, ...]
Measure = dict[Perm, Fraction]
Vector = tuple[Fraction, ...]


def compose(p: Perm, q: Perm) -> Perm:
    """Return p q under (p q)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    ans = [0] * len(p)
    for x, y in enumerate(p):
        ans[y] = x
    return tuple(ans)


def identity(n: int) -> Perm:
    return tuple(range(n))


def transposition(n: int, a: int, b: int) -> Perm:
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def cycle_perm(n: int, vertices: list[int]) -> Perm:
    p = list(range(n))
    for a, b in zip(vertices, vertices[1:] + vertices[:1]):
        p[a] = b
    return tuple(p)


@lru_cache(maxsize=None)
def cycles(p: Perm) -> tuple[tuple[int, ...], ...]:
    seen: set[int] = set()
    ans: list[tuple[int, ...]] = []
    for start in range(len(p)):
        if start in seen:
            continue
        cyc: list[int] = []
        x = start
        while x not in seen:
            seen.add(x)
            cyc.append(x)
            x = p[x]
        ans.append(tuple(cyc))
    return tuple(ans)


def rank(p: Perm) -> int:
    return len(p) - len(cycles(p))


@lru_cache(maxsize=None)
def tau(d: int) -> Fraction:
    if d <= 0:
        return Fraction(0)
    if d == 1:
        return Fraction(1)
    return Fraction(d ** (d - 2), math.factorial(d - 1))


@lru_cache(maxsize=None)
def factor_count(p: Perm) -> Fraction:
    r = rank(p)
    ans = Fraction(math.factorial(r))
    for cyc in cycles(p):
        ans *= tau(len(cyc))
    assert ans.denominator == 1
    return ans


@lru_cache(maxsize=None)
def internal_edges(p: Perm) -> tuple[Perm, ...]:
    ans: list[Perm] = []
    n = len(p)
    for cyc in cycles(p):
        if len(cyc) < 2:
            continue
        for i, a in enumerate(cyc):
            for b in cyc[i + 1 :]:
                ans.append(transposition(n, a, b))
    return tuple(ans)


def edge_vertices(e: Perm) -> tuple[int, int]:
    moved = [x for x in range(len(e)) if e[x] != x]
    assert len(moved) == 2
    return moved[0], moved[1]


def first_law(q: Perm) -> dict[Perm, Fraction]:
    total = factor_count(q)
    law: dict[Perm, Fraction] = {}
    r = rank(q)
    for e in internal_edges(q):
        rem = compose(e, q)
        assert rank(rem) == r - 1
        law[e] = factor_count(rem) / total
    assert sum(law.values(), Fraction()) == 1
    return law


def ordered_two_law(q: Perm) -> dict[tuple[Perm, Perm], Fraction]:
    total = factor_count(q)
    law: dict[tuple[Perm, Perm], Fraction] = {}
    r = rank(q)
    for e in internal_edges(q):
        rem1 = compose(e, q)
        for f in internal_edges(rem1):
            rem2 = compose(f, rem1)
            assert rank(rem2) == r - 2
            law[(e, f)] = factor_count(rem2) / total
    assert sum(law.values(), Fraction()) == 1
    return law


def split_of_edge(q: Perm, e: Perm) -> int:
    a, b = edge_vertices(e)
    for cyc in cycles(q):
        if a in cyc:
            assert b in cyc
            d = len(cyc)
            ia, ib = cyc.index(a), cyc.index(b)
            delta = (ib - ia) % d
            return min(delta, d - delta)
    raise AssertionError("edge is not internal")


def add_mass(out: defaultdict, key, value: Fraction) -> None:
    out[key] += value
    if out[key] == 0:
        del out[key]


def push_channel_one(
    exterior: dict[Perm, Fraction], middle: dict[Perm, Fraction]
) -> Measure:
    out: defaultdict[Perm, Fraction] = defaultdict(Fraction)
    for e, we in exterior.items():
        for f, wf in middle.items():
            add_mass(out, compose(e, f), we * wf)
    assert sum(out.values(), Fraction()) == 1
    return dict(out)


def push_channel_two(raw: dict[tuple[Perm, Perm], Fraction]) -> Measure:
    out: defaultdict[Perm, Fraction] = defaultdict(Fraction)
    for (e, f), weight in raw.items():
        add_mass(out, compose(e, f), weight)
    assert sum(out.values(), Fraction()) == 1
    return dict(out)


def scaled_add(out: defaultdict, measure: Measure, scale: Fraction) -> None:
    for state, weight in measure.items():
        add_mass(out, state, scale * weight)


def signed_difference(a: Measure, b: Measure) -> Measure:
    out: defaultdict[Perm, Fraction] = defaultdict(Fraction)
    scaled_add(out, a, Fraction(1))
    scaled_add(out, b, Fraction(-1))
    return dict(out)


def expectation(measure: Measure, observable) -> Fraction:
    return sum((weight * observable(state) for state, weight in measure.items()), Fraction())


def conditional_product_laws(
    q: Perm,
    first: dict[Perm, Fraction],
    raw_two: dict[tuple[Perm, Perm], Fraction],
    middle: dict[Perm, Fraction],
) -> tuple[dict[int, Fraction], dict[int, Measure], dict[int, Measure]]:
    split_mass: defaultdict[int, Fraction] = defaultdict(Fraction)
    one_raw: dict[int, defaultdict[Perm, Fraction]] = defaultdict(lambda: defaultdict(Fraction))
    two_raw: dict[int, defaultdict[Perm, Fraction]] = defaultdict(lambda: defaultdict(Fraction))
    for e, we in first.items():
        s = split_of_edge(q, e)
        split_mass[s] += we
        for f, wf in middle.items():
            add_mass(one_raw[s], compose(e, f), we * wf)
    for (e, f), weight in raw_two.items():
        s = split_of_edge(q, e)
        add_mass(two_raw[s], compose(e, f), weight)
    one: dict[int, Measure] = {}
    two: dict[int, Measure] = {}
    for s, mass in split_mass.items():
        one[s] = {state: weight / mass for state, weight in one_raw[s].items()}
        two[s] = {state: weight / mass for state, weight in two_raw[s].items()}
        assert sum(one[s].values(), Fraction()) == 1
        assert sum(two[s].values(), Fraction()) == 1
    return dict(split_mass), one, two


def nu_cycle(d: int, a: int) -> Fraction:
    if not 1 <= a <= d - 1:
        return Fraction(0)
    return tau(a) * tau(d - a) / ((d - 1) * tau(d))


def quantile_coupling(
    q: dict[int, Fraction], p: dict[int, Fraction]
) -> dict[tuple[int, int], Fraction]:
    def intervals(law: dict[int, Fraction]):
        lo = Fraction()
        ans = {}
        for x in sorted(law):
            hi = lo + law[x]
            ans[x] = (lo, hi)
            lo = hi
        assert lo == 1
        return ans

    iq, ip = intervals(q), intervals(p)
    coupling = {}
    for s, (lo_s, hi_s) in iq.items():
        for t, (lo_t, hi_t) in ip.items():
            mass = max(Fraction(), min(hi_s, hi_t) - max(lo_s, lo_t))
            if mass:
                coupling[(s, t)] = mass
    assert sum(coupling.values(), Fraction()) == 1
    for s in q:
        assert sum(w for (ss, _), w in coupling.items() if ss == s) == q[s]
    for t in p:
        assert sum(w for (_, tt), w in coupling.items() if tt == t) == p[t]
    return coupling


@lru_cache(maxsize=None)
def support(state: Perm) -> frozenset[int]:
    return frozenset(x for x in range(len(state)) if state[x] != x)


def product_kind(state: Perm) -> str:
    size = len(support(state))
    assert size in (3, 4)
    return "T" if size == 3 else "D"


def collision(state: Perm, ell: int) -> int:
    n = len(state)
    moved = support(state)
    return sum(
        1
        for r in range(n)
        if (r + 1) % n in moved and (r + ell + 1) % n in moved
    )


@lru_cache(maxsize=None)
def owner_data(state: Perm):
    n = len(state)
    h = cycle_perm(n, list(range(n)))
    residual = compose(inverse(state), h)
    residual_cycles = cycles(residual)
    owner_of_vertex = {}
    owner_size = {}
    for idx, cyc in enumerate(residual_cycles):
        owner_size[idx] = len(cyc)
        for x in cyc:
            owner_of_vertex[x] = idx
    owners: list[int | None] = []
    for r in range(n):
        head = (r + 1) % n
        owners.append(owner_of_vertex[r] if state[head] == head else None)
    assert len(residual_cycles) == 3
    return tuple(owners), owner_size


def kappa(owner_size: dict[int, int], a: int | None, b: int | None) -> Fraction:
    if a is None or b is None:
        return Fraction(0)
    da, db = owner_size[a], owner_size[b]
    if a == b:
        return tau(da - 2) / tau(da)
    return tau(da - 1) * tau(db - 1) / (tau(da) * tau(db))


def endpoint_charge(state: Perm, ell: int, x: int) -> Fraction:
    n = len(state)
    owners, sizes = owner_data(state)
    c = owners[(x - ell) % n]
    return kappa(sizes, c, owners[(x + 1) % n]) - kappa(sizes, c, owners[x])


def endpoint(state: Perm, ell: int) -> Fraction:
    return sum((endpoint_charge(state, ell, x) for x in range(len(state))), Fraction())


def vector_add(a: Vector, b: Vector, scale: Fraction = Fraction(1)) -> Vector:
    return tuple(x + scale * y for x, y in zip(a, b))


def vector_scale(scale: Fraction, a: Vector) -> Vector:
    return tuple(scale * x for x in a)


def vector_norm(a: Vector) -> Fraction:
    return sum((abs(x) for x in a), Fraction())


def delta_collision_vector(state: Perm) -> Vector:
    n = len(state)
    return tuple(collision(state, ell + 1) - collision(state, ell) for ell in range(2, n - 2))


def weighted_vector(raw, selector) -> Vector:
    entries = list(raw.items())
    assert entries
    n = len(entries[0][0][0])
    ans = tuple(Fraction() for _ in range(n - 4))
    for atom, weight in entries:
        if selector(atom):
            e, f = atom
            ans = vector_add(ans, delta_collision_vector(compose(e, f)), weight)
    return ans


def qstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def check_rank(k: int) -> dict:
    n = 3 * k
    ident = identity(n)
    c_minus = cycle_perm(n, list(range(0, k)))
    c_plus = cycle_perm(n, list(range(2 * k, 3 * k)))
    f_source = compose(c_minus, c_plus)
    l_source = cycle_perm(n, list(range(1, k)) + list(range(2 * k, 3 * k)))
    m_source = cycle_perm(n, list(range(k, 2 * k)))
    assert compose(f_source, m_source) != ident

    first_l = first_law(l_source)
    first_f = first_law(f_source)
    first_m = first_law(m_source)
    raw_l = ordered_two_law(l_source)
    raw_f = ordered_two_law(f_source)

    h1b = push_channel_one(first_l, first_m)
    h1a = push_channel_one(first_f, first_m)
    h2b = push_channel_two(raw_l)
    h2a = push_channel_two(raw_f)

    p, phi1, phi2 = conditional_product_laws(
        l_source, first_l, raw_l, first_m
    )
    q, psi1, psi2 = conditional_product_laws(
        f_source, first_f, raw_f, first_m
    )
    assert sorted(p) == list(range(1, k))
    assert sorted(q) == list(range(1, (k - 1) // 2 + 1))
    for s in p:
        assert p[s] == (2 * k - 1) * nu_cycle(2 * k - 1, s)
    for s in q:
        assert q[s] == k * nu_cycle(k, s)

    d_cum: dict[int, Fraction] = {}
    running = Fraction()
    for u in range(1, k):
        running += p[u] - q.get(u, Fraction())
        d_cum[u] = running
    assert d_cum[k - 1] == 0
    assert all(d_cum[u] < 0 for u in range(1, k - 1))

    for hb, ha, phi, psi in (
        (h1b, h1a, phi1, psi1),
        (h2b, h2a, phi2, psi2),
    ):
        lhs = signed_difference(hb, ha)
        rhs: defaultdict[Perm, Fraction] = defaultdict(Fraction)
        for u in range(1, k - 1):
            scaled_add(rhs, phi[u], d_cum[u])
            scaled_add(rhs, phi[u + 1], -d_cum[u])
        for s, mass in q.items():
            scaled_add(rhs, phi[s], mass)
            scaled_add(rhs, psi[s], -mass)
        assert dict(rhs) == lhs

    coupling = quantile_coupling(q, p)
    assert all(s <= t for s, t in coupling)
    for u in range(1, k - 1):
        crossing = sum(
            mass for (s, t), mass in coupling.items() if s <= u < t
        )
        assert crossing == -d_cum[u]

    m = k - 1
    denom = 3 * m * (3 * m - 1)
    alpha1 = Fraction(4 * m * m, denom)
    alpha2 = Fraction(2 * m * (2 * m - 1), denom)
    eta: defaultdict[Perm, Fraction] = defaultdict(Fraction)
    scaled_add(eta, h1b, alpha1)
    scaled_add(eta, h1a, -alpha1)
    scaled_add(eta, h2b, alpha2)
    scaled_add(eta, h2a, -alpha2)
    assert sum(eta.values(), Fraction()) == 0

    # Direct phase normalization and the literal good/bad partition.
    u_minus = set(range(1, k))
    u_plus = set(range(2 * k, 3 * k))
    phase_rows = []
    good_vector: list[Fraction] = []
    bad_vector: list[Fraction] = []
    for ell in range(2, n - 2):
        eta_e = expectation(dict(eta), lambda state, e=ell: endpoint(state, e))
        profile_by_kind = {
            kind: sum(
                (
                    weight * endpoint(state, ell) / n
                    for state, weight in eta.items()
                    if product_kind(state) == kind
                ),
                Fraction(),
            )
            for kind in ("T", "D")
        }
        assert sum(profile_by_kind.values(), Fraction()) == eta_e / n

        good = Fraction()
        bad = Fraction()
        for e, we in first_l.items():
            a, b = edge_vertices(e)
            is_bad = (a in u_minus and b in u_plus) or (b in u_minus and a in u_plus)
            for mid, wm in first_m.items():
                value = alpha1 * we * wm * endpoint(compose(e, mid), ell)
                bad += value if is_bad else 0
                good += 0 if is_bad else value
        for (e, second), weight in raw_l.items():
            a, b = edge_vertices(e)
            is_bad = (a in u_minus and b in u_plus) or (b in u_minus and a in u_plus)
            value = alpha2 * weight * endpoint(compose(e, second), ell)
            bad += value if is_bad else 0
            good += 0 if is_bad else value
        for e, we in first_f.items():
            is_bad = 0 in edge_vertices(e)
            for mid, wm in first_m.items():
                value = -alpha1 * we * wm * endpoint(compose(e, mid), ell)
                bad += value if is_bad else 0
                good += 0 if is_bad else value
        for (e, second), weight in raw_f.items():
            is_bad = 0 in edge_vertices(e)
            value = -alpha2 * weight * endpoint(compose(e, second), ell)
            bad += value if is_bad else 0
            good += 0 if is_bad else value
        assert good + bad == eta_e
        good_vector.append(good)
        bad_vector.append(bad)
        phase_rows.append(
            {
                "ell": ell,
                "eta_E_exact": qstr(eta_e),
                "profile_scalar_exact": qstr(eta_e / n),
                "good_exact": qstr(good),
                "bad_exact": qstr(bad),
            }
        )
    if k == 3:
        assert any(value != 0 for value in good_vector)

    # Channel-one collision identity.
    rho_a: dict[int, Fraction] = {}
    rho_b: dict[int, Fraction] = {}
    for a in range(1, k):
        rho_a[a] = (k - a) * nu_cycle(k, a)
    for a in range(1, 2 * k):
        straight = max(k - 1 - a, 0) + max(k - a, 0)
        crossing = (
            a - 1
            if 2 <= a <= k
            else (2 * k - a if k < a <= 2 * k - 1 else 0)
        )
        rho_b[a] = straight * nu_cycle(2 * k - 1, a) + crossing * nu_cycle(2 * k - 1, a - 1)
    assert sum(rho_a.values(), Fraction()) == 1
    assert sum(rho_b.values(), Fraction()) == 1
    delta_rho = {a: rho_b.get(a, Fraction()) - rho_a.get(a, Fraction()) for a in range(1, 2 * k)}
    delta_a = [Fraction() for _ in range(n)]
    middle_intensity = [Fraction() for _ in range(n)]
    for v in range(n):
        a_b = Fraction(2, 2 * k - 1) if v in u_minus or v in u_plus else Fraction()
        a_a = Fraction(1, k) if v == 0 or v in u_minus or v in u_plus else Fraction()
        delta_a[v] = a_b - a_a
        middle_intensity[v] = Fraction(2, k) if k <= v <= 2 * k - 1 else Fraction()
    assert sum(abs(x) for x in delta_a) == Fraction(2, k)
    circular_delta_middle = sum(
        abs(middle_intensity[(v + 1) % n] - middle_intensity[v]) for v in range(n)
    )
    assert circular_delta_middle == Fraction(4, k)
    eta1_collision = []
    for ell in range(n):
        direct = expectation(h1b, lambda state, e=ell: collision(state, e)) - expectation(
            h1a, lambda state, e=ell: collision(state, e)
        )
        formula = delta_rho.get(ell, Fraction()) + delta_rho.get(n - ell, Fraction())
        formula += sum(
            delta_a[v] * middle_intensity[(v + ell) % n]
            + middle_intensity[v] * delta_a[(v + ell) % n]
            for v in range(n)
        )
        assert direct == formula
        eta1_collision.append(direct)

    # Channel-two shared/disjoint reduction.
    def shares(atom: tuple[Perm, Perm]) -> bool:
        e, second = atom
        return bool(set(edge_vertices(e)) & set(edge_vertices(second)))

    p_hat: dict[int, Fraction] = {}
    q_hat: dict[int, Fraction] = {}
    phi_d: dict[int, Vector] = {}
    psi_d: dict[int, Vector] = {}
    gamma_l: dict[int, Fraction] = {}
    gamma_f: dict[int, Fraction] = {}
    zero_vector = tuple(Fraction() for _ in range(n - 4))
    for s in p:
        shared = sum(
            weight for atom, weight in raw_l.items()
            if split_of_edge(l_source, atom[0]) == s and shares(atom)
        )
        disjoint = p[s] - shared
        p_hat[s] = disjoint
        gamma_l[s] = shared / p[s]
        expected_gamma = Fraction(2, 2 * k - 3) * (
            2 - Fraction(1, s) - Fraction(1, 2 * k - 1 - s)
        )
        assert gamma_l[s] == expected_gamma
        accum = zero_vector
        for atom, weight in raw_l.items():
            if split_of_edge(l_source, atom[0]) == s and not shares(atom):
                accum = vector_add(accum, delta_collision_vector(compose(*atom)), weight)
        assert disjoint > 0
        phi_d[s] = vector_scale(1 / disjoint, accum)
    for s in q:
        shared = sum(
            weight for atom, weight in raw_f.items()
            if split_of_edge(f_source, atom[0]) == s and shares(atom)
        )
        disjoint = q[s] - shared
        q_hat[s] = disjoint
        gamma_f[s] = shared / q[s]
        expected_gamma = Fraction(2, 2 * k - 3) * (
            2 - Fraction(1, s) - Fraction(1, k - s)
        )
        assert gamma_f[s] == expected_gamma
        accum = zero_vector
        for atom, weight in raw_f.items():
            if split_of_edge(f_source, atom[0]) == s and not shares(atom):
                accum = vector_add(accum, delta_collision_vector(compose(*atom)), weight)
        assert disjoint > 0
        psi_d[s] = vector_scale(1 / disjoint, accum)

    shared_l = sum(p[s] * gamma_l[s] for s in p)
    shared_f = sum(q[s] * gamma_f[s] for s in q)
    assert shared_l == Fraction(3, 2 * k - 1)
    assert shared_f == Fraction(3 * (k - 2), k * (2 * k - 3))
    e_hat: dict[int, Fraction] = {}
    running = Fraction()
    for u in range(1, k):
        running += p_hat[u] - q_hat.get(u, Fraction())
        e_hat[u] = running
    endpoint_expected = Fraction(-6 * (k - 1), k * (2 * k - 1) * (2 * k - 3))
    assert e_hat[k - 1] == endpoint_expected

    rd = zero_vector
    theta = zero_vector
    for atom, weight in raw_l.items():
        vec = delta_collision_vector(compose(*atom))
        if shares(atom):
            theta = vector_add(theta, vec, weight)
        else:
            rd = vector_add(rd, vec, weight)
    for atom, weight in raw_f.items():
        vec = delta_collision_vector(compose(*atom))
        if shares(atom):
            theta = vector_add(theta, vec, -weight)
        else:
            rd = vector_add(rd, vec, -weight)

    csbv = vector_scale(e_hat[k - 1], phi_d[k - 1])
    for u in range(1, k - 1):
        csbv = vector_add(csbv, vector_add(phi_d[u], phi_d[u + 1], Fraction(-1)), e_hat[u])
    cebv = zero_vector
    for s in q:
        cebv = vector_add(cebv, vector_add(phi_d[s], psi_d[s], Fraction(-1)), q_hat[s])
    assert vector_add(csbv, cebv) == rd
    assert vector_norm(theta) <= 12 * (shared_l + shared_f)

    eta2_delta = vector_add(theta, rd)
    return {
        "k": k,
        "n": n,
        "raw_counts": {
            "first_L": len(first_l),
            "first_F": len(first_f),
            "ordered_L": len(raw_l),
            "ordered_F": len(raw_f),
            "H1B_states": len(h1b),
            "H1A_states": len(h1a),
            "H2B_states": len(h2b),
            "H2A_states": len(h2a),
        },
        "split_laws": {
            "p": {str(s): qstr(p[s]) for s in p},
            "q": {str(s): qstr(q[s]) for s in q},
            "D": {str(u): qstr(d_cum[u]) for u in d_cum},
        },
        "quantile_coupling": {
            f"{s},{t}": qstr(weight) for (s, t), weight in coupling.items()
        },
        "phase": {
            "rows": phase_rows,
            "n_times_good_l1_exact": qstr(n * sum(abs(x) for x in good_vector)),
            "n_times_bad_l1_exact": qstr(n * sum(abs(x) for x in bad_vector)),
            "good_nonzero": any(x != 0 for x in good_vector),
        },
        "channel_one": {
            "rho_A_TV_exact": qstr(sum(abs(rho_a.get(a + 1, Fraction()) - rho_a.get(a, Fraction())) for a in range(0, 2 * k))),
            "rho_B_TV_exact": qstr(sum(abs(rho_b.get(a + 1, Fraction()) - rho_b.get(a, Fraction())) for a in range(0, 2 * k))),
            "delta_rho_TV_exact": qstr(sum(abs(delta_rho.get(a + 1, Fraction()) - delta_rho.get(a, Fraction())) for a in range(0, 2 * k))),
            "derivative_l1_exact": qstr(sum(abs(eta1_collision[e + 1] - eta1_collision[e]) for e in range(2, n - 2))),
        },
        "channel_two": {
            "gamma_L": {str(s): qstr(gamma_l[s]) for s in gamma_l},
            "gamma_F": {str(s): qstr(gamma_f[s]) for s in gamma_f},
            "shared_L_exact": qstr(shared_l),
            "shared_F_exact": qstr(shared_f),
            "disjoint_endpoint_exact": qstr(e_hat[k - 1]),
            "theta_l1_exact": qstr(vector_norm(theta)),
            "CSBV_l1_exact": qstr(vector_norm(csbv)),
            "CEBV_l1_exact": qstr(vector_norm(cebv)),
            "eta2_delta_l1_exact": qstr(vector_norm(eta2_delta)),
        },
        "checks": {
            "raw_normalizations": True,
            "abel_measures": True,
            "quantile_crossings": True,
            "phase_factor_and_partition": True,
            "channel_one_collision_identity": True,
            "channel_two_gamma_endpoint_abel": True,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    results = [check_rank(k) for k in (3, 5)]
    payload = {
        "status": "exact finite checks passed",
        "scope": "clean-room k=3,5 falsification only",
        "convention": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "repository_commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
        "python": platform.python_version(),
        "deterministic": True,
        "seed": None,
        "nonstandard_dependencies": [],
        "input_artifacts": [],
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-76/mission-M276-m272-fresh-referee/independent_check.py "
            "--output experiments/20260811-polynomial-mixing-resolution/"
            "cycle-76/mission-M276-m272-fresh-referee/independent_results.json"
        ),
        "results": results,
    }
    Path(args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
