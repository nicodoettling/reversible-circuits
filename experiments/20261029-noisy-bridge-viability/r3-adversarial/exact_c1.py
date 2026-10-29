"""Exact matched full-word C1 checks. No random sampling or dependencies.

The Q_k transform is the degree-k coefficient of product_i(Id+z E_i),
where E_i sums over the old coordinate and broadcasts onto its fresh value.
Integer normalization is total_source_mass*binom(L,k)*q**k.
"""

import argparse
import itertools
import json
import math
import os
import platform
import subprocess
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path


def group(n):
    perms = list(itertools.permutations(range(n)))
    pindex = {p: i for i, p in enumerate(perms)}
    ident = pindex[tuple(range(n))]
    mul = [[pindex[tuple(p[q[i]] for i in range(n))] for q in perms]
           for p in perms]
    ends = list(itertools.combinations(range(n), 2))
    edge_index = {e: i for i, e in enumerate(ends)}
    gates = []
    for a, b in ends:
        p = list(range(n))
        p[a], p[b] = p[b], p[a]
        gates.append(pindex[tuple(p)])

    def product(w):
        p = ident
        for g in w:
            p = mul[p][gates[g]]
        return p

    def cycle_type(p):
        unseen = set(range(n))
        lengths = []
        while unseen:
            v = next(iter(unseen))
            start = v
            length = 0
            while True:
                unseen.remove(v)
                length += 1
                v = perms[p][v]
                if v == start:
                    break
            lengths.append(length)
        return tuple(sorted(lengths, reverse=True))

    conjugated = [[None] * len(ends) for _ in ends]
    for i, (a, b) in enumerate(ends):
        for j, (c, d) in enumerate(ends):
            swap = lambda x: b if x == a else a if x == b else x
            conjugated[i][j] = edge_index[tuple(sorted((swap(c), swap(d))))]
    return ends, edge_index, ident, product, cycle_type, conjugated


def encode(word, q):
    code = 0
    for x in word:
        code = code * q + x
    return code


def sum_axis(values, q, stride):
    result = [0] * len(values)
    for block in range(0, len(values), q * stride):
        for offset in range(stride):
            start = block + offset
            total = sum(values[start + a * stride] for a in range(q))
            for a in range(q):
                result[start + a * stride] = total
    return result


def all_noise(source, q, length):
    dp = [source.copy()]
    for position in range(length):
        stride = q ** (length - position - 1)
        dp.append(None)
        for degree in range(position + 1, 0, -1):
            refreshed = sum_axis(dp[degree - 1], q, stride)
            if degree == position + 1:
                dp[degree] = refreshed
            else:
                dp[degree] = [a + b for a, b in zip(dp[degree], refreshed)]
    total = sum(source)
    for k, row in enumerate(dp):
        assert sum(row) == total * math.comb(length, k) * q ** k
    assert dp[0] == source
    assert all(x == total for x in dp[length])
    return dp


def brute_one(source, words, q, length):
    result = [0] * len(words)
    for code, mass in enumerate(source):
        if not mass:
            continue
        word = words[code]
        for i in range(length):
            stride = q ** (length - 1 - i)
            for new in range(q):
                result[code + (new - word[i]) * stride] += mass
    return result


def features(word, ends, n, product, cycle_type):
    parent = list(range(n))

    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x

    touched = set()
    for gate in word:
        a, b = ends[gate]
        touched.update((a, b))
        parent[root(a)] = root(b)
    component_vertices = Counter(root(i) for i in range(n))
    component_edges = Counter(root(ends[gate][0]) for gate in word)
    weighted_components = tuple(sorted((size, component_edges[component])
                                      for component, size in component_vertices.items()))
    return {
        'all_six_edges_distinct': int(len(set(word)) == 6),
        'distinct_edges': len(set(word)),
        'positive_edge_multiplicity_profile': str(tuple(sorted(Counter(word).values()))),
        'word_support_size': len(touched),
        'support_components_including_isolates': len({root(i) for i in range(n)}),
        'weighted_component_profile_including_isolates': str(weighted_components),
        'adjacent_repeats': sum(a == b for a, b in zip(word, word[1:])),
        'prefix_three_cycle_type': str(cycle_type(product(word[:3]))),
        'first_four_cycle_type': str(cycle_type(product(word[:4]))),
        'middle_four_cycle_type': str(cycle_type(product(word[1:5]))),
        'endpoint_cycle_type': str(cycle_type(product(word))),
    }


def histogram(row, feature_rows, field):
    out = Counter()
    for mass, feat in zip(row, feature_rows):
        if mass:
            out[str(feat[field])] += mass
    return out


