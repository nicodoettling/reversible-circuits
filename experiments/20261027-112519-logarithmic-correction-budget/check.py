#!/usr/bin/env python3
"""Small deterministic falsification checks; no MCMC or word enumeration."""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations
from math import comb, factorial, lgamma, log, log2
from pathlib import Path
import json
import platform
import subprocess


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def product(n, word):
    """Rightmost-first product: append a factor by swapping image entries."""
    p = list(range(n))
    for a, b in word:
        p[a], p[b] = p[b], p[a]
    return tuple(p)


def defect(p):
    seen = set()
    cycles = 0
    for x in range(len(p)):
        if x not in seen:
            cycles += 1
            while x not in seen:
                seen.add(x)
                x = p[x]
    return len(p) - cycles


def matching_endpoint(p, k):
    return sum(x != p[x] for x in range(len(p))) == 2 * k and all(
        p[p[x]] == x for x in range(len(p))
    )


def delta(n, k):
    return Fraction(comb(k, 2) * 2 * (2 * n - 1), 3 * n * (n - 1))


def ball_coefficients(n, k):
    a = [1] + [0] * k
    for r in range(1, n):
        for j in range(min(r, k), 0, -1):
            a[j] += r * a[j - 1]
    return a


def legal(n, word, i, k):
    return {
        e for e in combinations(range(n), 2)
        if defect(product(n, word[:i] + (e,) + word[i + 1:])) <= k
    }


def uniform_tv(a, b):
    return 1 - Fraction(len(a & b), max(len(a), len(b)))


def witness(n, k, boundary):
    edges = tuple((2 * j, 2 * j + 1) for j in range(k + 2))
    a, b, c = edges[:3]
    ds = edges[3:3 + k - (1 if boundary else 2)]
    r = k + 2 if boundary else 2
    prefix_x = (a,) + ds if boundary else (a, a) + ds
    prefix_y = (b,) + ds if boundary else (b, a) + ds
    x, y = prefix_x + (c,) * r, prefix_y + (c,) * r
    m = len(x)
    all_edges = set(combinations(range(n), 2))
    assert defect(product(n, x)) == (k if boundary else k - 2)
    assert defect(product(n, y)) == k
    classes = [0, 1, k] if boundary else [0, 1, 2, k]
    # Include the changed coordinate, each type of remaining prefix gate,
    # and a repeated-c coordinate; other instances are symmetric.
    tvs = {}
    for i in classes:
        lx, ly = legal(n, x, i, k), legal(n, y, i, k)
        if i < k:
            assert lx == ly == all_edges
        elif boundary:
            assert lx == {a, c, *ds} and ly == {b, c, *ds}
        else:
            assert lx == all_edges and ly == {a, b, c, *ds}
        tvs[i] = uniform_tv(lx, ly)
    M = comb(n, 2)
    actual = 1 - Fraction(1, 2 * m) + Fraction(r, 2 * m) * tvs[k]
    expected = (
        1 + Fraction(m - 2 * k - 1, 2 * m * (k + 1)) if boundary else
        1 - Fraction(1, 2 * m) + Fraction(r, 2 * m) * (1 - Fraction(k + 1, M))
    )
    assert actual == expected and actual > 1
    return {
        "kind": "hamming_witness", "N": n, "k": k, "m": m,
        "family": "both_boundary" if boundary else "interior_boundary",
        "conditional_TVs": {str(i): str(t) for i, t in tvs.items()},
        "W1_exact": str(actual), "W1": float(actual),
        "representative_coordinate_classes_checked": len(classes),
    }


