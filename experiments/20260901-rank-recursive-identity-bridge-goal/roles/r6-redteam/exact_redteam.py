#!/usr/bin/env python3
"""Independent exact red team for rank disintegration and paired lifts.

This file intentionally imports no implementation from the R1 or R3 lanes.
Permutations are tuples of zero-based images.  ``compose(p,q)`` is p after q,
so displayed products act rightmost-first.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import subprocess
import time
from collections import Counter, defaultdict, deque
from fractions import Fraction
from math import comb, factorial, prod
from pathlib import Path
from typing import Iterable, Sequence

Edge = tuple[int, int]
Permutation = tuple[int, ...]
Word = tuple[Edge, ...]


def identity(n: int) -> Permutation:
    return tuple(range(n))


def compose(p: Permutation, q: Permutation) -> Permutation:
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Permutation) -> Permutation:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def edge(a: int, b: int) -> Edge:
    return (a, b) if a < b else (b, a)


def all_edges(n: int) -> tuple[Edge, ...]:
    return tuple((a, b) for a in range(n) for b in range(a + 1, n))


def edge_perm(n: int, e: Edge) -> Permutation:
    out = list(range(n))
    a, b = e
    out[a], out[b] = out[b], out[a]
    return tuple(out)


def apply_edge(e: Edge, x: int) -> int:
    a, b = e
    if x == a:
        return b
    if x == b:
        return a
    return x


def eval_word(n: int, word: Sequence[Edge]) -> Permutation:
    out = identity(n)
    for e in word:
        out = compose(out, edge_perm(n, e))
    return out


def perm_cycles(p: Permutation) -> list[tuple[int, ...]]:
    seen = [False] * len(p)
    out = []
    for start in range(len(p)):
        if seen[start]:
            continue
        cyc = []
        x = start
        while not seen[x]:
            seen[x] = True
            cyc.append(x)
            x = p[x]
        out.append(tuple(cyc))
    return out


def perm_label(p: Permutation) -> str:
    nontrivial = [c for c in perm_cycles(p) if len(c) > 1]
    if not nontrivial:
        return "e"
    return "".join("(" + " ".join(str(x + 1) for x in c) + ")" for c in nontrivial)


def all_permutations(n: int) -> Iterable[Permutation]:
    yield from itertools.permutations(range(n))


def endpoint_dp(n: int, generators: Sequence[Edge], max_length: int):
    tables = [{identity(n): 1}]
    for _ in range(max_length):
        nxt = defaultdict(int)
        for p, count in tables[-1].items():
            for generator in generators:
                nxt[compose(p, edge_perm(n, generator))] += count
        tables.append(dict(nxt))
    return tables


def enumerate_identity_words(n: int, length: int) -> list[Word]:
    generators = all_edges(n)
    return [
        tuple(word)
        for word in itertools.product(generators, repeat=length)
        if eval_word(n, word) == identity(n)
    ]


def factor_kind(e: Edge, pivot: int) -> str:
    return "B" if pivot in e else "A"


def star_lower(e: Edge, pivot: int) -> int:
    if pivot not in e:
        raise ValueError("not a star factor")
    return e[0] if e[1] == pivot else e[1]


def stable_sort_independent(n: int, word: Word):
    """Bubble B-A inversions via tau_i*a = a*tau_(a^{-1}(i))."""
    pivot = n - 1
    items = [(factor_kind(e, pivot), e) for e in word]
    rewrites = 0
    while True:
        found = False
        for j in range(len(items) - 1):
            if items[j][0] == "B" and items[j + 1][0] == "A":
                star = items[j][1]
                old = items[j + 1][1]
                lower = star_lower(star, pivot)
                new_star = edge(apply_edge(old, lower), pivot)
                items[j] = ("A", old)
                items[j + 1] = ("B", new_star)
                rewrites += 1
                found = True
                break
        if not found:
            break
    old = tuple(e for kind, e in items if kind == "A")
    star = tuple(e for kind, e in items if kind == "B")
    return old, star, rewrites


def inverse_stable_sort_independent(n: int, old: Word, star: Word, pattern: str) -> Word:
    pivot = n - 1
    items = [("A", e) for e in old] + [("B", e) for e in star]
    if pattern.count("A") != len(old) or pattern.count("B") != len(star):
        raise ValueError("pattern has wrong inventory")
    for pos, wanted in enumerate(pattern):
        if wanted == "A":
            if items[pos][0] != "A":
                raise AssertionError("inverse stable-sort scan invariant failed")
            continue
        location = next(j for j in range(pos, len(items)) if items[j][0] == "B")
        while location > pos:
            old_edge = items[location - 1][1]
            star_edge = items[location][1]
            lower = star_lower(star_edge, pivot)
            new_star = edge(apply_edge(old_edge, lower), pivot)
            items[location - 1] = ("B", new_star)
            items[location] = ("A", old_edge)
            location -= 1
    return tuple(e for _, e in items)


def r1_roundtrip_and_coeff_checks(max_n: int = 4, max_length: int = 6):
    roundtrips = 0
    rewrite_steps = 0
    coefficient_checks = 0
    case_records = []
    for n in range(2, max_n + 1):
        full_generators = all_edges(n)
        full_dp = endpoint_dp(n, full_generators, max_length)
        old_generators = tuple(e for e in full_generators if n - 1 not in e)
        star_generators = tuple(e for e in full_generators if n - 1 in e)
        old_dp = endpoint_dp(n, old_generators, max_length)
        star_dp = endpoint_dp(n, star_generators, max_length)
        h_values = [tuple(p) + (n - 1,) for p in all_permutations(n - 1)]
        for length in range(max_length + 1):
            words_checked = 0
            for word in itertools.product(full_generators, repeat=length):
                word = tuple(word)
                pattern = "".join(factor_kind(e, n - 1) for e in word)
                old, star, rewrites = stable_sort_independent(n, word)
                reconstructed = inverse_stable_sort_independent(n, old, star, pattern)
                assert reconstructed == word
                assert eval_word(n, word) == compose(eval_word(n, old), eval_word(n, star))
                inversion_count = sum(
                    pattern[i] == "B" and pattern[j] == "A"
                    for i in range(length)
                    for j in range(i + 1, length)
                )
                assert rewrites == inversion_count
                roundtrips += 1
                rewrite_steps += rewrites
                words_checked += 1
            for g in all_permutations(n):
                rhs = 0
                for k in range(length + 1):
                    for h in h_values:
                        q = compose(inverse(h), g)
                        rhs += (
                            comb(length, k)
                            * old_dp[length - k].get(h, 0)
                            * star_dp[k].get(q, 0)
                        )
                assert rhs == full_dp[length].get(g, 0), (n, length, g, rhs)
                coefficient_checks += 1
            case_records.append(
                {
                    "N": n,
                    "L": length,
                    "all_words_roundtripped": words_checked,
                    "reachable_endpoints": len(full_dp[length]),
                }
            )
    return {
        "roundtrip_words": roundtrips,
        "adjacent_rewrites": rewrite_steps,
        "all_endpoint_coefficient_checks": coefficient_checks,
        "cases": case_records,
    }


def _f_series(scale: int, degree: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(degree + 1)]
    for d in range(0, degree + 1, 2):
        out[d] = Fraction(scale**d, 2**d * factorial(d + 1))
    return out


def _poly_mul(a: Sequence[Fraction], b: Sequence[Fraction], degree: int):
    out = [Fraction(0) for _ in range(degree + 1)]
    for i, ai in enumerate(a):
        if not ai:
            continue
        for j, bj in enumerate(b[: degree - i + 1]):
            if bj:
                out[i + j] += ai * bj
    return out


def transitive_formula_count(parts: Sequence[int], k: int) -> int:
    n = sum(parts)
    excess = k - (n + len(parts) - 2)
    if excess < 0 or excess % 2:
        return 0
    if n == 1:
        return int(tuple(parts) == (1,) and k == 0)
    polynomial = [Fraction(1)] + [Fraction(0)] * excess
    for scale in [1] * (n - 2) + list(parts):
        polynomial = _poly_mul(polynomial, _f_series(scale, excess), excess)
    value = Fraction(factorial(k) * prod(parts), factorial(n)) * polynomial[excess]
    assert value.denominator == 1
    return value.numerator


def minimal_star_length(q: Permutation) -> int:
    pivot = len(q) - 1
    total = 0
    for cyc in perm_cycles(q):
        if pivot in cyc:
            total += len(cyc) - 1
        elif len(cyc) > 1:
            total += len(cyc) + 1
    return total


def star_formula_count(n: int, k: int, q: Permutation) -> int:
    minimum = minimal_star_length(q)
    if k < minimum or (k - minimum) % 2:
        return 0
    pivot = n - 1
    mandatory = []
    optional = 0
    for cyc in perm_cycles(q):
        if len(cyc) > 1 or pivot in cyc:
            mandatory.append(len(cyc))
        else:
            optional += 1
    return sum(
        comb(optional, s) * transitive_formula_count(tuple(mandatory) + (1,) * s, k)
        for s in range(optional + 1)
    )


def fraction_record(value: Fraction):
    return {"numerator": value.numerator, "denominator": value.denominator}


def star_formula_checks(star_jsonl: Path, max_n: int = 5, max_k: int = 6):
    endpoint_checks = 0
    recurrence_checks = 0
    boundary_checks = []
    with star_jsonl.open("w") as handle:
        for n in range(2, max_n + 1):
            generators = tuple((i, n - 1) for i in range(n - 1))
            direct = endpoint_dp(n, generators, max_k)
            for q in all_permutations(n):
                minimum = minimal_star_length(q)
                for k in range(max_k + 1):
                    actual = direct[k].get(q, 0)
                    formula = star_formula_count(n, k, q)
                    assert actual == formula, (n, k, q, actual, formula)
                    feasible = k >= minimum and (k - minimum) % 2 == 0
                    assert feasible == (actual > 0)
                    if k:
                        child_sum = sum(
                            direct[k - 1].get(compose(q, edge_perm(n, generator)), 0)
                            for generator in generators
                        )
                        assert child_sum == actual
                        recurrence_checks += 1
                    record = {
                        "N": n,
                        "k": k,
                        "endpoint_images": list(q),
                        "endpoint": perm_label(q),
                        "minimum_star_length": minimum,
                        "feasible": feasible,
                        "direct_count": actual,
                        "support_formula_count": formula,
                    }
                    handle.write(json.dumps(record, sort_keys=True) + "\n")
                    endpoint_checks += 1
                    if n == 2 or k in (0, minimum, minimum + 2):
                        boundary_checks.append(record)
    return {
        "endpoint_formula_checks": endpoint_checks,
        "last_factor_recurrence_checks": recurrence_checks,
        "boundary_records_retained": len(boundary_checks),
        "all_passed": True,
    }


def boundary_case_summary():
    records = []
    for n in (2, 3):
        full = endpoint_dp(n, all_edges(n), 6)
        for length in range(7):
            records.append(
                {
                    "kind": "full_identity_fiber",
                    "N": n,
                    "L": length,
                    "count": full[length].get(identity(n), 0),
                    "parity_expected_empty": bool(length % 2),
                }
            )
    fixtures = [
        (2, identity(2), "N2_identity"),
        (2, (1, 0), "N2_transposition"),
        (3, (1, 0, 2), "lower_transposition"),
        (3, (2, 1, 0), "pivot_transposition"),
        (3, (1, 2, 0), "three_cycle"),
    ]
    for n, q, name in fixtures:
        direct = endpoint_dp(n, tuple((i, n - 1) for i in range(n - 1)), 6)
        for k in range(7):
            records.append(
                {
                    "kind": "star_endpoint_fiber",
                    "name": name,
                    "N": n,
                    "k": k,
                    "endpoint": perm_label(q),
                    "minimum": minimal_star_length(q),
                    "count": direct[k].get(q, 0),
                }
            )
    return records


def branch_law_case(n: int, length: int):
    identity_words = enumerate_identity_words(n, length)
    direct = Counter()
    for word in identity_words:
        old, star, _ = stable_sort_independent(n, word)
        h = eval_word(n, old)
        direct[(len(star), h)] += 1

    full_generators = all_edges(n)
    old_generators = tuple(e for e in full_generators if n - 1 not in e)
    star_generators = tuple(e for e in full_generators if n - 1 in e)
    old_dp = endpoint_dp(n, old_generators, length)
    star_dp = endpoint_dp(n, star_generators, length)
    h_values = [tuple(p) + (n - 1,) for p in all_permutations(n - 1)]
    records = []
    for k in range(length + 1):
        for h in h_values:
            old_count = old_dp[length - k].get(h, 0)
            q = inverse(h)
            star_count = star_dp[k].get(q, 0)
            predicted = comb(length, k) * old_count * star_count
            observed = direct.get((k, h), 0)
            assert predicted == observed, (n, length, k, h, predicted, observed)
            if predicted:
                records.append(
                    {
                        "N": n,
                        "L": length,
                        "k": k,
                        "h_images": list(h),
                        "h": perm_label(h),
                        "old_fiber_size": old_count,
                        "star_endpoint_images": list(q),
                        "star_fiber_size": star_count,
                        "patterns": comb(length, k),
                        "branch_count": predicted,
                        "probability": fraction_record(Fraction(predicted, len(identity_words))),
                    }
                )
    assert sum(x["branch_count"] for x in records) == len(identity_words)
    k_marginal = Counter()
    for record in records:
        k_marginal[record["k"]] += record["branch_count"]
    return {
        "N": n,
        "L": length,
        "identity_fiber_size": len(identity_words),
        "branches": records,
        "k_marginal": [
            {
                "k": k,
                "count": count,
                "probability": fraction_record(Fraction(count, len(identity_words))),
            }
            for k, count in sorted(k_marginal.items())
        ],
    }


def support_signature(n: int, word: Word):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for a, b in set(word):
        union(a, b)
    vertices = Counter(find(x) for x in range(n))
    weights = Counter()
    for a, _ in word:
        weights[find(a)] += 1
    return tuple(sorted((vertices[root], weights[root]) for root in vertices))


def word_observables(n: int, word: Word):
    multiplicities = Counter(word)
    return {
        "distinct_edges": len(multiplicities),
        "edge_multiplicity_partition": tuple(sorted(multiplicities.values(), reverse=True)),
        "adjacent_repeats": sum(word[j] == word[j + 1] for j in range(len(word) - 1)),
        "support_signature": support_signature(n, word),
        "single_edge_word": len(multiplicities) == 1,
    }


def conjugate_word(word: Word, sigma: Permutation) -> Word:
    return tuple(edge(sigma[a], sigma[b]) for a, b in word)


def pair_insert_weights(n: int, length: int):
    if length < 2:
        raise ValueError("pair insertion needs length at least two")
    lower = enumerate_identity_words(n - 1, length - 2)
    if not lower:
        return {}, 0
    weights = Counter()
    for old_word in lower:
        for i in range(n - 1):
            pair = ((i, n - 1), (i, n - 1))
            for gap in range(length - 1):
                output = old_word[:gap] + pair + old_word[gap:]
                assert eval_word(n, output) == identity(n)
                weights[output] += 1
    denominator = len(lower) * (n - 1) * (length - 1)
    assert sum(weights.values()) == denominator
    return dict(weights), denominator


def symmetrize_weights(n: int, weights: dict[Word, int], denominator: int):
    out = Counter()
    permutations = list(all_permutations(n))
    for word, weight in weights.items():
        for sigma in permutations:
            out[conjugate_word(word, sigma)] += weight
    return dict(out), denominator * len(permutations)


def weights_to_distribution(weights: dict[Word, int], denominator: int):
    return {word: Fraction(weight, denominator) for word, weight in weights.items() if weight}


def uniform_distribution(words: Sequence[Word]):
    return {word: Fraction(1, len(words)) for word in words}


def total_variation(p: dict[Word, Fraction], q: dict[Word, Fraction]):
    return Fraction(1, 2) * sum(abs(p.get(x, 0) - q.get(x, 0)) for x in set(p) | set(q))


def integer_weight_tv(left: Counter, right: Counter):
    left_total = sum(left.values())
    right_total = sum(right.values())
    assert left_total and right_total
    return Fraction(1, 2) * sum(
        abs(Fraction(left[x], left_total) - Fraction(right[x], right_total))
        for x in set(left) | set(right)
    )


def two_sided_branch_weights(n: int, length: int, g: Permutation, old_dp, star_dp):
    """Independent reconstruction of the R2 exact and flattened branch laws."""
    hs = [tuple(p) + (n - 1,) for p in all_permutations(n - 1)]
    exact = Counter()
    approximate = Counter()
    old_degree = comb(n - 1, 2)
    star_degree = n - 1
    for k in range(length + 1):
        s = length - k
        for h in hs:
            q = compose(inverse(h), g)
            exact_weight = (
                comb(length, k) * old_dp[s].get(h, 0) * star_dp[k].get(q, 0)
            )
            if exact_weight:
                exact[(k, h)] = exact_weight
            if s >= k:
                approximate_weight = (
                    n
                    * comb(length, k)
                    * old_degree**s
                    * star_dp[k].get(q, 0)
                )
            else:
                approximate_weight = (
                    comb(length, k)
                    * old_dp[s].get(h, 0)
                    * star_degree**k
                )
            if approximate_weight:
                approximate[(k, h)] = approximate_weight
    return exact, approximate


def _old_pointwise_delta(rank: int, length: int):
    if rank <= 2:
        return Fraction(0)
    if rank == 3:
        return Fraction(factorial(rank) - 2, 2) if length == 0 else Fraction(0)
    return Fraction(factorial(rank) - 2, 2) * Fraction(rank - 3, rank - 1) ** length


def _star_pointwise_delta(rank: int, length: int):
    if rank <= 2:
        return Fraction(0)
    return Fraction(factorial(rank) - 2, 2) * Fraction(rank - 2, rank - 1) ** length


def two_sided_theorem_bound(n: int, length: int):
    if n == 2:
        return Fraction(0)
    delta = max(
        _old_pointwise_delta(n - 1, (length + 1) // 2),
        _star_pointwise_delta(n, length // 2 + 1),
    )
    return None if delta >= 1 else delta / (1 - delta)


def r2_candidate_audit():
    small = []
    for n, length in ((3, 4), (4, 4), (4, 6)):
        old = tuple(e for e in all_edges(n) if n - 1 not in e)
        star = tuple(e for e in all_edges(n) if n - 1 in e)
        old_dp = endpoint_dp(n, old, length)
        star_dp = endpoint_dp(n, star, length)
        exact, approximate = two_sided_branch_weights(
            n, length, identity(n), old_dp, star_dp
        )
        small.append(
            {
                "N": n,
                "L": length,
                "endpoint": "e",
                "exact_normalizer": sum(exact.values()),
                "scaled_approximate_normalizer": sum(approximate.values()),
                "tv": fraction_record(integer_weight_tv(exact, approximate)),
            }
        )

    dense = []
    for n in (4, 5):
        length = 2 * n**3
        old = tuple(e for e in all_edges(n) if n - 1 not in e)
        star = tuple(e for e in all_edges(n) if n - 1 in e)
        old_dp = endpoint_dp(n, old, length)
        star_dp = endpoint_dp(n, star, length)
        maximum = Fraction(0)
        maximizer = None
        checked = 0
        for g in all_permutations(n):
            # Dense even length: exactly the even endpoints are feasible.
            if (n - len(perm_cycles(g))) % 2:
                continue
            exact, approximate = two_sided_branch_weights(n, length, g, old_dp, star_dp)
            tv = integer_weight_tv(exact, approximate)
            if tv > maximum:
                maximum = tv
                maximizer = g
            checked += 1
        bound = two_sided_theorem_bound(n, length)
        assert bound is not None and maximum <= bound
        dense.append(
            {
                "N": n,
                "L": length,
                "feasible_endpoints_checked": checked,
                "maximum_tv": fraction_record(maximum),
                "maximum_endpoint_images": list(maximizer) if maximizer is not None else None,
                "pointwise_normalization_bound": fraction_record(bound),
            }
        )
    return {
        "candidate": "two-sided old/star parity flattening",
        "small_identity_cases": small,
        "dense_every_feasible_endpoint_cases": dense,
        "all_checks_passed": True,
    }


def conjugate_edge_by(e: Edge, by: Edge) -> Edge:
    return edge(apply_edge(by, e[0]), apply_edge(by, e[1]))


def hurwitz_neighbor(word: Word, position: int, direction: int) -> Word:
    a, b = word[position], word[position + 1]
    if direction == 1:
        replacement = (b, conjugate_edge_by(a, b))
    elif direction == -1:
        replacement = (conjugate_edge_by(b, a), a)
    else:
        raise ValueError("direction must be +/-1")
    return word[:position] + replacement + word[position + 2 :]


def lazy_symmetric_hurwitz_step(distribution: dict[Word, Fraction]):
    if not distribution:
        return {}
    length = len(next(iter(distribution)))
    if length < 2:
        return dict(distribution)
    out = defaultdict(Fraction)
    move_probability = Fraction(1, 4 * (length - 1))
    for word, probability in distribution.items():
        out[word] += probability / 2
        for position in range(length - 1):
            for direction in (-1, 1):
                neighbor = hurwitz_neighbor(word, position, direction)
                assert eval_word(max(max(e) for e in word) + 1, neighbor) == eval_word(
                    max(max(e) for e in word) + 1, word
                )
                out[neighbor] += probability * move_probability
    assert sum(out.values()) == 1
    return dict(out)


def hurwitz_components(words: Sequence[Word]):
    word_set = set(words)
    component_of = {}
    components = []
    for root in words:
        if root in component_of:
            continue
        cid = len(components)
        queue = deque([root])
        component_of[root] = cid
        members = []
        while queue:
            word = queue.popleft()
            members.append(word)
            for position in range(len(word) - 1):
                for direction in (-1, 1):
                    neighbor = hurwitz_neighbor(word, position, direction)
                    assert neighbor in word_set
                    if neighbor not in component_of:
                        component_of[neighbor] = cid
                        queue.append(neighbor)
        components.append(tuple(members))
    return component_of, components


def orbit_uniformize(distribution, component_of, components):
    masses = defaultdict(Fraction)
    for word, probability in distribution.items():
        masses[component_of[word]] += probability
    out = {}
    for cid, members in enumerate(components):
        if masses[cid]:
            probability = masses[cid] / len(members)
            for word in members:
                out[word] = probability
    return out, masses


def observable_distribution(n: int, distribution, key: str):
    out = defaultdict(Fraction)
    for word, probability in distribution.items():
        value = word_observables(n, word)[key]
        out[value] += probability
    return dict(out)


def jsonable_value(value):
    if isinstance(value, tuple):
        return [jsonable_value(x) for x in value]
    return value


def observable_records(n: int, distribution, key: str):
    dist = observable_distribution(n, distribution, key)
    return [
        {"value": jsonable_value(value), "probability": fraction_record(probability)}
        for value, probability in sorted(dist.items(), key=lambda item: repr(item[0]))
    ]


def paired_architecture_case(n: int, length: int, hurwitz_times=(0, 1, 2, 4)):
    target_words = enumerate_identity_words(n, length)
    target = uniform_distribution(target_words)
    pair_weights, pair_denominator = pair_insert_weights(n, length)
    pair = weights_to_distribution(pair_weights, pair_denominator)
    sym_weights, sym_denominator = symmetrize_weights(n, pair_weights, pair_denominator)
    sym = weights_to_distribution(sym_weights, sym_denominator)
    component_of, components = hurwitz_components(target_words)

    pair_components = {component_of[word] for word in pair}
    sym_components = {component_of[word] for word in sym}
    ideal, component_masses = orbit_uniformize(sym, component_of, components)
    target_component_mass = {
        cid: Fraction(len(members), len(target_words)) for cid, members in enumerate(components)
    }
    component_tv = Fraction(1, 2) * sum(
        abs(component_masses.get(cid, 0) - target_component_mass[cid])
        for cid in range(len(components))
    )
    assert component_tv == total_variation(ideal, target)

    target_macros = observable_distribution(n, target, "support_signature")
    sym_macros = observable_distribution(n, sym, "support_signature")
    pair_macros = set(sym_macros)
    missing_macro_mass = sum(
        probability for macro, probability in target_macros.items() if macro not in pair_macros
    )
    overweighted_macros = {
        macro
        for macro in set(target_macros) | set(sym_macros)
        if sym_macros.get(macro, 0) > target_macros.get(macro, 0)
    }
    overweighted_sym_probability = sum(sym_macros.get(macro, 0) for macro in overweighted_macros)
    overweighted_target_probability = sum(
        target_macros.get(macro, 0) for macro in overweighted_macros
    )
    overweighted_gap = overweighted_sym_probability - overweighted_target_probability
    macro_tv = Fraction(1, 2) * sum(
        abs(sym_macros.get(macro, 0) - target_macros.get(macro, 0))
        for macro in set(target_macros) | set(sym_macros)
    )
    assert overweighted_gap == macro_tv
    single_target = observable_distribution(n, target, "single_edge_word").get(True, 0)
    single_sym = observable_distribution(n, sym, "single_edge_word").get(True, 0)
    assert single_sym == 0

    finite = []
    current = sym
    for step in range(max(hurwitz_times) + 1):
        if step in hurwitz_times:
            single = observable_distribution(n, current, "single_edge_word").get(True, 0)
            assert single == 0
            finite.append(
                {
                    "steps": step,
                    "support_size": len(current),
                    "tv_to_uniform": fraction_record(total_variation(current, target)),
                    "single_edge_probability": fraction_record(single),
                }
            )
        if step < max(hurwitz_times):
            current = lazy_symmetric_hurwitz_step(current)

    return {
        "N": n,
        "L": length,
        "target_size": len(target_words),
        "pair_source_outcomes": pair_denominator,
        "pair_output_support": len(pair),
        "symmetrized_source_outcomes": sym_denominator,
        "symmetrized_output_support": len(sym),
        "hurwitz_components": len(components),
        "pair_components_occupied": len(pair_components),
        "symmetrized_components_occupied": len(sym_components),
        "adjacent_pair_tv": fraction_record(total_variation(pair, target)),
        "symmetrized_pair_tv": fraction_record(total_variation(sym, target)),
        "finite_hurwitz": finite,
        "ideal_orbit_uniformized_tv": fraction_record(total_variation(ideal, target)),
        "component_mass_tv": fraction_record(component_tv),
        "target_mass_of_macrotypes_absent_from_pair_lift": fraction_record(missing_macro_mass),
        "overweighted_support_macro_event": {
            "signatures": [jsonable_value(x) for x in sorted(overweighted_macros)],
            "under_symmetrized_pair": fraction_record(overweighted_sym_probability),
            "under_uniform_target": fraction_record(overweighted_target_probability),
            "probability_gap": fraction_record(overweighted_gap),
            "hurwitz_invariant": True,
        },
        "support_macro_tv_lower_bound_all_hurwitz_times": fraction_record(macro_tv),
        "single_edge_event": {
            "under_symmetrized_pair": fraction_record(single_sym),
            "under_uniform_target": fraction_record(single_target),
            "persistent_all_hurwitz_times": True,
        },
        "target_support_signatures": observable_records(n, target, "support_signature"),
        "symmetrized_support_signatures": observable_records(n, sym, "support_signature"),
        "target_edge_multiplicity_partitions": observable_records(
            n, target, "edge_multiplicity_partition"
        ),
        "symmetrized_edge_multiplicity_partitions": observable_records(
            n, sym, "edge_multiplicity_partition"
        ),
    }


def branch_jsonl_write(path: Path, cases):
    with path.open("w") as handle:
        for case in cases:
            for branch in case["branches"]:
                handle.write(json.dumps(branch, sort_keys=True) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    started = time.time()

    r1 = r1_roundtrip_and_coeff_checks()
    star = star_formula_checks(output_dir / "star_fibers.jsonl")
    branch_cases = [branch_law_case(*case) for case in ((3, 4), (4, 4), (4, 6))]
    branch_jsonl_write(output_dir / "branch_laws.jsonl", branch_cases)
    paired = [paired_architecture_case(*case) for case in ((3, 4), (4, 4), (4, 6))]

    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        commit = "unavailable"
    payload = {
        "metadata": {
            "repository_commit": commit,
            "command": f"python3 {Path(__file__).as_posix()} --output-dir {output_dir.as_posix()}",
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "nonstandard_dependencies": [],
            "random_seed": None,
            "deterministic": True,
            "elapsed_seconds": time.time() - started,
        },
        "convention": "(p q)(x)=p(q(x)); displayed word products act rightmost-first",
        "r1_independent_checks": r1,
        "r3_independent_checks": star,
        "boundary_cases": boundary_case_summary(),
        "r2_candidate_independent_audit": r2_candidate_audit(),
        "branch_law_cases": branch_cases,
        "paired_architecture_cases": paired,
    }
    (output_dir / "results.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        "r6 exact red team passed: "
        f"{r1['roundtrip_words']} R1 round trips, "
        f"{star['endpoint_formula_checks']} R3 endpoint counts, "
        f"{sum(x['identity_fiber_size'] for x in branch_cases)} branch words"
    )
    for case in paired:
        tv = case["ideal_orbit_uniformized_tv"]
        print(
            f"N={case['N']} L={case['L']} components={case['hurwitz_components']} "
            f"ideal-orbit TV={tv['numerator']}/{tv['denominator']}"
        )
    print(f"wrote {output_dir / 'results.json'}")


if __name__ == "__main__":
    main()
