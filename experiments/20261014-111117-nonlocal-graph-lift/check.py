"""Exact deterministic checks; standard library only."""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import json
import platform
import subprocess

HERE = Path(__file__).resolve().parent


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def perm(edge, n):
    p = list(range(n))
    a, b = edge
    p[a], p[b] = b, a
    return tuple(p)


def evaluate(word, n):
    p = tuple(range(n))
    for edge in word:
        p = compose(p, perm(edge, n))
    return p


def conj(edge, by):
    a, b = by
    return tuple(sorted(b if x == a else a if x == b else x for x in edge))


def hurwitz(w, i, sign):
    w = list(w)
    a, b = w[i:i+2]
    w[i:i+2] = (b, conj(a, b)) if sign == 1 else (conj(b, a), a)
    return tuple(w)


def macro(w, i, j, kind, arg):
    a, b = w[i], w[j]
    middle = w[i+1:j]
    if kind == 'H' and arg == 1:
        new = (b,) + tuple(conj(conj(x, a), b) for x in middle) + (conj(a, b),)
    elif kind == 'H':
        new = (conj(b, a),) + tuple(conj(conj(x, b), a) for x in middle) + (a,)
    elif a == b:
        new = (arg,) + tuple(conj(conj(x, a), arg) for x in middle) + (arg,)
    else:
        return w
    return w[:i] + new + w[j+1:]


def lifted_path(w, i, j, kind, arg):
    states = [w]
    for k in range(i, j-1):
        states.append(hurwitz(states[-1], k, -1))
    if kind == 'H':
        states.append(hurwitz(states[-1], j-1, arg))
    else:
        v = states[-1]
        states.append(v[:j-1] + (arg, arg) + v[j+1:] if v[j-1] == v[j] else v)
    for k in range(j-2, i-1, -1):
        states.append(hurwitz(states[-1], k, 1))
    return states


def reflection_length(g):
    seen = set()
    cycles = 0
    for v in range(len(g)):
        if v not in seen:
            cycles += 1
            while v not in seen:
                seen.add(v)
                v = g[v]
    return len(g) - cycles


def canonical(g):
    n = len(g)
    if n < 2:
        return ()
    v = n-1
    if g[v] == v:
        return canonical(g[:v])
    a = g.index(v)
    e = tuple(sorted((a, v)))
    h = compose(g, perm(e, n))
    assert h[v] == v
    return canonical(h[:v]) + (e,)


def normalize(word, n):
    w = word
    moves = 0

    def step(i, sign):
        nonlocal w, moves
        w = hurwitz(w, i, sign)
        moves += 1

    def sweep(end):
        """Normalize if reduced; otherwise expose a square and return its slot."""
        for v in range(n-1, 0, -1):
            i = next((i for i in range(end) if v in w[i]), None)
            if i is None:
                continue
            while i < end-1:
                if v not in w[i+1]:
                    step(i, 1)
                elif w[i] == w[i+1]:
                    return i
                else:
                    step(i, -1)
                    assert v not in w[i]
                i += 1
            end -= 1
        return None

    g = evaluate(w, n)
    ell = reflection_length(g)
    end = len(w)
    while end > ell:
        i = sweep(end)
        assert i is not None, (word, g, end)
        while i < end-2:
            step(i+1, 1)
            step(i, 1)
            i += 1
        assert w[end-2] == w[end-1]
        w = w[:end-2] + ((0, 1), (0, 1)) + w[end:]
        moves += 1
        end -= 2
    assert sweep(end) is None
    expected = canonical(g) + ((0, 1),) * (len(word)-ell)
    assert w == expected, (word, w, expected)
    assert evaluate(w, n) == g
    if len(word) >= 2:
        assert moves <= (n+3)*len(word)**2
    return moves


def normalization_checks(n, m):
    gates = list(combinations(range(n), 2))
    count = maximum = 0
    for w in product(gates, repeat=m):
        maximum = max(maximum, normalize(w, n))
        count += 1
    return dict(N=n, m=m, words=count, max_moves_to_normal_form=maximum)


def kernel_checks(n, m, identity_only=False):
    gates = list(combinations(range(n), 2))
    identity = tuple(range(n))
    words = [w for w in product(gates, repeat=m)
             if not identity_only or evaluate(w, n) == identity]
    rows = {}
    endpoints = {}
    channels = 0
    denominator = 8 * (m*(m-1)//2) * len(gates)
    for w in words:
        g = evaluate(w, n)
        endpoints[w] = g
        row = Counter({w: denominator//2})
        for i, j in combinations(range(m), 2):
            for kind, args, weight in [('H', (1, -1), len(gates)), ('R', gates, 2)]:
                for arg in args:
                    z = macro(w, i, j, kind, arg)
                    path = lifted_path(w, i, j, kind, arg)
                    assert path[-1] == z
                    assert len(path)-1 <= 2*m-3
                    assert evaluate(z, n) == g
                    assert all(evaluate(v, n) == g for v in path)
                    if kind == 'H':
                        assert macro(z, i, j, kind, -arg) == w
                    elif w[i] == w[j]:
                        assert macro(z, i, j, kind, w[i]) == w
                    row[z] += weight
                    channels += 1
        assert sum(row.values()) == denominator
        rows[w] = row
    for w, row in rows.items():
        for z, weight in row.items():
            assert rows[z][w] == weight
    unseen = set(words)
    component_counts = Counter()
    component_sizes = []
    while unseen:
        root = next(iter(unseen))
        unseen.remove(root)
        stack = [root]
        size = 0
        while stack:
            w = stack.pop()
            size += 1
            for z in rows[w]:
                if z in unseen:
                    unseen.remove(z)
                    stack.append(z)
        component_counts[endpoints[root]] += 1
        component_sizes.append(size)
    assert all(c == 1 for c in component_counts.values())
    return dict(N=n, m=m, identity_only=identity_only, states=len(words),
                endpoint_fibers=len(component_counts), components=len(component_sizes),
                component_sizes=sorted(component_sizes), checked_channels=channels,
                endpoint_and_path_preservation=True, integer_detailed_balance=True,
                all_uniform_observables_stationary=True)


def obstruction_checks():
    a, b = (0, 1), (2, 3)
    assert evaluate((a, b), 4) == evaluate((b, a), 4)
    assert len(set(a) & set(b)) == 0
    a, middle, s = (0, 1), (1, 2), (0, 2)
    assert evaluate((a, middle, a), 3) != evaluate((s, middle, s), 3)
    return dict(incident_only_frozen_two_disjoint_gates=True,
                naive_nonadjacent_square_replacement_fails=True)


def main():
    result = dict(python=platform.python_version(), dependencies='standard library only',
                  commit=subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
                  command='python3 -B ' + str(HERE.relative_to(Path.cwd()) / 'check.py'),
                  seeds='none: exhaustive deterministic enumeration')
    result['normal_forms'] = [normalization_checks(n, m)
                            for n in (2, 3, 4) for m in range(7)]
    result['normal_forms'].append(normalization_checks(5, 4))
    print('normal forms checked', flush=True)
    result['kernels'] = []
    for n, m, id_only in [(3, 4, False), (4, 4, False), (4, 6, True)]:
        result['kernels'].append(kernel_checks(n, m, id_only))
        print('kernel checked', n, m, id_only, flush=True)
    result['obstructions'] = obstruction_checks()
    result['status'] = 'all exact checks passed; no asymptotic inference from enumeration'
    (HERE / 'results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(result['status'])


if __name__ == '__main__':
    main()
