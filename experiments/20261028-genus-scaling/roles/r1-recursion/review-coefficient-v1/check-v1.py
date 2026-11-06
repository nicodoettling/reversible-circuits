"""New exact audit: support DP on N5/6 and full-polynomial extrapolation.

This is a reviewer program, independent of coordinator's cycle-type and
anchored-subprofile reference. Run only after coordinator reservation.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial, prod
from pathlib import Path
import argparse, hashlib, importlib.util, json, platform, subprocess, sys, time

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[2]
source = BASE / 'coordinator/coefficient_oracle_v1.py'
spec = importlib.util.spec_from_file_location('reviewed_coefficient', source)
C = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = C
spec.loader.exec_module(C)


def independent_types(p):
    unused = set(range(len(p)))
    result = []
    while unused:
        first = min(unused)
        nxt, size = first, 0
        while nxt in unused:
            unused.remove(nxt)
            nxt, size = p[nxt], size + 1
        result.append(size)
    return tuple(sorted(result))


def literal_reference(n, length):
    # Component labels are the minimal original vertex; no cycle-type compression.
    states = {(tuple(range(n)), tuple(range(n))): 1}
    edges = tuple(combinations(range(n), 2))
    cases, peak = 0, 1
    for ell in range(length + 1):
        ordinary, connected = defaultdict(int), defaultdict(int)
        for (p, partition), count in states.items():
            ordinary[p] += count
            if len(set(partition)) == 1:
                connected[p] += count
        for alpha in C.partitions(n):
            p = C.permutation(alpha)
            assert independent_types(p) == alpha
            a = C.ordinary(alpha, ell)
            c = C.connected(alpha, ell)
            assert a == ordinary[p], ('ordinary', n, ell, alpha, a, ordinary[p])
            assert c == connected[p], ('connected', n, ell, alpha, c, connected[p])
            cases += 2
        if ell == length:
            break
        nxt = defaultdict(int)
        for (p, partition), count in states.items():
            for x, y in edges:
                q = tuple(p[y] if j == x else p[x] if j == y else p[j]
                          for j in range(n))
                keep, lose = sorted((partition[x], partition[y]))
                updated = tuple(keep if j == lose else j for j in partition)
                nxt[(q, updated)] += count
        states = dict(nxt)
        peak = max(peak, len(states))
    return cases, peak


def indices(d, bound):
    if not d:
        yield ()
    else:
        for x in range(bound + 1):
            for rest in indices(d - 1, bound - x):
                yield (x,) + rest


def full_newton(genus, d):
    degree = 3*genus - 3 + d
    grid = tuple(indices(d, degree))
    values = {b: C.normalized(genus, tuple(sorted(x+1 for x in b))) for b in grid}
    coefficients = {}
    for beta in grid:
        value = Fraction(0)
        for gamma in product(*(range(x+1) for x in beta)):
            sign = -1 if (sum(beta)-sum(gamma)) % 2 else 1
            value += sign * prod(comb(x,y) for x,y in zip(beta,gamma)) * values[gamma]
        coefficients[beta] = value
    return coefficients


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    start=time.monotonic()
    count_checks=0;peaks={}
    for n in (5,6):
        cases,peak=literal_reference(n,2*n+6)
        count_checks+=cases;peaks[str(n)]=peak
    rows=[]
    for genus in (2,3,4):
        for d in (1,2):
            coefficients=full_newton(genus,d)
            points=((12,), (16,)) if d==1 else ((1,14),(14,1),(6,8),(8,6))
            for alpha in points:
                got=sum(value*prod(comb(a-1,b) if b<=a-1 else 0
                                   for a,b in zip(alpha,beta))
                        for beta,value in coefficients.items())
                want=C.normalized(genus,tuple(sorted(alpha)))
                assert got==want, ('extrapolation',genus,alpha,got,want)
                L=14*genus;M=9*genus
                denominator=factorial(L)**(M+2)
                assert all(denominator % q.denominator==0 for q in coefficients.values())
                rows.append({'genus':genus,'alpha':alpha,'value':str(got),
                             'grid_points':len(coefficients),
                             'degree':3*genus-3+d})
    # Strongly repeated profile: distinct cycles are still distinguished.
    repeated=[]
    for alpha in ((1,1,1,1,1,1),(1,1,2,2),(2,2,2),(1,1,1,3)):
        for genus in (0,1,2,3,4):
            r=sum(alpha)+len(alpha)-2+2*genus
            repeated.append({'alpha':alpha,'genus':genus,'count':C.connected(alpha,r)})
    result={'status':'passed','elapsed_seconds':time.monotonic()-start,
            'python':platform.python_version(),'dependencies':'standard-library-only',
            'seed':None,'command':sys.argv,
            'commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
            'literal_reference_count_checks':count_checks,'peak_literal_reference_states':peaks,
            'full_polynomial_extrapolations':rows,'repeated_cycle_rows':repeated,
            'reviewed_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'review_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'limitations':['finite extrapolation checks do not prove ELSV polynomiality',
                           'reviewer shares construction context',
                           'coordinator code is a finite Python research reference']}
    out=Path(args.output);tmp=out.with_name(out.name+'.tmp')
    tmp.write_text(json.dumps(result,indent=2)+'\n');tmp.replace(out)
    print(json.dumps({'status':'passed','count_checks':count_checks,
                      'extrapolations':len(rows),'seconds':result['elapsed_seconds']}))


if __name__=='__main__':main()
