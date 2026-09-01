#!/usr/bin/env python3
"""Exact finite falsifier for M274's predeclared termwise MON statement.

This imports the frozen M91 audit solely to reuse its independently checked
quotient and normalized conditional-law constructors.  It tests every first
fixed-cell lag at k=3,5 over Fraction.  Finite survival is not proof; any
failure refutes only MON, not the combined OS+/MS statements.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
M91 = (
    ROOT
    / "experiments/20260811-polynomial-mixing-resolution/cycle-18/"
      "mission-M91-h0-two-step-cancellation/balanced_abel_audit.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


B = load_module("frozen_m91_balanced_abel", M91)
M = B.M


def dot(row: list[Fraction], observable: list[Fraction]) -> Fraction:
    return sum((a * b for a, b in zip(row, observable)), Fraction(0))


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def analyze(k: int) -> dict[str, object]:
    n = 3 * k
    h, orbits, kernel, squared, pi, _ = M.build(n, True)
    dimension = len(orbits)
    oid = {state: index for index, orbit in enumerate(orbits) for state in orbit}

    source_a = B.oriented_cycle(n, (0, k, 2 * k))
    source_b = M.mul(M.edge_perm(n, 0, 1), M.edge_perm(n, k, 2 * k))
    ai, bi = oid[source_a], oid[source_b]
    residual_a = M.mul(M.inv(source_a), h)
    residual_b = M.mul(M.inv(source_b), h)

    components_a = M.cycles(residual_a)
    components_b = M.cycles(residual_b)
    cminus = next(c for c in components_a if 0 in c)
    middle = next(c for c in components_a if k in c)
    cplus = next(c for c in components_a if 2 * k in c)
    long_cycle = next(c for c in components_b if len(c) == 2 * k - 1)

    nu_minus = B.first_edge_distribution(n, cminus)
    nu_middle = B.first_edge_distribution(n, middle)
    nu_plus = B.first_edge_distribution(n, cplus)
    nu_long = B.first_edge_distribution(n, long_cycle)

    p1, phi1 = B.mixture_conditionals(
        [long_cycle], [nu_long], nu_middle, oid, dimension
    )
    q1, psi1 = B.mixture_conditionals(
        [cminus, cplus], [nu_minus, nu_plus], nu_middle, oid, dimension
    )
    residual_long = B.cycle_perm(n, long_cycle)
    residual_separate = M.mul(B.cycle_perm(n, cminus), B.cycle_perm(n, cplus))
    p2, phi2 = B.pair_law_conditioned_on_first_split(
        n, residual_long, [long_cycle], oid, dimension
    )
    q2, psi2 = B.pair_law_conditioned_on_first_split(
        n, residual_separate, [cminus, cplus], oid, dimension
    )
    assert p1 == p2 and q1 == q2
    p, qmass = p1, q1
    phis = {1: phi1, 2: phi2}
    psis = {1: psi1, 2: psi2}
    h_b = {
        1: B.unconditional(p1, phi1, dimension),
        2: B.unconditional(p2, phi2, dimension),
    }
    h_a = {
        1: B.unconditional(q1, psi1, dimension),
        2: B.unconditional(q2, psi2, dimension),
    }

    cumulative: dict[int, Fraction] = {}
    running = Fraction(0)
    for u in range(1, k):
        running += p.get(u, Fraction(0)) - qmass.get(u, Fraction(0))
        cumulative[u] = running
    assert cumulative[k - 1] == 0

    rank = k - 1
    den = (3 * rank) * (3 * rank - 1)
    alpha = {
        1: Fraction(4 * rank * rank, den),
        2: Fraction(2 * rank * (2 * rank - 1), den),
    }

    violations: list[dict[str, object]] = []
    block_sign_counts = {
        f"J{j}_{block}": {"negative": 0, "zero": 0, "positive": 0}
        for j in (1, 2)
        for block in ("gradient", "embedding")
    }
    rows: list[dict[str, object]] = []
    fosd_violations: list[dict[str, object]] = []

    for y in range(1, n - 2):
        target = M.mul(M.edge_perm(n, 0, 1), M.edge_perm(n, y + 1, y + 2))
        ti = oid[target]
        response = [kernel[s][ti] / pi[ti] for s in range(dimension)]
        blocks: dict[str, Fraction] = {}
        for j in (1, 2):
            phi_response = {
                u: dot(vector, response) for u, vector in phis[j].items()
            }
            psi_response = {
                u: dot(vector, response) for u, vector in psis[j].items()
            }
            gradient = Fraction(0)
            for u in range(1, k - 1):
                monotone_increment = phi_response[u + 1] - phi_response[u]
                if monotone_increment < 0:
                    violations.append({
                        "type": "adjacent",
                        "j": j,
                        "u": u,
                        "y": y,
                        "claimed_nonnegative_exact": qstr(monotone_increment),
                    })
                gradient += cumulative[u] * (
                    phi_response[u] - phi_response[u + 1]
                )
            embedding = Fraction(0)
            for u, mass in qmass.items():
                monotone_embedding = phi_response[u] - psi_response[u]
                if monotone_embedding < 0:
                    violations.append({
                        "type": "embedding",
                        "j": j,
                        "u": u,
                        "y": y,
                        "claimed_nonnegative_exact": qstr(monotone_embedding),
                    })
                embedding += mass * monotone_embedding

            blocks[f"J{j}_gradient"] = alpha[j] * gradient
            blocks[f"J{j}_embedding"] = alpha[j] * embedding

            # Exact upper-tail test for the fully recombined scalar response
            # laws.  This is a direct coupling/order falsifier, not a test of
            # the weaker mean inequality CP_j.
            thresholds = sorted(set(response), reverse=True)
            tail_b = Fraction(0)
            tail_a = Fraction(0)
            by_value_b: dict[Fraction, Fraction] = {}
            by_value_a: dict[Fraction, Fraction] = {}
            for index, value in enumerate(response):
                by_value_b[value] = by_value_b.get(value, Fraction(0)) + h_b[j][index]
                by_value_a[value] = by_value_a.get(value, Fraction(0)) + h_a[j][index]
            for threshold in thresholds:
                tail_b += by_value_b.get(threshold, Fraction(0))
                tail_a += by_value_a.get(threshold, Fraction(0))
                defect = tail_b - tail_a
                if defect < 0:
                    fosd_violations.append({
                        "j": j,
                        "y": y,
                        "threshold_exact": qstr(threshold),
                        "B_minus_A_upper_tail_exact": qstr(defect),
                    })

        for name, value in blocks.items():
            key = "positive" if value > 0 else "negative" if value < 0 else "zero"
            block_sign_counts[name][key] += 1
        reconstructed = sum(blocks.values(), Fraction(0))
        direct = (squared[bi][ti] - squared[ai][ti]) / pi[ti]
        assert reconstructed == direct
        rows.append({
            "y": y,
            "direct_score_exact": qstr(direct),
            "blocks_exact": {name: qstr(value) for name, value in blocks.items()},
        })

    first_by_type: dict[str, object] = {}
    for kind in ("adjacent", "embedding"):
        candidates = [row for row in violations if row["type"] == kind]
        first_by_type[kind] = candidates[0] if candidates else None

    return {
        "k": k,
        "n": n,
        "target_rows": len(rows),
        "mon_violations": len(violations),
        "violations_by_type": {
            kind: sum(row["type"] == kind for row in violations)
            for kind in ("adjacent", "embedding")
        },
        "first_violation_by_type": first_by_type,
        "block_sign_counts": block_sign_counts,
        "fosd_violations": len(fosd_violations),
        "first_fosd_violation": (
            fosd_violations[0] if fosd_violations else None
        ),
        "all_complete_scores_nonnegative": all(
            Fraction(row["direct_score_exact"]) >= 0 for row in rows
        ),
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "status": "exact finite falsifier for MON only; no asymptotic inference",
        "claim": "termwise adjacent/embedding response monotonicity (MON)",
        "scope": "first fixed cell, exactly k=3,5",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "results": [analyze(3), analyze(5)],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps([
        {
            "k": row["k"],
            "mon_violations": row["mon_violations"],
            "violations_by_type": row["violations_by_type"],
            "block_sign_counts": row["block_sign_counts"],
            "fosd_violations": row["fosd_violations"],
            "first_fosd_violation": row["first_fosd_violation"],
            "all_complete_scores_nonnegative": row["all_complete_scores_nonnegative"],
        }
        for row in payload["results"]
    ], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
