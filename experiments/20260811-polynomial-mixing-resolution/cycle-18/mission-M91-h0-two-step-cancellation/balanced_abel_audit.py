#!/usr/bin/env python3
"""Exact finite audit of the M91 balanced Borel--Abel decomposition.

The calculation verifies identities only; it is not asymptotic evidence.
All ordered-factor, product-lift, cyclic-orbit, and interleaving
multiplicities are retained over ``Fraction``.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import platform
import subprocess
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
M83_PATH = (
    ROOT
    / "experiments/20260811-polynomial-mixing-resolution/cycle-17/"
      "mission-M83-endpoint-sharing-influence/influence_diagnostic.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M = load_module("m83_influence", M83_PATH)
Perm = tuple[int, ...]
Vector = list[Fraction]


def oriented_cycle(n: int, entries: tuple[int, ...]) -> Perm:
    out = list(range(n))
    for a, b in zip(entries, entries[1:] + entries[:1]):
        out[a] = b
    return tuple(out)


def cycle_perm(n: int, entries: list[int]) -> Perm:
    return oriented_cycle(n, tuple(entries))


def zero(q: int) -> Vector:
    return [Fraction(0) for _ in range(q)]


def add_scaled(out: Vector, vector: Vector, scale: Fraction) -> None:
    for index, value in enumerate(vector):
        out[index] += scale * value


def difference(first: Vector, second: Vector) -> Vector:
    return [a - b for a, b in zip(first, second)]


def vector_equal(first: Vector, second: Vector) -> bool:
    return all(a == b for a, b in zip(first, second))


def total(vector: Vector) -> Fraction:
    return sum(vector, Fraction(0))


def tv(vector: Vector) -> Fraction:
    return sum((abs(value) for value in vector), Fraction(0)) / 2


def matmul_row(vector: Vector, kernel: list[list[Fraction]]) -> Vector:
    q = len(vector)
    return [
        sum((vector[source] * kernel[source][target] for source in range(q)), Fraction(0))
        for target in range(q)
    ]


def smaller_split(edge: Perm, component_cycle: list[int]) -> int:
    endpoints = sorted(M.edge_of(edge))
    positions = sorted(component_cycle.index(endpoint) for endpoint in endpoints)
    gap = positions[1] - positions[0]
    return min(gap, len(component_cycle) - gap)


def internal_edges(n: int, component_cycle: list[int]) -> list[Perm]:
    vertices = sorted(component_cycle)
    return [
        M.edge_perm(n, vertices[i], vertices[j])
        for i in range(len(vertices))
        for j in range(i + 1, len(vertices))
    ]


def first_edge_distribution(n: int, component_cycle: list[int]) -> dict[Perm, Fraction]:
    component = cycle_perm(n, component_cycle)
    d = len(component_cycle)
    denominator = d ** (d - 2)
    out: dict[Perm, Fraction] = {}
    for edge in internal_edges(n, component_cycle):
        numerator = M.count_minimal(M.mul(edge, component), d - 2)
        if numerator:
            out[edge] = Fraction(numerator, denominator)
    assert sum(out.values(), Fraction(0)) == 1
    return out


def product_pushforward(
    first: dict[Perm, Fraction],
    second: dict[Perm, Fraction],
    oid: dict[Perm, int],
    q: int,
) -> Vector:
    out = zero(q)
    for a, pa in first.items():
        for b, pb in second.items():
            out[oid[M.mul(a, b)]] += pa * pb
    assert total(out) == 1
    return out


def pair_law_conditioned_on_first_split(
    n: int,
    residual: Perm,
    initial_components: list[list[int]],
    oid: dict[Perm, int],
    q: int,
) -> tuple[dict[int, Fraction], dict[int, Vector]]:
    """First-two-factor product, stratified by the first edge's split."""
    rank = n - len(M.cycles(residual))
    denominator = M.count_minimal(residual, rank)
    gates = [edge for component in initial_components for edge in internal_edges(n, component)]
    mass: dict[int, Fraction] = defaultdict(Fraction)
    vectors: dict[int, Vector] = defaultdict(lambda: zero(q))
    component_for_vertex = {
        vertex: component for component in initial_components for vertex in component
    }
    for first in gates:
        endpoints = list(M.edge_of(first))
        component = component_for_vertex[endpoints[0]]
        assert component_for_vertex[endpoints[1]] is component
        split = smaller_split(first, component)
        after_first = M.mul(first, residual)
        after_components = [c for c in M.cycles(after_first) if len(c) > 1]
        second_gates = [
            edge for component2 in after_components for edge in internal_edges(n, component2)
        ]
        for second in second_gates:
            product = M.mul(first, second)
            numerator = M.count_minimal(M.mul(M.inv(product), residual), rank - 2)
            if not numerator:
                continue
            probability = Fraction(numerator, denominator)
            mass[split] += probability
            vectors[split][oid[product]] += probability
    assert sum(mass.values(), Fraction(0)) == 1
    conditional: dict[int, Vector] = {}
    for split, vector in vectors.items():
        conditional[split] = [value / mass[split] for value in vector]
        assert total(conditional[split]) == 1
    return dict(mass), conditional


