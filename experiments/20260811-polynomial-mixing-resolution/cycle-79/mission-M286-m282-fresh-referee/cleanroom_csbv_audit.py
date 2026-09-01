#!/usr/bin/env python3
"""Clean-room exact audit for M282's CSBV formulas.

This checker imports no project or predecessor code.  At k=3,5 it builds
the ordered first-two-factor completion laws directly from permutation
cycle counts, then compares their disjoint support-pair and ambient-lag
profiles with an independently coded coefficient formula.  A separate
formula-only scan checks boundary cases of the proposed stabilization
decomposition.  The scan is falsification evidence, not an asymptotic proof.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import subprocess
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return pq with (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def transposition(n: int, a: int, b: int) -> tuple[int, ...]:
    out = list(range(n))
    out[a], out[b] = out[b], out[a]
    return tuple(out)


def cycle_perm(n: int, vertices: list[int]) -> tuple[int, ...]:
    out = list(range(n))
    for a, b in zip(vertices, vertices[1:] + vertices[:1]):
        out[a] = b
    return tuple(out)


def cycle_sizes(p: tuple[int, ...]) -> list[int]:
    seen = [False] * len(p)
    sizes = []
    for x in range(len(p)):
        if seen[x]:
            continue
        y, size = x, 0
        while not seen[y]:
            seen[y] = True
            size += 1
            y = p[y]
        sizes.append(size)
    return sizes


def borel_weight(r: int) -> Fraction:
    # e^{-r} cancels from every ratio used here.
    return Fraction(r ** (r - 1), math.factorial(r))


def completion_count(p: tuple[int, ...], remaining: int) -> Fraction:
    sizes = cycle_sizes(p)
    rank = len(p) - len(sizes)
    if rank != remaining:
        return Fraction()
    out = Fraction(math.factorial(remaining))
    for r in sizes:
        out *= borel_weight(r)
    return out


def all_transpositions(n: int) -> list[tuple[tuple[int, ...], tuple[int, int]]]:
    return [
        (transposition(n, a, b), (a, b))
        for a in range(n)
        for b in range(a + 1, n)
    ]


def pair_law(g: tuple[int, ...]) -> list[tuple[tuple[int, int], tuple[int, int], Fraction]]:
    n = len(g)
    rank = n - len(cycle_sizes(g))
    total = completion_count(g, rank)
    atoms = []
    for e, ep in all_transpositions(n):
        for f, fp in all_transpositions(n):
            residual = compose(inverse(compose(e, f)), g)
            weight = completion_count(residual, rank - 2) / total
            if weight:
                atoms.append((ep, fp, weight))
    assert sum((w for _, _, w in atoms), Fraction()) == 1
    return atoms


def split_on_cycle(edge: tuple[int, int], cycle: list[int]) -> int | None:
    pos = {v: i for i, v in enumerate(cycle)}
    a, b = edge
    if a not in pos or b not in pos:
        return None
    d = (pos[b] - pos[a]) % len(cycle)
    return min(d, len(cycle) - d)


def classify_split(edge: tuple[int, int], cycles: list[list[int]]) -> int | None:
    values = [split_on_cycle(edge, cyc) for cyc in cycles]
    values = [s for s in values if s is not None]
    assert len(values) <= 1
    return values[0] if values else None


def h(r: int, R: int) -> Fraction:
    return Fraction((r - 1) * (r - 2), r * R)


def kernel(r: int, x: int, R: int) -> Fraction:
    if not 1 <= x < r:
        return Fraction()
    return borel_weight(x) * borel_weight(r - x) / (R * borel_weight(r))


def u_row(r: int, x: int, R: int) -> Fraction:
    if not 1 <= x < r:
        return Fraction()
    second_edge = (r - x - 1) * kernel(r, x, R) if x <= r - 2 else Fraction()
    cross_pairs = Fraction(4 * (r - 1), r * R) - 2 * kernel(r, x, R)
    return second_edge + cross_pairs


def total_variation(values: list[Fraction]) -> Fraction:
    return sum((abs(b - a) for a, b in zip(values, values[1:])), Fraction())


def l1(values: list[Fraction]) -> Fraction:
    return sum((abs(x) for x in values), Fraction())


def qtext(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def direct_reconstruction(k: int) -> dict[str, object]:
    D, R, n = 2 * k - 1, 2 * k - 3, 3 * k
    embedding = list(range(1, k)) + list(range(2 * k, 3 * k))
    assert len(embedding) == D
    abstract_pos = {v: i for i, v in enumerate(embedding)}

    long_cycle = cycle_perm(n, embedding)
    long_atoms = pair_law(long_cycle)

    # Work on a compact 2k-point support for the two-cycle source.  Only its
    # split and disjoint masses enter the CSBV coefficient A_s.
    two_cycles = [list(range(k)), list(range(k, 2 * k))]
    two_cycle_perm = compose(
        cycle_perm(2 * k, two_cycles[0]), cycle_perm(2 * k, two_cycles[1])
    )
    short_atoms = pair_law(two_cycle_perm)

    p = {s: Fraction() for s in range(1, k)}
    phat = {s: Fraction() for s in range(1, k)}
    q = {s: Fraction() for s in range(1, k)}
    qhat = {s: Fraction() for s in range(1, k)}
    long_disjoint_atoms: dict[int, list[tuple[tuple[int, int], tuple[int, int], Fraction]]] = {
        s: [] for s in range(1, k)
    }

    for e, f, weight in long_atoms:
        s = classify_split(e, [embedding])
        assert s is not None
        p[s] += weight
        if set(e).isdisjoint(f):
            phat[s] += weight
            long_disjoint_atoms[s].append((e, f, weight))

    for e, f, weight in short_atoms:
        s = classify_split(e, two_cycles)
        assert s is not None
        q[s] += weight
        if set(e).isdisjoint(f):
            qhat[s] += weight

    assert sum(p.values(), Fraction()) == 1
    assert sum(q.values(), Fraction()) == 1

    A: dict[int, Fraction] = {}
    W: dict[int, Fraction] = {}
    for s in range(1, k):
        p_formula = Fraction(D, D - 1) * (
            borel_weight(s) * borel_weight(D - s) / borel_weight(D)
        )
        q_formula = (
            Fraction(k, k - 1)
            * borel_weight(s)
            * borel_weight(k - s)
            / borel_weight(k)
            if 2 * s < k
            else Fraction()
        )
        a_l = h(s, R) + h(D - s, R)
        a_f = h(s, R) + h(k - s, R) + Fraction(k - 1, R) if 2 * s < k else Fraction()
        assert p[s] == p_formula
        assert q[s] == q_formula
        assert phat[s] == p_formula * a_l
        assert qhat[s] == q_formula * a_f
        A[s] = phat[s] - qhat[s]
        W[s] = A[s] / a_l

    endpoint = -Fraction(6 * (k - 1), k * D * R)
    assert sum(A.values(), Fraction()) == endpoint

    # Direct signed support-pair profiles and conditional Phi_s profiles.
    c_direct = [Fraction() for _ in range(D)]
    J_direct = [Fraction() for _ in range(n)]
    phi = {s: [Fraction() for _ in range(n)] for s in range(1, k)}
    for s in range(1, k):
        assert phat[s] > 0
        for e, f, weight in long_disjoint_atoms[s]:
            conditional = weight / phat[s]
            signed_weight = A[s] * conditional
            support = sorted(set(e) | set(f))
            assert len(support) == 4
            for x in support:
                for y in support:
                    if x == y:
                        continue
                    d = (abstract_pos[y] - abstract_pos[x]) % D
                    ell = (y - x) % n
                    c_direct[d] += signed_weight
                    J_direct[ell] += signed_weight
                    phi[s][ell] += conditional
        assert sum(phi[s], Fraction()) == 12

    c_formula = [Fraction() for _ in range(D)]
    for d in range(1, D):
        c_formula[d] = A[min(d, D - d)] + sum(
            (
                W[min(r, D - r)]
                * (u_row(r, d, R) + u_row(r, D - d, R))
                for r in range(1, D)
            ),
            Fraction(),
        )
    assert c_direct == c_formula
    assert all(c_formula[d] == c_formula[D - d] for d in range(1, D))

    half = [Fraction()] + c_formula[1:k] + [Fraction()]
    J_formula = [Fraction() for _ in range(n)]
    for ell in range(1, k + 1):
        J_formula[ell] = (
            (D - 2 * ell) * half[ell] + (ell - 1) * half[ell - 1]
        ) / D
    for ell in range(k + 1, 2 * k):
        J_formula[ell] = (
            (ell - k) * c_formula[ell - k]
            + (2 * k - ell) * c_formula[2 * k - ell]
        ) / D
    for ell in range(1, n):
        if J_formula[ell]:
            mirror = n - ell
            if J_formula[mirror]:
                assert J_formula[mirror] == J_formula[ell]
            else:
                J_formula[mirror] = J_formula[ell]
    assert J_direct == J_formula

    derivatives = {
        s: [phi[s][ell + 1] - phi[s][ell] for ell in range(2, n - 2)]
        for s in range(1, k)
    }
    E = {}
    running = Fraction()
    for s in range(1, k):
        running += A[s]
        E[s] = running
    abel = [E[k - 1] * x for x in derivatives[k - 1]]
    for u in range(1, k - 1):
        abel = [
            old + E[u] * (x - y)
            for old, x, y in zip(abel, derivatives[u], derivatives[u + 1])
        ]
    direct = [
        sum((A[s] * derivatives[s][i] for s in range(1, k)), Fraction())
        for i in range(n - 4)
    ]
    embedded = [J_formula[ell + 1] - J_formula[ell] for ell in range(2, n - 2)]
    assert abel == direct == embedded

    return {
        "k": k,
        "long_ordered_atoms": len(long_atoms),
        "two_cycle_ordered_atoms": len(short_atoms),
        "disjoint_long_atoms": sum(len(v) for v in long_disjoint_atoms.values()),
        "endpoint": qtext(endpoint),
        "sum_W": qtext(sum(W.values(), Fraction())),
        "c_half_tv": qtext(total_variation(half)),
        "csbv_l1": qtext(l1(embedded)),
        "assertions": "all passed",
    }


def formula_scan(k: int) -> dict[str, object]:
    D, R = 2 * k - 1, 2 * k - 3
    p, q, A, W = {}, {}, {}, {}
    for s in range(1, k):
        p[s] = Fraction(D, D - 1) * (
            borel_weight(s) * borel_weight(D - s) / borel_weight(D)
        )
        q[s] = (
            Fraction(k, k - 1)
            * borel_weight(s)
            * borel_weight(k - s)
            / borel_weight(k)
            if 2 * s < k
            else Fraction()
        )
        a_l = h(s, R) + h(D - s, R)
        a_f = h(s, R) + h(k - s, R) + Fraction(k - 1, R) if q[s] else Fraction()
        A[s] = p[s] * a_l - q[s] * a_f
        W[s] = A[s] / a_l

    # The reference profile contains the genuine Borel mass e^{-d}tau(d),
    # although all K-ratios above are rational because their exponentials
    # cancel.  Use high-precision Decimal only for this finite boundary scan.
    getcontext().prec = 80

    def genuine_borel(d: int) -> Decimal:
        t = borel_weight(d)
        return (-Decimal(d)).exp() * Decimal(t.numerator) / Decimal(t.denominator)

    stabilization = []
    for r in range(1, D):
        row = [Decimal(0)]
        for d in range(1, k):
            zq = u_row(r, d, R) + u_row(r, D - d, R)
            z = Decimal(zq.numerator) / Decimal(zq.denominator)
            reference = Decimal(r) / Decimal(R) * genuine_borel(d) + Decimal(4) / Decimal(R)
            row.append(z - reference)
        row.append(Decimal(0))
        stabilization.append((sum(abs(b - a) for a, b in zip(row, row[1:])), r))
    max_tv, argmax = max(stabilization)

    a_half = [Fraction()] + [A[s] for s in range(1, k)] + [Fraction()]
    delta_weight = -sum(W.values(), Fraction())
    assert delta_weight >= 0
    assert delta_weight <= Fraction(16, 3 * k * k)
    return {
        "k": k,
        "R_times_max_stabilization_tv": float(R * max_tv),
        "stabilization_argmax_r": argmax,
        "r1_scaled_tv": float(R * stabilization[0][0]),
        "r2_scaled_tv": float(R * stabilization[1][0]),
        "k_times_A_tv": float(k * total_variation(a_half)),
        "k2_abs_sum_W": float(k * k * abs(sum(W.values(), Fraction()))),
        "assertions": "all passed",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    payload = {
        "status": (
            "exact rational completion-law reconstruction plus high-precision "
            "finite boundary scan; no asymptotic inference"
        ),
        "target": "M282 Abel/support-pair/seam conventions and stabilization boundaries",
        "convention": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "direct_reconstruction": [direct_reconstruction(k) for k in (3, 5)],
        "formula_scan": [formula_scan(k) for k in (3, 5, 9, 17, 33, 65)],
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "deterministic": True,
        "seed": None,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(encoded, end="")
    print("normalized_sha256", hashlib.sha256(encoded.encode()).hexdigest())


if __name__ == "__main__":
    main()
