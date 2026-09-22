#!/usr/bin/env python3
"""Integration validity/boundary checks; exact laws are proved and audited separately."""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import platform
import random
import time

import sample


def validate(n, m, w):
    assert len(w) == m
    assert all(0 <= a < b < n for a,b in w)
    assert sample.recursive.evaluate(n,w) == tuple(range(n))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    start = time.monotonic()
    seeds = [1729,2718,31415]
    connected = restricted = 0
    observed = {}
    for seed in seeds:
        rng = random.Random(seed)
        for n in (2,3,4,5,8):
            w = sample.sample_connected_identity(n,rng)
            validate(n,2*n,w)
            assert len(sample.recursive.components(n,w)) == 1
            connected += 1
        for n in (0,1,2,3,4,8):
            lengths = (0,) if n < 2 else sorted({0,2,4,2*n})
            for m in lengths:
                draw = sample.sample_restricted_components(n,m,rng)
                validate(n,m,draw.word)
                macro = sample.mass.counts.support_macro(n,draw.word)
                assert all(sample.mass.allowed(len(labels),ell) for labels,ell in macro)
                assert 0 < draw.covered_mass <= 1
                observed[n,m] = draw.covered_mass
                restricted += 1
    for case,ratio in { (0,0):Fraction(1), (1,0):Fraction(1),
                        (2,4):Fraction(1), (3,4):Fraction(1),
                        (3,6):Fraction(80,81), (4,4):Fraction(1),
                        (4,8):Fraction(4375,4672)}.items():
        assert observed[case] == ratio
    invalid = []
    for n in (0,1):
        try:
            sample.sample_connected_identity(n,random.Random(17))
        except ValueError:
            invalid.append(['connected',n])
        else:
            raise AssertionError(('expected empty connected target',n))
    for n,m in ((1,2),(2,1),(2,6),(-1,0),(2,-2)):
        try:
            sample.sample_restricted_components(n,m,random.Random(17))
        except ValueError:
            invalid.append(['restricted',n,m])
        else:
            raise AssertionError(('expected rejection',n,m))
    data = {'python':platform.python_version(),'dependencies':{},'seeds':seeds,
            'connected_valid_draws':connected,'restricted_valid_draws':restricted,
            'invalid_inputs_rejected':invalid,
            'certificate_checks':[{'N':n,'m':m,'covered_mass':str(v)} for (n,m),v in sorted(observed.items())],
            'interpretation':'seeded draws check integration validity only; no empirical uniformity inference',
            'seconds':time.monotonic()-start}
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'seconds':data['seconds'],'connected':connected,
                      'restricted':restricted,'invalid':len(invalid),'all_passed':True}))


if __name__ == '__main__':
    main()
