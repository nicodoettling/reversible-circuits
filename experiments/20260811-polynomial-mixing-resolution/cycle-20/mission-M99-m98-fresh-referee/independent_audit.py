#!/usr/bin/env python3
"""Fresh exact referee audit of the frozen M98 counterfamily.

This file imports no M98 or predecessor Python module.  It reconstructs the
right-heavy defect twice: as an ordinary rational recurrence and directly as
a polynomial after multiplication by ``prod_(i=1)^s (K+i)^2``.  The latter
construction establishes the degree bound without polynomial fitting.
"""

from __future__ import annotations

import functools
import hashlib
import json
import math
import platform
import time
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
RUN_ROOT = HERE.parents[1]
M98 = RUN_ROOT / "cycle-19" / "mission-M98-reset-defect-sign"
EXPECTED_REPORT_SHA = "fcf92cf8222aec8f4675b56fc86fda0cb676a37aac79320571eb7a8856e34476"
EXPECTED_MANIFEST_SHA = "2a8772686dfcfdc4d16103c4ff2b32ff5a0f610da5988184eb7410e69f81521e"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rec(value: Fraction) -> dict[str, object]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


def from_rec(value: dict[str, object]) -> Fraction:
    return Fraction(int(value["numerator"]), int(value["denominator"]))


@functools.lru_cache(maxsize=None)
def w(a: int) -> Fraction:
    if a < 1:
        raise ValueError(a)
    return Fraction(a ** (a - 1), math.factorial(a))


@functools.lru_cache(maxsize=None)
def cayley(total: int, parts: int) -> Fraction:
    """Sum of product w(part) over positive ordered compositions."""
    if parts == 0:
        return Fraction(int(total == 0))
    if not 1 <= parts <= total:
        return Fraction(0)
    return Fraction(
        parts * total ** (total - parts),
        total * math.factorial(total - parts),
    )


@functools.lru_cache(maxsize=None)
def compositions(total: int) -> tuple[tuple[int, ...], ...]:
    if total == 0:
        return ((),)
    rows: list[tuple[int, ...]] = []
    for first in range(1, total + 1):
        for tail in compositions(total - first):
            rows.append((first,) + tail)
    return tuple(rows)


def rho_comp(comp: tuple[int, ...]) -> Fraction:
    answer = Fraction(1, math.factorial(len(comp)) * w(sum(comp) + 1))
    for part in comp:
        answer *= w(part)
    return answer


def q_split(s: int, B: int) -> Fraction:
    return w(s + 1 - B) * w(B) / w(s + 1)


def safe_comb_ratio(n1: int, k1: int, n2: int, k2: int) -> Fraction:
    if not (0 <= k1 <= n1 and 0 <= k2 <= n2):
        return Fraction(0)
    return Fraction(math.comb(n1, k1), math.comb(n2, k2))


def contextual(k: int, t: int, K: int, R: int, B: int) -> Fraction:
    if t < B:
        return Fraction(0)
    if t == B:
        return K * safe_comb_ratio(
            k + K - R - 2,
            K - R - 1,
            k + K - 1,
            K - 1,
        )
    return q_split(t - 1, B) * (
        1 - safe_comb_ratio(K, R + 1, K + k, R + 1)
    )


def attachment(K: int, R: int, k: int, j: int) -> Fraction:
    return Fraction(
        math.comb(R + j, j)
        * math.comb(K - R - 1 + k - j, k - j),
        math.comb(K + k, k),
    )


def product_linear_value(K: int, lo: int, hi: int) -> int:
    answer = 1
    for i in range(lo, hi + 1):
        answer *= K + i
    return answer


def right_heavy_contextual(k: int, t: int, K: int, B: int) -> Fraction:
    if t < B:
        return Fraction(0)
    if t == B:
        return Fraction(math.factorial(k), product_linear_value(K, 1, k - 1))
    return q_split(t - 1, B) * (
        1 - Fraction(math.factorial(k), product_linear_value(K, 1, k))
    )


