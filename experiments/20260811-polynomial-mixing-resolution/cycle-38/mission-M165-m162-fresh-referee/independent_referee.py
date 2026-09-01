#!/usr/bin/env python3
"""Clean-room exact referee for frozen M162.

This checker does not import predecessor code.  Unlike M162's bivariate
kernel implementation, it represents the actual history feature directly as
a finite rational sum ``K(u,v)=sum_f weight_f f(u)f(v)``.  It evaluates only
the four theorem-critical right-heavy trace-repair states.
"""

from __future__ import annotations

import functools
import hashlib
import json
import math
import platform
from fractions import Fraction as F
from pathlib import Path


Poly = tuple[F, ...]
Feature = tuple[Poly, F]


def clean(values: list[F] | tuple[F, ...]) -> Poly:
    out = list(values)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def add(left: Poly, right: Poly) -> Poly:
    out = [F(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    return clean(out)


def scale(poly: Poly, scalar: F) -> Poly:
    return clean([scalar * value for value in poly])


def multiply(left: Poly, right: Poly) -> Poly:
    out = [F(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return clean(out)


def monomial(degree: int) -> Poly:
    return tuple([F(0)] * degree + [F(1)])


def rising(start: int, length: int) -> int:
    return math.prod(range(start, start + length))


def moment(kappa: int, deficit: int, degree: int) -> F:
    assert 1 <= deficit < kappa
    return F(rising(deficit, degree), rising(kappa, degree))


def expect(poly: Poly, kappa: int, deficit: int) -> F:
    return sum(
        (coefficient * moment(kappa, deficit, degree)
         for degree, coefficient in enumerate(poly)),
        F(0),
    )


def inner(left: Poly, right: Poly, kappa: int, deficit: int) -> F:
    return expect(multiply(left, right), kappa, deficit)


@functools.cache
def tree_weight(n: int) -> F:
    assert n >= 1
    return F(n ** (n - 1), math.factorial(n))


@functools.cache
def compositions(total: int) -> tuple[tuple[int, ...], ...]:
    if total == 0:
        return ((),)
    return tuple(
        (head,) + tail
        for head in range(1, total + 1)
        for tail in compositions(total - head)
    )


@functools.cache
def cayley_count(total: int, parts: int) -> F:
    if (total, parts) == (0, 0):
        return F(1)
    if not 1 <= parts <= total:
        return F(0)
    return F(parts * total ** (total - parts), total * math.factorial(total - parts))


def split_mass(s: int, bottom: int) -> F:
    return tree_weight(s + 1 - bottom) * tree_weight(bottom) / tree_weight(s + 1)


def source_mass(source: tuple[int, ...]) -> F:
    return math.prod(tree_weight(part) for part in source) / (
        math.factorial(len(source)) * tree_weight(sum(source) + 1)
    )


def belongs(source: tuple[int, ...], endpoint: tuple[int, ...]) -> bool:
    return any(
        sum(source[:cut]) == endpoint[0] and source[cut:] == endpoint[1:]
        for cut in range(1, len(source) + 1)
    )


@functools.cache
def basin_rows(s: int) -> tuple[tuple[tuple[int, ...], tuple[tuple[int, ...], ...]], ...]:
    sources = compositions(s)
    endpoints = sorted(
        {
            (sum(source[:cut]),) + source[cut:]
            for source in sources
            for cut in range(1, len(source))
            if sum(source[:cut]) + source[cut] - 1 >= 2
        },
        key=lambda endpoint: (len(endpoint), endpoint),
    )
    return tuple(
        (endpoint, tuple(source for source in sources if belongs(source, endpoint)))
        for endpoint in endpoints
    )


def context(source: tuple[int, ...], bottom: int) -> Poly:
    degree = len(source)
    last = source[-1]
    if last < bottom:
        return (F(0),)
    if last == bottom:
        out = [F(0)] * degree
        out[-1] = F(degree)
        return clean(out)
    coefficient = split_mass(last - 1, bottom)
    out = [F(0)] * (degree + 1)
    out[0], out[-1] = coefficient, -coefficient
    return clean(out)


@functools.cache
def reset_features(s: int, bottom: int) -> tuple[Feature, ...]:
    q = split_mass(s, bottom)
    rows: list[Feature] = []
    for endpoint, sources in basin_rows(s):
        current: Poly = (F(0),)
        for source in sources:
            centered = add(context(source, bottom), (F(-q),))
            current = add(current, scale(centered, source_mass(source)))
        capacity = F(len(endpoint)) * source_mass(endpoint)
        if current != (F(0),):
            rows.append((current, F(1) / (q * capacity)))
    return tuple(rows)


@functools.cache
def groups(s: int) -> tuple[tuple[int, int, F], ...]:
    rows: list[tuple[int, int, F]] = []
    for degree in range(1, s + 1):
        for last in range(1, s + 1):
            mass = tree_weight(last) * cayley_count(s - last, degree - 1) / (
                math.factorial(degree) * tree_weight(s + 1)
            )
            if mass:
                rows.append((degree, last, mass))
    assert sum((mass for _, _, mass in rows), F(0)) == 1
    return tuple(rows)


def beta_binomial(kappa: int, deficit: int, degree: int, observed: int) -> F:
    return (
        F(math.comb(degree, observed))
        * rising(deficit, observed)
        * rising(kappa - deficit, degree - observed)
        / rising(kappa, degree)
    )


def bernstein(degree: int, observed: int) -> Poly:
    out = [F(0)] * (degree + 1)
    for extra in range(degree - observed + 1):
        out[observed + extra] += F(
            math.comb(degree, observed)
            * math.comb(degree - observed, extra)
            * (-1) ** extra
        )
    return clean(out)


def merge_feature(target: dict[Poly, F], poly: Poly, weight: F) -> None:
    if poly == (F(0),) or weight == 0:
        return
    assert weight > 0
    target[poly] = target.get(poly, F(0)) + weight


@functools.cache
def history_features(s: int, kappa: int, deficit: int, bottom: int) -> tuple[Feature, ...]:
    """Compressed explicit actual-history coordinates.

    Equal polynomial coordinates may be merged because
    ``w1*f tensor f + w2*f tensor f = (w1+w2)*f tensor f``.
    """
    q_parent = split_mass(s, bottom)
    merged: dict[Poly, F] = {}
    for poly, weight in reset_features(s, bottom):
        merge_feature(merged, poly, weight)
    for degree, last, mass in groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        q_child = split_mass(last - 1, bottom)
        eta = mass * q_child / q_parent
        for observed in range(degree):  # observed=degree is killed exactly
            pi = beta_binomial(kappa, deficit, degree, observed)
            like = bernstein(degree, observed)
            child = history_features(
                last - 1, kappa + degree, deficit + observed, bottom
            )
            for child_poly, child_weight in child:
                merge_feature(
                    merged,
                    multiply(like, child_poly),
                    eta * child_weight / pi,
                )
    return tuple(merged.items())


def feature_bilinear(
    features: tuple[Feature, ...],
    left: Poly,
    right: Poly,
    kappa: int,
    deficit: int,
) -> F:
    return sum(
        (
            weight
            * inner(left, poly, kappa, deficit)
            * inner(right, poly, kappa, deficit)
            for poly, weight in features
        ),
        F(0),
    )


def feature_trace(features: tuple[Feature, ...], kappa: int, deficit: int) -> F:
    return sum(
        (weight * inner(poly, poly, kappa, deficit) for poly, weight in features),
        F(0),
    )


@functools.cache
def scalar_h(s: int, kappa: int, deficit: int, bottom: int) -> F:
    reset = F(0)
    for current, normalized_weight in reset_features(s, bottom):
        # normalized_weight=1/(q*c), hence multiply by q to recover 1/c.
        reset += (
            split_mass(s, bottom)
            * normalized_weight
            * expect(current, kappa, deficit) ** 2
        )
    total = reset
    for degree, last, mass in groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        for observed in range(degree):
            total += (
                mass
                * beta_binomial(kappa, deficit, degree, observed)
                * scalar_h(last - 1, kappa + degree, deficit + observed, bottom)
            )
    return total


@functools.cache
def orthogonal(kappa: int, deficit: int, degree: int) -> tuple[tuple[Poly, ...], tuple[F, ...]]:
    polys: list[Poly] = []
    norms: list[F] = []
    for n in range(degree + 1):
        poly = monomial(n)
        for previous, norm in zip(polys, norms):
            poly = add(
                poly,
                scale(previous, -inner(poly, previous, kappa, deficit) / norm),
            )
        norm = inner(poly, poly, kappa, deficit)
        assert poly[-1] == 1 and norm > 0
        polys.append(poly)
        norms.append(norm)
    return tuple(polys), tuple(norms)


def diagonal_recursion(s: int, kappa: int, deficit: int, bottom: int) -> F:
    total = feature_trace(reset_features(s, bottom), kappa, deficit)
    q_parent = split_mass(s, bottom)
    for degree, last, mass in groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        eta = mass * split_mass(last - 1, bottom) / q_parent
        for observed in range(degree):
            child_kappa = kappa + degree
            child_deficit = deficit + observed
            like = bernstein(degree, observed)
            for poly, weight in history_features(
                last - 1, child_kappa, child_deficit, bottom
            ):
                total += eta * weight * expect(
                    multiply(like, multiply(poly, poly)),
                    child_kappa,
                    child_deficit,
                )
    return total


def first_mode_recursion(s: int, kappa: int, deficit: int, bottom: int) -> F:
    p_parent = F(deficit, kappa)
    center_parent = (F(-p_parent), F(1))
    variance_parent = moment(kappa, deficit, 2) - p_parent**2
    total = feature_bilinear(
        reset_features(s, bottom),
        center_parent,
        center_parent,
        kappa,
        deficit,
    ) / variance_parent
    q_parent = split_mass(s, bottom)
    for degree, last, mass in groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        eta = mass * split_mass(last - 1, bottom) / q_parent
        for observed in range(degree):
            pi = beta_binomial(kappa, deficit, degree, observed)
            child_kappa = kappa + degree
            child_deficit = deficit + observed
            p_child = F(child_deficit, child_kappa)
            delta = p_child - p_parent
            center_child = (F(-p_child), F(1))
            child = history_features(last - 1, child_kappa, child_deficit, bottom)
            mean_sq = feature_bilinear(
                child, (F(1),), (F(1),), child_kappa, child_deficit
            )
            mixed = feature_bilinear(
                child, (F(1),), center_child, child_kappa, child_deficit
            )
            centered_sq = feature_bilinear(
                child, center_child, center_child, child_kappa, child_deficit
            )
            total += eta * pi * (
                delta**2 * mean_sq + 2 * delta * mixed + centered_sq
            ) / variance_parent
    return total


def ratio(text: str) -> F:
    numerator, denominator = text.split("/")
    return F(int(numerator), int(denominator))


EXPECTED = {
    (8, 2, 1, 2): {
        "degree": 6,
        "budget": "3841777/4782969",
        "exact": "155388964128011262503320903402940849315591/354227185839954068610957846164747059200000",
        "trace": "10304304880412164262179965176912695056497059/12663621893778357952841743000389707366400000",
        "first": "402019179600185677632566092877/1254214379464465614844723200000",
        "t1": "4996140114572494719254376953733294500866709/10130897515022686362273394400311765893120000",
    },
    (7, 2, 1, 3): {
        "degree": 4,
        "budget": "222769/262144",
        "exact": "87889239421531159630365467873/176887761240853787443200000000",
        "trace": "252148230967853278398383537527/294812935401422979072000000000",
        "first": "70368015650316301693/228804951690000000000",
        "t1": "807398665985479360251261039443/1474064677007114895360000000000",
    },
    (8, 2, 1, 3): {
        "degree": 5,
        "budget": "5665/6561",
        "exact": "253985287689718867427349453367883132399/473678965726019627503656524945817600000",
        "trace": "1224306706195599231904288448107783787287/1302617155746553975635055443600998400000",
        "first": "413479481719546951991715566717/1222648205696781378807398400000",
        "t1": "627026434358121815325432827112120047681/1042093724597243180508044354880798720000",
    },
    (9, 2, 1, 3): {
        "degree": 6,
        "budget": "21823477/25000000",
        "exact": "884793664847325174104678035065147237189087444781/1562205337586660322231315333120000000000000000000",
        "trace": "18869946398780956645521860394138727391247148220693747/18765210515090963790642559781437440000000000000000000",
        "first": "22188869354818896067370178239706902418179/61428413402447622526650889002811392000000",
        "t1": "16122225803772674061119988493476225828060496537096871/25020280686787951720856746375249920000000000000000000",
    },
}


def record(value: F) -> dict[str, str | float]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


def main() -> None:
    failures: list[str] = []

    # Small, asymmetric shared-observation checks.  These test the single-pi
    # RN scaling and the exact retained/killed mass split without a grid.
    transfer_count = 0
    transfer_cases = ((2, 1, 3), (5, 1, 4), (5, 4, 4))
    for kappa, deficit, degree in transfer_cases:
        retained = F(0)
        for observed in range(degree + 1):
            pi = beta_binomial(kappa, deficit, degree, observed)
            like = bernstein(degree, observed)
            if expect(like, kappa, deficit) != pi:
                failures.append(f"likelihood-mass:{kappa,deficit,degree,observed}")
            for left_power, right_power in ((0, 0), (1, 2), (2, 1)):
                lhs = pi * moment(kappa + degree, deficit + observed, left_power) * moment(
                    kappa + degree, deficit + observed, right_power
                )
                rhs = (
                    expect(multiply(like, monomial(left_power)), kappa, deficit)
                    * expect(multiply(like, monomial(right_power)), kappa, deficit)
                    / pi
                )
                if lhs != rhs:
                    failures.append(f"shared-observation:{kappa,deficit,degree,observed}")
                transfer_count += 1
            if observed < degree:
                retained += expect(like, kappa, deficit) ** 2 / pi
        killed = beta_binomial(kappa, deficit, degree, degree)
        if retained != 1 - killed or killed <= 0:
            failures.append(f"killed-mass:{kappa,deficit,degree}")

    # The exact Gram--Schmidt polynomials fix the shifted-Jacobi order:
    # alpha=kappa-D-1 multiplies (1-u), beta=D-1 multiplies u.
    expected_jacobi = {
        (5, 1): (
            (F(1),),
            (F(-1, 5), F(1)),
            (F(1, 21), F(-4, 7), F(1)),
            (F(-1, 84), F(1, 4), F(-1), F(1)),
        ),
        (5, 4): (
            (F(1),),
            (F(-4, 5), F(1)),
            (F(10, 21), F(-10, 7), F(1)),
            (F(-5, 21), F(5, 4), F(-2), F(1)),
        ),
    }
    convention_rows = []
    for state, expected_polys in expected_jacobi.items():
        polys, norms = orthogonal(*state, 3)
        if polys != expected_polys:
            failures.append(f"jacobi-order:{state}")
        convention_rows.append(
            {
                "state_kappa_D": list(state),
                "standard_alpha_beta": [state[0] - state[1] - 1, state[1] - 1],
                "polynomials": [
                    [f"{coefficient.numerator}/{coefficient.denominator}" for coefficient in poly]
                    for poly in polys
                ],
                "norms": [record(norm) for norm in norms],
            }
        )

    rows = []
    for state, expected in EXPECTED.items():
        s, kappa, deficit, bottom = state
        features = history_features(s, kappa, deficit, bottom)
        degree = max((len(poly) - 1 for poly, _ in features), default=0)
        polys, norms = orthogonal(kappa, deficit, degree)
        energies = [
            feature_bilinear(features, poly, poly, kappa, deficit) / norm
            for poly, norm in zip(polys, norms)
        ]
        trace = feature_trace(features, kappa, deficit)
        exact = feature_bilinear(features, (F(1),), (F(1),), kappa, deficit)
        scalar = scalar_h(s, kappa, deficit, bottom) / split_mass(s, bottom)
        first = energies[1]
        t1 = trace - first
        budget = 1 - split_mass(s, bottom)
        trace_via_recursion = diagonal_recursion(s, kappa, deficit, bottom)
        first_via_recursion = first_mode_recursion(s, kappa, deficit, bottom)
        checks = {
            "degree": degree == expected["degree"],
            "budget": budget == ratio(expected["budget"]),
            "exact": exact == ratio(expected["exact"]),
            "scalar_normalization": scalar == exact,
            "trace": trace == ratio(expected["trace"]),
            "trace_recursion": trace_via_recursion == trace,
            "first": first == ratio(expected["first"]),
            "first_recursion": first_via_recursion == first,
            "t1": t1 == ratio(expected["t1"]),
            "parseval": sum(energies, F(0)) == trace,
            "modal_nonnegative": all(energy >= 0 for energy in energies),
            "upper_bound": t1 >= exact,
            "repairs_trace": trace > budget and t1 <= budget,
            "degree_bound": degree <= s - bottom,
        }
        for name, passed in checks.items():
            if not passed:
                failures.append(f"{name}:{state}")
        rows.append(
            {
                "state_s_kappa_D_B": list(state),
                "feature_count_after_equal-polynomial_merge": len(features),
                "degree": degree,
                "budget": record(budget),
                "exact_H_over_q": record(exact),
                "trace": record(trace),
                "first_mode_energy": record(first),
                "T1": record(t1),
                "T1_minus_budget": record(t1 - budget),
                "modal_energies": [record(energy) for energy in energies],
                "checks": checks,
            }
        )

    payload = {
        "claim": "fresh exact weighted-feature referee of frozen M162",
        "scope": "auxiliary normalized full unweighted reset excursion only",
        "python": platform.python_version(),
        "seed": None,
        "predecessor_imports": False,
        "tested_states_only": [list(state) for state in EXPECTED],
        "shared_observation": {
            "cases": [list(case) for case in transfer_cases],
            "monomial_pair_rows": transfer_count,
            "all_pass": not any(item.startswith(("likelihood", "shared", "killed")) for item in failures),
            "retained_branch": "a<d",
            "killed_branch": "a=d omitted exactly",
        },
        "jacobi_convention": convention_rows,
        "repair_rows": rows,
        "failure_count": len(failures),
        "failures": failures,
    }
    target = Path(__file__).with_name("independent_results.json")
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    target.write_text(encoded)
    print(
        json.dumps(
            {
                "output": str(target),
                "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
                "failure_count": len(failures),
                "states": len(rows),
                "predecessor_imports": False,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
