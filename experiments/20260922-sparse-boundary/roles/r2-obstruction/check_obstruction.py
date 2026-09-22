#!/usr/bin/env python3
"""Exact finite falsification of R2-O1 bounds; no sampling or asymptotic fit."""
from fractions import Fraction
from pathlib import Path
import hashlib
import importlib.util
import json
from math import comb, factorial
import platform
import subprocess
import time

ROLE = Path(__file__).resolve().parent
ROOT = ROLE.parents[3]
SOURCE = ROOT / 'experiments/20260905-bridge-length-phase-diagram/roles/r3-intermediate-hybrid/component_audit.py'


def cutoff(n, m):
    p = n + m + 2
    result = 1
    for v in range(1, n + 1):
        if v ** (2 * v) <= p**4:
            result = v
        else:
            break
    return result


def exponential_coefficient(component_coefficients, degree):
    result = [Fraction(0) for _ in range(degree + 1)]
    result[0] = Fraction(1)
    for q in range(1, degree + 1):
        result[q] = sum(i * component_coefficients[i] * result[q-i]
                        for i in range(1, q + 1)) / q
    return result[degree]


def main():
    started = time.monotonic()
    source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    expected = json.loads((ROLE / 'input_hashes.json').read_text())[str(SOURCE.relative_to(ROOT))]
    assert source_hash == expected
    spec = importlib.util.spec_from_file_location('r2_frozen_component_audit', SOURCE)
    module = importlib.util.module_from_spec(spec)
    # dataclasses consult sys.modules while loading this audited source.
    import sys
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    max_n, max_m = 32, 20
    counts = module.connected_counts(max_n, max_m)
    full = module.assembly_counts(max_n, max_m, counts)
    assert [full[3][4], full[4][4], full[4][6]] == [27, 120, 3936]
    for n in range(max_n + 1):
        assert full[n][0] == 1
        assert all(full[n][m] == 0 for m in range(1, max_m + 1, 2))
    assert all(full[2][m] == 1 for m in range(0, max_m + 1, 2))

    denominator_cells = 0
    for n in range(2, max_n + 1):
        for m in range(2, max_m + 1, 2):
            for r in range(2, n + 1):
                assert full[n][m] * factorial(r) >= 2 * comb(r, 2)**m
                denominator_cells += 1

    # Reuse one assembly table per K rather than refilling per top-level input.
    restricted = {}
    coefficient_cells = []
    numerator_bound_cells = 0
    small_high_genus_cells = 0
    for cap in range(2, 7):
        def allowed(v, ell, cap=cap):
            return v <= cap or ell <= 2*v
        restricted[cap] = module.assembly_counts(max_n, max_m, counts, allowed)
    for n in [2, 3, 4, 5, 8, 16, 32]:
        for m in [2, 4, 6, 8, 10, 14, 20]:
            k = m // 2
            for cap in sorted({2, cutoff(n, m)}):
                za = restricted[cap][n][m]
                coeff = [Fraction(0) for _ in range(k + 1)]
                for v in range(2, min(n, k + 1) + 1):
                    for cost in range(v - 1, k + 1):
                        ell = 2 * cost
                        if v <= cap or cost <= v:
                            coeff[cost] += Fraction(n**v * counts[v][ell], factorial(v) * factorial(ell))
                            if v <= cap and cost >= v + 1 and counts[v][ell]:
                                small_high_genus_cells += 1
                egf = exponential_coefficient(coeff, k)
                assert Fraction(za, factorial(m)) <= egf
                x = Fraction(k, n*n)
                q = 3 * n * x
                b_cap = Fraction(cap**3-cap, 36)
                condition = q <= Fraction(1, 2) and x <= 1 and b_cap*x <= 1
                if condition:
                    evaluated = sum(coeff[cost] * x**cost for cost in range(1, k + 1))
                    assert evaluated <= 8*k
                    assert za * k**k <= factorial(m) * n**(2*k) * 3**(8*k)
                    numerator_bound_cells += 1
                coefficient_cells.append({'N': n, 'm': m, 'K': cap,
                                          'ZA': za, 'Z': full[n][m],
                                          'finite_bound_hypotheses': condition,
                                          'coefficient_dominance': True})

    subsequence = []
    for j in [1, 2, 4, 8, 16, 32, 63, 64, 65, 128, 256]:
        n, m = 2**(8*j), 2**(6*j)
        k = m//2
        cap = cutoff(n, m)
        assert m**4 == n**3 and (m+2)**4 > n**3
        assert cap <= 16*j+2
        x = Fraction(k,n*n)
        assert 3*n*x <= Fraction(1,2)
        assert Fraction(cap**3-cap,36)*x <= 1
        r = m//(6*j)
        assert 2<=r<=n
        assert 12*j*r >= m
        assert 576*j*j*comb(r,2) >= m*m
        # Equivalent exact squared condition, valid only at claimed threshold.
        decay_condition = 2**36 * j**4 <= 2**j
        if j>=64:
            assert decay_condition
        subsequence.append({'j':j, 'log2_N':8*j, 'log2_m':6*j, 'K':cap,
                            'r_hex':hex(r), 'benchmark_equality':True,
                            'is_exact_m_star':True,
                            'decay_condition':decay_condition})

    result = {
        'status':'pass', 'scope':'finite falsification only; asymptotic proof is separate',
        'source':str(SOURCE.relative_to(ROOT)), 'source_sha256_before_import':source_hash,
        'python':platform.python_version(),
        'repository_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        'command':'timeout 90s python3 -B experiments/20260922-sparse-boundary/roles/r2-obstruction/check_obstruction.py',
        'random_seeds':'none: deterministic exact arithmetic',
        'denominator_cells':denominator_cells,
        'coefficient_cells':coefficient_cells,
        'finite_numerator_bound_cells':numerator_bound_cells,
        'retained_small_high_genus_terms':small_high_genus_cells,
        'subsequence_parameter_checks':subsequence,
        'seconds':time.monotonic()-started,
    }
    (ROLE / 'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ['status','denominator_cells','finite_numerator_bound_cells','retained_small_high_genus_terms','seconds']}))


if __name__ == '__main__':
    main()
