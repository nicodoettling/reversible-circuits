"""Exact C1 genus-one cut sampler. Standard library; rightmost-first product.

Finite weighted grammar; intentionally simple polynomial implementation.
The independent finite harness lives in audit.py.
"""
from collections import defaultdict
from fractions import Fraction as Q
from math import factorial, gcd, lcm
from itertools import combinations
import random


def cycles(p):
    seen = set()
    out = []
    for a in range(len(p)):
        if a in seen:
            continue
        c, x = [], a
        while x not in seen:
            c.append(x)
            seen.add(x)
            x = p[x]
        out.append(tuple(c))
    return out


def right_transpose(p, t):
    q = list(p)
    a, b = t
    q[a], q[b] = q[b], q[a]
    return tuple(q)


def evaluate(word, n):
    p = tuple(range(n))
    for t in word:
        p = right_transpose(p, t)
    return p


def components(word, n):
    parent = list(range(n))
    def root(a):
        while a != parent[a]:
            a = parent[a]
        return a
    for a, b in word:
        a, b = root(a), root(b)
        parent[a] = b
    groups = defaultdict(list)
    for a in range(n):
        groups[root(a)].append(a)
    return tuple(sorted(tuple(v) for v in groups.values()))


def genus(word, n):
    return (len(word) - n - len(cycles(evaluate(word, n)))
            + 2 * len(components(word, n))) // 2


def valid_cuts(word, n):
    return [j for j in range(1, len(word))
            if genus(word[:j], n) == genus(word[j:], n) == 0]


def edge_weight(a):
    return Q(a ** (2 * a + 1), factorial(a) ** 2)


def profile_factor(parts):
    value = Q(1)
    for a in parts:
        value *= Q(a ** (a + 1), factorial(a))
    return value


def f0(parts):
    v, k = sum(parts), len(parts)
    value = factorial(v + k - 2) * Q(v) ** (k - 3) * profile_factor(parts)
    assert value.denominator == 1
    return value.numerator


