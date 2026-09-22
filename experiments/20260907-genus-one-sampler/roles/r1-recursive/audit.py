"""Exact finite audit for R1-T1; all exponential loops are bounded tests."""

import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import json
import platform
import random
import subprocess
import sys
import time

import sampler as s


def partitions(n, floor=1):
    if n == 0:
        yield ()
    for a in range(floor, n + 1):
        for rest in partitions(n - a, a):
            yield (a,) + rest


@lru_cache(maxsize=8192)
def signed_count(alpha, genus):
    return s.count_signed(alpha, genus)


def direct_assignment_weight(lengths, ga, gb, assignment):
    aa = tuple(a for a, side in zip(lengths, assignment) if side == 0)
    bb = tuple(a for a, side in zip(lengths, assignment) if side == 1)
    ra = sum(aa) + len(aa) - 2 + 2 * ga
    rb = sum(bb) + len(bb) - 2 + 2 * gb
    return comb(ra + rb, ra) * signed_count(aa, ga) * signed_count(bb, gb)


def forced_oracle_audit(max_n):
    queries, inventories, assignments = 0, 0, 0
    digest = hashlib.sha256()
    for n in range(2, max_n + 1):
        # P,Q are oriented and remaining cycles are individually indexed.
        for p in range(1, n):
            for q in range(1, n - p + 1):
                for other in partitions(n - p - q):
                    lengths = (p, q) + other
                    inventories += 1
                    all_allocations = [(0, 1) + a for a in product((0, 1), repeat=len(other))]
                    assignments += len(all_allocations)
                    for ga, gb in ((0, 0), (0, 1), (1, 0)):
                        raw = {a: direct_assignment_weight(lengths, ga, gb, a) for a in all_allocations}
                        # -1 means unexposed. Exhaust all partial assignments,
                        # including non-prefix constraints and zero branches.
                        for partial in product((-1, 0, 1), repeat=len(other)):
                            forced = {0: 0, 1: 1}
                            forced.update({i + 2: a for i, a in enumerate(partial) if a >= 0})
                            expected = sum(w for a, w in raw.items() if all(a[i] == side for i, side in forced.items()))
                            actual = s.allocation_mass(lengths, ga, gb, forced)
                            assert actual == expected, (lengths, ga, gb, forced, actual, expected)
                            queries += 1
                            digest.update(repr((lengths, ga, gb, partial, actual)).encode())
    return dict(max_n=max_n, inventories=inventories, full_assignments=assignments,
                forced_queries=queries, digest=digest.hexdigest(), passed=True)


@lru_cache(maxsize=16384)
def merge_partition(partition, x, y):
    bx = next(a for a in partition if (a >> x) & 1)
    by = next(a for a in partition if (a >> y) & 1)
    if bx == by:
        return partition
    return tuple(sorted([a for a in partition if a != bx and a != by] + [bx | by]))


def endpoint_count_audit(max_n):
    """Independent positive DP on (labeled permutation,support partition)."""
    comparisons, rows = 0, []
    for n in range(1, max_n + 1):
        ident = tuple(range(n))
        edges = tuple(combinations(range(n), 2))
        connected = ((1 << n) - 1,)
        dp = {(ident, tuple(1 << x for x in range(n))): 1}
        for length in range(2 * n + 1):
            global_identity = sum(z for (p, pi), z in dp.items() if p == ident)
            connected_identity = dp.get((ident, connected), 0)
            endpoint_rows = {}
            for (p, partition), z in dp.items():
                if partition != connected:
                    continue
                alpha = tuple(len(c) for c in s.cycles(p))
                surplus = length - (n + len(alpha) - 2)
                if surplus in (0, 2):
                    genus = surplus // 2
                    expected = signed_count(alpha, genus)
                    assert z == expected == s.count(alpha, genus), (n, length, p, z, expected)
                    comparisons += 1
                    endpoint_rows[alpha] = z
            # Also demand equality for feasible formula endpoints even if the
            # independent DP has zero support there.
            if n == 1:
                assert connected_identity == (1 if length == 0 else 0)
            rows.append(dict(n=n, length=length, states=len(dp),
                             global_identity=global_identity,
                             connected_identity=connected_identity,
                             connected_types={str(a): z for a, z in endpoint_rows.items()}))
            if length == 2 * n:
                break
            nxt = Counter()
            for (p, partition), z in dp.items():
                for x, y in edges:
                    # Independent right multiplication: compose p with swap.
                    pp = tuple(p[y] if i == x else p[x] if i == y else p[i] for i in range(n))
                    nxt[(pp, merge_partition(partition, x, y))] += z
            dp = nxt
    return dict(max_n=max_n, endpoint_comparisons=comparisons, rows=rows, passed=True)


