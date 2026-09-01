#!/usr/bin/env python3
"""Targeted exact scan of M125's H[d,c] coefficients.

This is a falsification tool, not a proof.  It loads the frozen accepted M125
coefficient core and evaluates only requested cycle counts, avoiding the
irrelevant low-cycle types that dominate the cost of a complete large-d row.
All arithmetic is exact and deterministic.
"""

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


def partitions_fixed(
    total: int, parts: int, minimum: int = 1
):
    """Yield increasing integer partitions of total having exactly parts."""
    if parts == 0:
        if total == 0:
            yield ()
        return
    if total < parts * minimum:
        return
    maximum = total // parts
    for first in range(minimum, maximum + 1):
        for rest in partitions_fixed(total - first, parts - 1, first):
            yield (first,) + rest


def h_coefficient(core, d: int, cycles: int) -> tuple[int, int]:
    """Return H[d,cycles] and the number of evaluated cycle types."""
    if not 2 <= cycles <= d:
        return 0, 0
    total = Fraction(0)
    count = 0
    for cycle_type in partitions_fixed(d, cycles):
        count += 1
        incidence = core.connected_incidence_polynomial(cycle_type)
        multiplier = Fraction(core.cycle_type_permutation_count(d, cycle_type), 1)
        for size in cycle_type:
            multiplier *= core.hurwitz_atom_weight(size)
        for left in range(1, cycles):
            right = cycles - left
            weight = incidence[left][right]
            if weight:
                cut = d + cycles - 2 * left
                total += (
                    multiplier
                    * math.factorial(cut)
                    * math.factorial(2 * d - cut)
                    * weight
                )
    if total.denominator != 1:
        raise AssertionError((d, cycles, total))
    return total.numerator, count


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
    parser.add_argument(
        "--case",
        action="append",
        required=True,
        help="d:r, where r is the center defect in the tested LC triple",
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    core = load_m125_core()
    started = time.time()
    records = []
    for item in args.case:
        d_text, r_text = item.split(":", 1)
        d, r = int(d_text), int(r_text)
        if not (d >= 4 and 1 <= r <= d - 3):
            raise SystemExit(f"invalid LC case {item}")
        case_started = time.time()
        values = {}
        type_counts = {}
        for defect in (r - 1, r, r + 1):
            cycles = d - defect
            value, count = h_coefficient(core, d, cycles)
            values[str(defect)] = value
            type_counts[str(defect)] = count
        center = values[str(r)]
        left = values[str(r - 1)]
        right = values[str(r + 1)]
        ratio = Fraction(center * center, left * right)
        records.append(
            {
                "d": d,
                "center_defect": r,
                "masses_by_defect": values,
                "cycle_type_counts_by_defect": type_counts,
                "lc_margin": center * center - left * right,
                "lc_ratio_numerator": ratio.numerator,
                "lc_ratio_denominator": ratio.denominator,
                "lc_ratio_float": float(ratio),
                "elapsed_seconds": time.time() - case_started,
            }
        )
        print(
            f"d={d} r={r} ratio={float(ratio):.12g} "
            f"margin_sign={(center * center > left * right) - (center * center < left * right)}",
            flush=True,
        )
    payload = {
        "claim_scope": "exact finite falsification only; no asymptotic inference",
        "target": "H[d,d-r]=M[d,r] for the accepted M125/M129 recurrence",
        "m125_core": str(M125_CORE.relative_to(REPOSITORY)),
        "m125_core_sha256": sha256(M125_CORE),
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "arguments": {"case": args.case, "output": str(args.output)},
        "records": records,
        "elapsed_seconds": time.time() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(f"wrote {args.output} sha256={sha256(args.output)}", flush=True)


if __name__ == "__main__":
    main()