@functools.lru_cache(maxsize=None)
def groups(s: int) -> tuple[tuple[int, int, Fraction], ...]:
    rows: list[tuple[int, int, Fraction]] = []
    total = Fraction(0)
    for k in range(1, s + 1):
        for t in range(1, s + 1):
            mass = w(t) * cayley(s - t, k - 1) / (
                math.factorial(k) * w(s + 1)
            )
            if mass:
                rows.append((k, t, mass))
                total += mass
    if total != 1:
        raise AssertionError(("root normalization", s, total))
    return tuple(rows)


@functools.lru_cache(maxsize=None)
def basin_L(A: int, ell: int) -> Fraction:
    return sum(
        (cayley(A, p) / math.factorial(p + ell) for p in range(1, A + 1)),
        Fraction(),
    )


def basin_L_integral(A: int, ell: int) -> Fraction:
    """Exact expansion of the beta integral in M98 equation (2.5)."""
    return sum(
        (
            Fraction(math.comb(A - 1, r) * A ** (A - 1 - r), math.factorial(A))
            * Fraction(math.factorial(r + 1), math.factorial(r + ell + 1))
            for r in range(A)
        ),
        Fraction(),
    )


def tail_rows(s: int, A: int, b: int, ell: int):
    """Group endpoint suffixes by their last part."""
    after_b_parts = ell - 1
    after_b_total = s - A - b
    if after_b_parts == 0:
        if after_b_total == 0:
            yield b, w(b)
        return
    for last in range(1, after_b_total + 1):
        middle = cayley(after_b_total - last, after_b_parts - 1)
        if middle:
            yield last, w(b) * middle * w(last)


@functools.lru_cache(maxsize=None)
def reset_grouped(
    s: int, K: int, R: int, B: int, weighted: bool
) -> Fraction:
    q_parent = q_split(s, B)
    answer = Fraction(0)
    for ell in range(1, s):
        for A in range(1, s + 1):
            for b in range(1, s - A - (ell - 1) + 1):
                child_s = A + b - 1
                if child_s < 2:
                    continue
                for last, suffix_weight in tail_rows(s, A, b, ell):
                    scalar = sum(
                        (
                            cayley(A, p)
                            * (contextual(p + ell, last, K, R, B) - q_parent)
                            / math.factorial(p + ell)
                            for p in range(1, A + 1)
                        ),
                        Fraction(),
                    )
                    term = (
                        suffix_weight
                        * math.factorial(ell)
                        * scalar
                        * scalar
                        / (w(A) * w(s + 1))
                    )
                    if weighted:
                        term *= 1 - q_split(child_s, b)
                    answer += term
    return answer


def reset_literal(x: tuple[int, int, int, int], weighted: bool) -> Fraction:
    """Literal endpoint and literal prefix-refinement calculation."""
    s, K, R, B = x
    q_parent = q_split(s, B)
    answer = Fraction(0)
    for endpoint in compositions(s):
        if len(endpoint) < 2:
            continue
        A, b = endpoint[:2]
        child_s = A + b - 1
        if child_s < 2:
            continue
        suffix = endpoint[1:]
        theta = Fraction(0)
        for prefix in compositions(A):
            source = prefix + suffix
            theta += rho_comp(source) * (
                contextual(len(source), source[-1], K, R, B) - q_parent
            )
        qg = rho_comp(endpoint) * len(endpoint)
        term = theta * theta / qg
        if weighted:
            term *= 1 - q_split(child_s, b)
        answer += term
    return answer


def U(x: tuple[int, int, int, int]) -> Fraction:
    s, K, R, B = x
    q = q_split(s, B)
    return q * (1 - q) * Fraction(K, R + 1)


@functools.lru_cache(maxsize=None)
def children(
    x: tuple[int, int, int, int]
) -> tuple[tuple[Fraction, tuple[int, int, int, int]], ...]:
    s, K, R, B = x
    parent_phase = s + K - R
    rows: list[tuple[Fraction, tuple[int, int, int, int]]] = []
    for k, t, root_mass in groups(s):
        if t <= B or t - 1 < 2:
            continue
        for j in range(1, k + 1):
            p = attachment(K, R, k, j)
            if not p:
                continue
            child = (t - 1, K + k, R + j, B)
            if child[0] + child[1] - child[2] >= parent_phase:
                raise AssertionError(("phase", x, child))
            if not (child[1] > child[2] >= 1):
                raise AssertionError(("reachable closure", x, child))
            rows.append((root_mass * p, child))
    return tuple(rows)


