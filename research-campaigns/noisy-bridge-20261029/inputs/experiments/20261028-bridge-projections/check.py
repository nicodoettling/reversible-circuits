"""Deterministic small-group falsification of projection/replacement identities."""

import itertools
import json
import math
import platform
import resource
import subprocess
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path


def check(n, length):
    permutations = list(itertools.permutations(range(n)))
    index = {p: i for i, p in enumerate(permutations)}
    identity = index[tuple(range(n))]
    mul = [[index[tuple(p[q[i]] for i in range(n))] for q in permutations]
           for p in permutations]
    inverse = [next(j for j in range(len(permutations)) if mul[i][j] == identity)
               for i in range(len(permutations))]
    edges = []
    for a, b in itertools.combinations(range(n), 2):
        p = list(range(n))
        p[a], p[b] = p[b], p[a]
        edges.append(index[tuple(p)])
    edge_ends = {edge: tuple(i for i in range(n) if permutations[edge][i] != i)
                 for edge in edges}
    q = len(edges)

    def product(word):
        state = identity
        for gate in word:
            state = mul[state][gate]
        return state

    def connected(word):
        reached = {0}
        while True:
            previous = len(reached)
            for edge in word:
                a, b = edge_ends[edge]
                if a in reached or b in reached:
                    reached.update((a, b))
            if len(reached) == previous:
                return len(reached) == n

    def twist(word):
        prefix = identity
        result = []
        for gate in word:
            result.append(mul[mul[prefix][gate]][inverse[prefix]])
            prefix = mul[prefix][gate]
        return tuple(result)

    def distance(p):
        seen = set()
        cycles = 0
        for a in range(n):
            if a in seen:
                continue
            cycles += 1
            while a not in seen:
                seen.add(a)
                a = permutations[p][a]
        return n - cycles

    walk = [Counter({identity: 1})]
    for _ in range(max(length, 4)):
        next_counts = Counter()
        for p, count in walk[-1].items():
            for gate in edges:
                next_counts[mul[p][gate]] += count
        walk.append(next_counts)

    bridges = [word for word in itertools.product(edges, repeat=length)
               if product(word) == identity]
    connected_bridges = [word for word in bridges if connected(word)]
    assert len(bridges) == walk[length][identity]
    cases = []
    for name, words in (('global', bridges), ('connected', connected_bridges)):
        if not words:
            continue
        word_set = set(words)
        assert {twist(w) for w in words} == word_set
        total = len(words)
        for k in range(min(2, length) + 1):
            reference = Counter(w[:k] for w in words)
            tuple_space = list(itertools.product(edges, repeat=k))
            projection_tv = sum((abs(Fraction(reference[a], total) - Fraction(1, q**k))
                                 for a in tuple_space), Fraction()) / 2
            if k == 1:
                assert projection_tv == 0
            old_product = Counter()
            for a, count in reference.items():
                old_product[product(a)] += count
                assert distance(product(a)) <= length-k
                if name == 'global':
                    assert count == walk[length-k][inverse[product(a)]]
            if name == 'global':
                for a in tuple_space:
                    assert reference[a] == walk[length-k][inverse[product(a)]]
            predicted = Counter()
            for x, count_x in walk[k].items():
                for y, count_y in old_product.items():
                    predicted[mul[x][y]] += count_x * count_y
            endpoint_tv = sum((abs(Fraction(predicted[p], total*q**k)
                                   - Fraction(walk[2*k][p], q**(2*k)))
                               for p in range(len(permutations))), Fraction()) / 2
            assert endpoint_tv <= projection_tv
            if k == 1:
                assert endpoint_tv == 0
            index_sets = list(itertools.combinations(range(length), k))
            for positions in index_sets:
                actual_projection = Counter(tuple(w[i] for i in positions) for w in words)
                assert actual_projection == reference
                endpoint = Counter()
                for word in words:
                    for replacements in tuple_space:
                        changed = list(word)
                        for i, gate in zip(positions, replacements):
                            changed[i] = gate
                        endpoint[product(changed)] += 1
                assert endpoint == predicted
            cases.append(dict(target=name, k=k, index_sets=len(index_sets),
                              projection_tv=str(projection_tv), endpoint_tv=str(endpoint_tv)))
    return dict(N=n, L=length, bridge_words=len(bridges),
                connected_words=len(connected_bridges), cases=cases)


def main():
    resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2,) * 2)
    start = time.monotonic()
    results = [check(n, length) for n, length in
               ((2, 2), (2, 4), (3, 2), (3, 4), (3, 6), (4, 4), (4, 6))]
    lower_bounds = []
    for n in (3, 4, 16, 64, 128, 256, 1024):
        q = math.comb(n, 2)
        leaf_probability = Fraction(n, (2*n-2)*(2*n-3)) * Fraction(n-1, n)**(n-3)
        p4_identity = Fraction(q*q + 18*math.comb(n, 3) + 12*math.comb(n, 4), q**4)
        if n in (3, 4):
            case = next(row for row in results if row['N'] == n and row['L'] == 2*n-2)
            connected_count = math.factorial(2*n-2) * n**(n-3)
            assert case['connected_words'] == connected_count
        lower_bounds.append(dict(N=n, L=2*n-2, k=2,
                                 leaf_repeat_probability=str(leaf_probability),
                                 projection_tv_lower_bound=str(max(Fraction(), leaf_probability-Fraction(1, q))),
                                 endpoint_tv_lower_bound=str(max(Fraction(), leaf_probability/q-p4_identity))))
    output = dict(status='passed', python=platform.python_version(),
                  commit=subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
                  randomness='none; exact exhaustive integer and rational checks',
                  nonstandard_dependencies=[], memory_address_limit_bytes=512 * 1024**2,
                  elapsed_seconds=time.monotonic()-start, results=results,
                  connected_minimal_lower_bounds=lower_bounds)
    path = Path(__file__).with_name('results.json')
    path.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps({key: output[key] for key in ('status', 'elapsed_seconds', 'python')}))


if __name__ == '__main__':
    main()
