#!/usr/bin/env python3
"""Sole compact M285 test: exact k=3 signed spectral dominance.

No predecessor code or data is imported.  The script reconstructs both
normalized source channels, the rooted-owner response, and its
diagonal-repaired autocorrelation at all circular lags.  A negative exact
quadratic form refutes only signed PSD dominance, not OCI.
"""

from __future__ import annotations

import json
import math
import platform
import subprocess
import sys
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path


Perm = tuple[int, ...]


def mul(p: Perm, q: Perm) -> Perm:
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


def tr(n: int, x: int, y: int) -> Perm:
    return cyc(n, (x, y))


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


def completion(p: Perm, length: int) -> Fraction:
    cs = cycles(p)
    if len(p) - len(cs) != length:
        return Fraction(0)
    value = Fraction(math.factorial(length))
    for component in cs:
        value *= tau(len(component))
    assert value.denominator == 1
    return value


def internal_edges(n: int, component: tuple[int, ...]):
    for x, y in combinations(sorted(component), 2):
        yield tr(n, x, y)


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def source_law(k: int, label: str):
    n = 3 * k
    h = cyc(n, tuple(range(n)))
    if label == "A":
        source = cyc(n, (0, k, 2 * k))
    elif label == "B":
        source = mul(tr(n, 0, 1), tr(n, k, 2 * k))
    else:
        raise ValueError(label)
    residual = mul(inv(source), h)
    initial = cycles(residual)
    original_owner = {
        vertex: i for i, component in enumerate(initial) for vertex in component
    }
    middle = original_owner[k]
    rank = n - len(initial)
    denominator = completion(residual, rank)
    product_mass: dict[tuple[int, Perm], Fraction] = defaultdict(Fraction)
    channel_mass: dict[int, Fraction] = defaultdict(Fraction)
    kind_mass: dict[tuple[int, str], Fraction] = defaultdict(Fraction)
    raw_atoms = 0

    for first_component, component in enumerate(initial):
        if len(component) < 2:
            continue
        for first in internal_edges(n, component):
            after_first = mul(first, residual)
            for after_component in cycles(after_first):
                if len(after_component) < 2:
                    continue
                second_component = original_owner[after_component[0]]
                assert all(
                    original_owner[x] == second_component for x in after_component
                )
                for second in internal_edges(n, after_component):
                    numerator = completion(mul(second, after_first), rank - 2)
                    if not numerator:
                        continue
                    probability = numerator / denominator
                    channel = int(first_component != middle) + int(
                        second_component != middle
                    )
                    product = mul(first, second)
                    support = sum(product[x] != x for x in range(n))
                    kind = "T" if support == 3 else "D"
                    assert support in (3, 4)
                    product_mass[(channel, product)] += probability
                    channel_mass[channel] += probability
                    kind_mass[(channel, kind)] += probability
                    raw_atoms += 1
    assert sum(channel_mass.values(), Fraction(0)) == 1
    return product_mass, dict(channel_mass), dict(kind_mass), raw_atoms


def state_profiles(n: int, h: Perm, s: Perm):
    residual = mul(inv(s), h)
    cs = cycles(residual)
    assert len(cs) == 3
    owner = {vertex: i for i, component in enumerate(cs) for vertex in component}
    sizes = tuple(map(len, cs))
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
    assert all(delta[i] >= 0 for i, d in enumerate(sizes) if d >= 3)
    field = [
        a[o] if o is not None else Fraction(0)
        for o in generic
    ]

    repaired: list[Fraction] = []
    literal: list[Fraction] = []
    for ell in range(n):
        rank_one = sum(
            (field[r] * field[(r + ell) % n] for r in range(n)), Fraction(0)
        )
        correction = Fraction(0)
        direct = Fraction(0)
        for r in range(n):
            i = generic[r]
            j = generic[(r + ell) % n]
            if i is None or j is None:
                continue
            if i == j:
                direct += b[i]
            else:
                direct += a[i] * a[j]
        for i, d in enumerate(sizes):
            if d < 3:
                continue
            overlap = sum(
                generic[r] == i and generic[(r + ell) % n] == i
                for r in range(n)
            )
            correction += delta[i] * overlap
        repaired.append(rank_one + correction)
        literal.append(direct)
    for ell in range(2, n - 1):
        assert repaired[ell] == literal[ell]
    assert all(repaired[ell] == repaired[(-ell) % n] for ell in range(n))
    return tuple(repaired), tuple(literal), sizes


def quadratic_form(sequence: list[Fraction], vector: list[int]) -> Fraction:
    n = len(sequence)
    return sum(
        (
            Fraction(vector[i] * vector[j]) * sequence[(j - i) % n]
            for i in range(n)
            for j in range(n)
        ),
        Fraction(0),
    )


