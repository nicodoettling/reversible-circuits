#!/usr/bin/env python3
"""Clean-room exact guard for the frozen M290 formulas, at k=9 only.

The program imports no predecessor code or data.  It reconstructs the two
source laws from minimal-completion counts, checks the owner endpoint and
defect-field identities coefficientwise, checks the positive-composition
multiplicities and owner rows, and evaluates the one declared finite DSR row.
Nothing printed here is an all-rank estimate.
"""

from __future__ import annotations

import json
import math
import platform
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations


K = 9
N = 3 * K
Perm = tuple[int, ...]
Lin = tuple[Fraction, Fraction]       # A e^2 + B
Poly = tuple[Fraction, Fraction, Fraction]  # A e^2 + B e + C


def compose(p: Perm, q: Perm) -> Perm:
    """Return pq, with (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def cycle(items: tuple[int, ...], n: int = N) -> Perm:
    out = list(range(n))
    for x, y in zip(items, items[1:] + items[:1]):
        out[x] = y
    return tuple(out)


def transposition(x: int, y: int, n: int = N) -> Perm:
    return cycle((x, y), n)


def cycle_decomposition(p: Perm) -> tuple[tuple[int, ...], ...]:
    unseen = set(range(len(p)))
    answer = []
    while unseen:
        start = min(unseen)
        current = []
        x = start
        while x in unseen:
            unseen.remove(x)
            current.append(x)
            x = p[x]
        answer.append(tuple(current))
    return tuple(answer)


def transposition_rank(p: Perm) -> int:
    return len(p) - len(cycle_decomposition(p))


@lru_cache(maxsize=None)
def tau(d: int) -> Fraction:
    if d < 1:
        return Fraction(0)
    if d == 1:
        return Fraction(1)
    return Fraction(d ** (d - 2), math.factorial(d - 1))


def minimal_completions(p: Perm, length: int) -> int:
    if transposition_rank(p) != length:
        return 0
    value = Fraction(math.factorial(length))
    for component in cycle_decomposition(p):
        value *= tau(len(component))
    assert value.denominator == 1
    return value.numerator


def edges_within(component: tuple[int, ...]):
    for x, y in combinations(component, 2):
        yield transposition(x, y)


def source_product_law(label: str):
    h = cycle(tuple(range(N)))
    if label == "A":
        source = cycle((0, K, 2 * K))
    elif label == "B":
        source = compose(transposition(0, 1), transposition(K, 2 * K))
    else:
        raise ValueError(label)

    residual = compose(inverse(source), h)
    roots = cycle_decomposition(residual)
    root_owner = {x: i for i, block in enumerate(roots) for x in block}
    middle_owner = root_owner[K]
    length = transposition_rank(residual)
    denominator = minimal_completions(residual, length)
    law = defaultdict(Fraction)
    raw_pairs = 0

    for first_owner, block in enumerate(roots):
        for first in edges_within(block):
            after_first = compose(first, residual)
            for child in cycle_decomposition(after_first):
                second_owner = root_owner[child[0]]
                assert all(root_owner[x] == second_owner for x in child)
                for second in edges_within(child):
                    numerator = minimal_completions(
                        compose(second, after_first), length - 2
                    )
                    if numerator == 0:
                        continue
                    state = compose(first, second)
                    support = sum(state[x] != x for x in range(N))
                    assert support in (3, 4)
                    kind = "T" if support == 3 else "D"
                    channel = int(first_owner != middle_owner) + int(
                        second_owner != middle_owner
                    )
                    law[(channel, kind, state)] += Fraction(numerator, denominator)
                    raw_pairs += 1

    assert sum(law.values(), Fraction(0)) == 1
    return dict(law), raw_pairs


def owner_data(state: Perm):
    h = cycle(tuple(range(N)))
    residual = compose(inverse(state), h)
    blocks = cycle_decomposition(residual)
    assert len(blocks) == 3
    labels = {x: i for i, block in enumerate(blocks) for x in block}
    generic = tuple(
        labels[x] if state[(x + 1) % N] == (x + 1) % N else None
        for x in range(N)
    )
    return generic, tuple(len(block) for block in blocks)


def a_ratio(d: int) -> Fraction:
    return tau(d - 1) / tau(d)


def b_ratio(d: int) -> Fraction:
    return tau(d - 2) / tau(d)


def kappa(i: int | None, j: int | None, sizes: tuple[int, ...]) -> Fraction:
    if i is None or j is None:
        return Fraction(0)
    if i == j:
        return b_ratio(sizes[i])
    return a_ratio(sizes[i]) * a_ratio(sizes[j])


def lin_add(x: Lin, y: Lin) -> Lin:
    return x[0] + y[0], x[1] + y[1]


def lin_sub(x: Lin, y: Lin) -> Lin:
    return x[0] - y[0], x[1] - y[1]


def lin_scale(c: Fraction, x: Lin) -> Lin:
    return c * x[0], c * x[1]


def q_rows(generic, sizes) -> tuple[Lin, ...]:
    rows = []
    for lag in range(N):
        rooted = Fraction(0)
        generic_pairs = 0
        for x in range(N):
            i, j = generic[x], generic[(x + lag) % N]
            if i is None or j is None:
                continue
            rooted += kappa(i, j, sizes)
            generic_pairs += 1
        rows.append((rooted, Fraction(-generic_pairs)))
    return tuple(rows)


def endpoint_delta(generic, sizes, lag: int) -> Lin:
    answer = (Fraction(0), Fraction(0))
    for x in range(N):
        i = generic[(x - lag) % N]
        for sign, j in ((1, generic[(x + 1) % N]), (-1, generic[x])):
            if i is not None and j is not None:
                answer = lin_add(
                    answer,
                    (sign * kappa(i, j, sizes), Fraction(-sign)),
                )
    return answer


def defect_polynomial(generic, sizes, lag: int) -> Poly:
    c2 = c1 = c0 = Fraction(0)
    # 2 sum U, where U=e a_d-1 on a generic phase.
    for i in generic:
        if i is not None:
            c1 += 2 * a_ratio(sizes[i])
            c0 -= 2

    # -Corr(U,B)-Corr(B,U).
    for x in range(N):
        i, j = generic[x], generic[(x + lag) % N]
        if i is not None and j is None:
            c1 -= a_ratio(sizes[i])
            c0 += 1
        if i is None and j is not None:
            c1 -= a_ratio(sizes[j])
            c0 += 1

    # Corr(U,U).
    for x in range(N):
        i, j = generic[x], generic[(x + lag) % N]
        if i is None or j is None:
            continue
        c2 += a_ratio(sizes[i]) * a_ratio(sizes[j])
        c1 -= a_ratio(sizes[i]) + a_ratio(sizes[j])
        c0 += 1

    # e^2 sum_i delta_i Corr(chi_i,chi_i).
    for x in range(N):
        i, j = generic[x], generic[(x + lag) % N]
        if i is not None and i == j:
            c2 += b_ratio(sizes[i]) - a_ratio(sizes[i]) ** 2
    return c2, c1, c0


def circular_runs(points: set[int]) -> int:
    if not points:
        return 0
    if len(points) == N:
        return 1
    return sum(
        1 for x in range(N) if x in points and (x - 1) % N not in points
    )


def positive_compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(1, total - parts + 2):
        for rest in positive_compositions(total - first, parts - 1):
            yield (first,) + rest


def interval(start: int, length: int) -> set[int]:
    return {(start + j) % N for j in range(length)}


def check_owner_row(state: Perm, predicted: tuple[set[int], ...]) -> None:
    generic, _ = owner_data(state)
    actual = {
        frozenset(x for x, value in enumerate(generic) if value == i)
        for i in range(3)
    }
    assert actual == {frozenset(x) for x in predicted}


def composition_checks():
    counts = Counter()
    owner_row_checks = 0

    for g in positive_compositions(N, 3):
        cut = (0, g[0], g[0] + g[1])
        blocks = tuple(interval(cut[i], g[i] - 1) for i in range(3))
        check_owner_row(cycle(cut), blocks)
        owner_row_checks += 1
        for anchor in range(N):
            vertices = tuple((anchor + x) % N for x in cut)
            counts[cycle(vertices)] += 1

    for g in positive_compositions(N, 4):
        cut = (0, g[0], g[0] + g[1], g[0] + g[1] + g[2])
        blocks = tuple(interval(cut[i], g[i] - 1) for i in range(4))
        s_state = compose(
            transposition(cut[0], cut[1]), transposition(cut[2], cut[3])
        )
        n_state = compose(
            transposition(cut[0], cut[3]), transposition(cut[1], cut[2])
        )
        check_owner_row(s_state, (blocks[0], blocks[2], blocks[1] | blocks[3]))
        check_owner_row(n_state, (blocks[1], blocks[3], blocks[0] | blocks[2]))
        owner_row_checks += 2
        for anchor in range(N):
            v = tuple((anchor + x) % N for x in cut)
            counts[
                compose(transposition(v[0], v[1]), transposition(v[2], v[3]))
            ] += 1
            counts[
                compose(transposition(v[0], v[3]), transposition(v[1], v[2]))
            ] += 1

    triangle_counts = [count for state, count in counts.items() if sum(state[x] != x for x in range(N)) == 3]
    double_counts = [count for state, count in counts.items() if sum(state[x] != x for x in range(N)) == 4]
    assert triangle_counts and set(triangle_counts) == {3}
    assert double_counts and set(double_counts) == {4}
    return len(triangle_counts), len(double_counts), owner_row_checks


def exp_bounds(terms: int = 60):
    lower = sum((Fraction(1, math.factorial(j)) for j in range(terms + 1)), Fraction(0))
    upper = lower + Fraction(2, math.factorial(terms + 1))
    return lower, upper, lower * lower, upper * upper


def sign_lin(value: Lin, e2_low: Fraction, e2_high: Fraction) -> int:
    if value == (0, 0):
        return 0
    low = value[0] * (e2_low if value[0] >= 0 else e2_high) + value[1]
    high = value[0] * (e2_high if value[0] >= 0 else e2_low) + value[1]
    if low > 0:
        return 1
    if high < 0:
        return -1
    raise AssertionError("sign not certified")


def encode_lin(value: Lin):
    return {"e2": str(value[0]), "constant": str(value[1])}


def main() -> None:
    law_a, pairs_a = source_product_law("A")
    law_b, pairs_b = source_product_law("B")
    states = {state for _, _, state in law_a} | {state for _, _, state in law_b}

    eta = defaultdict(Fraction)
    signed_channel_kind = defaultdict(Fraction)
    for (channel, kind, state), mass in law_b.items():
        eta[state] += mass
        signed_channel_kind[(channel, kind)] += mass
    for (channel, kind, state), mass in law_a.items():
        eta[state] -= mass
        signed_channel_kind[(channel, kind)] -= mass
    assert sum(eta.values(), Fraction(0)) == 0
    assert sum(abs(x) for x in eta.values()) <= 2

    q = [(Fraction(0), Fraction(0)) for _ in range(N)]
    q_interior = [(Fraction(0), Fraction(0)) for _ in range(N)]
    endpoint_checks = defect_checks = 0
    max_owner_runs = 0
    size_two_nonzero_overlap = 0

    for state in states:
        generic, sizes = owner_data(state)
        rows = q_rows(generic, sizes)
        for owner in range(3):
            locations = {x for x, value in enumerate(generic) if value == owner}
            max_owner_runs = max(max_owner_runs, circular_runs(locations))
            if sizes[owner] == 2:
                size_two_nonzero_overlap += sum(
                    1
                    for lag in range(1, N)
                    if any(
                        generic[x] == owner and generic[(x + lag) % N] == owner
                        for x in range(N)
                    )
                )

        for lag in range(2, N - 2):
            assert endpoint_delta(generic, sizes, lag) == lin_sub(rows[lag + 1], rows[lag])
            endpoint_checks += 1
        for lag in range(2, N - 1):
            direct = (rows[lag][0], Fraction(0), rows[lag][1])
            assert defect_polynomial(generic, sizes, lag) == direct
            defect_checks += 1

        coefficient = eta[state]
        for lag in range(N):
            q[lag] = lin_add(q[lag], lin_scale(coefficient, rows[lag]))
            if min(sizes) >= (K + 1) // 2:
                q_interior[lag] = lin_add(
                    q_interior[lag], lin_scale(coefficient, rows[lag])
                )

    assert max_owner_runs <= 2
    assert size_two_nonzero_overlap == 0

    triangle_states, double_states, owner_row_checks = composition_checks()
    e_low, e_high, e2_low, e2_high = exp_bounds()
    ratio_checks = 0
    for d in range(2, N + 1):
        a = a_ratio(d)
        assert e_low * a - 1 >= 0
        assert e_high * a - 1 <= Fraction(4, d)
        if d >= 3:
            delta = b_ratio(d) - a * a
            assert delta >= 0
        ratio_checks += 1

    assert all(q[lag] == q[(-lag) % N] for lag in range(N))
    derivatives = {
        lag: lin_sub(q[lag + 1], q[lag]) for lag in range(2, N - 2)
    }
    assert all(
        derivatives[lag] == lin_scale(Fraction(-1), derivatives[N - lag - 1])
        for lag in derivatives
    )
    midpoint = (N - 1) // 2
    assert derivatives[midpoint] == (Fraction(0), Fraction(0))
    signs = {lag: sign_lin(value, e2_low, e2_high) for lag, value in derivatives.items()}

    dor = (Fraction(0), Fraction(0))
    for lag, value in derivatives.items():
        dor = lin_add(dor, lin_scale(Fraction(signs[lag]), value))
    dtr = lin_scale(
        Fraction(2),
        lin_add(lin_add(q[2], q[midpoint]), lin_scale(Fraction(-2), q[K - 1])),
    )
    assert dor == dtr

    interior_derivatives = {
        lag: lin_sub(q_interior[lag + 1], q_interior[lag])
        for lag in range(2, N - 2)
    }
    interior_l1 = (Fraction(0), Fraction(0))
    for value in interior_derivatives.values():
        interior_l1 = lin_add(
            interior_l1,
            lin_scale(Fraction(sign_lin(value, e2_low, e2_high)), value),
        )

    dor_low = dor[0] * (e2_low if dor[0] >= 0 else e2_high) + dor[1]
    dor_high = dor[0] * (e2_high if dor[0] >= 0 else e2_low) + dor[1]
    int_low = interior_l1[0] * (e2_low if interior_l1[0] >= 0 else e2_high) + interior_l1[1]
    int_high = interior_l1[0] * (e2_high if interior_l1[0] >= 0 else e2_low) + interior_l1[1]

    result = {
        "status": "clean-room exact k=9 convention/falsification guard only",
        "scope": "k=9, n=27 only; no BODT/DOR/DSR/DTR/downstream inference",
        "convention": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "python": platform.python_version(),
        "imports_predecessor_code_or_data": False,
        "source_mass": {"A": str(sum(law_a.values())), "B": str(sum(law_b.values()))},
        "raw_ordered_pairs": {"A": pairs_a, "B": pairs_b},
        "accessible_supported_products": len(states),
        "signed_channel_kind_mass": {
            f"J{j}_{kind}": str(signed_channel_kind[(j, kind)])
            for j in range(3)
            for kind in ("T", "D")
        },
        "signed_state_l1_at_most_two": str(sum(abs(x) for x in eta.values())),
        "endpoint_identity_checks": endpoint_checks,
        "defect_polynomial_checks": defect_checks,
        "max_circular_owner_intervals": max_owner_runs,
        "size_two_nonzero_lag_overlaps": size_two_nonzero_overlap,
        "finite_ratio_checks_d2_through_d27": ratio_checks,
        "composition_multiplicity": {
            "triangle_states": triangle_states,
            "triangle_count_each": 3,
            "double_states": double_states,
            "combined_S_N_count_each": 4,
            "owner_row_checks_at_anchor_zero": owner_row_checks,
            "extra_n_factor": False,
        },
        "reflection_exact": True,
        "central_derivative_zero_exact": True,
        "lower_half_signs": {str(lag): signs[lag] for lag in range(2, midpoint + 1)},
        "DOR_symbolic": encode_lin(dor),
        "DTR_symbolic": encode_lin(dtr),
        "DOR_equals_DTR_at_k9": dor == dtr,
        "DOR_enclosure_float": [float(dor_low), float(dor_high)],
        "k_times_DOR_enclosure_float": [float(K * dor_low), float(K * dor_high)],
        "interior_sector_l1_enclosure_float": [float(int_low), float(int_high)],
        "asymptotic_inference": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
