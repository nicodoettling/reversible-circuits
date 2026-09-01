#!/usr/bin/env python3
"""Independent exact k=3,5 referee checker for M199.

No M199 code or data is imported. Completion ratios and literal permutation
products are compared with separately coded interval formulas. Finite checks
are calibration/falsification only.
"""

from __future__ import annotations

import json
import math
import platform
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path


def compose(p, q):
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p):
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def transposition(n, edge):
    x, y = edge
    out = list(range(n))
    out[x], out[y] = out[y], out[x]
    return tuple(out)


def cycle_perm(n, entries):
    out = list(range(n))
    for x, y in zip(entries, entries[1:] + entries[:1]):
        out[x] = y
    return tuple(out)


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


def internal_edges(p):
    return [
        (min(x, y), max(x, y))
        for part in cycles(p)
        for x, y in combinations(part, 2)
    ]


def left_multiply(edge, p):
    return compose(transposition(len(p), edge), p)


def tau(d):
    return Fraction(d ** (d - 1), math.factorial(d))


def completion(p):
    parts = cycles(p)
    rank = sum(len(part) - 1 for part in parts)
    out = Fraction(math.factorial(rank))
    for part in parts:
        out *= tau(len(part))
    return out


def kernel(R, r, d):
    return tau(d) * tau(r - d) / (R * tau(r))


def source(k, side):
    n = 3 * k
    if side == "B":
        exterior = tuple(range(1, k)) + tuple(range(2 * k, 3 * k))
        return cycle_perm(n, exterior), [exterior]
    lower, upper = tuple(range(k)), tuple(range(2 * k, 3 * k))
    return compose(cycle_perm(n, lower), cycle_perm(n, upper)), [lower, upper]


def split_size(edge, originals):
    x, y = edge
    part = next(part for part in originals if x in part and y in part)
    ix, iy = part.index(x), part.index(y)
    d = (iy - ix) % len(part)
    return min(d, len(part) - d)


def ambient_runs(part, n):
    support = set(part)
    return sum((x - 1) % n not in support for x in support)


def literal_atoms(k, e, f):
    n = 3 * k
    h = cycle_perm(n, tuple(range(n)))
    ef = compose(transposition(n, e), transposition(n, f))
    residual = compose(inverse(ef), h)
    out = Counter()
    for part in cycles(residual):
        run_count = ambient_runs(part, n)
        assert run_count in (1, 2)
        out[(run_count, len(part))] += 1
    assert sum(out.values()) == 3
    return out


def gamma(k, side, s):
    other = 2 * k - 1 - s if side == "B" else k - s
    return Fraction(2, 2 * k - 3) * (
        2 - Fraction(1, s) - Fraction(1, other)
    )


def gap(V, n, i, x):
    D = len(V)
    return (V[(i + x) % D] - V[i]) % n


def direct_law(k, side, s):
    src, originals = source(k, side)
    first_edges = [e for e in internal_edges(src) if split_size(e, originals) == s]
    assert len(first_edges) == (2 * k - 1 if side == "B" else 2 * k)
    raw = defaultdict(Fraction)
    disjoint_mass = shared_mass = Fraction()
    collision_events = 0
    kinds = Counter()
    R = 2 * k - 3
    V = tuple(range(1, k)) + tuple(range(2 * k, 3 * k))
    seams = (set(V[: k - 1]), set(V[k - 1 :]))

    def kind(edge):
        if side != "B":
            return "contiguous"
        x, y = edge
        return "same" if any(x in run and y in run for run in seams) else "cross"

    for e in first_edges:
        after_e = left_multiply(e, src)
        second_total = Fraction()
        for f in internal_edges(after_e):
            after_f = left_multiply(f, after_e)
            weight = completion(after_f) / completion(after_e)
            parent = next(part for part in cycles(after_e) if set(f).issubset(part))
            children = [
                part for part in cycles(after_f) if set(part).issubset(parent)
            ]
            assert len(children) == 2
            assert weight == kernel(R, len(parent), len(children[0]))
            second_total += weight
            if set(e) & set(f):
                shared_mass += weight / len(first_edges)
                continue
            atoms = literal_atoms(k, e, f)
            disjoint_mass += weight / len(first_edges)
            for atom, multiplicity in atoms.items():
                raw[atom] += weight * multiplicity / len(first_edges)
            collision_events += any(v > 1 for v in atoms.values())
            kinds[(kind(e), kind(f))] += 1
        assert second_total == 1
    assert shared_mass == gamma(k, side, s)
    assert disjoint_mass == 1 - shared_mass
    law = {atom: value / disjoint_mass for atom, value in raw.items()}
    assert sum(law.values()) == 3
    return law, disjoint_mass, shared_mass, collision_events, kinds


