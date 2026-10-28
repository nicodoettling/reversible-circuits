"""C2.v1 author prototype: exact genus-two identity cut grammar.

Rightmost-first composition, standard library only. Exact law interprets rng
as independent unbiased bits; seeded PRNGs are diagnostics only. No execution
occurs on import. All polynomial tables are truncated by mass and genus totals.
"""
from collections import defaultdict
from fractions import Fraction as Q
from math import factorial, lcm
from pathlib import Path
import importlib.util
import random

REPO = Path(__file__).resolve().parents[5]
_old_path = REPO / 'experiments/20260907-genus-one-sampler/roles/r1-recursive/sampler.py'
_spec = importlib.util.spec_from_file_location('c2_g01_dependency', _old_path)
g01 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(g01)
ZERO = (0, 0, 0, 0)


def choose(items, rng):
    items = [(value, Q(weight)) for value, weight in items if weight]
    assert items and all(weight > 0 for _, weight in items)
    den = 1
    for _, weight in items:
        den = lcm(den, weight.denominator)
    integers = [(value, weight.numerator * (den // weight.denominator))
                for value, weight in items]
    z = rng.randrange(sum(weight for _, weight in integers))
    for value, weight in integers:
        if z < weight:
            return value
        z -= weight
    raise AssertionError('categorical draw failed')


def edge_weight(a):
    return Q(a ** (2 * a + 1), factorial(a) ** 2)


def plus(a, b):
    return tuple(x + y for x, y in zip(a, b))


def minus(a, b):
    return tuple(x - y for x, y in zip(a, b))


def admissible(index, n):
    return 0 <= index[0] <= n and 0 <= index[2] <= 1 and 0 <= index[3] <= 1


def vertex_index(c, h):
    return (0, c, h if c == -1 else 0, h if c == 1 else 0)


def poly_mul(left, right, n):
    out = defaultdict(Q)
    for ix, x in left.items():
        for iy, y in right.items():
            iz = plus(ix, iy)
            if admissible(iz, n):
                out[iz] += x * y
    return dict(out)


def matrix_mul(left, right, n):
    out = {}
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            total = defaultdict(Q)
            for c in range(1, n + 1):
                for ix, value in poly_mul(left.get((a, c), {}), right.get((c, b), {}), n).items():
                    total[ix] += value
            if total:
                out[a, b] = dict(total)
    return out


# A moment record is [F,Q,E_0..E_k,W_0..W_k]. E_j is weighted e_j of
# immediate edge sizes; W_j weights e_j's subset by the sum of selected sizes.
def initial_moments():
    return [Q(1), Q(0), [Q(1)], [Q(0)]]


def append_moments(moment, a, multiplier):
    f, q, e, w = moment
    length = len(e) + 1
    ne, nw = [Q(0)] * length, [Q(0)] * length
    for j in range(length):
        ne[j] = (e[j] if j < len(e) else 0) + (a * e[j - 1] if j else 0)
        nw[j] = ((w[j] if j < len(w) else 0)
                 + (a * w[j - 1] + a * a * e[j - 1] if j else 0))
    return [f * multiplier, (q + a * (a - 1) * f) * multiplier,
            [x * multiplier for x in ne], [x * multiplier for x in nw]]


def add_moments(target, source):
    target[0] += source[0]
    target[1] += source[1]
    for i in range(len(source[2])):
        target[2][i] += source[2][i]
        target[3][i] += source[3][i]


def forest_table(trees, n):
    out = {(0, 0): {ZERO: initial_moments()}}
    for k in range(1, n + 1):
        for s in range(k, n + 1):
            layer = {}
            for a in range(1, s - k + 2):
                for prev_index, moment in out.get((k - 1, s - a), {}).items():
                    for tree_index, value in trees[a].items():
                        index = plus(plus(prev_index, tree_index), (a, 0, 0, 0))
                        if not admissible(index, n):
                            continue
                        incoming = append_moments(moment, a, edge_weight(a) * value)
                        if index not in layer:
                            layer[index] = [Q(0), Q(0), [Q(0)] * (k + 1), [Q(0)] * (k + 1)]
                        add_moments(layer[index], incoming)
            if layer:
                out[k, s] = layer
    return out


def local_mass(moment, ports, k, s, h):
    """Exact sum of forest weight times H_h(ports + child edge sizes).

    ports may include already sampled child sizes. No child factorial here.
    This is a polynomial conditional-mass oracle, not a sampled approximation.
    """
    if moment is None:
        return Q(0)
    size, degree = sum(ports) + s, len(ports) + k
    if not size:
        return Q(0)
    f = moment[0]
    if h == 0:
        return f * Q(size) ** (degree - 3)
    current = moment
    for a in ports:
        current = append_moments(current, a, Q(1))
    value = Q(size) ** (degree - 2) * current[1]
    for j in range(2, degree + 1):
        value += factorial(j - 1) * Q(size) ** (degree - 1 - j) * current[3][j]
    return value / 24


def vertex_table(forests, c, ports, n, forced_h=None):
    out = defaultdict(Q)
    for (k, s), layer in forests.items():
        for index, moment in layer.items():
            for h in ((0, 1) if forced_h is None else (forced_h,)):
                ix = plus(index, vertex_index(c, h))
                if admissible(ix, n):
                    value = local_mass(moment, ports, k, s, h) / factorial(k)
                    if value:
                        out[ix] += value
    return dict(out)


class CutGrammar:
    def __init__(self, n):
        if not isinstance(n, int) or n < 2:
            raise ValueError('n must be an integer at least 2')
        self.n = n
        empty = {(0, 0): {ZERO: initial_moments()}}
        trees = {c: {a: vertex_table(empty, c, [a], n) for a in range(1, n + 1)}
                 for c in (-1, 1)}
        for _ in range(n):
            forests = {c: forest_table(trees[-c], n) for c in (-1, 1)}
            trees = {c: {a: vertex_table(forests[c], c, [a], n) for a in range(1, n + 1)}
                     for c in (-1, 1)}
        self.trees = trees
        self.forests = {c: forest_table(trees[-c], n) for c in (-1, 1)}
        self.root = vertex_table(self.forests[-1], -1, [], n, forced_h=1)
        self.core, self.matrices = {}, {}
        for c in (-1, 1):
            matrix = {}
            for a in range(1, n + 1):
                for b in range(1, n + 1):
                    value = vertex_table(self.forests[c], c, [a, b], n)
                    self.core[c, a, b] = value
                    shifted = {plus(ix, (b, 0, 0, 0)): edge_weight(b) * x
                               for ix, x in value.items() if ix[0] + b <= n}
                    if shifted:
                        matrix[a, b] = shifted
            self.matrices[c] = matrix
        self.top = []
        for index, value in self.root.items():
            mass, delta, gl, gr = index
            if (mass, gl, gr) == (n, 1, 1):
                j = n + delta + 1
                if 1 <= j < 2 * n + 2:
                    self.top.append((('tree', 0, index), value * factorial(j) * factorial(2 * n + 2 - j)))
        pair = matrix_mul(self.matrices[-1], self.matrices[1], n)
        power = pair
        self.traces = {}
        for s in range(1, n // 2 + 1):
            trace = defaultdict(Q)
            for a in range(1, n + 1):
                for index, value in power.get((a, a), {}).items():
                    trace[index] += value
            self.traces[s] = dict(trace)
            for index, value in trace.items():
                mass, delta, gl, gr = index
                if (mass, gl, gr) == (n, 1, 0):
                    j = n + delta + 2
                    if 1 <= j < 2 * n + 2:
                        self.top.append((('cycle', s, index), value * factorial(j) * factorial(2 * n + 2 - j) / (2 * s)))
            if s < n // 2:
                power = matrix_mul(power, pair, n)
        self.cut_count = factorial(n) * sum(value for _, value in self.top)
        assert self.cut_count.denominator == 1

    def _sample_vertices(self, tasks, rng):
        # task=(node,color,external ports,index,forced genus or None).
        while tasks:
            node, c, ports, index, forced_h = tasks.pop()
            options = []
            for h in ((0, 1) if forced_h is None else (forced_h,)):
                ix = minus(index, vertex_index(c, h))
                for (k, s), layer in self.forests[c].items():
                    value = local_mass(layer.get(ix), ports, k, s, h) / factorial(k)
                    if value:
                        options.append(((h, k, s, ix), value))
            h, k, s, remaining = choose(options, rng)
            node.update(color=c, genus=h, children=[])
            fixed = list(ports)
            child_tasks = []
            while k:
                options = []
                for a in range(1, s - k + 2):
                    residual = self.forests[c].get((k - 1, s - a), {})
                    for tree_index, value in self.trees[-c][a].items():
                        rem_index = minus(minus(remaining, tree_index), (a, 0, 0, 0))
                        mass = local_mass(residual.get(rem_index), fixed + [a], k - 1, s - a, h)
                        if mass:
                            options.append(((a, tree_index, rem_index), edge_weight(a) * value * mass))
                a, tree_index, remaining = choose(options, rng)
                child = {}
                node['children'].append((a, child))
                child_tasks.append((child, -c, [a], tree_index, None))
                fixed.append(a)
                k, s = k - 1, s - a
            assert remaining == ZERO and s == 0
            tasks.extend(reversed(child_tasks))

    def sample_code(self, rng):
        kind, s, index = choose(self.top, rng)
        n = self.n
        if kind == 'tree':
            node = {}
            self._sample_vertices([(node, -1, [], index, 1)], rng)
            return {'kind': 'tree', 'root': node, 'cut': n + index[1] + 1}
        length = 2 * s
        colors = [-1 if i % 2 == 0 else 1 for i in range(length)]
        suffix = [{(a, a): {ZERO: Q(1)} for a in range(1, n + 1)}]
        for c in reversed(colors):
            suffix.append(matrix_mul(self.matrices[c], suffix[-1], n))
        suffix.reverse()
        a0 = choose([(a, suffix[0].get((a, a), {}).get(index, 0)) for a in range(1, n + 1)], rng)
        a, remaining = a0, index
        nodes = [{} for _ in colors]
        sizes, tasks = [], []
        for i, c in enumerate(colors):
            options = []
            for b in range(1, n + 1):
                tail = suffix[i + 1].get((b, a0), {})
                for core_index, value in self.core[c, a, b].items():
                    rem = minus(minus(remaining, core_index), (b, 0, 0, 0))
                    weight = tail.get(rem, 0) * edge_weight(b) * value
                    if weight:
                        options.append(((b, core_index, rem), weight))
            b, core_index, remaining = choose(options, rng)
            sizes.append(b)
            tasks.append((nodes[i], c, [a, b], core_index, None))
            a = b
        assert a == a0 and remaining == ZERO
        self._sample_vertices(list(reversed(tasks)), rng)
        return {'kind': 'cycle', 'nodes': nodes, 'sizes': sizes, 'cut': n + index[1] + 2}

    def sample_cut(self, rng):
        code = self.sample_code(rng)
        vertices, edges = flatten_code(code)
        labels = list(range(self.n))
        rng.shuffle(labels)
        endpoint = list(range(self.n))
        supports = [set() for _ in vertices]
        cursor = 0
        for u, v, a in edges:
            block = labels[cursor:cursor + a]
            cursor += a
            for x, y in zip(block, block[1:] + block[:1]):
                endpoint[x] = y
            supports[u].update(block)
            supports[v].update(block)
        assert cursor == self.n
        inverse = [0] * self.n
        for x, y in enumerate(endpoint):
            inverse[y] = x
        sides = {-1: [], 1: []}
        for (color, genus), support in zip(vertices, supports):
            labels_local = sorted(support)
            reverse_labels = {a: i for i, a in enumerate(labels_local)}
            permutation = endpoint if color == -1 else inverse
            local_endpoint = tuple(reverse_labels[permutation[a]] for a in labels_local)
            local_word = g01.sample(local_endpoint, genus, rng)
            sides[color].append([tuple(sorted((labels_local[a], labels_local[b]))) for a, b in local_word])
        left, right = interleave(sides[-1], rng), interleave(sides[1], rng)
        word = left + right
        assert len(left) == code['cut'] and len(word) == 2 * self.n + 2
        assert g01.evaluate(self.n, word) == tuple(range(self.n))
        assert len(g01.components(self.n, word)) == 1
        assert code['cut'] in valid_cuts(word, self.n)
        return word, code['cut']

    def sample(self, rng):
        attempts = 0
        while True:
            attempts += 1
            word, _ = self.sample_cut(rng)
            if rng.randrange(len(valid_cuts(word, self.n))) == 0:
                return word, attempts


def flatten_code(code):
    if code['kind'] == 'tree':
        nodes = [code['root']]
        edges = []
    else:
        nodes = list(code['nodes'])
        edges = [(i, (i + 1) % len(nodes), a) for i, a in enumerate(code['sizes'])]
    stack = list(reversed([(i, node) for i, node in enumerate(nodes)]))
    while stack:
        root, node = stack.pop()
        children = []
        for a, child in node['children']:
            index = len(nodes)
            nodes.append(child)
            edges.append((root, index, a))
            children.append((index, child))
        stack.extend(reversed(children))
    return [(node['color'], node['genus']) for node in nodes], edges


def interleave(words, rng):
    colors = [i for i, word in enumerate(words) for _ in word]
    rng.shuffle(colors)
    offsets = [0] * len(words)
    out = []
    for color in colors:
        out.append(words[color][offsets[color]])
        offsets[color] += 1
    return out


def genus(word, n):
    return (len(word) - n - len(g01.cycles(g01.evaluate(n, word)))
            + 2 * len(g01.components(n, word))) // 2


def valid_cuts(word, n):
    return [j for j in range(1, len(word))
            if genus(word[:j], n) == 1 and genus(word[j:], n) <= 1]


def sample_connected_genus_two(n, rng=None):
    return CutGrammar(n).sample(rng or random.SystemRandom())[0]
