#!/usr/bin/env python3
"""Independent exact coordinator checks, uniform identity-bridge target.

Compose maps p*q as p after q; appending (a,b) swaps entries a,b of p.
Compare original rational DYZ eq.13 with connected counts extracted from
full labeled permutation DP, independently of the role implementations.
These finite tests are falsification attempts; reports give general proofs.
No stochastic diagnostics or external Python dependencies are used.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import argparse
import importlib.util
import json
import platform
import subprocess
import time


def total_counts(n, length):
    identity = tuple(range(n))
    current = {identity: 1}
    result = [1]
    for _ in range(length):
        after = defaultdict(int)
        for p, weight in current.items():
            for a, b in combinations(range(n), 2):
                q = list(p)
                q[a], q[b] = q[b], q[a]
                after[tuple(q)] += weight
        current = after
        result.append(current.get(identity, 0))
    return result


def connected_from_totals(totals, length):
    counts = [[0] * (length + 1) for _ in totals]
    for n in range(1, len(totals)):
        for k in range(length + 1):
            disconnected = sum(
                comb(n - 1, v - 1) * comb(k, ell)
                * counts[v][ell] * totals[n - v][k - ell]
                for v in range(1, n) for ell in range(k + 1)
            )
            counts[n][k] = totals[n][k] - disconnected
            assert counts[n][k] >= 0
    return counts


def original_dyz(n_max, length):
    h = {(1, 0): Fraction(1)}
    c = [[0] * (length + 1) for _ in range(n_max + 1)]
    c[1][0] = 1
    for d in range(2, n_max + 1):
        for genus in range(length // 2 - d + 2):
            value = Fraction()
            for a in range(1, d):
                b = d - a
                for ell in range(1, genus + 2):
                    for g1 in range(genus + 2 - ell):
                        g2 = genus + 1 - ell - g1
                        value += (Fraction(a ** (2 * ell + 1) * b * b,
                                           factorial(2 * ell))
                                  * h.get((a, g1), 0) * h.get((b, g2), 0))
            value *= Fraction(2, d * d * (d - 1))
            h[d, genus] = value
            k = 2 * (d - 1 + genus)
            count = value * factorial(d) * factorial(k)
            assert count.denominator == 1
            c[d][k] = int(count)
    return c


def load_role(name, filename):
    path = Path(__file__).parent / 'roles' / name / filename
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), path)
    module = importlib.util.module_from_spec(spec)
    # dataclasses resolves its own module by this registry.
    import sys
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    n_max, length = 6, 12
    totals = [[1] + [0] * length]
    totals += [total_counts(n, length) for n in range(1, n_max + 1)]
    independent = connected_from_totals(totals, length)
    dyz = original_dyz(n_max, length)
    assert independent == dyz
    r3 = load_role('r3-intermediate-hybrid', 'component_audit.py')
    role_counts = r3.connected_counts(n_max, length)
    assert role_counts == independent
    assert r3.assembly_counts(n_max, length, role_counts) == totals
    restricted = r3.assembly_counts(n_max, length, role_counts,
                                   r3.minimal_allowed)
    for n in range(1, n_max + 1):
        for k in range(length + 1):
            assert 0 <= restricted[n][k] <= totals[n][k]
            if k > 2 * (n - 1):
                assert restricted[n][k] == 0
            if k % 2 == 0 and 0 < k <= n:
                actual = Fraction(totals[n][k] - restricted[n][k], totals[n][k])
                bound = min(Fraction(1), Fraction(k ** 4, 48 * (n-k+1) ** 2))
                assert actual <= bound
    result = {
        'status': 'passed', 'seed': None, 'dependencies': {},
        'python': platform.python_version(),
        'commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
        'command': 'python3 -B experiments/20260905-bridge-length-phase-diagram/coordinator_checks.py --output experiments/20260905-bridge-length-phase-diagram/coordinator_check_results.json',
        'independent_method': 'labeled permutation DP; subtract disconnected least-label components; compare original rational DYZ recurrence and role integer convolution',
        'N_max': n_max, 'm_max': length,
        'connected_count_cells': n_max * (length + 1),
        'boundary_cells': ['N=1', 'm=0', 'odd m', 'm=2', 'N=2', 'minimum connected lengths'],
        'required_cases': [{'N': n, 'm': m, 'total': totals[n][m],
                            'connected': independent[n][m],
                            'minimal_subset': restricted[n][m],
                            'minimal_TV': str(Fraction(totals[n][m] - restricted[n][m], totals[n][m]))}
                           for n, m in [(3, 4), (4, 4), (4, 6)]],
        'elapsed_seconds': time.monotonic() - started,
    }
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
