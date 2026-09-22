#!/usr/bin/env python3
"""Exact finite checks for the blind genus-zero/one cut-and-join sampler.

No project mathematical implementation is imported. Vertices are zero based.
Products act rightmost first: appending (a,b) swaps p[a] and p[b].
All validation conclusions are finite exact identities, not asymptotic evidence.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
import json
from math import comb, factorial, prod
from pathlib import Path
import platform
import random
import time


def right_t(p, t):
    q = list(p)
    a, b = t
    q[a], q[b] = q[b], q[a]
    return tuple(q)


def cycles(p):
    seen = set()
    result = []
    for a in range(len(p)):
        if a in seen:
            continue
        c = []
        b = a
        while b not in seen:
            c.append(b)
            seen.add(b)
            b = p[b]
        result.append(tuple(c))
    return tuple(result)


def union(part, a, b):
    x, y = sorted((part[a], part[b]))
    return tuple(x if c == y else c for c in part)


def elementary(alpha):
    e = [1]
    for a in alpha:
        e.append(0)
        for j in range(len(e)-1, 0, -1):
            e[j] += a * e[j-1]
    return e


def qfactor(alpha):
    return prod((Fraction(a**a, factorial(a-1)) for a in alpha), start=Fraction(1))


def f0(n, k):
    return Fraction(n)**(k-3)


def f1_aggregate(n, k, e):
    """e[j] is sum e_j over a family; e[0] is its cardinality."""
    v = e[0] * (n**k - n**(k-1))
    for j in range(2, k+1):
        v -= factorial(j-2) * e[j] * n**(k-j)
    return Fraction(v, 24)


@lru_cache(None)
def connected_count(alpha, g):
    alpha = tuple(alpha)
    if g not in (0, 1):
        return 0
    n, k = sum(alpha), len(alpha)
    if not n:
        raise ValueError('empty vertex set is outside the sampler domain')
    r = n+k+2*g-2
    if r < 0:
        return 0
    f = f0(n, k) if g == 0 else f1_aggregate(n, k, elementary(alpha))
    answer = factorial(r) * qfactor(alpha) * f
    assert answer.denominator == 1 and answer >= 0, (alpha, g, answer)
    return answer.numerator


def polynomial_add_scaled(dst, src, a=0):
    """Add src*(1+a*x), preserving exact coefficients."""
    size = len(src) + bool(a)
    if len(dst) < size:
        dst.extend([0] * (size-len(dst)))
    for j, c in enumerate(src):
        dst[j] += c
        if a:
            dst[j+1] += a*c


def allocation_mass(left, right, free, g_left, g_right):
    """Total integer number of shuffled pairs over all free-cycle allocations.

    left and right contain the lengths of labeled cycles forced to each side;
    both are nonempty. free contains the lengths of distinct undecided cycles.
    Equal cycle lengths still represent separate labeled cycles.
    """
    assert left and right and g_left + g_right <= 1
    all_cycles = tuple(left) + tuple(right) + tuple(free)
    n, k = sum(all_cycles), len(all_cycles)
    state = {(sum(left), len(left)): [elementary(left), elementary(right)]}
    for a in free:
        new = {}
        for (s, q), (ea, eb) in state.items():
            da, db = new.setdefault((s+a, q+1), [[], []])
            polynomial_add_scaled(da, ea, a)
            polynomial_add_scaled(db, eb)
            da, db = new.setdefault((s, q), [[], []])
            polynomial_add_scaled(da, ea)
            polynomial_add_scaled(db, eb, a)
        state = new
    total = Fraction(0)
    for (s, q), (ea, eb) in state.items():
        assert ea[0] == eb[0]
        if g_left:
            contribution = f1_aggregate(s, q, ea) * f0(n-s, k-q)
        elif g_right:
            contribution = f0(s, q) * f1_aggregate(n-s, k-q, eb)
        else:
            contribution = ea[0] * f0(s, q) * f0(n-s, k-q)
        assert contribution >= 0
        total += contribution
    r = n+k+2*(g_left+g_right)-4
    result = factorial(r) * qfactor(all_cycles) * total
    assert result.denominator == 1 and result >= 0, (left, right, free, g_left, g_right, result)
    return result.numerator


def allocation_mass_bruteforce(left, right, free, g_left, g_right):
    total = 0
    for mask in product((0, 1), repeat=len(free)):
        aa = tuple(left) + tuple(a for a, side in zip(free, mask) if side == 0)
        bb = tuple(right) + tuple(a for a, side in zip(free, mask) if side == 1)
        ra, rb = sum(aa)+len(aa)+2*g_left-2, sum(bb)+len(bb)+2*g_right-2
        total += comb(ra+rb, ra) * connected_count(aa, g_left) * connected_count(bb, g_right)
    return total


def branches(p, g):
    """Return exact disjoint last-edge branches and their integer weights."""
    cs = cycles(p)
    which = {a:i for i, c in enumerate(cs) for a in c}
    out = []
    for t in combinations(range(len(p)), 2):
        rho = right_t(p, t)
        rc = cycles(rho)
        if which[t[0]] != which[t[1]]:
            w = connected_count(tuple(map(len, rc)), g)
            if w:
                out.append((('connected', t, g), w))
        else:
            if g:
                w = connected_count(tuple(map(len, rc)), g-1)
                if w:
                    out.append((('connected', t, g-1), w))
            ca = next(c for c in rc if t[0] in c)
            cb = next(c for c in rc if t[1] in c)
            free = tuple(c for c in rc if c != ca and c != cb)
            for ga, gb in ((0, 0),) if not g else ((0, 1), (1, 0)):
                w = allocation_mass((len(ca),), (len(cb),), tuple(map(len, free)), ga, gb)
                if w:
                    out.append((('disconnected', t, ga, gb), w))
    return out


def partition_profiles(n, minimum=1):
    if n == 0:
        yield ()
    for a in range(minimum, n+1):
        for tail in partition_profiles(n-a, a):
            yield (a,) + tail


def check_allocations(limit):
    cases = 0
    for n in range(2, limit+1):
        for profile in partition_profiles(n):
            if len(profile) < 2:
                continue
            # Every pair of distinct labeled anchor cycles, including equal sizes.
            for i, j in combinations(range(len(profile)), 2):
                a, b = profile[i], profile[j]
                free = tuple(x for h, x in enumerate(profile) if h not in (i, j))
                for ga, gb in ((0, 0), (1, 0), (0, 1)):
                    got = allocation_mass((a,), (b,), free, ga, gb)
                    want = allocation_mass_bruteforce((a,), (b,), free, ga, gb)
                    assert got == want, (profile, i, j, ga, gb, got, want)
                    # Falsify conditional normalization on every one-step branch.
                    if free:
                        x, rest = free[0], free[1:]
                        left_mass = allocation_mass((a, x), (b,), rest, ga, gb)
                        right_mass = allocation_mass((a,), (b, x), rest, ga, gb)
                        assert got == left_mass + right_mass
                    cases += 1
    return {'test':'allocation_dp','maximum_total_vertices':limit,'exact_cases':cases,'result':'pass'}


def finite_reference(n):
    """Exact word-count DP using (endpoint, actual support partition)."""
    start = (tuple(range(n)), tuple(range(n)))
    levels = [{start:1}]
    trans = tuple(combinations(range(n), 2))
    for r in range(1, 2*n+1):
        nxt = defaultdict(int)
        for (p, part), count in levels[-1].items():
            for t in trans:
                nxt[right_t(p, t), union(part, *t)] += count
        levels.append(dict(nxt))
    return levels


def restrict_permutation(p, vertices):
    order = tuple(sorted(vertices))
    relabel = {a:i for i,a in enumerate(order)}
    return tuple(relabel[p[a]] for a in order), order


def check_endpoint_counts(n):
    levels = finite_reference(n)
    checked = 0
    branch_checked = 0
    for g in (0, 1):
        # All endpoints, not merely one representative per cycle type.
        for r, level in enumerate(levels):
            for (p, part), want in level.items():
                if len(set(part)) != 1 or r != n+len(cycles(p))+2*g-2:
                    continue
                got = connected_count(tuple(map(len, cycles(p))), g)
                assert got == want, (n, r, p, g, got, want)
                if r:
                    expected = defaultdict(int)
                    for (rho, old_part), count in levels[r-1].items():
                        for t in combinations(range(n), 2):
                            if right_t(rho, t) != p or len(set(union(old_part, *t))) != 1:
                                continue
                            comps = sorted(set(old_part))
                            if len(comps) == 1:
                                childg = (r-1-n-len(cycles(rho))+2)//2
                                expected['connected', t, childg] += count
                            else:
                                assert len(comps) == 2
                                aa = tuple(a for a in range(n) if old_part[a] == old_part[t[0]])
                                bb = tuple(a for a in range(n) if old_part[a] == old_part[t[1]])
                                # Genus assignment needs factor lengths. The state DP
                                # forgets these, so compare the sum over assignments.
                                assert set(aa).isdisjoint(bb)
                                expected['disconnected', t] += count
                    actual = defaultdict(int)
                    for key, weight in branches(p, g):
                        actual[key if key[0] == 'connected' else key[:2]] += weight
                    assert dict(actual) == dict(expected), (n, r, p, g, actual, expected)
                    assert sum(actual.values()) == want
                    branch_checked += len(actual)
                checked += 1
    # Include structural zeros and every boundary length.
    summary = []
    for r, level in enumerate(levels):
        identity = sum(c for (p, part), c in level.items() if p == tuple(range(n)))
        connected_identity = sum(c for (p, part), c in level.items() if p == tuple(range(n)) and len(set(part)) == 1)
        summary.append({'length':r,'identity_count':identity,'connected_identity_count':connected_identity,'dp_states':len(level)})
    return {'test':'endpoint_and_branch_counts','n':n,'endpoints_checked':checked,'last_edge_branches_checked':branch_checked,'by_length':summary,'result':'pass'}


def uniform_int(bound, rng):
    assert bound > 0
    if bound == 1:
        return 0
    bits = (bound-1).bit_length()
    while True:
        x = rng.getrandbits(bits)
        if x < bound:
            return x


def weighted_choice(items, rng):
    items = [(x, w) for x, w in items if w]
    x = uniform_int(sum(w for _, w in items), rng)
    for a, w in items:
        if x < w:
            return a
        x -= w
    raise AssertionError('unreachable')


def sampler(p, g, rng):
    n = len(p)
    r = n+len(cycles(p))+2*g-2
    assert connected_count(tuple(map(len, cycles(p))), g) > 0
    if r == 0:
        assert n == 1 and g == 0
        return ()
    candidates = branches(p, g)
    assert sum(w for _, w in candidates) == connected_count(tuple(map(len, cycles(p))), g)
    branch = weighted_choice(candidates, rng)
    kind, t = branch[:2]
    rho = right_t(p, t)
    if kind == 'connected':
        return sampler(rho, branch[2], rng) + (t,)
    ga, gb = branch[2:]
    rc = cycles(rho)
    aa = [next(c for c in rc if t[0] in c)]
    bb = [next(c for c in rc if t[1] in c)]
    free = [c for c in rc if c not in aa and c not in bb]
    while free:
        c, *rest = free
        al, bl, fl = tuple(map(len, aa)), tuple(map(len, bb)), tuple(map(len, rest))
        wa = allocation_mass(al+(len(c),), bl, fl, ga, gb)
        wb = allocation_mass(al, bl+(len(c),), fl, ga, gb)
        (aa if weighted_choice(((0, wa), (1, wb)), rng) == 0 else bb).append(c)
        free = rest
    pa, map_a = restrict_permutation(rho, tuple(a for c in aa for a in c))
    pb, map_b = restrict_permutation(rho, tuple(a for c in bb for a in c))
    wa = tuple(tuple(map_a[a] for a in e) for e in sampler(pa, ga, rng))
    wb = tuple(tuple(map_b[a] for a in e) for e in sampler(pb, gb, rng))
    i = j = 0
    merged = []
    while i < len(wa) or j < len(wb):
        remaining_a, remaining_b = len(wa)-i, len(wb)-j
        if uniform_int(remaining_a+remaining_b, rng) < remaining_a:
            merged.append(wa[i]); i += 1
        else:
            merged.append(wb[j]); j += 1
    return tuple(merged) + (t,)


def check_samples(max_n, samples):
    rows = []
    for seed in (17, 101, 20260907):
        rng = random.Random(seed)
        for n in range(2, max_n+1):
            for _ in range(samples):
                w = sampler(tuple(range(n)), 1, rng)
                p, part = tuple(range(n)), tuple(range(n))
                for t in w:
                    p, part = right_t(p, t), union(part, *t)
                assert len(w) == 2*n and p == tuple(range(n)) and len(set(part)) == 1
            rows.append({'n':n,'seed':seed,'samples':samples})
    return {'test':'prototype_support_smoke','runs':rows,'distribution_claim':'support only; no empirical uniformity inference','result':'pass'}


@lru_cache(None)
def word_probability(p, g, word):
    """Reconstruct the prototype's exact fair-bit conditional law for one word."""
    n = len(p)
    want_r = n+len(cycles(p))+2*g-2
    if len(word) != want_r:
        return Fraction(0)
    q, partition = tuple(range(n)), tuple(range(n))
    for e in word:
        q, partition = right_t(q, e), union(partition, *e)
    if q != p or len(set(partition)) != 1:
        return Fraction(0)
    if not word:
        return Fraction(int(n == 1 and g == 0))
    t, prefix = word[-1], word[:-1]
    rho = right_t(p, t)
    part = tuple(range(n))
    for e in prefix:
        part = union(part, *e)
    branch_weights = dict(branches(p, g))
    total = sum(branch_weights.values())
    if len(set(part)) == 1:
        child_g = (len(prefix)-n-len(cycles(rho))+2)//2
        key = ('connected', t, child_g)
        return Fraction(branch_weights[key], total) * word_probability(rho, child_g, prefix)
    assert len(set(part)) == 2
    va = tuple(a for a in range(n) if part[a] == part[t[0]])
    vb = tuple(a for a in range(n) if part[a] == part[t[1]])
    pa, map_a = restrict_permutation(rho, va)
    pb, map_b = restrict_permutation(rho, vb)
    inverse_a, inverse_b = {a:i for i,a in enumerate(map_a)}, {a:i for i,a in enumerate(map_b)}
    wa = tuple(tuple(inverse_a[a] for a in e) for e in prefix if e[0] in inverse_a)
    wb = tuple(tuple(inverse_b[a] for a in e) for e in prefix if e[0] in inverse_b)
    ga = (len(wa)-len(va)-len(cycles(pa))+2)//2
    gb = (len(wb)-len(vb)-len(cycles(pb))+2)//2
    key = ('disconnected', t, ga, gb)
    probability = Fraction(branch_weights[key], total)
    cs = cycles(rho)
    aa = [next(c for c in cs if t[0] in c)]
    bb = [next(c for c in cs if t[1] in c)]
    free = [c for c in cs if c not in aa and c not in bb]
    while free:
        c, *rest = free
        al, bl, fl = tuple(map(len, aa)), tuple(map(len, bb)), tuple(map(len, rest))
        mass_a = allocation_mass(al+(len(c),), bl, fl, ga, gb)
        mass_b = allocation_mass(al, bl+(len(c),), fl, ga, gb)
        assert mass_a + mass_b > 0
        chosen_a = c[0] in va
        probability *= Fraction(mass_a if chosen_a else mass_b, mass_a+mass_b)
        (aa if chosen_a else bb).append(c)
        free = rest
    probability *= word_probability(pa, ga, wa) * word_probability(pb, gb, wb)
    probability /= comb(len(prefix), len(wa))
    return probability


