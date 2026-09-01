#!/usr/bin/env python3
"""Fresh exact referee checker for the frozen M125 coefficient package.

This file intentionally does not import any M125 module.  It implements three
separate enumerators for weighted pairs of cycle-atom partitions:

* literal pairs of set partitions;
* an indexed-subset root recurrence; and
* an equal-size-atom multiset recurrence using a different root convention.

All calculations are deterministic and use exact Fraction arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
import subprocess
import time
from functools import cache
from fractions import Fraction
from pathlib import Path


Partition = tuple[tuple[int, ...], ...]
Matrix = tuple[tuple[Fraction, ...], ...]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_commit() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], text=True
    ).strip()


def integer_partitions(total: int, lower: int = 1):
    """Yield nondecreasing integer partitions of total."""
    if total == 0:
        yield ()
        return
    for first in range(lower, total + 1):
        for rest in integer_partitions(total - first, first):
            yield (first,) + rest


@cache
def set_partitions(n: int) -> tuple[Partition, ...]:
    """Canonical set partitions of range(n)."""
    if n == 0:
        return ((),)
    previous = set_partitions(n - 1)
    atom = n - 1
    out: list[Partition] = []
    for partition in previous:
        for index in range(len(partition)):
            blocks = list(partition)
            blocks[index] = blocks[index] + (atom,)
            out.append(tuple(blocks))
        out.append(partition + ((atom,),))
    return tuple(out)


def block_weight(atom_sizes: tuple[int, ...], block: tuple[int, ...]) -> Fraction:
    label_count = sum(atom_sizes[index] for index in block)
    return Fraction(label_count) ** (len(block) - 3)


def partition_weight(
    atom_sizes: tuple[int, ...], partition: Partition
) -> Fraction:
    answer = Fraction(1)
    for block in partition:
        answer *= block_weight(atom_sizes, block)
    return answer


def join_connected(n: int, left: Partition, right: Partition) -> bool:
    parent = list(range(n))

    def find(vertex: int) -> int:
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    def union(first: int, second: int) -> None:
        first_root, second_root = find(first), find(second)
        if first_root != second_root:
            parent[second_root] = first_root

    for partition in (left, right):
        for block in partition:
            for atom in block[1:]:
                union(block[0], atom)
    return len({find(atom) for atom in range(n)}) == 1


def zero_matrix(size: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(size)] for _ in range(size)]


def freeze_matrix(matrix: list[list[Fraction]]) -> Matrix:
    return tuple(tuple(row) for row in matrix)


def direct_connected_polynomial(atom_sizes: tuple[int, ...]) -> Matrix:
    """Literal enumeration of all ordered pairs of set partitions."""
    c = len(atom_sizes)
    answer = zero_matrix(c + 1)
    partitions = set_partitions(c)
    weights = {
        partition: partition_weight(atom_sizes, partition)
        for partition in partitions
    }
    for left in partitions:
        for right in partitions:
            if join_connected(c, left, right):
                answer[len(left)][len(right)] += weights[left] * weights[right]
    return freeze_matrix(answer)


def outer(values: tuple[Fraction, ...]) -> Matrix:
    return tuple(
        tuple(left * right for right in values)
        for left in values
    )


def subtract_convolution(
    target: list[list[Fraction]], first: Matrix, second: Matrix, factor: int = 1
) -> None:
    for left, row in enumerate(first):
        for right, value in enumerate(row):
            if value == 0:
                continue
            for left2, row2 in enumerate(second):
                for right2, value2 in enumerate(row2):
                    if value2:
                        target[left + left2][right + right2] -= (
                            factor * value * value2
                        )


def subset_connected_polynomial(atom_sizes: tuple[int, ...]) -> Matrix:
    """Indexed-subset recurrence rooted at the greatest indexed atom."""
    c = len(atom_sizes)
    full = (1 << c) - 1

    @cache
    def one_colour(mask: int) -> tuple[Fraction, ...]:
        if mask == 0:
            return (Fraction(1),)
        cardinality = mask.bit_count()
        answer = [Fraction(0) for _ in range(cardinality + 1)]
        root = 1 << (mask.bit_length() - 1)
        optional = mask ^ root
        extras = optional
        while True:
            block = extras | root
            indices = tuple(
                index for index in range(c) if block & (1 << index)
            )
            weight = block_weight(atom_sizes, indices)
            remainder = mask ^ block
            for blocks, value in enumerate(one_colour(remainder)):
                answer[blocks + 1] += weight * value
            if extras == 0:
                break
            extras = (extras - 1) & optional
        return tuple(answer)

    @cache
    def arbitrary(mask: int) -> Matrix:
        return outer(one_colour(mask))

    @cache
    def connected(mask: int) -> Matrix:
        cardinality = mask.bit_count()
        answer = [list(row) for row in arbitrary(mask)]
        root = 1 << (mask.bit_length() - 1)
        optional = mask ^ root
        extras = optional
        while True:
            component = extras | root
            if component != mask:
                subtract_convolution(
                    answer, connected(component), arbitrary(mask ^ component)
                )
            if extras == 0:
                break
            extras = (extras - 1) & optional
        assert len(answer) == cardinality + 1
        return freeze_matrix(answer)

    return connected(full)


def multiset_connected_polynomial(atom_sizes: tuple[int, ...]) -> Matrix:
    """Aggregate equal-size atoms, rooting at the largest present size."""
    sizes = tuple(sorted(set(atom_sizes), reverse=True))
    initial = tuple(atom_sizes.count(size) for size in sizes)

    def rooted_choices(counts: tuple[int, ...]):
        root_index = next(index for index, count in enumerate(counts) if count)
        available = list(counts)
        available[root_index] -= 1
        for extras in itertools.product(
            *(range(count + 1) for count in available)
        ):
            chosen = list(extras)
            chosen[root_index] += 1
            multiplicity = math.prod(
                math.comb(available[index], extras[index])
                for index in range(len(sizes))
            )
            yield tuple(chosen), multiplicity

    @cache
    def one_colour(counts: tuple[int, ...]) -> tuple[Fraction, ...]:
        total_atoms = sum(counts)
        if total_atoms == 0:
            return (Fraction(1),)
        answer = [Fraction(0) for _ in range(total_atoms + 1)]
        for block, multiplicity in rooted_choices(counts):
            block_atoms = sum(block)
            block_labels = sum(
                size * count for size, count in zip(sizes, block)
            )
            weight = Fraction(block_labels) ** (block_atoms - 3)
            remainder = tuple(
                counts[index] - block[index]
                for index in range(len(sizes))
            )
            for blocks, value in enumerate(one_colour(remainder)):
                answer[blocks + 1] += multiplicity * weight * value
        return tuple(answer)

    @cache
    def arbitrary(counts: tuple[int, ...]) -> Matrix:
        return outer(one_colour(counts))

    @cache
    def connected(counts: tuple[int, ...]) -> Matrix:
        answer = [list(row) for row in arbitrary(counts)]
        for component, multiplicity in rooted_choices(counts):
            if component == counts:
                continue
            remainder = tuple(
                counts[index] - component[index]
                for index in range(len(sizes))
            )
            subtract_convolution(
                answer,
                connected(component),
                arbitrary(remainder),
                factor=multiplicity,
            )
        return freeze_matrix(answer)

    return connected(initial)


def permutation_type_count(d: int, cycle_type: tuple[int, ...]) -> int:
    denominator = 1
    for size in set(cycle_type):
        multiplicity = cycle_type.count(size)
        denominator *= size**multiplicity * math.factorial(multiplicity)
    return math.factorial(d) // denominator


def atom_factor(size: int) -> Fraction:
    return Fraction(size**size, math.factorial(size - 1)) ** 2


def type_mass(
    d: int, cycle_type: tuple[int, ...], incidence: Matrix
) -> Fraction:
    c = len(cycle_type)
    if c < 2:
        return Fraction(0)
    multiplier = Fraction(permutation_type_count(d, cycle_type))
    for size in cycle_type:
        multiplier *= atom_factor(size)
    answer = Fraction(0)
    for left_blocks in range(1, c):
        right_blocks = c - left_blocks
        j = d + c - 2 * left_blocks
        answer += (
            multiplier
            * math.factorial(j)
            * math.factorial(2 * d - j)
            * incidence[left_blocks][right_blocks]
        )
    return answer


def defect_row(d: int, engine=multiset_connected_polynomial) -> list[int]:
    row = [Fraction(0) for _ in range(d - 1)]
    for cycle_type in integer_partitions(d):
        c = len(cycle_type)
        if c < 2:
            continue
        row[d - c] += type_mass(d, cycle_type, engine(cycle_type))
    if any(value.denominator != 1 for value in row):
        raise AssertionError((d, row))
    return [value.numerator for value in row]


def primitive(row: list[int]) -> tuple[list[int], int]:
    divisor = math.gcd(*row)
    return [value // divisor for value in row], divisor


def sequence_diagnostics(row: list[int]) -> dict:
    n = len(row) - 1
    ordinary = [
        row[r] ** 2 - row[r - 1] * row[r + 1]
        for r in range(1, len(row) - 1)
    ]
    ulc = [
        r * (n - r) * row[r] ** 2
        - (r + 1) * (n - r + 1) * row[r - 1] * row[r + 1]
        for r in range(1, len(row) - 1)
    ]
    mode = max(row)
    first = row.index(mode)
    last = len(row) - 1 - list(reversed(row)).index(mode)
    unimodal = (
        all(row[index] <= row[index + 1] for index in range(first))
        and all(row[index] == mode for index in range(first, last + 1))
        and all(
            row[index] >= row[index + 1]
            for index in range(last, len(row) - 1)
        )
    )
    return {
        "unimodal": unimodal,
        "log_concave": all(margin >= 0 for margin in ordinary),
        "ultra_log_concave": all(margin >= 0 for margin in ulc),
        "ordinary_margins": ordinary,
        "ulc_margins": ulc,
        "mode_interval": [first, last],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-d", type=int, default=22)
    parser.add_argument("--direct-max-d", type=int, default=6)
    parser.add_argument("--recurrence-compare-max-d", type=int, default=8)
    parser.add_argument(
        "--frozen",
        type=Path,
        default=Path(
            "experiments/20260811-polynomial-mixing-resolution/cycle-26/"
            "mission-M125-defect-mass-no-valley/exact_results.json"
        ),
    )
    parser.add_argument(
        "--m124",
        type=Path,
        default=Path(
            "experiments/20260811-polynomial-mixing-resolution/cycle-25/"
            "mission-M124-m120-fresh-referee/results.json"
        ),
    )
    args = parser.parse_args()
    started = time.time()
    failures: list[dict] = []

    direct_type_cases = 0
    direct_partition_pairs = 0
    direct_rows: dict[int, list[int]] = {}
    for d in range(2, args.direct_max_d + 1):
        direct_row = [Fraction(0) for _ in range(d - 1)]
        for cycle_type in integer_partitions(d):
            c = len(cycle_type)
            if c < 2:
                continue
            direct = direct_connected_polynomial(cycle_type)
            subset = subset_connected_polynomial(cycle_type)
            multiset = multiset_connected_polynomial(cycle_type)
            direct_type_cases += 1
            direct_partition_pairs += len(set_partitions(c)) ** 2
            if direct != subset:
                failures.append(
                    {"kind": "direct_vs_subset", "cycle_type": cycle_type}
                )
            if direct != multiset:
                failures.append(
                    {"kind": "direct_vs_multiset", "cycle_type": cycle_type}
                )
            if any(
                direct[left][right] != direct[right][left]
                for left in range(c + 1)
                for right in range(c + 1)
            ):
                failures.append(
                    {"kind": "colour_symmetry", "cycle_type": cycle_type}
                )
            direct_row[d - c] += type_mass(d, cycle_type, direct)
        if any(value.denominator != 1 for value in direct_row):
            failures.append({"kind": "direct_row_nonintegral", "d": d})
        direct_rows[d] = [value.numerator for value in direct_row]
        print(f"direct d={d} complete", flush=True)

    recurrence_type_cases = 0
    for d in range(2, args.recurrence_compare_max_d + 1):
        for cycle_type in integer_partitions(d):
            if len(cycle_type) < 2:
                continue
            recurrence_type_cases += 1
            if subset_connected_polynomial(
                cycle_type
            ) != multiset_connected_polynomial(cycle_type):
                failures.append(
                    {"kind": "subset_vs_multiset", "cycle_type": cycle_type}
                )

    frozen_payload = json.loads(args.frozen.read_text())
    frozen_rows = {
        case["d"]: case["raw_integer_masses"]
        for case in frozen_payload["cases"]
    }
    m124_payload = json.loads(args.m124.read_text())
    m124_rows = {
        case["d"]: [
            entry["weight"] for entry in case["defect_projection"]
        ]
        for case in m124_payload["cases"]
    }

    cases = []
    weakest: tuple[Fraction, int, int] | None = None
    for d in range(2, args.max_d + 1):
        case_started = time.time()
        row = defect_row(d)
        diagnostics = sequence_diagnostics(row)
        primitive_row, divisor = primitive(row)
        if d in direct_rows and row != direct_rows[d]:
            failures.append({"kind": "direct_row_mismatch", "d": d})
        if row != frozen_rows.get(d):
            failures.append({"kind": "frozen_row_mismatch", "d": d})
        if d in m124_rows and row != m124_rows[d]:
            failures.append({"kind": "m124_exact_key_row_mismatch", "d": d})
        for r in range(1, len(row) - 1):
            ratio = Fraction(row[r] ** 2, row[r - 1] * row[r + 1])
            candidate = (ratio, d, r)
            if weakest is None or candidate < weakest:
                weakest = candidate
        cases.append(
            {
                "d": d,
                "raw_integer_masses": row,
                "primitive_integer_masses": primitive_row,
                "common_gcd": divisor,
                "diagnostics": diagnostics,
                "elapsed_seconds": time.time() - case_started,
            }
        )
        print(
            f"exact d={d} LC={diagnostics['log_concave']} "
            f"ULC={diagnostics['ultra_log_concave']} "
            f"unimodal={diagnostics['unimodal']}",
            flush=True,
        )

    d4 = next(case for case in cases if case["d"] == 4)
    d4_primitive = d4["primitive_integer_masses"]
    d4_ordinary = d4_primitive[1] ** 2 - d4_primitive[0] * d4_primitive[2]
    d4_ulc = d4_primitive[1] ** 2 - 4 * d4_primitive[0] * d4_primitive[2]
    boundary_checks = {
        "c1_excluded_by_positive_LR_and_L_plus_R_equals_c": True,
        "d2_row": next(case["raw_integer_masses"] for case in cases if case["d"] == 2),
        "d4_primitive": d4_primitive,
        "d4_ordinary_margin": d4_ordinary,
        "d4_ulc_margin": d4_ulc,
    }
    expected_boundary = {
        "d2_row": [1],
        "d4_primitive": [627, 1520, 1113],
        "d4_ordinary_margin": 1612549,
        "d4_ulc_margin": -481004,
    }
    for key, expected in expected_boundary.items():
        if boundary_checks[key] != expected:
            failures.append(
                {"kind": "boundary_or_d4", "field": key, "expected": expected}
            )

    all_lc = all(case["diagnostics"]["log_concave"] for case in cases)
    all_unimodal = all(case["diagnostics"]["unimodal"] for case in cases)
    ulc_false_all_d_ge_4 = all(
        not case["diagnostics"]["ultra_log_concave"]
        for case in cases
        if case["d"] >= 4
    )
    if not all_lc:
        failures.append({"kind": "finite_lc_claim"})
    if not all_unimodal:
        failures.append({"kind": "finite_unimodality_claim"})
    if not ulc_false_all_d_ge_4:
        failures.append({"kind": "finite_ulc_scope_claim"})

    weakest_payload = None
    if weakest is not None:
        ratio, weak_d, weak_r = weakest
        weakest_payload = {
            "d": weak_d,
            "r": weak_r,
            "numerator": str(ratio.numerator),
            "denominator": str(ratio.denominator),
            "float": float(ratio),
        }
        frozen_weakest = frozen_payload["finite_summary"][
            "weakest_ordinary_lc_ratio"
        ]
        if weakest_payload != frozen_weakest:
            failures.append(
                {
                    "kind": "weakest_ratio_mismatch",
                    "observed": weakest_payload,
                    "expected": frozen_weakest,
                }
            )

    payload = {
        "claim_scope": (
            "fresh exact referee audit of frozen M125; finite d<=22 checks "
            "are not a universal no-valley or spectral-gap theorem"
        ),
        "target": "auxiliary rho(kappa)=|C_kappa|/Z_inc and masses M[d,r]",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "parameters": {
            "max_d": args.max_d,
            "direct_max_d": args.direct_max_d,
            "recurrence_compare_max_d": args.recurrence_compare_max_d,
        },
        "independence": (
            "no frozen M125 module imported; literal, indexed-subset, and "
            "fresh multiset implementations compared"
        ),
        "frozen_exact_results_sha256": sha256(args.frozen),
        "m124_exact_key_results_sha256": sha256(args.m124),
        "m124_exact_key_rows_compared": sorted(m124_rows),
        "direct_type_cases": direct_type_cases,
        "direct_partition_pair_tests": direct_partition_pairs,
        "recurrence_type_cases": recurrence_type_cases,
        "boundary_checks": boundary_checks,
        "finite_summary": {
            "all_rows_log_concave": all_lc,
            "all_rows_unimodal": all_unimodal,
            "ulc_false_for_every_d_4_through_max": ulc_false_all_d_ge_4,
            "weakest_ordinary_lc_ratio": weakest_payload,
        },
        "cases": cases,
        "failure_count": len(failures),
        "failures": failures,
        "all_checks_pass": not failures,
        "elapsed_seconds": time.time() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "all_checks_pass": not failures,
                "failure_count": len(failures),
                "elapsed_seconds": payload["elapsed_seconds"],
            },
            sort_keys=True,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
