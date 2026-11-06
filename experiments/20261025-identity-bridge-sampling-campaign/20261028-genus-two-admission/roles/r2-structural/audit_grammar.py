"""Author exact C2 grammar/parser checks. No stochastic law inference."""
import argparse
import ast
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations, product
from math import factorial
from pathlib import Path
import hashlib
import importlib.util
import json
import os
import platform
import random
import time

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('c2_author_target', HERE / 'cut_genus_two.py')
c2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c2)


class Fork(Exception):
    def __init__(self, options):
        self.options = options


class ExactExecution:
    def __init__(self, tape):
        self.tape, self.cursor, self.probability = tape, 0, Q(1)

    def choose(self, items, ignored=None):
        items = [(x, Q(w)) for x, w in items if w]
        assert items and all(w > 0 for _, w in items)
        if len(items) == 1:
            return items[0][0]
        total = sum(w for _, w in items)
        if self.cursor == len(self.tape):
            raise Fork(tuple(w / total for _, w in items))
        i = self.tape[self.cursor]
        self.cursor += 1
        x, w = items[i]
        self.probability *= w / total
        return x

    def randrange(self, n):
        return self.choose([(i, 1) for i in range(n)])

    def shuffle(self, values):
        values[:] = self.choose([(p, 1) for p in sorted(set(permutations(values)))])


def canonical(code):
    vertices, edges = c2.flatten_code(code)
    return code['kind'], tuple(vertices), tuple(edges), code['cut']


def execution_law(operation):
    stack, out = [((), Q(1))], defaultdict(Q)
    nodes = leaves = depth = 0
    saved = c2.choose
    try:
        while stack:
            tape, prefix = stack.pop()
            execution = ExactExecution(tape)
            c2.choose = execution.choose
            nodes += 1
            depth = max(depth, len(tape))
            try:
                value = operation(execution)
            except Fork as event:
                assert execution.probability == prefix
                for i, probability in enumerate(event.options):
                    stack.append((tape + (i,), prefix * probability))
            else:
                assert execution.cursor == len(tape) and execution.probability == prefix
                out[canonical(value)] += prefix
                leaves += 1
    finally:
        c2.choose = saved
    assert sum(out.values()) == 1
    return dict(out), dict(execution_nodes=nodes, execution_leaves=leaves, depth=depth)


@lru_cache(None)
def forests(mass):
    if mass == 0:
        return ((),)
    out = []
    for a in range(1, mass + 1):
        for below in range(mass - a + 1):
            for tree in forests(below):
                for rest in forests(mass - a - below):
                    out.append(((a, tree),) + rest)
    return tuple(out)


def compositions(total, count, minimum):
    if count == 0:
        if total == 0:
            yield ()
        return
    for a in range(minimum, total - minimum * (count - 1) + 1):
        for tail in compositions(total - a, count - 1, minimum):
            yield (a,) + tail


def node_from_forest(forest, color):
    return dict(color=color, genus=0,
                children=[(a, node_from_forest(child, -color)) for a, child in forest])


def all_nodes(code):
    stack = [code['root']] if code['kind'] == 'tree' else list(code['nodes'])
    out = []
    while stack:
        node = stack.pop()
        out.append(node)
        stack.extend(child for _, child in node['children'])
    return out


def independent_h(parts, genus):
    size, degree = sum(parts), len(parts)
    if genus == 0:
        return Q(size) ** (degree - 3)
    elementary = [1]
    for a in parts:
        nxt = [0] * (len(elementary) + 1)
        for j, value in enumerate(elementary):
            nxt[j] += value
            nxt[j + 1] += a * value
        elementary = nxt
    value = Q(size) ** degree - Q(size) ** (degree - 1)
    for j in range(2, degree + 1):
        value -= factorial(j - 2) * elementary[j] * Q(size) ** (degree - j)
    assert value >= 0
    return value / 24


def code_weight(code, n):
    vertices, edges = c2.flatten_code(code)
    lists = [[] for _ in vertices]
    weight = Q(1, len(code['nodes'])) if code['kind'] == 'cycle' else Q(1)
    for u, v, a in edges:
        weight *= Q(a ** (2 * a + 1), factorial(a) ** 2)
        lists[u].append(a)
        lists[v].append(a)
    for (color, genus), parts in zip(vertices, lists):
        weight *= independent_h(parts, genus)
    for node in all_nodes(code):
        weight /= factorial(len(node['children']))
    j = code['cut']
    weight *= factorial(j) * factorial(2 * n + 2 - j)
    return weight