def identity_words(n, length):
    edges = tuple(combinations(range(n), 2))
    ident = tuple(range(n))
    if length == 0:
        yield ()
        return
    if length % 2 or not edges:
        return

    def visit(p, word, remaining):
        if remaining == 1:
            moved = tuple(i for i in range(n) if p[i] != i)
            if len(moved) == 2 and p[moved[0]] == moved[1] and p[moved[1]] == moved[0]:
                yield word + (moved,)
            return
        for edge in edges:
            yield from visit(s.right_swap(p, edge), word + (edge,), remaining - 1)

    yield from visit(ident, (), length)


@lru_cache(maxsize=8192)
def allocation_probability(lengths, ga, gb, assignment):
    forced = {0: 0, 1: 1}
    initial = current = s.allocation_mass(lengths, ga, gb, forced)
    assert initial > 0
    prob = Fraction(1)
    for i in range(2, len(lengths)):
        wa = s.allocation_mass(lengths, ga, gb, forced | {i: 0})
        wb = s.allocation_mass(lengths, ga, gb, forced | {i: 1})
        assert wa + wb == current
        selected = (wa, wb)[assignment[i]]
        assert selected > 0
        prob *= Fraction(selected, current)
        current = selected
        forced[i] = assignment[i]
    expected = direct_assignment_weight(lengths, ga, gb, assignment)
    assert current == expected and prob == Fraction(expected, initial)
    return prob


@lru_cache(maxsize=100000)
def word_probability(n, endpoint, genus, word):
    """Reconstruct the unique recursive path, multiplying actual algorithm laws."""
    parent_count = signed_count(tuple(len(c) for c in s.cycles(endpoint)), genus)
    assert parent_count > 0
    assert len(word) == n + len(s.cycles(endpoint)) - 2 + 2 * genus
    assert s.evaluate(n, word) == endpoint
    assert len(s.components(n, word)) == 1
    if not word:
        assert n == 1 and genus == 0 and parent_count == 1
        return Fraction(1)
    prefix, edge = word[:-1], word[-1]
    pi = s.right_swap(endpoint, edge)
    assert s.evaluate(n, prefix) == pi
    groups = s.components(n, prefix)
    if len(groups) == 1:
        gg = (len(prefix) - n - len(s.cycles(pi)) + 2) // 2
        choices = [b for b in s.branches(endpoint, genus)
                   if b.edge == edge and b.kind == "connected" and b.child_genus == gg]
        assert len(choices) == 1
        branch = choices[0]
        probability = Fraction(branch.weight, parent_count) * word_probability(n, pi, gg, prefix)
    else:
        assert len(groups) == 2
        aa = next(a for a in groups if edge[0] in a)
        bb = next(a for a in groups if edge[1] in a)
        assert aa != bb
        ai, bi = {x: i for i, x in enumerate(aa)}, {x: i for i, x in enumerate(bb)}
        positions = tuple(i for i, (x, y) in enumerate(prefix) if x in ai)
        raw_a = tuple(t for t in prefix if t[0] in ai)
        raw_b = tuple(t for t in prefix if t[0] in bi)
        assert all(x in ai and y in ai for x, y in raw_a)
        assert all(x in bi and y in bi for x, y in raw_b)
        wa = tuple((ai[x], ai[y]) for x, y in raw_a)
        wb = tuple((bi[x], bi[y]) for x, y in raw_b)
        pa, pb = s.restrict(pi, aa), s.restrict(pi, bb)
        ga = (len(wa) - len(aa) - len(s.cycles(pa)) + 2) // 2
        gb = (len(wb) - len(bb) - len(s.cycles(pb)) + 2) // 2
        assert ga >= 0 and gb >= 0 and ga + gb == genus
        choices = [b for b in s.branches(endpoint, genus)
                   if b.edge == edge and b.kind == "split" and (b.ga, b.gb) == (ga, gb)]
        assert len(choices) == 1
        branch = choices[0]
        assignment = tuple(0 if c[0] in ai else 1 for c in branch.cut_cycles)
        assert assignment[:2] == (0, 1)
        lengths = tuple(len(c) for c in branch.cut_cycles)
        conditional = allocation_probability(lengths, ga, gb, assignment)
        child_a = word_probability(len(aa), pa, ga, wa)
        child_b = word_probability(len(bb), pb, gb, wb)
        probability = Fraction(branch.weight, parent_count) * conditional * child_a * child_b / comb(len(prefix), len(wa))
        # Actual inverse reconstruction checks position multiplicity.
        assert s.interleave(raw_a, raw_b, positions) + (edge,) == word
    assert probability == Fraction(1, parent_count), (n, endpoint, genus, word, probability, parent_count)
    return probability


