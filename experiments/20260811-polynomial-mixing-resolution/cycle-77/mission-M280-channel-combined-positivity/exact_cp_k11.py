#!/usr/bin/env python3
"""One predeclared exact falsifier for M280's per-channel CP lemma.

The sole tested rank is k=11.  The program enumerates only the first two
ordered factors of the two source residuals.  It evaluates the accepted
owner-correlation response over every target lag, retaining T/D and
IS/IN/X before channel recombination.  Finite survival is not a theorem.
"""

from __future__ import annotations

import json
import math
import platform
import subprocess
import sys
import time
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path


Perm = tuple[int, ...]
KINDS = ("T", "D")
TOPOLOGIES = ("IS", "IN", "X")


def mul(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inv(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def cyc(n: int, entries: tuple[int, ...]) -> Perm:
    out = list(range(n))
    if len(entries) > 1:
        for x, y in zip(entries, entries[1:] + entries[:1]):
            out[x] = y
    return tuple(out)


def tr(n: int, x: int, y: int) -> Perm:
    return cyc(n, (x, y))


def cycles(p: Perm) -> list[tuple[int, ...]]:
    seen: set[int] = set()
    out: list[tuple[int, ...]] = []
    for start in range(len(p)):
        if start in seen:
            continue
        c: list[int] = []
        x = start
        while x not in seen:
            seen.add(x)
            c.append(x)
            x = p[x]
        out.append(tuple(c))
    return out


@lru_cache(maxsize=None)
def completion_sizes(sizes: tuple[int, ...], length: int) -> int:
    if sum(sizes) - len(sizes) != length:
        return 0
    ans = math.factorial(length)
    for d in sizes:
        if d > 1:
            ans = ans * d ** (d - 2) // math.factorial(d - 1)
    return ans


def completion(p: Perm, length: int) -> int:
    return completion_sizes(tuple(sorted(map(len, cycles(p)))), length)


def internal_edges(n: int, component: tuple[int, ...]):
    for x, y in combinations(sorted(component), 2):
        yield tr(n, x, y)


def ratio_one(d: int) -> Fraction:
    """tau(d-1)/tau(d), with invalid shifts set to zero."""
    if d < 2:
        return Fraction(0)
    return Fraction(d - 1, d) ** (d - 2)


def ratio_two(d: int) -> Fraction:
    """tau(d-2)/tau(d), with invalid shifts set to zero."""
    if d < 3:
        return Fraction(0)
    return Fraction(d - 1, d) * Fraction(d - 2, d) ** (d - 3)


def same_owner_topology(
    first: tuple[int, int],
    second: tuple[int, int],
    position: dict[int, int],
) -> str:
    ordered = sorted(set(first + second), key=lambda vertex: position[vertex])
    assert len(ordered) == 4
    index = {vertex: offset for offset, vertex in enumerate(ordered)}
    matching = {
        tuple(sorted((index[first[0]], index[first[1]]))),
        tuple(sorted((index[second[0]], index[second[1]]))),
    }
    if matching == {(0, 1), (2, 3)}:
        return "IS"
    if matching == {(0, 3), (1, 2)}:
        return "IN"
    if matching == {(0, 2), (1, 3)}:
        raise AssertionError("generic boundary edges cannot cross")
    raise AssertionError(matching)


def response_parts(
    n: int, h: Perm, s: Perm, kind: str
) -> dict[tuple[str, str], tuple[Fraction, ...]]:
    """Return F_ell(s)/R_n, ell=2,...,n-2, by kind/topology."""
    residual = mul(inv(s), h)
    cs = cycles(residual)
    assert len(cs) == 3
    owner = {vertex: i for i, c in enumerate(cs) for vertex in c}
    position = {vertex: p for c in cs for p, vertex in enumerate(c)}
    sizes = [len(c) for c in cs]
    generic_owner = [-1] * n
    for r in range(n):
        if s[(r + 1) % n] == (r + 1) % n:
            generic_owner[r] = owner[r]

    kappa = [[Fraction(0) for _ in cs] for _ in cs]
    for i in range(3):
        kappa[i][i] = ratio_two(sizes[i])
        for j in range(3):
            if i != j:
                kappa[i][j] = ratio_one(sizes[i]) * ratio_one(sizes[j])

    length = n - 3
    raw = {
        (candidate_kind, topology): [Fraction(0) for _ in range(length)]
        for candidate_kind in KINDS
        for topology in TOPOLOGIES
    }
    for index, ell in enumerate(range(2, n - 1)):
        for r in range(n):
            i = generic_owner[r]
            j = generic_owner[(r + ell) % n]
            if i < 0 or j < 0:
                continue
            if i != j:
                topology = "X"
            else:
                topology = same_owner_topology(
                    (r, (r + 1) % n),
                    ((r + ell) % n, (r + ell + 1) % n),
                    position,
                )
            raw[(kind, topology)][index] += kappa[i][j]

    denominator = (n - 3) * (n - 4)
    out = {
        key: tuple(value / denominator for value in values)
        for key, values in raw.items()
    }
    total = tuple(
        sum((out[key][i] for key in out), Fraction(0)) for i in range(length)
    )
    assert all(total[i] == total[length - 1 - i] for i in range(length))
    return out


def source_expectation(k: int, label: str):
    n = 3 * k
    h = cyc(n, tuple(range(n)))
    if label == "A":
        source = cyc(n, (0, k, 2 * k))
    elif label == "B":
        source = mul(tr(n, 0, 1), tr(n, k, 2 * k))
    else:
        raise ValueError(label)

    residual = mul(inv(source), h)
    initial = cycles(residual)
    middle_index = next(i for i, c in enumerate(initial) if k in c)
    component_of = {vertex: i for i, c in enumerate(initial) for vertex in c}
    rank = n - len(initial)
    denominator = completion(residual, rank)
    length = n - 3
    values: dict[tuple[int, str, str], list[Fraction]] = defaultdict(
        lambda: [Fraction(0) for _ in range(length)]
    )
    masses: dict[tuple[int, str], Fraction] = defaultdict(Fraction)
    channel_masses: dict[int, Fraction] = defaultdict(Fraction)
    cache: dict[Perm, dict[tuple[str, str], tuple[Fraction, ...]]] = {}
    kind_cache: dict[Perm, str] = {}
    total_mass = Fraction(0)

    for first_component, component in enumerate(initial):
        if len(component) == 1:
            continue
        first_exterior = first_component != middle_index
        for first in internal_edges(n, component):
            after_first = mul(first, residual)
            for next_component in cycles(after_first):
                if len(next_component) == 1:
                    continue
                original = component_of[next_component[0]]
                assert all(component_of[x] == original for x in next_component)
                second_exterior = original != middle_index
                for second in internal_edges(n, next_component):
                    s = mul(first, second)
                    numerator = completion(mul(inv(s), residual), rank - 2)
                    if not numerator:
                        continue
                    probability = Fraction(numerator, denominator)
                    support = sum(x != s[x] for x in range(n))
                    kind = "T" if support == 3 else "D"
                    assert support in (3, 4)
                    channel = int(first_exterior) + int(second_exterior)
                    if s not in cache:
                        cache[s] = response_parts(n, h, s, kind)
                        kind_cache[s] = kind
                    assert kind_cache[s] == kind
                    for topology in TOPOLOGIES:
                        row = values[(channel, kind, topology)]
                        part = cache[s][(kind, topology)]
                        for index, value in enumerate(part):
                            row[index] += probability * value
                    masses[(channel, kind)] += probability
                    channel_masses[channel] += probability
                    total_mass += probability

    assert total_mass == 1
    return (
        {key: tuple(row) for key, row in values.items()},
        dict(masses),
        dict(channel_masses),
        len(cache),
    )


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def main() -> None:
    if len(sys.argv) != 3 or sys.argv[1] != "--output":
        raise SystemExit("usage: exact_cp_k11.py --output PATH")
    output = Path(sys.argv[2])
    started = time.monotonic()
    k = 11
    n = 3 * k
    length = n - 3
    a, a_kind_mass, a_channel_mass, a_count = source_expectation(k, "A")
    b, b_kind_mass, b_channel_mass, b_count = source_expectation(k, "B")

    m = k - 1
    color_denominator = (3 * m) * (3 * m - 1)
    alpha = {
        0: Fraction(m * (m - 1), color_denominator),
        1: Fraction(4 * m * m, color_denominator),
        2: Fraction(2 * m * (2 * m - 1), color_denominator),
    }
    assert sum(alpha.values(), Fraction(0)) == 1
    assert all(a_channel_mass[j] == alpha[j] for j in range(3))
    assert all(b_channel_mass[j] == alpha[j] for j in range(3))

    h = cyc(n, tuple(range(n)))
    target = mul(tr(n, 0, 1), tr(n, 2, 3))
    f_target = completion(mul(inv(target), h), n - 3)
    lambda_n = Fraction(n ** (n - 2), n * f_target)

    zeros = tuple(Fraction(0) for _ in range(length))
    conditional_parts: dict[tuple[int, str, str], tuple[Fraction, ...]] = {}
    for channel in (1, 2):
        for kind in KINDS:
            for topology in TOPOLOGIES:
                key = (channel, kind, topology)
                left = b.get(key, zeros)
                right = a.get(key, zeros)
                conditional_parts[key] = tuple(
                    lambda_n * (left[i] - right[i]) / alpha[channel]
                    for i in range(length)
                )

    # The common middle-middle channel cancels as a measure, including every
    # response part, not merely after summing kinds.
    assert all(
        b.get((0, kind, topology), zeros) == a.get((0, kind, topology), zeros)
        for kind in KINDS
        for topology in TOPOLOGIES
    )

    rows = []
    channel_scores: dict[int, list[Fraction]] = {1: [], 2: []}
    for index, ell in enumerate(range(2, n - 1)):
        pieces_by_channel: dict[int, dict[str, Fraction]] = {}
        for channel in (1, 2):
            pieces = {
                f"{kind}_{topology}": conditional_parts[(channel, kind, topology)][index]
                for kind in KINDS
                for topology in TOPOLOGIES
            }
            pieces_by_channel[channel] = pieces
            channel_scores[channel].append(sum(pieces.values(), Fraction(0)))
        weighted = sum(
            (alpha[channel] * channel_scores[channel][-1] for channel in (1, 2)),
            Fraction(0),
        )
        direct = Fraction(0)
        for channel in (1, 2):
            for kind in KINDS:
                for topology in TOPOLOGIES:
                    key = (channel, kind, topology)
                    direct += lambda_n * (
                        b.get(key, zeros)[index] - a.get(key, zeros)[index]
                    )
        assert weighted == direct
        rows.append({
            "y": ell - 1,
            "ell": ell,
            "weighted_full_score_exact": qstr(weighted),
            "weighted_full_score_float": float(weighted),
            "channel_scores": {
                str(channel): {
                    "exact": qstr(channel_scores[channel][-1]),
                    "float": float(channel_scores[channel][-1]),
                    "pieces": {
                        name: qstr(value)
                        for name, value in pieces_by_channel[channel].items()
                    },
                }
                for channel in (1, 2)
            },
        })

    for channel in (1, 2):
        assert all(
            channel_scores[channel][i] == channel_scores[channel][length - 1 - i]
            for i in range(length)
        )
    assert rows[0]["ell"] == 2 and rows[-1]["ell"] == n - 2
    assert all(rows[0]["channel_scores"][str(j)]["exact"] == rows[-1]["channel_scores"][str(j)]["exact"] for j in (1, 2))

    negative = [
        {"channel": channel, "y": i + 1, "ell": i + 2, "exact": qstr(value)}
        for channel in (1, 2)
        for i, value in enumerate(channel_scores[channel])
        if value < 0
    ]
    minima = {
        str(channel): {
            "y": min(range(length), key=lambda i: channel_scores[channel][i]) + 1,
            "exact": qstr(min(channel_scores[channel])),
            "float": float(min(channel_scores[channel])),
        }
        for channel in (1, 2)
    }

    payload = {
        "status": "single exact finite CP falsifier; finite survival is not proof",
        "claim_tested": "CP_j(k,y)>=0 for both literal M91 channels",
        "scope": "exactly k=11, n=33, every first fixed-cell lag",
        "target": "auxiliary minimal-long-cycle first fixed cell under M73 nonlazy rank-two quotient",
        "convention": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
        "k": k,
        "n": n,
        "lags": {"minimum": 2, "maximum": n - 2, "count": length},
        "source_accessible_products": {"A": a_count, "B": b_count},
        "channel_masses": {
            str(j): {
                "alpha_exact": qstr(alpha[j]),
                "A_exact": qstr(a_channel_mass[j]),
                "B_exact": qstr(b_channel_mass[j]),
            }
            for j in range(3)
        },
        "kind_masses": {
            label: {
                f"J{j}_{kind}": qstr(table.get((j, kind), Fraction(0)))
                for j in range(3)
                for kind in KINDS
            }
            for label, table in (("A", a_kind_mass), ("B", b_kind_mass))
        },
        "lambda_n_exact": qstr(lambda_n),
        "all_decompositions_exact": True,
        "channelwise_reflection_exact": True,
        "endpoint_equality_exact": True,
        "negative_channel_entries": negative,
        "all_channel_entries_strictly_positive": all(
            value > 0 for values in channel_scores.values() for value in values
        ),
        "channel_minima": minima,
        "rows": rows,
        "runtime_seconds": time.monotonic() - started,
    }
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "k": k,
        "negative_channel_entries": negative,
        "all_channel_entries_strictly_positive": payload[
            "all_channel_entries_strictly_positive"
        ],
        "channel_minima": minima,
        "runtime_seconds": payload["runtime_seconds"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
