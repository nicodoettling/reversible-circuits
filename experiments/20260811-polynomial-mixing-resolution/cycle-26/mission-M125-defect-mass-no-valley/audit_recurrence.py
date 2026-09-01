#!/usr/bin/env python3
"""Independent finite audit of the M125 incidence-species recurrence.

The direct checker enumerates pairs of set partitions of indexed cycle atoms;
it does not use the subset connected-component extraction under audit.  It
also compares complete defect rows with the frozen M124 exact key enumerator.
All comparisons are exact and deterministic.
"""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
import time
from fractions import Fraction
from pathlib import Path

import defect_species as core


Partition = tuple[tuple[int, ...], ...]


def set_partitions(n: int) -> list[Partition]:
    partitions: list[Partition] = [()]
    for atom in range(n):
        new: list[Partition] = []
        for partition in partitions:
            for index in range(len(partition)):
                blocks = list(partition)
                blocks[index] = blocks[index] + (atom,)
                new.append(tuple(blocks))
            new.append(partition + ((atom,),))
        partitions = new
    return partitions


def partition_weight(
    atom_sizes: tuple[int, ...], partition: Partition
) -> Fraction:
    value = Fraction(1)
    for block in partition:
        label_size = sum(atom_sizes[index] for index in block)
        value *= Fraction(label_size, 1) ** (len(block) - 3)
    return value


def join_is_connected(n: int, left: Partition, right: Partition) -> bool:
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> None:
        x, y = find(x), find(y)
        if x != y:
            parent[y] = x

    for partition in (left, right):
        for block in partition:
            for atom in block[1:]:
                union(block[0], atom)
    return len({find(atom) for atom in range(n)}) == 1


def direct_connected_polynomial(
    atom_sizes: tuple[int, ...]
) -> list[list[Fraction]]:
    c = len(atom_sizes)
    result = core.poly_zero(c + 1, c + 1)
    partitions = set_partitions(c)
    weights = {
        partition: partition_weight(atom_sizes, partition)
        for partition in partitions
    }
    for left in partitions:
        for right in partitions:
            if join_is_connected(c, left, right):
                result[len(left)][len(right)] += weights[left] * weights[right]
    return result


def frozen_m124_rows(path: Path) -> dict[int, list[int]]:
    payload = json.loads(path.read_text())
    rows: dict[int, list[int]] = {}
    for case in payload["cases"]:
        rows[case["d"]] = [entry["weight"] for entry in case["defect_projection"]]
    return rows


def git_commit() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--frozen-m124",
        type=Path,
        default=Path(
            "experiments/20260811-polynomial-mixing-resolution/cycle-25/"
            "mission-M124-m120-fresh-referee/results.json"
        ),
    )
    args = parser.parse_args()
    started = time.time()

    failures: list[dict] = []
    direct_cases = 0
    direct_pair_tests = 0
    symmetry_tests = 0
    for d in range(2, 6):
        for cycle_type in core.integer_partitions(d):
            if len(cycle_type) < 2:
                continue
            direct = direct_connected_polynomial(cycle_type)
            recurrent = core.connected_incidence_polynomial(cycle_type)
            subset_recurrent = core.connected_incidence_polynomial_subset(cycle_type)
            direct_cases += 1
            bell = len(set_partitions(len(cycle_type)))
            direct_pair_tests += bell * bell
            if direct != recurrent:
                failures.append(
                    {
                        "kind": "direct_connected_polynomial",
                        "cycle_type": list(cycle_type),
                    }
                )
            if subset_recurrent != recurrent:
                failures.append(
                    {
                        "kind": "subset_multiset_recurrence",
                        "cycle_type": list(cycle_type),
                    }
                )
            for left in range(len(cycle_type) + 1):
                for right in range(len(cycle_type) + 1):
                    symmetry_tests += 1
                    if recurrent[left][right] != recurrent[right][left]:
                        failures.append(
                            {
                                "kind": "colour_symmetry",
                                "cycle_type": list(cycle_type),
                                "left": left,
                                "right": right,
                            }
                        )

    frozen_rows = frozen_m124_rows(args.frozen_m124)
    frozen_checks = []
    for d in range(2, 6):
        row, records = core.defect_row(d)
        expected = frozen_rows[d]
        ok = row == expected
        frozen_checks.append({"d": d, "observed": row, "expected": expected, "ok": ok})
        if not ok:
            failures.append({"kind": "frozen_row", "d": d})
        if any(len(record["cycle_type"]) < 2 for record in records):
            failures.append({"kind": "impossible_one_cycle_record", "d": d})

    stress_expected = {
        6: [9139662, 33979680, 63794575, 62828640, 25565795],
        7: [38271780, 151229400, 340051475, 470006334, 366720025, 123380706],
    }
    stress_checks = []
    for d, expected in stress_expected.items():
        row, _ = core.defect_row(d)
        observed, divisor = core.primitive(row)
        ok = observed == expected
        stress_checks.append(
            {"d": d, "observed": observed, "expected": expected, "gcd": divisor, "ok": ok}
        )
        if not ok:
            failures.append({"kind": "stress_row", "d": d})

    d2_row, _ = core.defect_row(2)
    d4_row, _ = core.defect_row(4)
    d4_primitive, _ = core.primitive(d4_row)
    d4_checks = core.sequence_checks(d4_primitive)
    boundary_checks = {
        "d2_one_state": d2_row == [1],
        "d4_primitive": d4_primitive,
        "d4_ordinary_log_concavity_margin": d4_checks["log_concavity_margins"][0],
        "d4_ulc_cleared_margin": d4_checks["ulc_cleared_margins"][0],
        "d4_ulc_refuted": not d4_checks["ultra_log_concave"],
    }
    if not all(
        (
            boundary_checks["d2_one_state"],
            boundary_checks["d4_primitive"] == [627, 1520, 1113],
            boundary_checks["d4_ordinary_log_concavity_margin"] == 1612549,
            boundary_checks["d4_ulc_cleared_margin"] == -481004,
            boundary_checks["d4_ulc_refuted"],
        )
    ):
        failures.append({"kind": "boundary_or_ulc"})

    payload = {
        "claim_scope": (
            "exact finite audit of the recurrence and boundary handling; not a "
            "universal no-valley or mixing proof"
        ),
        "method": (
            "direct pairs of set partitions for all cycle types d<=5, frozen "
            "M124 row comparison, and primitive d=6,7 stress rows"
        ),
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "direct_cycle_type_cases": direct_cases,
        "direct_partition_pair_tests": direct_pair_tests,
        "colour_symmetry_tests": symmetry_tests,
        "frozen_checks": frozen_checks,
        "stress_checks": stress_checks,
        "boundary_checks": boundary_checks,
        "failure_count": len(failures),
        "failures": failures,
        "all_checks_pass": not failures,
        "elapsed_seconds": time.time() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"all_checks_pass": not failures, "failure_count": len(failures)}))


if __name__ == "__main__":
    main()
