#!/usr/bin/env python3
"""Exact bounded audit of the contextual-variance supersolution route.

The pointwise contextual observables are reconstructed from the accepted
small parking-macro harness.  The M90 grouped resolvent is independent exact
code in this directory.  Empty failure lists are finite falsification data,
not proofs of the displayed universal inequalities.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import importlib.util
import json
import platform
import time
from fractions import Fraction
from pathlib import Path

import exact_weighted_resolvent as EXACT


def load_contextual_harness():
    source = Path(__file__).resolve().parents[2] / (
        "cycle-13/mission-M56-marked-root-history-flow/"
        "recursive_contextual_locality.py"
    )
    spec = importlib.util.spec_from_file_location("m56_contextual", source)
    if spec is None or spec.loader is None:
        raise RuntimeError(source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M56 = load_contextual_harness()


def fraction_record(value: Fraction) -> dict[str, object]:
    return {
        "decimal": float(value),
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


class ContextualAudit:
    def __init__(self, ambient_max: int):
        self.ambient_max = ambient_max
        self.tables = {
            ambient: M56.contextual_tables(ambient)[0]
            for ambient in range(3, ambient_max + 1)
        }
        self.resolvent = EXACT.ExactResolvent()

    @functools.lru_cache(maxsize=None)
    def pointwise(self, s: int, K: int, R: int, B: int):
        ambient = s + K
        if not 3 <= ambient <= self.ambient_max:
            raise ValueError((s, K, R, B, ambient))
        index = K - R - 1
        coarse = (1,) * index + (s + 1,) + (1,) * R
        refined = coarse[:index] + (s + 1 - B, B) + coarse[index + 1 :]
        context = next(
            row
            for row in self.tables[ambient]
            if row["coarse"] == coarse
            and row["refined"] == refined
            and row["branch_index"] == index
        )
        rows = []
        for macro, values in context["values_by_local"].items():
            if len(values) != 1:
                raise AssertionError((s, K, R, B, macro, values))
            value = next(iter(values))
            weight = Fraction(M56.M50.M41.BASE.orbit_weight(macro))
            rows.append((weight, value))
        normalization = sum((weight for weight, _ in rows), Fraction())
        return tuple((weight / normalization, value) for weight, value in rows)

    @functools.lru_cache(maxsize=None)
    def variance(self, s: int, K: int, R: int, B: int) -> Fraction:
        rows = self.pointwise(s, K, R, B)
        mean = sum((weight * value for weight, value in rows), Fraction())
        expected = EXACT.q_split(s, B)
        if mean != expected:
            raise AssertionError((s, K, R, B, mean, expected))
        return sum(
            (weight * (value - mean) ** 2 for weight, value in rows),
            Fraction(),
        )

    def one_step(self, s: int, K: int, R: int, B: int):
        reset = EXACT.reset_budget(s, K, R, B)
        continuation = Fraction(0)
        parent_phase = s + K - R
        child_count = 0
        for k, t, mass in EXACT.groups(s):
            if t <= B or t - 1 < 2:
                continue
            for j in range(1, k + 1):
                probability = EXACT.nu(K, R, k, j)
                if not probability:
                    continue
                child = (t - 1, K + k, R + j, B)
                if sum((child[0], child[1], -child[2])) >= parent_phase:
                    raise AssertionError((s, K, R, B, child))
                if child[0] + child[1] > self.ambient_max:
                    raise AssertionError(("ambient closure", child))
                continuation += mass * probability * self.variance(*child)
                child_count += 1
        parent = self.variance(s, K, R, B)
        return reset, continuation, parent, child_count


def scan(ambient_max: int) -> dict[str, object]:
    audit = ContextualAudit(ambient_max)
    counts = {
        "contexts": 0,
        "right_heavy_contexts": 0,
        "one_step_children": 0,
    }
    failures = {
        "resolvent_over_contextual_variance": [],
        "one_step_contextual_variance": [],
        "beta_binomial_variance_envelope": [],
        "right_heavy_pointwise_unit_interval": [],
    }
    maxima: dict[str, tuple[Fraction, dict[str, object]] | None] = {
        "resolvent_over_contextual_variance": None,
        "one_step_contextual_variance": None,
        "variance_over_beta_binomial_envelope": None,
    }

    def update(name: str, ratio: Fraction, row: dict[str, object]) -> None:
        current = maxima[name]
        if current is None or ratio > current[0]:
            maxima[name] = (ratio, row)

    for ambient in range(3, ambient_max + 1):
        for s in range(2, ambient):
            K = ambient - s
            for R in range(K):
                for B in range(1, s + 1):
                    x = (s, K, R, B)
                    counts["contexts"] += 1
                    q = EXACT.q_split(s, B)
                    variance = audit.variance(*x)
                    g = audit.resolvent.g(*x)
                    envelope = q * (1 - q) * Fraction(K, R + 1)
                    reset, continuation, parent, child_count = audit.one_step(*x)
                    counts["one_step_children"] += child_count
                    one_step = reset + continuation
                    row = {
                        "ambient": ambient,
                        "context": list(x),
                        "q": fraction_record(q),
                        "variance": fraction_record(variance),
                        "transformed_resolvent": fraction_record(g),
                        "beta_binomial_envelope": fraction_record(envelope),
                        "reset_budget": fraction_record(reset),
                        "continuation_variance_budget": fraction_record(continuation),
                        "one_step_total": fraction_record(one_step),
                        "one_step_margin": fraction_record(parent - one_step),
                    }
                    if variance:
                        update(
                            "resolvent_over_contextual_variance",
                            g / variance,
                            row,
                        )
                        update(
                            "one_step_contextual_variance",
                            one_step / variance,
                            row,
                        )
                    if envelope:
                        update(
                            "variance_over_beta_binomial_envelope",
                            variance / envelope,
                            row,
                        )
                    if g > variance:
                        failures["resolvent_over_contextual_variance"].append(row)
                    if one_step > variance:
                        failures["one_step_contextual_variance"].append(row)
                    if variance > envelope:
                        failures["beta_binomial_variance_envelope"].append(row)
                    if R == K - 1:
                        counts["right_heavy_contexts"] += 1
                        values = [value for _, value in audit.pointwise(*x)]
                        if min(values) < 0 or max(values) > 1:
                            failures["right_heavy_pointwise_unit_interval"].append({
                                **row,
                                "minimum": str(min(values)),
                                "maximum": str(max(values)),
                            })

    def maximum_record(name: str) -> dict[str, object]:
        ratio, row = maxima[name]
        return {"ratio": fraction_record(ratio), "row": row}

    return {
        "counts": counts,
        "failure_counts": {key: len(rows) for key, rows in failures.items()},
        "first_failures": {key: rows[:3] for key, rows in failures.items()},
        "maxima": {name: maximum_record(name) for name in maxima},
        "resolvent_memoized_contexts": audit.resolvent.contexts,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ambient-max", type=int, default=7)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 3 <= args.ambient_max <= 7:
        raise SystemExit("accepted exact macro harness supports 3<=ambient-max<=7")
    started = time.time()
    result = scan(args.ambient_max)
    payload = {
        "claim_tested": (
            "g=q K_reset W <= Var(Phi), its one-step variance supersolution, "
            "and the beta-binomial variance envelope"
        ),
        "finite_scope_warning": "Exact bounded survival proves no universal inequality.",
        "arithmetic": "fractions.Fraction exact parking-macro enumeration",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "parameters": {"ambient_max": args.ambient_max},
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
    }, sort_keys=True))


if __name__ == "__main__":
    main()
