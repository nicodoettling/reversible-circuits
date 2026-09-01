#!/usr/bin/env python3
"""Clean-room exact audit of the M285 coefficient and PSD claims.

This file imports no predecessor code or data.  It reconstructs the two
conditioned source laws from minimal-factorization completion counts, derives
the beta coefficients a second way, checks the cyclic-composition owner
parameterization, and evaluates the prescribed k=3 quadratic witness.
"""

from __future__ import annotations

import json
import math
import platform
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations


Perm = tuple[int, ...]


def compose(p: Perm, q: Perm) -> Perm:
    """Return p q, so (p q)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    answer = [0] * len(p)
    for x, y in enumerate(p):
        answer[y] = x
    return tuple(answer)


def cycle(n: int, vertices: tuple[int, ...]) -> Perm:
    answer = list(range(n))
    if len(vertices) > 1:
        for x, y in zip(vertices, vertices[1:] + vertices[:1]):
            answer[x] = y
    return tuple(answer)


def transposition(n: int, x: int, y: int) -> Perm:
    return cycle(n, (x, y))


def cycle_components(p: Perm) -> tuple[tuple[int, ...], ...]:
    unseen = set(range(len(p)))
    answer = []
    while unseen:
        root = min(unseen)
        component = []
        x = root
        while x in unseen:
            unseen.remove(x)
            component.append(x)
            x = p[x]
        answer.append(tuple(component))
    return tuple(answer)


def transposition_rank(p: Perm) -> int:
    return len(p) - len(cycle_components(p))


@lru_cache(maxsize=None)
def tau(d: int) -> Fraction:
    if d < 1:
        return Fraction(0)
    if d == 1:
        return Fraction(1)
    return Fraction(d ** (d - 2), math.factorial(d - 1))


def completion_count(p: Perm, length: int) -> Fraction:
    if transposition_rank(p) != length:
        return Fraction(0)
    answer = Fraction(math.factorial(length))
    for component in cycle_components(p):
        answer *= tau(len(component))
    assert answer.denominator == 1
    return answer


def internal_edges(n: int, vertices: tuple[int, ...]):
    for x, y in combinations(sorted(vertices), 2):
        yield transposition(n, x, y)


def all_transpositions(n: int) -> tuple[Perm, ...]:
    return tuple(
        transposition(n, x, y)
        for x, y in combinations(range(n), 2)
    )


def support_size(p: Perm) -> int:
    return sum(p[x] != x for x in range(len(p)))


def product_kind(p: Perm) -> str:
    size = support_size(p)
    assert size in (3, 4)
    return "T" if size == 3 else "D"


def ordered_pair_products(n: int):
    multiplicity: dict[Perm, int] = defaultdict(int)
    for first in all_transpositions(n):
        for second in all_transpositions(n):
            product = compose(first, second)
            if support_size(product) in (3, 4):
                multiplicity[product] += 1
    assert all(
        count == (3 if product_kind(product) == "T" else 2)
        for product, count in multiplicity.items()
    )
    return dict(multiplicity)


def source_pair_law(k: int, label: str):
    """Unconditional first-two-factor product law, marked by color channel."""
    n = 3 * k
    h = cycle(n, tuple(range(n)))
    if label == "A":
        source = cycle(n, (0, k, 2 * k))
    elif label == "B":
        source = compose(
            transposition(n, 0, 1), transposition(n, k, 2 * k)
        )
    else:
        raise ValueError(label)

    residual = compose(inverse(source), h)
    original = cycle_components(residual)
    owner = {
        vertex: index
        for index, component in enumerate(original)
        for vertex in component
    }
    middle = owner[k]
    rank = transposition_rank(residual)
    denominator = completion_count(residual, rank)
    product_mass: dict[tuple[int, Perm], Fraction] = defaultdict(Fraction)
    channel_mass: dict[int, Fraction] = defaultdict(Fraction)
    kind_mass: dict[tuple[int, str], Fraction] = defaultdict(Fraction)

    for first_owner, component in enumerate(original):
        for first in internal_edges(n, component):
            after_first = compose(first, residual)
            for child in cycle_components(after_first):
                second_owner = owner[child[0]]
                assert all(owner[x] == second_owner for x in child)
                for second in internal_edges(n, child):
                    weight = (
                        completion_count(compose(second, after_first), rank - 2)
                        / denominator
                    )
                    if not weight:
                        continue
                    channel = int(first_owner != middle) + int(
                        second_owner != middle
                    )
                    product = compose(first, second)
                    kind = product_kind(product)
                    product_mass[(channel, product)] += weight
                    channel_mass[channel] += weight
                    kind_mass[(channel, kind)] += weight

    assert sum(channel_mass.values(), Fraction(0)) == 1
    return dict(product_mass), dict(channel_mass), dict(kind_mass)


def first_edge_law(n: int, vertices: tuple[int, ...]):
    d = len(vertices)
    positions = {vertex: index for index, vertex in enumerate(vertices)}
    answer = {}
    for x, y in combinations(vertices, 2):
        cut = (positions[y] - positions[x]) % d
        edge = transposition(n, x, y)
        answer[edge] = tau(cut) * tau(d - cut) / ((d - 1) * tau(d))
    assert sum(answer.values(), Fraction(0)) == 1
    return answer


def explicit_beta_coefficients(k: int, pair_multiplicity: dict[Perm, int]):
    """Derive beta_1 and beta_2 from the displayed normalized laws."""
    n = 3 * k
    left_vertices = tuple(range(1, k)) + tuple(range(2 * k, 3 * k))
    middle_vertices = tuple(range(k, 2 * k))
    minus_vertices = tuple(range(0, k))
    plus_vertices = tuple(range(2 * k, 3 * k))

    nu_left = first_edge_law(n, left_vertices)
    nu_middle = first_edge_law(n, middle_vertices)
    nu_minus = first_edge_law(n, minus_vertices)
    nu_plus = first_edge_law(n, plus_vertices)

    h1_b: dict[Perm, Fraction] = defaultdict(Fraction)
    h1_a: dict[Perm, Fraction] = defaultdict(Fraction)
    for first, p_first in nu_left.items():
        for second, p_second in nu_middle.items():
            h1_b[compose(first, second)] += p_first * p_second
    for exterior in (nu_minus, nu_plus):
        for first, p_first in exterior.items():
            for second, p_second in nu_middle.items():
                h1_a[compose(first, second)] += Fraction(1, 2) * p_first * p_second

    left = cycle(n, left_vertices)
    split = compose(cycle(n, minus_vertices), cycle(n, plus_vertices))
    rank = 2 * k - 2
    den_left = completion_count(left, rank)
    den_split = completion_count(split, rank)
    h2_b: dict[Perm, Fraction] = {}
    h2_a: dict[Perm, Fraction] = {}
    for product, lifts in pair_multiplicity.items():
        h2_b[product] = (
            lifts
            * completion_count(compose(inverse(product), left), rank - 2)
            / den_left
        )
        h2_a[product] = (
            lifts
            * completion_count(compose(inverse(product), split), rank - 2)
            / den_split
        )

    assert sum(h1_a.values(), Fraction(0)) == 1
    assert sum(h1_b.values(), Fraction(0)) == 1
    assert sum(h2_a.values(), Fraction(0)) == 1
    assert sum(h2_b.values(), Fraction(0)) == 1
    states = set(pair_multiplicity)
    beta_1 = {s: h1_b.get(s, Fraction(0)) - h1_a.get(s, Fraction(0)) for s in states}
    beta_2 = {s: h2_b.get(s, Fraction(0)) - h2_a.get(s, Fraction(0)) for s in states}
    return {1: beta_1, 2: beta_2}, {
        "h1_A_mass": sum(h1_a.values(), Fraction(0)),
        "h1_B_mass": sum(h1_b.values(), Fraction(0)),
        "h2_A_mass": sum(h2_a.values(), Fraction(0)),
        "h2_B_mass": sum(h2_b.values(), Fraction(0)),
        "F_r_L": den_left,
        "F_r_F": den_split,
    }


def owner_profile(n: int, h: Perm, product: Perm):
    residual = compose(inverse(product), h)
    components = cycle_components(residual)
    assert len(components) == 3
    owner = {
        vertex: index
        for index, component in enumerate(components)
        for vertex in component
    }
    generic = tuple(
        owner[x] if product[(x + 1) % n] == (x + 1) % n else None
        for x in range(n)
    )
    sizes = tuple(len(component) for component in components)
    return generic, sizes


def ratios(d: int):
    return tau(d - 1) / tau(d), tau(d - 2) / tau(d)


def owner_response(generic, sizes, lag: int, repaired: bool):
    n = len(generic)
    a = [ratios(d)[0] for d in sizes]
    b = [ratios(d)[1] for d in sizes]
    if not repaired:
        answer = Fraction(0)
        for x in range(n):
            i = generic[x]
            j = generic[(x + lag) % n]
            if i is None or j is None:
                continue
            answer += b[i] if i == j else a[i] * a[j]
        return answer

    field = [Fraction(0) if i is None else a[i] for i in generic]
    answer = sum(
        (field[x] * field[(x + lag) % n] for x in range(n)), Fraction(0)
    )
    for i, d in enumerate(sizes):
        if d < 3:
            continue
        delta = b[i] - a[i] * a[i]
        overlap = sum(
            generic[x] == i and generic[(x + lag) % n] == i
            for x in range(n)
        )
        answer += delta * overlap
    return answer


def positive_compositions(total: int, parts: int):
    for cuts in combinations(range(1, total), parts - 1):
        points = (0,) + cuts + (total,)
        yield tuple(points[i + 1] - points[i] for i in range(parts))


def interval_blocks(n: int, anchor: int, gaps: tuple[int, ...]):
    blocks = []
    start = 0
    for gap in gaps:
        blocks.append(frozenset((anchor + start + t) % n for t in range(gap - 1)))
        start += gap
    return tuple(blocks)


def expected_owner_data(kind: str, gaps: tuple[int, ...], blocks):
    if kind == "T":
        return tuple((gaps[i], blocks[i]) for i in range(3))
    if kind == "S":
        return (
            (gaps[0], blocks[0]),
            (gaps[2], blocks[2]),
            (gaps[1] + gaps[3], blocks[1] | blocks[3]),
        )
    if kind == "N":
        return (
            (gaps[1], blocks[1]),
            (gaps[3], blocks[3]),
            (gaps[0] + gaps[2], blocks[0] | blocks[2]),
        )
    raise ValueError(kind)


def expected_product(n: int, anchor: int, gaps: tuple[int, ...], kind: str):
    vertices = [anchor]
    running = anchor
    for gap in gaps[:-1]:
        running = (running + gap) % n
        vertices.append(running)
    if kind == "T":
        return cycle(n, tuple(vertices))
    if kind == "S":
        return compose(
            transposition(n, vertices[0], vertices[1]),
            transposition(n, vertices[2], vertices[3]),
        )
    if kind == "N":
        return compose(
            transposition(n, vertices[0], vertices[3]),
            transposition(n, vertices[1], vertices[2]),
        )
    raise ValueError(kind)


def response_from_expected_owners(n: int, data, lag: int):
    answer = Fraction(0)
    for i, (d_i, block_i) in enumerate(data):
        a_i, b_i = ratios(d_i)
        for j, (d_j, block_j) in enumerate(data):
            a_j, _ = ratios(d_j)
            overlap = len(block_i & frozenset((x - lag) % n for x in block_j))
            answer += (b_i if i == j else a_i * a_j) * overlap
    return answer


def qstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else str(x)


def main() -> None:
    k = 3
    n = 3 * k
    h = cycle(n, tuple(range(n)))
    pair_multiplicity = ordered_pair_products(n)
    explicit_beta, normalization = explicit_beta_coefficients(k, pair_multiplicity)

    source = {}
    channel_mass = {}
    kind_mass = {}
    for label in ("A", "B"):
        source[label], channel_mass[label], kind_mass[label] = source_pair_law(k, label)

    m = k - 1
    color_denominator = 3 * m * (3 * m - 1)
    alpha = {
        0: Fraction(m * (m - 1), color_denominator),
        1: Fraction(4 * m * m, color_denominator),
        2: Fraction(2 * m * (2 * m - 1), color_denominator),
    }
    for label in ("A", "B"):
        assert all(channel_mass[label][j] == alpha[j] for j in range(3))

    states = set(pair_multiplicity)
    conditional_beta = {
        j: {
            state: (
                source["B"].get((j, state), Fraction(0))
                - source["A"].get((j, state), Fraction(0))
            )
            / alpha[j]
            for state in states
        }
        for j in (1, 2)
    }
    assert conditional_beta == explicit_beta
    assert all(sum(explicit_beta[j].values(), Fraction(0)) == 0 for j in (1, 2))

    supported_states = {
        state
        for state in states
        if transposition_rank(compose(inverse(state), h)) == n - 3
    }
    assert all(
        explicit_beta[j][state] == 0
        for j in (1, 2)
        for state in states - supported_states
    )
    profiles = {state: owner_profile(n, h, state) for state in supported_states}
    for state, (generic, sizes) in profiles.items():
        for owner, d in enumerate(sizes):
            if d == 2:
                assert sum(x == owner for x in generic) <= 1
                assert all(
                    not any(
                        generic[x] == owner and generic[(x + lag) % n] == owner
                        for x in range(n)
                    )
                    for lag in range(1, n)
                )
        for lag in range(2, n - 1):
            assert owner_response(generic, sizes, lag, False) == owner_response(
                generic, sizes, lag, True
            )

    ratio_increases = all(
        tau(d) / tau(d - 1) < tau(d + 1) / tau(d)
        for d in range(2, 80)
    )
    delta_nonnegative = all(
        ratios(d)[1] - ratios(d)[0] ** 2 >= 0 for d in range(3, 81)
    )
    assert ratio_increases and delta_nonnegative
    assert ratios(2)[1] - ratios(2)[0] ** 2 == -1

    counts = {"T": defaultdict(int), "D": defaultdict(int)}
    accumulated = {
        j: {lag: Fraction(0) for lag in range(2, n - 1)} for j in (1, 2)
    }
    owner_records_checked = 0
    for parts, kinds in ((3, ("T",)), (4, ("S", "N"))):
        for gaps in positive_compositions(n, parts):
            for anchor in range(n):
                blocks = interval_blocks(n, anchor, gaps)
                for encoding in kinds:
                    product = expected_product(n, anchor, gaps, encoding)
                    broad_kind = "T" if encoding == "T" else "D"
                    counts[broad_kind][product] += 1
                    data = expected_owner_data(encoding, gaps, blocks)
                    generic, sizes = profiles[product]
                    actual_data = sorted(
                        [
                            (
                                sizes[i],
                                frozenset(x for x in range(n) if generic[x] == i),
                            )
                            for i in range(3)
                        ],
                        key=lambda item: (item[0], tuple(sorted(item[1]))),
                    )
                    expected_data = sorted(
                        data, key=lambda item: (item[0], tuple(sorted(item[1])))
                    )
                    assert actual_data == expected_data
                    owner_records_checked += 1
                    for lag in range(2, n - 1):
                        expected_response = response_from_expected_owners(n, data, lag)
                        direct_response = owner_response(generic, sizes, lag, False)
                        assert expected_response == direct_response
                        divisor = 3 if broad_kind == "T" else 4
                        for j in (1, 2):
                            accumulated[j][lag] += (
                                explicit_beta[j][product] * expected_response / divisor
                            )

    assert all(value == 3 for value in counts["T"].values())
    assert all(value == 4 for value in counts["D"].values())
    assert len(counts["T"]) == math.comb(n, 3)
    assert len(counts["D"]) == 2 * math.comb(n, 4)

    literal_sequence = {}
    repaired_sequence = {}
    for j in (1, 2):
        literal_sequence[j] = [
            sum(
                (
                    explicit_beta[j][state]
                    * owner_response(*profiles[state], lag, repaired=False)
                    for state in supported_states
                ),
                Fraction(0),
            )
            for lag in range(n)
        ]
        repaired_sequence[j] = [
            sum(
                (
                    explicit_beta[j][state]
                    * owner_response(*profiles[state], lag, repaired=True)
                    for state in supported_states
                ),
                Fraction(0),
            )
            for lag in range(n)
        ]
        assert all(
            accumulated[j][lag] == literal_sequence[j][lag]
            for lag in range(2, n - 1)
        )
        assert all(literal_sequence[j][lag] > 0 for lag in range(2, n - 1))
        assert all(
            repaired_sequence[j][lag] == literal_sequence[j][lag]
            for lag in range(2, n - 1)
        )
        assert all(
            repaired_sequence[j][lag] == repaired_sequence[j][(-lag) % n]
            for lag in range(n)
        )

    theta = Fraction(6 * (k - 1), k * (2 * k - 3) * (2 * k - 1))
    eta_triangle = {
        j: (
            kind_mass["B"].get((j, "T"), Fraction(0))
            - kind_mass["A"].get((j, "T"), Fraction(0))
        )
        / alpha[j]
        for j in (1, 2)
    }
    assert eta_triangle == {1: Fraction(0), 2: theta}

    vector = (10, 8, 2, -5, -9, -9, -5, 2, 8)
    channel = 2
    quadratic = sum(
        Fraction(vector[a] * vector[b])
        * repaired_sequence[channel][(b - a) % n]
        for a in range(n)
        for b in range(n)
    )
    expected_quadratic = Fraction(-310962953715709, 12252303000000)
    assert quadratic == expected_quadratic < 0

    payload = {
        "status": "clean-room exact convention and falsification audit",
        "scope": "k=3, n=9 only; no all-rank positivity inference",
        "convention": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "imports_predecessor_code_or_data": False,
        "alpha": {str(j): qstr(alpha[j]) for j in range(3)},
        "normalizations": {key: qstr(value) for key, value in normalization.items()},
        "conditional_beta_matches_explicit_beta": True,
        "positive_composition_multiplicity": {"triangle": 3, "double": 4},
        "distinct_composition_states": {
            "triangle": len(counts["T"]), "double": len(counts["D"])
        },
        "owner_records_checked": owner_records_checked,
        "owner_interval_formula_exact": True,
        "size_two_deletion_changes_only_lag_zero": True,
        "delta_log_convexity_exact_proof_required_beyond_finite_guard": True,
        "finite_delta_guard_through_d": 80,
        "all_admissible_k3_entries_positive": True,
        "eta_triangle": {str(j): qstr(eta_triangle[j]) for j in (1, 2)},
        "literal_sequences": {
            str(j): [qstr(x) for x in literal_sequence[j]] for j in (1, 2)
        },
        "repaired_sequences": {
            str(j): [qstr(x) for x in repaired_sequence[j]] for j in (1, 2)
        },
        "channel_2_quadratic_witness": {
            "vector": list(vector), "value": qstr(quadratic), "negative": True
        },
        "OCI_inference": False,
        "gap_mixing_terminal_inference": False,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
