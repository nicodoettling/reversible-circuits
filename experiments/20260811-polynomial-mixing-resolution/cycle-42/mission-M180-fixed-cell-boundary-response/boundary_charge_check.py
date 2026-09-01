#!/usr/bin/env python3
"""Exact k=3,5 calibration for the M180 boundary-charge reduction.

The two source laws are reconstructed from literal ordered transpositions in
uniform minimal factorizations.  All channel/kind contributions are combined
before evaluating the component charge.  The affine identities are checked
as polynomials in a formal variable E (later E=e).

Convention: (pq)(x)=p(q(x)); factors multiply left-to-right.
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import platform
import subprocess
import time
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path


Perm = tuple[int, ...]
Poly = tuple[Fraction, Fraction, Fraction]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    ans = [0] * len(p)
    for x, y in enumerate(p):
        ans[y] = x
    return tuple(ans)


def cycle_perm(n: int, entries: tuple[int, ...]) -> Perm:
    ans = list(range(n))
    for x, y in zip(entries, entries[1:] + entries[:1]):
        ans[x] = y
    return tuple(ans)


def transposition(n: int, x: int, y: int) -> Perm:
    return cycle_perm(n, (x, y))


def cycles(p: Perm) -> list[tuple[int, ...]]:
    seen: set[int] = set()
    ans = []
    for start in range(len(p)):
        if start in seen:
            continue
        c = []
        x = start
        while x not in seen:
            seen.add(x)
            c.append(x)
            x = p[x]
        ans.append(tuple(c))
    return ans


@lru_cache(maxsize=None)
def completion_sizes(sizes: tuple[int, ...], length: int) -> int:
    if not sizes or any(d <= 0 for d in sizes):
        return 0
    if sum(sizes) - len(sizes) != length:
        return 0
    ans = Fraction(math.factorial(length))
    for d in sizes:
        if d > 1:
            ans *= Fraction(d ** (d - 2), math.factorial(d - 1))
    if ans.denominator != 1:
        raise AssertionError(ans)
    return ans.numerator


def completion(p: Perm, length: int) -> int:
    return completion_sizes(tuple(sorted(map(len, cycles(p)))), length)


def tau(d: int) -> Fraction:
    if d < 1:
        raise ValueError(d)
    return Fraction(d ** (d - 1), math.factorial(d))


def internal_edges(n: int, component: tuple[int, ...]):
    for x, y in combinations(sorted(component), 2):
        yield transposition(n, x, y)


def ambient_runs(component: tuple[int, ...], n: int) -> tuple[int, ...]:
    support = set(component)
    starts = sorted(x for x in support if (x - 1) % n not in support)
    if not starts:
        return (n,)
    ans = []
    for start in starts:
        size = 1
        while (start + size) % n in support:
            size += 1
        ans.append(size)
    if sum(ans) != len(component):
        raise AssertionError((component, ans))
    return tuple(sorted(ans))


def qstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def padd(x: Poly, y: Poly) -> Poly:
    return tuple(a + b for a, b in zip(x, y))  # type: ignore[return-value]


def pscale(c: Fraction | int, x: Poly) -> Poly:
    return tuple(Fraction(c) * a for a in x)  # type: ignore[return-value]


def psub(x: Poly, y: Poly) -> Poly:
    return padd(x, pscale(-1, y))


def pmul(x: Poly, y: Poly) -> Poly:
    raw = [Fraction(0)] * 5
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            raw[i + j] += a * b
    if raw[3] or raw[4]:
        raise AssertionError(raw)
    return tuple(raw[:3])  # type: ignore[return-value]


def peval(x: Poly) -> float:
    return float(x[0]) + math.e * float(x[1]) + math.e**2 * float(x[2])


def component_data(n: int, s: Perm):
    h = cycle_perm(n, tuple(range(n)))
    q = compose(inverse(s), h)
    data = []
    for c in cycles(q):
        d = len(c)
        runs = ambient_runs(c, n)
        if len(runs) == 1:
            typ, eps, linear_c = 1, Fraction(1, 2), 2
            generic = d - 1
            adjacent = max(d - 2, 0)
            indicator = 0
        elif len(runs) == 2:
            typ, eps, linear_c = 2, Fraction(-1, 2), 4
            generic = d - 2
            adjacent = sum(max(a - 2, 0) for a in runs)
            indicator = sum(a == 1 for a in runs)
        else:
            raise AssertionError((d, runs))
        ordered = generic * (generic - 1) - 2 * adjacent
        U = Fraction(0) if generic == 0 else generic * tau(d - 1) / tau(d)
        V = Fraction(0) if ordered == 0 else ordered * tau(d - 2) / tau(d)
        u: Poly = (Fraction(-d) - eps, U, Fraction(0))
        v: Poly = (Fraction(-d * d + linear_c * d), Fraction(0), V)
        data.append(
            {
                "size": d,
                "type": typ,
                "runs": runs,
                "indicator": indicator,
                "eps": eps,
                "c": linear_c,
                "U": U,
                "V": V,
                "u": u,
                "v": v,
            }
        )
    if len(data) != 3:
        raise AssertionError(data)
    return data


def boundary_poly(n: int, kind: str, data) -> Poly:
    L = 0 if kind == "T" else -2
    B: Poly = (Fraction(-sum(x["c"] * x["size"] for x in data) - L * n), Fraction(0), Fraction(0))
    for x in data:
        B = padd(B, x["v"])
    for i in range(3):
        for j in range(i + 1, 3):
            xi, xj = data[i], data[j]
            wi = padd((xi["eps"], Fraction(0), Fraction(0)), xi["u"])
            wj = padd((xj["eps"], Fraction(0), Fraction(0)), xj["u"])
            term = padd(pscale(xi["size"], wj), pscale(xj["size"], wi))
            term = padd(term, pmul(wi, wj))
            B = padd(B, pscale(2, term))
    return B


def charge_poly(data) -> Poly:
    return tuple(sum((x["u"][i] for x in data), Fraction(0)) for i in range(3))  # type: ignore[return-value]


def bounded_remainder_poly(n: int, kind: str, data, B: Poly, Q: Poly) -> Poly:
    indicator = sum(x["indicator"] for x in data if x["type"] == 2)
    base = Fraction(-7, 2) - 2 * indicator if kind == "D" else Fraction(-7, 2)
    return psub(psub(B, pscale(2 * n, Q)), (base, Fraction(0), Fraction(0)))


def source_law(k: int, label: str):
    n = 3 * k
    h = cycle_perm(n, tuple(range(n)))
    source = (
        cycle_perm(n, (0, k, 2 * k))
        if label == "A"
        else compose(transposition(n, 0, 1), transposition(n, k, 2 * k))
    )
    residual = compose(inverse(source), h)
    original = cycles(residual)
    middle = next(i for i, c in enumerate(original) if k in c)
    owner = {x: i for i, c in enumerate(original) for x in c}
    denominator = completion(residual, n - 3)
    law: collections.defaultdict[tuple[Perm, int, str], Fraction] = collections.defaultdict(Fraction)
    for i, c in enumerate(original):
        for first in internal_edges(n, c):
            after = compose(first, residual)
            for c2 in cycles(after):
                if len(c2) == 1:
                    continue
                old = owner[c2[0]]
                if any(owner[x] != old for x in c2):
                    raise AssertionError(c2)
                for second in internal_edges(n, c2):
                    remainder = compose(second, after)
                    numerator = completion(remainder, n - 5)
                    if not numerator:
                        continue
                    s = compose(first, second)
                    support = sum(s[x] != x for x in range(n))
                    kind = "T" if support == 3 else "D"
                    if support not in (3, 4):
                        raise AssertionError(support)
                    j = int(i != middle) + int(old != middle)
                    law[(s, j, kind)] += Fraction(numerator, denominator)
    if sum(law.values(), Fraction(0)) != 1:
        raise AssertionError(sum(law.values(), Fraction(0)))
    return dict(law)


def analyze(k: int) -> dict[str, object]:
    started = time.monotonic()
    n = 3 * k
    laws = {label: source_law(k, label) for label in ("A", "B")}
    states = sorted({key[0] for law in laws.values() for key in law})
    state_data = {}
    max_remainder = 0.0
    for s in states:
        data = component_data(n, s)
        kind = "T" if sum(s[x] != x for x in range(n)) == 3 else "D"
        B = boundary_poly(n, kind, data)
        Q = charge_poly(data)
        R = bounded_remainder_poly(n, kind, data, B, Q)
        max_remainder = max(max_remainder, abs(peval(R)))
        state_data[s] = (kind, data, B, Q, R)

    signed: collections.defaultdict[Perm, Fraction] = collections.defaultdict(Fraction)
    channel_signed: dict[int, collections.defaultdict[Perm, Fraction]] = {
        j: collections.defaultdict(Fraction) for j in range(3)
    }
    for label, sign in (("B", 1), ("A", -1)):
        for (s, j, _), p in laws[label].items():
            signed[s] += sign * p
            channel_signed[j][s] += sign * p

    eta_t = sum(p for s, p in signed.items() if state_data[s][0] == "T")
    eta_t_closed = Fraction(12 * (k - 1), 3 * k * (3 * k - 4) * (2 * k - 1))
    if eta_t != eta_t_closed:
        raise AssertionError((eta_t, eta_t_closed))

    component_measure: collections.defaultdict[tuple[int, int], Fraction] = collections.defaultdict(Fraction)
    for s, p in signed.items():
        for x in state_data[s][1]:
            component_measure[(x["type"], x["size"])] += p
    if sum(component_measure.values(), Fraction(0)) != 0:
        raise AssertionError("total component count did not cancel")
    if sum(d * p for (_, d), p in component_measure.items()) != 0:
        raise AssertionError("component size did not cancel")
    if sum(p for (typ, _), p in component_measure.items() if typ == 1) != eta_t:
        raise AssertionError("one-run count transfer")
    if sum(p for (typ, _), p in component_measure.items() if typ == 2) != -eta_t:
        raise AssertionError("two-run count transfer")

    def integrate(poly_index: int, which):
        return sum((p * state_data[s][which][poly_index] for s, p in signed.items()), Fraction(0))

    eta_B: Poly = tuple(integrate(i, 2) for i in range(3))  # type: ignore[assignment]
    eta_Q: Poly = tuple(integrate(i, 3) for i in range(3))  # type: ignore[assignment]
    eta_R: Poly = tuple(integrate(i, 4) for i in range(3))  # type: ignore[assignment]
    eta_indicator = sum(
        p * sum(x["indicator"] for x in state_data[s][1] if x["type"] == 2)
        for s, p in signed.items()
    )
    reconstructed = padd(pscale(2 * n, eta_Q), eta_R)
    reconstructed = padd(reconstructed, (-2 * eta_indicator, Fraction(0), Fraction(0)))
    if eta_B != reconstructed:
        raise AssertionError((eta_B, reconstructed))
    # Q=e*H-n-sum eps, hence eta(Q)=e*eta(H)-eta(T).
    eta_H = sum(
        p * sum((x["U"] for x in state_data[s][1]), Fraction(0))
        for s, p in signed.items()
    )
    if eta_Q != (-eta_t, eta_H, Fraction(0)):
        raise AssertionError((eta_Q, eta_t, eta_H))

    channel_charge = {}
    for j in (1, 2):
        qj: Poly = tuple(
            sum((p * state_data[s][3][i] for s, p in channel_signed[j].items()), Fraction(0))
            for i in range(3)
        )  # type: ignore[assignment]
        channel_charge[str(j)] = [qstr(x) for x in qj]

    projected_by_size = []
    projected_l1 = 0.0
    projected_small_signed = 0.0
    projected_tail_signed = 0.0
    projected_tail_l1 = 0.0
    for d in sorted({size for _, size in component_measure}):
        m1 = component_measure.get((1, d), Fraction(0))
        m2 = component_measure.get((2, d), Fraction(0))
        u1 = (
            Fraction(-d) - Fraction(1, 2),
            (d - 1) * tau(d - 1) / tau(d) if d >= 2 else Fraction(0),
            Fraction(0),
        )
        u2 = (
            Fraction(-d) + Fraction(1, 2),
            (d - 2) * tau(d - 1) / tau(d) if d >= 2 else Fraction(0),
            Fraction(0),
        )
        coefficient = padd(pscale(m1, u1), pscale(m2, u2))
        value = peval(coefficient)
        projected_l1 += abs(value)
        if 2 * d <= n:
            projected_small_signed += value
        else:
            projected_tail_signed += value
            projected_tail_l1 += abs(value)
        projected_by_size.append(
            {
                "size": d,
                "combined_type_coefficient_E0_E1_E2": [qstr(x) for x in coefficient],
                "combined_type_coefficient_float": value,
            }
        )

    return {
        "k": k,
        "n": n,
        "distinct_intermediates": len(states),
        "eta_triangle_exact": qstr(eta_t),
        "eta_H_exact": qstr(eta_H),
        "n_times_eta_H_float": n * float(eta_H),
        "eta_Q_coefficients_E0_E1_E2": [qstr(x) for x in eta_Q],
        "n_times_eta_Q_float": n * peval(eta_Q),
        "eta_B_coefficients_E0_E1_E2": [qstr(x) for x in eta_B],
        "eta_B_float": peval(eta_B),
        "eta_bounded_remainder_coefficients": [qstr(x) for x in eta_R],
        "eta_small_run_indicator_exact": qstr(eta_indicator),
        "max_abs_bounded_remainder_on_accessible_states_float": max_remainder,
        "channel_charge_coefficients_before_combination": channel_charge,
        "component_measure": [
            {"type": typ, "size": d, "signed_mass_exact": qstr(p)}
            for (typ, d), p in sorted(component_measure.items())
            if p
        ],
        "projected_component_charge_by_size": projected_by_size,
        "projected_component_charge_l1_float": projected_l1,
        "n_times_projected_component_charge_l1_float": n * projected_l1,
        "n_times_small_component_signed_charge_float": n * projected_small_signed,
        "n_times_large_component_signed_charge_float": n * projected_tail_signed,
        "n_times_large_component_charge_l1_float": n * projected_tail_l1,
        "BIR_delta_W_exact": qstr(Fraction(2, n - 3) * eta_H),
        "n_squared_BIR_delta_W_float": n * n * float(Fraction(2, n - 3) * eta_H),
        "component_count_and_size_moments_cancel_exact": True,
        "one_two_run_count_transfer_is_plus_minus_eta_T": True,
        "boundary_decomposition_formal_exact": True,
        "runtime_seconds": time.monotonic() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--frozen-m174", type=Path)
    args = parser.parse_args()
    rows = [analyze(k) for k in (3, 5)]
    frozen_matches = []
    if args.frozen_m174:
        frozen = json.loads(args.frozen_m174.read_text())
        by_k = {row["k"]: row for row in frozen["results"]}
        for row in rows:
            observed = row["eta_B_float"]
            expected = by_k[row["k"]]["boundary_response_coefficient_float"]
            if not math.isclose(observed, expected, rel_tol=2e-15, abs_tol=2e-15):
                raise AssertionError((row["k"], observed, expected))
            frozen_matches.append({"k": row["k"], "eta_B_match": True})
    payload = {
        "status": "exact finite calibration only; no asymptotic inference",
        "target": "M180 channel-combined boundary-charge reduction",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": "boundary_charge_check.py --output boundary_charge_results.json --frozen-m174 <pcs_channel_exact.json>",
        "frozen_M174_checks": frozen_matches,
        "results": rows,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(rows, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
