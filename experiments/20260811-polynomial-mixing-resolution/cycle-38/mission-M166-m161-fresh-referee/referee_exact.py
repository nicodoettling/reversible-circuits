#!/usr/bin/env python3
"""Clean-room exact audit of M161 at k=3,5.

Rank-two intermediates are generated from literal ordered transposition
pairs.  No predecessor module and no quotient matrix is imported or built.
Convention: (pq)(x)=p(q(x)); factors multiply left-to-right.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import subprocess
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path


def mul(p, q):
    return tuple(p[q[x]] for x in range(len(p)))


def inv(p):
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def cyc(n, entries):
    p = list(range(n))
    for x, y in zip(entries, entries[1:] + entries[:1]):
        p[x] = y
    return tuple(p)


def tr(n, edge):
    return cyc(n, tuple(edge))


def cycle_list(p):
    seen, ans = set(), []
    for a in range(len(p)):
        if a in seen:
            continue
        c, x = [], a
        while x not in seen:
            seen.add(x)
            c.append(x)
            x = p[x]
        ans.append(tuple(c))
    return ans


def completion(p, length):
    cs = cycle_list(p)
    if len(p) - len(cs) != length:
        return 0
    ans = math.factorial(length)
    for c in cs:
        d = len(c)
        if d > 1:
            ans = ans * d ** (d - 2) // math.factorial(d - 1)
    return ans


def tau(d):
    return Fraction(d ** (d - 1), math.factorial(d))


def orbit(p, h):
    hi = inv(h)
    out, x = set(), p
    while x not in out:
        out.add(x)
        x = mul(hi, mul(x, h))
    return frozenset(out)


def supported(n, h):
    """Literal pair enumeration; value is the ordered lift count."""
    edges = list(combinations(range(n), 2))
    counts = Counter()
    perms = {e: tr(n, e) for e in edges}
    for e in edges:
        for f in edges:
            if e != f:
                counts[mul(perms[e], perms[f])] += 1
    keep = {}
    for state, lift in counts.items():
        if completion(mul(inv(state), h), n - 3):
            keep[state] = lift
    return keep


def metadata(q):
    cs = cycle_list(q)
    owner, pos = {}, {}
    for i, c in enumerate(cs):
        for j, x in enumerate(c):
            owner[x], pos[x] = i, j
    return cs, owner, pos


def chord_nu(c, pos, edge):
    d = len(c)
    a = (pos[edge[1]] - pos[edge[0]]) % d
    a = min(a, d - a)
    return Fraction(math.factorial(d - 2), d ** (d - 2)) * tau(a) * tau(d - a)


def same_schema_and_mu(n, c, pos, e, f):
    ordered = sorted(set(e + f), key=lambda x: pos[x])
    labels = {x: j for j, x in enumerate(ordered)}
    matching = {tuple(sorted((labels[e[0]], labels[e[1]]))),
                tuple(sorted((labels[f[0]], labels[f[1]])))}
    if matching == {(0, 2), (1, 3)}:
        return "crossing", Fraction(0)
    schema = "IS" if matching == {(0, 1), (2, 3)} else "IN"

    local = {x: j for j, x in enumerate(c)}
    qloc = cyc(len(c), tuple(range(len(c))))
    eloc = tr(len(c), tuple(local[x] for x in e))
    floc = tr(len(c), tuple(local[x] for x in f))
    sizes = [len(x) for x in cycle_list(mul(mul(eloc, floc), qloc))]
    if len(sizes) != 3:
        return "crossing", Fraction(0)
    mu = Fraction(2 * math.factorial(len(c) - 3), len(c) ** (len(c) - 2))
    for d in sizes:
        mu *= tau(d)
    return schema, mu


def predicted_phase(n, q, e, f):
    cs, owner, pos = metadata(q)
    ie = {owner[x] for x in e}
    jf = {owner[x] for x in f}
    if len(ie) != 1 or len(jf) != 1:
        return "inadmissible", Fraction(0)
    i, j = next(iter(ie)), next(iter(jf))
    denom = (n - 3) * (n - 4)
    if i != j:
        ri, rj = len(cs[i]) - 1, len(cs[j]) - 1
        val = Fraction(2 * ri * rj, denom)
        val *= chord_nu(cs[i], pos, e) * chord_nu(cs[j], pos, f)
        return "X", val
    schema, mu = same_schema_and_mu(n, cs[i], pos, e, f)
    ri = len(cs[i]) - 1
    return schema, Fraction(ri * (ri - 1), denom) * mu


def qstr(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def analyze(k):
    n = 3 * k
    h = cyc(n, tuple(range(n)))
    A = cyc(n, (0, k, 2 * k))
    B = mul(tr(n, (0, 1)), tr(n, (k, 2 * k)))
    fA = completion(mul(inv(A), h), n - 3)
    fB = completion(mul(inv(B), h), n - 3)
    states = supported(n, h)
    kind_counts = Counter("T" if sum(x != s[x] for x in range(n)) == 3 else "D"
                          for s in states)
    lift_counts = Counter(states.values())

    ys = list(range(1, n - 2))
    targets = {}
    target_orbits = {}
    for y in ys:
        t = mul(tr(n, (0, 1)), tr(n, (y + 1, y + 2)))
        targets[y] = t
        target_orbits[y] = orbit(t, h)
        sizes = sorted(map(len, cycle_list(mul(inv(t), h))))
        assert sizes == [1, 1, n - 2]
    fT = completion(mul(inv(targets[1]), h), n - 3)
    pi_direct = Fraction(n * 2 * fT, n ** (n - 2))
    pi_formula = Fraction(2 * n * math.factorial(n - 3), n ** (n - 2)) * tau(n - 2)
    assert pi_direct == pi_formula
    assert all(len(target_orbits[y]) == n for y in ys)
    assert all(target_orbits[y] == target_orbits[n - 2 - y] for y in ys)
    orbit_multiplicities = Counter(target_orbits.values())
    assert set(orbit_multiplicities.values()) == {2}

    direct = [Fraction(0) for _ in ys]
    pieces = [defaultdict(Fraction) for _ in ys]
    local_checks = 0
    zero_crossing = zero_inadmissible = 0
    for state, lift in states.items():
        q = mul(inv(state), h)
        fs = completion(q, n - 3)
        signed = Fraction(lift, fs) * (Fraction(completion(mul(inv(mul(B, state)), h), n - 5), fB)
                                             - Fraction(completion(mul(inv(mul(A, state)), h), n - 5), fA))
        kind = "T" if sum(x != state[x] for x in range(n)) == 3 else "D"
        for iy, y in enumerate(ys):
            lag = y + 1
            for r in range(n):
                e = (r, (r + 1) % n)
                f = ((r + lag) % n, (r + lag + 1) % n)
                t = mul(tr(n, e), tr(n, f))
                f5 = completion(mul(t, q), n - 5)
                actual = Fraction(2 * f5, fs)
                schema, predicted = predicted_phase(n, q, e, f)
                assert actual == predicted, (k, state, y, r, schema, actual, predicted)
                local_checks += 1
                if schema == "crossing":
                    zero_crossing += 1
                elif schema == "inadmissible":
                    zero_inadmissible += 1
                if f5:
                    assert schema in {"IS", "IN", "X"}
                    value = signed * f5
                    direct[iy] += value
                    pieces[iy][f"{kind}_{schema}"] += value

    norm = Fraction(n ** (n - 2), n * fT)
    scores, category_totals = [], defaultdict(Fraction)
    for iy in range(len(ys)):
        score = norm * direct[iy]
        rebuilt = sum((norm * x for x in pieces[iy].values()), Fraction(0))
        assert score == rebuilt
        scores.append(score)
        for name, x in pieces[iy].items():
            category_totals[name] += norm * x
    assert set(category_totals) == {"T_IS", "T_IN", "T_X", "D_IS", "D_IN", "D_X"}
    assert all(scores[i] == scores[-1 - i] for i in range(len(scores)))

    Aexact = Fraction(k * k, n - 3) * sum(map(abs, scores), Fraction(0))
    Z_l1 = sum((abs(k * z) for z in scores), Fraction(0))
    assert Aexact == Fraction(k, n - 3) * Z_l1
    return {
        "k": k,
        "n": n,
        "target_cell_mass_exact": qstr(pi_direct),
        "target_colored_appearances_per_orbit": 2,
        "distinct_cell_orbits": len(orbit_multiplicities),
        "intermediate_kind_counts": dict(sorted(kind_counts.items())),
        "ordered_lift_histogram": {str(a): b for a, b in sorted(lift_counts.items())},
        "literal_phase_formula_checks": local_checks,
        "zero_crossing_phase_checks": zero_crossing,
        "zero_inadmissible_phase_checks": zero_inadmissible,
        "retained_signed_categories": sorted(category_totals),
        "mirror_symmetry_exact": True,
        "A_k_1_1_exact": qstr(Aexact),
        "A_k_1_1_float": float(Aexact),
        "sum_abs_Z_exact": qstr(Z_l1),
        "scores_exact": [qstr(x) for x in scores],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    payload = {
        "status": "fresh exact finite referee; no asymptotic inference",
        "target": "M73 nonlazy cyclic rank-two quotient, balanced fixed boundary cell",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "results": [analyze(3), analyze(5)],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps([{"k": x["k"], "A": x["A_k_1_1_float"],
                       "phase_checks": x["literal_phase_formula_checks"]}
                      for x in payload["results"]], indent=2))


if __name__ == "__main__":
    main()
