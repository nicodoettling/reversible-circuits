#!/usr/bin/env python3
"""Exact codec and kernel checks for one-cycle factorizations; no spectra."""
from collections import Counter
from itertools import combinations, product
from fractions import Fraction
from pathlib import Path
import hashlib
import importlib.util
import json
import platform
import subprocess


def edge(a, b):
    assert a != b
    return tuple(sorted((a, b)))


def evaluate(n, word):
    p = list(range(n))
    for a, b in word:
        p[a], p[b] = p[b], p[a]  # right multiplication, rightmost-first action
    return tuple(p)


def target(n):
    return tuple((i + 1) % n for i in range(n))


def parents(n, tree):
    neighbors = [set() for _ in range(n)]
    for a, b in tree:
        neighbors[a].add(b)
        neighbors[b].add(a)
    parent = [-1] * n
    parent[0] = 0
    todo = [0]
    while todo:
        a = todo.pop()
        for b in neighbors[a]:
            if parent[b] == -1:
                parent[b] = a
                todo.append(b)
    assert all(p >= 0 for p in parent)
    return parent


def word_to_tree(n, word):
    assert len(set(word)) == n - 1
    par = parents(n, word)
    times = {e: i + 1 for i, e in enumerate(word)}
    relabel = [0] + [times[edge(v, par[v])] for v in range(1, n)]
    assert sorted(relabel) == list(range(n))
    return tuple(sorted(edge(relabel[a], relabel[b]) for a, b in word))


def tree_to_word(n, tree):
    par = parents(n, tree)
    timed = tuple(edge(par[i], i) for i in range(1, n))
    h = evaluate(n, timed)
    relabel = [-1] * n
    v = 0
    for j in range(n):
        assert relabel[v] == -1
        relabel[v] = j
        v = h[v]
    assert v == 0
    return tuple(edge(relabel[a], relabel[b]) for a, b in timed)


def tree_to_code(n, tree):
    adj = [set() for _ in range(n)]
    for a, b in tree:
        adj[a].add(b)
        adj[b].add(a)
    out = []
    for _ in range(n - 2):
        leaf = next(i for i in range(n) if len(adj[i]) == 1)
        neighbor = next(iter(adj[leaf]))
        out.append(neighbor)
        adj[leaf].remove(neighbor)
        adj[neighbor].remove(leaf)
    return tuple(out)


def code_to_tree(n, code):
    degree = [1] * n
    for x in code:
        degree[x] += 1
    tree = []
    for x in code:
        leaf = next(i for i in range(n) if degree[i] == 1)
        tree.append(edge(leaf, x))
        degree[leaf] -= 1
        degree[x] -= 1
    last = [i for i in range(n) if degree[i] == 1]
    assert len(last) == 2
    tree.append(edge(*last))
    return tuple(sorted(tree))


def hurwitz(word, i, sign):
    a, b = word[i:i + 2]
    def conjugate(e, t):
        def act(x):
            return t[1] if x == t[0] else t[0] if x == t[1] else x
        return edge(*(act(x) for x in e))
    pair = (b, conjugate(a, b)) if sign == 1 else (conjugate(b, a), a)
    return word[:i] + pair + word[i + 2:]


def brute_words(n):
    gates = tuple(combinations(range(n), 2))
    found = set()
    for prefix in product(gates, repeat=n - 2):
        p = evaluate(n, prefix)
        inv = [0] * n
        for i, x in enumerate(p):
            inv[x] = i
        last = tuple(inv[x] for x in target(n))
        changed = [i for i, x in enumerate(last) if i != x]
        if len(changed) == 2:
            a, b = changed
            if last[a] == b and last[b] == a:
                found.add(prefix + ((a, b),))
    return found


