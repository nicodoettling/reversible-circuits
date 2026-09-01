#!/usr/bin/env python3
"""Deterministic/exact validation and fixed-seed sampler smoke tests."""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import subprocess
import time
from collections import Counter, defaultdict
from math import comb
from pathlib import Path
from random import Random

from star_bridge import (
    active_base_cycle_type,
    all_pointed_types,
    compose,
    cycle_type,
    evaluate_star_word,
    feasible_star_bridge,
    identity,
    minimal_star_length,
    orbit_dp_tables,
    pointed_type,
    pointed_type_transitions,
    sample_star_bridge,
    star_bridge_count,
    star_transposition,
    transitive_star_count,
)


def all_permutations(n: int):
    yield from itertools.permutations(range(n))


def direct_endpoint_tables(n: int, max_k: int):
    table = {identity(n): 1}
    tables = [table]
    for _ in range(max_k):
        nxt = defaultdict(int)
        for p, count in table.items():
            for lower in range(n - 1):
                nxt[compose(p, star_transposition(n, lower))] += count
        table = dict(nxt)
        tables.append(table)
    return tables


def exact_checks(max_n: int, max_k: int):
    summaries = []
    total_endpoint_checks = 0
    total_recurrence_checks = 0
    total_orbit_transition_checks = 0
    for n in range(1, max_n + 1):
        direct = direct_endpoint_tables(n, max_k)
        orbit = orbit_dp_tables(n, max_k)
        perms = list(all_permutations(n))
        for state in all_pointed_types(n):
            assert sum(pointed_type_transitions(state).values()) == n - 1
        for p in perms:
            for k in range(max_k + 1):
                expected = direct[k].get(p, 0)
                formula = star_bridge_count(n, k, p)
                orbit_count = orbit[k][pointed_type(p)]
                assert formula == expected, (n, k, p, formula, expected)
                assert orbit_count == expected, (n, k, p, orbit_count, expected)
                assert feasible_star_bridge(n, k, p) == (expected > 0), (n, k, p)
                total_endpoint_checks += 1
                if k:
                    rhs = sum(
                        star_bridge_count(
                            n, k - 1, compose(p, star_transposition(n, lower))
                        )
                        for lower in range(n - 1)
                    )
                    assert formula == rhs, (n, k, p, formula, rhs)
                    total_recurrence_checks += 1
        # Check the claimed orbit transition multiplicities against every
        # labeled representative, not merely against one canonical example.
        for p in perms:
            actual = Counter(
                pointed_type(compose(p, star_transposition(n, lower)))
                for lower in range(n - 1)
            )
            claimed = pointed_type_transitions(pointed_type(p))
            assert actual == claimed, (n, p, actual, claimed)
            total_orbit_transition_checks += 1
        summaries.append(
            {
                "N": n,
                "max_k": max_k,
                "permutations": len(perms),
                "pointed_states": len(all_pointed_types(n)),
                "total_words_at_max_k": sum(direct[max_k].values()),
                "reachable_endpoints_by_k": [len(x) for x in direct],
            }
        )
    return {
        "case_summaries": summaries,
        "endpoint_count_equalities": total_endpoint_checks,
        "last_factor_recurrence_equalities": total_recurrence_checks,
        "labeled_orbit_transition_equalities": total_orbit_transition_checks,
    }


def boundary_checks():
    out = []
    # N=1: no generator.
    for k in range(5):
        q = identity(1)
        out.append(
            {
                "name": f"N1_identity_k{k}",
                "count": star_bridge_count(1, k, q),
                "feasible": feasible_star_bridge(1, k, q),
                "minimum": minimal_star_length(q),
            }
        )
    # N=2: the only word is forced by parity.
    s = star_transposition(2, 0)
    for q_name, q in [("identity", identity(2)), ("star", s)]:
        for k in range(7):
            out.append(
                {
                    "name": f"N2_{q_name}_k{k}",
                    "count": star_bridge_count(2, k, q),
                    "feasible": feasible_star_bridge(2, k, q),
                    "minimum": minimal_star_length(q),
                }
            )
    return out


