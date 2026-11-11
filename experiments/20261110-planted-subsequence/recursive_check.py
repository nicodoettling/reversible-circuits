#!/usr/bin/env python3
"""Exact law of recursive inverse-Hurwitz planting, with a chosen exact base."""
from collections import Counter
from fractions import Fraction
from functools import cache
from itertools import combinations, product
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import time

from check import Group


def main():
    started = time.monotonic()
    directory = Path(__file__).resolve().parent
    baseline = json.loads((directory / "results.json").read_text())
    result = {"metadata": {
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": "python3 -B experiments/20261110-planted-subsequence/recursive_check.py",
        "python": platform.python_version(), "dependencies": "standard library; imports check.Group",
        "randomness": "none; exact enumeration of all recursive generation choices",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "check_sha256": hashlib.sha256((directory / "check.py").read_bytes()).hexdigest(),
    }, "cases": []}
    for n in (3, 4):
        group = Group(n, 8)
        for base in (2, 4):
            @cache
            def law(length):
                if length <= base:
                    words = Counter({word: 1 for word in product(range(len(group.edges)), repeat=length)
                                     if group.evaluate(word) == group.identity})
                    return words, len(words)
                k = 2 * (length // 4)
                left, left_denominator = law(k)
                right, right_denominator = law(length - k)
                positions = list(combinations(range(length), k))
                words = Counter()
                for a, ca in left.items():
                    for b, cb in right.items():
                        for indices in positions:
                            words[group.unplant(a, b, indices)] += ca * cb
                denominator = left_denominator * right_denominator * len(positions)
                assert sum(words.values()) == denominator
                assert all(group.evaluate(word) == group.identity for word in words)
                return words, denominator
            for length in (4, 6, 8):
                words, denominator = law(length)
                z = group.completions[length][group.identity]
                missing = z - len(words)
                histogram = Counter(words.values())
                if missing:
                    histogram[0] = missing
                tv = Fraction(sum(count * abs(weight * z - denominator)
                                  for weight, count in histogram.items()), 2 * z * denominator)
                k = 2 * (length // 4)
                top_only = next(c for row in baseline["sweep"] for c in row["cases"]
                                if (c["N"], c["m"], c["k"]) == (n, length, k))
                if length <= base:
                    assert tv == 0
                elif length <= 2 * base:
                    assert str(tv) == top_only["total_variation"]["exact"]
                row = {"N": n, "m": length, "exact_base_max_length": base,
                       "bridge_count": z, "generation_denominator": denominator,
                       "missing_words": missing, "TV": str(tv), "TV_decimal": float(tv),
                       "one_top_plant_TV": top_only["total_variation"],
                       "generation_weight_histogram": sorted(histogram.items())}
                result["cases"].append(row)
                print(json.dumps({k: v for k, v in row.items()
                                  if k != "generation_weight_histogram"}), flush=True)
    result["metadata"]["seconds"] = time.monotonic() - started
    (directory / "recursive-results.json").write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
