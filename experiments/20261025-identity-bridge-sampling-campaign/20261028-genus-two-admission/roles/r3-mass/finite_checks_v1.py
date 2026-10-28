#!/usr/bin/env python3
"""Deterministic exact R3 mass checks; must run through a reserved bounded job."""
import argparse
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from math import comb, factorial
from pathlib import Path
import json
import os
import platform
import sys
import time

BASE_COMMIT = 'd8893491e04aff74ff3185f7054470ffa24a44a4'
ROLE = Path(__file__).resolve().parent
ROOT = ROLE.parents[4]


def rational(q):
    q = F(q)
    return {'numerator': str(q.numerator), 'denominator': str(q.denominator)}


def dyz_table(vmax=8, gmax=8):
    a = {(1, 0): F(1)}
    for v in range(2, vmax + 1):
        for g in range(gmax + 1):
            acc = F(0)
            for u in range(1, v):
                w = v - u
                for ga in range(g + 1):
                    for gb in range(g - ga + 1):
                        r = g + 1 - ga - gb
                        acc += (2 * comb(v, u) * u * w * w *
                                F(u ** (2 * r), factorial(2 * r)) *
                                a.get((u, ga), 0) * a.get((w, gb), 0))
            a[v, g] = acc / (v * v * (v - 1))
    return a


def connected_count(a, v, ell):
    if v == 1:
        return int(ell == 0)
    if ell % 2 or ell < 2 * v - 2:
        return 0
    g = ell // 2 - v + 1
    value = a[v, g] * factorial(ell)
    assert value.denominator == 1
    return value.numerator


def support_step(parts, i, j):
    """Canonical support blocks with accumulated edge counts, including isolates."""
    bi = next(t for t, (mask, _) in enumerate(parts) if mask & (1 << i))
    bj = next(t for t, (mask, _) in enumerate(parts) if mask & (1 << j))
    updated = [part for t, part in enumerate(parts) if t not in (bi, bj)]
    if bi == bj:
        mask, length = parts[bi]
        updated.append((mask, length + 1))
    else:
        updated.append((parts[bi][0] | parts[bj][0], parts[bi][1] + parts[bj][1] + 1))
    return tuple(sorted(updated))


def product_support_dp(n, max_length=10):
    """Independent literal product DP; appending t means p*t, swapping p's entries."""
    identity = tuple(range(n))
    initial_parts = tuple((1 << i, 0) for i in range(n))
    dp = {(identity, initial_parts): 1}
    endpoints = {}
    state_counts = []
    for ell in range(max_length + 1):
        counts = defaultdict(int)
        for (perm, parts), value in dp.items():
            if perm == identity:
                counts[parts] += value
        endpoints[ell] = dict(counts)
        state_counts.append({'length': ell, 'states': len(dp), 'identity_support_states': len(counts)})
        if ell == max_length:
            break
        nxt = defaultdict(int)
        for (perm, parts), value in dp.items():
            for i in range(n):
                for j in range(i + 1, n):
                    newperm = list(perm)
                    newperm[i], newperm[j] = newperm[j], newperm[i]
                    nxt[(tuple(newperm), support_step(parts, i, j))] += value
        dp = nxt
    return endpoints, state_counts


def profile_allowed(parts, genus_cap, cutoff):
    for mask, length in parts:
        v = mask.bit_count()
        if v == 1:
            assert length == 0
            continue
        assert length % 2 == 0
        g = length // 2 - v + 1
        assert g >= 0
        if g > genus_cap and v > cutoff:
            return False
    return True


def assembly(a, n, m, genus_cap, cutoff):
    @lru_cache(None)
    def z(size, length):
        if size == 0:
            return int(length == 0)
        acc = z(size - 1, length)
        for v in range(2, size + 1):
            for ell in range(2 * v - 2, length + 1, 2):
                g = ell // 2 - v + 1
                if g <= genus_cap or v <= cutoff:
                    acc += comb(size - 1, v - 1) * comb(length, ell) * connected_count(a, v, ell) * z(size - v, length - ell)
        return acc
    return z(n, m)


