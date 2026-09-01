#!/usr/bin/env python3
"""Independent exact referee audit of the frozen M90 bundle.

This implementation intentionally imports no M90 or predecessor module.  It
uses literal ordered compositions and literal canonical-basin sums, then
compares those results with M90's grouped Cayley outputs.  All arithmetic
supporting signs and equalities is ``fractions.Fraction`` arithmetic.
"""

from __future__ import annotations

import functools
import hashlib
import json
import math
import platform
import time
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
RUN_ROOT = HERE.parents[1]
M90 = RUN_ROOT / "cycle-18" / "mission-M90-weighted-reset-resolvent"
M82 = RUN_ROOT / "cycle-17" / "mission-M82-reset-substochasticity"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rec(value: Fraction) -> dict[str, object]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


@functools.lru_cache(maxsize=None)
def w(a: int) -> Fraction:
    if a < 1:
        raise ValueError(a)
    return Fraction(a ** (a - 1), math.factorial(a))


@functools.lru_cache(maxsize=None)
def compositions(n: int) -> tuple[tuple[int, ...], ...]:
    if n == 0:
        return ((),)
    rows: list[tuple[int, ...]] = []
    for first in range(1, n + 1):
        for tail in compositions(n - first):
            rows.append((first,) + tail)
    return tuple(rows)


def rho(comp: tuple[int, ...]) -> Fraction:
    s = sum(comp)
    value = Fraction(1, math.factorial(len(comp)) * w(s + 1))
    for part in comp:
        value *= w(part)
    return value


def q_split(s: int, B: int) -> Fraction:
    return w(s + 1 - B) * w(B) / w(s + 1)


def safe_ratio(n1: int, k1: int, n2: int, k2: int) -> Fraction:
    if not (0 <= k1 <= n1 and 0 <= k2 <= n2):
        return Fraction(0)
    return Fraction(math.comb(n1, k1), math.comb(n2, k2))


def H(comp: tuple[int, ...], K: int, R: int, B: int) -> Fraction:
    k, t = len(comp), comp[-1]
    if t < B:
        return Fraction(0)
    if t == B:
        return K * safe_ratio(
            k + K - R - 2,
            K - R - 1,
            k + K - 1,
            K - 1,
        )
    local = w(t - B) * w(B) / w(t)
    bad = safe_ratio(K, R + 1, K + k, R + 1)
    return local * (1 - bad)


def nu(K: int, R: int, k: int, j: int) -> Fraction:
    return Fraction(
        math.comb(R + j, j)
        * math.comb(K - R - 1 + k - j, k - j),
        math.comb(K + k, k),
    )


@functools.lru_cache(maxsize=None)
def cayley(total: int, parts: int) -> Fraction:
    if parts == 0:
        return Fraction(int(total == 0))
    if not 1 <= parts <= total:
        return Fraction(0)
    return Fraction(
        parts * total ** (total - parts),
        total * math.factorial(total - parts),
    )


@functools.lru_cache(maxsize=None)
def reset_direct(x: tuple[int, int, int, int], weighted: bool) -> Fraction:
    """Literal endpoint and literal basin enumeration of q_parent J reward."""
    s, K, R, B = x
    q_parent = q_split(s, B)
    answer = Fraction(0)
    for endpoint in compositions(s):
        if len(endpoint) < 2:
            continue
        A, b = endpoint[:2]
        child_s = A + b - 1
        if child_s < 2:
            continue
        child = (child_s, len(endpoint) - 1, len(endpoint) - 2, b)
        if child[1] - child[2] != 1:
            raise AssertionError(("reset right-heavy", x, endpoint, child))
        if child[0] + child[1] - child[2] >= s + K - R:
            raise AssertionError(("reset phase", x, endpoint, child))
        theta = Fraction(0)
        suffix = endpoint[1:]
        for prefix in compositions(A):
            comp = prefix + suffix
            theta += rho(comp) * (H(comp, K, R, B) - q_parent)
        qg = rho(endpoint) * len(endpoint)
        energy = theta * theta / qg
        if weighted:
            energy *= 1 - q_split(child_s, b)
        answer += energy
    return answer


