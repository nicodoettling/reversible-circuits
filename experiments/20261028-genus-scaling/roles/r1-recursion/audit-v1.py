"""Reserved deterministic diagnostic; never runs by importing this file.

Independent finite reference: exact DP over (literal permutation, support
partition), not source formulas or production branches. Full word laws only
at N<=3. Standard library, no external dependencies.
"""
import argparse
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial
import importlib.util
import json
from pathlib import Path
import platform
import random
import subprocess
import time

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('r1_sampler', HERE / 'sampler-v1.py')
S = importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name] = S
spec.loader.exec_module(S)


def swap(p, edge):
    # Independent right multiplication of permutation table by an involution.
    a, b = edge
    return tuple(p[b] if i == a else p[a] if i == b else p[i]
                 for i in range(len(p)))


def union(part, edge):
    a, b = (part[i] for i in edge)
    merged = tuple(min(a, b) if x in (a, b) else x for x in part)
    labels = {x: i for i, x in enumerate(sorted(set(merged)))}
    return tuple(labels[x] for x in merged)


def cycle_type(p):
    seen, sizes = set(), []
    for i in range(len(p)):
        if i not in seen:
            j, length = i, 0
            while j not in seen:
                seen.add(j)
                j, length = p[j], length + 1
            sizes.append(length)
    return tuple(sorted(sizes))


def endpoint(alpha):
    answer, offset = [], 0
    for a in alpha:
        answer.extend(list(range(offset + 1, offset + a)) + [offset])
        offset += a
    return tuple(answer)


def exact_tables(n, max_length):
    table = {(tuple(range(n)), tuple(range(n))): 1}
    tables = [table]
    edges = tuple(combinations(range(n), 2))
    for _ in range(max_length):
        nxt = defaultdict(int)
        for (p, part), count in table.items():
            for edge in edges:
                nxt[(swap(p, edge), union(part, edge))] += count
        table = dict(nxt)
        tables.append(table)
    return tables


def compositions(n):
    if not n:
        yield ()
    for first in range(1, n + 1):
        for rest in compositions(n - first):
            yield (first,) + rest


def raw_connected(tables, alpha, genus):
    n = sum(alpha)
    length = n + len(alpha) - 2 + 2 * genus
    return tables[n][length].get((endpoint(alpha), (0,) * n), 0)


@lru_cache(None)
def assignment_law(lengths, ga, gb):
    """Exhaust exact production sequential conditional choices."""
    queue = [({0: 0, 1: 1}, Fraction(1))]
    for i in range(2, len(lengths)):
        nxt = []
        for forced, probability in queue:
            total = S.allocation_mass(lengths, ga, gb, forced)
            for side in (0, 1):
                new = forced | {i: side}
                mass = S.allocation_mass(lengths, ga, gb, new)
                if mass:
                    nxt.append((new, probability * Fraction(mass, total)))
        queue = nxt
    return tuple((tuple(h[i] for i in range(len(lengths))), p) for h, p in queue)


@lru_cache(None)
def whole_law(p, genus):
    """Exact law following production branch/assignment/interleaving weights."""
    if len(p) == 1 and genus == 0:
        return {(): Fraction(1)}
    result = defaultdict(Fraction)
    bs = S.branches(p, genus)
    total = sum(b.weight for b in bs)
    for b in bs:
        bp = Fraction(b.weight, total)
        if b.kind == 'connected':
            for word, probability in whole_law(b.endpoint, b.child_genus).items():
                result[word + (b.edge,)] += bp * probability
        else:
            lengths = tuple(map(len, b.cut_cycles))
            for assignment, ap in assignment_law(lengths, b.ga, b.gb):
                aa = tuple(sorted(x for c, side in zip(b.cut_cycles, assignment)
                                  if side == 0 for x in c))
                bb = tuple(sorted(x for c, side in zip(b.cut_cycles, assignment)
                                  if side == 1 for x in c))
                aw = whole_law(S.restrict(b.endpoint, aa), b.ga)
                bw = whole_law(S.restrict(b.endpoint, bb), b.gb)
                for a, pa in aw.items():
                    ar = tuple(tuple(sorted((aa[x], aa[y]))) for x, y in a)
                    for child_b, pb in bw.items():
                        br = tuple(tuple(sorted((bb[x], bb[y]))) for x, y in child_b)
                        L = len(ar) + len(br)
                        wp = bp * ap * pa * pb / comb(L, len(ar))
                        for positions in combinations(range(L), len(ar)):
                            result[S.interleave(ar, br, positions) + (b.edge,)] += wp
    return dict(result)


