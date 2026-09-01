#!/usr/bin/env python3
"""Clean-room exact audit for M195.

This checker reconstructs the exterior residual laws directly from the
minimal-factorization recurrence.  It imports no M192 code or data and is
deliberately capped at k=3,5.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import DefaultDict

Perm = tuple[int, ...]
Key = tuple[int, int]


def identity(n: int) -> Perm:
    return tuple(range(n))


def compose(p: Perm, q: Perm) -> Perm:
    """Return pq with (pq)(x)=p(q(x))."""
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
    ans = list(range(n))
    ans[x], ans[y] = ans[y], ans[x]
    return tuple(ans)


def cycles(p: Perm) -> list[tuple[int, ...]]:
    seen: set[int] = set()
    ans: list[tuple[int, ...]] = []
    for start in range(len(p)):
        if start in seen:
            continue
        cur: list[int] = []
        x = start
        while x not in seen:
            seen.add(x)
            cur.append(x)
            x = p[x]
        ans.append(tuple(cur))
    return ans


def edge_vertices(e: Perm) -> tuple[int, int]:
    moved = [x for x in range(len(e)) if e[x] != x]
    assert len(moved) == 2
    return moved[0], moved[1]


def internal_edges(p: Perm) -> list[Perm]:
    ans: list[Perm] = []
    n = len(p)
    for component in cycles(p):
        for x, y in combinations(component, 2):
            ans.append(transposition(n, x, y))
    return ans


def tau(d: int) -> Fraction:
    assert d >= 1
    return Fraction(d ** (d - 1), math.factorial(d))


def factorization_count(p: Perm) -> Fraction:
    cs = cycles(p)
    rank = sum(len(c) - 1 for c in cs)
    ans = Fraction(math.factorial(rank))
    for c in cs:
        ans *= tau(len(c))
    return ans


def split_size(e: Perm, source: Perm) -> int:
    x, y = edge_vertices(e)
    component = next(c for c in cycles(source) if x in c)
    assert y in component
    ix, iy = component.index(x), component.index(y)
    distance = (iy - ix) % len(component)
    return min(distance, len(component) - distance)


def ambient_runs(component: tuple[int, ...], n: int) -> tuple[int, ...]:
    support = set(component)
    starts = sorted(x for x in support if (x - 1) % n not in support)
    assert starts
    lengths: list[int] = []
    for start in starts:
        d = 0
        while (start + d) % n in support:
            d += 1
        lengths.append(d)
    assert sum(lengths) == len(component)
    return tuple(sorted(lengths))


def component_counts(first: Perm, second: Perm, h: Perm) -> dict[Key, int]:
    product = compose(first, second)
    residual = compose(inverse(product), h)
    cs = cycles(residual)
    assert len(cs) == 3
    ans: DefaultDict[Key, int] = defaultdict(int)
    for component in cs:
        run_count = len(ambient_runs(component, len(h)))
        assert run_count in (1, 2)
        ans[(run_count, len(component))] += 1
    assert sum(ans.values()) == 3
    return dict(ans)


def source_residual(k: int, label: str) -> Perm:
    n = 3 * k
    if label == "B":
        exterior = tuple(range(1, k)) + tuple(range(2 * k, 3 * k))
        return cycle_perm(n, exterior)
    if label == "A":
        lower = cycle_perm(n, tuple(range(0, k)))
        upper = cycle_perm(n, tuple(range(2 * k, 3 * k)))
        return compose(lower, upper)
    raise ValueError(label)


def edge_color(k: int, edge: Perm) -> str:
    x, y = edge_vertices(edge)

    def side(v: int) -> int:
        if 0 <= v < k:
            return 0
        if 2 * k <= v < 3 * k:
            return 1
        raise AssertionError(("non-exterior endpoint", v))

    return "same" if side(x) == side(y) else "cross"


def qstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def prefix_value(counts: dict[Key, int], ell: int, one_run_only: bool) -> int:
    total = 0
    for (run_type, size), multiplicity in counts.items():
        if 2 <= size <= ell and (not one_run_only or run_type == 1):
            total += multiplicity
    assert 0 <= total <= 3
    return total


def analyze_law(k: int, label: str) -> dict:
    n = 3 * k
    h = cycle_perm(n, tuple(range(n)))
    source = source_residual(k, label)
    denominator = factorization_count(source)
    expected_rank = 2 * k - 2
    assert sum(len(c) - 1 for c in cycles(source)) == expected_rank

    mass: DefaultDict[int, Fraction] = defaultdict(Fraction)
    triangle: DefaultDict[int, Fraction] = defaultdict(Fraction)
    disjoint: DefaultDict[int, Fraction] = defaultdict(Fraction)
    disjoint_profile_raw: dict[int, DefaultDict[Key, Fraction]] = {}
    records: list[tuple[int, bool, Fraction, dict[Key, int]]] = []
    collision_events = 0
    collision_weight = Fraction()
    color_mass: DefaultDict[str, Fraction] = defaultdict(Fraction)
    disjoint_color_mass: DefaultDict[str, Fraction] = defaultdict(Fraction)

    for first in internal_edges(source):
        s = split_size(first, source)
        after_first = compose(first, source)
        for second in internal_edges(after_first):
            after_second = compose(second, after_first)
            weight = factorization_count(after_second) / denominator
            common_endpoint = bool(set(edge_vertices(first)) & set(edge_vertices(second)))
            counts = component_counts(first, second, h)
            pattern = f"{edge_color(k, first)}-{edge_color(k, second)}"

            records.append((s, common_endpoint, weight, counts))
            mass[s] += weight
            color_mass[pattern] += weight
            if common_endpoint:
                triangle[s] += weight
            else:
                disjoint[s] += weight
                disjoint_color_mass[pattern] += weight
                bucket = disjoint_profile_raw.setdefault(s, defaultdict(Fraction))
                for key, multiplicity in counts.items():
                    bucket[key] += weight * multiplicity
            if any(multiplicity >= 2 for multiplicity in counts.values()):
                collision_events += 1
                collision_weight += weight

    assert sum(mass.values(), Fraction()) == 1
    assert sum(color_mass.values(), Fraction()) == 1

    profiles: dict[int, dict[Key, Fraction]] = {}
    for s, raw in disjoint_profile_raw.items():
        assert disjoint[s] > 0
        profiles[s] = {key: value / disjoint[s] for key, value in raw.items()}
        assert sum(profiles[s].values(), Fraction()) == 3

    return {
        "mass": dict(mass),
        "triangle": dict(triangle),
        "disjoint": dict(disjoint),
        "profiles": profiles,
        "records": records,
        "pair_events": len(records),
        "collision_events": collision_events,
        "collision_weight": collision_weight,
        "color_mass": dict(color_mass),
        "disjoint_color_mass": dict(disjoint_color_mass),
    }


def expected_gamma(k: int, label: str, s: int) -> Fraction:
    if label == "B":
        other = 2 * k - 1 - s
    else:
        other = k - s
    return Fraction(2, 2 * k - 3) * (
        2 - Fraction(1, s) - Fraction(1, other)
    )


def profile_prefix(profile: dict[Key, Fraction], ell: int, one_run_only: bool) -> Fraction:
    return sum(
        value
        for (run_type, size), value in profile.items()
        if 2 <= size <= ell and (not one_run_only or run_type == 1)
    )


def direct_prefix(records: list[tuple[int, bool, Fraction, dict[Key, int]]],
                  ell: int,
                  one_run_only: bool,
                  shared: bool) -> Fraction:
    return sum(
        weight * prefix_value(counts, ell, one_run_only)
        for _s, is_shared, weight, counts in records
        if is_shared == shared
    )


def check_cayley_convolution(limit: int) -> None:
    for r in range(2, limit + 1):
        lhs = sum((tau(c) * tau(r - c) for c in range(1, r)), Fraction())
        rhs = Fraction(2 * (r - 1), r) * tau(r)
        assert lhs == rhs, (r, lhs, rhs)


def run_case(k: int) -> dict:
    assert k in (3, 5)
    check_cayley_convolution(2 * k - 1)
    law_b = analyze_law(k, "B")
    law_a = analyze_law(k, "A")
    D = 2 * k - 1
    a_support = range(1, (k - 1) // 2 + 1)

    for s in range(1, k):
        predicted = Fraction(D, D - 1) * tau(s) * tau(D - s) / tau(D)
        assert law_b["mass"][s] == predicted
        gamma = law_b["triangle"][s] / law_b["mass"][s]
        assert gamma == expected_gamma(k, "B", s)

    for s in a_support:
        predicted = Fraction(k, k - 1) * tau(s) * tau(k - s) / tau(k)
        assert law_a["mass"][s] == predicted
        gamma = law_a["triangle"][s] / law_a["mass"][s]
        assert gamma == expected_gamma(k, "A", s)

    triangle_b = sum(law_b["triangle"].values(), Fraction())
    triangle_a = sum(law_a["triangle"].values(), Fraction())
    assert triangle_b == Fraction(3, 2 * k - 1)
    assert triangle_a == Fraction(3 * (k - 2), k * (2 * k - 3))

    p_hat = law_b["disjoint"]
    q_hat = law_a["disjoint"]
    cumulative: dict[int, Fraction] = {}
    running = Fraction()
    for u in range(1, k):
        running += p_hat.get(u, Fraction()) - q_hat.get(u, Fraction())
        cumulative[u] = running

    endpoint = cumulative[k - 1]
    expected_endpoint = Fraction(-6 * (k - 1), k * (2 * k - 1) * (2 * k - 3))
    assert endpoint == expected_endpoint
    assert endpoint < 0

    max_scaled_e = 0.0
    for u, value in cumulative.items():
        max_scaled_e = max(max_scaled_e, k * abs(float(value)) / math.sqrt(u))

    abel_checks = 0
    shared_checks = 0
    max_shared_scaled = 0.0
    for ell in range(2, (3 * k - 1) // 2 + 1):
        for one_run_only in (False, True):
            phi = {
                s: profile_prefix(law_b["profiles"][s], ell, one_run_only)
                for s in range(1, k)
            }
            psi = {
                s: profile_prefix(law_a["profiles"][s], ell, one_run_only)
                for s in a_support
            }

            direct_disjoint = (
                sum(p_hat[s] * phi[s] for s in range(1, k))
                - sum(q_hat[s] * psi[s] for s in a_support)
            )
            abel = endpoint * phi[k - 1]
            abel += sum(
                cumulative[u] * (phi[u] - phi[u + 1])
                for u in range(1, k - 1)
            )
            abel += sum(
                q_hat[s] * (phi[s] - psi[s])
                for s in a_support
            )
            assert direct_disjoint == abel
            abel_checks += 1

            shared_b = direct_prefix(
                law_b["records"], ell, one_run_only, shared=True
            )
            shared_a = direct_prefix(
                law_a["records"], ell, one_run_only, shared=True
            )
            assert 0 <= shared_b <= 3 * triangle_b
            assert 0 <= shared_a <= 3 * triangle_a
            max_shared_scaled = max(
                max_shared_scaled,
                k * abs(float(shared_b - shared_a)) / math.sqrt(ell),
            )
            shared_checks += 1

    collision_events = law_b["collision_events"] + law_a["collision_events"]
    disjoint_collision_events = sum(
        1
        for law in (law_b, law_a)
        for _s, shared, _weight, counts in law["records"]
        if not shared and any(value >= 2 for value in counts.values())
    )
    shared_collision_events = sum(
        1
        for law in (law_b, law_a)
        for _s, shared, _weight, counts in law["records"]
        if shared and any(value >= 2 for value in counts.values())
    )
    assert disjoint_collision_events + shared_collision_events == collision_events
    assert collision_events > 0
    assert any(key[0] == 2 for p in law_b["profiles"].values() for key in p)
    assert sum(law_b["disjoint_color_mass"].values(), Fraction()) == (
        1 - triangle_b
    )

    return {
        "k": k,
        "cayley_convolution_checked_through": 2 * k - 1,
        "ordered_pair_events": {
            "B": law_b["pair_events"],
            "A": law_a["pair_events"],
        },
        "collision_events_retained": {
            "B": law_b["collision_events"],
            "A": law_a["collision_events"],
            "disjoint": disjoint_collision_events,
            "shared_endpoint": shared_collision_events,
            "total": collision_events,
        },
        "collision_probability_mass": {
            "B": qstr(law_b["collision_weight"]),
            "A": qstr(law_a["collision_weight"]),
        },
        "triangle_mass": {
            "B": qstr(triangle_b),
            "A": qstr(triangle_a),
        },
        "disjoint_endpoint": qstr(endpoint),
        "endpoint_sign": "negative",
        "max_k_abs_E_over_sqrt_u": max_scaled_e,
        "abel_identities_checked": abel_checks,
        "shared_prefix_bounds_checked": shared_checks,
        "max_k_abs_shared_response_over_sqrt_l": max_shared_scaled,
        "B_ordered_color_mass": {
            key: qstr(value) for key, value in sorted(law_b["color_mass"].items())
        },
        "B_disjoint_color_mass": {
            key: qstr(value)
            for key, value in sorted(law_b["disjoint_color_mass"].items())
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    result = {
        "mission": "M195",
        "method": "independent exact minimal-factorization recurrence",
        "imports_m192_code_or_data": False,
        "scope": {"k": [3, 5], "finite_only": True, "seed": None},
        "python": platform.python_version(),
        "cases": [run_case(k) for k in (3, 5)],
        "verdict": "all exact clean-room assertions passed",
        "universal_inference": False,
    }
    path = Path(args.output)
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