def diagnostic(a, da, b, db, feature_rows):
    tv = Fraction(sum(abs(x * db - y * da) for x, y in zip(a, b)), 2 * da * db)
    fields = {}
    for field in feature_rows[0]:
        ah, bh = histogram(a, feature_rows, field), histogram(b, feature_rows, field)
        keys = sorted(set(ah) | set(bh))
        fields[field] = {
            'structured': {key: str(Fraction(ah[key], da)) for key in keys},
            'reference': {key: str(Fraction(bh[key], db)) for key in keys},
            'histogram_tv': str(sum((abs(Fraction(ah[key], da) - Fraction(bh[key], db))
                                     for key in keys), Fraction()) / 2),
        }
    return {'full_word_tv': str(tv), 'features': fields}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    path = Path(args.output)
    if path.exists():
        raise FileExistsError('Immutable result already exists: ' + str(path))
    start = time.monotonic()
    n, length = 4, 6
    ends, edge_index, ident, product, cycle_type, conjugated = group(n)
    q = len(ends)
    words = list(itertools.product(range(q), repeat=length))
    reference = [int(product(w) == ident) for w in words]
    assert sum(reference) == 3936
    sources = {}
    source = [0] * len(words)
    for a, b, c, d in itertools.permutations(range(n), 4):
        edge = lambda u, v: edge_index[tuple(sorted((u, v)))]
        w = (edge(a, c), edge(c, d), edge(a, b), edge(a, d), edge(b, c), edge(b, d))
        assert product(w) == ident and len(set(w)) == 6
        source[encode(w, q)] += 1
    assert sum(source) == 24 and sum(x > 0 for x in source) == 24
    sources[0] = source
    for s in (1, 2):
        target = [0] * len(words)
        for code, mass in enumerate(source):
            if not mass:
                continue
            w = words[code]
            for i in range(length - 1):
                u, v = w[i], w[i + 1]
                for pair in ((v, conjugated[v][u]), (conjugated[u][v], u)):
                    changed = w[:i] + pair + w[i + 2:]
                    assert product(changed) == ident
                    target[encode(changed, q)] += mass
        assert sum(target) == sum(source) * 2 * (length - 1)
        sources[s] = target
        source = target
    feature_rows = [features(w, ends, n, product, cycle_type) for w in words]
    reference_noise = all_noise(reference, q, length)
    assert reference_noise[1] == brute_one(reference, words, q, length)
    cases = []
    for s, source in sources.items():
        noisy = all_noise(source, q, length)
        if s == 0:
            assert noisy[1] == brute_one(source, words, q, length)
        for k in range(length + 1):
            factor = math.comb(length, k) * q ** k
            da, db = sum(source) * factor, sum(reference) * factor
            result = diagnostic(noisy[k], da, reference_noise[k], db, feature_rows)
            marginals = []
            for i in range(length):
                a = [0] * q
                b = [0] * q
                for code, w in enumerate(words):
                    a[w[i]] += noisy[k][code]
                    b[w[i]] += reference_noise[k][code]
                assert all(x * q == da for x in a)
                assert all(x * q == db for x in b)
                marginals.append('exactly uniform')
            if s == 0 and k == 0:
                assert result['full_word_tv'] == '163/164'
            if k == length:
                assert result['full_word_tv'] == '0'
            cases.append({'N': n, 'L': length, 'candidate': 'C1-v1', 's': s, 'k': k,
                          'source_total_integer_mass': sum(source),
                          'source_support_words': sum(x > 0 for x in source),
                          'structured_denominator': da, 'reference_denominator': db,
                          'per_position_edge_marginals': marginals, **result})
    output = {
        'status': 'passed', 'target': 'M0 global U(4,6), same hidden uniform-k-subset replacement',
        'composition': '(p q)(x)=p(q(x)); rightmost first',
        'candidate_version': 'C1-v1 plus runtime-only erratum',
        'baseline_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
        'python': platform.python_version(), 'dependencies': [],
        'randomness': 'none; exact enumeration and integer transforms',
        'state_count': len(words), 'global_bridge_count': sum(reference),
        'predeclared_features': list(feature_rows[0]),
        'classification': 'exact finite diagnostics, not asymptotic proof or held-out security test',
        'checks': ['all identity outputs before noise', 'exact global bridge count',
                   'Q1 transform agrees with independent literal replacement enumeration',
                   'Q0 identity channel', 'QL source-independent iid law',
                   'all position marginals uniform', 'normalization at every k'],
        'elapsed_seconds': time.monotonic() - start, 'cases': cases,
    }
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(json.dumps(output, indent=2) + '\n')
    if path.exists():
        raise FileExistsError('Immutable result appeared during run: ' + str(path))
    os.replace(temporary, path)
    print(json.dumps({'status': output['status'], 'cases': len(cases),
                      'elapsed_seconds': output['elapsed_seconds'], 'output': str(path)}))


if __name__ == '__main__':
    main()
