#!/usr/bin/env python3
"""Exact second-moment recursion for contextual suffix observables.

M65's pointwise inheritance closes not only first moments but mixed second
moments.  For two attachment contexts ``a=(K,R)`` and ``b=(L,S)`` at the
same local rank and suffix size, condition on root part count ``k`` and last
part ``t``.  At ``t=B`` both observables are constant.  At ``t>B`` expand
both exact negative-hypergeometric mixtures on the same child macro.  This
gives an exact rank-descending recursion for ``E[Phi_a Phi_b]``.

The script uses that recursion to falsify the proposed contextual-variance
supersolution beyond the ranks available to direct macro enumeration.  A
finite pass remains non-theorem evidence.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import platform
import time
from fractions import Fraction
from pathlib import Path

import exact_weighted_resolvent as EXACT


def ordered_pair(K: int, R: int, L: int, S: int) -> tuple[int, int, int, int]:
    if (L, S) < (K, R):
        return L, S, K, R
    return K, R, L, S


class SecondMoment:
    def __init__(self) -> None:
        self.calls = 0
        self.pair_terms = 0

    def moment(
        self, s: int, K: int, R: int, L: int, S: int, B: int
    ) -> Fraction:
        K, R, L, S = ordered_pair(K, R, L, S)
        return self._moment(s, K, R, L, S, B)

    @functools.lru_cache(maxsize=None)
    def _moment(
        self, s: int, K: int, R: int, L: int, S: int, B: int
    ) -> Fraction:
        if s == 1:
            if B != 1:
                raise AssertionError((s, K, R, L, S, B))
            # The unique local macro has terminal statistic identically one.
            return Fraction(1)
        if s < 1:
            return Fraction(0)
        self.calls += 1
        answer = Fraction(0)
        parent_phase_a = s + K - R
        parent_phase_b = s + L - S
        for k, t, mass in EXACT.groups(s):
            if t < B:
                continue
            if t == B:
                left = EXACT.contextual_value(k, t, K, R, B)
                right = EXACT.contextual_value(k, t, L, S, B)
                answer += mass * left * right
                continue
            if t - 1 < 1:
                continue
            for j in range(1, k + 1):
                left_probability = EXACT.nu(K, R, k, j)
                if not left_probability:
                    continue
                left_child = (t - 1, K + k, R + j)
                if left_child[0] + left_child[1] - left_child[2] >= parent_phase_a:
                    raise AssertionError(("left phase", s, K, R, k, t, j))
                for ell in range(1, k + 1):
                    right_probability = EXACT.nu(L, S, k, ell)
                    if not right_probability:
                        continue
                    right_child = (t - 1, L + k, S + ell)
                    if (
                        right_child[0] + right_child[1] - right_child[2]
                        >= parent_phase_b
                    ):
                        raise AssertionError(("right phase", s, L, S, k, t, ell))
                    self.pair_terms += 1
                    answer += (
                        mass
                        * left_probability
                        * right_probability
                        * self.moment(
                            t - 1,
                            left_child[1],
                            left_child[2],
                            right_child[1],
                            right_child[2],
                            B,
                        )
                    )
        return answer

    @functools.lru_cache(maxsize=None)
    def variance(self, s: int, K: int, R: int, B: int) -> Fraction:
        q = EXACT.q_split(s, B)
        return self.moment(s, K, R, K, R, B) - q * q


def fraction_record(value: Fraction) -> dict[str, object]:
    return {
        "decimal": float(value),
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def scan(s_max: int, k_max: int) -> dict[str, object]:
    moments = SecondMoment()
    resolvent = EXACT.ExactResolvent()
    failures = {
        "mean_or_variance_sanity": [],
        "one_step_variance_supersolution": [],
        "resolvent_over_variance": [],
        "beta_binomial_variance_envelope": [],
    }
    maxima: dict[str, tuple[Fraction, dict[str, object]] | None] = {
        "one_step_over_variance": None,
        "resolvent_over_variance": None,
        "variance_over_envelope": None,
    }
    contexts = 0

    def update(name: str, ratio: Fraction, row: dict[str, object]) -> None:
        current = maxima[name]
        if current is None or ratio > current[0]:
            maxima[name] = (ratio, row)

    for s in range(2, s_max + 1):
        for K in range(1, k_max + 1):
            for R in range(K):
                if R == 0 and K > 1:
                    continue
                for B in range(1, s + 1):
                    contexts += 1
                    x = (s, K, R, B)
                    q = EXACT.q_split(s, B)
                    variance = moments.variance(*x)
                    reset = EXACT.reset_budget(*x)
                    continuation = Fraction(0)
                    for k, t, mass in EXACT.groups(s):
                        if t <= B or t - 1 < 2:
                            continue
                        for j in range(1, k + 1):
                            probability = EXACT.nu(K, R, k, j)
                            if probability:
                                continuation += mass * probability * moments.variance(
                                    t - 1, K + k, R + j, B
                                )
                    one_step = reset + continuation
                    g = resolvent.g(*x)
                    envelope = q * (1 - q) * Fraction(K, R + 1)
                    row = {
                        "context": list(x),
                        "q": fraction_record(q),
                        "variance": fraction_record(variance),
                        "reset_budget": fraction_record(reset),
                        "continuation_variance_budget": fraction_record(continuation),
                        "one_step_total": fraction_record(one_step),
                        "one_step_margin": fraction_record(variance - one_step),
                        "transformed_resolvent": fraction_record(g),
                        "beta_binomial_envelope": fraction_record(envelope),
                    }
                    if variance < 0 or variance > envelope * 4:
                        failures["mean_or_variance_sanity"].append(row)
                    if variance:
                        update("one_step_over_variance", one_step / variance, row)
                        update("resolvent_over_variance", g / variance, row)
                    if envelope:
                        update("variance_over_envelope", variance / envelope, row)
                    if one_step > variance:
                        failures["one_step_variance_supersolution"].append(row)
                    if g > variance:
                        failures["resolvent_over_variance"].append(row)
                    if variance > envelope:
                        failures["beta_binomial_variance_envelope"].append(row)

    # Independent exact direct-macro calibration values from the M90 audit.
    calibrations = [
        ((5, 2, 1, 2), Fraction(10981, 131220)),
        ((6, 1, 0, 3), Fraction(24731355, 282475249)),
    ]
    calibration_rows = []
    for context, expected in calibrations:
        observed = moments.variance(*context)
        calibration_rows.append({
            "context": list(context),
            "expected": fraction_record(expected),
            "observed": fraction_record(observed),
            "exact_match": observed == expected,
        })
        if observed != expected:
            failures["mean_or_variance_sanity"].append(calibration_rows[-1])

    return {
        "contexts": contexts,
        "failure_counts": {key: len(rows) for key, rows in failures.items()},
        "first_failures": {key: rows[:3] for key, rows in failures.items()},
        "maxima": {
            name: {"ratio": fraction_record(item[0]), "row": item[1]}
            for name, item in maxima.items()
        },
        "direct_macro_calibrations": calibration_rows,
        "memoized_mixed_moment_contexts": moments.calls,
        "mixed_pair_terms_visited": moments.pair_terms,
        "memoized_resolvent_contexts": resolvent.contexts,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=8)
    parser.add_argument("--k-max", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    result = scan(args.s_max, args.k_max)
    payload = {
        "claim_tested": (
            "exact contextual second-moment recurrence and the variance "
            "supersolution g<=Var(Phi)"
        ),
        "finite_scope_warning": "Exact bounded survival proves no universal inequality.",
        "arithmetic": "fractions.Fraction exact grouped mixed moments",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "parameters": {"s_max": args.s_max, "k_max": args.k_max},
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
        "maxima": result["maxima"],
        "calibrations": result["direct_macro_calibrations"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
