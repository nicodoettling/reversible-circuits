#!/usr/bin/env python3
"""One clean-room exact falsifier for M289's fixed CEBV formulas.

At k=3,5 this script constructs the ordered first-two-factor laws directly
from minimal-completion counts and compares every raw B/A support-pair
coefficient with the closed kernel/phase formula.  It then scans the fixed
formula at a few larger ranks.  It imports no project or predecessor code and
makes no asymptotic inference.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


Perm = tuple[int, ...]
Edge = tuple[int, int]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def transposition(n: int, a: int, b: int) -> Perm:
    out = list(range(n))
    out[a], out[b] = out[b], out[a]
    return tuple(out)


def cycle_perm(n: int, vertices: list[int]) -> Perm:
    out = list(range(n))
    for a, b in zip(vertices, vertices[1:] + vertices[:1]):
        out[a] = b
    return tuple(out)


def cycle_sizes(p: Perm) -> list[int]:
    seen = [False] * len(p)
    out = []
    for start in range(len(p)):
        if seen[start]:
            continue
        x, size = start, 0
        while not seen[x]:
            seen[x] = True
            size += 1
            x = p[x]
        out.append(size)
    return out


def tau(r: int) -> Fraction:
    # This equals e^r b_r; exponentials cancel in all ratios below.
    return Fraction(r ** (r - 1), math.factorial(r))


def completion_count(p: Perm, remaining: int) -> Fraction:
    sizes = cycle_sizes(p)
    if len(p) - len(sizes) != remaining:
        return Fraction()
    out = Fraction(math.factorial(remaining))
    for r in sizes:
        out *= tau(r)
    return out


def all_edges(n: int) -> list[tuple[Perm, Edge]]:
    return [
        (transposition(n, a, b), (a, b))
        for a in range(n)
        for b in range(a + 1, n)
    ]


def pair_law(g: Perm) -> list[tuple[Edge, Edge, Fraction]]:
    rank = len(g) - len(cycle_sizes(g))
    denominator = completion_count(g, rank)
    edges = all_edges(len(g))
    out = []
    for e, ep in edges:
        for f, fp in edges:
            residual = compose(inverse(compose(e, f)), g)
            weight = completion_count(residual, rank - 2) / denominator
            if weight:
                out.append((ep, fp, weight))
    assert sum((w for _, _, w in out), Fraction()) == 1
    return out


def split_size(edge: Edge, source_cycles: list[list[int]]) -> int:
    a, b = edge
    for cyc in source_cycles:
        if a in cyc:
            assert b in cyc
            ia, ib = cyc.index(a), cyc.index(b)
            d = (ib - ia) % len(cyc)
            return min(d, len(cyc) - d)
    raise AssertionError("edge outside source cycles")


def collision_profile(n: int, e: Edge, f: Edge) -> list[Fraction]:
    support = sorted(set(e) | set(f))
    assert len(support) == 4
    out = [Fraction() for _ in range(n)]
    for x in support:
        for y in support:
            if x != y:
                out[(y - x) % n] += 1
    assert sum(out, Fraction()) == 12
    return out


def add(out: list[Fraction], row: list[Fraction], scale: Fraction = Fraction(1)) -> None:
    for i, value in enumerate(row):
        out[i] += scale * value


def scaled(row: list[Fraction], scale: Fraction) -> list[Fraction]:
    return [scale * x for x in row]


def difference(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    return [a - b for a, b in zip(left, right)]


def l1(row: list[Fraction]) -> Fraction:
    return sum((abs(x) for x in row), Fraction())


def circular_tv(row: list[Fraction]) -> Fraction:
    return sum(
        (abs(row[(i + 1) % len(row)] - row[i]) for i in range(len(row))),
        Fraction(),
    )


def qtext(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def h(r: int, R: int) -> Fraction:
    return Fraction((r - 1) * (r - 2), r * R)


def kernel(R: int, r: int, d: int) -> Fraction:
    if not 1 <= d < r:
        return Fraction()
    return tau(d) * tau(r - d) / (R * tau(r))


def u_row(R: int, r: int, d: int) -> Fraction:
    if not 1 <= d < r:
        return Fraction()
    second = (r - d - 1) * kernel(R, r, d) if d <= r - 2 else Fraction()
    cross = Fraction(4 * (r - 1), r * R) - 2 * kernel(R, r, d)
    return second + cross


def embed(coeff: list[Fraction], word: list[int], n: int) -> list[Fraction]:
    m = len(word)
    assert len(coeff) == m
    out = [Fraction() for _ in range(n)]
    for d in range(1, m):
        if not coeff[d]:
            continue
        for i in range(m):
            ell = (word[(i + d) % m] - word[i]) % n
            out[ell] += coeff[d] / m
    return out


def parameters(k: int) -> tuple[int, int, int, int]:
    if k < 3 or k % 2 == 0:
        raise ValueError("k must be odd and at least 3")
    return 3 * k, 2 * k - 1, 2 * k - 3, (k - 1) // 2


def split_weights(k: int, s: int) -> tuple[Fraction, Fraction, Fraction]:
    _, D, R, _ = parameters(k)
    q = Fraction(k, k - 1) * tau(s) * tau(k - s) / tau(k)
    a_l = h(s, R) + h(D - s, R)
    a_f = h(s, R) + h(k - s, R) + Fraction(k - 1, R)
    return q, a_l, a_f


def cross_profile(k: int) -> list[Fraction]:
    n, _, R, _ = parameters(k)
    lower = range(0, k)
    upper = range(2 * k, 3 * k)
    u = Fraction(k - 1, R)
    atom = Fraction(4, k * k) * u
    out = [Fraction() for _ in range(n)]
    for x in lower:
        for y in upper:
            out[(y - x) % n] += atom
            out[(x - y) % n] += atom
    assert sum(out, Fraction()) == 8 * u
    return out


def raw_formula(k: int, side: str, s: int) -> dict[str, list[Fraction] | Fraction]:
    n, D, R, _ = parameters(k)
    if side == "B":
        _, a_l, _ = split_weights(k, s)
        coeff_first = [Fraction() for _ in range(D)]
        coeff_other = [Fraction() for _ in range(D)]
        for d in range(1, D):
            if min(d, D - d) == s:
                coeff_first[d] = a_l
            for r in (s, D - s):
                coeff_other[d] += u_row(R, r, d) + u_row(R, r, D - d)
        first = embed(coeff_first, list(range(1, k)) + list(range(2 * k, 3 * k)), n)
        other = embed(coeff_other, list(range(1, k)) + list(range(2 * k, 3 * k)), n)
        total = [a + b for a, b in zip(first, other)]
        assert sum(total, Fraction()) == 12 * a_l
        return {"first": first, "other": other, "cross": [Fraction() for _ in range(n)], "total": total, "mass": a_l}

    q, _, a_f = split_weights(k, s)
    del q
    coeff_first = [Fraction() for _ in range(k)]
    coeff_other = [Fraction() for _ in range(k)]
    for d in range(1, k):
        if min(d, k - d) == s:
            coeff_first[d] = a_f
        for r in (s, k - s):
            coeff_other[d] += u_row(R, r, d) + u_row(R, r, k - d)
        coeff_other[d] += k * kernel(R, k, d)
    first = embed(coeff_first, list(range(k)), n)
    other = embed(coeff_other, list(range(k)), n)
    cross = cross_profile(k)
    total = [a + b + c for a, b, c in zip(first, other, cross)]
    assert sum(total, Fraction()) == 12 * a_f
    return {"first": first, "other": other, "cross": cross, "total": total, "mass": a_f}


def formula_analysis(k: int) -> tuple[dict[str, object], list[Fraction]]:
    n, _, _, j = parameters(k)
    H0 = [Fraction() for _ in range(n)]
    HN = [Fraction() for _ in range(n)]
    Hfirst = [Fraction() for _ in range(n)]
    Hother = [Fraction() for _ in range(n)]
    Hcross = [Fraction() for _ in range(n)]
    qsum = Fraction()
    for s in range(1, j + 1):
        q, a_l, a_f = split_weights(k, s)
        qsum += q
        B = raw_formula(k, "B", s)
        A = raw_formula(k, "A", s)
        add(H0, difference(B["total"], A["total"]), q)  # type: ignore[arg-type]
        delta = a_f / a_l - 1
        add(HN, B["total"], q * delta)  # type: ignore[arg-type]
        add(Hfirst, difference(B["first"], A["first"]), q)  # type: ignore[arg-type]
        add(Hother, difference(B["other"], A["other"]), q)  # type: ignore[arg-type]
        add(Hcross, A["cross"], -q)  # type: ignore[arg-type]
    assert qsum == 1
    H = [a + b for a, b in zip(H0, HN)]
    assert H0 == [a + b + c for a, b, c in zip(Hfirst, Hother, Hcross)]
    derivative = [H[ell + 1] - H[ell] for ell in range(2, n - 2)]
    return {
        "k": k,
        "cebv_l1_exact": qtext(l1(derivative)),
        "cebv_l1_float": float(l1(derivative)),
        "k_times_cebv_l1_float": float(k * l1(derivative)),
        "k_times_full_profile_tv_float": float(k * circular_tv(H)),
        "k_times_H0_tv_float": float(k * circular_tv(H0)),
        "k2_times_normalizer_tv_float": float(k * k * circular_tv(HN)),
        "k_times_first_tv_float": float(k * circular_tv(Hfirst)),
        "k_times_other_tv_float": float(k * circular_tv(Hother)),
        "k_times_cross_tv_float": float(k * circular_tv(Hcross)),
    }, H


def enumerated_profiles(k: int, side: str) -> tuple[dict[int, Fraction], dict[int, Fraction], dict[int, list[Fraction]], int]:
    n, _, _, _ = parameters(k)
    if side == "B":
        cycles = [list(range(1, k)) + list(range(2 * k, 3 * k))]
        source = cycle_perm(n, cycles[0])
    else:
        cycles = [list(range(k)), list(range(2 * k, 3 * k))]
        source = compose(cycle_perm(n, cycles[0]), cycle_perm(n, cycles[1]))
    split_mass: defaultdict[int, Fraction] = defaultdict(Fraction)
    disjoint_mass: defaultdict[int, Fraction] = defaultdict(Fraction)
    raw: dict[int, list[Fraction]] = defaultdict(lambda: [Fraction() for _ in range(n)])
    atom_count = 0
    for e, f, weight in pair_law(source):
        s = split_size(e, cycles)
        split_mass[s] += weight
        if set(e).isdisjoint(f):
            disjoint_mass[s] += weight
            add(raw[s], collision_profile(n, e, f), weight)
            atom_count += 1
    return dict(split_mass), dict(disjoint_mass), dict(raw), atom_count


def direct_check(k: int) -> dict[str, object]:
    n, _, _, j = parameters(k)
    bsplit, bmass, braw, batoms = enumerated_profiles(k, "B")
    asplit, amass, araw, aatoms = enumerated_profiles(k, "A")
    H = [Fraction() for _ in range(n)]
    assertions = 0
    for s in range(1, j + 1):
        q, a_l, a_f = split_weights(k, s)
        assert asplit[s] == q
        assert bmass[s] == bsplit[s] * a_l
        assert amass[s] == q * a_f
        B = raw_formula(k, "B", s)
        A = raw_formula(k, "A", s)
        bconditional_raw = scaled(braw[s], Fraction(1, bsplit[s]))
        aconditional_raw = scaled(araw[s], Fraction(1, q))
        assert bconditional_raw == B["total"]
        assert aconditional_raw == A["total"]
        phi = scaled(braw[s], Fraction(1, bmass[s]))
        psi = scaled(araw[s], Fraction(1, amass[s]))
        add(H, difference(phi, psi), amass[s])
        assertions += 5
    formula_row, formula_H = formula_analysis(k)
    assert H == formula_H
    derivative = [H[ell + 1] - H[ell] for ell in range(2, n - 2)]
    assert qtext(l1(derivative)) == formula_row["cebv_l1_exact"]
    return {
        "k": k,
        "B_ordered_disjoint_atoms": batoms,
        "A_ordered_disjoint_atoms": aatoms,
        "formula_assertions": assertions + 2,
        "cebv_l1_exact": qtext(l1(derivative)),
        "assertions": "all passed",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    formula_rows = [formula_analysis(k)[0] for k in (3, 5, 7, 9, 15, 31)]
    payload = {
        "status": "exact finite formula/convention falsification only; no asymptotic inference",
        "target": "M289 raw B/A support-pair collapse and CEBV vector",
        "convention": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "formulas_fixed_before_computation": True,
        "direct_completion_checks": [direct_check(k) for k in (3, 5)],
        "formula_scan": formula_rows,
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
