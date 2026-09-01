#!/usr/bin/env python3
"""Import-free exact audit of the finite claims used by M274.

This is a clean-room reconstruction from the stated permutation and
completion-count formulas.  It imports no project code.  Exact finite checks
can refute universal sign/order claims but cannot prove asymptotic OS+ or MS.
Convention: (pq)(x)=p(q(x)); factor tuples multiply left-to-right.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


Perm = tuple[int, ...]
Vector = list[Fraction]


def mul(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[i]] for i in range(len(p)))


def inv(p: Perm) -> Perm:
    out = [0] * len(p)
    for i, image in enumerate(p):
        out[image] = i
    return tuple(out)


def transposition(n: int, a: int, b: int) -> Perm:
    out = list(range(n))
    out[a], out[b] = out[b], out[a]
    return tuple(out)


def oriented_cycle(n: int, entries: tuple[int, ...] | list[int]) -> Perm:
    entries = tuple(entries)
    out = list(range(n))
    for a, b in zip(entries, entries[1:] + entries[:1]):
        out[a] = b
    return tuple(out)


def cycles(p: Perm) -> list[list[int]]:
    seen: set[int] = set()
    answer: list[list[int]] = []
    for start in range(len(p)):
        if start in seen:
            continue
        cycle: list[int] = []
        x = start
        while x not in seen:
            seen.add(x)
            cycle.append(x)
            x = p[x]
        answer.append(cycle)
    return answer


def completion_count(p: Perm, rank: int) -> int:
    sizes = [len(cycle) for cycle in cycles(p)]
    if len(p) - len(sizes) != rank:
        return 0
    answer = math.factorial(rank)
    for size in sizes:
        if size > 1:
            answer = answer * size ** (size - 2) // math.factorial(size - 1)
    return answer


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def dot(left: Vector, right: Vector) -> Fraction:
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def difference(left: Vector, right: Vector) -> Vector:
    return [a - b for a, b in zip(left, right)]


def quotient_kernel(n: int) -> tuple[Perm, list[list[Perm]], list[Vector], Vector]:
    """Construct the exact cyclic-orbit quotient directly from ordered lifts."""
    h = tuple((i + 1) % n for i in range(n))
    hi = inv(h)
    gates = [transposition(n, i, j) for i in range(n) for j in range(i + 1, n)]
    lift_multiplicity: Counter[Perm] = Counter(mul(a, b) for a in gates for b in gates)
    marginal = {
        state: multiplicity * completion_count(mul(inv(state), h), n - 3)
        for state, multiplicity in lift_multiplicity.items()
    }
    marginal = {state: mass for state, mass in marginal.items() if mass}

    orbit_id: dict[Perm, int] = {}
    orbits: list[list[Perm]] = []
    for state in sorted(marginal):
        if state in orbit_id:
            continue
        orbit: list[Perm] = []
        x = state
        while x not in orbit:
            orbit.append(x)
            x = mul(hi, mul(x, h))
        index = len(orbits)
        for x in orbit:
            orbit_id[x] = index
        orbits.append(orbit)

    dimension = len(orbits)
    kernel = [[Fraction(0) for _ in range(dimension)] for _ in range(dimension)]
    for source_index, orbit in enumerate(orbits):
        source = orbit[0]
        denominator = completion_count(mul(inv(source), h), n - 3)
        for target in marginal:
            remainder = mul(inv(mul(source, target)), h)
            numerator = lift_multiplicity[target] * completion_count(remainder, n - 5)
            if numerator:
                kernel[source_index][orbit_id[target]] += Fraction(numerator, denominator)
        assert sum(kernel[source_index], Fraction(0)) == 1

    pi = [Fraction(len(orbit) * marginal[orbit[0]], n ** (n - 2)) for orbit in orbits]
    assert sum(pi, Fraction(0)) == 1
    return h, orbits, kernel, pi


def smaller_split(edge: Perm, component: list[int]) -> int:
    endpoints = [i for i, image in enumerate(edge) if i != image]
    positions = sorted(component.index(endpoint) for endpoint in endpoints)
    gap = positions[1] - positions[0]
    return min(gap, len(component) - gap)


def internal_edges(n: int, component: list[int]) -> list[Perm]:
    vertices = sorted(component)
    return [
        transposition(n, vertices[i], vertices[j])
        for i in range(len(vertices))
        for j in range(i + 1, len(vertices))
    ]


def first_edge_law(n: int, component: list[int]) -> dict[Perm, Fraction]:
    residual = oriented_cycle(n, component)
    size = len(component)
    law: dict[Perm, Fraction] = {}
    for edge in internal_edges(n, component):
        numerator = completion_count(mul(edge, residual), size - 2)
        if numerator:
            law[edge] = Fraction(numerator, size ** (size - 2))
    assert sum(law.values(), Fraction(0)) == 1
    return law


def product_mixture(
    components: list[list[int]],
    laws: list[dict[Perm, Fraction]],
    other: dict[Perm, Fraction] | None,
    orbit_id: dict[Perm, int],
    dimension: int,
) -> tuple[dict[int, Fraction], dict[int, Vector]]:
    masses: dict[int, Fraction] = defaultdict(Fraction)
    raw: dict[int, Vector] = defaultdict(lambda: [Fraction(0)] * dimension)
    for component, law in zip(components, laws):
        for edge, edge_probability in law.items():
            split = smaller_split(edge, component)
            base = edge_probability / len(components)
            if other is None:
                raw[split][orbit_id[edge]] += base
                masses[split] += base
            else:
                for second, second_probability in other.items():
                    probability = base * second_probability
                    raw[split][orbit_id[mul(edge, second)]] += probability
                    masses[split] += probability
    assert sum(masses.values(), Fraction(0)) == 1
    conditional = {
        split: [entry / masses[split] for entry in row]
        for split, row in raw.items()
    }
    return dict(masses), conditional


def ordered_pair_law(
    n: int,
    residual: Perm,
    components: list[list[int]],
    orbit_id: dict[Perm, int],
    dimension: int,
) -> tuple[dict[int, Fraction], dict[int, Vector]]:
    rank = n - len(cycles(residual))
    denominator = completion_count(residual, rank)
    component_of = {vertex: component for component in components for vertex in component}
    masses: dict[int, Fraction] = defaultdict(Fraction)
    raw: dict[int, Vector] = defaultdict(lambda: [Fraction(0)] * dimension)
    for first in [edge for component in components for edge in internal_edges(n, component)]:
        endpoint = next(i for i, image in enumerate(first) if i != image)
        split = smaller_split(first, component_of[endpoint])
        after_first = mul(first, residual)
        next_edges = [
            edge
            for component in cycles(after_first)
            if len(component) > 1
            for edge in internal_edges(n, component)
        ]
        for second in next_edges:
            product = mul(first, second)
            numerator = completion_count(mul(inv(product), residual), rank - 2)
            if not numerator:
                continue
            probability = Fraction(numerator, denominator)
            masses[split] += probability
            raw[split][orbit_id[product]] += probability
    assert sum(masses.values(), Fraction(0)) == 1
    conditional = {
        split: [entry / masses[split] for entry in row]
        for split, row in raw.items()
    }
    return dict(masses), conditional


def unconditional(masses: dict[int, Fraction], rows: dict[int, Vector], dimension: int) -> Vector:
    answer = [Fraction(0)] * dimension
    for split, mass in masses.items():
        for index, entry in enumerate(rows[split]):
            answer[index] += mass * entry
    assert sum(answer, Fraction(0)) == 1
    return answer


def audit_rank(k: int) -> dict[str, object]:
    n = 3 * k
    h, orbits, kernel, pi = quotient_kernel(n)
    dimension = len(orbits)
    orbit_id = {state: index for index, orbit in enumerate(orbits) for state in orbit}
    source_a = oriented_cycle(n, (0, k, 2 * k))
    source_b = mul(transposition(n, 0, 1), transposition(n, k, 2 * k))
    ai, bi = orbit_id[source_a], orbit_id[source_b]
    components_a = cycles(mul(inv(source_a), h))
    components_b = cycles(mul(inv(source_b), h))
    cminus = next(component for component in components_a if 0 in component)
    middle = next(component for component in components_a if k in component)
    cplus = next(component for component in components_a if 2 * k in component)
    long_cycle = next(component for component in components_b if len(component) == 2 * k - 1)

    nu_minus = first_edge_law(n, cminus)
    nu_middle = first_edge_law(n, middle)
    nu_plus = first_edge_law(n, cplus)
    nu_long = first_edge_law(n, long_cycle)
    p1, phi1 = product_mixture([long_cycle], [nu_long], nu_middle, orbit_id, dimension)
    q1, psi1 = product_mixture(
        [cminus, cplus], [nu_minus, nu_plus], nu_middle, orbit_id, dimension
    )
    p2, phi2 = ordered_pair_law(
        n, oriented_cycle(n, long_cycle), [long_cycle], orbit_id, dimension
    )
    separate = mul(oriented_cycle(n, cminus), oriented_cycle(n, cplus))
    q2, psi2 = ordered_pair_law(n, separate, [cminus, cplus], orbit_id, dimension)
    assert p1 == p2 and q1 == q2
    p, qmass = p1, q1
    phis = {1: phi1, 2: phi2}
    psis = {1: psi1, 2: psi2}
    law_b = {j: unconditional(p, phis[j], dimension) for j in (1, 2)}
    law_a = {j: unconditional(qmass, psis[j], dimension) for j in (1, 2)}

    cumulative: dict[int, Fraction] = {}
    running = Fraction(0)
    for u in range(1, k):
        running += p.get(u, Fraction(0)) - qmass.get(u, Fraction(0))
        cumulative[u] = running
    assert cumulative[k - 1] == 0

    rank = k - 1
    denominator = 3 * rank * (3 * rank - 1)
    alpha = {
        1: Fraction(4 * rank * rank, denominator),
        2: Fraction(2 * rank * (2 * rank - 1), denominator),
    }
    violations: list[dict[str, object]] = []
    fosd: list[dict[str, object]] = []
    block_counts = {
        f"J{j}_{block}": {"negative": 0, "zero": 0, "positive": 0}
        for j in (1, 2)
        for block in ("gradient", "embedding")
    }
    rows: list[dict[str, object]] = []
    for y in range(1, n - 2):
        target = mul(transposition(n, 0, 1), transposition(n, y + 1, y + 2))
        target_index = orbit_id[target]
        response = [kernel[source][target_index] / pi[target_index] for source in range(dimension)]
        blocks: dict[str, Fraction] = {}
        channel_scores: dict[int, Fraction] = {}
        for channel in (1, 2):
            phi_response = {u: dot(row, response) for u, row in phis[channel].items()}
            psi_response = {u: dot(row, response) for u, row in psis[channel].items()}
            gradient = Fraction(0)
            for u in range(1, k - 1):
                increment = phi_response[u + 1] - phi_response[u]
                if increment < 0:
                    violations.append({
                        "type": "adjacent", "channel": channel, "u": u,
                        "y": y, "defect": qstr(increment),
                    })
                gradient += cumulative[u] * (phi_response[u] - phi_response[u + 1])
            embedding = Fraction(0)
            for u, mass in qmass.items():
                defect = phi_response[u] - psi_response[u]
                if defect < 0:
                    violations.append({
                        "type": "embedding", "channel": channel, "u": u,
                        "y": y, "defect": qstr(defect),
                    })
                embedding += mass * defect
            blocks[f"J{channel}_gradient"] = alpha[channel] * gradient
            blocks[f"J{channel}_embedding"] = alpha[channel] * embedding
            channel_scores[channel] = dot(difference(law_b[channel], law_a[channel]), response)

            mass_b: dict[Fraction, Fraction] = defaultdict(Fraction)
            mass_a: dict[Fraction, Fraction] = defaultdict(Fraction)
            for index, value in enumerate(response):
                mass_b[value] += law_b[channel][index]
                mass_a[value] += law_a[channel][index]
            tail_b = tail_a = Fraction(0)
            for threshold in sorted(set(response), reverse=True):
                tail_b += mass_b[threshold]
                tail_a += mass_a[threshold]
                if tail_b < tail_a:
                    fosd.append({
                        "channel": channel, "y": y, "threshold": qstr(threshold),
                        "defect": qstr(tail_b - tail_a),
                    })

        for name, value in blocks.items():
            block_counts[name]["positive" if value > 0 else "negative" if value < 0 else "zero"] += 1
        direct = dot(difference(kernel[bi], kernel[ai]), response)
        reconstructed = sum(blocks.values(), Fraction(0))
        assert direct == reconstructed
        assert direct == sum((alpha[j] * channel_scores[j] for j in (1, 2)), Fraction(0))
        rows.append({
            "y": y,
            "score": qstr(direct),
            "channel_scores": {str(j): qstr(channel_scores[j]) for j in (1, 2)},
            "blocks": {name: qstr(value) for name, value in blocks.items()},
        })

    scores = [Fraction(row["score"]) for row in rows]
    channel_scores = {
        j: [Fraction(row["channel_scores"][str(j)]) for row in rows]
        for j in (1, 2)
    }
    weighted_minima = {j: min(alpha[j] * value for value in channel_scores[j]) for j in (1, 2)}
    positive = sum((value for value in scores if value > 0), Fraction(0))
    negative = sum((-value for value in scores if value < 0), Fraction(0))
    pcs_ms_left = sum((abs(k * value) for value in scores), Fraction(0))
    pcs_ms_right = k * abs(sum(scores, Fraction(0))) + 2 * k * min(positive, negative)
    assert pcs_ms_left == pcs_ms_right
    assert scores == list(reversed(scores))
    first = {
        kind: next((row for row in violations if row["type"] == kind), None)
        for kind in ("adjacent", "embedding")
    }
    result = {
        "k": k,
        "n": n,
        "quotient_states": dimension,
        "target_rows": len(rows),
        "mon_violations": len(violations),
        "violations_by_type": {
            kind: sum(row["type"] == kind for row in violations)
            for kind in ("adjacent", "embedding")
        },
        "first_violation_by_type": first,
        "fosd_violations": len(fosd),
        "first_fosd_violation": fosd[0] if fosd else None,
        "block_sign_counts": block_counts,
        "all_complete_scores_nonnegative": all(value >= 0 for value in scores),
        "all_complete_scores_strictly_positive": all(value > 0 for value in scores),
        "all_channel_scores_nonnegative": all(
            Fraction(row["channel_scores"][str(j)]) >= 0 for row in rows for j in (1, 2)
        ),
        "all_channel_scores_strictly_positive": all(
            value > 0 for values in channel_scores.values() for value in values
        ),
        "minimum_weighted_channel_scores": {
            str(j): qstr(weighted_minima[j]) for j in (1, 2)
        },
        "reflection_exact": True,
        "pcs_ms_identity_exact": True,
        "positive_mass": qstr(positive),
        "negative_mass": qstr(negative),
        "rows": rows,
    }
    expected = {
        3: (4, {"adjacent": 0, "embedding": 4}, 36),
        5: (46, {"adjacent": 32, "embedding": 14}, 250),
    }[k]
    assert (result["mon_violations"], result["violations_by_type"], result["fosd_violations"]) == expected
    if k == 3:
        assert first["embedding"] == {
            "type": "embedding", "channel": 1, "u": 1, "y": 2,
            "defect": "-876877452441/14123762450000",
        }
        assert result["first_fosd_violation"] == {
            "channel": 1, "y": 1, "threshold": "343359/268912", "defect": "-32/375",
        }
    expected_minima = {
        3: {
            "1": "29326617178443/882735153125000",
            "2": "288372901815351/3530940612500000",
        },
        5: {
            "1": "469380953030255528575240193615921483304253622141733093283/62593163860600167157006651607817304625660070187459136716800",
            "2": "12355546254704689070281046180638277338919762446656677440681/751117966327202005884079819293807655507920842249509640601600",
        },
    }
    assert result["minimum_weighted_channel_scores"] == expected_minima[k]
    assert result["all_complete_scores_strictly_positive"]
    assert result["all_channel_scores_strictly_positive"]
    return result


def raw_atom_witness(k: int) -> dict[str, object]:
    """Check the two signed ordered atoms used in the all-odd-k refutation."""
    n = 3 * k
    h = tuple((i + 1) % n for i in range(n))
    source_a = oriented_cycle(n, (0, k, 2 * k))
    source_b = mul(transposition(n, 0, 1), transposition(n, k, 2 * k))
    components_a = cycles(mul(inv(source_a), h))
    components_b = cycles(mul(inv(source_b), h))
    cminus = next(component for component in components_a if 0 in component)
    cplus = next(component for component in components_a if 2 * k in component)
    middle = next(component for component in components_a if k in component)
    long_cycle = next(component for component in components_b if len(component) == 2 * k - 1)
    e_positive = transposition(n, 1, 2 * k)
    e_negative = transposition(n, 0, 1)
    middle_edge = transposition(n, k, k + 1)
    second = transposition(n, 1, 2)
    assert e_positive in internal_edges(n, long_cycle)
    assert e_negative in internal_edges(n, cminus)
    assert middle_edge in internal_edges(n, middle)
    assert first_edge_law(n, long_cycle)[e_positive] > 0
    assert first_edge_law(n, cminus)[e_negative] > 0

    long_residual = oriented_cycle(n, long_cycle)
    separate_residual = mul(oriented_cycle(n, cminus), oriented_cycle(n, cplus))
    rank = 2 * k - 2
    positive_completion = completion_count(
        mul(inv(mul(e_positive, second)), long_residual), rank - 2
    )
    negative_completion = completion_count(
        mul(inv(mul(e_negative, second)), separate_residual), rank - 2
    )
    assert positive_completion > 0 and negative_completion > 0
    return {
        "k": k,
        "channel1_B_atom_positive": True,
        "channel1_A_atom_negative": True,
        "channel2_B_ordered_atom_positive": True,
        "channel2_A_ordered_atom_negative": True,
        "channel2_completion_counts": [positive_completion, negative_completion],
    }


def audit_k9(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text())
    assert len(payload["results"]) == 1
    result = payload["results"][0]
    assert result["k"] == 9 and result["n"] == 27
    rows = result["rows"]
    assert len(rows) == result["cell_y_count"] == 24
    assert [row["y"] for row in rows] == list(range(1, 25))
    assert all(row["lag"] == row["y"] + 1 for row in rows)
    scores = [Fraction(row["score_exact"]) for row in rows]
    for row, score in zip(rows, scores):
        assert sum((Fraction(part["exact"]) for part in row["parts"].values()), Fraction(0)) == score
    assert all(score > 0 for score in scores)
    assert scores == list(reversed(scores))
    assert scores[0] == scores[-1]
    minimum = min(scores)
    minimum_y = [row["y"] for row, score in zip(rows, scores) if score == minimum]
    assert minimum_y == [7, 18]
    signed_average = Fraction(9 * 9, len(rows)) * sum(scores, Fraction(0))
    assert signed_average == Fraction(result["k_squared_signed_cell_average_exact"])
    exemplar = rows[minimum_y[0] - 1]
    triangle = sum(
        (Fraction(part["exact"]) for name, part in exemplar["parts"].items() if name.startswith("T_")),
        Fraction(0),
    )
    double = sum(
        (Fraction(part["exact"]) for name, part in exemplar["parts"].items() if name.startswith("D_")),
        Fraction(0),
    )
    assert triangle + double == minimum
    return {
        "rows": len(rows),
        "all_scores_strictly_positive": True,
        "reflection_exact": True,
        "endpoint_equality_exact": True,
        "minimum_y": minimum_y,
        "minimum_score_exact": qstr(minimum),
        "minimum_score_float": float(minimum),
        "triangle_at_minimum_exact": qstr(triangle),
        "triangle_at_minimum_float": float(triangle),
        "double_at_minimum_exact": qstr(double),
        "double_at_minimum_float": float(double),
        "parts_reconstruct_each_score_exactly": True,
        "signed_average_normalization_exact": True,
    }


def compare_small_artifact(path: Path, computed: list[dict[str, object]]) -> dict[str, object]:
    frozen = json.loads(path.read_text())["results"]
    assert [row["k"] for row in frozen] == [row["k"] for row in computed]
    compared_rows = 0
    for expected, actual in zip(frozen, computed):
        assert expected["mon_violations"] == actual["mon_violations"]
        assert expected["violations_by_type"] == actual["violations_by_type"]
        assert expected["fosd_violations"] == actual["fosd_violations"]
        assert expected["block_sign_counts"] == actual["block_sign_counts"]
        assert expected["all_complete_scores_nonnegative"] == actual["all_complete_scores_nonnegative"]
        assert len(expected["rows"]) == len(actual["rows"])
        for old_row, new_row in zip(expected["rows"], actual["rows"]):
            assert old_row["y"] == new_row["y"]
            assert old_row["direct_score_exact"] == new_row["score"]
            assert old_row["blocks_exact"] == new_row["blocks"]
            compared_rows += 1
    return {
        "ranks": [row["k"] for row in computed],
        "exact_rows_compared": compared_rows,
        "counts_blocks_and_scores_match": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k9", type=Path, required=True)
    parser.add_argument("--m274-small", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    small_rank = [audit_rank(3), audit_rank(5)]
    payload = {
        "status": "exact finite audit only; no asymptotic inference",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "project_code_imported": False,
        "nonstandard_dependencies": None,
        "small_rank": small_rank,
        "frozen_small_artifact_comparison": compare_small_artifact(args.m274_small, small_rank),
        "raw_atom_witnesses": [raw_atom_witness(k) for k in range(3, 22, 2)],
        "k9_frozen_artifact_audit": audit_k9(args.k9),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "small_rank": [
            {
                "k": row["k"],
                "mon_violations": row["mon_violations"],
                "fosd_violations": row["fosd_violations"],
                "all_channel_scores_nonnegative": row["all_channel_scores_nonnegative"],
                "all_complete_scores_nonnegative": row["all_complete_scores_nonnegative"],
            }
            for row in payload["small_rank"]
        ],
        "raw_atom_odd_k_checked": [row["k"] for row in payload["raw_atom_witnesses"]],
        "k9": payload["k9_frozen_artifact_audit"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
