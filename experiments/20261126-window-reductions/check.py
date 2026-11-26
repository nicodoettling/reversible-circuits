"""Exact finite falsification checks; these do not prove asymptotic claims."""
import itertools
import json
import math
import platform
import subprocess
from collections import Counter, defaultdict
from fractions import Fraction as F


def emit(**x):
    print(json.dumps(x, sort_keys=True), flush=True)


def mul(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def model(n):
    ident = tuple(range(n))
    ts = []
    for i, j in itertools.combinations(range(n), 2):
        t = list(ident)
        t[i], t[j] = t[j], t[i]
        ts.append(tuple(t))
    return ident, ts


def prod(w, ident):
    p = ident
    for t in w:
        p = mul(p, t)
    return p


def conj(w, h):
    return tuple(mul(mul(h, t), h) for t in w)


def conjugation_path(word, i, j, h):
    w = list(word)
    s = w[i]
    assert s == w[j]
    path = [tuple(w)]
    extraction = []

    def hurwitz(k, inverse=False):
        a, b = w[k:k+2]
        w[k:k+2] = (mul(mul(a, b), a), a) if inverse else (b, mul(mul(b, a), b))
        path.append(tuple(w))

    for k in range(i-1, -1, -1):
        hurwitz(k)
        extraction.append(k)
    for k in range(j-1, 0, -1):
        hurwitz(k)
        extraction.append(k)
    assert w[:2] == [s, s]
    w[:2] = [h, h]
    path.append(tuple(w))
    for k in range(1, len(w)-1):
        hurwitz(k, True)
    for k in range(len(w)-2, 0, -1):
        hurwitz(k, True)
    assert w[:2] == [h, h]
    v = mul(mul(h, s), h)
    w[:2] = [v, v]
    path.append(tuple(w))
    for k in reversed(extraction):
        hurwitz(k, True)
    assert tuple(w) == conj(word, h)
    assert len(path)-1 <= 8*len(word)
    return path


def fibers_and_paths(n, m, every_pair):
    ident, ts = model(n)
    fibers = defaultdict(list)
    for w in itertools.product(ts, repeat=m):
        fibers[prod(w, ident)].append(w)
    bridges = fibers.get(ident, [])
    pair_spellings = defaultdict(list)
    for a, b in itertools.product(ts, repeat=2):
        pair_spellings[mul(a, b)].append((a, b))
    path_count = edge_count = 0
    encodings = {}
    for w in bridges:
        pairs = [(i, j) for i in range(m) for j in range(i+1, m) if w[i] == w[j]]
        if m > len(ts):
            assert len(pairs) >= F(m*(m-len(ts)), 2*len(ts))
        for i, j in pairs if every_pair else pairs[:1]:
            for h in ts:
                path = conjugation_path(w, i, j, h)
                path_count += 1
                for stage, v in enumerate(path):
                    assert prod(v, ident) == ident
                    if every_pair:
                        key = (i, j, w[i], h, stage, v)
                        assert key not in encodings or encodings[key] == w
                        encodings[key] = w
                for u, v in zip(path, path[1:]):
                    changed = [i for i in range(m) if u[i] != v[i]]
                    if changed:
                        assert len(changed) == 2 and changed[1] == changed[0]+1
                        k = changed[0]
                        assert mul(*u[k:k+2]) == mul(*v[k:k+2])
                        assert v[k:k+2] in pair_spellings[mul(*u[k:k+2])]
                        edge_count += 1
        # Equivariance of every adjacent conditional, hence strong lumpability.
        h = ts[0]
        for k in range(m-1):
            before = {conj(p, h) for p in pair_spellings[mul(*w[k:k+2])]}
            hw = conj(w, h)
            assert before == set(pair_spellings[mul(*hw[k:k+2])])
    # Exact block-boundary counts on every endpoint, including odd endpoints.
    left = Counter(prod(w, ident) for w in itertools.product(ts, repeat=m//2))
    right = Counter(prod(w, ident) for w in itertools.product(ts, repeat=m-m//2))
    identities = 0
    for g, words in fibers.items():
        counts = Counter(prod(w[:m//2], ident) for w in words)
        for x, lx in left.items():
            inv = tuple(x.index(i) for i in range(n))
            assert counts[x] == lx*right[mul(inv, g)]
            identities += 1
    emit(check="fibers_paths_and_equivariance", N=n, m=m, identity_words=len(bridges),
         endpoint_fibers=len(fibers), paths=path_count, legal_path_edges=edge_count,
         injective_encodings=len(encodings), factorization_equalities=identities)


def permutation_checks():
    for n in range(2, 7):
        ident, ts = model(n)
        perms = list(itertools.permutations(range(n)))
        even = [p for p in perms if sum(p[i] > p[j] for i in range(n) for j in range(i+1, n)) % 2 == 0]
        if n >= 5:
            vals = [sum(i == p[i] for i in range(n))-1 for p in even]
            assert sum(vals) == 0 and sum(v*v for v in vals) == len(even)
        for p in perms:
            f = sum(i == p[i] for i in range(n))-1
            mean = sum(sum(i == mul(p, t)[i] for i in range(n))-1 for t in ts)
            assert F(mean, len(ts)) == (1-F(2, n-1))*f
        counts = {ident: 1}
        for r in range(1, 21):
            new = Counter()
            for p, c in counts.items():
                for t in ts:
                    new[mul(p, t)] += c
            counts = new
            error = max(abs(F(math.factorial(n)*v, 2*len(ts)**r)-1) for v in counts.values())
            # Include reachable-parity states still having zero probability.
            if len(counts) < math.factorial(n)//2:
                error = max(error, 1)
            rhs = math.expm1(n*n*math.exp(-r/(n-1)))
            assert float(error) <= rhs+1e-12
        emit(check="parity_smoothing_and_fixed_point_eigenfunction", N=n, permutations=len(perms), lengths=20)


def geometry_and_boundaries():
    comparisons = 0
    for b in range(1, 30):
        for m in range(2*b, 15*b+1):
            q = m//b
            lengths = [b]*(q-1)+[m-b*(q-1)]
            starts = [0]
            for ell in lengths:
                starts.append(starts[-1]+ell)
            coefficients = [F(0) for _ in range(m-1)]
            for i in range(q-1):
                ell = lengths[i]+lengths[i+1]
                assert 2*b <= ell <= 4*b-2 if b >= 2 else ell == 2
                for k in range(starts[i], starts[i+2]-1):
                    coefficients[k] += F(1, 2*(ell-1))
            assert max(coefficients) <= F(1, 2*b-1)
            comparisons += 1
    # S3 prefixes at all positive gaps are exactly parity-uniform. Hence the
    # coarse update has zero neighbor influence and heals at rate 1/(2d).
    ident, ts = model(3)
    for a, b in itertools.product(itertools.permutations(range(3)), repeat=2):
        common = set(mul(a, t) for t in ts) & set(mul(b, t) for t in ts)
        assert len(common) in (0, 3)
    for n in (2, 3, 4):
        ident, ts = model(n)
        assert prod((), ident) == ident
        assert all(prod(w, ident) != ident for w in itertools.product(ts, repeat=3))
        assert sum(prod(w, ident) == ident for w in itertools.product(ts, repeat=2)) == len(ts)
        if n == 2:
            assert len(ts) == 1 and prod(ts*4, ident) == ident
    emit(check="block_scan_normalization_and_boundary_cases", interval_geometries=comparisons,
         S3_neighbor_influence=0, odd_identity_empty=True, m0_m2_N2=True)


if __name__ == "__main__":
    emit(python=platform.python_version(), dependencies="standard library", seed=None,
         command="python3 -B experiments/20261126-window-reductions/check.py",
         commit=subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip())
    fibers_and_paths(3, 4, True)
    fibers_and_paths(4, 4, True)
    fibers_and_paths(4, 6, False)
    fibers_and_paths(3, 6, True)
    fibers_and_paths(3, 3, True)
    permutation_checks()
    geometry_and_boundaries()
    emit(verdict="all exact checks passed", scope="finite falsification only")
