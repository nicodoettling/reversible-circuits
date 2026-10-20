#!/usr/bin/env python3
"""Static bridge-count checks; no MCMC run or asymptotic numerical claim."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import importlib.util
import json
import math
import platform
import random
import subprocess

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT/'experiments/20261019-140150-local-endpoint-blindness/check.py'
spec = importlib.util.spec_from_file_location('bridge_previous', SOURCE)
previous = importlib.util.module_from_spec(spec)
spec.loader.exec_module(previous)
Group = previous.Group
SEEDS = (20261020, 20261021)


def joint_matrix(G, Z, m, g):
    a = m//3
    b = m-2*a
    left = [u for u in range(len(G.perms))
            if Z[a][u] and Z[m-a][G.mul[G.inv[u]][g]]]
    right = [v for v in range(len(G.perms))
             if Z[a][v] and Z[m-a][G.mul[g][G.inv[v]]]]
    A = [[Z[a][u]*Z[b][G.mul[G.mul[G.inv[u]][g]][G.inv[v]]]*Z[a][v]
          for v in right] for u in left]
    rows = list(map(sum, A))
    cols = list(map(sum, zip(*A)))
    assert sum(rows) == Z[m][g] == sum(cols)
    for i, u in enumerate(left):
        assert rows[i] == Z[a][u]*Z[m-a][G.mul[G.inv[u]][g]]
    for j, v in enumerate(right):
        assert cols[j] == Z[a][v]*Z[m-a][G.mul[g][G.inv[v]]]
    return left, right, A, rows, cols


def singular_estimates(A, rows, cols):
    total = sum(rows)
    B = [[A[i][j]/math.sqrt(rows[i]*cols[j])
          -math.sqrt(rows[i]*cols[j])/total for j in range(len(cols))]
         for i in range(len(rows))]
    BT = list(zip(*B))
    ans = []
    for seed in SEEDS:
        rng = random.Random(seed)
        v = [rng.uniform(-1, 1) for _ in rows]
        norm = math.sqrt(sum(x*x for x in v))
        v = [x/norm for x in v]
        prev = -1.0
        rho = 0.0
        converged = False
        for iteration in range(1000):
            y = [sum(x*w for x, w in zip(col, v)) for col in BT]
            z = [sum(x*w for x, w in zip(row, y)) for row in B]
            rho = math.sqrt(sum(x*x for x in y))
            norm = math.sqrt(sum(x*x for x in z))
            if norm < 1e-28:
                rho = 0.0
                converged = True
                break
            v = [x/norm for x in z]
            if abs(rho-prev) < 1e-13:
                converged = True
                break
            prev = rho
        ans.append({'seed':seed, 'rho_estimate':rho, 'iterations':iteration+1,
                    'iteration_tolerance_reached':converged})
    return ans


def rational_certificate(A, rows, cols, bound=F(99, 100)):
    # rho^2<=b^2 iff b^2 diag(rows)-A diag(cols)^-1 A^T is
    # positive semidefinite on the rows-weighted mean-zero subspace.
    n = len(rows)
    if n <= 1 or len(cols) <= 1:
        return {'bound':str(bound), 'strict_certificate':True, 'dimension':0}
    G = [[(bound*bound*rows[i] if i == j else F(0))
          -sum((F(A[i][k]*A[j][k], cols[k]) for k in range(len(cols))), F(0))
          for j in range(n)] for i in range(n)]
    ratios = [F(rows[i], rows[-1]) for i in range(n-1)]
    C = [[G[i][j]-ratios[i]*G[-1][j]-ratios[j]*G[i][-1]
          +ratios[i]*ratios[j]*G[-1][-1] for j in range(n-1)]
         for i in range(n-1)]
    pivots = []
    for k in range(n-1):
        pivot = C[k][k]
        pivots.append(pivot)
        if pivot <= 0:
            return {'bound':str(bound), 'strict_certificate':False,
                    'dimension':n-1, 'failed_pivot':str(pivot)}
        for i in range(k+1, n-1):
            for j in range(i, n-1):
                C[i][j] -= C[i][k]*C[j][k]/pivot
                C[j][i] = C[i][j]
    return {'bound':str(bound), 'strict_certificate':True, 'dimension':n-1,
            'minimum_pivot':str(min(pivots)),
            'pivot_sha256':hashlib.sha256('\n'.join(map(str,pivots)).encode()).hexdigest()}


def enumeration_checks():
    result = []
    for n, m, expected in ((3,4,27), (4,4,120), (4,6,3936)):
        G = Group(n)
        words = G.fibers(m)[G.e]
        assert len(words) == expected
        a = m//3
        joint = Counter((G.eval(w[:a]), G.eval(w[-a:])) for w in words)
        left, right, A, _, _ = joint_matrix(G,G.counts(m),m,G.e)
        assert all(joint[u,v] == A[i][j]
                   for i,u in enumerate(left) for j,v in enumerate(right))
        result.append({'N':n,'m':m,'identity_states':expected,
                       'joint_count_equalities':len(left)*len(right)})
    return result


def main():
    records = [{'kind':'manifest', 'python':platform.python_version(),
      'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
      'dependencies':'standard library only', 'seeds':SEEDS,
      'command':f'python3 -B {Path(__file__).relative_to(ROOT)}',
      'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'imported_source':str(SOURCE.relative_to(ROOT)),
      'imported_source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest()}]
    records.append({'kind':'exact_enumeration','cases':enumeration_checks()})
    # Falsify the stronger guess rho<=1/2 with a simple rational observable.
    G = Group(5)
    g = G.index[(0,2,1,4,3)]
    left,right,A,rows,cols = joint_matrix(G,G.counts(4),4,g)
    def observable(u):
        moved = {i for i,j in enumerate(G.perms[u]) if i != j}
        if 0 in moved:
            return -16
        if moved in ({1,2},{3,4}):
            return 0
        return 9
    f = [observable(u) for u in left]
    h = [observable(v) for v in right]
    assert sum(x*w for x,w in zip(f,rows)) == 0
    assert sum(x*w for x,w in zip(h,cols)) == 0
    variance_numerator = sum(w*x*x for w,x in zip(rows,f))
    assert variance_numerator == sum(w*x*x for w,x in zip(cols,h))
    covariance_numerator = sum(A[i][j]*f[i]*h[j]
                               for i in range(len(rows)) for j in range(len(cols)))
    correlation = F(covariance_numerator,variance_numerator)
    assert correlation == F(917,1800) > F(1,2)
    records.append({'kind':'exact_refutation_rho_half','N':5,'m':4,
                    'endpoint':G.perms[g], 'observable':f,
                    'row_masses':rows, 'matrix':A,
                    'correlation':str(correlation)})
    for n, max_m in ((3,12),(4,12),(5,12),(6,8)):
        G = Group(n)
        Z = G.counts(max_m)
        reps = {}
        for g in range(len(G.perms)):
            reps.setdefault(G.cycle_type(g),g)
        for m in range(4,max_m+1):
            for ct, g in sorted(reps.items()):
                if Z[m][g] == 0:
                    continue
                _,_,A,rows,cols = joint_matrix(G,Z,m,g)
                estimates = singular_estimates(A,rows,cols)
                rec = {'kind':'tail_correlation','N':n,'m':m,'endpoint_type':ct,
                       'tail_length':m//3,'overlap_length':m-2*(m//3),
                       'matrix_shape':[len(rows),len(cols)],'word_count':Z[m][g],
                       'power_iteration':estimates}
                if n <= 4:
                    rec['exact_certificate'] = rational_certificate(A,rows,cols)
                if n == 3:
                    assert max(x['rho_estimate'] for x in estimates) < 1e-10
                records.append(rec)
    # Recursion and edge normalization, including rounded small cases.
    geometry = 0
    for m in range(4,1001):
        a = m//3
        ell = m-a
        assert 3*(ell-2) <= 2*(m-2)
        for k in (3,4,5,10,100):
            if m <= k:
                continue
            depth = 0
            length = m
            while length > k:
                length -= length//3
                depth += 1
            # Integer comparison avoids logarithmic rounding.
            assert (m-2)*2**depth <= (k-2)*3**depth or length <= k
            upper = 0
            while (m-2)*2**upper > (k-2)*3**upper:
                upper += 1
            assert depth <= upper
        for j in range(m-1):
            multiplicity = int(j+1 < ell)+int(j >= a)
            assert 1 <= multiplicity <= 2
            geometry += 1
    records.append({'kind':'recursion_geometry','slot_cases':geometry})
    path = Path(__file__).with_name('results.jsonl')
    path.write_text(''.join(json.dumps(x,sort_keys=True)+'\n' for x in records))
    cases = [x for x in records if x['kind']=='tail_correlation']
    worst = max(cases,key=lambda x:max(y['rho_estimate'] for y in x['power_iteration']))
    failed = [x for x in cases if x.get('exact_certificate',{}).get('strict_certificate') is False]
    print(json.dumps({'status':'completed','cases':len(cases),'failed_certificates':len(failed),
                      'worst_empirical_case':worst,'output':str(path.relative_to(ROOT))}))


if __name__ == '__main__':
    main()
