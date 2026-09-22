#!/usr/bin/env python3
"""Stable entry point for the audited H0/H1 restricted sampler and certificate."""
import hashlib
from pathlib import Path
import runpy

p=Path(__file__).resolve().parent/'roles/r3-sampler/sampler-v3.py'
expected='56b27019396f93d4784032028ca1099d45ddd1cab1f740520c20c8c0169a8e06'
if hashlib.sha256(p.read_bytes()).hexdigest()!=expected:
    raise RuntimeError('audited sampler version hash mismatch')
runpy.run_path(str(p),run_name='__main__')
