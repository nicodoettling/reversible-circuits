#!/usr/bin/env python3
"""Clean-room exact audit of M295's channel-one FMCP_1 claim.

This program deliberately does not import or read any M295 artifact.  It builds
the completion laws, residual-cycle response, repaired autocorrelation, and
cyclic-composition representation directly from their mathematical definitions.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
from collections import Counter
from fractions import Fraction
from functools import cache
from itertools import combinations
from pathlib import Path


Permutation = tuple[int, ...]
Chord = tuple[int, int]


def compose(p: Permutation, q: Permutation) -> Permutation:
    """Composition pq under (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Permutation) -> Permutation:
    ans = [0] * len(p)
    for x, px in enumerate(p):
        ans[px] = x
    return tuple(ans)


def cycle_permutation(n: int, entries: tuple[int, ...]) -> Permutation:
    ans = list(range(n))
    for i, x in enumerate(entries):
        ans[x] = entries[(i + 1) % len(entries)]
    return tuple(ans)


def canonical_chord(x: int, y: int) -> Chord:
    assert x != y
    return (x, y) if x < y else (y, x)


def transposition(n: int, chord: Chord) -> Permutation:
    return cycle_permutation(n, chord)


def cycle_decomposition(p: Permutation) -> tuple[tuple[int, ...], ...]:
    used = [False] * len(p)
    answer: list[tuple[int, ...]] = []
    for start in range(len(p)):
        if used[start]:
            continue
        orbit: list[int] = []
        x = start
        while not used[x]:
            used[x] = True
            orbit.append(x)
            x = p[x]
        answer.append(tuple(orbit))
    return tuple(answer)


def rank(p: Permutation) -> int:
    return len(p) - len(cycle_decomposition(p))


@cache
def tau(d: int) -> Fraction:
    if d <= 0:
        return Fraction(0)
    if d == 1:
        return Fraction(1)
    return Fraction(d ** (d - 2), math.factorial(d - 1))


def completion_count(p: Permutation, required_rank: int) -> Fraction:
    if rank(p) != required_rank:
        return Fraction(0)
    value = Fraction(math.factorial(required_rank))
    for component in cycle_decomposition(p):
        value *= tau(len(component))
    return value


def first_chord_law(cycle: tuple[int, ...]) -> dict[Chord, Fraction]:
    """First factor in a uniform minimal transposition factorization."""
    d = len(cycle)
    law: dict[Chord, Fraction] = {}
    for i, j in combinations(range(d), 2):
        u = j - i
        chord = canonical_chord(cycle[i], cycle[j])
        law[chord] = tau(u) * tau(d - u) / ((d - 1) * tau(d))
    assert sum(law.values(), Fraction()) == 1
    return law


def owner_data(
    n: int, ambient: Permutation, exterior: Chord, middle: Chord
) -> tuple[Permutation, list[int | None], tuple[int, ...]]:
    state = compose(transposition(n, exterior), transposition(n, middle))
    residual = compose(inverse(state), ambient)
    residual_cycles = cycle_decomposition(residual)
    assert len(residual_cycles) == 3
    owner_of = {
        vertex: label
        for label, component in enumerate(residual_cycles)
        for vertex in component
    }
    generic_owner: list[int | None] = []
    for tail in range(n):
        head = (tail + 1) % n
        generic_owner.append(owner_of[tail] if state[head] == head else None)
    return state, generic_owner, tuple(map(len, residual_cycles))


def a_ratio(d: int) -> Fraction:
    return tau(d - 1) / tau(d) if d >= 2 else Fraction(0)


def b_ratio(d: int) -> Fraction:
    return tau(d - 2) / tau(d) if d >= 3 else Fraction(0)


