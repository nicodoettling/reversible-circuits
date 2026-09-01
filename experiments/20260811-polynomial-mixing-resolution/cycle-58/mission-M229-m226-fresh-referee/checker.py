#!/usr/bin/env python3
"""Clean-room exact M229 audit at k=3,5.

Uses only standard-library primitives and loads no M226 code or data.
"""

import json
from fractions import Fraction
from itertools import combinations
from math import factorial


def b(d):
    return Fraction(d ** (d - 1), factorial(d))


def ker(k, r, d):
    return b(d) * b(r - d) / ((2 * k - 3) * b(r))


def h(k, r):
    return Fraction((r - 1) * (r - 2), r * (2 * k - 3))


def q(k, s):
    return Fraction(k, k - 1) * b(s) * b(k - s) / b(k)


def g_closed(k, x):
    D, j = 2 * k - 1, (k - 1) // 2
    ans = q(k, x) * h(k, D - x) if x <= j else Fraction()
    ans += sum(q(k, s) * (s - x - 1) * ker(k, s, x)
               for s in range(x + 1, j + 1))
    ans += sum(q(k, s) * (D - s - x - 1) * ker(k, D - s, x)
               for s in range(1, j + 1))
    return ans


def g_direct(k, x):
    """Directly collect relevant B F(x) sources."""
    D, j = 2 * k - 1, (k - 1) // 2
    ans = Fraction()
    for s in range(1, j + 1):
        if x == s:
            ans += q(k, s) * h(k, D - s)
        if x == D - s:
            ans += q(k, s) * h(k, s)
        if x < s:
            ans += q(k, s) * (s - x - 1) * ker(k, s, x)
        if x < D - s:
            ans += q(k, s) * (D - s - x - 1) * ker(k, D - s, x)
    return ans


def f_atom(k, x, y):
    D, n = 2 * k - 1, 3 * k
    if x < k:
        atoms = ((x, D - 2 * x), (x + 1, x), (x + k, x))
    else:
        c = D - x
        atoms = ((n - c, D - 2 * c), (n - c - 1, c), (n - c - k, c))
    return Fraction(sum(mult for size, mult in atoms if size == y), D)


def j_atom(k, x, y):
    return Fraction(k - x, k) if x == y else Fraction()


def w_atom(k, r, y, side):
    atom = f_atom if side == "B" else j_atom
    return sum((r - d - 1) * ker(k, r, d) * atom(k, d, y)
               for d in range(1, r))


def direct_y_atoms(k, y):
    D, j = 2 * k - 1, (k - 1) // 2
    raw_b = raw_a = Fraction()
    for s in range(1, j + 1):
        bs = h(k, s) * f_atom(k, D - s, y) + h(k, D - s) * f_atom(k, s, y)
        bf = w_atom(k, s, y, "B") + w_atom(k, D - s, y, "B")
        ass = (
            h(k, s) * j_atom(k, k - s, y)
            + h(k, k - s) * j_atom(k, s, y)
            + Fraction(k - 1, 2 * k - 3)
            * (j_atom(k, s, y) + j_atom(k, k - s, y))
        )
        c = (k - y) * ker(k, k, y) if 1 <= y < k else Fraction()
        af = w_atom(k, s, y, "A") + w_atom(k, k - s, y, "A") + c
        raw_b += q(k, s) * (bs + bf)
        raw_a += q(k, s) * (ass + af)
    return raw_b, raw_a


def b_closed(k, y):
    D = 2 * k - 1
    if y < k:
        return Fraction(D - 2 * y, D) * g_closed(k, y) + Fraction(y - 1, D) * g_closed(k, y - 1)
    if y == k:
        return Fraction(k - 1, D) * g_closed(k, k - 1)
    return Fraction(2 * k - y, D) * g_closed(k, y - 1) + Fraction(y - k, D) * g_closed(k, y - k)


def a_closed(k, y):
    if y >= k:
        return Fraction()
    m = k - y
    return 2 * b(y) * b(m) / ((2 * k - 3) * b(k)) * (
        m + Fraction((m - 1) * (m - 2), k - 1)
    )


def compose(p, qperm):
    return tuple(p[qperm[x]] for x in range(len(p)))


def inverse(p):
    ans = [0] * len(p)
    for x, y in enumerate(p):
        ans[y] = x
    return tuple(ans)


def cycperm(n, entries):
    ans = list(range(n))
    for x, y in zip(entries, entries[1:] + entries[:1]):
        ans[x] = y
    return tuple(ans)


def trans(n, x, y):
    ans = list(range(n))
    ans[x], ans[y] = ans[y], ans[x]
    return tuple(ans)


