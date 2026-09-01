#!/usr/bin/env python3
"""Code-independent exact algebra checks for the frozen M65 claims.

This script deliberately imports no M65 or earlier experiment module.  It
checks the composition law, shuffle counts, fixed-cut Dirichlet energy,
rank-two counterexample, and extreme marked weights using ``Fraction``.
Finite checks are falsifiers/calibrations, not proofs of universal claims.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
from fractions import Fraction
from pathlib import Path


def compositions(total: int):
    if total == 0:
        yield ()
        return
    for first in range(1, total + 1):
        if first == total:
            yield (first,)
        else:
            for rest in compositions(total - first):
                yield (first,) + rest


def w(a: int) -> Fraction:
    return Fraction(a ** (a - 1), math.factorial(a))


def z(s: int) -> Fraction:
    return Fraction((s + 1) ** (s - 1), math.factorial(s))


def rho(comp: tuple[int, ...]) -> Fraction:
    ans = Fraction(1, math.factorial(len(comp)) * z(sum(comp)))
    for part in comp:
        ans *= w(part)
    return ans


def terminal(K: int, R: int, k: int) -> Fraction:
    return Fraction(
        K * math.comb(k + K - R - 2, K - R - 1),
        math.comb(k + K - 1, K - 1),
    )


def deep(K: int, R: int, k: int) -> Fraction:
    return 1 - Fraction(math.comb(K, R + 1), math.comb(K + k, R + 1))


def h_value(comp: tuple[int, ...], K: int, R: int, B: int) -> Fraction:
    k = len(comp)
    t = comp[-1]
    if t < B:
        return Fraction()
    if t == B:
        return terminal(K, R, k)
    return w(t - B) * w(B) / w(t) * deep(K, R, k)


def binary_words(K: int, k: int):
    n = K + k
    for inner_positions in itertools.combinations(range(n), k):
        inner = set(inner_positions)
        yield tuple("I" if q in inner else "O" for q in range(n))


def j_of_word(word: tuple[str, ...], R: int) -> int:
    outer_seen = 0
    inner_seen = 0
    for symbol in word:
        if symbol == "I":
            inner_seen += 1
        elif outer_seen == R:
            return inner_seen
        else:
            outer_seen += 1
    raise AssertionError("active outer factor not found")


def terminal_favourable(word: tuple[str, ...], R: int) -> bool:
    outer_seen = 0
    inner_seen = 0
    active_pos = None
    first_inner_pos = None
    for pos, symbol in enumerate(word):
        if symbol == "I":
            if inner_seen == 0:
                first_inner_pos = pos
            inner_seen += 1
        else:
            if outer_seen == R:
                active_pos = pos
            outer_seen += 1
    assert active_pos is not None and first_inner_pos is not None
    return abs(active_pos - first_inner_pos) == 1


def shuffle_checks(max_chain: int = 6):
    checks = 0
    for K in range(1, max_chain + 1):
        for k in range(1, max_chain + 1):
            words = tuple(binary_words(K, k))
            denominator = len(words)
            for R in range(K):
                counts = [0] * (k + 1)
                for word in words:
                    counts[j_of_word(word, R)] += 1
                for j, count in enumerate(counts):
                    expected = (
                        math.comb(R + j, j)
                        * math.comb(K - R - 1 + k - j, k - j)
                    )
                    assert count == expected
                    checks += 1

                favourable = sum(terminal_favourable(word, R) for word in words)
                normalized = Fraction(K + k, 2) * Fraction(favourable, denominator)
                assert normalized == terminal(K, R, k)
                checks += 1
    return checks


def composition_checks(s_max: int = 10, K_max: int = 8):
    rows = []
    for s in range(2, s_max + 1):
        comps = tuple(compositions(s))
        assert sum((rho(c) for c in comps), Fraction()) == 1

        terminal_set = tuple(c for c in comps if c[-1] == 1)
        p_s = sum((rho(c) for c in terminal_set), Fraction())
        outside = tuple(c for c in comps if c[-1] > 1)
        q_out = sum(
            (
                rho(c)
                * w(c[-1] - 1)
                * w(1)
                / w(c[-1])
                for c in outside
            ),
            Fraction(),
        )
        q_in = sum((rho(c) * len(c) for c in terminal_set), Fraction())
        m_s = w(s) / w(s + 1)
        assert q_out == q_in == m_s

        for K in range(1, K_max + 1):
            for R in range(K):
                for B in range(1, s + 1):
                    mean = sum(
                        (rho(c) * h_value(c, K, R, B) for c in comps),
                        Fraction(),
                    )
                    expected = w(s + 1 - B) * w(B) / w(s + 1)
                    assert mean == expected
        rows.append(
            {
                "s": s,
                "composition_count": len(comps),
                "fixed_cut_energy": str(m_s),
                "terminal_probability": str(p_s),
            }
        )
    return rows


def rank_two_checks():
    rows = []
    first_failure = None
    for K in range(1, 31):
        h_deep = Fraction(K, K + 1)
        h_terminal = Fraction(2, K + 1)
        mean = Fraction(2, 3) * h_deep + Fraction(1, 3) * h_terminal
        assert mean == Fraction(2, 3)
        green = Fraction(2 * (K - 2) ** 2, 27 * (K + 1) ** 2)
        terminal_mass = Fraction(2, 3 * (K + 1))
        ratio = green / terminal_mass
        assert ratio == Fraction((K - 2) ** 2, 9 * (K + 1))
        if ratio > 1 and first_failure is None:
            first_failure = K
        rows.append(
            {
                "K": K,
                "ambient_r": K + 2,
                "ratio": str(ratio),
            }
        )
    assert first_failure == 14
    assert rows[12]["ratio"] == "121/126"  # K=13, ambient 15.
    assert rows[13]["ratio"] == "16/15"    # K=14, ambient 16.
    return rows, first_failure


def extreme_checks():
    sequences = [(1,), (1, 1, 1, 1), (2, 3, 1), (4, 2, 5, 1)]
    rows = []
    for K0 in range(1, 8):
        for parts in sequences:
            K = K0
            product = Fraction(1)
            for k in parts:
                product *= Fraction(K, K + k)
                K += k
            assert product == Fraction(K0, K)
            rows.append({"K0": K0, "degrees": list(parts), "weight": str(product)})
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    shuffle_count = shuffle_checks()
    composition_rows = composition_checks()
    rank_two_rows, first_failure = rank_two_checks()
    extreme_rows = extreme_checks()
    result = {
        "claim_tested": "Independent exact algebra checks for frozen M65",
        "finite_scope_warning": "Finite checks are falsifiers and calibrations only.",
        "imports_m65_code": False,
        "python": platform.python_version(),
        "seed": None,
        "shuffle_identity_check_count": shuffle_count,
        "composition_rows": composition_rows,
        "rank_two_rows": rank_two_rows,
        "rank_two_first_failure_K": first_failure,
        "rank_two_first_failure_ambient_r": first_failure + 2,
        "extreme_rows": extreme_rows,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "shuffle_identity_check_count": shuffle_count,
        "composition_ranks": len(composition_rows),
        "rank_two_first_failure_K": first_failure,
        "rank_two_first_failure_ambient_r": first_failure + 2,
        "extreme_check_count": len(extreme_rows),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
