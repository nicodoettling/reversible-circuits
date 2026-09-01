#!/usr/bin/env python3
"""Finite clean-room guards for the M276 append-only salvage.

The proof is analytic.  This script imports no project/predecessor module and
reads no M276/M272 data.  Predeclared exact channel cases are k=3,5,9;
predeclared tail-calibration cases are k=3,5,9,31,101.
"""

from __future__ import annotations

import hashlib
import json
import math
import platform
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "cleanroom_salvage_results.json"
CHANNEL_CASES = (3, 5, 9)
TAIL_CASES = (3, 5, 9, 31, 101)


def tau(d: int) -> Fraction:
    if d == 1:
        return Fraction(1)
    if d < 1:
        return Fraction(0)
    return Fraction(d ** (d - 2), math.factorial(d - 1))


def nu(d: int, s: int) -> Fraction:
    if not 1 <= s <= d - 1:
        return Fraction(0)
    return tau(s) * tau(d - s) / ((d - 1) * tau(d))


def split_laws(k: int) -> tuple[dict[int, Fraction], dict[int, Fraction]]:
    h = (k - 1) // 2
    p = {s: (2 * k - 1) * nu(2 * k - 1, s) for s in range(1, k)}
    q = {s: (k * nu(k, s) if s <= h else Fraction(0)) for s in range(1, k)}
    assert sum(p.values()) == 1
    assert sum(q.values()) == 1
    return p, q


def rho_laws(k: int) -> tuple[dict[int, Fraction], dict[int, Fraction]]:
    rho_a: dict[int, Fraction] = {}
    rho_b: dict[int, Fraction] = {}
    for a in range(0, 2 * k + 1):
        rho_a[a] = (k - a) * nu(k, a) if 1 <= a < k else Fraction(0)
        s_count = max(k - 1 - a, 0) + max(k - a, 0)
        if 2 <= a <= k:
            c_count = a - 1
        elif k < a <= 2 * k - 1:
            c_count = 2 * k - a
        else:
            c_count = 0
        rho_b[a] = s_count * nu(2 * k - 1, a) + c_count * nu(2 * k - 1, a - 1)
    assert sum(rho_a.values()) == 1
    assert sum(rho_b.values()) == 1
    return rho_a, rho_b


def total_variation(seq: dict[int, Fraction], lo: int, hi: int) -> Fraction:
    return sum(abs(seq[a + 1] - seq[a]) for a in range(lo, hi))


def quantile_joint(q: dict[int, Fraction], p: dict[int, Fraction]) -> dict[tuple[int, int], Fraction]:
    q_intervals: dict[int, tuple[Fraction, Fraction]] = {}
    p_intervals: dict[int, tuple[Fraction, Fraction]] = {}
    left = Fraction(0)
    for s, mass in sorted(q.items()):
        q_intervals[s] = (left, left + mass)
        left += mass
    assert left == 1
    left = Fraction(0)
    for t, mass in sorted(p.items()):
        p_intervals[t] = (left, left + mass)
        left += mass
    assert left == 1
    joint: dict[tuple[int, int], Fraction] = {}
    for s, (ql, qr) in q_intervals.items():
        for t, (pl, pr) in p_intervals.items():
            overlap = min(qr, pr) - max(ql, pl)
            if overlap > 0:
                joint[s, t] = overlap
    return joint


def gamma_l(k: int, s: int) -> Fraction:
    return Fraction(2, 2 * k - 3) * (
        2 - Fraction(1, s) - Fraction(1, 2 * k - 1 - s)
    )


def gamma_f(k: int, s: int) -> Fraction:
    return Fraction(2, 2 * k - 3) * (
        2 - Fraction(1, s) - Fraction(1, k - s)
    )


