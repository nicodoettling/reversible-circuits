#!/usr/bin/env python3
"""Clean-room exact audit of the frozen M174 PCS reduction at k=3,5.

No M174 module is imported.  First-pair laws are reconstructed from literal
ordered transposition choices in uniform minimal factorizations.  The fixed
cell response is computed both by a literal all-phase boundary-edge sum and
by the component decorations.  The affine formula is checked coefficientwise
as a polynomial in a formal variable E (later E=e).

Convention: (pq)(x)=p(q(x)); displayed factors multiply left-to-right.
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import platform
import subprocess
import time
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path


Perm = tuple[int, ...]
Poly = tuple[Fraction, Fraction, Fraction]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    ans = [0] * len(p)
    for x, y in enumerate(p):
        ans[y] = x
    return tuple(ans)


def cycle_perm(n: int, entries: tuple[int, ...]) -> Perm:
    ans = list(range(n))
    for x, y in zip(entries, entries[1:] + entries[:1]):
        ans[x] = y
    return tuple(ans)


def transposition(n: int, x: int, y: int) -> Perm:
    return cycle_perm(n, (x, y))


def cycles(p: Perm) -> list[tuple[int, ...]]:
    seen: set[int] = set()
    ans: list[tuple[int, ...]] = []
    for start in range(len(p)):
        if start in seen:
            continue
        c: list[int] = []
        x = start
        while x not in seen:
            seen.add(x)
            c.append(x)
            x = p[x]
        ans.append(tuple(c))
    return ans


@lru_cache(maxsize=None)
def completion_sizes(sizes: tuple[int, ...], length: int) -> int:
    if not sizes or any(d <= 0 for d in sizes):
        return 0
    if sum(sizes) - len(sizes) != length:
        return 0
    ans = Fraction(math.factorial(length))
    for d in sizes:
        if d > 1:
            ans *= Fraction(d ** (d - 2), math.factorial(d - 1))
    if ans.denominator != 1:
        raise AssertionError((sizes, length, ans))
    return ans.numerator


def completion(p: Perm, length: int) -> int:
    return completion_sizes(tuple(sorted(map(len, cycles(p)))), length)


def tau(d: int) -> Fraction:
    if d < 1:
        raise ValueError(d)
    return Fraction(d ** (d - 1), math.factorial(d))


def internal_edges(n: int, component: tuple[int, ...]):
    for x, y in combinations(sorted(component), 2):
        yield transposition(n, x, y)


def ambient_runs(component: tuple[int, ...], n: int) -> tuple[int, ...]:
    support = set(component)
    starts = sorted(x for x in support if (x - 1) % n not in support)
    if not starts:
        return (n,)
    lengths = []
    for start in starts:
        length = 1
        while (start + length) % n in support:
            length += 1
        lengths.append(length)
    if sum(lengths) != len(support):
        raise AssertionError((component, starts, lengths))
    return tuple(sorted(lengths))


def qstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def padd(x: Poly, y: Poly) -> Poly:
    return tuple(a + b for a, b in zip(x, y))  # type: ignore[return-value]


def pscale(c: Fraction | int, x: Poly) -> Poly:
    return tuple(Fraction(c) * a for a in x)  # type: ignore[return-value]


def pmul(x: Poly, y: Poly) -> Poly:
    raw = [Fraction(0)] * 5
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            raw[i + j] += a * b
    if raw[3] or raw[4]:
        raise AssertionError((x, y, raw))
    return tuple(raw[:3])  # type: ignore[return-value]


def component_data(n: int, s: Perm):
    h = cycle_perm(n, tuple(range(n)))
    q = compose(inverse(s), h)
    answer = []
    for c in cycles(q):
        d = len(c)
        runs = ambient_runs(c, n)
        if len(runs) == 1:
            eps, linear_c = Fraction(1, 2), 2
            generic = d - 1
            adjacent = max(d - 2, 0)
        elif len(runs) == 2:
            eps, linear_c = Fraction(-1, 2), 4
            generic = d - 2
            adjacent = sum(max(a - 2, 0) for a in runs)
        else:
            raise AssertionError((d, runs))
        literal_generic = sum(s[(r + 1) % n] == (r + 1) % n and r in c for r in range(n))
        literal_adjacent = sum(
            s[(r + 1) % n] == (r + 1) % n
            and s[(r + 2) % n] == (r + 2) % n
            and r in c
            for r in range(n)
        )
        if (literal_generic, literal_adjacent) != (generic, adjacent):
            raise AssertionError((d, runs, literal_generic, literal_adjacent, generic, adjacent))
        ordered = generic * (generic - 1) - 2 * adjacent
        U = Fraction(0) if generic == 0 else generic * tau(d - 1) / tau(d)
        V = Fraction(0) if ordered == 0 else ordered * tau(d - 2) / tau(d)
        answer.append(
            {
                "size": d,
                "runs": runs,
                "eps": eps,
                "c": linear_c,
                "U": U,
                "V": V,
            }
        )
    if len(answer) != 3:
        raise AssertionError(answer)
    return q, answer


def decorated_response(n: int, data) -> Fraction:
    total = sum((x["V"] for x in data), Fraction(0))
    total += 2 * sum(
        (data[i]["U"] * data[j]["U"] for i in range(3) for j in range(i + 1, 3)),
        Fraction(0),
    )
    return total / ((n - 3) * (n - 4))


def literal_response(n: int, q: Perm) -> Fraction:
    boundary = [transposition(n, r, (r + 1) % n) for r in range(n)]
    total = 0
    for r in range(n):
        for lag in range(2, n - 1):
            t = (r + lag) % n
            total += completion(compose(compose(boundary[r], boundary[t]), q), n - 5)
    return Fraction(total, completion(q, n - 3))


def affine_boundary_poly(n: int, kind: str, data) -> Poly:
    L = 0 if kind == "T" else -2
    B: Poly = (Fraction(-sum(x["c"] * x["size"] for x in data) - L * n), Fraction(0), Fraction(0))
    for x in data:
        d, eps, c, V = x["size"], x["eps"], x["c"], x["V"]
        v: Poly = (Fraction(-d * d + c * d), Fraction(0), V)
        B = padd(B, v)
    for i in range(3):
        for j in range(i + 1, 3):
            xi, xj = data[i], data[j]
            # eps+u = E*U-d exactly.
            wi: Poly = (Fraction(-xi["size"]), xi["U"], Fraction(0))
            wj: Poly = (Fraction(-xj["size"]), xj["U"], Fraction(0))
            bracket = padd(pscale(xi["size"], wj), pscale(xj["size"], wi))
            bracket = padd(bracket, pmul(wi, wj))
            B = padd(B, pscale(2, bracket))
    return B


def source_law(k: int, label: str):
    n = 3 * k
    h = cycle_perm(n, tuple(range(n)))
    if label == "A":
        source = cycle_perm(n, (0, k, 2 * k))
    elif label == "B":
        source = compose(transposition(n, 0, 1), transposition(n, k, 2 * k))
    else:
        raise ValueError(label)
    residual = compose(inverse(source), h)
    original = cycles(residual)
    middle = next(i for i, c in enumerate(original) if k in c)
    owner = {x: i for i, c in enumerate(original) for x in c}
    denominator = completion(residual, n - 3)
    law: collections.defaultdict[tuple[Perm, int, str], Fraction] = collections.defaultdict(Fraction)
    for i, c in enumerate(original):
        for first in internal_edges(n, c):
            after = compose(first, residual)
            for c2 in cycles(after):
                if len(c2) == 1:
                    continue
                old = owner[c2[0]]
                if any(owner[x] != old for x in c2):
                    raise AssertionError(c2)
                for second in internal_edges(n, c2):
                    remainder = compose(second, after)
                    numerator = completion(remainder, n - 5)
                    if not numerator:
                        continue
                    s = compose(first, second)
                    support = sum(s[x] != x for x in range(n))
                    if support not in (3, 4):
                        raise AssertionError(support)
                    kind = "T" if support == 3 else "D"
                    j = int(i != middle) + int(old != middle)
                    law[(s, j, kind)] += Fraction(numerator, denominator)
    if sum(law.values(), Fraction(0)) != 1:
        raise AssertionError(sum(law.values(), Fraction(0)))
    return dict(law)


def analyze(k: int) -> dict[str, object]:
    if k not in (3, 5):
        raise ValueError("clean-room audit is capped at k=3,5")
    started = time.monotonic()
    n = 3 * k
    law_a = source_law(k, "A")
    law_b = source_law(k, "B")
    states = sorted({key[0] for key in law_a} | {key[0] for key in law_b})
    responses: dict[Perm, Fraction] = {}
    boundaries: dict[Perm, Poly] = {}
    kind_by_state: dict[Perm, str] = {}
    run_profiles = collections.Counter()
    for s in states:
        q, data = component_data(n, s)
        kind = "T" if sum(s[x] != x for x in range(n)) == 3 else "D"
        profile = tuple(sorted(len(x["runs"]) for x in data))
        expected = (1, 1, 1) if kind == "T" else (1, 1, 2)
        if profile != expected:
            raise AssertionError((kind, profile))
        run_profiles[(kind, profile)] += 1
        direct = literal_response(n, q)
        decorated = decorated_response(n, data)
        if direct != decorated:
            raise AssertionError((s, direct, decorated))
        B = affine_boundary_poly(n, kind, data)
        L = 0 if kind == "T" else -2
        lhs = padd((Fraction(n * n + L * n), Fraction(0), Fraction(0)), B)
        rhs: Poly = (Fraction(0), Fraction(0), Fraction((n - 3) * (n - 4)) * direct)
        if lhs != rhs:
            raise AssertionError((kind, lhs, rhs))
        responses[s] = direct
        boundaries[s] = B
        kind_by_state[s] = kind

    def marginal(law, j=None, kind=None):
        ans: collections.defaultdict[Perm, Fraction] = collections.defaultdict(Fraction)
        for (s, jj, kk), p in law.items():
            if (j is None or jj == j) and (kind is None or kk == kind):
                ans[s] += p
        return dict(ans)

    if marginal(law_a, j=0) != marginal(law_b, j=0):
        raise AssertionError("J=0 measures differ")
    m = k - 1
    denominator = 3 * m * (3 * m - 1)
    alphas = (
        Fraction(m * (m - 1), denominator),
        Fraction(4 * m * m, denominator),
        Fraction(2 * m * (2 * m - 1), denominator),
    )
    for label, law in (("A", law_a), ("B", law_b)):
        for j in range(3):
            mass = sum((p for (_, jj, _), p in law.items() if jj == j), Fraction(0))
            if mass != alphas[j]:
                raise AssertionError((label, j, mass, alphas[j]))

    signed: collections.defaultdict[Perm, Fraction] = collections.defaultdict(Fraction)
    signed_kind_channel = collections.defaultdict(Fraction)
    for law, sign in ((law_b, 1), (law_a, -1)):
        for (s, j, kind), p in law.items():
            signed[s] += sign * p
            signed_kind_channel[(j, kind)] += sign * p
    if any(signed_kind_channel[(j, kind)] for j in (0, 1) for kind in ("T", "D")):
        raise AssertionError(signed_kind_channel)
    eta_t = signed_kind_channel[(2, "T")]
    eta_closed = Fraction(12 * (k - 1), 3 * k * (3 * k - 4) * (2 * k - 1))
    if eta_t != eta_closed or signed_kind_channel[(2, "D")] != -eta_closed:
        raise AssertionError((eta_t, eta_closed, signed_kind_channel))

    delta = sum((p * responses[s] for s, p in signed.items()), Fraction(0))
    channel_deltas = {
        j: sum(
            (
                (law_b.get((s, j, kind_by_state[s]), Fraction(0)) - law_a.get((s, j, kind_by_state[s]), Fraction(0)))
                * responses[s]
                for s in states
            ),
            Fraction(0),
        )
        for j in range(3)
    }
    if sum(channel_deltas.values(), Fraction(0)) != delta or channel_deltas[0] != 0:
        raise AssertionError(channel_deltas)

    eta_b: Poly = (Fraction(0), Fraction(0), Fraction(0))
    for s, p in signed.items():
        eta_b = padd(eta_b, pscale(p, boundaries[s]))
    expected_eta_b: Poly = (
        -2 * n * eta_t,
        Fraction(0),
        Fraction((n - 3) * (n - 4)) * delta,
    )
    if eta_b != expected_eta_b:
        raise AssertionError((eta_b, expected_eta_b))

    target = compose(transposition(n, 0, 1), transposition(n, 2, 3))
    h = cycle_perm(n, tuple(range(n)))
    f_target = completion(compose(inverse(target), h), n - 3)
    pi_completion = Fraction(2 * n * f_target, n ** (n - 2))
    pi_closed = Fraction(2, n - 2) * Fraction(n - 2, n) ** (n - 3)
    if pi_completion != pi_closed:
        raise AssertionError((pi_completion, pi_closed))
    signed_cell_sum = 2 * delta / pi_closed

    return {
        "k": k,
        "n": n,
        "source_A_atoms": len(law_a),
        "source_B_atoms": len(law_b),
        "distinct_intermediates": len(states),
        "run_profiles": {str(key): value for key, value in sorted(run_profiles.items())},
        "literal_equals_decorated_for_every_intermediate": True,
        "formal_affine_identity_for_every_intermediate": True,
        "J0_measures_identical": True,
        "channel_masses_exact": [qstr(x) for x in alphas],
        "J0_and_J1_kind_transfer_zero": True,
        "eta_triangle_exact": qstr(eta_t),
        "eta_double_exact": qstr(-eta_t),
        "event_delta_exact": qstr(delta),
        "channel_event_deltas_exact": {str(j): qstr(x) for j, x in channel_deltas.items()},
        "pi_y_exact": qstr(pi_closed),
        "signed_cell_sum_exact": qstr(signed_cell_sum),
        "eta_B_formal_coefficients_E0_E1_E2": [qstr(x) for x in eta_b],
        "reduction_identity_formal_exact": True,
        "runtime_seconds": time.monotonic() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--frozen-m174", type=Path)
    args = parser.parse_args()
    rows = [analyze(k) for k in (3, 5)]
    frozen_matches = []
    if args.frozen_m174:
        frozen = json.loads(args.frozen_m174.read_text())
        by_k = {row["k"]: row for row in frozen["results"]}
        for row in rows:
            expected = by_k[row["k"]]
            if row["event_delta_exact"] != expected["event_delta_exact"]:
                raise AssertionError((row["k"], row["event_delta_exact"], expected["event_delta_exact"]))
            if row["signed_cell_sum_exact"] != expected["signed_cell_sum_exact"]:
                raise AssertionError((row["k"], row["signed_cell_sum_exact"], expected["signed_cell_sum_exact"]))
            frozen_matches.append({"k": row["k"], "exact_match_after_cleanroom_computation": True})
    payload = {
        "status": "fresh exact finite audit; no asymptotic inference",
        "scope": "M174 PCS reduction at k=3,5 only",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": "cleanroom_pcs_audit.py --output cleanroom_results.json --frozen-m174 <frozen pcs_channel_exact.json>",
        "frozen_comparison": frozen_matches,
        "results": rows,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(rows, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
