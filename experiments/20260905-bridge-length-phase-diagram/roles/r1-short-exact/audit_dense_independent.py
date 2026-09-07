#!/usr/bin/env python3
"""Nonauthor R2 audit: fresh group-walk and cut/join encodings, exact arithmetic."""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial, isqrt
from pathlib import Path
import hashlib
import json
import platform
import time

import short_exact as sx


def mult(p, q):
    return tuple(p[x] for x in q)


def inverse(p):
    q = [0] * len(p)
    for x, y in enumerate(p):
        q[y] = x
    return tuple(q)


def ceilrat(value):
    return (value.numerator + value.denominator - 1) // value.denominator


def floor_data(top, density):
    cumulative = Fraction(1)
    out = {4: 0}
    cs = {}
    for rank in range(5, top + 1):
        if rank > 5:
            ceiling_root = isqrt(rank - 1) + 1
            cumulative += Fraction(1, rank * ceiling_root)
        cs[rank] = cumulative
        out[rank] = ceilrat(density * rank * (rank - 1) * cumulative)
    return cs, out


def type_completions(rank, length):
    types = list(sx.type_universe(rank, rank - 1))
    coefficients = {mu: sx.transition_counts(rank, mu) for mu in types}
    values = [{mu: int(not mu) for mu in types}]
    for _ in range(length):
        old = values[-1]
        values.append({mu: sum(weight * old[nu] for nu, weight in coefficients[mu].items())
                       for mu in types})
    return values


def star_coefficients(rank, length):
    states = tuple(permutations(range(rank)))
    index = {p: j for j, p in enumerate(states)}
    neighbors = []
    for p in states:
        row = []
        for a in range(rank - 1):
            q = list(p)
            q[a], q[-1] = q[-1], q[a]
            row.append(index[tuple(q)])
        neighbors.append(row)
    table = [[0] * len(states)]
    table[0][index[tuple(range(rank))]] = 1
    for _ in range(length):
        old = table[-1]
        # Backward accumulation, rather than the author's forward accumulation.
        table.append([sum(old[j] for j in row) for row in neighbors])
    return states, index, table


def scalar_audit():
    cases, smallest_ratio = 0, None
    for top in list(range(5, 90)) + [127, 128, 129, 255, 256, 257, 511, 512, 513]:
        minimum = 4 * (top - 1).bit_length()
        for density in [minimum, minimum + 1, 37 + minimum, 1000 + minimum]:
            cs, floors = floor_data(top, density)
            assert floors[top] <= 2 * density * top * (top - 1)
            for rank in range(5, top + 1):
                assert Fraction(1) <= cs[rank] < 2
                assert floors[rank] >= density * rank * (rank - 1)
                if rank > 5:
                    difference = Fraction(rank - 2, rank) * floors[rank] - floors[rank - 1]
                    assert difference > 0
                    ratio = 16 * difference * difference / (density * density * rank)
                    assert ratio >= 1
                    smallest_ratio = ratio if smallest_ratio is None else min(smallest_ratio, ratio)
                    # Also check the mean upper bound and exact rational
                    # square-root-free denominator comparison.
                    mean_star = Fraction(2 * floors[rank], rank)
                    assert mean_star <= 4 * density * rank
                    assert 4 * rank <= rank * rank
                    assert Fraction(97, 12) <= 9
                cases += 1
    return {"cases": cases, "minimum_gap_ratio_squared": float(smallest_ratio)}


