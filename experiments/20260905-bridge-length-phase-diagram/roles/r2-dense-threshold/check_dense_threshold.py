#!/usr/bin/env python3
"""Deterministic exact checks for Theorem D and its new survival lemma.

All new combinatorial and floor checks use integers/Fraction. Reported decimal
ratios are summaries of exact rational calculations. Finite checks are only
falsification attempts; report.md contains the completeness proof.
"""
from __future__ import annotations
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial, isqrt
from pathlib import Path
import hashlib
import json
import platform
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inv(a):
    out = [0] * len(a)
    for i, x in enumerate(a):
        out[x] = i
    return tuple(out)


def trans(n, i, j):
    out = list(range(n))
    out[i], out[j] = out[j], out[i]
    return tuple(out)


def generators(n):
    return [trans(n, i, j) for i, j in combinations(range(n), 2)]


def endpoint_tables(n, gens, length):
    """Right multiplication in the displayed-word convention."""
    ps = list(permutations(range(n)))
    index = {p: j for j, p in enumerate(ps)}
    nxt = [[index[compose(p, t)] for t in gens] for p in ps]
    tables = [[0] * len(ps)]
    tables[0][index[tuple(range(n))]] = 1
    for _ in range(length):
        old = tables[-1]
        new = [0] * len(ps)
        for i, count in enumerate(old):
            if count:
                for j in nxt[i]:
                    new[j] += count
        tables.append(new)
    return ps, index, tables


def parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2


def cycles(p):
    seen = set()
    out = 0
    for i in range(len(p)):
        if i not in seen:
            out += 1
            while i not in seen:
                seen.add(i)
                i = p[i]
    return out


def ceil_sqrt(n):
    a = isqrt(n)
    return a + (a*a != n)