def residual_and_repaired_responses(
    n: int, ambient: Permutation, exterior: Chord, middle: Chord
) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...], tuple[int, ...]]:
    """Two independent evaluations of the same owner response."""
    _, generic, sizes = owner_data(n, ambient, exterior, middle)
    a = tuple(a_ratio(d) for d in sizes)
    b = tuple(b_ratio(d) for d in sizes)
    scalar_field = tuple(Fraction(0) if o is None else a[o] for o in generic)

    direct: list[Fraction] = []
    repaired: list[Fraction] = []
    for ell in range(n):
        literal = Fraction(0)
        for x in range(n):
            left = generic[x]
            right = generic[(x + ell) % n]
            if left is None or right is None:
                continue
            literal += b[left] if left == right else a[left] * a[right]

        rank_one = sum(
            (scalar_field[x] * scalar_field[(x + ell) % n] for x in range(n)),
            Fraction(0),
        )
        correction = Fraction(0)
        for label, d in enumerate(sizes):
            if d < 3:
                continue
            delta = b_ratio(d) - a_ratio(d) ** 2
            assert delta >= 0
            overlap = sum(
                generic[x] == label and generic[(x + ell) % n] == label
                for x in range(n)
            )
            correction += delta * overlap
        direct.append(literal)
        repaired.append(rank_one + correction)

    # A size-two owner's omitted delta can affect lag zero only.
    assert all(direct[ell] == repaired[ell] for ell in range(1, n))
    assert all(value >= 0 for value in repaired)
    return tuple(direct), tuple(repaired), sizes


def cyclic_order(support: set[int], anchor: int, n: int) -> tuple[int, ...]:
    assert anchor in support
    return tuple(sorted(support, key=lambda x: (x - anchor) % n))


def interval_representation_response(
    n: int, exterior: Chord, middle: Chord, anchor: int
) -> tuple[str, tuple[int, ...], tuple[Fraction, ...]]:
    """One anchored S/N interval reconstruction of a supported double."""
    support = set(exterior) | set(middle)
    assert len(support) == 4
    vertices = cyclic_order(support, anchor, n)
    gaps = tuple(
        (vertices[(i + 1) % 4] - vertices[i]) % n for i in range(4)
    )
    assert all(g > 0 for g in gaps) and sum(gaps) == n

    intervals = tuple(
        frozenset((vertices[i] + offset) % n for offset in range(gaps[i] - 1))
        for i in range(4)
    )
    matching = {frozenset(exterior), frozenset(middle)}
    separated = {
        frozenset((vertices[0], vertices[1])),
        frozenset((vertices[2], vertices[3])),
    }
    nested = {
        frozenset((vertices[0], vertices[3])),
        frozenset((vertices[1], vertices[2])),
    }
    if matching == separated:
        kind = "S"
        owner_sets = (intervals[0], intervals[2], intervals[1] | intervals[3])
        owner_sizes = (gaps[0], gaps[2], gaps[1] + gaps[3])
    elif matching == nested:
        kind = "N"
        owner_sets = (intervals[1], intervals[3], intervals[0] | intervals[2])
        owner_sizes = (gaps[1], gaps[3], gaps[0] + gaps[2])
    else:
        raise AssertionError("crossing matching is not S/N-compatible")

    response: list[Fraction] = []
    for ell in range(n):
        total = Fraction(0)
        for i in range(3):
            for j in range(3):
                coefficient = (
                    b_ratio(owner_sizes[i])
                    if i == j
                    else a_ratio(owner_sizes[i]) * a_ratio(owner_sizes[j])
                )
                overlap = sum(
                    (x + ell) % n in owner_sets[j] for x in owner_sets[i]
                )
                total += coefficient * overlap
        response.append(total)
    return kind, gaps, tuple(response)


def positive_compositions(total: int, parts: int):
    for cuts in combinations(range(1, total), parts - 1):
        marks = (0,) + cuts + (total,)
        yield tuple(marks[i + 1] - marks[i] for i in range(parts))


