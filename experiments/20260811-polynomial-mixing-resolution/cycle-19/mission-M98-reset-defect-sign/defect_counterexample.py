#!/usr/bin/env python3
"""Independent exact certificate for the M98 reset-defect counterfamily.

The script uses every attachment rank ``j=1,...,k``.  It imports no
predecessor experiment module.  All signs and limiting identities use
``fractions.Fraction`` arithmetic; decimals are presentation only.
"""

from __future__ import annotations

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
    return q_split(t - 1, B) * (
        1 - comb_ratio(K, R + 1, K + k, R + 1)
    )


def attachment_probability(K: int, R: int, k: int, j: int) -> Fraction:
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
        raise AssertionError(("stationary normalization", s, total))
    return tuple(rows)


@functools.lru_cache(maxsize=None)
def basin_coefficient(A: int, ell: int) -> Fraction:
    """L_(A,ell)=sum_p [z^A]T^p/(p+ell)! exactly."""
    return sum(
        (cayley(A, p) / math.factorial(p + ell) for p in range(1, A + 1)),
        Fraction(),
    )


@functools.lru_cache(maxsize=None)
def reset_energy(
    s: int, K: int, R: int, B: int, weighted: bool = True
) -> Fraction:
    """Return canonical reset energy, with optional ``1-q_child`` reward."""
    q_parent = q_split(s, B)
    answer = Fraction(0)
    scalar_cache: dict[tuple[int, int, int], Fraction] = {}

    def scalar(A: int, ell: int, last: int) -> Fraction:
        key = (A, ell, last)
        if key not in scalar_cache:
            scalar_cache[key] = sum(
                (
                    cayley(A, p)
                    * (contextual_value(p + ell, last, K, R, B) - q_parent)
                    / math.factorial(p + ell)
                    for p in range(1, A + 1)
                ),
                Fraction(),
            )
        return scalar_cache[key]

    # A refined endpoint is (A,b,middle...,last), with ell suffix parts.
    for ell in range(1, s):
        middle_parts = ell - 1
        for A in range(1, s + 1):
            for b in range(1, s - A - middle_parts + 1):
                middle_and_last_total = s - A - b
                child_rank = A + b - 1
                if child_rank < 2:
                    continue
                if middle_parts == 0:
                    tail_rows = ((b, w(b)),) if middle_and_last_total == 0 else ()
                else:
                    tail_rows = tuple(
                        (
                            last,
                            w(b)
                            * cayley(middle_and_last_total - last, middle_parts - 1)
                            * w(last),
                        )
                        for last in range(1, middle_and_last_total + 1)
                        if cayley(middle_and_last_total - last, middle_parts - 1)
                    )
                for last, suffix_weight in tail_rows:
                    current = scalar(A, ell, last)
                    energy = (
                        suffix_weight
                        * math.factorial(ell)
                        * current
                        * current
                        / (w(A) * w(s + 1))
                    )
                    answer += energy * (
                        (1 - q_split(child_rank, b)) if weighted else 1
                    )
    return answer


def U(s: int, K: int, R: int, B: int) -> Fraction:
    q = q_split(s, B)
    return q * (1 - q) * Fraction(K, R + 1)


def deep_U(s: int, K: int, R: int, B: int) -> Fraction:
    answer = Fraction(0)
    for k, t, mass in groups(s):
        if t <= B or t - 1 < 2:
            continue
        for j in range(1, k + 1):
            probability = attachment_probability(K, R, k, j)
            child = (t - 1, K + k, R + j, B)
            answer += mass * probability * U(*child)
    return answer


def defect(s: int, K: int, R: int, B: int) -> Fraction:
    return U(s, K, R, B) - reset_energy(s, K, R, B) - deep_U(s, K, R, B)


