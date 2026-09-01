#!/usr/bin/env python3
"""Falsify/check Lorentzianity of the weighted join-position polynomial.

For N vertices, n=N-1, define

    F_N(z)=sum_P W_N(P) product_{j:P_j=U} z_j,

where W_N(P) is the exact connected minimal-identity path weight.  A
homogeneous multiaffine degree-n polynomial is Lorentzian only if, after
every derivative in n-2 distinct variables, the remaining quadratic has a
Hessian with at most one positive eigenvalue.  A single derivative with two
positive eigenvalues therefore refutes the proposed universal Lorentzian
route.  Floating eigenvalues locate a witness; the output includes its full
integer Hessian so a witness can be independently checked exactly.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import subprocess
import sys
from pathlib import Path

import numpy as np


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return "unavailable"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    payload = json.loads(args.input.read_text())
    records = []
    first_failure = None
    for record in payload["records"]:
        if record.get("path_weights") is None:
            continue
        N = int(record["N"])
        n = N - 1
        m = 2 * n
        weights = {
            tuple(i for i, symbol in enumerate(path) if symbol == "U"): int(w)
            for path, w in record["path_weights"].items()
        }
        derivative_sets = sorted({
            S
            for basis in weights
            for S in itertools.combinations(basis, n - 2)
        })
        minimum_second_positive = None
        failure = None
        checked = 0
        for S in derivative_sets:
            Sset = set(S)
            variables = sorted({
                i for basis in weights if Sset.issubset(basis)
                for i in basis if i not in Sset
            })
            index = {v: j for j, v in enumerate(variables)}
            H = np.zeros((len(variables), len(variables)), dtype=np.float64)
            H_integer = [[0 for _ in variables] for _ in variables]
            for basis, weight in weights.items():
                if not Sset.issubset(basis):
                    continue
                remainder = [i for i in basis if i not in Sset]
                if len(remainder) != 2:
                    raise AssertionError((N, S, basis))
                i, j = map(index.__getitem__, remainder)
                H[i, j] += weight
                H[j, i] += weight
                H_integer[i][j] += weight
                H_integer[j][i] += weight
            eigenvalues = np.linalg.eigvalsh(H)
            scale = max(1.0, float(np.max(np.abs(eigenvalues))))
            positive = [float(x) for x in eigenvalues if x > 1e-10 * scale]
            checked += 1
            if len(positive) >= 2:
                second = positive[-2]
                if minimum_second_positive is None or second < minimum_second_positive:
                    minimum_second_positive = second
                failure = {
                    "derivative_set_zero_based": list(S),
                    "variables_zero_based": variables,
                    "integer_hessian": H_integer,
                    "eigenvalues_float": [float(x) for x in eigenvalues],
                    "positive_eigenvalue_count": len(positive),
                }
                break
        result = {
            "N": N,
            "degree": n,
            "variables": m,
            "path_count": len(weights),
            "derivatives_checked": checked,
            "lorentzian_quadratic_signature_passed": failure is None,
            "first_failure": failure,
        }
        records.append(result)
        if first_failure is None and failure is not None:
            first_failure = result

    output = {
        "metadata": {
            "command": " ".join(sys.argv),
            "repository_commit": git_commit(),
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
            "deterministic": True,
            "seed": None,
        },
        "claim_tested": (
            "For every N, the weighted join-position basis polynomial "
            "F_N is Lorentzian.  One derivative quadratic with at least two "
            "positive Hessian eigenvalues refutes the claim."
        ),
        "records": records,
        "universal_claim_refuted": first_failure is not None,
        "first_failure": first_failure,
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "universal_claim_refuted": first_failure is not None,
        "first_failure_N": None if first_failure is None else first_failure["N"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