def cycles(p):
    seen, out = set(), []
    for start in range(len(p)):
        if start in seen:
            continue
        part, x = [], start
        while x not in seen:
            seen.add(x)
            part.append(x)
            x = p[x]
        out.append(tuple(part))
    return out


def edges(p):
    return [trans(len(p), x, y) for part in cycles(p) for x, y in combinations(part, 2)]


def verts(e):
    return tuple(x for x in range(len(e)) if e[x] != x)


def runs(part, n):
    support = set(part)
    return sum(1 for x in support if (x - 1) % n not in support)


def split(e, original):
    x, y = verts(e)
    part = next(c for c in original if x in c)
    gap = (part.index(y) - part.index(x)) % len(part)
    return min(gap, len(part) - gap)


def source(k, side):
    n = 3 * k
    if side == "B":
        part = tuple(range(1, k)) + tuple(range(2 * k, 3 * k))
        return cycperm(n, part), [part]
    p, qpart = tuple(range(k)), tuple(range(2 * k, 3 * k))
    return compose(cycperm(n, p), cycperm(n, qpart)), [p, qpart]


def literal_atoms(k, side):
    n, j = 3 * k, (k - 1) // 2
    target = cycperm(n, tuple(range(n)))
    src, original = source(k, side)
    out = {}
    for s in range(1, j + 1):
        firsts = [e for e in edges(src) if split(e, original) == s]
        atom = {}
        for e in firsts:
            after = compose(e, src)
            for f in edges(after):
                if set(verts(e)) & set(verts(f)):
                    continue
                parent = next(c for c in cycles(after) if set(verts(f)).issubset(c))
                aft2 = compose(f, after)
                children = [c for c in cycles(aft2) if set(c).issubset(parent)]
                weight = ker(k, len(parent), len(children[0]))
                residual = compose(inverse(compose(e, f)), target)
                for face in cycles(residual):
                    key = (runs(face, n), len(face))
                    atom[key] = atom.get(key, Fraction()) + weight / len(firsts)
        out[s] = atom
    return out


def shortcut_witness():
    k, n, ell = 5, 15, 7
    target = cycperm(n, tuple(range(n)))
    src, original = source(k, "B")
    witnesses = []
    for e in edges(src):
        if split(e, original) != 2:
            continue
        after = compose(e, src)
        for parent in cycles(after):
            if len(parent) != 7:
                continue
            qualifying = []
            for f in edges(after):
                if set(verts(e)) & set(verts(f)) or not set(verts(f)).issubset(parent):
                    continue
                aft2 = compose(f, after)
                children = [c for c in cycles(aft2) if set(c).issubset(parent)]
                if min(map(len, children)) != 1:
                    continue
                residual = compose(inverse(compose(e, f)), target)
                two = next(len(c) for c in cycles(residual) if runs(c, n) == 2)
                if two <= ell:
                    qualifying.append([list(verts(f)), two])
            if len(qualifying) == 5:
                witnesses.append({"first_edge": verts(e), "parent": parent, "second_edges": qualifying})
    assert witnesses
    return witnesses[0]


def audit_k(k):
    L = (3 * k - 1) // 2
    # G is needed only through L-1 by the seam coefficient formulas.
    assert all(g_closed(k, x) == g_direct(k, x) for x in range(1, L))
    rows = []
    for y in range(2, L + 1):
        db, da = direct_y_atoms(k, y)
        assert db == b_closed(k, y)
        assert da == a_closed(k, y)
        rows.append([y, str(db - da)])

    bp, ap = literal_atoms(k, "B"), literal_atoms(k, "A")
    for y in range(2, L + 1):
        one = two = total = Fraction()
        for s in range(1, (k - 1) // 2 + 1):
            one += q(k, s) * (bp[s].get((1, y), 0) - ap[s].get((1, y), 0))
            two += q(k, s) * (bp[s].get((2, y), 0) - ap[s].get((2, y), 0))
            total += q(k, s) * (
                sum(v for (r, size), v in bp[s].items() if size == y)
                - sum(v for (r, size), v in ap[s].items() if size == y)
            )
        assert one == Fraction(rows[y - 2][1])
        assert total == one + two
    return {"k": k, "Y_coefficients": rows, "checks_pass": True}


payload = {
    "mission": "M229",
    "method": "clean-room exact formulas and literal tuples",
    "imports_M226": False,
    "universal_inference": False,
    "results": [audit_k(3), audit_k(5)],
    "shortcut_witness": shortcut_witness(),
}
print(json.dumps(payload, sort_keys=True))
