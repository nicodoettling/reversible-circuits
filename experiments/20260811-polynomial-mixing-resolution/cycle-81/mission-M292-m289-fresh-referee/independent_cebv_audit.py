#!/usr/bin/env python3
"""Independent exact/formula audit for M289; imports no project/M289 code."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction as F
from itertools import combinations


def comp(p, q):
    return tuple(p[q[x]] for x in range(len(p)))


def inv(p):
    z = [0] * len(p)
    for x, y in enumerate(p):
        z[y] = x
    return tuple(z)


def transposition(n, a, b):
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def cycle(n, vertices):
    p = list(range(n))
    for a, b in zip(vertices, vertices[1:] + vertices[:1]):
        p[a] = b
    return tuple(p)


def cycle_lengths(p):
    seen = set()
    out = []
    for x in range(len(p)):
        if x in seen:
            continue
        y = x
        d = 0
        while y not in seen:
            seen.add(y)
            d += 1
            y = p[y]
        out.append(d)
    return out


def tau(d):
    if d == 1:
        return F(1)
    return F(d ** (d - 2), math.factorial(d - 1))


def completion_count(p, expected_rank):
    ds = cycle_lengths(p)
    rank = len(p) - len(ds)
    if rank != expected_rank:
        return F(0)
    ans = F(math.factorial(rank))
    for d in ds:
        ans *= tau(d)
    return ans


def ordered_two_weight(target, e, f, target_rank, denominator):
    residual = comp(inv(comp(e, f)), target)
    return completion_count(residual, target_rank - 2) / denominator


def borel0(r):
    """The rational part of b_r; exponentials cancel in every exact ratio."""
    return F(r ** (r - 1), math.factorial(r))


def nu(d, s):
    return tau(s) * tau(d - s) / ((d - 1) * tau(d))


def split_law(d, s):
    return d * nu(d, s)


def h(r, R):
    return F((r - 1) * (r - 2), r * R)


def K(R, r, x):
    if not (1 <= x < r):
        return F(0)
    return borel0(x) * borel0(r - x) / (R * borel0(r))


def U(R, r, x):
    if not (1 <= x < r):
        return F(0)
    first = (r - x - 1) * K(R, r, x) if x <= r - 2 else F(0)
    return first + F(4 * (r - 1), r * R) - 2 * K(R, r, x)


def Z(R, M, r, d):
    return U(R, r, d) + U(R, r, M - d)


def ed_embed(k, half):
    n, D = 3 * k, 2 * k - 1
    z = [F(0) for _ in range(n)]
    f = lambda d: half[d] if 0 <= d < len(half) else F(0)
    for ell in range(1, k + 1):
        z[ell] = (D - 2 * ell) * f(ell) / D + (ell - 1) * f(ell - 1) / D
    for r in range(1, k):
        z[k + r] = (r * f(r) + (k - r) * f(k - r)) / D
    for ell in range(1, k + 1):
        z[n - ell] = z[ell]
    assert all(z[ell] == z[n - ell] for ell in range(1, n))
    return z


def ek_embed(k, half):
    n = 3 * k
    z = [F(0) for _ in range(n)]
    for ell in range(1, k):
        d = min(ell, k - ell)
        z[ell] = F(k - ell, k) * half[d]
        z[n - ell] = z[ell]
    return z


def coordinate_embed(vertices, half, n):
    M = len(vertices)
    z = [F(0) for _ in range(n)]
    for d in range(1, M):
        c = half[min(d, M - d)]
        for t in range(M):
            ell = (vertices[(t + d) % M] - vertices[t]) % n
            z[ell] += c / M
    return z


def collision_add(profile, support, weight):
    n = len(profile)
    for x in support:
        for y in support:
            if x != y:
                profile[(y - x) % n] += weight


def first_chords(vertices, s, n):
    out = []
    M = len(vertices)
    for t in range(M):
        a, b = vertices[t], vertices[(t + s) % M]
        out.append((frozenset((a, b)), transposition(n, a, b)))
    assert len({edge for edge, _ in out}) == M
    return out


def direct_raw_profile(k, side, s):
    n, D, R = 3 * k, 2 * k - 1, 2 * k - 3
    C0 = list(range(k))
    C2 = list(range(2 * k, 3 * k))
    V = list(range(1, k)) + list(range(2 * k, 3 * k))
    if side == "B":
        target = cycle(n, V)
        chords = first_chords(V, s, n)
        split_mass = split_law(D, s)
    else:
        target = comp(cycle(n, C0), cycle(n, C2))
        chords = first_chords(C0, s, n) + first_chords(C2, s, n)
        split_mass = split_law(k, s)
    target_rank = 2 * k - 2
    denominator = completion_count(target, target_rank)
    profile = [F(0) for _ in range(n)]
    raw_mass = F(0)
    atom_count = 0
    trans = [(frozenset(edge), transposition(n, *edge)) for edge in combinations(range(n), 2)]
    first_mass = F(0)
    for e_support, e in chords:
        row_mass = F(0)
        for f_support, f in trans:
            w = ordered_two_weight(target, e, f, target_rank, denominator)
            row_mass += w
            if w and e_support.isdisjoint(f_support):
                normalized = w / split_mass
                raw_mass += normalized
                atom_count += 1
                collision_add(profile, e_support | f_support, normalized)
        first_mass += row_mass
    assert first_mass == split_mass
    assert sum(profile) == 12 * raw_mass
    return profile, raw_mass, atom_count


def formula_profiles(k, s):
    n, D, R, j = 3 * k, 2 * k - 1, 2 * k - 3, (k - 1) // 2
    aL = h(s, R) + h(D - s, R)
    u = F(k - 1, R)
    aF = h(s, R) + h(k - s, R) + u
    bhalf = [F(0)] * (k + 1)
    for d in range(1, k):
        bhalf[d] = aL * (d == s) + Z(R, D, s, d) + Z(R, D, D - s, d)
    B = ed_embed(k, bhalf)

    ahalf = [F(0)] * (j + 2)
    for d in range(1, j + 1):
        ahalf[d] = (
            aF * (d == s)
            + Z(R, k, s, d)
            + Z(R, k, k - s, d)
            + k * K(R, k, d)
        )
    A = ek_embed(k, ahalf)
    C0, C2 = range(k), range(2 * k, 3 * k)
    N = [0] * n
    for x in C0:
        for y in C2:
            N[(y - x) % n] += 1
    X = [F(4 * u * (N[ell] + N[(n - ell) % n]), k * k) for ell in range(n)]
    A = [x + y for x, y in zip(A, X)]
    assert sum(B) == 12 * aL
    assert sum(A) == 12 * aF
    delta = aF / aL - 1
    delta_formula = F(2 * (k - 1), R * (k - s) * (D - s)) / aL
    assert delta == delta_formula
    return B, A, aL, aF, X


def circ_tv(v):
    return sum(abs(v[(i + 1) % len(v)] - v[i]) for i in range(len(v)))


def line_tv(v):
    return sum(abs(b - a) for a, b in zip(v, v[1:]))


def cebv_norm(H):
    n = len(H)
    return sum(abs(H[ell + 1] - H[ell]) for ell in range(2, n - 2))


def frac(x):
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def exact_case(k):
    j = (k - 1) // 2
    H_direct = [F(0)] * (3 * k)
    H_formula = [F(0)] * (3 * k)
    rows = []
    for s in range(1, j + 1):
        Bf, Af, aL, aF, X = formula_profiles(k, s)
        Bd, massB, atomsB = direct_raw_profile(k, "B", s)
        Ad, massA, atomsA = direct_raw_profile(k, "A", s)
        assert Bd == Bf and Ad == Af
        assert massB == aL and massA == aF
        q = split_law(k, s)
        for ell in range(3 * k):
            H_direct[ell] += q * (aF / aL * Bd[ell] - Ad[ell])
            H_formula[ell] += q * (aF / aL * Bf[ell] - Af[ell])
        rows.append({
            "s": s,
            "a_L": frac(aL),
            "a_F": frac(aF),
            "B_atoms": atomsB,
            "A_atoms": atomsA,
            "B_raw_collision_mass": frac(sum(Bd)),
            "A_raw_collision_mass": frac(sum(Ad)),
            "X_mass": frac(sum(X)),
        })
    assert H_direct == H_formula
    return {
        "k": k,
        "rows": rows,
        "cebv_l1": frac(cebv_norm(H_direct)),
        "full_circular_tv": frac(circ_tv(H_direct)),
    }


def phase_test(k):
    n, D, j = 3 * k, 2 * k - 1, (k - 1) // 2
    V = list(range(1, k)) + list(range(2 * k, 3 * k))
    C0 = list(range(k))
    fD = [F(0)] * (k + 1)
    fk = [F(0)] * (j + 2)
    for d in range(1, k):
        fD[d] = F(d * d + 3, 7 * d + 5)
    for d in range(1, j + 1):
        fk[d] = F(d * d + 1, 5 * d + 2)
    assert ed_embed(k, fD) == coordinate_embed(V, fD, n)
    assert ek_embed(k, fk) == coordinate_embed(C0, fk, n)


def floating_b(r):
    return math.exp(-r) * (r ** (r - 1)) / math.factorial(r)


def floating_U(R, r, x):
    if not (1 <= x < r):
        return 0.0
    kval = floating_b(x) * floating_b(r - x) / (R * floating_b(r))
    return ((r - x - 1) * kval if x <= r - 2 else 0.0) + 4 * (r - 1) / (r * R) - 2 * kval


def analytic_boundary_scan(ks):
    max_stab = {"scaled_tv": -1.0}
    special_stab = []
    max_untouched = {"scaled_tv": -1.0}
    max_triangle = {"scaled_tv": -1.0}
    lemma1_rows = []
    tail_rows = []
    for k in ks:
        n, D, R, j = 3 * k, 2 * k - 1, 2 * k - 3, (k - 1) // 2
        phase_test(k)
        for M in (k, D):
            half = (M - 1) // 2
            for r in range(1, M):
                err = [0.0]
                for d in range(1, half + 1):
                    z = floating_U(R, r, d) + floating_U(R, r, M - d)
                    ref = (r / R) * floating_b(d) + 4 / R
                    err.append(z - ref)
                err.append(0.0)
                score = R * line_tv(err)
                if score > max_stab["scaled_tv"]:
                    max_stab = {"scaled_tv": score, "k": k, "M": M, "r": r}
                if k in (3, 5) and r in {1, 2, M - 1}:
                    special_stab.append({"k": k, "M": M, "r": r, "R_tv": score})
        terr = [0.0]
        for d in range(1, j + 1):
            Tk = k * floating_b(d) * floating_b(k - d) / (R * floating_b(k))
            terr.append(Tk - (k / R) * floating_b(d))
        terr.append(0.0)
        uscore = k * line_tv(terr)
        if uscore > max_untouched["scaled_tv"]:
            max_untouched = {"scaled_tv": uscore, "k": k}

        _, _, _, _, X = formula_profiles(k, 1)
        tscore = k * circ_tv(X)
        if float(tscore) > max_triangle["scaled_tv"]:
            max_triangle = {"scaled_tv": float(tscore), "k": k, "exact": frac(tscore)}

        # Lemma 1 on the actual q_s a_L(s), including every seam and endpoint.
        w = [F(0)] * (j + 1)
        a = [F(0)]
        for s in range(1, j + 1):
            aL = h(s, R) + h(D - s, R)
            w[s] = split_law(k, s) * aL
            a.append(s * w[s])
        fD = [F(0)] * (k + 1)
        fk = [F(0)] * (j + 2)
        for s in range(1, j + 1):
            fD[s] = fk[s] = w[s]
        lhs = circ_tv([x - y for x, y in zip(ed_embed(k, fD), ek_embed(k, fk))])
        denom = line_tv(a)
        lemma1_rows.append({"k": k, "k_tv": float(k * lhs), "a_tv": float(denom)})

        # Exercise Lemma 1's two extensions: the omitted D-tail of b_d and
        # a height-8/R constant profile including that tail.
        bfull = [0.0] * (k + 1)
        bsym = [0.0] * (j + 2)
        btail = [0.0] * (k + 1)
        cfull = [F(0)] * (k + 1)
        csym = [F(0)] * (j + 2)
        c = F(8, R)
        for d in range(1, k):
            bfull[d] = floating_b(d)
            if d > j:
                btail[d] = floating_b(d)
            cfull[d] = c
        for d in range(1, j + 1):
            bsym[d] = floating_b(d)
            csym[d] = c
        bcmp = circ_tv([x - y for x, y in zip(ed_embed(k, bfull), ek_embed(k, bsym))])
        tail_cost = circ_tv(ed_embed(k, btail))
        ccmp = circ_tv([x - y for x, y in zip(ed_embed(k, cfull), ek_embed(k, csym))])
        tail_rows.append({
            "k": k,
            "k_borel_comparison_tv": k * bcmp,
            "k_borel_tail_embedding_tv": k * tail_cost,
            "k_constant_comparison_tv": float(k * ccmp),
        })
    return {
        "generalized_Z": max_stab,
        "generalized_Z_boundary_rows": special_stab,
        "untouched": max_untouched,
        "triangular_cross": max_triangle,
        "lemma1_actual_profile": lemma1_rows,
        "lemma1_tail_and_constant_profiles": tail_rows,
    }


def formula_case(k):
    j = (k - 1) // 2
    H = [F(0)] * (3 * k)
    HN = [F(0)] * (3 * k)
    qsum = F(0)
    for s in range(1, j + 1):
        B, A, aL, aF, _ = formula_profiles(k, s)
        q = split_law(k, s)
        qsum += q
        delta = aF / aL - 1
        for ell in range(3 * k):
            H[ell] += q * (B[ell] - A[ell]) + q * delta * B[ell]
            HN[ell] += q * delta * B[ell]
    assert qsum == 1
    return {
        "k": k,
        "cebv_l1_exact": frac(cebv_norm(H)) if k <= 5 else None,
        "k_times_cebv": float(k * cebv_norm(H)),
        "full_tv_exact": frac(circ_tv(H)) if k <= 5 else None,
        "k_times_full_tv": float(k * circ_tv(H)),
        "k2_times_normalizer_tv": float(k * k * circ_tv(HN)),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    exact = [exact_case(k) for k in (3, 5)]
    ks = (3, 5, 7, 9, 15, 31, 63)
    result = {
        "status": "all assertions passed",
        "composition": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "target": "CEBV for the auxiliary fixed-cell disjoint channel-two law only",
        "exact_direct_enumeration": exact,
        "formula_scan": [formula_case(k) for k in ks],
        "boundary_scan": analytic_boundary_scan(ks),
        "limitations": "Finite checks are convention/boundary falsifiers, not the asymptotic proof.",
    }
    with open(args.output, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, sort_keys=True)
        fh.write("\n")


if __name__ == "__main__":
    main()
