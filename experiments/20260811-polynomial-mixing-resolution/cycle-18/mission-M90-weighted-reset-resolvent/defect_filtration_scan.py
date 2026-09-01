#!/usr/bin/env python3
"""Exact right-heavy scan of the contextual-variance excursion defect.

Write ``Q(x,y)=rho_s(k,t) nu(j)``, ``g=(I-Q)^(-1)A``,
``U=q(1-q)K/(R+1)``, and ``V=Var(Phi)``.  The exact one-step variance
defect has the law-of-total-variance decomposition

    r_V = V-A-QV = Var(E[Phi|C])-A-L_attach,

where ``L_attach`` is the Jensen loss from replacing the correlated
mixture ``sum_j nu_j Phi_j`` by separately charged children.  This script
checks that identity and profiles the nilpotent telescoping sums
``sum_d Q^d r_U=U-g`` and ``sum_d Q^d r_V=V-g`` on right-heavy seeds.

Every attachment rank ``j>=1`` is retained.  Bounded survival is not a
proof of any universal inequality.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import time
from fractions import Fraction
from pathlib import Path

import exact_weighted_resolvent as EXACT
from resolvent_slack_profile import Profiler, deep_children, record


def local_variance_decomposition(
    profiler: Profiler, x: tuple[int, int, int, int]
) -> dict[str, Fraction]:
    s, K, R, B = x
    q = EXACT.q_split(s, B)
    variance_of_root_mean = sum(
        (
            mass
            * (EXACT.contextual_value(k, t, K, R, B) - q) ** 2
            for k, t, mass in EXACT.groups(s)
        ),
        Fraction(),
    )
    attachment_jensen_loss = Fraction(0)
    deep_variance = Fraction(0)
    for k, t, mass in EXACT.groups(s):
        if t <= B or t - 1 < 1:
            continue
        children = []
        for j in range(1, k + 1):
            probability = EXACT.nu(K, R, k, j)
            if probability:
                children.append((probability, (t - 1, K + k, R + j, B)))
        if not children:
            continue
        average_child_variance = sum(
            (
                probability * profiler.V(child)
                for probability, child in children
            ),
            Fraction(),
        )
        mixture_second_moment = Fraction(0)
        for left_probability, left in children:
            for right_probability, right in children:
                mixture_second_moment += (
                    left_probability
                    * right_probability
                    * profiler.moments.moment(
                        t - 1,
                        left[1],
                        left[2],
                        right[1],
                        right[2],
                        B,
                    )
                )
        mixture_mean = sum(
            (
                probability * EXACT.q_split(t - 1, B)
                for probability, _ in children
            ),
            Fraction(),
        )
        expected_mean = EXACT.contextual_value(k, t, K, R, B)
        if mixture_mean != expected_mean:
            raise AssertionError(("deep mean", x, k, t, mixture_mean, expected_mean))
        mixture_variance = mixture_second_moment - mixture_mean * mixture_mean
        loss = average_child_variance - mixture_variance
        if loss < 0:
            raise AssertionError(("negative Jensen loss", x, k, t, loss))
        attachment_jensen_loss += mass * loss
        deep_variance += mass * mixture_variance

    variance = profiler.V(x)
    if variance != variance_of_root_mean + deep_variance:
        raise AssertionError(("total variance", x))
    reset = EXACT.reset_budget(*x)
    q_variance = sum(
        (weight * profiler.V(child) for weight, child in deep_children(x)),
        Fraction(),
    )
    defect = variance - reset - q_variance
    decomposed = variance_of_root_mean - reset - attachment_jensen_loss
    if defect != decomposed:
        raise AssertionError(("defect decomposition", x, defect, decomposed))
    return {
        "variance": variance,
        "variance_of_root_mean": variance_of_root_mean,
        "deep_mixture_variance": deep_variance,
        "attachment_jensen_loss": attachment_jensen_loss,
        "reset_budget": reset,
        "deep_separate_variance": q_variance,
        "defect": defect,
    }


def scan(s_max: int, K_values: list[int]) -> dict[str, object]:
    profiler = Profiler()
    counters = {
        "main_U_failures": 0,
        "right_heavy_g_over_V_failures": 0,
        "variance_envelope_failures": 0,
        "negative_local_U_defects": 0,
        "negative_local_V_defects": 0,
        "negative_positive_depth_U_contributions": 0,
        "negative_positive_depth_V_contributions": 0,
        "negative_U_reverse_tails": 0,
        "negative_V_reverse_tails": 0,
    }
    first = {key: None for key in counters}
    extrema: dict[str, tuple[Fraction, dict[str, object]] | None] = {
        "max_g_over_U": None,
        "max_g_over_V": None,
        "min_local_U_defect_over_U": None,
        "min_local_V_defect_over_V": None,
        "min_positive_depth_U_contribution_over_U": None,
        "min_positive_depth_V_contribution_over_V": None,
        "min_U_reverse_tail_over_U": None,
        "min_V_reverse_tail_over_V": None,
    }

    def update(name: str, value: Fraction, row: dict[str, object], minimum: bool) -> None:
        current = extrema[name]
        if current is None or (value < current[0] if minimum else value > current[0]):
            extrema[name] = (value, row)

    def fail(name: str, row: dict[str, object]) -> None:
        counters[name] += 1
        if first[name] is None:
            first[name] = row

    contexts = 0
    for s in range(2, s_max + 1):
        for K in K_values:
            x = (s, K, K - 1, 1)
            for B in range(1, s + 1):
                x = (s, K, K - 1, B)
                contexts += 1
                U = profiler.U(x)
                V = profiler.V(x)
                reset_profile = profiler.reset_depth(x)
                g = sum(reset_profile, Fraction())
                u_profile = profiler.defect_depth("U", x)
                v_profile = profiler.defect_depth("V", x)
                if sum(u_profile, Fraction()) != U - g:
                    raise AssertionError(("U telescoping", x))
                if sum(v_profile, Fraction()) != V - g:
                    raise AssertionError(("V telescoping", x))
                decomposition = local_variance_decomposition(profiler, x)
                if decomposition["defect"] != v_profile[0]:
                    raise AssertionError(("local defect", x))

                base_row = {
                    "context": list(x),
                    "U": record(U),
                    "V": record(V),
                    "g": record(g),
                    "U_minus_g": record(U - g),
                    "V_minus_g": record(V - g),
                    "local_U_defect": record(u_profile[0]),
                    "local_V_defect": record(v_profile[0]),
                    "variance_of_root_mean": record(
                        decomposition["variance_of_root_mean"]
                    ),
                    "attachment_jensen_loss": record(
                        decomposition["attachment_jensen_loss"]
                    ),
                    "reset_budget": record(decomposition["reset_budget"]),
                }
                update("max_g_over_U", g / U, base_row, False)
                if V:
                    update("max_g_over_V", g / V, base_row, False)
                update(
                    "min_local_U_defect_over_U",
                    u_profile[0] / U,
                    base_row,
                    True,
                )
                if V:
                    update(
                        "min_local_V_defect_over_V",
                        v_profile[0] / V,
                        base_row,
                        True,
                    )
                if g > U:
                    fail("main_U_failures", base_row)
                if g > V:
                    fail("right_heavy_g_over_V_failures", base_row)
                if V > U:
                    fail("variance_envelope_failures", base_row)
                if u_profile[0] < 0:
                    fail("negative_local_U_defects", base_row)
                if v_profile[0] < 0:
                    fail("negative_local_V_defects", base_row)

                for kind, values, scale in (("U", u_profile, U), ("V", v_profile, V)):
                    tail = Fraction(0)
                    tails = [Fraction(0)] * len(values)
                    for depth in range(len(values) - 1, -1, -1):
                        tail += values[depth]
                        tails[depth] = tail
                    for depth in range(1, len(values)):
                        row = dict(base_row)
                        row.update({
                            "depth": depth,
                            "contribution": record(values[depth]),
                            "reverse_tail": record(tails[depth]),
                        })
                        update(
                            f"min_positive_depth_{kind}_contribution_over_{kind}",
                            values[depth] / scale,
                            row,
                            True,
                        )
                        update(
                            f"min_{kind}_reverse_tail_over_{kind}",
                            tails[depth] / scale,
                            row,
                            True,
                        )
                        if values[depth] < 0:
                            fail(
                                f"negative_positive_depth_{kind}_contributions",
                                row,
                            )
                        if tails[depth] < 0:
                            fail(f"negative_{kind}_reverse_tails", row)

    return {
        "contexts": contexts,
        "failure_counts": counters,
        "first_failures": first,
        "extrema": {
            name: {"value": record(item[0]), "row": item[1]}
            for name, item in extrema.items()
        },
        "memoized_mixed_moment_contexts": profiler.moments.calls,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=12)
    parser.add_argument("--K-values", type=int, nargs="+", default=[1, 2, 4, 8, 16, 32])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    result = scan(args.s_max, args.K_values)
    payload = {
        "claim_tested": (
            "exact law-of-total-variance defect and full all-j excursion "
            "tails on right-heavy seeds"
        ),
        "finite_scope_warning": "Exact bounded survival proves no universal inequality.",
        "arithmetic": "fractions.Fraction exact grouped recurrences",
        "normalization": "Q=rho*nu for every j>=1; g=(I-Q)^-1 A",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "parameters": {"s_max": args.s_max, "K_values": args.K_values},
        "elapsed_seconds": time.time() - started,
        "result": result,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "elapsed_seconds": payload["elapsed_seconds"],
        "failure_counts": result["failure_counts"],
        "extrema": result["extrema"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
