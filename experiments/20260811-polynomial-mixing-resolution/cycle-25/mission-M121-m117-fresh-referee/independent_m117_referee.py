#!/usr/bin/env python3
"""Fresh exact referee reconstruction for M117.

This program imports no experiment module and reads no predecessor output.  It
starts from the accepted parking-projection definitions, implements literal
and aggregate canonical-basin paths separately, retains every attachment rank,
and derives the Bernstein certificates with an endpoint-grid Vandermonde
transform (different from M117's integer-node Lagrange implementation).
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import itertools
import json
import math
import platform
import time
from fractions import Fraction as F
from pathlib import Path


def rec(x: F) -> dict[str, str | float]:
    return {
        "numerator": str(x.numerator),
        "denominator": str(x.denominator),
        "decimal": float(x),
    }


@functools.cache
def weight(n: int) -> F:
    assert n >= 1
    return F(n ** (n - 1), math.factorial(n))


@functools.cache
def compositions(n: int) -> tuple[tuple[int, ...], ...]:
    """Ordered compositions, generated from separator masks."""
    if n == 0:
        return ((),)
    out: list[tuple[int, ...]] = []
    for mask in range(1 << (n - 1)):
        row: list[int] = []
        start = 0
        for pos in range(n - 1):
            if mask & (1 << pos):
                row.append(pos + 1 - start)
                start = pos + 1
        row.append(n - start)
        out.append(tuple(row))
    return tuple(out)


def choose(n: int, k: int) -> int:
    return math.comb(n, k) if 0 <= k <= n else 0


@functools.cache
def forest_weight(n: int, p: int) -> F:
    """Sum of products of w over p-part ordered compositions of n."""
    if n == 0 and p == 0:
        return F(1)
    if not 1 <= p <= n:
        return F(0)
    return F(p * n ** (n - p), n * math.factorial(n - p))


def literal_forest_weight(n: int, p: int) -> F:
    return sum(
        (math.prod(weight(a) for a in row) for row in compositions(n) if len(row) == p),
        F(0),
    )


def split(s: int, B: int) -> F:
    return weight(s + 1 - B) * weight(B) / weight(s + 1)


def root_mass(parts: tuple[int, ...]) -> F:
    s = sum(parts)
    return math.prod(weight(a) for a in parts) / (
        math.factorial(len(parts)) * weight(s + 1)
    )


def context_mean(k: int, t: int, K: int, R: int, B: int) -> F:
    if t < B:
        return F(0)
    if t == B:
        den = choose(k + K - 1, K - 1)
        num = K * choose(k + K - R - 2, K - R - 1)
        return F(num, den) if den else F(0)
    return split(t - 1, B) * (
        1 - F(choose(K, R + 1), choose(K + k, R + 1))
    )


def attach(K: int, R: int, k: int, j: int) -> F:
    return F(
        choose(R + j, j) * choose(K - R - 1 + k - j, k - j),
        choose(K + k, k),
    )


@functools.cache
def group_law(s: int) -> tuple[tuple[int, int, F], ...]:
    out: list[tuple[int, int, F]] = []
    for t in range(1, s + 1):
        for k in range(1, s + 1):
            mass = weight(t) * forest_weight(s - t, k - 1) / (
                math.factorial(k) * weight(s + 1)
            )
            if mass:
                out.append((k, t, mass))
    assert sum((row[2] for row in out), F(0)) == 1
    return tuple(out)


def active_endpoint(endpoint: tuple[int, ...]) -> bool:
    return len(endpoint) >= 2 and endpoint[0] + endpoint[1] - 1 >= 2


def in_basin(source: tuple[int, ...], endpoint: tuple[int, ...]) -> bool:
    tail = endpoint[1:]
    A = endpoint[0]
    for cut in range(1, len(source) + 1):
        if sum(source[:cut]) == A and source[cut:] == tail:
            return True
    return False


@functools.cache
def literal_basin_skeleton(s: int) -> tuple[tuple[tuple[int, ...], tuple[tuple[int, ...], ...]], ...]:
    roots = compositions(s)
    endpoints = tuple(
        row for row in roots if len(row) >= 2 and active_endpoint(row)
    )
    return tuple(
        (endpoint, tuple(source for source in roots if in_basin(source, endpoint)))
        for endpoint in endpoints
    )


def literal_basin_rows(s: int, K: int, R: int, B: int):
    q = split(s, B)
    masses = {row: root_mass(row) for row in compositions(s)}
    out = []
    for endpoint, sources in literal_basin_skeleton(s):
        theta = sum(
            (
                masses[source]
                * (context_mean(len(source), source[-1], K, R, B) - q)
                for source in sources
            ),
            F(0),
        )
        cap = len(endpoint) * masses[endpoint]
        out.append((endpoint, sources, theta, cap))
    return tuple(out)


def aggregate_basin_rows(s: int, K: int, R: int, B: int):
    """Independent p-summed basin computation using the forest identity."""
    q = split(s, B)
    out = []
    for endpoint in compositions(s):
        if not active_endpoint(endpoint):
            continue
        A, tail = endpoint[0], endpoint[1:]
        ell = len(tail)
        tail_weight = math.prod(weight(a) for a in tail)
        theta = tail_weight / weight(s + 1) * sum(
            (
                forest_weight(A, p)
                * (context_mean(p + ell, tail[-1], K, R, B) - q)
                / math.factorial(p + ell)
                for p in range(1, A + 1)
            ),
            F(0),
        )
        cap = len(endpoint) * root_mass(endpoint)
        out.append((endpoint, theta, cap))
    return tuple(out)


@functools.cache
def reset_literal(state: tuple[int, int, int, int]) -> F:
    return sum(
        (theta * theta / cap for _, _, theta, cap in literal_basin_rows(*state)),
        F(0),
    )


@functools.cache
def reset_aggregate(state: tuple[int, int, int, int]) -> F:
    return sum(
        (theta * theta / cap for _, theta, cap in aggregate_basin_rows(*state)),
        F(0),
    )


@functools.cache
def child_rows(state: tuple[int, int, int, int]):
    s, K, R, B = state
    phase = s + K - R
    out = []
    for k, t, mass in group_law(s):
        if t <= B or t - 1 < 2:
            continue
        assert sum((attach(K, R, k, j) for j in range(k + 1)), F(0)) == 1
        for j in range(1, k + 1):
            nu = attach(K, R, k, j)
            if not nu:
                continue
            child = (t - 1, K + k, R + j, B)
            assert child[0] + child[1] - child[2] < phase
            out.append((mass, nu, child, k, t, j))
    return tuple(out)


@functools.cache
def H_literal(state: tuple[int, int, int, int]) -> F:
    return reset_literal(state) + sum(
        (mass * nu * H_literal(child) for mass, nu, child, _, _, _ in child_rows(state)),
        F(0),
    )


@functools.cache
def H_aggregate(state: tuple[int, int, int, int]) -> F:
    return reset_aggregate(state) + sum(
        (mass * nu * H_aggregate(child) for mass, nu, child, _, _, _ in child_rows(state)),
        F(0),
    )


def killed(k: int, z: F) -> F:
    return F(math.factorial(k)) * z**k / math.prod(1 + a * z for a in range(1, k))


def nu_rh(k: int, j: int, z: F) -> F:
    if j == 0:
        return killed(k, z)
    return (
        F(math.factorial(k), math.factorial(j))
        * z ** (k - j)
        * (1 - z)
        * math.prod(1 + a * z for a in range(1, j - 1))
        / math.prod(1 + a * z for a in range(1, k))
    )


def F1(b: F, y: F, h: F, p: F) -> F:
    return b * (h - b / 2) + (2 * p - b) ** 2 / 4 + (1 - p) * (1 - y)


def F2_parts(R: F, U: F, Y: F, H0: F, H1: F, p: F, d: F, p_next: F) -> tuple[F, F]:
    a = U * Y
    q = F(3, 2) * R * a
    reset = (
        q * (H0 - 5 * q / 9 - q / (3 * Y))
        + (3 * d - q) ** 2 / 27
        + (3 * d + 6 * p - 4 * q) ** 2 / 54
        + (Y * (1 - d) - q) ** 2 / (6 * Y)
    )
    descendants = (1 - d) * (1 - Y) / 3 + F(2, 3) * (1 - p) * F1(a, Y, H1, p_next)
    return reset, descendants


def F2(R: F, U: F, Y: F, H0: F, H1: F, p: F, d: F, p_next: F) -> F:
    a, b = F2_parts(R, U, Y, H0, H1, p, d, p_next)
    return a + b


def actual_l4_parameters(s: int, K: int):
    return (
        weight(s) / weight(s + 1),
        weight(s - 1) / weight(s),
        weight(s - 2) / weight(s - 1),
        weight(s - 3) / weight(s - 2),
        weight(s - 4) / weight(s - 3),
        F(1, K + 1),
        F(s - 1, s + 1),
        F(s - 4, s - 2),
        F(s - 3, s - 1),
    )


def l4_support_closed(r: F, u: F, v: F, y: F, x: F, z: F):
    d, e, f = killed(2, z), killed(3, z), killed(4, z)
    q = F(125, 24) * r * u * v * y * x
    rows = {
        (0, (4,)): (F(32, 125), 2 * z),
        (0, (1, 3)): (F(6, 125), 3 * d),
        (0, (3, 1)): (F(6, 125), 3 * d),
        (0, (2, 2)): (F(4, 125), 3 * d),
        (0, (1, 1, 2)): (F(1, 125), 4 * e),
        (0, (1, 2, 1)): (F(1, 125), 4 * e),
        (0, (2, 1, 1)): (F(1, 125), 4 * e),
        (0, (1, 1, 1, 1)): (F(1, 625), 5 * f),
        (1, (3,)): (F(18, 125) / x, x * (1 - d)),
        (1, (1, 2)): (F(4, 125) / x, x * (1 - e)),
        (1, (2, 1)): (F(4, 125) / x, x * (1 - e)),
        (1, (1, 1, 1)): (F(1, 125) / x, x * (1 - f)),
        (2, (2,)): (F(12, 125) / (x * y), x * y * (1 - d)),
        (2, (1, 1)): (F(4, 125) / (x * y), x * y * (1 - e)),
        (3, (1,)): (F(12, 125) / (x * y * v), F(3, 2) * x * y * v * (1 - d)),
        (4, ()): (F(24, 125) / (u * v * y * x), F(8, 3) * u * v * y * x * (1 - z)),
    }
    assert len(rows) == 16
    assert sum((mass * mean for mass, mean in rows.values()), F(0)) == 1
    return q, rows


def prefix_endpoints(prefix: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple((sum(prefix[:cut]),) + prefix[cut:] for cut in range(1, len(prefix) + 1))


def prefix_in_basin(source: tuple[int, ...], endpoint: tuple[int, ...]) -> bool:
    return in_basin(source, endpoint)


def l4_exception_rows(r: F, u: F, v: F, y: F, x: F, z: F):
    q, support = l4_support_closed(r, u, v, y, x, z)
    endpoints = sorted(
        {(h, e) for h, prefix in support for e in prefix_endpoints(prefix)},
        key=lambda item: (item[0], len(item[1]), item[1]),
    )
    assert len(endpoints) == 15
    out = []
    for h, endpoint in endpoints:
        sources = tuple(
            prefix
            for (source_h, prefix), _ in support.items()
            if source_h == h and prefix_in_basin(prefix, endpoint)
        )
        theta_q = sum(
            (support[(h, source)][0] * (support[(h, source)][1] - q) for source in sources),
            F(0),
        )
        cap_q = (len(endpoint) + 1) * support[(h, endpoint)][0]
        full_endpoint = endpoint + (None,)
        is_active = not (len(full_endpoint) >= 2 and endpoint[0] == 1 and (len(endpoint) >= 2 and endpoint[1] == 1))
        # The exact activity test depends on the first two full parts.  For a
        # one-part prefix, the second part is the last part and is >=2 here.
        if len(endpoint) == 1:
            is_active = True
        out.append((h, endpoint, sources, theta_q, cap_q, is_active))
    return q, tuple(out)


def l4_expected_exception_values(r: F, u: F, v: F, y: F, x: F, z: F):
    q = F(125, 24) * r * u * v * y * x
    d, e, f = killed(2, z), killed(3, z), killed(4, z)
    return {
        (0, (1, 1, 1, 1)): ((5 * f - q) / 625, F(1, 125)),
        (0, (2, 1, 1)): ((20 * e + 5 * f - 6 * q) / 625, F(4, 125)),
        (0, (1, 2, 1)): ((4 * e - q) / 125, F(4, 125)),
        (0, (3, 1)): ((90 * d + 40 * e + 5 * f - 41 * q) / 625, F(18, 125)),
        (0, (1, 1, 2)): ((4 * e - q) / 125, F(4, 125)),
        (0, (2, 2)): ((12 * d + 4 * e - 5 * q) / 125, F(12, 125)),
        (0, (1, 3)): (6 * (3 * d - q) / 125, F(18, 125)),
        (0, (4,)): ((320 * z + 240 * d + 60 * e + 5 * f - 256 * q) / 625, F(64, 125)),
        (1, (1, 1, 1)): ((x * (1 - f) - q) / (125 * x), F(4, 125) / x),
        (1, (2, 1)): ((5 * x - 4 * x * e - x * f - 5 * q) / (125 * x), F(12, 125) / x),
        (1, (1, 2)): (4 * (x * (1 - e) - q) / (125 * x), F(12, 125) / x),
        (1, (3,)): ((27 * x - 18 * x * d - 8 * x * e - x * f - 27 * q) / (125 * x), F(36, 125) / x),
        (2, (1, 1)): (4 * (x * y * (1 - e) - q) / (125 * x * y), F(12, 125) / (x * y)),
        (2, (2,)): ((16 * x * y - 12 * x * y * d - 4 * x * y * e - 16 * q) / (125 * x * y), F(24, 125) / (x * y)),
        (3, (1,)): (12 * (F(3, 2) * x * y * v * (1 - d) - q) / (125 * x * y * v), F(24, 125) / (x * y * v)),
    }


def l4_reset_envelope(r: F, u: F, v: F, y: F, x: F, z: F, h0: F) -> F:
    """Upper bound for A_0/q, including inactive exceptional edges."""
    q, support = l4_support_closed(r, u, v, y, x, z)
    q2, rows = l4_exception_rows(r, u, v, y, x, z)
    assert q2 == q
    supported_height = sum(
        (mass * len(prefix) for (_, prefix), (mass, _) in support.items()), F(0)
    )
    expected_height = F(369, 625) + F(37, 125) / x + F(4, 25) / (x * y) + F(12, 125) / (x * y * v)
    assert supported_height == expected_height
    return q * (h0 - q * supported_height) + sum(
        (theta * theta / cap for _, _, _, theta, cap, _ in rows), F(0)
    )


def l4_live_group_masses(x: F, y: F, v: F, u: F):
    return {
        (1, 2): F(18, 125) / x,
        (1, 3): F(8, 125) / x,
        (1, 4): F(1, 125) / x,
        (2, 2): F(12, 125) / (x * y),
        (2, 3): F(4, 125) / (x * y),
        (3, 2): F(12, 125) / (x * y * v),
        (4, 1): F(24, 125) / (u * v * y * x),
    }


def l4_descendant_rank_sum(r: F, u: F, v: F, y: F, x: F, z: F, h1: F, h2: F):
    """All seven groups and all retained ranks, before any aggregation."""
    total = F(0)
    audit = []
    for (h, k), mass_q in l4_live_group_masses(x, y, v, u).items():
        assert sum((nu_rh(k, j, z) for j in range(k + 1)), F(0)) == 1
        rank_rows = []
        for j in range(1, k + 1):
            nu = nu_rh(k, j, z)
            deficit = k + 1 - j
            if h == 1:
                sector = "all-deficit L=0"
                child_split = x
                child_bound = x * (1 - x)
            elif h == 2:
                sector = "arbitrary-deficit L=1"
                child_split = x * y
                p = deficit * z / (1 + k * z)
                child_bound = child_split * F1(child_split, x, h1, p)
            elif h == 3:
                child_split = F(3, 2) * v * y * x
                if j == 1:
                    sector = "arbitrary-deficit L=2"
                    p = 2 * z / (1 + 2 * z)
                    d = 6 * z * z / ((1 + 2 * z) * (1 + 3 * z))
                    p_next = 2 * z / (1 + 3 * z)
                    child_bound = child_split * F2(v, y, x, h2, h1, p, d, p_next)
                else:
                    assert j == 2
                    sector = "right-heavy L=2"
                    child_bound = child_split * (1 - child_split)
            else:
                assert h == 4 and k == 1 and j == 1
                sector = "right-heavy L=3"
                child_split = F(8, 3) * u * v * y * x
                child_bound = child_split * (1 - child_split)
            contribution = mass_q * nu * child_bound
            total += contribution
            rank_rows.append(
                {
                    "j": j,
                    "nu": nu,
                    "deficit": deficit,
                    "sector": sector,
                    "child_split": child_split,
                    "child_bound": child_bound,
                    "normalized_contribution": contribution,
                }
            )
        audit.append(
            {
                "h": h,
                "k": k,
                "mass_over_q": mass_q,
                "killed": nu_rh(k, 0, z),
                "retained_sum": sum((row["nu"] for row in rank_rows), F(0)),
                "ranks": tuple(rank_rows),
            }
        )
    assert len(audit) == 7
    return total, tuple(audit)


def l4_descendant_closed(r: F, u: F, v: F, y: F, x: F, z: F, h1: F, h2: F) -> F:
    d, e, f = killed(2, z), killed(3, z), killed(4, z)
    first = (1 - x) * (18 * (1 - d) + 8 * (1 - e) + (1 - f)) / 125
    second = F(0)
    for k, coefficient in ((2, F(12, 125)), (3, F(4, 125))):
        for j in range(1, k + 1):
            p = (k + 1 - j) * z / (1 + k * z)
            second += coefficient * nu_rh(k, j, z) * F1(x * y, x, h1, p)
    c2 = F(3, 2) * v * y * x
    p = 2 * z / (1 + 2 * z)
    d2 = 6 * z * z / ((1 + 2 * z) * (1 + 3 * z))
    p_next = 2 * z / (1 + 3 * z)
    third = F(18, 125) * (
        nu_rh(2, 1, z) * F2(v, y, x, h2, h1, p, d2, p_next)
        + nu_rh(2, 2, z) * (1 - c2)
    )
    c3 = F(8, 3) * u * v * y * x
    fourth = F(64, 125) * (1 - z) * (1 - c3)
    return first + second + third + fourth


def l4_envelope(r: F, u: F, v: F, y: F, x: F, z: F, h0: F, h1: F, h2: F) -> tuple[F, F]:
    descendants, _ = l4_descendant_rank_sum(r, u, v, y, x, z, h1, h2)
    closed = l4_descendant_closed(r, u, v, y, x, z, h1, h2)
    assert descendants == closed
    q = F(125, 24) * r * u * v * y * x
    return l4_reset_envelope(r, u, v, y, x, z, h0) + descendants, q


def cleared_slack(r: F, u: F, v: F, y: F, x: F, z: F, h0: F, h1: F, h2: F) -> F:
    envelope, q = l4_envelope(r, u, v, y, x, z, h0, h1, h2)
    Delta = math.prod(1 + a * z for a in range(1, 5))
    return Delta * Delta * (1 - q - envelope)


def l2_closed_support(S: int, K: int, R0: int):
    B = S - 2
    D = K - R0
    p = F(D, K + 1)
    d = F(D * (D + 1), (K + 1) * (K + 2))
    top = weight(S) / weight(S + 1)
    middle = weight(S - 1) / weight(S)
    Y = weight(S - 2) / weight(S - 1)
    a = middle * Y
    q = F(3, 2) * top * a
    return q, {
        (2, B): (q / 3, 2 * p),
        (1, 1, B): (q / 9, 3 * d),
        (1, S - 1): (q / (3 * Y), Y * (1 - d)),
        (S,): (top, a * (1 - p)),
    }


def l2_exception_rows(S: int, K: int, R0: int):
    q, support = l2_closed_support(S, K, R0)
    basins = ((1, 1, S - 2), (2, S - 2), (1, S - 1))
    out = []
    for endpoint in basins:
        sources = tuple(source for source in support if in_basin(source, endpoint))
        theta_q = sum(
            (support[source][0] / q * (support[source][1] - q) for source in sources),
            F(0),
        )
        cap_q = len(endpoint) * support[endpoint][0] / q
        out.append((endpoint, sources, theta_q, cap_q, active_endpoint(endpoint)))
    return q, tuple(out)


def l2_expected_exception_values(S: int, K: int, R0: int):
    D = K - R0
    p = F(D, K + 1)
    d = F(D * (D + 1), (K + 1) * (K + 2))
    top = weight(S) / weight(S + 1)
    middle = weight(S - 1) / weight(S)
    Y = weight(S - 2) / weight(S - 1)
    q = F(3, 2) * top * middle * Y
    return {
        (1, 1, S - 2): ((3 * d - q) / 9, F(1, 3)),
        (2, S - 2): ((3 * d + 6 * p - 4 * q) / 9, F(2, 3)),
        (1, S - 1): ((Y * (1 - d) - q) / (3 * Y), F(2, 3) / Y),
    }


def l2_descendant_rank_bound(S: int, K: int, R0: int) -> tuple[F, tuple[dict[str, object], ...]]:
    D = K - R0
    B = S - 2
    top = weight(S) / weight(S + 1)
    middle = weight(S - 1) / weight(S)
    Y = weight(S - 2) / weight(S - 1)
    a = middle * Y
    q = F(3, 2) * top * a
    p = F(D, K + 1)
    p_next = F(D, K + 2)
    rows = []
    total = F(0)
    for k, t, mass in group_law(S):
        if t <= B:
            continue
        if (k, t) == (2, S - 1):
            ranks = []
            for j in range(1, 3):
                nu = attach(K, R0, 2, j)
                bound = Y * (1 - Y)
                contribution = F(0) if S == 3 else mass * nu * bound / q
                total += contribution
                ranks.append((j, nu, bound, contribution))
            rows.append({"k": 2, "t": t, "mass_over_q": mass / q, "ranks": tuple(ranks), "boundary_inactive": S == 3})
        elif (k, t) == (1, S):
            nu = attach(K, R0, 1, 1)
            bound = a * F1(a, Y, F(S - 2, S), p_next)
            contribution = mass * nu * bound / q
            total += contribution
            rows.append({"k": 1, "t": t, "mass_over_q": mass / q, "ranks": ((1, nu, bound, contribution),), "boundary_inactive": False})
        else:
            raise AssertionError((S, k, t))
    d = F(D * (D + 1), (K + 1) * (K + 2))
    displayed = (1 - d) * (1 - Y) / 3 + F(2, 3) * (1 - p) * F1(a, Y, F(S - 2, S), p_next)
    assert total == displayed
    return total, tuple(rows)


def forward_layers(values: list[F]) -> list[list[F]]:
    layers = [values]
    while len(layers[-1]) > 1:
        row = layers[-1]
        layers.append([row[i + 1] - row[i] for i in range(len(row) - 1)])
    return layers


def inverse_matrix(matrix: list[list[F]]) -> list[list[F]]:
    n = len(matrix)
    aug = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if aug[i][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for row in range(n):
            if row == col or not aug[row][col]:
                continue
            scale = aug[row][col]
            aug[row] = [a - scale * b for a, b in zip(aug[row], aug[col])]
    return [row[n:] for row in aug]


@functools.cache
def endpoint_value_to_bernstein(degree: int) -> tuple[tuple[F, ...], ...]:
    """Values at i/d on [0,1] to degree-d Bernstein coefficients."""
    assert degree >= 1
    nodes = [F(i, degree) for i in range(degree + 1)]
    vandermonde = [[x**p for p in range(degree + 1)] for x in nodes]
    inv = inverse_matrix(vandermonde)
    transform = []
    for j in range(degree + 1):
        row = []
        for value_index in range(degree + 1):
            row.append(
                sum(
                    (
                        F(math.comb(j, p), math.comb(degree, p))
                        * inv[p][value_index]
                        for p in range(j + 1)
                    ),
                    F(0),
                )
            )
        transform.append(tuple(row))
    return tuple(transform)


def tensor_transform(values: dict[tuple[int, ...], F], degrees: tuple[int, ...]) -> dict[tuple[int, ...], F]:
    current = values
    ranges = tuple(range(d + 1) for d in degrees)
    for axis, degree in enumerate(degrees):
        matrix = endpoint_value_to_bernstein(degree)
        nxt = {}
        for out_index in itertools.product(*ranges):
            nxt[out_index] = sum(
                (
                    matrix[out_index[axis]][node]
                    * current[out_index[:axis] + (node,) + out_index[axis + 1 :]]
                    for node in range(degree + 1)
                ),
                F(0),
            )
        current = nxt
    return current


def bernstein_eval(coefficients: dict[tuple[int, ...], F], degrees: tuple[int, ...], point: tuple[F, ...]) -> F:
    total = F(0)
    for index, coefficient in coefficients.items():
        basis = F(1)
        for degree, i, x in zip(degrees, index, point):
            basis *= math.comb(degree, i) * x**i * (1 - x) ** (degree - i)
        total += coefficient * basis
    return total


def jsonable(obj):
    if isinstance(obj, F):
        return rec(obj)
    if isinstance(obj, tuple):
        return [jsonable(x) for x in obj]
    if isinstance(obj, list):
        return [jsonable(x) for x in obj]
    if isinstance(obj, dict):
        return {str(k): jsonable(v) for k, v in obj.items()}
    return obj


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()

    # First validate the closed forest-weight identity against a literal sum.
    forest_checks = []
    for n in range(1, 10):
        for p in range(1, n + 1):
            literal = literal_forest_weight(n, p)
            closed = forest_weight(n, p)
            assert literal == closed
            forest_checks.append((n, p, closed))

    l4_rows = []
    support_snapshot = None
    basin_snapshot = None
    live_snapshot = None
    for s in range(5, 10):
        B = s - 4
        for K in (1, 2, 5):
            r, u, v, y, x, z, h0, h1, h2 = actual_l4_parameters(s, K)
            q, closed_support = l4_support_closed(r, u, v, y, x, z)
            assert q == split(s, B)

            direct_support = {}
            for parts in compositions(s):
                mean = context_mean(len(parts), parts[-1], K, K - 1, B)
                if mean:
                    direct_support[parts] = (root_mass(parts) / q, mean)
            expected_parts = {
                prefix + (B + h,): values
                for (h, prefix), values in closed_support.items()
            }
            assert direct_support == expected_parts
            assert len(direct_support) == 16
            assert sum((root_mass(parts) * mean for parts, (_, mean) in direct_support.items()), F(0)) == q

            nonzero_groups = tuple(
                sorted(
                    (k, t)
                    for k, t, _ in group_law(s)
                    if context_mean(k, t, K, K - 1, B)
                )
            )
            expected_groups = tuple(
                sorted(
                    ((2, B), (3, B), (4, B), (5, B),
                     (2, s - 3), (3, s - 3), (4, s - 3),
                     (2, s - 2), (3, s - 2), (2, s - 1), (1, s))
                )
            )
            assert nonzero_groups == expected_groups

            q2, exception_rows = l4_exception_rows(r, u, v, y, x, z)
            assert q2 == q
            expected_exception = l4_expected_exception_values(r, u, v, y, x, z)
            assert {(h, endpoint) for h, endpoint, *_ in exception_rows} == set(expected_exception)
            assert len(exception_rows) == 15
            for h, endpoint, sources, theta_q, cap_q, _ in exception_rows:
                assert (theta_q, cap_q) == expected_exception[(h, endpoint)]
                assert sources
            assert sum(int(row[-1]) for row in exception_rows) == 11

            literal_rows = literal_basin_rows(s, K, K - 1, B)
            literal_map = {endpoint: (sources, theta / q, cap / q) for endpoint, sources, theta, cap in literal_rows}
            for h, endpoint_prefix, source_prefixes, theta_q, cap_q, active in exception_rows:
                full_endpoint = endpoint_prefix + (B + h,)
                if not active:
                    assert not active_endpoint(full_endpoint)
                    continue
                assert active_endpoint(full_endpoint)
                sources, theta_literal_q, cap_literal_q = literal_map[full_endpoint]
                expected_sources = tuple(prefix + (B + h,) for prefix in source_prefixes)
                assert set(sources) == set(expected_sources)
                assert theta_literal_q == theta_q
                assert cap_literal_q == cap_q

            state = (s, K, K - 1, B)
            assert reset_literal(state) == reset_aggregate(state)
            exact_reset = reset_literal(state)
            reset_bound_q = q * l4_reset_envelope(r, u, v, y, x, z, h0)
            assert exact_reset <= reset_bound_q

            rank_bound, live_rows = l4_descendant_rank_sum(r, u, v, y, x, z, h1, h2)
            assert rank_bound == l4_descendant_closed(r, u, v, y, x, z, h1, h2)
            assert len(live_rows) == 7
            group_map = {(k, t): mass for k, t, mass in group_law(s)}
            for live in live_rows:
                h, k = live["h"], live["k"]
                t = B + h
                assert group_map[(k, t)] / q == live["mass_over_q"]
                assert tuple(rank["j"] for rank in live["ranks"]) == tuple(range(1, k + 1))
                assert live["retained_sum"] == 1 - live["killed"]
                for rank in live["ranks"]:
                    j = rank["j"]
                    assert rank["nu"] == attach(K, K - 1, k, j)
                    child = (t - 1, K + k, K - 1 + j, B)
                    assert child[1] - child[2] == rank["deficit"]
                    assert child[0] - child[3] == h - 1

            envelope_q, q3 = l4_envelope(r, u, v, y, x, z, h0, h1, h2)
            assert q3 == q
            exact_literal = H_literal(state)
            exact_aggregate = H_aggregate(state)
            assert exact_literal == exact_aggregate
            assert exact_literal <= q * envelope_q <= q * (1 - q)
            l4_rows.append(
                {
                    "s": s,
                    "K": K,
                    "literal_basin_count": len(literal_rows),
                    "active_exception_count": sum(int(row[-1]) for row in exception_rows),
                    "reset_ratio_to_envelope": exact_reset / reset_bound_q,
                    "resolvent_ratio_to_envelope": exact_literal / (q * envelope_q),
                    "resolvent_ratio_to_target": exact_literal / (q * (1 - q)),
                    "envelope_ratio_to_target": envelope_q / (1 - q),
                }
            )

            if (s, K) == (9, 5):
                support_snapshot = [
                    {
                        "h": h,
                        "prefix": prefix,
                        "full_composition": prefix + (B + h,),
                        "mass_over_q": values[0],
                        "mean": values[1],
                    }
                    for (h, prefix), values in sorted(closed_support.items())
                ]
                basin_snapshot = [
                    {
                        "h": h,
                        "endpoint_prefix": endpoint,
                        "full_endpoint": endpoint + (B + h,),
                        "source_prefixes": sources,
                        "theta_over_q": theta,
                        "capacity_over_q": cap,
                        "active": active,
                    }
                    for h, endpoint, sources, theta, cap, active in exception_rows
                ]
                live_snapshot = live_rows

    assert support_snapshot is not None and basin_snapshot is not None and live_snapshot is not None
    assert [row["literal_basin_count"] for row in l4_rows if row["K"] == 1] == [11, 23, 47, 95, 191]
    recursive_states = set()
    stack = [(s, K, K - 1, s - 4) for s in range(5, 10) for K in (1, 2, 5)]
    while stack:
        state = stack.pop()
        if state in recursive_states:
            continue
        recursive_states.add(state)
        stack.extend(child for _, _, child, _, _, _ in child_rows(state))
    assert all(reset_literal(state) == reset_aggregate(state) for state in recursive_states)

    # General-attachment L=2 proposition, including the S=3 boundary.
    l2_rows = []
    boundary_rows = []
    for S in range(3, 10):
        B = S - 2
        top = weight(S) / weight(S + 1)
        middle = weight(S - 1) / weight(S)
        Y = weight(S - 2) / weight(S - 1)
        for K in range(2, 10):
            for R0 in range(1, K):
                D = K - R0
                q, closed_support = l2_closed_support(S, K, R0)
                assert q == split(S, B)
                direct_support = {
                    parts: (root_mass(parts), context_mean(len(parts), parts[-1], K, R0, B))
                    for parts in compositions(S)
                    if context_mean(len(parts), parts[-1], K, R0, B)
                }
                assert direct_support == closed_support
                assert len(direct_support) == 4
                assert sum((mass * mean for mass, mean in direct_support.values()), F(0)) == q

                _, exception_rows = l2_exception_rows(S, K, R0)
                expected = l2_expected_exception_values(S, K, R0)
                assert len(exception_rows) == 3
                for endpoint, sources, theta_q, cap_q, active in exception_rows:
                    assert (theta_q, cap_q) == expected[endpoint]
                    assert sources
                    if S == 3 and endpoint == (1, 1, 1):
                        assert not active

                state = (S, K, R0, B)
                assert reset_literal(state) == reset_aggregate(state)
                exact_reset = reset_literal(state)
                exact_H = H_literal(state)
                assert exact_H == H_aggregate(state)
                p = F(D, K + 1)
                d = F(D * (D + 1), (K + 1) * (K + 2))
                p_next = F(D, K + 2)
                reset_over_q, descendants_over_q = F2_parts(
                    top, middle, Y, F(S - 1, S + 1), F(S - 2, S), p, d, p_next
                )
                rank_descendants, rank_rows = l2_descendant_rank_bound(S, K, R0)
                assert rank_descendants == descendants_over_q
                assert exact_reset <= q * reset_over_q
                assert exact_H <= q * (reset_over_q + descendants_over_q)
                l2_rows.append(
                    {
                        "S": S,
                        "K": K,
                        "R": R0,
                        "D": D,
                        "reset_ratio": exact_reset / (q * reset_over_q),
                        "resolvent_ratio": exact_H / (q * (reset_over_q + descendants_over_q)),
                    }
                )
                if S == 3:
                    actual_children = child_rows(state)
                    assert all(not (k == 2 and t == 2) for _, _, _, k, t, _ in actual_children)
                    assert Y == 1
                    assert (1 - d) * (1 - Y) / 3 == 0
                    boundary_rows.append(
                        {
                            "K": K,
                            "R": R0,
                            "D": D,
                            "Y": Y,
                            "terminal_group_actual_rank_count": 0,
                            "terminal_group_displayed_charge": F(0),
                            "live_group_rows": rank_rows,
                        }
                    )
    assert len(l2_rows) == 252

    # Height monotonicity is checked as an exact affine identity at a generic
    # point; the proof note records the algebraic nonnegative coefficients.
    generic = (F(7, 20), F(9, 25), F(11, 30), F(3, 8), F(19, 50), F(2, 7))
    height_base = (F(4, 5), F(3, 4), F(5, 6))
    height_slopes = []
    for axis in range(3):
        values = []
        for bump in range(3):
            heights = list(height_base)
            heights[axis] += bump
            values.append(l4_envelope(*generic, *heights)[0])
        assert values[2] - 2 * values[1] + values[0] == 0
        slope = values[1] - values[0]
        assert slope > 0
        height_slopes.append(slope)

    # Finite s certificates via values at the actual interval nodes i/20.
    finite_certificates = []
    for s in range(5, 22):
        r, u, v, y, x, _, h0, h1, h2 = actual_l4_parameters(s, 1)
        values = {
            (i,): cleared_slack(r, u, v, y, x, F(i, 20), h0, h1, h2)
            for i in range(11)
        }
        coefficients = tensor_transform(values, (10,))
        assert all(value > 0 for value in coefficients.values())
        degree_values = [
            cleared_slack(r, u, v, y, x, F(i, 22), h0, h1, h2)
            for i in range(12)
        ]
        layers = forward_layers(degree_values)
        assert layers[10][0] != 0 and layers[11][0] == 0
        off_grid = F(2, 7)
        assert bernstein_eval(coefficients, (10,), (off_grid,)) == cleared_slack(
            r, u, v, y, x, off_grid / 2, h0, h1, h2
        )
        finite_certificates.append(
            {
                "s": s,
                "degree": 10,
                "minimum": min(coefficients.values()),
                "minimum_index": min(coefficients, key=coefficients.get),
                "nonpositive_count": sum(value <= 0 for value in coefficients.values()),
                "off_grid_identity": True,
                "coefficients": [coefficients[(i,)] for i in range(11)],
            }
        )
    finite_min_row = min(
        ((row["minimum"], row["s"], row["minimum_index"]) for row in finite_certificates),
        key=lambda row: row[0],
    )
    assert finite_min_row == (
        F(71734022477173585947, 9023189417984000000000), 7, (0,)
    )

    # Tail tensor certificate, sampled only at in-box endpoint grids.
    degrees = (2, 2, 2, 2, 2, 10)
    box_values = {}
    for index in itertools.product(*(range(d + 1) for d in degrees)):
        ratios = tuple(F(1, 3) + F(1, 15) * F(index[a], 2) for a in range(5))
        z = F(index[5], 20)
        box_values[index] = cleared_slack(*ratios, z, F(1), F(1), F(1))
    box_coefficients = tensor_transform(box_values, degrees)
    assert len(box_coefficients) == 2673
    assert all(value > 0 for value in box_coefficients.values())
    tail_min_index = min(box_coefficients, key=box_coefficients.get)
    tail_minimum = box_coefficients[tail_min_index]
    assert (tail_min_index, tail_minimum) == (
        (2, 2, 2, 2, 0, 0), F(742081, 227812500)
    )
    off_grid = (F(1, 7), F(2, 7), F(3, 7), F(4, 7), F(5, 7), F(3, 8))
    physical = tuple(F(1, 3) + F(1, 15) * off_grid[a] for a in range(5)) + (F(1, 2) * off_grid[5],)
    assert bernstein_eval(box_coefficients, degrees, off_grid) == cleared_slack(
        *physical, F(1), F(1), F(1)
    )

    # Exact generic-slice degree detection supplements the algebraic degree
    # bound: every ratio has sharp degree two and z has sharp degree ten.
    ratio_degrees = []
    representatives = [F(7, 20), F(9, 25), F(11, 30), F(3, 8), F(19, 50)]
    for axis in range(5):
        values = []
        for i in range(4):
            point = representatives[:]
            point[axis] = F(1, 3) + F(1, 15) * F(i, 3)
            values.append(cleared_slack(*point, F(2, 7), F(4, 5), F(3, 4), F(5, 6)))
        layers = forward_layers(values)
        assert layers[2][0] != 0 and layers[3][0] == 0
        ratio_degrees.append(2)
    z_values = [
        cleared_slack(*representatives, F(i, 22), F(4, 5), F(3, 4), F(5, 6))
        for i in range(12)
    ]
    z_layers = forward_layers(z_values)
    assert z_layers[10][0] != 0 and z_layers[11][0] == 0

    b18 = F(18, 19) ** 17
    assert b18 < F(2, 5)
    assert all(F(1, 3) < weight(n) / weight(n + 1) for n in range(1, 80))
    assert all(weight(n + 1) / weight(n + 2) < weight(n) / weight(n + 1) for n in range(1, 79))

    source_path = Path(__file__)
    payload = {
        "claim": "fresh exact audit of auxiliary right-heavy suffix excess L=4 contraction",
        "scope": "auxiliary full nonlazy stationary-flow parking-degree reset excursion only",
        "target": "uniform fixed-length identity words on Omega(N,m) remains the project target",
        "convention": "(pq)(x)=p(q(x)); factors displayed left-to-right",
        "status": "exact reconstruction plus universal Bernstein certificates",
        "base_commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
        "command": "python3 -B independent_m117_referee.py --output independent_m117_referee.json",
        "python": platform.python_version(),
        "dependencies": "Python standard library only",
        "seed": None,
        "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
        "forest_identity_check_count": len(forest_checks),
        "support": {
            "count": len(support_snapshot),
            "snapshot_s9_K5": support_snapshot,
            "direct_formula_rows_checked": 15,
            "positive_group_count": 11,
        },
        "basins": {
            "exceptional_count": len(basin_snapshot),
            "active_exceptional_count": sum(int(row["active"]) for row in basin_snapshot),
            "snapshot_s9_K5": basin_snapshot,
            "literal_basin_counts_s5_to_s9": [row["literal_basin_count"] for row in l4_rows if row["K"] == 1],
        },
        "live_groups": {
            "count": len(live_snapshot),
            "snapshot_s9_K5": live_snapshot,
            "every_j_retained": True,
            "rank_sum_equals_closed_formula": True,
        },
        "l4_exact_dag": {
            "row_count": len(l4_rows),
            "recursive_state_count": len(recursive_states),
            "rows": l4_rows,
            "literal_equals_grouped_every_state": True,
            "failure_count": 0,
        },
        "arbitrary_deficit_l2": {
            "row_count": len(l2_rows),
            "rows": l2_rows,
            "three_exceptional_basins": True,
            "two_descendant_groups": True,
            "boundary_S3": boundary_rows,
            "failure_count": 0,
        },
        "height_monotonicity": {
            "affine": True,
            "positive_slopes": height_slopes,
            "interpretation": "replacing h0,h1,h2 by one enlarges E4",
        },
        "finite_certificates": {
            "range": "s=5,...,21; z in [0,1/2]",
            "degree": 10,
            "coefficient_count": 187,
            "nonpositive_count": 0,
            "minimum": finite_min_row[0],
            "minimum_s": finite_min_row[1],
            "minimum_index": finite_min_row[2],
            "rows": finite_certificates,
        },
        "tail_certificate": {
            "box": "[1/3,2/5]^5 x [0,1/2]",
            "multidegree": degrees,
            "detected_sharp_multidegree": tuple(ratio_degrees) + (10,),
            "coefficient_count": len(box_coefficients),
            "nonpositive_count": 0,
            "minimum": tail_minimum,
            "minimum_index": tail_min_index,
            "off_grid_identity": True,
            "b18": b18,
            "b18_below_two_fifths": True,
            "inclusion_proof": "b_n decreases, b_n>1/3, and b_18<2/5; s>=22 has all five indices >=18",
            "coefficients": [
                {"index": index, "value": value}
                for index, value in sorted(box_coefficients.items())
            ],
        },
        "failure_count": 0,
    }
    encoded = json.dumps(jsonable(payload), indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
                "source_sha256": payload["source_sha256"],
                "l4_rows": len(l4_rows),
                "l2_rows": len(l2_rows),
                "tail_coefficients": len(box_coefficients),
                "tail_minimum": f"{tail_minimum.numerator}/{tail_minimum.denominator}",
                "failure_count": 0,
                "elapsed_seconds": time.time() - started,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
