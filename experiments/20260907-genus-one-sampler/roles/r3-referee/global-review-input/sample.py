#!/usr/bin/env python3
"""Research entry points for the provisional R1 sampler and exact assembly.

Labels in Python words are 0,...,N-1. CLI output relabels them 1,...,N.
Connected output targets X_N. Restricted output is uniform conditional on
all support components having genus <=1, and includes its exact mass in the
global target. It must not be described as globally uniform unless that
mass is one. The final proof/audit status is recorded in proof.md/ledger.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import importlib.util
import json
from math import comb
from pathlib import Path
import random
import sys

HERE = Path(__file__).resolve().parent


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


recursive = load_module('genus_one_recursive_sampler', HERE/'roles/r1-recursive/sampler.py')
mass = load_module('genus_one_mass_certificate', HERE/'global_mass.py')


def sample_connected_identity(n, rng=None):
    """Exact X_N draw in the ideal independent-fair-bit model, N>=2."""
    return recursive.sample_identity(n, rng)


@dataclass(frozen=True)
class RestrictedSample:
    word: tuple
    covered_mass: Fraction

    @property
    def global_tv(self):
        return 1-self.covered_mass


def sample_restricted_components(n, m, rng=None):
    """Exact conditional g<=1 assembly plus exact global TV certificate.

Independent repeated calls recompute tables; caching is unnecessary for
polynomiality. Zero restricted mass is rejected before making a draw.
"""
    if n < 0 or m < 0:
        raise ValueError('N and m must be nonnegative')
    if m % 2 or (n < 2 and m > 0):
        raise ValueError('the global identity fiber is empty')
    if m > 2*n:
        raise ValueError('the genus<=1 restricted fiber is empty')
    rng = random.SystemRandom() if rng is None else rng
    c = mass.counts.connected_counts(n,m)
    z = mass.counts.assembly_counts(n,m,c)
    z01 = mass.counts.assembly_counts(n,m,c,mass.allowed)
    if not z01[n][m]:
        raise ValueError('the genus<=1 restricted fiber is empty')
    labels, positions = list(range(n)), list(range(m))
    result = [None]*m
    while labels:
        nn, mm = len(labels), len(positions)
        choices, weights = [], []
        for v in range(1,nn+1):
            for ell in range(mm+1):
                if c[v][ell] and mass.allowed(v,ell):
                    w = comb(nn-1,v-1)*comb(mm,ell)*c[v][ell]*z01[nn-v][mm-ell]
                    if w:
                        choices.append((v,ell))
                        weights.append(w)
        assert sum(weights) == z01[nn][mm]
        v,ell = recursive.weighted_choice(rng,choices,weights)
        selected_other = recursive.unrank_subset(nn-1,v-1,
                          recursive.randbelow(rng,comb(nn-1,v-1)))
        selected_labels = [labels[0]]+[labels[i+1] for i in selected_other]
        selected_positions = recursive.unrank_subset(mm,ell,
                             recursive.randbelow(rng,comb(mm,ell)))
        genus = (ell-2*v+2)//2
        local = recursive.sample(tuple(range(v)),genus,rng)
        assert len(local) == ell
        for i,(a,b) in zip(selected_positions,local):
            result[positions[i]] = (selected_labels[a],selected_labels[b])
        chosen_labels, chosen_positions = set(selected_labels), set(selected_positions)
        labels = [x for x in labels if x not in chosen_labels]
        positions = [x for i,x in enumerate(positions) if i not in chosen_positions]
    assert not positions and all(x is not None for x in result)
    return RestrictedSample(tuple(result),Fraction(z01[n][m],z[n][m]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--n',type=int,required=True)
    parser.add_argument('--target',choices=('connected','restricted'),default='connected')
    parser.add_argument('--m',type=int)
    parser.add_argument('--seed',type=int,help='reproducible diagnostic PRNG; omitted uses SystemRandom')
    args = parser.parse_args()
    rng = None if args.seed is None else random.Random(args.seed)
    if args.target == 'connected':
        if args.m is not None and args.m != 2*args.n:
            parser.error('connected target X_N has m=2N')
        word = sample_connected_identity(args.n,rng)
        data = {'target':'Unif(X_N)','TV_error':'0','length':2*args.n}
    else:
        if args.m is None:
            parser.error('restricted component target requires --m')
        draw = sample_restricted_components(args.n,args.m,rng)
        word = draw.word
        data = {'target':'Unif(Omega(N,m) | every component genus <=1)',
                'covered_mass':str(draw.covered_mass),'global_TV_error':str(draw.global_tv),
                'length':args.m}
    data.update({'N':args.n,'word_on_1_to_N':[[a+1,b+1] for a,b in word],
                 'composition':'rightmost acts first','diagnostic_seed':args.seed,
                 'randomness_model':'ideal independent fair bits; seed is for reproducibility only'})
    print(json.dumps(data,indent=2))


if __name__ == '__main__':
    main()
