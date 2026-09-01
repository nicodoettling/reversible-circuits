#!/usr/bin/env python3
"""Sparse bounded falsifier for contextual quotient absorption.

For each composition rank s, this builds the exact normalized quotient
generator G_s, compresses its Green quadratic form to functions of
(number of parts, last part), and scans the closed contextual means over
many external K,R and suffix B.  Numerical agreement cannot prove the
universal inequality; a ratio above one beyond certified residual error
would refute it.
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


def git_commit():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def compositions(total):
    if total == 0:
        yield ()
        return
    for mask in range(1 << (total - 1)):
        answer = []
        start = 0
        for position in range(total - 1):
            if mask & (1 << position):
                answer.append(position + 1 - start)
                start = position + 1
        answer.append(total - start)
        yield tuple(answer)


def log_w(a):
    return (a - 1) * math.log(a) - math.lgamma(a + 1)


def w_ratio(left, right):
    return math.exp(log_w(left) + log_w(right) - log_w(left + right))


def log_z(s):
    if s == 0:
        return 0.0
    return (s - 1) * math.log(s + 1) - math.lgamma(s + 1)


def build_rank(s):
    comps = list(compositions(s))
    index = {comp: i for i, comp in enumerate(comps)}
    n = len(comps)
    log_rho = np.array(
        [
            -math.lgamma(len(comp) + 1)
            + sum(log_w(part) for part in comp)
            - log_z(s)
            for comp in comps
        ]
    )
    rho = np.exp(log_rho)
    rho /= rho.sum()

    rows = []
    cols = []
    data = []
    diagonal = np.zeros(n)
    for i, comp in enumerate(comps):
        k = len(comp)
        for boundary in range(k - 1):
            target = (
                comp[:boundary]
                + (comp[boundary] + comp[boundary + 1],)
                + comp[boundary + 2 :]
            )
            j = index[target]
            rate = float(k)
            reverse = w_ratio(comp[boundary], comp[boundary + 1])
            rows.append(i)
            cols.append(j)
            data.append(-math.sqrt(rate * reverse))
            diagonal[i] += rate
        for part_index, part in enumerate(comp):
            for left in range(1, part):
                right = part - left
                target = (
                    comp[:part_index]
                    + (left, right)
                    + comp[part_index + 1 :]
                )
                j = index[target]
                rate = w_ratio(left, right)
                reverse = float(k + 1)
                rows.append(i)
                cols.append(j)
                data.append(-math.sqrt(rate * reverse))
                diagonal[i] += rate
    rows.extend(range(n))
    cols.extend(range(n))
    data.extend(diagonal)
    laplacian = sp.csr_matrix((data, (rows, cols)), shape=(n, n))

    asymmetry = float(
        np.max(np.abs((laplacian - laplacian.T).data))
        if (laplacian - laplacian.T).nnz
        else 0.0
    )
    groups = defaultdict(list)
    for i, comp in enumerate(comps):
        groups[(len(comp), comp[-1])].append(i)
    keys = sorted(groups)
    return comps, rho, laplacian, keys, groups, asymmetry


def compressed_green(rho, laplacian, keys, groups, rtol, maxiter):
    n = len(rho)
    u = np.sqrt(rho)

    def matvec(x):
        return laplacian @ x + u * np.dot(u, x)

    operator = spla.LinearOperator((n, n), matvec=matvec, dtype=float)
    rhs_columns = []
    masses = []
    for key in keys:
        indicator = np.zeros(n)
        indicator[groups[key]] = 1.0
        mass = float(np.dot(rho, indicator))
        masses.append(mass)
        rhs_columns.append(u * (indicator - mass))
    rhs = np.column_stack(rhs_columns)
    solutions = np.empty_like(rhs)
    residuals = []
    iterations = []
    diagonal_preconditioner = 1.0 / (laplacian.diagonal() + rho)
    preconditioner = spla.LinearOperator(
        (n, n), matvec=lambda x: diagonal_preconditioner * x, dtype=float
    )
    for column in range(rhs.shape[1]):
        count = [0]

        def callback(_):
            count[0] += 1

        try:
            solution, info = spla.cg(
                operator,
                rhs[:, column],
                M=preconditioner,
                rtol=rtol,
                atol=0.0,
                maxiter=maxiter,
                callback=callback,
            )
        except TypeError:  # scipy<1.12 uses ``tol`` rather than ``rtol``.
            solution, info = spla.cg(
                operator,
                rhs[:, column],
                M=preconditioner,
                tol=rtol,
                maxiter=maxiter,
                callback=callback,
            )
        if info != 0:
            raise RuntimeError(
                f"CG failed for group {keys[column]}: info={info}"
            )
        solutions[:, column] = solution
        residuals.append(
            float(
                np.linalg.norm(matvec(solution) - rhs[:, column])
                / max(np.linalg.norm(rhs[:, column]), 1e-300)
            )
        )
        iterations.append(count[0])
    green = rhs.T @ solutions
    green = (green + green.T) / 2.0
    return np.array(masses), green, max(residuals), max(iterations)


def log_comb(n, k):
    if k < 0 or k > n:
        return -math.inf
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def comb_ratio(n1, k1, n2, k2):
    return math.exp(log_comb(n1, k1) - log_comb(n2, k2))


def contextual_values(keys, K, R, B):
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


def scan_rank(s, k_values, rtol, maxiter):
    started = time.time()
    comps, rho, laplacian, keys, groups, asymmetry = build_rank(s)
    masses, green, max_residual, max_iterations = compressed_green(
        rho, laplacian, keys, groups, rtol, maxiter
    )
    worst = None
    maximum_mean_error = 0.0
    context_count = 0
    for K in k_values:
        r_values = range(K) if K <= 64 else sorted({
            0,
            1 if K > 1 else 0,
            K // 4,
            K // 2,
            (3 * K) // 4,
            K - 2 if K > 1 else 0,
            K - 1,
        })
        for R in r_values:
            for B in range(1, s + 1):
                values = contextual_values(keys, K, R, B)
                mean = float(np.dot(masses, values))
                expected_mean = w_ratio(s + 1 - B, B)
                maximum_mean_error = max(
                    maximum_mean_error,
                    abs(mean - expected_mean) / max(expected_mean, 1e-300),
                )
                terminal = float(
                    sum(
                        masses[j] * values[j]
                        for j, (_, t) in enumerate(keys)
                        if t == B
                    )
                )
                energy = float(values @ green @ values)
                ratio = energy / terminal if terminal > 0 else 0.0
                delta_plus_a = 1.0 + (energy - terminal) / mean
                row = {
                    "s": s,
                    "K": K,
                    "R": R,
                    "B": B,
                    "mean": mean,
                    "terminal_mass": terminal,
                    "energy": energy,
                    "absorption_ratio": ratio,
                    "delta_plus_a": delta_plus_a,
                }
                if worst is None or ratio > worst["absorption_ratio"]:
                    worst = row
                context_count += 1
    return {
        "s": s,
        "state_count": len(comps),
        "group_count": len(keys),
        "context_count": context_count,
        "external_K_values": k_values,
        "laplacian_max_asymmetry": asymmetry,
        "cg_max_relative_residual": max_residual,
        "cg_max_iterations": max_iterations,
        "maximum_relative_mean_identity_error": maximum_mean_error,
        "worst": worst,
        "elapsed_seconds": time.time() - started,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=12)
    parser.add_argument("--K-max", type=int, default=64)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--rtol", type=float, default=1e-11)
    parser.add_argument("--maxiter", type=int, default=20000)
    args = parser.parse_args()
    if not 2 <= args.s_max <= 18:
        raise SystemExit("bounded numerical range is 2 <= s-max <= 18")
    if args.K_max < 1:
        raise SystemExit("K-max must be positive")
    k_values = list(range(1, args.K_max + 1))
    for extra in (128, 256, 512, 1024, 4096):
        if extra > args.K_max:
            k_values.append(extra)
    records = []
    for s in range(2, args.s_max + 1):
        record = scan_rank(s, k_values, args.rtol, args.maxiter)
        records.append(record)
        print(json.dumps(record, sort_keys=True), flush=True)
    result = {
        "claim_tested": (
            "For all contextual closed means H, the normalized Green "
            "energy is at most the terminal last-part-B mass."
        ),
        "finite_scope_warning": (
            "A ratio above one beyond numerical error refutes absorption. "
            "Ratios below one on this finite grid do not prove it."
        ),
        "normalization": (
            "G=R_s/alpha_s; absorption_ratio="
            "<H-EH,(-G)^+(H-EH)>_rho/E[H 1_{last=B}]."
        ),
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "seed": None,
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-14/mission-M65-contextual-quotient-absorption/"
            f"absorption_scan.py --s-max {args.s_max} --K-max {args.K_max} "
            f"--rtol {args.rtol} --maxiter {args.maxiter} --output "
            f"{args.output}"
        ),
        "records": records,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