def rational_psd_witness(sequence: list[Fraction]):
    n = len(sequence)
    approximate = [
        sum(
            float(sequence[ell]) * math.cos(2 * math.pi * frequency * ell / n)
            for ell in range(n)
        )
        for frequency in range(n)
    ]
    order = sorted(range(n), key=approximate.__getitem__)
    for frequency in order:
        for mode in ("cos", "sin"):
            for scale in (10, 100, 1000, 10000):
                if mode == "cos":
                    vector = [
                        round(scale * math.cos(2 * math.pi * frequency * r / n))
                        for r in range(n)
                    ]
                else:
                    vector = [
                        round(scale * math.sin(2 * math.pi * frequency * r / n))
                        for r in range(n)
                    ]
                if not any(vector):
                    continue
                value = quadratic_form(sequence, vector)
                if value < 0:
                    return {
                        "frequency": frequency,
                        "mode": mode,
                        "scale": scale,
                        "vector": vector,
                        "quadratic_form_exact": qstr(value),
                        "quadratic_form_float": float(value),
                        "approximate_eigenvalue": approximate[frequency],
                    }, approximate
    return None, approximate


def main() -> None:
    if len(sys.argv) != 3 or sys.argv[1] != "--output":
        raise SystemExit("usage: psd_obstruction_k3.py --output PATH")
    output = Path(sys.argv[2])
    k = 3
    n = 9
    h = cyc(n, tuple(range(n)))
    laws = {}
    channel_masses = {}
    kind_masses = {}
    raw_atoms = {}
    for label in ("A", "B"):
        laws[label], channel_masses[label], kind_masses[label], raw_atoms[label] = (
            source_law(k, label)
        )

    m = k - 1
    denominator = 3 * m * (3 * m - 1)
    alpha = {
        0: Fraction(m * (m - 1), denominator),
        1: Fraction(4 * m * m, denominator),
        2: Fraction(2 * m * (2 * m - 1), denominator),
    }
    for label in ("A", "B"):
        assert all(channel_masses[label][j] == alpha[j] for j in range(3))

    states = {product for law in laws.values() for (_, product) in law}
    profiles = {s: state_profiles(n, h, s) for s in states}
    signed_sequences: dict[int, list[Fraction]] = {}
    literal_sequences: dict[int, list[Fraction]] = {}
    beta_signs = {}
    witnesses = {}
    eigenvalues = {}
    for channel in (1, 2):
        beta = {
            s: (
                laws["B"].get((channel, s), Fraction(0))
                - laws["A"].get((channel, s), Fraction(0))
            ) / alpha[channel]
            for s in states
        }
        assert sum(beta.values(), Fraction(0)) == 0
        beta_signs[channel] = {
            "positive": sum(value > 0 for value in beta.values()),
            "negative": sum(value < 0 for value in beta.values()),
            "zero": sum(value == 0 for value in beta.values()),
        }
        repaired = [
            sum((beta[s] * profiles[s][0][ell] for s in states), Fraction(0))
            for ell in range(n)
        ]
        literal = [
            sum((beta[s] * profiles[s][1][ell] for s in states), Fraction(0))
            for ell in range(n)
        ]
        assert all(
            repaired[ell] == literal[ell] for ell in range(2, n - 1)
        )
        assert all(
            repaired[ell] == repaired[(-ell) % n] for ell in range(n)
        )
        assert all(literal[ell] > 0 for ell in range(2, n - 1))
        signed_sequences[channel] = repaired
        literal_sequences[channel] = literal
        witnesses[channel], approximate = rational_psd_witness(repaired)
        eigenvalues[channel] = approximate

    theta = Fraction(6 * (k - 1), k * (2 * k - 3) * (2 * k - 1))
    eta_triangle = {}
    for channel in (1, 2):
        eta_triangle[channel] = (
            kind_masses["B"].get((channel, "T"), Fraction(0))
            - kind_masses["A"].get((channel, "T"), Fraction(0))
        ) / alpha[channel]
    assert eta_triangle[1] == 0 and eta_triangle[2] == theta

    payload = {
        "status": "sole compact exact PSD-dominance falsifier; OCI remains open",
        "target": "M285 signed channel expectation of diagonal-repaired owner autocorrelation",
        "scope": "exactly k=3, n=9; no rank scan",
        "convention": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "imports_predecessor_code_or_data": False,
        "raw_atom_counts": raw_atoms,
        "distinct_supported_products": len(states),
        "alpha": {str(j): qstr(alpha[j]) for j in range(3)},
        "beta_sign_counts": {
            str(j): beta_signs[j] for j in (1, 2)
        },
        "eta_triangle": {str(j): qstr(eta_triangle[j]) for j in (1, 2)},
        "theta_k": qstr(theta),
        "admissible_owner_equals_repaired_exact": True,
        "admissible_OCI_entries_strictly_positive_finite_only": True,
        "signed_repaired_sequences": {
            str(j): [qstr(value) for value in signed_sequences[j]]
            for j in (1, 2)
        },
        "signed_literal_sequences": {
            str(j): [qstr(value) for value in literal_sequences[j]]
            for j in (1, 2)
        },
        "approximate_circulant_eigenvalues": {
            str(j): eigenvalues[j] for j in (1, 2)
        },
        "negative_exact_quadratic_witness": {
            str(j): witnesses[j] for j in (1, 2)
        },
        "signed_PSD_dominance_survives_k3": all(
            witnesses[j] is None for j in (1, 2)
        ),
        "OCI_inference": False,
        "gap_mixing_terminal_inference": False,
    }
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "k": k,
        "witnesses": {str(j): witnesses[j] for j in (1, 2)},
        "OCI": "unresolved",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
