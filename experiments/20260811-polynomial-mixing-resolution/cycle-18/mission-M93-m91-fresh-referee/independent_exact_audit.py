#!/usr/bin/env python3
"""Independent exact referee audit of M91's balanced reduction.

This file intentionally imports no predecessor or M91 implementation.  It
reconstructs the raw ordered-pair kernel, cyclic quotient, residual-color
decomposition, conditioned split measures, Abel identity, posterior score,
and localized four-step contrast directly over ``Fraction``.

The calculation is a finite identity checker at k=3,5, not asymptotic
evidence.  Convention: (pq)(x)=p(q(x)); tuple factors multiply left-to-right.
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import platform
import subprocess
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


Perm = tuple[int, ...]
Vector = list[Fraction]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def transposition(n: int, x: int, y: int) -> Perm:
    out = list(range(n))
    out[x], out[y] = out[y], out[x]
    return tuple(out)


def cycle_permutation(n: int, entries: list[int] | tuple[int, ...]) -> Perm:
    out = list(range(n))
    for x, y in zip(entries, entries[1:] + entries[:1]):
        out[x] = y
    return tuple(out)


def cycle_lists(p: Perm) -> list[list[int]]:
    seen: set[int] = set()
    answer: list[list[int]] = []
    for start in range(len(p)):
        if start in seen:
            continue
        block: list[int] = []
        x = start
        while x not in seen:
            seen.add(x)
            block.append(x)
            x = p[x]
        answer.append(block)
    return answer


def minimal_count(p: Perm, length: int) -> int:
    blocks = cycle_lists(p)
    if len(p) - len(blocks) != length:
        return 0
    value = Fraction(math.factorial(length), 1)
    for block in blocks:
        d = len(block)
        if d > 1:
            value *= Fraction(d ** (d - 2), math.factorial(d - 1))
    assert value.denominator == 1
    return value.numerator


def theta(p: Perm, h: Perm) -> Perm:
    return compose(inverse(h), compose(p, h))


def edge_endpoints(edge: Perm) -> tuple[int, int]:
    moved = [x for x, y in enumerate(edge) if x != y]
    assert len(moved) == 2
    return moved[0], moved[1]


def product_kind(p: Perm) -> str:
    sizes = sorted(len(c) for c in cycle_lists(p) if len(c) > 1)
    if sizes == [3]:
        return "triangle"
    if sizes == [2, 2]:
        return "double"
    raise AssertionError(sizes)


def zero(dimension: int) -> Vector:
    return [Fraction(0) for _ in range(dimension)]


def vector_add_scaled(out: Vector, vector: Vector, scalar: Fraction) -> None:
    for index, value in enumerate(vector):
        out[index] += scalar * value


def vector_difference(first: Vector, second: Vector) -> Vector:
    return [x - y for x, y in zip(first, second)]


def row_times_kernel(row: Vector, kernel: list[Vector]) -> Vector:
    dimension = len(row)
    return [
        sum((row[source] * kernel[source][target] for source in range(dimension)), Fraction(0))
        for target in range(dimension)
    ]


def kernel_times_function(kernel: list[Vector], function: Vector) -> Vector:
    dimension = len(function)
    return [
        sum((kernel[source][target] * function[target] for target in range(dimension)), Fraction(0))
        for source in range(dimension)
    ]


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def split_size(edge: Perm, component: list[int]) -> int:
    x, y = edge_endpoints(edge)
    a, b = sorted((component.index(x), component.index(y)))
    gap = b - a
    return min(gap, len(component) - gap)


def internal_edges(n: int, components: list[list[int]]) -> list[tuple[Perm, int]]:
    answer: list[tuple[Perm, int]] = []
    for color, component in enumerate(components):
        vertices = sorted(component)
        for i, x in enumerate(vertices):
            for y in vertices[i + 1 :]:
                answer.append((transposition(n, x, y), color))
    return answer


def construct_kernel(n: int) -> dict[str, Any]:
    h = cycle_permutation(n, list(range(n)))
    gates = [transposition(n, x, y) for x in range(n) for y in range(x + 1, n)]
    multiplicity: collections.Counter[Perm] = collections.Counter()
    for first in gates:
        for second in gates:
            multiplicity[compose(first, second)] += 1

    completion: dict[Perm, int] = {}
    for product, lifts in multiplicity.items():
        count = minimal_count(compose(inverse(product), h), n - 3)
        if count:
            assert lifts in (2, 3)
            completion[product] = count

    orbit_id: dict[Perm, int] = {}
    orbits: list[list[Perm]] = []
    for product in sorted(completion):
        if product in orbit_id:
            continue
        orbit: list[Perm] = []
        current = product
        while current not in orbit:
            assert current in completion
            orbit.append(current)
            current = theta(current, h)
        assert current == product
        index = len(orbits)
        for state in orbit:
            assert state not in orbit_id
            orbit_id[state] = index
        orbits.append(orbit)

    dimension = len(orbits)
    kernel = [zero(dimension) for _ in range(dimension)]
    for source_index, orbit in enumerate(orbits):
        source = orbit[0]
        denominator = completion[source]
        for target, target_lifts in multiplicity.items():
            if target not in orbit_id:
                continue
            residual = compose(inverse(compose(source, target)), h)
            numerator = target_lifts * minimal_count(residual, n - 5)
            if numerator:
                kernel[source_index][orbit_id[target]] += Fraction(numerator, denominator)
        assert sum(kernel[source_index], Fraction(0)) == 1

    z = n ** (n - 2)
    stationary = [
        Fraction(len(orbit) * multiplicity[orbit[0]] * completion[orbit[0]], z)
        for orbit in orbits
    ]
    assert sum(stationary, Fraction(0)) == 1
    for i in range(dimension):
        for j in range(dimension):
            assert stationary[i] * kernel[i][j] == stationary[j] * kernel[j][i]

    return {
        "h": h,
        "gates": gates,
        "multiplicity": multiplicity,
        "completion": completion,
        "orbits": orbits,
        "orbit_id": orbit_id,
        "kernel": kernel,
        "stationary": stationary,
    }


def residual_pair_decomposition(
    n: int,
    residual: Perm,
    components: list[list[int]],
    exterior_colors: set[int],
    orbit_id: dict[Perm, int],
    product_multiplicity: collections.Counter[Perm],
    dimension: int,
) -> dict[str, Any]:
    """Enumerate literal ordered completion factors and classify them by J."""
    rank = n - len(cycle_lists(residual))
    denominator = minimal_count(residual, rank)
    available = internal_edges(n, components)
    raw_by_j = {j: zero(dimension) for j in range(3)}
    split_raw = {j: collections.defaultdict(lambda: zero(dimension)) for j in (1, 2)}
    split_mass = {j: collections.defaultdict(Fraction) for j in (1, 2)}
    observed_lifts: dict[Perm, set[tuple[Perm, Perm]]] = collections.defaultdict(set)

    for first, first_color in available:
        for second, second_color in available:
            product = compose(first, second)
            completions = minimal_count(compose(inverse(product), residual), rank - 2)
            if not completions:
                continue
            assert product in orbit_id
            observed_lifts[product].add((first, second))
            weight = Fraction(completions, denominator)
            first_ext = first_color in exterior_colors
            second_ext = second_color in exterior_colors
            j = int(first_ext) + int(second_ext)
            raw_by_j[j][orbit_id[product]] += weight

            if j == 1:
                exterior_edge = first if first_ext else second
                exterior_color = first_color if first_ext else second_color
                split = split_size(exterior_edge, components[exterior_color])
                split_raw[j][split][orbit_id[product]] += weight
                split_mass[j][split] += weight
            elif j == 2:
                split = split_size(first, components[first_color])
                split_raw[j][split][orbit_id[product]] += weight
                split_mass[j][split] += weight

    alpha = {j: sum(raw_by_j[j], Fraction(0)) for j in range(3)}
    assert sum(alpha.values(), Fraction(0)) == 1
    conditional_h = {
        j: [value / alpha[j] for value in raw_by_j[j]] for j in range(3)
    }
    for j in range(3):
        assert sum(conditional_h[j], Fraction(0)) == 1

    split_law: dict[int, dict[int, Fraction]] = {1: {}, 2: {}}
    split_conditional: dict[int, dict[int, Vector]] = {1: {}, 2: {}}
    for j in (1, 2):
        for split, mass in split_mass[j].items():
            split_law[j][split] = mass / alpha[j]
            split_conditional[j][split] = [value / mass for value in split_raw[j][split]]
            assert sum(split_conditional[j][split], Fraction(0)) == 1
        assert sum(split_law[j].values(), Fraction(0)) == 1

    lift_counts = collections.Counter()
    for product, lifts in observed_lifts.items():
        expected = product_multiplicity[product]
        assert len(lifts) == expected
        kind = product_kind(product)
        assert (kind, expected) in (("triangle", 3), ("double", 2))
        lift_counts[f"{kind}:{expected}"] += 1

    return {
        "alpha": alpha,
        "H": conditional_h,
        "split_law": split_law,
        "conditional": split_conditional,
        "lift_counts": dict(lift_counts),
    }


def conditioned_borel_weight(d: int, split: int) -> Fraction:
    tau_left = Fraction(split ** (split - 1), math.factorial(split))
    right = d - split
    tau_right = Fraction(right ** (right - 1), math.factorial(right))
    per_chord = Fraction(math.factorial(d - 2), d ** (d - 2)) * tau_left * tau_right
    return d * per_chord


def abel_reconstruction(
    p: dict[int, Fraction],
    q: dict[int, Fraction],
    phi: dict[int, Vector],
    psi: dict[int, Vector],
    maximum: int,
    dimension: int,
) -> tuple[Vector, list[Fraction]]:
    cumulative: list[Fraction] = []
    current = Fraction(0)
    for split in range(1, maximum + 1):
        current += p.get(split, Fraction(0)) - q.get(split, Fraction(0))
        cumulative.append(current)
    assert cumulative[-1] == 0
    result = zero(dimension)
    for split in range(1, maximum):
        gradient = vector_difference(phi[split], phi[split + 1])
        vector_add_scaled(result, gradient, cumulative[split - 1])
    for split, mass in q.items():
        defect = vector_difference(phi[split], psi[split])
        vector_add_scaled(result, defect, mass)
    return result, cumulative


def weighted_inner(first: Vector, second: Vector, stationary: Vector) -> Fraction:
    return sum(
        (x * y / mass for x, y, mass in zip(first, second, stationary)),
        Fraction(0),
    )


def analyze(k: int, frozen_directory: Path) -> dict[str, Any]:
    if k < 3 or k % 2 == 0:
        raise ValueError("k must be odd and at least three")
    n = 3 * k
    built = construct_kernel(n)
    h: Perm = built["h"]
    multiplicity = built["multiplicity"]
    completion = built["completion"]
    orbits: list[list[Perm]] = built["orbits"]
    orbit_id: dict[Perm, int] = built["orbit_id"]
    kernel: list[Vector] = built["kernel"]
    stationary: Vector = built["stationary"]
    dimension = len(orbits)

    source_a = cycle_permutation(n, [0, k, 2 * k])
    source_b = compose(transposition(n, 0, 1), transposition(n, k, 2 * k))
    ai, bi = orbit_id[source_a], orbit_id[source_b]
    assert len(orbits[ai]) == k
    assert len(orbits[bi]) == n

    residual_a = compose(inverse(source_a), h)
    residual_b = compose(inverse(source_b), h)
    components_a = cycle_lists(residual_a)
    components_b = cycle_lists(residual_b)
    middle_a = next(i for i, component in enumerate(components_a) if k in component)
    middle_b = next(i for i, component in enumerate(components_b) if k in component)
    singleton_b = next(component for component in components_b if len(component) == 1)
    assert singleton_b == [0]
    assert set(components_a[middle_a]) == set(components_b[middle_b])

    decomposition_a = residual_pair_decomposition(
        n,
        residual_a,
        components_a,
        set(range(len(components_a))) - {middle_a},
        orbit_id,
        multiplicity,
        dimension,
    )
    decomposition_b = residual_pair_decomposition(
        n,
        residual_b,
        components_b,
        set(range(len(components_b))) - {middle_b, components_b.index(singleton_b)},
        orbit_id,
        multiplicity,
        dimension,
    )

    m = k - 1
    color_denominator = 3 * m * (3 * m - 1)
    expected_alpha = {
        0: Fraction(m * (m - 1), color_denominator),
        1: Fraction(4 * m * m, color_denominator),
        2: Fraction(2 * m * (2 * m - 1), color_denominator),
    }
    assert decomposition_a["alpha"] == expected_alpha
    assert decomposition_b["alpha"] == expected_alpha
    assert decomposition_a["H"][0] == decomposition_b["H"][0]

    reconstructed_rows: dict[str, Vector] = {}
    for label, decomposition, source_index in (
        ("A", decomposition_a, ai),
        ("B", decomposition_b, bi),
    ):
        row = zero(dimension)
        for j in range(3):
            vector_add_scaled(row, decomposition["H"][j], expected_alpha[j])
        assert row == kernel[source_index]
        reconstructed_rows[label] = row

    eta = vector_difference(kernel[bi], kernel[ai])
    merge = zero(dimension)
    for j in (1, 2):
        vector_add_scaled(
            merge,
            vector_difference(decomposition_b["H"][j], decomposition_a["H"][j]),
            expected_alpha[j],
        )
    assert merge == eta

    p = decomposition_b["split_law"][1]
    q = decomposition_a["split_law"][1]
    assert p == decomposition_b["split_law"][2]
    assert q == decomposition_a["split_law"][2]
    assert set(p) == set(range(1, k))
    assert set(q) == set(range(1, (k - 1) // 2 + 1))
    for split, value in p.items():
        assert value == conditioned_borel_weight(2 * k - 1, split)
    for split, value in q.items():
        assert value == conditioned_borel_weight(k, split)
    for split in q:
        assert p[split] < q[split]

    abel_channels: dict[int, Vector] = {}
    cumulative: list[Fraction] | None = None
    for j in (1, 2):
        abel, current_cumulative = abel_reconstruction(
            p,
            q,
            decomposition_b["conditional"][j],
            decomposition_a["conditional"][j],
            k - 1,
            dimension,
        )
        assert abel == vector_difference(decomposition_b["H"][j], decomposition_a["H"][j])
        if cumulative is None:
            cumulative = current_cumulative
        else:
            assert cumulative == current_cumulative
        abel_channels[j] = abel
    assert cumulative is not None
    assert all(value < 0 for value in cumulative[:-1])
    assert cumulative[-1] == 0

    # Posterior score, including the short orbit of A and all n phases.
    posterior = [eta[index] / stationary[index] for index in range(dimension)]
    posterior_db = [
        kernel[index][bi] / stationary[bi] - kernel[index][ai] / stationary[ai]
        for index in range(dimension)
    ]
    assert posterior == posterior_db
    phase_formula: Vector = []
    a_count = completion[source_a]
    b_count = completion[source_b]
    for orbit in orbits:
        s = orbit[0]
        s_count = completion[s]
        a_phase = source_a
        b_phase = source_b
        phase_sum = Fraction(0)
        for _ in range(n):
            c_b = minimal_count(compose(inverse(compose(s, b_phase)), h), n - 5)
            c_a = minimal_count(compose(inverse(compose(s, a_phase)), h), n - 5)
            phase_sum += Fraction(c_b, b_count) - Fraction(c_a, a_count)
            a_phase = theta(a_phase, h)
            b_phase = theta(b_phase, h)
        phase_formula.append(Fraction(n ** (n - 3), s_count) * phase_sum)
    assert phase_formula == posterior

    image = row_times_kernel(eta, kernel)
    smoothed_score = kernel_times_function(kernel, posterior)
    assert image == [mass * value for mass, value in zip(stationary, smoothed_score)]
    row_a_two = row_times_kernel(kernel[ai], kernel)
    row_b_two = row_times_kernel(kernel[bi], kernel)
    assert image == vector_difference(row_b_two, row_a_two)

    ba2 = weighted_inner(image, image, stationary)
    aa = weighted_inner(row_a_two, row_a_two, stationary)
    bb = weighted_inner(row_b_two, row_b_two, stationary)
    ab = weighted_inner(row_a_two, row_b_two, stationary)
    k4_aa = stationary[ai] * aa
    k4_bb = stationary[bi] * bb
    k4_ab = stationary[bi] * ab
    k4_ba = stationary[ai] * ab
    contrast = (
        k4_bb / stationary[bi]
        + k4_aa / stationary[ai]
        - k4_ab / stationary[bi]
        - k4_ba / stationary[ai]
    )
    assert contrast == ba2

    channel_images: dict[int, Vector] = {
        j: row_times_kernel(abel_channels[j], kernel) for j in (1, 2)
    }
    norm1 = weighted_inner(channel_images[1], channel_images[1], stationary)
    norm2 = weighted_inner(channel_images[2], channel_images[2], stationary)
    cross = weighted_inner(channel_images[1], channel_images[2], stationary)
    assert cross > 0
    reconstructed_ba2 = (
        expected_alpha[1] ** 2 * norm1
        + expected_alpha[2] ** 2 * norm2
        + 2 * expected_alpha[1] * expected_alpha[2] * cross
    )
    assert reconstructed_ba2 == ba2

    one_step_tv = sum((abs(value) for value in eta), Fraction(0)) / 2
    two_step_tv = sum((abs(value) for value in image), Fraction(0)) / 2

    frozen_path = frozen_directory / f"balanced_abel_exact_k{k}.json"
    frozen = json.loads(frozen_path.read_text())["results"][0]
    comparisons = {
        "one_step_TV": fraction_text(one_step_tv) == frozen["one_step_TV"],
        "two_step_TV": fraction_text(two_step_tv) == frozen["two_step_TV"],
        "k_fourth_BA2_L2": fraction_text(k ** 4 * ba2) == frozen["k_fourth_BA2_L2"],
        "cross_inner_product": fraction_text(cross)
        == frozen["two_channel_L2_exact"]["cross_inner_product"],
        "source_orbit_sizes": {"A": len(orbits[ai]), "B": len(orbits[bi])}
        == frozen["source_orbit_sizes"],
        "interleaving_probabilities": {
            "J0_common_middle_middle": fraction_text(expected_alpha[0]),
            "J1_exterior_middle": fraction_text(expected_alpha[1]),
            "J2_exterior_exterior": fraction_text(expected_alpha[2]),
        }
        == frozen["interleaving_probabilities"],
    }
    assert all(comparisons.values())

    return {
        "k": k,
        "n": n,
        "quotient_states": dimension,
        "source_orbit_sizes": {"A": len(orbits[ai]), "B": len(orbits[bi])},
        "source_stationary_masses": {
            "A": fraction_text(stationary[ai]),
            "B": fraction_text(stationary[bi]),
        },
        "residual_component_sizes": {
            "A": sorted(len(component) for component in components_a),
            "B": sorted(len(component) for component in components_b),
        },
        "alpha": {str(j): fraction_text(value) for j, value in expected_alpha.items()},
        "micro_lift_counts_A": decomposition_a["lift_counts"],
        "micro_lift_counts_B": decomposition_b["lift_counts"],
        "common_J0_exact": True,
        "full_row_reconstruction_exact": True,
        "posterior_detailed_balance_exact": True,
        "all_n_phase_formula_exact": True,
        "split_conditionals_normalized_exact": True,
        "conditioned_borel_formula_exact": True,
        "conditioned_borel_common_support_strict_sign": True,
        "abel_J1_exact": True,
        "abel_J2_exact": True,
        "cumulative_D": [fraction_text(value) for value in cumulative],
        "one_step_TV": fraction_text(one_step_tv),
        "two_step_TV": fraction_text(two_step_tv),
        "k_fourth_BA2_L2": fraction_text(k ** 4 * ba2),
        "K4_entries": {
            "AA": fraction_text(k4_aa),
            "BB": fraction_text(k4_bb),
            "AB": fraction_text(k4_ab),
            "BA": fraction_text(k4_ba),
        },
        "K4_denominated_contrast": fraction_text(contrast),
        "BA2_stationary_norm": fraction_text(ba2),
        "K4_contrast_equals_BA2": True,
        "channel_L2": {
            "J1_norm_squared": fraction_text(norm1),
            "J2_norm_squared": fraction_text(norm2),
            "cross_inner_product": fraction_text(cross),
            "cross_strictly_positive": True,
            "weighted_reconstruction": fraction_text(reconstructed_ba2),
        },
        "frozen_exact_comparisons": comparisons,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", nargs="+", type=int, required=True)
    parser.add_argument("--frozen-directory", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    payload = {
        "status": "fresh_exact_identity_audit_not_asymptotic_evidence",
        "target": "uniform minimal long-cycle pair-product cyclic quotient",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "claim_tested": "M91 balanced posterior/Borel-Abel reduction and finite certificates",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
        "results": [analyze(k, arguments.frozen_directory) for k in arguments.k],
    }
    arguments.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

