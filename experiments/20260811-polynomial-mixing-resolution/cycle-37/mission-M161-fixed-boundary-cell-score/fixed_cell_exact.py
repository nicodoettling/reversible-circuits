#!/usr/bin/env python3
"""Exact finite fixed-cell score without constructing a quotient matrix.

For n=3k, the program evaluates M94's raw intermediate convolution only on
the separated targets (1,y,1,n-2-y).  It retains intermediate kind, second
row schema, and the exceptional phases where an h-boundary edge meets the
support of the intermediate product.  Fractions are introduced only after
the phase sum for one intermediate state, so k=3,5,7 remains compact.

Convention: (pq)(x)=p(q(x)); factors multiply left-to-right.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import math
import platform
import subprocess
import sys
import time
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path


Perm = tuple[int, ...]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def cycle_perm(n: int, entries: tuple[int, ...]) -> Perm:
    out = list(range(n))
    if len(entries) > 1:
        for x, y in zip(entries, entries[1:] + entries[:1]):
            out[x] = y
    return tuple(out)


def edge_perm(n: int, x: int, y: int) -> Perm:
    return cycle_perm(n, (x, y))


def cycles(p: Perm) -> list[tuple[int, ...]]:
    seen: set[int] = set()
    out = []
    for start in range(len(p)):
        if start in seen:
            continue
        cycle = []
        x = start
        while x not in seen:
            seen.add(x)
            cycle.append(x)
            x = p[x]
        out.append(tuple(cycle))
    return out


def cycle_sizes(p: Perm) -> tuple[int, ...]:
    return tuple(sorted((len(c) for c in cycles(p)), reverse=True))


@lru_cache(maxsize=None)
def completion_from_sizes(sizes: tuple[int, ...], length: int) -> int:
    n = sum(sizes)
    if n - len(sizes) != length:
        return 0
    out = math.factorial(length)
    for d in sizes:
        if d > 1:
            out = out * d ** (d - 2) // math.factorial(d - 1)
    return out


def completion(p: Perm, length: int) -> int:
    return completion_from_sizes(cycle_sizes(p), length)


def moved(p: Perm) -> frozenset[int]:
    return frozenset(x for x, y in enumerate(p) if x != y)


def supported_states(n: int):
    """Generate every raw admissible rank-two product exactly once."""
    for a, b, c in combinations(range(n), 3):
        yield cycle_perm(n, (a, b, c)), "T", 3
    for a, b, c, d in combinations(range(n), 4):
        yield compose(edge_perm(n, a, b), edge_perm(n, c, d)), "D", 2
        yield compose(edge_perm(n, a, d), edge_perm(n, b, c)), "D", 2


def boundary_target(n: int, phase: int, lag: int) -> Perm:
    return compose(
        edge_perm(n, phase, (phase + 1) % n),
        edge_perm(n, (phase + lag) % n, (phase + lag + 1) % n),
    )


def residual_metadata(q: Perm):
    cs = cycles(q)
    component: dict[int, int] = {}
    position: dict[int, int] = {}
    for i, cycle in enumerate(cs):
        for j, vertex in enumerate(cycle):
            component[vertex] = i
            position[vertex] = j
    return cs, component, position


def second_schema(
    endpoints: tuple[tuple[int, int], tuple[int, int]],
    cs: list[tuple[int, ...]],
    component: dict[int, int],
    position: dict[int, int],
) -> str:
    """Classify a nonzero double target as IS, IN, or X in q's cycles."""
    first, second = endpoints
    first_components = {component[x] for x in first}
    second_components = {component[x] for x in second}
    if len(first_components) != 1 or len(second_components) != 1:
        return "inadmissible"
    i = next(iter(first_components))
    j = next(iter(second_components))
    if i != j:
        return "X"

    ordered = sorted(
        set(first + second),
        key=lambda vertex: position[vertex],
    )
    if len(ordered) != 4:
        raise AssertionError("target edges were not disjoint")
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
        return "crossing"
    raise AssertionError((cs[i], endpoints, matching))