@functools.lru_cache(maxsize=None)
def transformed_children(
    s: int, K: int, R: int, B: int
) -> tuple[tuple[Fraction, tuple[int, int, int, int]], ...]:
    rows = []
    parent_phase = s + K - R
    for k, t, mass in groups(s):
        if t <= B or t - 1 < 2:
            continue
        for j in range(1, k + 1):
            probability = attachment_probability(K, R, k, j)
            if not probability:
                continue
            child = (t - 1, K + k, R + j, B)
            if child[0] + child[1] - child[2] >= parent_phase:
                raise AssertionError(("strict phase", (s, K, R, B), child))
            rows.append((mass * probability, child))
    return tuple(rows)


@functools.lru_cache(maxsize=None)
def weighted_resolvent(s: int, K: int, R: int, B: int) -> Fraction:
    if s <= 1:
        return Fraction(0)
    return reset_energy(s, K, R, B, True) + sum(
        (
            mass * weighted_resolvent(*child)
            for mass, child in transformed_children(s, K, R, B)
        ),
        Fraction(),
    )


@functools.lru_cache(maxsize=None)
def unweighted_resolvent(s: int, K: int, R: int, B: int) -> Fraction:
    if s <= 1:
        return Fraction(0)
    return reset_energy(s, K, R, B, False) + sum(
        (
            mass * unweighted_resolvent(*child)
            for mass, child in transformed_children(s, K, R, B)
        ),
        Fraction(),
    )


def limiting_root_mean(s: int, B: int, k: int, t: int) -> Fraction:
    if t < B:
        return Fraction(0)
    if t == B:
        return Fraction(int(k == 1))
    return q_split(t - 1, B)


def limiting_energy_coefficients(s: int) -> tuple[Fraction, ...]:
    """Coefficient e_(s,t) of (H_infty(t)-q)^2 in reset energy."""
    answer = [Fraction(0) for _ in range(s + 1)]
    for ell in range(1, s):
        middle_parts = ell - 1
        for A in range(1, s + 1):
            L = basin_coefficient(A, ell)
            for b in range(1, s - A - middle_parts + 1):
                middle_and_last_total = s - A - b
                child_rank = A + b - 1
                if child_rank < 2:
                    continue
                if middle_parts == 0:
                    tail_rows = ((b, w(b)),) if middle_and_last_total == 0 else ()
                else:
                    tail_rows = tuple(
                        (
                            last,
                            w(b)
                            * cayley(middle_and_last_total - last, middle_parts - 1)
                            * w(last),
                        )
                        for last in range(1, middle_and_last_total + 1)
                        if cayley(middle_and_last_total - last, middle_parts - 1)
                    )
                for last, suffix_weight in tail_rows:
                    answer[last] += (
                        suffix_weight
                        * math.factorial(ell)
                        * L
                        * L
                        / (w(A) * w(s + 1))
                        * (1 - q_split(child_rank, b))
                    )
    return tuple(answer)


def limiting_decomposition(s: int, B: int) -> dict[str, object]:
    q = q_split(s, B)
    masses = [Fraction(0) for _ in range(s + 1)]
    root_means: list[Fraction | None] = [None for _ in range(s + 1)]
    for k, t, mass in groups(s):
        masses[t] += mass
        h = limiting_root_mean(s, B, k, t)
        if root_means[t] is None:
            root_means[t] = h
        elif root_means[t] != h:
            # The only possible exceptional terminal value is the unary
            # composition t=s=B, whose last-part fibre is itself unary.
            raise AssertionError(("last-part mean not constant", s, B, k, t))
    energy = limiting_energy_coefficients(s)
    rows = []
    total = Fraction(0)
    variance = Fraction(0)
    reset = Fraction(0)
    for t in range(1, s + 1):
        h = root_means[t]
        if h is None:
            raise AssertionError(("missing last part", s, t))
        square = (h - q) ** 2
        contribution = (masses[t] - energy[t]) * square
        variance += masses[t] * square
        reset += energy[t] * square
        total += contribution
        rows.append({
            "last_part": t,
            "mass": record(masses[t]),
            "reset_energy_coefficient": record(energy[t]),
            "coefficient_mass_minus_energy": record(masses[t] - energy[t]),
            "limiting_root_mean": record(h),
            "square": record(square),
            "defect_contribution": record(contribution),
        })

    deep = sum(
        (
            mass * q_split(t - 1, B) * (1 - q_split(t - 1, B))
            for _, t, mass in groups(s)
            if t > B
        ),
        Fraction(),
    )
    if q * (1 - q) - deep != variance:
        raise AssertionError(("law of total variance", s, B))
    if total != variance - reset:
        raise AssertionError(("coefficient decomposition", s, B))
    return {
        "q": record(q),
        "U_limit": record(q * (1 - q)),
        "deep_U_limit": record(deep),
        "variance_limit": record(variance),
        "reset_energy_limit": record(reset),
        "defect_limit": record(total),
        "normalized_defect_limit": record(total / (q * (1 - q))),
        "last_part_rows": rows,
    }


