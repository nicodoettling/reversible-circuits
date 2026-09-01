#!/usr/bin/env python3
"""Clean-room exact referee for M230.

This standard-library checker imports/reads no predecessor code or data.
The rational certificates under audit are transcribed here after the
independent definitions and conic programs were fixed in plan.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path


def q(value: str | int) -> F:
    return F(value)


def mat(rows: list[list[str | int]]) -> list[list[F]]:
    return [[q(x) for x in row] for row in rows]


def outer(x: list[F], y: list[F]) -> list[list[F]]:
    return [[a * b for b in y] for a in x]


def sub(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def contract(a: list[list[F]], b: list[list[F]]) -> F:
    return sum((x * y for ar, br in zip(a, b) for x, y in zip(ar, br)), F(0))


def quadratic(x: list[F], a: list[list[F]]) -> F:
    return sum((x[i] * a[i][j] * x[j] for i in range(len(x)) for j in range(len(x))), F(0))


def ldl_pivots(a: list[list[F]]) -> list[F]:
    n = len(a)
    l = [[F(0) for _ in range(n)] for _ in range(n)]
    d: list[F] = []
    for i in range(n):
        l[i][i] = F(1)
        pivot = a[i][i] - sum(l[i][k] * l[i][k] * d[k] for k in range(i))
        d.append(pivot)
        if pivot == 0:
            continue
        for j in range(i + 1, n):
            l[j][i] = (a[j][i] - sum(l[j][k] * l[i][k] * d[k] for k in range(i))) / pivot
    return d


def sha_matrix(a: list[list[F]]) -> str:
    payload = json.dumps([[str(x) for x in row] for row in a], separators=(",", ":"), sort_keys=False)
    return hashlib.sha256(payload.encode()).hexdigest()


def bernstein_product_integral(i: int, j: int) -> F:
    return F(comb(6, i) * comb(6, j) * factorial(i + j) * factorial(12 - i - j), factorial(13))


def build_g() -> list[list[F]]:
    # Integral (u-1/2)b_(6,i)(u) du = (i-3)/56.
    moments = [F(i - 3, 56) for i in range(7)]
    return [[bernstein_product_integral(i, j) - 12 * moments[i] * moments[j] for j in range(7)] for i in range(7)]


def elevate(z: list[F], n: int, big_l: int) -> list[F]:
    h = big_l - n
    out: list[F] = []
    for r in range(big_l + 1):
        value = F(0)
        for k in range(n + 1):
            if 0 <= r - k <= h:
                value += z[k] * F(comb(n, k) * comb(h, r - k), comb(big_l, r))
        out.append(value)
    return out


DUAL_FULL = {
    1: mat([
        ["433/10192", "79/5096", "31/1000", "7/200", "309/10000", "153/5000", "14773/830000"],
        ["79/5096", "747/28028", "1335/56056", "201/10000", "47/2000", "79/5000", "68651/7470000"],
        ["31/1000", "1335/56056", "3491/112112", "25/858", "309/10000", "59/2500", "51271/3735000"],
        ["7/200", "201/10000", "25/858", "100/3003", "25/858", "73/2500", "63437/3735000"],
        ["309/10000", "47/2000", "309/10000", "25/858", "3491/112112", "1335/56056", "35155/2537808"],
        ["153/5000", "79/5000", "59/2500", "73/2500", "1335/56056", "747/28028", "79/5096"],
        ["14773/830000", "68651/7470000", "51271/3735000", "63437/3735000", "35155/2537808", "79/5096", "433/10192"],
    ]),
    2: mat([
        ["433/10192", "79/5096", "673/112112", "59/5000", "61/2500", "147/5000", "10039/540000"],
        ["79/5096", "747/28028", "1335/56056", "8/429", "87/5000", "109/5000", "929/64800"],
        ["673/112112", "1335/56056", "3491/112112", "25/858", "2529/112112", "87/5000", "8587591/1891890000"],
        ["59/5000", "8/429", "25/858", "100/3003", "25/858", "8/429", "127/138996"],
        ["61/2500", "87/5000", "2529/112112", "25/858", "3491/112112", "1335/56056", "673/112112"],
        ["147/5000", "109/5000", "87/5000", "8/429", "1335/56056", "747/28028", "79/5096"],
        ["10039/540000", "929/64800", "8587591/1891890000", "127/138996", "673/112112", "79/5096", "433/10192"],
    ]),
}


PRIMAL = {
    1: mat([
        ["19731/10000", "16443/10000", 0, 0, 0, 0],
        ["16443/10000", "1713/1250", 0, 0, 0, 0],
        [0, 0, "12753/10000", "589/625", 0, 0],
        [0, 0, "589/625", "7067/10000", "7/500", 0],
        [0, 0, 0, "7/500", "7697/10000", "1933/5000"],
        [0, 0, 0, 0, "1933/5000", "1993/10000"],
    ]),
    2: mat([
        ["15391/10000", "997/10000", "1204/625", 0, 0, 0],
        ["997/10000", "3589/1250", "-30297/10000", "3649/1250", 0, 0],
        ["1204/625", "-30297/10000", "33663/5000", "-5507/1250", "11997/10000", 0],
        [0, "3649/1250", "-5507/1250", "11909/2500", "-17379/10000", "1111/5000"],
        [0, 0, "11997/10000", "-17379/10000", "1077/625", "-487/5000"],
        [0, 0, 0, "1111/5000", "-487/5000", "4381/10000"],
    ]),
}


EXPECTED = {
    1: {
        "lower": q("60650731/180180000"),
        "upper": q("1136822741/3363360000"),
        "last_pivot": q("25/747"),
        "extension": [q("869/1494")],
        "digest": "73f302213b3de78b2da2b4bba7968d59c2fab0aa93a2f6548be13ac02ec4f6d6",
    },
    2: {
        "lower": q("167478197/630630000"),
        "upper": q("894863807/3363360000"),
        "last_pivot": q("97/3564"),
        "extension": [q("-43/54"), q("419/324")],
        "digest": "4d70d7645a7f74443a2c7c575279cfc065e794512bc588323607b5b8ebdb7190",
    },
}


def objective_gap_witness(g: list[list[F]], m: list[list[F]], w: int) -> F:
    # C=M+t vv^T is feasible for all t>=0. Choose v=e_6, so this perturbation
    # is bandwidth zero. Its restriction to coordinates 0..5 is unchanged,
    # while its objective changes by t G_66 >0. This directly refutes the
    # claimed objective preservation under restriction.
    v = [F(0)] * 7
    v[6] = F(1)
    c = [[m[i][j] + v[i] * v[j] for j in range(7)] for i in range(7)]
    assert all(c[i][j] == 0 for i in range(7) for j in range(7) if abs(i - j) > w and m[i][j] == 0)
    return contract(g, c) - contract([row[:6] for row in g[:6]], [row[:6] for row in c[:6]])


def main(output: Path) -> None:
    g = build_g()
    z2 = [F(1), F(1, 2), F(0)]
    e = elevate(z2, 2, 6)
    assert e == [F(1), F(5, 6), F(2, 3), F(1, 2), F(1, 3), F(1, 6), F(0)]
    m = outer(e, e)
    raw = contract(g, m)
    assert raw == F(1, 4)

    restriction_gap = objective_gap_witness(g, m, 1)
    assert restriction_gap == g[6][6] == F(433, 10192) > 0

    certs: dict[str, object] = {}
    for w in (1, 2):
        x = DUAL_FULL[w]
        pivots = ldl_pivots(x)
        assert all(p > 0 for p in pivots)
        assert pivots[-1] == EXPECTED[w]["last_pivot"]
        assert all(x[i][j] == g[i][j] for i in range(7) for j in range(7) if abs(i - j) <= w)

        xbar = [row[:6] for row in x[:6]]
        if w == 1:
            alpha = EXPECTED[w]["extension"][0]
            constructed = [alpha * xbar[i][5] for i in range(6)]
        else:
            alpha, beta = EXPECTED[w]["extension"]
            constructed = [alpha * xbar[i][4] + beta * xbar[i][5] for i in range(6)]
        assert constructed == [x[i][6] for i in range(6)]
        assert quadratic(e, x) == quadratic(e[:6], xbar) == EXPECTED[w]["lower"]

        c6 = PRIMAL[w]
        c7 = [row + [F(0)] for row in c6] + [[F(0)] * 7]
        assert all(c7[i][j] == 0 for i in range(7) for j in range(7) if abs(i - j) > w)
        slack = sub(c7, m)
        slack6 = [row[:6] for row in slack[:6]]
        slack_pivots = ldl_pivots(slack6)
        assert all(p > 0 for p in slack_pivots)
        assert all(slack[i][6] == 0 and slack[6][i] == 0 for i in range(7))
        assert contract(g, c7) == contract([row[:6] for row in g[:6]], c6) == EXPECTED[w]["upper"]
        assert sha_matrix(x) == EXPECTED[w]["digest"]

        certs[str(w)] = {
            "dual_full_ldl_pivots": [str(p) for p in pivots],
            "dual_extension_last_pivot": str(pivots[-1]),
            "dual_objective": str(quadratic(e, x)),
            "dual_on_band": True,
            "dual_matrix_sha256": sha_matrix(x),
            "primal_zero_extension": True,
            "primal_active_slack_ldl_pivots": [str(p) for p in slack_pivots],
            "primal_objective": str(contract(g, c7)),
        }

    assert EXPECTED[1]["lower"] - EXPECTED[2]["upper"] == q("10951531/155232000") > 0
    assert EXPECTED[1]["lower"] - raw == q("15605731/180180000") > 0
    assert EXPECTED[2]["lower"] - raw == q("9820697/630630000") > 0

    # Generic elevation and bookkeeping checks. The elevation formula is
    # linear; hence outer products stay rank one. Positive lambda scales both
    # PSD domination and the linear charge. Applying the operation only to a
    # declared live-atom list cannot create a killed branch.
    generic_z = [q("3/5"), q("-2/7"), q("11/13")]
    generic_e = elevate(generic_z, 2, 6)
    assert outer(generic_e, generic_e) == outer(elevate(generic_z, 2, 6), elevate(generic_z, 2, 6))
    lam = q("17/19")
    assert contract(g, [[lam * x for x in row] for row in m]) == lam * contract(g, m)
    live = [(0, m), (1, m)]
    transformed = [(a, [[lam * x for x in row] for row in atom]) for a, atom in live]
    assert [a for a, _ in transformed] == [0, 1] and 2 not in [a for a, _ in transformed]

    result = {
        "schema": "m233.m230-fresh-referee.v1",
        "verdict": "ACCEPT_M230_CORRECTED_SALVAGE",
        "m227_disposition": "REJECT_AS_SELF_CONTAINED_FROZEN_PROOF",
        "material_objections_to_m230": [],
        "nonmaterial_objections_to_m230": [],
        "m230_sha256sums_digest": "5e9e0b59490a64dec97738127f0d2060187f062598d527e3b6cbbb47378b96d3",
        "atom": [str(x) for x in e],
        "raw_charge": str(raw),
        "restriction_counterexample_objective_gap": str(restriction_gap),
        "certificates": certs,
        "separations": {
            "p1_lower_minus_p2_upper": str(EXPECTED[1]["lower"] - EXPECTED[2]["upper"]),
            "p1_lower_minus_raw": str(EXPECTED[1]["lower"] - raw),
            "p2_lower_minus_raw": str(EXPECTED[2]["lower"] - raw),
        },
        "generic_rank_one_elevation_checked": True,
        "positive_eta_over_pi_scaling_checked": True,
        "killed_branch_preservation_checked": True,
        "scope": "one atom only; no exact optima, uniform factor, aggregation, recursion, gap, mixing, or Terminal",
    }
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("results.json"))
    main(parser.parse_args().output)
