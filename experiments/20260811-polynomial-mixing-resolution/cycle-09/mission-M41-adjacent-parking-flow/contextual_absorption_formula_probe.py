#!/usr/bin/env python3
"""Finite falsifier for the conjectural closed-form contextual absorption law.

This script does not prove the contextual rate formula or its H^{-1}
inequality.  It assumes the formula observed in the independently generated
ambient-rank-seven data and tests the resulting root-composition quotient at
larger local ranks.  All computations use the normalized quotient generator
G/alpha; the common alpha factor cancels from the proposed inequality.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import time
from pathlib import Path

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import splu


def compositions(total: int) -> list[tuple[int, ...]]:
    if total == 0:
        return [()]
    out: list[tuple[int, ...]] = []
    for mask in range(1 << (total - 1)):
        current = 1
        parts: list[int] = []
        for j in range(total - 1):
            if mask & (1 << j):
                parts.append(current)
                current = 1
            else:
                current += 1
        parts.append(current)
        out.append(tuple(parts))
    return out


def log_w(size: int) -> float:
    # w_size = size^(size-1)/size!, with w_1=1.
    return (size - 1) * math.log(size) - math.lgamma(size + 1)


def split_ratio(left: int, right: int) -> float:
    return math.exp(log_w(left) + log_w(right) - log_w(left + right))


def stationary(comps: list[tuple[int, ...]]) -> np.ndarray:
    logs = np.array(
        [sum(log_w(x) for x in comp) - math.lgamma(len(comp) + 1) for comp in comps],
        dtype=float,
    )
    logs -= float(logs.max())
    weights = np.exp(logs)
    return weights / weights.sum()


def normalized_laplacian(
    total: int, comps: list[tuple[int, ...]], pi: np.ndarray
):
    """Return D^(1/2)(-G/alpha)D^(-1/2), with one gauge row removed."""
    index = {comp: i for i, comp in enumerate(comps)}
    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []
    diagonal = np.zeros(len(comps), dtype=float)

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
            diagonal[i] += rate
            rows.append(i)
            cols.append(j)
            data.append(-rate * math.sqrt(pi[i] / pi[j]))

        for part_index, size in enumerate(comp):
            for left in range(1, size):
                right = size - left
                target = comp[:part_index] + (left, right) + comp[part_index + 1 :]
                j = index[target]
                rate = split_ratio(left, right)
                diagonal[i] += rate
                rows.append(i)
                cols.append(j)
                data.append(-rate * math.sqrt(pi[i] / pi[j]))

    rows.extend(range(len(comps)))
    cols.extend(range(len(comps)))
    data.extend(diagonal.tolist())
    matrix = coo_matrix((data, (rows, cols)), shape=(len(comps), len(comps))).tocsc()
    asymmetry = matrix - matrix.transpose()
    max_asymmetry = float(np.max(np.abs(asymmetry.data))) if asymmetry.nnz else 0.0

    # A principal minor fixes the additive constant.  For compatible b, the
    # resulting quadratic form is exactly b^T A^+ b.
    reduced = matrix[:-1, :-1].tocsc()
    factor = splu(reduced)
    return matrix, factor, max_asymmetry


def contextual_q(comp: tuple[int, ...], suffix: int, outer_k: int, right: int) -> float:
    """Conjectural exact q=E[f|C]/alpha from the ambient-rank-seven pattern."""
    inner_k = len(comp)
    last = comp[-1]
    if last < suffix:
        return 0.0
    if last == suffix:
        numerator = outer_k * math.comb(
            inner_k + outer_k - right - 2, outer_k - right - 1
        )
        denominator = math.comb(inner_k + outer_k - 1, outer_k - 1)
        return numerator / denominator

    weight = split_ratio(last - suffix, suffix)
    deep = 1.0 - math.comb(outer_k, right + 1) / math.comb(
        outer_k + inner_k, right + 1
    )
    return weight * deep


def evaluate_candidate(
    comps: list[tuple[int, ...]],
    pi: np.ndarray,
    factor,
    suffix: int,
    outer_k: int,
    right: int,
) -> dict[str, float | int]:
    q = np.fromiter(
        (contextual_q(comp, suffix, outer_k, right) for comp in comps),
        dtype=float,
        count=len(comps),
    )
    mean = float(np.dot(pi, q))
    centered = q - mean
    b = np.sqrt(pi) * centered
    solution = factor.solve(b[:-1])
    hminus = float(np.dot(b[:-1], solution))
    terminal = float(
        sum(pi[i] * q[i] for i, comp in enumerate(comps) if comp[-1] == suffix)
    )
    deep = float(
        sum(pi[i] * q[i] for i, comp in enumerate(comps) if comp[-1] > suffix)
    )
    ratio = hminus / terminal if terminal > 0 else math.inf
    delta = deep / mean if mean > 0 else 0.0
    a_value = hminus / mean if mean > 0 else 0.0
    return {
        "suffix": suffix,
        "outer_k": outer_k,
        "right": right,
        "mean": mean,
        "terminal": terminal,
        "deep": deep,
        "hminus": hminus,
        "ratio_hminus_terminal": ratio,
        "delta": delta,
        "a": a_value,
        "delta_plus_a": delta + a_value,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-rank", type=int, default=11)
    parser.add_argument("--max-outer-k", type=int, default=20)
    parser.add_argument(
        "--rightmost-suffix-one-only",
        action="store_true",
        help="test only B=1, K=max-outer-k, R=K-1 at each rank",
    )
    parser.add_argument(
        "--fixed-right",
        type=int,
        default=None,
        help="test only this R for every K>R (incompatible with rightmost-only)",
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    started = time.time()
    ranks: list[dict[str, object]] = []
    global_worst: dict[str, object] | None = None
    violations: list[dict[str, object]] = []

    for rank in range(2, args.max_rank + 1):
        comps = compositions(rank)
        pi = stationary(comps)
        matrix, factor, max_asymmetry = normalized_laplacian(rank, comps, pi)
        rank_worst: dict[str, object] | None = None
        candidates = 0

        suffixes = [1] if args.rightmost_suffix_one_only else range(1, rank + 1)
        outer_values = (
            [args.max_outer_k]
            if args.rightmost_suffix_one_only
            else range(1, args.max_outer_k + 1)
        )
        for suffix in suffixes:
            for outer_k in outer_values:
                if args.rightmost_suffix_one_only:
                    right_values = [outer_k - 1]
                elif args.fixed_right is not None:
                    right_values = (
                        [args.fixed_right] if args.fixed_right < outer_k else []
                    )
                else:
                    right_values = range(outer_k)
                for right in right_values:
                    result = evaluate_candidate(
                        comps, pi, factor, suffix, outer_k, right
                    )
                    result["rank"] = rank
                    candidates += 1
                    if rank_worst is None or result["ratio_hminus_terminal"] > rank_worst[
                        "ratio_hminus_terminal"
                    ]:
                        rank_worst = result.copy()
                    if global_worst is None or result[
                        "ratio_hminus_terminal"
                    ] > global_worst["ratio_hminus_terminal"]:
                        global_worst = result.copy()
                    if result["ratio_hminus_terminal"] > 1.0 + 1e-8:
                        violations.append(result.copy())

        ranks.append(
            {
                "rank": rank,
                "states": len(comps),
                "generator_nnz": int(matrix.nnz),
                "max_symmetry_error": max_asymmetry,
                "stationary_sum": float(pi.sum()),
                "candidates": candidates,
                "worst": rank_worst,
            }
        )

    payload = {
        "status": "finite_falsifier_only",
        "assumption": "closed contextual formula observed at ambient rank seven",
        "max_rank": args.max_rank,
        "max_outer_k": args.max_outer_k,
        "rightmost_suffix_one_only": args.rightmost_suffix_one_only,
        "fixed_right": args.fixed_right,
        "global_worst": global_worst,
        "violation_count": len(violations),
        "first_violations": violations[:20],
        "ranks": ranks,
        "runtime_seconds": time.time() - started,
        "python": platform.python_version(),
        "numpy": np.__version__,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
