#!/usr/bin/env python3
"""Clean-room M283 audit of the M280 CP/OCI reduction.

The only newly enumerated rank is k=3.  No M280 code is imported.  After the
clean-room calculation is complete, the frozen M280 k=11 JSON is read only
to check its hash and internal exact-rational identities; it is not evidence
for an all-rank sign claim.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import subprocess
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path


Perm = tuple[int, ...]
KINDS = ("T", "D")
TOPOLOGIES = ("IS", "IN", "X")


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def cycle(n: int, vertices: tuple[int, ...]) -> Perm:
    out = list(range(n))
    for x, y in zip(vertices, vertices[1:] + vertices[:1]):
        out[x] = y
    return tuple(out)


def transposition(n: int, x: int, y: int) -> Perm:
    return cycle(n, (x, y))


def cycle_decomposition(p: Perm) -> tuple[tuple[int, ...], ...]:
    seen: set[int] = set()
    answer: list[tuple[int, ...]] = []
    for root in range(len(p)):
        if root in seen:
            continue
        current: list[int] = []
        x = root
        while x not in seen:
            seen.add(x)
            current.append(x)
            x = p[x]
        answer.append(tuple(current))
    return tuple(answer)


@lru_cache(maxsize=None)
def tau(d: int) -> Fraction:
    if d < 1:
        return Fraction(0)
    if d == 1:
        return Fraction(1)
    return Fraction(d ** (d - 2), math.factorial(d - 1))


def completion(p: Perm, length: int) -> Fraction:
    cs = cycle_decomposition(p)
    if len(p) - len(cs) != length:
        return Fraction(0)
    out = Fraction(math.factorial(length))
    for component in cs:
        out *= tau(len(component))
    assert out.denominator == 1
    return out


def edges_in_component(n: int, component: tuple[int, ...]):
    for x, y in combinations(sorted(component), 2):
        yield transposition(n, x, y), (x, y)


def chord_split(component: tuple[int, ...], endpoints: tuple[int, int]) -> int:
    position = {vertex: index for index, vertex in enumerate(component)}
    x, y = endpoints
    forward = (position[y] - position[x]) % len(component)
    assert 0 < forward < len(component)
    return min(forward, len(component) - forward)


def qtext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def parse_fraction(value: str) -> Fraction:
    return Fraction(value)


def owner_coefficients(sizes: tuple[int, ...]) -> tuple[tuple[Fraction, ...], ...]:
    rows: list[tuple[Fraction, ...]] = []
    for i, d_i in enumerate(sizes):
        row: list[Fraction] = []
        for j, d_j in enumerate(sizes):
            if i == j:
                row.append(tau(d_i - 2) / tau(d_i) if d_i >= 3 else Fraction(0))
            else:
                left = tau(d_i - 1) / tau(d_i) if d_i >= 2 else Fraction(0)
                right = tau(d_j - 1) / tau(d_j) if d_j >= 2 else Fraction(0)
                row.append(left * right)
        rows.append(tuple(row))
    return tuple(rows)


def topology(
    first: tuple[int, int],
    second: tuple[int, int],
    positions: dict[int, int],
) -> str:
    ordered = sorted(set(first + second), key=positions.__getitem__)
    assert len(ordered) == 4
    index = {vertex: i for i, vertex in enumerate(ordered)}
    matching = {
        tuple(sorted((index[first[0]], index[first[1]]))),
        tuple(sorted((index[second[0]], index[second[1]]))),
    }
    if matching == {(0, 1), (2, 3)}:
        return "IS"
    if matching == {(0, 3), (1, 2)}:
        return "IN"
    if matching == {(0, 2), (1, 3)}:
        raise AssertionError("crossing generic edges")
    raise AssertionError(matching)


def response_profile(n: int, h: Perm, s: Perm) -> dict[str, object]:
    q = compose(inverse(s), h)
    cs = cycle_decomposition(q)
    assert len(cs) == 3
    owner = {vertex: i for i, component in enumerate(cs) for vertex in component}
    positions = {vertex: i for component in cs for i, vertex in enumerate(component)}
    kappa = owner_coefficients(tuple(map(len, cs)))
    generic_owner: list[int | None] = []
    for r in range(n):
        head = (r + 1) % n
        generic_owner.append(owner[r] if s[head] == head else None)
    support_size = sum(s[x] != x for x in range(n))
    kind = "T" if support_size == 3 else "D"
    assert support_size in (3, 4)

    values: list[Fraction] = []
    owner_free: list[int] = []
    collisions: list[int] = []
    pieces = {
        (candidate_kind, candidate_topology): []
        for candidate_kind in KINDS
        for candidate_topology in TOPOLOGIES
    }
    for ell in range(2, n - 1):
        value = Fraction(0)
        count = 0
        collision = 0
        local = {(candidate_kind, candidate_topology): Fraction(0)
                 for candidate_kind in KINDS for candidate_topology in TOPOLOGIES}
        for r in range(n):
            i = generic_owner[r]
            j = generic_owner[(r + ell) % n]
            if s[(r + 1) % n] != (r + 1) % n and s[(r + ell + 1) % n] != (r + ell + 1) % n:
                collision += 1
            if i is None or j is None:
                continue
            count += 1
            value += kappa[i][j]
            if i != j:
                label = "X"
            else:
                label = topology(
                    (r, (r + 1) % n),
                    ((r + ell) % n, (r + ell + 1) % n),
                    positions,
                )
            local[(kind, label)] += kappa[i][j]
        assert value == sum(local.values(), Fraction(0))
        assert count == n - 2 * support_size + collision
        assert count == n - 8 + 2 * int(kind == "T") + collision
        values.append(value)
        owner_free.append(count)
        collisions.append(collision)
        for key in pieces:
            pieces[key].append(local[key])

    assert values == list(reversed(values))
    assert owner_free == list(reversed(owner_free))
    assert collisions == list(reversed(collisions))
    return {
        "kind": kind,
        "F": tuple(values),
        "C": tuple(owner_free),
        "I": tuple(collisions),
        "pieces": {key: tuple(row) for key, row in pieces.items()},
    }


def source_records(k: int, label: str) -> tuple[list[dict[str, object]], Fraction]:
    n = 3 * k
    h = cycle(n, tuple(range(n)))
    if label == "A":
        source = cycle(n, (0, k, 2 * k))
    elif label == "B":
        source = compose(transposition(n, 0, 1), transposition(n, k, 2 * k))
    else:
        raise ValueError(label)
    residual = compose(inverse(source), h)
    initial = cycle_decomposition(residual)
    owner = {vertex: i for i, component in enumerate(initial) for vertex in component}
    middle = owner[k]
    rank = n - len(initial)
    denominator = completion(residual, rank)
    records: list[dict[str, object]] = []

    for first_component, component in enumerate(initial):
        if len(component) < 2:
            continue
        for first, first_pair in edges_in_component(n, component):
            after_first = compose(first, residual)
            for split_component in cycle_decomposition(after_first):
                if len(split_component) < 2:
                    continue
                original_component = owner[split_component[0]]
                assert all(owner[x] == original_component for x in split_component)
                for second, second_pair in edges_in_component(n, split_component):
                    numerator = completion(compose(second, after_first), rank - 2)
                    if not numerator:
                        continue
                    first_exterior = first_component != middle
                    second_exterior = original_component != middle
                    channel = int(first_exterior) + int(second_exterior)
                    product = compose(first, second)
                    exterior_pair = first_pair if first_exterior else second_pair
                    exterior_component = initial[first_component if first_exterior else original_component]
                    records.append({
                        "probability": numerator / denominator,
                        "channel": channel,
                        "product": product,
                        "kind": "T" if sum(product[x] != x for x in range(n)) == 3 else "D",
                        "exterior_split": (
                            chord_split(exterior_component, exterior_pair) if channel else None
                        ),
                    })
    assert sum((record["probability"] for record in records), Fraction(0)) == 1
    return records, denominator


def split_law(d: int) -> dict[int, Fraction]:
    answer: dict[int, Fraction] = {}
    for s in range(1, (d - 1) // 2 + 1):
        specified = tau(s) * tau(d - s) / ((d - 1) * tau(d))
        answer[s] = d * specified
    assert sum(answer.values(), Fraction(0)) == 1
    return answer


def cleanroom_rank_three() -> dict[str, object]:
    k = 3
    n = 3 * k
    h = cycle(n, tuple(range(n)))
    records = {}
    denominators = {}
    for label in ("A", "B"):
        records[label], denominators[label] = source_records(k, label)

    m = k - 1
    color_total = 3 * m * (3 * m - 1)
    alpha = {
        0: Fraction(m * (m - 1), color_total),
        1: Fraction(4 * m * m, color_total),
        2: Fraction(2 * m * (2 * m - 1), color_total),
    }
    assert sum(alpha.values(), Fraction(0)) == 1

    profiles: dict[Perm, dict[str, object]] = {}
    channel_mass: dict[str, dict[int, Fraction]] = {label: defaultdict(Fraction) for label in ("A", "B")}
    kind_mass: dict[str, dict[tuple[int, str], Fraction]] = {label: defaultdict(Fraction) for label in ("A", "B")}
    split_mass: dict[str, dict[tuple[int, int], Fraction]] = {label: defaultdict(Fraction) for label in ("A", "B")}
    expectations: dict[str, dict[tuple[int, str], list[Fraction]]] = {
        label: defaultdict(lambda: [Fraction(0) for _ in range(n - 3)])
        for label in ("A", "B")
    }
    split_expectations: dict[str, dict[tuple[int, int], list[Fraction]]] = {
        label: defaultdict(lambda: [Fraction(0) for _ in range(n - 3)])
        for label in ("A", "B")
    }
    piece_expectations: dict[str, dict[tuple[int, str, str], list[Fraction]]] = {
        label: defaultdict(lambda: [Fraction(0) for _ in range(n - 3)])
        for label in ("A", "B")
    }

    for label in ("A", "B"):
        for record in records[label]:
            probability = record["probability"]
            channel = record["channel"]
            product = record["product"]
            kind = record["kind"]
            if product not in profiles:
                profiles[product] = response_profile(n, h, product)
            profile = profiles[product]
            assert profile["kind"] == kind
            channel_mass[label][channel] += probability
            kind_mass[label][(channel, kind)] += probability
            if channel:
                split = record["exterior_split"]
                split_mass[label][(channel, split)] += probability
                for i, value in enumerate(profile["F"]):
                    split_expectations[label][(channel, split)][i] += probability * value
            for statistic in ("F", "C", "I"):
                for i, value in enumerate(profile[statistic]):
                    expectations[label][(channel, statistic)][i] += probability * value
            for (_, topo), row in profile["pieces"].items():
                for i, value in enumerate(row):
                    piece_expectations[label][(channel, kind, topo)][i] += probability * value

    for label in ("A", "B"):
        assert all(channel_mass[label][j] == alpha[j] for j in range(3))
    for statistic in ("F", "C", "I"):
        assert expectations["A"][(0, statistic)] == expectations["B"][(0, statistic)]

    p = split_law(2 * k - 1)
    q = split_law(k)
    for channel in (1, 2):
        for s, mass in p.items():
            assert split_mass["B"][(channel, s)] / alpha[channel] == mass
        for s, mass in q.items():
            assert split_mass["A"][(channel, s)] / alpha[channel] == mass

    target = compose(transposition(n, 0, 1), transposition(n, 2, 3))
    f_target = completion(compose(inverse(target), h), n - 3)
    lambda_n = Fraction(n ** (n - 2), n * f_target)
    expected_lambda = Fraction(n - 2) * Fraction(n, n - 2) ** (n - 3)
    assert lambda_n == expected_lambda
    response_denominator = (n - 3) * (n - 4)

    eta: dict[tuple[int, str], list[Fraction]] = {}
    cp: dict[int, list[Fraction]] = {}
    cp_pieces: dict[int, dict[str, list[Fraction]]] = {}
    for channel in (1, 2):
        for statistic in ("F", "C", "I"):
            eta[(channel, statistic)] = [
                (expectations["B"][(channel, statistic)][i]
                 - expectations["A"][(channel, statistic)][i]) / alpha[channel]
                for i in range(n - 3)
            ]
        cp[channel] = [lambda_n * value / response_denominator for value in eta[(channel, "F")]]
        cp_pieces[channel] = {}
        for kind in KINDS:
            for topo in TOPOLOGIES:
                key = f"{kind}_{topo}"
                cp_pieces[channel][key] = [
                    lambda_n
                    * (piece_expectations["B"][(channel, kind, topo)][i]
                       - piece_expectations["A"][(channel, kind, topo)][i])
                    / (alpha[channel] * response_denominator)
                    for i in range(n - 3)
                ]
        for i in range(n - 3):
            assert cp[channel][i] == sum(
                (cp_pieces[channel][key][i] for key in cp_pieces[channel]),
                Fraction(0),
            )
        assert cp[channel] == list(reversed(cp[channel]))

    eta_triangle = {
        channel: (
            kind_mass["B"][(channel, "T")] - kind_mass["A"][(channel, "T")]
        ) / alpha[channel]
        for channel in (1, 2)
    }
    theta = Fraction(6 * (k - 1), k * (2 * k - 3) * (2 * k - 1))
    assert eta_triangle[1] == 0
    assert eta_triangle[2] == theta
    for channel in (1, 2):
        for i in range(n - 3):
            assert eta[(channel, "C")][i] == (
                2 * eta_triangle[channel] + eta[(channel, "I")][i]
            )

    # Independently evaluate the exact M91 Abel identity at F_ell.
    D: dict[int, Fraction] = {}
    for u in range(1, k):
        D[u] = sum((p.get(v, Fraction(0)) - q.get(v, Fraction(0))
                    for v in range(1, u + 1)), Fraction(0))
    assert D[k - 1] == 0
    abel_checks = 0
    for channel in (1, 2):
        phi = {
            s: [split_expectations["B"][(channel, s)][i] / (alpha[channel] * p[s])
                for i in range(n - 3)]
            for s in p
        }
        psi = {
            s: [split_expectations["A"][(channel, s)][i] / (alpha[channel] * q[s])
                for i in range(n - 3)]
            for s in q
        }
        for i in range(n - 3):
            abel = sum(
                (D[u] * (phi[u][i] - phi[u + 1][i]) for u in range(1, k - 1)),
                Fraction(0),
            )
            abel += sum(
                (q[s] * (phi[s][i] - psi[s][i]) for s in q),
                Fraction(0),
            )
            assert abel == eta[(channel, "F")][i]
            abel_checks += 1

    weighted = [
        alpha[1] * cp[1][i] + alpha[2] * cp[2][i]
        for i in range(n - 3)
    ]
    direct = [
        lambda_n / response_denominator
        * sum(
            expectations["B"][(channel, "F")][i]
            - expectations["A"][(channel, "F")][i]
            for channel in (0, 1, 2)
        )
        for i in range(n - 3)
    ]
    assert weighted == direct
    assert weighted == list(reversed(weighted))

    return {
        "k": k,
        "n": n,
        "newly_enumerated_ranks": [k],
        "source_record_counts": {label: len(records[label]) for label in ("A", "B")},
        "source_completion_denominators": {
            label: qtext(denominators[label]) for label in ("A", "B")
        },
        "distinct_accessible_products": len(profiles),
        "alpha": {str(j): qtext(alpha[j]) for j in range(3)},
        "p": {str(s): qtext(value) for s, value in p.items()},
        "q": {str(s): qtext(value) for s, value in q.items()},
        "D": {str(s): qtext(value) for s, value in D.items()},
        "lambda_n": qtext(lambda_n),
        "response_denominator": response_denominator,
        "direct_raw_equals_owner_correlation": True,
        "abel_equals_direct": True,
        "abel_channel_lag_checks": abel_checks,
        "channel_two_fair_component_choice_in_raw_law": True,
        "all_T_D_IS_IN_X_pieces_reconstruct": True,
        "reflection_and_endpoints_exact": True,
        "eta_triangle": {str(j): qtext(eta_triangle[j]) for j in (1, 2)},
        "theta_k": qtext(theta),
        "collision_affine_identity_exact": True,
        "all_channel_entries_strictly_positive": all(
            value > 0 for row in cp.values() for value in row
        ),
        "channel_scores": {
            str(channel): [qtext(value) for value in cp[channel]]
            for channel in (1, 2)
        },
        "weighted_scores": [qtext(value) for value in weighted],
    }


def verify_frozen_k11(path: Path, expected_digest: str) -> dict[str, object]:
    observed = hashlib.sha256(path.read_bytes()).hexdigest()
    assert observed == expected_digest
    payload = json.loads(path.read_text())
    assert payload["k"] == 11 and payload["n"] == 33
    assert payload["lags"] == {"minimum": 2, "maximum": 31, "count": 30}
    assert payload["negative_channel_entries"] == []
    assert payload["all_channel_entries_strictly_positive"] is True
    assert payload["source_accessible_products"] == {"A": 11550, "B": 25675}
    rows = payload["rows"]
    assert [row["ell"] for row in rows] == list(range(2, 32))
    k = 11
    m = k - 1
    denominator = 3 * m * (3 * m - 1)
    alpha = {
        1: Fraction(4 * m * m, denominator),
        2: Fraction(2 * m * (2 * m - 1), denominator),
    }
    scores = {1: [], 2: []}
    weighted: list[Fraction] = []
    decomposition_checks = 0
    for row in rows:
        for channel in (1, 2):
            entry = row["channel_scores"][str(channel)]
            score = parse_fraction(entry["exact"])
            pieces = [parse_fraction(value) for value in entry["pieces"].values()]
            assert len(pieces) == 6 and score == sum(pieces, Fraction(0))
            scores[channel].append(score)
            decomposition_checks += 1
        w = parse_fraction(row["weighted_full_score_exact"])
        assert w == alpha[1] * scores[1][-1] + alpha[2] * scores[2][-1]
        weighted.append(w)
    for channel in (1, 2):
        assert scores[channel] == list(reversed(scores[channel]))
    assert weighted == list(reversed(weighted))
    assert rows[0]["ell"] == 2 and rows[-1]["ell"] == 31
    minima = {
        str(channel): {
            "exact": qtext(min(scores[channel])),
            "ys": [i + 1 for i, value in enumerate(scores[channel]) if value == min(scores[channel])],
        }
        for channel in (1, 2)
    }
    assert minima["1"]["ys"] == [9, 22]
    assert minima["2"]["ys"] == [9, 22]
    assert payload["channel_minima"]["1"]["y"] == 9
    assert payload["channel_minima"]["2"]["y"] == 9

    kind = payload["kind_masses"]
    eta_1_triangle = (
        parse_fraction(kind["B"]["J1_T"]) - parse_fraction(kind["A"]["J1_T"])
    ) / alpha[1]
    eta_2_triangle = (
        parse_fraction(kind["B"]["J2_T"]) - parse_fraction(kind["A"]["J2_T"])
    ) / alpha[2]
    theta = Fraction(6 * (k - 1), k * (2 * k - 3) * (2 * k - 1))
    assert eta_1_triangle == 0 and eta_2_triangle == theta
    phase_total = k * sum(weighted, Fraction(0))
    return {
        "path": str(path),
        "sha256": observed,
        "new_rank_enumerated_by_m283": False,
        "finite_only": True,
        "rows": len(rows),
        "exact_decomposition_checks": decomposition_checks,
        "reflection_and_endpoints_exact": True,
        "strictly_positive_frozen_entries": True,
        "channel_minima": minima,
        "eta_triangle": {"1": qtext(eta_1_triangle), "2": qtext(eta_2_triangle)},
        "theta_k": qtext(theta),
        "k_times_weighted_phase_sum_exact": qtext(phase_total),
        "k_times_weighted_phase_sum_float": float(phase_total),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--frozen-k11", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    clean = cleanroom_rank_three()
    frozen = verify_frozen_k11(
        args.frozen_k11,
        "d08c8b0d9b2abe61e26752033d91438e0e9c912397c087734cc9b4fe10a10f93",
    )
    result = {
        "status": "fresh exact reduction audit; CP/OCI unresolved",
        "target": "first auxiliary minimal-long-cycle fixed cell under the M73 nonlazy cyclic rank-two quotient",
        "convention": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "imports_m280_code": False,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "cleanroom": clean,
        "frozen_k11_verification": frozen,
        "all_rank_CP_or_OCI_inference": False,
        "gap_mixing_or_terminal_inference": False,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "cleanroom_k": clean["k"],
        "cleanroom_all_channel_entries_strictly_positive": clean[
            "all_channel_entries_strictly_positive"
        ],
        "frozen_k11_sha256": frozen["sha256"],
        "frozen_k11_phase_total_float": frozen["k_times_weighted_phase_sum_float"],
        "CP_OCI": "unresolved",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
