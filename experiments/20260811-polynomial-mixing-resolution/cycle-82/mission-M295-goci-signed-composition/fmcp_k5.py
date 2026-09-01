#!/usr/bin/env python3
"""Exact one-rank falsifier for M295's pre-frozen FMCP_1 candidate.

The calculation uses only the accepted closed formulas for the channel-one
exterior signed coefficient and the literal/repaired owner response.  It
imports no predecessor code or data and tests exactly k=5.
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


def tr(n: int, edge: Edge) -> Perm:
    return cyc(n, edge)


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


@lru_cache(maxsize=None)
def tau(d: int) -> Fraction:
    if d < 1:
        return Fraction(0)
    if d == 1:
        return Fraction(1)
    return Fraction(d ** (d - 2), math.factorial(d - 1))


def edge(x: int, y: int) -> Edge:
    return (x, y) if x < y else (y, x)


def chord_law(component: tuple[int, ...]) -> dict[Edge, Fraction]:
    """First-transposition law nu_C on unordered chords of a directed cycle."""
    d = len(component)
    position = {x: i for i, x in enumerate(component)}
    law: dict[Edge, Fraction] = {}
    for x, y in combinations(component, 2):
        u = (position[y] - position[x]) % d
        law[edge(x, y)] = tau(u) * tau(d - u) / ((d - 1) * tau(d))
    assert sum(law.values(), Fraction(0)) == 1
    return law


def owner_response(n: int, h: Perm, exterior: Edge, middle: Edge):
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
    assert all(value >= 0 for value in repaired)
    return tuple(literal), tuple(repaired), sizes


def composition_response(n: int, exterior: Edge, middle: Edge):
    """Reconstruct M285's S/N positive-composition interval response."""
    vertices = tuple(sorted(exterior + middle))
    assert len(set(vertices)) == 4
    gaps = tuple(
        vertices[i + 1] - vertices[i] for i in range(3)
    ) + (n - vertices[3] + vertices[0],)
    pair_set = {frozenset(exterior), frozenset(middle)}
    separated = {
        frozenset((vertices[0], vertices[1])),
        frozenset((vertices[2], vertices[3])),
    }
    nested = {
        frozenset((vertices[0], vertices[3])),
        frozenset((vertices[1], vertices[2])),
    }

    starts = (0, gaps[0], gaps[0] + gaps[1], gaps[0] + gaps[1] + gaps[2])
    intervals = tuple(
        frozenset((starts[i] + offset) % n for offset in range(gaps[i] - 1))
        for i in range(4)
    )
    if pair_set == separated:
        kind = "S"
        owner_sets = (intervals[0], intervals[2], intervals[1] | intervals[3])
        owner_sizes = (gaps[0], gaps[2], gaps[1] + gaps[3])
    elif pair_set == nested:
        kind = "N"
        owner_sets = (intervals[1], intervals[3], intervals[0] | intervals[2])
        owner_sizes = (gaps[1], gaps[3], gaps[0] + gaps[2])
    else:
        raise AssertionError("rank-incompatible crossing double")

    response = []
    for ell in range(n):
        value = Fraction(0)
        for i, owner_i in enumerate(owner_sets):
            for j, owner_j in enumerate(owner_sets):
                if i == j:
                    kappa = (
                        tau(owner_sizes[i] - 2) / tau(owner_sizes[i])
                        if owner_sizes[i] >= 3
                        else Fraction(0)
                    )
                else:
                    kappa = (
                        tau(owner_sizes[i] - 1)
                        * tau(owner_sizes[j] - 1)
                        / (tau(owner_sizes[i]) * tau(owner_sizes[j]))
                        if owner_sizes[i] >= 2 and owner_sizes[j] >= 2
                        else Fraction(0)
                    )
                overlap = sum((x + ell) % n in owner_j for x in owner_i)
                value += kappa * overlap
        response.append(value)
    return tuple(response), kind, gaps, owner_sizes


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def main() -> None:
    if len(sys.argv) != 3 or sys.argv[1] != "--output":
        raise SystemExit("usage: fmcp_k5.py --output PATH")
    output = Path(sys.argv[2])

    k = 5
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

    responses = {
        (e, f): owner_response(n, h, e, f)
        for e in exterior_edges
        for f in sorted(law_middle)
    }
    composition_responses = {
        (e, f): composition_response(n, e, f)
        for e in exterior_edges
        for f in sorted(law_middle)
    }
    assert all(
        responses[(e, f)][0] == composition_responses[(e, f)][0]
        for e in exterior_edges
        for f in law_middle
    )

    cells: list[dict[str, object]] = []
    lag_totals: dict[int, Fraction] = {}
    for ell in range(2, n - 1):
        lag_total = Fraction(0)
        for f, middle_weight in sorted(law_middle.items()):
            value = sum(
                (gamma[e] * responses[(e, f)][0][ell] for e in exterior_edges),
                Fraction(0),
            )
            lag_total += middle_weight * value
            cells.append(
                {
                    "ell": ell,
                    "middle_edge": list(f),
                    "middle_weight": qstr(middle_weight),
                    "fmcp_value": qstr(value),
                    "fmcp_value_float": float(value),
                    "sign": "negative" if value < 0 else "positive" if value > 0 else "zero",
                }
            )
        lag_totals[ell] = lag_total

    assert all(lag_totals[ell] == lag_totals[n - ell] for ell in lag_totals)
    assert all(
        Fraction(str(cell["fmcp_value"]))
        == next(
            Fraction(str(other["fmcp_value"]))
            for other in cells
            if other["ell"] == n - cell["ell"]
            and other["middle_edge"] == cell["middle_edge"]
        )
        for cell in cells
    )

    alpha_1 = Fraction(4 * (k - 1) ** 2, (3 * k - 3) * (3 * k - 4))
    lambda_n = Fraction(n - 2) * Fraction(n, n - 2) ** (n - 3)
    r_n = (n - 3) * (n - 4)
    weighted_cp = {
        ell: alpha_1 * lambda_n * value / r_n
        for ell, value in lag_totals.items()
    }

    negative = [cell for cell in cells if cell["sign"] == "negative"]
    minimum = min(cells, key=lambda cell: Fraction(str(cell["fmcp_value"])))
    minimum_value = Fraction(str(minimum["fmcp_value"]))
    witness_f = tuple(minimum["middle_edge"])
    witness_ell = int(minimum["ell"])

    contributions = []
    for e in exterior_edges:
        term = gamma[e] * responses[(e, witness_f)][0][witness_ell]
        if term:
            contributions.append(
                {
                    "exterior_edge": list(e),
                    "gamma": qstr(gamma[e]),
                    "response": qstr(responses[(e, witness_f)][0][witness_ell]),
                    "term": qstr(term),
                    "term_float": float(term),
                }
            )
    assert sum((Fraction(row["term"]) for row in contributions), Fraction(0)) == minimum_value

    payload = {
        "status": "exact one-rank test of pre-frozen FMCP_1; GOCI_1 remains separate",
        "candidate": "FMCP_1: fixed-middle fully recombined exterior signed sum is nonnegative",
        "scope": "exactly k=5, n=15; all admissible lags and middle chords; no rank scan",
        "convention": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "imports_predecessor_code_or_data": False,
        "command": "python3 fmcp_k5.py --output fmcp_k5.json",
        "k": k,
        "n": n,
        "admissible_lags": list(range(2, n - 1)),
        "middle_chords": len(law_middle),
        "exterior_chords": len(exterior_edges),
        "gamma_mass": qstr(sum(gamma.values(), Fraction(0))),
        "gamma_sign_counts": {
            "positive": sum(value > 0 for value in gamma.values()),
            "negative": sum(value < 0 for value in gamma.values()),
            "zero": sum(value == 0 for value in gamma.values()),
        },
        "literal_equals_repaired_on_admissible_lags": True,
        "direct_equals_positive_composition_all_lags": True,
        "cells_tested": len(cells),
        "negative_cells": len(negative),
        "fmcp_survives_k5": not negative,
        "minimum_cell": minimum,
        "minimum_cell_exact_reconstruction": qstr(minimum_value),
        "minimum_cell_nonzero_contributions": contributions,
        "channel_one_lag_totals": {
            str(ell): qstr(value) for ell, value in lag_totals.items()
        },
        "alpha_1": qstr(alpha_1),
        "Lambda_n": qstr(lambda_n),
        "R_n": r_n,
        "weighted_channel_one_cp": {
            str(ell): qstr(value) for ell, value in weighted_cp.items()
        },
        "minimum_weighted_channel_one_cp": qstr(min(weighted_cp.values())),
        "statewise_and_cellwise_reflection_exact": True,
        "all_channel_one_lag_totals_positive": all(
            value > 0 for value in lag_totals.values()
        ),
        "goci_counterexample": False,
        "downstream_inference": False,
        "cells": cells,
    }
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "k": k,
                "negative_cells": len(negative),
                "minimum_cell": minimum,
                "all_channel_one_lag_totals_positive": payload[
                    "all_channel_one_lag_totals_positive"
                ],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