def choose(items, rng):
    """Items are (value, nonnegative exact rational weight)."""
    items = [(v, Q(w)) for v, w in items if w]
    assert items and all(w > 0 for _, w in items)
    den = 1
    for _, w in items:
        den = lcm(den, w.denominator)
    ints = [(v, w.numerator * (den // w.denominator)) for v, w in items]
    point = rng.randrange(sum(w for _, w in ints))
    for v, w in ints:
        if point < w:
            return v
        point -= w
    raise AssertionError


def subset_table(lengths):
    tables = [{(0, 0): 1}]
    for a in lengths:
        nxt = defaultdict(int, tables[-1])
        for (s, k), count in tables[-1].items():
            nxt[s + a, k + 1] += count
        tables.append(dict(nxt))
    return tables


def sample_subset(lengths, tables, s, k, rng):
    chosen = []
    for i in range(len(lengths) - 1, -1, -1):
        a = lengths[i]
        take = choose([(False, tables[i].get((s, k), 0)),
                       (True, tables[i].get((s - a, k - 1), 0))], rng)
        if take:
            chosen.append(i)
            s, k = s - a, k - 1
    assert (s, k) == (0, 0)
    return chosen


def restrict(p, labels):
    labels = sorted(labels)
    index = {a: i for i, a in enumerate(labels)}
    return tuple(index[p[a]] for a in labels), labels


def lift_word(word, labels):
    return [tuple(sorted((labels[a], labels[b]))) for a, b in word]


def interleave(words, rng):
    positions = [(i, j) for i, w in enumerate(words) for j in range(len(w))]
    colors = [i for i, _ in positions]
    rng.shuffle(colors)
    cursors = [0] * len(words)
    out = []
    for i in colors:
        out.append(words[i][cursors[i]])
        cursors[i] += 1
    return out


def genus_zero_branches(p):
    n = len(p)
    cs = cycles(p)
    k = len(cs)
    r = n + k - 2
    cycle_of = {a: i for i, c in enumerate(cs) for a in c}
    out = []
    for t in combinations(range(n), 2):
        q = right_transpose(p, t)
        qs = cycles(q)
        if cycle_of[t[0]] != cycle_of[t[1]]:
            out.append(((t, q, None), Q(f0([len(c) for c in qs]))))
            continue
        a0 = next(c for c in qs if t[0] in c)
        b0 = next(c for c in qs if t[1] in c)
        rest = [c for c in qs if c != a0 and c != b0]
        tables = subset_table([len(c) for c in rest])
        factor = factorial(r - 1) * profile_factor([len(c) for c in qs])
        cells = []
        for (s, h), count in tables[-1].items():
            va, ka = len(a0) + s, 1 + h
            vb, kb = n - va, k + 1 - ka
            weight = factor * Q(va) ** (ka - 3) * Q(vb) ** (kb - 3)
            assert weight.denominator == 1
            cells.append(((s, h), count * weight))
        info = (a0, b0, rest, tables, cells)
        out.append(((t, q, info), sum(w for _, w in cells)))
    assert sum(w for _, w in out) == f0([len(c) for c in cs])
    return out


def sample_genus_zero(p, rng):
    tasks, values = [('sample', p)], []
    while tasks:
        task = tasks.pop()
        if task[0] == 'append':
            values[-1].append(task[1])
            continue
        if task[0] == 'join':
            _, t, la, lb = task
            wb, wa = values.pop(), values.pop()
            values.append(interleave([lift_word(wa, la), lift_word(wb, lb)], rng) + [t])
            continue
        p = task[1]
        if len(p) == 1:
            values.append([])
            continue
        t, q, info = choose(genus_zero_branches(p), rng)
        if info is None:
            tasks.extend([('append', t), ('sample', q)])
            continue
        a0, b0, rest, tables, cells = info
        s, h = choose(cells, rng)
        selected = sample_subset([len(c) for c in rest], tables, s, h, rng)
        aset = set(a0)
        for i in selected:
            aset.update(rest[i])
        bset = set(range(len(p))) - aset
        pa, la = restrict(q, aset)
        pb, lb = restrict(q, bset)
        tasks.extend([('join', t, la, lb), ('sample', pb), ('sample', pa)])
    assert len(values) == 1
    return values[0]


def poly_add(target, source, factor=1):
    for key, val in source.items():
        target[key] += factor * val


def poly_mul(left, right, cap):
    out = defaultdict(Q)
    for (a, x), u in left.items():
        for (b, y), v in right.items():
            if a + b <= cap:
                out[a + b, x + y] += u * v
    return dict(out)


def poly_shift(poly, mass=0, delta=0, factor=1, cap=None):
    return {(m + mass, d + delta): factor * v for (m, d), v in poly.items()
            if cap is None or m + mass <= cap}


def forest_table(trees, n):
    """F[(k,S)] stores polynomials in (mass, color imbalance)."""
    branch = {}
    for a in range(1, n + 1):
        branch[a] = poly_shift(trees[a], a, 0, edge_weight(a), n)
    forests = {(0, 0): {(0, 0): Q(1)}}
    for k in range(1, n + 1):
        for s in range(k, n + 1):
            value = defaultdict(Q)
            for a in range(1, s - k + 2):
                previous = forests.get((k - 1, s - a))
                if previous:
                    poly_add(value, poly_mul(previous, branch[a], n))
            if value:
                forests[k, s] = dict(value)
    return forests


def planted_from_forest(forests, color, a):
    out = defaultdict(Q)
    for (k, s), poly in forests.items():
        factor = Q(a + s) ** (k - 2) / factorial(k)
        poly_add(out, poly_shift(poly, delta=color), factor)
    return dict(out)


def matrix_mul(left, right, n):
    out = {}
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            value = defaultdict(Q)
            for c in range(1, n + 1):
                if (a, c) in left and (c, b) in right:
                    poly_add(value, poly_mul(left[a, c], right[c, b], n))
            if value:
                out[a, b] = dict(value)
    return out


class CutGrammar:
    def __init__(self, n):
        assert n >= 2
        self.n = n
        trees = {c: {a: {(0, c): Q(1, a * a)} for a in range(1, n + 1)}
                 for c in (-1, 1)}
        # A mass-n planted tree has at most n child edges on every path.
        # Positive edge size makes n fixed-point rounds exact at degree <=n.
        for _ in range(n):
            forests = {c: forest_table(trees[-c], n) for c in (-1, 1)}
            trees = {c: {a: planted_from_forest(forests[c], c, a)
                         for a in range(1, n + 1)} for c in (-1, 1)}
        self.trees = trees
        self.forests = {c: forest_table(trees[-c], n) for c in (-1, 1)}
        self.core = {}
        self.matrices = {}
        for c in (-1, 1):
            mat = {}
            for a in range(1, n + 1):
                for b in range(1, n + 1):
                    value = defaultdict(Q)
                    for (k, s), poly in self.forests[c].items():
                        factor = Q(a + b + s) ** (k - 1) / factorial(k)
                        poly_add(value, poly_shift(poly, delta=c), factor)
                    self.core[c, a, b] = dict(value)
                    shifted = poly_shift(value, b, 0, edge_weight(b), n)
                    if shifted:
                        mat[a, b] = shifted
            self.matrices[c] = mat
        pair = matrix_mul(self.matrices[-1], self.matrices[1], n)
        power = pair
        self.traces = {}
        self.top = []
        for s in range(1, n // 2 + 1):
            trace = defaultdict(Q)
            for a in range(1, n + 1):
                poly_add(trace, power.get((a, a), {}))
            self.traces[s] = dict(trace)
            for (mass, delta), value in trace.items():
                if mass == n:
                    j = n + delta
                    assert 1 <= j <= 2 * n - 1
                    self.top.append(((s, delta), value * factorial(j)
                                     * factorial(2 * n - j) / (2 * s)))
            if s < n // 2:
                power = matrix_mul(power, pair, n)
        self.cut_count = sum(w for _, w in self.top) * factorial(n)
        assert self.cut_count.denominator == 1

    def _sample_core(self, c, a, b, mass, delta, rng, vertices, edges, root):
        tasks = [('vertex', c, a + b, 1, mass, delta, root)]
        while tasks:
            task = tasks.pop()
            if task[0] == 'vertex':
                _, c, incoming, offset, mass, delta, root = task
                choices = []
                for (k, s), poly in self.forests[c].items():
                    val = poly.get((mass, delta - c), 0)
                    if val:
                        weight = val * Q(incoming + s) ** (k - 2 + offset) / factorial(k)
                        choices.append(((k, s), weight))
                k, s = choose(choices, rng)
                tasks.append(('forest', c, k, s, mass, delta - c, root))
                continue
            _, c, k, s, mass, delta, root = task
            if k == 0:
                assert (s, mass, delta) == (0, 0, 0)
                continue
            choices = []
            for a in range(1, s - k + 2):
                remaining = self.forests[c].get((k - 1, s - a), {})
                for (tm, td), tv in self.trees[-c][a].items():
                    rem = remaining.get((mass - a - tm, delta - td), 0)
                    if rem:
                        choices.append(((a, tm, td), edge_weight(a) * tv * rem))
            a, tm, td = choose(choices, rng)
            child = len(vertices)
            vertices.append(-c)
            edges.append((root, child, a))
            tasks.extend([('forest', c, k - 1, s - a, mass - a - tm, delta - td, root),
                          ('vertex', -c, a, 0, tm, td, child)])

    def sample_code(self, rng):
        n = self.n
        s, delta = choose(self.top, rng)
        length = 2 * s
        colors = [-1 if i % 2 == 0 else 1 for i in range(length)]
        # Suffix matrices indexed by the current incoming edge size and final
        # size. A diagonal identity closes the alternating core.
        suffix = [{(a, a): {(0, 0): Q(1)} for a in range(1, n + 1)}]
        for c in reversed(colors):
            suffix.append(matrix_mul(self.matrices[c], suffix[-1], n))
        suffix.reverse()
        a0 = choose([(a, suffix[0].get((a, a), {}).get((n, delta), 0))
                     for a in range(1, n + 1)], rng)
        a, mass, imbalance = a0, n, delta
        vertices, edges, core_data = list(colors), [], []
        for i, c in enumerate(colors):
            choices = []
            for b in range(1, n + 1):
                rem = suffix[i + 1].get((b, a0), {})
                for (cm, cd), cv in self.core[c, a, b].items():
                    rv = rem.get((mass - b - cm, imbalance - cd), 0)
                    if rv:
                        choices.append(((b, cm, cd), edge_weight(b) * cv * rv))
            b, cm, cd = choose(choices, rng)
            edges.append((i, (i + 1) % length, b))
            core_data.append((c, a, b, cm, cd))
            a, mass, imbalance = b, mass - b - cm, imbalance - cd
        assert (a, mass, imbalance) == (a0, 0, 0)
        for i, data in enumerate(core_data):
            self._sample_core(*data, rng, vertices, edges, i)
        assert sum(e[2] for e in edges) == n
        assert len(vertices) == len(edges)
        return vertices, edges, n + delta

    def sample_cut(self, rng):
        vertices, edges, j = self.sample_code(rng)
        labels = list(range(self.n))
        rng.shuffle(labels)
        p = list(range(self.n))
        vertex_sets = [set() for _ in vertices]
        cursor = 0
        for u, v, a in edges:
            block = labels[cursor:cursor + a]
            cursor += a
            for x, y in zip(block, block[1:] + block[:1]):
                p[x] = y
            vertex_sets[u].update(block)
            vertex_sets[v].update(block)
        inverse = [0] * self.n
        for x, y in enumerate(p):
            inverse[y] = x
        sides = {-1: [], 1: []}
        for c, support in zip(vertices, vertex_sets):
            q, lift = restrict(p if c == -1 else inverse, support)
            sides[c].append(lift_word(sample_genus_zero(q, rng), lift))
        left = interleave(sides[-1], rng)
        right = interleave(sides[1], rng)
        assert len(left) == j and len(right) == 2 * self.n - j
        word = left + right
        assert evaluate(word, self.n) == tuple(range(self.n))
        assert len(components(word, self.n)) == 1
        assert j in valid_cuts(word, self.n)
        return word, j

    def sample(self, rng):
        tries = 0
        while True:
            tries += 1
            word, _ = self.sample_cut(rng)
            if rng.randrange(len(valid_cuts(word, self.n))) == 0:
                return word, tries


def sample_connected_genus_one(n, rng=None):
    """Return an exact connected genus-one word under an ideal random-bit RNG.

    The default uses SystemRandom. Pass random.Random(seed) only for reproducible
    diagnostics; a seeded pseudorandom stream is not the theorem's probability law.
    """
    if not isinstance(n, int) or n < 2:
        raise ValueError('n must be an integer at least 2')
    if n == 2:
        return [(0, 1)] * 4
    return CutGrammar(n).sample(rng or random.SystemRandom())[0]