def global_composition_multiplicities(n: int) -> dict[str, int | bool]:
    """Enumerate the 1/3 and 1/4 inverse representation counts."""
    triangles: Counter[Permutation] = Counter()
    doubles: Counter[Permutation] = Counter()

    for anchor in range(n):
        for gaps in positive_compositions(n, 3):
            v0 = anchor
            v1 = (v0 + gaps[0]) % n
            v2 = (v1 + gaps[1]) % n
            triangles[cycle_permutation(n, (v0, v1, v2))] += 1

        for gaps in positive_compositions(n, 4):
            v0 = anchor
            v1 = (v0 + gaps[0]) % n
            v2 = (v1 + gaps[1]) % n
            v3 = (v2 + gaps[2]) % n
            s_state = compose(
                transposition(n, canonical_chord(v0, v1)),
                transposition(n, canonical_chord(v2, v3)),
            )
            n_state = compose(
                transposition(n, canonical_chord(v0, v3)),
                transposition(n, canonical_chord(v1, v2)),
            )
            doubles[s_state] += 1
            doubles[n_state] += 1

    assert set(triangles.values()) == {3}
    assert set(doubles.values()) == {4}
    assert len(triangles) == 2 * math.comb(n, 3) // 2
    assert len(doubles) == 2 * math.comb(n, 4)
    return {
        "triangle_distinct_states": len(triangles),
        "triangle_representations": sum(triangles.values()),
        "triangle_multiplicity": 3,
        "triangle_normalization": "1/3",
        "double_distinct_S_or_N_states": len(doubles),
        "double_representations": sum(doubles.values()),
        "double_multiplicity": 4,
        "double_normalization": "1/4",
        "anchor_is_support_vertex": True,
        "extra_n_factor": False,
    }


def ordered_rank_two_products(n: int) -> Counter[Permutation]:
    chords = tuple(combinations(range(n), 2))
    multiplicity: Counter[Permutation] = Counter()
    for left in chords:
        p_left = transposition(n, left)
        for right in chords:
            state = compose(p_left, transposition(n, right))
            if rank(state) == 2:
                multiplicity[state] += 1
    assert set(multiplicity.values()) == {2, 3}
    return multiplicity


