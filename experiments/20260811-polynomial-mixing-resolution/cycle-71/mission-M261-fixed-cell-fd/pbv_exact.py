#!/usr/bin/env python3
"""Exact finite audit of M261's phase-boundary observable.

The program enumerates only the first two ordered factors of the balanced
source residuals.  It retains source channel J=0,1,2 and intermediate kind
triangle/double.  It computes the endpoint observable from the literal
generic-edge intervals, then compares its adjacent-phase reconstruction with
frozen M161 scores only after the clean calculation.

Finite output is falsification/calibration evidence, never an asymptotic FD
or sign theorem.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
import sys
import time
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path


Perm = tuple[int, ...]


def mul(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inv(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def cyc(n: int, entries: tuple[int, ...]) -> Perm:
    out = list(range(n))
    if len(entries) > 1:
        for x, y in zip(entries, entries[1:] + entries[:1]):
            out[x] = y
    return tuple(out)


def tr(n: int, x: int, y: int) -> Perm:
    return cyc(n, (x, y))


def cycles(p: Perm) -> list[tuple[int, ...]]:
    seen: set[int] = set()
    out: list[tuple[int, ...]] = []
    for start in range(len(p)):
        if start in seen:
            continue
        c: list[int] = []
        x = start
        while x not in seen:
            seen.add(x)
            c.append(x)
            x = p[x]
        out.append(tuple(c))
    return out


@lru_cache(maxsize=None)
def completion_sizes(sizes: tuple[int, ...], length: int) -> int:
    if sum(sizes) - len(sizes) != length:
        return 0
    ans = math.factorial(length)
    for d in sizes:
        if d > 1:
            ans = ans * d ** (d - 2) // math.factorial(d - 1)
    return ans


def completion(p: Perm, length: int) -> int:
    return completion_sizes(tuple(sorted(map(len, cycles(p)))), length)


def internal_edges(n: int, component: tuple[int, ...]):
    for x, y in combinations(sorted(component), 2):
        yield tr(n, x, y)


def tau_ratio_1(d: int) -> Fraction:
    """tau(d-1)/tau(d), with an invalid shift set to zero."""
    if d < 2:
        return Fraction(0)
    return Fraction(d - 1, d) ** (d - 2)


def tau_ratio_2(d: int) -> Fraction:
    """tau(d-2)/tau(d), with an invalid shift set to zero."""
    if d < 3:
        return Fraction(0)
    return Fraction(d - 1, d) * Fraction(d - 2, d) ** (d - 3)


def endpoint_vector(n: int, h: Perm, s: Perm) -> tuple[Fraction, ...]:
    """Return E_ell(s) for ell=2,...,n-3."""
    q = mul(inv(s), h)
    cs = cycles(q)
    assert len(cs) == 3
    owner = {x: i for i, c in enumerate(cs) for x in c}
    sizes = [len(c) for c in cs]
    chi = [[0] * n for _ in cs]
    generic_owner = [-1] * n
    for r in range(n):
        if s[(r + 1) % n] == (r + 1) % n:
            i = owner[r]
            chi[i][r] = 1
            generic_owner[r] = i

    kappa = [[Fraction(0) for _ in cs] for _ in cs]
    for i in range(3):
        kappa[i][i] = tau_ratio_2(sizes[i])
        for j in range(3):
            if i != j:
                kappa[i][j] = tau_ratio_1(sizes[i]) * tau_ratio_1(sizes[j])

    values: list[Fraction] = []
    for ell in range(2, n - 2):
        value = Fraction(0)
        for j in range(3):
            for x in range(n):
                jump = chi[j][(x + 1) % n] - chi[j][x]
                if not jump:
                    continue
                i = generic_owner[(x - ell) % n]
                if i >= 0:
                    value += kappa[i][j] * jump
        assert abs(value) <= 8
        values.append(value)
    return tuple(values)


def collision_delta_vector(n: int, s: Perm) -> tuple[Fraction, ...]:
    """Return I_(ell+1)(s)-I_ell(s) for ell=2,...,n-3."""
    bad = [int(s[(r + 1) % n] != (r + 1) % n) for r in range(n)]
    profile = [
        sum(bad[r] * bad[(r + ell) % n] for r in range(n))
        for ell in range(2, n - 1)
    ]
    return tuple(Fraction(profile[i + 1] - profile[i]) for i in range(n - 4))


def source_expectation(
    k: int, label: str
) -> tuple[
    dict[tuple[int, str], tuple[Fraction, ...]],
    dict[tuple[int, str], tuple[Fraction, ...]],
    dict[tuple[int, str], Fraction],
    int,
]:
    n = 3 * k
    h = cyc(n, tuple(range(n)))
    if label == "A":
        source = cyc(n, (0, k, 2 * k))
    elif label == "B":
        source = mul(tr(n, 0, 1), tr(n, k, 2 * k))
    else:
        raise ValueError(label)

    residual = mul(inv(source), h)
    initial = cycles(residual)
    middle_index = next(i for i, c in enumerate(initial) if k in c)
    component_of = {x: i for i, c in enumerate(initial) for x in c}
    rank = n - len(initial)
    denominator = completion(residual, rank)
    length = n - 4
    ans_lists: dict[tuple[int, str], list[Fraction]] = defaultdict(
        lambda: [Fraction(0) for _ in range(length)]
    )
    collision_lists: dict[tuple[int, str], list[Fraction]] = defaultdict(
        lambda: [Fraction(0) for _ in range(length)]
    )
    masses: dict[tuple[int, str], Fraction] = defaultdict(Fraction)
    response_cache: dict[Perm, tuple[Fraction, ...]] = {}
    collision_cache: dict[Perm, tuple[Fraction, ...]] = {}
    kind_cache: dict[Perm, str] = {}
    mass = Fraction(0)

    for first_component, c in enumerate(initial):
        if len(c) == 1:
            continue
        first_exterior = first_component != middle_index
        for first in internal_edges(n, c):
            after_first = mul(first, residual)
            for c2 in cycles(after_first):
                if len(c2) == 1:
                    continue
                original = component_of[c2[0]]
                assert all(component_of[x] == original for x in c2)
                second_exterior = original != middle_index
                for second in internal_edges(n, c2):
                    s = mul(first, second)
                    numerator = completion(mul(inv(s), residual), rank - 2)
                    if not numerator:
                        continue
                    probability = Fraction(numerator, denominator)
                    support = sum(x != s[x] for x in range(n))
                    kind = "T" if support == 3 else "D"
                    assert support in (3, 4)
                    channel = int(first_exterior) + int(second_exterior)
                    if s not in response_cache:
                        response_cache[s] = endpoint_vector(n, h, s)
                        collision_cache[s] = collision_delta_vector(n, s)
                        kind_cache[s] = kind
                    assert kind_cache[s] == kind
                    row = ans_lists[(channel, kind)]
                    for index, value in enumerate(response_cache[s]):
                        row[index] += probability * value
                    collision_row = collision_lists[(channel, kind)]
                    for index, value in enumerate(collision_cache[s]):
                        collision_row[index] += probability * value
                    masses[(channel, kind)] += probability
                    mass += probability
    assert mass == 1
    return (
        {key: tuple(value) for key, value in ans_lists.items()},
        {key: tuple(value) for key, value in collision_lists.items()},
        dict(masses),
        len(response_cache),
    )


def qstr(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def vector_add(rows: list[tuple[Fraction, ...]], length: int) -> tuple[Fraction, ...]:
    return tuple(sum((row[i] for row in rows), Fraction(0)) for i in range(length))


def vector_sub(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...], length: int
) -> tuple[Fraction, ...]:
    return tuple(left[i] - right[i] for i in range(length))


def summarize_vector(row: tuple[Fraction, ...]) -> dict[str, object]:
    return {
        "signed_sum_exact": qstr(sum(row, Fraction(0))),
        "absolute_sum_exact": qstr(sum((abs(x) for x in row), Fraction(0))),
        "absolute_sum_float": float(sum((abs(x) for x in row), Fraction(0))),
        "maximum_absolute_float": float(max(map(abs, row), default=Fraction(0))),
    }


def analyze(k: int, frozen_rows: list[dict[str, object]]) -> dict[str, object]:
    if k < 3 or k > 7 or k % 2 == 0:
        raise ValueError("exact audit is capped at odd 3<=k<=7")
    started = time.monotonic()
    n = 3 * k
    length = n - 4
    a, a_collision, amass, acount = source_expectation(k, "A")
    b, b_collision, bmass, bcount = source_expectation(k, "B")
    zero = tuple(Fraction(0) for _ in range(length))
    keys = [(j, kind) for j in range(3) for kind in ("T", "D")]
    pieces = {
        key: vector_sub(b.get(key, zero), a.get(key, zero), length) for key in keys
    }
    collision_pieces = {
        key: vector_sub(
            b_collision.get(key, zero), a_collision.get(key, zero), length
        )
        for key in keys
    }
    assert all(value == 0 for kind in ("T", "D") for value in pieces[(0, kind)])
    combined = vector_add([pieces[key] for key in keys], length)
    combined_collision = vector_add([collision_pieces[key] for key in keys], length)
    decorated_remainder = tuple(
        math.exp(2) * float(combined[i]) - float(combined_collision[i])
        for i in range(length)
    )

    h = cyc(n, tuple(range(n)))
    target = mul(tr(n, 0, 1), tr(n, 2, 3))
    f_t = completion(mul(inv(target), h), n - 3)
    lambda_n = Fraction(n ** (n - 2), n * f_t)
    r_n = (n - 3) * (n - 4)
    z_differences = tuple(Fraction(lambda_n, r_n) * x for x in combined)

    frozen_scores = tuple(Fraction(str(row["score_exact"])) for row in frozen_rows)
    frozen_differences = tuple(
        frozen_scores[i + 1] - frozen_scores[i]
        for i in range(len(frozen_scores) - 1)
    )
    assert z_differences == frozen_differences

    signed_masses = {
        key: bmass.get(key, Fraction(0)) - amass.get(key, Fraction(0))
        for key in keys
    }
    assert all(signed_masses[(0, kind)] == 0 for kind in ("T", "D"))
    assert all(signed_masses[(1, kind)] == 0 for kind in ("T", "D"))

    positive = sum((max(x, Fraction(0)) for x in frozen_scores), Fraction(0))
    negative = sum((max(-x, Fraction(0)) for x in frozen_scores), Fraction(0))
    fd_value = k * k * sum((abs(x) for x in z_differences), Fraction(0))

    phase_rows = []
    for index, combined_value in enumerate(combined):
        phase_rows.append({
            "ell": index + 2,
            "combined_eta_endpoint_exact": qstr(combined_value),
            "z_difference_exact": qstr(z_differences[index]),
            "combined_collision_delta_exact": qstr(combined_collision[index]),
            "combined_decorated_delta_float": decorated_remainder[index],
            "by_channel_kind": {
                f"J{j}_{kind}": qstr(pieces[(j, kind)][index])
                for j, kind in keys
            },
        })

    channel_kind = {
        f"J{j}_{kind}": {
            **summarize_vector(pieces[(j, kind)]),
            "A_mass_exact": qstr(amass.get((j, kind), Fraction(0))),
            "B_mass_exact": qstr(bmass.get((j, kind), Fraction(0))),
            "signed_mass_exact": qstr(signed_masses[(j, kind)]),
        }
        for j, kind in keys
    }
    channel_totals = {
        f"J{j}": summarize_vector(
            vector_add([pieces[(j, "T")], pieces[(j, "D")]], length)
        )
        for j in range(3)
    }
    kind_totals = {
        kind: summarize_vector(
            vector_add([pieces[(j, kind)] for j in range(3)], length)
        )
        for kind in ("T", "D")
    }

    return {
        "k": k,
        "n": n,
        "source_accessible_products": {"A": acount, "B": bcount},
        "combined_endpoint": summarize_vector(combined),
        "combined_collision_delta": summarize_vector(combined_collision),
        "n_times_combined_collision_l1": float(
            n * sum((abs(x) for x in combined_collision), Fraction(0))
        ),
        "combined_decorated_delta_l1_float": sum(map(abs, decorated_remainder)),
        "n_times_combined_decorated_delta_l1_float": n
        * sum(map(abs, decorated_remainder)),
        "n_times_combined_endpoint_l1": float(
            n * sum((abs(x) for x in combined), Fraction(0))
        ),
        "fd_k_squared_variation_exact": qstr(fd_value),
        "fd_k_squared_variation_float": float(fd_value),
        "minority_sign": {
            "positive_mass_exact": qstr(positive),
            "negative_mass_exact": qstr(negative),
            "k_times_minority_exact": qstr(k * min(positive, negative)),
        },
        "channel_kind": channel_kind,
        "channel_totals": channel_totals,
        "kind_totals": kind_totals,
        "phase_rows": phase_rows,
        "frozen_adjacent_scores_exact_match": True,
        "runtime_seconds": time.monotonic() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", nargs="+", type=int, required=True)
    parser.add_argument("--frozen-m161", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    frozen = json.loads(args.frozen_m161.read_text())
    frozen_by_k = {int(row["k"]): row["rows"] for row in frozen["results"]}
    results = [analyze(k, frozen_by_k[k]) for k in args.k]
    payload = {
        "status": "exact finite PBV falsification only; no asymptotic or sign inference",
        "target": "M161/M168 balanced first fixed cell under M73 nonlazy cyclic rank-two kernel",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
        "results": results,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps([
        {
            "k": row["k"],
            "n_times_combined_endpoint_l1": row["n_times_combined_endpoint_l1"],
            "fd_k_squared_variation": row["fd_k_squared_variation_float"],
            "k_times_minority": row["minority_sign"]["k_times_minority_exact"],
            "runtime_seconds": row["runtime_seconds"],
        }
        for row in results
    ], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
