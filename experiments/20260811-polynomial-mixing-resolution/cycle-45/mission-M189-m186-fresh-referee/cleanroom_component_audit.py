#!/usr/bin/env python3
"""Clean-room exact referee for frozen M186, restricted to k=3,5.

This file imports no M186 code or data.  It constructs the two residual
factorization rows from the definitions, separately constructs component
prefix laws, and checks the identities assigned to M189 over Fraction.

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
Edge = tuple[int, int]
Profile = dict[tuple[int, int], Fraction]
Poly = tuple[Fraction, Fraction]


def mul(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inv(p: Perm) -> Perm:
    ans = [0] * len(p)
    for x, y in enumerate(p):
        ans[y] = x
    return tuple(ans)


def cycle(n: int, vertices: tuple[int, ...]) -> Perm:
    ans = list(range(n))
    for x, y in zip(vertices, vertices[1:] + vertices[:1]):
        ans[x] = y
    return tuple(ans)


def transposition(n: int, x: int, y: int) -> Perm:
    return cycle(n, (x, y))


def cycle_parts(p: Perm) -> list[tuple[int, ...]]:
    used: set[int] = set()
    out: list[tuple[int, ...]] = []
    for start in range(len(p)):
        if start in used:
            continue
        part: list[int] = []
        x = start
        while x not in used:
            used.add(x)
            part.append(x)
            x = p[x]
        out.append(tuple(part))
    return out


def trank(p: Perm) -> int:
    return len(p) - len(cycle_parts(p))


def tau(d: int) -> Fraction:
    assert d >= 1
    return Fraction(d ** (d - 1), math.factorial(d))


def completion_count(p: Perm, length: int) -> Fraction:
    if trank(p) != length:
        return Fraction()
    ans = Fraction(math.factorial(length))
    for part in cycle_parts(p):
        ans *= tau(len(part))
    return ans


def moved_edge(t: Perm) -> Edge:
    moved = [x for x in range(len(t)) if t[x] != x]
    assert len(moved) == 2
    return tuple(sorted(moved))  # type: ignore[return-value]


def internal_transpositions(p: Perm) -> list[Perm]:
    out: list[Perm] = []
    for part in cycle_parts(p):
        for x, y in combinations(part, 2):
            out.append(transposition(len(p), x, y))
    return out


def permutation_on_parts(n: int, parts: list[tuple[int, ...]]) -> Perm:
    ans = list(range(n))
    for part in parts:
        for x, y in zip(part, part[1:] + part[:1]):
            ans[x] = y
    return tuple(ans)


def source_data(k: int, side: str) -> tuple[Perm, Perm, Perm, list[tuple[int, ...]], tuple[int, ...]]:
    n = 3 * k
    h = cycle(n, tuple(range(n)))
    if side == "A":
        g = cycle(n, (0, k, 2 * k))
    else:
        g = mul(transposition(n, 0, 1), transposition(n, k, 2 * k))
    q = mul(inv(g), h)
    parts = cycle_parts(q)
    middle = next(part for part in parts if set(part) == set(range(k, 2 * k)))
    return h, g, q, parts, middle


def cyclic_runs(part: tuple[int, ...], n: int) -> tuple[int, ...]:
    support = set(part)
    starts = [x for x in support if (x - 1) % n not in support]
    assert starts
    lengths: list[int] = []
    for start in starts:
        length = 0
        while (start + length) % n in support:
            length += 1
        lengths.append(length)
    assert sum(lengths) == len(part)
    return tuple(sorted(lengths))


def component_profile(s: Perm, h: Perm) -> dict[tuple[int, int], int]:
    residual = mul(inv(s), h)
    out: defaultdict[tuple[int, int], int] = defaultdict(int)
    parts = cycle_parts(residual)
    assert len(parts) == 3
    for part in parts:
        runs = cyclic_runs(part, len(h))
        assert len(runs) in (1, 2)
        out[(len(runs), len(part))] += 1
    return dict(out)


def add_profile(dst: defaultdict[tuple[int, int], Fraction], src: dict[tuple[int, int], int], weight: Fraction) -> None:
    for key, multiplicity in src.items():
        dst[key] += weight * multiplicity


def profile_add(a: Profile, b: Profile) -> Profile:
    keys = set(a) | set(b)
    return {key: a.get(key, Fraction()) + b.get(key, Fraction()) for key in keys if a.get(key, Fraction()) + b.get(key, Fraction())}


def profile_sub(a: Profile, b: Profile) -> Profile:
    keys = set(a) | set(b)
    return {key: a.get(key, Fraction()) - b.get(key, Fraction()) for key in keys if a.get(key, Fraction()) - b.get(key, Fraction())}


def profile_scale(c: Fraction, a: Profile) -> Profile:
    return {key: c * value for key, value in a.items() if c * value}


def direct_row(k: int, side: str) -> dict[str, object]:
    h, _, q, parts, middle = source_data(k, side)
    owner = {x: index for index, part in enumerate(parts) for x in part}
    middle_index = parts.index(middle)
    rank = trank(q)
    denominator = completion_count(q, rank)
    row: defaultdict[Perm, Fraction] = defaultdict(Fraction)
    channel_rows = {j: defaultdict(Fraction) for j in range(3)}
    channel_profiles = {j: defaultdict(Fraction) for j in range(3)}
    channel_masses: defaultdict[int, Fraction] = defaultdict(Fraction)
    for e in internal_transpositions(q):
        x, _ = moved_edge(e)
        owner_e = owner[x]
        q1 = mul(e, q)
        for f in internal_transpositions(q1):
            u, _ = moved_edge(f)
            owner_f = owner[u]
            weight = completion_count(mul(f, q1), rank - 2) / denominator
            assert weight
            channel = int(owner_e != middle_index) + int(owner_f != middle_index)
            s = mul(e, f)
            row[s] += weight
            channel_rows[channel][s] += weight
            add_profile(channel_profiles[channel], component_profile(s, h), weight)
            channel_masses[channel] += weight
    assert sum(row.values(), Fraction()) == 1
    return {
        "row": dict(row),
        "channel_rows": {j: dict(channel_rows[j]) for j in range(3)},
        "channel_profiles": {j: dict(channel_profiles[j]) for j in range(3)},
        "masses": dict(channel_masses),
    }


def first_prefix_law(q: Perm, shape: str, k: int) -> dict[Perm, Fraction]:
    rank = trank(q)
    denominator = completion_count(q, rank)
    out: dict[Perm, Fraction] = {}
    for e in internal_transpositions(q):
        residual = mul(e, q)
        weight = completion_count(residual, rank - 1) / denominator
        sizes = [len(part) for part in cycle_parts(residual) if any(e[x] != x for x in part)]
        # Check the closed factorial-cancellation denominators directly.
        product_tau = Fraction(1)
        active = set(x for x in range(len(q)) if q[x] != x or e[x] != x)
        for part in cycle_parts(residual):
            if set(part) & active:
                product_tau *= tau(len(part))
        if shape == "L":
            closed = product_tau / ((2 * k - 2) * tau(2 * k - 1))
        elif shape == "F":
            closed = product_tau / ((2 * k - 2) * tau(k) ** 2)
        else:
            closed = product_tau / ((k - 1) * tau(k))
        assert weight == closed, (shape, moved_edge(e), sizes, weight, closed)
        out[e] = weight
    assert sum(out.values(), Fraction()) == 1
    return out


def pair_prefix_law(q: Perm, shape: str, k: int) -> dict[tuple[Perm, Perm], Fraction]:
    rank = trank(q)
    denominator = completion_count(q, rank)
    active = set(x for x in range(len(q)) if q[x] != x)
    out: dict[tuple[Perm, Perm], Fraction] = {}
    for e in internal_transpositions(q):
        q1 = mul(e, q)
        for f in internal_transpositions(q1):
            residual = mul(f, q1)
            weight = completion_count(residual, rank - 2) / denominator
            product_tau = Fraction(1)
            for part in cycle_parts(residual):
                if set(part) & active:
                    product_tau *= tau(len(part))
            if shape == "L":
                closed = product_tau / ((2 * k - 2) * (2 * k - 3) * tau(2 * k - 1))
            else:
                closed = product_tau / ((2 * k - 2) * (2 * k - 3) * tau(k) ** 2)
            assert weight == closed
            out[(e, f)] = weight
    assert sum(out.values(), Fraction()) == 1
    return out


def isolated_parts(k: int, side: str) -> tuple[Perm, Perm, list[tuple[int, ...]], tuple[int, ...]]:
    h, _, _, parts, middle = source_data(k, side)
    exterior = [part for part in parts if part != middle and len(part) > 1]
    return permutation_on_parts(3 * k, exterior), permutation_on_parts(3 * k, [middle]), exterior, middle


def smaller_split(e: Perm, original: list[tuple[int, ...]]) -> int:
    x, y = moved_edge(e)
    part = next(part for part in original if x in part)
    assert y in part
    positions = {z: i for i, z in enumerate(part)}
    gap = (positions[y] - positions[x]) % len(part)
    return min(gap, len(part) - gap)


def conditional_formula(k: int, side: str, channel: int) -> tuple[Profile, dict[int, Profile], dict[int, Fraction]]:
    assert channel in (1, 2)
    h, _, _, _, _ = source_data(k, side)
    exterior_q, middle_q, exterior_parts, _ = isolated_parts(k, side)
    shape = "L" if side == "B" else "F"
    first_ext = first_prefix_law(exterior_q, shape, k)
    raw_profiles: dict[int, defaultdict[tuple[int, int], Fraction]] = defaultdict(lambda: defaultdict(Fraction))
    split_mass: defaultdict[int, Fraction] = defaultdict(Fraction)
    total: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
    if channel == 1:
        first_mid = first_prefix_law(middle_q, "M", k)
        events = ((e, f, pe * pf) for e, pe in first_ext.items() for f, pf in first_mid.items())
    else:
        pairs = pair_prefix_law(exterior_q, shape, k)
        events = ((e, f, weight) for (e, f), weight in pairs.items())
    for e, f, weight in events:
        split = smaller_split(e, exterior_parts)
        profile = component_profile(mul(e, f), h)
        add_profile(total, profile, weight)
        add_profile(raw_profiles[split], profile, weight)
        split_mass[split] += weight
    normalized = {
        split: {key: value / split_mass[split] for key, value in profile.items()}
        for split, profile in raw_profiles.items()
    }
    assert sum(split_mass.values(), Fraction()) == 1
    return dict(total), normalized, dict(split_mass)


def abel(phi: dict[int, Profile], psi: dict[int, Profile], p: dict[int, Fraction], q: dict[int, Fraction], k: int) -> Profile:
    cumulative: dict[int, Fraction] = {}
    running = Fraction()
    for split in range(1, k):
        running += p.get(split, Fraction()) - q.get(split, Fraction())
        cumulative[split] = running
    assert cumulative[k - 1] == 0
    out: Profile = {}
    for split in range(1, k - 1):
        out = profile_add(out, profile_scale(cumulative[split], profile_sub(phi[split], phi[split + 1])))
    for split, mass in q.items():
        out = profile_add(out, profile_scale(mass, profile_sub(phi[split], psi[split])))
    return out


def chord_probability(d: int, a: int) -> Fraction:
    if not 1 <= a < d:
        return Fraction()
    return Fraction(math.factorial(d - 2)) * tau(a) * tau(d - a) / d ** (d - 2)


def face_laws(k: int) -> tuple[dict[int, Fraction], dict[int, Fraction]]:
    rho_a = {a: Fraction(k - a) * chord_probability(k, a) for a in range(1, k)}
    d = 2 * k - 1
    rho_b: dict[int, Fraction] = {}
    for a in range(1, d + 1):
        same = max(k - 1 - a, 0) + max(k - a, 0)
        cross = a - 1 if 2 <= a <= k else (2 * k - a if k < a <= 2 * k - 1 else 0)
        value = same * chord_probability(d, a) + cross * chord_probability(d, a - 1)
        if value:
            rho_b[a] = value
    assert sum(rho_a.values(), Fraction()) == sum(rho_b.values(), Fraction()) == 1
    for c in range(1, k):
        assert rho_b[2 * k - c] == c * chord_probability(2 * k - 1, c)
    return rho_a, rho_b


def expected_face_delta(k: int) -> tuple[Profile, Fraction, Fraction]:
    n = 3 * k
    rho_a, rho_b = face_laws(k)
    delta = {a: rho_b.get(a, Fraction()) - rho_a.get(a, Fraction()) for a in set(rho_a) | set(rho_b)}
    out: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
    for a, signed in delta.items():
        out[(1, a)] += signed
        for b, probability in rho_a.items():
            out[(2, n - a - b)] += signed * probability
    weighted_one = sum((abs(value) / a for a, value in delta.items()), Fraction())
    weighted_two = sum(
        (abs(value) * probability / (n - a - b) for a, value in delta.items() for b, probability in rho_a.items()),
        Fraction(),
    )
    return dict(out), weighted_one, weighted_two


def product_lifts(n: int) -> dict[Perm, list[tuple[Perm, Perm]]]:
    edges = [transposition(n, x, y) for x, y in combinations(range(n), 2)]
    out: defaultdict[Perm, list[tuple[Perm, Perm]]] = defaultdict(list)
    for a in edges:
        for b in edges:
            s = mul(a, b)
            if trank(s) == 2:
                out[s].append((a, b))
    return dict(out)


def is_triangle(s: Perm) -> bool:
    return sorted(len(part) for part in cycle_parts(s) if len(part) > 1) == [3]


def boundary_incidence(s: Perm, lifts: dict[Perm, list[tuple[Perm, Perm]]]) -> Fraction:
    n = len(s)
    boundary = {tuple(sorted((x, (x + 1) % n))) for x in range(n)}
    pairs = lifts[s]
    expected_lifts = 3 if is_triangle(s) else 2
    assert len(pairs) == expected_lifts
    total = sum(int(moved_edge(a) in boundary) + int(moved_edge(b) in boundary) for a, b in pairs)
    return Fraction(total, len(pairs))


def U1(d: int) -> Fraction:
    return Fraction() if d == 1 else Fraction(d - 1) * tau(d - 1) / tau(d)


def U2(d: int) -> Fraction:
    assert d >= 2
    return Fraction(d - 2) * tau(d - 1) / tau(d)


def p_add(a: Poly, b: Poly) -> Poly:
    return a[0] + b[0], a[1] + b[1]


def p_scale(c: Fraction, a: Poly) -> Poly:
    return c * a[0], c * a[1]


def u1_poly(d: int) -> Poly:
    return -Fraction(d) - Fraction(1, 2), U1(d)


def u2_poly(d: int) -> Poly:
    return -Fraction(d) + Fraction(1, 2), U2(d)


def direct_charge(M: Profile, cutoff: int) -> Poly:
    out = (Fraction(), Fraction())
    for (run_type, d), mass in M.items():
        if d <= cutoff:
            out = p_add(out, p_scale(mass, u1_poly(d) if run_type == 1 else u2_poly(d)))
    return out


def summation_by_parts(M: Profile, cutoff: int) -> Poly:
    singleton = M.get((1, 1), Fraction())
    out = p_scale(singleton, u1_poly(1))
    if cutoff < 2:
        return out
    A: dict[int, Fraction] = {}
    C: dict[int, Fraction] = {}
    a_running = c_running = Fraction()
    for d in range(2, cutoff + 1):
        c_running += M.get((1, d), Fraction())
        a_running += M.get((1, d), Fraction()) + M.get((2, d), Fraction())
        A[d], C[d] = a_running, c_running
    r = {d: p_add(u1_poly(d), p_scale(-1, u2_poly(d))) for d in range(2, cutoff + 1)}
    out = p_add(out, p_scale(A[cutoff], u2_poly(cutoff)))
    out = p_add(out, p_scale(C[cutoff], r[cutoff]))
    for d in range(2, cutoff):
        out = p_add(out, p_scale(A[d], p_add(u2_poly(d), p_scale(-1, u2_poly(d + 1)))))
        out = p_add(out, p_scale(C[d], p_add(r[d], p_scale(-1, r[d + 1]))))
    return out


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def analyze(k: int) -> dict[str, object]:
    n = 3 * k
    source_a = direct_row(k, "A")
    source_b = direct_row(k, "B")
    masses_a = source_a["masses"]
    masses_b = source_b["masses"]
    assert isinstance(masses_a, dict) and isinstance(masses_b, dict) and masses_a == masses_b
    m = k - 1
    expected_alpha = {
        0: Fraction(m * (m - 1), 3 * m * (3 * m - 1)),
        1: Fraction(4 * m * m, 3 * m * (3 * m - 1)),
        2: Fraction(2 * m * (2 * m - 1), 3 * m * (3 * m - 1)),
    }
    assert masses_a == expected_alpha

    channel_delta: dict[int, Profile] = {}
    formula_delta: dict[int, Profile] = {}
    for channel in (1, 2):
        direct_a = profile_scale(1 / expected_alpha[channel], source_a["channel_profiles"][channel])  # type: ignore[index]
        direct_b = profile_scale(1 / expected_alpha[channel], source_b["channel_profiles"][channel])  # type: ignore[index]
        channel_delta[channel] = profile_sub(direct_b, direct_a)
        total_a, psi, q = conditional_formula(k, "A", channel)
        total_b, phi, p = conditional_formula(k, "B", channel)
        formula_delta[channel] = profile_sub(total_b, total_a)
        assert formula_delta[channel] == channel_delta[channel]
        assert abel(phi, psi, p, q, k) == channel_delta[channel]

    combined = profile_add(
        profile_scale(expected_alpha[1], channel_delta[1]),
        profile_scale(expected_alpha[2], channel_delta[2]),
    )
    direct_combined = profile_sub(
        profile_add(source_b["channel_profiles"][1], source_b["channel_profiles"][2]),  # type: ignore[index]
        profile_add(source_a["channel_profiles"][1], source_a["channel_profiles"][2]),  # type: ignore[index]
    )
    assert combined == direct_combined

    face_delta, weighted_one, weighted_two = expected_face_delta(k)
    assert face_delta == channel_delta[1]

    row_a = source_a["row"]
    row_b = source_b["row"]
    assert isinstance(row_a, dict) and isinstance(row_b, dict)
    lifts = product_lifts(n)
    all_states = set(row_a) | set(row_b)
    W = {s: boundary_incidence(s, lifts) for s in all_states}
    h, _, _, _, _ = source_data(k, "A")
    for s in all_states:
        singleton = component_profile(s, h).get((1, 1), 0)
        expected = W[s] + (W[s] / 2 if is_triangle(s) else 0)
        assert singleton == expected

    def signed_expectation(observable: dict[Perm, Fraction]) -> Fraction:
        return sum((row_b.get(s, Fraction()) - row_a.get(s, Fraction())) * observable[s] for s in all_states)

    eta_w = signed_expectation(W)
    eta_wt = signed_expectation({s: W[s] if is_triangle(s) else Fraction() for s in all_states})
    singleton_coefficient = combined.get((1, 1), Fraction())
    assert singleton_coefficient == eta_w + eta_wt / 2
    expected_eta_w = Fraction(2, n - 3) * (U2(2 * k - 1) - 2 * U1(k))
    assert eta_w == expected_eta_w

    triangle_probabilities: dict[str, str] = {}
    for side, source in (("A", source_a), ("B", source_b)):
        for channel in range(3):
            probability = sum(weight for s, weight in source["channel_rows"][channel].items() if is_triangle(s)) / expected_alpha[channel]  # type: ignore[index]
            triangle_probabilities[f"{side}{channel}"] = qstr(probability)
            if channel == 0:
                assert probability == Fraction(3, k)
            elif channel == 1:
                assert probability == 0
            elif side == "B":
                assert probability == Fraction(3, 2 * k - 1)
            else:
                assert probability == Fraction(k - 2, 2 * k - 3) * Fraction(3, k)

    cutoff = n // 2
    direct_poly = direct_charge(combined, cutoff)
    sbp_poly = summation_by_parts(combined, cutoff)
    assert direct_poly == sbp_poly

    return {
        "k": k,
        "n": n,
        "source_accessible_states": len(all_states),
        "channel_masses": {str(j): qstr(expected_alpha[j]) for j in range(3)},
        "lambda_and_Lambda_closed_normalizations_exact": True,
        "combined_CB_signs_exact": True,
        "component_Abel_identity_exact": True,
        "J1_face_law_and_tail_exact": True,
        "k_times_J1_weighted_sum_float": float(k * (weighted_one + weighted_two)),
        "singleton_pointwise_and_signed_identity_exact": True,
        "eta_W": qstr(eta_w),
        "triangle_probabilities_by_side_channel": triangle_probabilities,
        "signed_SBP_polynomial_exact": True,
        "small_charge_polynomial_1_E": [qstr(value) for value in direct_poly],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    payload = {
        "mission": "M189",
        "status": "all clean-room exact k=3,5 referee assertions passed; no PCR or asymptotic inference",
        "method": "self-contained literal completion rows and separately derived component-prefix laws",
        "composition": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "parameters": {"k": [3, 5], "seed": None},
        "python": platform.python_version(),
        "standard_library_only": True,
        "imports_M186": False,
        "results": [analyze(3), analyze(5)],
    }
    Path(args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": payload["status"], "output": args.output}, sort_keys=True))


if __name__ == "__main__":
    main()