def record(value: Fraction) -> dict[str, object]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


def cleared_denominator(K: int, s: int) -> int:
    """Positive K-dependent denominator clearing every right-heavy term."""
    answer = 1
    for i in range(1, s + 1):
        answer *= (K + i) ** 2
    return answer


def newton_tail_certificate(s: int, B: int, K0: int) -> dict[str, object]:
    """Certify ``defect(s,K,K-1,B)<0`` for every integer ``K>=K0``.

    Analytically, multiplication by ``prod_(i=1)^s(K+i)^2`` turns the
    right-heavy defect into a polynomial of degree at most ``2s``.  We
    record its exact Newton coefficients at ``K0``.  If they are all
    negative, the binomial-series expansion is negative at every
    nonnegative integer displacement.
    """
    values = [
        defect(s, K, K - 1, B) * cleared_denominator(K, s)
        for K in range(K0, K0 + 2 * s + 2)
    ]
    rows = []
    current = values
    for order in range(2 * s + 2):
        rows.append(current[0])
        current = [current[i + 1] - current[i] for i in range(len(current) - 1)]
    if rows[-1] != 0:
        raise AssertionError(("degree bound audit", rows[-1]))
    if any(value >= 0 for value in rows[:-1]):
        raise AssertionError("Newton coefficients are not all negative")
    return {
        "K0": K0,
        "clearing_factor": "product_(i=1)^s (K+i)^2",
        "polynomial_degree_bound": 2 * s,
        "degree_bound_check_delta_order_2s_plus_1": record(rows[-1]),
        "all_orders_0_through_2s_strictly_negative": True,
        "newton_coefficients": [
            {"order": order, "value": record(value)}
            for order, value in enumerate(rows[:-1])
        ],
        "conclusion": (
            "For K=K0+n, n>=0 integer, the cleared numerator equals "
            "sum_order Delta^order P(K0) binom(n,order)<0."
        ),
    }


