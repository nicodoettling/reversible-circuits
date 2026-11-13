#!/usr/bin/env python3
"""Independent literal counting of the S4,m8,k4 result; no check.py imports."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import hashlib
import json
import math
from pathlib import Path
import platform
import subprocess
import time


def evaluate(word, n):
    p = list(range(n))
    for a, b in word:
        p[a], p[b] = p[b], p[a]
    return tuple(p)


def main():
    started = time.monotonic()
    directory = Path(__file__).resolve().parent
    data = json.loads((directory / "results.json").read_text())
    n, m, k = 4, 8, 4
    edges = tuple(combinations(range(n), 2))
    identity = tuple(range(n))
    last_edges = {evaluate((edge,), n): edge for edge in edges}
    subsets = tuple(combinations(range(m), k))
    histogram = Counter()
    accepted_null = accepted_plant = total_plant = 0
    # Fix the first gate. Conjugation makes all six choices equally numerous
    # for these invariant observables; do not quotient the remaining labels.
    for tail in product(edges, repeat=m - 2):
        prefix = (edges[0],) + tail
        endpoint = evaluate(prefix, n)
        if endpoint not in last_edges:
            continue
        word = prefix + (last_edges[endpoint],)
        assert evaluate(word, n) == identity
        witnesses = sum(evaluate(tuple(word[i] for i in positions), n) == identity
                        for positions in subsets)
        histogram[witnesses] += len(edges)
        total_plant += len(edges) * witnesses
        repeats = sum(x * (x - 1) // 2 for x in Counter(word).values())
        if repeats > 6:
            accepted_null += len(edges)
            accepted_plant += len(edges) * witnesses
    total = sum(histogram.values())
    recorded = next(c for row in data["sweep"] for c in row["cases"]
                    if (c["N"], c["m"], c["k"]) == (n, m, k))
    assert dict(histogram) == dict(recorded["witness_histogram"])
    assert total == 140160
    tv = Fraction(sum(count * abs(total * x - total_plant)
                      for x, count in histogram.items()), 2 * total * total_plant)
    attack = Fraction(accepted_plant, total_plant) - Fraction(accepted_null, total)
    assert str(tv) == recorded["total_variation"]["exact"]
    assert str(attack) == recorded["repeat_pair_threshold"]["advantage"]["exact"]
    # Verify the complete support-size bound's extremal coefficient by a
    # different counting formula: disjoint edges, each used exactly twice.
    universal = next(row for row in data["sweep"] if (row["N"], row["m"]) == (8, 8))
    leading = math.factorial(8) ** 2 // (4 ** 4 * math.factorial(4))
    for case in universal["cases"]:
        top = [(x, count) for v, x, count in case["support_witness_coefficients"] if v == 8]
        assert top == [(math.comb(4, case["k"] // 2), leading)]
    result = {
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": "python3 -B experiments/20261110-planted-subsequence/audit.py",
        "python": platform.python_version(), "dependencies": "standard library only",
        "randomness": "none; deterministic independent enumeration",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "N": n, "m": m, "k": k, "bridge_count": total,
        "histogram": sorted(histogram.items()), "TV": str(tv),
        "repeat_pair_attack": {"condition": "repeat pairs > 6",
                               "null_acceptance": str(Fraction(accepted_null, total)),
                               "planted_acceptance": str(Fraction(accepted_plant, total_plant)),
                               "advantage": str(attack)},
        "universal_m8_leading_coefficient": leading,
        "seconds": time.monotonic() - started,
        "status": "all assertions passed; same-agent independent implementation, not independent proof review",
    }
    (directory / "audit-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
