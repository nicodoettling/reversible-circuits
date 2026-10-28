#!/usr/bin/env python3
"""Independent finite source-normalization checks; reservation I1-J5."""
import argparse
import itertools
import json
import math
import os
import platform
import time
from collections import Counter
from fractions import Fraction as Q

TERMS = {
    1: [(1, (2,), 1), (-1, (1,), 0)],
    2: [(5, (5,), 3), (-12, (4,), 3), (7, (3,), 3),
        (44, (2, 4), 4), (29, (3, 3), 4), (-86, (2, 3), 4),
        (21, (2, 2), 4), (200, (2, 2, 3), 5),
        (-100, (2, 2, 2), 5), (140, (2, 2, 2, 2), 6)],
}


def cycles(p):
    unseen = set(range(len(p)))
    result = []
    while unseen:
        x = min(unseen)
        cyc = []
        while x in unseen:
            unseen.remove(x)
            cyc.append(x)
            x = p[x]
        result.append(cyc)
    return result


def connected_count(alpha, genus):
    n = sum(alpha)
    c = len(alpha)
    if n == 1:
        return int(genus == 0)
    r = n + c - 2 + 2 * genus
    prod_a = math.prod(Q(a ** a, math.factorial(a - 1)) for a in alpha)
    if genus == 0:
        power = Q(n ** (c - 3)) if c >= 3 else Q(1, n ** (3 - c))
        answer = math.factorial(r) * power * prod_a
    else:
        total = Q(0)
        for coefficient, exponents, denominator_power in TERMS[genus]:
            for marked in itertools.permutations(range(c), len(exponents)):
                marked_weight = math.prod(alpha[i] ** j for i, j in zip(marked, exponents))
                remaining = [alpha[i] for i in range(c) if i not in marked]
                elementary = [1] + [0] * len(remaining)
                for a in remaining:
                    for q in range(len(remaining), 0, -1):
                        elementary[q] += a * elementary[q - 1]
                residual = Q(0)
                for q in range(len(remaining) + 1):
                    if denominator_power == 0 and q:
                        continue
                    factor = 1 if denominator_power == 0 else math.comb(denominator_power + q - 1, q)
                    residual += factor * math.factorial(q) * elementary[q] * n ** (len(remaining) - q)
                total += coefficient * marked_weight * residual
        answer = math.factorial(r) * prod_a * total / (n * (24 if genus == 1 else 5760))
    assert answer.denominator == 1, (alpha, genus, answer)
    return answer.numerator


def enumerate_counts(n, max_length):
    edges = list(itertools.combinations(range(n), 2))
    is_connected = {}
    for mask in range(1 << len(edges)):
        reached = {0}
        for _ in range(n):
            for i, (a, b) in enumerate(edges):
                if mask & (1 << i) and (a in reached or b in reached):
                    reached.update((a, b))
        is_connected[mask] = len(reached) == n
    counts = Counter()
    visited = 0
    def visit(p, mask, depth):
        nonlocal visited
        visited += 1
        if is_connected[mask]:
            counts[depth, p] += 1
        if depth == max_length:
            return
        for i, (a, b) in enumerate(edges):
            nxt = list(p)
            nxt[a], nxt[b] = nxt[b], nxt[a]
            visit(tuple(nxt), mask | (1 << i), depth + 1)
    visit(tuple(range(n)), 0, 0)
    comparisons = 0
    for p in itertools.permutations(range(n)):
        alpha = tuple(map(len, cycles(p)))
        for g in range(3):
            r = n + len(alpha) - 2 + 2 * g
            if r <= max_length:
                expected = connected_count(alpha, g)
                assert counts[r, p] == expected, (n, p, g, r, counts[r, p], expected)
                comparisons += 1
    return {"degree": n, "max_length": max_length, "word_prefixes_enumerated": visited,
            "fixed_permutation_comparisons": comparisons}


def dyz_checks():
    h = {(g, 1): Q(int(g == 0)) for g in range(6)}
    comparisons = 0
    for v in range(2, 9):
        for g in range(6):
            total = Q(0)
            for a in range(1, v):
                b = v - a
                for k in range(1, g + 2):
                    for g1 in range(g + 2 - k):
                        g2 = g + 1 - k - g1
                        total += Q(a ** (2 * k + 1) * b * b, math.factorial(2 * k)) * h[g1, a] * h[g2, b]
            h[g, v] = Q(2, v * v * (v - 1)) * total
            h0 = Q(v ** (v - 3), math.factorial(v)) if v >= 3 else Q(1, 4)
            if g == 0:
                assert h[g, v] == h0
            majorant = h0 * v ** (2 * g) * math.comb(v + g - 2, g)
            assert 0 <= h[g, v] <= majorant, (g, v, h[g, v], majorant)
            comparisons += 1
    return {"max_degree": 8, "max_genus": 5, "majorant_comparisons": comparisons,
            "h_0_2": str(h[0, 2]), "h_2_2": str(h[2, 2]), "h_2_3": str(h[2, 3])}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    started = time.monotonic()
    checks = [enumerate_counts(2, 6), enumerate_counts(3, 8), enumerate_counts(4, 6)]
    result = {"reservation": "I1-J5", "base_commit": "d8893491e04aff74ff3185f7054470ffa24a44a4",
              "seed": 0, "stochastic": False, "python": platform.python_version(),
              "nonstandard_dependencies": [], "enumeration": checks, "dyz": dyz_checks(),
              "boundary_counts": {"S3_identity_length4": connected_count((1, 1, 1), 0),
                                  "S3_identity_length6": connected_count((1, 1, 1), 1),
                                  "S3_identity_length8": connected_count((1, 1, 1), 2),
                                  "S4_identity_length6": connected_count((1, 1, 1, 1), 0)},
              "elapsed_seconds": time.monotonic() - started, "status": "passed"}
    tmp = args.output + ".tmp"
    with open(tmp, "w", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    os.replace(tmp, args.output)
    print(json.dumps({"status": "passed", "fixed_permutation_comparisons": sum(x["fixed_permutation_comparisons"] for x in checks),
                      "word_prefixes_enumerated": sum(x["word_prefixes_enumerated"] for x in checks),
                      "elapsed_seconds": result["elapsed_seconds"]}, sort_keys=True))


if __name__ == "__main__":
    main()
