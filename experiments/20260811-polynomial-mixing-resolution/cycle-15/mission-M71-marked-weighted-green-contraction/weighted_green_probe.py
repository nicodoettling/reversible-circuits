#!/usr/bin/env python3
"""Finite falsifier for child-rank-weighted contextual Green contraction.

This script studies the normalized root-composition generator G_s=R_s/alpha_s.
For every scanned contextual mean H, it solves

    (-G_s) u = H - E H

and resolves the electrical energy edge by edge.  A merge/split edge joining
parts A,B is assigned residual child rank A+B-1.  Deep continuation through a
last part t>B is assigned child rank t-1.  The resulting polynomial Lyapunov
coefficient is a necessary finite test for the rank-resolved M56 recurrence.

Finite passes are not proofs.  A coefficient above one (beyond the recorded
linear-solve residual) refutes the corresponding exponent/normalization.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import scipy
import scipy.sparse as sp
import scipy.sparse.linalg as spla


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def compositions(total: int):
    for mask in range(1 << (total - 1)):
        answer = []
        start = 0
        for position in range(total - 1):
            if mask & (1 << position):
                answer.append(position + 1 - start)
                start = position + 1
        answer.append(total - start)
        yield tuple(answer)


def log_w(a: int) -> float:
    return (a - 1) * math.log(a) - math.lgamma(a + 1)


def w_ratio(left: int, right: int) -> float:
    return math.exp(log_w(left) + log_w(right) - log_w(left + right))


def log_z(s: int) -> float:
    return (s - 1) * math.log(s + 1) - math.lgamma(s + 1)


def log_comb(n: int, k: int) -> float:
    if k < 0 or k > n:
        return -math.inf
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def comb_ratio(n1: int, k1: int, n2: int, k2: int) -> float:
    return math.exp(log_comb(n1, k1) - log_comb(n2, k2))


def contextual_values(keys, K: int, R: int, B: int) -> np.ndarray:
    values = np.zeros(len(keys))
    for index, (k, t) in enumerate(keys):
        if t < B:
            continue
        if t == B:
            values[index] = K * comb_ratio(
                k + K - R - 2,
                K - R - 1,
                k + K - 1,
                K - 1,
            )
        else:
            local = w_ratio(t - B, B)
            bad = comb_ratio(K, R + 1, K + k, R + 1)
            values[index] = local * (1.0 - bad)
    return values


def build_rank(s: int):
    comps = list(compositions(s))
    index = {comp: i for i, comp in enumerate(comps)}
    rho = np.array(
        [
            math.exp(
                -math.lgamma(len(comp) + 1)
                + sum(log_w(part) for part in comp)
                - log_z(s)
            )
            for comp in comps
        ]
    )
    rho /= rho.sum()

    diagonal = np.zeros(len(comps))
    rows = []
    cols = []
    data = []
    merge_edges = []
    for i, comp in enumerate(comps):
        k = len(comp)
        for boundary in range(k - 1):
            left = comp[boundary]
            right = comp[boundary + 1]
            target = (
                comp[:boundary]
                + (left + right,)
                + comp[boundary + 2 :]
            )
            j = index[target]
            forward = float(k)
            reverse = w_ratio(left, right)
            rows.append(i)
            cols.append(j)
            data.append(-math.sqrt(forward * reverse))
            diagonal[i] += forward
            merge_edges.append(
                (
                    i,
                    j,
                    float(rho[i] * forward),
                    left + right - 1,
                    left,
                    right,
                    k - 1,
                    k - boundary - 2,
                )
            )
        for part_index, part in enumerate(comp):
            for left in range(1, part):
                right = part - left
                target = (
                    comp[:part_index]
                    + (left, right)
                    + comp[part_index + 1 :]
                )
                j = index[target]
                forward = w_ratio(left, right)
                reverse = float(k + 1)
                rows.append(i)
                cols.append(j)
                data.append(-math.sqrt(forward * reverse))
                diagonal[i] += forward

    rows.extend(range(len(comps)))
    cols.extend(range(len(comps)))
    data.extend(diagonal)
    laplacian = sp.csr_matrix(
        (data, (rows, cols)), shape=(len(comps), len(comps))
    )
    groups = defaultdict(list)
    for i, comp in enumerate(comps):
        groups[(len(comp), comp[-1])].append(i)
    keys = sorted(groups)
    return comps, rho, laplacian, keys, groups, merge_edges


def solve_group_basis(rho, laplacian, keys, groups, rtol, maxiter):
    root_rho = np.sqrt(rho)

    def matvec(x):
        return laplacian @ x + root_rho * np.dot(root_rho, x)

    operator = spla.LinearOperator(
        laplacian.shape, matvec=matvec, dtype=float
    )
    preconditioner = spla.LinearOperator(
        laplacian.shape,
        matvec=lambda x: x / (laplacian.diagonal() + rho),
        dtype=float,
    )
    masses = []
    solutions = []
    residuals = []
    iterations = []
    for key in keys:
        indicator = np.zeros(len(rho))
        indicator[groups[key]] = 1.0
        mass = float(np.dot(rho, indicator))
        rhs = root_rho * (indicator - mass)
        count = [0]

        def callback(_):
            count[0] += 1

        try:
            solution, info = spla.cg(
                operator,
                rhs,
                M=preconditioner,
                rtol=rtol,
                atol=0.0,
                maxiter=maxiter,
                callback=callback,
            )
        except TypeError:  # scipy<1.12 uses ``tol`` rather than ``rtol``.
            solution, info = spla.cg(
                operator,
                rhs,
                M=preconditioner,
                tol=rtol,
                maxiter=maxiter,
                callback=callback,
            )
        if info != 0:
            raise RuntimeError(f"CG failed for group {key}: info={info}")
        relative = float(
            np.linalg.norm(matvec(solution) - rhs)
            / max(np.linalg.norm(rhs), 1e-300)
        )
        masses.append(mass)
        solutions.append(solution)
        residuals.append(relative)
        iterations.append(count[0])
    return (
        np.array(masses),
        np.column_stack(solutions),
        max(residuals),
        max(iterations),
    )


def rank_weight(rank: int, exponent: int) -> float:
    return float(rank**exponent) if rank >= 2 else 0.0


def analyze_context(
    s,
    rho,
    keys,
    masses,
    basis_solutions,
    merge_edges,
    K,
    R,
    B,
    exponents,
    bonuses,
):
    values = contextual_values(keys, K, R, B)
    mean = float(np.dot(masses, values))
    symmetric_potential = basis_solutions @ values
    physical_potential = symmetric_potential / np.sqrt(rho)

    edge_rows = []
    total_energy = 0.0
    for (
        i,
        j,
        capacity,
        child_rank,
        left,
        right,
        child_K,
        child_R,
    ) in merge_edges:
        energy = capacity * (
            physical_potential[i] - physical_potential[j]
        ) ** 2
        total_energy += energy
        edge_rows.append(
            (
                energy,
                child_rank,
                left,
                right,
                child_K,
                child_R,
            )
        )

    terminal = float(
        sum(
            masses[index] * values[index]
            for index, (_, last) in enumerate(keys)
            if last == B
        )
    )
    deep = mean - terminal
    rows = {}
    for exponent in exponents:
        deep_weighted = float(
            sum(
                masses[index]
                * values[index]
                * rank_weight(last - 1, exponent)
                for index, (_, last) in enumerate(keys)
                if last > B
            )
        )
        quotient_weighted = float(
            sum(
                energy * rank_weight(child_rank, exponent)
                for energy, child_rank, _, _, _, _ in edge_rows
            )
        )
        coefficient = (deep_weighted + quotient_weighted) / (
            mean * (s**exponent)
        )
        rows[str(exponent)] = {
            "coefficient": coefficient,
            "deep_weighted_over_mean": deep_weighted / mean,
            "quotient_weighted_over_mean": quotient_weighted / mean,
            "slack_times_s": (1.0 - coefficient) * s,
        }
        excess_deep_weighted = float(
            sum(
                masses[index]
                * values[index]
                * float((last - B) ** exponent)
                for index, (_, last) in enumerate(keys)
                if last > B
            )
        )
        excess_quotient_weighted = float(
            sum(
                energy * float(left**exponent)
                for energy, _, left, _, _, _ in edge_rows
            )
        )
        parent_excess_potential = float((s - B + 1) ** exponent)
        excess_coefficient = (
            excess_deep_weighted + excess_quotient_weighted
        ) / (mean * parent_excess_potential)
        rows[str(exponent)].update(
            {
                "excess_coefficient": excess_coefficient,
                "excess_deep_weighted_over_mean": (
                    excess_deep_weighted / mean
                ),
                "excess_quotient_weighted_over_mean": (
                    excess_quotient_weighted / mean
                ),
                "excess_absolute_drift": parent_excess_potential
                * (1.0 - excess_coefficient),
            }
        )
    bonus_rows = {}
    for bonus in bonuses:
        parent_potential = float(s * (1.0 + bonus * (B < s)))
        bonus_deep_weighted = float(
            sum(
                masses[index]
                * values[index]
                * float(
                    (last - 1)
                    * (1.0 + bonus * (B < last - 1))
                )
                for index, (_, last) in enumerate(keys)
                if last > B
            )
        )
        bonus_quotient_weighted = float(
            sum(
                energy
                * float(
                    child_rank
                    * (1.0 + bonus * (right < child_rank))
                )
                for energy, child_rank, _, right, _, _ in edge_rows
            )
        )
        coefficient = (
            bonus_deep_weighted + bonus_quotient_weighted
        ) / (mean * parent_potential)
        bonus_rows[f"{bonus:.12g}"] = {
            "coefficient": coefficient,
            "deep_weighted_over_mean": bonus_deep_weighted / mean,
            "quotient_weighted_over_mean": bonus_quotient_weighted / mean,
            "absolute_drift": parent_potential * (1.0 - coefficient),
        }
    return {
        "s": s,
        "K": K,
        "R": R,
        "B": B,
        "mean": mean,
        "terminal_mass": terminal,
        "deep_fraction": deep / mean,
        "green_energy": total_energy,
        "green_over_mean": total_energy / mean,
        "delta_plus_a": (deep + total_energy) / mean,
        "weighted": rows,
        "deep_bonus_weighted": bonus_rows,
    }


def scan_rank(s, k_values, exponents, bonuses, rtol, maxiter):
    started = time.time()
    (
        comps,
        rho,
        laplacian,
        keys,
        groups,
        merge_edges,
    ) = build_rank(s)
    masses, basis, max_residual, max_iterations = solve_group_basis(
        rho, laplacian, keys, groups, rtol, maxiter
    )
    worst = {str(exponent): None for exponent in exponents}
    worst_excess = {str(exponent): None for exponent in exponents}
    worst_bonus = {f"{bonus:.12g}": None for bonus in bonuses}
    worst_unweighted = None
    count = 0
    max_energy_identity_error = 0.0
    for K in k_values:
        if K <= 32:
            r_values = range(K)
        else:
            r_values = sorted(
                {
                    0,
                    1 if K > 1 else 0,
                    K // 4,
                    K // 2,
                    (3 * K) // 4,
                    K - 2 if K > 1 else 0,
                    K - 1,
                }
            )
        for R in r_values:
            for B in range(1, s + 1):
                row = analyze_context(
                    s,
                    rho,
                    keys,
                    masses,
                    basis,
                    merge_edges,
                    K,
                    R,
                    B,
                    exponents,
                    bonuses,
                )
                values = contextual_values(keys, K, R, B)
                symmetric_potential = basis @ values
                quadratic = float(
                    np.dot(
                        np.sqrt(rho) * (values[
                            [
                                next(
                                    index
                                    for index, key in enumerate(keys)
                                    if key == (len(comp), comp[-1])
                                )
                                for comp in comps
                            ]
                        ] - row["mean"]),
                        symmetric_potential,
                    )
                )
                max_energy_identity_error = max(
                    max_energy_identity_error,
                    abs(quadratic - row["green_energy"])
                    / max(abs(quadratic), 1e-300),
                )
                if (
                    worst_unweighted is None
                    or row["delta_plus_a"] > worst_unweighted["delta_plus_a"]
                ):
                    worst_unweighted = row
                for exponent in exponents:
                    key = str(exponent)
                    if (
                        worst[key] is None
                        or row["weighted"][key]["coefficient"]
                        > worst[key]["weighted"][key]["coefficient"]
                    ):
                        worst[key] = row
                    if (
                        worst_excess[key] is None
                        or row["weighted"][key]["excess_coefficient"]
                        > worst_excess[key]["weighted"][key][
                            "excess_coefficient"
                        ]
                    ):
                        worst_excess[key] = row
                for bonus in bonuses:
                    key = f"{bonus:.12g}"
                    if (
                        worst_bonus[key] is None
                        or row["deep_bonus_weighted"][key]["coefficient"]
                        > worst_bonus[key]["deep_bonus_weighted"][key][
                            "coefficient"
                        ]
                    ):
                        worst_bonus[key] = row
                count += 1
    return {
        "s": s,
        "state_count": len(comps),
        "group_count": len(keys),
        "merge_edge_count": len(merge_edges),
        "context_count": count,
        "max_cg_relative_residual": max_residual,
        "max_cg_iterations": max_iterations,
        "max_energy_identity_relative_error": max_energy_identity_error,
        "worst_unweighted": worst_unweighted,
        "worst_by_exponent": worst,
        "worst_excess_by_exponent": worst_excess,
        "worst_deep_bonus": worst_bonus,
        "elapsed_seconds": time.time() - started,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=10)
    parser.add_argument("--K-max", type=int, default=32)
    parser.add_argument("--exponents", type=int, nargs="+", default=[1, 2, 3, 4])
    parser.add_argument(
        "--bonuses", type=float, nargs="+", default=[0.05, 0.1, 0.2, 0.4]
    )
    parser.add_argument("--rtol", type=float, default=1e-11)
    parser.add_argument("--maxiter", type=int, default=20000)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 2 <= args.s_max <= 16:
        raise SystemExit("bounded range is 2 <= s-max <= 16")
    if args.K_max < 1 or any(p < 1 for p in args.exponents):
        raise SystemExit("K-max and exponents must be positive")
    k_values = list(range(1, args.K_max + 1))
    for extra in (64, 128, 256, 1024, 4096):
        if extra > args.K_max:
            k_values.append(extra)
    records = []
    for s in range(2, args.s_max + 1):
        record = scan_rank(
            s,
            k_values,
            args.exponents,
            args.bonuses,
            args.rtol,
            args.maxiter,
        )
        records.append(record)
        print(
            json.dumps(
                {
                    "s": s,
                    "state_count": record["state_count"],
                    "worst_coefficients": {
                        exponent: record["worst_by_exponent"][str(exponent)][
                            "weighted"
                        ][str(exponent)]["coefficient"]
                        for exponent in args.exponents
                    },
                    "worst_excess_coefficients": {
                        exponent: record["worst_excess_by_exponent"][
                            str(exponent)
                        ]["weighted"][str(exponent)]["excess_coefficient"]
                        for exponent in args.exponents
                    },
                    "worst_deep_bonus_coefficients": {
                        f"{bonus:.12g}": record["worst_deep_bonus"][
                            f"{bonus:.12g}"
                        ]["deep_bonus_weighted"][f"{bonus:.12g}"][
                            "coefficient"
                        ]
                        for bonus in args.bonuses
                    },
                    "elapsed_seconds": record["elapsed_seconds"],
                },
                sort_keys=True,
            ),
            flush=True,
        )

    command = (
        "python3 -B experiments/20260811-polynomial-mixing-resolution/"
        "cycle-15/mission-M71-marked-weighted-green-contraction/"
        f"weighted_green_probe.py --s-max {args.s_max} --K-max {args.K_max} "
        f"--exponents {' '.join(map(str, args.exponents))} "
        f"--bonuses {' '.join(map(str, args.bonuses))} "
        f"--rtol {args.rtol} --maxiter {args.maxiter} --output {args.output}"
    )
    result = {
        "claim_tested": (
            "For contextual means H, the exact deep-continuation mass and "
            "quotient electrical energy contract after weighting each "
            "recursive residual by its actual lower child rank^p."
        ),
        "finite_scope_warning": (
            "A coefficient above one beyond numerical error refutes that "
            "exponent on the scanned context. Finite coefficients below one "
            "do not prove a universal contraction."
        ),
        "normalization": (
            "G_s=R_s/alpha_s; undirected capacity rho(C)G_s(C,C'); "
            "merge A,B residual rank A+B-1; deep last-part t residual rank "
            "t-1; ranks 0 and 1 have zero recursive Green cost."
        ),
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "seed": None,
        "command": command,
        "parameters": {
            "s_max": args.s_max,
            "K_max": args.K_max,
            "extra_K": [value for value in k_values if value > args.K_max],
            "exponents": args.exponents,
            "bonuses": args.bonuses,
            "rtol": args.rtol,
            "maxiter": args.maxiter,
        },
        "records": records,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