def deep_U(x: tuple[int, int, int, int]) -> Fraction:
    return sum((mass * U(child) for mass, child in children(x)), Fraction())


@functools.lru_cache(maxsize=None)
def defect(x: tuple[int, int, int, int]) -> Fraction:
    return U(x) - reset_grouped(*x, True) - deep_U(x)


@functools.lru_cache(maxsize=None)
def resolvent(x: tuple[int, int, int, int], weighted: bool) -> Fraction:
    if x[0] <= 1:
        return Fraction(0)
    return reset_grouped(*x, weighted) + sum(
        (mass * resolvent(child, weighted) for mass, child in children(x)),
        Fraction(),
    )


# Polynomials in K, represented by low-to-high tuples of Fractions.
Poly = tuple[Fraction, ...]


def ptrim(a: list[Fraction] | tuple[Fraction, ...]) -> Poly:
    values = list(a)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values or [Fraction(0)])


def padd(a: Poly, b: Poly) -> Poly:
    n = max(len(a), len(b))
    out = [Fraction(0) for _ in range(n)]
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return ptrim(out)


def pneg(a: Poly) -> Poly:
    return tuple(-value for value in a)


def psub(a: Poly, b: Poly) -> Poly:
    return padd(a, pneg(b))


def pscale(a: Poly, scalar: Fraction) -> Poly:
    return ptrim([scalar * value for value in a])


def pmul(a: Poly, b: Poly) -> Poly:
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return ptrim(out)


def plinear(offset: int) -> Poly:
    return (Fraction(offset), Fraction(1))


def pprod(factors) -> Poly:
    answer: Poly = (Fraction(1),)
    for factor in factors:
        answer = pmul(answer, factor)
    return answer


def peval(poly: Poly, K: int) -> Fraction:
    answer = Fraction(0)
    for coefficient in reversed(poly):
        answer = answer * K + coefficient
    return answer


def right_heavy_H_numerator(
    s: int, B: int, k: int, t: int, D: Poly
) -> Poly:
    """N such that H_(K,K-1)(k,t)=N(K)/D(K)."""
    if t < B:
        return (Fraction(0),)
    if t == B:
        complement = pprod(plinear(i) for i in range(k, s + 1))
        return pscale(complement, Fraction(math.factorial(k)))
    complement = pprod(plinear(i) for i in range(k + 1, s + 1))
    return pscale(
        psub(D, pscale(complement, Fraction(math.factorial(k)))),
        q_split(t - 1, B),
    )


def cleared_deep_multiplier(s: int, k: int, j: int) -> Poly:
    """D(K)^2 nu(j)(K+k)/(K+j), for right-heavy nu."""
    numerator = pprod(plinear(r) for r in range(0, j))
    numerator = pmul(numerator, plinear(k))
    complement: Poly = (Fraction(1),)
    for i in range(1, s + 1):
        exponent = 2
        if i <= k:
            exponent -= 1
        if i == j:
            exponent -= 1
        for _ in range(exponent):
            complement = pmul(complement, plinear(i))
    return pscale(
        pmul(numerator, complement),
        Fraction(math.factorial(k), math.factorial(j)),
    )