def main() -> None:
    started = time.time()
    s, B = 16, 4
    finite_rows = []
    for K in (2, 32, 709, 710, 1024):
        x = (s, K, K - 1, B)
        value = defect(*x)
        finite_rows.append({
            "context": list(x),
            "U": record(U(*x)),
            "reset_energy": record(reset_energy(*x)),
            "deep_U": record(deep_U(*x)),
            "defect": record(value),
            "normalized_defect": record(value / U(*x)),
            "sign": (value > 0) - (value < 0),
        })

    limiting = limiting_decomposition(s, B)
    tail = newton_tail_certificate(s, B, 710)
    witness = (s, 710, 709, B)
    witness_target = q_split(s, B) * (1 - q_split(s, B))
    weighted_full = weighted_resolvent(*witness)
    unweighted_full = unweighted_resolvent(*witness)
    witness_local = defect(*witness)
    witness_first_layer = sum(
        (mass * defect(*child) for mass, child in transformed_children(*witness)),
        Fraction(),
    )
    fresh_rows = []
    for fresh in ((11, 1, 0, 4), (12, 1, 0, 4), (20, 1, 0, 6)):
        local = defect(*fresh)
        first_layer = sum(
            (mass * defect(*child) for mass, child in transformed_children(*fresh)),
            Fraction(),
        )
        fresh_rows.append({
            "context": list(fresh),
            "r_U": record(local),
            "Q_r_U": record(first_layer),
            "two_level_block": record(local + first_layer),
            "normalized_two_level_block": record((local + first_layer) / U(*fresh)),
            "sign": ((local + first_layer) > 0) - ((local + first_layer) < 0),
        })
    if finite_rows[2]["sign"] != 1 or finite_rows[3]["sign"] != -1:
        raise AssertionError("adjacent finite sign certificate failed")
    if int(limiting["defect_limit"]["numerator"]) >= 0:
        raise AssertionError("limiting counterfamily sign failed")

    payload = {
        "claim_tested": (
            "r_U>=0 on every reachable nonfresh context; right-heavy family "
            "(s,K,R,B)=(16,K,K-1,4)"
        ),
        "verdict": "refuted exactly at K=710 and for all sufficiently large K",
        "scope": "auxiliary nonlazy minimal-long-cycle Pbar reset operator only",
        "normalization": (
            "all j=1,...,k retained; U=q(1-q)K/(R+1); "
            "A=sum(theta^2/Q_G)(1-q_child); r_U=U-A-QU"
        ),
        "limiting_identity": (
            "r_infty=sum_t (m_(s,t)-e_(s,t))(H_infty(t)-q)^2; "
            "q(1-q)-Q_infty U=Var_rho(H_infty)"
        ),
        "basin_coefficient_identity": (
            "L_(A,ell)=sum_p [z^A]T(z)^p/(p+ell)!; "
            "also L=1/(ell-1)! integral_0^1 (1-u)^(ell-1) "
            "u(u+A)^(A-1)/A! du"
        ),
        "finite_scope_note": (
            "K=709 positive and K=710 negative are adjacent certificates, "
            "not a claim that 710 is the first failure over all K."
        ),
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "arithmetic": "fractions.Fraction exact",
        "python": platform.python_version(),
        "seed": None,
        "elapsed_seconds": time.time() - started,
        "finite_rows": finite_rows,
        "limit": limiting,
        "integer_tail_certificate": tail,
        "surviving_full_resolvents_at_K710": {
            "status": "exact finite survival only",
            "target_q_one_minus_q": record(witness_target),
            "weighted_value": record(weighted_full),
            "weighted_ratio": record(weighted_full / witness_target),
            "weighted_margin": record(witness_target - weighted_full),
            "unweighted_value": record(unweighted_full),
            "unweighted_ratio": record(unweighted_full / witness_target),
            "unweighted_margin": record(witness_target - unweighted_full),
        },
        "nonfresh_two_level_compensation_at_K710": {
            "status": "exact finite survival only",
            "r_U": record(witness_local),
            "Q_r_U": record(witness_first_layer),
            "two_level_block": record(witness_local + witness_first_layer),
            "normalized_two_level_block": record(
                (witness_local + witness_first_layer) / witness_target
            ),
        },
        "fresh_two_level_calibrations": {
            "status": "exact finite survival only; universal target unresolved",
            "rows": fresh_rows,
        },
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    output = Path(__file__).with_name("defect_counterexample.json")
    output.write_text(encoded)
    print(json.dumps({
        "output": str(output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "elapsed_seconds": payload["elapsed_seconds"],
        "K709": finite_rows[2]["defect"],
        "K710": finite_rows[3]["defect"],
        "limit": limiting["defect_limit"],
        "all_K_at_least_710": tail["all_orders_0_through_2s_strictly_negative"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
