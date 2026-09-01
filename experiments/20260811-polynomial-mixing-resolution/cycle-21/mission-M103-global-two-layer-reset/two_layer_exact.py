#!/usr/bin/env python3
"""Standalone exact certificate for the M103 global two-layer obstruction.

The implementation imports no predecessor experiment.  It retains every live
attachment rank ``j=1,...,k`` and uses ``fractions.Fraction`` throughout.
The optional complete resolvents are finite DAG sums under strict phase
descent; they are enabled by default for the frozen witness.
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
            mass = w(t) * cayley(s - t, k - 1) / (math.factorial(k) * w(s + 1))
            if mass:
                rows.append((k, t, mass))
                total += mass
    if total != 1:
        raise AssertionError(("root normalization", s, total))
    return tuple(rows)


def U(s: int, K: int, R: int, B: int) -> Fraction:
    q = q_split(s, B)
    return q * (1 - q) * Fraction(K, R + 1)


@functools.lru_cache(maxsize=None)
def reset_energy(s: int, K: int, R: int, B: int, weighted: bool) -> Fraction:
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

    for ell in range(1, s):
        tail_parts = ell - 1
        for A in range(1, s + 1):
            for b in range(1, s - A - tail_parts + 1):
                tail_total = s - A - b
                child_rank = A + b - 1
                if child_rank < 2:
                    continue
                if tail_parts == 0:
                    tail_rows = ((b, w(b)),) if tail_total == 0 else ()
                else:
                    tail_rows = tuple(
                        (
                            last,
                            w(b) * cayley(tail_total - last, tail_parts - 1) * w(last),
                        )
                        for last in range(1, tail_total + 1)
                        if cayley(tail_total - last, tail_parts - 1)
                    )
                for last, suffix_weight in tail_rows:
                    current = scalar(A, ell, last)
                    energy = (
                        suffix_weight
                        * math.factorial(ell)
                        * current * current
                        / (w(A) * w(s + 1))
                    )
                    if weighted:
                        energy *= 1 - q_split(child_rank, b)
                    answer += energy
    return answer


@functools.lru_cache(maxsize=None)
def children(x: tuple[int, int, int, int]) -> tuple[tuple[Fraction, tuple[int, int, int, int]], ...]:
    s, K, R, B = x
    rows = []
    phase = s + K - R
    for k, t, mass in groups(s):
        if t <= B or t - 1 < 2:
            continue
        law_total = sum(
            (attachment_probability(K, R, k, j) for j in range(k + 1)),
            Fraction(),
        )
        if law_total != 1:
            raise AssertionError(("attachment normalization", x, k, law_total))
        for j in range(1, k + 1):
            probability = attachment_probability(K, R, k, j)
            if not probability:
                continue
            child = (t - 1, K + k, R + j, B)
            if child[0] + child[1] - child[2] >= phase:
                raise AssertionError(("strict phase", x, child))
            rows.append((mass * probability, child))
    return tuple(rows)


@functools.lru_cache(maxsize=None)
def defect(x: tuple[int, int, int, int]) -> Fraction:
    return U(*x) - reset_energy(*x, True) - sum(
        (mass * U(*child) for mass, child in children(x)), Fraction()
    )


def two_layer(x: tuple[int, int, int, int]) -> tuple[Fraction, Fraction, Fraction]:
    local = defect(x)
    first = sum((mass * defect(child) for mass, child in children(x)), Fraction())
    return local, first, local + first


@functools.lru_cache(maxsize=None)
def weighted_resolvent(x: tuple[int, int, int, int]) -> Fraction:
    return reset_energy(*x, True) + sum(
        (mass * weighted_resolvent(child) for mass, child in children(x)),
        Fraction(),
    )


@functools.lru_cache(maxsize=None)
def unweighted_resolvent(x: tuple[int, int, int, int]) -> Fraction:
    return reset_energy(*x, False) + sum(
        (mass * unweighted_resolvent(child) for mass, child in children(x)),
        Fraction(),
    )


def record(value: Fraction) -> dict[str, object]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--with-resolvents", action="store_true")
    args = parser.parse_args()
    started = time.time()
    witness = (30, 1, 0, 10)
    local, first, block = two_layer(witness)
    target = U(*witness)
    if block >= 0:
        raise AssertionError("two-layer witness lost its negative sign")

    payload: dict[str, object] = {
        "claim_tested": "(I+Q)r_U>=0 at every reachable active context",
        "verdict": "refuted by exact fresh-context witness",
        "scope": "auxiliary nonlazy minimal-long-cycle Pbar reset operator only",
        "witness": list(witness),
        "reachability": "fresh contexts (K,R)=(1,0) are in the accepted reachable closure",
        "normalization": "all j=1,...,k retained; j=0 killed; every full attachment law sums to one",
        "identity": "(I+Q)r_U=U-A-QA-Q^2U",
        "target_U": record(target),
        "r_U": record(local),
        "Q_r_U": record(first),
        "two_layer": record(block),
        "normalized_two_layer": record(block / target),
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "arithmetic": "fractions.Fraction exact",
        "python": platform.python_version(),
        "seed": None,
    }
    if args.with_resolvents:
        weighted = weighted_resolvent(witness)
        unweighted = unweighted_resolvent(witness)
        payload["full_resolvents"] = {
            "status": "exact finite survival only",
            "weighted": record(weighted),
            "weighted_ratio": record(weighted / target),
            "weighted_margin": record(target - weighted),
            "unweighted": record(unweighted),
            "unweighted_ratio": record(unweighted / target),
            "unweighted_margin": record(target - unweighted),
        }
    else:
        payload["full_resolvents"] = {
            "status": (
                "exact Fraction values from a separate run of the frozen M98 "
                "all-rank finite-DAG core; not recomputed by this compact command"
            ),
            "weighted_ratio_decimal": 0.7372496452184509,
            "weighted_margin_decimal": 0.005756384312696922,
            "unweighted_ratio_decimal": 0.826726883909605,
            "unweighted_margin_decimal": 0.003796100097007001,
            "reproduction": (
                "rerun this script with --with-resolvents, or evaluate "
                "weighted_resolvent/unweighted_resolvent at (30,1,0,10)"
            ),
        }
    payload["elapsed_seconds"] = time.time() - started
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "two_layer": payload["two_layer"],
        "normalized_two_layer": payload["normalized_two_layer"],
        "full_resolvents": payload.get("full_resolvents"),
        "elapsed_seconds": payload["elapsed_seconds"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
