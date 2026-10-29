"""Exact checks of interval coordinates, Fourier gaps and lifted pair channels."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import hashlib
import importlib.util
import json
import platform
import subprocess

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / '20261014-111117-nonlocal-graph-lift/check.py'
spec = importlib.util.spec_from_file_location('nonlocal_core', SOURCE)
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
REFLECTIONS = ((1, 2), (0, 1), (0, 2))
PARAM = {t: a for a, t in enumerate(REFLECTIONS)}


def coordinates(w):
    b = 0
    y = []
    for k, t in enumerate(w):
        b = (b + (-1)**k * PARAM[t]) % 3
        if k < len(w)-1:
            y.append(((-1)**k * b) % 3)
    return tuple(y)


def translate(y, i, j, delta):
    return tuple((v+delta) % 3 if i <= k < j else v
                 for k, v in enumerate(y))


def ternary_check(m):
    C = m*(m-1)//2
    seen = defaultdict(set)
    channels = 0
    ratio_set = set()
    for params in product(range(3), repeat=m):
        w = tuple(REFLECTIONS[a] for a in params)
        g = core.evaluate(w, 3)
        y = coordinates(w)
        assert y not in seen[g]
        seen[g].add(y)
        p = defaultdict(F)
        q = defaultdict(F)
        p[y] = q[y] = F(1, 2)
        for i, j in combinations(range(m), 2):
            a, b = params[i], params[j]
            for sign in (1, -1):
                z = core.macro(w, i, j, 'H', sign)
                assert core.evaluate(z, 3) == g
                yz = coordinates(z)
                assert yz == translate(y, i, j, sign*(b-a))
                p[yz] += F(1, 8*C)
                channels += 1
            for s in range(3):
                z = core.macro(w, i, j, 'R', REFLECTIONS[s])
                assert core.evaluate(z, 3) == g
                yz = coordinates(z)
                expected = translate(y, i, j, s-a) if a == b else y
                assert yz == expected
                p[yz] += F(1, 12*C)
                q[translate(y, i, j, s)] += F(1, 6*C)
                channels += 1
        assert sum(p.values()) == sum(q.values()) == 1
        assert set(p) == set(q)
        for z in q:
            if z != y:
                ratio = p[z]/q[z]
                assert F(1, 2) <= ratio <= F(3, 4)
                ratio_set.add(str(ratio))
    assert len(seen) == 3
    assert all(len(v) == 3**(m-1) for v in seen.values())
    return dict(m=m, words=3**m, endpoints=3, channels=channels,
                prefix_bijection=True, interval_identity=True,
                actual_to_auxiliary_off_diagonal_ratios=sorted(ratio_set))


def fourier_check(m):
    C = m*(m-1)//2
    min_D = C
    hist = Counter()
    for z in product(range(3), repeat=m-1):
        if not any(z):
            continue
        prefix = [0]
        for a in z:
            prefix.append((prefix[-1]+a) % 3)
        direct = sum(sum(z[i:j]) % 3 != 0
                     for i, j in combinations(range(m), 2))
        counts = Counter(prefix)
        D = (m*m-sum(v*v for v in counts.values()))//2
        assert D == direct and D >= m-1
        hist[D] += 1
        min_D = min(min_D, D)
    assert F(min_D, 2*C) == F(1, m)
    return dict(m=m, nonconstant_modes=3**(m-1)-1,
                gap=str(F(min_D, 2*C)), cut_size_histogram=dict(sorted(hist.items())))


def bridge_check(n, m):
    gates = tuple(combinations(range(n), 2))
    idp = tuple(range(n))
    inverse = {core.perm(t, n): t for t in gates}
    rows = {}
    channels = 0
    for prefix in product(gates, repeat=m-1):
        p = core.evaluate(prefix, n)
        if p not in inverse:
            continue
        w = prefix + (inverse[p],)
        assert core.evaluate(w, n) == idp
        row = Counter()
        for i, j in combinations(range(m), 2):
            for sign in (1, -1):
                z = core.macro(w, i, j, 'H', sign)
                path = core.lifted_path(w, i, j, 'H', sign)
                assert z == path[-1]
                assert core.macro(z, i, j, 'H', -sign) == w
                assert all(core.evaluate(x, n) == idp for x in path)
                row[z] += len(gates)
                channels += 1
            for s in gates:
                z = core.macro(w, i, j, 'R', s)
                if w[i] == w[j]:
                    assert core.macro(z, i, j, 'R', w[i]) == w
                path = core.lifted_path(w, i, j, 'R', s)
                assert z == path[-1]
                assert all(core.evaluate(x, n) == idp for x in path)
                row[z] += 2
                channels += 1
        # Active mass scaled by 8*C*M; laziness contributes 4*C*M.
        C = m*(m-1)//2
        row[w] += 4*C*len(gates)
        assert sum(row.values()) == 8*C*len(gates)
        rows[w] = row
    for w, row in rows.items():
        for z, count in row.items():
            assert rows[z][w] == count
    visited = set()
    todo = [next(iter(rows))]
    while todo:
        w = todo.pop()
        if w in visited:
            continue
        visited.add(w)
        todo.extend(z for z in rows[w] if z not in visited)
    assert len(visited) == len(rows)
    return dict(N=n, m=m, states=len(rows), channels=channels,
                endpoint_and_primitive_lift=True, inverse_channels=True,
                integer_detailed_balance=True, connected=True)


def comparison_counts():
    checked = 0
    for m in range(2, 101):
        for k in range(1, m):
            shuttle = sum(2*(j-i)-1 for i in range(1, k+1)
                          for j in range(k+2, m+1))
            middle = sum(2*(k+1-i)-1 for i in range(1, k+1))
            assert shuttle == m*k*(m-k-1) and middle == k*k
            constant = 16*k*(m-k-1)+F(2*k*k, m)
            assert constant <= 4*m*m
            checked += 1
    return dict(m_range=[2, 100], positions_checked=checked,
                weighted_occurrence_formula=True, constant_bound=True)


if __name__ == '__main__':
    result = dict(
        metadata=dict(commit=subprocess.check_output(
            ['git', 'rev-parse', 'HEAD'], text=True).strip(),
            python=platform.python_version(), dependencies='standard library only',
            random_seeds='none: exhaustive deterministic checks',
            command='python3 -B experiments/20261015-113600-all-pair-interval-gap/check.py',
            imported_source=str(SOURCE.relative_to(HERE.parents[1])),
            imported_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest()),
        ternary=[ternary_check(m) for m in range(2, 8)],
        fourier=[fourier_check(m) for m in range(2, 10)],
        bridges=[bridge_check(n, m) for n, m in [(3, 4), (4, 4), (4, 6)]],
        comparison=comparison_counts(),
        verdict='All assertions passed; exact finite checks supplement the symbolic proof.')
    (HERE/'results.jsonl').write_text(json.dumps(result, sort_keys=True)+'\n')
    print(json.dumps(dict(ternary_words=sum(x['words'] for x in result['ternary']),
        ternary_channels=sum(x['channels'] for x in result['ternary']),
        bridge_states=sum(x['states'] for x in result['bridges']),
        bridge_channels=sum(x['channels'] for x in result['bridges']),
        verdict=result['verdict']), indent=2))