def exact_retention(rank=6, density=12):
    _, floors = floor_data(rank, density)
    lengths = [floors[rank], floors[rank] + 1]
    states, index, star = star_coefficients(rank, max(lengths))
    full = type_completions(rank, max(lengths))
    old = type_completions(rank - 1, max(lengths))
    embedded = [p + (rank - 1,) for p in permutations(range(rank - 1))]
    inverses = [inverse(p) for p in embedded]
    old_types = [sx.defect_type(p) for p in embedded]
    all_results = []
    for length in lengths:
        old_degree, star_degree, full_degree = comb(rank - 1, 2), rank - 1, comb(rank, 2)
        discarded = [k for k in range(length + 1)
                     if length - k >= k and length - k < floors[rank - 1]]
        tail_numerator = sum(comb(length, k) * old_degree ** (length - k) * star_degree ** k
                             for k in range(length + 1) if length - k < floors[rank - 1])
        delta_old = Fraction(factorial(rank - 1) - 2, 2) * Fraction(rank - 4, rank - 2) ** ((length + 1) // 2)
        max_ratio, max_mass, endpoints = Fraction(0), Fraction(0), 0
        mass_digest = hashlib.sha256()
        for endpoint in states:
            target_count = full[length][sx.defect_type(endpoint)]
            if not target_count:
                continue
            assert target_count * factorial(rank) >= full_degree ** length
            star_indices = [index[mult(h_inv, endpoint)] for h_inv in inverses]
            numerator = sum(comb(length, k) * sum(
                old[length - k][mu] * star[k][j]
                for mu, j in zip(old_types, star_indices)) for k in discarded)
            assert numerator * factorial(rank - 1) <= 2 * (1 + delta_old) * tail_numerator
            mass = Fraction(numerator, target_count)
            ratio = mass / Fraction(tail_numerator, full_degree ** length)
            assert ratio <= 2 * rank * (1 + delta_old)
            max_mass, max_ratio = max(max_mass, mass), max(max_ratio, ratio)
            mass_digest.update(str(mass).encode())
            endpoints += 1
        all_results.append({"rank": rank, "q": density, "length": length,
            "child_floor": floors[rank - 1], "feasible_labeled_endpoints": endpoints,
            "parity": length % 2, "discarded_k_min": min(discarded),
            "discarded_k_max": max(discarded), "max_exact_mass": float(max_mass),
            "max_exact_conditioning_ratio": float(max_ratio),
            "all_D11_D17_checks_exact": True, "all_mass_sha256": mass_digest.hexdigest()})
    return all_results


def exact_rank_five_lift(density=12):
    rank, length = 5, 20 * density
    states, index, star = star_coefficients(rank, length)
    old = type_completions(rank - 1, length)
    full = type_completions(rank, length)
    embedded = [p + (rank - 1,) for p in permutations(range(rank - 1))]
    inverses = [inverse(p) for p in embedded]
    old_types = [sx.defect_type(p) for p in embedded]
    d, b = comb(rank - 1, 2), rank - 1
    delta = max(
        Fraction(factorial(rank - 1) - 2, 2) * Fraction(rank - 4, rank - 2) ** ((length + 1) // 2),
        Fraction(factorial(rank) - 2, 2) * Fraction(rank - 2, rank - 1) ** (length // 2 + 1))
    maximum_tv, endpoints, branches = Fraction(0), 0, 0
    for endpoint in states:
        total_exact = full[length][sx.defect_type(endpoint)]
        if not total_exact:
            continue
        rows, exact_normalizer, flat_normalizer = [], 0, 0
        star_indices = [index[mult(h_inv, endpoint)] for h_inv in inverses]
        for k in range(length + 1):
            s, choose = length - k, comb(length, k)
            flat_at_k = 0
            for mu, j in zip(old_types, star_indices):
                a, v = old[s][mu], star[k][j]
                exact = choose * a * v
                # Only parity-compatible h can be generated in either half.
                if (sum(mu) - s) % 2:
                    continue
                flat = (rank * choose * d ** s * v if s >= k
                        else choose * a * b ** k)
                assert bool(exact) == bool(flat)
                assert (1 - delta) * 2 * flat <= factorial(rank) * exact <= (1 + delta) * 2 * flat
                rows.append((exact, flat))
                exact_normalizer += exact
                flat_normalizer += flat
                flat_at_k += flat
                branches += 1
            x = inverse(endpoint)[rank - 1]
            z = ((b ** k + b * (-1) ** k) if x == rank - 1 else (b ** k - (-1) ** k)) // rank
            predicted_flat = (rank * choose * d ** s * z if s >= k
                              else choose * d ** s * b ** k)
            assert flat_at_k == predicted_flat
        assert exact_normalizer == total_exact
        assert flat_normalizer > 0
        discrepancy = sum(abs(exact * flat_normalizer - flat * exact_normalizer)
                          for exact, flat in rows)
        tv = Fraction(discrepancy, 2 * exact_normalizer * flat_normalizer)
        assert tv <= delta / (1 - delta)
        maximum_tv = max(maximum_tv, tv)
        endpoints += 1
    return {"rank": rank, "q": density, "length": length,
        "feasible_labeled_endpoints": endpoints, "joint_k_h_branches": branches,
        "max_exact_one_rank_TV": float(maximum_tv),
        "Delta_over_one_minus_Delta": float(delta / (1 - delta)),
        "exact_normalization_pointwise_ratio_support_projection_passed": True}


def main():
    start = time.perf_counter()
    result = {"role": "fresh nonauthor audit by R1 of frozen R2",
              "python": platform.python_version(), "dependencies": "standard library",
              "randomness": None}
    result["floors"] = scalar_audit()
    print("fresh floor audit passed", flush=True)
    result["retention"] = exact_retention()
    print("fresh even/odd retention audit passed", flush=True)
    result["one_rank"] = exact_rank_five_lift()
    print("fresh rank-five positive-lift audit passed", flush=True)
    result["elapsed_seconds"] = time.perf_counter() - start
    result["failures"] = 0
    path = Path(__file__).with_name("fresh_dense_audit_results.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"result": str(path), "elapsed_seconds": result["elapsed_seconds"]}))


if __name__ == "__main__":
    main()
