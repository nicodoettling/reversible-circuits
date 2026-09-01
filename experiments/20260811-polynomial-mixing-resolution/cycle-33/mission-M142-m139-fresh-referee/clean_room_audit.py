#!/usr/bin/env python3
"""Independent bounded audit of the frozen M139 two-edge-core package.

This file deliberately imports no M139 implementation.  It uses literal
set-partition enumeration for the smallest cases and a separately written
marked-component dynamic program to reach the claimed d=16 counterexample.
Finite positive signs are reported only as finite checks.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import itertools
import json
import math
import platform
import subprocess
import time
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
M139 = (
    ROOT
    / "experiments/20260811-polynomial-mixing-resolution/cycle-32"
    / "mission-M139-two-edge-core-curvature"
)

SUPPLIED_HASHES = {
    "report.md": "3a9998104df900cc8385793acc74b6151784e7920486553a4b4382fbe3b73103",
    "two_edge_core_reduction.md": "cb067b68ac404f60314f4d85bcb3894c15f55abae1b0276ac8a6e5a3238c6461",
    "two_edge_core_scan.py": "605e01db0ca51f2f5b7fd3a3dea4e6449fb546d9acb6a9c7f5bbfb41aaa9e085",
    "two_edge_core_results.json": "f2bdb9a2a43f88e943e59c303182914beede626fbd8a73cbb771e51ae2fd5873",
    "analytic_certificates.json": "ce9d5b037f5a4214473f45b805719e323db611ad3a044ab894ee6e78a5946db6",
    "curvature_budget_results.json": "82845e78055032c6c9f7099058eff8699d190ca94a51cf0e312b4e391b8a4bb6",
    "freeze_manifest.md": "ddbcdc572626bfd72a210082866a967703310f1e6548cb49aff58e99fadbb12f",
    "SHA256SUMS": "aaf23ad3ad94e96d592c5e0234a7432c22dc4790ad229a34880f7e2072db99dd",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
    except Exception:
        return "unavailable"


def integer_partitions(total: int, floor: int = 1):
    """Nondecreasing integer partitions."""
    if total == 0:
        yield ()
        return
    for first in range(floor, total + 1):
        for tail in integer_partitions(total - first, first):
            yield (first,) + tail


@functools.cache
def set_partitions(n: int) -> tuple[tuple[tuple[int, ...], ...], ...]:
    """Literal set partitions in canonical order."""
    if n == 0:
        return ((),)
    if n == 1:
        return (((0,),),)
    answer: list[tuple[tuple[int, ...], ...]] = []
    new = n - 1
    for old in set_partitions(n - 1):
        answer.append(old + ((new,),))
        for index in range(len(old)):
            blocks = list(old)
            blocks[index] = blocks[index] + (new,)
            answer.append(tuple(blocks))
    return tuple(answer)


def memberships(partition: tuple[tuple[int, ...], ...], n: int) -> list[int]:
    owner = [-1] * n
    for block_index, block in enumerate(partition):
        for edge in block:
            owner[edge] = block_index
    assert all(value >= 0 for value in owner)
    return owner


def join_connected(
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
    n: int,
) -> bool:
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> None:
        x, y = find(x), find(y)
        if x != y:
            parent[y] = x

    for partition in (left, right):
        for block in partition:
            for edge in block[1:]:
                union(block[0], edge)
    return n == 0 or len({find(edge) for edge in range(n)}) == 1


def peeled_core_edges(
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
    n: int,
) -> int:
    """Number of edges left after repeatedly deleting degree-one vertices."""
    lo = memberships(left, n)
    ro = memberships(right, n)
    offset = len(left)
    endpoints = [(lo[e], offset + ro[e]) for e in range(n)]
    incidence: list[set[int]] = [set() for _ in range(len(left) + len(right))]
    for edge, (u, v) in enumerate(endpoints):
        incidence[u].add(edge)
        incidence[v].add(edge)
    alive = [True] * n
    queue = [vertex for vertex, edges in enumerate(incidence) if len(edges) <= 1]
    cursor = 0
    while cursor < len(queue):
        vertex = queue[cursor]
        cursor += 1
        live_here = [edge for edge in incidence[vertex] if alive[edge]]
        if len(live_here) > 1:
            continue
        for edge in live_here:
            alive[edge] = False
            u, v = endpoints[edge]
            other = v if u == vertex else u
            if sum(alive[e] for e in incidence[other]) <= 1:
                queue.append(other)
    return sum(alive)


def common_pairs(
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
    n: int,
) -> tuple[tuple[int, int], ...]:
    lo = memberships(left, n)
    ro = memberships(right, n)
    return tuple(
        (a, b)
        for a in range(n)
        for b in range(a + 1, n)
        if lo[a] == lo[b] and ro[a] == ro[b]
    )


def block_weight(partition: tuple[tuple[int, ...], ...], sizes: tuple[int, ...]) -> Fraction:
    result = Fraction(1)
    for block in partition:
        label_sum = sum(sizes[edge] for edge in block)
        result *= Fraction(label_sum) ** (len(block) - 3)
    return result


def literal_two_core_polynomial(sizes: tuple[int, ...]) -> dict[tuple[int, int], Fraction]:
    n = len(sizes)
    output: dict[tuple[int, int], Fraction] = {}
    for left in set_partitions(n):
        left_weight = block_weight(left, sizes)
        for right in set_partitions(n):
            if len(left) + len(right) != n or not join_connected(left, right, n):
                continue
            if peeled_core_edges(left, right, n) != 2:
                continue
            key = (len(left), len(right))
            output[key] = output.get(key, Fraction(0)) + left_weight * block_weight(right, sizes)
    return output


def q(size: int) -> Fraction:
    return Fraction(size ** (2 * size + 1), math.factorial(size) ** 2)


def h(size: int) -> Fraction:
    return Fraction(size**size, math.factorial(size - 1))


def type_multiplier_q(d: int, cycle_type: tuple[int, ...]) -> Fraction:
    answer = Fraction(math.factorial(d))
    for size in sorted(set(cycle_type)):
        multiplicity = cycle_type.count(size)
        answer *= q(size) ** multiplicity / math.factorial(multiplicity)
    return answer


def type_multiplier_original(d: int, cycle_type: tuple[int, ...]) -> Fraction:
    multiplicities = {size: cycle_type.count(size) for size in set(cycle_type)}
    number = math.factorial(d) // math.prod(
        size**count * math.factorial(count)
        for size, count in multiplicities.items()
    )
    answer = Fraction(number)
    for size in cycle_type:
        answer *= h(size) ** 2
    return answer


def subcounts(counts: tuple[int, ...]):
    yield from itertools.product(*(range(count + 1) for count in counts))


def choose_submultiset(counts: tuple[int, ...], chosen: tuple[int, ...]) -> int:
    return math.prod(math.comb(total, take) for total, take in zip(counts, chosen))


def poly_outer(one: dict[int, Fraction]) -> dict[tuple[int, int], Fraction]:
    return {(a, b): x * y for a, x in one.items() for b, y in one.items()}


def poly_convolution(
    first: dict[tuple[int, int], Fraction],
    second: dict[tuple[int, int], Fraction],
) -> dict[tuple[int, int], Fraction]:
    result: dict[tuple[int, int], Fraction] = {}
    for (a, b), x in first.items():
        for (c, d), y in second.items():
            key = (a + c, b + d)
            result[key] = result.get(key, Fraction(0)) + x * y
    return result


class CleanMarkedDP:
    """Independent multiset implementation of the marked-component formulas."""

    def __init__(self, sizes: tuple[int, ...]):
        self.sizes = sizes

    @functools.cache
    def ordinary(self, counts: tuple[int, ...]) -> dict[int, Fraction]:
        if sum(counts) == 0:
            return {0: Fraction(1)}
        root = max(index for index, count in enumerate(counts) if count)
        available = list(counts)
        available[root] -= 1
        result: dict[int, Fraction] = {}
        for extras in subcounts(tuple(available)):
            block = list(extras)
            block[root] += 1
            block_tuple = tuple(block)
            multiplicity = choose_submultiset(tuple(available), extras)
            cardinality = sum(block_tuple)
            label_sum = sum(size * count for size, count in zip(self.sizes, block_tuple))
            weight = Fraction(label_sum) ** (cardinality - 3)
            remainder = tuple(total - take for total, take in zip(counts, block_tuple))
            for blocks, value in self.ordinary(remainder).items():
                degree = blocks + 1
                result[degree] = result.get(degree, Fraction(0)) + multiplicity * weight * value
        return result

    @functools.cache
    def arbitrary(self, counts: tuple[int, ...]) -> dict[tuple[int, int], Fraction]:
        return poly_outer(self.ordinary(counts))

    @functools.cache
    def co_blocked_one(
        self, mark_a: int, mark_b: int, counts: tuple[int, ...]
    ) -> dict[int, Fraction]:
        result: dict[int, Fraction] = {}
        for selected in subcounts(counts):
            multiplicity = choose_submultiset(counts, selected)
            label_sum = mark_a + mark_b + sum(
                size * count for size, count in zip(self.sizes, selected)
            )
            marked_weight = Fraction(label_sum) ** (sum(selected) - 1)
            remainder = tuple(total - take for total, take in zip(counts, selected))
            for blocks, value in self.ordinary(remainder).items():
                degree = blocks + 1
                result[degree] = result.get(degree, Fraction(0)) + multiplicity * marked_weight * value
        return result

    @functools.cache
    def marked_connected(
        self, mark_a: int, mark_b: int, counts: tuple[int, ...]
    ) -> dict[tuple[int, int], Fraction]:
        result = poly_outer(self.co_blocked_one(mark_a, mark_b, counts))
        for selected in subcounts(counts):
            if selected == counts:
                continue
            multiplicity = choose_submultiset(counts, selected)
            remainder = tuple(total - take for total, take in zip(counts, selected))
            product = poly_convolution(
                self.marked_connected(mark_a, mark_b, selected),
                self.arbitrary(remainder),
            )
            for key, value in product.items():
                result[key] = result.get(key, Fraction(0)) - multiplicity * value
        return {key: value for key, value in result.items() if value}

    def two_core_polynomial(self, cycle_type: tuple[int, ...]) -> dict[tuple[int, int], Fraction]:
        initial = tuple(cycle_type.count(size) for size in self.sizes)
        answer: dict[tuple[int, int], Fraction] = {}
        for i, a in enumerate(self.sizes):
            for j in range(i, len(self.sizes)):
                b = self.sizes[j]
                if i == j:
                    pair_count = math.comb(initial[i], 2)
                else:
                    pair_count = initial[i] * initial[j]
                if pair_count == 0:
                    continue
                remainder = list(initial)
                remainder[i] -= 1
                remainder[j] -= 1
                marked = self.marked_connected(a, b, tuple(remainder))
                for key, value in marked.items():
                    answer[key] = answer.get(key, Fraction(0)) + pair_count * value
        return answer


def h2_row(d: int, literal: bool = False) -> dict[int, int]:
    row: dict[int, Fraction] = {}
    for cycle_type in integer_partitions(d):
        cycles = len(cycle_type)
        if cycles < 2:
            continue
        if literal:
            incidence = literal_two_core_polynomial(cycle_type)
        else:
            distinct = tuple(sorted(set(cycle_type)))
            incidence = CleanMarkedDP(distinct).two_core_polynomial(cycle_type)
        subtotal = Fraction(0)
        multiplier = type_multiplier_q(d, cycle_type)
        for left in range(1, cycles):
            right = cycles - left
            value = incidence.get((left, right), Fraction(0))
            cut = d + cycles - 2 * left
            subtotal += multiplier * math.factorial(cut) * math.factorial(2 * d - cut) * value
        row[cycles] = row.get(cycles, Fraction(0)) + subtotal
    assert all(value.denominator == 1 for value in row.values())
    return {cycles: value.numerator for cycles, value in row.items()}


def boundary_two(d: int) -> Fraction:
    convolution = sum((q(a) * q(d - a) for a in range(1, d)), Fraction(0))
    return Fraction(math.factorial(d) ** 3, 2 * d * d) * convolution


def boundary_three(d: int) -> Fraction:
    coefficient = Fraction(0)
    for n in range(2, d):
        core = sum((q(a) * q(n - a) for a in range(1, n)), Fraction(0))
        coefficient += core * q(d - n) / (n * (d - n) ** 2)
    return math.factorial(d) * math.factorial(d - 1) * math.factorial(d + 1) * coefficient


def series_add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    return [x + y for x, y in zip(a, b)]


def series_scale(a: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return [scalar * x for x in a]


def series_exp(a: list[Fraction]) -> list[Fraction]:
    assert a[0] == 0
    degree = len(a) - 1
    result = [Fraction(0)] * (degree + 1)
    result[0] = 1
    for n in range(1, degree + 1):
        result[n] = sum(
            k * a[k] * result[n - k] for k in range(1, n + 1)
        ) / n
    return result


def lagrange_specialization(
    child_weights: dict[int, Fraction], s: int, degree: int
) -> tuple[list[Fraction], list[Fraction], list[Fraction]]:
    tau = [Fraction(0)] * (degree + 1)
    for _ in range(degree + 2):
        inside = [Fraction(0)] * (degree + 1)
        for b, weight in child_weights.items():
            inside = series_add(inside, series_scale(series_exp(series_scale(tau, b)), weight))
        tau = [Fraction(0)] + inside[:degree]
    lagrange = series_scale(series_exp(series_scale(tau, s)), Fraction(1, s))
    direct_psi = [Fraction(0)] * (degree + 1)
    direct_phi = [Fraction(0)] * (degree + 1)
    direct_psi[0] = Fraction(1, s)
    direct_phi[0] = Fraction(1, s * s)
    alphabet = tuple(child_weights)
    for k in range(1, degree + 1):
        for children in itertools.product(alphabet, repeat=k):
            child_sum = sum(children)
            product = math.prod(child_weights[b] for b in children)
            direct_psi[k] += (
                product * Fraction(s + child_sum) ** (k - 1) / math.factorial(k)
            )
            direct_phi[k] += (
                product * Fraction(s + child_sum) ** (k - 2) / math.factorial(k)
            )
    return lagrange, direct_psi, direct_phi


def kernel_minor(s1: int, s2: int, total1: int, total2: int, k: int) -> Fraction:
    def entry(s: int, total: int) -> Fraction:
        return Fraction(s + total) ** (k - 2) / math.factorial(k)

    return entry(s1, total1) * entry(s2, total2) - entry(s1, total2) * entry(s2, total1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-d", type=int, default=16)
    args = parser.parse_args()
    if args.max_d != 16:
        raise SystemExit("this frozen audit is intentionally capped at d=16")
    started = time.time()

    supplied_hash_checks = {
        name: {"expected": expected, "observed": sha256(M139 / name)}
        for name, expected in SUPPLIED_HASHES.items()
    }
    inventory_checks = []
    for line in (M139 / "SHA256SUMS").read_text().splitlines():
        expected, name = line.split(None, 1)
        name = name.strip()
        inventory_checks.append(
            {"file": name, "expected": expected, "observed": sha256(M139 / name)}
        )

    topology = []
    topology_failures = []
    for n in range(2, 7):
        tested = 0
        two_core = 0
        for left in set_partitions(n):
            for right in set_partitions(n):
                if len(left) + len(right) != n or not join_connected(left, right, n):
                    continue
                tested += 1
                core_length = peeled_core_edges(left, right, n)
                pairs = common_pairs(left, right, n)
                if core_length == 2:
                    two_core += 1
                if (core_length == 2) != (len(pairs) == 1):
                    topology_failures.append(
                        {"n": n, "left": left, "right": right, "core": core_length, "pairs": pairs}
                    )
        topology.append({"atoms": n, "connected_unicycles": tested, "two_core": two_core})

    q_failures = []
    q_case_count = 0
    for d in range(1, 9):
        for cycle_type in integer_partitions(d):
            q_case_count += 1
            if type_multiplier_q(d, cycle_type) != type_multiplier_original(d, cycle_type):
                q_failures.append({"d": d, "cycle_type": cycle_type})

    rows: dict[int, dict[int, int]] = {}
    row_times: dict[int, float] = {}
    literal_comparisons = []
    for d in range(2, args.max_d + 1):
        case_started = time.time()
        rows[d] = h2_row(d)
        row_times[d] = time.time() - case_started
        if d <= 5:
            literal = h2_row(d, literal=True)
            literal_comparisons.append({"d": d, "match": literal == rows[d]})
        print(f"d={d} elapsed={row_times[d]:.3f}s", flush=True)

    frozen_payload = json.loads((M139 / "two_edge_core_results.json").read_text())
    frozen_rows = {
        record["d"]: {
            int(c): int(value)
            for c, value in record["masses_by_cycles"].items()
        }
        for record in frozen_payload["records"]
        if record["d"] <= args.max_d
    }
    frozen_row_comparisons = [
        {"d": d, "match": rows[d] == frozen_rows[d]}
        for d in range(2, args.max_d + 1)
    ]

    pair_factor_checks = {
        "equal_size": str(Fraction(1, 2) * q(2) * q(2)),
        "equal_size_expected": str(q(2) ** 2 / math.factorial(2)),
        "unequal_size": str(Fraction(1, 2) * (q(1) * q(2) + q(2) * q(1))),
        "unequal_size_expected": str(q(1) * q(2)),
    }

    boundary_checks = []
    for d, row in rows.items():
        record = {
            "d": d,
            "c2_formula": str(boundary_two(d)),
            "c2_observed": str(row[2]),
            "c2_match": boundary_two(d) == row[2],
        }
        if d >= 3:
            record.update(
                {
                    "c3_formula": str(boundary_three(d)),
                    "c3_observed": str(row[3]),
                    "c3_match": boundary_three(d) == row[3],
                }
            )
        boundary_checks.append(record)

    lagrange_checks = []
    for weights in ({1: Fraction(1), 2: Fraction(2)}, {1: Fraction(3, 2), 3: Fraction(1, 3)}):
        for s in range(1, 5):
            lagrange, psi, phi = lagrange_specialization(weights, s, 5)
            # The integral representation gives each ordered child tuple one
            # extra factor 1/(s+sum children), hence exactly direct Phi.
            phi_integral = [Fraction(0)] * 6
            phi_integral[0] = Fraction(1, s * s)
            alphabet = tuple(weights)
            for k in range(1, 6):
                for children in itertools.product(alphabet, repeat=k):
                    total = sum(children)
                    product = math.prod(weights[b] for b in children)
                    psi_term = (
                        product * Fraction(s + total) ** (k - 1) / math.factorial(k)
                    )
                    phi_integral[k] += psi_term / (s + total)
            lagrange_checks.append(
                {
                    "weights": {str(k): str(v) for k, v in weights.items()},
                    "s": s,
                    "lagrange_match": lagrange == psi,
                    "k0": str(lagrange[0]),
                    "k0_expected": str(Fraction(1, s)),
                    "phi_integral_match": phi_integral == phi,
                }
            )

    q_poly = {a: q(a) for a in range(1, 5)}
    i2_checks = []
    for n in range(2, 9):
        convolution = sum(
            (q_poly.get(a, 0) * q_poly.get(n - a, 0) for a in range(1, n)),
            Fraction(0),
        )
        direct = sum(
            (
                qa * qb / (a + b) ** 2
                for a, qa in q_poly.items()
                for b, qb in q_poly.items()
                if a + b == n
            ),
            Fraction(0),
        )
        i2_checks.append({"degree": n, "match": direct == convolution / n**2})

    beta_checks = []
    for d in range(2, 9):
        for c in range(2, d + 1):
            for left in range(1, c):
                right = c - left
                cut = d + c - 2 * left
                beta_value = Fraction(
                    math.factorial(cut) * math.factorial(2 * d - cut),
                    math.factorial(2 * d + 1),
                )
                beta_checks.append(
                    {
                        "d": d,
                        "c": c,
                        "left": left,
                        "right": right,
                        "t_exponent_match": d + right - left == cut,
                        "one_minus_t_exponent_match": d + left - right == 2 * d - cut,
                        "beta_positive": beta_value > 0,
                    }
                )

    first_shifted = None
    first_inverse_linear = None
    first_inverse_square = None
    ordinary_failures = []
    for d, row in rows.items():
        for c in range(3, d):
            centre = row[c]
            sides = row[c - 1] * row[c + 1]
            if centre * centre < sides:
                ordinary_failures.append({"d": d, "c": c})
            index = c - 2
            degree = d - 2
            shifted = index * (degree - index) * centre * centre - (
                (index + 1) * (degree - index + 1) * sides
            )
            inverse_linear = d * centre * centre - (d + 1) * sides
            inverse_square = d * d * centre * centre - (d * d + 1) * sides
            item = {"d": d, "c": c}
            if shifted < 0 and first_shifted is None:
                first_shifted = {**item, "margin": str(shifted)}
            if inverse_linear < 0 and first_inverse_linear is None:
                first_inverse_linear = {**item, "margin": str(inverse_linear)}
            if inverse_square < 0 and first_inverse_square is None:
                first_inverse_square = {**item, "margin": str(inverse_square)}

    d4 = rows[4]
    d16 = rows[16]
    shifted_margin = d4[3] ** 2 - 4 * d4[2] * d4[4]
    inverse_linear_margin = 16 * d16[12] ** 2 - 17 * d16[11] * d16[13]
    claimed_d16 = {
        11: 15339706693275758759417829532728706703572126924800000,
        12: 8801172795119208736433518466349564786249616588800000,
        13: 4798920138978605227248331071925220344236657868800000,
    }
    claimed_inverse_margin = -12068184285817619472004173248675719963879857493070204183335383575630227635520668657140147159040000000000

    tp_minors = {
        str(k): str(kernel_minor(1, 2, 1, 2, k)) for k in range(5)
    }
    scalar_phi = [
        Fraction(1 + k) ** (k - 2) / math.factorial(k) for k in range(4)
    ]

    payload = {
        "claim_scope": "fresh exact bounded audit; finite positive signs are not asymptotic theorems",
        "target": "auxiliary incidence-law two-parallel-edge profile H_2[d,c]",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "arguments": {"max_d": args.max_d, "literal_max_d": 5, "topology_max_atoms": 6},
        "integrity": {
            "supplied": supplied_hash_checks,
            "supplied_failure_count": sum(v["expected"] != v["observed"] for v in supplied_hash_checks.values()),
            "inventory": inventory_checks,
            "inventory_failure_count": sum(v["expected"] != v["observed"] for v in inventory_checks),
        },
        "marked_pair_topology": {
            "records": topology,
            "failure_count": len(topology_failures),
            "failures": topology_failures,
        },
        "atom_weight_translation": {"case_count": q_case_count, "failure_count": len(q_failures), "failures": q_failures},
        "literal_vs_marked": literal_comparisons,
        "independent_vs_frozen_rows": frozen_row_comparisons,
        "independent_vs_frozen_failure_count": sum(
            not item["match"] for item in frozen_row_comparisons
        ),
        "unordered_pair_factor_checks": pair_factor_checks,
        "rows": {str(d): {str(c): str(value) for c, value in sorted(row.items())} for d, row in rows.items()},
        "row_elapsed_seconds": {str(d): value for d, value in row_times.items()},
        "boundary_checks": boundary_checks,
        "boundary_failure_count": sum(
            (not item["c2_match"]) or ("c3_match" in item and not item["c3_match"])
            for item in boundary_checks
        ),
        "formal_transform_checks": {
            "lagrange_phi": lagrange_checks,
            "failure_count": sum(
                (not item["lagrange_match"])
                or (item["k0"] != item["k0_expected"])
                or (not item["phi_integral_match"])
                for item in lagrange_checks
            ),
            "i2": i2_checks,
            "i2_failure_count": sum(not item["match"] for item in i2_checks),
        },
        "beta_checks": {
            "case_count": len(beta_checks),
            "failure_count": sum(
                (not item["t_exponent_match"])
                or (not item["one_minus_t_exponent_match"])
                or (not item["beta_positive"])
                for item in beta_checks
            ),
        },
        "counterexamples": {
            "d4_row": {str(c): str(d4[c]) for c in (2, 3, 4)},
            "d4_matches_claim": tuple(d4[c] for c in (2, 3, 4)) == (80136, 109440, 44928),
            "shifted_ulc_margin": str(shifted_margin),
            "shifted_ulc_margin_matches_claim": shifted_margin == -2424287232,
            "first_shifted_ulc_failure_through_d16": first_shifted,
            "d16_values": {str(c): str(d16[c]) for c in (11, 12, 13)},
            "d16_values_match_claim": all(d16[c] == value for c, value in claimed_d16.items()),
            "inverse_linear_margin": str(inverse_linear_margin),
            "inverse_linear_margin_matches_claim": inverse_linear_margin == claimed_inverse_margin,
            "first_inverse_linear_failure_through_d16": first_inverse_linear,
            "first_inverse_square_failure_through_d16": first_inverse_square,
            "ordinary_h2_failures_through_d16": ordinary_failures,
        },
        "tp_obstruction": {
            "test_minors_k0_to_k4": tp_minors,
            "scalar_phi_first_four": [str(value) for value in scalar_phi],
            "scalar_first_lc_margin": str(scalar_phi[1] ** 2 - scalar_phi[0] * scalar_phi[2]),
        },
        "elapsed_seconds": time.time() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        "failures",
        payload["integrity"]["supplied_failure_count"],
        payload["integrity"]["inventory_failure_count"],
        payload["marked_pair_topology"]["failure_count"],
        payload["atom_weight_translation"]["failure_count"],
        sum(not item["match"] for item in literal_comparisons),
        payload["boundary_failure_count"],
        payload["formal_transform_checks"]["failure_count"],
        payload["formal_transform_checks"]["i2_failure_count"],
        payload["beta_checks"]["failure_count"],
    )
    print("first_shifted", first_shifted)
    print("first_inverse_linear", first_inverse_linear)
    print("wrote", args.output, sha256(args.output))


if __name__ == "__main__":
    main()
