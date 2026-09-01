#!/usr/bin/env python3
"""Finite exact test of log-concavity after unique-cycle-core separation."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import platform
import subprocess
import time
from fractions import Fraction
from pathlib import Path

import positive_unicycle_audit as positive


REPOSITORY = Path(__file__).resolve().parents[4]
M125_CORE = (
    REPOSITORY
    / "experiments/20260811-polynomial-mixing-resolution/cycle-26"
    / "mission-M125-defect-mass-no-valley/defect_species.py"
)


def load_m125_core():
    spec = importlib.util.spec_from_file_location("m125_defect_species", M125_CORE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {M125_CORE}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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
    parser.add_argument("--max-d", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    core = load_m125_core()
    started = time.time()
    records = []
    first_core_failure = None
    first_polarized_failure = None
    reference_mismatches = []
    for d in range(2, args.max_d + 1):
        by_core: dict[int, dict[int, Fraction]] = {}
        total: dict[int, Fraction] = {}
        for cycle_type in core.integer_partitions(d):
            cycles = len(cycle_type)
            if cycles < 2:
                continue
            multiplier = Fraction(core.cycle_type_permutation_count(d, cycle_type), 1)
            for size in cycle_type:
                multiplier *= core.hurwitz_atom_weight(size)
            incidence = positive.positive_unicycle_by_core(cycle_type)
            for core_length, polynomial in incidence.items():
                subtotal = Fraction(0)
                for left in range(1, cycles):
                    right = cycles - left
                    weight = polynomial.get((left, right), Fraction(0))
                    if weight:
                        cut = d + cycles - 2 * left
                        subtotal += (
                            multiplier
                            * math.factorial(cut)
                            * math.factorial(2 * d - cut)
                            * weight
                        )
                by_core.setdefault(core_length, {})[cycles] = (
                    by_core.setdefault(core_length, {}).get(cycles, Fraction(0))
                    + subtotal
                )
                total[cycles] = total.get(cycles, Fraction(0)) + subtotal
        core_checks = []
        for core_length, sequence in sorted(by_core.items()):
            for cycles in range(core_length + 1, d):
                if not all(value in sequence for value in (cycles - 1, cycles, cycles + 1)):
                    continue
                margin = sequence[cycles] ** 2 - sequence[cycles - 1] * sequence[cycles + 1]
                entry = {
                    "core_length": core_length,
                    "cycles": cycles,
                    "margin": str(margin),
                    "holds": margin >= 0,
                }
                core_checks.append(entry)
                if margin < 0 and first_core_failure is None:
                    first_core_failure = {"d": d, **entry}
        total_checks = []
        for cycles in range(3, d):
            margin = total[cycles] ** 2 - total[cycles - 1] * total[cycles + 1]
            total_checks.append(
                {"cycles": cycles, "margin": str(margin), "holds": margin >= 0}
            )
        polarized_checks = []
        core_lengths = sorted(by_core)
        for cycles in range(3, d):
            for first_index, first_core in enumerate(core_lengths):
                for second_core in core_lengths[first_index:]:
                    first = by_core[first_core]
                    second = by_core[second_core]
                    margin = (
                        2
                        * first.get(cycles, Fraction(0))
                        * second.get(cycles, Fraction(0))
                        - first.get(cycles - 1, Fraction(0))
                        * second.get(cycles + 1, Fraction(0))
                        - second.get(cycles - 1, Fraction(0))
                        * first.get(cycles + 1, Fraction(0))
                    )
                    entry = {
                        "cycles": cycles,
                        "first_core": first_core,
                        "second_core": second_core,
                        "margin": str(margin),
                        "holds": margin >= 0,
                    }
                    polarized_checks.append(entry)
                    if margin < 0 and first_polarized_failure is None:
                        first_polarized_failure = {"d": d, **entry}
        reference_row, _ = core.defect_row(d)
        reference_by_cycles = {
            d - defect: Fraction(value)
            for defect, value in enumerate(reference_row)
        }
        reference_match = total == reference_by_cycles
        if not reference_match:
            reference_mismatches.append(
                {
                    "d": d,
                    "positive": {str(k): str(v) for k, v in sorted(total.items())},
                    "reference": {
                        str(k): str(v) for k, v in sorted(reference_by_cycles.items())
                    },
                }
            )
        records.append(
            {
                "d": d,
                "masses_by_cycles": {str(k): str(v) for k, v in sorted(total.items())},
                "masses_by_core_and_cycles": {
                    str(core_length): {
                        str(cycles): str(value)
                        for cycles, value in sorted(sequence.items())
                    }
                    for core_length, sequence in sorted(by_core.items())
                },
                "total_lc_checks": total_checks,
                "core_lc_checks": core_checks,
                "polarized_core_checks": polarized_checks,
                "matches_m125_total_row": reference_match,
            }
        )
        print(
            f"d={d} core_lc_failures={sum(not item['holds'] for item in core_checks)}",
            flush=True,
        )
    payload = {
        "claim_scope": (
            "finite exact falsification of termwise core-length log-concavity; "
            "finite total signs do not prove the universal H inequality"
        ),
        "target": "H[d,c] separated by unique bipartite incidence-core length",
        "m125_core": str(M125_CORE.relative_to(REPOSITORY)),
        "m125_core_sha256": sha256(M125_CORE),
        "positive_core_script_sha256": sha256(Path(positive.__file__)),
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "arguments": {"max_d": args.max_d, "output": str(args.output)},
        "first_core_log_concavity_failure": first_core_failure,
        "first_polarized_core_failure": first_polarized_failure,
        "reference_mismatch_count": len(reference_mismatches),
        "reference_mismatches": reference_mismatches,
        "records": records,
        "elapsed_seconds": time.time() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        f"first_core_failure={first_core_failure} elapsed={payload['elapsed_seconds']:.3f}s",
        flush=True,
    )
    print(f"wrote {args.output} sha256={sha256(args.output)}", flush=True)


if __name__ == "__main__":
    main()