def channel_two_normalization(
    n: int, merged: Permutation, split: Permutation
) -> dict[str, str | bool | int]:
    """Check that the full two-cycle denominator already pays the fair choice."""
    r = rank(merged)
    assert r == rank(split)
    multiplicity = ordered_rank_two_products(n)

    masses: dict[str, Fraction] = {}
    for name, source in (("merged", merged), ("split", split)):
        denominator = completion_count(source, r)
        numerator = sum(
            (
                lift_count
                * completion_count(compose(inverse(state), source), r - 2)
                for state, lift_count in multiplicity.items()
            ),
            Fraction(0),
        )
        masses[name] = numerator / denominator
        assert masses[name] == 1

    split_cycles = tuple(c for c in cycle_decomposition(split) if len(c) > 1)
    assert len(split_cycles) == 2
    denominator = completion_count(split, r)
    first_component_masses: list[Fraction] = []
    for component in split_cycles:
        component_mass = Fraction(0)
        for chord in combinations(component, 2):
            after_first = compose(transposition(n, chord), split)
            component_mass += completion_count(after_first, r - 1) / denominator
        first_component_masses.append(component_mass)
    assert first_component_masses == [Fraction(1, 2), Fraction(1, 2)]

    return {
        "ordered_product_states": len(multiplicity),
        "merged_channel_two_mass": str(masses["merged"]),
        "split_channel_two_mass": str(masses["split"]),
        "split_first_component_masses": [str(x) for x in first_component_masses],
        "extra_half_would_give_split_mass": "1/2",
        "extra_channel_two_half": False,
    }


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    k = 5
    n = 3 * k
    admissible = range(2, n - 1)
    ambient = cycle_permutation(n, tuple(range(n)))
    c_minus = tuple(range(k))
    middle = tuple(range(k, 2 * k))
    c_plus = tuple(range(2 * k, 3 * k))
    merged_cycle = tuple(range(1, k)) + c_plus

    nu_minus = first_chord_law(c_minus)
    nu_middle = first_chord_law(middle)
    nu_plus = first_chord_law(c_plus)
    nu_merged = first_chord_law(merged_cycle)
    exterior_chords = sorted(set(nu_merged) | set(nu_minus) | set(nu_plus))
    gamma = {
        chord: nu_merged.get(chord, Fraction(0))
        - Fraction(1, 2) * nu_minus.get(chord, Fraction(0))
        - Fraction(1, 2) * nu_plus.get(chord, Fraction(0))
        for chord in exterior_chords
    }
    assert sum(gamma.values(), Fraction(0)) == 0
    assert any(x < 0 for x in gamma.values()) and any(x > 0 for x in gamma.values())

    # This is beta_1(ef)=gamma(e)nu_M(f): the disjoint product uniquely
    # identifies its exterior and middle factors.
    product_to_pair: dict[Permutation, tuple[Chord, Chord]] = {}
    beta: dict[Permutation, Fraction] = {}
    for exterior in exterior_chords:
        for mid, mid_weight in nu_middle.items():
            state = compose(transposition(n, exterior), transposition(n, mid))
            assert state not in product_to_pair
            product_to_pair[state] = (exterior, mid)
            beta[state] = gamma[exterior] * mid_weight
    assert sum(beta.values(), Fraction(0)) == 0

    responses: dict[tuple[Chord, Chord], tuple[Fraction, ...]] = {}
    direct_repaired_checks = 0
    anchored_composition_checks = 0
    topology_counts = Counter()
    for exterior in exterior_chords:
        for mid in nu_middle:
            direct, repaired, residual_sizes = residual_and_repaired_responses(
                n, ambient, exterior, mid
            )
            assert all(direct[ell] == repaired[ell] for ell in admissible)
            direct_repaired_checks += len(tuple(admissible))
            responses[(exterior, mid)] = direct

            support = set(exterior) | set(mid)
            assert len(support) == 4
            anchored = []
            for anchor in sorted(support):
                kind, _, interval_response = interval_representation_response(
                    n, exterior, mid, anchor
                )
                topology_counts[kind] += 1
                assert interval_response == direct
                anchored.append(interval_response)
                anchored_composition_checks += n
            assert len(anchored) == 4
            assert tuple(
                sum((row[ell] for row in anchored), Fraction(0)) / 4
                for ell in range(n)
            ) == direct
            # A missing 1/4 or an extra n cannot satisfy this identity.
            assert len(residual_sizes) == 3

    multiplicity_summary = global_composition_multiplicities(n)

    cells: list[dict[str, object]] = []
    eta_direct: dict[int, Fraction] = {}
    eta_repaired: dict[int, Fraction] = {}
    eta_composition: dict[int, Fraction] = {}
    for ell in admissible:
        direct_total = Fraction(0)
        repaired_total = Fraction(0)
        composition_total = Fraction(0)
        for mid, mid_weight in sorted(nu_middle.items()):
            fixed_middle = Fraction(0)
            for exterior in exterior_chords:
                direct, repaired, _ = residual_and_repaired_responses(
                    n, ambient, exterior, mid
                )
                fixed_middle += gamma[exterior] * direct[ell]
                repaired_total += (
                    mid_weight * gamma[exterior] * repaired[ell]
                )
                anchored_responses = [
                    interval_representation_response(n, exterior, mid, anchor)[2]
                    for anchor in sorted(set(exterior) | set(mid))
                ]
                composition_total += (
                    mid_weight
                    * gamma[exterior]
                    * sum((row[ell] for row in anchored_responses), Fraction(0))
                    / 4
                )
            direct_total += mid_weight * fixed_middle
            cells.append(
                {
                    "ell": ell,
                    "middle_edge": list(mid),
                    "fmcp_value": q(fixed_middle),
                    "sign": (
                        "negative"
                        if fixed_middle < 0
                        else "positive"
                        if fixed_middle > 0
                        else "zero"
                    ),
                }
            )
        eta_direct[ell] = direct_total
        eta_repaired[ell] = repaired_total
        eta_composition[ell] = composition_total
        assert direct_total == repaired_total == composition_total

    assert len(cells) == 120
    negatives = [row for row in cells if row["sign"] == "negative"]
    minimum_value = min(Fraction(str(row["fmcp_value"])) for row in cells)
    minimizers = [
        row for row in cells if Fraction(str(row["fmcp_value"])) == minimum_value
    ]
    assert len(negatives) == 16
    assert {(row["ell"], tuple(row["middle_edge"])) for row in minimizers} == {
        (6, (6, 9)),
        (9, (6, 9)),
    }
    assert all(value > 0 for value in eta_direct.values())
    assert all(eta_direct[ell] == eta_direct[n - ell] for ell in admissible)

    alpha_1 = Fraction(4 * (k - 1) ** 2, (n - 3) * (n - 4))
    lambda_n = Fraction(n - 2) * Fraction(n, n - 2) ** (n - 3)
    response_denominator = (n - 3) * (n - 4)
    weighted_eta = {
        ell: alpha_1 * lambda_n * eta_direct[ell] / response_denominator
        for ell in admissible
    }

    merged_perm = cycle_permutation(n, merged_cycle)
    split_perm = compose(
        cycle_permutation(n, c_minus), cycle_permutation(n, c_plus)
    )
    channel_two = channel_two_normalization(n, merged_perm, split_perm)

    payload = {
        "status": "independent exact audit; FMCP_1 refuted only",
        "scope": "k=5, n=15, all 12 admissible lags and 10 middle chords",
        "convention": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "repository_status": subprocess.check_output(
            ["git", "status", "--short"], text=True
        ).splitlines(),
        "python": platform.python_version(),
        "nonstandard_dependencies": [],
        "random_seed": None,
        "deterministic": True,
        "command": "python3 independent_fmcp_audit.py --output independent_results.json",
        "imports_or_reads_m295": False,
        "k": k,
        "n": n,
        "admissible_lags": list(admissible),
        "beta1_factorization": "beta_1(ef)=gamma(e)nu_M(f)",
        "gamma_total_mass": q(sum(gamma.values(), Fraction(0))),
        "gamma_sign_counts": {
            "positive": sum(value > 0 for value in gamma.values()),
            "negative": sum(value < 0 for value in gamma.values()),
            "zero": sum(value == 0 for value in gamma.values()),
        },
        "direct_repaired_admissible_checks": direct_repaired_checks,
        "anchored_interval_response_checks": anchored_composition_checks,
        "anchored_topology_counts": dict(topology_counts),
        "composition_multiplicities": multiplicity_summary,
        "channel_two_normalization": channel_two,
        "cells_tested": len(cells),
        "negative_cells": len(negatives),
        "minimum_value": q(minimum_value),
        "minimizers": minimizers,
        "eta1_direct": {str(ell): q(value) for ell, value in eta_direct.items()},
        "eta1_repaired": {str(ell): q(value) for ell, value in eta_repaired.items()},
        "eta1_positive_composition": {
            str(ell): q(value) for ell, value in eta_composition.items()
        },
        "all_eta1_lags_positive": all(value > 0 for value in eta_direct.values()),
        "all_eta1_three_reconstructions_equal": eta_direct
        == eta_repaired
        == eta_composition,
        "statewise_and_weighted_reflection_exact": True,
        "alpha_1": q(alpha_1),
        "Lambda_n": q(lambda_n),
        "R_n": response_denominator,
        "weighted_alpha1_CP1": {
            str(ell): q(value) for ell, value in weighted_eta.items()
        },
        "minimum_weighted_alpha1_CP1": q(min(weighted_eta.values())),
        "fmcp1": "refuted",
        "goci1": "unresolved",
        "downstream_inference": False,
        "cells": cells,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "negative_cells": len(negatives),
                "minimum_value": q(minimum_value),
                "minimizers": minimizers,
                "all_eta1_lags_positive": payload["all_eta1_lags_positive"],
                "all_eta1_three_reconstructions_equal": payload[
                    "all_eta1_three_reconstructions_equal"
                ],
                "channel_two_split_mass": channel_two["split_channel_two_mass"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
