#!/usr/bin/env python3
"""Grouped independent attack on M76's eliminated inverse-q inequality.

The transformed value

    g(x)=q_x * [(I-D)^(-1) J_can h](x),  h=1/q,

satisfies ``g=jhat + Dhat g``.  Exact child-q cancellation gives

    Dhat(x,y)=rho_s(k,t) * nu_j,

while a canonical reset edge contributes its unnormalised flow energy
divided by the child split mass.  Root-composition and fixed-suffix sums are
evaluated by Cayley coefficients, without enumerating all compositions.

All calculations here use IEEE doubles and are finite falsifiers only.  A
reported value above one by a robust margin would refute the inequality;
values below one prove no universal statement.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import platform
import time
from pathlib import Path


E_MINUS_ONE = math.exp(-1.0)


def log_comb(n: int, k: int) -> float:
    if k < 0 or k > n:
        return -math.inf
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def comb_ratio(n1: int, k1: int, n2: int, k2: int) -> float:
    log_value = log_comb(n1, k1) - log_comb(n2, k2)
    if log_value == -math.inf:
        return 0.0
    return math.exp(log_value)


class GroupedResolvent:
    def __init__(self, s_max: int):
        self.s_max = s_max
        # v_a=e^{-a} a^{a-1}/a!.  All stationary composition sums acquire
        # one explicit factor e^{-1}; split ratios are unchanged.
        self.v = [0.0] + [
            math.exp((a - 1) * math.log(a) - math.lgamma(a + 1) - a)
            for a in range(1, s_max + 2)
        ]
        # coeff[a][p]=[z^a] V(z)^p, where V uses the scaled v_a.
        self.coeff = [[0.0] * (s_max + 1) for _ in range(s_max + 1)]
        self.coeff[0][0] = 1.0
        for a in range(1, s_max + 1):
            for p in range(1, a + 1):
                log_c = (
                    math.log(p)
                    + (a - p - 1) * math.log(a)
                    - math.lgamma(a - p + 1)
                    - a
                )
                self.coeff[a][p] = math.exp(log_c)
        self.contexts = 0
        self.max_group_mass_error = 0.0
        self.max_nu_error = 0.0
        self.max_mean_error = 0.0
        self.max_negative_roundoff = 0.0

    def q(self, s: int, B: int) -> float:
        return self.v[s + 1 - B] * self.v[B] / self.v[s + 1]

    def group_mass(self, s: int, k: int, t: int) -> float:
        a, p = s - t, k - 1
        if not (0 <= p <= a):
            return 0.0
        return (
            E_MINUS_ONE
            * self.v[t]
            * self.coeff[a][p]
            / (math.factorial(k) * self.v[s + 1])
        )

    def contextual_value(
        self, k: int, t: int, K: int | None, R: int | None, B: int
    ) -> float:
        if t < B:
            return 0.0
        if K is None:
            if t == B:
                return 1.0 if k == 1 else 0.0
            return self.v[t - B] * self.v[B] / self.v[t]
        assert R is not None
        if t == B:
            return K * comb_ratio(
                k + K - R - 2,
                K - R - 1,
                k + K - 1,
                K - 1,
            )
        local = self.v[t - B] * self.v[B] / self.v[t]
        log_bad = log_comb(K, R + 1) - log_comb(K + k, R + 1)
        one_minus_bad = -math.expm1(log_bad)
        return local * one_minus_bad

    def nu(self, K: int, R: int, k: int, j: int) -> float:
        return math.exp(
            log_comb(R + j, j)
            + log_comb(K - R - 1 + k - j, k - j)
            - log_comb(K + k, k)
        )

    @functools.lru_cache(maxsize=None)
    def groups(self, s: int):
        rows = []
        total = 0.0
        for k in range(1, s + 1):
            for t in range(1, s + 1):
                mass = self.group_mass(s, k, t)
                if mass:
                    rows.append((k, t, mass))
                    total += mass
        self.max_group_mass_error = max(self.max_group_mass_error, abs(total - 1.0))
        return tuple(rows)

    def tail_last_weights(self, total: int, parts: int):
        """Return (last, product-weight sum) for positive tail compositions."""
        if parts == 0:
            if total == 0:
                return ((0, 1.0),)
            return ()
        answer = []
        for last in range(1, total + 1):
            prefix_total = total - last
            prefix_parts = parts - 1
            coefficient = (
                self.coeff[prefix_total][prefix_parts]
                if 0 <= prefix_parts <= prefix_total
                else 0.0
            )
            if coefficient:
                answer.append((last, coefficient * self.v[last]))
        return tuple(answer)

    @functools.lru_cache(maxsize=None)
    def jhat(self, s: int, K: int | None, R: int | None, B: int):
        """Canonical reset contribution after h-transform, aggregated by child."""
        q_parent = self.q(s, B)
        result: dict[tuple[int, int, int, int], float] = {}
        # l is the number of suffix parts in a refined first-boundary edge;
        # its total root degree is l+1 and the reset mark is (l,l-1).
        for l in range(1, s):
            tail_parts = l - 1
            for A in range(1, s + 1):
                max_b = s - A - tail_parts
                if max_b < 1:
                    continue
                for b in range(1, max_b + 1):
                    tail_total = s - A - b
                    child_rank = A + b - 1
                    if child_rank < 2:
                        continue
                    q_child = self.v[A] * self.v[b] / self.v[A + b]
                    aggregate_energy = 0.0
                    if tail_parts == 0:
                        if tail_total != 0:
                            continue
                        tail_rows = ((b, 1.0),)
                    else:
                        tail_rows = tuple(
                            (last, self.v[b] * product)
                            for last, product in self.tail_last_weights(
                                tail_total, tail_parts
                            )
                        )
                    if tail_parts == 0:
                        # Include the distinguished first suffix part b.
                        tail_rows = ((b, self.v[b]),)
                    for last, suffix_product in tail_rows:
                        scalar = 0.0
                        for p in range(1, A + 1):
                            coefficient = self.coeff[A][p]
                            if not coefficient:
                                continue
                            h_value = self.contextual_value(
                                p + l, last, K, R, B
                            )
                            scalar += (
                                coefficient
                                * (h_value - q_parent)
                                / math.factorial(p + l)
                            )
                        aggregate_energy += (
                            E_MINUS_ONE
                            * suffix_product
                            / self.v[s + 1]
                            * math.factorial(l)
                            / self.v[A]
                            * scalar
                            * scalar
                        )
                    if aggregate_energy:
                        child = (child_rank, l, l - 1, b)
                        result[child] = result.get(child, 0.0) + aggregate_energy / q_child
        return tuple(sorted(result.items()))

    @functools.lru_cache(maxsize=None)
    def value(self, s: int, K: int | None, R: int | None, B: int) -> float:
        """Return g=q*(I-D)^-1 J h on a rank-descending DAG."""
        if s <= 1:
            return 0.0
        self.contexts += 1
        q_parent = self.q(s, B)
        # The contextual mean identity is an independent normalization check.
        mean = sum(
            mass * self.contextual_value(k, t, K, R, B)
            for k, t, mass in self.groups(s)
        )
        self.max_mean_error = max(self.max_mean_error, abs(mean - q_parent))
        answer = sum(weight for _, weight in self.jhat(s, K, R, B))
        for k, t, mass in self.groups(s):
            if t <= B or t - 1 < 2:
                continue
            if K is None:
                answer += mass * self.value(t - 1, None, None, B)
                continue
            assert R is not None
            nu_sum = 0.0
            for j in range(1, k + 1):
                coefficient = self.nu(K, R, k, j)
                nu_sum += coefficient
                if coefficient:
                    answer += mass * coefficient * self.value(
                        t - 1, K + k, R + j, B
                    )
            expected = 1.0 - self.nu(K, R, k, 0)
            self.max_nu_error = max(self.max_nu_error, abs(nu_sum - expected))
        if answer < 0:
            self.max_negative_roundoff = max(self.max_negative_roundoff, -answer)
        return answer

    @functools.lru_cache(maxsize=None)
    def row_value(self, s: int, K: int | None, R: int | None, B: int) -> float:
        """Return [(I-D)^(-1)J]1 for the active reset kernel."""
        if s <= 1:
            return 0.0
        q_parent = self.q(s, B)
        answer = 0.0
        for child, transformed_weight in self.jhat(s, K, R, B):
            q_child = self.q(child[0], child[3])
            answer += transformed_weight * q_child / q_parent
        for k, t, mass in self.groups(s):
            if t <= B or t - 1 < 2:
                continue
            q_child = self.q(t - 1, B)
            if K is None:
                answer += (
                    mass
                    * q_child
                    / q_parent
                    * self.row_value(t - 1, None, None, B)
                )
                continue
            assert R is not None
            for j in range(1, k + 1):
                coefficient = self.nu(K, R, k, j)
                if coefficient:
                    answer += (
                        mass
                        * q_child
                        * coefficient
                        / q_parent
                        * self.row_value(t - 1, K + k, R + j, B)
                    )
        return answer

    def raw_active_row(self, s: int, K: int | None, R: int | None, B: int):
        """Return (D1,J1,D1+J1) with inactive rank <=1 children removed."""
        q_parent = self.q(s, B)
        reset = 0.0
        for child, transformed_weight in self.jhat(s, K, R, B):
            reset += transformed_weight * self.q(child[0], child[3]) / q_parent
        deep = 0.0
        for k, t, mass in self.groups(s):
            if t <= B or t - 1 < 2:
                continue
            q_child = self.q(t - 1, B)
            if K is None:
                deep += mass * q_child / q_parent
            else:
                assert R is not None
                deep += mass * q_child / q_parent * sum(
                    self.nu(K, R, k, j) for j in range(1, k + 1)
                )
        return deep, reset, deep + reset


def scan(s_max: int, k_values: list[int], include_infinite: bool) -> dict:
    solver = GroupedResolvent(s_max)
    records = []
    global_worst = None
    global_worst_row_sum = None
    global_worst_raw_row = None
    global_worst_variance_ratio = None
    for s in range(2, s_max + 1):
        contexts = [(K, K - 1) for K in k_values]
        if include_infinite:
            contexts.append((None, None))
        rank_worst = None
        rank_worst_row_sum = None
        rank_worst_raw_row = None
        rank_worst_variance_ratio = None
        for K, R in contexts:
            for B in range(1, s + 1):
                value = solver.value(s, K, R, B)
                raw_deep, raw_reset, raw_row = solver.raw_active_row(
                    s, K, R, B
                )
                row = {
                    "s": s,
                    "K": "infinity" if K is None else K,
                    "R": "infinity-1" if R is None else R,
                    "B": B,
                    "ratio": value,
                    "direct_jhat": sum(
                        weight for _, weight in solver.jhat(s, K, R, B)
                    ),
                    "eliminated_reset_row_sum": solver.row_value(s, K, R, B),
                    "raw_active_deep_row_sum": raw_deep,
                    "raw_active_reset_row_sum": raw_reset,
                    "raw_active_total_row_sum": raw_row,
                    "row_sum_over_one_minus_q": (
                        solver.row_value(s, K, R, B) / (1.0 - solver.q(s, B))
                        if solver.q(s, B) < 1.0
                        else 0.0
                    ),
                }
                if rank_worst is None or value > rank_worst["ratio"]:
                    rank_worst = row
                if (
                    rank_worst_row_sum is None
                    or row["eliminated_reset_row_sum"]
                    > rank_worst_row_sum["eliminated_reset_row_sum"]
                ):
                    rank_worst_row_sum = row
                if global_worst is None or value > global_worst["ratio"]:
                    global_worst = row
                if (
                    global_worst_row_sum is None
                    or row["eliminated_reset_row_sum"]
                    > global_worst_row_sum["eliminated_reset_row_sum"]
                ):
                    global_worst_row_sum = row
                if (
                    rank_worst_raw_row is None
                    or raw_row > rank_worst_raw_row["raw_active_total_row_sum"]
                ):
                    rank_worst_raw_row = row
                if (
                    global_worst_raw_row is None
                    or raw_row > global_worst_raw_row["raw_active_total_row_sum"]
                ):
                    global_worst_raw_row = row
                if (
                    rank_worst_variance_ratio is None
                    or row["row_sum_over_one_minus_q"]
                    > rank_worst_variance_ratio["row_sum_over_one_minus_q"]
                ):
                    rank_worst_variance_ratio = row
                if (
                    global_worst_variance_ratio is None
                    or row["row_sum_over_one_minus_q"]
                    > global_worst_variance_ratio["row_sum_over_one_minus_q"]
                ):
                    global_worst_variance_ratio = row
        record = {
            "s": s,
            "worst_inverse_q_ratio": rank_worst,
            "worst_eliminated_reset_row_sum": rank_worst_row_sum,
            "worst_raw_active_row_sum": rank_worst_raw_row,
            "worst_row_sum_over_one_minus_q": rank_worst_variance_ratio,
        }
        records.append(record)
        print(json.dumps(record, sort_keys=True), flush=True)
    return {
        "records": records,
        "global_worst": global_worst,
        "global_worst_eliminated_reset_row_sum": global_worst_row_sum,
        "global_worst_raw_active_row_sum": global_worst_raw_row,
        "global_worst_row_sum_over_one_minus_q": global_worst_variance_ratio,
        "diagnostics": {
            "memoized_contexts": solver.contexts,
            "max_group_mass_error": solver.max_group_mass_error,
            "max_nu_sum_error": solver.max_nu_error,
            "max_contextual_mean_error": solver.max_mean_error,
            "max_negative_roundoff": solver.max_negative_roundoff,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=14)
    parser.add_argument("--K-values", type=int, nargs="*", default=[1, 2, 4, 16, 4096])
    parser.add_argument("--no-infinite", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    result = scan(args.s_max, args.K_values, not args.no_infinite)
    payload = {
        "claim_tested": "M76 deep-eliminated inverse-split-mass inequality",
        "status_rule": "ratio>1 by robust numerical margin refutes; ratio<=1 is finite evidence only",
        "normalization": "g=q*(I-D)^-1*J*(1/q); Dhat=rho_group*nu; Jhat=edge_energy/q_child",
        "arithmetic": "IEEE-754 binary64 grouped Cayley coefficients",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "parameters": {
            "s_max": args.s_max,
            "K_values": args.K_values,
            "include_infinite_right_heavy_limit": not args.no_infinite,
        },
        "elapsed_seconds": time.time() - started,
        "result": result,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "elapsed_seconds": payload["elapsed_seconds"],
        "global_worst": result["global_worst"],
        "diagnostics": result["diagnostics"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
