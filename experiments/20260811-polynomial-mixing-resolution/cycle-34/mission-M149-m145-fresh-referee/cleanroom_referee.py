#!/usr/bin/env python3
"""Clean-room exact referee for frozen M145.

This file imports no predecessor source or result.  It rebuilds the
composition/basin recurrence from the displayed definitions.  Its polynomial
certificate route is deliberately different from M145: integer-node Newton
interpolation followed by the direct power-to-Bernstein identity.  Since the
seven ratio variables are proved multiaffine, tail ratio coefficients are
obtained directly from box vertices.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import itertools
import json
import math
import platform
import sys
from fractions import Fraction as Q
from pathlib import Path


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def record(x: Q) -> dict[str, str | float]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator), "decimal": float(x)}


@functools.lru_cache(None)
def w(n: int) -> Q:
    assert n >= 1
    return Q(n ** (n - 1), math.factorial(n))


@functools.lru_cache(None)
def comps(n: int) -> tuple[tuple[int, ...], ...]:
    if n == 0:
        return ((),)
    return tuple((first,) + rest for first in range(1, n + 1) for rest in comps(n - first))


@functools.lru_cache(None)
def forest(n: int, p: int) -> Q:
    if n == 0 and p == 0:
        return Q(1)
    if p < 1 or p > n:
        return Q(0)
    return Q(p * n ** (n - p), n * math.factorial(n - p))


def rise(a: int, k: int) -> int:
    return math.prod(range(a, a + k))


def fall(a: int, k: int) -> int:
    return math.prod(range(a - k + 1, a + 1))


@functools.lru_cache(None)
def lambda_basin(a: int, degree: int) -> Q:
    return math.factorial(degree - 1) * sum(
        (
            Q(p * fall(a, p), math.factorial(p + degree - 1) * a**p)
            for p in range(1, a + 1)
        ),
        Q(0),
    )


@functools.lru_cache(None)
def scalar_c(s: int) -> Q:
    return sum(
        (
            w(a)
            * forest(s - a, degree - 1)
            * lambda_basin(a, degree) ** 2
            / (math.factorial(degree - 1) * w(s + 1))
            for degree in range(2, s + 1)
            for a in range(1, s - degree + 2)
        ),
        Q(0),
    )


def attach(a: int, deficit: int, degree: int, j: int, z: Q) -> Q:
    """Positive-rank attachment law in offset/deficit coordinates."""
    denominator = math.prod(1 + (a + r) * z for r in range(degree))
    if j == 0:
        return Q(rise(deficit, degree)) * z**degree / denominator
    return (
        Q(math.comb(degree, j) * rise(deficit, degree - j))
        * z ** (degree - j)
        * math.prod(1 + (a - deficit + r) * z for r in range(j))
        / denominator
    )


def split(ratios: tuple[Q, ...]) -> Q:
    return w(len(ratios)) * math.prod(ratios)


@functools.lru_cache(None)
def normalized_support(
    excess: int, ratios: tuple[Q, ...], z: Q, offset: int, deficit: int
) -> tuple[tuple[tuple[int, tuple[int, ...]], tuple[int, Q, Q]], ...]:
    """Rows keyed by (height,prefix), with (degree,mass/q,contextual mean)."""
    rows = []
    for height in range(excess + 1):
        for prefix in comps(excess - height):
            degree = len(prefix) + 1
            bottom_product = math.prod(ratios[-height:]) if height else Q(1)
            mass = (
                math.prod(w(part) for part in prefix)
                / (math.factorial(degree) * w(excess + 1) * bottom_product)
            )
            if height == 0:
                mean = degree * attach(offset, deficit, degree - 1, 0, z)
            else:
                mean = split(ratios[-height:]) * (
                    1 - attach(offset, deficit, degree, 0, z)
                )
            rows.append(((height, prefix), (degree, mass, mean)))
    assert len(rows) == 2**excess
    assert sum((mass * mean for _, (_, mass, mean) in rows), Q(0)) == 1
    return tuple(rows)


def support_dict(
    excess: int, ratios: tuple[Q, ...], z: Q, offset: int, deficit: int
) -> dict[tuple[int, tuple[int, ...]], tuple[int, Q, Q]]:
    return dict(normalized_support(excess, ratios, z, offset, deficit))


@functools.lru_cache(None)
def refined_reset(
    excess: int,
    ratios: tuple[Q, ...],
    z: Q,
    offset: int,
    deficit: int,
    ordinary: Q,
) -> tuple[Q, int, int]:
    """Expanded reset divided by q, with full-basin one-power subtraction."""
    rows = support_dict(excess, ratios, z, offset, deficit)
    q = split(ratios)
    subtraction = Q(0)
    squares = Q(0)
    endpoint_count = 0
    normalization_count = 0

    # For fixed height every composition of excess-height is an endpoint.
    # Its basin consists of every refinement of its first part; this also
    # proves that an intersecting basin is wholly inside contextual support.
    for height in range(excess):
        for endpoint in comps(excess - height):
            first, tail = endpoint[0], endpoint[1:]
            degree, endpoint_mass, _ = rows[(height, endpoint)]
            capacity = degree * endpoint_mass
            sources = tuple(partition + tail for partition in comps(first))
            basin_mass = sum((rows[(height, source)][1] for source in sources), Q(0))
            lam = lambda_basin(first, degree)
            assert basin_mass == capacity * lam
            theta = sum(
                (
                    rows[(height, source)][1] * (rows[(height, source)][2] - q)
                    for source in sources
                ),
                Q(0),
            )
            subtraction += capacity * lam**2
            squares += theta**2 / capacity
            endpoint_count += 1
            normalization_count += 1

    assert endpoint_count == 2**excess - 1
    value = q * ordinary - q**2 * subtraction + squares
    return value, endpoint_count, normalization_count


@functools.lru_cache(None)
def refined_envelope(
    excess: int,
    ratios: tuple[Q, ...],
    z: Q,
    offset: int,
    deficit: int,
    ordinary_by_rank: tuple[Q, ...],
) -> Q:
    """Return F=upper bound on H/q for an arbitrary-deficit context."""
    assert len(ratios) == excess + 1
    assert len(ordinary_by_rank) == excess + 1
    q = split(ratios)
    if excess == 0:
        return 1 - q
    value = refined_reset(
        excess, ratios, z, offset, deficit, ordinary_by_rank[0]
    )[0]
    rows = support_dict(excess, ratios, z, offset, deficit)
    for height in range(1, excess + 1):
        degree_mass: dict[int, Q] = {}
        for (hh, _), (degree, mass, _) in rows.items():
            if hh == height:
                degree_mass[degree] = degree_mass.get(degree, Q(0)) + mass
        child_ratios = ratios[-height:]
        child_ordinary = ordinary_by_rank[-height:]
        child_q = split(child_ratios)
        for degree, mass in degree_mass.items():
            for j in range(1, degree + 1):
                child = refined_envelope(
                    height - 1,
                    child_ratios,
                    z,
                    offset + degree,
                    deficit + degree - j,
                    child_ordinary,
                )
                value += mass * attach(offset, deficit, degree, j, z) * child_q * child
    return value


def cayley(n: int) -> Q:
    return w(n) / w(n + 1)


def actual_data(s: int) -> tuple[tuple[Q, ...], tuple[Q, ...]]:
    return (
        tuple(cayley(s - i) for i in range(7)),
        tuple(scalar_c(s - i) for i in range(7)),
    )


def cleared_slack(ratios: tuple[Q, ...], z: Q, ordinary: tuple[Q, ...]) -> Q:
    q = split(ratios)
    envelope = refined_envelope(6, ratios, z, 0, 1, ordinary)
    delta = math.prod(1 + a * z for a in range(1, 7))
    return delta**2 * (1 - q - envelope)


# ---- Independent full-state literal/grouped recurrence --------------------


def choose(n: int, k: int) -> int:
    return math.comb(n, k) if 0 <= k <= n else 0


def q_state(s: int, bottom: int) -> Q:
    return w(s + 1 - bottom) * w(bottom) / w(s + 1)


def contextual_mean(degree: int, last: int, K: int, R: int, bottom: int) -> Q:
    if last < bottom:
        return Q(0)
    if last == bottom:
        den = choose(degree + K - 1, K - 1)
        return Q(K * choose(degree + K - R - 2, K - R - 1), den) if den else Q(0)
    return q_state(last - 1, bottom) * (
        1 - Q(choose(K, R + 1), choose(K + degree, R + 1))
    )


def root_mass(parts: tuple[int, ...]) -> Q:
    return math.prod(w(part) for part in parts) / (
        math.factorial(len(parts)) * w(sum(parts) + 1)
    )


@functools.lru_cache(None)
def active_endpoints(s: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        endpoint
        for endpoint in comps(s)
        if len(endpoint) >= 2 and endpoint[0] + endpoint[1] - 1 >= 2
    )


def source_refines_endpoint(source: tuple[int, ...], endpoint: tuple[int, ...]) -> bool:
    return any(
        sum(source[:cut]) == endpoint[0] and source[cut:] == endpoint[1:]
        for cut in range(1, len(source))
    )


@functools.lru_cache(None)
def reset_literal(state: tuple[int, int, int, int]) -> Q:
    s, K, R, bottom = state
    q = q_state(s, bottom)
    sources = comps(s)
    value = Q(0)
    for endpoint in active_endpoints(s):
        theta = sum(
            (
                root_mass(source)
                * (contextual_mean(len(source), source[-1], K, R, bottom) - q)
                for source in sources
                if source_refines_endpoint(source, endpoint)
            ),
            Q(0),
        )
        value += theta**2 / (len(endpoint) * root_mass(endpoint))
    return value


@functools.lru_cache(None)
def reset_grouped(state: tuple[int, int, int, int]) -> Q:
    s, K, R, bottom = state
    q = q_state(s, bottom)
    value = Q(0)
    for endpoint in active_endpoints(s):
        first, tail = endpoint[0], endpoint[1:]
        tail_weight = math.prod(w(part) for part in tail)
        theta = sum(
            (
                forest(first, p)
                * tail_weight
                * (
                    contextual_mean(p + len(tail), tail[-1], K, R, bottom)
                    - q
                )
                / (math.factorial(p + len(tail)) * w(s + 1))
                for p in range(1, first + 1)
            ),
            Q(0),
        )
        value += theta**2 / (len(endpoint) * root_mass(endpoint))
    return value


def attach_integer(K: int, R: int, degree: int, j: int) -> Q:
    return Q(
        choose(R + j, j) * choose(K - R - 1 + degree - j, degree - j),
        choose(K + degree, degree),
    )


@functools.lru_cache(None)
def root_groups(s: int) -> tuple[tuple[int, int, Q], ...]:
    rows = tuple(
        (
            degree,
            last,
            w(last) * forest(s - last, degree - 1)
            / (math.factorial(degree) * w(s + 1)),
        )
        for degree in range(1, s + 1)
        for last in range(1, s + 1)
        if forest(s - last, degree - 1)
    )
    assert sum((mass for _, _, mass in rows), Q(0)) == 1
    return rows


@functools.lru_cache(None)
def deep_children(state: tuple[int, int, int, int]):
    s, K, R, bottom = state
    rows = []
    for degree, last, mass in root_groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        assert sum((attach_integer(K, R, degree, j) for j in range(degree + 1)), Q(0)) == 1
        for j in range(1, degree + 1):
            probability = attach_integer(K, R, degree, j)
            if probability:
                rows.append(
                    (
                        mass * probability,
                        (last - 1, K + degree, R + j, bottom),
                        degree,
                        last,
                        j,
                    )
                )
    return tuple(rows)


@functools.lru_cache(None)
def H_grouped(state: tuple[int, int, int, int]) -> Q:
    return reset_grouped(state) + sum(
        (mass * H_grouped(child) for mass, child, _, _, _ in deep_children(state)),
        Q(0),
    )


@functools.lru_cache(None)
def H_literal(state: tuple[int, int, int, int]) -> Q:
    return reset_literal(state) + sum(
        (mass * H_literal(child) for mass, child, _, _, _ in deep_children(state)),
        Q(0),
    )


# ---- Newton/power/Bernstein conversion, independent of M145 --------------


def poly_mul_linear(poly: list[Q], root: int) -> list[Q]:
    out = [Q(0)] * (len(poly) + 1)
    for i, coefficient in enumerate(poly):
        out[i] -= root * coefficient
        out[i + 1] += coefficient
    return out


def integer_newton_power(values: list[Q]) -> list[Q]:
    """Interpolate p(0),...,p(n) into ascending monomial coefficients."""
    n = len(values) - 1
    differences = values[:]
    leading = []
    for _ in range(n + 1):
        leading.append(differences[0])
        differences = [b - a for a, b in zip(differences, differences[1:])]
    power = [Q(0)] * (n + 1)
    basis = [Q(1)]
    for order, delta in enumerate(leading):
        scale = delta / math.factorial(order)
        for i, coefficient in enumerate(basis):
            power[i] += scale * coefficient
        basis = poly_mul_linear(basis, order)
    return power


def poly_eval(power: list[Q], x: Q) -> Q:
    value = Q(0)
    for coefficient in reversed(power):
        value = value * x + coefficient
    return value


def half_interval_bernstein(power: list[Q], degree: int) -> list[Q]:
    """Bernstein coefficients on z=x/2, 0<=x<=1."""
    assert len(power) <= degree + 1
    padded = power + [Q(0)] * (degree + 1 - len(power))
    return [
        sum(
            (
                padded[k]
                * Q(math.comb(i, k), math.comb(degree, k))
                / 2**k
                for k in range(i + 1)
            ),
            Q(0),
        )
        for i in range(degree + 1)
    ]


def bernstein_eval(coefficients: list[Q], x: Q) -> Q:
    degree = len(coefficients) - 1
    return sum(
        (
            coefficient
            * math.comb(degree, i)
            * x**i
            * (1 - x) ** (degree - i)
            for i, coefficient in enumerate(coefficients)
        ),
        Q(0),
    )


def sample_degree(values: list[Q]) -> int:
    differences = values[:]
    for degree in range(len(values) - 1):
        differences = [b - a for a, b in zip(differences, differences[1:])]
        if all(value == 0 for value in differences):
            return degree
    return len(values) - 1


def digest(values: list[Q]) -> str:
    body = "".join(f"{x.numerator}/{x.denominator}\n" for x in values)
    return hashlib.sha256(body.encode()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    failures: list[dict[str, object]] = []

    # Immutable M145 provenance, checked by this script as a second gate.
    predecessor = Path(__file__).resolve().parents[2] / "cycle-33" / "mission-M145-suffix-excess-six"
    expected_hashes = {
        "plan.md": "eef285e14c41ba475dac8c16bfeb9500188935807f766f98ddbacb4d45385231",
        "checkpoint.md": "4b7519915ee8ca97c4483c818a99b020fa0a589196ac05d5a49ab602eaa70182",
        "suffix_excess_six.md": "6e0af764322dcde3108f6b35102f9a7f334c427077ae5ae5de95ce0bbe84e65d",
        "l6_exact.py": "9ec575eea344e9ea57e9561b29fdfa3dc3c7c982fe5f0052fbf61b853423e314",
        "l6_exact.json": "a3583b387a6553fcdbf156fdb3f37bf71f077c729a400983f79ebfa81513c6fc",
        "report.md": "46bc88095f2223874341d820daa60ffe90f59815ab29aecc5156b0f645b815f4",
    }
    observed_hashes = {
        name: hashlib.sha256((predecessor / name).read_bytes()).hexdigest()
        for name in expected_hashes
    }
    if observed_hashes != expected_hashes:
        failures.append({"kind": "immutable-hash-mismatch", "observed": observed_hashes})

    # Exact structure and all-j accounting.
    ratios7, ordinary7 = actual_data(7)
    z7 = Q(1, 2)
    rows7 = support_dict(6, ratios7, z7, 0, 1)
    positive_groups = {(height, degree) for (height, _), (degree, _, _) in rows7.items()}
    live_groups = {(height, degree) for height, degree in positive_groups if height >= 1}
    nominal_ranks = sum(degree for _, degree in live_groups)
    active_ranks = len(deep_children((7, 1, 0, 1)))
    all_j_checks = 0
    for height, degree in live_groups:
        assert sum((attach(0, 1, degree, j, z7) for j in range(degree + 1)), Q(0)) == 1
        all_j_checks += degree
    structure = {
        "support": len(rows7),
        "exceptional_basins": refined_reset(6, ratios7, z7, 0, 1, ordinary7[0])[1],
        "positive_groups": len(positive_groups),
        "live_groups": len(live_groups),
        "nominal_positive_ranks": nominal_ranks,
        "s7_retained_ranks": active_ranks,
        "all_j_terms_checked": all_j_checks,
        "mean_identity": record(sum((mass * mean for _, (_, mass, mean) in rows7.items()), Q(0))),
    }
    expected_structure = (64, 63, 22, 16, 51, 31)
    observed_structure = (
        structure["support"],
        structure["exceptional_basins"],
        structure["positive_groups"],
        structure["live_groups"],
        structure["nominal_positive_ranks"],
        structure["s7_retained_ranks"],
    )
    if observed_structure != expected_structure:
        failures.append({"kind": "structure", "observed": observed_structure})

    # Six selected roots: independent literal/grouped resets and resolvents.
    root_rows = []
    for s in (7, 8):
        ratios, ordinary = actual_data(s)
        for K in (1, 2, 5):
            state = (s, K, K - 1, s - 6)
            z = Q(1, K + 1)
            literal_reset = reset_literal(state)
            grouped_reset = reset_grouped(state)
            literal_h = H_literal(state)
            grouped_h = H_grouped(state)
            envelope = refined_envelope(6, ratios, z, 0, 1, ordinary)
            q = split(ratios)
            if literal_reset != grouped_reset:
                failures.append({"kind": "root-reset-disagreement", "state": state})
            if literal_h != grouped_h:
                failures.append({"kind": "root-resolvent-disagreement", "state": state})
            if not grouped_h <= q * envelope < q * (1 - q):
                failures.append({"kind": "root-bound", "state": state})
            root_rows.append(
                {
                    "state": list(state),
                    "reset_equal": literal_reset == grouped_reset,
                    "H_equal": literal_h == grouped_h,
                    "H_target_ratio": record(grouped_h / (q * (1 - q))),
                    "envelope_target_ratio": record(envelope / (1 - q)),
                    "retained_children": len(deep_children(state)),
                }
            )

    # All 270 lower-excess arbitrary-deficit contexts.
    arbitrary = []
    for excess in range(1, 5):
        for S in range(excess + 1, 8):
            bottom = S - excess
            ratios = tuple(cayley(S - i) for i in range(excess + 1))
            ordinary = tuple(scalar_c(S - i) for i in range(excess + 1))
            q = split(ratios)
            for K in range(2, 7):
                for R in range(1, K):
                    state = (S, K, R, bottom)
                    bound = q * refined_envelope(
                        excess, ratios, Q(1, K + 1), 0, K - R, ordinary
                    )
                    exact = H_grouped(state)
                    ratio = exact / bound if bound else Q(0)
                    arbitrary.append((ratio, state, exact <= bound))
                    if exact > bound:
                        failures.append({"kind": "arbitrary-deficit", "state": state})
    maximum_arbitrary = max(arbitrary, key=lambda row: row[0])
    arbitrary_payload = {
        "count": len(arbitrary),
        "failure_count": sum(not ok for _, _, ok in arbitrary),
        "maximum_exact_to_bound": record(maximum_arbitrary[0]),
        "maximizer": list(maximum_arbitrary[1]),
        "matches_761_over_763": maximum_arbitrary[0] == Q(761, 763),
    }
    if len(arbitrary) != 270 or maximum_arbitrary[:2] != (Q(761, 763), (3, 4, 2, 1)):
        failures.append({"kind": "arbitrary-extremum", "payload": arbitrary_payload})

    # Independent generic degree/multiaffinity diagnostics.
    generic_ratios = (
        Q(7, 20), Q(9, 25), Q(11, 30), Q(3, 8), Q(19, 50), Q(23, 60), Q(29, 75)
    )
    generic_ordinary = (Q(3, 4),) * 7
    generic_values = [
        cleared_slack(generic_ratios, Q(j), generic_ordinary) for j in range(17)
    ]
    z_degree = sample_degree(generic_values)
    ratio_degrees = []
    for axis in range(7):
        axis_values = []
        for j in range(3):
            point = list(generic_ratios)
            point[axis] += Q(j, 100)
            axis_values.append(cleared_slack(tuple(point), Q(2, 7), generic_ordinary))
        ratio_degrees.append(sample_degree(axis_values))
    degrees = tuple(ratio_degrees) + (z_degree,)
    if degrees != (1, 1, 1, 1, 1, 1, 1, 14):
        failures.append({"kind": "degree", "observed": degrees})

    # Finite s=7,...,104: Newton at z=0,...,14; direct power->Bernstein.
    finite_values: list[Q] = []
    finite_offgrid_failures = 0
    finite_min_indexed = []
    for s in range(7, 105):
        ratios, ordinary = actual_data(s)
        samples = [cleared_slack(ratios, Q(j), ordinary) for j in range(15)]
        power = integer_newton_power(samples)
        coefficients = half_interval_bernstein(power, 14)
        off = Q(7, 38)
        if poly_eval(power, off) != cleared_slack(ratios, off, ordinary):
            finite_offgrid_failures += 1
        finite_values.extend(coefficients)
        finite_min_indexed.extend((value, s, i) for i, value in enumerate(coefficients))
    finite_minimum, finite_min_s, finite_min_i = min(finite_min_indexed)
    finite_digest = digest(finite_values)
    finite_payload = {
        "range": "s=7,...,104; z in [0,1/2]",
        "method": "integer-node Newton to monomials; direct power-to-Bernstein",
        "count": len(finite_values),
        "nonpositive": sum(value <= 0 for value in finite_values),
        "offgrid_failures": finite_offgrid_failures,
        "minimum": record(finite_minimum),
        "minimum_s": finite_min_s,
        "minimum_index": finite_min_i,
        "coefficient_sha256": finite_digest,
        "matches_frozen_digest": finite_digest
        == "12bcb36c2409ede2ae36d8157a10671246c498043e0f6c6a8dc9f081018edde0",
    }
    if (
        finite_payload["count"] != 1470
        or finite_payload["nonpositive"]
        or finite_payload["offgrid_failures"]
        or not finite_payload["matches_frozen_digest"]
    ):
        failures.append({"kind": "finite-certificate", "payload": finite_payload})

    # Tail: multiaffinity makes ratio-axis Bernstein coefficients the vertices.
    lo, hi = Q(4, 11), Q(187, 500)
    tail_by_vertex: dict[tuple[int, ...], list[Q]] = {}
    tail_values: list[Q] = []
    for bits in itertools.product((0, 1), repeat=7):
        ratios = tuple(hi if bit else lo for bit in bits)
        samples = [cleared_slack(ratios, Q(j), generic_ordinary) for j in range(15)]
        power = integer_newton_power(samples)
        coefficients = half_interval_bernstein(power, 14)
        tail_by_vertex[bits] = coefficients
        tail_values.extend(coefficients)
    tail_minimum, tail_flat_index = min((value, i) for i, value in enumerate(tail_values))
    tail_bits = tuple(tail_flat_index // 15 >> shift & 1 for shift in reversed(range(7)))
    tail_z_index = tail_flat_index % 15

    # Full tensor off-grid identity.
    units = (Q(1, 8), Q(2, 8), Q(3, 8), Q(4, 8), Q(5, 8), Q(6, 8), Q(7, 8))
    x = Q(7, 11)
    off_ratios = tuple(lo + (hi - lo) * u for u in units)
    tensor_value = Q(0)
    for bits, coefficients in tail_by_vertex.items():
        ratio_basis = math.prod(u if bit else 1 - u for u, bit in zip(units, bits))
        tensor_value += ratio_basis * bernstein_eval(coefficients, x)
    tail_offgrid_ok = tensor_value == cleared_slack(off_ratios, x / 2, generic_ordinary)
    tail_digest = digest(tail_values)
    tail_payload = {
        "box": "seven ratios in [4/11,187/500], z in [0,1/2], every C_S=3/4",
        "method": "ratio vertices from multiaffinity; Newton/power Bernstein in z",
        "b99": record(cayley(99)),
        "b99_below_upper": cayley(99) < hi,
        "degrees": list(degrees),
        "count": len(tail_values),
        "nonpositive": sum(value <= 0 for value in tail_values),
        "offgrid_ok": tail_offgrid_ok,
        "minimum": record(tail_minimum),
        "minimum_index": list(tail_bits) + [tail_z_index],
        "coefficient_sha256": tail_digest,
        "matches_frozen_digest": tail_digest
        == "b2aafe3c93fc583b7ae7dc32fadaf3a46de97dac0fe8ba46f8ace2a6815dec1d",
    }
    if (
        tail_payload["count"] != 1920
        or tail_payload["nonpositive"]
        or not tail_payload["offgrid_ok"]
        or not tail_payload["b99_below_upper"]
        or not tail_payload["matches_frozen_digest"]
    ):
        failures.append({"kind": "tail-certificate", "payload": tail_payload})

    payload = {
        "mission": "M149 clean-room fresh referee of immutable M145",
        "status": "ACCEPT" if not failures else "REJECT",
        "scope": "auxiliary full nonlazy stationary-flow parking-degree suffix excess L=6 only",
        "target": "uniform fixed-length identity words in Omega(N,m); no gap or mixing inference",
        "convention": "(pq)(x)=p(q(x)); factors displayed left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "predecessor_hashes": observed_hashes,
        "structure": structure,
        "root_audits": root_rows,
        "arbitrary_deficit": arbitrary_payload,
        "degree_audit": {"multidegree": list(degrees)},
        "finite_certificate": finite_payload,
        "tail_certificate": tail_payload,
        "failure_count": len(failures),
        "failures": failures,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
                "status": payload["status"],
                "failure_count": len(failures),
                "finite": {
                    key: finite_payload[key]
                    for key in ("count", "nonpositive", "offgrid_failures", "minimum_s",
                                "minimum_index", "coefficient_sha256")
                },
                "tail": {
                    key: tail_payload[key]
                    for key in ("count", "nonpositive", "offgrid_ok", "minimum_index",
                                "coefficient_sha256")
                },
                "arbitrary": arbitrary_payload,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
