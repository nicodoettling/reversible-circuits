#!/usr/bin/env python3
"""Single predeclared k=11 guard for M305's combined CBPV candidate.

The script SHA-gates and imports the frozen M297 clean-room arithmetic, then
rebuilds both complete A/B product laws at k=11.  It groups the already
combined physical coefficient omega=P_B-P_A by exact literal lag-response
profiles before taking coefficient total variation.  It never norms a
source, channel, T/S/N kind, phase, seam, or incidence row separately.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import platform
import subprocess
import sys
import time
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


K = 11
M297_TOP_SHA = "a1bfa3684113b84cad5741061fcebb860cc52461ef29f0f02e29752a68dc1792"
M297_SCRIPT_SHA = "9809433b8a978831d105f1de71f56f6f63424fa472756c6e3944b87390161b73"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_m297(repo: Path):
    directory = (
        repo
        / "experiments/20260811-polynomial-mixing-resolution/cycle-83"
        / "mission-M297-bodt-small-owner-tail"
    )
    manifest = directory / "SHA256SUMS"
    script = directory / "bodt_k9_probe.py"
    observed = {"manifest": sha256(manifest), "script": sha256(script)}
    expected = {"manifest": M297_TOP_SHA, "script": M297_SCRIPT_SHA}
    if observed != expected:
        raise AssertionError(("M297 SHA gate failed", expected, observed))
    spec = importlib.util.spec_from_file_location("m297_frozen_probe", script)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module, observed


def add_measure(measure, profile, weight):
    measure[profile] += weight
    if measure[profile] == 0:
        del measure[profile]


def measure_tv(measure):
    return sum((abs(value) for value in measure.values()), Fraction(0))


def measure_mass(measure):
    return sum(measure.values(), Fraction(0))


def fstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def profile_derivative(module, row, lags):
    delta = module.int_derivative(row)
    return tuple(delta[ell] for ell in lags)


def row_l1(row):
    return sum((abs(value) for value in row), Fraction(0))


def run(repo: Path):
    module, dependency_hashes = load_m297(repo)
    k = K
    n = 3 * k
    threshold = (k - 1) // 2
    target_lags = range(2, n - 2)
    h = module.cyc(n, tuple(range(n)))
    laws = {label: module.source_law(k, label) for label in ("A", "B")}
    probability = {label: item[0] for label, item in laws.items()}
    raw_pairs = {label: item[1] for label, item in laws.items()}
    states = {s for law in probability.values() for _, _, s in law}
    omega = {
        s: sum(
            (p for (_, _, t), p in probability["B"].items() if t == s),
            Fraction(0),
        )
        - sum(
            (p for (_, _, t), p in probability["A"].items() if t == s),
            Fraction(0),
        )
        for s in states
    }
    if sum(omega.values(), Fraction(0)) != 0:
        raise AssertionError("combined coefficient is not centered")

    mu_h = defaultdict(lambda: defaultdict(Fraction))
    mu_a = defaultdict(lambda: defaultdict(Fraction))
    mu_c = defaultdict(lambda: defaultdict(Fraction))
    raw_h = defaultdict(Fraction)
    raw_a = defaultdict(Fraction)
    raw_c = defaultdict(Fraction)
    direct_h = defaultdict(lambda: tuple(Fraction(0) for _ in target_lags))
    direct_a = defaultdict(lambda: tuple(Fraction(0) for _ in target_lags))
    direct_c = defaultdict(lambda: tuple(Fraction(0) for _ in target_lags))
    representation_count = 0

    for state in states:
        generic, sizes = module.owner_profile(n, h, state)
        if min(sizes) > threshold:
            continue
        reps = module.positive_representations(state)
        if len(reps) not in (3, 4):
            raise AssertionError("bad positive-composition multiplicity")
        representation_count += len(reps)
        for kind, gaps in reps:
            if tuple(sorted(module.owner_sizes_from_rep(kind, gaps))) != tuple(sorted(sizes)):
                raise AssertionError("representation owner-size mismatch")
        weight = omega[state]
        chis = tuple(tuple(int(value == i) for value in generic) for i in range(3))
        heads = tuple(int(value is None) for value in generic)
        for i, d in enumerate(sizes):
            if d > threshold:
                continue
            h_row = tuple(
                x + y
                for x, y in zip(
                    module.corr01(chis[i], heads),
                    module.corr01(heads, chis[i]),
                )
            )
            h_profile = profile_derivative(module, h_row, target_lags)
            a_profile = profile_derivative(
                module, module.corr01(chis[i], chis[i]), target_lags
            )
            add_measure(mu_h[d], h_profile, weight)
            add_measure(mu_a[d], a_profile, weight)
            raw_h[d] += abs(weight)
            raw_a[d] += abs(weight)
            direct_h[d] = tuple(
                old + weight * value for old, value in zip(direct_h[d], h_profile)
            )
            direct_a[d] = tuple(
                old + weight * value for old, value in zip(direct_a[d], a_profile)
            )
        for i, d in enumerate(sizes):
            if d > threshold:
                continue
            for j, e in enumerate(sizes):
                if i == j or e > threshold:
                    continue
                profile = profile_derivative(
                    module, module.corr01(chis[i], chis[j]), target_lags
                )
                add_measure(mu_c[(d, e)], profile, weight)
                raw_c[(d, e)] += abs(weight)
                direct_c[(d, e)] = tuple(
                    old + weight * value
                    for old, value in zip(direct_c[(d, e)], profile)
                )

    def bmass(d):
        return math.exp(-d) * float(module.tau(d))

    h_rows = {}
    a_rows = {}
    c_rows = {}
    for d in range(1, threshold + 1):
        tv_h = measure_tv(mu_h[d])
        tv_a = measure_tv(mu_a[d])
        norm_h = row_l1(direct_h[d])
        norm_a = row_l1(direct_a[d])
        h_rows[str(d)] = {
            "profile_count": len(mu_h[d]),
            "coefficient_mass_exact": fstr(measure_mass(mu_h[d])),
            "coefficient_tv_exact": fstr(tv_h),
            "ungrouped_occurrence_tv_exact": fstr(raw_h[d]),
            "normalized_cbpv_k_over_d_b": k * float(tv_h) / (d * bmass(d)),
            "row_l1_exact": fstr(norm_h),
            "normalized_socl_k_over_d_b": k * float(norm_h) / (d * bmass(d)),
        }
        a_rows[str(d)] = {
            "profile_count": len(mu_a[d]),
            "coefficient_mass_exact": fstr(measure_mass(mu_a[d])),
            "coefficient_tv_exact": fstr(tv_a),
            "ungrouped_occurrence_tv_exact": fstr(raw_a[d]),
            "normalized_cbpv_k_over_d_b": k * float(tv_a) / (d * bmass(d)),
            "row_l1_exact": fstr(norm_a),
            "normalized_socl_k_over_d2_b": k * float(norm_a) / (d * d * bmass(d)),
        }
    for d in range(1, threshold + 1):
        for e in range(1, threshold + 1):
            tv = measure_tv(mu_c[(d, e)])
            norm = row_l1(direct_c[(d, e)])
            c_rows[f"{d},{e}"] = {
                "profile_count": len(mu_c[(d, e)]),
                "coefficient_mass_exact": fstr(measure_mass(mu_c[(d, e)])),
                "coefficient_tv_exact": fstr(tv),
                "ungrouped_occurrence_tv_exact": fstr(raw_c[(d, e)]),
                "normalized_cbpv_k_over_max_bdb_e": (
                    k * float(tv) / (max(d, e) * bmass(d) * bmass(e))
                    if d > 1 and e > 1
                    else 0.0
                ),
                "row_l1_exact": fstr(norm),
                "normalized_socl_k_over_de_bdb_e": (
                    k * float(norm) / (d * e * bmass(d) * bmass(e))
                    if d > 1 and e > 1
                    else 0.0
                ),
            }

    nontrivial_h = [row["normalized_cbpv_k_over_d_b"] for d, row in h_rows.items() if int(d) >= 2]
    nontrivial_a = [row["normalized_cbpv_k_over_d_b"] for d, row in a_rows.items() if int(d) >= 4]
    nontrivial_c = [
        row["normalized_cbpv_k_over_max_bdb_e"]
        for key, row in c_rows.items()
        if all(int(value) >= 2 for value in key.split(","))
    ]
    return {
        "status": "exact k=11 falsification/calibration only",
        "candidate": "CBPV fixed in plan.md before computation",
        "scope": "complete combined omega grouped by exact literal response profile",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "k": k,
        "n": n,
        "threshold": threshold,
        "target_lags": [2, n - 3],
        "dependency_hashes": dependency_hashes,
        "raw_ordered_pairs": raw_pairs,
        "state_count": len(states),
        "positive_composition_representation_count": representation_count,
        "combined_omega_total": "0",
        "all_source_type_rows_combined_before_profile_norm": True,
        "formal_u1": 0,
        "H_rows": h_rows,
        "A_rows": a_rows,
        "C_off_rows": c_rows,
        "max_normalized_cbpv": {
            "H_d_ge_2": max(nontrivial_h),
            "A_d_ge_4": max(nontrivial_a),
            "C_d_e_ge_2": max(nontrivial_c),
        },
        "inference": {
            "all_rank_CBPV": False,
            "SOCL": False,
            "BODT_DOR_or_downstream": False,
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("cbpv_k11_results.json"))
    args = parser.parse_args()
    start = time.perf_counter()
    repo = Path(__file__).resolve().parents[4]
    payload = run(repo)
    payload.update(
        {
            "seed": None,
            "python": platform.python_version(),
            "dependencies": {},
            "repository_commit": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=repo, text=True
            ).strip(),
            "command": "python3 -B cbpv_k11_guard.py --output cbpv_k11_results.json",
            "elapsed_seconds": time.perf_counter() - start,
        }
    )
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "max_normalized_cbpv": payload["max_normalized_cbpv"],
                "elapsed_seconds": payload["elapsed_seconds"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
