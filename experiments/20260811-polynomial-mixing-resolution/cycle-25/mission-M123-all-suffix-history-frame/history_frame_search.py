#!/usr/bin/env python3
"""Exact complete-history and signed reset-frame audit for M123.

This script is deliberately independent of predecessor Python modules.  It
implements the accepted grouped/literal recurrence with ``Fraction``
arithmetic, retains every attachment rank ``j=1,...,k``, and tests:

1. the complete marked suffix-history mass recursion (total mass ``q``);
2. the exact signed two-copy canonical-basin identity for ``A0`` and ``H``;
3. the proposed unique active-reset-category property;
4. the right-heavy target and the stronger all-context multitype envelope on
   bounded exact DAGs (finite falsification only).

The script does not model the original identity-word heat-bath chain and does
not make an asymptotic inference from bounded checks.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import platform
import subprocess
import time
from fractions import Fraction as F
from pathlib import Path


State = tuple[int, int, int, int]
Composition = tuple[int, ...]


def record(value: F) -> dict[str, str | float]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


def repository_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


@functools.cache
def weight(n: int) -> F:
    if n < 1:
        raise ValueError(n)
    return F(n ** (n - 1), math.factorial(n))


@functools.cache
def compositions(n: int) -> tuple[Composition, ...]:
    if n == 0:
        return ((),)
    out: list[Composition] = []
    for first in range(1, n + 1):
        for tail in compositions(n - first):
            out.append((first,) + tail)
    return tuple(out)


@functools.cache
def forest_weight(total: int, parts: int) -> F:
    """Sum of ``prod w(part)`` over positive ordered ``parts``-compositions."""
    if total == 0 and parts == 0:
        return F(1)
    if not (1 <= parts <= total):
        return F(0)
    return F(parts * total ** (total - parts), total * math.factorial(total - parts))


def choose(n: int, k: int) -> int:
    return math.comb(n, k) if 0 <= k <= n else 0


def split_mass(s: int, B: int) -> F:
    if not (1 <= B <= s):
        raise ValueError((s, B))
    return weight(s + 1 - B) * weight(B) / weight(s + 1)


def root_mass(parts: Composition) -> F:
    s = sum(parts)
    return math.prod(weight(a) for a in parts) / (
        math.factorial(len(parts)) * weight(s + 1)
    )


def context_mean(k: int, t: int, K: int, R: int, B: int) -> F:
    """Accepted closed conditional mean of the contextual suffix statistic."""
    if t < B:
        return F(0)
    if t == B:
        return F(
            K * choose(k + K - R - 2, K - R - 1),
            choose(k + K - 1, K - 1),
        )
    return split_mass(t - 1, B) * (
        1 - F(choose(K, R + 1), choose(K + k, R + 1))
    )


def attachment(K: int, R: int, k: int, j: int) -> F:
    return F(
        choose(R + j, j) * choose(K - R - 1 + k - j, k - j),
        choose(K + k, k),
    )


@functools.cache
def group_law(s: int) -> tuple[tuple[int, int, F], ...]:
    out: list[tuple[int, int, F]] = []
    for t in range(1, s + 1):
        for k in range(1, s + 1):
            mass = weight(t) * forest_weight(s - t, k - 1) / (
                math.factorial(k) * weight(s + 1)
            )
            if mass:
                out.append((k, t, mass))
    assert sum((row[2] for row in out), F(0)) == 1
    return tuple(out)


def active_endpoint(endpoint: Composition) -> bool:
    return len(endpoint) >= 2 and endpoint[0] + endpoint[1] - 1 >= 2


def in_basin(source: Composition, endpoint: Composition) -> bool:
    """Whether source refines the first part of the canonical endpoint."""
    A, tail = endpoint[0], endpoint[1:]
    for cut in range(1, len(source) + 1):
        if sum(source[:cut]) == A and source[cut:] == tail:
            return True
    return False


@functools.cache
def basin_skeleton(
    s: int,
) -> tuple[tuple[Composition, tuple[Composition, ...]], ...]:
    roots = compositions(s)
    endpoints = tuple(row for row in roots if active_endpoint(row))
    return tuple(
        (endpoint, tuple(source for source in roots if in_basin(source, endpoint)))
        for endpoint in endpoints
    )


@functools.cache
def basin_rows(state: State):
    s, K, R, B = state
    q = split_mass(s, B)
    masses = {row: root_mass(row) for row in compositions(s)}
    means = {
        row: context_mean(len(row), row[-1], K, R, B)
        for row in compositions(s)
    }
    out = []
    for endpoint, sources in basin_skeleton(s):
        charge_rows = tuple(
            (source, masses[source] * (means[source] - q)) for source in sources
        )
        theta = sum((charge for _, charge in charge_rows), F(0))
        capacity = len(endpoint) * masses[endpoint]
        out.append((endpoint, sources, charge_rows, theta, capacity))
    return tuple(out)


@functools.cache
def reset_energy(state: State) -> F:
    return sum(
        (theta * theta / capacity for _, _, _, theta, capacity in basin_rows(state)),
        F(0),
    )


@functools.cache
def signed_pair_reset(state: State) -> F:
    """Expand every squared basin current into all ordered signed pairs."""
    answer = F(0)
    for _, _, charges, _, capacity in basin_rows(state):
        for _, left in charges:
            for _, right in charges:
                answer += left * right / capacity
    return answer


@functools.cache
def energy_children(state: State):
    """All live Q children; every j>=1 is retained, j=0 is killed."""
    s, K, R, B = state
    parent_phase = s + K - R
    out = []
    for k, t, mass in group_law(s):
        law_total = sum((attachment(K, R, k, j) for j in range(k + 1)), F(0))
        assert law_total == 1
        if t <= B or t - 1 < 2:
            continue
        for j in range(1, k + 1):
            nu = attachment(K, R, k, j)
            if not nu:
                continue
            child = (t - 1, K + k, R + j, B)
            assert child[0] + child[1] - child[2] < parent_phase
            out.append((mass * nu, child, k, t, j))
    return tuple(out)


@functools.cache
def resolvent(state: State) -> F:
    return reset_energy(state) + sum(
        (probability * resolvent(child) for probability, child, _, _, _ in energy_children(state)),
        F(0),
    )


@functools.cache
def signed_frame_resolvent(state: State) -> F:
    return signed_pair_reset(state) + sum(
        (
            probability * signed_frame_resolvent(child)
            for probability, child, _, _, _ in energy_children(state)
        ),
        F(0),
    )


@functools.cache
def success_history_stats(state: State):
    """Full marked success history, including rank-one terminal resolution.

    All quantities stay in the initial transformed normalization.  In
    particular, no extra child/parent ``alpha`` ratio is inserted.
    """
    s, K, R, B = state
    total = F(0)
    leaf_count = 0
    max_depth = 0
    attachment_labels: set[tuple[int, int]] = set()
    terminal_group_count = 0
    for k, t, mass in group_law(s):
        if t < B:
            continue
        if t == B:
            terminal = context_mean(k, t, K, R, B)
            if terminal:
                total += mass * terminal
                leaf_count += 1
                terminal_group_count += 1
            continue
        # t>B: pointwise marked inheritance, retaining every j>=1.  The
        # child rank can be one here because success resolution, unlike
        # reset energy, does not discard its terminal marked outcome.
        for j in range(1, k + 1):
            nu = attachment(K, R, k, j)
            if not nu:
                continue
            child = (t - 1, K + k, R + j, B)
            child_total, child_leaves, child_depth, child_labels, child_terms = (
                success_history_stats(child)
            )
            total += mass * nu * child_total
            leaf_count += child_leaves
            max_depth = max(max_depth, 1 + child_depth)
            attachment_labels.add((k, j))
            attachment_labels.update(child_labels)
            terminal_group_count += child_terms
    assert total == split_mass(s, B), (state, total, split_mass(s, B))
    return (
        total,
        leaf_count,
        max_depth,
        frozenset(attachment_labels),
        terminal_group_count,
    )


def alpha(rank: int) -> F:
    if rank < 2:
        return F(1)
    return F(2, 3 * rank * (rank - 1))


@functools.cache
def wrongly_renormalized_success(state: State, direction: str) -> F:
    """A deliberate falsifier for inserting an extra child-alpha ratio."""
    s, K, R, B = state
    answer = F(0)
    for k, t, mass in group_law(s):
        if t < B:
            continue
        if t == B:
            answer += mass * context_mean(k, t, K, R, B)
            continue
        for j in range(1, k + 1):
            nu = attachment(K, R, k, j)
            if not nu:
                continue
            child = (t - 1, K + k, R + j, B)
            if child[0] < 2:
                factor = F(1)
            elif direction == "child_over_parent":
                factor = alpha(child[0]) / alpha(s)
            elif direction == "parent_over_child":
                factor = alpha(s) / alpha(child[0])
            else:
                raise ValueError(direction)
            answer += mass * nu * factor * wrongly_renormalized_success(
                child, direction
            )
    return answer


def canonical_active_path(source: Composition) -> tuple[Composition, ...]:
    current = source
    out = []
    while len(current) >= 2:
        if active_endpoint(current):
            out.append(current)
        current = (current[0] + current[1],) + current[2:]
    return tuple(out)


def unique_category_collision(state: State):
    s, K, R, B = state
    q = split_mass(s, B)
    for source in compositions(s):
        mean = context_mean(len(source), source[-1], K, R, B)
        path = canonical_active_path(source)
        if mean > 0 and len(path) >= 2:
            mass = root_mass(source)
            rows = {row[0]: row for row in basin_rows(state)}
            return {
                "state": list(state),
                "source": list(source),
                "source_mass": record(mass),
                "context_mean": record(mean),
                "success_mass": record(mass * mean),
                "q": record(q),
                "centered_source_charge": record(mass * (mean - q)),
                "active_canonical_endpoints": [list(endpoint) for endpoint in path],
                "endpoint_rows": [
                    {
                        "endpoint": list(endpoint),
                        "theta": record(rows[endpoint][3]),
                        "capacity": record(rows[endpoint][4]),
                        "source_is_in_basin": in_basin(source, endpoint),
                    }
                    for endpoint in path
                ],
            }
    return None


def first_edge_partition_energy(state: State):
    """Assign each source charge to its first active edge (a false identity)."""
    rows = {row[0]: row for row in basin_rows(state)}
    q = split_mass(state[0], state[3])
    assigned = {endpoint: F(0) for endpoint in rows}
    assignments = {}
    for source in compositions(state[0]):
        path = canonical_active_path(source)
        if not path:
            continue
        endpoint = path[0]
        charge = root_mass(source) * (
            context_mean(len(source), source[-1], state[1], state[2], state[3]) - q
        )
        assigned[endpoint] += charge
        assignments[source] = endpoint
    value = sum(
        (assigned[endpoint] ** 2 / rows[endpoint][4] for endpoint in rows), F(0)
    )
    mismatches = []
    for endpoint, row in rows.items():
        if assigned[endpoint] != row[3]:
            mismatches.append(
                {
                    "endpoint": list(endpoint),
                    "assigned_disjoint_charge": record(assigned[endpoint]),
                    "true_nested_basin_current": record(row[3]),
                    "difference": record(row[3] - assigned[endpoint]),
                }
            )
    return value, tuple(mismatches), assignments


def run_audit(s_max: int, multitype_s_max: int) -> tuple[list[dict], dict]:
    result_rows: list[dict] = []
    right_heavy_failures = []
    multitype_failures = []
    frame_failures = []
    success_failures = []
    right_heavy_worst = None
    multitype_worst = None
    all_attachment_labels: set[tuple[int, int]] = set()

    for s in range(2, s_max + 1):
        for K in (1, 2, 5):
            for B in range(1, s + 1):
                state = (s, K, K - 1, B)
                q = split_mass(s, B)
                target = q * (1 - q)
                value = resolvent(state)
                frame = signed_frame_resolvent(state)
                success, leaves, depth, labels, terminal_groups = success_history_stats(state)
                all_attachment_labels.update(labels)
                row = {
                    "kind": "right_heavy_root",
                    "state": list(state),
                    "suffix_excess": s - B,
                    "q": record(q),
                    "success_history_mass": record(success),
                    "success_leaf_count": leaves,
                    "success_max_depth": depth,
                    "terminal_group_count_with_multiplicity": terminal_groups,
                    "attachment_labels": [list(label) for label in sorted(labels)],
                    "H": record(value),
                    "signed_frame_H": record(frame),
                    "target": record(target),
                    "ratio": record(value / target),
                }
                result_rows.append(row)
                if success != q:
                    success_failures.append(row)
                if frame != value:
                    frame_failures.append(row)
                if value > target:
                    right_heavy_failures.append(row)
                if right_heavy_worst is None or value / target > right_heavy_worst[0]:
                    right_heavy_worst = (value / target, row)

    # Stronger all-context multitype envelope, used only as a bounded
    # falsifier for the natural category budget.  Reachable R=0 occurs only
    # at (K,R)=(1,0).
    for s in range(2, multitype_s_max + 1):
        for K in range(1, 7):
            for R in range(K):
                if R == 0 and K != 1:
                    continue
                for B in range(1, s + 1):
                    state = (s, K, R, B)
                    q = split_mass(s, B)
                    target = (K - R) * q * (1 - q)
                    value = resolvent(state)
                    ratio = value / target
                    if multitype_worst is None or ratio > multitype_worst[0]:
                        multitype_worst = (
                            ratio,
                            {
                                "state": list(state),
                                "H": record(value),
                                "target": record(target),
                                "ratio": record(ratio),
                            },
                        )
                    if value > target:
                        multitype_failures.append({"state": list(state), "H": record(value), "target": record(target), "ratio": record(ratio)})

    # Search the proposed unique-category property in increasing rank.
    first_collision = None
    for s in range(2, s_max + 1):
        for B in range(1, s + 1):
            candidate = unique_category_collision((s, 1, 0, B))
            if candidate is not None:
                first_collision = candidate
                break
        if first_collision is not None:
            break
    assert first_collision is not None
    collision_state = tuple(first_collision["state"])
    partition_value, partition_mismatches, _ = first_edge_partition_energy(
        collision_state  # type: ignore[arg-type]
    )
    exact_reset = reset_energy(collision_state)  # type: ignore[arg-type]

    # Find the first exact failure caused by inserting an extra alpha ratio.
    wrong_alpha = {}
    for direction in ("child_over_parent", "parent_over_child"):
        witness = None
        for s in range(2, s_max + 1):
            for B in range(1, s + 1):
                state = (s, 1, 0, B)
                wrong = wrongly_renormalized_success(state, direction)
                q = split_mass(s, B)
                if wrong != q:
                    witness = {
                        "state": list(state),
                        "direction": direction,
                        "wrong_total": record(wrong),
                        "correct_q": record(q),
                        "difference": record(wrong - q),
                    }
                    break
            if witness is not None:
                break
        wrong_alpha[direction] = witness

    summary = {
        "claims_tested": {
            "complete_history_mass": "sum of all marked success histories equals q",
            "signed_frame_identity": "full all-j signed two-copy expansion equals H",
            "unique_active_reset_category": "each success atom lies in at most one active reset basin",
            "right_heavy_target": "H<=q(1-q), bounded exact falsification only",
            "multitype_target": "H<=(K-R)q(1-q), bounded exact falsification only",
        },
        "parameters": {
            "right_heavy_s_max": s_max,
            "right_heavy_K_values": [1, 2, 5],
            "multitype_s_max": multitype_s_max,
            "multitype_K_max": 6,
        },
        "right_heavy_row_count": len(result_rows),
        "right_heavy_failure_count": len(right_heavy_failures),
        "right_heavy_first_failures": right_heavy_failures[:3],
        "right_heavy_worst": right_heavy_worst[1],
        "complete_history_mass_failure_count": len(success_failures),
        "signed_frame_identity_failure_count": len(frame_failures),
        "multitype_failure_count": len(multitype_failures),
        "multitype_first_failures": multitype_failures[:3],
        "multitype_worst": multitype_worst[1],
        "attachment_labels_seen": [list(label) for label in sorted(all_attachment_labels)],
        "first_unique_category_collision": first_collision,
        "first_edge_partition_at_collision": {
            "candidate_energy": record(partition_value),
            "true_A0": record(exact_reset),
            "difference_true_minus_candidate": record(exact_reset - partition_value),
            "current_mismatch_count": len(partition_mismatches),
            "current_mismatches": list(partition_mismatches),
        },
        "extra_alpha_ratio_witnesses": wrong_alpha,
        "cache_sizes": {
            "resolvent": resolvent.cache_info().currsize,
            "signed_frame_resolvent": signed_frame_resolvent.cache_info().currsize,
            "success_history_stats": success_history_stats.cache_info().currsize,
            "reset_energy": reset_energy.cache_info().currsize,
        },
    }
    return result_rows, summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=8)
    parser.add_argument("--multitype-s-max", type=int, default=7)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    rows, summary = run_audit(args.s_max, args.multitype_s_max)
    metadata = {
        "repository_commit": repository_commit(),
        "python": platform.python_version(),
        "nonstandard_dependencies": [],
        "seed": None,
        "arithmetic": "fractions.Fraction exact",
        "convention": "(pq)(x)=p(q(x)); factors displayed left-to-right",
        "normalization": (
            "H=A0+QH; Q=rho_s(k,t)nu(K,R,k,j), every j=1,...,k; "
            "complete success histories retain the initial transformed normalization"
        ),
        "finite_scope_warning": (
            "Bounded survival cannot prove either universal contraction inequality."
        ),
        "command": (
            f"python3 -B {Path(__file__)} --s-max {args.s_max} "
            f"--multitype-s-max {args.multitype_s_max} "
            f"--results {args.results} --summary {args.summary}"
        ),
        "elapsed_seconds": time.time() - started,
    }
    with args.results.open("w") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True) + "\n")
    payload = {"metadata": metadata, "result": summary}
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.summary.write_text(encoded)
    print(
        json.dumps(
            {
                "results": str(args.results),
                "summary": str(args.summary),
                "summary_sha256": hashlib.sha256(encoded.encode()).hexdigest(),
                "elapsed_seconds": metadata["elapsed_seconds"],
                "right_heavy_failure_count": summary["right_heavy_failure_count"],
                "multitype_failure_count": summary["multitype_failure_count"],
                "complete_history_mass_failure_count": summary[
                    "complete_history_mass_failure_count"
                ],
                "signed_frame_identity_failure_count": summary[
                    "signed_frame_identity_failure_count"
                ],
                "first_collision": summary["first_unique_category_collision"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