@functools.lru_cache(maxsize=None)
def reset_grouped(x: tuple[int, int, int, int], weighted: bool) -> Fraction:
    """Independent grouped evaluation of the same reset reward."""
    s, K, R, B = x
    q_parent = q_split(s, B)
    answer = Fraction(0)
    for endpoint in compositions(s):
        if len(endpoint) < 2:
            continue
        A, b = endpoint[:2]
        child_s = A + b - 1
        if child_s < 2:
            continue
        ell = len(endpoint) - 1
        last = endpoint[-1]
        scalar = sum(
            (
                cayley(A, p)
                * (H((1,) * (p + ell - 1) + (last,), K, R, B) - q_parent)
                / math.factorial(p + ell)
                for p in range(1, A + 1)
            ),
            Fraction(),
        )
        suffix_weight = math.prod((w(part) for part in endpoint[1:]), start=Fraction(1))
        energy = (
            suffix_weight
            * math.factorial(ell)
            * scalar
            * scalar
            / (w(A) * w(s + 1))
        )
        if weighted:
            energy *= 1 - q_split(child_s, b)
        answer += energy
    return answer


@functools.lru_cache(maxsize=None)
def deep_children(
    x: tuple[int, int, int, int], all_j: bool = True
) -> tuple[tuple[Fraction, tuple[int, int, int, int]], ...]:
    s, K, R, B = x
    parent_phase = s + K - R
    aggregate: dict[tuple[int, int, int, int], Fraction] = defaultdict(Fraction)
    for comp in compositions(s):
        k, t = len(comp), comp[-1]
        if t <= B or t - 1 < 2:
            continue
        ranks = range(1, k + 1) if all_j else (k,)
        for j in ranks:
            probability = nu(K, R, k, j)
            if not probability:
                continue
            child = (t - 1, K + k, R + j, B)
            if child[0] + child[1] - child[2] >= parent_phase:
                raise AssertionError(("deep phase", x, comp, j, child))
            if not (child[1] > child[2] >= 1):
                raise AssertionError(("deep closure", x, comp, j, child))
            aggregate[child] += rho(comp) * probability
    return tuple(sorted((mass, child) for child, mass in aggregate.items()))


@functools.lru_cache(maxsize=None)
def g(x: tuple[int, int, int, int], all_j: bool = True) -> Fraction:
    if x[0] <= 1:
        return Fraction(0)
    return reset_direct(x, True) + sum(
        (mass * g(child, all_j) for mass, child in deep_children(x, all_j)),
        Fraction(),
    )


@functools.lru_cache(maxsize=None)
def h(x: tuple[int, int, int, int]) -> Fraction:
    if x[0] <= 1:
        return Fraction(0)
    return reset_direct(x, False) + sum(
        (mass * h(child) for mass, child in deep_children(x)), Fraction()
    )


def U(x: tuple[int, int, int, int]) -> Fraction:
    s, K, R, B = x
    q = q_split(s, B)
    return q * (1 - q) * Fraction(K, R + 1)


@functools.lru_cache(maxsize=None)
def defect_U(x: tuple[int, int, int, int]) -> Fraction:
    return U(x) - reset_direct(x, True) - sum(
        (mass * U(child) for mass, child in deep_children(x)), Fraction()
    )


@functools.lru_cache(maxsize=None)
def defect_resolvent(x: tuple[int, int, int, int]) -> Fraction:
    return defect_U(x) + sum(
        (mass * defect_resolvent(child) for mass, child in deep_children(x)),
        Fraction(),
    )


def ordered_pair(a: tuple[int, int], b: tuple[int, int]):
    return (a, b) if a <= b else (b, a)


def mixed_moment(
    s: int, a: tuple[int, int], b: tuple[int, int], B: int
) -> Fraction:
    a, b = ordered_pair(a, b)
    return _mixed_moment(s, a[0], a[1], b[0], b[1], B)


@functools.lru_cache(maxsize=None)
def _mixed_moment(s: int, K: int, R: int, L: int, S: int, B: int) -> Fraction:
    if s == 1:
        if B != 1:
            raise AssertionError((s, K, R, L, S, B))
        return Fraction(1)
    answer = Fraction(0)
    for comp in compositions(s):
        k, t = len(comp), comp[-1]
        mass = rho(comp)
        if t < B:
            continue
        if t == B:
            answer += mass * H(comp, K, R, B) * H(comp, L, S, B)
            continue
        left = [(nu(K, R, k, j), (K + k, R + j)) for j in range(1, k + 1)]
        right = [(nu(L, S, k, j), (L + k, S + j)) for j in range(1, k + 1)]
        for p, child_a in left:
            if not p:
                continue
            for q, child_b in right:
                if q:
                    answer += p * q * mass * mixed_moment(t - 1, child_a, child_b, B)
    return answer


