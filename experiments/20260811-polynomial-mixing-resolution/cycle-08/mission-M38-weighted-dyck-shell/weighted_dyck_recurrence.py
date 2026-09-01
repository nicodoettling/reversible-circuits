#!/usr/bin/env python3
"""Exact weighted-Dyck recurrence for minimal identity factorizations.

The universal statement this bounded calculation can falsify is the proposed
existence, for every N, of an area threshold q whose conditional CDF lies in
[1/4,1/2].  It also checks (but cannot prove from finitely many N) candidate
polynomial lower bounds on the exact layer/CDF ratio.

Mathematically, the script evaluates a proved finite recurrence.  For a set
partition rho of [N], A_rho counts identity words all of whose transpositions
lie within rho-blocks.  The connected count is obtained by partition-lattice
Möbius inversion.  A_rho itself is computed on tuples of conjugacy classes of
the Young subgroup product_{B in rho} S_B.  All arithmetic is integral and
deterministic.

Convention: permutations are maps and pq means p after q.  Right
multiplication by the transposition (i j) therefore swaps p[i] and p[j].
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import random
import subprocess
import sys
import time
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Mapping, Sequence, Tuple


SEED = 380811
Part = Tuple[int, ...]
TypeTuple = Tuple[Part, ...]


def integer_partitions(n: int, maximum: int | None = None) -> Iterator[Part]:
    """Partitions of n in weakly decreasing order."""
    if n == 0:
        yield ()
        return
    if maximum is None or maximum > n:
        maximum = n
    for first in range(maximum, 0, -1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def dyck_paths(n: int) -> Iterator[str]:
    def rec(u: int, d: int, prefix: str) -> Iterator[str]:
        if u == n and d == n:
            yield prefix
            return
        if u < n:
            yield from rec(u + 1, d, prefix + "U")
        if d < u:
            yield from rec(u, d + 1, prefix + "D")

    yield from rec(0, 0, "")


def path_area(path: str) -> int:
    h = 0
    area = 0
    for step in path:
        h += 1 if step == "U" else -1
        if h < 0:
            raise ValueError(f"not a Dyck path: {path}")
        area += h
    if h != 0:
        raise ValueError(f"not a bridge: {path}")
    return area


def representative(cycle_type: Part) -> Tuple[int, ...]:
    """Canonical permutation with consecutive cycles of specified lengths."""
    n = sum(cycle_type)
    p = list(range(n))
    start = 0
    for length in cycle_type:
        for offset in range(length):
            p[start + offset] = start + ((offset + 1) % length)
        start += length
    return tuple(p)


def cycle_type(p: Sequence[int]) -> Part:
    seen = [False] * len(p)
    sizes: List[int] = []
    for root in range(len(p)):
        if seen[root]:
            continue
        x = root
        size = 0
        while not seen[x]:
            seen[x] = True
            size += 1
            x = p[x]
        sizes.append(size)
    return tuple(sorted(sizes, reverse=True))


@lru_cache(maxsize=None)
def class_transitions(n: int, alpha: Part) -> Tuple[Tuple[Part, int], ...]:
    """c(alpha,beta): transpositions taking a fixed alpha element to beta."""
    if sum(alpha) != n:
        raise ValueError((n, alpha))
    p = representative(alpha)
    counts: Counter[Part] = Counter()
    for i in range(n):
        for j in range(i + 1, n):
            # p after (i j): swap the two inputs of p.
            q = list(p)
            q[i], q[j] = q[j], q[i]
            counts[cycle_type(q)] += 1
    if sum(counts.values()) != n * (n - 1) // 2:
        raise AssertionError("transition row has wrong size")
    return tuple(sorted(counts.items()))


def type_rank(alpha: Part) -> int:
    return sum(alpha) - len(alpha)


def tuple_rank(state: TypeTuple) -> int:
    return sum(type_rank(alpha) for alpha in state)


def identity_state(profile: Part) -> TypeTuple:
    return tuple((1,) * size for size in profile)


def outgoing(profile: Part, state: TypeTuple) -> Iterator[Tuple[TypeTuple, int, int]]:
    """Yield (new state, multiplicity, rank increment), with exact blocks."""
    old_rank = tuple_rank(state)
    for coordinate, (size, alpha) in enumerate(zip(profile, state)):
        for beta, multiplicity in class_transitions(size, alpha):
            target = list(state)
            target[coordinate] = beta
            new_state = tuple(target)
            delta = tuple_rank(new_state) - old_rank
            if delta not in (-1, 1):
                raise AssertionError((profile, state, new_state, delta))
            yield new_state, multiplicity, delta


def restricted_path_count(profile: Part, path: str) -> int:
    """A_profile(path) for one fixed labeled Young subgroup."""
    ident = identity_state(profile)
    dp: Dict[TypeTuple, int] = {ident: 1}
    for symbol in path:
        wanted = 1 if symbol == "U" else -1
        nxt: Dict[TypeTuple, int] = defaultdict(int)
        for state, count in dp.items():
            for target, multiplicity, delta in outgoing(profile, state):
                if delta == wanted:
                    nxt[target] += count * multiplicity
        dp = dict(nxt)
    return dp.get(ident, 0)


def restricted_area_counts(profile: Part, length: int) -> Dict[int, int]:
    """A_profile by prefix-rank area, summed over all rank paths."""
    ident = identity_state(profile)
    dp: Dict[Tuple[TypeTuple, int], int] = {(ident, 0): 1}
    for _ in range(length):
        nxt: Dict[Tuple[TypeTuple, int], int] = defaultdict(int)
        for (state, area), count in dp.items():
            for target, multiplicity, _delta in outgoing(profile, state):
                nxt[(target, area + tuple_rank(target))] += count * multiplicity
        dp = dict(nxt)
    result: Dict[int, int] = {}
    for (state, area), count in dp.items():
        if state == ident:
            result[area] = result.get(area, 0) + count
    return result


def profile_multiplicity(n: int, profile: Part) -> int:
    """Number of set partitions of [n] with these block sizes."""
    denom = 1
    repeated = Counter(profile)
    for size in profile:
        denom *= math.factorial(size)
    for count in repeated.values():
        denom *= math.factorial(count)
    return math.factorial(n) // denom


def mobius_to_top(number_of_blocks: int) -> int:
    return (-1) ** (number_of_blocks - 1) * math.factorial(number_of_blocks - 1)


def connected_path_weights(n_vertices: int) -> Dict[str, int]:
    paths = list(dyck_paths(n_vertices - 1))
    total: Dict[str, int] = {path: 0 for path in paths}
    for profile in integer_partitions(n_vertices):
        coefficient = (
            profile_multiplicity(n_vertices, profile)
            * mobius_to_top(len(profile))
        )
        if coefficient == 0:
            continue
        for path in paths:
            value = restricted_path_count(profile, path)
            if value:
                total[path] += coefficient * value
    if any(value < 0 for value in total.values()):
        raise AssertionError("negative connected path count")
    return total


def connected_area_counts(n_vertices: int) -> Dict[int, int]:
    length = 2 * n_vertices - 2
    total: Dict[int, int] = defaultdict(int)
    for profile in integer_partitions(n_vertices):
        coefficient = (
            profile_multiplicity(n_vertices, profile)
            * mobius_to_top(len(profile))
        )
        if coefficient == 0:
            continue
        for area, value in restricted_area_counts(profile, length).items():
            total[area] += coefficient * value
    answer = {area: count for area, count in sorted(total.items()) if count}
    if any(value < 0 for value in answer.values()):
        raise AssertionError("negative connected area count")
    return answer


EXPECTED_PATHS: Mapping[int, Mapping[str, int]] = {
    3: {"UDUD": 6, "UUDD": 18},
    4: {
        "UDUDUD": 96,
        "UDUUDD": 264,
        "UUDDUD": 264,
        "UUDUDD": 720,
        "UUUDDD": 1536,
    },
    5: {
        "UDUDUDUD": 3000,
        "UDUDUUDD": 7800,
        "UDUUDDUD": 7800,
        "UDUUDUDD": 20160,
        "UDUUUDDD": 40440,
        "UUDDUDUD": 7800,
        "UUDDUUDD": 20280,
        "UUDUDDUD": 20160,
        "UUDUDUDD": 51960,
        "UUDUUDDD": 103800,
        "UUUDDDUD": 40440,
        "UUUDDUDD": 103800,
        "UUUDUDDD": 205560,
        "UUUUDDDD": 375000,
    },
}

EXPECTED_AREAS: Mapping[int, Mapping[int, int]] = {
    3: {2: 6, 4: 18},
    4: {3: 96, 5: 528, 7: 720, 9: 1536},
    5: {4: 3000, 6: 23400, 8: 60600, 10: 132840,
        12: 207600, 14: 205560, 16: 375000},
}


def hurwitz_total(n_vertices: int) -> int:
    # (2N-2)! N^(N-3), interpreted directly also at N=2.
    if n_vertices == 2:
        return 1
    return math.factorial(2 * n_vertices - 2) * n_vertices ** (n_vertices - 3)


def mountain_count(n_vertices: int) -> int:
    return math.factorial(n_vertices - 1) * n_vertices ** (2 * n_vertices - 4)


def quantile_summary(area_counts: Mapping[int, int]) -> Dict[str, object]:
    total = sum(area_counts.values())
    cumulative = 0
    first_quarter = None
    admissible: List[Dict[str, object]] = []
    layers: List[Dict[str, object]] = []
    for area, count in sorted(area_counts.items()):
        cumulative += count
        entry = {
            "area": area,
            "count": count,
            "cdf_num": cumulative,
            "cdf_den": total,
            "layer_over_cdf_num": count,
            "layer_over_cdf_den": cumulative,
            "cdf_float": cumulative / total,
            "layer_over_cdf_float": count / cumulative,
        }
        layers.append(entry)
        if first_quarter is None and 4 * cumulative >= total:
            first_quarter = dict(entry)
        if 4 * cumulative >= total and 2 * cumulative <= total:
            admissible.append(dict(entry))
    return {
        "total": total,
        "first_cdf_at_least_quarter": first_quarter,
        "admissible_quarter_to_half": admissible,
        "layers": layers,
    }


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        return "unavailable"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=9)
    parser.add_argument("--path-validation-max-n", type=int, default=5)
    parser.add_argument("--output", type=Path, default=Path("results.json"))
    args = parser.parse_args()
    if args.max_n < 3:
        raise SystemExit("--max-n must be at least 3")

    random.seed(SEED)
    started = time.time()
    records: List[Dict[str, object]] = []
    all_validations = True

    for n_vertices in range(3, args.max_n + 1):
        t0 = time.time()
        area_counts = connected_area_counts(n_vertices)
        total_ok = sum(area_counts.values()) == hurwitz_total(n_vertices)
        mountain_ok = area_counts.get((n_vertices - 1) ** 2) == mountain_count(n_vertices)
        area_expected_ok = (
            n_vertices not in EXPECTED_AREAS
            or area_counts == dict(EXPECTED_AREAS[n_vertices])
        )
        path_expected_ok = None
        path_area_aggregation_ok = None
        path_weights_json = None
        if n_vertices <= args.path_validation_max_n:
            path_weights = connected_path_weights(n_vertices)
            path_expected_ok = (
                n_vertices not in EXPECTED_PATHS
                or path_weights == dict(EXPECTED_PATHS[n_vertices])
            )
            aggregated: Dict[int, int] = defaultdict(int)
            for path, count in path_weights.items():
                aggregated[path_area(path)] += count
            path_area_aggregation_ok = dict(sorted(aggregated.items())) == area_counts
            path_weights_json = dict(sorted(path_weights.items()))

        checks = [total_ok, mountain_ok, area_expected_ok]
        checks.extend(
            value for value in (path_expected_ok, path_area_aggregation_ok)
            if value is not None
        )
        all_validations = all_validations and all(checks)
        records.append({
            "N": n_vertices,
            "m": 2 * n_vertices - 2,
            "area_counts": {str(k): v for k, v in area_counts.items()},
            "quantiles": quantile_summary(area_counts),
            "hurwitz_total": hurwitz_total(n_vertices),
            "mountain_count": mountain_count(n_vertices),
            "checks": {
                "hurwitz_total": total_ok,
                "mountain": mountain_ok,
                "expected_area_table": area_expected_ok,
                "expected_path_table": path_expected_ok,
                "path_area_aggregation": path_area_aggregation_ok,
            },
            "path_weights": path_weights_json,
            "elapsed_seconds": time.time() - t0,
        })
        print(
            f"N={n_vertices} layers={len(area_counts)} "
            f"total={sum(area_counts.values())} seconds={time.time()-t0:.3f}",
            flush=True,
        )

    payload = {
        "metadata": {
            "repository_commit": git_commit(),
            "command": " ".join(sys.argv),
            "python": sys.version,
            "platform": platform.platform(),
            "seed": SEED,
            "deterministic": True,
            "nonstandard_dependencies": [],
            "started_unix": started,
            "elapsed_seconds": time.time() - started,
        },
        "tested_claims": [
            "The support-partition Mobius/cycle-type recurrence reproduces the exact N=3,4,5 path and area tables.",
            "For every enumerated N there is a feasible area q with conditional CDF in [1/4,1/2].  One finite failure would refute the proposed universal threshold existence.",
            "Finite shell ratios are diagnostics only and do not prove a uniform inverse-polynomial lower bound.",
        ],
        "all_validations_passed": all_validations,
        "records": records,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    if not all_validations:
        raise SystemExit("an exact validation failed")


if __name__ == "__main__":
    main()
