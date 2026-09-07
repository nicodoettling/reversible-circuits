#!/usr/bin/env python3
"""Positive exact transposition-bridge sampling; standard library only.

Convention: compose(alpha,beta)[x] = alpha[beta[x]].
The RNG interface is getrandbits; exactness assumes independent fair bits.
Random smoke tests use random.Random only for reproducibility.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
import argparse
import json
import math
from pathlib import Path
import platform
import random
import time


def identity(n):
    return tuple(range(n))


def compose(alpha, beta):
    return tuple(alpha[beta[x]] for x in range(len(alpha)))


def left_transpose(p, edge):
    a, b = edge
    return tuple(b if x == a else a if x == b else x for x in p)


def evaluate(n, word):
    p = identity(n)
    for a, b in word:
        # Right multiplication swaps the two entries of the map p.
        p = list(p)
        p[a], p[b] = p[b], p[a]
        p = tuple(p)
    return p


def cycle_lengths(p):
    seen = set()
    lengths = []
    for x in range(len(p)):
        if x not in seen:
            y, length = x, 0
            while y not in seen:
                seen.add(y)
                length += 1
                y = p[y]
            lengths.append(length)
    return tuple(sorted(lengths))


def defect_type(p):
    return tuple(a - 1 for a in cycle_lengths(p) if a > 1)


def partitions(total, least=1):
    if total == 0:
        yield ()
    for first in range(least, total + 1):
        for rest in partitions(total - first, first):
            yield (first,) + rest


def type_universe(n, max_defect):
    for d in range(max_defect + 1):
        for mu in partitions(d):
            if d + len(mu) <= n:
                yield mu


def transition_counts(n, mu):
    """Number of individual left transpositions producing each next type."""
    lengths = Counter(x + 1 for x in mu)
    fixed = n - sum(mu) - len(mu)
    if fixed:
        lengths[1] = fixed
    sizes = sorted(lengths)
    out = Counter()

    def add(changes, multiplicity):
        if not multiplicity:
            return
        updated = lengths.copy()
        for a, amount in changes:
            updated[a] += amount
        assert all(amount >= 0 for amount in updated.values())
        result = tuple(a - 1 for a in sorted(updated) if a > 1
                       for _ in range(updated[a]))
        out[result] += multiplicity

    # Joining two distinct cycles.
    for j, a in enumerate(sizes):
        for b in sizes[j:]:
            multiplicity = (a * b * lengths[a] * lengths[b] if a != b
                            else a * a * math.comb(lengths[a], 2))
            add(((a, -1), (b, -1), (a + b, 1)), multiplicity)
    # Cutting a cycle into two cycles. Equal halves have only a/2 edges.
    for a in sizes:
        for b in range(1, a // 2 + 1):
            c = a - b
            multiplicity = lengths[a] * (a if b != c else a // 2)
            add(((a, -1), (b, 1), (c, 1)), multiplicity)
    return dict(out)


def feasible(n, m, g):
    if n < 1 or m < 0 or sorted(g) != list(range(n)):
        return False
    if n == 1:
        return m == 0
    h = sum(defect_type(g))
    return m >= h and (m - h) % 2 == 0


def valid_word(n, m, g):
    """Deterministic minimal cycle factorization, padded by identical pairs."""
    if not feasible(n, m, g):
        raise ValueError("empty endpoint fiber")
    word, seen = [], set()
    for x in range(n):
        if x in seen:
            continue
        cycle, y = [], x
        while y not in seen:
            seen.add(y)
            cycle.append(y)
            y = g[y]
        word.extend(tuple(sorted((cycle[0], y))) for y in reversed(cycle[1:]))
    while len(word) < m:
        word.extend(((0, 1), (0, 1)))
    assert evaluate(n, word) == g
    return word


def minimal_cycle_counts(n):
    """Positive recurrence for a specified a-cycle in exactly a-1 factors."""
    counts = [1] * (n + 1)
    for a in range(2, n + 1):
        counts[a] = sum((a if b != a - b else a // 2)
                        * math.comb(a - 2, b - 1) * counts[b] * counts[a - b]
                        for b in range(1, a // 2 + 1))
    return counts


def minimal_completion_count(p, counts):
    lengths = cycle_lengths(p)
    h = sum(a - 1 for a in lengths)
    numerator = math.factorial(h) * math.prod(counts[a] for a in lengths)
    denominator = math.prod(math.factorial(a - 1) for a in lengths)
    assert numerator % denominator == 0
    return numerator // denominator


def sample_minimal(endpoint, rng):
    n = len(endpoint)
    counts, residual, word = minimal_cycle_counts(n), tuple(endpoint), []
    for h in range(sum(defect_type(endpoint)), 0, -1):
        weights = []
        for edge in combinations(range(n), 2):
            following = left_transpose(residual, edge)
            if sum(defect_type(following)) == h - 1:
                weights.append((edge, minimal_completion_count(following, counts)))
        total = sum(weight for _, weight in weights)
        assert total == minimal_completion_count(residual, counts)
        ticket = random_below(rng, total)
        for edge, weight in weights:
            if ticket < weight:
                word.append(edge)
                residual = left_transpose(residual, edge)
                break
            ticket -= weight
    assert evaluate(n, word) == tuple(endpoint)
    return word


class RejectionLimit(Exception):
    pass


def random_below(rng, total, attempts=None):
    if total < 1:
        raise ValueError("positive total required")
    if total == 1:
        return 0
    bits = (total - 1).bit_length()
    used = 0
    while attempts is None or used < attempts:
        value = rng.getrandbits(bits)
        used += 1
        if value < total:
            return value
    raise RejectionLimit()


class BridgeDP:
    def __init__(self, n, m, endpoint=None):
        self.n, self.m = n, m
        self.endpoint = identity(n) if endpoint is None else tuple(endpoint)
        if not feasible(n, m, self.endpoint):
            raise ValueError("empty endpoint fiber")
        self.h = sum(defect_type(self.endpoint))
        self.max_defect = min(n - 1, (m + self.h) // 2)
        self.types = tuple(type_universe(n, self.max_defect))
        self.transitions = {mu: transition_counts(n, mu) for mu in self.types}
        self.tables = [{} for _ in range(m + 1)]
        self.tables[m][()] = 1
        for i in range(m - 1, -1, -1):
            cap = min(self.h + i, m - i, n - 1)
            following = self.tables[i + 1]
            for mu in self.types:
                d = sum(mu)
                if d > cap or (d - self.h - i) % 2:
                    continue
                count = sum(mult * following.get(nu, 0)
                            for nu, mult in self.transitions[mu].items())
                if count:
                    self.tables[i][mu] = count
        self.count = self.tables[0].get(defect_type(self.endpoint), 0)
        assert self.count > 0
        self.edges = tuple(combinations(range(n), 2))

    def weighted_edges(self, i, residual):
        following = self.tables[i + 1]
        return [(edge, following.get(defect_type(left_transpose(residual, edge)), 0))
                for edge in self.edges]

    def sample(self, rng, accuracy_bits=None):
        """Exact expected time, or TV <=2^-accuracy_bits with bounded trials."""
        attempts = None
        if accuracy_bits is not None:
            if accuracy_bits < 0:
                raise ValueError("nonnegative accuracy_bits required")
            attempts = accuracy_bits + max(1, self.m).bit_length()
        residual, word = self.endpoint, []
        try:
            for i in range(self.m):
                weights = self.weighted_edges(i, residual)
                total = sum(weight for _, weight in weights)
                assert total == self.tables[i][defect_type(residual)]
                ticket = random_below(rng, total, attempts)
                for edge, weight in weights:
                    if ticket < weight:
                        word.append(edge)
                        residual = left_transpose(residual, edge)
                        break
                    ticket -= weight
        except RejectionLimit:
            return valid_word(self.n, self.m, self.endpoint)
        assert residual == identity(self.n)
        assert evaluate(self.n, word) == self.endpoint
        return word

    def word_probability(self, word):
        if len(word) != self.m:
            return Fraction(0)
        residual, probability = self.endpoint, Fraction(1)
        for i, edge in enumerate(word):
            denominator = self.tables[i].get(defect_type(residual), 0)
            residual = left_transpose(residual, edge)
            numerator = self.tables[i + 1].get(defect_type(residual), 0)
            if not denominator or not numerator:
                return Fraction(0)
            probability *= Fraction(numerator, denominator)
        return probability if residual == identity(self.n) else Fraction(0)


def canonical_pattern(word):
    """Sort endpoints numerically before assigning first-appearance names."""
    labels, encoded, pairs = {}, [], []
    for edge in word:
        old_k = len(labels)
        new = []
        for x in sorted(edge):
            if x not in labels:
                labels[x] = len(labels)
                new.append(labels[x])
        if len(new) == 2:
            assert new == [old_k, old_k + 1]
            pairs.append(tuple(new))
        encoded.append(tuple(sorted(labels[x] for x in edge)))
    return tuple(encoded), len(labels), tuple(pairs)


def pattern_words(m, prefix=(), k=0, pairs=()):
    if len(prefix) == m:
        if evaluate(k, prefix) == identity(k):
            yield prefix, k, pairs
        return
    for edge in combinations(range(k), 2):
        yield from pattern_words(m, prefix + (edge,), k, pairs)
    if k < m:
        for a in range(k):
            yield from pattern_words(m, prefix + ((a, k),), k + 1, pairs)
    if k + 2 <= m:
        pair = (k, k + 1)
        yield from pattern_words(m, prefix + (pair,), k + 2, pairs + (pair,))


def pattern_weight(n, k, pairs):
    if k > n:
        return 0
    return math.prod(range(n - k + 1, n + 1)) // (2 ** len(pairs))


def sample_pattern(n, m, rng):
    if not feasible(n, m, identity(n)):
        raise ValueError("empty identity fiber")
    patterns = [(word, k, pairs, pattern_weight(n, k, pairs))
                for word, k, pairs in pattern_words(m)]
    total = sum(weight for _, _, _, weight in patterns)
    ticket = random_below(rng, total)
    for word, k, pairs, weight in patterns:
        if ticket >= weight:
            ticket -= weight
            continue
        # Uniform injection; sort images within the disjoint introduction pairs.
        available, embedding = list(range(n)), []
        for _ in range(k):
            index = random_below(rng, len(available))
            embedding.append(available.pop(index))
        for a, b in pairs:
            if embedding[a] > embedding[b]:
                embedding[a], embedding[b] = embedding[b], embedding[a]
        result = [tuple(sorted((embedding[a], embedding[b]))) for a, b in word]
        assert evaluate(n, result) == identity(n)
        return result
    raise AssertionError("unreachable")


def word_statistics(n, word):
    prefix, prefixes = identity(n), []
    for a, b in word:
        p = list(prefix)
        p[a], p[b] = p[b], p[a]
        prefix = tuple(p)
        prefixes.append(cycle_lengths(prefix))
    parent = list(range(n))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for a, b in word:
        parent[root(a)] = root(b)
    sets = {}
    for x in range(n):
        sets.setdefault(root(x), []).append(x)
    component_weights = Counter(root(a) for a, _ in word)
    weighted = tuple(sorted((tuple(labels), component_weights[r])
                            for r, labels in sets.items()))
    return {
        "prefix_cycle_types": tuple(prefixes),
        "per_position_edges": tuple(word),
        "edge_multiplicities": tuple(sorted(Counter(word).items())),
        "adjacent_repeats": sum(word[i] == word[i + 1]
                                for i in range(len(word) - 1)),
        "weighted_components": weighted,
        "window_products_r2": tuple(cycle_lengths(evaluate(n, word[i:i + 2]))
                                    for i in range(max(0, len(word) - 1))),
    }


def exact_checks():
    results = {"python": platform.python_version(), "dependencies": "standard library",
               "seeds": [7, 20260905, 4103], "transition_checks": [],
               "identity_checks": [], "endpoint_checks": [], "boundary_checks": []}
    for n in range(1, 7):
        checked, types = 0, set()
        for p in permutations(range(n)):
            mu = defect_type(p)
            expected = Counter(defect_type(left_transpose(p, edge))
                               for edge in combinations(range(n), 2))
            actual = transition_counts(n, mu)
            assert expected == actual, (n, p, expected, actual)
            assert sum(actual.values()) == math.comb(n, 2)
            checked += 1
            types.add(mu)
        results["transition_checks"].append({"N": n, "permutations": checked,
                                              "cycle_types": len(types), "ok": True})
    for n, m in [(3, 4), (4, 4), (4, 6)]:
        dp = BridgeDP(n, m)
        words = [word for word in product(dp.edges, repeat=m)
                 if evaluate(n, word) == identity(n)]
        assert len(words) == dp.count
        probability_total = Fraction(0)
        reference_statistics, sampler_statistics = {}, {}
        observed_patterns = Counter()
        for word in words:
            probability = dp.word_probability(word)
            assert probability == Fraction(1, len(words))
            probability_total += probability
            key, k, pairs = canonical_pattern(word)
            observed_patterns[(key, k, pairs)] += 1
            for statistic, value in word_statistics(n, word).items():
                reference_statistics.setdefault(statistic, Counter())[value] += 1
                sampler_statistics.setdefault(statistic, Counter())[value] += probability
        assert probability_total == 1
        for statistic, values in reference_statistics.items():
            assert {key: Fraction(value, len(words)) for key, value in values.items()} == sampler_statistics[statistic]
        predicted_patterns = {(word, k, pairs): pattern_weight(n, k, pairs)
                              for word, k, pairs in pattern_words(m)
                              if k <= n}
        assert dict(observed_patterns) == predicted_patterns
        for seed in results["seeds"]:
            rng = random.Random(seed)
            for _ in range(25):
                assert evaluate(n, dp.sample(rng)) == identity(n)
                assert evaluate(n, dp.sample(rng, accuracy_bits=20)) == identity(n)
                assert evaluate(n, sample_pattern(n, m, rng)) == identity(n)
        results["identity_checks"].append({
            "N": n, "m": m, "words": len(words), "count": dp.count,
            "types_in_universe": len(dp.types),
            "table_entries": sum(map(len, dp.tables)),
            "all_word_probabilities": str(Fraction(1, len(words))),
            "probability_sum": str(probability_total),
            "canonical_patterns": len(predicted_patterns),
            "pattern_weights_exact": True,
            "diagnostic_distribution_cardinalities": {k: len(v) for k, v in reference_statistics.items()},
            "all_exact_diagnostics_match": True,
            "weighted_component_classes": len(reference_statistics["weighted_components"]),
        })
    # Independent word enumeration, including endpoints that are not involutions.
    for n, m in [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 3), (4, 4), (4, 6)]:
        words_by_endpoint = {}
        edges = tuple(combinations(range(n), 2))
        for word in product(edges, repeat=m):
            words_by_endpoint.setdefault(evaluate(n, word), []).append(word)
        probabilities_checked = 0
        for endpoint, words in words_by_endpoint.items():
            dp = BridgeDP(n, m, endpoint)
            assert dp.count == len(words)
            assert evaluate(n, valid_word(n, m, endpoint)) == endpoint
            for word in words:
                assert dp.word_probability(word) == Fraction(1, len(words))
                probabilities_checked += 1
            for seed in results["seeds"]:
                assert evaluate(n, dp.sample(random.Random(seed))) == endpoint
        results["endpoint_checks"].append({"N": n, "m": m,
            "feasible_endpoints": len(words_by_endpoint),
            "all_word_probabilities_checked": probabilities_checked, "ok": True})
    for n in range(1, 6):
        for endpoint in permutations(range(n)):
            h = sum(defect_type(endpoint))
            for m in sorted(set([0, 1, 2, 3, h, h + 1, h + 2, h + 4])):
                if feasible(n, m, endpoint):
                    dp = BridgeDP(n, m, endpoint)
                    assert evaluate(n, valid_word(n, m, endpoint)) == endpoint
                    assert evaluate(n, dp.sample(random.Random(4103))) == endpoint
                else:
                    try:
                        BridgeDP(n, m, endpoint)
                    except ValueError:
                        pass
                    else:
                        raise AssertionError("accepted an empty fiber")
        results["boundary_checks"].append({"N": n, "all_endpoints": math.factorial(n),
            "lengths": "0,1,2,3,h,h+1,h+2,h+4", "ok": True})
    results["minimal_endpoint_checks"] = []
    for n in range(1, 7):
        counts = minimal_cycle_counts(n)
        for endpoint in permutations(range(n)):
            h = sum(defect_type(endpoint))
            assert minimal_completion_count(endpoint, counts) == BridgeDP(n, h, endpoint).count
            assert evaluate(n, sample_minimal(endpoint, random.Random(20260905))) == endpoint
        results["minimal_endpoint_checks"].append({"N": n, "all_endpoints": math.factorial(n),
            "single_cycle_counts": counts[1:], "counts_and_sampler_valid": True})
    # Force every nontrivial random-integer rejection to fail: bounded sampler
    # must still return the requested endpoint, not an error or invalid word.
    class RejectingBits:
        @staticmethod
        def getrandbits(k):
            return (1 << k) - 1
    for endpoint in [identity(3), (1, 2, 0)]:
        dp = BridgeDP(3, 4, endpoint)
        assert evaluate(3, dp.sample(RejectingBits(), accuracy_bits=8)) == endpoint
    results["forced_rejection_fallback"] = "valid endpoints"
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    results = exact_checks()
    results["elapsed_seconds"] = time.perf_counter() - start
    args.output.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps({"status": "passed", "output": str(args.output),
                      "elapsed_seconds": results["elapsed_seconds"]}))


if __name__ == "__main__":
    main()
