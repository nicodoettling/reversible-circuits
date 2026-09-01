#!/usr/bin/env python3
"""Exact literal diagnostics for M235's signed two-run moment.

This checker uses only the Python standard library and reconstructs the
ordered disjoint-pair law directly.  Finite output is falsification and
formula calibration only; it is not a proof of TCM.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from math import factorial


def b(size: int) -> Fraction:
    return Fraction(size ** (size - 1), factorial(size))


def kernel(k: int, parent: int, child: int) -> Fraction:
    return b(child) * b(parent - child) / ((2 * k - 3) * b(parent))


def qsplit(k: int, split: int) -> Fraction:
    return Fraction(k, k - 1) * b(split) * b(k - split) / b(k)


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[x]] for x in range(len(left)))


def inverse(perm: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * len(perm)
    for x, y in enumerate(perm):
        out[y] = x
    return tuple(out)


def cycle_perm(n: int, entries: tuple[int, ...]) -> tuple[int, ...]:
    out = list(range(n))
    for x, y in zip(entries, entries[1:] + entries[:1]):
        out[x] = y
    return tuple(out)


def transposition(n: int, x: int, y: int) -> tuple[int, ...]:
    out = list(range(n))
    out[x], out[y] = out[y], out[x]
    return tuple(out)


def cycles(perm: tuple[int, ...]) -> list[tuple[int, ...]]:
    seen: set[int] = set()
    out: list[tuple[int, ...]] = []
    for start in range(len(perm)):
        if start in seen:
            continue
        part: list[int] = []
        x = start
        while x not in seen:
            seen.add(x)
            part.append(x)
            x = perm[x]
        out.append(tuple(part))
    return out


def internal_edges(perm: tuple[int, ...]) -> list[tuple[int, ...]]:
    return [
        transposition(len(perm), x, y)
        for part in cycles(perm)
        for x, y in combinations(part, 2)
    ]


def edge_vertices(edge: tuple[int, ...]) -> tuple[int, int]:
    moved = tuple(x for x in range(len(edge)) if edge[x] != x)
    assert len(moved) == 2
    return moved


def ambient_runs(component: tuple[int, ...], n: int) -> int:
    support = set(component)
    return sum(1 for x in support if (x - 1) % n not in support)


def source(k: int, side: str) -> tuple[tuple[int, ...], list[tuple[int, ...]]]:
    n = 3 * k
    if side == "B":
        part = tuple(range(1, k)) + tuple(range(2 * k, 3 * k))
        return cycle_perm(n, part), [part]
    lower = tuple(range(k))
    upper = tuple(range(2 * k, 3 * k))
    return compose(cycle_perm(n, lower), cycle_perm(n, upper)), [lower, upper]


def split_size(edge: tuple[int, ...], originals: list[tuple[int, ...]]) -> int:
    x, y = edge_vertices(edge)
    part = next(c for c in originals if x in c)
    gap = (part.index(y) - part.index(x)) % len(part)
    return min(gap, len(part) - gap)


def literal_records(k: int, side: str) -> list[dict[str, object]]:
    """Return every literal ordered disjoint tuple with its two-run face."""
    n = 3 * k
    target = cycle_perm(n, tuple(range(n)))
    src, originals = source(k, side)
    records: list[dict[str, object]] = []
    for first in internal_edges(src):
        split = split_size(first, originals)
        if split > (k - 1) // 2:
            continue
        after_first = compose(first, src)
        first_support = set(edge_vertices(first))
        first_parts = cycles(after_first)
        original_with_first = next(set(c) for c in originals if first_support <= set(c))
        for second in internal_edges(after_first):
            if first_support & set(edge_vertices(second)):
                continue
            parent = next(
                part
                for part in first_parts
                if set(edge_vertices(second)) <= set(part)
            )
            after_second = compose(second, after_first)
            children = [part for part in cycles(after_second) if set(part) <= set(parent)]
            assert len(children) == 2
            residual = compose(inverse(compose(first, second)), target)
            residual_parts = cycles(residual)
            assert len(residual_parts) == 3
            two = [part for part in residual_parts if ambient_runs(part, n) == 2]
            assert len(two) == 1
            case = "marked" if set(parent) <= original_with_first else "untouched"
            records.append(
                {
                    "split": split,
                    "first": edge_vertices(first),
                    "second": edge_vertices(second),
                    "case": case,
                    "parent": len(parent),
                    "children": tuple(sorted(map(len, children))),
                    "two_size": len(two[0]),
                    "two_support": two[0],
                    "one_sizes": tuple(
                        sorted(
                            len(part)
                            for part in residual_parts
                            if ambient_runs(part, n) == 1
                        )
                    ),
                    "weight": kernel(k, len(parent), len(children[0])),
                }
            )
    return records


def grouped_counts(k: int, side: str) -> dict[tuple[object, ...], Counter[int]]:
    grouped: dict[tuple[object, ...], Counter[int]] = defaultdict(Counter)
    for record in literal_records(k, side):
        key = (
            record["split"],
            record["case"],
            record["parent"],
            record["children"],
        )
        grouped[key][int(record["two_size"])] += 1
    return dict(grouped)


def literal_two_coefficients(k: int, side: str) -> dict[int, Fraction]:
    """Exact q-averaged raw two-run coefficients from literal tuples."""
    records = literal_records(k, side)
    first_count = (2 * k - 1) if side == "B" else 2 * k
    out: dict[int, Fraction] = defaultdict(Fraction)
    for record in records:
        out[int(record["two_size"])] += (
            qsplit(k, int(record["split"]))
            * Fraction(record["weight"])
            / first_count
        )
    return dict(out)


def b_two_coefficients_formula(k: int) -> dict[int, Fraction]:
    """Two-seam retained-arc formula, before any inequality."""
    d_total = 2 * k - 1
    seam_big = k - 2
    seam_small = d_total - 1
    out: dict[int, Fraction] = defaultdict(Fraction)
    for split in range(1, (k - 1) // 2 + 1):
        for parent in (split, d_total - split):
            for child in range(1, parent):
                retained = parent - child
                for offset in range(1, retained):
                    for start in range(d_total):
                        edges = {
                            (start + edge_offset) % d_total
                            for edge_offset in (
                                *range(offset),
                                *range(offset + child, parent),
                            )
                        }
                        size = retained
                        size += k * int(seam_big in edges)
                        size += int(seam_small in edges)
                        out[size] += (
                            qsplit(k, split)
                            * kernel(k, parent, child)
                            / d_total
                        )
    return dict(out)


def check_b_placement_bound(k: int) -> None:
    """Check the exact seam bound at every finite formula tuple."""
    d_total = 2 * k - 1
    seam_big = k - 2
    seam_small = d_total - 1
    limit = (3 * k - 1) // 2
    for split in range(1, (k - 1) // 2 + 1):
        for parent in (split, d_total - split):
            for child in range(1, parent):
                retained = parent - child
                for offset in range(1, retained):
                    sizes = []
                    for start in range(d_total):
                        edges = {
                            (start + edge_offset) % d_total
                            for edge_offset in (
                                *range(offset),
                                *range(offset + child, parent),
                            )
                        }
                        sizes.append(
                            retained
                            + k * int(seam_big in edges)
                            + int(seam_small in edges)
                        )
                    for cutoff in range(2, limit + 1):
                        actual = Fraction(sum(size <= cutoff for size in sizes), d_total)
                        upper = (
                            int(retained <= cutoff - k)
                            + Fraction(d_total - retained, d_total)
                            * int(retained <= cutoff)
                        )
                        assert actual <= upper


def a_two_coefficients_formula(k: int) -> dict[int, Fraction]:
    """One-seam marked plus separated-cycle untouched formula."""
    out: dict[int, Fraction] = defaultdict(Fraction)
    for split in range(1, (k - 1) // 2 + 1):
        q = qsplit(k, split)
        # A marked-parent channel.  The retained union has source length t;
        # it has ambient size t unless it contains the unique block seam,
        # in which case its size is t+2k.
        for parent in (split, k - split):
            for retained in range(2, parent):
                mass = q * (retained - 1) * kernel(k, parent, retained)
                out[retained] += mass * Fraction(k - retained, k)
                out[retained + 2 * k] += mass * Fraction(retained, k)

        # A untouched-cycle channel.  The two one-run faces have sizes x
        # and y, where x=s or k-s and the second-face raw mass is
        # (k-y)K(k,y).  Their complement has size 3k-x-y.
        for first_face, first_mass in (
            (split, Fraction(k - split, k)),
            (k - split, Fraction(split, k)),
        ):
            for second_face in range(1, k):
                size = 3 * k - first_face - second_face
                out[size] += (
                    q
                    * first_mass
                    * (k - second_face)
                    * kernel(k, k, second_face)
                )
    return dict(out)


def coefficient_digest(coefficients: dict[int, Fraction]) -> str:
    payload = "|".join(
        f"{size}:{value.numerator}/{value.denominator}"
        for size, value in sorted(coefficients.items())
    )
    return sha256(payload.encode()).hexdigest()


def audit_formula(k: int) -> dict[str, object]:
    literal_b = literal_two_coefficients(k, "B")
    literal_a = literal_two_coefficients(k, "A")
    formula_b = b_two_coefficients_formula(k)
    formula_a = a_two_coefficients_formula(k)
    assert literal_b == formula_b
    assert literal_a == formula_a
    check_b_placement_bound(k)
    limit = (3 * k - 1) // 2
    prefix_b = prefix_a = Fraction()
    max_signed = (0.0, 0, Fraction())
    max_b = (0.0, 0, Fraction())
    max_a = (0.0, 0, Fraction())
    for cutoff in range(2, limit + 1):
        prefix_b += literal_b.get(cutoff, Fraction())
        prefix_a += literal_a.get(cutoff, Fraction())
        scaled_b = k * float(prefix_b) / cutoff ** 0.5
        scaled_a = k * float(prefix_a) / cutoff ** 0.5
        if scaled_b > max_b[0]:
            max_b = (scaled_b, cutoff, prefix_b)
        if scaled_a > max_a[0]:
            max_a = (scaled_a, cutoff, prefix_a)
        signed = prefix_b - prefix_a
        scaled = k * abs(float(signed)) / cutoff ** 0.5
        if scaled > max_signed[0]:
            max_signed = (scaled, cutoff, signed)
    return {
        "k": k,
        "exact_formula_match": True,
        "b_placement_bound": True,
        "b_coefficient_digest": coefficient_digest(literal_b),
        "a_coefficient_digest": coefficient_digest(literal_a),
        "max_scaled_signed_prefix": max_signed[0],
        "max_cutoff": max_signed[1],
        "signed_prefix": str(max_signed[2]),
        "max_scaled_b_prefix": max_b[0],
        "max_b_cutoff": max_b[1],
        "b_prefix": str(max_b[2]),
        "max_scaled_a_prefix": max_a[0],
        "max_a_cutoff": max_a[1],
        "a_prefix": str(max_a[2]),
    }


if __name__ == "__main__":
    payload = {
        "mission": "M235",
        "method": "literal ordered tuples versus independent seam formulas",
        "universal_inference_from_finite_checks": False,
        "audits": [audit_formula(candidate_k) for candidate_k in (3, 5, 7)],
        "theorem": {
            "claim": "TCM",
            "domain": "odd k>=3 and 2<=ell<=(3k-1)/2",
            "proved_bound": "|sum_{y=2}^ell cT_{k,y}| <= 160 sqrt(ell)/k",
            "proof_depends_on_finite_checks": False,
            "status": "proved_subject_to_fresh_audit",
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
