#!/usr/bin/env python3
"""Exact audit of the R2 branch law and its two-sided dense approximation.

Convention: ``compose(p,q)`` is p after q, so the rightmost displayed factor
acts first.  This script uses only Python exact integers/Fractions for claims;
floating-point fields in the JSON are display-only renderings of exact values.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import random
import subprocess
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence


Perm = tuple[int, ...]


def identity(n: int) -> Perm:
    return tuple(range(n))


def compose(left: Perm, right: Perm) -> Perm:
    return tuple(left[right[x]] for x in range(len(left)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def transposition(n: int, i: int, j: int) -> Perm:
    p = list(range(n))
    p[i], p[j] = p[j], p[i]
    return tuple(p)


def all_transpositions(n: int) -> tuple[Perm, ...]:
    return tuple(transposition(n, i, j) for i in range(n) for j in range(i + 1, n))


def old_transpositions(n: int) -> tuple[Perm, ...]:
    return tuple(
        transposition(n, i, j)
        for i in range(n - 1)
        for j in range(i + 1, n - 1)
    )


def star_transpositions(n: int) -> tuple[Perm, ...]:
    return tuple(transposition(n, i, n - 1) for i in range(n - 1))


def h_elements(n: int) -> tuple[Perm, ...]:
    return tuple(tuple(p) + (n - 1,) for p in itertools.permutations(range(n - 1)))


def evaluate(word: Sequence[Perm], n: int) -> Perm:
    out = identity(n)
    for factor in word:
        out = compose(out, factor)
    return out


def endpoint_tables(n: int, alphabet: Sequence[Perm], max_length: int) -> list[Counter[Perm]]:
    tables: list[Counter[Perm]] = [Counter({identity(n): 1})]
    for _ in range(max_length):
        following: Counter[Perm] = Counter()
        for endpoint, count in tables[-1].items():
            for factor in alphabet:
                following[compose(endpoint, factor)] += count
        tables.append(following)
    return tables


def cycle_count(p: Perm) -> int:
    seen = [False] * len(p)
    answer = 0
    for start in range(len(p)):
        if seen[start]:
            continue
        answer += 1
        x = start
        while not seen[x]:
            seen[x] = True
            x = p[x]
    return answer


def sign(p: Perm) -> int:
    return -1 if (len(p) - cycle_count(p)) % 2 else 1


def feasible_full(n: int, length: int, g: Perm) -> bool:
    return length >= n - cycle_count(g) and sign(g) == (-1) ** length


def token_tables(n: int, max_length: int) -> tuple[list[int], list[int]]:
    """Counts taking pivot/lower token to the pivot under applied-order stars."""

    pivot_to_pivot = [1]
    lower_to_pivot = [0]
    for _ in range(max_length):
        pivot_to_pivot.append((n - 1) * lower_to_pivot[-1])
        lower_to_pivot.append(pivot_to_pivot[-2] + (n - 2) * lower_to_pivot[-1])
    return pivot_to_pivot, lower_to_pivot


def token_count(
    n: int,
    length: int,
    start: int,
    token_data: tuple[list[int], list[int]],
) -> int:
    u, v = token_data
    return u[length] if start == n - 1 else v[length]


def apply_star_to_token(n: int, token: int, lower: int) -> int:
    if token == n - 1:
        return lower
    if token == lower:
        return n - 1
    return token


def sample_token_conditioned_star_word(
    n: int,
    length: int,
    start: int,
    rng: random.Random,
    token_data: tuple[list[int], list[int]],
) -> tuple[Perm, ...]:
    """Uniform displayed star word q conditioned on q(start)=N.

    Star factors act on the token in reverse displayed order.  We sample that
    applied order by completion counts and reverse it at the end.
    """

    if token_count(n, length, start, token_data) == 0:
        raise ValueError("empty token bridge")
    token = start
    applied_lowers: list[int] = []
    for remaining in range(length, 0, -1):
        choices: list[tuple[int, int, int]] = []
        total = 0
        for lower in range(n - 1):
            next_token = apply_star_to_token(n, token, lower)
            weight = token_count(n, remaining - 1, next_token, token_data)
            if weight:
                choices.append((lower, next_token, weight))
                total += weight
        assert total == token_count(n, remaining, token, token_data)
        draw = rng.randrange(total)
        cumulative = 0
        for lower, next_token, weight in choices:
            cumulative += weight
            if draw < cumulative:
                applied_lowers.append(lower)
                token = next_token
                break
        else:  # pragma: no cover
            raise AssertionError("draw outside total")
    assert token == n - 1
    return tuple(
        transposition(n, lower, n - 1) for lower in reversed(applied_lowers)
    )


def exact_branch_weights(
    n: int,
    length: int,
    g: Perm,
    old_dp: Sequence[Counter[Perm]],
    star_dp: Sequence[Counter[Perm]],
    hs: Sequence[Perm],
) -> Counter[tuple[int, Perm]]:
    out: Counter[tuple[int, Perm]] = Counter()
    for k in range(length + 1):
        s = length - k
        choose = math.comb(length, k)
        for h in hs:
            q = compose(inverse(h), g)
            weight = choose * old_dp[s][h] * star_dp[k][q]
            if weight:
                out[(k, h)] = weight
    return out


def approximate_branch_weights_scaled(
    n: int,
    length: int,
    g: Perm,
    old_dp: Sequence[Counter[Perm]],
    star_dp: Sequence[Counter[Perm]],
    hs: Sequence[Perm],
) -> Counter[tuple[int, Perm]]:
    """Two-sided flattened weights, all scaled by N!/2.

    Old-long: N*binom*d^s*B(q).
    Star-long: binom*A(h)*b^k.
    """

    if n == 2:
        # H=S_1 and the only feasible branch has k=L,h=e.
        exact = exact_branch_weights(n, length, g, old_dp, star_dp, hs)
        return exact
    d = len(old_transpositions(n))
    b = n - 1
    out: Counter[tuple[int, Perm]] = Counter()
    for k in range(length + 1):
        s = length - k
        choose = math.comb(length, k)
        if s >= k:
            old_flat = d**s
            for h in hs:
                q = compose(inverse(h), g)
                weight = n * choose * old_flat * star_dp[k][q]
                if weight:
                    out[(k, h)] = weight
        else:
            star_flat = b**k
            for h in hs:
                weight = choose * old_dp[s][h] * star_flat
                if weight:
                    out[(k, h)] = weight
    return out


def exact_tv(left: Counter, right: Counter) -> Fraction:
    left_total = sum(left.values())
    right_total = sum(right.values())
    if left_total == 0 or right_total == 0:
        raise ValueError("TV requires nonempty distributions")
    keys = set(left) | set(right)
    return sum(
        (abs(Fraction(left[key], left_total) - Fraction(right[key], right_total)) for key in keys),
        Fraction(0),
    ) / 2


def old_pointwise_bound(rank: int, length: int) -> Fraction:
    """Relative error from parity-uniform for all-transposition walk."""

    if rank <= 2:
        return Fraction(0)
    prefactor = Fraction(math.factorial(rank) - 2, 2)
    if rank == 3:
        return prefactor if length == 0 else Fraction(0)
    rho = Fraction(rank - 3, rank - 1)
    return prefactor * rho**length


def star_pointwise_bound(rank: int, length: int) -> Fraction:
    """Relative error from parity-uniform for nonlazy star walk."""

    if rank <= 2:
        return Fraction(0)
    prefactor = Fraction(math.factorial(rank) - 2, 2)
    rho = Fraction(rank - 2, rank - 1)
    return prefactor * rho**length


def combined_normalized_bound(n: int, length: int) -> Fraction | None:
    if n == 2:
        return Fraction(0)
    old_minimum = (length + 1) // 2
    # k>s is nonempty only for k=floor(L/2)+1,...,L.
    star_minimum = length // 2 + 1
    delta = max(
        old_pointwise_bound(n - 1, old_minimum),
        star_pointwise_bound(n, star_minimum),
    )
    if delta >= 1:
        return None
    return delta / (1 - delta)


def exact_relative_endpoint_error(
    rank: int,
    length: int,
    dp: Counter[Perm],
    degree: int,
) -> Fraction:
    if rank <= 2:
        return Fraction(0)
    flat = Fraction(2 * degree**length, math.factorial(rank))
    worst = Fraction(0)
    for endpoint in itertools.permutations(range(rank)):
        endpoint = tuple(endpoint)
        if sign(endpoint) != (-1) ** length:
            assert dp[endpoint] == 0
            continue
        worst = max(worst, abs(Fraction(dp[endpoint], 1) / flat - 1))
    return worst


def sample_approximate_branch(
    n: int,
    length: int,
    g: Perm,
    rng: random.Random,
) -> tuple[int, Perm]:
    """Sample the two-sided flattened branch without enumerating H."""

    if not feasible_full(n, length, g):
        raise ValueError("empty external endpoint fiber")
    if n == 2:
        return length, identity(2)

    old_alphabet = old_transpositions(n)
    d = len(old_alphabet)
    b = n - 1
    token_data = token_tables(n, length)
    a = inverse(g)[n - 1]
    marginal: list[int] = []
    for k in range(length + 1):
        s = length - k
        choose = math.comb(length, k)
        if s >= k:
            star_coset_mass = token_count(n, k, a, token_data)
            marginal.append(n * choose * d**s * star_coset_mass)
        else:
            marginal.append(choose * d**s * b**k)
    total = sum(marginal)
    if total == 0:
        raise AssertionError("flattened branch unexpectedly empty")
    draw = rng.randrange(total)
    cumulative = 0
    k = 0
    for candidate, weight in enumerate(marginal):
        cumulative += weight
        if draw < cumulative:
            k = candidate
            break
    s = length - k
    if s >= k:
        star_word = sample_token_conditioned_star_word(n, k, a, rng, token_data)
        q = evaluate(star_word, n)
        assert q[a] == n - 1
        h = compose(g, inverse(q))
        assert h[n - 1] == n - 1
        return k, h

    old_word = tuple(rng.choice(old_alphabet) for _ in range(s))
    h = evaluate(old_word, n)
    assert h[n - 1] == n - 1
    return k, h


def partition_numbers(maximum: int) -> list[int]:
    p = [0] * (maximum + 1)
    p[0] = 1
    for part in range(1, maximum + 1):
        for total in range(part, maximum + 1):
            p[total] += p[total - part]
    return p


def frac_record(value: Fraction) -> dict[str, object]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "float": float(value),
    }


def commit(repo: Path) -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()


def audit_small(max_n: int, max_length: int) -> dict[str, object]:
    coefficient_checks = 0
    token_checks = 0
    feasibility_checks = 0
    approximation_cases = 0
    bound_checks = 0
    worst_small_tv = Fraction(0)
    rng = random.Random(20260901)
    sampler_smoke_checks = 0

    for n in range(2, max_n + 1):
        full = all_transpositions(n)
        old = old_transpositions(n)
        star = star_transpositions(n)
        hs = h_elements(n)
        endpoints = tuple(tuple(p) for p in itertools.permutations(range(n)))
        full_dp = endpoint_tables(n, full, max_length)
        old_dp = endpoint_tables(n, old, max_length)
        star_dp = endpoint_tables(n, star, max_length)
        tokens = token_tables(n, max_length)

        for k in range(max_length + 1):
            for start in range(n):
                direct = sum(count for q, count in star_dp[k].items() if q[start] == n - 1)
                assert direct == token_count(n, k, start, tokens)
                token_checks += 1
                if direct:
                    for _ in range(3):
                        word = sample_token_conditioned_star_word(n, k, start, rng, tokens)
                        assert evaluate(word, n)[start] == n - 1
                        sampler_smoke_checks += 1

        for length in range(max_length + 1):
            for g in endpoints:
                feasible = feasible_full(n, length, g)
                assert (full_dp[length][g] > 0) == feasible
                feasibility_checks += 1
                exact = exact_branch_weights(n, length, g, old_dp, star_dp, hs)
                assert sum(exact.values()) == full_dp[length][g]
                coefficient_checks += 1
                if not feasible:
                    assert not exact
                    continue
                approx = approximate_branch_weights_scaled(n, length, g, old_dp, star_dp, hs)
                tv = exact_tv(exact, approx)
                worst_small_tv = max(worst_small_tv, tv)
                approximation_cases += 1
                bound = combined_normalized_bound(n, length)
                if bound is not None:
                    assert tv <= bound
                    bound_checks += 1
                for _ in range(3):
                    sampled = sample_approximate_branch(n, length, g, rng)
                    assert approx[sampled] > 0
                    sampler_smoke_checks += 1

            if n >= 3:
                old_rank = n - 1
                old_degree = len(old)
                # Restrict embedded endpoints to S_(N-1), then drop pivot.
                old_counter_small: Counter[Perm] = Counter()
                for h, value in old_dp[length].items():
                    old_counter_small[h[:-1]] = value
                old_error = exact_relative_endpoint_error(
                    old_rank, length, old_counter_small, old_degree
                )
                assert old_error <= old_pointwise_bound(old_rank, length)
                star_error = exact_relative_endpoint_error(n, length, star_dp[length], len(star))
                assert star_error <= star_pointwise_bound(n, length)

    return {
        "max_N": max_n,
        "max_L": max_length,
        "coefficient_checks": coefficient_checks,
        "token_coset_count_checks": token_checks,
        "feasibility_checks": feasibility_checks,
        "approximation_cases": approximation_cases,
        "spectral_normalization_bound_checks": bound_checks,
        "sampler_smoke_checks": sampler_smoke_checks,
        "worst_small_exact_tv": frac_record(worst_small_tv),
        "all_checks_passed": True,
    }


def audit_dense(n_values: Iterable[int]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for n in n_values:
        length = 2 * n**3
        full = all_transpositions(n)
        old = old_transpositions(n)
        star = star_transpositions(n)
        hs = h_elements(n)
        endpoints = tuple(tuple(p) for p in itertools.permutations(range(n)))
        full_dp = endpoint_tables(n, full, length)
        old_dp = endpoint_tables(n, old, length)
        star_dp = endpoint_tables(n, star, length)
        max_tv = Fraction(0)
        max_endpoint: Perm | None = None
        checked = 0
        for g in endpoints:
            if not feasible_full(n, length, g):
                continue
            exact = exact_branch_weights(n, length, g, old_dp, star_dp, hs)
            assert sum(exact.values()) == full_dp[length][g]
            approx = approximate_branch_weights_scaled(n, length, g, old_dp, star_dp, hs)
            tv = exact_tv(exact, approx)
            if tv > max_tv:
                max_tv = tv
                max_endpoint = g
            checked += 1
        theorem_bound = combined_normalized_bound(n, length)
        assert theorem_bound is not None and max_tv <= theorem_bound
        simple_negligible_bound = 2 * math.exp(-(n**2) / 2)
        assert float(theorem_bound) <= simple_negligible_bound
        rows.append(
            {
                "N": n,
                "L": length,
                "feasible_endpoints_checked": checked,
                "maximum_exact_tv": frac_record(max_tv),
                "maximum_endpoint_one_based": (
                    [x + 1 for x in max_endpoint] if max_endpoint is not None else None
                ),
                "pointwise_theorem_bound": frac_record(theorem_bound),
                "simple_bound_2exp_minus_N2_over_2": simple_negligible_bound,
                "all_checks_passed": True,
            }
        )
    return rows


def audit_exact_low_rank(max_length: int) -> dict[str, object]:
    """Check the special exact positive k-marginals for N=2,3,4.

    For N=3 every parity class of H=S_2 is a singleton.  For N=4 the
    all-transposition walk on H=S_3 is parity-uniform after every positive
    number of steps; only s=0 is treated as its forced h=e branch.
    """

    checks = 0
    for n in (2, 3, 4):
        full = all_transpositions(n)
        old = old_transpositions(n)
        star = star_transpositions(n)
        hs = h_elements(n)
        endpoints = tuple(tuple(p) for p in itertools.permutations(range(n)))
        full_dp = endpoint_tables(n, full, max_length)
        old_dp = endpoint_tables(n, old, max_length)
        star_dp = endpoint_tables(n, star, max_length)
        tokens = token_tables(n, max_length)
        d = len(old)
        for length in range(max_length + 1):
            for g in endpoints:
                if not feasible_full(n, length, g):
                    continue
                exact = exact_branch_weights(n, length, g, old_dp, star_dp, hs)
                exact_marginal = [
                    sum(weight for (branch_k, _), weight in exact.items() if branch_k == k)
                    for k in range(length + 1)
                ]
                if n == 2:
                    compressed = [0] * length + [1]
                    assert exact_marginal == compressed
                else:
                    a = inverse(g)[n - 1]
                    compressed_scaled: list[int] = []
                    for k in range(length + 1):
                        s = length - k
                        choose = math.comb(length, k)
                        if n == 3:
                            compressed_scaled.append(
                                choose * d**s * token_count(n, k, a, tokens)
                            )
                        elif s >= 1:
                            # Three times the exact mass: 2/|S_3|=1/3.
                            compressed_scaled.append(
                                choose * d**s * token_count(n, k, a, tokens)
                            )
                        else:
                            # The forced s=0,h=e branch, on the same x3 scale.
                            compressed_scaled.append(3 * star_dp[k][g])
                    if n == 3:
                        assert compressed_scaled == exact_marginal
                    else:
                        assert compressed_scaled == [3 * value for value in exact_marginal]
                assert sum(exact_marginal) == full_dp[length][g]
                checks += 1
    return {
        "ranks": [2, 3, 4],
        "max_L": max_length,
        "exact_positive_k_marginal_checks": checks,
        "all_checks_passed": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    parser.add_argument("--max-small-n", type=int, default=5)
    parser.add_argument("--max-small-length", type=int, default=8)
    parser.add_argument("--dense-n", type=int, nargs="*", default=[4, 5])
    args = parser.parse_args()
    started = time.time()
    repo = Path(__file__).resolve().parents[4]

    small = audit_small(args.max_small_n, args.max_small_length)
    dense = audit_dense(args.dense_n)
    exact_low_rank = audit_exact_low_rank(args.max_small_length)
    p = partition_numbers(100)
    state_counts = []
    for n in (5, 10, 20, 50, 100):
        state_counts.append(
            {
                "N": n,
                "H_cycle_types_p_N_minus_1": p[n - 1],
                "pointed_types_sum_p_0_to_N_minus_1": sum(p[:n]),
                "rectangular_type_cell_inventory": p[n - 1] * sum(p[:n]),
            }
        )

    result = {
        "claim": "positive exact type-cell compression and polynomial two-sided dense branch sampler",
        "convention": "(alpha beta)(x)=alpha(beta(x)); rightmost displayed factor acts first",
        "repository_commit": commit(repo),
        "python_version": platform.python_version(),
        "nonstandard_dependencies": [],
        "seed": 20260901,
        "small_exact_audit": small,
        "exact_low_rank_audit": exact_low_rank,
        "dense_exact_audit": dense,
        "type_cell_state_counts": state_counts,
        "elapsed_seconds": time.time() - started,
        "all_checks_passed": small["all_checks_passed"] and exact_low_rank[
            "all_checks_passed"
        ] and all(
            row["all_checks_passed"] for row in dense
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