def frac(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def analyze(k: int) -> dict[str, object]:
    if k < 3 or k % 2 == 0:
        raise ValueError("k must be odd and at least three")
    started = time.monotonic()
    n = 3 * k
    h = cycle_perm(n, tuple(range(n)))
    source_a = cycle_perm(n, (0, k, 2 * k))
    source_b = compose(edge_perm(n, 0, 1), edge_perm(n, k, 2 * k))
    f3_a = completion(compose(inverse(source_a), h), n - 3)
    f3_b = completion(compose(inverse(source_b), h), n - 3)
    target0 = boundary_target(n, 0, 2)
    f3_target = completion(compose(inverse(target0), h), n - 3)
    if not f3_a or not f3_b or not f3_target:
        raise AssertionError("source or target marginal count vanished")

    ys = list(range(1, n - 2))
    lags = [y + 1 for y in ys]
    categories = [
        f"{kind}_{schema}_{phase_type}"
        for kind in ("T", "D")
        for schema in ("IS", "IN", "X")
        for phase_type in ("generic", "exceptional")
    ]
    source_b_sum = {category: [Fraction(0) for _ in ys] for category in categories}
    source_a_sum = {category: [Fraction(0) for _ in ys] for category in categories}
    raw_count = collections.Counter()
    nonzero_phase_count = 0
    exceptional_nonzero_phase_count = 0
    crossing_nonzero = 0
    inadmissible_nonzero = 0

    for state, kind, lift in supported_states(n):
        residual = compose(inverse(state), h)
        f3_state = completion(residual, n - 3)
        if not f3_state:
            raise AssertionError("generated rank-two state was inadmissible")
        raw_count[kind] += 1
        f5_b = completion(compose(inverse(compose(source_b, state)), h), n - 5)
        f5_a = completion(compose(inverse(compose(source_a, state)), h), n - 5)
        coefficient_b = Fraction(lift * f5_b, f3_b * f3_state)
        coefficient_a = Fraction(lift * f5_a, f3_a * f3_state)
        if not coefficient_b and not coefficient_a:
            continue

        cs, component, position = residual_metadata(residual)
        bad_tails = {(vertex - 1) % n for vertex in moved(state)}
        phase_sums = {
            category: [0 for _ in ys]
            for category in categories
        }
        for y_index, lag in enumerate(lags):
            for phase in range(n):
                first = (phase, (phase + 1) % n)
                second = ((phase + lag) % n, (phase + lag + 1) % n)
                target = compose(
                    edge_perm(n, *first),
                    edge_perm(n, *second),
                )
                f5 = completion(compose(target, residual), n - 5)
                if not f5:
                    continue
                nonzero_phase_count += 1
                schema = second_schema((first, second), cs, component, position)
                if schema == "crossing":
                    crossing_nonzero += 1
                    continue
                if schema == "inadmissible":
                    inadmissible_nonzero += 1
                    continue
                phase_type = (
                    "exceptional"
                    if phase in bad_tails or (phase + lag) % n in bad_tails
                    else "generic"
                )
                if phase_type == "exceptional":
                    exceptional_nonzero_phase_count += 1
                phase_sums[f"{kind}_{schema}_{phase_type}"][y_index] += f5

        for category in categories:
            for y_index, value in enumerate(phase_sums[category]):
                if value:
                    source_b_sum[category][y_index] += coefficient_b * value
                    source_a_sum[category][y_index] += coefficient_a * value

    if crossing_nonzero or inadmissible_nonzero:
        raise AssertionError((crossing_nonzero, inadmissible_nonzero))

    normalization = Fraction(n ** (n - 2), n * f3_target)
    rows = []
    scores: list[Fraction] = []
    for y_index, y in enumerate(ys):
        parts = {
            category: normalization * (
                source_b_sum[category][y_index] - source_a_sum[category][y_index]
            )
            for category in categories
        }
        score = sum(parts.values(), Fraction(0))
        scores.append(score)
        source_b_score = normalization * sum(
            (source_b_sum[category][y_index] for category in categories),
            Fraction(0),
        )
        source_a_score = normalization * sum(
            (source_a_sum[category][y_index] for category in categories),
            Fraction(0),
        )
        if score != source_b_score - source_a_score:
            raise AssertionError("source and category reconstructions disagree")
        rows.append({
            "y": y,
            "w": n - 2 - y,
            "lag": y + 1,
            "score_exact": frac(score),
            "score_float": float(score),
            "k_times_score": float(k * score),
            "k_squared_absolute_score": float(k * k * abs(score)),
            "source_B_score_float": float(source_b_score),
            "source_A_score_float": float(source_a_score),
            "parts": {
                category: {
                    "exact": frac(value),
                    "float": float(value),
                    "k_times": float(k * value),
                }
                for category, value in parts.items()
                if value
            },
        })

    for index, y in enumerate(ys):
        mirror = n - 2 - y
        mirror_index = ys.index(mirror)
        if scores[index] != scores[mirror_index]:
            raise AssertionError((y, mirror, scores[index], scores[mirror_index]))

    a_exact = Fraction(k * k, n - 3) * sum((abs(score) for score in scores), Fraction(0))
    signed_average = Fraction(k * k, n - 3) * sum(scores, Fraction(0))
    sequence_tv = sum(
        (abs(scores[i + 1] - scores[i]) for i in range(len(scores) - 1)),
        Fraction(0),
    )
    category_summary = {}
    for category in categories:
        values = [
            normalization * (source_b_sum[category][i] - source_a_sum[category][i])
            for i in range(len(ys))
        ]
        if any(values):
            category_summary[category] = {
                "signed_y_sum_exact": frac(sum(values, Fraction(0))),
                "signed_y_sum_float": float(sum(values, Fraction(0))),
                "absolute_y_sum_float": float(sum((abs(value) for value in values), Fraction(0))),
                "maximum_absolute_float": float(max(map(abs, values))),
            }

    return {
        "k": k,
        "n": n,
        "raw_intermediates": dict(sorted(raw_count.items())),
        "cell_y_count": n - 3,
        "target_marginal_count": f3_target,
        "source_marginal_counts": {"A": f3_a, "B": f3_b},
        "nonzero_intermediate_phase_terms": nonzero_phase_count,
        "exceptional_nonzero_phase_terms": exceptional_nonzero_phase_count,
        "crossing_nonzero_terms": crossing_nonzero,
        "inadmissible_nonzero_terms": inadmissible_nonzero,
        "mirror_symmetry_exact": True,
        "A_k_1_1_exact": frac(a_exact),
        "A_k_1_1_float": float(a_exact),
        "k_squared_signed_cell_average_exact": frac(signed_average),
        "k_squared_signed_cell_average_float": float(signed_average),
        "unscaled_score_sequence_TV_exact": frac(sequence_tv),
        "k_times_score_sequence_TV_float": float(k * sequence_tv),
        "category_summary": category_summary,
        "rows": rows,
        "runtime_seconds": time.monotonic() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", nargs="+", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    proof_path = Path(__file__).with_name("fixed_cell_convolution.md")
    payload = {
        "status": "exact_finite_fixed_cell_convolution_only",
        "target": "M73 nonlazy cyclic rank-two quotient; balanced fixed boundary cell",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
        "proof_note_sha256_before_run": sha256(proof_path),
        "results": [analyze(k) for k in args.k],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps([
        {
            "k": row["k"],
            "A_k_1_1": row["A_k_1_1_float"],
            "k_times_score_TV": row["k_times_score_sequence_TV_float"],
            "runtime_seconds": row["runtime_seconds"],
        }
        for row in payload["results"]
    ], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