def vector_abel_guard(k: int, p: dict[int, Fraction], q: dict[int, Fraction]) -> dict:
    p_hat = {s: p[s] * (1 - gamma_l(k, s)) for s in p}
    q_hat = {
        s: q[s] * (1 - gamma_f(k, s)) if q[s] else Fraction(0)
        for s in q
    }
    cumulative: dict[int, Fraction] = {}
    running = Fraction(0)
    for s in range(1, k):
        running += p_hat[s] - q_hat[s]
        cumulative[s] = running
    expected_endpoint = Fraction(-6 * (k - 1), k * (2 * k - 1) * (2 * k - 3))
    assert cumulative[k - 1] == expected_endpoint

    # Two synthetic coordinates ensure the identity is vector-valued rather
    # than an accidental scalar cancellation.
    phi = {
        s: (Fraction(s * s + 1, k + 2), Fraction(3 * s + 2, 2 * k + 1))
        for s in range(1, k)
    }
    psi = {
        s: (Fraction(2 * s + 3, k + 3), Fraction(s * s + s + 1, 3 * k + 2))
        for s in range(1, k)
    }
    direct = [
        sum(p_hat[s] * phi[s][j] - q_hat[s] * psi[s][j] for s in range(1, k))
        for j in range(2)
    ]
    rhs: list[Fraction] = []
    for j in range(2):
        value = cumulative[k - 1] * phi[k - 1][j]
        value += sum(
            cumulative[u] * (phi[u][j] - phi[u + 1][j])
            for u in range(1, k - 1)
        )
        value += sum(
            q_hat[s] * (phi[s][j] - psi[s][j])
            for s in range(1, (k - 1) // 2 + 1)
        )
        rhs.append(value)
    assert direct == rhs
    return {
        "endpoint": str(cumulative[k - 1]),
        "expected_endpoint": str(expected_endpoint),
        "direct_vector": [str(x) for x in direct],
        "abel_vector": [str(x) for x in rhs],
    }


def phase_guard(k: int) -> dict:
    n = 3 * k
    owner: list[int | None] = [None if x % 5 == 0 else (x * x + 2 * x) % 3 for x in range(n)]
    kap = (
        (Fraction(1, 3), Fraction(1, 5), Fraction(1, 7)),
        (Fraction(1, 5), Fraction(2, 7), Fraction(1, 4)),
        (Fraction(1, 7), Fraction(1, 4), Fraction(3, 8)),
    )

    def kappa(a: int | None, b: int | None) -> Fraction:
        if a is None or b is None:
            return Fraction(0)
        return kap[a][b]

    ell = min(2, n - 3)
    charges: list[Fraction] = []
    profile: dict[tuple[int | None, int | None, int | None], int] = defaultdict(int)
    for x in range(n):
        triple = (owner[(x - ell) % n], owner[x], owner[(x + 1) % n])
        profile[triple] += 1
        charges.append(kappa(triple[0], triple[2]) - kappa(triple[0], triple[1]))
    e_ell = sum(charges)
    paired = sum(
        Fraction(count, n) * (kappa(key[0], key[2]) - kappa(key[0], key[1]))
        for key, count in profile.items()
    )
    assert paired == e_ell / n
    return {"n": n, "ell": ell, "E": str(e_ell), "profile_pairing": str(paired)}


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[x]] for x in range(len(p)))


def transposition(n: int, a: int, b: int) -> tuple[int, ...]:
    out = list(range(n))
    out[a], out[b] = out[b], out[a]
    return tuple(out)


def cycle_permutation(cycles: list[list[int]], n: int) -> tuple[int, ...]:
    out = list(range(n))
    for cyc in cycles:
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            out[a] = b
    return tuple(out)


def cycle_sizes(p: tuple[int, ...]) -> list[int]:
    seen: set[int] = set()
    sizes: list[int] = []
    for x in range(len(p)):
        if x in seen:
            continue
        y, size = x, 0
        while y not in seen:
            seen.add(y)
            size += 1
            y = p[y]
        sizes.append(size)
    return sizes


def factor_count(p: tuple[int, ...]) -> Fraction:
    sizes = cycle_sizes(p)
    rank = sum(d - 1 for d in sizes)
    ans = Fraction(math.factorial(rank))
    for d in sizes:
        ans *= tau(d)
    return ans


