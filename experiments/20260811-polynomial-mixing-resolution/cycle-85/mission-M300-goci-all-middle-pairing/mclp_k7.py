#!/usr/bin/env python3
"""Exact sole-rank falsifier for M300's pre-frozen MCLP_1 candidate.

This script imports no predecessor code or data.  It reconstructs the
channel-one exterior signed law, the middle chord law, and the literal and
repaired owner responses at exactly k=7.
"""

from __future__ import annotations

import json
import math
import platform
import subprocess
import sys
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path


Perm = tuple[int, ...]
Edge = tuple[int, int]


def mul(p: Perm, q: Perm) -> Perm:
    """Return pq, so (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inv(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def cyc(n: int, vertices: tuple[int, ...]) -> Perm:
    out = list(range(n))
    for x, y in zip(vertices, vertices[1:] + vertices[:1]):
        out[x] = y
    return tuple(out)


def tr(n: int, e: Edge) -> Perm:
    return cyc(n, e)


def cycles(p: Perm) -> tuple[tuple[int, ...], ...]:
    seen: set[int] = set()
    answer: list[tuple[int, ...]] = []
    for root in range(len(p)):
        if root in seen:
            continue
        component: list[int] = []
        x = root
        while x not in seen:
            seen.add(x)
            component.append(x)
            x = p[x]
        answer.append(tuple(component))
    return tuple(answer)


def edge(x: int, y: int) -> Edge:
    return (x, y) if x < y else (y, x)


@lru_cache(maxsize=None)
def tau(d: int) -> Fraction:
    if d < 1:
        return Fraction(0)
    if d == 1:
        return Fraction(1)
    return Fraction(d ** (d - 2), math.factorial(d - 1))


def chord_law(component: tuple[int, ...]) -> dict[Edge, Fraction]:
    """Exact first-factor chord law on one directed cycle."""
    d = len(component)
    pos = {x: i for i, x in enumerate(component)}
    law: dict[Edge, Fraction] = {}
    for x, y in combinations(component, 2):
        u = (pos[y] - pos[x]) % d
        law[edge(x, y)] = tau(u) * tau(d - u) / ((d - 1) * tau(d))
    assert sum(law.values(), Fraction(0)) == 1
    return law


def owner_responses(n: int, h: Perm, exterior: Edge, middle: Edge):
    """Return literal and repaired F_ell for all circular lags."""
    assert set(exterior).isdisjoint(middle)
    s = mul(tr(n, exterior), tr(n, middle))
    residual = mul(inv(s), h)
    components = cycles(residual)
    assert len(components) == 3
    owner = {
        vertex: owner_id
        for owner_id, component in enumerate(components)
        for vertex in component
    }
    sizes = tuple(len(component) for component in components)

    generic: list[int | None] = []
    for r in range(n):
        head = (r + 1) % n
        generic.append(owner[r] if s[head] == head else None)

    a = [
        tau(d - 1) / tau(d) if d >= 2 else Fraction(0)
        for d in sizes
    ]
    b = [
        tau(d - 2) / tau(d) if d >= 3 else Fraction(0)
        for d in sizes
    ]
    delta = [b[i] - a[i] * a[i] for i in range(3)]
    field = [a[o] if o is not None else Fraction(0) for o in generic]

    literal: list[Fraction] = []
    repaired: list[Fraction] = []
    for ell in range(n):
        direct = Fraction(0)
        rank_one = sum(
            (field[r] * field[(r + ell) % n] for r in range(n)),
            Fraction(0),
        )
        correction = Fraction(0)
        for r in range(n):
            i = generic[r]
            j = generic[(r + ell) % n]
            if i is None or j is None:
                continue
            direct += b[i] if i == j else a[i] * a[j]
        for i, d in enumerate(sizes):
            if d < 3:
                continue
            overlap = sum(
                generic[r] == i and generic[(r + ell) % n] == i
                for r in range(n)
            )
            correction += delta[i] * overlap
        literal.append(direct)
        repaired.append(rank_one + correction)

    assert all(literal[ell] == repaired[ell] for ell in range(2, n - 1))
    assert all(literal[ell] == literal[n - ell] for ell in range(1, n))
    assert all(value >= 0 for value in repaired)
    return tuple(literal), tuple(repaired), sizes


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def main() -> None:
    if len(sys.argv) != 3 or sys.argv[1] != "--output":
        raise SystemExit("usage: mclp_k7.py --output PATH")
    output = Path(sys.argv[2])

    k = 7
    n = 3 * k
    h = cyc(n, tuple(range(n)))
    c_minus = tuple(range(0, k))
    middle = tuple(range(k, 2 * k))
    c_plus = tuple(range(2 * k, 3 * k))
    merged = tuple(range(1, k)) + c_plus

    law_minus = chord_law(c_minus)
    law_middle = chord_law(middle)
    law_plus = chord_law(c_plus)
    law_merged = chord_law(merged)
    exterior_edges = sorted(set(law_minus) | set(law_plus) | set(law_merged))
    gamma = {
        e: law_merged.get(e, Fraction(0))
        - Fraction(1, 2) * law_minus.get(e, Fraction(0))
        - Fraction(1, 2) * law_plus.get(e, Fraction(0))
        for e in exterior_edges
    }
    assert sum(gamma.values(), Fraction(0)) == 0
    assert any(value > 0 for value in gamma.values())
    assert any(value < 0 for value in gamma.values())

    phase_chord: dict[tuple[int, int], Edge] = {}
    chord_class: dict[Edge, tuple[int, int]] = {}
    class_weight: dict[int, Fraction] = {}
    for u in range(1, (k + 1) // 2):
        expected = tau(u) * tau(k - u) / ((k - 1) * tau(k))
        class_weight[u] = expected
        for phase in range(k):
            f = edge(middle[phase], middle[(phase + u) % k])
            assert f not in chord_class
            phase_chord[(u, phase)] = f
            chord_class[f] = (u, phase)
            assert law_middle[f] == expected
    assert set(chord_class) == set(law_middle)
    assert sum(k * weight for weight in class_weight.values()) == 1

    responses = {
        (e, f): owner_responses(n, h, e, f)
        for e in exterior_edges
        for f in sorted(law_middle)
    }

    phase_cells: list[dict[str, object]] = []
    class_cells: list[dict[str, object]] = []
    full_lag_totals: dict[int, Fraction] = {}
    class_totals: dict[tuple[int, int], Fraction] = {}
    for ell in range(2, n - 1):
        full = Fraction(0)
        for u in sorted(class_weight):
            orbit_total = Fraction(0)
            for phase in range(k):
                f = phase_chord[(u, phase)]
                fixed = sum(
                    (gamma[e] * responses[(e, f)][0][ell] for e in exterior_edges),
                    Fraction(0),
                )
                orbit_total += fixed
                full += class_weight[u] * fixed
                phase_cells.append(
                    {
                        "ell": ell,
                        "u": u,
                        "phase": phase,
                        "middle_edge": list(f),
                        "fixed_middle_value": qstr(fixed),
                        "fixed_middle_value_float": float(fixed),
                        "sign": "negative" if fixed < 0 else "positive" if fixed > 0 else "zero",
                    }
                )
            class_totals[(u, ell)] = orbit_total
            class_cells.append(
                {
                    "ell": ell,
                    "u": u,
                    "per_chord_weight": qstr(class_weight[u]),
                    "phase_orbit_total": qstr(orbit_total),
                    "phase_orbit_total_float": float(orbit_total),
                    "weighted_contribution": qstr(class_weight[u] * orbit_total),
                    "sign": "negative" if orbit_total < 0 else "positive" if orbit_total > 0 else "zero",
                }
            )
        direct_full = sum(
            law_middle[f]
            * sum(
                (gamma[e] * responses[(e, f)][0][ell] for e in exterior_edges),
                Fraction(0),
            )
            for f in law_middle
        )
        assert full == direct_full
        full_lag_totals[ell] = full

    assert all(
        class_totals[(u, ell)] == class_totals[(u, n - ell)]
        for u in class_weight
        for ell in range(2, n - 1)
    )
    assert all(
        full_lag_totals[ell] == full_lag_totals[n - ell]
        for ell in full_lag_totals
    )

    negative_classes = [row for row in class_cells if row["sign"] == "negative"]
    first_negative = negative_classes[0] if negative_classes else None
    minimum_class = min(
        class_cells,
        key=lambda row: Fraction(str(row["phase_orbit_total"])),
    )
    negative_phases = [row for row in phase_cells if row["sign"] == "negative"]

    alpha_1 = Fraction(4 * (k - 1) ** 2, (3 * k - 3) * (3 * k - 4))
    lambda_n = Fraction(n - 2) * Fraction(n, n - 2) ** (n - 3)
    r_n = (n - 3) * (n - 4)
    weighted_cp = {
        ell: alpha_1 * lambda_n * value / r_n
        for ell, value in full_lag_totals.items()
    }

    payload = {
        "status": "exact sole-rank test of pre-frozen MCLP_1; GOCI_1 remains logically separate",
        "candidate": "MCLP_1: each complete middle cut-length phase orbit has nonnegative signed exterior response",
        "scope": "exactly k=7, n=21; all admissible lags and all three middle cut-length classes; no rank scan",
        "convention": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "imports_predecessor_code_or_data": False,
        "command": "python3 mclp_k7.py --output mclp_k7.json",
        "k": k,
        "n": n,
        "admissible_lags": list(range(2, n - 1)),
        "cut_lengths": sorted(class_weight),
        "middle_chords": len(law_middle),
        "exterior_chords": len(exterior_edges),
        "gamma_mass": qstr(sum(gamma.values(), Fraction(0))),
        "gamma_sign_counts": {
            "positive": sum(value > 0 for value in gamma.values()),
            "negative": sum(value < 0 for value in gamma.values()),
            "zero": sum(value == 0 for value in gamma.values()),
        },
        "middle_class_weights": {
            str(u): qstr(weight) for u, weight in class_weight.items()
        },
        "middle_class_mass_check": qstr(
            sum(k * weight for weight in class_weight.values())
        ),
        "literal_equals_repaired_on_admissible_lags": True,
        "statewise_lag_reflection_exact": True,
        "classwise_lag_reflection_exact": True,
        "class_cells_tested": len(class_cells),
        "negative_class_cells": len(negative_classes),
        "mclp_survives_k7": not negative_classes,
        "first_negative_class": first_negative,
        "minimum_class": minimum_class,
        "fixed_middle_cells_tested": len(phase_cells),
        "negative_fixed_middle_cells": len(negative_phases),
        "class_cells": class_cells,
        "phase_cells": phase_cells,
        "channel_one_eta_lag_totals": {
            str(ell): qstr(value) for ell, value in full_lag_totals.items()
        },
        "all_full_eta_lags_positive": all(value > 0 for value in full_lag_totals.values()),
        "alpha_1": qstr(alpha_1),
        "Lambda_n": qstr(lambda_n),
        "R_n": r_n,
        "weighted_channel_one_cp": {
            str(ell): qstr(value) for ell, value in weighted_cp.items()
        },
        "minimum_weighted_channel_one_cp": qstr(min(weighted_cp.values())),
        "goci_counterexample": any(value < 0 for value in full_lag_totals.values()),
        "downstream_inference": False,
    }
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "k": k,
                "negative_class_cells": len(negative_classes),
                "first_negative_class": first_negative,
                "minimum_class": minimum_class,
                "negative_fixed_middle_cells": len(negative_phases),
                "all_full_eta_lags_positive": payload["all_full_eta_lags_positive"],
                "goci_counterexample": payload["goci_counterexample"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