def per_word_audit(max_n):
    rows = []
    cases = [(1, 0), (1, 2), (2, 0), (2, 1), (2, 2), (2, 4),
             (3, 0), (3, 2), (3, 3), (3, 4), (3, 6),
             (4, 0), (4, 2), (4, 4), (4, 6), (4, 8)]
    expected_global = {(3, 4): 27, (4, 4): 120, (4, 6): 3936}
    expected_connected = {(2, 4): 1, (3, 6): 240, (4, 8): 131040}
    for n, length in cases:
        if n > max_n:
            continue
        all_count, connected_count = 0, 0
        probability_sum = Fraction(0)
        digest = hashlib.sha256()
        branches_observed = Counter()
        for word in identity_words(n, length):
            all_count += 1
            assert s.evaluate(n, word) == tuple(range(n))
            if len(s.components(n, word)) == 1:
                connected_count += 1
                genus = (length - 2 * n + 2) // 2
                assert genus in (0, 1), (n, length, genus)
                prob = word_probability(n, tuple(range(n)), genus, word)
                probability_sum += prob
                digest.update(repr((word, prob.numerator, prob.denominator)).encode())
                if word:
                    branches_observed[str((word[-1], len(s.components(n, word[:-1]))))] += 1
        if (n, length) in expected_global:
            assert all_count == expected_global[n, length]
        if (n, length) in expected_connected:
            assert connected_count == expected_connected[n, length]
        assert probability_sum == (1 if connected_count else 0)
        row = dict(n=n, length=length, total=all_count, connected=connected_count,
                   probability_sum=str(probability_sum),
                   each_probability=f"1/{connected_count}" if connected_count else None,
                   unique_reconstruction_checked=connected_count,
                   digest=digest.hexdigest(), final_branches=dict(branches_observed))
        rows.append(row)
        print(json.dumps(dict(stage="per-word", **row)), flush=True)
    return dict(rows=rows, passed=True, recursive_cache=word_probability.cache_info()._asdict())


def regression_audit():
    a, b = (0, 1), (1, 2)
    braid = (a, b) * 3
    assert all(braid[i] != braid[i + 1] for i in range(len(braid) - 1))
    assert word_probability(3, (0, 1, 2), 1, braid) == Fraction(1, 240)
    extension = braid + ((2, 3), (2, 3))
    assert word_probability(4, (0, 1, 2, 3), 1, extension) == Fraction(1, 131040)
    for n in range(1, 9):
        for k in range(n + 1):
            unranked = [s.unrank_subset(n, k, rank) for rank in range(comb(n, k))]
            assert len(set(unranked)) == comb(n, k)
            assert set(unranked) == set(combinations(range(n), k))
    # CP-1 rejects the invalid marginal product rule. This sampler instead
    # computes exact partial-assignment conditional masses at every branch.
    gamma = Fraction(1, 10)
    posterior_a = Fraction(21, 2000)
    posterior_c = Fraction(1, 20)
    posterior_d = Fraction(879, 1000)
    assert 2 * posterior_a + 2 * posterior_c + posterior_d == 1
    assert posterior_a + posterior_c == Fraction(121, 2000) < gamma
    assert posterior_a > gamma * gamma
    assert posterior_a / (posterior_a + posterior_c + posterior_c) == Fraction(21, 221) < gamma
    return dict(braid_probability="1/240", tree_extension_probability="1/131040",
                cp1_joint="21/2000 > 1/100", cp1_status="old product bound rejected",
                interleaving_unranking="all n<=8,k,rank", passed=True)


def smoke_audit():
    rows = []
    for seed in (1729, 2718):
        rng = random.Random(seed)
        for n in (2, 3, 4, 6, 8, 12):
            start = time.perf_counter()
            draws = 3
            dig = hashlib.sha256()
            for _ in range(draws):
                word = s.sample_identity(n, rng)
                assert len(word) == 2 * n
                assert s.evaluate(n, word) == tuple(range(n))
                assert len(s.components(n, word)) == 1
                dig.update(repr(word).encode())
            rows.append(dict(seed=seed, n=n, draws=draws,
                             seconds=time.perf_counter() - start, digest=dig.hexdigest()))
    return dict(rows=rows, interpretation="validity only; no empirical uniformity claim", passed=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--forced-max", type=int, default=8)
    parser.add_argument("--endpoint-max", type=int, default=5)
    parser.add_argument("--word-max", type=int, default=4)
    parser.add_argument("--output", default="results.json")
    args = parser.parse_args()
    start = time.perf_counter()
    result = dict(proof_version="R1-T1", python=platform.python_version(),
                  dependencies="standard library only", command=" ".join(sys.argv),
                  git_head=subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
                  git_status=subprocess.check_output(["git", "status", "--short"], text=True),
                  deterministic_tests=True)
    for name, function in (
        ("forced_oracle", lambda: forced_oracle_audit(args.forced_max)),
        ("endpoint_counts", lambda: endpoint_count_audit(args.endpoint_max)),
        ("per_word", lambda: per_word_audit(args.word_max)),
        ("regressions", regression_audit),
        ("smoke", smoke_audit),
    ):
        step = time.perf_counter()
        result[name] = function()
        result[name]["seconds"] = time.perf_counter() - step
        Path(args.output).write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps(dict(stage=name, seconds=result[name]["seconds"], passed=True)), flush=True)
    result["seconds"] = time.perf_counter() - start
    result["all_passed"] = True
    Path(args.output).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(dict(all_passed=True, seconds=result["seconds"])), flush=True)


if __name__ == "__main__":
    main()
