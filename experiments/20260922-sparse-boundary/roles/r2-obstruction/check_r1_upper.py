#!/usr/bin/env python3
"""Nonauthor exact falsification tests of frozen R1 UPPER.v2."""
from fractions import Fraction
from pathlib import Path
import hashlib
import importlib.util
import json
from math import comb, factorial, prod
import platform
import sys
import time

ROLE = Path(__file__).resolve().parent
ROOT = ROLE.parents[3]


def falling(n, q):
    return prod(range(n-q+1, n+1))


def main():
    started = time.monotonic()
    proof = ROOT/'experiments/20260922-sparse-boundary/roles/r1-upper/proof-v2.md'
    digest = hashlib.sha256(proof.read_bytes()).hexdigest()
    assert digest == 'b76f706aad3dae20ed3550298b98bd260b295f7cc9752eb3f1ecef663c87ac3c'
    source = ROOT/'experiments/20260905-bridge-length-phase-diagram/roles/r3-intermediate-hybrid/component_audit.py'
    old_hash = json.loads((ROLE/'input_hashes.json').read_text())[str(source.relative_to(ROOT))]
    assert hashlib.sha256(source.read_bytes()).hexdigest() == old_hash
    spec=importlib.util.spec_from_file_location('r2_upper_frozen_counts',source)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    C=module.connected_counts(32,20)
    Z=module.assembly_counts(32,20,C)
    genus_cells=0
    binomial_cells=0
    rising_cells=0
    empty_h0_cells=0
    for n in range(2,33):
        for m in range(2,min(n,20)+1,2):
            k=m//2
            d=n-m+1
            for v in range(2,min(n,k+1)+1):
                b=Fraction(v**3-v,36)
                a=4*b/(d*d)
                h=k-v+1
                A0=Fraction(v**v,v**3)
                pref=comb(n,v)*A0*falling(k,v-1)*Fraction(4,d*d)**(v-1)
                actual=Fraction(0)
                expanded=Fraction(0)
                actual_h0=Fraction(0)
                for g in range(h+1):
                    q=v-1+g
                    ell=2*q
                    marked=Fraction(comb(n,v)*comb(m,ell)*C[v][ell]*Z[n-v][m-ell],Z[n][m])
                    bound=comb(n,v)*A0*b**g/factorial(g)*4**q*falling(k,q)/d**(2*q)
                    rising=comb(n,v)*A0*b**g/factorial(g)*Fraction(4**q*falling(k,q),prod(range(d,d+2*q)))
                    assert marked<=rising<=bound
                    actual+=marked
                    expanded+=bound
                    if g>=2:
                        actual_h0+=marked
                    genus_cells+=1
                    rising_cells+=1
                assert expanded==pref*(1+a)**h
                assert actual<=expanded
                assert actual_h0<=pref*((1+a)**h-1-h*a)
                if h<=1:
                    assert actual_h0==0
                    empty_h0_cells+=1
                binomial_cells+=1
    result={
        'status':'pass',
        'audited_proof':str(proof.relative_to(ROOT)),
        'audited_proof_sha256':digest,
        'count_source_sha256_before_import':old_hash,
        'domain':'2<=N<=32, even2<=m<=min(N,20), all feasible v,g',
        'genus_term_cells':genus_cells,
        'finite_binomial_cells':binomial_cells,
        'rising_factorial_cells':rising_cells,
        'near_minimal_zero_H0_cells':empty_h0_cells,
        'seeds':'none, deterministic exact rationals',
        'python':platform.python_version(),
        'seconds':time.monotonic()-started,
        'command':'timeout 90s python3 -B experiments/20260922-sparse-boundary/roles/r2-obstruction/check_r1_upper.py',
    }
    (ROLE/'r1-upper-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':
    main()
