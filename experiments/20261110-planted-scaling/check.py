#!/usr/bin/env python3
"""Exact return counts and certified bounds for a random-pair distinguisher."""
from collections import Counter
from fractions import Fraction
from functools import cache
import hashlib
import gzip
import json
import math
from pathlib import Path
import platform
import subprocess
import sys
import time


def partitions(n, cap=None):
    if not n:
        yield ()
        return
    for first in range(min(n, cap if cap is not None else n), 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


@cache
def dimension(shape):
    if not shape:
        return 1
    result = 0
    for i, length in enumerate(shape):
        if i + 1 < len(shape) and shape[i + 1] == length:
            continue
        smaller = list(shape)
        smaller[i] -= 1
        result += dimension(tuple(x for x in smaller if x))
    return result


class Spectrum:
    def __init__(self, n):
        self.n, self.q = n, math.comb(n, 2)
        self.factorial = math.factorial(n)
        self.weights = Counter()
        self.shapes = 0
        for shape in partitions(n):
            self.shapes += 1
            content = sum(length * (length - 2 * i - 1)
                          for i, length in enumerate(shape)) // 2
            self.weights[content] += dimension(shape) ** 2
        assert sum(self.weights.values()) == self.factorial
        assert self.weights[self.q] == self.weights[-self.q] == 1

    @cache
    def trace(self, length):
        return sum(weight * eigenvalue ** length
                   for eigenvalue, weight in self.weights.items())

    def count(self, length):
        quotient, remainder = divmod(self.trace(length), self.factorial)
        assert not remainder
        return quotient

    def delta(self, length):
        assert length >= 0 and length % 2 == 0
        value = Fraction(self.trace(length), 2 * self.q ** length) - 1
        assert value >= 0
        return value


def cycle_transitions(shape):
    result = Counter()
    for i, a in enumerate(shape):
        for j in range(i + 1, len(shape)):
            b = shape[j]
            nxt = tuple(sorted([x for h, x in enumerate(shape) if h not in (i, j)]
                               + [a + b], reverse=True))
            result[nxt] += a * b
        for d in range(1, a // 2 + 1):
            nxt = tuple(sorted([x for h, x in enumerate(shape) if h != i]
                               + [d, a - d], reverse=True))
            result[nxt] += a if 2 * d < a else a // 2
    return result


def independent_counts(n, maximum):
    transitions = {shape: cycle_transitions(shape) for shape in partitions(n)}
    assert all(sum(row.values()) == math.comb(n, 2) for row in transitions.values())
    identity = (1,) * n
    values = Counter({identity: 1})
    answer = [1]
    for _ in range(maximum):
        nxt = Counter()
        for shape, count in values.items():
            for target, weight in transitions[shape].items():
                nxt[target] += count * weight
        values = nxt
        answer.append(values[identity])
    return answer


def moment_bound(r):
    if r == 1:
        return Fraction(1)
    return max(Fraction(2 * r * r - 4 * r + 3),
               Fraction(12 * r * r - 8 * r + 5, 8),
               Fraction(2 * r * r + r, 2))


def check_radial_rows(r):
    # Bound b_i*b_j by (2i+1)(2j+1)/8, b_h=sqrt(h(h+1)/2).
    # Calculate every row of the squared tridiagonal using rational products.
    if r == 1:
        return True
    rows = []
    for h in range(r + 1):
        value = Fraction(0)
        for j in (h - 1, h + 1):
            if not 0 <= j <= r:
                continue
            first_edge = max(h, j)
            for ell in (j - 1, j + 1):
                if 0 <= ell <= r:
                    second_edge = max(j, ell)
                    value += Fraction((2 * first_edge + 1) * (2 * second_edge + 1), 8)
        rows.append(value)
    assert max(rows) <= moment_bound(r)
    return True


def rational(value):
    return {"exact": str(value), "decimal": float(value)}


def main():
    sys.set_int_max_str_digits(0)
    started = time.monotonic()
    directory = Path(__file__).resolve().parent
    result = {"metadata": {
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": "python3 -B experiments/20261110-planted-scaling/check.py",
        "python": platform.python_version(), "dependencies": "standard library only",
        "random_seed": None, "randomness": "none; deterministic exact integer/rational arithmetic",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }, "independent_checks": [], "cases": []}
    for n in range(2, 9):
        spectrum = Spectrum(n)
        reference = independent_counts(n, 2 * n)
        assert reference == [spectrum.count(r) for r in range(2 * n + 1)]
        result["independent_checks"].append({"N": n, "lengths": list(range(2 * n + 1)),
                                              "return_counts": reference, "passed": True})
    assert Spectrum(3).count(4) == 27
    assert Spectrum(4).count(4) == 120
    assert Spectrum(4).count(6) == 3936
    for r in range(1, 501):
        assert check_radial_rows(r)
        if r >= 6:
            assert moment_bound(r) == 2 * r * r - 4 * r + 3
            assert moment_bound(r) < math.comb(2 * r, 2)
    result["radial_row_checks"] = {"r_min": 1, "r_max": 500, "passed": True}
    prior = directory.parent / "20261110-planted-subsequence"
    prior_summary = json.loads((prior / "results.json").read_text())
    prior_histograms = json.loads(gzip.decompress((prior / "feature-histograms.json.gz").read_bytes()))
    result["literal_law_comparisons"] = []
    for item in prior_summary["sweep"]:
        n, m = item["N"], item["m"]
        spectrum = Spectrum(n)
        features = next(row for row in prior_histograms if (row["N"], row["m"]) == (n, m))
        histogram = features["feature_histograms"]["repeat_pairs"]
        for case in item["cases"]:
            k = case["k"]
            z = case["bridge_count"]
            total = sum(row["planted_numerators_by_k"][str(k)] for row in histogram)
            null_mean = Fraction(sum(row["value"] * row["null_count"] for row in histogram), z)
            planted_mean = Fraction(sum(row["value"] * row["planted_numerators_by_k"][str(k)]
                                        for row in histogram), total)
            actual_gap = (planted_mean - null_mean) / math.comb(m, 2)
            b = Fraction(spectrum.q * spectrum.count(k - 2), spectrum.count(k))
            ideal_gap = Fraction(math.comb(k, 2), math.comb(m, 2)) * (b - Fraction(1, spectrum.q))
            delta = spectrum.delta(m - k - 2)
            if delta < 1:
                error = 8 * delta / (1 - delta) ** 2
                assert abs(actual_gap - ideal_gap) <= error
                result["literal_law_comparisons"].append({"N": n, "m": m, "k": k,
                    "actual_gap": rational(actual_gap), "ideal_gap": rational(ideal_gap),
                    "error_bound": rational(error), "passed": True})
    result["metadata"]["prior_results_sha256"] = hashlib.sha256((prior / "results.json").read_bytes()).hexdigest()
    result["metadata"]["prior_histograms_sha256"] = hashlib.sha256((prior / "feature-histograms.json.gz").read_bytes()).hexdigest()
    for n in (4, 6, 8, 12, 16, 24, 32):
        spectrum = Spectrum(n)
        log = (n - 1).bit_length()
        options = {"linear": n, "log": 2 * math.ceil(log / 2),
                   "log_squared": 2 * math.ceil(log * log / 2)}
        for schedule, k in options.items():
            b = Fraction(spectrum.q * spectrum.count(k - 2), spectrum.count(k))
            bound = moment_bound(k // 2)
            assert b >= 1 / bound
            for host in ("quadratic", "linear"):
                m = n * n if host == "quadratic" else n
                row = {"N": n, "m": m, "k": k, "host": host, "plant": schedule,
                       "partition_count": spectrum.shapes,
                       "plant_pair_equality": rational(b), "pair_ratio_lower_bound": rational(1 / bound)}
                if k >= m:
                    row["status"] = "trivial planting" if k == m else "infeasible k>m"
                    result["cases"].append(row)
                    continue
                suffix = m - k - 2
                row["expected_null_witnesses"] = rational(Fraction(
                    math.comb(m, k) * spectrum.count(k) * spectrum.count(m - k),
                    spectrum.count(m)))
                delta = spectrum.delta(suffix)
                inclusion = Fraction(math.comb(k, 2), math.comb(m, 2))
                ideal_gap = inclusion * (b - Fraction(1, spectrum.q))
                row["suffix"] = suffix
                row["delta_suffix"] = rational(delta)
                row["ideal_pair_advantage"] = rational(ideal_gap)
                row["null_pair_equality"] = rational(Fraction(spectrum.q * spectrum.count(m - 2), spectrum.count(m)))
                if delta < 1:
                    error = 8 * delta / (1 - delta) ** 2
                    pair_lower = ideal_gap - error
                    degree_lower = (inclusion * (Fraction(1, k - 1) - Fraction(2, n)) - error)
                    row["comparison_error_bound"] = rational(error)
                    row["certified_pair_advantage_lower_bound"] = rational(pair_lower)
                    row["certified_label_advantage_lower_bound"] = rational(degree_lower)
                    row["status"] = "positive attack certificate" if max(pair_lower, degree_lower) > 0 else "bound inconclusive"
                else:
                    row["status"] = "smoothing bound unavailable (delta>=1)"
                result["cases"].append(row)
                print(json.dumps({"N": n, "m": m, "k": k, "status": row["status"],
                                  "pair_advantage_lower": row.get("certified_pair_advantage_lower_bound", {}).get("decimal"),
                                  "delta": float(delta)}), flush=True)
    result["metadata"]["seconds"] = time.monotonic() - started
    (directory / "results.json").write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