def small_counts(n):
    ps = list(permutations(range(n)))
    lookup = {p: i for i, p in enumerate(ps)}
    M = comb(n, 2)
    transitions = []
    for p in ps:
        row = []
        for a, b in combinations(range(n), 2):
            q = list(p)
            q[a], q[b] = q[b], q[a]
            row.append(lookup[tuple(q)])
        transitions.append(row)
    ds = [defect(p) for p in ps]
    counts = [0] * len(ps)
    counts[0] = 1
    history = []
    rows = []
    coefficients = ball_coefficients(n, 8)
    for k in range(9):
        history.append(counts)
        assert sum(counts) == M ** k
        ball = [i for i, d in enumerate(ds) if d <= k and (d - k) % 2 == 0]
        assert len(ball) == sum(coefficients[j] for j in range(k % 2, k + 1, 2))
        assert all((counts[i] > 0) == (i in ball) for i in range(len(ps)))
        if k % 2 == 0:
            assert counts[0] >= M ** (k // 2)
        row = {"kind": "permutation_DP", "N": n, "k": k,
               "ball_size": len(ball), "identity_count": counts[0],
               "min_positive_count": min(counts[i] for i in ball)}
        if n >= 2 * k:
            assert min(counts[i] for i in ball) == factorial(k)
            assert all(counts[i] == factorial(k) for i in ball
                       if matching_endpoint(ps[i], k))
            alpha = Fraction(factorial(k) * len(ball), M ** k)
            tv = sum(abs(Fraction(counts[i], M ** k) - Fraction(1, len(ball)))
                     for i in ball) / 2
            assert tv <= 1 - alpha <= delta(n, k)
            row.update(alpha=str(alpha), TV_exact=str(tv), Delta=str(delta(n, k)))
        rows.append(row)
        nxt = [0] * len(ps)
        for i, value in enumerate(counts):
            for j in transitions[i]:
                nxt[j] += value
        counts = nxt
    for k in range(1, n // 2 + 1):
        M = comb(n, 2)
        matchings = [i for i, p in enumerate(ps) if matching_endpoint(p, k)]
        z, denom = history[k], history[2 * k][0]
        pi_d = sum(Fraction(z[i], M ** k) for i in matchings)
        nu_d = sum(Fraction(z[i] ** 2, denom) for i in matchings)
        upper_nu = Fraction(2 ** k, comb(2 * k, k))
        lower_pi = 1 - Fraction(2 * k * (k - 1), n - 1)
        assert pi_d >= lower_pi and nu_d <= upper_nu
        assert denom >= len(matchings) * factorial(2 * k) // (2 ** k)
        tv = sum(abs(Fraction(v, M ** k) - Fraction(v * v, denom))
                 for v in z) / 2
        assert tv >= pi_d - nu_d >= lower_pi - upper_nu
        rows.append({"kind": "prefix_lift_bias", "N": n, "m": k, "k": k,
                     "TV_exact": str(tv), "pi_matching_mass": str(pi_d),
                     "nu_matching_mass": str(nu_d),
                     "nu_matching_upper_bound": str(upper_nu)})
    if n in (4, 6):
        k = 2
        ball = [i for i, d in enumerate(ds) if d <= k and d % 2 == 0]
        for m in (4, 6):
            z = history[m]
            a = history[k]
            za = sum(z[i] for i in ball)
            zl = sum(z[i] * a[i] for i in ball)
            assert zl == history[m + k][0]
            lo, hi = min(z[i] for i in ball), max(z[i] for i in ball)
            epsilon = Fraction(hi - lo, hi + lo)
            alpha = Fraction(factorial(k) * len(ball), M ** k)
            # Both conditional word laws are uniform within endpoint fibers,
            # so endpoint TV equals full word-law TV, without word enumeration.
            tv = sum(abs(Fraction(z[i], za) - Fraction(z[i] * a[i], zl))
                     for i in ball) / 2
            bound = 1 - alpha * (1 - epsilon) / (1 + epsilon)
            assert tv <= bound <= delta(n, k) + 2 * epsilon
            rows.append({"kind": "conditional_transfer", "N": n, "m": m,
                         "k": k, "epsilon": str(epsilon), "TV_exact": str(tv),
                         "bound_exact": str(bound)})
    if n == 3:
        assert history[4][0] == 27
    if n == 4:
        assert history[4][0] == 120 and history[6][0] == 3936
    return rows


def main():
    script = Path(__file__).resolve()
    records = [{"kind": "manifest", "commit": subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "python": platform.python_version(), "dependencies": "standard library",
        "script_sha256": sha256(script.read_bytes()).hexdigest(),
        "command": f"python3 -B {script.relative_to(ROOT)}",
        "seeds": None, "method": "deterministic exact arithmetic; no simulation",
        "convention": "products rightmost first"}]
    assert product(3, ((0, 1), (1, 2))) == (1, 2, 0)
    for n in range(2, 7):
        records.extend(small_counts(n))
    for n, k in ((16, 4), (32, 10), (64, 12)):
        for boundary in (False, True):
            records.append(witness(n, k, boundary))
    for n in (32, 64, 128, 256, 1024, 4096):
        k = 2 * (n - 1).bit_length()
        M = comb(n, 2)
        coefficients = ball_coefficients(n, k)
        ball = sum(coefficients[j] for j in range(k % 2, k + 1, 2))
        alpha = Fraction(factorial(k) * ball, M ** k)
        assert 0 < alpha <= 1 and 1 - alpha <= delta(n, k)
        records.append({"kind": "log_budget_coefficient_DP", "N": n, "k": k,
                        "alpha_exact": str(alpha), "TV_upper_exact": str(1 - alpha),
                        "TV_upper": float(1 - alpha), "Delta": float(delta(n, k))})
    for n in (2 ** 20, 2 ** 40):
        k = 2 * (n - 1).bit_length()
        records.append({"kind": "proved_bound_evaluation", "N": n, "k": k,
                        "Delta": float(delta(n, k)),
                        "prefix_lift_TV_lower_bound": float(
                            1 - Fraction(2 * k * (k - 1), n - 1)
                            - Fraction(2 ** k, comb(2 * k, k))),
                        "log2_multiplicity_ratio_lower_bound":
                        k / 2 * log2(comb(n, 2)) - lgamma(k + 1) / log(2)})
    (HERE / "results.jsonl").write_text("".join(json.dumps(r, sort_keys=True) + "\n"
                                               for r in records))
    print(json.dumps({"status": "PASS", "records": len(records),
                      "hamming_witnesses": 6, "max_permutation_states": factorial(6),
                      "max_coefficient_DP_N": 4096, "simulation": False}))


if __name__ == "__main__":
    main()