@functools.lru_cache(maxsize=None)
def variance(x: tuple[int, int, int, int]) -> Fraction:
    s, K, R, B = x
    q = q_split(s, B)
    return mixed_moment(s, (K, R), (K, R), B) - q * q


def root_mean_variance(x: tuple[int, int, int, int]) -> Fraction:
    s, K, R, B = x
    q = q_split(s, B)
    return sum((rho(c) * (H(c, K, R, B) - q) ** 2 for c in compositions(s)), Fraction())


def Q_variance(x: tuple[int, int, int, int]) -> Fraction:
    return sum((mass * variance(child) for mass, child in deep_children(x)), Fraction())


def coefficients(x: tuple[int, int, int, int]) -> dict[str, Fraction]:
    s, K, R, _ = x
    P = s + K - R
    return {
        "rank_s_over_s_plus_1": Fraction(s, s + 1),
        "rank_s_over_s_plus_2": Fraction(s, s + 2),
        "rank_s_over_s_plus_4": Fraction(s, s + 4),
        "phase_P_over_P_plus_1": Fraction(P, P + 1),
        "phase_P_over_P_plus_2": Fraction(P, P + 2),
        "phase_P_over_P_plus_4": Fraction(P, P + 4),
        "rank_one_minus_inverse_square": 1 - Fraction(1, s * s),
        "phase_one_minus_inverse_square": 1 - Fraction(1, P * P),
    }


def interpolant(name: str, x: tuple[int, int, int, int]) -> Fraction:
    V = variance(x)
    return V + coefficients(x)[name] * (U(x) - V)


def manifest_audit() -> dict[str, object]:
    manifest = M90 / "SHA256SUMS"
    rows = []
    for line in manifest.read_text().splitlines():
        expected, name = line.split("  ", 1)
        observed = digest(M90 / name)
        rows.append({"file": name, "expected": expected, "observed": observed, "match": expected == observed})
    return {
        "entry_count": len(rows),
        "all_match": all(row["match"] for row in rows),
        "rows": rows,
    }


def exact_from_string(value: str) -> Fraction:
    numerator, denominator = value.split("/")
    return Fraction(int(numerator), int(denominator))


def fraction_from_record(value: dict[str, object]) -> Fraction:
    return Fraction(int(value["numerator"]), int(value["denominator"]))


