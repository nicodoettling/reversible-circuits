#!/usr/bin/env python3
"""One-rank exact-symbolic falsifier for the frozen M290 DSR candidate.

This is a clean-room formula checker: it imports no predecessor code or data.
It reconstructs both normalized source laws from minimal-completion counts,
keeps channel and triangle/double labels until the final sum, and evaluates
the complete decorated coefficient as A*e^2+B.  Its k=9 output is only a
falsification/convention check, never evidence for an all-rank theorem.
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
Lin = tuple[Fraction, Fraction]  # A*e^2+B
K = 9


def mul(p: Perm, q: Perm) -> Perm:
    """Return pq, so (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inv(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def cyc(n: int, entries: tuple[int, ...]) -> Perm:
    out = list(range(n))
    if len(entries) > 1:
        for x, y in zip(entries, entries[1:] + entries[:1]):
            out[x] = y
    return tuple(out)


def tr(n: int, x: int, y: int) -> Perm:
    return cyc(n, (x, y))


def cycles(p: Perm) -> tuple[tuple[int, ...], ...]:
    unseen = set(range(len(p)))
    out = []
    while unseen:
        start = min(unseen)
        component = []
        x = start
        while x in unseen:
            unseen.remove(x)
            component.append(x)
            x = p[x]
        out.append(tuple(component))
    return tuple(out)


def rank(p: Perm) -> int:
    return len(p) - len(cycles(p))


@lru_cache(maxsize=None)
def tau(d: int) -> Fraction:
    if d < 1:
        return Fraction(0)
    if d == 1:
        return Fraction(1)
    return Fraction(d ** (d - 2), math.factorial(d - 1))


def completion(p: Perm, length: int) -> int:
    if rank(p) != length:
        return 0
    value = Fraction(math.factorial(length))
    for component in cycles(p):
        value *= tau(len(component))
    assert value.denominator == 1
    return value.numerator


def internal_edges(n: int, component: tuple[int, ...]):
    for x, y in combinations(sorted(component), 2):
        yield tr(n, x, y)


def source_law(k: int, label: str):
    """Raw first-two-factor law, retaining J and T/D decorations."""
    n = 3 * k
    h = cyc(n, tuple(range(n)))
    if label == "A":
        source = cyc(n, (0, k, 2 * k))
    elif label == "B":
        source = mul(tr(n, 0, 1), tr(n, k, 2 * k))
    else:
        raise ValueError(label)
    residual = mul(inv(source), h)
    original = cycles(residual)
    owner = {x: i for i, c in enumerate(original) for x in c}
    middle = owner[k]
    initial_rank = rank(residual)
    denominator = completion(residual, initial_rank)
    law = defaultdict(Fraction)
    raw_pairs = 0
    for first_owner, component in enumerate(original):
        for first in internal_edges(n, component):
            after_first = mul(first, residual)
            for child in cycles(after_first):
                second_owner = owner[child[0]]
                assert all(owner[x] == second_owner for x in child)
                for second in internal_edges(n, child):
                    numerator = completion(mul(second, after_first), initial_rank - 2)
                    if not numerator:
                        continue
                    product = mul(first, second)
                    support = sum(product[x] != x for x in range(n))
                    assert support in (3, 4)
                    kind = "T" if support == 3 else "D"
                    channel = int(first_owner != middle) + int(
                        second_owner != middle
                    )
                    law[(channel, kind, product)] += Fraction(numerator, denominator)
                    raw_pairs += 1
    assert sum(law.values(), Fraction(0)) == 1
    return dict(law), raw_pairs


def owner_profile(n: int, h: Perm, product: Perm):
    residual = mul(inv(product), h)
    components = cycles(residual)
    assert len(components) == 3
    owner = {x: i for i, c in enumerate(components) for x in c}
    generic = tuple(
        owner[x] if product[(x + 1) % n] == (x + 1) % n else None
        for x in range(n)
    )
    sizes = tuple(len(c) for c in components)
    assert sum(x is None for x in generic) in (3, 4)
    return generic, sizes


def owner_q_rows(generic, sizes):
    """Return exact Q_l=A_l*e^2+B_l, keeping the literal owner map."""
    n = len(generic)
    a = [tau(d - 1) / tau(d) for d in sizes]
    b = [tau(d - 2) / tau(d) for d in sizes]
    rows = []
    for lag in range(n):
        f_value = Fraction(0)
        generic_overlap = 0
        for x in range(n):
            i = generic[x]
            j = generic[(x + lag) % n]
            if i is None or j is None:
                continue
            generic_overlap += 1
            f_value += b[i] if i == j else a[i] * a[j]
        rows.append((f_value, Fraction(-generic_overlap)))
    return tuple(rows)


def add(x: Lin, y: Lin) -> Lin:
    return x[0] + y[0], x[1] + y[1]


def sub(x: Lin, y: Lin) -> Lin:
    return x[0] - y[0], x[1] - y[1]


def scale(c: Fraction, x: Lin) -> Lin:
    return c * x[0], c * x[1]


def sum_lin(values) -> Lin:
    out = (Fraction(0), Fraction(0))
    for value in values:
        out = add(out, value)
    return out


def e2_interval(terms: int = 50) -> tuple[Fraction, Fraction]:
    lower_e = sum((Fraction(1, math.factorial(j)) for j in range(terms + 1)), Fraction(0))
    upper_e = lower_e + Fraction(2, math.factorial(terms + 1))
    return lower_e * lower_e, upper_e * upper_e


def enclosure(x: Lin, e2_bounds: tuple[Fraction, Fraction]):
    low_e2, high_e2 = e2_bounds
    if x[0] >= 0:
        return x[0] * low_e2 + x[1], x[0] * high_e2 + x[1]
    return x[0] * high_e2 + x[1], x[0] * low_e2 + x[1]


def certified_sign(x: Lin, e2_bounds: tuple[Fraction, Fraction]) -> int:
    if x == (Fraction(0), Fraction(0)):
        return 0
    low, high = enclosure(x, e2_bounds)
    if low > 0:
        return 1
    if high < 0:
        return -1
    raise AssertionError("e^2 enclosure does not certify the sign")


def qstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else str(x)


def lstr(x: Lin) -> dict[str, str]:
    return {"e2": qstr(x[0]), "constant": qstr(x[1])}


def main() -> None:
    k = K
    n = 3 * k
    h = cyc(n, tuple(range(n)))
    laws = {}
    raw_counts = {}
    for label in ("A", "B"):
        laws[label], raw_counts[label] = source_law(k, label)

    keys = tuple((j, kind) for j in range(3) for kind in ("T", "D"))
    masses = {
        label: {
            key: sum(
                (p for (j, kind, _), p in laws[label].items() if (j, kind) == key),
                Fraction(0),
            )
            for key in keys
        }
        for label in ("A", "B")
    }
    assert sum(masses["A"].values(), Fraction(0)) == 1
    assert sum(masses["B"].values(), Fraction(0)) == 1

    states = {state for law in laws.values() for _, _, state in law}
    responses = {state: owner_q_rows(*owner_profile(n, h, state)) for state in states}
    pieces = {
        key: tuple(
            add(
                sum_lin(
                    (
                        scale(p, responses[state][lag])
                        for (j, kind, state), p in laws["B"].items()
                        if (j, kind) == key
                    )
                ),
                scale(
                    Fraction(-1),
                    sum_lin(
                        (
                            scale(p, responses[state][lag])
                            for (j, kind, state), p in laws["A"].items()
                            if (j, kind) == key
                        )
                    ),
                ),
            )
            for lag in range(n)
        )
        for key in keys
    }
    q = tuple(
        sum_lin(pieces[key][lag] for key in keys)
        for lag in range(n)
    )
    d = tuple(sub(q[(lag + 1) % n], q[lag]) for lag in range(n))

    assert all(q[lag] == q[(-lag) % n] for lag in range(n))
    assert all(d[lag] == scale(Fraction(-1), d[(n - lag - 1) % n]) for lag in range(n))
    midpoint = (n - 1) // 2
    assert d[midpoint] == (Fraction(0), Fraction(0))

    bounds = e2_interval()
    signs = {lag: certified_sign(d[lag], bounds) for lag in range(2, n - 2)}
    dsr_negative = all(signs[lag] <= 0 for lag in range(2, k - 1))
    dsr_positive = all(signs[lag] >= 0 for lag in range(k - 1, midpoint))
    dsr_survives = dsr_negative and dsr_positive

    dor = (Fraction(0), Fraction(0))
    for lag in range(2, n - 2):
        dor = add(dor, scale(Fraction(signs[lag]), d[lag]))
    dtr = scale(Fraction(2), add(add(q[2], q[midpoint]), scale(Fraction(-2), q[k - 1])))
    if dsr_survives:
        assert dor == dtr

    dor_low, dor_high = enclosure(dor, bounds)
    channel_kind_signed_mass = {
        f"J{j}_{kind}": qstr(masses["B"][(j, kind)] - masses["A"][(j, kind)])
        for j, kind in keys
    }
    payload = {
        "status": "single authorized exact-symbolic falsifier",
        "scope": "k=9, n=27 only; no all-rank DSR, DTR, BODT, or DOR inference",
        "convention": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "imports_predecessor_code_or_data": False,
        "source_mass_exact": {label: qstr(sum(laws[label].values(), Fraction(0))) for label in ("A", "B")},
        "raw_ordered_pairs": raw_counts,
        "accessible_supported_products": len(states),
        "channel_kind_signed_mass": channel_kind_signed_mass,
        "all_channel_kind_rows_summed_before_sign": True,
        "owner_sizes_phases_seams_used_literally": True,
        "same_cross_and_collision_decoration_combined_before_sign": True,
        "reflection_exact_symbolic": True,
        "central_derivative_zero_exact_symbolic": True,
        "DSR_k9_survives": dsr_survives,
        "lower_half_signs": {str(lag): signs[lag] for lag in range(2, midpoint + 1)},
        "combined_derivative_symbolic": {str(lag): lstr(d[lag]) for lag in range(2, n - 2)},
        "DOR_symbolic_under_certified_signs": lstr(dor),
        "DTR_symbolic": lstr(dtr),
        "DOR_equals_DTR_at_k9": dor == dtr,
        "DOR_enclosure_float": [float(dor_low), float(dor_high)],
        "k_times_DOR_enclosure_float": [float(k * dor_low), float(k * dor_high)],
        "BODT_inference": False,
        "DOR_inference": False,
        "downstream_inference": False,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
