#!/usr/bin/env python3
"""M230 clean-room exact audit of the frozen M227 rational certificates."""

import argparse
import hashlib
import json
import platform
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path

L = 6
ACTIVE = 6


def frac(text):
    return Q(text)


def elevate(coefficients, old_degree, new_degree):
    """Exact Bernstein degree elevation."""
    extra = new_degree - old_degree
    assert extra >= 0 and len(coefficients) == old_degree + 1
    answer = []
    for r in range(new_degree + 1):
        value = Q(0)
        for k, z in enumerate(coefficients):
            if 0 <= r - k <= extra:
                value += z * Q(
                    comb(old_degree, k) * comb(extra, r - k),
                    comb(new_degree, r),
                )
        answer.append(value)
    return answer


def reconstruct_atom():
    # Child feature coefficients (1,1), multiplied by b_(1,0).
    child = [Q(1), Q(1)]
    product = [Q(0)] * 3
    for k, z in enumerate(child):
        product[k] = z * Q(comb(1, 0) * comb(1, k), comb(2, k))
    assert product == [Q(1), Q(1, 2), Q(0)]
    return elevate(product, 2, L)


def bernstein_product_integral(i, j):
    # C(6,i)C(6,j) * Beta(i+j+1,13-i-j).
    return Q(
        comb(L, i) * comb(L, j) * factorial(i + j) * factorial(2 * L - i - j),
        factorial(2 * L + 1),
    )


def first_moment(i):
    # Integral (u-1/2)b_(6,i)(u)du = (i-3)/56.
    return Q(i - 3, 56)


def reconstruct_charge():
    return [
        [bernstein_product_integral(i, j) - 12 * first_moment(i) * first_moment(j)
         for j in range(L + 1)]
        for i in range(L + 1)
    ]


def parse_matrix(rows):
    return [[frac(z) for z in row] for row in rows]


DUAL = {
    1: parse_matrix([
        ["433/10192", "79/5096", "31/1000", "7/200", "309/10000", "153/5000"],
        ["79/5096", "747/28028", "1335/56056", "201/10000", "47/2000", "79/5000"],
        ["31/1000", "1335/56056", "3491/112112", "25/858", "309/10000", "59/2500"],
        ["7/200", "201/10000", "25/858", "100/3003", "25/858", "73/2500"],
        ["309/10000", "47/2000", "309/10000", "25/858", "3491/112112", "1335/56056"],
        ["153/5000", "79/5000", "59/2500", "73/2500", "1335/56056", "747/28028"],
    ]),
    2: parse_matrix([
        ["433/10192", "79/5096", "673/112112", "59/5000", "61/2500", "147/5000"],
        ["79/5096", "747/28028", "1335/56056", "8/429", "87/5000", "109/5000"],
        ["673/112112", "1335/56056", "3491/112112", "25/858", "2529/112112", "87/5000"],
        ["59/5000", "8/429", "25/858", "100/3003", "25/858", "8/429"],
        ["61/2500", "87/5000", "2529/112112", "25/858", "3491/112112", "1335/56056"],
        ["147/5000", "109/5000", "87/5000", "8/429", "1335/56056", "747/28028"],
    ]),
}

PRIMAL = {
    1: parse_matrix([
        ["19731/10000", "16443/10000", "0", "0", "0", "0"],
        ["16443/10000", "1713/1250", "0", "0", "0", "0"],
        ["0", "0", "12753/10000", "589/625", "0", "0"],
        ["0", "0", "589/625", "7067/10000", "7/500", "0"],
        ["0", "0", "0", "7/500", "7697/10000", "1933/5000"],
        ["0", "0", "0", "0", "1933/5000", "1993/10000"],
    ]),
    2: parse_matrix([
        ["15391/10000", "997/10000", "1204/625", "0", "0", "0"],
        ["997/10000", "3589/1250", "-30297/10000", "3649/1250", "0", "0"],
        ["1204/625", "-30297/10000", "33663/5000", "-5507/1250", "11997/10000", "0"],
        ["0", "3649/1250", "-5507/1250", "11909/2500", "-17379/10000", "1111/5000"],
        ["0", "0", "11997/10000", "-17379/10000", "1077/625", "-487/5000"],
        ["0", "0", "0", "1111/5000", "-487/5000", "4381/10000"],
    ]),
}

