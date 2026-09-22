"""Nonauthor exact audit of R2 C1's actual backward parser and cut sampler.

The production module is read without modification. Its `choose` callback and
RNG shuffles are instrumented in this process to enumerate finite weighted
execution trees exactly; grammar coefficients and decoding are unchanged.
No genus-one count formula is used.
"""

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, permutations, product
from math import factorial
from pathlib import Path
import hashlib
import importlib.util
import json
import platform
import subprocess
import time


ROOT = Path(__file__).resolve().parents[0]
R2 = ROOT.parent / "r2-structural"
spec = importlib.util.spec_from_file_location("r2_frozen_cut", R2 / "cut_sampler.py")
c1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c1)


class Fork(Exception):
    def __init__(self, options):
        self.options = options


class ExactExecution:
    def __init__(self, tape):
        self.tape = tape
        self.cursor = 0
        self.probability = Q(1)

    def choose(self, items, ignored_rng=None):
        items = [(value, Q(weight)) for value, weight in items if weight]
        assert items and all(weight > 0 for _, weight in items)
        if len(items) == 1:
            return items[0][0]
        total = sum(w for _, w in items)
        if self.cursor == len(self.tape):
            raise Fork(tuple(w / total for _, w in items))
        index = self.tape[self.cursor]
        self.cursor += 1
        value, weight = items[index]
        self.probability *= weight / total
        return value

    def shuffle(self, values):
        # Uniform shuffling induces uniform distinct multiset permutations.
        options = sorted(set(permutations(values)))
        chosen = self.choose([(p, 1) for p in options])
        values[:] = chosen

    def randrange(self, bound):
        return self.choose([(i, 1) for i in range(bound)])


def execution_distribution(operation, canonical):
    """Enumerate positive-mass decision tapes, preserving exact conditionals."""
    saved = c1.choose
    stack = [((), Q(1))]
    law = defaultdict(Q)
    nodes = leaves = 0
    max_depth = 0
    try:
        while stack:
            tape, expected_prefix_probability = stack.pop()
            execution = ExactExecution(tape)
            c1.choose = execution.choose
            nodes += 1
            max_depth = max(max_depth, len(tape))
            try:
                value = operation(execution)
            except Fork as event:
                assert execution.probability == expected_prefix_probability
                assert sum(event.options) == 1
                for i, probability in enumerate(event.options):
                    stack.append((tape + (i,), execution.probability * probability))
            else:
                assert execution.cursor == len(tape)
                assert execution.probability == expected_prefix_probability
                law[canonical(value)] += execution.probability
                leaves += 1
    finally:
        c1.choose = saved
    assert sum(law.values()) == 1
    return dict(law), dict(execution_nodes=nodes, weighted_leaves=leaves, max_branch_depth=max_depth)


@lru_cache(None)
def forests(mass):
    if mass == 0:
        return ((),)
    result = []
    for size in range(1, mass + 1):
        for below in range(mass - size + 1):
            for subtree in forests(below):
                for rest in forests(mass - size - below):
                    result.append(((size, subtree),) + rest)
    return tuple(result)


def compositions(total, number, minimum):
    if number == 0:
        if total == 0:
            yield ()
        return
    for first in range(minimum, total - minimum * (number - 1) + 1):
        for tail in compositions(total - first, number - 1, minimum):
            yield (first,) + tail


def independent_codes(n):
    """Direct finite positive-size plane core/forest inventory, no C1 DP."""
    result = defaultdict(Q)
    for core in range(2, n + 1, 2):
        for core_mass in range(core, n + 1):
            for edge_sizes in compositions(core_mass, core, 1):
                for hanging_mass in compositions(n - core_mass, core, 0):
                    for hanging in product(*(forests(m) for m in hanging_mass)):
                        colors = [-1 if i % 2 == 0 else 1 for i in range(core)]
                        edges = [(i, (i + 1) % core, a) for i, a in enumerate(edge_sizes)]
                        children = [len(f) for f in hanging]

                        def attach(root, forest):
                            for size, subtree in forest:
                                child = len(colors)
                                colors.append(-colors[root])
                                children.append(len(subtree))
                                edges.append((root, child, size))
                                attach(child, subtree)

                        for i, forest in enumerate(hanging):
                            attach(i, forest)
                        degrees = [0] * len(colors)
                        incident = [0] * len(colors)
                        weight = Q(1, core)
                        for u, v, a in edges:
                            weight *= Q(a ** (2 * a + 1), factorial(a) ** 2)
                            for vertex in (u, v):
                                incident[vertex] += a
                                degrees[vertex] += 1
                        for size, degree, kids in zip(incident, degrees, children):
                            weight *= Q(size) ** (degree - 3) / factorial(kids)
                        cut = n + sum(colors)
                        weight *= factorial(cut) * factorial(2 * n - cut)
                        result[tuple(colors), tuple(edges), cut] += weight
    return dict(result)


