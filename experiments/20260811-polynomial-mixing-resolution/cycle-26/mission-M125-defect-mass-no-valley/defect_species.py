#!/usr/bin/env python3
"""Exact defect coefficients from the M113 connected-incidence cell formula.

This does not enumerate permutations, transposition words, or pairs of set
partitions.  It sums over integer cycle types.  For each indexed collection of
permutation-cycle atoms it builds the weighted one-colour partition polynomial
and then uses the labelled SET/connected-component recurrence to extract pairs
of partitions whose join is indiscrete.  On the diagonal L+R=c this is exactly
the connected-unicyclic incidence condition.

All arithmetic is fractions/integers.  The computation is deterministic and
has no random seed.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import itertools
import json
import math
import platform
import subprocess
import time
from fractions import Fraction
from pathlib import Path


def integer_partitions(n: int, minimum: int = 1) -> list[tuple[int, ...]]:
    """Increasing integer partitions of n."""
    if n == 0:
        return [()]
    out: list[tuple[int, ...]] = []
    for first in range(minimum, n + 1):
        for rest in integer_partitions(n - first, first):
            out.append((first,) + rest)
    return out


def poly_zero(rows: int, cols: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(cols)] for _ in range(rows)]


def poly_convolve_add(
    target: list[list[Fraction]],
    first: list[list[Fraction]],
    second: list[list[Fraction]],
    sign: int = 1,
) -> None:
    for i, row in enumerate(first):
        for j, value in enumerate(row):
            if not value:
                continue
            for k, row2 in enumerate(second):
                if i + k >= len(target):
                    break
                for ell, value2 in enumerate(row2):
                    if j + ell >= len(target[i + k]):
                        break
                    if value2:
                        target[i + k][j + ell] += sign * value * value2


def connected_incidence_polynomial_subset(
    atom_sizes: tuple[int, ...],
) -> list[list[Fraction]]:
    """Return C[L][R] for connected pairs of weighted atom partitions.

    A block B containing q cycle atoms and n original labels has weight
    n^(q-3).  A pair (pi_L,pi_R) is connected when pi_L join pi_R is the
    indiscrete partition.  The returned coefficient is the sum of products of
    all left and right block weights.
    """
    c = len(atom_sizes)
    full = (1 << c) - 1
    popcount = [mask.bit_count() for mask in range(full + 1)]
    size_sum = [0] * (full + 1)
    for mask in range(1, full + 1):
        bit = mask & -mask
        size_sum[mask] = size_sum[mask ^ bit] + atom_sizes[bit.bit_length() - 1]
    block_weight = [Fraction(0)] * (full + 1)
    for mask in range(1, full + 1):
        block_weight[mask] = Fraction(size_sum[mask], 1) ** (popcount[mask] - 3)

    # P_S(y)=sum_{partitions pi of S} y^|pi| product_{B in pi} w(B).
    one_colour: list[list[Fraction]] = [[] for _ in range(full + 1)]
    one_colour[0] = [Fraction(1)]
    for cardinality in range(1, c + 1):
        for mask in range(1, full + 1):
            if popcount[mask] != cardinality:
                continue
            values = [Fraction(0) for _ in range(cardinality + 1)]
            root = mask & -mask
            optional = mask ^ root
            sub = optional
            while True:
                block = root | sub
                remainder = mask ^ block
                weight = block_weight[block]
                for blocks, value in enumerate(one_colour[remainder]):
                    if value:
                        values[blocks + 1] += weight * value
                if sub == 0:
                    break
                sub = (sub - 1) & optional
            one_colour[mask] = values

    # A_S(y,z)=P_S(y)P_S(z), the pair-partition polynomial without a
    # connectedness condition.  Every such object is a SET of components of
    # the join.  Selecting the component U containing the least atom gives
    # A_S=sum_{root in U subset S} C_U A_{S-U}, hence the recurrence below.
    arbitrary: list[list[list[Fraction]]] = []
    for mask in range(full + 1):
        q = popcount[mask]
        matrix = poly_zero(q + 1, q + 1)
        for left, value_left in enumerate(one_colour[mask]):
            for right, value_right in enumerate(one_colour[mask]):
                matrix[left][right] = value_left * value_right
        arbitrary.append(matrix)

    connected: list[list[list[Fraction]]] = [poly_zero(1, 1) for _ in range(full + 1)]
    for cardinality in range(1, c + 1):
        for mask in range(1, full + 1):
            if popcount[mask] != cardinality:
                continue
            matrix = [row[:] for row in arbitrary[mask]]
            root = mask & -mask
            optional = mask ^ root
            sub = optional
            while sub:
                component = root | sub
                if component != mask:
                    remainder = mask ^ component
                    poly_convolve_add(
                        matrix, connected[component], arbitrary[remainder], sign=-1
                    )
                sub = (sub - 1) & optional
            # The case component={root} is omitted by the loop above when
            # sub=0, so include it separately whenever the set is nontrivial.
            if cardinality > 1:
                component = root
                remainder = mask ^ root
                poly_convolve_add(
                    matrix, connected[component], arbitrary[remainder], sign=-1
                )
            connected[mask] = matrix
    return connected[full]


def connected_incidence_polynomial(
    atom_sizes: tuple[int, ...],
) -> list[list[Fraction]]:
    """Return the same polynomial with equal-size atoms aggregated exactly.

    The subset recurrence above treats all cycle atoms individually.  This
    implementation groups subsets by their multiplicity vector.  Binomial
    coefficients count the choices of the other indexed atoms after fixing
    the least available atom as root.  It is algebraically the same rooted
    recurrence but avoids a 2^c table for cycle types with repeated parts.
    """
    distinct = tuple(sorted(set(atom_sizes)))
    initial = tuple(atom_sizes.count(size) for size in distinct)

    def cardinality(counts: tuple[int, ...]) -> int:
        return sum(counts)

    def rooted_submultisets(
        counts: tuple[int, ...],
    ) -> tuple[int, tuple[int, ...], itertools.product]:
        root_index = next(index for index, count in enumerate(counts) if count)
        available = list(counts)
        available[root_index] -= 1
        choices = itertools.product(*(range(count + 1) for count in available))
        return root_index, tuple(available), choices

    @functools.cache
    def one_colour(counts: tuple[int, ...]) -> tuple[Fraction, ...]:
        q_total = cardinality(counts)
        if q_total == 0:
            return (Fraction(1),)
        values = [Fraction(0) for _ in range(q_total + 1)]
        root_index, available, choices = rooted_submultisets(counts)
        for extras in choices:
            block = list(extras)
            block[root_index] += 1
            block_tuple = tuple(block)
            q_block = cardinality(block_tuple)
            label_size = sum(
                size * count for size, count in zip(distinct, block_tuple)
            )
            multiplicity = math.prod(
                math.comb(available[index], extras[index])
                for index in range(len(distinct))
            )
            weight = Fraction(label_size, 1) ** (q_block - 3)
            remainder = tuple(
                counts[index] - block_tuple[index]
                for index in range(len(distinct))
            )
            for blocks, value in enumerate(one_colour(remainder)):
                values[blocks + 1] += multiplicity * weight * value
        return tuple(values)

    @functools.cache
    def arbitrary(counts: tuple[int, ...]) -> tuple[tuple[Fraction, ...], ...]:
        q_total = cardinality(counts)
        values = one_colour(counts)
        return tuple(
            tuple(values[left] * values[right] for right in range(q_total + 1))
            for left in range(q_total + 1)
        )

    @functools.cache
    def connected(counts: tuple[int, ...]) -> tuple[tuple[Fraction, ...], ...]:
        q_total = cardinality(counts)
        matrix = [list(row) for row in arbitrary(counts)]
        root_index, available, choices = rooted_submultisets(counts)
        for extras in choices:
            component = list(extras)
            component[root_index] += 1
            component_tuple = tuple(component)
            if component_tuple == counts:
                continue
            multiplicity = math.prod(
                math.comb(available[index], extras[index])
                for index in range(len(distinct))
            )
            remainder = tuple(
                counts[index] - component_tuple[index]
                for index in range(len(distinct))
            )
            component_poly = connected(component_tuple)
            remainder_poly = arbitrary(remainder)
            for left, row in enumerate(component_poly):
                for right, value in enumerate(row):
                    if not value:
                        continue
                    for left2, row2 in enumerate(remainder_poly):
                        for right2, value2 in enumerate(row2):
                            if value2:
                                matrix[left + left2][right + right2] -= (
                                    multiplicity * value * value2
                                )
        return tuple(tuple(row) for row in matrix)

    return [list(row) for row in connected(initial)]


def cycle_type_permutation_count(d: int, cycle_type: tuple[int, ...]) -> int:
    multiplicities: dict[int, int] = {}
    for size in cycle_type:
        multiplicities[size] = multiplicities.get(size, 0) + 1
    denominator = 1
    for size, multiplicity in multiplicities.items():
        denominator *= size**multiplicity * math.factorial(multiplicity)
    return math.factorial(d) // denominator


def hurwitz_atom_weight(size: int) -> Fraction:
    return Fraction(size**size, math.factorial(size - 1)) ** 2


def defect_row(d: int) -> tuple[list[int], list[dict]]:
    if d < 2:
        raise ValueError("d must be at least 2")
    masses = [Fraction(0) for _ in range(d - 1)]
    type_records: list[dict] = []
    for cycle_type in integer_partitions(d):
        c = len(cycle_type)
        # A realizable key has at least one left and one right block and its
        # connected-unicyclic incidence graph has c edges and c vertices.
        # Hence c=|Q_L|+|Q_R|>=2.  The one-cycle type contributes no key and
        # would otherwise address the nonexistent defect slot d-1.
        if c < 2:
            continue
        defect = d - c
        incidence = connected_incidence_polynomial(cycle_type)
        type_multiplier = Fraction(cycle_type_permutation_count(d, cycle_type), 1)
        for size in cycle_type:
            type_multiplier *= hurwitz_atom_weight(size)
        subtotal = Fraction(0)
        cut_terms = []
        for left_blocks in range(1, c):
            right_blocks = c - left_blocks
            incidence_weight = incidence[left_blocks][right_blocks]
            if not incidence_weight:
                continue
            cut = d + right_blocks - left_blocks
            term = (
                type_multiplier
                * math.factorial(cut)
                * math.factorial(2 * d - cut)
                * incidence_weight
            )
            subtotal += term
            cut_terms.append(
                {
                    "left_blocks": left_blocks,
                    "right_blocks": right_blocks,
                    "cut": cut,
                    "incidence_weight": str(incidence_weight),
                    "mass": str(term),
                }
            )
        masses[defect] += subtotal
        type_records.append(
            {
                "cycle_type": list(cycle_type),
                "cycles": c,
                "defect": defect,
                "permutation_count": cycle_type_permutation_count(d, cycle_type),
                "atom_weight": str(
                    math.prod((hurwitz_atom_weight(size) for size in cycle_type), start=Fraction(1))
                ),
                "cut_terms": cut_terms,
                "subtotal": str(subtotal),
            }
        )
    if any(value.denominator != 1 for value in masses):
        raise AssertionError((d, masses))
    return [value.numerator for value in masses], type_records


def primitive(row: list[int]) -> tuple[list[int], int]:
    divisor = 0
    for value in row:
        divisor = math.gcd(divisor, value)
    return [value // divisor for value in row], divisor


def sequence_checks(row: list[int]) -> dict:
    n = len(row) - 1
    ordinary_margins = [
        row[r] ** 2 - row[r - 1] * row[r + 1] for r in range(1, len(row) - 1)
    ]
    # Ultra-log-concavity means a_r/binom(n,r) is log-concave.  Clearing
    # denominators gives r(n-r) a_r^2 >= (r+1)(n-r+1)a_{r-1}a_{r+1}.
    ulc_margins = [
        r * (n - r) * row[r] ** 2
        - (r + 1) * (n - r + 1) * row[r - 1] * row[r + 1]
        for r in range(1, len(row) - 1)
    ]
    mode_value = max(row)
    first_mode = row.index(mode_value)
    last_mode = len(row) - 1 - list(reversed(row)).index(mode_value)
    unimodal = (
        all(row[i] <= row[i + 1] for i in range(first_mode))
        and all(row[i] == mode_value for i in range(first_mode, last_mode + 1))
        and all(row[i] >= row[i + 1] for i in range(last_mode, len(row) - 1))
    )
    return {
        "unimodal": unimodal,
        "log_concave": all(value >= 0 for value in ordinary_margins),
        "log_concavity_margins": ordinary_margins,
        "ultra_log_concave": all(value >= 0 for value in ulc_margins),
        "ulc_cleared_margins": ulc_margins,
        "mode_interval": [first_mode, last_mode],
    }


def polynomial_roots(row: list[int]) -> list[dict[str, float]] | None:
    try:
        import numpy as np
    except ImportError:
        return None
    roots = np.roots(list(reversed(row)))
    return [
        {"real": float(value.real), "imag": float(value.imag)}
        for value in sorted(roots, key=lambda z: (float(z.real), float(z.imag)))
    ]


def git_commit() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unavailable"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", nargs="+", type=int, default=list(range(2, 8)))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--include-types", action="store_true")
    parser.add_argument("--numeric-roots", action="store_true")
    args = parser.parse_args()
    if any(d < 2 for d in args.d):
        raise SystemExit("all d must be at least 2")
    started = time.time()
    cases = []
    for d in args.d:
        case_started = time.time()
        row, type_records = defect_row(d)
        primitive_row, gcd = primitive(row)
        record = {
            "d": d,
            "raw_integer_masses": row,
            "primitive_integer_masses": primitive_row,
            "common_gcd": gcd,
            "total_mass": sum(row),
            "checks": sequence_checks(row),
            "elapsed_seconds": time.time() - case_started,
        }
        if args.numeric_roots:
            record["defect_polynomial_roots_numeric"] = polynomial_roots(row)
        if args.include_types:
            record["cycle_type_contributions"] = type_records
        cases.append(record)
        print(f"d={d} primitive={primitive_row} checks={record['checks']}", flush=True)
    payload = {
        "claim_scope": (
            "exact coefficient evaluation from the M113 cell formula; finite sequence "
            "checks do not prove a universal no-valley statement"
        ),
        "target": "M[d,r]=sum_{R(kappa)=r}|C_kappa| for rho(kappa)=|C_kappa|/Z_inc",
        "coefficient_method": (
            "integer cycle types + weighted partition polynomial + exact rooted "
            "multiset-aggregated connected recurrence; retain only L+R=c"
        ),
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "numpy": None,
        "seed": None,
        "arguments": {
            "d": args.d,
            "output": str(args.output),
            "include_types": args.include_types,
            "numeric_roots": args.numeric_roots,
        },
        "cases": cases,
        "elapsed_seconds": time.time() - started,
    }
    try:
        import numpy as np

        payload["numpy"] = np.__version__
    except ImportError:
        pass
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(f"wrote {args.output} sha256={sha256(args.output)}", flush=True)


if __name__ == "__main__":
    main()