def mixture_conditionals(
    components: list[list[int]],
    edge_laws: list[dict[Perm, Fraction]],
    other_edge_law: dict[Perm, Fraction] | None,
    oid: dict[Perm, int],
    q: int,
) -> tuple[dict[int, Fraction], dict[int, Vector]]:
    """Equal mixture of component edge laws, optionally tensored with another edge."""
    assert len(components) == len(edge_laws)
    count = len(components)
    masses: dict[int, Fraction] = defaultdict(Fraction)
    raw: dict[int, Vector] = defaultdict(lambda: zero(q))
    for component, edge_law in zip(components, edge_laws):
        for edge, probability in edge_law.items():
            split = smaller_split(edge, component)
            first_probability = Fraction(1, count) * probability
            if other_edge_law is None:
                raw[split][oid[edge]] += first_probability
                masses[split] += first_probability
            else:
                for other, other_probability in other_edge_law.items():
                    value = first_probability * other_probability
                    raw[split][oid[M.mul(edge, other)]] += value
                    masses[split] += value
    assert sum(masses.values(), Fraction(0)) == 1
    conditional = {
        split: [value / masses[split] for value in vector]
        for split, vector in raw.items()
    }
    for vector in conditional.values():
        assert total(vector) == 1
    return dict(masses), conditional


def unconditional(masses: dict[int, Fraction], conditional: dict[int, Vector], q: int) -> Vector:
    out = zero(q)
    for split, probability in masses.items():
        add_scaled(out, conditional[split], probability)
    assert total(out) == 1
    return out


def abel_vector(
    p: dict[int, Fraction],
    qmass: dict[int, Fraction],
    phi: dict[int, Vector],
    psi: dict[int, Vector],
    maximum: int,
    dimension: int,
) -> tuple[Vector, list[Fraction]]:
    cumulative: list[Fraction] = []
    running = Fraction(0)
    for split in range(1, maximum + 1):
        running += p.get(split, Fraction(0)) - qmass.get(split, Fraction(0))
        cumulative.append(running)
    assert cumulative[-1] == 0

    out = zero(dimension)
    for split in range(1, maximum):
        add_scaled(out, difference(phi[split], phi[split + 1]), cumulative[split - 1])
    for split, probability in qmass.items():
        add_scaled(out, difference(phi[split], psi[split]), probability)
    return out, cumulative


