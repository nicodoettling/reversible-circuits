#!/usr/bin/env python3
"""Exact audit of the rank stable-sort disintegration.

Convention: permutations are tuples representing maps, and
compose(a, b) = a o b.  Thus the rightmost factor of a displayed product
acts first.

The coefficient calculation uses endpoint dynamic programming.  The separate
word-level audit enumerates the Cartesian domains of the fixed-pattern inverse
maps; this is the requested exhaustive bijection check, not the method used to
obtain the endpoint coefficients.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
import subprocess
import time
from collections import Counter
from pathlib import Path
from typing import Iterable, Iterator, Sequence


Perm = tuple[int, ...]
Word = tuple[Perm, ...]
Pattern = tuple[bool, ...]  # False = old, True = star.


def identity(n: int) -> Perm:
    return tuple(range(n))


def compose(left: Perm, right: Perm) -> Perm:
    """Return left o right, so right acts first."""

    return tuple(left[right[x]] for x in range(len(left)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def transposition(n: int, i: int, j: int) -> Perm:
    p = list(range(n))
    p[i], p[j] = p[j], p[i]
    return tuple(p)


def all_transpositions(n: int) -> tuple[Perm, ...]:
    return tuple(transposition(n, i, j) for i in range(n) for j in range(i + 1, n))


def old_transpositions(n: int) -> tuple[Perm, ...]:
    return tuple(
        transposition(n, i, j)
        for i in range(n - 1)
        for j in range(i + 1, n - 1)
    )


def star_transpositions(n: int) -> tuple[Perm, ...]:
    return tuple(transposition(n, i, n - 1) for i in range(n - 1))


def permutations(n: int) -> Iterator[Perm]:
    yield from itertools.permutations(range(n))


def evaluate(word: Sequence[Perm], n: int) -> Perm:
    value = identity(n)
    for factor in word:
        value = compose(value, factor)
    return value


def is_star(factor: Perm) -> bool:
    return factor[-1] != len(factor) - 1


def star_lower_endpoint(factor: Perm) -> int:
    assert is_star(factor)
    i = factor[-1]
    assert factor[i] == len(factor) - 1
    return i


def word_pattern(word: Sequence[Perm]) -> Pattern:
    return tuple(is_star(factor) for factor in word)


def pattern_inversions(pattern: Pattern) -> int:
    stars_seen = 0
    inversions = 0
    for tag in pattern:
        if tag:
            stars_seen += 1
        else:
            inversions += stars_seen
    return inversions


def move_star_right(star: Perm, old: Perm) -> tuple[Perm, Perm]:
    """Rewrite tau_i old as old tau_{old^{-1}(i)}."""

    n = len(star)
    assert is_star(star) and not is_star(old)
    i = star_lower_endpoint(star)
    j = inverse(old)[i]
    new_star = transposition(n, j, n - 1)
    assert compose(star, old) == compose(old, new_star)
    return old, new_star


def move_star_left(old: Perm, star: Perm) -> tuple[Perm, Perm]:
    """Rewrite old tau_j as tau_{old(j)} old."""

    n = len(star)
    assert not is_star(old) and is_star(star)
    j = star_lower_endpoint(star)
    i = old[j]
    new_star = transposition(n, i, n - 1)
    assert compose(old, star) == compose(new_star, old)
    return new_star, old


def stable_sort_adjacent(word: Sequence[Perm], strategy: str) -> tuple[Word, Word, int]:
    """Stable-sort old factors left using the local product-preserving rule."""

    items = list(word)
    swaps = 0
    while True:
        candidates = [
            i
            for i in range(len(items) - 1)
            if is_star(items[i]) and not is_star(items[i + 1])
        ]
        if not candidates:
            break
        if strategy == "leftmost":
            i = candidates[0]
        elif strategy == "rightmost":
            i = candidates[-1]
        else:
            raise ValueError(strategy)
        items[i], items[i + 1] = move_star_right(items[i], items[i + 1])
        swaps += 1
    split = next((i for i, factor in enumerate(items) if is_star(factor)), len(items))
    old_word = tuple(items[:split])
    star_word = tuple(items[split:])
    assert all(not is_star(factor) for factor in old_word)
    assert all(is_star(factor) for factor in star_word)
    return old_word, star_word, swaps


def stable_sort_formula(word: Sequence[Perm], n: int) -> tuple[Word, Word]:
    """Closed form: a star is acted on by the inverse old suffix to its right."""

    old_word = tuple(factor for factor in word if not is_star(factor))
    transformed_stars: list[Perm] = []
    for position, factor in enumerate(word):
        if not is_star(factor):
            continue
        suffix = tuple(candidate for candidate in word[position + 1 :] if not is_star(candidate))
        suffix_value = evaluate(suffix, n)
        old_i = star_lower_endpoint(factor)
        new_i = inverse(suffix_value)[old_i]
        transformed_stars.append(transposition(n, new_i, n - 1))
    return old_word, tuple(transformed_stars)


def invert_stable_sort(
    old_word: Sequence[Perm], star_word: Sequence[Perm], pattern: Pattern
) -> tuple[Word, int]:
    """Invert the stable sort for one fixed binary pattern.

    Start at old_word + star_word.  Reading the target pattern from left to
    right, move the next star left whenever the target position is a star.
    Every move uses old tau_j -> tau_{old(j)} old.
    """

    assert len(old_word) + len(star_word) == len(pattern)
    assert sum(pattern) == len(star_word)
    items = list(old_word) + list(star_word)
    swaps = 0
    for position, want_star in enumerate(pattern):
        if not want_star:
            assert not is_star(items[position])
            continue
        star_position = next(
            i for i in range(position, len(items)) if is_star(items[i])
        )
        while star_position > position:
            assert not is_star(items[star_position - 1])
            items[star_position - 1], items[star_position] = move_star_left(
                items[star_position - 1], items[star_position]
            )
            star_position -= 1
            swaps += 1
    answer = tuple(items)
    assert word_pattern(answer) == pattern
    return answer, swaps


def all_patterns(length: int, star_count: int) -> Iterable[Pattern]:
    for star_positions in itertools.combinations(range(length), star_count):
        position_set = set(star_positions)
        yield tuple(position in position_set for position in range(length))


def endpoint_dp(n: int, alphabet: Sequence[Perm], max_length: int) -> list[Counter[Perm]]:
    counts: list[Counter[Perm]] = [Counter({identity(n): 1})]
    for _ in range(max_length):
        following: Counter[Perm] = Counter()
        for endpoint, multiplicity in counts[-1].items():
            for factor in alphabet:
                following[compose(endpoint, factor)] += multiplicity
        counts.append(following)
    return counts


def cycle_count(p: Perm) -> int:
    seen = [False] * len(p)
    answer = 0
    for start in range(len(p)):
        if seen[start]:
            continue
        answer += 1
        x = start
        while not seen[x]:
            seen[x] = True
            x = p[x]
    return answer


def sign_from_cycles(p: Perm) -> int:
    return -1 if (len(p) - cycle_count(p)) % 2 else 1


def one_based(p: Perm) -> list[int]:
    return [x + 1 for x in p]


def perm_cycles_string(p: Perm) -> str:
    seen = [False] * len(p)
    cycles: list[str] = []
    for start in range(len(p)):
        if seen[start]:
            continue
        cycle: list[int] = []
        x = start
        while not seen[x]:
            seen[x] = True
            cycle.append(x + 1)
            x = p[x]
        if len(cycle) > 1:
            cycles.append("(" + " ".join(map(str, cycle)) + ")")
    return "".join(cycles) if cycles else "e"


def git_commit(repo: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=repo, text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def audit_rank(
    n: int,
    max_length: int,
) -> tuple[list[dict[str, object]], list[dict[str, object]], dict[str, object]]:
    full_alphabet = all_transpositions(n)
    old_alphabet = old_transpositions(n)
    star_alphabet = star_transpositions(n)
    endpoints = tuple(permutations(n))

    direct_dp = endpoint_dp(n, full_alphabet, max_length)
    old_dp = endpoint_dp(n, old_alphabet, max_length)
    star_dp = endpoint_dp(n, star_alphabet, max_length)

    endpoint_rows: list[dict[str, object]] = []
    case_rows: list[dict[str, object]] = []
    total_bijection_cases = 0
    total_endpoint_checks = 0

    # Exhaustively audit the conjugation identity h tau_i = tau_{h(i)} h.
    conjugation_identity_checks = 0
    for h_small in itertools.permutations(range(n - 1)):
        h = tuple(h_small) + (n - 1,)
        for i in range(n - 1):
            tau_i = transposition(n, i, n - 1)
            tau_hi = transposition(n, h[i], n - 1)
            assert compose(h, tau_i) == compose(tau_hi, h)
            conjugation_identity_checks += 1

    for length in range(max_length + 1):
        bijection_endpoint_counts: Counter[Perm] = Counter()
        bijection_cases = 0
        adjacent_swap_steps = 0
        for star_count in range(length + 1):
            old_length = length - star_count
            for pattern in all_patterns(length, star_count):
                expected_swaps = pattern_inversions(pattern)
                for old_word in itertools.product(old_alphabet, repeat=old_length):
                    for star_word in itertools.product(star_alphabet, repeat=star_count):
                        reconstructed, inverse_swaps = invert_stable_sort(
                            old_word, star_word, pattern
                        )
                        assert inverse_swaps == expected_swaps
                        left_old, left_star, left_swaps = stable_sort_adjacent(
                            reconstructed, "leftmost"
                        )
                        right_old, right_star, right_swaps = stable_sort_adjacent(
                            reconstructed, "rightmost"
                        )
                        formula_old, formula_star = stable_sort_formula(reconstructed, n)
                        assert left_old == tuple(old_word)
                        assert left_star == tuple(star_word)
                        assert (right_old, right_star) == (left_old, left_star)
                        assert (formula_old, formula_star) == (left_old, left_star)
                        assert left_swaps == expected_swaps == right_swaps
                        round_trip, round_trip_swaps = invert_stable_sort(
                            left_old, left_star, pattern
                        )
                        assert round_trip == reconstructed
                        assert round_trip_swaps == expected_swaps
                        sorted_product = compose(
                            evaluate(old_word, n), evaluate(star_word, n)
                        )
                        endpoint = evaluate(reconstructed, n)
                        assert endpoint == sorted_product
                        bijection_endpoint_counts[endpoint] += 1
                        bijection_cases += 1
                        adjacent_swap_steps += left_swaps + right_swaps + inverse_swaps + round_trip_swaps

        expected_cases = len(full_alphabet) ** length
        assert bijection_cases == expected_cases
        total_bijection_cases += bijection_cases

        # Positive convolution form of the RHS, independently of the full DP.
        convolution_rhs: Counter[Perm] = Counter()
        for star_count in range(length + 1):
            pattern_count = math.comb(length, star_count)
            for h, old_multiplicity in old_dp[length - star_count].items():
                for q, star_multiplicity in star_dp[star_count].items():
                    convolution_rhs[compose(h, q)] += (
                        pattern_count * old_multiplicity * star_multiplicity
                    )

        max_abs_difference = 0
        opposite_orientation_max_abs_difference = 0
        feasible_mismatches = 0
        for g in endpoints:
            direct = direct_dp[length][g]
            disintegration = 0
            opposite_orientation = 0
            for star_count in range(length + 1):
                pattern_count = math.comb(length, star_count)
                for h, old_multiplicity in old_dp[length - star_count].items():
                    required_q = compose(inverse(h), g)
                    # This is not the word endpoint, but its coefficient is
                    # equal here because J_N commutes with H.  Record that
                    # numerical coefficient checks cannot settle orientation.
                    opposite_q = compose(g, inverse(h))
                    disintegration += (
                        pattern_count
                        * old_multiplicity
                        * star_dp[star_count][required_q]
                    )
                    opposite_orientation += (
                        pattern_count
                        * old_multiplicity
                        * star_dp[star_count][opposite_q]
                    )
            assert disintegration == convolution_rhs[g]
            max_abs_difference = max(max_abs_difference, abs(direct - disintegration))
            opposite_orientation_max_abs_difference = max(
                opposite_orientation_max_abs_difference,
                abs(direct - opposite_orientation),
            )
            transposition_length = n - cycle_count(g)
            feasible = (
                ((-1) ** length == sign_from_cycles(g))
                and length >= transposition_length
            )
            if (direct > 0) != feasible:
                feasible_mismatches += 1
            assert bijection_endpoint_counts[g] == direct
            endpoint_rows.append(
                {
                    "record": "endpoint",
                    "N": n,
                    "L": length,
                    "endpoint_map_one_based": one_based(g),
                    "endpoint_cycles": perm_cycles_string(g),
                    "transposition_length": transposition_length,
                    "feasible": feasible,
                    "direct_coefficient": direct,
                    "disintegration_coefficient": disintegration,
                    "opposite_orientation_coefficient": opposite_orientation,
                    "bijection_cases": bijection_endpoint_counts[g],
                }
            )
            total_endpoint_checks += 1

        assert max_abs_difference == 0
        assert opposite_orientation_max_abs_difference == 0
        assert feasible_mismatches == 0
        assert sum(direct_dp[length].values()) == expected_cases
        assert sum(convolution_rhs.values()) == expected_cases
        assert sum(bijection_endpoint_counts.values()) == expected_cases
        case_rows.append(
            {
                "record": "case_summary",
                "N": n,
                "L": length,
                "transposition_types": len(full_alphabet),
                "binary_patterns": 2**length,
                "endpoints_checked": len(endpoints),
                "coefficient_max_abs_difference": max_abs_difference,
                "opposite_orientation_coefficient_max_abs_difference": opposite_orientation_max_abs_difference,
                "feasibility_mismatches": feasible_mismatches,
                "bijection_cases": bijection_cases,
                "adjacent_rewrite_steps_checked": adjacent_swap_steps,
                "all_checks_passed": True,
            }
        )

    # A concrete word-level witness that h^{-1}g, not g h^{-1}, is q.
    if n >= 3:
        h = transposition(n, 0, 1)
        q = transposition(n, 0, n - 1)
        g = compose(h, q)
        correct_q = compose(inverse(h), g)
        wrong_q = compose(g, inverse(h))
        assert correct_q == q
        assert wrong_q != q
        orientation_witness: dict[str, object] | None = {
            "N": n,
            "h_cycles": perm_cycles_string(h),
            "q_cycles": perm_cycles_string(q),
            "g_equals_hq_cycles": perm_cycles_string(g),
            "h_inverse_g_cycles": perm_cycles_string(correct_q),
            "g_h_inverse_cycles": perm_cycles_string(wrong_q),
        }
    else:
        orientation_witness = None

    rank_summary: dict[str, object] = {
        "N": n,
        "lengths": [0, max_length],
        "endpoint_checks": total_endpoint_checks,
        "bijection_cases": total_bijection_cases,
        "conjugation_identity_checks": conjugation_identity_checks,
        "orientation_witness": orientation_witness,
        "all_checks_passed": True,
    }
    return endpoint_rows, case_rows, rank_summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-n", type=int, default=2)
    parser.add_argument("--max-n", type=int, default=5)
    parser.add_argument("--max-length", type=int, default=6)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent,
    )
    args = parser.parse_args()
    if not (2 <= args.min_n <= args.max_n):
        raise SystemExit("require 2 <= min-n <= max-n")
    if args.max_length < 0:
        raise SystemExit("require max-length >= 0")

    start = time.time()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    repo = Path(__file__).resolve().parents[4]
    all_endpoint_rows: list[dict[str, object]] = []
    all_case_rows: list[dict[str, object]] = []
    rank_summaries: list[dict[str, object]] = []

    for n in range(args.min_n, args.max_n + 1):
        endpoint_rows, case_rows, rank_summary = audit_rank(n, args.max_length)
        all_endpoint_rows.extend(endpoint_rows)
        all_case_rows.extend(case_rows)
        rank_summaries.append(rank_summary)

    results_path = output_dir / "results.jsonl"
    with results_path.open("w", encoding="utf-8") as handle:
        for row in all_case_rows:
            handle.write(json.dumps(row, sort_keys=True) + "\n")
        for row in all_endpoint_rows:
            handle.write(json.dumps(row, sort_keys=True) + "\n")

    summary: dict[str, object] = {
        "claim": "fixed-pattern stable sort is a product-preserving bijection and (D) holds",
        "status": "exact finite validation",
        "convention": "(alpha beta)(x)=alpha(beta(x)); rightmost displayed factor acts first",
        "parameters": {
            "min_N": args.min_n,
            "max_N": args.max_n,
            "min_L": 0,
            "max_L": args.max_length,
        },
        "repository_commit": git_commit(repo),
        "python_version": platform.python_version(),
        "nonstandard_dependencies": [],
        "rank_summaries": rank_summaries,
        "totals": {
            "rank_length_cases": len(all_case_rows),
            "endpoint_coefficient_checks": len(all_endpoint_rows),
            "bijection_cases": sum(row["bijection_cases"] for row in all_case_rows),
            "adjacent_rewrite_steps_checked": sum(
                row["adjacent_rewrite_steps_checked"] for row in all_case_rows
            ),
            "all_checks_passed": all(row["all_checks_passed"] for row in all_case_rows),
        },
        "coefficient_method": "exact endpoint dynamic programming",
        "bijection_method": "exhaustive structured enumeration over pattern x old-word x star-word",
        "note_on_orientation": (
            "The opposite g h^{-1} coefficient happens to agree because J_N commutes "
            "with H; the stored word-level witness distinguishes the actual star endpoint."
        ),
        "elapsed_seconds": time.time() - start,
    }
    summary_path = output_dir / "summary.json"
    with summary_path.open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2, sort_keys=True)
        handle.write("\n")

    # Hash after both files are closed.  This line is intended for captured logs.
    print(json.dumps(summary, sort_keys=True))
    print(f"results_sha256={sha256(results_path)}")
    print(f"summary_path={summary_path}")


if __name__ == "__main__":
    main()