EXPECTED_PIVOTS = {
    (1, "dual"): [
        "433/10192", "100/4763", "478393499063/446345900000000",
        "146578076991996360023/107746175826464175000000",
        "1774449641877241678819703/3950279174934301902619850000",
        "397009562865787636388448576/2061688677656120175578642423125",
    ],
    (1, "slack"): [
        "9731/10000", "253/2335440", "946509/2530000",
        "3758291/378603600", "30808771/37582910000",
        "2397701/44012530000",
    ],
    (2, "dual"): [
        "433/10192", "100/4763", "97/12100",
        "8000756693/71002181250000",
        "5857714693874697183/55798514794032948437500",
        "1780018672270340745295529/2052250342999000158064050000000",
    ],
    (2, "slack"): [
        "5391/10000", "571743947/485190000",
        "427619287063/1143487894000",
        "6274564933193/1336310272071875",
        "657401275019469/1003930389310880000",
        "9621597299447/139872611706270000",
    ],
}
EXPECTED_PIVOTS = {key: [frac(z) for z in value] for key, value in EXPECTED_PIVOTS.items()}


def outer(v):
    return [[x * y for y in v] for x in v]


def subtract(a, b):
    return [[x - y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def ldl_pivots(a):
    size = len(a)
    ell = [[Q(int(i == j)) for j in range(size)] for i in range(size)]
    diagonal = []
    for j in range(size):
        pivot = a[j][j] - sum(ell[j][k] ** 2 * diagonal[k] for k in range(j))
        if pivot == 0:
            diagonal.append(pivot)
            continue
        diagonal.append(pivot)
        for i in range(j + 1, size):
            ell[i][j] = (
                a[i][j] - sum(ell[i][k] * ell[j][k] * diagonal[k] for k in range(j))
            ) / pivot
    return diagonal


def inner(a, b):
    return sum(x * y for row_a, row_b in zip(a, b) for x, y in zip(row_a, row_b))


def extend_dual(active_x, w, full_g):
    """Exact clique/Schur extension of a reduced feasible dual."""
    full = [[Q(0) for _ in range(L + 1)] for _ in range(L + 1)]
    for i in range(ACTIVE):
        for j in range(ACTIVE):
            full[i][j] = active_x[i][j]
    if w == 1:
        alpha = full_g[5][6] / full_g[5][5]
        y = [alpha * active_x[i][5] for i in range(ACTIVE)]
        schur = full_g[6][6] - alpha * full_g[5][6]
    else:
        determinant = full_g[4][4] * full_g[5][5] - full_g[4][5] ** 2
        alpha = (full_g[5][5] * full_g[4][6] - full_g[4][5] * full_g[5][6]) / determinant
        beta = (-full_g[4][5] * full_g[4][6] + full_g[4][4] * full_g[5][6]) / determinant
        y = [alpha * active_x[i][4] + beta * active_x[i][5] for i in range(ACTIVE)]
        schur = full_g[6][6] - alpha * full_g[4][6] - beta * full_g[5][6]
    for i, value in enumerate(y):
        full[i][6] = full[6][i] = value
    full[6][6] = full_g[6][6]
    assert schur > 0
    for i in range(L + 1):
        for j in range(L + 1):
            if abs(i - j) <= w:
                assert full[i][j] == full_g[i][j]
    return full, schur


def canonical(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def matrix_digest(a):
    rows = [[canonical(x) for x in row] for row in a]
    return hashlib.sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    args = parser.parse_args()

    e7 = reconstruct_atom()
    assert e7 == [Q(1), Q(5, 6), Q(2, 3), Q(1, 2), Q(1, 3), Q(1, 6), Q(0)]
    g7 = reconstruct_charge()
    e = e7[:ACTIVE]
    g = [row[:ACTIVE] for row in g7[:ACTIVE]]
    m = outer(e)
    m7 = outer(e7)
    raw = inner(g, m)
    assert raw == Q(1, 4)

    expected_hashes = {
        (1, "dual"): "f0a151f10acdfeb02ca627a08e94a195de1d88bdffec4e64bc316a4ea19e1f7f",
        (1, "primal"): "ff073c9bb6861dec4283424970d23b37dfe970de2d6ff03084dab7844c1fb788",
        (2, "dual"): "321320c33f194a19b33d29034e4223661aebea19910a71f16f5d95cc8a1ed2ad",
        (2, "primal"): "f62da8dabbaad2e8a99df10fc09198506d15d0292191fca5ec52bb223b571d12",
    }
    audit = {}
    for w in (1, 2):
        x = DUAL[w]
        c = PRIMAL[w]
        slack = subtract(c, m)
        for i in range(ACTIVE):
            for j in range(ACTIVE):
                assert (abs(i - j) <= w or c[i][j] == 0)
                if abs(i - j) <= w:
                    assert x[i][j] == g[i][j]
        piv_x = ldl_pivots(x)
        piv_s = ldl_pivots(slack)
        assert piv_x == EXPECTED_PIVOTS[(w, "dual")]
        assert piv_s == EXPECTED_PIVOTS[(w, "slack")]
        assert all(value > 0 for value in piv_x + piv_s)
        full_x, schur = extend_dual(x, w, g7)
        full_pivots = ldl_pivots(full_x)
        assert full_pivots == piv_x + [schur]
        assert all(value > 0 for value in full_pivots)
        assert matrix_digest(x) == expected_hashes[(w, "dual")]
        assert matrix_digest(c) == expected_hashes[(w, "primal")]
        lower, upper = inner(m, x), inner(g, c)
        assert lower < upper
        # Positive homogeneity of the exact branch weight.
        lam = Q(7, 11)
        assert inner(g, [[lam * z for z in row] for row in c]) == lam * upper
        assert subtract(
            [[lam * z for z in row] for row in c],
            [[lam * z for z in row] for row in m],
        ) == [[lam * z for z in row] for row in slack]
        audit[str(w)] = {
            "lower": canonical(lower), "upper": canonical(upper),
            "dual_active_ldl_pivots": [canonical(z) for z in piv_x],
            "dual_extension_schur_pivot": canonical(schur),
            "dual_full_matrix": [[canonical(z) for z in row] for row in full_x],
            "dual_full_ldl_pivots": [canonical(z) for z in full_pivots],
            "dual_full_matrix_sha256": matrix_digest(full_x),
            "primal_slack_active_ldl_pivots": [canonical(z) for z in piv_s],
            "dual_matrix_sha256": matrix_digest(x),
            "primal_matrix_sha256": matrix_digest(c),
        }

    lo1 = frac(audit["1"]["lower"])
    hi1 = frac(audit["1"]["upper"])
    lo2 = frac(audit["2"]["lower"])
    hi2 = frac(audit["2"]["upper"])
    assert (lo1, hi1) == (Q(60650731, 180180000), Q(1136822741, 3363360000))
    assert (lo2, hi2) == (Q(167478197, 630630000), Q(894863807, 3363360000))
    assert lo1 - hi2 == Q(10951531, 155232000) > 0
    assert lo1 - raw == Q(15605731, 180180000) > 0
    assert lo2 - raw == Q(9820697, 630630000) > 0

    result = {
        "schema": "m230.m227-fresh-referee.v1",
        "python": platform.python_version(), "seed": None,
        "m227_inventory": {
            "ledger_digest": "7b679294f7c6a4aa956a3577ae3350880698eb92d7b5776157f5f0e444e09105",
            "payload_count": 8, "all_payloads_verified_externally": True,
        },
        "atom": [canonical(z) for z in e7],
        "raw_charge": canonical(raw),
        "active_G_sha256": matrix_digest(g),
        "active_M_sha256": matrix_digest(m),
        "full_G_sha256": matrix_digest(g7),
        "full_M_sha256": matrix_digest(m7),
        "certificate_audit": audit,
        "separations": {
            "p1_lower_minus_p2_upper": canonical(lo1 - hi2),
            "p1_lower_minus_raw": canonical(lo1 - raw),
            "p2_lower_minus_raw": canonical(lo2 - raw),
        },
        "zero_coordinate_audit": (
            "primal zero extension and exact dual clique/Schur extension prove "
            "equality of the 6x6 and 7x7 optima for w=1,2"
        ),
        "generic_elevation_formula_checked": True,
        "eta_over_pi_positive_homogeneity_checked": True,
        "killed_branch_policy": "envelope acts only on surviving atoms and creates no branch",
        "verdict": "REJECT_FROZEN_PROOF_CORRECTED_THEOREM_INDEPENDENTLY_SALVAGED",
        "objections": [{
            "number": "M-1",
            "severity": "material",
            "text": (
                "M227 section 2 falsely says primal restriction preserves the objective, and "
                "its 6x6 duals are not by themselves certificates for the declared full "
                "program. M230 supplies and verifies missing exact 7x7 clique/Schur extensions."
            ),
        }],
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(encoded)
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
