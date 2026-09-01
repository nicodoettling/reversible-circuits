#!/usr/bin/env python3
"""Clean-room exact audit for M182.

This script implements the literal permutation/completion-count definitions.
It does not import M180 code or data and is intentionally capped at k=3,5.
All asserted identities are rational or formal-polynomial equalities.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import sys
from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


Poly = tuple[Fraction, Fraction, Fraction]  # coefficients of 1,E,E^2


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return pq, so (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def identity(n: int) -> tuple[int, ...]:
    return tuple(range(n))


def transposition(n: int, a: int, b: int) -> tuple[int, ...]:
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def cycle_perm(n: int, vertices: tuple[int, ...]) -> tuple[int, ...]:
    p = list(range(n))
    for a, b in zip(vertices, vertices[1:] + vertices[:1]):
        p[a] = b
    return tuple(p)


def cycles(p: tuple[int, ...]) -> list[tuple[int, ...]]:
    seen: set[int] = set()
    out: list[tuple[int, ...]] = []
    for x in range(len(p)):
        if x in seen:
            continue
        c: list[int] = []
        y = x
        while y not in seen:
            seen.add(y)
            c.append(y)
            y = p[y]
        out.append(tuple(c))
    return out


def tau(d: int) -> Fraction:
    if d < 1:
        raise ValueError("tau is used only at positive indices")
    return Fraction(d ** (d - 1), math.factorial(d))


def factorization_count(r: int, q: tuple[int, ...]) -> Fraction:
    cs = cycles(q)
    if len(q) - len(cs) != r:
        return Fraction(0)
    ans = Fraction(math.factorial(r))
    for c in cs:
        ans *= tau(len(c))
    return ans


def residual(g: tuple[int, ...], h: tuple[int, ...]) -> tuple[int, ...]:
    return compose(inverse(g), h)


def mul3(g: tuple[int, ...], s: tuple[int, ...], h: tuple[int, ...]) -> tuple[int, ...]:
    return residual(compose(g, s), h)


def boundary_edge(a: int, b: int, n: int) -> bool:
    return (a - b) % n in (1, n - 1)


def build_pair_products(n: int) -> dict[tuple[int, ...], tuple[int, int]]:
    """Map nonidentity pair products to (ordered lift count, boundary sum)."""
    ts: list[tuple[tuple[int, ...], tuple[int, int]]] = []
    for a in range(n):
        for b in range(a + 1, n):
            ts.append((transposition(n, a, b), (a, b)))
    counts: defaultdict[tuple[int, ...], list[int]] = defaultdict(lambda: [0, 0])
    for p, ep in ts:
        for q, eq in ts:
            if p == q:
                continue
            s = compose(p, q)
            counts[s][0] += 1
            counts[s][1] += int(boundary_edge(*ep, n)) + int(boundary_edge(*eq, n))
    out = {s: (v[0], v[1]) for s, v in counts.items()}
    for s, (a, _) in out.items():
        typ = sorted(len(c) for c in cycles(s) if len(c) > 1)
        expected = 3 if typ == [3] else 2 if typ == [2, 2] else None
        assert expected is not None and a == expected
    return out


def source_row(
    g: tuple[int, ...],
    h: tuple[int, ...],
    products: dict[tuple[int, ...], tuple[int, int]],
) -> dict[tuple[int, ...], Fraction]:
    n = len(g)
    normalizer = factorization_count(n - 3, residual(g, h))
    assert normalizer > 0
    row: dict[tuple[int, ...], Fraction] = {}
    for s, (a_s, _) in products.items():
        completion = factorization_count(n - 5, mul3(g, s, h))
        if completion:
            row[s] = Fraction(a_s) * completion / normalizer
    assert sum(row.values(), Fraction()) == 1
    return row


def run_lengths(component: tuple[int, ...], n: int) -> tuple[int, ...]:
    support = set(component)
    starts = sorted(x for x in support if (x - 1) % n not in support)
    assert starts  # every residual component here is proper
    lengths: list[int] = []
    for start in starts:
        d = 0
        x = start
        while x in support:
            d += 1
            x = (x + 1) % n
        lengths.append(d)
    assert sum(lengths) == len(component)
    return tuple(lengths)


def components_of(s: tuple[int, ...], h: tuple[int, ...]) -> list[dict[str, object]]:
    n = len(s)
    cs = cycles(residual(s, h))
    assert len(cs) == 3
    out: list[dict[str, object]] = []
    for c in cs:
        runs = run_lengths(c, n)
        assert len(runs) in (1, 2)
        out.append({"d": len(c), "run_type": len(runs), "runs": runs})
    return out


def kind(s: tuple[int, ...]) -> str:
    typ = sorted(len(c) for c in cycles(s) if len(c) > 1)
    if typ == [3]:
        return "T"
    if typ == [2, 2]:
        return "D"
    raise AssertionError(typ)


def decoration(component: dict[str, object]) -> dict[str, object]:
    d = int(component["d"])
    r = int(component["run_type"])
    runs = tuple(int(x) for x in component["runs"])
    if r == 1:
        U = Fraction(0) if d == 1 else Fraction(d - 1) * tau(d - 1) / tau(d)
        V = Fraction(0) if d < 3 else Fraction((d - 2) * (d - 3)) * tau(d - 2) / tau(d)
        return {"d": d, "r": r, "I": 0, "eps": Fraction(1, 2), "c": 2, "U": U, "V": V}
    assert len(runs) == 2 and all(x >= 1 for x in runs)
    I = sum(x == 1 for x in runs)
    U = Fraction(d - 2) * tau(d - 1) / tau(d)
    numerator = (d - 2) * (d - 3) - 2 * sum(max(x - 2, 0) for x in runs)
    V = Fraction(0) if d == 2 else Fraction(numerator) * tau(d - 2) / tau(d)
    assert numerator == d * d - 7 * d + 14 - 2 * I
    return {"d": d, "r": r, "I": I, "eps": Fraction(-1, 2), "c": 4, "U": U, "V": V}


def pconst(x: Fraction | int) -> Poly:
    return (Fraction(x), Fraction(), Fraction())


def padd(a: Poly, b: Poly) -> Poly:
    return tuple(a[i] + b[i] for i in range(3))  # type: ignore[return-value]


def pscale(c: Fraction | int, a: Poly) -> Poly:
    return tuple(Fraction(c) * x for x in a)  # type: ignore[return-value]


def pmul(a: Poly, b: Poly) -> Poly:
    out = [Fraction(), Fraction(), Fraction()]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= 2:
                out[i + j] += x * y
            else:
                assert x * y == 0
    return tuple(out)  # type: ignore[return-value]


def psum(xs: list[Poly]) -> Poly:
    ans = pconst(0)
    for x in xs:
        ans = padd(ans, x)
    return ans


def state_formulas(s: tuple[int, ...], h: tuple[int, ...]) -> dict[str, object]:
    n = len(s)
    typ = kind(s)
    dec = [decoration(c) for c in components_of(s, h)]
    assert ([int(x["r"]) for x in dec].count(2) == (typ == "D"))
    assert sum(int(x["d"]) for x in dec) == n
    L = 0 if typ == "T" else -2
    I_D = sum(int(x["I"]) for x in dec if int(x["r"]) == 2)

    us: list[Poly] = []
    vs: list[Poly] = []
    for x in dec:
        d, eps, c, U, V = int(x["d"]), Fraction(x["eps"]), int(x["c"]), Fraction(x["U"]), Fraction(x["V"])
        us.append((Fraction(-d) - eps, U, Fraction()))
        vs.append((Fraction(-d * d + c * d), Fraction(), V))

    B = pconst(-sum(int(x["c"]) * int(x["d"]) for x in dec) - L * n)
    B = padd(B, psum(vs))
    for i in range(3):
        for j in range(i + 1, 3):
            di, dj = int(dec[i]["d"]), int(dec[j]["d"])
            xi = padd(pconst(Fraction(dec[i]["eps"])), us[i])
            xj = padd(pconst(Fraction(dec[j]["eps"])), us[j])
            bracket = padd(pscale(di, xj), pscale(dj, xi))
            bracket = padd(bracket, pmul(xi, xj))
            B = padd(B, pscale(2, bracket))

    Q = psum(us)
    ws: list[Poly] = []
    for x, v in zip(dec, vs):
        if int(x["r"]) == 1:
            ws.append(padd(v, pconst(Fraction(5, 3))))
        else:
            ws.append(padd(v, pconst(Fraction(-1, 3) + 2 * int(x["I"]))))
    R = psum(ws)
    R = padd(R, pscale(-2, psum([pscale(int(x["d"]), u) for x, u in zip(dec, us)])))
    for i in range(3):
        for j in range(i + 1, 3):
            cross = padd(pscale(Fraction(dec[i]["eps"]), us[j]), pscale(Fraction(dec[j]["eps"]), us[i]))
            cross = padd(cross, pmul(us[i], us[j]))
            R = padd(R, pscale(2, cross))
    assert B == padd(padd(pscale(2 * n, Q), pconst(Fraction(-7, 2) - 2 * I_D)), R)

    sumV = sum((Fraction(x["V"]) for x in dec), Fraction())
    sumUU = sum((Fraction(dec[i]["U"]) * Fraction(dec[j]["U"]) for i in range(3) for j in range(i + 1, 3)), Fraction())
    left = (Fraction(), Fraction(), sumV + 2 * sumUU)
    assert left == padd(pconst(n * n + L * n), B)
    H = sum((Fraction(x["U"]) for x in dec), Fraction())
    return {"kind": typ, "components": dec, "I_D": I_D, "B": B, "Q": Q, "R": R, "H": H}


def direct_kw(
    s: tuple[int, ...],
    h: tuple[int, ...],
    products: dict[tuple[int, ...], tuple[int, int]],
) -> Fraction:
    n = len(s)
    normalizer = factorization_count(n - 3, residual(s, h))
    assert normalizer > 0
    total = Fraction()
    for t, (_, boundary_lift_sum) in products.items():
        if not boundary_lift_sum:
            continue
        total += boundary_lift_sum * factorization_count(n - 5, mul3(s, t, h))
    return total / normalizer


def beta_ratio(g: tuple[int, ...], s: tuple[int, ...], h: tuple[int, ...]) -> Fraction:
    before = residual(g, h)
    after = mul3(g, s, h)
    n = len(g)
    if n - len(cycles(after)) != n - 5:
        return Fraction()
    num = Fraction(1)
    den = Fraction(1)
    for c in cycles(after):
        num *= tau(len(c))
    for c in cycles(before):
        den *= tau(len(c))
    return num / den


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def poly_json(p: Poly) -> list[str]:
    return [fstr(x) for x in p]


def decimal_fraction(x: Fraction) -> Decimal:
    return Decimal(x.numerator) / Decimal(x.denominator)


def eval_poly(p: Poly, E: Decimal) -> Decimal:
    return decimal_fraction(p[0]) + decimal_fraction(p[1]) * E + decimal_fraction(p[2]) * E * E


def audit_k(k: int) -> dict[str, object]:
    assert k in (3, 5)
    n = 3 * k
    h = cycle_perm(n, tuple(range(n)))
    A = cycle_perm(n, (0, k, 2 * k))
    B = compose(transposition(n, 0, 1), transposition(n, k, 2 * k))
    products = build_pair_products(n)
    PA = source_row(A, h, products)
    PB = source_row(B, h, products)
    support = sorted(set(PA) | set(PB))
    eta = {s: PB.get(s, Fraction()) - PA.get(s, Fraction()) for s in support}
    assert sum(eta.values(), Fraction()) == 0
    Rn = (n - 3) * (n - 4)

    formulas: dict[tuple[int, ...], dict[str, object]] = {}
    raw_normalization_ok = True
    for s in support:
        formulas[s] = state_formulas(s, h)
        delta = beta_ratio(B, s, h) - beta_ratio(A, s, h)
        a_s = products[s][0]
        raw_normalization_ok &= eta[s] == Fraction(a_s, Rn) * delta
    assert raw_normalization_ok

    t = sum((eta[s] for s in support if formulas[s]["kind"] == "T"), Fraction())
    t_formula = Fraction(12 * (k - 1), 3 * k * (3 * k - 4) * (2 * k - 1))
    assert t == t_formula

    M1: defaultdict[int, Fraction] = defaultdict(Fraction)
    M2: defaultdict[int, Fraction] = defaultdict(Fraction)
    for s, weight in eta.items():
        for c in formulas[s]["components"]:  # type: ignore[union-attr]
            target = M1 if int(c["r"]) == 1 else M2
            target[int(c["d"])] += weight
    assert sum(M1.values(), Fraction()) == t
    assert sum(M2.values(), Fraction()) == -t
    assert sum((d * (M1[d] + M2[d]) for d in set(M1) | set(M2)), Fraction()) == 0
    component_tv = sum((abs(x) for x in M1.values()), Fraction()) + sum((abs(x) for x in M2.values()), Fraction())
    assert component_tv <= 6

    etaQ = pconst(0)
    etaB = pconst(0)
    etaR = pconst(0)
    etaH = Fraction()
    etaI = Fraction()
    for s, weight in eta.items():
        etaQ = padd(etaQ, pscale(weight, formulas[s]["Q"]))  # type: ignore[arg-type]
        etaB = padd(etaB, pscale(weight, formulas[s]["B"]))  # type: ignore[arg-type]
        etaR = padd(etaR, pscale(weight, formulas[s]["R"]))  # type: ignore[arg-type]
        etaH += weight * Fraction(formulas[s]["H"])
        etaI += weight * int(formulas[s]["I_D"])
    etaQ_from_M = pconst(0)
    for d in set(M1) | set(M2):
        if M1[d]:
            U1 = Fraction(0) if d == 1 else Fraction(d - 1) * tau(d - 1) / tau(d)
            etaQ_from_M = padd(etaQ_from_M, pscale(M1[d], (Fraction(-d) - Fraction(1, 2), U1, Fraction())))
        if M2[d]:
            U2 = Fraction(d - 2) * tau(d - 1) / tau(d)
            etaQ_from_M = padd(etaQ_from_M, pscale(M2[d], (Fraction(-d) + Fraction(1, 2), U2, Fraction())))
    assert etaQ == etaQ_from_M
    assert etaQ == (Fraction(-t), etaH, Fraction())
    assert etaB == padd(padd(pscale(2 * n, etaQ), pconst(-2 * etaI)), etaR)

    kw_values: dict[tuple[int, ...], Fraction] = {}
    for s in support:
        kw = direct_kw(s, h, products)
        assert kw == Fraction(2, n - 3) * Fraction(formulas[s]["H"])
        kw_values[s] = kw
    delta_W = sum((eta[s] * kw_values[s] for s in support), Fraction())
    assert etaH == Fraction(n - 3, 2) * delta_W

    large = sorted(d for d in set(M1) | set(M2) if d > Fraction(n, 2))
    large_mass_tv = sum((abs(M1[d]) + abs(M2[d]) for d in large), Fraction())
    assert large_mass_tv <= 6

    E = Decimal(1).exp()
    return {
        "k": k,
        "n": n,
        "candidate_pair_products": len(products),
        "source_support_union": len(support),
        "source_support_A": len(PA),
        "source_support_B": len(PB),
        "source_normalization": {"A": fstr(sum(PA.values(), Fraction())), "B": fstr(sum(PB.values(), Fraction()))},
        "raw_delta_normalization_exact": raw_normalization_ok,
        "eta_triangle": fstr(t),
        "eta_triangle_formula": fstr(t_formula),
        "component_moments": {
            "sum_M1": fstr(sum(M1.values(), Fraction())),
            "sum_M2": fstr(sum(M2.values(), Fraction())),
            "size_sum": fstr(sum((d * (M1[d] + M2[d]) for d in set(M1) | set(M2)), Fraction())),
            "component_total_variation": fstr(component_tv),
        },
        "eta_Q_polynomial_1_E_E2": poly_json(etaQ),
        "eta_B_polynomial_1_E_E2": poly_json(etaB),
        "eta_R_polynomial_1_E_E2": poly_json(etaR),
        "eta_I_D": fstr(etaI),
        "eta_H": fstr(etaH),
        "delta_W": fstr(delta_W),
        "KW_identity_states_checked": len(support),
        "large_component_sizes": large,
        "large_component_coefficient_tv": fstr(large_mass_tv),
        "finite_calibration": {
            "n_eta_H": str(Decimal(n) * decimal_fraction(etaH)),
            "n_eta_Q_at_e": str(Decimal(n) * eval_poly(etaQ, E)),
            "n2_delta_W": str(Decimal(n * n) * decimal_fraction(delta_W)),
            "eta_B_at_e": str(eval_poly(etaB, E)),
        },
    }


def ratio_series_check() -> dict[str, object]:
    # Coefficient of x^r, x=1/d, in 2+log(1-x)+(1/x-3)log(1-2x).
    def second_log_coefficient(r: int) -> Fraction:
        return -Fraction(2 ** (r + 1), r + 1) + Fraction(3 * 2**r, r) - Fraction(1, r)

    # Coefficient in 1+(1/x-2)log(1-x).
    def first_log_coefficient(r: int) -> Fraction:
        return -Fraction(1, r + 1) + Fraction(2, r)

    a1, a2 = first_log_coefficient(1), first_log_coefficient(2)
    b1, b2 = second_log_coefficient(1), second_log_coefficient(2)
    first_exp_second = a2 + a1 * a1 / 2
    second_exp_second = b2 + b1 * b1 / 2
    assert (a1, a2, first_exp_second) == (Fraction(3, 2), Fraction(2, 3), Fraction(43, 24))
    assert (b1, b2, second_exp_second) == (Fraction(3), Fraction(17, 6), Fraction(22, 3))
    return {
        "first_ratio_log_coefficients": [fstr(a1), fstr(a2)],
        "first_ratio_exp_second_coefficient": fstr(first_exp_second),
        "second_ratio_log_coefficients": [fstr(b1), fstr(b2)],
        "second_ratio_exp_second_coefficient": fstr(second_exp_second),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    getcontext().prec = 60
    result = {
        "mission": "M182",
        "method": "clean-room literal permutations, exact Fraction arithmetic, formal E polynomials",
        "composition": "(pq)(x)=p(q(x)); displayed products left-to-right",
        "parameters": {"k": [3, 5], "seed": None},
        "ratio_series": ratio_series_check(),
        "cases": [audit_k(3), audit_k(5)],
        "status": "all exact assertions passed",
        "python": platform.python_version(),
        "standard_library_only": True,
    }
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"], "output": args.output, "python": result["python"]}, sort_keys=True))


if __name__ == "__main__":
    main()