def moment(d, q):
    # Stirling expansion of sum_{v>=0} v^d*q^v, subtract v=0 where needed.
    if d == 0:
        return q / (1 - q)
    stirling = [1]
    for n in range(1, d + 1):
        nxt = [0] * (n + 1)
        for s in range(1, n + 1):
            nxt[s] = (stirling[s - 1] if s - 1 < len(stirling) else 0) + s * (stirling[s] if s < len(stirling) else 0)
        stirling = nxt
    all_v = sum((F(stirling[s] * factorial(s)) * q ** s / (1 - q) ** (s + 1) for s in range(1, d + 1)), F(0))
    return all_v / q - 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    output = Path(args.output)
    if output.exists():
        raise SystemExit('Immutable output already exists; choose a unique artifact.')
    started = time.monotonic()
    a = dyz_table()
    majorant_rows = []
    for (v, g), value in sorted(a.items()):
        if v == 1:
            continue
        a0 = F(v ** (v - 3)) if v >= 3 else F(1, 2)
        bound = a0 * F(v ** 3 - v, 36) ** g / factorial(g)
        assert value <= bound
        if g == 0:
            assert value == a0
        majorant_rows.append({'v': v, 'g': g, 'A': rational(value), 'majorant': rational(bound)})
    dp_rows = []
    assembly_rows = []
    states = []
    denominator_rows = []
    for n in range(2, 5):
        endpoints, state_counts = product_support_dp(n)
        states.append({'N': n, 'counts': state_counts})
        for ell, counts in endpoints.items():
            total = sum(counts.values())
            connected = sum(value for parts, value in counts.items() if len(parts) == 1)
            expected = connected_count(a, n, ell)
            assert connected == expected
            if ell % 2:
                assert total == 0
            if ell > 0 and ell % 2 == 0:
                lower = F(2 * comb(n, 2) ** ell, factorial(n))
                assert total >= lower
                denominator_rows.append({'N': n, 'm': ell, 'total': str(total), 'lower': rational(lower)})
            dp_rows.append({'N': n, 'm': ell, 'total': str(total), 'connected': str(connected), 'DYZ_connected': str(expected)})
            if ell % 2 == 0:
                for G in range(3):
                    for cutoff in range(1, n + 1):
                        direct = sum(value for parts, value in counts.items() if profile_allowed(parts, G, cutoff))
                        predicted = assembly(a, n, ell, G, cutoff)
                        assert direct == predicted
                        assembly_rows.append({'N': n, 'm': ell, 'G': G, 'fixed_cutoff': cutoff, 'allowed': str(direct), 'total': str(total), 'mass': rational(F(direct, total))})
    moment_rows = []
    for g in range(1, 17):
        d = 3 * g - 3
        c_g = F(factorial(3 * g - 2) * 2 ** (3 * g - 1), 36 ** g * factorial(g))
        assert c_g <= (6 * g ** 3) ** g
        for q in (F(1, 64), F(1, 8), F(3, 8), F(1, 2)):
            exact = moment(d, q)
            upper = factorial(d + 1) * 2 ** (d + 2) * q
            assert exact <= upper
            moment_rows.append({'g': g, 'q': rational(q), 'moment': rational(exact), 'upper': rational(upper), 'c_g': rational(c_g)})
    sequence_rows = []
    for j in (1, 2, 3, 8, 16, 32, 64, 65, 128):
        x = F(1, 2 ** (10 * j + 1))
        q = F(3, 2 ** (2 * j + 1))
        cutoff_bound = F((32 * j + 4) ** 3, 72 * 2 ** (10 * j))
        G = 2 ** j
        a_bound = 6 * G ** 3 * x
        assert q <= F(1, 2) and cutoff_bound < 1 and a_bound <= F(1, 16)
        if j >= 64:
            # Square both positive sides to avoid irrational arithmetic.
            assert (2 ** 18 * j ** 2) ** 2 <= 2 ** j
        sequence_rows.append({'j': j, 'max_G': str(G), 'x': rational(x), 'q': rational(q), 'b_L_x_upper': rational(cutoff_bound), 'six_G3_x': rational(a_bound)})
    # CP-1 must continue rejecting the old marginal-product rule.
    cp1 = F(21, 2000)
    assert cp1 > F(1, 100)
    source_paths = [
        Path(__file__).resolve(), ROLE / 'proof-v1.md', ROLE / 'plan-v1.md', ROLE / 'scope-growing-v1.md',
        ROOT / 'experiments/20260922-sparse-boundary/source_checks.md',
        ROOT / 'experiments/20260922-sparse-boundary/obstruction.md',
        ROOT / 'experiments/20260922-sparse-boundary/roles/r2-obstruction/corollary-h2-v1.md',
        ROOT / 'experiments/20260922-sparse-boundary/roles/r5-referee/blind_report.md',
    ]
    result = {
        'schema_version': 1, 'status': 'PASS', 'claim': 'Finite falsification/normalization checks for FG.v1 and M-GROW.v1; not an asymptotic proof',
        'base_commit': BASE_COMMIT, 'argv': sys.argv, 'seed': 0, 'seed_used': False,
        'python': platform.python_version(), 'third_party_dependencies': [],
        'completed_utc': datetime.now(timezone.utc).isoformat(), 'elapsed_seconds': time.monotonic() - started,
        'source_sha256': {str(path.relative_to(ROOT)): sha256(path.read_bytes()).hexdigest() for path in source_paths},
        'parameters': {'DYZ_vmax': 8, 'DYZ_gmax': 8, 'literal_dp_N': [2, 3, 4], 'literal_dp_max_m': 10, 'moment_gmax': 16},
        'majorant': majorant_rows, 'product_support_counts': dp_rows, 'assembly': assembly_rows,
        'denominator': denominator_rows, 'geometric_moments': moment_rows, 'sequence_conditions': sequence_rows,
        'state_sizes': states, 'CP1': {'two_stage_hit': rational(cp1), 'claimed_old_bound': rational(F(1,100)), 'old_claim_rejected': True},
    }
    tmp = output.with_name(output.name + '.tmp')
    with tmp.open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    os.replace(tmp, output)
    print('PASS R3 exact checks:', len(majorant_rows), 'majorant;', len(dp_rows), 'product/support;', len(assembly_rows), 'assembly;', len(moment_rows), 'moment; data written.')


if __name__ == '__main__':
    main()