def raw_law_guard(cycles: list[list[int]], n: int) -> dict:
    qperm = cycle_permutation(cycles, n)
    rank = sum(d - 1 for d in cycle_sizes(qperm))
    denom = factor_count(qperm)
    edges = [transposition(n, a, b) for a in range(n) for b in range(a + 1, n)]
    nu_e: dict[int, Fraction] = {}
    ordered_mass = Fraction(0)
    for idx, e in enumerate(edges):
        rem = compose(e, qperm)
        mass = factor_count(rem) / denom if sum(d - 1 for d in cycle_sizes(rem)) == rank - 1 else Fraction(0)
        nu_e[idx] = mass
        conditional_sum = Fraction(0)
        for f in edges:
            rem2 = compose(f, rem)
            if sum(d - 1 for d in cycle_sizes(rem2)) == rank - 2:
                conditional_sum += factor_count(rem2) / denom
        assert conditional_sum == mass
        ordered_mass += conditional_sum
    assert sum(nu_e.values()) == 1
    assert ordered_mass == 1
    return {"cycles": cycles, "rank": rank, "first_mass": "1", "ordered_mass": "1"}


def channel_case(k: int) -> dict:
    p, q = split_laws(k)
    d = {u: sum(p[s] - q[s] for s in range(1, u + 1)) for u in range(1, k)}
    assert all(d[u] < 0 for u in range(1, k - 1))
    assert d[k - 1] == 0
    joint = quantile_joint(q, p)
    assert all(s <= t for (s, t), mass in joint.items() if mass)
    for u in range(1, k - 1):
        crossing = sum(mass for (s, t), mass in joint.items() if s <= u < t)
        assert crossing == -d[u]

    shared_l = sum(p[s] * gamma_l(k, s) for s in range(1, k))
    shared_f = sum(q[s] * gamma_f(k, s) for s in range(1, (k - 1) // 2 + 1))
    assert shared_l == Fraction(3, 2 * k - 1)
    assert shared_f == Fraction(3 * (k - 2), k * (2 * k - 3))
    return {
        "k": k,
        "p_mass": "1",
        "q_mass": "1",
        "quantile_order": True,
        "crossing_matches_minus_D": True,
        "shared_L": str(shared_l),
        "shared_F": str(shared_f),
        "abel": vector_abel_guard(k, p, q),
        "phase": phase_guard(k),
    }


def tail_case(k: int) -> dict:
    rho_a, rho_b = rho_laws(k)
    delta = {a: rho_b[a] - rho_a[a] for a in rho_a}
    h = (k - 1) // 2
    endpoint = rho_a[k - 1]
    endpoint_formula = Fraction((k - 1) ** (k - 3), k ** (k - 2))
    assert endpoint == endpoint_formula
    g = {0: Fraction(0)}
    for c in range(1, h + 1):
        g[c] = c * nu(k, c)
        assert g[c] == rho_a[k - c]
    g_tv = total_variation(g, 0, h)
    full_tv = total_variation(delta, 0, 2 * k)
    # At the long-cycle bulk/far-tail junction the values agree exactly.
    assert rho_b[k] == rho_b[k + 1]
    return {
        "k": k,
        "rho_A_k_minus_1": str(endpoint),
        "k_times_endpoint": float(k * endpoint),
        "k_3_over_2_times_endpoint": float((k ** 1.5) * endpoint),
        "g_tail_variation": str(g_tv),
        "k_times_g_tail_variation": float(k * g_tv),
        "delta_rho_variation": str(full_tv),
        "k_times_delta_rho_variation": float(k * full_tv),
        "bulk_far_junction_exact": True,
    }


def main() -> None:
    raw = [
        raw_law_guard([[0, 1, 2, 3, 4, 5, 6]], 7),
        raw_law_guard([[0, 1, 2], [3, 4, 5, 6]], 7),
    ]
    result = {
        "mission": "M279 clean-room M276-salvage guard",
        "status": "finite calibration only; universal proof is analytic",
        "predecessor_imports": False,
        "predecessor_reads": False,
        "raw_law_cases": raw,
        "channel_cases": [channel_case(k) for k in CHANNEL_CASES],
        "tail_cases": [tail_case(k) for k in TAIL_CASES],
        "holds": True,
        "environment": {
            "python": platform.python_version(),
            "nonstandard_dependencies": {},
            "seed": None,
        },
    }
    normalized = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["normalized_digest"] = hashlib.sha256(normalized.encode()).hexdigest()
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
