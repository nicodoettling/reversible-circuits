#!/usr/bin/env python3
"""Clean-room exact referee for the frozen M235 TCM theorem.

This standard-library program imports no predecessor module or generated
data.  It compares a literal permutation enumeration with independently
implemented seam/marked/untouched coefficient laws at k=3,5,7.  It also
checks the B cyclic-placement inequality tuple by tuple and finite-falsifies
the componentwise constant bookkeeping.  None of the finite checks is used
as a universal proof.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from math import factorial


Permutation = tuple[int, ...]
Edge = tuple[int, int]


def borel_without_common_exponential(r: int) -> Fraction:
    assert r >= 1
    return Fraction(r ** (r - 1), factorial(r))


def split_kernel(k: int, parent: int, child: int) -> Fraction:
    assert 1 <= child < parent
    b = borel_without_common_exponential
    return b(child) * b(parent - child) / ((2 * k - 3) * b(parent))


def first_split_weight(k: int, s: int) -> Fraction:
    assert 1 <= s <= (k - 1) // 2
    b = borel_without_common_exponential
    return Fraction(k, k - 1) * b(s) * b(k - s) / b(k)


def multiply(p: Permutation, q: Permutation) -> Permutation:
    """Return p o q, so (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def invert(p: Permutation) -> Permutation:
    ans = [0] * len(p)
    for x, y in enumerate(p):
        ans[y] = x
    return tuple(ans)


def cycle(n: int, vertices: tuple[int, ...]) -> Permutation:
    p = list(range(n))
    for x, y in zip(vertices, vertices[1:] + vertices[:1]):
        p[x] = y
    return tuple(p)


def swap(n: int, edge: Edge) -> Permutation:
    x, y = edge
    p = list(range(n))
    p[x], p[y] = p[y], p[x]
    return tuple(p)


def cycle_parts(p: Permutation) -> list[tuple[int, ...]]:
    unseen = set(range(len(p)))
    ans: list[tuple[int, ...]] = []
    while unseen:
        start = min(unseen)
        part: list[int] = []
        x = start
        while x in unseen:
            unseen.remove(x)
            part.append(x)
            x = p[x]
        ans.append(tuple(part))
    return ans


def edges_internal_to_cycles(p: Permutation) -> list[Edge]:
    return [
        (x, y)
        for part in cycle_parts(p)
        for x, y in combinations(part, 2)
    ]


def ambient_run_count(part: tuple[int, ...], n: int) -> int:
    support = set(part)
    return sum((x - 1) % n not in support for x in support)


def source_data(k: int, side: str) -> tuple[Permutation, list[tuple[int, ...]]]:
    n = 3 * k
    if side == "B":
        exterior = tuple(range(1, k)) + tuple(range(2 * k, 3 * k))
        return cycle(n, exterior), [exterior]
    lower = tuple(range(k))
    upper = tuple(range(2 * k, 3 * k))
    return multiply(cycle(n, lower), cycle(n, upper)), [lower, upper]


def smaller_cyclic_split(edge: Edge, originals: list[tuple[int, ...]]) -> int:
    x, y = edge
    original = next(part for part in originals if x in part and y in part)
    forward = (original.index(y) - original.index(x)) % len(original)
    return min(forward, len(original) - forward)


def literal_law(k: int, side: str) -> tuple[dict[int, Fraction], dict[str, object]]:
    """Enumerate the literal ordered disjoint-pair raw two-run law."""
    n = 3 * k
    target = cycle(n, tuple(range(n)))
    source, originals = source_data(k, side)
    first_normalizer = 2 * k - 1 if side == "B" else 2 * k
    j = (k - 1) // 2
    coefficients: dict[int, Fraction] = defaultdict(Fraction)
    records_by_split: Counter[int] = Counter()
    first_edges_by_split: dict[int, set[Edge]] = defaultdict(set)
    parent_counts: Counter[tuple[int, str, int]] = Counter()

    for e in edges_internal_to_cycles(source):
        s = smaller_cyclic_split(e, originals)
        if s > j:
            continue
        first_edges_by_split[s].add(e)
        e_perm = swap(n, e)
        after_e = multiply(e_perm, source)
        after_e_parts = cycle_parts(after_e)
        marked_original = next(set(part) for part in originals if set(e) <= set(part))
        for f in edges_internal_to_cycles(after_e):
            if set(e) & set(f):
                continue
            parent = next(part for part in after_e_parts if set(f) <= set(part))
            kind = "marked" if set(parent) <= marked_original else "untouched"
            after_f = multiply(swap(n, f), after_e)
            children = [part for part in cycle_parts(after_f) if set(part) <= set(parent)]
            assert len(children) == 2

            ef = multiply(e_perm, swap(n, f))
            residual = multiply(invert(ef), target)
            residual_parts = cycle_parts(residual)
            run_profile = sorted(ambient_run_count(part, n) for part in residual_parts)
            assert run_profile == [1, 1, 2]
            two_run_parts = [
                part for part in residual_parts if ambient_run_count(part, n) == 2
            ]
            assert len(two_run_parts) == 1
            two_size = len(two_run_parts[0])
            weight = (
                first_split_weight(k, s)
                * split_kernel(k, len(parent), len(children[0]))
                / first_normalizer
            )
            coefficients[two_size] += weight
            records_by_split[s] += 1
            parent_counts[(s, kind, len(parent))] += 1

    for s in range(1, j + 1):
        assert len(first_edges_by_split[s]) == first_normalizer
        if side == "B":
            d_total = 2 * k - 1
            placements_per_first = sum(
                retained - 1
                for parent in (s, d_total - s)
                for retained in range(2, parent)
            )
        else:
            placements_per_first = (
                sum(retained - 1 for parent in (s, k - s) for retained in range(2, parent))
                + k * (k - 1) // 2
            )
        assert records_by_split[s] == first_normalizer * placements_per_first

    diagnostics = {
        "record_count": sum(records_by_split.values()),
        "records_by_split": {str(s): records_by_split[s] for s in sorted(records_by_split)},
        "first_edges_per_split": {
            str(s): len(first_edges_by_split[s]) for s in sorted(first_edges_by_split)
        },
        "parent_record_counts": {
            f"s={s},{kind},r={r}": count
            for (s, kind, r), count in sorted(parent_counts.items())
        },
    }
    return dict(coefficients), diagnostics


def b_formula_law(k: int) -> tuple[dict[int, Fraction], dict[str, object]]:
    """Evaluate retained arcs from source-edge increments, then seam identity."""
    n = 3 * k
    d_total = 2 * k - 1
    j = (k - 1) // 2
    exterior = tuple(range(1, k)) + tuple(range(2 * k, 3 * k))
    increments = [
        (exterior[(i + 1) % d_total] - exterior[i]) % n for i in range(d_total)
    ]
    exceptional = [(i, delta - 1) for i, delta in enumerate(increments) if delta != 1]
    assert sorted(extra for _, extra in exceptional) == [1, k]
    small_seam = next(i for i, extra in exceptional if extra == 1)
    large_seam = next(i for i, extra in exceptional if extra == k)

    coefficients: dict[int, Fraction] = defaultdict(Fraction)
    placement_checks = 0
    max_actual_minus_bound = Fraction()
    limit = (3 * k - 1) // 2
    for s in range(1, j + 1):
        q = first_split_weight(k, s)
        for parent in (s, d_total - s):
            for middle in range(1, parent):
                retained = parent - middle
                for a in range(1, retained):
                    sizes: list[int] = []
                    for start in range(d_total):
                        edge_positions = {
                            (start + offset) % d_total
                            for offset in list(range(a))
                            + list(range(a + middle, parent))
                        }
                        assert len(edge_positions) == retained
                        direct_size = sum(increments[pos] for pos in edge_positions)
                        seam_size = (
                            retained
                            + k * int(large_seam in edge_positions)
                            + int(small_seam in edge_positions)
                        )
                        assert direct_size == seam_size
                        sizes.append(direct_size)
                        coefficients[direct_size] += (
                            q * split_kernel(k, parent, middle) / d_total
                        )
                    for ell in range(2, limit + 1):
                        actual = Fraction(sum(y <= ell for y in sizes), d_total)
                        bound = (
                            int(retained <= ell - k)
                            + Fraction(d_total - retained, d_total)
                            * int(retained <= ell)
                        )
                        assert actual <= bound
                        max_actual_minus_bound = max(max_actual_minus_bound, actual - bound)
                        placement_checks += 1
    return dict(coefficients), {
        "large_seam_edge": large_seam,
        "small_seam_edge": small_seam,
        "placement_inequalities_checked": placement_checks,
        "maximum_actual_minus_bound": str(max_actual_minus_bound),
    }


def a_formula_law(k: int) -> dict[int, Fraction]:
    """Evaluate the independent marked and untouched closed coefficient laws."""
    j = (k - 1) // 2
    coefficients: dict[int, Fraction] = defaultdict(Fraction)
    for s in range(1, j + 1):
        q = first_split_weight(k, s)
        for parent in (s, k - s):
            for retained in range(2, parent):
                raw = q * (retained - 1) * split_kernel(k, parent, retained)
                coefficients[retained] += raw * Fraction(k - retained, k)
                coefficients[retained + 2 * k] += raw * Fraction(retained, k)

        for first_face, first_mass in (
            (s, Fraction(k - s, k)),
            (k - s, Fraction(s, k)),
        ):
            for second_face in range(1, k):
                two_size = 3 * k - first_face - second_face
                raw_second_mass = (k - second_face) * split_kernel(
                    k, k, second_face
                )
                coefficients[two_size] += q * first_mass * raw_second_mass
    return dict(coefficients)


def canonical_digest(coefficients: dict[int, Fraction]) -> str:
    payload = [
        [size, value.numerator, value.denominator]
        for size, value in sorted(coefficients.items())
    ]
    return sha256(json.dumps(payload, separators=(",", ":")).encode()).hexdigest()


def exact_sqrt_bound(value: Fraction, constant: int, ell: int, k: int) -> bool:
    assert value >= 0
    return (value * k) ** 2 <= constant * constant * ell


def component_bounds(k: int, ell: int) -> dict[str, Fraction]:
    """Reconstruct every positive component used in M235 Sections 4 and 6."""
    d_total = 2 * k - 1
    j = (k - 1) // 2
    b_short = Fraction()
    b_long_free = Fraction()
    b_long_low = Fraction()
    b_long_high = Fraction()
    a_short = Fraction()
    a_long_low = Fraction()
    a_long_high = Fraction()
    a_untouched = Fraction()

    for s in range(1, j + 1):
        q = first_split_weight(k, s)
        for retained in range(2, s):
            base = q * (retained - 1) * split_kernel(k, s, retained)
            brace = int(retained <= ell - k) + Fraction(
                d_total - retained, d_total
            ) * int(retained <= ell)
            b_short += base * brace
            if retained <= ell:
                a_short += base * Fraction(k - retained, k)

        long_b_parent = d_total - s
        for retained in range(2, long_b_parent):
            base = q * (retained - 1) * split_kernel(
                k, long_b_parent, retained
            )
            if retained <= ell - k:
                b_long_free += base
            if retained <= ell:
                seam_exclusion = Fraction(d_total - retained, d_total)
                if 2 * retained <= long_b_parent:
                    b_long_low += base * seam_exclusion
                else:
                    b_long_high += base * seam_exclusion

        long_a_parent = k - s
        for retained in range(2, long_a_parent):
            if retained > ell:
                continue
            base = (
                q
                * (retained - 1)
                * split_kernel(k, long_a_parent, retained)
                * Fraction(k - retained, k)
            )
            if 2 * retained <= k:
                a_long_low += base
            else:
                a_long_high += base

        for c in range(1, ell - k - s + 1):
            a_untouched += (
                q * Fraction(s, k) * c * split_kernel(k, k, c)
            )

    components = {
        "B_short": b_short,
        "B_long_free": b_long_free,
        "B_long_low": b_long_low,
        "B_long_high": b_long_high,
        "A_mark_short": a_short,
        "A_mark_long_low": a_long_low,
        "A_mark_long_high": a_long_high,
        "A_untouched": a_untouched,
    }
    constants = {
        "B_short": 24,
        "B_long_free": 4,
        "B_long_low": 4,
        "B_long_high": 52,
        "A_mark_short": 12,
        "A_mark_long_low": 12,
        "A_mark_long_high": 17,
        "A_untouched": 20,
    }
    for name, value in components.items():
        assert exact_sqrt_bound(value, constants[name], ell, k), (k, ell, name, value)
    assert exact_sqrt_bound(
        b_short + b_long_free + b_long_low + b_long_high, 84, ell, k
    )
    assert exact_sqrt_bound(
        a_short + a_long_low + a_long_high + a_untouched, 61, ell, k
    )
    return components


def audit_k(k: int) -> dict[str, object]:
    literal_b, literal_b_diag = literal_law(k, "B")
    literal_a, literal_a_diag = literal_law(k, "A")
    formula_b, placement_diag = b_formula_law(k)
    formula_a = a_formula_law(k)
    assert literal_b == formula_b
    assert literal_a == formula_a
    limit = (3 * k - 1) // 2
    prefix_b = Fraction()
    prefix_a = Fraction()
    max_scaled_square = Fraction()
    maximizing_ell = 2
    maximizing_signed = Fraction()
    for ell in range(2, limit + 1):
        prefix_b += literal_b.get(ell, Fraction())
        prefix_a += literal_a.get(ell, Fraction())
        signed = prefix_b - prefix_a
        scaled_square = signed * signed * k * k / ell
        if scaled_square > max_scaled_square:
            max_scaled_square = scaled_square
            maximizing_ell = ell
            maximizing_signed = signed
        assert scaled_square <= 160 * 160
    return {
        "k": k,
        "literal_formula_match": True,
        "b_coefficient_digest": canonical_digest(literal_b),
        "a_coefficient_digest": canonical_digest(literal_a),
        "b_record_count": literal_b_diag["record_count"],
        "a_record_count": literal_a_diag["record_count"],
        "first_edges_per_split_b": next(
            iter(set(literal_b_diag["first_edges_per_split"].values()))
        ),
        "first_edges_per_split_a": next(
            iter(set(literal_a_diag["first_edges_per_split"].values()))
        ),
        "placement_inequalities_checked": placement_diag[
            "placement_inequalities_checked"
        ],
        "maximizing_allowed_cutoff": maximizing_ell,
        "signed_prefix_at_maximum": str(maximizing_signed),
        "maximum_scaled_absolute_prefix": float(max_scaled_square) ** 0.5,
    }


def convolution_audit(max_m: int) -> dict[str, object]:
    b = borel_without_common_exponential
    for m in range(2, max_m + 1):
        total = sum((b(a) * b(m - a) for a in range(1, m)), Fraction())
        assert total == Fraction(2 * (m - 1), m) * b(m)
        weighted = sum(
            ((a - 1) * b(a) * b(m - a) for a in range(1, m)),
            Fraction(),
        )
        assert weighted == Fraction((m - 1) * (m - 2), m) * b(m)
    return {
        "m_min": 2,
        "m_max": max_m,
        "rooted_tree_convolution": True,
        "weighted_convolution": True,
    }


def finite_constant_audit(max_k: int) -> dict[str, object]:
    checked = 0
    for k in range(3, max_k + 1, 2):
        q_total = sum(
            (first_split_weight(k, s) for s in range(1, (k - 1) // 2 + 1)),
            Fraction(),
        )
        assert q_total == 1
        for ell in range(2, (3 * k - 1) // 2 + 1):
            components = component_bounds(k, ell)
            assert len(components) == 8
            checked += 1
    return {
        "odd_k_min": 3,
        "odd_k_max": max_k,
        "parameter_pairs": checked,
        "all_component_claims_pass": True,
        "universal_inference": False,
    }


def main() -> None:
    payload = {
        "mission": "M238",
        "method": "clean-room literal permutations versus independent coefficient laws",
        "imports_predecessor_code_or_data": False,
        "coefficient_audits": [audit_k(k) for k in (3, 5, 7)],
        "convolution_audit": convolution_audit(31),
        "finite_constant_audit": finite_constant_audit(31),
        "theorem_scope": "TCM constant 160 only",
        "universal_inference_from_finite_checks": False,
        "verdict": "ACCEPT",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
