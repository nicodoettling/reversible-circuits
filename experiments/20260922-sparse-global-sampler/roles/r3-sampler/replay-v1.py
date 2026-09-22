#!/usr/bin/env python3
"""Replay frozen audit-v1.py against frozen sampler-v1.py, never current code."""
import hashlib
import importlib.util
from pathlib import Path
import runpy
import sys
HERE = Path(__file__).resolve().parent
assert hashlib.sha256((HERE/'sampler-v1.py').read_bytes()).hexdigest() == 'c8fc1bc78dc2c187c3f3cf7b71b58833aba3b1b4a10e19776717d5032591f40b'
spec = importlib.util.spec_from_file_location('sampler', HERE/'sampler-v1.py')
module = importlib.util.module_from_spec(spec)
sys.modules['sampler'] = module
spec.loader.exec_module(module)
if len(sys.argv) == 1:
    sys.argv.append(str(HERE/'replay-v1-results.json'))
runpy.run_path(str(HERE/'audit-v1.py'), run_name='__main__')