def direct_pair_set(k, side, s):
    src, originals = source(k, side)
    out = set()
    for e in internal_edges(src):
        if split_size(e, originals) != s:
            continue
        after_e = left_multiply(e, src)
        for f in internal_edges(after_e):
            if not set(e) & set(f):
                assert (e, f) not in out
                out.add((e, f))
    return out


def b_tuple_law(k, s):
    n, D, R = 3 * k, 2 * k - 1, 2 * k - 3
    V = tuple(range(1, k)) + tuple(range(2 * k, 3 * k))
    raw, pairs = defaultdict(Fraction), Counter()
    assertions = 0
    for i in range(D):
        for r in (s, D - s):
            z = D - r
            e = tuple(sorted((V[i], V[(i + r) % D])))
            for d in range(1, r):
                weight = kernel(R, r, d)
                for a in range(1, r - d):
                    f = tuple(sorted((V[(i + a) % D], V[(i + a + d) % D])))
                    assert not set(e) & set(f)
                    pairs[(e, f)] += 1
                    g1 = gap(V, n, (i + r) % D, z)
                    g2 = gap(V, n, (i + a) % D, d)
                    predicted = Counter()
                    predicted[(1, g1)] += 1
                    predicted[(1, g2)] += 1
                    predicted[(2, n - g1 - g2)] += 1
                    assert literal_atoms(k, e, f) == predicted
                    assertions += 1
                    for atom, multiplicity in predicted.items():
                        raw[atom] += weight * multiplicity / D
    assert all(v == 1 for v in pairs.values())
    normalizer = 1 - gamma(k, "B", s)
    assert sum(raw.values()) == 3 * normalizer
    return {a: v / normalizer for a, v in raw.items()}, set(pairs), assertions


def seam_check(k):
    n, D = 3 * k, 2 * k - 1
    V = tuple(range(1, k)) + tuple(range(2 * k, 3 * k))
    for x in range(1, D):
        actual = Counter(gap(V, n, i, x) for i in range(D))
        if x < k:
            expected = Counter({x: D - 2 * x, x + 1: x, x + k: x})
        else:
            c = D - x
            expected = Counter(
                {n - c: D - 2 * c, n - c - 1: c, n - c - k: c}
            )
        expected += Counter()
        assert actual == expected
    return D - 1


def J(k, ell, x):
    return Fraction(k - x, k) if 2 <= x <= ell else Fraction()


def a_y_formula(k, s, ell):
    R = 2 * k - 3
    u = Fraction(k - 1, R)
    h = lambda r: Fraction((r - 1) * (r - 2), r * R)
    total = Fraction()
    for r in (s, k - s):
        total += h(r) * J(k, ell, k - r)
        total += sum(
            (r - d - 1) * kernel(R, r, d) * J(k, ell, d)
            for d in range(1, r)
        )
    total += u * (J(k, ell, s) + J(k, ell, k - s))
    total += sum(
        (k - d) * kernel(R, k, d)
        for d in range(1, k)
        if 2 <= d <= ell
    )
    return total / (1 - gamma(k, "A", s))


