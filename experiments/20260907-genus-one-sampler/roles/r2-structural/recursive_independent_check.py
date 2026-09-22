"""Nonauthor audit: raw allocation moments and forward production stack law.

Imports production code solely as the implementation under test. The reference
uses literal finite subsets and words and a separately coded signed formula.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
import hashlib
import importlib.util
from itertools import combinations, permutations, product
import json
from math import comb, factorial, prod
from pathlib import Path
import platform
import random
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
RUN = HERE.parent.parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


s = load('r2_reviewed_r1', RUN / 'roles/r1-recursive/sampler.py')


def elementary(parts):
    # Literal marked subsets, independent of the production E/S recurrence.
    return [sum(prod(parts[i] for i in subset)
                for subset in combinations(range(len(parts)), j))
            for j in range(len(parts) + 1)]


def moments(parts):
    e = elementary(parts)
    marks = [sum(prod(parts[i] for i in subset) * sum(parts[i] for i in subset)
                 for subset in combinations(range(len(parts)), j))
             for j in range(len(parts) + 1)]
    return e, marks, sum(a * (a - 1) for a in parts)


def reference_count(parts, genus):
    n, k = sum(parts), len(parts)
    common = prod(Q(a ** a, factorial(a - 1)) for a in parts)
    length = n + k - 2 + 2 * genus
    if genus == 0:
        answer = factorial(length) * common * Q(n) ** (k - 3)
    else:
        e = elementary(parts)
        bracket = n * n - n - sum(Q(n) ** (2 - j) * factorial(j - 2) * e[j]
                                  for j in range(2, k + 1))
        answer = factorial(length) * common * Q(n) ** (k - 2) * bracket / 24
    assert answer.denominator == 1 and answer >= 0
    return answer.numerator


def reference_weight(lengths, assignment, ga, gb):
    aa = [a for a, side in zip(lengths, assignment) if side == 0]
    bb = [a for a, side in zip(lengths, assignment) if side == 1]
    ra = sum(aa) + len(aa) - 2 + 2 * ga
    rb = sum(bb) + len(bb) - 2 + 2 * gb
    return comb(ra + rb, ra) * reference_count(aa, ga) * reference_count(bb, gb)


def forced_moment_audit():
    inventories = [(1, 1, 1), (2, 1, 1, 2), (3, 2, 1, 4, 1, 2, 3),
                   (1, 5, 2, 2, 1, 3, 1, 4)]
    rows = []
    for lengths in inventories:
        all_assignments = [(0, 1) + free for free in product((0, 1), repeat=len(lengths) - 2)]
        reference = {}
        for allocation in all_assignments:
            reference[allocation] = {
                'moments': [moments([a for a, side in zip(lengths, allocation) if side == tracked])
                            for tracked in (0, 1)],
                'weights': {(ga, gb): reference_weight(lengths, allocation, ga, gb)
                            for ga, gb in ((0, 0), (1, 0), (0, 1))}}
        queries = cells = zeros = 0
        digest = hashlib.sha256()
        for partial in product((-1, 0, 1), repeat=len(lengths) - 2):
            forced = {0: 0, 1: 1}
            forced.update({i + 2: side for i, side in enumerate(partial) if side != -1})
            retained = [a for a in all_assignments if all(a[i] == side for i, side in forced.items())]
            for tracked in (0, 1):
                expected = {}
                for allocation in retained:
                    parts = [a for a, side in zip(lengths, allocation) if side == tracked]
                    key = sum(parts), len(parts)
                    e, marks, q = reference[allocation]['moments'][tracked]
                    if key not in expected:
                        expected[key] = ([0] * len(e), [0] * len(e), 0)
                    ee, ss, qq = expected[key]
                    for j in range(len(e)):
                        ee[j] += e[j]
                        ss[j] += marks[j]
                    expected[key] = ee, ss, qq + q
                actual = s.allocation_table(lengths, forced, tracked)
                assert actual == expected, (lengths, forced, tracked, actual, expected)
                cells += sum(2 * len(e) + 1 for e, _, _ in expected.values())
                queries += 1
            for ga, gb in ((0, 0), (1, 0), (0, 1)):
                expected = sum(reference[a]['weights'][ga, gb] for a in retained)
                actual = s.allocation_mass(lengths, ga, gb, forced)
                assert actual == expected, (lengths, forced, ga, gb, actual, expected)
                zeros += expected == 0
                queries += 1
                digest.update(repr((partial, ga, gb, actual)).encode())
        rows.append(dict(lengths=lengths, total_size=sum(lengths), assignments=len(all_assignments),
                         partial_queries=queries, exact_moment_entries=cells,
                         zero_mass_queries=zeros, digest=digest.hexdigest()))
    return rows


class NeedDecision(Exception):
    def __init__(self, weights):
        self.weights = weights


class Oracle:
    def __init__(self, tape):
        self.tape, self.position = tape, 0

    def decide(self, values, weights):
        positive = [(v, w) for v, w in zip(values, weights) if w]
        assert positive and all(w > 0 for _, w in positive)
        if len(positive) == 1:
            return positive[0][0]
        if self.position == len(self.tape):
            raise NeedDecision(tuple(w for _, w in positive))
        index = self.tape[self.position]
        self.position += 1
        return positive[index][0]


def forward_law(call, module, leaf_cap=10000):
    original_choice, original_randbelow = module.weighted_choice, module.randbelow
    todo = [((), Q(1))]
    law = defaultdict(Q)
    leaves = trials = 0
    try:
        while todo:
            tape, probability = todo.pop()
            oracle = Oracle(tape)
            module.weighted_choice = lambda rng, values, weights: oracle.decide(values, weights)
            module.randbelow = lambda rng, bound: oracle.decide(range(bound), (1,) * bound)
            trials += 1
            try:
                word = call()
            except NeedDecision as decision:
                total = sum(decision.weights)
                for i, weight in enumerate(decision.weights):
                    todo.append((tape + (i,), probability * Q(weight, total)))
            else:
                assert oracle.position == len(tape)
                law[tuple(word)] += probability
                leaves += 1
                assert leaves <= leaf_cap
    finally:
        module.weighted_choice, module.randbelow = original_choice, original_randbelow
    assert sum(law.values()) == 1
    return law, dict(logical_leaf_tapes=leaves, implementation_replays=trials,
                     word_count=len(law), all_words_one_logical_tape=leaves == len(law))


def own_eval(word, n):
    p = list(range(n))
    for a, b in word:
        p[a], p[b] = p[b], p[a]
    return tuple(p)


def own_components(word, n):
    blocks = [{i} for i in range(n)]
    for a, b in word:
        aa = next(block for block in blocks if a in block)
        bb = next(block for block in blocks if b in block)
        if aa is not bb:
            blocks.remove(aa)
            blocks.remove(bb)
            blocks.append(aa | bb)
    return blocks


def direct_words(n, endpoint, length, connected=True, allowed=False):
    good = set()
    for word in product(tuple(combinations(range(n), 2)), repeat=length):
        if own_eval(word, n) != endpoint:
            continue
        blocks = own_components(word, n)
        if connected and len(blocks) != 1:
            continue
        if allowed:
            for block in blocks:
                ell = sum(a in block for a, _ in word)
                genus = (ell - 2 * len(block) + 2) // 2
                if genus > 1:
                    break
            else:
                good.add(word)
            continue
        good.add(word)
    return good


def stack_law_audit():
    rows = []
    cases = [(p, genus) for p in permutations(range(3)) for genus in (0, 1)]
    cases += [((1, 0, 3, 2), 1), ((1, 2, 3, 0), 1)]
    for p, genus in cases:
        n = len(p)
        length = n + len(s.cycles(p)) - 2 + 2 * genus
        law, row = forward_law(lambda: s.sample(p, genus, object()), s)
        expected = direct_words(n, p, length)
        assert set(law) == expected
        assert all(value == Q(1, len(expected)) for value in law.values())
        assert len(expected) == reference_count([len(c) for c in s.cycles(p)], genus)
        row.update(endpoint=p, genus=genus, length=length,
                   each_probability=str(Q(1, len(expected))),
                   digest=hashlib.sha256(repr(sorted(law.items())).encode()).hexdigest())
        rows.append(row)
    return rows


def integration_audit():
    top = load('r2_top_integration', RUN / 'sample.py')
    rows = []
    for n, m in ((3, 4), (4, 4), (5, 4)):
        certificate = top.sample_restricted_components(n, m, random.Random(1729)).covered_mass
        law, row = forward_law(lambda: top.sample_restricted_components(n, m, object()).word,
                              top.recursive)
        full = direct_words(n, tuple(range(n)), m, connected=False)
        allowed = direct_words(n, tuple(range(n)), m, connected=False, allowed=True)
        assert set(law) == allowed
        assert all(value == Q(1, len(allowed)) for value in law.values())
        assert certificate == Q(len(allowed), len(full))
        row.update(n=n, length=m, global_count=len(full), allowed_count=len(allowed),
                   certificate=str(certificate), each_probability=str(Q(1, len(allowed))))
        rows.append(row)
    # Positive omitted mass and the saturated two-component branch are checked
    # exactly by direct words, while two seeded samples check the integration.
    boundary = []
    for n, m in ((0, 0), (1, 0), (2, 0), (2, 2), (2, 4), (3, 6), (4, 6), (4, 8)):
        full = direct_words(n, tuple(range(n)), m, connected=False)
        allowed = direct_words(n, tuple(range(n)), m, connected=False, allowed=True)
        for seed in (1729, 2718):
            draw = top.sample_restricted_components(n, m, random.Random(seed))
            assert draw.word in allowed
            assert draw.covered_mass == Q(len(allowed), len(full))
        if m == 2 * n and n >= 2:
            for word in allowed:
                blocks = own_components(word, n)
                assert all(len(b) >= 2 and sum(a in b for a, _ in word) == 2 * len(b)
                           for b in blocks)
        boundary.append(dict(n=n, length=m, global_count=len(full),
                             allowed_count=len(allowed), certificate=str(Q(len(allowed), len(full)))))
    rejected = []
    for n, m in ((1, 2), (2, 3), (2, 6), (3, 8)):
        try:
            top.sample_restricted_components(n, m, random.Random(1729))
        except ValueError as exc:
            rejected.append(dict(n=n, length=m, error=str(exc)))
        else:
            raise AssertionError((n, m))
    return dict(full_forward_laws=rows, boundary_certificates=boundary,
                correctly_rejected=rejected)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default=str(HERE / 'recursive_independent_results.json'))
    args = parser.parse_args()
    result = dict(python=platform.python_version(), dependencies={},
                  command=' '.join(sys.argv), exact_seed=None, diagnostic_seeds=[1729, 2718],
                  commit=subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
                  git_status=subprocess.check_output(['git', 'status', '--short'], text=True),
                  methodology='independent literal subset moments and complete forward decision-tree execution of production stack')
    # Canonical cached-prefix regression: reject multiplication of marginal
    # lightness bounds. R1 instead recomputes each exact exposed-assignment sum.
    gamma, aa, cc, dd = Q(1, 10), Q(21, 2000), Q(1, 20), Q(879, 1000)
    assert 2 * aa + 2 * cc + dd == 1
    assert 2 * cc == gamma and aa + cc < gamma and aa < gamma
    joint, later = aa, aa / (aa + 2 * cc)
    assert joint > gamma * gamma and later == Q(21, 221) < gamma
    result['cp1_regression'] = dict(posterior_A_each=str(aa), posterior_C_each=str(cc),
                                    posterior_D=str(dd), joint=str(joint),
                                    invalid_product_bound=str(gamma * gamma), later=str(later),
                                    verdict='old marginal product bound rejected; R1 uses exact conditional sums')
    start = time.monotonic()
    for name, test in [('forced_moments', forced_moment_audit),
                       ('actual_stack_forward_law', stack_law_audit),
                       ('top_integration', integration_audit)]:
        section = time.monotonic()
        result[name] = test()
        result[name + '_seconds'] = time.monotonic() - section
        Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
        print(name, result[name + '_seconds'], flush=True)
    result['elapsed_seconds'] = time.monotonic() - start
    result['all_passed'] = True
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print('all_passed', result['elapsed_seconds'], flush=True)


if __name__ == '__main__':
    main()