def ceil_fraction(x):
    return -(-x.numerator // x.denominator)


def floors(n, q):
    cs = {5: Fraction(1)}
    bs = {4: 0, 5: 20*q}
    for r in range(6, n+1):
        cs[r] = cs[r-1] + Fraction(1, r*ceil_sqrt(r))
        bs[r] = ceil_fraction(q*r*(r-1)*cs[r])
    return cs, bs


def z(n, k, x):
    b = n-1
    return (b**k + b*(-1)**k)//n if x == n-1 else (b**k-(-1)**k)//n


def scalar_checks():
    cases = 0
    minimum_gap_ratio_squared = None
    selected = []
    ns = list(range(5, 65)) + [128, 256, 512, 1024]
    for n in ns:
        ell = (n-1).bit_length()
        for q in sorted({4*ell, 144, 1000}):
            if q < 4*ell:
                continue
            cs, bs = floors(n, q)
            assert bs[n] <= 2*q*n*(n-1)
            for r in range(5, n+1):
                assert 1 <= cs[r] < 2
                assert bs[r] >= q*r*(r-1)
                assert 2*bs[r] <= 4*q*r*r
                if r >= 6:
                    mu = Fraction(r-2, r)*bs[r]
                    gap = mu-bs[r-1]
                    raw = Fraction(q*(r-1)*(r-2), r*ceil_sqrt(r))-1
                    assert gap >= raw > 0
                    assert gap*gap >= Fraction(q*q*r, 16)
                    assert (r-1)*(r-2)*2 >= r*r
                    assert 4*ceil_sqrt(r)**2 <= 9*r
                    assert q*q*r >= 144
                    # Denominator bound uses sqrt(r)<=r/2.
                    assert 4*r <= r*r
                    assert Fraction(97, 12) <= 9
                    ratio_sq = gap*gap/Fraction(q*q*r, 16)
                    minimum_gap_ratio_squared = ratio_sq if minimum_gap_ratio_squared is None else min(minimum_gap_ratio_squared, ratio_sq)
                cases += 1
            if n in (6, 64, 1024) and q in (4*ell, 1000):
                selected.append({'N': n, 'q': q, 'B_N': bs[n], 'top_length': 2*q*n*(n-1)})
    return {'rank_floor_cases': cases, 'minimum_gap_over_claim_squared': float(minimum_gap_ratio_squared), 'selected': selected}


def small_word_checks():
    result = []
    total_words = 0
    for n, length in [(2,0),(2,2),(2,5),(3,4),(4,4),(4,6),(4,3)]:
        gens = generators(n)
        ps, ix, tables = endpoint_tables(n, gens, length)
        hist = [0]*len(ps)
        valid_identity = 0
        for word in product(gens, repeat=length):
            endpoint = tuple(range(n))
            for t in word:
                endpoint = compose(endpoint, t)
            hist[ix[endpoint]] += 1
            total_words += 1
            # Verify the exact per-word probability of the backward low-rank
            # fallback for EVERY endpoint, not just the identity endpoint.
            prob = Fraction(1)
            state = endpoint
            for remaining, t in zip(range(length, 0, -1), reversed(word)):
                prev = compose(state, t)
                prob *= Fraction(tables[remaining-1][ix[prev]], tables[remaining][ix[state]])
                state = prev
            assert state == tuple(range(n))
            assert prob == Fraction(1, tables[length][ix[endpoint]])
            if endpoint == tuple(range(n)):
                valid_identity += 1
        assert hist == tables[length]
        assert sum(hist) == len(gens)**length
        for p in ps:
            expected = (parity(p) == length%2 and length >= n-cycles(p))
            assert bool(tables[length][ix[p]]) == expected
        result.append({'N': n, 'm': length, 'all_words': len(gens)**length, 'identity_count': valid_identity, 'all_endpoint_per_word_probabilities_exact': True})
    return {'words_checked': total_words, 'cases': result}


def projection_checks():
    cases = 0
    orientation = 0
    for n in range(2, 7):
        stars = [trans(n,i,n-1) for i in range(n-1)]
        ps, ix, tables = endpoint_tables(n, stars, 8)
        hs = [p+(n-1,) for p in permutations(range(n-1))]
        for k in range(9):
            aggregate = [0]*n
            for q, count in zip(ps,tables[k]):
                aggregate[inv(q)[n-1]] += count
            for x in range(n):
                assert aggregate[x] == z(n,k,x)
                assert 0 <= z(n,k,x) <= (n-1)**k
                if k:
                    assert z(n,k,x) == sum(z(n,k-1,t[x]) for t in stars)
                cases += 1
            for g in ps:
                x = inv(g)[n-1]
                actual = sum(tables[k][ix[compose(inv(h),g)]] for h in hs)
                assert actual == z(n,k,x)
                cases += 1
                # All q orientation equivalences, once per endpoint pair.
                if k == 0:
                    for q in ps:
                        h = compose(g, inv(q))
                        assert (h[n-1] == n-1) == (q[x] == n-1)
                        orientation += 1
    return {'projection_recurrence_and_convolution_equalities': cases, 'orientation_equivalences': orientation}


def dense_survival_check(n=6, q=12):
    """Exact new D17/D16 bounds at every feasible labeled endpoint.

    The small q makes the final exp(-q/144) guarantee loose, while the exact
    conditioning-factor check is nonvacuous. Its purpose is to falsify the
    pivotal improved transfer, not empirically certify an asymptotic error.
    """
    cs, bs = floors(n,q)
    length = bs[n]
    ps, ix, full = endpoint_tables(n, generators(n), length)
    olds = [trans(n,i,j) for i,j in combinations(range(n-1),2)]
    hs, hx, old = endpoint_tables(n-1,generators(n-1),length)
    _, _, star = endpoint_tables(n,[trans(n,i,n-1) for i in range(n-1)],length)
    h_embed = [h+(n-1,) for h in hs]
    d = comb(n-1,2)
    b = n-1
    M = comb(n,2)
    disc = [k for k in range(length+1) if length-k>=k and length-k<bs[n-1]]
    tail = sum(comb(length,k)*d**(length-k)*b**k for k in disc)
    full_tail = sum(comb(length,k)*d**(length-k)*b**k for k in range(length+1) if length-k<bs[n-1])
    assert tail <= full_tail
    delta = Fraction(factorial(n-1)-2,2)*Fraction(n-4,n-2)**((length+1)//2)
    assert delta < Fraction(1,2)
    bound_numerator = 2*(1+delta)*full_tail
    max_conditioning_ratio = Fraction(0)
    max_conditional_mass = Fraction(0)
    endpoint_cases = 0
    selected = []
    for g in ps:
        if parity(g) != length%2:
            continue
        exact_total = full[length][ix[g]]
        assert exact_total*factorial(n) >= M**length
        qs = [ix[compose(inv(h),g)] for h in h_embed]
        actual = sum(comb(length,k)*sum(a*star[k][j] for a,j in zip(old[length-k],qs)) for k in disc)
        # D17 exact integer/Fraction numerator inequality.
        assert actual*factorial(n-1) <= bound_numerator
        conditional = Fraction(actual,exact_total)
        conditioning_ratio = conditional/Fraction(full_tail,M**length)
        assert conditioning_ratio <= 2*n*(1+delta)
        max_conditioning_ratio = max(max_conditioning_ratio,conditioning_ratio)
        max_conditional_mass = max(max_conditional_mass,conditional)
        endpoint_cases += 1
        if len(selected)<3:
            selected.append({'endpoint': g, 'discarded_mass_float': float(conditional), 'conditioning_ratio_float': float(conditioning_ratio), 'discarded_numerator_sha256': hashlib.sha256(str(actual).encode()).hexdigest()})
    return {'N':n,'q':q,'L':length,'child_floor':bs[n-1], 'discarded_k_range':[min(disc),max(disc)], 'all_feasible_endpoints_checked':endpoint_cases,'old_relative_error_bound_float':float(delta), 'binomial_tail_float':float(Fraction(full_tail,M**length)), 'max_exact_discard_mass_float':float(max_conditional_mass), 'max_exact_conditioning_ratio_float':float(max_conditioning_ratio), 'proved_conditioning_bound_float':float(2*n*(1+delta)), 'selected':selected}


def main():
    started=time.monotonic()
    result={'schema':'dense-threshold-exact-checks-v1','python':platform.python_version(),'dependencies':{'standard_library_only':True},'deterministic':True,'random_seeds':None,'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'command':'python3 experiments/20260905-bridge-length-phase-diagram/roles/r2-dense-threshold/check_dense_threshold.py'}
    for name, fn in [('floors',scalar_checks),('small_words',small_word_checks),('projection',projection_checks),('dense_survival',dense_survival_check)]:
        result[name]=fn()
        print(name, json.dumps(result[name],sort_keys=True),flush=True)
    result['elapsed_seconds']=round(time.monotonic()-started,3)
    result['failures']=0
    HERE.joinpath('results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('all checks passed',flush=True)

if __name__=='__main__':
    main()
