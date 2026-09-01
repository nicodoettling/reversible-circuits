#!/usr/bin/env python3
"""Exact/finite audit of the balanced-family posterior-cancellation identity.

This is a falsifier for the analytic formulas in ``posterior_identity.md``.
It is not evidence for an asymptotic rate.  Exact arithmetic is intended only
for the smallest family member; larger runs may use floating arithmetic.

Convention: ``(pq)(x)=p(q(x))`` and tuple factors multiply left-to-right.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
M83_PATH = (
    ROOT
    / "experiments/20260811-polynomial-mixing-resolution/cycle-17/"
      "mission-M83-endpoint-sharing-influence/influence_diagnostic.py"
)
M73_PATH = (
    ROOT
    / "experiments/20260811-polynomial-mixing-resolution/cycle-15/"
      "mission-M73-cyclic-orbit-incidence-gap/h0_coordinate_correlation.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M83 = load_module("m83_influence", M83_PATH)
M73 = load_module("m73_h0", M73_PATH)


def oriented_cycle(n: int, entries: tuple[int, ...]):
    out = list(range(n))
    for a, b in zip(entries, entries[1:] + entries[:1]):
        out[a] = b
    return tuple(out)


def scalar_string(value: Any) -> str | float:
    if isinstance(value, Fraction):
        return str(value.numerator) if value.denominator == 1 else str(value)
    return float(value)


def sum_values(values, exact: bool):
    return sum(values, Fraction(0)) if exact else float(np.sum(values))


def abs_sum(values, exact: bool):
    return (
        sum((abs(value) for value in values), Fraction(0))
        if exact
        else float(np.sum(np.abs(values)))
    )


def matvec(kernel, vector, exact: bool):
    if not exact:
        return kernel @ vector
    return [
        sum((kernel[i][j] * vector[j] for j in range(len(vector))), Fraction(0))
        for i in range(len(vector))
    ]


def analyze(n: int, exact: bool) -> dict[str, Any]:
    if n < 9 or n % 6 != 3:
        raise ValueError("balanced family requires n=3 mod 6 and n>=9")
    k = n // 3
    h, orbits, kernel, squared, pi, _ = M83.build(n, exact)
    hi = M83.inv(h)

    source_a = oriented_cycle(n, (0, k, 2 * k))
    source_b = M83.mul(
        M83.edge_perm(n, 0, 1), M83.edge_perm(n, k, 2 * k)
    )
    ai = next(index for index, orbit in enumerate(orbits) if source_a in orbit)
    bi = next(index for index, orbit in enumerate(orbits) if source_b in orbit)
    q = len(orbits)

    if exact:
        eta = [kernel[bi][s] - kernel[ai][s] for s in range(q)]
        delta = [squared[bi][t] - squared[ai][t] for t in range(q)]
        posterior = [eta[s] / pi[s] for s in range(q)]
        posterior_db = [
            kernel[s][bi] / pi[bi] - kernel[s][ai] / pi[ai]
            for s in range(q)
        ]
    else:
        eta = kernel[bi] - kernel[ai]
        delta = squared[bi] - squared[ai]
        posterior = eta / pi
        posterior_db = kernel[:, bi] / pi[bi] - kernel[:, ai] / pi[ai]

    if exact:
        assert posterior == posterior_db
    else:
        if not np.allclose(posterior, posterior_db, rtol=2e-10, atol=2e-10):
            raise AssertionError("detailed-balance posterior identity failed")

    a_count = M83.count_minimal(M83.mul(M83.inv(source_a), h), n - 3)
    b_count = M83.count_minimal(M83.mul(M83.inv(source_b), h), n - 3)
    phase_posterior = []
    phase_l1 = []
    for orbit in orbits:
        s = orbit[0]
        s_count = M83.count_minimal(M83.mul(M83.inv(s), h), n - 3)
        a_phase = source_a
        b_phase = source_b
        terms = []
        for _ in range(n):
            sb = M83.count_minimal(
                M83.mul(M83.inv(M83.mul(s, b_phase)), h), n - 5
            )
            sa = M83.count_minimal(
                M83.mul(M83.inv(M83.mul(s, a_phase)), h), n - 5
            )
            if exact:
                term = Fraction(sb, b_count) - Fraction(sa, a_count)
            else:
                term = sb / b_count - sa / a_count
            terms.append(term)
            a_phase = M83.theta(a_phase, h, hi)
            b_phase = M83.theta(b_phase, h, hi)
        total = sum_values(terms, exact)
        scale = Fraction(n ** (n - 3), s_count) if exact else n ** (n - 3) / s_count
        phase_posterior.append(scale * total)
        phase_l1.append(scale * abs_sum(terms, exact))

    if exact:
        assert phase_posterior == posterior
    else:
        if not np.allclose(phase_posterior, posterior, rtol=2e-9, atol=2e-9):
            raise AssertionError("phase/orbit posterior identity failed")

    smoothed = matvec(kernel, posterior, exact)
    reconstructed = [pi[t] * smoothed[t] for t in range(q)]
    if exact:
        assert reconstructed == delta
    else:
        if not np.allclose(reconstructed, delta, rtol=2e-9, atol=2e-12):
            raise AssertionError("posterior smoothing identity failed")

    tv_direct = abs_sum(delta, exact) / 2
    tv_posterior = (
        sum((pi[t] * abs(smoothed[t]) for t in range(q)), Fraction(0)) / 2
        if exact
        else 0.5 * float(np.sum(pi * np.abs(smoothed)))
    )
    if exact:
        assert tv_direct == tv_posterior
    elif not np.isclose(tv_direct, tv_posterior, rtol=2e-10, atol=2e-12):
        raise AssertionError("stationary L1 identity failed")

    if exact:
        score_l2 = sum((pi[s] * posterior[s] ** 2 for s in range(q)), Fraction(0))
        smoothed_l2 = sum((pi[t] * smoothed[t] ** 2 for t in range(q)), Fraction(0))
    else:
        score_l2 = float(np.dot(pi, posterior ** 2))
        smoothed_l2 = float(np.dot(pi, smoothed ** 2))

    grouped: dict[tuple[str, str], dict[str, Any]] = defaultdict(
        lambda: {
            "signed": Fraction(0) if exact else 0.0,
            "absolute": Fraction(0) if exact else 0.0,
            "states": 0,
        }
    )
    records = []
    for index, orbit in enumerate(orbits):
        parameter = M73.gap_parameter(orbit[0])
        key = (str(parameter["color"]), str(min(parameter["cyclic_composition"])))
        grouped[key]["signed"] += delta[index]
        grouped[key]["absolute"] += abs(delta[index])
        grouped[key]["states"] += 1
        records.append({
            "orbit": index,
            "orbit_size": len(orbit),
            "lift_multiplicity": 3 if M83.kind(orbit[0]) == "3" else 2,
            "parameter": parameter,
            "residual_sizes": M83.cycle_sizes(M83.mul(M83.inv(orbit[0]), h)),
            "delta": scalar_string(delta[index]),
            "posterior_score": scalar_string(posterior[index]),
            "smoothed_score": scalar_string(smoothed[index]),
            "phase_triangle_ratio": (
                scalar_string(abs(posterior[index]) / phase_l1[index])
                if phase_l1[index] != 0
                else None
            ),
        })
    records.sort(
        key=lambda row: abs(float(Fraction(str(row["delta"])))), reverse=True
    )

    group_rows = []
    for (color, minimum_gap), values in sorted(grouped.items()):
        group_rows.append({
            "color": color,
            "minimum_gap": int(minimum_gap),
            "states": values["states"],
            "signed_delta": scalar_string(values["signed"]),
            "absolute_delta": scalar_string(values["absolute"]),
        })

    return {
        "n": n,
        "k": k,
        "exact": exact,
        "quotient_states": q,
        "source_orbits": {"A": ai, "B": bi},
        "source_orbit_sizes": {"A": len(orbits[ai]), "B": len(orbits[bi])},
        "source_completion_counts": {"A": str(a_count), "B": str(b_count)},
        "posterior_identity_exact_or_close": True,
        "phase_identity_exact_or_close": True,
        "smoothed_identity_exact_or_close": True,
        "eta_mass": scalar_string(sum_values(eta, exact)),
        "posterior_stationary_mean": scalar_string(
            sum((pi[s] * posterior[s] for s in range(q)), Fraction(0))
            if exact
            else float(np.dot(pi, posterior))
        ),
        "two_step_TV": scalar_string(tv_direct),
        "k_squared_two_step_TV": scalar_string(k * k * tv_direct),
        "score_L2_squared": scalar_string(score_l2),
        "smoothed_score_L2_squared": scalar_string(smoothed_l2),
        "k_fourth_smoothed_score_L2_squared": scalar_string(k ** 4 * smoothed_l2),
        "target_groups": group_rows,
        "largest_target_discrepancies": records[:20],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", nargs="+", type=int, required=True)
    parser.add_argument("--exact", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "status": "exact_identity_falsifier_not_asymptotic_evidence",
        "target": "uniform minimal long-cycle H0 pair-product quotient",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "claim_tested": "balanced posterior-cancellation and cyclic phase formulas",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
        "results": [analyze(n, args.exact) for n in args.n],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
