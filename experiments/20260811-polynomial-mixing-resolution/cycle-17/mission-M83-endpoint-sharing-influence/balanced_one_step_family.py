#!/usr/bin/env python3
"""Focused one-step TV for the balanced-3 versus singleton-double family.

For n=3k odd, compare the cyclic orbits represented by the oriented
three-cycle (0,k,2k) and separated double (0,1)(k,2k).  These are Lambda_n
adjacent.  Kernel rows are accumulated directly over raw rank-two targets,
then quotient TV is obtained by summing each theta orbit.  This avoids the
dense quotient K^2 matrix and reaches larger n.  Arithmetic is floating but
every completion count is an exact integer before division.
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import platform
import subprocess
import sys
from pathlib import Path


Perm = tuple[int, ...]


def mul(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[i]] for i in range(len(p)))


def inv(p: Perm) -> Perm:
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def transposition(n: int, a: int, b: int) -> Perm:
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def cycle(n: int, entries: tuple[int, ...]) -> Perm:
    p = list(range(n))
    for a, b in zip(entries, entries[1:] + entries[:1]):
        p[a] = b
    return tuple(p)


def cycle_sizes(p: Perm) -> list[int]:
    seen: set[int] = set()
    out = []
    for start in range(len(p)):
        if start in seen:
            continue
        size = 0
        x = start
        while x not in seen:
            seen.add(x)
            size += 1
            x = p[x]
        out.append(size)
    return out


def count_minimal(p: Perm, r: int) -> int:
    sizes = cycle_sizes(p)
    if len(p) - len(sizes) != r:
        return 0
    out = math.factorial(r)
    for d in sizes:
        if d > 1:
            out = out * d ** (d - 2) // math.factorial(d - 1)
    return out


def theta(p: Perm, h: Perm, hi: Perm) -> Perm:
    return mul(hi, mul(p, h))


def target_kind(p: Perm) -> str:
    sizes = sorted(d for d in cycle_sizes(p) if d > 1)
    return "3" if sizes == [3] else "D"


def rank_two_targets(n: int) -> list[tuple[Perm, int]]:
    out = []
    # Positively oriented 3-cycles; multiplicity 3.
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                out.append((cycle(n, (a, b, c)), 3))
    # Both noncrossing matchings on each cyclically ordered quadruple;
    # multiplicity 2.
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                for d in range(c + 1, n):
                    out.append((mul(transposition(n, a, b), transposition(n, c, d)), 2))
                    out.append((mul(transposition(n, a, d), transposition(n, b, c)), 2))
    return out


def row(source: Perm, targets: list[tuple[Perm, int]], h: Perm, r: int) -> dict[Perm, float]:
    den = count_minimal(mul(inv(source), h), r + 2)
    out = {}
    for target, multiplicity in targets:
        numerator = multiplicity * count_minimal(mul(inv(mul(source, target)), h), r)
        if numerator:
            out[target] = numerator / den
    return out


def analyze(n: int) -> dict[str, object]:
    if n < 9 or n % 6 != 3:
        raise ValueError("this family requires n=3 mod 6 and n>=9")
    k = n // 3
    h = tuple((x + 1) % n for x in range(n))
    hi = inv(h)
    balanced = cycle(n, (0, k, 2 * k))
    double = mul(transposition(n, 0, 1), transposition(n, k, 2 * k))
    targets = rank_two_targets(n)
    first = row(balanced, targets, h, n - 5)
    second = row(double, targets, h, n - 5)
    raw_tv = 0.5 * sum(
        abs(first.get(target, 0.0) - second.get(target, 0.0))
        for target, _ in targets
    )

    orbit_id: dict[Perm, int] = {}
    orbit_rows = [collections.defaultdict(float), collections.defaultdict(float)]
    for target, _ in targets:
        if target not in orbit_id:
            orbit = []
            x = target
            while x not in orbit:
                orbit.append(x)
                x = theta(x, h, hi)
            oid = len(set(orbit_id.values()))
            for x in orbit:
                orbit_id[x] = oid
        oid = orbit_id[target]
        orbit_rows[0][oid] += first.get(target, 0.0)
        orbit_rows[1][oid] += second.get(target, 0.0)
    ids = set(orbit_rows[0]) | set(orbit_rows[1])
    tv = 0.5 * sum(abs(orbit_rows[0][i] - orbit_rows[1][i]) for i in ids)
    orbit_kind = {}
    orbit_representative = {}
    for target, _ in targets:
        orbit_kind[orbit_id[target]] = target_kind(target)
        orbit_representative.setdefault(orbit_id[target], target)
    tv_by_kind = {
        kind: 0.5 * sum(
            abs(orbit_rows[0][i] - orbit_rows[1][i])
            for i in ids if orbit_kind[i] == kind
        )
        for kind in ("3", "D")
    }
    # Quotient-invariant target events classified by residual cycle sizes.
    event_signed = collections.defaultdict(float)
    event_absolute = collections.defaultdict(float)
    for i in ids:
        key = (orbit_kind[i], tuple(sorted(cycle_sizes(mul(inv(orbit_representative[i]), h)))))
        difference = orbit_rows[0][i] - orbit_rows[1][i]
        event_signed[str(key)] += difference
        event_absolute[str(key)] += abs(difference)
    top_signed_events = sorted(
        ({"event": key, "signed_difference": value,
          "absolute_orbit_difference": event_absolute[key]}
         for key, value in event_signed.items()),
        key=lambda row: abs(row["signed_difference"]), reverse=True,
    )[:12]
    threshold_events = []
    for threshold in range(1, k + 1):
        first_probability = 0.0
        second_probability = 0.0
        for i in ids:
            if orbit_kind[i] != "D":
                continue
            sizes = sorted(cycle_sizes(mul(inv(orbit_representative[i]), h)))
            if sizes[0] == 1 and sizes[1] <= threshold:
                first_probability += orbit_rows[0][i]
                second_probability += orbit_rows[1][i]
        threshold_events.append({"second_smallest_at_most": threshold,
                                 "balanced_probability": first_probability,
                                 "singleton_double_probability": second_probability,
                                 "signed_difference": first_probability-second_probability})
    return {
        "n": n,
        "k": k,
        "raw_rank_two_targets": len(targets),
        "quotient_orbits": len(ids),
        "row_sum_balanced": sum(orbit_rows[0].values()),
        "row_sum_singleton_double": sum(orbit_rows[1].values()),
        "TV_K": tv,
        "raw_unquotiented_TV_K": raw_tv,
        "quotient_over_raw_TV_ratio": tv / raw_tv,
        "sqrt_n_times_TV_K": math.sqrt(n) * tv,
        "n_times_TV_K": n * tv,
        "TV_K_by_target_kind": tv_by_kind,
        "top_residual_size_events": top_signed_events,
        "singleton_residual_threshold_events": threshold_events,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", nargs="+", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "status": "finite_floating_diagnostic_only",
        "family": "n=3k odd: [k,k,k]_3 versus [1,k-1,k,k]_S",
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
