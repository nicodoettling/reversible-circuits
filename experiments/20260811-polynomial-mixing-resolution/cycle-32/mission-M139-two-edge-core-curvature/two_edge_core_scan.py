#!/usr/bin/env python3
"""Exact marked-pair recurrence for the two-parallel-edge core profile.

For fixed indexed cycle atoms, a connected unicyclic bipartite incidence graph
has core length two iff its two core edge-atoms form the unique unordered pair
that lies in a common left block and a common right block.  Marking that pair
turns the usual connected-component extraction into a recurrence whose root
component must contain both marks.  Equal-sized unmarked atoms are aggregated
with exact binomial multiplicities.

The recurrence is computational.  Its finite signs are falsification data,
not a proof of universal log-concavity.
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


Poly = tuple[Fraction, ...]
Matrix = tuple[tuple[Fraction, ...], ...]


def integer_partitions(n: int, minimum: int = 1):
    if n == 0:
        yield ()
        return
    for first in range(minimum, n + 1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def cycle_type_permutation_count(d: int, cycle_type: tuple[int, ...]) -> int:
    multiplicities: dict[int, int] = {}
    for size in cycle_type:
        multiplicities[size] = multiplicities.get(size, 0) + 1
    denominator = math.prod(
        size**multiplicity * math.factorial(multiplicity)
        for size, multiplicity in multiplicities.items()
    )
    return math.factorial(d) // denominator


def hurwitz_atom_weight(size: int) -> Fraction:
    return Fraction(size**size, math.factorial(size - 1)) ** 2


def outer_product(values: Poly) -> Matrix:
    return tuple(tuple(x * y for y in values) for x in values)


def subtract_convolution(
    target: list[list[Fraction]],
    first: Matrix,
    second: Matrix,
    multiplicity: int,
) -> None:
    for left, row in enumerate(first):
        for right, value in enumerate(row):
            if not value:
                continue
            for left2, row2 in enumerate(second):
                if left + left2 >= len(target):
                    break
                for right2, value2 in enumerate(row2):
                    if right + right2 >= len(target[left + left2]):
                        break
                    if value2:
                        target[left + left2][right + right2] -= (
                            multiplicity * value * value2
                        )


class MarkedPairRecurrence:
    """Multiset recurrence with two fixed distinguished boundary atoms."""

    def __init__(self, distinct: tuple[int, ...]):
        self.distinct = distinct

    @staticmethod
    def cardinality(counts: tuple[int, ...]) -> int:
        return sum(counts)

    @functools.cache
    def one_colour(self, counts: tuple[int, ...]) -> Poly:
        """Ordinary weighted partition polynomial of unmarked atoms."""
        total = self.cardinality(counts)
        if total == 0:
            return (Fraction(1),)
        root_index = next(index for index, count in enumerate(counts) if count)
        available = list(counts)
        available[root_index] -= 1
        values = [Fraction(0) for _ in range(total + 1)]
        for extras in itertools.product(
            *(range(count + 1) for count in available)
        ):
            block = list(extras)
            block[root_index] += 1
            block_tuple = tuple(block)
            block_count = self.cardinality(block_tuple)
            label_size = sum(
                size * count for size, count in zip(self.distinct, block_tuple)
            )
            multiplicity = math.prod(
                math.comb(available[index], extras[index])
                for index in range(len(self.distinct))
            )
            weight = Fraction(label_size, 1) ** (block_count - 3)
            remainder = tuple(
                counts[index] - block_tuple[index]
                for index in range(len(self.distinct))
            )
            for blocks, value in enumerate(self.one_colour(remainder)):
                values[blocks + 1] += multiplicity * weight * value
        return tuple(values)

    @functools.cache
    def arbitrary(self, counts: tuple[int, ...]) -> Matrix:
        return outer_product(self.one_colour(counts))

    @functools.cache
    def marked_one_colour(
        self, mark_a: int, mark_b: int, counts: tuple[int, ...]
    ) -> Poly:
        """Partitions in which the two fixed marks lie in one block."""
        total = self.cardinality(counts)
        values = [Fraction(0) for _ in range(total + 2)]
        for extras in itertools.product(*(range(count + 1) for count in counts)):
            extras_count = self.cardinality(extras)
            label_size = mark_a + mark_b + sum(
                size * count for size, count in zip(self.distinct, extras)
            )
            multiplicity = math.prod(
                math.comb(counts[index], extras[index])
                for index in range(len(self.distinct))
            )
            # The common block has 2+extras_count incident original atoms.
            weight = Fraction(label_size, 1) ** (extras_count - 1)
            remainder = tuple(
                counts[index] - extras[index]
                for index in range(len(self.distinct))
            )
            for blocks, value in enumerate(self.one_colour(remainder)):
                values[blocks + 1] += multiplicity * weight * value
        return tuple(values)

    @functools.cache
    def marked_arbitrary(
        self, mark_a: int, mark_b: int, counts: tuple[int, ...]
    ) -> Matrix:
        return outer_product(self.marked_one_colour(mark_a, mark_b, counts))

    @functools.cache
    def marked_connected(
        self, mark_a: int, mark_b: int, counts: tuple[int, ...]
    ) -> Matrix:
        """Connected pairs with both marks co-blocked in both colours."""
        matrix = [
            list(row) for row in self.marked_arbitrary(mark_a, mark_b, counts)
        ]
        for component_extra in itertools.product(
            *(range(count + 1) for count in counts)
        ):
            if component_extra == counts:
                continue
            multiplicity = math.prod(
                math.comb(counts[index], component_extra[index])
                for index in range(len(self.distinct))
            )
            remainder = tuple(
                counts[index] - component_extra[index]
                for index in range(len(self.distinct))
            )
            subtract_convolution(
                matrix,
                self.marked_connected(mark_a, mark_b, component_extra),
                self.arbitrary(remainder),
                multiplicity,
            )
        # The two marks are forced into one block, so at most
        # `len(counts)+1` blocks occur and the coefficient vector has
        # `len(counts)+2` entries including degree zero.
        assert len(matrix) == self.cardinality(counts) + 2
        return tuple(tuple(row) for row in matrix)


def two_edge_incidence(cycle_type: tuple[int, ...]) -> Matrix:
    """Sum fixed-pair connected polynomials over all unordered atom pairs."""
    distinct = tuple(sorted(set(cycle_type)))
    initial = tuple(cycle_type.count(size) for size in distinct)
    recurrence = MarkedPairRecurrence(distinct)
    total_atoms = len(cycle_type)
    result = [
        [Fraction(0) for _ in range(total_atoms + 1)]
        for _ in range(total_atoms + 1)
    ]
    for first_index, first_size in enumerate(distinct):
        for second_index in range(first_index, len(distinct)):
            second_size = distinct[second_index]
            if first_index == second_index:
                pair_count = math.comb(initial[first_index], 2)
                if not pair_count:
                    continue
            else:
                pair_count = initial[first_index] * initial[second_index]
            unmarked = list(initial)
            unmarked[first_index] -= 1
            unmarked[second_index] -= 1
            marked = recurrence.marked_connected(
                first_size, second_size, tuple(unmarked)
            )
            for left, row in enumerate(marked):
                for right, value in enumerate(row):
                    result[left][right] += pair_count * value
    return tuple(tuple(row) for row in result)


def h2_row(d: int) -> tuple[dict[int, int], list[dict]]:
    masses: dict[int, Fraction] = {}
    type_records = []
    for cycle_type in integer_partitions(d):
        cycles = len(cycle_type)
        if cycles < 2:
            continue
        incidence = two_edge_incidence(cycle_type)
        multiplier = Fraction(cycle_type_permutation_count(d, cycle_type), 1)
        for size in cycle_type:
            multiplier *= hurwitz_atom_weight(size)
        subtotal = Fraction(0)
        for left in range(1, cycles):
            right = cycles - left
            weight = incidence[left][right]
            if weight:
                cut = d + cycles - 2 * left
                subtotal += (
                    multiplier
                    * math.factorial(cut)
                    * math.factorial(2 * d - cut)
                    * weight
                )
        masses[cycles] = masses.get(cycles, Fraction(0)) + subtotal
        type_records.append(
            {
                "cycle_type": list(cycle_type),
                "cycles": cycles,
                "subtotal": str(subtotal),
            }
        )
    if any(value.denominator != 1 for value in masses.values()):
        raise AssertionError((d, masses))
    return {cycles: value.numerator for cycles, value in masses.items()}, type_records


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception:
        return "unavailable"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-d", type=int, default=12)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--include-types", action="store_true")
    args = parser.parse_args()
    started = time.time()
    records = []
    first_failure = None
    weakest_ratio = None
    for d in range(2, args.max_d + 1):
        case_started = time.time()
        masses, type_records = h2_row(d)
        checks = []
        for cycles in range(3, d):
            margin = masses[cycles] ** 2 - masses[cycles - 1] * masses[cycles + 1]
            ratio = Fraction(
                masses[cycles] ** 2,
                masses[cycles - 1] * masses[cycles + 1],
            )
            check = {
                "cycles": cycles,
                "margin": str(margin),
                "ratio_numerator": str(ratio.numerator),
                "ratio_denominator": str(ratio.denominator),
                "ratio_decimal": float(ratio),
                "holds": margin >= 0,
            }
            checks.append(check)
            candidate = {"d": d, **check}
            if margin < 0 and first_failure is None:
                first_failure = candidate
            if weakest_ratio is None or ratio < Fraction(
                int(weakest_ratio["ratio_numerator"]),
                int(weakest_ratio["ratio_denominator"]),
            ):
                weakest_ratio = candidate
        record = {
            "d": d,
            "masses_by_cycles": {str(k): str(v) for k, v in sorted(masses.items())},
            "log_concavity_checks": checks,
            "elapsed_seconds": time.time() - case_started,
        }
        if args.include_types:
            record["type_contributions"] = type_records
        records.append(record)
        print(
            f"d={d} elapsed={record['elapsed_seconds']:.3f}s "
            f"failures={sum(not check['holds'] for check in checks)}",
            flush=True,
        )
    payload = {
        "claim_scope": (
            "exact finite falsification of two-edge-core log-concavity; "
            "finite nonnegative signs do not prove the universal theorem"
        ),
        "target": "H_2[d,c] for the M133 two-parallel-edge incidence core",
        "method": (
            "marked atom pair co-blocked in both colours plus exact rooted "
            "connected-component recurrence aggregated by unmarked sizes"
        ),
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "arguments": {
            "max_d": args.max_d,
            "output": str(args.output),
            "include_types": args.include_types,
        },
        "first_log_concavity_failure": first_failure,
        "weakest_ratio": weakest_ratio,
        "records": records,
        "elapsed_seconds": time.time() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        f"first_failure={first_failure} weakest_ratio={weakest_ratio} "
        f"elapsed={payload['elapsed_seconds']:.3f}s",
        flush=True,
    )
    print(f"wrote {args.output} sha256={sha256(args.output)}", flush=True)


if __name__ == "__main__":
    main()