def cycle_type(p):
    seen, lengths = set(), []
    for i in range(len(p)):
        if i not in seen:
            v, length = i, 0
            while v not in seen:
                seen.add(v)
                length += 1
                v = p[v]
            lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def check_n(n):
    codes = tuple(product(range(n), repeat=n - 2))
    encoded = {}
    for code in codes:
        tree = code_to_tree(n, code)
        assert tree_to_code(n, tree) == code
        word = tree_to_word(n, tree)
        assert evaluate(n, word) == target(n)
        assert word_to_tree(n, word) == tree
        assert word not in encoded
        encoded[word] = code
    assert len(encoded) == n ** (n - 2)
    if n <= 6:
        assert set(encoded) == brute_words(n)
    result = {"N": n, "m": n - 1, "states": len(encoded),
              "codec_both_inverse_identities": True,
              "independent_word_enumeration": n <= 6,
              "endpoint_preserved": True}
    if n == 2:
        result["singleton"] = True
        return result
    d = n - 2
    # Numerators for K under common denominator 8*d.
    rows = {}
    ratios = Counter()
    prefix_types, window_types = Counter(), Counter()
    positions = [Counter() for _ in range(n - 1)]
    for word in encoded:
        row = Counter({word: 6 * d})
        qrow = Counter({word: Fraction(1, 2)})
        for i in range(d):
            a, b = word[i:i + 2]
            assert a != b
            neighbors = {word}
            for sign in (-1, 1):
                y = hurwitz(word, i, sign)
                assert y in encoded
                assert hurwitz(y, i, -sign) == word
                row[y] += 1
                neighbors.add(y)
            expected = 2 if set(a).isdisjoint(b) else 3
            assert len(neighbors) == expected
            for y in neighbors:
                qrow[y] += Fraction(1, 2 * d * expected)
            window_types[str(cycle_type(evaluate(n, (a, b))))] += 1
        assert sum(row.values()) == 8 * d
        assert sum(qrow.values()) == 1
        for y, numer in row.items():
            if y != word:
                ratio = Fraction(numer, 8 * d) / qrow[y]
                assert Fraction(3, 4) <= ratio <= 1
                ratios[str(ratio)] += 1
        rows[word] = row
        for i, e in enumerate(word):
            positions[i][str(e)] += 1
            typ = cycle_type(evaluate(n, word[:i + 1]))
            assert len(typ) == n - i - 1
            prefix_types[str((i + 1, typ))] += 1
    for word, row in rows.items():
        for y, numer in row.items():
            assert rows[y][word] == numer
    seen = {next(iter(encoded))}
    todo = list(seen)
    while todo:
        word = todo.pop()
        for y in rows[word]:
            if y not in seen:
                seen.add(y)
                todo.append(y)
    assert len(seen) == len(encoded)
    result.update({"local_exact_detailed_balance": True, "hurwitz_connected": True,
                   "no_repeated_edges_or_equal_pairs": True,
                   "K_over_Q_offdiagonal_ratios": dict(ratios),
                   "prefix_cycle_type_counts": dict(prefix_types),
                   "window_product_type_counts": dict(window_types),
                   "position_edge_counts": [dict(c) for c in positions],
                   "weighted_support_signature": {"vertices": n, "factors": n - 1}})
    if n <= 6:
        code_to_word = {code: word for word, code in encoded.items()}
        changes, nonlocal_changes, max_changed_factors = 0, 0, 0
        witness = None
        for word, code in encoded.items():
            for i in range(d):
                for value in range(n):
                    if value == code[i]:
                        continue
                    new = code[:i] + (value,) + code[i + 1:]
                    other = code_to_word[new]
                    assert evaluate(n, other) == target(n)
                    count = sum(a != b for a, b in zip(word, other))
                    max_changed_factors = max(count, max_changed_factors)
                    changes += 1
                    if other not in rows[word]:
                        nonlocal_changes += 1
                        if count > 2 and witness is None:
                            witness = {"code": code, "new_code": new, "word": word,
                                       "new_word": other, "changed_factors": count}
        result["code_refresh"] = {"directed_changes": changes,
                                  "not_local_K_edges": nonlocal_changes,
                                  "max_changed_factors": max_changed_factors,
                                  "witness": witness}
    return result


def main():
    script = Path(__file__)
    baseline = script.parent.parent / '20261013-product-s3-mixing' / 'check.py'
    spec = importlib.util.spec_from_file_location('baseline', baseline)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    out = {"commit": subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
           "python": platform.python_version(), "dependencies": "standard library only",
           "seed": 20261013, "randomness": "none; exhaustive deterministic checks",
           "command": "python3 -B experiments/20261013-single-cycle-walk/check.py",
           "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
           "baseline_script": str(baseline.relative_to(Path.cwd())) if baseline.is_absolute() else str(baseline),
           "baseline_script_sha256": hashlib.sha256(baseline.read_bytes()).hexdigest(),
           "identity_baselines": [], "cycle_cases": []}
    for n, m in ((3, 4), (4, 4), (4, 6)):
        r = mod.check_case(n, m)
        out['identity_baselines'].append({key: r[key] for key in
                                        ('N','m','states','identity_and_exact_detailed_balance','connected')})
    assert evaluate(1, ()) == (0,)
    for n in range(2, 8):
        r = check_n(n)
        out['cycle_cases'].append(r)
        print(json.dumps({key: r[key] for key in ('N','m','states','endpoint_preserved')}), flush=True)
    a = ((0, 2), (0, 1), (2, 3))
    b = ((0, 2), (2, 3), (0, 1))
    assert evaluate(4, a) == evaluate(4, b) == target(4)
    assert set(a) == set(b) and word_to_tree(4, a) != word_to_tree(4, b)
    out['ordinary_support_forgetting_collision'] = {"word": a, "other_word": b}
    out['boundary_checks'] = 'N=1, N=2 singleton; N=3 first nontrivial case; minimal lengths'
    script.with_name('results.json').write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    print('PASS', flush=True)


if __name__ == '__main__':
    main()
