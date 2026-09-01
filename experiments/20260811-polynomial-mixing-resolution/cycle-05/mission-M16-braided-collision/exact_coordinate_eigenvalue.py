#!/usr/bin/env python3
"""Exact characteristic polynomial in the leading N=6 centralizer character.

This does not by itself certify that the selected character contains the
global second eigenvalue; the full numerical Gram audit identifies that
sector.  It gives an exact algebraic description of the candidate.
"""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp

from braided_collision_audit import compose, conjugate, cycles, inverse, setup
from three_gap_scaling import cycle_type


def main():
    n = 6
    ident, _ts, group, support, weights, _lifts = setup(n)
    h = next(g for g in group if cycle_type(g) == (2, 2, 1, 1))
    centralizer = [
        c for c in itertools.permutations(range(n))
        if compose(c, h) == compose(h, c)
    ]

    def chi(c):
        # The numerically leading mode is the sign character of the action on
        # the two fixed points 1,2 and is trivial on the moved four points.
        return 1 if c[0] == 0 else -1

    visited = set()
    basis = []
    for rep in support:
        if rep in visited:
            continue
        values = {}
        consistent = True
        for c in centralizer:
            y = conjugate(rep, c)
            sign = chi(c)
            if y in values and values[y] != sign:
                consistent = False
            values[y] = sign
        visited.update(values)
        if consistent:
            basis.append((rep, values))

    matrix = []
    for rep_i, _values_i in basis:
        marginal = 0
        joint = {}
        for y in support:
            z = compose(inverse(rep_i), compose(h, inverse(y)))
            mass = weights[rep_i] * weights[y] * weights.get(z, 0)
            joint[y] = mass
            marginal += mass
        row = []
        for _rep_j, values_j in basis:
            row.append(sum(Fraction(joint[y] * sign, marginal) for y, sign in values_j.items()))
        matrix.append(row)

    smat = sp.Matrix([
        [sp.Rational(x.numerator, x.denominator) for x in row] for row in matrix
    ])
    lam = sp.symbols("lambda")
    charpoly = sp.Poly(smat.charpoly(lam).as_expr(), lam)
    factors = sp.factor_list(charpoly.as_expr())
    eig = np.linalg.eigvals(np.array([[float(x) for x in row] for row in matrix]))
    lead = max(eig.real)
    selected = None
    for factor, multiplicity in factors[1]:
        roots = [complex(r) for r in sp.nroots(factor, maxsteps=200)]
        if any(abs(r.real - lead) < 1e-8 and abs(r.imag) < 1e-8 for r in roots):
            selected = {
                "factor": str(factor),
                "multiplicity": multiplicity,
                "real_roots_numeric": sorted(
                    r.real for r in roots if abs(r.imag) < 1e-8
                ),
            }
            break
    payload = {
        "status": "complete",
        "N": n,
        "endpoint_cycles": cycles(h),
        "centralizer_size": len(centralizer),
        "character": "sign on swapping fixed points 1,2; trivial on the other generators",
        "character_space_dimension": len(basis),
        "matrix": [
            [[x.numerator, x.denominator] for x in row] for row in matrix
        ],
        "characteristic_polynomial": str(charpoly.as_expr()),
        "factorization": str(factors),
        "leading_eigenvalue_numeric": float(lead),
        "selected_leading_factor": selected,
        "candidate_mu_3_formula": "mu=(1+2*kappa)/3 for the selected real root kappa",
        "scope": (
            "exact algebraic candidate in the numerically leading character; global optimality remains numerical"
        ),
    }
    out = Path(
        "experiments/20260811-polynomial-mixing-resolution/cycle-05/"
        "mission-M16-braided-collision/exact_coordinate_eigenvalue.json"
    )
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in payload.items() if k != "matrix"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