def main() -> None:
    started = time.time()
    manifest = manifest_audit()
    if not manifest["all_match"]:
        raise AssertionError("M90 manifest mismatch")

    required_hashes = {
        "report.md": "36230c7e509eff638eb5888b2e61703957dcc32f2f06fae582739d7f1414d458",
        "SHA256SUMS": "3d63f177659abae99b6c3a4247aee67b6dfc087cd1270df40e806f5a9f99b5b8",
    }
    observed_hashes = {name: digest(M90 / name) for name in required_hashes}
    if observed_hashes != required_hashes:
        raise AssertionError((required_hashes, observed_hashes))

    # Literal-composition mass and grouped Cayley mass checks.
    group_checks = 0
    nu_checks = 0
    normalization_rows = []
    for s in range(1, 9):
        total = sum((rho(comp) for comp in compositions(s)), Fraction())
        if total != 1:
            raise AssertionError(("rho normalization", s, total))
        for k in range(1, s + 1):
            for t in range(1, s + 1):
                direct = sum(
                    (rho(comp) for comp in compositions(s) if len(comp) == k and comp[-1] == t),
                    Fraction(),
                )
                grouped = w(t) * cayley(s - t, k - 1) / (math.factorial(k) * w(s + 1))
                if direct != grouped:
                    raise AssertionError(("group mass", s, k, t, direct, grouped))
                group_checks += 1
        normalization_rows.append({"s": s, "composition_count": len(compositions(s)), "total_mass": rec(total)})

    for K in range(1, 9):
        for R in range(K):
            for k in range(1, 9):
                total = sum((nu(K, R, k, j) for j in range(k + 1)), Fraction())
                if total != 1:
                    raise AssertionError(("nu normalization", K, R, k, total))
                nu_checks += 1

    # Direct canonical basins against the Cayley-grouped endpoint identity.
    reset_group_checks = 0
    for s in range(2, 8):
        for K in range(1, 5):
            for R in range(K):
                if R == 0 and K > 1:
                    continue
                for B in range(1, s + 1):
                    x = (s, K, R, B)
                    for weighted in (False, True):
                        direct = reset_direct(x, weighted)
                        grouped = reset_grouped(x, weighted)
                        if direct != grouped:
                            raise AssertionError(("reset grouping", x, weighted, direct, grouped))
                        reset_group_checks += 1

    m82_s8 = json.loads((M82 / "exact_reset_audit_s8.json").read_text())
    m82_s11 = json.loads((M82 / "exact_reset_seed_s11.json").read_text())
    expected_w8 = exact_from_string(m82_s8["result"]["maxima"]["eliminated_W_over_W"]["exact"])
    expected_w11 = exact_from_string(m82_s11["result"]["maxima"]["eliminated_W_over_W"]["exact"])
    expected_h8 = exact_from_string(m82_s8["result"]["maxima"]["row_over_u_one_minus_q"]["exact"])
    expected_h11 = exact_from_string(m82_s11["result"]["maxima"]["row_over_u_one_minus_q"]["exact"])
    xw8, xw11 = (8, 1, 0, 4), (11, 1, 0, 5)
    xh8, xh11 = (8, 1, 0, 3), (11, 1, 0, 4)
    observed_w8 = g(xw8) / U(xw8)
    observed_w11 = g(xw11) / U(xw11)
    observed_h8 = h(xh8) / (q_split(8, 3) * (1 - q_split(8, 3)))
    observed_h11 = h(xh11) / (q_split(11, 4) * (1 - q_split(11, 4)))
    calibration_rows = [
        {"name": "weighted_s8", "context": list(xw8), "observed": rec(observed_w8), "expected": rec(expected_w8), "match": observed_w8 == expected_w8},
        {"name": "weighted_s11", "context": list(xw11), "observed": rec(observed_w11), "expected": rec(expected_w11), "match": observed_w11 == expected_w11},
        {"name": "unweighted_s8", "context": list(xh8), "observed": rec(observed_h8), "expected": rec(expected_h8), "match": observed_h8 == expected_h8},
        {"name": "unweighted_s11", "context": list(xh11), "observed": rec(observed_h11), "expected": rec(expected_h11), "match": observed_h11 == expected_h11},
    ]
    if not all(row["match"] for row in calibration_rows):
        raise AssertionError(calibration_rows)

    # Explicitly distinguish the corrected recurrence from the stale j=k-only one.
    stale_ratio = g(xw11, False) / U(xw11)
    if stale_ratio == observed_w11:
        raise AssertionError("all-j recurrence did not differ from stale recurrence")
    discovery = json.loads((M90 / "discovery_s11_k1.json").read_text())
    retained_discovery_ratio = Fraction(str(discovery["result"]["overall_worst"]["ratio"]))

    # Exact finite-DAG defect identity and a fresh two-level compensation witness.
    defect_x = (11, 1, 0, 4)
    q_r = sum((mass * defect_U(child) for mass, child in deep_children(defect_x)), Fraction())
    defect_identity_left = U(defect_x) - g(defect_x)
    defect_identity_right = defect_resolvent(defect_x)
    if defect_identity_left != defect_identity_right:
        raise AssertionError(("defect resolvent", defect_identity_left, defect_identity_right))
    if not (defect_U(defect_x) < 0 < defect_U(defect_x) + q_r):
        raise AssertionError(("fresh compensation", defect_U(defect_x), q_r))

    # Finite independent closure audit through all fresh ranks <= 11.
    visited: set[tuple[int, int, int, int]] = set()
    def visit(x: tuple[int, int, int, int]) -> None:
        if x in visited:
            return
        visited.add(x)
        for _, child in deep_children(x):
            visit(child)
    fresh_two_step_failures = []
    for s in range(2, 12):
        for B in range(1, s + 1):
            x = (s, 1, 0, B)
            visit(x)
            qr = sum((mass * defect_U(child) for mass, child in deep_children(x)), Fraction())
            if defect_U(x) + qr < 0:
                fresh_two_step_failures.append(x)
    nonfresh_negative = [x for x in visited if x[1:] != (1, 0, x[3]) and (x[1], x[2]) != (1, 0) and defect_U(x) < 0]
    if fresh_two_step_failures or nonfresh_negative:
        raise AssertionError((fresh_two_step_failures, nonfresh_negative))

    # Decisive exact variance and local-budget obstructions.
    raw_variance_x = (6, 2, 1, 2)
    raw_variance_defect = variance(raw_variance_x) - reset_direct(raw_variance_x, True) - Q_variance(raw_variance_x)
    expected_raw_variance_defect = Fraction(-21394206021215, 36917038301316768)
    if raw_variance_defect != expected_raw_variance_defect:
        raise AssertionError(("raw variance", raw_variance_defect))

    full_variance_x = (11, 6, 1, 4)
    full_variance_margin = g(full_variance_x) - variance(full_variance_x)
    if full_variance_margin <= 0:
        raise AssertionError(("full variance", full_variance_margin))

    bessel_x = (8, 1, 0, 3)
    bessel_margin = h(bessel_x) - variance(bessel_x)
    if bessel_margin <= 0:
        raise AssertionError(("h over variance", bessel_margin))

    root_bessel_x = (11, 1, 0, 4)
    root_bessel_margin = reset_direct(root_bessel_x, False) - root_mean_variance(root_bessel_x)
    if root_bessel_margin <= 0:
        raise AssertionError(("A0 over root variance", root_bessel_margin))

    nonprob_x = (12, 32, 5, 4)
    nonprob_H = H((1, 1, 1, 1, 4, 4), 32, 5, 4)
    if nonprob_H != Fraction(16182, 6919):
        raise AssertionError(("nonprobability contextual value", nonprob_H))

    # One common fresh context refutes all eight named interpolants.
    interpolant_x = (11, 1, 0, 4)
    interpolant_rows = []
    for name in coefficients(interpolant_x):
        parent = interpolant(name, interpolant_x)
        deep = sum((mass * interpolant(name, child) for mass, child in deep_children(interpolant_x)), Fraction())
        defect = parent - reset_direct(interpolant_x, True) - deep
        interpolant_rows.append({"name": name, "defect": rec(defect), "refuted": defect < 0})
    if not all(row["refuted"] for row in interpolant_rows):
        raise AssertionError(interpolant_rows)

    # Match each independently reproduced obstruction to its frozen integer.
    frozen_moment = json.loads((M90 / "contextual_second_moment_s12_k32.json").read_text())["result"]
    frozen_structural = json.loads((M90 / "structural_witnesses.json").read_text())["witnesses"]
    frozen_compensators = json.loads((M90 / "compensator_s12_k32.json").read_text())["result"]
    frozen_reachable = json.loads((M90 / "reachable_defect_s12_k32.json").read_text())["result"]

    frozen_full_row = next(
        row for row in frozen_moment["first_failures"]["resolvent_over_variance"]
        if row["context"] == list(full_variance_x)
    )
    frozen_full_margin = (
        fraction_from_record(frozen_full_row["transformed_resolvent"])
        - fraction_from_record(frozen_full_row["variance"])
    )
    frozen_bessel_margin = (
        fraction_from_record(frozen_structural["unweighted_resolvent_exceeds_contextual_variance"]["transformed_unweighted_resolvent"])
        - fraction_from_record(frozen_structural["unweighted_resolvent_exceeds_contextual_variance"]["contextual_variance"])
    )
    frozen_root_bessel_margin = (
        fraction_from_record(frozen_structural["raw_unweighted_reset_energy_exceeds_root_mean_variance"]["A0"])
        - fraction_from_record(frozen_structural["raw_unweighted_reset_energy_exceeds_root_mean_variance"]["variance_of_root_mean"])
    )
    frozen_nonprob_H = fraction_from_record(
        frozen_structural["nonright_contextual_statistic_not_probability_valued"]["contextual_value"]
    )
    frozen_raw_U = next(
        fraction_from_record(row["defect"])
        for row in frozen_reachable["all_negative_defects"]
        if row["context"] == list(defect_x)
    )
    frozen_interpolant_defects = {}
    for name, rows in frozen_compensators["first_failures"].items():
        row = next(row for row in rows if row["context"] == list(interpolant_x))
        frozen_interpolant_defects[name] = fraction_from_record(row["defect"])

    independent_interpolant_defects = {
        row["name"]: fraction_from_record(row["defect"])
        for row in interpolant_rows
    }
    obstruction_matches = {
        "raw_variance": raw_variance_defect == expected_raw_variance_defect,
        "full_context_g_over_variance": full_variance_margin == frozen_full_margin,
        "unweighted_resolvent_over_variance": bessel_margin == frozen_bessel_margin,
        "raw_reset_over_root_variance": root_bessel_margin == frozen_root_bessel_margin,
        "nonright_context_not_probability": nonprob_H == frozen_nonprob_H,
        "raw_U_local_defect": defect_U(defect_x) == frozen_raw_U,
        "all_eight_scalar_interpolants": independent_interpolant_defects == frozen_interpolant_defects,
    }
    if not all(obstruction_matches.values()):
        raise AssertionError(obstruction_matches)

    # Frozen report/range consistency and corrected-source inspection.
    frozen_boundary = json.loads((M90 / "boundary_layer_s20.json").read_text())["result"]
    frozen_unweighted = json.loads((M90 / "exact_unweighted_s20.json").read_text())["result"]
    frozen_weighted20 = json.loads((M90 / "exact_s20_k32.json").read_text())["result"]
    frozen_weighted24 = json.loads((M90 / "exact_s24_k1.json").read_text())["result"]
    frozen_discovery30 = json.loads((M90 / "discovery_s30.json").read_text())["result"]
    frozen_range_checks = {
        "reachable_context_count_38269": frozen_reachable["contexts"] == 38269,
        "reachable_negative_count_7": frozen_reachable["negative_defect_count"] == 7,
        "reachable_nonfresh_negative_count_0": frozen_reachable["negative_nonfresh_defect_count"] == 0,
        "boundary_fresh_seed_count_209": frozen_boundary["fresh_seed_count"] == 209,
        "boundary_closure_count_7334": frozen_boundary["reachable_context_count"] == 7334,
        "boundary_nonfresh_negative_count_0": frozen_boundary["negative_nonfresh_defect_count"] == 0,
        "boundary_fresh_two_step_negative_count_0": frozen_boundary["negative_fresh_two_step_count"] == 0,
        "weighted_s20_no_failures": frozen_weighted20["failure_count"] == 0,
        "weighted_s24_no_failures": frozen_weighted24["failure_count"] == 0,
        "unweighted_s20_no_failures": frozen_unweighted["failure_count"] == 0,
        "unweighted_s20_worst_context": frozen_unweighted["overall_worst"]["context"] == [20, 1, 0, 6],
        "discovery_s30_worst_context": [
            frozen_discovery30["overall_worst"][key] for key in ("s", "K", "R", "B")
        ] == [30, 1, 0, 10],
    }
    if not all(frozen_range_checks.values()):
        raise AssertionError(frozen_range_checks)

    deep_sources = [
        "exact_weighted_resolvent.py",
        "exact_unweighted_resolvent.py",
        "boundary_layer_scan.py",
        "contextual_second_moment.py",
        "compensator_probe.py",
        "defect_filtration_scan.py",
        "discovery_scan.py",
        "resolvent_slack_profile.py",
        "contextual_variance_audit.py",
    ]
    source_all_j_checks = {}
    for name in deep_sources:
        source = (M90 / name).read_text()
        source_all_j_checks[name] = {
            "has_full_rank_loop": "range(1, k + 1)" in source,
            "has_literal_singleton_k_loop": "for j in (k,)" in source,
        }
    if not all(
        row["has_full_rank_loop"] and not row["has_literal_singleton_k_loop"]
        for row in source_all_j_checks.values()
    ):
        raise AssertionError(source_all_j_checks)

    retained_discovery_checks = {}
    for name in ("discovery_s11_k1.json", "discovery_s20.json", "discovery_s30.json"):
        data = json.loads((M90 / name).read_text())
        retained_discovery_checks[name] = "every j>=1" in data["normalization"]
    if not all(retained_discovery_checks.values()):
        raise AssertionError(retained_discovery_checks)

    # The stronger unweighted inequality implies the weighted one termwise.
    implication_rows = []
    for x in (xw8, xw11, defect_x):
        q = q_split(x[0], x[3])
        weighted_value = g(x) / q
        unweighted_value = h(x) / q
        implication_rows.append({
            "context": list(x),
            "Kreset_W": rec(weighted_value),
            "Kreset_1": rec(unweighted_value),
            "W_parent": rec(1 - q),
            "termwise_weighted_le_unweighted": weighted_value <= unweighted_value,
            "finite_unweighted_frontier_pass": unweighted_value <= 1 - q,
        })
    if not all(row["termwise_weighted_le_unweighted"] and row["finite_unweighted_frontier_pass"] for row in implication_rows):
        raise AssertionError(implication_rows)

    payload = {
        "claim_tested": "fresh independent referee audit of frozen M90",
        "status": "exact audit data; finite survival proves no open inequality",
        "convention": "(pq)(x)=p(q(x)); factors displayed left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "arithmetic": "fractions.Fraction; literal compositions and literal canonical basins",
        "elapsed_seconds": time.time() - started,
        "frozen_source": {
            "required_hashes": required_hashes,
            "observed_hashes": observed_hashes,
            "manifest": manifest,
        },
        "normalization": {
            "rank_range": "every j=1,...,k; j=0 is the killed/no-mark branch",
            "rho_normalizations": normalization_rows,
            "direct_vs_grouped_deep_mass_checks": group_checks,
            "negative_hypergeometric_normalization_checks": nu_checks,
            "direct_vs_grouped_reset_reward_checks": reset_group_checks,
        },
        "predecessor_calibrations": calibration_rows,
        "stale_recurrence_exclusion": {
            "context": list(xw11),
            "corrected_all_j_ratio": rec(observed_w11),
            "independent_j_equals_k_only_ratio": rec(stale_ratio),
            "retained_discovery_ratio_binary64": float(retained_discovery_ratio),
            "retained_discovery_normalization": discovery["normalization"],
            "corrected_differs_from_stale": observed_w11 != stale_ratio,
            "source_all_j_checks": source_all_j_checks,
            "retained_discovery_checks": retained_discovery_checks,
        },
        "excursion_and_closure": {
            "fresh_witness_context": list(defect_x),
            "r_U": rec(defect_U(defect_x)),
            "Qr_U": rec(q_r),
            "r_U_plus_Qr_U": rec(defect_U(defect_x) + q_r),
            "U_minus_g": rec(defect_identity_left),
            "defect_resolvent": rec(defect_identity_right),
            "identity_match": defect_identity_left == defect_identity_right,
            "fresh_seed_count_through_s11": sum(range(2, 12)),
            "visited_pure_deep_closure_contexts": len(visited),
            "negative_nonfresh_defects": len(nonfresh_negative),
            "negative_fresh_two_step_blocks": len(fresh_two_step_failures),
        },
        "exact_obstructions": {
            "raw_variance": {"context": list(raw_variance_x), "defect": rec(raw_variance_defect), "matches_frozen": raw_variance_defect == expected_raw_variance_defect},
            "full_context_g_over_variance": {"context": list(full_variance_x), "g_minus_V": rec(full_variance_margin), "refuted": full_variance_margin > 0},
            "unweighted_resolvent_over_variance": {"context": list(bessel_x), "h_minus_V": rec(bessel_margin), "refuted": bessel_margin > 0},
            "raw_reset_over_root_variance": {"context": list(root_bessel_x), "A0_minus_root_variance": rec(root_bessel_margin), "refuted": root_bessel_margin > 0},
            "nonright_context_not_probability": {"context": list(nonprob_x), "root_group": [6, 4], "H": rec(nonprob_H), "exceeds_one": nonprob_H > 1},
            "raw_U_local_defect": {"context": list(defect_x), "defect": rec(defect_U(defect_x)), "refuted": defect_U(defect_x) < 0},
            "scalar_interpolants": {"context": list(interpolant_x), "rows": interpolant_rows},
            "independent_exact_matches_to_frozen": obstruction_matches,
        },
        "frozen_range_consistency": frozen_range_checks,
        "unweighted_implication_finite_checks": implication_rows,
        "scope": "auxiliary nonlazy Pbar_r marked reset occupation only; no Pbar gap, ROOT-MEAN LIFT, original-K gap, Terminal A, or Terminal B",
    }
    output = HERE / "independent_audit.json"
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    output.write_text(encoded)
    print(json.dumps({
        "output": str(output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "elapsed_seconds": payload["elapsed_seconds"],
        "calibrations": calibration_rows,
        "exact_obstructions": payload["exact_obstructions"],
        "closure": payload["excursion_and_closure"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
