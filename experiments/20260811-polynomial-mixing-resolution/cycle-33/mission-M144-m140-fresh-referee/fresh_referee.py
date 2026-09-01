#!/usr/bin/env python3
"""Clean-room exact referee for frozen M140.

This program imports no predecessor code or data.  It reconstructs the
scalar identities and corrected L=5 recurrence from the formulas in the
proof, then obtains Bernstein certificates by Lagrange interpolation into
the monomial basis followed by the direct monomial-to-Bernstein formula.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import itertools
import json
import math
import platform
from fractions import Fraction as Q
from pathlib import Path


def frac(x: Q) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


@functools.lru_cache(None)
def w(n: int) -> Q:
    if n < 1:
        raise ValueError(n)
    return Q(n ** (n - 1), math.factorial(n))


@functools.lru_cache(None)
def tree_forest(n: int, roots: int) -> Q:
    if n == roots == 0:
        return Q(1)
    if roots < 1 or roots > n:
        return Q(0)
    return Q(roots * n ** (n - roots), n * math.factorial(n - roots))


def falling(n: int, r: int) -> int:
    return math.prod(range(n - r + 1, n + 1))


def rising(n: int, r: int) -> int:
    return math.prod(range(n, n + r))


@functools.lru_cache(None)
def basin_ratio(a: int, degree: int) -> Q:
    return math.factorial(degree - 1) * sum(
        (
            Q(p * falling(a, p), math.factorial(p + degree - 1) * a**p)
            for p in range(1, a + 1)
        ),
        Q(0),
    )


def endpoint_mass(s: int, a: int, degree: int) -> Q:
    return (
        w(a)
        * tree_forest(s - a, degree - 1)
        / (math.factorial(degree - 1) * w(s + 1))
    )


@functools.lru_cache(None)
def scalar_c(s: int) -> Q:
    return sum(
        (
            endpoint_mass(s, a, degree) * basin_ratio(a, degree) ** 2
            for degree in range(2, s + 1)
            for a in range(1, s - degree + 2)
        ),
        Q(0),
    )


def binomial_tail(s: int, degree: int) -> Q:
    den = (s + 1) ** (s - 1)
    return sum(
        (
            Q(math.comb(s - 1, j) * s ** (s - 1 - j), den)
            for j in range(degree - 1, s)
        ),
        Q(0),
    )


@functools.lru_cache(None)
def compositions(total: int) -> tuple[tuple[int, ...], ...]:
    if total == 0:
        return ((),)
    return tuple(
        (head,) + tail
        for head in range(1, total + 1)
        for tail in compositions(total - head)
    )


def attach(start: int, deficit: int, degree: int, rank: int, z: Q) -> Q:
    denominator = math.prod(1 + (start + r) * z for r in range(degree))
    if rank == 0:
        return Q(rising(deficit, degree)) * z**degree / denominator
    numerator = (
        math.comb(degree, rank)
        * rising(deficit, degree - rank)
        * z ** (degree - rank)
        * math.prod(1 + (start - deficit + r) * z for r in range(rank))
    )
    return Q(numerator, denominator)


def split_mass(ratios: tuple[Q, ...]) -> Q:
    return w(len(ratios)) * math.prod(ratios)


def root_rows(
    excess: int,
    ratios: tuple[Q, ...],
    z: Q,
    start: int,
    deficit: int,
) -> tuple[tuple[tuple[int, tuple[int, ...]], Q, Q], ...]:
    q = split_mass(ratios)
    rows = []
    for height in range(excess + 1):
        suffix_product = math.prod(ratios[-height:]) if height else Q(1)
        for prefix in compositions(excess - height):
            degree = len(prefix) + 1
            mass = Q(math.prod(w(part) for part in prefix)) / (
                math.factorial(degree) * w(excess + 1) * suffix_product
            )
            if height == 0:
                mean = degree * attach(start, deficit, degree - 1, 0, z)
            else:
                child_q = w(height) * suffix_product
                mean = child_q * (1 - attach(start, deficit, degree, 0, z))
            rows.append(((height, prefix), mass, mean))
    if len(rows) != 2**excess:
        raise AssertionError("root count")
    if sum((mass * mean for _, mass, mean in rows), Q(0)) != 1:
        raise AssertionError("root normalization")
    return tuple(rows)


def cuts(prefix: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(
        (sum(prefix[:cut]),) + prefix[cut:]
        for cut in range(1, len(prefix) + 1)
    )


def contains(source: tuple[int, ...], endpoint: tuple[int, ...]) -> bool:
    return any(
        sum(source[:cut]) == endpoint[0] and source[cut:] == endpoint[1:]
        for cut in range(1, len(source) + 1)
    )


def currents(rows, q: Q):
    by_key = {key: (mass, mean) for key, mass, mean in rows}
    endpoints = sorted(
        {
            (height, endpoint)
            for (height, prefix), _, _ in rows
            for endpoint in cuts(prefix)
        },
        key=lambda item: (item[0], len(item[1]), item[1]),
    )
    result = []
    for height, endpoint in endpoints:
        source_rows = [
            (mass, mean)
            for (h, prefix), mass, mean in rows
            if h == height and contains(prefix, endpoint)
        ]
        theta = sum((mass * (mean - q) for mass, mean in source_rows), Q(0))
        endpoint_mass_normalized = by_key[(height, endpoint)][0]
        capacity = (len(endpoint) + 1) * endpoint_mass_normalized
        supported_mass = sum((mass for mass, _ in source_rows), Q(0))
        result.append((height, endpoint, theta, capacity, supported_mass))
    return tuple(result)


def group_weight(rows, height: int, degree: int) -> Q:
    return sum(
        (
            mass
            for (h, prefix), mass, _ in rows
            if h == height and len(prefix) + 1 == degree
        ),
        Q(0),
    )


def ordinary_reset(
    excess: int,
    ratios: tuple[Q, ...],
    z: Q,
    start: int,
    deficit: int,
    height_bound: Q,
) -> Q:
    q = split_mass(ratios)
    rows = root_rows(excess, ratios, z, start, deficit)
    occurrence_mass = sum((mass * len(prefix) for (_, prefix), mass, _ in rows), Q(0))
    return q * (height_bound - q * occurrence_mass) + sum(
        (theta * theta / capacity for _, _, theta, capacity, _ in currents(rows, q)),
        Q(0),
    )


def arbitrary_deficit(
    excess: int,
    ratios: tuple[Q, ...],
    z: Q,
    start: int,
    deficit: int,
    height_bounds: dict[int, Q],
) -> Q:
    q = split_mass(ratios)
    if excess == 0:
        return 1 - q
    if excess > 3:
        raise AssertionError("accepted arbitrary-deficit range exceeded")
    rows = root_rows(excess, ratios, z, start, deficit)
    answer = ordinary_reset(excess, ratios, z, start, deficit, height_bounds[excess])
    for height in range(1, excess + 1):
        for degree in range(1, excess - height + 2):
            mass = group_weight(rows, height, degree)
            if mass == 0:
                continue
            child_ratios = ratios[-height:]
            child_q = split_mass(child_ratios)
            for rank in range(1, degree + 1):
                next_excess = height - 1
                next_deficit = deficit + degree - rank
                continuation = (
                    1 - child_q
                    if next_excess == 0
                    else arbitrary_deficit(
                        next_excess,
                        child_ratios,
                        z,
                        start + degree,
                        next_deficit,
                        height_bounds,
                    )
                )
                answer += (
                    mass
                    * attach(start, deficit, degree, rank, z)
                    * child_q
                    * continuation
                )
    return answer


def corrected_root_reset(ratios: tuple[Q, ...], z: Q, ordinary: Q):
    q = split_mass(ratios)
    rows = root_rows(5, ratios, z, 0, 1)
    data = currents(rows, q)
    if len(data) != 31:
        raise AssertionError("exceptional count")
    # Normalized supported_mass is a_E/q, so the internal subtraction is
    # q*sum((a_E/q)*lambda_E).  Exactly one lambda occurs here.
    supported = sum(
        (
            source_mass * basin_ratio(endpoint[0], len(endpoint) + 1)
            for _, endpoint, _, _, source_mass in data
        ),
        Q(0),
    )
    value = q * (ordinary - q * supported) + sum(
        (theta * theta / capacity for _, _, theta, capacity, _ in data),
        Q(0),
    )
    return value, rows


def l5_bound(
    ratios: tuple[Q, ...], z: Q, height_bounds: dict[int, Q], ordinary: Q
):
    q = split_mass(ratios)
    answer, rows = corrected_root_reset(ratios, z, ordinary)
    live_groups = 0
    nominal_ranks = 0
    nonzero_ranks = 0
    for height in range(1, 6):
        for degree in range(1, 7 - height):
            mass = group_weight(rows, height, degree)
            if mass == 0:
                continue
            live_groups += 1
            child_ratios = ratios[-height:]
            child_q = split_mass(child_ratios)
            for rank in range(1, degree + 1):
                nominal_ranks += 1
                next_excess = height - 1
                next_deficit = degree + 1 - rank
                if next_deficit == 1:
                    continuation = 1 - child_q
                else:
                    continuation = arbitrary_deficit(
                        next_excess,
                        child_ratios,
                        z,
                        degree,
                        next_deficit,
                        height_bounds,
                    )
                term = mass * attach(0, 1, degree, rank, z) * child_q * continuation
                answer += term
                if term != 0:
                    nonzero_ranks += 1
    if (live_groups, nominal_ranks) != (11, 31):
        raise AssertionError((live_groups, nominal_ranks))
    return answer, q, nonzero_ranks


def actual_data(s: int):
    ratios = tuple(w(s - offset) / w(s - offset + 1) for offset in range(6))
    bottom = s - 5
    heights = {
        excess: Q(bottom + excess - 1, bottom + excess + 1)
        for excess in range(1, 6)
    }
    return ratios, heights


def cleared_slack(ratios, z: Q, heights, ordinary: Q):
    bound, q, nonzero = l5_bound(ratios, z, heights, ordinary)
    denominator = math.prod(1 + a * z for a in range(1, 6)) ** 2
    return denominator * (1 - q - bound), nonzero


def poly_multiply(left: list[Q], right: list[Q]) -> list[Q]:
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


@functools.lru_cache(None)
def sample_to_power_matrix(degree: int) -> tuple[tuple[Q, ...], ...]:
    """Matrix from values at x=j/degree to monomial coefficients."""
    nodes = [Q(j, degree) for j in range(degree + 1)]
    columns = []
    for j, node in enumerate(nodes):
        basis = [Q(1)]
        scale = Q(1)
        for m, other in enumerate(nodes):
            if m == j:
                continue
            basis = poly_multiply(basis, [-other, Q(1)])
            scale *= node - other
        columns.append([coefficient / scale for coefficient in basis])
    return tuple(
        tuple(columns[column][power] for column in range(degree + 1))
        for power in range(degree + 1)
    )


def axis_transform(values, degrees, axis: int, matrix):
    output = {}
    other_ranges = [range(d + 1) for i, d in enumerate(degrees) if i != axis]
    for other in itertools.product(*other_ranges):
        def key(position: int):
            it = iter(other)
            return tuple(position if i == axis else next(it) for i in range(len(degrees)))

        vector = [values[key(j)] for j in range(degrees[axis] + 1)]
        for i, row in enumerate(matrix):
            output[key(i)] = sum((row[j] * vector[j] for j in range(len(row))), Q(0))
    return output


def sampled_grid_to_bernstein(samples, degrees):
    coefficients = samples
    for axis, degree in enumerate(degrees):
        coefficients = axis_transform(
            coefficients, degrees, axis, sample_to_power_matrix(degree)
        )
    # x^j=sum_{i>=j} C(i,j)/C(d,j) B_{i,d}(x).
    for axis, degree in enumerate(degrees):
        matrix = tuple(
            tuple(
                Q(math.comb(i, j), math.comb(degree, j)) if j <= i else Q(0)
                for j in range(degree + 1)
            )
            for i in range(degree + 1)
        )
        coefficients = axis_transform(coefficients, degrees, axis, matrix)
    return coefficients


def bernstein_value(coefficients, degrees, point):
    total = Q(0)
    for index, coefficient in coefficients.items():
        basis = Q(1)
        for degree, i, x in zip(degrees, index, point):
            basis *= math.comb(degree, i) * x**i * (1 - x) ** (degree - i)
        total += coefficient * basis
    return total


def rho(word: tuple[int, ...]) -> Q:
    return Q(math.prod(w(part) for part in word), math.factorial(len(word)) * w(sum(word) + 1))


def scalar_audit(failures):
    first_count = 0
    for s in range(2, 31):
        for degree in range(2, s + 1):
            lhs = sum(
                (
                    endpoint_mass(s, a, degree) * basin_ratio(a, degree)
                    for a in range(1, s - degree + 2)
                ),
                Q(0),
            )
            rhs = binomial_tail(s, degree)
            first_count += 1
            if lhs != rhs:
                failures.append({"kind": "first-moment", "s": s, "degree": degree})

    seven_terms = sum(
        (Q(2, n * (n + 2) * math.factorial(n)) for n in range(1, 8)), Q(0)
    )
    u_bound = seven_terms + Q(1, 17920)
    if seven_terms != Q(10388003, 12700800) or u_bound != Q(41554847, 50803200):
        failures.append({"kind": "U-arithmetic"})

    e_bound = sum((Q(1, math.factorial(n)) for n in range(7)), Q(0)) + Q(1, 4410)
    if e_bound != Q(31967, 11760) or not e_bound < Q(87, 32):
        failures.append({"kind": "e-bound"})

    n, u, h = 96, 5, 2
    log_error = (
        Q(u**3, 3 * n**2)
        + Q(u**3 * (u - 1), 3 * n**3)
        + Q(sum(r * r for r in range(1, u + 1)), 2 * n**2)
        + sum((Q(a * a, 2 * n * (n - a)) for a in range(1, h + 1)), Q(0))
    )
    if log_error != Q(23612897, 2962759680) or not log_error < Q(1, 100):
        failures.append({"kind": "log-error"})

    selected = (
        tuple((a, 2, Q(1)) for a in range(1, 5))
        + tuple((a, 3, Q(9, 16)) for a in range(1, 5))
        + ((1, 4, Q(3, 8)),)
    )
    expected_lambdas = {
        (1, 2): Q(1, 2), (2, 2): Q(2, 3), (3, 2): Q(3, 4), (4, 2): Q(4, 5),
        (1, 3): Q(1, 3), (2, 3): Q(5, 12), (3, 3): Q(41, 90), (4, 3): Q(153, 320),
        (1, 4): Q(1, 4),
    }
    correction = Q(0)
    ratio_identity_count = 0
    for a, degree, lower_l in selected:
        lam = basin_ratio(a, degree)
        if lam != expected_lambdas[(a, degree)] or not lower_l > lam:
            failures.append({"kind": "selected-lambda", "A": a, "degree": degree})
        correction += (
            w(a) * Q(32, 87) ** (a + 1) / math.factorial(degree - 2)
            * lam * (lower_l - lam)
        )
        for s in (100, 101, 137):
            nn, uu, hh = s - a, a + 1, degree - 2
            lhs = endpoint_mass(s, a, degree) / (w(a) / math.factorial(degree - 2))
            rhs = Q(nn, nn + uu) ** (nn + uu - 1) * math.prod(
                Q(nn + r, nn) for r in range(-hh, uu + 1)
            )
            ratio_identity_count += 1
            if lhs != rhs:
                failures.append({"kind": "R-identity", "s": s, "A": a, "degree": degree})
    if correction != Q(78988317872, 1121447071575) or not correction > Q(69, 1000):
        failures.append({"kind": "correction"})
    after_mass = Q(99, 100) * correction
    final = Q(409, 500) - Q(99, 100) * Q(69, 1000)
    if after_mass != Q(217217874148, 3115130754375) or final != Q(74969, 100000):
        failures.append({"kind": "normalization"})

    # Literal one-power check at the two smallest full-composition spaces.
    literal_count = 0
    min_unremoved = None
    for s in (6, 7):
        bottom = s - 5
        supported = tuple(
            (height, prefix, prefix + (bottom + height,))
            for height in range(6)
            for prefix in compositions(5 - height)
        )
        endpoints = sorted(
            {(height, endpoint) for height, prefix, _ in supported for endpoint in cuts(prefix)}
        )
        if len(supported) != 32 or len(endpoints) != 31:
            failures.append({"kind": "literal-count", "s": s})
        all_words = compositions(s)
        for height, endpoint_prefix in endpoints:
            endpoint = endpoint_prefix + (bottom + height,)
            a_mass = sum(
                (rho(word) for h0, prefix, word in supported if h0 == height and contains(prefix, endpoint_prefix)),
                Q(0),
            )
            b_mass = sum((rho(word) for word in all_words if contains(word, endpoint)), Q(0))
            capacity = len(endpoint) * rho(endpoint)
            lam = basin_ratio(endpoint[0], len(endpoint))
            literal_count += 1
            if b_mass != capacity * lam or a_mass > b_mass:
                failures.append({"kind": "one-power", "s": s, "endpoint": endpoint})
            remainder = (b_mass - a_mass) * lam
            min_unremoved = remainder if min_unremoved is None else min(min_unremoved, remainder)

    return {
        "first_moment_rows": first_count,
        "U_first_seven": frac(seven_terms),
        "U_upper": frac(u_bound),
        "e_upper": frac(e_bound),
        "log_error": frac(log_error),
        "R_identity_rows": ratio_identity_count,
        "selected_correction_D0": frac(correction),
        "after_mass_factor": frac(after_mass),
        "final_scalar_bound": frac(final),
        "literal_one_power_rows": literal_count,
        "minimum_unremoved_ordinary_term": frac(min_unremoved),
    }


def certificate_audit(failures):
    finite_coefficients = []
    finite_indexed = []
    s6_nonzero = None
    s6_structural = None
    finite_degrees = (12,)
    for s in range(6, 100):
        ratios, heights = actual_data(s)
        if s == 6:
            boundary_rows = root_rows(5, ratios, Q(1, 3), 0, 1)
            # Height one is the rank-one t=2 boundary and is inactive.
            # The remaining positive groups retain every nominal rank.
            s6_structural = sum(
                degree
                for height in range(2, 6)
                for degree in range(1, 7 - height)
                if group_weight(boundary_rows, height, degree) != 0
            )
        samples = {}
        for i in range(13):
            x = Q(i, 12)
            value, nonzero = cleared_slack(ratios, x / 2, heights, scalar_c(s))
            samples[(i,)] = value
            if s == 6 and i == 8:  # z=1/3, an interior actual point.
                s6_nonzero = nonzero
        coefficients = sampled_grid_to_bernstein(samples, finite_degrees)
        for i in range(13):
            value = coefficients[(i,)]
            finite_coefficients.append(value)
            finite_indexed.append((value, s, i))
        x = Q(7, 19)
        direct, _ = cleared_slack(ratios, x / 2, heights, scalar_c(s))
        if bernstein_value(coefficients, finite_degrees, (x,)) != direct:
            failures.append({"kind": "finite-off-grid", "s": s})

    finite_min, finite_s, finite_i = min(finite_indexed)
    finite_bad = sum(value <= 0 for value in finite_coefficients)
    finite_source = "\n".join(f"{x.numerator}/{x.denominator}" for x in finite_coefficients) + "\n"
    finite_digest = hashlib.sha256(finite_source.encode()).hexdigest()
    if finite_bad:
        failures.append({"kind": "finite-sign", "count": finite_bad})
    if finite_digest != "733243ff50622263540085ff0d6d4b01246164cc8119003cacb5dbeda11684f7":
        failures.append({"kind": "finite-digest", "observed": finite_digest})
    if (finite_min, finite_s, finite_i) != (
        Q(5307578203959502651, 4736091661711441920000), 7, 0
    ):
        failures.append({"kind": "finite-minimum"})
    s6_row = finite_coefficients[:13]
    s6_min = min(s6_row)
    if s6_min != Q(13461835439971, 11861248695609600) or s6_structural != 17:
        failures.append({"kind": "s6-boundary", "structural": s6_structural})

    degrees = (1, 1, 2, 2, 2, 2, 12)
    lo, hi = Q(4, 11), Q(187, 500)
    unit_heights = {excess: Q(1) for excess in range(1, 6)}
    samples = {}
    for index in itertools.product(*(range(degree + 1) for degree in degrees)):
        unit = tuple(Q(i, degree) for i, degree in zip(index, degrees))
        ratios = tuple(lo + (hi - lo) * unit[i] for i in range(6))
        value, _ = cleared_slack(ratios, unit[6] / 2, unit_heights, Q(3, 4))
        samples[index] = value
    tail = sampled_grid_to_bernstein(samples, degrees)
    tail_index, tail_min = min(tail.items(), key=lambda item: item[1])
    tail_bad = sum(value <= 0 for value in tail.values())
    tail_source = "\n".join(
        f"{','.join(map(str, index))}:{value.numerator}/{value.denominator}"
        for index, value in sorted(tail.items())
    ) + "\n"
    tail_digest = hashlib.sha256(tail_source.encode()).hexdigest()
    if tail_bad:
        failures.append({"kind": "tail-sign", "count": tail_bad})
    if tail_digest != "2c1aa8475dba3ae3d3c09f587662facb78b1c11e14aec2d04ae8d87bb5adf22f":
        failures.append({"kind": "tail-digest", "observed": tail_digest})
    if (tail_index, tail_min) != (
        (1, 1, 2, 2, 2, 0, 0),
        Q(4360847276079323, 50118750000000000000),
    ):
        failures.append({"kind": "tail-minimum"})
    off = (Q(1, 7), Q(2, 7), Q(3, 7), Q(4, 7), Q(5, 7), Q(6, 7), Q(7, 11))
    off_ratios = tuple(lo + (hi - lo) * off[i] for i in range(6))
    direct, _ = cleared_slack(off_ratios, off[6] / 2, unit_heights, Q(3, 4))
    if bernstein_value(tail, degrees, off) != direct:
        failures.append({"kind": "tail-off-grid"})

    b95 = w(95) / w(96)
    if not b95 < hi:
        failures.append({"kind": "ratio-upper"})
    return {
        "method": "Lagrange sample-to-monomial interpolation, then direct monomial-to-Bernstein conversion",
        "finite": {
            "range": "s=6,...,99; z in [0,1/2]",
            "count": len(finite_coefficients),
            "nonpositive": finite_bad,
            "minimum": frac(finite_min),
            "minimum_at": [finite_s, finite_i],
            "coefficient_sha256": finite_digest,
            "s6_minimum": frac(s6_min),
            "s6_structurally_retained_children": s6_structural,
            "s6_nonzero_numerical_charges_at_z_1_over_3": s6_nonzero,
            "s6_zero_charge_note": "one structurally retained lower child has zero envelope charge; positivity is certified by the slack coefficients",
        },
        "tail": {
            "box": "[4/11,187/500]^6 x [0,1/2]",
            "degrees": list(degrees),
            "count": len(tail),
            "nonpositive": tail_bad,
            "minimum": frac(tail_min),
            "minimum_at": list(tail_index),
            "coefficient_sha256": tail_digest,
            "b95": frac(b95),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    failures = []
    scalar = scalar_audit(failures)
    certificates = certificate_audit(failures)
    payload = {
        "claim": "fresh referee audit of M140 scalar lemma and corrected auxiliary L=5 theorem",
        "scope": "auxiliary full nonlazy stationary-flow parking-degree recurrence only; no gap or terminal",
        "convention": "(pq)(x)=p(q(x)); factors displayed left-to-right",
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "exceptional_subtraction": "one power: q*a_E*lambda_E; a_E*lambda_E^2 is rejected and unused",
        "scalar": scalar,
        "certificates": certificates,
        "failure_count": len(failures),
        "failures": failures,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "failure_count": len(failures),
        "finite_count": certificates["finite"]["count"],
        "finite_digest": certificates["finite"]["coefficient_sha256"],
        "tail_count": certificates["tail"]["count"],
        "tail_digest": certificates["tail"]["coefficient_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