def audit():
    start = time.monotonic()
    tables = {n: exact_tables(n, 2*n + 4) for n in range(1, 5)}
    count_cases, identity_rows = 0, []
    branch_cases = 0
    for n in range(1, 5):
        for p in permutations(range(n)):
            alpha = cycle_type(p)
            for genus in range(4):
                expected = tables[n][n + len(alpha) - 2 + 2*genus].get((p, (0,)*n), 0)
                actual = S.count(alpha, genus)
                assert actual == expected, ('count', p, genus, actual, expected)
                count_cases += 1
                if n > 1 and actual:
                    assert sum(b.weight for b in S.branches(p, genus)) == expected
                    branch_cases += 1
                if p == tuple(range(n)):
                    identity_rows.append({'n': n, 'g': genus, 'count': actual})
    global_regressions = []
    for n, length, expected in ((3, 4, 27), (4, 4, 120), (4, 6, 3936)):
        p = tuple(range(n))
        actual = sum(c for (q, _), c in tables[n][length].items() if q == p)
        assert actual == expected
        global_regressions.append({'n': n, 'length': length, 'count': actual})
    transposition = (1, 0, 2)
    ordinary = sum(c for (p, _), c in tables[3][5].items() if p == transposition)
    connected = tables[3][5][(transposition, (0, 0, 0))]
    assert (ordinary, connected) == (81, 80)

    forcing_cases = 0
    for n in range(2, 6):
        for lengths in compositions(n):
            if len(lengths) < 2:
                continue
            for total_g in range(4):
                for ga in range(total_g + 1):
                    gb = total_g - ga
                    assignments = []
                    for tail in product((0, 1), repeat=len(lengths)-2):
                        assignment = (0, 1) + tail
                        a = tuple(x for x, s in zip(lengths, assignment) if s == 0)
                        b = tuple(x for x, s in zip(lengths, assignment) if s == 1)
                        la, lb = sum(a)+len(a)-2+2*ga, sum(b)+len(b)-2+2*gb
                        w = (comb(la+lb, la) * raw_connected(tables, a, ga)
                             * raw_connected(tables, b, gb))
                        assignments.append((assignment, w))
                    for tail in product((-1, 0, 1), repeat=len(lengths)-2):
                        forced = {0: 0, 1: 1} | {i+2: x for i, x in enumerate(tail) if x >= 0}
                        expected = sum(w for assignment, w in assignments
                                       if all(assignment[i] == s for i, s in forced.items()))
                        actual = S.allocation_mass(lengths, ga, gb, forced)
                        assert actual == expected, ('forcing', lengths, ga, gb, forced, actual, expected)
                        forcing_cases += 1

    law_rows, total_words = [], 0
    for n in (2, 3):
        for p in permutations(range(n)):
            for genus in range(4):
                law = whole_law(p, genus)
                count = S.count(cycle_type(p), genus)
                assert len(law) == count and sum(law.values()) == 1
                assert all(probability == Fraction(1, count) for probability in law.values())
                for word in law:
                    assert S.evaluate(n, word) == p
                    assert len(S.components(n, word)) == 1
                    assert len(word) == n + len(cycle_type(p)) - 2 + 2*genus
                total_words += len(law)
                law_rows.append({'n': n, 'endpoint': list(p), 'g': genus,
                                 'words': len(law), 'probability': str(Fraction(1, count))})

    seeds = (19401, 19402, 19403)
    sample_cases = 0
    for seed in seeds:
        rng = random.Random(seed)
        for n in (2, 3, 4):
            for genus in range(4):
                for _ in range(5):
                    word = S.sample_identity(n, genus, rng)
                    assert S.evaluate(n, word) == tuple(range(n))
                    assert len(S.components(n, word)) == 1
                    assert len(word) == 2*n - 2 + 2*genus
                    sample_cases += 1

    return {'status': 'pass', 'elapsed_seconds': time.monotonic()-start,
            'python': platform.python_version(), 'dependencies': 'standard-library-only',
            'commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
            'seeds': list(seeds), 'count_cases': count_cases, 'branch_cases': branch_cases,
            'forcing_cases': forcing_cases, 'whole_law_cases': len(law_rows),
            'whole_law_words': total_words, 'sample_cases': sample_cases,
            'identity_counts': identity_rows, 'global_regressions': global_regressions,
            'connected_vs_ordinary': [connected, ordinary], 'whole_laws': law_rows,
            'peak_reference_states': max(len(t) for ts in tables.values() for t in ts),
            'limitations': ['No all N4,g3 literal enumeration',
                            'Genus-three diagnostic coefficient list is supplied',
                            'Finite tests do not certify arbitrary genus or complexity']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    result = audit()
    output = Path(args.output)
    temporary = output.with_name(output.name + '.tmp')
    temporary.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    temporary.replace(output)
    print(json.dumps({key: result[key] for key in ('status', 'elapsed_seconds', 'count_cases',
                                                   'forcing_cases', 'whole_law_words')}))
