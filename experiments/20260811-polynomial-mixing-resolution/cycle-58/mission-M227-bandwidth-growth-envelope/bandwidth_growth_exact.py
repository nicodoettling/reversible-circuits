#!/usr/bin/env python3
"""M227 standalone exact checker: rank-one Bernstein compression brackets."""

import argparse
import hashlib
import json
import platform
from fractions import Fraction as F
from math import comb
from pathlib import Path

N = 6  # omit the identically zero final atom coordinate
E = [F(1), F(5, 6), F(2, 3), F(1, 2), F(1, 3), F(1, 6)]


def integral_product(i, j):
    return F(comb(6, i) * comb(6, j), 13 * comb(12, i + j))


def integral_first(i):
    # Integral (u-1/2) b_{6,i}(u) du.
    return F(comb(6, i)) * (
        F(1, 8 * comb(7, i + 1)) - F(1, 14 * comb(6, i))
    )


def charge_matrix():
    return [
        [integral_product(i, j) - 12 * integral_first(i) * integral_first(j)
         for j in range(N)]
        for i in range(N)
    ]


G = charge_matrix()
M = [[E[i] * E[j] for j in range(N)] for i in range(N)]


DUAL_FREE = {
    1: {
        (0, 2): F(31, 1000), (0, 3): F(7, 200),
        (0, 4): F(309, 10000), (0, 5): F(153, 5000),
        (1, 3): F(201, 10000), (1, 4): F(47, 2000),
        (1, 5): F(79, 5000), (2, 4): F(309, 10000),
        (2, 5): F(59, 2500), (3, 5): F(73, 2500),
    },
    2: {
        (0, 3): F(59, 5000), (0, 4): F(61, 2500),
        (0, 5): F(147, 5000), (1, 4): F(87, 5000),
        (1, 5): F(109, 5000), (2, 5): F(87, 5000),
    },
}

PRIMAL_BAND = {
    1: {
        (0, 0): F(19731, 10000), (0, 1): F(16443, 10000),
        (1, 1): F(1713, 1250), (1, 2): F(0),
        (2, 2): F(12753, 10000), (2, 3): F(589, 625),
        (3, 3): F(7067, 10000), (3, 4): F(7, 500),
        (4, 4): F(7697, 10000), (4, 5): F(1933, 5000),
        (5, 5): F(1993, 10000),
    },
    2: {
        (0, 0): F(15391, 10000), (0, 1): F(997, 10000),
        (0, 2): F(1204, 625), (1, 1): F(3589, 1250),
        (1, 2): F(-30297, 10000), (1, 3): F(3649, 1250),
        (2, 2): F(33663, 5000), (2, 3): F(-5507, 1250),
        (2, 4): F(11997, 10000), (3, 3): F(11909, 2500),
        (3, 4): F(-17379, 10000), (3, 5): F(1111, 5000),
        (4, 4): F(1077, 625), (4, 5): F(-487, 5000),
        (5, 5): F(4381, 10000),
    },
}


def zero_matrix():
    return [[F(0) for _ in range(N)] for _ in range(N)]


def dual_matrix(w):
    x = zero_matrix()
    for i in range(N):
        for j in range(i, N):
            z = G[i][j] if j - i <= w else DUAL_FREE[w][(i, j)]
            x[i][j] = x[j][i] = z
    return x


def primal_matrix(w):
    c = zero_matrix()
    for (i, j), z in PRIMAL_BAND[w].items():
        c[i][j] = c[j][i] = z
    return c


def subtract(a, b):
    return [[a[i][j] - b[i][j] for j in range(N)] for i in range(N)]


def ldl_pivots(a):
    """Exact unpivoted LDL^T pivots; positivity proves positive definite."""
    ell = [[F(int(i == j)) for j in range(N)] for i in range(N)]
    pivots = []
    for j in range(N):
        d = a[j][j] - sum(ell[j][k] ** 2 * pivots[k] for k in range(j))
        assert d != 0
        pivots.append(d)
        for i in range(j + 1, N):
            ell[i][j] = (
                a[i][j]
                - sum(ell[i][k] * ell[j][k] * pivots[k] for k in range(j))
            ) / d
    return pivots


def inner(a, b):
    return sum(a[i][j] * b[i][j] for i in range(N) for j in range(N))


def fmt(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def matrix_strings(a):
    return [[fmt(z) for z in row] for row in a]


def sha_matrix(a):
    blob = json.dumps(matrix_strings(a), separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    args = parser.parse_args()

    # Degree elevation identity for (1-u): b_{1,0} elevated to degree 6.
    elevated = [F(6 - i, 6) for i in range(7)]
    assert elevated == E + [F(0)]
    raw_cost = inner(G, M)
    assert raw_cost == F(1, 4)

    records = {}
    for w in (1, 2):
        x = dual_matrix(w)
        c = primal_matrix(w)
        s = subtract(c, M)
        for i in range(N):
            for j in range(N):
                if abs(i - j) <= w:
                    assert x[i][j] == G[i][j]
                if abs(i - j) > w:
                    assert c[i][j] == 0
        xp = ldl_pivots(x)
        sp = ldl_pivots(s)
        assert all(z > 0 for z in xp)
        assert all(z > 0 for z in sp)
        lower = inner(M, x)
        upper = inner(G, c)
        assert lower <= upper
        records[str(w)] = {
            "lower": fmt(lower), "upper": fmt(upper),
            "gap": fmt(upper - lower),
            "dual_X": matrix_strings(x),
            "dual_ldl_pivots": [fmt(z) for z in xp],
            "primal_C": matrix_strings(c),
            "primal_slack_ldl_pivots": [fmt(z) for z in sp],
            "dual_sha256": sha_matrix(x), "primal_sha256": sha_matrix(c),
        }

    lo1 = F(records["1"]["lower"])
    hi2 = F(records["2"]["upper"])
    lo2 = F(records["2"]["lower"])
    assert lo1 > hi2 > lo2 > raw_cost
    assert lo1 - hi2 == F(10951531, 155232000)
    assert lo1 - raw_cost == F(15605731, 180180000)
    assert lo2 - raw_cost == F(9820697, 630630000)

    out = {
        "schema": "m227.bandwidth-growth-envelope.v1",
        "python": platform.python_version(), "seed": None,
        "atom_e_degree6": [fmt(z) for z in E + [F(0)]],
        "zero_coordinate_eliminated": 6,
        "raw_charge": fmt(raw_cost),
        "G_sha256": sha_matrix(G), "M_sha256": sha_matrix(M),
        "brackets": records,
        "strict_separations": {
            "p1_lower_minus_raw": fmt(lo1 - raw_cost),
            "p2_lower_minus_raw": fmt(lo2 - raw_cost),
            "p1_lower_minus_p2_upper": fmt(lo1 - hi2),
        },
        "verdict": (
            "exact rational brackets prove p1>p2>raw charge; exact optima "
            "and a degree-uniform compression factor remain unresolved"
        ),
    }
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