def cleared_defect_polynomial(s: int, B: int) -> dict[str, Poly]:
    """Construct D^2(U-A-QU) directly in Q[K]."""
    D = pprod(plinear(i) for i in range(1, s + 1))
    D2 = pmul(D, D)
    q_parent = q_split(s, B)
    u_poly = pscale(D2, q_parent * (1 - q_parent))

    reset_poly: Poly = (Fraction(0),)
    for ell in range(1, s):
        for A in range(1, s + 1):
            for b in range(1, s - A - (ell - 1) + 1):
                child_s = A + b - 1
                if child_s < 2:
                    continue
                for last, suffix_weight in tail_rows(s, A, b, ell):
                    scalar_num: Poly = (Fraction(0),)
                    for p in range(1, A + 1):
                        h_num = right_heavy_H_numerator(
                            s, B, p + ell, last, D
                        )
                        centered_num = psub(h_num, pscale(D, q_parent))
                        scalar_num = padd(
                            scalar_num,
                            pscale(
                                centered_num,
                                cayley(A, p) / math.factorial(p + ell),
                            ),
                        )
                    coefficient = (
                        suffix_weight
                        * math.factorial(ell)
                        / (w(A) * w(s + 1))
                        * (1 - q_split(child_s, b))
                    )
                    reset_poly = padd(
                        reset_poly,
                        pscale(pmul(scalar_num, scalar_num), coefficient),
                    )

    deep_poly: Poly = (Fraction(0),)
    for k, t, root_mass in groups(s):
        if t <= B or t - 1 < 2:
            continue
        q_child = q_split(t - 1, B)
        reward = q_child * (1 - q_child)
        for j in range(1, k + 1):
            deep_poly = padd(
                deep_poly,
                pscale(
                    cleared_deep_multiplier(s, k, j),
                    root_mass * reward,
                ),
            )
    return {
        "D": D,
        "D2": D2,
        "U_cleared": u_poly,
        "A_cleared": reset_poly,
        "QU_cleared": deep_poly,
        "P": psub(psub(u_poly, reset_poly), deep_poly),
    }


def limiting_H(k: int, t: int, B: int) -> Fraction:
    if t < B:
        return Fraction(0)
    if t == B:
        return Fraction(int(k == 1))
    return q_split(t - 1, B)


def limiting_energy_coefficients(s: int) -> tuple[Fraction, ...]:
    answer = [Fraction(0) for _ in range(s + 1)]
    for ell in range(1, s):
        for A in range(1, s + 1):
            L = basin_L(A, ell)
            for b in range(1, s - A - (ell - 1) + 1):
                child_s = A + b - 1
                if child_s < 2:
                    continue
                for last, suffix_weight in tail_rows(s, A, b, ell):
                    answer[last] += (
                        suffix_weight
                        * math.factorial(ell)
                        * L
                        * L
                        / (w(A) * w(s + 1))
                        * (1 - q_split(child_s, b))
                    )
    return tuple(answer)


def limiting_energy_coefficients_literal(s: int) -> tuple[Fraction, ...]:
    answer = [Fraction(0) for _ in range(s + 1)]
    for endpoint in compositions(s):
        if len(endpoint) < 2:
            continue
        A, b = endpoint[:2]
        child_s = A + b - 1
        if child_s < 2:
            continue
        ell = len(endpoint) - 1
        suffix_weight = Fraction(1)
        for part in endpoint[1:]:
            suffix_weight *= w(part)
        answer[endpoint[-1]] += (
            suffix_weight
            * math.factorial(ell)
            * basin_L(A, ell) ** 2
            / (w(A) * w(s + 1))
            * (1 - q_split(child_s, b))
        )
    return tuple(answer)


def limiting_decomposition(s: int, B: int) -> dict[str, object]:
    q = q_split(s, B)
    masses = [Fraction(0) for _ in range(s + 1)]
    mean = Fraction(0)
    variance = Fraction(0)
    deep = Fraction(0)
    for k, t, mass in groups(s):
        h = limiting_H(k, t, B)
        masses[t] += mass
        mean += mass * h
        variance += mass * (h - q) ** 2
        if t > B:
            deep += mass * h * (1 - h)
    if mean != q:
        raise AssertionError(("limiting mean", mean, q))
    if q * (1 - q) - deep != variance:
        raise AssertionError("limiting variance identity")

    energy = limiting_energy_coefficients(s)
    reset = Fraction(0)
    rows = []
    for t in range(1, s + 1):
        # Every reset basin has p+ell>=2, so the t=B basin value is zero.
        h = Fraction(0) if t <= B else q_split(t - 1, B)
        square = (h - q) ** 2
        contribution = (masses[t] - energy[t]) * square
        reset += energy[t] * square
        rows.append({
            "last_part": t,
            "mass": rec(masses[t]),
            "energy_coefficient": rec(energy[t]),
            "mass_minus_energy": rec(masses[t] - energy[t]),
            "limiting_H": rec(h),
            "square": rec(square),
            "contribution": rec(contribution),
        })
    defect_limit = variance - reset
    return {
        "q": rec(q),
        "mean_H": rec(mean),
        "U_limit": rec(q * (1 - q)),
        "deep_U_limit": rec(deep),
        "variance": rec(variance),
        "reset_energy": rec(reset),
        "defect": rec(defect_limit),
        "rows": rows,
    }


