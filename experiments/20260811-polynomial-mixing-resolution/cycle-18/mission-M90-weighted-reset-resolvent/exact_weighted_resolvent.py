#!/usr/bin/env python3
"""Exact grouped recurrence for M90's weighted reset resolvent.

For ``x=(s,K,R,B)`` define

    g(x) = q_x [(I-D)^(-1) J_can W](x).

Multiplication by ``q_x`` cancels the parent divisor in both kernels and
gives the finite rank-descending recurrence

    g(x) = A(x) + sum_{k,t,j} rho_s(k,t) nu_{K,R,k}(j) g(y),

where ``A=sum_e (theta_e^2/Q_G(e)) (1-q_{y_e})``.  All sums use Cayley
coefficients and ``fractions.Fraction``.  A bounded pass is a falsifier only.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import platform
import time
from fractions import Fraction
from pathlib import Path


@functools.lru_cache(maxsize=None)
def w(a: int) -> Fraction:
    if a < 1:
        raise ValueError(a)
    return Fraction(a ** (a - 1), math.factorial(a))


@functools.lru_cache(maxsize=None)
def cayley(total: int, parts: int) -> Fraction:
    """Product-weight sum over positive ordered ``parts``-compositions."""
    if parts == 0:
        return Fraction(int(total == 0))
    if not 1 <= parts <= total:
        return Fraction(0)
    return Fraction(
        parts * total ** (total - parts),
        total * math.factorial(total - parts),
    )


def q_split(s: int, B: int) -> Fraction:
    return w(s + 1 - B) * w(B) / w(s + 1)


def comb_ratio(n1: int, k1: int, n2: int, k2: int) -> Fraction:
    if not (0 <= k1 <= n1 and 0 <= k2 <= n2):
        return Fraction(0)
    return Fraction(math.comb(n1, k1), math.comb(n2, k2))


def contextual_value(k: int, t: int, K: int, R: int, B: int) -> Fraction:
    if t < B:
        return Fraction(0)
    if t == B:
        return K * comb_ratio(
            k + K - R - 2,
            K - R - 1,
            k + K - 1,
            K - 1,
        )
    local = w(t - B) * w(B) / w(t)
    bad = comb_ratio(K, R + 1, K + k, R + 1)
    return local * (1 - bad)


def nu(K: int, R: int, k: int, j: int) -> Fraction:
    return Fraction(
        math.comb(R + j, j)
        * math.comb(K - R - 1 + k - j, k - j),
        math.comb(K + k, k),
    )


@functools.lru_cache(maxsize=None)
def groups(s: int) -> tuple[tuple[int, int, Fraction], ...]:
    rows = []
    total = Fraction(0)
    for k in range(1, s + 1):
        for t in range(1, s + 1):
            mass = w(t) * cayley(s - t, k - 1) / (
                math.factorial(k) * w(s + 1)
            )
            if mass:
                rows.append((k, t, mass))
                total += mass
    if total != 1:
        raise AssertionError((s, total))
    return tuple(rows)


@functools.lru_cache(maxsize=None)
def reset_budget(s: int, K: int, R: int, B: int) -> Fraction:
    """Return ``A=sum_e (theta_e^2/Q_G(e))(1-q_child)`` exactly."""
    q_parent = q_split(s, B)
    answer = Fraction(0)
    scalar_cache: dict[tuple[int, int, int], Fraction] = {}

    def basin_scalar(A: int, ell: int, last: int) -> Fraction:
        key = (A, ell, last)
        if key not in scalar_cache:
            value = Fraction(0)
            for p in range(1, A + 1):
                coefficient = cayley(A, p)
                if coefficient:
                    value += coefficient * (
                        contextual_value(p + ell, last, K, R, B) - q_parent
                    ) / math.factorial(p + ell)
            scalar_cache[key] = value
        return scalar_cache[key]

    # Refined endpoint is (A,b,tail), with ell suffix parts after A.
    for ell in range(1, s):
        tail_parts = ell - 1
        for A in range(1, s + 1):
            max_b = s - A - tail_parts
            for b in range(1, max_b + 1):
                tail_total = s - A - b
                child_rank = A + b - 1
                if child_rank < 2:
                    continue
                if tail_parts == 0:
                    if tail_total != 0:
                        continue
                    tail_rows = ((b, w(b)),)
                else:
                    rows = []
                    for last in range(1, tail_total + 1):
                        prefix = cayley(tail_total - last, tail_parts - 1)
                        if prefix:
                            rows.append((last, w(b) * prefix * w(last)))
                    tail_rows = tuple(rows)
                q_child = q_split(child_rank, b)
                for last, suffix_weight in tail_rows:
                    scalar = basin_scalar(A, ell, last)
                    energy = (
                        suffix_weight
                        * math.factorial(ell)
                        * scalar
                        * scalar
                        / (w(A) * w(s + 1))
                    )
                    answer += energy * (1 - q_child)
    return answer


class ExactResolvent:
    def __init__(self) -> None:
        self.contexts = 0
        self.deep_terms = 0

    @functools.lru_cache(maxsize=None)
    def g(self, s: int, K: int, R: int, B: int) -> Fraction:
        if s <= 1:
            return Fraction(0)
        self.contexts += 1
        answer = reset_budget(s, K, R, B)
        parent_phase = s + K - R
        for k, t, mass in groups(s):
            if t <= B or t - 1 < 2:
                continue
            for j in range(1, k + 1):
                probability = nu(K, R, k, j)
                if not probability:
                    continue
                child = (t - 1, K + k, R + j, B)
                if child[0] + child[1] - child[2] >= parent_phase:
                    raise AssertionError((s, K, R, B, child))
                self.deep_terms += 1
                answer += mass * probability * self.g(*child)
        return answer


def fraction_record(value: Fraction) -> dict[str, object]:
    return {
        "decimal": float(value),
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def scan(s_values: list[int], K_values: list[int]) -> dict[str, object]:
    solver = ExactResolvent()
    rows = []
    overall = None
    failures = []
    for s in s_values:
        rank_worst = None
        for K in K_values:
            R = K - 1
            for B in range(1, s + 1):
                q = q_split(s, B)
                value = solver.g(s, K, R, B)
                target = q * (1 - q)
                ratio = value / target
                row = {
                    "context": [s, K, R, B],
                    "q": fraction_record(q),
                    "transformed_value": fraction_record(value),
                    "target_variance": fraction_record(target),
                    "ratio": fraction_record(ratio),
                    "margin_target_minus_value": fraction_record(target - value),
                }
                if rank_worst is None or ratio > rank_worst[0]:
                    rank_worst = (ratio, row)
                if overall is None or ratio > overall[0]:
                    overall = (ratio, row)
                if value > target:
                    failures.append(row)
        rows.append({"s": s, "worst": rank_worst[1]})
        print(json.dumps(rows[-1], sort_keys=True), flush=True)
    return {
        "rank_worst_rows": rows,
        "overall_worst": overall[1],
        "failure_count": len(failures),
        "first_failures": failures[:3],
        "memoized_contexts": solver.contexts,
        "deep_terms_visited": solver.deep_terms,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-values", type=int, nargs="+", required=True)
    parser.add_argument("--K-values", type=int, nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    result = scan(args.s_values, args.K_values)
    payload = {
        "claim_tested": "right-heavy K_reset W <= W",
        "finite_scope_warning": "Exact bounded survival proves no universal inequality.",
        "normalization": (
            "g=q*(I-D)^-1*J_can*W; transformed deep coefficient=rho*nu; "
            "transformed reset coefficient=(theta^2/Q)*(1-q_child)"
        ),
        "strict_phase": "P=s+K-R decreases on every retained deep child",
        "arithmetic": "fractions.Fraction exact grouped Cayley recurrence",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "parameters": {"s_values": args.s_values, "K_values": args.K_values},
        "elapsed_seconds": time.time() - started,
        "result": result,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "elapsed_seconds": payload["elapsed_seconds"],
        "overall_worst": result["overall_worst"],
        "failure_count": result["failure_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