def independent_codes(n):
    out = defaultdict(Q)
    for forest in forests(n):
        code = {'kind': 'tree', 'root': node_from_forest(forest, -1)}
        code['root']['genus'] = 1
        nodes = all_nodes(code)
        code['cut'] = n + sum(node['color'] for node in nodes) + 1
        for marked in (node for node in nodes if node['color'] == 1):
            marked['genus'] = 1
            weight = code_weight(code, n)
            if weight:
                out[canonical(code)] += weight
            marked['genus'] = 0
    for length in range(2, n + 1, 2):
        for mass in range(length, n + 1):
            for sizes in compositions(mass, length, 1):
                for hanging in compositions(n - mass, length, 0):
                    for choices in product(*(forests(x) for x in hanging)):
                        code = {'kind': 'cycle', 'sizes': sizes,
                                'nodes': [node_from_forest(f, -1 if i % 2 == 0 else 1)
                                          for i, f in enumerate(choices)]}
                        nodes = all_nodes(code)
                        code['cut'] = n + sum(node['color'] for node in nodes) + 2
                        for marked in (node for node in nodes if node['color'] == -1):
                            marked['genus'] = 1
                            weight = code_weight(code, n)
                            if weight:
                                out[canonical(code)] += weight
                            marked['genus'] = 0
    return dict(out)


def macro_key(code_key, label_list):
    kind, vertices, edges, j = code_key
    n = len(label_list)
    endpoint = list(range(n))
    support = [set() for _ in vertices]
    cursor = 0
    for u, v, size in edges:
        block = label_list[cursor:cursor + size]
        cursor += size
        for a, b in zip(block, block[1:] + block[:1]):
            endpoint[a] = b
        support[u].update(block)
        support[v].update(block)
    left, right = [], []
    for (color, genus), labels in zip(vertices, support):
        (left if color == -1 else right).append((tuple(sorted(labels)), genus))
    return (j, tuple(endpoint), tuple(sorted(left)), tuple(sorted(right)))


def audit(n, references, samples):
    started = time.perf_counter()
    grammar = c2.CutGrammar(n)
    actual, meta = execution_law(grammar.sample_code)
    expected = independent_codes(n)
    normalizer = sum(expected.values())
    assert normalizer * factorial(n) == grammar.cut_count
    assert actual == {key: value / normalizer for key, value in expected.items()}
    macros = defaultdict(Q)
    descriptions = defaultdict(int)
    for code, probability in actual.items():
        for labels in permutations(range(n)):
            key = macro_key(code, labels)
            macros[key] += probability / factorial(n)
            descriptions[key] += 1
    ref = next((case for case in references['cases'] if case['N'] == n), None)
    if ref:
        expected_macros = {ast.literal_eval(item['key']): Q(item['literal_count'], ref['cut_incidences'])
                           for item in ref['macro_data']}
        assert macros == expected_macros
        assert grammar.cut_count == ref['cut_incidences']
    smoke = []
    for seed in (1729, 2718):
        rng = random.Random(seed)
        total_attempts = 0
        for _ in range(samples):
            word, attempts = grammar.sample(rng)
            assert len(word) == 2 * n + 2 and c2.genus(word, n) == 2
            total_attempts += attempts
        smoke.append(dict(seed=seed, samples=samples, attempts=total_attempts, valid=True))
    return dict(N=n, cut_count=int(grammar.cut_count), numeric_codes=len(actual), labeled_macros=len(macros),
                parser_equals_independent_code_law=True, macro_matches_literal_reference=bool(ref),
                maximum_macro_description_count=max(descriptions.values()),
                execution=meta, smoke=smoke, elapsed_seconds=time.perf_counter() - started,
                macro_data=[dict(key=repr(key), probability=str(probability), descriptions=descriptions[key])
                            for key, probability in sorted(macros.items())])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-n', type=int, default=4)
    parser.add_argument('--samples', type=int, default=5)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    references = json.loads((HERE.parent.parent / 'coordinator/cut-reference-results-v1.json').read_text())
    result = dict(status='complete', generated_utc=datetime.now(timezone.utc).isoformat(),
                  python=platform.python_version(), nonstandard_dependencies=[],
                  deterministic_seed=None, stochastic_validity_seeds=[1729,2718],
                  base_commit='d8893491e04aff74ff3185f7054470ffa24a44a4',
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  sampler_sha256=hashlib.sha256((HERE / 'cut_genus_two.py').read_bytes()).hexdigest(),
                  cases=[audit(n, references, args.samples) for n in range(2,args.max_n+1)])
    temp = args.output.with_name(args.output.name + '.tmp')
    temp.write_text(json.dumps(result, indent=2) + '\n')
    os.replace(temp, args.output)
    print(json.dumps(dict(status='complete', cases=[{k:case[k] for k in ('N','cut_count','numeric_codes','labeled_macros','elapsed_seconds')} for case in result['cases']]),sort_keys=True))


if __name__ == '__main__':
    main()