def check_laws():
    rows = []
    n = 3
    trans = tuple(combinations(range(n), 2))
    target_diagnostics = {'adjacent_repeat_histogram':defaultdict(int),'edge_multiplicity_histogram':defaultdict(int),'support_graph_histogram':defaultdict(int),'prefix_cycle_types':defaultdict(int),'window_product_types':defaultdict(int),'per_position_edges':defaultdict(int)}
    tested_words = 0
    for r in range(1, 7):
        masses = defaultdict(Fraction)
        counts = defaultdict(int)
        for w in product(trans, repeat=r):
            p, part = tuple(range(n)), tuple(range(n))
            for e in w:
                p, part = right_t(p, e), union(part, *e)
            if len(set(part)) != 1:
                if p == tuple(range(n)) and r == 6:
                    assert word_probability(p, 1, w) == 0
                continue
            g2 = r-n-len(cycles(p))+2
            if g2 not in (0, 2):
                continue
            g = g2//2
            probability = word_probability(p, g, w)
            denominator = connected_count(tuple(map(len, cycles(p))), g)
            assert probability == Fraction(1, denominator), (p, g, w, probability, denominator)
            masses[p, g] += probability
            counts[p, g] += 1
            tested_words += 1
            if p == tuple(range(n)) and r == 6:
                target_diagnostics['adjacent_repeat_histogram'][str(sum(a == b for a,b in zip(w,w[1:])))] += 1
                target_diagnostics['edge_multiplicity_histogram'][str(tuple(sorted(w.count(t) for t in trans)))] += 1
                target_diagnostics['support_graph_histogram'][str(tuple(t for t in trans if t in w))] += 1
                pref = tuple(range(n))
                for i, e in enumerate(w):
                    target_diagnostics['per_position_edges'][str((i, e))] += 1
                    pref = right_t(pref, e)
                    target_diagnostics['prefix_cycle_types'][str((i+1, tuple(sorted(map(len, cycles(pref))))))] += 1
                for length in range(2, 6):
                    for i in range(r-length+1):
                        endpoint = tuple(range(n))
                        for e in w[i:i+length]:
                            endpoint = right_t(endpoint, e)
                        target_diagnostics['window_product_types'][str((length, i, tuple(sorted(map(len, cycles(endpoint))))))] += 1
        for key, mass in masses.items():
            assert mass == 1
            p, g = key
            rows.append({'r':r,'endpoint':p,'genus':g,'support_count':counts[key],'total_probability':str(mass)})
    # Finite-support normalization of rejection-sampled bounded integers.
    for bound in range(1, 257):
        width = (bound-1).bit_length()
        unconditional = Fraction(1, 2**width)
        acceptance = bound*unconditional
        assert acceptance > Fraction(1, 2) or bound == 1
        for x in range(bound):
            assert unconditional/acceptance == Fraction(1, bound)
    # Uniform shuffle: every binary interleaving receives 1/binomial.
    shuffle_cases = 0
    for total in range(0, 9):
        for a_count in range(total+1):
            for positions in combinations(range(total), a_count):
                positions = set(positions)
                a, b = a_count, total-a_count
                probability = Fraction(1)
                for i in range(total):
                    if i in positions:
                        probability *= Fraction(a, a+b); a -= 1
                    else:
                        probability *= Fraction(b, a+b); b -= 1
                assert probability == Fraction(1, comb(total, a_count))
                shuffle_cases += 1
    return {'test':'exact_conditional_laws','n':n,'enumerated_connected_words':tested_words,'endpoint_laws':rows,'bounded_integer_supports_checked':256,'uniform_shuffles_checked':shuffle_cases,'target_diagnostics':target_diagnostics,'result':'pass'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=('allocation','counts','samples','laws'), required=True)
    parser.add_argument('--max-n', type=int, required=True)
    parser.add_argument('--samples', type=int, default=2)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    start = time.monotonic()
    if args.mode == 'allocation':
        results = [check_allocations(args.max_n)]
    elif args.mode == 'counts':
        results = [check_endpoint_counts(n) for n in range(1, args.max_n+1)]
    elif args.mode == 'samples':
        results = [check_samples(args.max_n, args.samples)]
    else:
        results = [check_laws()]
    metadata = {'python':platform.python_version(),'nonstandard_dependencies':[],'elapsed_seconds':time.monotonic()-start,'results':results}
    args.output.write_text(json.dumps(metadata, indent=2)+'\n')
    print(json.dumps(metadata))


if __name__ == '__main__':
    main()
