#!/usr/bin/env python3
"""Stable entry point for the audited H0/H1 restricted sampler and certificate."""
import hashlib
from pathlib import Path
import runpy

p=Path(__file__).resolve().parent/'roles/r3-sampler/sampler-v4.py'
expected='cdb91799b02539190bc31ce7d6fe31ee5af0477b1cc653f43452eb18de734002'
if hashlib.sha256(p.read_bytes()).hexdigest()!=expected:
    raise RuntimeError('audited sampler version hash mismatch')
runpy.run_path(str(p),run_name='__main__')
