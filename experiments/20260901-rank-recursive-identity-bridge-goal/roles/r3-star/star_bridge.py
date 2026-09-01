#!/usr/bin/env python3
"""Exact counts and sampling for prescribed-endpoint star bridges.

Convention: permutations are tuples of zero-based images and ``compose(p,q)``
is p after q, so a displayed word t_1 ... t_k evaluates as the map
x -> t_1(t_2(...t_k(x))).  The distinguished/pivot label is N-1 internally.

The polynomial count uses Féray, Theorem 1.2 (arXiv:0904.4854v2), after a
positive decomposition by the exact set of lower fixed labels used by a word.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import comb, factorial, prod
from random import Random
from typing import Iterable, Sequence

Permutation = tuple[int, ...]
PointedType = tuple[int, tuple[int, ...]]


def identity(n: int) -> Permutation:
    return tuple(range(n))


def compose(p: Permutation, q: Permutation) -> Permutation:
    """Return p*q as maps: (p*q)(x) = p(q(x))."""
    if len(p) != len(q):
        raise ValueError("permutations have different degrees")
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Permutation) -> Permutation:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def star_transposition(n: int, lower: int) -> Permutation:
    if not (n >= 2 and 0 <= lower < n - 1):
        raise ValueError("star factor requires 0 <= lower < N-1 and N >= 2")
    out = list(range(n))
    out[lower], out[n - 1] = out[n - 1], out[lower]
    return tuple(out)


def evaluate_star_word(n: int, word: Sequence[int]) -> Permutation:
    out = identity(n)
    for lower in word:
        out = compose(out, star_transposition(n, lower))
    return out


def cycles(p: Permutation) -> list[tuple[int, ...]]:
    seen = [False] * len(p)
    out: list[tuple[int, ...]] = []
    for start in range(len(p)):
        if seen[start]:
            continue
        cyc = []
        x = start
        while not seen[x]:
            seen[x] = True
            cyc.append(x)
            x = p[x]
        out.append(tuple(cyc))
    return out


def cycle_type(p: Permutation) -> tuple[int, ...]:
    return tuple(sorted((len(c) for c in cycles(p)), reverse=True))


def pointed_type(p: Permutation) -> PointedType:
    """H=S_{N-1} conjugacy invariant: pivot-cycle length and other lengths."""
    if not p:
        raise ValueError("degree zero is not supported")
    pivot = len(p) - 1
    pivot_length = None
    other: list[int] = []
    for cyc in cycles(p):
        if pivot in cyc:
            pivot_length = len(cyc)
        else:
            other.append(len(cyc))
    assert pivot_length is not None
    return pivot_length, tuple(sorted(other))


def minimal_star_length(p: Permutation) -> int:
    """Exact word metric for the star generating set."""
    if not p:
        raise ValueError("degree zero is not supported")
    pivot = len(p) - 1
    total = 0
    for cyc in cycles(p):
        ell = len(cyc)
        if pivot in cyc:
            total += ell - 1
        elif ell > 1:
            total += ell + 1
    return total


def feasible_star_bridge(n: int, k: int, q: Permutation) -> bool:
    if n < 1 or len(q) != n or k < 0:
        return False
    if n == 1:
        return k == 0 and q == identity(1)
    minimum = minimal_star_length(q)
    return k >= minimum and (k - minimum) % 2 == 0


def _f_series(scale: int, degree: int) -> list[Fraction]:
    """Truncation of f(scale*t), f(t)=2*sinh(t/2)/t."""
    out = [Fraction(0) for _ in range(degree + 1)]
    for d in range(0, degree + 1, 2):
        out[d] = Fraction(scale**d, (2**d) * factorial(d + 1))
    return out


def _mul_truncated(a: Sequence[Fraction], b: Sequence[Fraction], degree: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(degree + 1)]
    for i, ai in enumerate(a):
        if not ai:
            continue
        top = min(len(b) - 1, degree - i)
        for j in range(top + 1):
            if b[j]:
                out[i + j] += ai * b[j]
    return out


def transitive_star_count(parts: Sequence[int], k: int) -> int:
    """Féray Theorem 1.2, evaluated by a positive coefficient extraction.

    ``parts`` is the complete cycle type on the active label set, including
    fixed points.  Transitive means every active nonpivot label occurs in at
    least one star factor.
    """
    parts = tuple(int(x) for x in parts)
    if not parts or any(x <= 0 for x in parts) or k < 0:
        return 0
    n = sum(parts)
    ell = len(parts)
    minimum = n + ell - 2
    excess = k - minimum
    if excess < 0 or excess % 2:
        return 0
    # The singleton active set has no generators.  This is also the removable
    # n=1 limiting case of f(t)^{-1}*f(t) in the theorem.
    if n == 1:
        return int(parts == (1,) and k == 0)

    poly = [Fraction(1)] + [Fraction(0) for _ in range(excess)]
    # f(t)^(n-2) * product_i f(parts_i*t); every coefficient is nonnegative.
    for scale in [1] * (n - 2) + list(parts):
        poly = _mul_truncated(poly, _f_series(scale, excess), excess)
    value = Fraction(factorial(k) * prod(parts), factorial(n)) * poly[excess]
    if value.denominator != 1:
        raise ArithmeticError(f"nonintegral star count {value} for {parts=}, {k=}")
    return value.numerator


def active_base_cycle_type(q: Permutation) -> tuple[tuple[int, ...], int]:
    """Return mandatory active cycle type and number of optional fixed labels.

    The pivot singleton is mandatory when q fixes it.  Fixed nonpivot labels
    are optional support labels and are counted by the second return value.
    """
    if not q:
        raise ValueError("degree zero is not supported")
    pivot = len(q) - 1
    base: list[int] = []
    optional_fixed = 0
    for cyc in cycles(q):
        if len(cyc) > 1 or pivot in cyc:
            base.append(len(cyc))
        else:
            optional_fixed += 1
    return tuple(sorted(base, reverse=True)), optional_fixed


def star_bridge_count(n: int, k: int, q: Permutation) -> int:
    """Count length-k words in {(i,N)} with displayed product q."""
    if n < 1 or len(q) != n or k < 0:
        return 0
    if not feasible_star_bridge(n, k, q):
        return 0
    base, optional_fixed = active_base_cycle_type(q)
    total = 0
    # A word has a unique exact support.  Choose s optional fixed lower labels;
    # on that active set it is a transitive star factorization.
    for s in range(optional_fixed + 1):
        parts = base + (1,) * s
        total += comb(optional_fixed, s) * transitive_star_count(parts, k)
    return total


def pointed_type_transitions(state: PointedType) -> Counter[PointedType]:
    """Right-multiplication transitions, with star-label multiplicities."""
    r, lam = state
    out: Counter[PointedType] = Counter()
    mult = Counter(lam)
    # Join the pivot cycle to a nonpivot j-cycle: j choices per such cycle.
    for j, copies in mult.items():
        remaining = list(lam)
        remaining.remove(j)
        out[(r + j, tuple(sorted(remaining)))] += j * copies
    # Split the pivot cycle.  Each possible new pivot length occurs once.
    for new_r in range(1, r):
        out[(new_r, tuple(sorted(lam + (r - new_r,))))] += 1
    return out


def partitions(total: int, minimum: int = 1) -> Iterable[tuple[int, ...]]:
    if total == 0:
        yield ()
        return
    for first in range(minimum, total + 1):
        for rest in partitions(total - first, first):
            yield (first,) + rest


def all_pointed_types(n: int) -> list[PointedType]:
    if n < 1:
        return []
    return [(r, lam) for r in range(1, n + 1) for lam in partitions(n - r)]


def orbit_dp_tables(n: int, max_k: int) -> list[dict[PointedType, int]]:
    """Partition-scale exact DP: per-labeled-endpoint counts by pointed type."""
    states = all_pointed_types(n)
    zero = {state: 0 for state in states}
    tables = [dict(zero)]
    tables[0][(1, (1,) * (n - 1))] = 1
    for _ in range(max_k):
        previous = tables[-1]
        current = dict(zero)
        for state in states:
            current[state] = sum(
                multiplicity * previous[next_state]
                for next_state, multiplicity in pointed_type_transitions(state).items()
            )
        tables.append(current)
    return tables


def sample_star_bridge(n: int, k: int, q: Permutation, rng: Random) -> list[int]:
    """Sample exactly uniformly; return lower labels in displayed word order."""
    total = star_bridge_count(n, k, q)
    if total == 0:
        raise ValueError("empty prescribed-endpoint star fiber")
    if k == 0:
        return []

    endpoint = q
    last_to_first: list[int] = []
    for remaining in range(k, 0, -1):
        weighted: list[tuple[int, int, Permutation]] = []
        weight_sum = 0
        for lower in range(n - 1):
            predecessor = compose(endpoint, star_transposition(n, lower))
            weight = star_bridge_count(n, remaining - 1, predecessor)
            if weight:
                weighted.append((lower, weight, predecessor))
                weight_sum += weight
        if weight_sum != star_bridge_count(n, remaining, endpoint):
            raise ArithmeticError("last-factor recurrence failed")
        draw = rng.randrange(weight_sum)
        cumulative = 0
        for lower, weight, predecessor in weighted:
            cumulative += weight
            if draw < cumulative:
                last_to_first.append(lower)
                endpoint = predecessor
                break
        else:  # pragma: no cover - defensive assertion
            raise AssertionError("weighted draw fell outside total")
    if endpoint != identity(n):
        raise AssertionError("backward sampler did not terminate at identity")
    return list(reversed(last_to_first))