def frac(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def analyze(k: int) -> dict[str, Any]:
    if k < 3 or k % 2 == 0:
        raise ValueError("k must be odd and at least three")
    n = 3 * k
    h, orbits, kernel, squared, pi, _ = M.build(n, True)
    q = len(orbits)
    oid = {state: index for index, orbit in enumerate(orbits) for state in orbit}

    source_a = oriented_cycle(n, (0, k, 2 * k))
    source_b = M.mul(M.edge_perm(n, 0, 1), M.edge_perm(n, k, 2 * k))
    ai = oid[source_a]
    bi = oid[source_b]
    residual_a = M.mul(M.inv(source_a), h)
    residual_b = M.mul(M.inv(source_b), h)

    components_a = M.cycles(residual_a)
    components_b = M.cycles(residual_b)
    cminus = next(c for c in components_a if 0 in c)
    middle = next(c for c in components_a if k in c)
    cplus = next(c for c in components_a if 2 * k in c)
    singleton = next(c for c in components_b if len(c) == 1)
    long_cycle = next(c for c in components_b if len(c) == 2 * k - 1)
    middle_b = next(c for c in components_b if len(c) == k)
    assert singleton == [0]
    assert set(middle_b) == set(middle)

    nu_minus = first_edge_distribution(n, cminus)
    nu_middle = first_edge_distribution(n, middle)
    nu_plus = first_edge_distribution(n, cplus)
    nu_long = first_edge_distribution(n, long_cycle)

    # J=1: one exterior and one middle factor.  The B and A conditional laws
    # share the same middle-edge distribution.
    p1, phi1 = mixture_conditionals(
        [long_cycle], [nu_long], nu_middle, oid, q
    )
    q1mass, psi1 = mixture_conditionals(
        [cminus, cplus], [nu_minus, nu_plus], nu_middle, oid, q
    )
    h1_b = unconditional(p1, phi1, q)
    h1_a = unconditional(q1mass, psi1, q)

    # J=2: both factors exterior.  Keep their order and all product-lift
    # multiplicities by enumerating the conditional second factor exactly.
    residual_long = cycle_perm(n, long_cycle)
    residual_separate = M.mul(cycle_perm(n, cminus), cycle_perm(n, cplus))
    p2, phi2 = pair_law_conditioned_on_first_split(
        n, residual_long, [long_cycle], oid, q
    )
    q2mass, psi2 = pair_law_conditioned_on_first_split(
        n, residual_separate, [cminus, cplus], oid, q
    )
    h2_b = unconditional(p2, phi2, q)
    h2_a = unconditional(q2mass, psi2, q)

    assert p1 == p2
    assert q1mass == q2mass
    p = p1
    qmass = q1mass
    maximum = k - 1
    assert set(p) == set(range(1, maximum + 1))
    assert set(qmass) == set(range(1, (k - 1) // 2 + 1))

    # The common J=0 law consists of two middle-component factors.
    _, phi0 = pair_law_conditioned_on_first_split(
        n, cycle_perm(n, middle), [middle], oid, q
    )
    # Its split mixture is the q law because the middle component has size k.
    h0 = unconditional(qmass, phi0, q)

    m = k - 1
    denominator = (3 * m) * (3 * m - 1)
    alpha0 = Fraction(m * (m - 1), denominator)
    alpha1 = Fraction(4 * m * m, denominator)
    alpha2 = Fraction(2 * m * (2 * m - 1), denominator)
    assert alpha0 + alpha1 + alpha2 == 1

    reconstructed_a = zero(q)
    reconstructed_b = zero(q)
    for out, pieces in (
        (reconstructed_a, ((alpha0, h0), (alpha1, h1_a), (alpha2, h2_a))),
        (reconstructed_b, ((alpha0, h0), (alpha1, h1_b), (alpha2, h2_b))),
    ):
        for coefficient, vector in pieces:
            add_scaled(out, vector, coefficient)
    assert vector_equal(reconstructed_a, kernel[ai])
    assert vector_equal(reconstructed_b, kernel[bi])

    eta = difference(kernel[bi], kernel[ai])
    merge_defect = zero(q)
    add_scaled(merge_defect, difference(h1_b, h1_a), alpha1)
    add_scaled(merge_defect, difference(h2_b, h2_a), alpha2)
    assert vector_equal(eta, merge_defect)

    abel1, cumulative1 = abel_vector(p, qmass, phi1, psi1, maximum, q)
    abel2, cumulative2 = abel_vector(p, qmass, phi2, psi2, maximum, q)
    assert cumulative1 == cumulative2
    assert vector_equal(abel1, difference(h1_b, h1_a))
    assert vector_equal(abel2, difference(h2_b, h2_a))
    abel_eta = zero(q)
    add_scaled(abel_eta, abel1, alpha1)
    add_scaled(abel_eta, abel2, alpha2)
    assert vector_equal(abel_eta, eta)

    image = matmul_row(eta, kernel)
    abel_image = matmul_row(abel_eta, kernel)
    direct_image = difference(squared[bi], squared[ai])
    assert vector_equal(image, abel_image)
    assert vector_equal(image, direct_image)

    channel1 = difference(h1_b, h1_a)
    channel2 = difference(h2_b, h2_a)
    channel1_image = matmul_row(channel1, kernel)
    channel2_image = matmul_row(channel2, kernel)
    channel1_l2 = sum(
        (channel1_image[t] ** 2 / pi[t] for t in range(q)), Fraction(0)
    )
    channel2_l2 = sum(
        (channel2_image[t] ** 2 / pi[t] for t in range(q)), Fraction(0)
    )
    channel_cross = sum(
        (channel1_image[t] * channel2_image[t] / pi[t] for t in range(q)),
        Fraction(0),
    )
    image_l2 = sum((image[t] ** 2 / pi[t] for t in range(q)), Fraction(0))
    l2_reconstruction = (
        alpha1 ** 2 * channel1_l2
        + alpha2 ** 2 * channel2_l2
        + 2 * alpha1 * alpha2 * channel_cross
    )
    assert l2_reconstruction == image_l2

    # Check the exact conditioned-Borel formula for the scalar split laws.
    def tau(d: int) -> Fraction:
        return Fraction(d ** (d - 1), math.factorial(d))

    def w(d: int, split: int) -> Fraction:
        return Fraction(math.factorial(d - 2), d ** (d - 2)) * tau(split) * tau(d - split)

    for split, probability in p.items():
        assert probability == (2 * k - 1) * w(2 * k - 1, split)
    for split, probability in qmass.items():
        assert probability == k * w(k, split)

    return {
        "k": k,
        "n": n,
        "quotient_states": q,
        "source_orbits": {"A": ai, "B": bi},
        "source_orbit_sizes": {"A": len(orbits[ai]), "B": len(orbits[bi])},
        "residual_component_sizes": {
            "A": sorted(map(len, components_a)),
            "B": sorted(map(len, components_b)),
        },
        "interleaving_probabilities": {
            "J0_common_middle_middle": frac(alpha0),
            "J1_exterior_middle": frac(alpha1),
            "J2_exterior_exterior": frac(alpha2),
        },
        "p_long_cycle_split": {str(s): frac(v) for s, v in sorted(p.items())},
        "q_two_k_cycles_split": {str(s): frac(v) for s, v in sorted(qmass.items())},
        "borel_abel_cumulative": [frac(value) for value in cumulative1],
        "common_J0_exactly_cancelled": True,
        "full_rows_reconstructed_exactly": True,
        "merge_defect_identity_exact": True,
        "one_edge_abel_identity_exact": True,
        "two_edge_abel_identity_exact": True,
        "post_K_abel_identity_exact": True,
        "eta_mass": frac(total(eta)),
        "one_step_TV": frac(tv(eta)),
        "two_step_TV": frac(tv(image)),
        "k_squared_two_step_TV": frac(k * k * tv(image)),
        "k_fourth_BA2_L2": frac(k ** 4 * image_l2),
        "two_channel_L2_exact": {
            "channel1_norm_squared": frac(channel1_l2),
            "channel2_norm_squared": frac(channel2_l2),
            "cross_inner_product": frac(channel_cross),
            "cross_positive": channel_cross > 0,
            "correlation_squared": frac(
                channel_cross ** 2 / (channel1_l2 * channel2_l2)
            ),
            "alpha1_squared_channel1": frac(alpha1 ** 2 * channel1_l2),
            "alpha2_squared_channel2": frac(alpha2 ** 2 * channel2_l2),
            "twice_alpha1_alpha2_cross": frac(
                2 * alpha1 * alpha2 * channel_cross
            ),
            "reconstructed": frac(l2_reconstruction),
        },
        "separate_abel_channel_image_TV": {
            "alpha1_one_edge": frac(alpha1 * tv(matmul_row(abel1, kernel))),
            "alpha2_two_edge": frac(alpha2 * tv(matmul_row(abel2, kernel))),
            "triangle_sum": frac(
                alpha1 * tv(matmul_row(abel1, kernel))
                + alpha2 * tv(matmul_row(abel2, kernel))
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", nargs="+", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "status": "exact_finite_identity_falsifier_not_asymptotic_evidence",
        "target": "uniform minimal long-cycle H0 pair-product quotient",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "claim_tested": "balanced common-component cancellation and Borel-Abel identity",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
        "results": [analyze(k) for k in args.k],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
