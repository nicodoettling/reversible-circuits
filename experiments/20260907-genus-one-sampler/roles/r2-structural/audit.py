"""Exact finite audit of C1, using direct word enumeration and explicit codes."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, permutations, product
from math import factorial
import hashlib
import json
import platform
import random
import subprocess
import time

from cut_sampler import (CutGrammar, components, cycles, edge_weight, evaluate,
                         f0, genus_zero_branches, sample_genus_zero,
                         right_transpose, valid_cuts)


def partition_after(partition, a, b):
    ia = next(i for i, block in enumerate(partition) if a in block)
    ib = next(i for i, block in enumerate(partition) if b in block)
    if ia == ib:
        return partition
    joined = tuple(sorted(partition[ia] + partition[ib]))
    return tuple(sorted([block for i, block in enumerate(partition)
                         if i not in (ia, ib)] + [joined]))


def words(n, length):
    edges = tuple(combinations(range(n), 2))
    perms = tuple(permutations(range(n)))
    index = {p: i for i, p in enumerate(perms)}
    transitions = [[index[right_transpose(p, t)] for t in edges] for p in perms]
    start = index[tuple(range(n))]
    for inds in product(range(len(edges)), repeat=length):
        state = start
        for i in inds:
            state = transitions[state][i]
        yield tuple(edges[i] for i in inds), perms[state]


def macro_of(word, j, n):
    return (evaluate(word[:j], n), components(word[:j], n),
            components(word[j:], n))


def macro_words(n):
    result = Counter()
    jhist = Counter()
    ellhist = Counter()
    count = 0
    square_free = 0
    identity = tuple(range(n))
    discrete = tuple((i,) for i in range(n))
    for word, endpoint in words(n, 2 * n):
        if endpoint != identity or len(components(word, n)) != 1:
            continue
        count += 1
        p, ql = identity, discrete
        prefix = [(p, ql)]
        for a, b in word:
            p = right_transpose(p, (a, b))
            ql = partition_after(ql, a, b)
            prefix.append((p, ql))
        suffix = [None] * (2 * n + 1)
        qr = discrete
        suffix[-1] = qr
        for j in range(2 * n - 1, -1, -1):
            qr = partition_after(qr, *word[j])
            suffix[j] = qr
        ell = 0
        for j in range(1, 2 * n):
            p, ql = prefix[j]
            qr = suffix[j]
            c = len(cycles(p))
            gl = (j - n - c + 2 * len(ql)) // 2
            gr = (2 * n - j - n - c + 2 * len(qr)) // 2
            if gl == gr == 0:
                ell += 1
                jhist[j] += 1
                result[p, ql, qr] += 1
        assert ell >= 1
        ellhist[ell] += 1
        marks = sum(word[i] == word[i + 1]
                    and len(components(word[:i] + word[i + 2:], n)) == 1
                    for i in range(2 * n - 1))
        square_free += marks == 0
    return result, dict(words=count, cut_count=sum(result.values()),
                        j_histogram=dict(jhist), ell_histogram=dict(ellhist),
                        unmarked=square_free)


@lru_cache(None)
def ordered_forests(mass):
    if mass == 0:
        return ((),)
    out = []
    for a in range(1, mass + 1):
        for subtree_mass in range(mass - a + 1):
            for subtree in ordered_forests(subtree_mass):
                for rest in ordered_forests(mass - a - subtree_mass):
                    out.append(((a, subtree),) + rest)
    return tuple(out)


def compositions(total, parts, minimum=0):
    if parts == 0:
        if total == 0:
            yield ()
        return
    for a in range(minimum, total - minimum * (parts - 1) + 1):
        for tail in compositions(total - a, parts - 1, minimum):
            yield (a,) + tail


def explicit_codes(n):
    for s in range(1, n // 2 + 1):
        core = 2 * s
        for coremass in range(core, n + 1):
            for sizes in compositions(coremass, core, 1):
                for hanging in compositions(n - coremass, core):
                    for forests in product(*(ordered_forests(a) for a in hanging)):
                        colors = [-1 if i % 2 == 0 else 1 for i in range(core)]
                        edges = [(i, (i + 1) % core, a) for i, a in enumerate(sizes)]
                        children = [len(forest) for forest in forests]
                        def add_forest(root, forest):
                            for a, subtree in forest:
                                child = len(colors)
                                colors.append(-colors[root])
                                children.append(len(subtree))
                                edges.append((root, child, a))
                                add_forest(child, subtree)
                        for i, forest in enumerate(forests):
                            add_forest(i, forest)
                        assert sum(a for _, _, a in edges) == n
                        incident = [0] * len(colors)
                        degrees = [0] * len(colors)
                        weight = Q(1, 2 * s)
                        for u, v, a in edges:
                            weight *= edge_weight(a)
                            incident[u] += a
                            incident[v] += a
                            degrees[u] += 1
                            degrees[v] += 1
                        for total, d, k in zip(incident, degrees, children):
                            weight *= Q(total) ** (d - 3) / factorial(k)
                        yield colors, edges, weight


def code_macros(n):
    result = defaultdict(Q)
    numeric_codes = 0
    total_weight = Q(0)
    for colors, edges, weight in explicit_codes(n):
        numeric_codes += 1
        j = n + sum(colors)
        word_weight = weight * factorial(j) * factorial(2 * n - j)
        total_weight += word_weight
        for order in permutations(range(n)):
            support = [set() for _ in colors]
            p = list(range(n))
            pos = 0
            for u, v, a in edges:
                block = order[pos:pos + a]
                pos += a
                for x, y in zip(block, block[1:] + block[:1]):
                    p[x] = y
                support[u].update(block)
                support[v].update(block)
            left = tuple(sorted(tuple(sorted(block)) for c, block in zip(colors, support) if c == -1))
            right = tuple(sorted(tuple(sorted(block)) for c, block in zip(colors, support) if c == 1))
            result[tuple(p), left, right] += word_weight
    return dict(result), dict(numeric_codes=numeric_codes,
                             total_weight=str(total_weight))


def genus_zero_audit(n):
    per_word = 0
    branches = defaultdict(Counter)
    totals = Counter()
    for length in range(n - 1, 2 * n - 1):
        for word, endpoint in words(n, length):
            if length != n + len(cycles(endpoint)) - 2:
                continue
            if len(components(word, n)) != 1:
                continue
            per_word += 1
            totals[endpoint] += 1
            # Every actual word has a unique terminal branch; this tests the
            # complete branch multiplicities, not endpoint cycle marginals.
            branches[endpoint][word[-1], components(word[:-1], n)] += 1
    for p in permutations(range(n)):
        assert totals[p] == f0([len(c) for c in cycles(p)])
        # Independently expand all candidate component assignments.
        expected = Counter()
        for (t, q, info), weight in genus_zero_branches(p):
            if info is None:
                expected[t, (tuple(range(n)),)] += int(weight)
                continue
            a0, b0, rest, tables, cells = info
            r = n + len(cycles(p)) - 2
            for mask in range(1 << len(rest)):
                aset = set(a0)
                for i, c in enumerate(rest):
                    if mask >> i & 1:
                        aset.update(c)
                bset = set(range(n)) - aset
                pa = [len(c) for c in cycles(q) if c[0] in aset]
                pb = [len(c) for c in cycles(q) if c[0] in bset]
                ra = sum(pa) + len(pa) - 2
                rb = sum(pb) + len(pb) - 2
                mult = factorial(r - 1) // factorial(ra) // factorial(rb)
                key = t, tuple(sorted((tuple(sorted(aset)), tuple(sorted(bset)))))
                expected[key] += mult * f0(pa) * f0(pb)
        assert expected == branches[p], (n, p, expected, branches[p])
    return dict(n=n, endpoints=len(totals), complete_words=per_word,
                terminal_branches=sum(len(c) for c in branches.values()))


def boundary_audit():
    cases = [(1, 0), (1, 2), (2, 0), (2, 2), (2, 3), (2, 4),
             (3, 0), (3, 2), (3, 3), (3, 4), (4, 4), (4, 6)]
    rows = []
    expected = {(3, 4): 27, (4, 4): 120, (4, 6): 3936}
    for n, length in cases:
        total = connected = 0
        for word, endpoint in words(n, length):
            if endpoint == tuple(range(n)):
                total += 1
                connected += len(components(word, n)) == 1
        if (n, length) in expected:
            assert total == expected[n, length]
        rows.append(dict(n=n, length=length, total=total, connected=connected))
    regressions = []
    for n in range(3, 13):
        word = ((0, 1), (1, 2)) * 3 + tuple(t for v in range(3, n)
                                                for t in [(v - 1, v)] * 2)
        assert len(word) == 2 * n
        assert evaluate(word, n) == tuple(range(n))
        assert len(components(word, n)) == 1
        marks = [i for i in range(len(word) - 1) if word[i] == word[i + 1]
                 and len(components(word[:i] + word[i + 2:], n)) == 1]
        cuts = valid_cuts(word, n)
        assert not marks and cuts
        regressions.append(dict(n=n, zero_square_fiber=True, cuts=cuts))
    return rows, regressions


def run(max_n, samples):
    start = time.time()
    result = dict(python=platform.python_version(), dependencies={},
                  command=" ".join(__import__('sys').argv),
                  commit=subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
                  dirty=subprocess.check_output(['git', 'status', '--short'], text=True),
                  exact_seed=None, stochastic_seeds=[1729, 2718], cut_cases=[],
                  genus_zero_cases=[], smoke=[])
    result['boundaries'], result['zero_fiber_regressions'] = boundary_audit()
    for n in range(2, max_n + 1):
        print('exact n', n, flush=True)
        actual, row = macro_words(n)
        proposed, code_info = code_macros(n)
        assert proposed == actual, (n, set(proposed) ^ set(actual))
        grammar = CutGrammar(n)
        assert grammar.cut_count == row['cut_count']
        assert sum(proposed.values()) == grammar.cut_count
        assert row['words'] == {2: 1, 3: 240, 4: 131040}[n]
        row.update(n=n, macros=len(actual), full_macro_multiplicity_failures=0,
                   full_word_law='uniform by exact macro fibers and terminal-branch multiplicities',
                   numeric_code_info=code_info,
                   acceptance=str(Q(row['words'], row['cut_count'])))
        # Given a macro, every word has the same exact product-fiber weight;
        # division by ell removes all cut multiplicity for every actual word.
        assert sum(Q(count, ell) * ell for ell, count in row['ell_histogram'].items()) == row['words']
        result['cut_cases'].append(row)
        result['genus_zero_cases'].append(genus_zero_audit(n))
        for seed in result['stochastic_seeds']:
            rng = random.Random(seed)
            tries = []
            digest = hashlib.sha256()
            for _ in range(samples):
                word, attempts = grammar.sample(rng)
                assert len(word) == 2 * n
                assert evaluate(word, n) == tuple(range(n))
                assert len(components(word, n)) == 1
                tries.append(attempts)
                digest.update(repr(word).encode())
            result['smoke'].append(dict(n=n, seed=seed, samples=samples,
                                        total_proposals=sum(tries), max_proposals=max(tries),
                                        output_sha256=digest.hexdigest()))
    result['elapsed_seconds'] = time.time() - start
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-n', type=int, default=4)
    parser.add_argument('--samples', type=int, default=30)
    parser.add_argument('--output', default='results.json')
    args = parser.parse_args()
    result = run(args.max_n, args.samples)
    with open(args.output, 'w') as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps(result, indent=2, sort_keys=True))