def numeric_parser_audit(n):
    start = time.perf_counter()
    grammar = c1.CutGrammar(n)
    actual, info = execution_distribution(grammar.sample_code,
                                          lambda v: (tuple(v[0]), tuple(v[1]), v[2]))
    expected = independent_codes(n)
    normalizer = sum(expected.values())
    assert normalizer * factorial(n) == grammar.cut_count
    assert actual == {code: w / normalizer for code, w in expected.items()}
    parallel = sum(1 for _, edges, _ in actual if edges[1][1] == 0)
    maximum_children = 0
    maximum_depth = 0
    for colors, edges, _ in actual:
        core = next(i + 1 for i, (_, v, _) in enumerate(edges) if v == 0)
        kids = Counter(u for u, _, _ in edges[core:])
        maximum_children = max(maximum_children, max(kids.values(), default=0))
        depths = [0] * len(colors)
        for u, v, _ in edges[core:]:
            depths[v] = depths[u] + 1
        maximum_depth = max(maximum_depth, max(depths))
    denominator = factorial(3 * n) ** (12 * n + 4)
    fractions_checked = 0
    max_numerator_bits = max_denominator_bits = 0
    polynomials = []
    for color in (-1, 1):
        polynomials.extend(grammar.trees[color].values())
        polynomials.extend(grammar.forests[color].values())
        polynomials.extend(grammar.matrices[color].values())
    polynomials.extend(grammar.core.values())
    polynomials.extend(grammar.traces.values())
    # Include the open suffix matrix paths actually used by the parser.
    for length in range(2, n + 1, 2):
        suffix = {(a, a): {(0, 0): Q(1)} for a in range(1, n + 1)}
        for color in reversed([-1 if i % 2 == 0 else 1 for i in range(length)]):
            suffix = c1.matrix_mul(grammar.matrices[color], suffix, n)
            polynomials.extend(suffix.values())
    for poly in polynomials:
        for (mass, delta), coefficient in poly.items():
            assert 0 <= mass <= n and abs(delta) <= n + 1
            assert coefficient >= 0 and denominator % coefficient.denominator == 0
            fractions_checked += 1
            max_numerator_bits = max(max_numerator_bits, coefficient.numerator.bit_length())
            max_denominator_bits = max(max_denominator_bits, coefficient.denominator.bit_length())
    return dict(n=n, numeric_codes=len(actual), parallel_core_codes=parallel,
                max_child_count=maximum_children, max_hanging_depth=maximum_depth,
                cut_count=int(grammar.cut_count), parser_law="every numeric code exact",
                partial_coefficients_checked=fractions_checked,
                denominator_bound_verified=True, support_truncation_verified=True,
                max_numerator_bits=max_numerator_bits, max_denominator_bits=max_denominator_bits,
                seconds=time.perf_counter() - start, **info)


def labeled_macro_audit(n):
    """Fresh label/multiplicity check beyond the author's degree-four bound."""
    macro_weights = defaultdict(Q)
    code_list_representations = Counter()
    for (colors, edges, cut), weight in independent_codes(n).items():
        for order in permutations(range(n)):
            support = [set() for _ in colors]
            endpoint, cursor = list(range(n)), 0
            for u, v, size in edges:
                block = order[cursor:cursor + size]
                cursor += size
                for x, y in zip(block, block[1:] + block[:1]):
                    endpoint[x] = y
                support[u].update(block)
                support[v].update(block)
            left = tuple(sorted(tuple(sorted(b)) for c, b in zip(colors, support) if c == -1))
            right = tuple(sorted(tuple(sorted(b)) for c, b in zip(colors, support) if c == 1))
            key = (tuple(endpoint), left, right, cut)
            macro_weights[key] += weight
            code_list_representations[key] += 1

    def cycle_sizes(endpoint, block):
        unseen = set(block)
        sizes = []
        while unseen:
            x, size = min(unseen), 0
            while x in unseen:
                unseen.remove(x)
                size += 1
                x = endpoint[x]
            sizes.append(size)
        return sizes

    for (endpoint, left, right, cut), weight in macro_weights.items():
        expected = Q(factorial(cut) * factorial(2 * n - cut))
        for block in left + right:
            sizes = cycle_sizes(endpoint, block)
            expected *= Q(len(block)) ** (len(sizes) - 3)
            for a in sizes:
                expected *= Q(a ** (a + 1), factorial(a))
        assert weight == expected and weight.denominator == 1
    # Parallel core with three isomorphic numeric leaves, all cycles labeled
    # singletons: the two core directions and all 3! child orders must survive.
    witness = None
    if n == 5:
        key = (tuple(range(5)), ((0, 1, 2, 3, 4),), ((0, 1), (2,), (3,), (4,)), 8)
        assert code_list_representations[key] == 12
        assert macro_weights[key] == 1008000
        witness = dict(code_list_representations=12, expected="2 * 3!", macro_words=1008000)
    return dict(n=n, macros=len(macro_weights),
                ordered_code_label_lists=sum(code_list_representations.values()),
                all_macro_weights_exact=True, parallel_three_children=witness)


