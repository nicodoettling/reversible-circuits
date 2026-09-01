#!/usr/bin/env python3
"""Independent exact audit of M103's two-layer reset obstruction.

This file imports no predecessor experiment.  It reconstructs the grouped
root law, the full negative-hypergeometric attachment law, canonical reset
energies, and the finite-DAG resolvents directly from the displayed formulas
accepted in M90/M96.  Every arithmetic operation affecting a promoted sign
uses ``fractions.Fraction``.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import itertools
import json
import math
import platform
import time
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterator

Context = tuple[int, int, int, int]


def exact_record(value: Fraction) -> dict[str, str]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": format(float(value), ".17g"),
    }


@functools.cache
def tree_weight(size: int) -> Fraction:
    """Cayley rooted-tree weight w_size=size^(size-1)/size!."""
    if size < 1:
        raise ValueError(size)
    return Fraction(size ** (size - 1), math.factorial(size))


@functools.cache
def ordered_forest_weight(total: int, parts: int) -> Fraction:
    """Sum of products of tree weights over ordered positive compositions."""
    if total == 0 and parts == 0:
        return Fraction(1)
    if total < 1 or parts < 1 or parts > total:
        return Fraction(0)
    # p*n^(n-p-1)/(n-p)!, written without a negative exponent.
    return Fraction(
        parts * total ** (total - parts),
        total * math.factorial(total - parts),
    )


def compositions(total: int) -> Iterator[tuple[int, ...]]:
    """All ordered positive compositions; used only for small direct audits."""
    if total < 1:
        return
    for mask in range(1 << (total - 1)):
        row = []
        run = 1
        for pos in range(total - 1):
            if mask & (1 << pos):
                row.append(run)
                run = 1
            else:
                run += 1
        row.append(run)
        yield tuple(row)


@functools.cache
def root_groups(rank: int) -> tuple[tuple[int, int, Fraction], ...]:
    """Grouped root-composition law (part count, last part, probability)."""
    rows: list[tuple[int, int, Fraction]] = []
    total = Fraction(0)
    for part_count in range(1, rank + 1):
        for last in range(1, rank + 1):
            mass = (
                tree_weight(last)
                * ordered_forest_weight(rank - last, part_count - 1)
                / (math.factorial(part_count) * tree_weight(rank + 1))
            )
            if mass:
                rows.append((part_count, last, mass))
                total += mass
    if total != 1:
        raise AssertionError(("root law", rank, total))
    return tuple(rows)


def split_mass(rank: int, mark: int) -> Fraction:
    if not (rank >= 1 and 1 <= mark <= rank):
        raise ValueError((rank, mark))
    return (
        tree_weight(rank + 1 - mark)
        * tree_weight(mark)
        / tree_weight(rank + 1)
    )


def safe_binomial(n: int, r: int) -> int:
    return math.comb(n, r) if 0 <= r <= n else 0


def contextual_mean(
    part_count: int,
    last: int,
    population: int,
    occupied: int,
    mark: int,
) -> Fraction:
    """M56/M65 contextual closed mean H_(K,R;B)(k,t)."""
    if last < mark:
        return Fraction(0)
    if last == mark:
        numerator = population * safe_binomial(
            part_count + population - occupied - 2,
            population - occupied - 1,
        )
        denominator = safe_binomial(
            part_count + population - 1,
            population - 1,
        )
        return Fraction(numerator, denominator)
    return split_mass(last - 1, mark) * (
        1
        - Fraction(
            safe_binomial(population, occupied + 1),
            safe_binomial(population + part_count, occupied + 1),
        )
    )


@functools.cache
def attachment_row(
    population: int, occupied: int, part_count: int
) -> tuple[Fraction, ...]:
    """Full j=0,...,k negative-hypergeometric attachment distribution."""
    denominator = safe_binomial(population + part_count, part_count)
    row = tuple(
        Fraction(
            safe_binomial(occupied + j, j)
            * safe_binomial(
                population - occupied - 1 + part_count - j,
                part_count - j,
            ),
            denominator,
        )
        for j in range(part_count + 1)
    )
    if sum(row, Fraction()) != 1:
        raise AssertionError(("attachment law", population, occupied, part_count))
    return row


def progress(context: Context) -> int:
    rank, population, occupied, _ = context
    return rank + population - occupied


@functools.cache
def live_edges(context: Context) -> tuple[tuple[Fraction, Context], ...]:
    """Every live Q edge; j=0 alone is killed."""
    rank, population, occupied, mark = context
    if not (rank >= 2 and population > occupied >= 0 and 1 <= mark <= rank):
        raise ValueError(context)
    edges: list[tuple[Fraction, Context]] = []
    for part_count, last, root_mass in root_groups(rank):
        # t<=B is terminal/killed; rank t-1<2 is inactive.
        if last <= mark or last - 1 < 2:
            continue
        law = attachment_row(population, occupied, part_count)
        for j in range(1, part_count + 1):
            probability = law[j]
            if not probability:
                raise AssertionError(("unexpected zero live rank", context, part_count, j))
            child = (
                last - 1,
                population + part_count,
                occupied + j,
                mark,
            )
            drop = progress(context) - progress(child)
            # A positive root group is an ordered composition of rank with
            # k-1 positive parts before t, hence rank-t>=k-1.
            if drop != rank - last - part_count + j + 1 or drop < j:
                raise AssertionError(("progress descent", context, child, j, drop))
            edges.append((root_mass * probability, child))
    return tuple(edges)


def budget(context: Context) -> Fraction:
    rank, population, occupied, mark = context
    q = split_mass(rank, mark)
    return q * (1 - q) * Fraction(population, occupied + 1)


@functools.cache
def basin_current_scalar(
    context: Context, first: int, suffix_length: int, last: int
) -> Fraction:
    """Grouped basin current S_e after refining the first endpoint part."""
    rank, population, occupied, mark = context
    parent_mean = split_mass(rank, mark)
    return sum(
        (
            ordered_forest_weight(first, source_parts)
            * (
                contextual_mean(
                    source_parts + suffix_length,
                    last,
                    population,
                    occupied,
                    mark,
                )
                - parent_mean
            )
            / math.factorial(source_parts + suffix_length)
            for source_parts in range(1, first + 1)
        ),
        Fraction(),
    )


@functools.cache
def canonical_energy_pair(context: Context) -> tuple[Fraction, Fraction]:
    """Return (weighted A, unweighted A_0) by grouped endpoint summation."""
    rank, _, _, _ = context
    weighted_total = Fraction(0)
    unweighted_total = Fraction(0)

    # An endpoint is e=(A,b,c_3,...,c_(ell+1)), an ordered composition
    # of rank with ell+1 parts.  Group its middle suffix parts while retaining
    # b and the last part, because the reset reward depends on b and the
    # current depends on the last part.
    for first in range(1, rank):
        suffix_total = rank - first
        for suffix_length in range(1, suffix_total + 1):
            tail_parts = suffix_length - 1
            for second in range(1, suffix_total + 1):
                tail_total = suffix_total - second
                if tail_parts == 0:
                    tails = ((second, tree_weight(second)),) if tail_total == 0 else ()
                else:
                    tails = tuple(
                        (
                            last,
                            tree_weight(second)
                            * ordered_forest_weight(tail_total - last, tail_parts - 1)
                            * tree_weight(last),
                        )
                        for last in range(1, tail_total + 1)
                        if ordered_forest_weight(tail_total - last, tail_parts - 1)
                    )
                reset_rank = first + second - 1
                if reset_rank < 2:
                    continue
                reward = 1 - split_mass(reset_rank, second)
                for last, suffix_weight in tails:
                    current = basin_current_scalar(
                        context, first, suffix_length, last
                    )
                    raw = (
                        suffix_weight
                        * math.factorial(suffix_length)
                        * current * current
                        / (tree_weight(first) * tree_weight(rank + 1))
                    )
                    unweighted_total += raw
                    weighted_total += raw * reward
    return weighted_total, unweighted_total


def apply_q(context: Context, function: Callable[[Context], Fraction]) -> Fraction:
    return sum(
        (edge_mass * function(child) for edge_mass, child in live_edges(context)),
        Fraction(),
    )


@functools.cache
def local_defect(context: Context) -> Fraction:
    weighted, _ = canonical_energy_pair(context)
    return budget(context) - weighted - apply_q(context, budget)


@functools.cache
def full_resolvents(context: Context) -> tuple[Fraction, Fraction]:
    """Finite-DAG values ((I-Q)^-1 A, (I-Q)^-1 A_0)."""
    weighted, unweighted = canonical_energy_pair(context)
    for edge_mass, child in live_edges(context):
        child_weighted, child_unweighted = full_resolvents(child)
        weighted += edge_mass * child_weighted
        unweighted += edge_mass * child_unweighted
    return weighted, unweighted


def literal_root_group_audit(max_rank: int) -> dict[str, object]:
    checks = 0
    for rank in range(1, max_rank + 1):
        literal: dict[tuple[int, int], Fraction] = {}
        for row in compositions(rank):
            key = (len(row), row[-1])
            mass = math.prod(tree_weight(part) for part in row) / (
                math.factorial(len(row)) * tree_weight(rank + 1)
            )
            literal[key] = literal.get(key, Fraction()) + mass
        grouped = {(k, t): mass for k, t, mass in root_groups(rank)}
        all_keys = literal.keys() | grouped.keys()
        for key in all_keys:
            if literal.get(key, Fraction()) != grouped.get(key, Fraction()):
                raise AssertionError(("literal root mismatch", rank, key))
            checks += 1
    return {"ranks": [1, max_rank], "group_cells_checked": checks, "passed": True}


def literal_canonical_energy(context: Context) -> tuple[Fraction, Fraction]:
    """Direct endpoint-composition check for small rank only."""
    rank, _, _, _ = context
    weighted = Fraction(0)
    unweighted = Fraction(0)
    for endpoint in compositions(rank):
        if len(endpoint) < 2:
            continue
        first, second = endpoint[0], endpoint[1]
        reset_rank = first + second - 1
        if reset_rank < 2:
            continue
        suffix_length = len(endpoint) - 1
        suffix_weight = math.prod(tree_weight(part) for part in endpoint[1:])
        current = basin_current_scalar(
            context, first, suffix_length, endpoint[-1]
        )
        raw = (
            suffix_weight
            * math.factorial(suffix_length)
            * current * current
            / (tree_weight(first) * tree_weight(rank + 1))
        )
        unweighted += raw
        weighted += raw * (1 - split_mass(reset_rank, second))
    return weighted, unweighted


def direct_small_checks() -> dict[str, object]:
    root_check = literal_root_group_audit(7)

    attachment_checks = 0
    for population in range(1, 5):
        for occupied in range(population):
            for part_count in range(1, 8):
                row = attachment_row(population, occupied, part_count)
                if sum(row, Fraction()) != 1 or any(value <= 0 for value in row):
                    raise AssertionError("attachment audit")
                attachment_checks += 1

    mean_checks = []
    for context in ((6, 1, 0, 3), (8, 2, 1, 3), (11, 1, 0, 4)):
        rank, population, occupied, mark = context
        root_mean = sum(
            (
                mass
                * contextual_mean(k, last, population, occupied, mark)
                for k, last, mass in root_groups(rank)
            ),
            Fraction(),
        )
        target = split_mass(rank, mark)
        if root_mean != target:
            raise AssertionError(("contextual root mean", context, root_mean, target))
        mean_checks.append({"context": list(context), "mean": exact_record(root_mean)})

    endpoint_checks = []
    for context in ((6, 1, 0, 3), (8, 1, 0, 4)):
        grouped = canonical_energy_pair(context)
        literal = literal_canonical_energy(context)
        if grouped != literal:
            raise AssertionError(("canonical endpoint grouping", context))
        endpoint_checks.append(
            {
                "context": list(context),
                "weighted": exact_record(grouped[0]),
                "unweighted": exact_record(grouped[1]),
            }
        )

    calibration = (11, 1, 0, 4)
    local = local_defect(calibration)
    first = apply_q(calibration, local_defect)
    if not (local < 0 < local + first):
        raise AssertionError(("M90 boundary calibration", local, first))

    return {
        "literal_root_groups": root_check,
        "attachment_laws_checked": attachment_checks,
        "contextual_root_means": mean_checks,
        "literal_canonical_endpoint_checks": endpoint_checks,
        "predecessor_boundary_calibration": {
            "context": list(calibration),
            "r_U": exact_record(local),
            "Q_r_U": exact_record(first),
            "two_layer": exact_record(local + first),
        },
    }


def first_layer_accounting(context: Context) -> dict[str, object]:
    rank, population, occupied, mark = context
    eligible = []
    edge_count = 0
    live_ranks: set[int] = set()
    live_mass = Fraction(0)
    killed_j0_mass = Fraction(0)
    min_drop: int | None = None
    for part_count, last, root_mass in root_groups(rank):
        if last <= mark or last - 1 < 2:
            continue
        law = attachment_row(population, occupied, part_count)
        expected = list(range(1, part_count + 1))
        retained = [j for j in expected if law[j] > 0]
        if retained != expected:
            raise AssertionError(("omitted live j", part_count, last))
        killed_j0_mass += root_mass * law[0]
        for j in retained:
            child = (last - 1, population + part_count, occupied + j, mark)
            drop = progress(context) - progress(child)
            min_drop = drop if min_drop is None else min(min_drop, drop)
            live_mass += root_mass * law[j]
            edge_count += 1
            live_ranks.add(j)
        eligible.append(
            {
                "part_count": part_count,
                "last": last,
                "retained_j": expected,
            }
        )
    if tuple((m, c) for m, c in live_edges(context)) != live_edges(context):
        raise AssertionError("edge cache integrity")
    return {
        "eligible_root_groups": len(eligible),
        "live_edges": edge_count,
        "live_ranks_observed": sorted(live_ranks),
        "every_j_1_through_k_retained_per_group": True,
        "j_0_only_killed": True,
        "live_Q_row_mass": exact_record(live_mass),
        "killed_j0_mass_on_deep_eligible_groups": exact_record(killed_j0_mass),
        "minimum_observed_progress_drop": min_drop,
        "eligible_group_digest": hashlib.sha256(
            json.dumps(eligible, sort_keys=True).encode()
        ).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()

    small_checks = direct_small_checks()
    witness: Context = (30, 1, 0, 10)
    if not (witness[0] >= 2 and witness[1:] == (1, 0, 10)):
        raise AssertionError("witness is not an active fresh context")

    target = budget(witness)
    local = local_defect(witness)
    first = apply_q(witness, local_defect)
    paired = local + first

    weighted_A, _ = canonical_energy_pair(witness)
    q_A = apply_q(witness, lambda child: canonical_energy_pair(child)[0])
    q2_U = apply_q(witness, lambda child: apply_q(child, budget))
    expanded = target - weighted_A - q_A - q2_U
    if paired != expanded:
        raise AssertionError(("two-layer identity", paired, expanded))
    if paired >= 0:
        raise AssertionError("claimed exact counterexample is not negative")

    weighted, unweighted = full_resolvents(witness)
    weighted_margin = target - weighted
    # At the fresh witness K/(R+1)=1, the unweighted target q(1-q) equals U.
    unweighted_margin = target - unweighted
    if not (weighted_margin > 0 and unweighted_margin > 0):
        raise AssertionError(("full resolvent survival", weighted_margin, unweighted_margin))

    payload = {
        "audit": "M106 independent exact audit of frozen M103",
        "arithmetic": "fractions.Fraction exact; decimals presentation only",
        "convention": "(pq)(x)=p(q(x)); displayed factors multiply left-to-right",
        "target": "uniform fixed-length identity words; auxiliary recurrence only",
        "witness": list(witness),
        "reachability": {
            "active": True,
            "fresh": True,
            "reason": "(K,R)=(1,0), so the witness is a depth-zero fresh seed in the accepted reachable closure",
            "progress": "P=s+K-R",
            "live_child_drop": "P(x)-P(y)=s-t-k+j+1>=j>=1",
        },
        "definitions": {
            "Q": "rho_s(k,t) nu_(K,R,k)(j), all j=1,...,k; j=0 killed",
            "A": "sum_e theta_e^2/Q_G(e) times (1-q_reset(e))",
            "A0": "sum_e theta_e^2/Q_G(e)",
            "U": "q_(s,B)(1-q_(s,B)) K/(R+1)",
            "r_U": "U-A-QU",
        },
        "algebra": {
            "identity": "(I+Q)r_U=U-A-QA-Q^2U",
            "exact_forms_agree": paired == expanded,
            "expanded_value": exact_record(expanded),
        },
        "all_j_accounting": first_layer_accounting(witness),
        "two_layer_certificate": {
            "U": exact_record(target),
            "r_U": exact_record(local),
            "Q_r_U": exact_record(first),
            "I_plus_Q_r_U": exact_record(paired),
            "normalized_by_U": exact_record(paired / target),
            "strictly_negative": paired < 0,
        },
        "full_resolvents": {
            "weighted": exact_record(weighted),
            "weighted_ratio_to_U": exact_record(weighted / target),
            "weighted_margin_U_minus_value": exact_record(weighted_margin),
            "unweighted": exact_record(unweighted),
            "unweighted_ratio_to_q_one_minus_q": exact_record(unweighted / target),
            "unweighted_margin_q_one_minus_q_minus_value": exact_record(unweighted_margin),
            "both_exact_margins_positive": True,
            "logical_status": "finite survival diagnostics only",
        },
        "direct_small_checks": small_checks,
        "cache_statistics": {
            "root_groups": str(root_groups.cache_info()),
            "attachment_rows": str(attachment_row.cache_info()),
            "live_edges": str(live_edges.cache_info()),
            "basin_currents": str(basin_current_scalar.cache_info()),
            "canonical_energy_pairs": str(canonical_energy_pair.cache_info()),
            "full_resolvents": str(full_resolvents.cache_info()),
        },
        "scope": {
            "refuted": "universal pointwise global two-layer sufficient condition",
            "not_refuted": [
                "universal full weighted reset resolvent inequality",
                "universal full unweighted reset resolvent inequality",
                "auxiliary Pbar spectral gap",
                "ROOT-MEAN LIFT",
                "original {3,4,5} heat-bath polynomial mixing",
                "Terminal A",
                "Terminal B",
            ],
            "next_open_target": "FULL RESET EXCURSION",
        },
        "python": platform.python_version(),
        "seed": None,
        "elapsed_seconds": time.time() - started,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
                "two_layer": payload["two_layer_certificate"]["I_plus_Q_r_U"],
                "weighted_margin": payload["full_resolvents"]["weighted_margin_U_minus_value"],
                "unweighted_margin": payload["full_resolvents"]["unweighted_margin_q_one_minus_q_minus_value"],
                "elapsed_seconds": payload["elapsed_seconds"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
