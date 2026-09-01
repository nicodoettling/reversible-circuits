#!/usr/bin/env python3
"""Independent exact referee for frozen M131.

No predecessor experiment source is imported.  The mathematical payload is
constructed first from ordered compositions, Cayley forest weights, literal
canonical basins, and the attachment law.  An optional frozen JSON is read
only after the fresh payload and certificates have been computed.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import itertools
import json
import math
import platform
from fractions import Fraction as F
from pathlib import Path


def rec(x: F) -> dict[str, str | float]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator), "decimal": float(x)}


@functools.lru_cache(None)
def wt(n: int) -> F:
    assert n >= 1
    return F(n ** (n - 1), math.factorial(n))


@functools.lru_cache(None)
def comps(n: int) -> tuple[tuple[int, ...], ...]:
    if n == 0:
        return ((),)
    return tuple((a,) + tail for a in range(1, n + 1) for tail in comps(n - a))


@functools.lru_cache(None)
def forest(n: int, p: int) -> F:
    if (n, p) == (0, 0):
        return F(1)
    if not (1 <= p <= n):
        return F(0)
    return F(p * n ** (n - p), n * math.factorial(n - p))


def choose(n: int, k: int) -> int:
    return math.comb(n, k) if 0 <= k <= n else 0


def split(s: int, bottom: int) -> F:
    return wt(s + 1 - bottom) * wt(bottom) / wt(s + 1)


def rho_word(c: tuple[int, ...]) -> F:
    s = sum(c)
    return math.prod(wt(a) for a in c) / (math.factorial(len(c)) * wt(s + 1))


def h_value(k: int, last: int, K: int, R: int, bottom: int) -> F:
    if last < bottom:
        return F(0)
    if last == bottom:
        den = choose(k + K - 1, K - 1)
        return F(K * choose(k + K - R - 2, K - R - 1), den) if den else F(0)
    return split(last - 1, bottom) * (
        1 - F(choose(K, R + 1), choose(K + k, R + 1))
    )


def nu_direct(K: int, R: int, k: int, j: int) -> F:
    return F(
        choose(R + j, j) * choose(K - R - 1 + k - j, k - j),
        choose(K + k, k),
    )


@functools.lru_cache(None)
def macro_groups(s: int) -> tuple[tuple[int, int, F], ...]:
    ans = []
    total = F(0)
    for k in range(1, s + 1):
        for last in range(1, s + 1):
            mass = wt(last) * forest(s - last, k - 1) / (math.factorial(k) * wt(s + 1))
            if mass:
                ans.append((k, last, mass))
                total += mass
    assert total == 1
    return tuple(ans)


def basin_contains(source: tuple[int, ...], endpoint: tuple[int, ...]) -> bool:
    return any(
        sum(source[:cut]) == endpoint[0] and source[cut:] == endpoint[1:]
        for cut in range(1, len(source) + 1)
    )


@functools.lru_cache(None)
def active_basins(s: int) -> tuple[tuple[tuple[int, ...], tuple[tuple[int, ...], ...]], ...]:
    roots = comps(s)
    endpoints = {
        (sum(source[:cut]),) + source[cut:]
        for source in roots
        for cut in range(1, len(source))
        if sum(source[:cut]) + source[cut] - 1 >= 2
    }
    return tuple(
        (e, tuple(c for c in roots if basin_contains(c, e)))
        for e in sorted(endpoints, key=lambda x: (len(x), x))
    )


@functools.lru_cache(None)
def literal_reset(s: int, K: int, R: int, bottom: int) -> F:
    q = split(s, bottom)
    masses = {c: rho_word(c) for c in comps(s)}
    energy = F(0)
    for endpoint, sources in active_basins(s):
        current = sum(masses[c] * (h_value(len(c), c[-1], K, R, bottom) - q) for c in sources)
        capacity = len(endpoint) * masses[endpoint]
        energy += current * current / capacity
    return energy


@functools.lru_cache(None)
def child_rows(state: tuple[int, int, int, int]) -> tuple[tuple[F, tuple[int, int, int, int], int, int, int], ...]:
    s, K, R, bottom = state
    phase = s + K - R
    out = []
    for k, last, mass in macro_groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        assert sum((nu_direct(K, R, k, j) for j in range(k + 1)), F(0)) == 1
        for j in range(1, k + 1):
            nu = nu_direct(K, R, k, j)
            if not nu:
                continue
            child = (last - 1, K + k, R + j, bottom)
            assert child[0] + child[1] - child[2] < phase
            out.append((mass * nu, child, k, last, j))
    return tuple(out)


@functools.lru_cache(None)
def exact_H(state: tuple[int, int, int, int]) -> F:
    return literal_reset(*state) + sum(coef * exact_H(child) for coef, child, _, _, _ in child_rows(state))


def rise(a: int, n: int) -> int:
    return math.prod(range(a, a + n))


def nu_param(a: int, deficit: int, k: int, j: int, z: F) -> F:
    den = math.prod(1 + (a + r) * z for r in range(k))
    if j == 0:
        return F(rise(deficit, k)) * z**k / den
    return (
        F(math.comb(k, j) * rise(deficit, k - j))
        * z ** (k - j)
        * math.prod(1 + (a - deficit + r) * z for r in range(j))
        / den
    )


def prefix_endpoints(prefix: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple((sum(prefix[:cut]),) + prefix[cut:] for cut in range(1, len(prefix) + 1))


def q_from_ratios(ratios: tuple[F, ...]) -> F:
    ell = len(ratios) - 1
    return wt(ell + 1) * math.prod(ratios)


def supported_rows(ell: int, ratios: tuple[F, ...], z: F, a: int, deficit: int):
    assert len(ratios) == ell + 1
    q = q_from_ratios(ratios)
    rows = []
    for h in range(ell + 1):
        n = ell - h
        bottom_product = math.prod(ratios[-h:]) if h else F(1)
        child_q = wt(h) * bottom_product if h else None
        for prefix in comps(n):
            degree = len(prefix) + 1
            normalized_mass = math.prod(wt(c) for c in prefix) / (
                math.factorial(degree) * wt(ell + 1) * bottom_product
            )
            if h == 0:
                mean = degree * nu_param(a, deficit, degree - 1, 0, z)
            else:
                mean = child_q * (1 - nu_param(a, deficit, degree, 0, z))
            rows.append((h, prefix, normalized_mass, mean))
    assert len(rows) == 2**ell
    assert sum(m * f for _, _, m, f in rows) == 1
    return tuple(rows), q


def exceptional_data(ell: int, ratios: tuple[F, ...], z: F, a: int, deficit: int):
    rows, q = supported_rows(ell, ratios, z, a, deficit)
    keyed = {(h, p): (m, f) for h, p, m, f in rows}
    exceptions = sorted(
        {(h, e) for h, p, _, _ in rows for e in prefix_endpoints(p)},
        key=lambda item: (item[0], len(item[1]), item[1]),
    )
    data = []
    for h, endpoint in exceptions:
        sources = tuple((p, m, f) for hh, p, m, f in rows if hh == h and basin_contains(p, endpoint))
        theta = sum(m * (f - q) for _, m, f in sources)
        endpoint_mass = keyed[(h, endpoint)][0]
        capacity = (len(endpoint) + 1) * endpoint_mass
        data.append((h, endpoint, tuple(p for p, _, _ in sources), theta, capacity, sum(m for _, m, _ in sources)))
    return rows, q, tuple(data)


def coarse_reset_bound(ell: int, ratios: tuple[F, ...], z: F, a: int, deficit: int, height: F):
    rows, q, data = exceptional_data(ell, ratios, z, a, deficit)
    occurrence_mass = sum(m * len(p) for _, p, m, _ in rows)
    value = q * (height - q * occurrence_mass)
    value += sum(theta * theta / cap for _, _, _, theta, cap, _ in data)
    return value, data


def falling(a: int, p: int) -> int:
    return math.prod(range(a - p + 1, a + 1))


@functools.lru_cache(None)
def lam(first: int, degree: int) -> F:
    return math.factorial(degree - 1) * sum(
        F(p * falling(first, p), math.factorial(p + degree - 1) * first**p)
        for p in range(1, first + 1)
    )


@functools.lru_cache(None)
def coefficient_C(s: int) -> F:
    return sum(
        wt(first) * forest(s - first, degree - 1)
        / (math.factorial(degree) * wt(s + 1))
        * degree * lam(first, degree) ** 2
        for degree in range(2, s + 1)
        for first in range(1, s - degree + 2)
    )


def refined_reset_bound(ratios: tuple[F, ...], z: F, ordinary: F, subtraction_power: int = 1):
    assert subtraction_power in (1, 2)
    rows, q, data = exceptional_data(5, ratios, z, 0, 1)
    subtraction = sum(source_mass * lam(endpoint[0], len(endpoint) + 1) ** subtraction_power
                      for _, endpoint, _, _, _, source_mass in data)
    value = q * (ordinary - q * subtraction)
    value += sum(theta * theta / cap for _, _, _, theta, cap, _ in data)
    return value, data, subtraction


def group_mass(rows, h: int, degree: int) -> F:
    return sum(m for hh, p, m, _ in rows if hh == h and len(p) + 1 == degree)


def arbitrary_F(ell: int, ratios: tuple[F, ...], z: F, a: int, deficit: int, heights: dict[int, F]) -> F:
    q = q_from_ratios(ratios)
    if ell == 0:
        return 1 - q
    assert ell <= 3
    reset, _ = coarse_reset_bound(ell, ratios, z, a, deficit, heights[ell])
    rows, q2 = supported_rows(ell, ratios, z, a, deficit)
    assert q2 == q
    descendants = F(0)
    for h in range(1, ell + 1):
        for degree in range(1, ell - h + 2):
            mass = group_mass(rows, h, degree)
            if not mass:
                continue
            child_ratios = ratios[-h:]
            child_q = q_from_ratios(child_ratios)
            for j in range(1, degree + 1):
                nu = nu_param(a, deficit, degree, j, z)
                child_ell = h - 1
                child_D = deficit + degree - j
                child_a = a + degree
                child_bound = child_q * (
                    1 - child_q if child_ell == 0 else
                    arbitrary_F(child_ell, child_ratios, z, child_a, child_D, heights)
                )
                descendants += mass * nu * child_bound
    return reset + descendants


def direct_F1(split0: F, terminal: F, height: F, p: F) -> F:
    return split0 * (height - split0 / 2) + (2 * p - split0) ** 2 / 4 + (1 - p) * (1 - terminal)


def direct_F2(ratios: tuple[F, ...], h2: F, h1: F, p: F, killed: F, child_p: F) -> F:
    top, middle, terminal = ratios
    q = F(3, 2) * top * middle * terminal
    split1 = middle * terminal
    reset = (
        q * (h2 - 5 * q / 9 - q / (3 * terminal))
        + (3 * killed - q) ** 2 / 27
        + (3 * killed + 6 * p - 4 * q) ** 2 / 54
        + (terminal * (1 - killed) - q) ** 2 / (6 * terminal)
    )
    return reset + (1 - killed) * (1 - terminal) / 3 + F(2, 3) * (1 - p) * direct_F1(split1, terminal, h1, child_p)


def envelope_L5(
    ratios: tuple[F, ...], z: F, heights: dict[int, F], ordinary: F,
    subtraction_power: int = 1,
):
    rows, q = supported_rows(5, ratios, z, 0, 1)
    reset, basins, subtraction = refined_reset_bound(ratios, z, ordinary, subtraction_power)
    desc = F(0)
    live = []
    for h in range(1, 6):
        for degree in range(1, 7 - h):
            mass = group_mass(rows, h, degree)
            if not mass:
                continue
            rank_rows = []
            child_ratios = ratios[-h:]
            child_q = q_from_ratios(child_ratios)
            for j in range(1, degree + 1):
                nu = nu_param(0, 1, degree, j, z)
                child_D = degree + 1 - j
                child_ell = h - 1
                if child_D == 1:
                    bound = child_q * (1 - child_q)
                    source = "accepted-right-heavy-L<=4"
                else:
                    assert child_ell <= 3
                    bound = child_q * arbitrary_F(child_ell, child_ratios, z, degree, child_D, heights)
                    source = "arbitrary-deficit-L<=3"
                desc += mass * nu * bound
                rank_rows.append((j, nu, child_D, child_ell, source))
            live.append((h, degree, mass, tuple(rank_rows)))
    assert len(live) == 11
    return reset + desc, q, reset, desc, basins, tuple(live), subtraction


def actual_tuple(s: int, K: int):
    ratios = tuple(wt(s - i) / wt(s - i + 1) for i in range(6))
    z = F(1, K + 1)
    B = s - 5
    heights = {ell: F(B + ell - 1, B + ell + 1) for ell in range(1, 6)}
    return ratios, z, heights


def cleared(
    ratios: tuple[F, ...], z: F, heights: dict[int, F], ordinary: F,
    subtraction_power: int = 1,
) -> F:
    env, q, *_ = envelope_L5(ratios, z, heights, ordinary, subtraction_power)
    return math.prod(1 + a * z for a in range(1, 6)) ** 2 * (1 - q - env)


def invert(a: list[list[F]]) -> list[list[F]]:
    n = len(a)
    m = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(a)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if m[r][col])
        m[col], m[pivot] = m[pivot], m[col]
        scale = m[col][col]
        m[col] = [x / scale for x in m[col]]
        for r in range(n):
            if r == col or not m[r][col]:
                continue
            scale = m[r][col]
            m[r] = [x - scale * y for x, y in zip(m[r], m[col])]
    return [row[n:] for row in m]


@functools.lru_cache(None)
def bern_inverse(degree: int) -> tuple[tuple[F, ...], ...]:
    if degree == 0:
        return ((F(1),),)
    matrix = []
    for j in range(degree + 1):
        t = F(j, degree)
        matrix.append([
            F(math.comb(degree, i)) * t**i * (1 - t) ** (degree - i)
            for i in range(degree + 1)
        ])
    return tuple(tuple(row) for row in invert(matrix))


def transform_axis(values: dict[tuple[int, ...], F], degrees: tuple[int, ...], axis: int):
    inv = bern_inverse(degrees[axis])
    out: dict[tuple[int, ...], F] = {}
    other_axes = [range(d + 1) for i, d in enumerate(degrees) if i != axis]
    for other in itertools.product(*other_axes):
        def full_index(j: int):
            it = iter(other)
            return tuple(j if i == axis else next(it) for i in range(len(degrees)))
        samples = [values[full_index(j)] for j in range(degrees[axis] + 1)]
        for i in range(degrees[axis] + 1):
            out[full_index(i)] = sum(inv[i][j] * samples[j] for j in range(degrees[axis] + 1))
    return out


def tensor_coefficients(values: dict[tuple[int, ...], F], degrees: tuple[int, ...]):
    ans = values
    for axis in range(len(degrees)):
        ans = transform_axis(ans, degrees, axis)
    return ans


def bern_eval(coeffs: dict[tuple[int, ...], F], degrees: tuple[int, ...], point: tuple[F, ...]) -> F:
    ans = F(0)
    for idx, coef in coeffs.items():
        basis = F(1)
        for d, i, t in zip(degrees, idx, point):
            basis *= math.comb(d, i) * t**i * (1 - t) ** (d - i)
        ans += coef * basis
    return ans


def diff_degree(values: list[F]) -> int:
    row = values[:]
    for d in range(len(values) - 1):
        row = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        if all(x == 0 for x in row):
            return d
    return len(values) - 1


def parse_record(obj: dict[str, str | float]) -> F:
    return F(int(obj["numerator"]), int(obj["denominator"]))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--reference-json", type=Path)
    args = ap.parse_args()

    failures: list[dict[str, object]] = []

    # Root structure and literal reconstruction.
    structure = []
    literal_checks = []
    refined_mass_failures = 0
    for s in (6, 7):
        B = s - 5
        ratios, z, heights = actual_tuple(s, 1)
        rows, q, basins = exceptional_data(5, ratios, z, 0, 1)
        positive_groups = sorted({(h, len(p) + 1) for h, p, _, f in rows if f > 0})
        live_groups = sorted((h, k) for h, k in positive_groups if h >= 1)
        inactive = []
        for h, endpoint, *_ in basins:
            full = endpoint + (B + h,)
            if full[0] + full[1] - 1 < 2:
                inactive.append((h, endpoint))
        structure.append({
            "s": s, "support_count": len(rows), "mean_sum": rec(sum(m * f for _, _, m, f in rows)),
            "exception_count": len(basins), "inactive_exception_count": len(inactive),
            "positive_groups": [list(x) for x in positive_groups], "live_groups": [list(x) for x in live_groups],
            "all_rank_rows": [
                {"h": h, "k": k, "ranks": [
                    {"j": j, "nu": rec(nu_param(0, 1, k, j, z)), "deficit": k + 1 - j}
                    for j in range(1, k + 1)
                ]} for h, k in live_groups
            ],
        })
        if not (len(rows) == 32 and len(basins) == 31 and len(inactive) == 8 and len(positive_groups) == 16 and len(live_groups) == 11):
            failures.append({"kind": "root-structure", "s": s})
        for h, endpoint, _, _, capacity_over_q, source_mass_over_q in basins:
            full_endpoint = endpoint + (B + h,)
            full_sources = tuple(c for c in comps(s) if basin_contains(c, full_endpoint))
            full_mass = sum(rho_word(c) for c in full_sources)
            capacity = len(full_endpoint) * rho_word(full_endpoint)
            supported_mass = q * source_mass_over_q
            if not (
                supported_mass <= full_mass
                and full_mass / capacity == lam(endpoint[0], len(endpoint) + 1)
                and capacity / q == capacity_over_q
            ):
                refined_mass_failures += 1

        for K in (1, 5):
            zK = F(1, K + 1)
            rowsK, qK, basinK = exceptional_data(5, ratios, zK, 0, 1)
            full_map = {e: (src, theta / qK, cap / qK) for e, src, theta, cap in (
                (e, src, sum(rho_word(c) * (h_value(len(c), c[-1], K, K - 1, B) - qK) for c in src), len(e) * rho_word(e))
                for e, src in active_basins(s)
            )}
            matched = 0
            for h, ep, sources, theta, cap, _ in basinK:
                full = ep + (B + h,)
                if full[0] + full[1] - 1 < 2:
                    continue
                full_sources, th, cp = full_map[full]
                expected = tuple(p + (B + h,) for p in sources)
                if full_sources != expected or th != theta or cp != cap:
                    failures.append({"kind": "literal-basin-mismatch", "s": s, "K": K, "endpoint": list(full)})
                matched += 1
            grouped_energy = literal_reset(s, K, K - 1, B)
            direct_energy = sum(theta * theta / cap for _, _, theta, cap in (
                (e, src, sum(rho_word(c) * (h_value(len(c), c[-1], K, K - 1, B) - qK) for c in src), len(e) * rho_word(e))
                for e, src in active_basins(s)
            ))
            if grouped_energy != direct_energy:
                failures.append({"kind": "literal-reset-mismatch", "s": s, "K": K})
            literal_checks.append({"s": s, "K": K, "full_basin_count": len(active_basins(s)), "matched_active_exceptions": matched, "reset": rec(grouped_energy)})

    boundary = child_rows((6, 1, 0, 1))
    boundary_triples = [(k, t, j) for _, _, k, t, j in boundary]
    expected_boundary = (
        [(1, 6, 1)]
        + [(2, t, j) for t in (3, 4, 5) for j in (1, 2)]
        + [(3, t, j) for t in (3, 4) for j in (1, 2, 3)]
        + [(4, 3, j) for j in (1, 2, 3, 4)]
    )
    if sorted(boundary_triples) != sorted(expected_boundary):
        failures.append({"kind": "s6-boundary-children"})

    # Arbitrary-deficit envelopes and accepted lower-level formulas.
    child_rows_out = []
    child_failures = 0
    formula_failures = 0
    for ell in (1, 2, 3):
        for S in range(ell + 1, 9):
            B = S - ell
            ratios = tuple(wt(S - i) / wt(S - i + 1) for i in range(ell + 1))
            heights = {d: F(B + d - 1, B + d + 1) for d in range(1, ell + 1)}
            q = q_from_ratios(ratios)
            assert q == split(S, B)
            for K in range(2, 9):
                for R in range(1, K):
                    D = K - R
                    z = F(1, K + 1)
                    bound = arbitrary_F(ell, ratios, z, 0, D, heights)
                    actual = exact_H((S, K, R, B))
                    if actual > q * bound:
                        child_failures += 1
                    if ell == 1:
                        direct = direct_F1(ratios[0] * ratios[1], ratios[1], heights[1], F(D, K + 1))
                        if bound != direct:
                            formula_failures += 1
                    elif ell == 2:
                        direct = direct_F2(ratios, heights[2], heights[1], F(D, K + 1), F(D * (D + 1), (K + 1) * (K + 2)), F(D, K + 2))
                        if bound != direct:
                            formula_failures += 1
                    child_rows_out.append({"ell": ell, "state": [S, K, R, B], "ratio": rec(actual / (q * bound)) if bound else rec(F(0))})
    if child_failures or formula_failures:
        failures.append({"kind": "arbitrary-deficit", "bound_failures": child_failures, "formula_failures": formula_failures})

    # Lambda, endpoint marginal, C_s, and rational inequalities.
    lambda_failures = 0
    lambda_identity_failures = 0
    for A in range(1, 51):
        if lam(A, 2) != F(A, A + 1):
            lambda_failures += 1
        for degree in range(2, 12):
            if lam(A, degree) > F(2 * A, degree * (A + 1)):
                lambda_failures += 1
    for A in range(1, 9):
        for degree in range(2, 9):
            endpoint = (A,) + (1,) * (degree - 1)
            basin_mass = sum(rho_word(c) for c in comps(sum(endpoint)) if basin_contains(c, endpoint))
            capacity = degree * rho_word(endpoint)
            if basin_mass / capacity != lam(A, degree):
                lambda_identity_failures += 1
    marginal_failures = 0
    for s in range(2, 21):
        for degree in range(2, s + 1):
            lhs = sum(wt(A) * forest(s - A, degree - 1) / (math.factorial(degree) * wt(s + 1)) for A in range(1, s - degree + 2))
            rhs = F(math.comb(s - 1, degree - 1) * s ** (s - degree), (s + 1) ** (s - 1))
            if lhs != rhs:
                marginal_failures += 1
    if lambda_failures or lambda_identity_failures or marginal_failures or refined_mass_failures:
        failures.append({
            "kind": "lambda-or-marginal", "lambda": lambda_failures,
            "lambda_identity": lambda_identity_failures,
            "marginal": marginal_failures, "refined_mass": refined_mass_failures,
        })
    scalar_values = {s: coefficient_C(s) for s in (6, 7, 30, 50, 99, 100)}

    # Selected exact DAG/envelope checks and the coarse-template witness.
    # The sharp, valid subtraction is supported_mass*lambda.  The frozen
    # proof note instead displays supported_mass*lambda^2; retain exact
    # counterdiagnostics for that written (looser) envelope.
    exact_rows = []
    written_squared_rows = []
    for s in range(6, 10):
        for K in (1, 2, 5, 64, 4096):
            ratios, z, heights = actual_tuple(s, K)
            env, q, reset, desc, basins, live, subtraction = envelope_L5(ratios, z, heights, coefficient_C(s))
            actual = exact_H((s, K, K - 1, s - 5))
            actual_reset = literal_reset(s, K, K - 1, s - 5)
            if actual_reset > q * reset or actual > q * env or q * env > q * (1 - q):
                failures.append({"kind": "selected-L5", "s": s, "K": K})
            exact_rows.append({"s": s, "K": K, "actual_ratio": rec(actual / (q * (1 - q))), "envelope_ratio": rec(env / (1 - q)), "reset_ratio": rec(actual_reset / (q * reset)), "subtraction": rec(subtraction)})
            squared_env, squared_q, *_ = envelope_L5(ratios, z, heights, coefficient_C(s), 2)
            written_squared_rows.append({
                "s": s, "K": K,
                "envelope_ratio": rec(squared_env / (1 - squared_q)),
                "passes_target": squared_env <= 1 - squared_q,
            })

    s, K = 7, 4096
    ratios, z, heights = actual_tuple(s, K)
    refined, q, refined_reset, desc, *_ = envelope_L5(ratios, z, heights, coefficient_C(s))
    coarse_reset, _ = coarse_reset_bound(5, ratios, z, 0, 1, heights[5])
    coarse = coarse_reset + desc
    coarse_actual = exact_H((s, K, K - 1, 2))
    if not (coarse > 1 - q and coarse_actual < q * (1 - q)):
        failures.append({"kind": "coarse-witness"})

    # Finite in-interval Bernstein certificates.
    finite_certs = []
    finite_nonpositive = 0
    finite_min: tuple[F, int, int] | None = None
    inv12 = bern_inverse(12)
    for s in range(6, 100):
        ratios, _, heights = actual_tuple(s, 1)
        C = coefficient_C(s)
        samples = [cleared(ratios, F(j, 24), heights, C) for j in range(13)]
        coeff = [sum(inv12[i][j] * samples[j] for j in range(13)) for i in range(13)]
        off_t = F(7, 19)
        off_interp = sum(coeff[i] * math.comb(12, i) * off_t**i * (1 - off_t) ** (12 - i) for i in range(13))
        off_direct = cleared(ratios, off_t / 2, heights, C)
        if off_interp != off_direct:
            failures.append({"kind": "finite-off-grid", "s": s})
        finite_nonpositive += sum(x <= 0 for x in coeff)
        local = min((x, s, i) for i, x in enumerate(coeff))
        finite_min = local if finite_min is None or local < finite_min else finite_min
        finite_certs.append({"s": s, "coefficients": [rec(x) for x in coeff], "minimum": rec(local[0])})
    if finite_nonpositive:
        failures.append({"kind": "finite-Bernstein", "nonpositive": finite_nonpositive})

    # Exact countercertificate for the lambda^2 formula printed in the proof.
    sq_s = 6
    sq_ratios, _, sq_heights = actual_tuple(sq_s, 1)
    sq_samples = [cleared(sq_ratios, F(j, 24), sq_heights, coefficient_C(sq_s), 2) for j in range(13)]
    sq_coeff = [sum(inv12[i][j] * sq_samples[j] for j in range(13)) for i in range(13)]
    sq_min_index, sq_minimum = min(enumerate(sq_coeff), key=lambda pair: pair[1])

    # Degree audit and conditional tail tensor certificate.
    generic_ratios = (F(7, 20), F(9, 25), F(11, 30), F(3, 8), F(19, 50), F(23, 60))
    unit_heights = {ell: F(1) for ell in range(1, 6)}
    z_degree = diff_degree([cleared(generic_ratios, F(j, 17), unit_heights, F(3, 4)) for j in range(15)])
    ratio_degrees = []
    for axis in range(6):
        vals = []
        for j in range(4):
            x = list(generic_ratios)
            x[axis] += F(j, 100)
            vals.append(cleared(tuple(x), F(2, 7), unit_heights, F(3, 4)))
        ratio_degrees.append(diff_degree(vals))
    degrees = tuple(ratio_degrees) + (z_degree,)
    if degrees != (1, 1, 2, 2, 2, 2, 12):
        failures.append({"kind": "tail-degree", "degrees": list(degrees)})
    lo, hi = F(4, 11), F(187, 500)
    grid: dict[tuple[int, ...], F] = {}
    for idx in itertools.product(*(range(d + 1) for d in degrees)):
        unit = tuple(F(i, d) if d else F(0) for i, d in zip(idx, degrees))
        physical_ratios = tuple(lo + (hi - lo) * unit[i] for i in range(6))
        grid[idx] = cleared(physical_ratios, unit[6] / 2, unit_heights, F(3, 4))
    tail_coeff = tensor_coefficients(grid, degrees)
    tail_nonpositive = sum(x <= 0 for x in tail_coeff.values())
    tail_min_idx, tail_min = min(tail_coeff.items(), key=lambda pair: pair[1])
    off_unit = (F(1, 7), F(2, 7), F(3, 7), F(4, 7), F(5, 7), F(6, 7), F(7, 11))
    off_ratios = tuple(lo + (hi - lo) * off_unit[i] for i in range(6))
    if bern_eval(tail_coeff, degrees, off_unit) != cleared(off_ratios, off_unit[6] / 2, unit_heights, F(3, 4)):
        failures.append({"kind": "tail-off-grid"})
    if tail_nonpositive:
        failures.append({"kind": "tail-Bernstein", "nonpositive": tail_nonpositive})

    # Ratio box and corrected e inequalities, all rational.
    b95 = F(95**94, 96**94)
    e_upper = F(1957, 720) + F(1, 4410)
    e_partial = sum((F(1, math.factorial(n)) for n in range(6)), F(0))
    rational_checks = {
        "b95_below_upper": b95 < hi,
        "e_upper_below_87_over_32": e_upper < F(87, 32),
        "old_9_over_16_direction_refuted": 2 * (3 - e_upper) > F(9, 16),
        "partial_sum": rec(e_partial),
        "corrected_boundary": rec(2 * (3 - e_partial)),
    }
    if not all(v is True for k, v in rational_checks.items() if isinstance(v, bool)) or e_partial != F(163, 60) or 2 * (3 - e_partial) != F(17, 30):
        failures.append({"kind": "rational-bound"})

    # Fresh payload is complete before any optional reference is opened.
    comparison = None
    if args.reference_json:
        reference = json.loads(args.reference_json.read_text())
        finite_equal = 0
        for fresh, old in zip(finite_certs, reference["certificates"]["finite"]["rows"]):
            if fresh["s"] == old["s"] and all(parse_record(a) == parse_record(b) for a, b in zip(fresh["coefficients"], old["coefficients"])):
                finite_equal += len(fresh["coefficients"])
        old_tail = {tuple(row["index"]): parse_record(row["value"]) for row in reference["certificates"]["tail"]["coefficients"]}
        tail_equal = sum(tail_coeff[idx] == old_tail.get(idx) for idx in tail_coeff)
        old_children = {
            (row["excess"], row["S"], row["K"], row["R"]): parse_record(row["ratio"])
            for row in reference["child_audit"]
        }
        child_equal = sum(
            parse_record(row["ratio"]) == old_children.get((row["ell"], *row["state"][:3]))
            for row in child_rows_out
        )
        old_rows = {(row["s"], row["K"]): row for row in reference["rows"]}
        selected_equal = sum(
            all(
                parse_record(row[field]) == parse_record(old_rows[(row["s"], row["K"])][old_field])
                for field, old_field in (
                    ("actual_ratio", "actual_ratio"),
                    ("envelope_ratio", "envelope_ratio"),
                    ("reset_ratio", "reset_ratio_to_envelope"),
                )
            )
            for row in exact_rows
        )
        old_C = {row["s"]: parse_record(row["C_s"]) for row in reference["scalar_audit"]}
        scalar_equal = sum(value == old_C[s] for s, value in scalar_values.items())
        comparison = {
            "finite_equal": finite_equal, "finite_total": 1222,
            "tail_equal": tail_equal, "tail_total": 4212,
            "child_equal": child_equal, "child_total": 504,
            "selected_L5_equal": selected_equal, "selected_L5_total": len(exact_rows),
            "scalar_C_equal": scalar_equal, "scalar_C_total": len(scalar_values),
            "finite_min_equal": parse_record(reference["certificates"]["finite"]["rows"][1]["minimum"]) == finite_min[0],
            "tail_min_equal": parse_record(reference["certificates"]["tail"]["minimum"]) == tail_min,
            "coarse_ratio_equal": parse_record(reference["coarse_template_obstruction"]["coarse_envelope_ratio"]) == coarse / (1 - q),
            "coarse_actual_equal": parse_record(reference["coarse_template_obstruction"]["actual_ratio"]) == coarse_actual / (q * (1 - q)),
        }
        if (
            finite_equal != 1222 or tail_equal != 4212 or child_equal != 504
            or selected_equal != len(exact_rows) or scalar_equal != len(scalar_values)
            or not all(comparison[k] for k in ("finite_min_equal", "tail_min_equal", "coarse_ratio_equal", "coarse_actual_equal"))
        ):
            failures.append({"kind": "posthoc-reference-comparison", "comparison": comparison})

    payload = {
        "claim": "fresh audit of conditional auxiliary right-heavy L=5 reduction",
        "scope": "full nonlazy stationary-flow parking-degree reset recurrence only; Lemma C not attempted",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(), "dependencies": {}, "seed": None,
        "structure": structure,
        "literal_checks": literal_checks,
        "boundary_s6": {"retained_count": len(boundary), "triples": [list(x) for x in boundary_triples], "t2_absent": all(t != 2 for _, t, _ in boundary_triples)},
        "arbitrary_deficit": {"row_count": len(child_rows_out), "bound_failures": child_failures, "formula_failures": formula_failures, "rows": child_rows_out},
        "lambda_audit": {
            "bound_failures": lambda_failures,
            "direct_basin_identity_failures": lambda_identity_failures,
            "marginal_failures": marginal_failures,
            "refined_supported_mass_failures": refined_mass_failures,
            "C_values": {str(s): rec(x) for s, x in scalar_values.items()},
        },
        "selected_L5": exact_rows,
        "written_lambda_squared_formula": {
            "status": "valid but too loose; does not receive the frozen positive certificates",
            "selected_rows": written_squared_rows,
            "s6_minimum_Bernstein_index": sq_min_index,
            "s6_minimum_Bernstein_coefficient": rec(sq_minimum),
            "s6_nonpositive_count": sum(x <= 0 for x in sq_coeff),
            "correction": "replace supported_mass*lambda^2 by supported_mass*lambda; this is valid since supported_mass<=full_basin_mass=capacity*lambda",
        },
        "coarse_obstruction": {"state": [7, 4096, 4095, 2], "coarse_ratio": rec(coarse / (1 - q)), "actual_ratio": rec(coarse_actual / (q * (1 - q)))},
        "finite_certificate": {"count": 1222, "nonpositive": finite_nonpositive, "minimum": rec(finite_min[0]), "minimum_s": finite_min[1], "minimum_index": finite_min[2], "rows": finite_certs},
        "tail_certificate": {"degrees": list(degrees), "count": len(tail_coeff), "nonpositive": tail_nonpositive, "minimum": rec(tail_min), "minimum_index": list(tail_min_idx), "off_grid_identity": True,
            "coefficients": [{"index": list(idx), "value": rec(x)} for idx, x in sorted(tail_coeff.items())]},
        "ratio_and_e_checks": {"lo": rec(lo), "hi": rec(hi), "b95": rec(b95), "e_upper": rec(e_upper), **rational_checks},
        "posthoc_comparison": comparison,
        "frozen_objection_count": 1,
        "frozen_objection": "proof equation (5.1) prints lambda^2 while the certified implementation uses the sharper valid lambda subtraction",
        "failure_count": len(failures), "failures": failures,
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(text)
    print(json.dumps({
        "output": str(args.output), "sha256": hashlib.sha256(text.encode()).hexdigest(),
        "failure_count": len(failures), "finite_nonpositive": finite_nonpositive,
        "tail_nonpositive": tail_nonpositive, "finite_min": rec(finite_min[0]),
        "tail_min": rec(tail_min), "comparison": comparison,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