def literal_cut_pairs(n):
    """Independent literal words, no genus-one formula or outer grammar."""
    edges = list(combinations(range(n), 2))
    identity = tuple(range(n))
    result = set()
    word_count = 0
    for word in product(edges, repeat=2 * n):
        p = list(range(n))
        graph = [{i} for i in range(n)]
        for a, b in word:
            p[a], p[b] = p[b], p[a]
            ia, ib = next(i for i, z in enumerate(graph) if a in z), next(i for i, z in enumerate(graph) if b in z)
            if ia != ib:
                graph[ia] |= graph[ib]
                graph.pop(ib)
        if tuple(p) != identity or len(graph) != 1:
            continue
        word_count += 1
        for cut in range(1, 2 * n):
            # Use elementary per-component minimum length, with separately
            # reconstructed endpoint cycles and actual support blocks.
            valid = True
            for side in (word[:cut], word[cut:]):
                q = list(range(n))
                blocks = [{i} for i in range(n)]
                for a, b in side:
                    q[a], q[b] = q[b], q[a]
                    ia, ib = next(i for i, z in enumerate(blocks) if a in z), next(i for i, z in enumerate(blocks) if b in z)
                    if ia != ib:
                        blocks[ia] |= blocks[ib]
                        blocks.pop(ib)
                unseen = set(range(n))
                cycle_count = 0
                while unseen:
                    x = min(unseen)
                    cycle_count += 1
                    while x in unseen:
                        unseen.remove(x)
                        x = q[x]
                valid &= len(side) == n + cycle_count - 2 * len(blocks)
            if valid:
                result.add((word, cut))
    return result, word_count


def full_cut_audit(n):
    start = time.perf_counter()
    grammar = c1.CutGrammar(n)
    actual, info = execution_distribution(grammar.sample_cut, lambda v: (tuple(v[0]), v[1]))
    expected, word_count = literal_cut_pairs(n)
    assert set(actual) == expected
    assert set(actual.values()) == {Q(1, len(expected))}
    cuts_per_word = Counter(w for w, _ in expected)
    accepted = defaultdict(Q)
    for (word, _), probability in actual.items():
        ell = cuts_per_word[word]
        assert ell == len(c1.valid_cuts(word, n))
        accepted[word] += probability / ell
    acceptance = sum(accepted.values())
    assert len(accepted) == word_count
    assert set(w / acceptance for w in accepted.values()) == {Q(1, word_count)}
    return dict(n=n, cut_pairs=len(expected), words=word_count,
                each_cut_probability=str(Q(1, len(expected))),
                accepted_word_probability=str(Q(1, word_count)),
                exact_acceptance=str(acceptance), seconds=time.perf_counter() - start, **info)


def snapshot_audit():
    expected = json.loads((R2 / "freeze_manifest.json").read_text())["payload_sha256"]
    observed = {name: hashlib.sha256((R2 / name).read_bytes()).hexdigest() for name in expected}
    assert observed == expected
    for line in (R2 / "SHA256SUMS").read_text().splitlines():
        sha, name = line.split(maxsplit=1)
        assert hashlib.sha256((R2 / name).read_bytes()).hexdigest() == sha
    return observed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--numeric-max", type=int, default=5)
    parser.add_argument("--cut-max", type=int, default=3)
    parser.add_argument("--output", default="structural_parser_results.json")
    args = parser.parse_args()
    result = dict(snapshot=snapshot_audit(), python=platform.python_version(),
                  dependencies="standard library only", deterministic=True,
                  command=" ".join(__import__("sys").argv),
                  commit=subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
                  numeric=[], full_cut=[], labeled_macros=[])
    for n in range(2, args.numeric_max + 1):
        row = numeric_parser_audit(n)
        result["numeric"].append(row)
        Path(args.output).write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps(dict(stage="numeric", **row)), flush=True)
    for n in range(2, args.cut_max + 1):
        row = full_cut_audit(n)
        result["full_cut"].append(row)
        Path(args.output).write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps(dict(stage="full-cut", **row)), flush=True)
    for n in range(2, args.numeric_max + 1):
        row = labeled_macro_audit(n)
        result["labeled_macros"].append(row)
        Path(args.output).write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps(dict(stage="labeled-macro", **row)), flush=True)
    snapshot_audit()
    result["all_passed"] = True
    Path(args.output).write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
