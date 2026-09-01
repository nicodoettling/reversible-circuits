#!/usr/bin/env python3
"""Fast grouped probe for the exact terminal seed counterfamily.

For x_s=(s,1,0,s), D=0.  If a canonical first-boundary edge has prefix
mass A and suffix length l, put

    beta(A,l)=rho(basin)/rho(refined)
             =(l+1)!/w_A * sum_p C(A,p)/(p+l)!.

After summing the remaining suffix composition and cancelling the child
split mass, the transformed reset row is

    R_s = q_s^2 e^-1/v_(s+1) sum_l 1/[(l+1)(l+1)!]
          sum_A beta(A,l)^2 sum_(c>A) v_c C_v(s-c,l-1),

with the inactive rank-one child (A,c)=(1,2) omitted.  Here
v_a=e^-a w_a and C_v is the coefficient of V(z)^p.  This is algebraically
identical to the exact rational sum in ``terminal_exact_counterexample.py``
but runs in O(s^3) time and uses binary64 arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import time
from pathlib import Path


def tables(s_max: int):
    v = [0.0] + [
        math.exp((a - 1) * math.log(a) - math.lgamma(a + 1) - a)
        for a in range(1, s_max + 2)
    ]
    coefficient = [[0.0] * (s_max + 1) for _ in range(s_max + 1)]
    coefficient[0][0] = 1.0
    for a in range(1, s_max + 1):
        for p in range(1, a + 1):
            coefficient[a][p] = math.exp(
                math.log(p)
                + (a - p - 1) * math.log(a)
                - math.lgamma(a - p + 1)
                - a
            )
    return v, coefficient


def beta(A: int, l: int, v, coefficient) -> float:
    # (l+1)!/(p+l)! is evaluated as a short reciprocal product, avoiding
    # factorial overflow and keeping beta bounded by e.
    answer = 0.0
    factorial_ratio = 1.0  # p=1
    for p in range(1, A + 1):
        if p > 1:
            factorial_ratio /= l + p
        answer += coefficient[A][p] * factorial_ratio / v[A]
    return answer


def terminal_ratio(s: int, v, coefficient) -> tuple[float, dict]:
    # q=w_1 w_s/w_(s+1)=v_1 v_s/v_(s+1); unlike a generic split,
    # omitting v_1 would leave an erroneous factor e.
    q = v[1] * v[s] / v[s + 1]
    total = 0.0
    max_beta = 0.0
    degree_terms = []
    for l in range(1, s):
        prefix_parts = l - 1
        # suffix_after_A[A] = sum_(c>A) v_c C_v(s-c,l-1).
        terms = [0.0] * (s + 1)
        for c in range(1, s + 1):
            rest = s - c
            if 0 <= prefix_parts <= rest:
                terms[c] = v[c] * coefficient[rest][prefix_parts]
        suffix_after_A = [0.0] * (s + 2)
        for c in range(s, 0, -1):
            suffix_after_A[c - 1] = suffix_after_A[c] + terms[c]
        inner = 0.0
        for A in range(1, s):
            b = beta(A, l, v, coefficient)
            max_beta = max(max_beta, b)
            tail = suffix_after_A[A]
            if A == 1:
                # Omit c=2, equivalent to child rank A+(c-A)-1=1.
                tail -= terms[2]
            inner += b * b * max(tail, 0.0)
        degree_factor = math.exp(-math.lgamma(l + 2)) / (l + 1)
        contribution = degree_factor * inner
        total += contribution
        degree_terms.append(contribution)
    ratio = q * q * math.exp(-1.0) * total / v[s + 1]
    scaled_terms = [q * q * math.exp(-1.0) * x / v[s + 1] for x in degree_terms]
    leading = sorted(
        ((i + 1, value) for i, value in enumerate(scaled_terms)),
        key=lambda item: item[1],
        reverse=True,
    )[:5]
    return ratio, {
        "q": q,
        "max_beta": max_beta,
        "degree_contribution_sum": sum(scaled_terms),
        "leading_suffix_lengths": leading,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-values", type=int, nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    v, coefficient = tables(max(args.s_values))
    records = []
    for s in args.s_values:
        ratio, diagnostics = terminal_ratio(s, v, coefficient)
        P = s + 1
        row = {
            "s": s,
            "context": [s, 1, 0, s],
            "P": P,
            "ratio": ratio,
            "ratio_minus_one": ratio - 1.0,
            "P_times_ratio_minus_one": P * (ratio - 1.0),
            "ratio_over_log_s": ratio / math.log(s),
            "ratio_over_s": ratio / s,
            "diagnostics": diagnostics,
        }
        records.append(row)
        print(json.dumps(row, sort_keys=True), flush=True)
    payload = {
        "claim_tested": (
            "Whether the terminal seed family can satisfy R_s<=1+C/(s+1) "
            "for a universal C"
        ),
        "finite_scope_warning": (
            "Growth in bounded floating values is empirical until paired with "
            "an analytic lower bound; exact ranks 18--21 are separately certified."
        ),
        "arithmetic": "IEEE-754 binary64 grouped Cayley coefficients",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "parameters": {"s_values": args.s_values},
        "elapsed_seconds": time.time() - started,
        "records": records,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "elapsed_seconds": payload["elapsed_seconds"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
