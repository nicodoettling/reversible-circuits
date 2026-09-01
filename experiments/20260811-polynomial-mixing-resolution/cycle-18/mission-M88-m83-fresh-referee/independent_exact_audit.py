#!/usr/bin/env python3
"""Independent exact audit of M83's balanced far-singleton theorem.

This file intentionally imports no M83 or M73 implementation.  It enumerates
all admissible rank-two products for k=3,5 and computes the two raw kernel rows
over Fraction.  The cyclic quotient event is represented by its full raw
union, as required by the quotient-kernel definition.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path


Perm = tuple[int, ...]
Edge = tuple[int, int]


def mul(p: Perm, q: Perm) -> Perm:
    """Return pq, with (pq)(x)=p(q(x))."""

    return tuple(p[q[x]] for x in range(len(p)))


def inv(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def transposition(n: int, x: int, y: int) -> Perm:
    out = list(range(n))
    out[x], out[y] = out[y], out[x]
    return tuple(out)


def cycle(n: int, entries: tuple[int, ...]) -> Perm:
    out = list(range(n))
    for x, y in zip(entries, entries[1:] + entries[:1]):
        out[x] = y
    return tuple(out)


def cycle_sizes(p: Perm) -> tuple[int, ...]:
    seen: set[int] = set()
    answer: list[int] = []
    for start in range(len(p)):
        if start in seen:
            continue
        x = start
        size = 0
        while x not in seen:
            seen.add(x)
            size += 1
            x = p[x]
        answer.append(size)
    return tuple(sorted(answer))


def transposition_rank(p: Perm) -> int:
    return len(p) - len(cycle_sizes(p))


def minimal_count(p: Perm, length: int) -> int:
    """Dénes/interleaving count F_length(p), including fixed cycles."""

    sizes = cycle_sizes(p)
    if len(p) - len(sizes) != length:
        return 0
    answer = math.factorial(length)
    for d in sizes:
        if d > 1:
            answer = answer * d ** (d - 2) // math.factorial(d - 1)
    return answer


def all_transpositions(n: int) -> list[tuple[Edge, Perm]]:
    return [
        ((x, y), transposition(n, x, y))
        for x in range(n)
        for y in range(x + 1, n)
    ]


def rank_two_states(
    n: int, h: Perm
) -> tuple[dict[Perm, int], dict[Perm, tuple[tuple[Edge, Edge], ...]]]:
    """Enumerate X and independently count every ordered two-factor lift."""

    lifts: dict[Perm, list[Edge]] = {}
    trans = all_transpositions(n)
    for edge_u, u in trans:
        for edge_v, v in trans:
            g = mul(u, v)
            if transposition_rank(g) != 2:
                continue
            if minimal_count(mul(inv(g), h), n - 3) == 0:
                continue
            lifts.setdefault(g, []).append((edge_u, edge_v))
    counts = {g: len(value) for g, value in lifts.items()}
    # The second return is used only for an auditable micro-lift count.
    return counts, {g: tuple(value) for g, value in lifts.items()}


def theta(h: Perm, g: Perm) -> Perm:
    return mul(mul(inv(h), g), h)


def row_entry(n: int, h: Perm, lifts: dict[Perm, int], g: Perm, s: Perm) -> Fraction:
    denominator = minimal_count(mul(inv(g), h), n - 3)
    residual = mul(inv(mul(g, s)), h)
    return Fraction(lifts[s] * minimal_count(residual, n - 5), denominator)


def is_far_singleton(n: int, k: int, h: Perm, s: Perm) -> bool:
    sizes = cycle_sizes(mul(inv(s), h))
    return len(sizes) == 3 and sizes[0] == 1 and sizes[1] >= k


def tau(d: int) -> Fraction:
    return Fraction(d ** (d - 1), math.factorial(d))


def w(d: int, s: int) -> Fraction:
    return (
        Fraction(math.factorial(d - 2), d ** (d - 2))
        * tau(s)
        * tau(d - s)
    )


def closed_probability(k: int) -> Fraction:
    d = 2 * k - 1
    cross_color = Fraction(
        2 * (2 * k - 2) * (k - 1),
        (3 * k - 3) * (3 * k - 4),
    )
    middle = (k - 1) * w(k, 1)
    long = sum((s * w(d, s) for s in range(1, k - 1)), Fraction(0))
    long += 2 * (k - 1) * w(d, k - 1)
    return cross_color * middle * long


def selected_targets(n: int, k: int) -> tuple[set[Perm], Counter[int]]:
    selected: set[Perm] = set()
    split_multiplicity: Counter[int] = Counter()
    long_cycle = tuple(range(1, k)) + tuple(range(2 * k, 3 * k))
    position = {x: i for i, x in enumerate(long_cycle)}
    d = len(long_cycle)
    for i in range(1, k):
        for j in range(2 * k, 3 * k):
            if not (k + 1 <= j - i <= 2 * k):
                continue
            distance = (position[j] - position[i]) % d
            split_multiplicity[min(distance, d - distance)] += 1
            e = transposition(n, i, j)
            for m in range(k, 2 * k - 1):
                f = transposition(n, m, m + 1)
                selected.add(mul(e, f))
    return selected, split_multiplicity


def log_w(d: int, s: int) -> float:
    def log_tau(x: int) -> float:
        return (x - 1) * math.log(x) - math.lgamma(x + 1)

    return (
        math.lgamma(d - 1)
        - (d - 2) * math.log(d)
        + log_tau(s)
        + log_tau(d - s)
    )


def asymptotic_probability(k: int) -> float:
    d = 2 * k - 1
    cross_color = (
        2.0 * (2 * k - 2) * (k - 1) / ((3 * k - 3) * (3 * k - 4))
    )
    middle = (k - 1) * math.exp(log_w(k, 1))
    long = sum(s * math.exp(log_w(d, s)) for s in range(1, k - 1))
    long += 2 * (k - 1) * math.exp(log_w(d, k - 1))
    return cross_color * middle * long


def orbit(h: Perm, s: Perm) -> tuple[Perm, ...]:
    answer: list[Perm] = []
    current = s
    while current not in answer:
        answer.append(current)
        current = theta(h, current)
    return tuple(answer)


def analyze(k: int) -> dict[str, object]:
    if k < 3 or k % 2 == 0:
        raise ValueError("k must be odd and at least 3")
    n = 3 * k
    h = cycle(n, tuple(range(n)))
    a_source = cycle(n, (0, k, 2 * k))
    common = transposition(n, k, 2 * k)
    a_other = transposition(n, 2 * k, 0)
    b_other = transposition(n, 0, 1)
    b_source = mul(common, b_other)
    adjacency_checks = {
        "A_equals_lift_product": a_source == mul(common, a_other),
        "B_equals_lift_product": b_source == mul(common, b_other),
        "differing_chords_share_exact_endpoint_0": (
            set((2 * k, 0)) & set((0, 1)) == {0}
        ),
    }

    lifts, micro_lifts = rank_two_states(n, h)
    if a_source not in lifts or b_source not in lifts:
        raise AssertionError("balanced sources not in rank-two support")
    event = {s for s in lifts if is_far_singleton(n, k, h, s)}
    event_invariant = all(is_far_singleton(n, k, h, theta(h, s)) for s in event)

    row_a = {s: row_entry(n, h, lifts, a_source, s) for s in lifts}
    row_b = {s: row_entry(n, h, lifts, b_source, s) for s in lifts}
    selected, split_counts = selected_targets(n, k)
    formula = closed_probability(k)
    expected_splits = Counter({s: s for s in range(1, k - 1)})
    expected_splits[k - 1] = 2 * (k - 1)
    expected_selected = (k - 1) ** 2 * (k + 2) // 2

    # This checks the Borel identity with exponentials cancelled algebraically.
    borel_checks = []
    for d in (k, 2 * k - 1):
        all_entries = []
        for s in range(1, d):
            rhs_without_exp = tau(s) * tau(d - s) / (
                (1 - Fraction(1, d)) * tau(d)
            )
            all_entries.append(d * w(d, s) == rhs_without_exp)
        smaller_mass = sum(
            (d * w(d, s) for s in range(1, (d - 1) // 2 + 1)),
            Fraction(0),
        )
        borel_checks.append(
            {
                "d": d,
                "identity_all_s": all(all_entries),
                "odd_smaller_fragment_mass": str(smaller_mass),
            }
        )

    selected_probability_a = sum((row_a[s] for s in selected), Fraction(0))
    selected_probability_b = sum((row_b[s] for s in selected), Fraction(0))
    full_event_a = sum((row_a[s] for s in event), Fraction(0))
    full_event_b = sum((row_b[s] for s in event), Fraction(0))
    selected_orbits = {min(orbit(h, s)) for s in selected}

    return {
        "k": k,
        "n": n,
        "rank_two_support": len(lifts),
        "source_micro_lifts": {
            "A": lifts[a_source],
            "B": lifts[b_source],
        },
        "source_residual_cycle_sizes": {
            "A": cycle_sizes(mul(inv(a_source), h)),
            "B": cycle_sizes(mul(inv(b_source), h)),
        },
        "adjacency_checks": adjacency_checks,
        "row_normalization": {
            "A": str(sum(row_a.values(), Fraction(0))),
            "B": str(sum(row_b.values(), Fraction(0))),
        },
        "far_singleton_event": {
            "raw_target_count": len(event),
            "theta_invariant": event_invariant,
            "A_probability": str(full_event_a),
            "B_probability": str(full_event_b),
        },
        "selected_cross_schema": {
            "raw_target_count": len(selected),
            "expected_raw_target_count": expected_selected,
            "selected_targets_are_supported": selected <= lifts.keys(),
            "selected_targets_lie_in_event": selected <= event,
            "distinct_cyclic_orbits_met": len(selected_orbits),
            "A_probability": str(selected_probability_a),
            "B_probability": str(selected_probability_b),
            "closed_probability": str(formula),
            "formula_equals_B_probability": formula == selected_probability_b,
            "split_multiplicity": dict(sorted(split_counts.items())),
            "expected_split_multiplicity": dict(sorted(expected_splits.items())),
            "multiplicity_matches": split_counts == expected_splits,
            "each_target_has_two_micro_lifts": all(lifts[s] == 2 for s in selected),
            "no_duplicate_raw_targets": len(selected) == expected_selected,
        },
        "borel_checks": borel_checks,
        "explicit_bound_numeric": {
            "p": float(formula),
            "lower": 2 / (27 * math.e**2 * math.sqrt(k)),
            "holds": float(formula) >= 2 / (27 * math.e**2 * math.sqrt(k)),
        },
        "micro_lift_storage_check": all(len(micro_lifts[g]) == lifts[g] for g in lifts),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", nargs="+", type=int, default=[3, 5])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    asymptotic_ks = [11, 101, 1001, 10001]
    target_constant = 4 / (9 * math.e * math.sqrt(math.pi))
    payload = {
        "status": "exact finite audit plus floating asymptotic calibration",
        "claim": "M83 balanced far-singleton one-step lower bound",
        "scope": (
            "Exact Fraction enumeration is used for k requested on the command "
            "line.  Large-k values only calibrate the separately proved limit."
        ),
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "target": (
            "uniform minimal length-(n-1) bridge to the odd long cycle, "
            "rank-two product coordinate, cyclic quotient"
        ),
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
        "exact_results": [analyze(k) for k in args.k],
        "asymptotic_calibration": {
            "target_sqrt_k_p": target_constant,
            "values": [
                {
                    "k": k,
                    "sqrt_k_p": math.sqrt(k) * asymptotic_probability(k),
                }
                for k in asymptotic_ks
            ],
        },
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