def manifest_audit() -> dict[str, object]:
    rows = []
    for line in (M98 / "SHA256SUMS").read_text().splitlines():
        expected, name = line.split("  ", 1)
        observed = digest(M98 / name)
        rows.append({
            "file": name,
            "expected": expected,
            "observed": observed,
            "match": expected == observed,
        })
    return {
        "entry_count": len(rows),
        "all_match": all(row["match"] for row in rows),
        "rows": rows,
    }


def main() -> None:
    started = time.time()
    report_sha = digest(M98 / "report.md")
    manifest_sha = digest(M98 / "SHA256SUMS")
    manifest = manifest_audit()
    if report_sha != EXPECTED_REPORT_SHA or manifest_sha != EXPECTED_MANIFEST_SHA:
        raise AssertionError("assigned frozen hashes do not match")
    if not manifest["all_match"]:
        raise AssertionError("M98 manifest mismatch")
    frozen = json.loads((M98 / "defect_counterexample.json").read_text())

    # Literal composition checks for the Cayley grouping and root law.
    cayley_checks = 0
    root_group_checks = 0
    for total in range(1, 9):
        for parts in range(1, total + 1):
            literal = sum(
                (
                    math.prod((w(a) for a in comp), start=Fraction(1))
                    for comp in compositions(total)
                    if len(comp) == parts
                ),
                Fraction(),
            )
            if literal != cayley(total, parts):
                raise AssertionError(("Cayley grouping", total, parts))
            cayley_checks += 1
        literal_groups: dict[tuple[int, int], Fraction] = {}
        for comp in compositions(total):
            key = (len(comp), comp[-1])
            literal_groups[key] = literal_groups.get(key, Fraction()) + rho_comp(comp)
        if sum(literal_groups.values(), Fraction()) != 1:
            raise AssertionError(("literal root total", total))
        grouped = {(k, t): mass for k, t, mass in groups(total)}
        if literal_groups != grouped:
            raise AssertionError(("literal/grouped roots", total))
        root_group_checks += len(grouped)

    # Chu--Vandermonde normalization includes killed j=0; Q retains all j>=1.
    attachment_checks = 0
    for K in range(1, 9):
        for R in range(K):
            for k in range(1, 9):
                if sum((attachment(K, R, k, j) for j in range(k + 1)), Fraction()) != 1:
                    raise AssertionError(("attachment normalization", K, R, k))
                attachment_checks += 1
    for K in (709, 710):
        for k in range(1, 17):
            law = [attachment(K, K - 1, k, j) for j in range(k + 1)]
            closed = [Fraction(math.comb(K - 1 + j, j), math.comb(K + k, k)) for j in range(k + 1)]
            if law != closed or sum(law, Fraction()) != 1:
                raise AssertionError(("right-heavy attachment", K, k))
            attachment_checks += 1

    contextual_checks = 0
    s, B = 16, 4
    for K in (2, 709, 710, 1024):
        mean = Fraction(0)
        for k, t, mass in groups(s):
            left = contextual(k, t, K, K - 1, B)
            right = right_heavy_contextual(k, t, K, B)
            if left != right:
                raise AssertionError(("right-heavy contextual", K, k, t))
            mean += mass * left
            contextual_checks += 1
        if mean != q_split(s, B):
            raise AssertionError(("finite contextual mean", K, mean))

    # Basin coefficient: Cayley sum, literal compositions, and beta integral.
    basin_checks = 0
    for A in range(1, 17):
        for ell in range(1, 17 - A + 1):
            if basin_L(A, ell) != basin_L_integral(A, ell):
                raise AssertionError(("beta integral", A, ell))
            if A <= 8:
                literal = sum(
                    (
                        math.prod((w(a) for a in comp), start=Fraction(1))
                        / math.factorial(len(comp) + ell)
                        for comp in compositions(A)
                    ),
                    Fraction(),
                )
                if literal != basin_L(A, ell):
                    raise AssertionError(("literal basin L", A, ell))
            basin_checks += 1

    literal_reset_contexts = ((5, 2, 1, 2), (6, 1, 0, 3), (7, 5, 2, 3))
    literal_reset_checks = 0
    for x in literal_reset_contexts:
        for weighted in (False, True):
            if reset_literal(x, weighted) != reset_grouped(*x, weighted):
                raise AssertionError(("literal reset", x, weighted))
            literal_reset_checks += 1
    for small_s in range(2, 9):
        if limiting_energy_coefficients_literal(small_s) != limiting_energy_coefficients(small_s):
            raise AssertionError(("literal limiting energy", small_s))

    # Direct construction of the cleared polynomial, with no interpolation.
    polys = cleared_defect_polynomial(s, B)
    P = polys["P"]
    degree = len(P) - 1
    if degree > 2 * s:
        raise AssertionError(("polynomial degree", degree))
    limit = limiting_decomposition(s, B)
    limit_defect = from_rec(limit["defect"])
    if P[-1] != limit_defect:
        raise AssertionError(("leading coefficient/limit", P[-1], limit_defect))
    if limit_defect >= 0:
        raise AssertionError("limiting defect is not negative")
    if limit_defect != from_rec(frozen["limit"]["defect_limit"]):
        raise AssertionError("frozen limiting defect mismatch")

    frozen_limit = frozen["limit"]
    limit_field_pairs = (
        ("q", "q"),
        ("U_limit", "U_limit"),
        ("deep_U_limit", "deep_U_limit"),
        ("variance", "variance_limit"),
        ("reset_energy", "reset_energy_limit"),
        ("defect", "defect_limit"),
    )
    for ours, theirs in limit_field_pairs:
        if from_rec(limit[ours]) != from_rec(frozen_limit[theirs]):
            raise AssertionError(("limiting field mismatch", ours, theirs))
    if len(limit["rows"]) != len(frozen_limit["last_part_rows"]):
        raise AssertionError("limiting row count")
    for ours, theirs in zip(limit["rows"], frozen_limit["last_part_rows"]):
        if ours["last_part"] != theirs["last_part"]:
            raise AssertionError("limiting last-part ordering")
        row_fields = (
            ("mass", "mass"),
            ("energy_coefficient", "reset_energy_coefficient"),
            ("mass_minus_energy", "coefficient_mass_minus_energy"),
            ("limiting_H", "limiting_root_mean"),
            ("square", "square"),
            ("contribution", "defect_contribution"),
        )
        for ours_name, theirs_name in row_fields:
            if from_rec(ours[ours_name]) != from_rec(theirs[theirs_name]):
                raise AssertionError(("limiting row mismatch", ours["last_part"], ours_name))
    negative_limit_fibres = [
        row["last_part"]
        for row in limit["rows"]
        if from_rec(row["mass_minus_energy"]) < 0
    ]
    if negative_limit_fibres != [3, 4, 5, 6, 7, 8]:
        raise AssertionError(("negative limiting fibres", negative_limit_fibres))

    # Check every cleared component separately, including the deep multiplier.
    component_checks = 0
    for K in (709, 710):
        D_value = product_linear_value(K, 1, s)
        D2_value = D_value * D_value
        x = (s, K, K - 1, B)
        component_values = (
            (polys["U_cleared"], U(x)),
            (polys["A_cleared"], reset_grouped(*x, True)),
            (polys["QU_cleared"], deep_U(x)),
        )
        for poly, rational_value in component_values:
            if peval(poly, K) / D2_value != rational_value:
                raise AssertionError(("cleared component", K))
            component_checks += 1
        for k, t, _ in groups(s):
            h_num = right_heavy_H_numerator(s, B, k, t, polys["D"])
            if peval(h_num, K) / D_value != right_heavy_contextual(k, t, K, B):
                raise AssertionError(("cleared contextual numerator", K, k, t))
            component_checks += 1
        for k in range(1, s + 1):
            for j in range(1, k + 1):
                cleared = peval(cleared_deep_multiplier(s, k, j), K) / D2_value
                direct = attachment(K, K - 1, k, j) * Fraction(K + k, K + j)
                if cleared != direct:
                    raise AssertionError(("cleared deep multiplier", K, k, j))
                component_checks += 1

    finite_rows = []
    frozen_finite = {row["context"][1]: row for row in frozen["finite_rows"]}
    for K in (2, 32, 709, 710, 1024):
        D_value = product_linear_value(K, 1, s)
        polynomial_value = peval(P, K) / (D_value * D_value)
        recurrence_value = defect((s, K, K - 1, B))
        if polynomial_value != recurrence_value:
            raise AssertionError(("polynomial/recurrence", K))
        if recurrence_value != from_rec(frozen_finite[K]["defect"]):
            raise AssertionError(("frozen finite defect", K))
        finite_rows.append({
            "K": K,
            "defect": rec(recurrence_value),
            "sign": (recurrence_value > 0) - (recurrence_value < 0),
            "cleared_value": rec(peval(P, K)),
        })
    if finite_rows[2]["sign"] != 1 or finite_rows[3]["sign"] != -1:
        raise AssertionError("K=709/710 sign transition")

    values = [peval(P, 710 + n) for n in range(34)]
    newton = []
    current = values
    for order in range(34):
        newton.append(current[0])
        current = [current[i + 1] - current[i] for i in range(len(current) - 1)]
    if any(value >= 0 for value in newton[:33]) or newton[33] != 0:
        raise AssertionError("Newton tail certificate")
    frozen_newton = [from_rec(row["value"]) for row in frozen["integer_tail_certificate"]["newton_coefficients"]]
    if newton[:33] != frozen_newton:
        raise AssertionError("frozen Newton coefficients mismatch")

    # The exact fresh-to-witness transition has positive mass 1/K.
    reachability_rows = []
    for K in (710, 1024):
        parent = (K + 15, 1, 0, 4)
        root_composition = (1,) * (K - 2) + (17,)
        root_k = len(root_composition)
        rank = K - 1
        child = (root_composition[-1] - 1, 1 + root_k, rank, 4)
        attach_mass = attachment(1, 0, root_k, rank)
        if child != (16, K, K - 1, 4) or attach_mass != Fraction(1, K):
            raise AssertionError(("reachability", K, child, attach_mass))
        if sum(root_composition) != parent[0] or rho_comp(root_composition) <= 0:
            raise AssertionError(("positive root composition", K))
        reachability_rows.append({
            "K": K,
            "fresh_parent": list(parent),
            "root_part_count": root_k,
            "root_last_part": 17,
            "attachment_rank": rank,
            "attachment_probability": rec(attach_mass),
            "child": list(child),
            "positive_root_mass": True,
        })

    witness = (16, 710, 709, 4)
    weighted_value = resolvent(witness, True)
    unweighted_value = resolvent(witness, False)
    target = q_split(16, 4) * (1 - q_split(16, 4))
    frozen_full = frozen["surviving_full_resolvents_at_K710"]
    if weighted_value != from_rec(frozen_full["weighted_value"]):
        raise AssertionError("weighted full-resolvent mismatch")
    if unweighted_value != from_rec(frozen_full["unweighted_value"]):
        raise AssertionError("unweighted full-resolvent mismatch")
    if not (weighted_value < target and unweighted_value < target):
        raise AssertionError("full-resolvent survival")
    first_layer = sum((mass * defect(child) for mass, child in children(witness)), Fraction())
    local = defect(witness)
    frozen_two = frozen["nonfresh_two_level_compensation_at_K710"]
    if local != from_rec(frozen_two["r_U"]) or first_layer != from_rec(frozen_two["Q_r_U"]):
        raise AssertionError("two-layer compensation mismatch")

    payload = {
        "audit": "M99 fresh exact audit of frozen M98",
        "verdict": "ACCEPT with zero material numbered objections",
        "scope": (
            "auxiliary full nonlazy stationary-flow parking-degree projection; "
            "not the original lazy {3,4,5} heat-bath chain"
        ),
        "convention": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "arithmetic": "fractions.Fraction exact; seed=null",
        "python": platform.python_version(),
        "provenance": {
            "expected_report_sha256": EXPECTED_REPORT_SHA,
            "observed_report_sha256": report_sha,
            "expected_manifest_sha256": EXPECTED_MANIFEST_SHA,
            "observed_manifest_sha256": manifest_sha,
            "manifest": manifest,
        },
        "normalization_and_formula_checks": {
            "cayley_literal_checks": cayley_checks,
            "literal_root_group_checks": root_group_checks,
            "attachment_normalization_checks": attachment_checks,
            "contextual_right_heavy_checks": contextual_checks,
            "basin_sum_integral_checks": basin_checks,
            "literal_reset_checks": literal_reset_checks,
            "componentwise_cleared_checks": component_checks,
            "limiting_energy_literal_ranks": list(range(2, 9)),
            "attachment_note": "j=0,...,k sums to one; every live j=1,...,k is retained",
        },
        "direct_cleared_polynomial": {
            "construction": (
                "coefficient arithmetic in Q[K], using D=product_(i=1)^16(K+i); "
                "not interpolation"
            ),
            "degree": degree,
            "degree_bound": 32,
            "coefficient_count": len(P),
            "leading_coefficient": rec(P[-1]),
            "leading_coefficient_equals_limit": True,
            "coefficients_low_to_high": [rec(value) for value in P],
        },
        "finite_defects": finite_rows,
        "limiting_decomposition": limit,
        "negative_limiting_coefficient_fibres": negative_limit_fibres,
        "newton_tail": {
            "base_K": 710,
            "orders_0_through_32_all_negative": True,
            "order_33_zero": rec(newton[33]),
            "coefficients": [
                {"order": order, "value": rec(value)}
                for order, value in enumerate(newton[:33])
            ],
            "conclusion": "P(710+n)<0 for every integer n>=0",
        },
        "reachability": reachability_rows,
        "full_resolvent_at_K710": {
            "target_q_one_minus_q": rec(target),
            "weighted_value": rec(weighted_value),
            "weighted_ratio": rec(weighted_value / target),
            "weighted_survives": weighted_value < target,
            "unweighted_value": rec(unweighted_value),
            "unweighted_ratio": rec(unweighted_value / target),
            "unweighted_survives": unweighted_value < target,
            "local_defect": rec(local),
            "Q_local_defect": rec(first_layer),
            "two_level_block": rec(local + first_layer),
            "two_level_survives": local + first_layer > 0,
            "status": "exact finite calibration only",
        },
        "claim_status": {
            "nonfresh_one_step_sign": "refuted by an exact reachable infinite family",
            "fresh_two_level_sign": "unresolved",
            "global_two_layer_sign": "unresolved",
            "weighted_full_resolvent": "unresolved universally; survives K=710 exactly",
            "unweighted_full_resolvent": "unresolved universally; survives K=710 exactly",
            "auxiliary_gap": "unresolved",
            "original_heat_bath_gap": "unresolved",
            "terminal_A_or_B": "unresolved",
        },
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    output = HERE / "independent_audit.json"
    output.write_text(encoded)
    print(json.dumps({
        "output": str(output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "elapsed_seconds": time.time() - started,
        "degree": degree,
        "K709": finite_rows[2]["defect"],
        "K710": finite_rows[3]["defect"],
        "all_newton_negative": True,
        "weighted_ratio": float(weighted_value / target),
        "unweighted_ratio": float(unweighted_value / target),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