def partition_state_growth(ranks=(1, 2, 3, 4, 5, 10, 20, 50, 100)):
    """Exact |S_N/S_(N-1)-conjugacy| = sum_{u=0}^{N-1} p(u)."""
    out = []
    for n in ranks:
        p = [0] * n
        p[0] = 1
        for part in range(1, n):
            for total in range(part, n):
                p[total] += p[total - part]
        out.append(
            {
                "N": n,
                "pointed_state_count": sum(p),
                "p_N_minus_1": p[-1],
            }
        )
    return out


def support_decomposition_examples():
    fixtures = [
        (4, 6, identity(4)),
        (4, 5, (1, 0, 2, 3)),
        (5, 6, (1, 0, 2, 4, 3)),
    ]
    out = []
    for n, k, q in fixtures:
        base, optional = active_base_cycle_type(q)
        terms = []
        for s in range(optional + 1):
            transitive = transitive_star_count(base + (1,) * s, k)
            terms.append(
                {
                    "optional_fixed_used": s,
                    "support_choices": comb(optional, s),
                    "count_per_support": transitive,
                    "contribution": comb(optional, s) * transitive,
                }
            )
        assert sum(x["contribution"] for x in terms) == star_bridge_count(n, k, q)
        out.append(
            {
                "N": n,
                "k": k,
                "endpoint": list(q),
                "mandatory_cycle_type": list(base),
                "optional_fixed_labels": optional,
                "terms": terms,
                "total": star_bridge_count(n, k, q),
            }
        )
    return out


def sampler_checks(seed: int, draws: int):
    rng = Random(seed)
    cases = []
    fixtures = [
        (3, 4, identity(3)),
        (4, 5, (1, 0, 2, 3)),  # lower transposition (0 1), minimum star length 3
        (4, 6, identity(4)),
        (5, 6, (1, 0, 2, 4, 3)),  # (0 1)(3 4), minimum star length 4
    ]
    for n, k, q in fixtures:
        exact_count = star_bridge_count(n, k, q)
        assert exact_count > 0, (n, k, q)
        observed = Counter()
        for _ in range(draws):
            word = tuple(sample_star_bridge(n, k, q, rng))
            assert evaluate_star_word(n, word) == q
            observed[word] += 1
        # Descriptive only: finite samples are not used in the exactness proof.
        exact_probability = 1 / exact_count
        empirical_tv = 0.5 * sum(
            abs(observed.get(word, 0) / draws - exact_probability)
            for word in observed
        )
        empirical_tv += 0.5 * (exact_count - len(observed)) * exact_probability
        cases.append(
            {
                "N": n,
                "k": k,
                "endpoint": list(q),
                "endpoint_cycle_type": list(cycle_type(q)),
                "exact_fiber_size": exact_count,
                "draws": draws,
                "distinct_words_seen": len(observed),
                "empirical_tv": empirical_tv,
                "all_products_correct": True,
            }
        )
    return cases


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=5)
    parser.add_argument("--max-k", type=int, default=6)
    parser.add_argument("--seed", type=int, default=20260901)
    parser.add_argument("--draws", type=int, default=2000)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()

    started = time.time()
    exact = exact_checks(args.max_n, args.max_k)
    boundaries = boundary_checks()
    samples = sampler_checks(args.seed, args.draws)
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        commit = "unavailable"
    payload = {
        "metadata": {
            "repository_commit": commit,
            "command": (
                f"python3 {Path(__file__).as_posix()} --max-n {args.max_n} "
                f"--max-k {args.max_k} --seed {args.seed} --draws {args.draws} "
                f"--output {args.output.as_posix()}"
            ),
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "nonstandard_dependencies": [],
            "seed": args.seed,
            "elapsed_seconds": time.time() - started,
        },
        "convention": "compose(p,q)(x)=p(q(x)); displayed word t1...tk",
        "exact_checks": exact,
        "boundary_checks": boundaries,
        "pointed_state_growth": partition_state_growth(),
        "support_decomposition_examples": support_decomposition_examples(),
        "sampler_smoke_checks_empirical": samples,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        "r3-star exact checks passed: "
        f"{exact['endpoint_count_equalities']} endpoint counts, "
        f"{exact['last_factor_recurrence_equalities']} last-factor recurrences, "
        f"{exact['labeled_orbit_transition_equalities']} orbit transitions"
    )
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
