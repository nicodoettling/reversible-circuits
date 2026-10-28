"""Integrated research reference: generated genus coefficients + literal decoder.

Mathematical all-input guarantee belongs to the versioned proof, not to finite
Python runtime observations. Standard Python implementation/resource limits
apply to this research reference. No built-in g>=2 constants are used.
"""
from fractions import Fraction
import importlib.util
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module

coefficient=load('genus_scaling_coefficient_v1',HERE/'coefficient_oracle_v1.py')
decoder=load('genus_scaling_decoder_v1',HERE.parent/'roles/r1-recursion/sampler-v1.py')
for genus in list(decoder.SPECS):
    if genus>=2:del decoder.SPECS[genus]
decoder.count.cache_clear();decoder.branches.cache_clear()
installed_through=1


def prepare(genus):
    global installed_through
    if not isinstance(genus,int) or genus<0:raise ValueError('nonnegative integer genus required')
    for h in range(installed_through+1,genus+1):
        terms=coefficient.recover(h)
        decoder.install_coefficients(h,[(term['theta'],Fraction(*term['coefficient'])) for term in terms])
    installed_through=max(installed_through,genus)


def sample_endpoint(endpoint,genus,rng=None):
    prepare(genus)
    return decoder.sample(tuple(endpoint),genus,rng)


def sample_identity(n,genus,rng=None):
    if not isinstance(n,int) or n<2:raise ValueError('T0 requires integer N>=2')
    return sample_endpoint(tuple(range(n)),genus,rng)
