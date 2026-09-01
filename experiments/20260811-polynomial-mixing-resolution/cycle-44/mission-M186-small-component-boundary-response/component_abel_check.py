#!/usr/bin/env python3
"""Exact k=3,5 calibration of the M186 component Borel--Abel formula.

The checker constructs the source rows literally, reconstructs their two
noncommon channels from independent critical-Borel chord measures, verifies
the measure-valued Abel identity coefficient by coefficient, and checks the
channel-1 face-law collapse and final signed summation-by-parts identity.

Convention: (pq)(x)=p(q(x)); displayed factors multiply left-to-right.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path


Perm = tuple[int, ...]
Key = tuple[int, int]  # (run type, component size)
Poly = tuple[Fraction, Fraction]  # coefficients of 1,E


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def cycle_perm(n: int, vertices: tuple[int, ...]) -> Perm:
    p = list(range(n))
    for x, y in zip(vertices, vertices[1:] + vertices[:1]):
        p[x] = y
    return tuple(p)


def transposition(n: int, x: int, y: int) -> Perm:
    return cycle_perm(n, (x, y))


def cycles(p: Perm) -> list[tuple[int, ...]]:
    seen: set[int] = set()
    ans: list[tuple[int, ...]] = []
    for start in range(len(p)):
        if start in seen:
            continue
        c: list[int] = []
        x = start
        while x not in seen:
            seen.add(x)
            c.append(x)
            x = p[x]
        ans.append(tuple(c))
    return ans


def tau(d: int) -> Fraction:
    assert d >= 1
    return Fraction(d ** (d - 1), math.factorial(d))


def rank(p: Perm) -> int:
    return len(p) - len(cycles(p))


def completion(p: Perm, length: int) -> Fraction:
    if rank(p) != length:
        return Fraction()
    ans = Fraction(math.factorial(length))
    for c in cycles(p):
        ans *= tau(len(c))
    return ans


def internal_edges(n: int, p: Perm) -> list[Perm]:
    ans: list[Perm] = []
    for c in cycles(p):
        if len(c) < 2:
            continue
        for x, y in combinations(c, 2):
            ans.append(transposition(n, x, y))
    return ans


def edge_vertices(e: Perm) -> tuple[int, int]:
    moved = [x for x in range(len(e)) if e[x] != x]
    assert len(moved) == 2
    return tuple(sorted(moved))  # type: ignore[return-value]


def ambient_runs(component: tuple[int, ...], n: int) -> tuple[int, ...]:
    support = set(component)
    starts = sorted(x for x in support if (x - 1) % n not in support)
    assert starts
    ans: list[int] = []
    for start in starts:
        d = 0
        while (start + d) % n in support:
            d += 1
        ans.append(d)
    assert sum(ans) == len(component)
    return tuple(sorted(ans))


def component_counts(s: Perm, h: Perm) -> dict[Key, int]:
    q = compose(inverse(s), h)
    ans: defaultdict[Key, int] = defaultdict(int)
    cs = cycles(q)
    assert len(cs) == 3
    for c in cs:
        runs = ambient_runs(c, len(s))
        assert len(runs) in (1, 2)
        ans[(len(runs), len(c))] += 1
    return dict(ans)


def add_scaled(dst: defaultdict[Key, Fraction], src: dict[Key, int], w: Fraction) -> None:
    for key, multiplicity in src.items():
        dst[key] += w * multiplicity


def sub_maps(a: dict[Key, Fraction], b: dict[Key, Fraction]) -> dict[Key, Fraction]:
    keys = set(a) | set(b)
    return {key: a.get(key, Fraction()) - b.get(key, Fraction()) for key in keys if a.get(key, Fraction()) != b.get(key, Fraction())}


def add_maps(a: dict[Key, Fraction], b: dict[Key, Fraction]) -> dict[Key, Fraction]:
    keys = set(a) | set(b)
    return {key: a.get(key, Fraction()) + b.get(key, Fraction()) for key in keys if a.get(key, Fraction()) + b.get(key, Fraction())}


def scale_map(c: Fraction, a: dict[Key, Fraction]) -> dict[Key, Fraction]:
    return {key: c * value for key, value in a.items() if c * value}


def exact_source_channels(k: int, label: str) -> dict[int, dict[Key, Fraction]]:
    n = 3 * k
    h = cycle_perm(n, tuple(range(n)))
    source = cycle_perm(n, (0, k, 2 * k)) if label == "A" else compose(transposition(n, 0, 1), transposition(n, k, 2 * k))
    q = compose(inverse(source), h)
    original = cycles(q)
    middle_index = next(i for i, c in enumerate(original) if k in c)
    owner = {x: i for i, c in enumerate(original) for x in c}
    denominator = completion(q, n - 3)
    out = {j: defaultdict(Fraction) for j in range(3)}
    masses = defaultdict(Fraction)
    for i, c in enumerate(original):
        if len(c) < 2:
            continue
        for x, y in combinations(c, 2):
            e = transposition(n, x, y)
            q1 = compose(e, q)
            for c2 in cycles(q1):
                if len(c2) < 2:
                    continue
                old = owner[c2[0]]
                assert all(owner[z] == old for z in c2)
                for u, v in combinations(c2, 2):
                    f = transposition(n, u, v)
                    q2 = compose(f, q1)
                    w = completion(q2, n - 5) / denominator
                    if not w:
                        continue
                    j = int(i != middle_index) + int(old != middle_index)
                    s = compose(e, f)
                    add_scaled(out[j], component_counts(s, h), w)
                    masses[j] += w
    assert sum(masses.values(), Fraction()) == 1
    return {j: dict(out[j]) for j in range(3)} | {99: {(j, 0): p for j, p in masses.items()}}  # type: ignore[return-value]


def restrict_to_vertices(n: int, cs: list[tuple[int, ...]]) -> Perm:
    p = list(range(n))
    for c in cs:
        if len(c) < 2:
            continue
        for x, y in zip(c, c[1:] + c[:1]):
            p[x] = y
    return tuple(p)


def first_edge_weights(q: Perm) -> dict[Perm, Fraction]:
    R = rank(q)
    denominator = completion(q, R)
    ans: dict[Perm, Fraction] = {}
    for e in internal_edges(len(q), q):
        w = completion(compose(e, q), R - 1) / denominator
        if w:
            ans[e] = w
    assert sum(ans.values(), Fraction()) == 1
    return ans


def pair_weights(q: Perm) -> dict[tuple[Perm, Perm], Fraction]:
    R = rank(q)
    denominator = completion(q, R)
    ans: dict[tuple[Perm, Perm], Fraction] = {}
    for e in internal_edges(len(q), q):
        q1 = compose(e, q)
        for f in internal_edges(len(q), q1):
            w = completion(compose(f, q1), R - 2) / denominator
            if w:
                ans[(e, f)] = w
    assert sum(ans.values(), Fraction()) == 1
    return ans


def split_size(e: Perm, original_cycles: list[tuple[int, ...]]) -> int:
    x, y = edge_vertices(e)
    c = next(c for c in original_cycles if x in c)
    assert y in c
    pos = {z: i for i, z in enumerate(c)}
    d = (pos[y] - pos[x]) % len(c)
    return min(d, len(c) - d)


def borel_channel_profiles(k: int, label: str, j: int) -> tuple[dict[Key, Fraction], dict[int, dict[Key, Fraction]], dict[int, Fraction]]:
    assert label in ("A", "B") and j in (1, 2)
    n = 3 * k
    h = cycle_perm(n, tuple(range(n)))
    source = cycle_perm(n, (0, k, 2 * k)) if label == "A" else compose(transposition(n, 0, 1), transposition(n, k, 2 * k))
    cs = cycles(compose(inverse(source), h))
    middle = next(c for c in cs if k in c)
    exterior = [c for c in cs if c is not middle and len(c) > 1]
    q_ext = restrict_to_vertices(n, exterior)
    q_mid = restrict_to_vertices(n, [middle])
    ext_first = first_edge_weights(q_ext)
    profiles: dict[int, defaultdict[Key, Fraction]] = defaultdict(lambda: defaultdict(Fraction))
    masses: defaultdict[int, Fraction] = defaultdict(Fraction)
    total: defaultdict[Key, Fraction] = defaultdict(Fraction)
    if j == 1:
        mid_first = first_edge_weights(q_mid)
        for e, pe in ext_first.items():
            split = split_size(e, exterior)
            for f, pf in mid_first.items():
                w = pe * pf
                counts = component_counts(compose(e, f), h)
                add_scaled(profiles[split], counts, w)
                add_scaled(total, counts, w)
                masses[split] += w
    else:
        pairs = pair_weights(q_ext)
        for (e, f), w in pairs.items():
            split = split_size(e, exterior)
            counts = component_counts(compose(e, f), h)
            add_scaled(profiles[split], counts, w)
            add_scaled(total, counts, w)
            masses[split] += w
    assert sum(masses.values(), Fraction()) == 1
    normalized = {
        s: {key: value / masses[s] for key, value in prof.items()}
        for s, prof in profiles.items()
    }
    return dict(total), normalized, dict(masses)


def abel_reconstruct(
    phi: dict[int, dict[Key, Fraction]],
    psi: dict[int, dict[Key, Fraction]],
    p: dict[int, Fraction],
    q: dict[int, Fraction],
    k: int,
) -> dict[Key, Fraction]:
    D: dict[int, Fraction] = {}
    running = Fraction()
    for u in range(1, k):
        running += p.get(u, Fraction()) - q.get(u, Fraction())
        D[u] = running
    assert D[k - 1] == 0
    out: dict[Key, Fraction] = {}
    for u in range(1, k - 1):
        out = add_maps(out, scale_map(D[u], sub_maps(phi[u], phi[u + 1])))
    for s, qs in q.items():
        out = add_maps(out, scale_map(qs, sub_maps(phi[s], psi[s])))
    return out


def per_chord_weight(d: int, split: int) -> Fraction:
    return Fraction(math.factorial(d - 2)) * tau(split) * tau(d - split) / (d ** (d - 2))


def rho_contiguous(k: int) -> dict[int, Fraction]:
    return {a: Fraction(k - a) * per_chord_weight(k, a) for a in range(1, k)}


def cross_count(k: int, a: int) -> int:
    if 2 <= a <= k:
        return a - 1
    if k < a <= 2 * k - 1:
        return 2 * k - a
    return 0


def rho_two_run(k: int) -> dict[int, Fraction]:
    D = 2 * k - 1
    ans: dict[int, Fraction] = {}
    for a in range(1, D + 1):
        same = max(k - 1 - a, 0) + max(k - a, 0)
        value = Fraction()
        if same:
            value += same * per_chord_weight(D, a)
        cross = cross_count(k, a)
        if cross:
            value += cross * per_chord_weight(D, a - 1)
        if value:
            ans[a] = value
    assert sum(ans.values(), Fraction()) == 1
    return ans


def face_size(e: Perm, k: int, label: str) -> int:
    n = 3 * k
    x, y = edge_vertices(e)
    if label == "B" and x < k and y >= 2 * k:
        return n - (y - x)
    return y - x


def channel1_face_check(k: int) -> tuple[dict[Key, Fraction], dict[str, object]]:
    n = 3 * k
    rhoA = rho_contiguous(k)
    rhoB = rho_two_run(k)
    delta = {a: rhoB.get(a, Fraction()) - rhoA.get(a, Fraction()) for a in set(rhoA) | set(rhoB)}
    coeff: defaultdict[Key, Fraction] = defaultdict(Fraction)
    for a, da in delta.items():
        coeff[(1, a)] += da
        for b, pb in rhoA.items():
            coeff[(2, n - a - b)] += da * pb
    weighted_one = sum((abs(v) / a for a, v in delta.items()), Fraction())
    weighted_two = sum((abs(da) * pb / (n - a - b) for a, da in delta.items() for b, pb in rhoA.items()), Fraction())
    return dict(coeff), {
        "rho_A_mass": qstr(sum(rhoA.values(), Fraction())),
        "rho_B_mass": qstr(sum(rhoB.values(), Fraction())),
        "weighted_face_defect_one": qstr(weighted_one),
        "weighted_face_defect_two": qstr(weighted_two),
        "k_times_weighted_face_defect_sum_float": float(k * (weighted_one + weighted_two)),
    }


def u1(d: int) -> Poly:
    U = Fraction() if d == 1 else Fraction(d - 1) * tau(d - 1) / tau(d)
    return (Fraction(-d) - Fraction(1, 2), U)


def u2(d: int) -> Poly:
    assert d >= 2
    U = Fraction(d - 2) * tau(d - 1) / tau(d)
    return (Fraction(-d) + Fraction(1, 2), U)


def padd(a: Poly, b: Poly) -> Poly:
    return (a[0] + b[0], a[1] + b[1])


def pscale(c: Fraction, a: Poly) -> Poly:
    return (c * a[0], c * a[1])


def charge_poly(M: dict[Key, Fraction], cutoff: int) -> Poly:
    ans = (Fraction(), Fraction())
    for (r, d), mass in M.items():
        if d <= cutoff:
            ans = padd(ans, pscale(mass, u1(d) if r == 1 else u2(d)))
    return ans


def sbp_poly(M: dict[Key, Fraction], cutoff: int) -> Poly:
    P = {d: M.get((1, d), Fraction()) for d in range(1, cutoff + 1)}
    N = {d: P[d] + M.get((2, d), Fraction()) for d in range(1, cutoff + 1)}
    ans = pscale(P[1], u1(1))
    if cutoff == 1:
        return ans
    A: dict[int, Fraction] = {}
    C: dict[int, Fraction] = {}
    ra = Fraction()
    rc = Fraction()
    for d in range(2, cutoff + 1):
        ra += N[d]
        rc += P[d]
        A[d], C[d] = ra, rc
    rpoly = {d: padd(u1(d), pscale(Fraction(-1), u2(d))) for d in range(2, cutoff + 1)}
    ans = padd(ans, pscale(A[cutoff], u2(cutoff)))
    ans = padd(ans, pscale(C[cutoff], rpoly[cutoff]))
    for d in range(2, cutoff):
        ans = padd(ans, pscale(A[d], padd(u2(d), pscale(Fraction(-1), u2(d + 1)))))
        ans = padd(ans, pscale(C[d], padd(rpoly[d], pscale(Fraction(-1), rpoly[d + 1]))))
    return ans


def qstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def map_json(M: dict[Key, Fraction]) -> list[dict[str, object]]:
    return [
        {"run_type": r, "size": d, "mass": qstr(value)}
        for (r, d), value in sorted(M.items())
        if value
    ]


def analyze(k: int) -> dict[str, object]:
    n = 3 * k
    directA = exact_source_channels(k, "A")
    directB = exact_source_channels(k, "B")
    massesA = {j: directA[99][(j, 0)] for j in range(3)}
    massesB = {j: directB[99][(j, 0)] for j in range(3)}
    assert massesA == massesB
    alpha1, alpha2 = massesA[1], massesA[2]

    conditional_deltas: dict[int, dict[Key, Fraction]] = {}
    abel_deltas: dict[int, dict[Key, Fraction]] = {}
    for j in (1, 2):
        totalA, psi, q = borel_channel_profiles(k, "A", j)
        totalB, phi, p = borel_channel_profiles(k, "B", j)
        delta = sub_maps(totalB, totalA)
        conditional_deltas[j] = delta
        assert delta == sub_maps(scale_map(1 / massesB[j], directB[j]), scale_map(1 / massesA[j], directA[j]))
        abel = abel_reconstruct(phi, psi, p, q, k)
        assert abel == delta
        abel_deltas[j] = abel

    face_delta, face_stats = channel1_face_check(k)
    assert face_delta == conditional_deltas[1]

    M = add_maps(scale_map(alpha1, conditional_deltas[1]), scale_map(alpha2, conditional_deltas[2]))
    directM = sub_maps(add_maps(directB[1], directB[2]), add_maps(directA[1], directA[2]))
    assert M == directM
    cutoff = n // 2
    charge = charge_poly(M, cutoff)
    sbp = sbp_poly(M, cutoff)
    assert charge == sbp

    prefix = []
    for D in range(2, cutoff + 1):
        all_mass = sum((mass for (r, d), mass in M.items() if 2 <= d <= D), Fraction())
        one_mass = sum((mass for (r, d), mass in M.items() if r == 1 and 2 <= d <= D), Fraction())
        scale = n / math.sqrt(D)
        prefix.append({
            "D": D,
            "all_types_prefix": qstr(all_mass),
            "one_run_prefix": qstr(one_mass),
            "diagnostic_n_over_sqrtD_times_max_abs_float": scale * max(abs(float(all_mass)), abs(float(one_mass))),
        })

    return {
        "k": k,
        "n": n,
        "channel_masses": {str(j): qstr(massesA[j]) for j in range(3)},
        "conditional_channel_1_coefficients": map_json(conditional_deltas[1]),
        "conditional_channel_2_coefficients": map_json(conditional_deltas[2]),
        "fully_combined_coefficients": map_json(M),
        "channel_1_face_formula": face_stats,
        "abel_identity_exact": True,
        "critical_borel_chord_formula_exact": True,
        "channel_1_face_collapse_exact": True,
        "signed_summation_by_parts_exact": True,
        "small_charge_polynomial_1_E": [qstr(x) for x in charge],
        "prefix_diagnostics_finite_only": prefix,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    payload = {
        "mission": "M186",
        "status": "all exact k=3,5 coefficient assertions passed; no asymptotic inference",
        "method": "literal source rows versus separate critical-Borel chord/Abel reconstruction",
        "composition": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "parameters": {"k": [3, 5], "seed": None},
        "python": platform.python_version(),
        "standard_library_only": True,
        "results": [analyze(3), analyze(5)],
    }
    Path(args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": payload["status"], "output": args.output}, sort_keys=True))


if __name__ == "__main__":
    main()
