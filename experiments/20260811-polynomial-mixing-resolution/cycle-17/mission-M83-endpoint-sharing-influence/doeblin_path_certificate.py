#!/usr/bin/env python3
"""Exact finite audit of the M83 constructive two-hop support path.

For odd n>=9 and each quotient source g, select an adjacent oriented
three-cycle s inside a longest support gap of g.  For each target orbit,
rotate a representative away from the two singleton residual vertices of s.
The proof note shows this makes both K(g,s) and K(s,t) positive universally.
This script exhaustively verifies the construction and exact lower bounds in
finite n.  It is a certificate/falsifier, not the universal proof.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("m83", HERE / "influence_diagnostic.py")
assert SPEC is not None and SPEC.loader is not None
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def oriented_cycle(n: int, entries: tuple[int, int, int]):
    p = list(range(n))
    for a, b in zip(entries, entries[1:] + entries[:1]):
        p[a] = b
    return tuple(p)


def support(p):
    return {i for i, j in enumerate(p) if i != j}


def choose_intermediate(g):
    n = len(g)
    points = sorted(support(g))
    gaps = [((points[(i + 1) % len(points)] - points[i]) % n, points[i])
            for i in range(len(points))]
    gap, start = max(gaps)
    if gap < 3:
        raise AssertionError(("no support gap of size three", n, points, gaps))
    return oriented_cycle(n, (start, (start + 1) % n, (start + 2) % n)), start, gap


def analyze(n: int):
    h, orbits, kernel, _, _, _ = M.build(n, True)
    hi = M.inv(h)
    failures = []
    first_min = None
    second_min = None
    two_hop_min = None
    safe_rotation_max = 0
    checks = 0
    for source, orbit in enumerate(orbits):
        g = orbit[0]
        s, start, gap = choose_intermediate(g)
        # Look up the quotient orbit of s without depending on build internals.
        middle = next(i for i, members in enumerate(orbits) if s in members)
        first = kernel[source][middle]
        if first <= 0:
            failures.append({"source": source, "failure": "first hop", "gap": gap})
            continue
        first_min = first if first_min is None else min(first_min, first)
        excluded = {start, (start + 1) % n}
        for target, members in enumerate(orbits):
            t = members[0]
            rotations = 0
            while support(t) & excluded:
                t = M.theta(t, h, hi)
                rotations += 1
                if rotations >= n:
                    break
            safe_rotation_max = max(safe_rotation_max, rotations)
            if support(t) & excluded:
                failures.append({"source": source, "target": target,
                                 "failure": "no safe rotation"})
                continue
            # The quotient row entry includes this raw target term; verify its
            # exact raw conditional probability directly.
            den = M.count_minimal(M.mul(M.inv(s), h), n - 3)
            multiplicity = 3 if M.kind(t) == "3" else 2
            raw_second = Fraction(
                multiplicity * M.count_minimal(M.mul(M.inv(M.mul(s, t)), h), n - 5),
                den,
            )
            if raw_second <= 0:
                failures.append({"source": source, "target": target,
                                 "failure": "second hop after safe rotation"})
                continue
            second_min = raw_second if second_min is None else min(second_min, raw_second)
            product = first * raw_second
            two_hop_min = product if two_hop_min is None else min(two_hop_min, product)
            checks += 1
    bound = Fraction(32, 9 * n ** 14)
    return {
        "n": n,
        "quotient_states": len(orbits),
        "source_target_checks": checks,
        "construction_failures": failures,
        "maximum_rotations_to_safe_target": safe_rotation_max,
        "minimum_first_quotient_hop_exact": str(first_min),
        "minimum_selected_raw_second_hop_exact": str(second_min),
        "minimum_selected_two_hop_product_exact": str(two_hop_min),
        "proved_formula_lower_bound": str(bound),
        "finite_check_exceeds_formula_bound": two_hop_min >= bound,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", nargs="+", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "status": "exact_finite_certificate_only",
        "claim_tested": "constructive adjacent-triangle two-hop support path",
        "convention": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "repository_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": " ".join(sys.argv),
        "results": [analyze(n) for n in args.n],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