def prefix(law, ell, one_run_only):
    return sum(
        mass
        for (run_count, size), mass in law.items()
        if 2 <= size <= ell and (not one_run_only or run_count == 1)
    )


def untouched_mass_check(k, s):
    src, originals = source(k, "A")
    first_edges = [e for e in internal_edges(src) if split_size(e, originals) == s]
    R = 2 * k - 3
    for e in first_edges:
        after_e = left_multiply(e, src)
        total = Fraction()
        for f in internal_edges(after_e):
            parent = next(part for part in cycles(after_e) if set(f).issubset(part))
            if len(parent) == k:
                total += completion(left_multiply(f, after_e)) / completion(after_e)
        assert total == Fraction(k - 1, R)
    return len(first_edges)


def boundary_map_check(k):
    D = 2 * k - 1
    domain = lambda r: {
        (d, a) for d in range(1, r) for a in range(1, r - d)
    }
    out = []
    for s in range(1, k - 1):
        short_old, short_new = domain(s), domain(s + 1)
        long_old, long_new = domain(D - s), domain(D - s - 1)
        added, deleted = short_new - short_old, long_old - long_new
        assert short_old <= short_new and long_new <= long_old
        assert added == {(d, s - d) for d in range(1, s)}
        assert deleted == {
            (d, D - s - 1 - d) for d in range(1, D - s - 1)
        }
        out.append(
            {
                "s": s,
                "short_added_per_start": len(added),
                "long_deleted_per_start": len(deleted),
                "short_paired_per_start": len(short_old),
                "long_paired_per_start": len(long_new),
            }
        )
    return out


def run_case(k):
    assertions = seam_check(k)
    collisions = {"B": 0, "A": 0}
    shared, disjoint = {"B": {}, "A": {}}, {"B": {}, "A": {}}
    kinds = Counter()
    for s in range(1, k):
        law, dm, gm, count, strata = direct_law(k, "B", s)
        tuple_law, tuple_pairs, checks = b_tuple_law(k, s)
        assert tuple_law == law
        assert tuple_pairs == direct_pair_set(k, "B", s)
        assertions += checks + 2
        collisions["B"] += count
        shared["B"][str(s)], disjoint["B"][str(s)] = str(gm), str(dm)
        kinds.update(strata)
        for ell in range(2, (3 * k - 1) // 2 + 1):
            assert prefix(tuple_law, ell, False) == prefix(law, ell, False)
            assert prefix(tuple_law, ell, True) == prefix(law, ell, True)
            assertions += 2
    for s in range(1, (k - 1) // 2 + 1):
        law, dm, gm, count, _ = direct_law(k, "A", s)
        assertions += untouched_mass_check(k, s)
        collisions["A"] += count
        shared["A"][str(s)], disjoint["A"][str(s)] = str(gm), str(dm)
        for ell in range(2, (3 * k - 1) // 2 + 1):
            assert prefix(law, ell, True) == a_y_formula(k, s, ell)
            assertions += 1
    return {
        "k": k,
        "exact_assertions": assertions,
        "conditional_shared_mass": shared,
        "conditional_disjoint_mass": disjoint,
        "collision_events_retained": collisions,
        "B_disjoint_kind_strata": {
            f"{a}/{b}": v for (a, b), v in sorted(kinds.items())
        },
        "boundary_domain_edits": boundary_map_check(k),
    }


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: cleanroom_check.py OUTPUT.json")
    payload = {
        "mission": "M207",
        "method": "independent completion-ratio and literal-face audit",
        "parameters": {"k": [3, 5], "seed": None},
        "python": platform.python_version(),
        "standard_library_only": True,
        "imports_m199_code_or_data": False,
        "finite_only": True,
        "universal_inference": False,
        "results": [run_case(k) for k in (3, 5)],
        "status": "all exact k=3,5 referee assertions passed",
    }
    Path(sys.argv[1]).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
