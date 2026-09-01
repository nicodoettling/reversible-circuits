#!/usr/bin/env python3
"""Exact finite falsification harness for the midpoint-prefix renewal cut.

The computation can refute the universal count, mass-orientation, crossing-
window, or one-step-exit identities used in the M20 proof.  Positive finite
conductance is not used to infer an asymptotic spectral gap.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import time
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


Perm = tuple[int, ...]
Word = tuple[Perm, ...]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[i]] for i in range(len(p)))


def transpositions(n: int) -> list[Perm]:
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            p = list(range(n))
            p[i], p[j] = p[j], p[i]
            out.append(tuple(p))
    return out


def product(word: Word, ident: Perm) -> Perm:
    ans = ident
    for t in word:
        ans = compose(ans, t)
    return ans


def connected(word: Word, n: int) -> bool:
    parent = list(range(n))

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for t in word:
        moved = [i for i in range(n) if t[i] != i]
        a, b = moved
        ra, rb = root(a), root(b)
        if ra != rb:
            parent[ra] = rb
    return len({root(i) for i in range(n)}) == 1


def identity_words(n: int, m: int):
    ident = tuple(range(n))
    ts = transpositions(n)
    return [w for w in itertools.product(ts, repeat=m) if product(w, ident) == ident]


def block_fibers(n: int, lengths):
    ident = tuple(range(n))
    ts = transpositions(n)
    ans = {}
    for r in lengths:
        fibers = defaultdict(list)
        for block in itertools.product(ts, repeat=r):
            fibers[product(block, ident)].append(block)
        ans[r] = fibers
    return ans


def prefix_cut(word: Word, n: int, require_connected: bool) -> bool:
    ident = tuple(range(n))
    k = len(word) // 2
    return product(word[:k], ident) == ident and (
        connected(word, n) if require_connected else True
    )


def exact_exit_probability(word, n, fibers, require_connected):
    m = len(word)
    ident = tuple(range(n))
    lengths = tuple(r for r in (3, 4, 5) if r <= m)
    ans = Fraction(0)
    for r in lengths:
        for i in range(m - r + 1):
            q = product(word[i:i+r], ident)
            fiber = fibers[r][q]
            exits = 0
            for replacement in fiber:
                out = word[:i] + replacement + word[i+r:]
                exits += not prefix_cut(out, n, require_connected)
            ans += Fraction(1, 2 * len(lengths) * (m-r+1)) * Fraction(exits, len(fiber))
    return ans


def certificate_target(word: Word, n: int):
    """The length-three exit used in the proof, at one-based start k."""
    ts = transpositions(n)
    k = len(word) // 2
    a, b, c = word[k-1:k+2]
    if a != b:
        bab = compose(b, compose(a, b))
        replacement = (b, bab, c)
        case = "hurwitz_distinct"
    else:
        d = next(t for t in ts if t != a)
        replacement = (d, d, c)
        case = "square_refresh_equal"
    out = word[:k-1] + replacement + word[k+2:]
    ident = tuple(range(n))
    return {
        "case": case,
        "same_block_product": product((a, b, c), ident) == product(replacement, ident),
        "global_identity": product(out, ident) == ident,
        "prefix_exits": product(out[:k], ident) != ident,
    }


def set_partitions(items):
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for part in set_partitions(rest):
        yield [[first]] + [b[:] for b in part]
        for i in range(len(part)):
            new = [b[:] for b in part]
            new[i] = [first] + new[i]
            yield new


def return_counts(n: int, max_length: int):
    ident = tuple(range(n))
    if n <= 1:
        return [1] + [0] * max_length
    ts = transpositions(n)
    dist = {ident: 1}
    ans = [1]
    for _ in range(max_length):
        nxt = defaultdict(int)
        for g, count in dist.items():
            for t in ts:
                nxt[compose(g, t)] += count
        dist = dict(nxt)
        ans.append(dist.get(ident, 0))
    return ans


def partition_allowed_return(block_sizes, k, returns):
    dp = [0] * (k + 1)
    dp[0] = 1
    used = 0
    for d in block_sizes:
        nxt = [0] * (k + 1)
        for s in range(used + 1):
            if dp[s] == 0:
                continue
            for t in range(k - s + 1):
                count = returns[d][t]
                if count:
                    nxt[s+t] += math.comb(s+t, t) * dp[s] * count
        dp = nxt
        used = k
    return dp[k]


def mobius_connected_pair_count(n: int, k: int):
    returns = {d: return_counts(d, k) for d in range(1, n + 1)}
    total = 0
    terms = []
    for part in set_partitions(list(range(n))):
        sizes = sorted(map(len, part), reverse=True)
        allowed = partition_allowed_return(sizes, k, returns)
        mu = (-1) ** (len(part)-1) * math.factorial(len(part)-1)
        contribution = mu * allowed * allowed
        total += contribution
        terms.append((sizes, allowed, mu, contribution))
    return total, terms, returns[n][k]


def finite_case(n: int, m: int, do_kernel: bool):
    start = time.perf_counter()
    states = identity_words(n, m)
    relaxed = [w for w in states if prefix_cut(w, n, False)]
    conn = [w for w in states if prefix_cut(w, n, True)]
    record = {
        "N": n,
        "m": m,
        "identity_word_count": len(states),
        "prefix_renewal_count": len(relaxed),
        "connected_prefix_renewal_count": len(conn),
        "prefix_renewal_mass": [len(relaxed), len(states)],
        "connected_prefix_renewal_mass": [len(conn), len(states)],
    }
    if m % 2 == 0 and m // 2 % 2 == 0:
        mobius, _terms, half_returns = mobius_connected_pair_count(n, m // 2)
        record["mobius_connected_pair_count"] = mobius
        record["half_return_count"] = half_returns
        record["mobius_matches_enumeration"] = mobius == len(conn)
    if relaxed:
        certs = [certificate_target(w, n) for w in relaxed]
        record["exit_certificate_all_words"] = all(
            c["same_block_product"] and c["global_identity"] and c["prefix_exits"]
            for c in certs
        )
        record["exit_certificate_case_counts"] = {
            case: sum(c["case"] == case for c in certs)
            for case in ("hurwitz_distinct", "square_refresh_equal")
        }
    if do_kernel:
        lengths = tuple(r for r in (3, 4, 5) if r <= m)
        fibers = block_fibers(n, lengths)
        for name, cut, require_connected in (
            ("relaxed", relaxed, False),
            ("connected", conn, True),
        ):
            if not cut:
                continue
            exits = [exact_exit_probability(w, n, fibers, require_connected) for w in cut]
            avg = sum(exits, Fraction(0)) / len(exits)
            record[f"{name}_min_exit"] = [min(exits).numerator, min(exits).denominator]
            record[f"{name}_conductance"] = [avg.numerator, avg.denominator]
    record["runtime_seconds"] = time.perf_counter() - start
    return record


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    cases = [
        finite_case(3, 4, True),
        finite_case(4, 4, True),
        finite_case(4, 6, False),
    ]
    extra = []
    for n, k in ((4, 6), (5, 8)):
        count, _terms, half = mobius_connected_pair_count(n, k)
        extra.append({
            "N": n,
            "half_length": k,
            "connected_pair_count": count,
            "half_return_count": half,
            "positive": count > 0,
        })
    payload = {
        "status": "complete",
        "deterministic": True,
        "python": platform.python_version(),
        "composition": "(pq)(x)=p(q(x))",
        "target": "global uniform identity bridge and original lazy r={3,4,5} K",
        "claim_scope": (
            "finite falsification of exact count, mass, crossing-window, and one-step-exit identities"
        ),
        "crossing_window_formula": {
            "r3": 2,
            "r4": 3,
            "r5": 4,
            "total": 9,
        },
        "cases": cases,
        "mobius_positive_cases": extra,
    }
    Path(args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
