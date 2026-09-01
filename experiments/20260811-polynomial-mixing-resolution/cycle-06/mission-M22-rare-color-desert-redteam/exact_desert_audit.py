#!/usr/bin/env python3
"""Exact finite audit for the M22 rare-color desert cut.

Universal statements this bounded calculation can falsify:

* a length-r same-product heat bath is normalized by its exact ordered-product
  fiber for r=3,4,5;
* the disjoint-factor H3 swap is in the claimed conditional fiber and exits
  the desert cut;
* for the N=5,m=24 representative, all r=3,4,5 boundary outcomes decompose
  into target-macro color exits and macro-changing exits.

It cannot prove any asymptotic conductance statement.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import subprocess
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return pq, meaning p after q: (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def transposition_perm(n: int, e: tuple[int, int]) -> tuple[int, ...]:
    p = list(range(n))
    i, j = e
    p[i], p[j] = p[j], p[i]
    return tuple(p)


def word_product(
    word: tuple[tuple[int, int], ...], edge_perm: dict[tuple[int, int], tuple[int, ...]], n: int
) -> tuple[int, ...]:
    p = tuple(range(n))
    for e in word:
        p = compose(p, edge_perm[e])
    return p


def support_components(n: int, word: tuple[tuple[int, int], ...]):
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

    for i, j in word:
        union(i, j)
    blocks: dict[int, set[int]] = defaultdict(set)
    for x in range(n):
        blocks[find(x)].add(x)
    out = []
    for block in blocks.values():
        weight = sum(1 for e in word if e[0] in block and e[1] in block)
        out.append((frozenset(block), weight))
    return sorted(out, key=lambda z: (len(z[0]), sorted(z[0])))


def target_macro(n: int, word, rare_weight: int = 4):
    comps = support_components(n, word)
    nontrivial = [(s, k) for s, k in comps if len(s) >= 2]
    isolates = [(s, k) for s, k in comps if len(s) == 1]
    if isolates or len(nontrivial) != 2:
        return None
    rare = [(s, k) for s, k in nontrivial if len(s) == 3 and k == rare_weight]
    big = [(s, k) for s, k in nontrivial if len(s) == n - 3 and k == len(word) - rare_weight]
    if len(rare) != 1 or len(big) != 1 or rare[0][0] & big[0][0]:
        return None
    return rare[0][0]


def in_desert_cut(n: int, word, separation: int) -> bool:
    rare = target_macro(n, word)
    if rare is None:
        return False
    positions = [i for i, e in enumerate(word) if e[0] in rare and e[1] in rare]
    return len(positions) == 4 and all(
        positions[j + 1] - positions[j] - 1 >= separation for j in range(3)
    )


def macro_change_kind(n: int, word) -> str:
    """Classify topology after leaving the two-component target macro."""
    comps = support_components(n, word)
    if len(comps) == 1 and len(comps[0][0]) == n:
        return "merge_to_full_support"
    if len(comps) >= 3:
        return "split_to_three_or_more_components"
    return "two_component_repartition_or_weight_change"


def frac_dict(x: Fraction) -> dict[str, object]:
    return {
        "numerator": x.numerator,
        "denominator": x.denominator,
        "decimal": float(x),
    }


def identity_count(n: int, m: int) -> int:
    edges = tuple(itertools.combinations(range(n), 2))
    perms = {e: transposition_perm(n, e) for e in edges}
    identity = tuple(range(n))
    return sum(
        word_product(word, perms, n) == identity
        for word in itertools.product(edges, repeat=m)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="results.json")
    args = parser.parse_args()

    n, m, separation = 5, 24, 5
    edges = tuple(itertools.combinations(range(n), 2))
    edge_perm = {e: transposition_perm(n, e) for e in edges}
    identity = tuple(range(n))
    M = len(edges)

    fibers: dict[int, dict[tuple[int, ...], list[tuple[tuple[int, int], ...]]]] = {}
    for r in (3, 4, 5):
        groups = defaultdict(list)
        for block in itertools.product(edges, repeat=r):
            groups[word_product(block, edge_perm, n)].append(block)
        assert sum(map(len, groups.values())) == M**r
        fibers[r] = groups

    rare_internal = ((0, 1), (1, 2), (1, 2), (0, 1))
    big_internal = ((3, 4),) * 20
    assert word_product(rare_internal, edge_perm, n) == identity
    assert word_product(big_internal, edge_perm, n) == identity
    rare_it = iter(rare_internal)
    big_it = iter(big_internal)
    colors = tuple("A" + "B" * separation) * 4
    word = tuple(next(rare_it) if c == "A" else next(big_it) for c in colors)
    assert len(word) == m
    assert word_product(word, edge_perm, n) == identity
    assert in_desert_cut(n, word, separation)

    total = Fraction(0)
    by_r = {}
    all_window_color_counts = {}
    for r in (3, 4, 5):
        rw = m - r + 1
        probs = defaultdict(Fraction)
        macro_details = defaultdict(Fraction)
        for key in (
            "merge_to_full_support",
            "split_to_three_or_more_components",
            "two_component_repartition_or_weight_change",
        ):
            macro_details[key] = Fraction(0)
        occupancy = defaultdict(int)
        for i in range(rw):
            current = word[i : i + r]
            product = word_product(current, edge_perm, n)
            fiber = fibers[r][product]
            rare_in_window = sum(1 for e in current if e[0] <= 2 and e[1] <= 2)
            occupancy[rare_in_window] += 1
            scan_weight = Fraction(1, 6 * rw * len(fiber))
            for target in fiber:
                new_word = word[:i] + target + word[i + r :]
                if in_desert_cut(n, new_word, separation):
                    kind = "stays_in_cut"
                elif target_macro(n, new_word) is not None:
                    kind = "same_target_macro_non_desert"
                else:
                    kind = "macro_change"
                    macro_details[macro_change_kind(n, new_word)] += scan_weight
                probs[kind] += scan_weight
        # These are update-part probabilities including the 1/(2|R|)=1/6
        # coefficient, but excluding contributions from other r and laziness.
        by_r[str(r)] = {k: frac_dict(v) for k, v in sorted(probs.items())}
        by_r[str(r)]["macro_change_breakdown"] = {
            k: frac_dict(v) for k, v in sorted(macro_details.items())
        }
        all_window_color_counts[str(r)] = dict(sorted(occupancy.items()))
        total += probs["same_target_macro_non_desert"] + probs["macro_change"]

    first = word[:3]
    swapped = (first[1], first[0], first[2])
    first_product = word_product(first, edge_perm, n)
    assert word_product(swapped, edge_perm, n) == first_product
    assert swapped in fibers[3][first_product]
    swapped_word = swapped + word[3:]
    assert target_macro(n, swapped_word) is not None
    assert not in_desert_cut(n, swapped_word, separation)
    specified_swap_probability = Fraction(1, 6 * (m - 2) * len(fibers[3][first_product]))
    theorem_lower_bound = Fraction(1, 6 * (m - 2) * M**2)
    assert specified_swap_probability >= theorem_lower_bound

    repo_commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], text=True
    ).strip()
    result = {
        "metadata": {
            "repository_commit": repo_commit,
            "python": platform.python_version(),
            "command": "python3 exact_desert_audit.py --output results.json",
            "random_seed": None,
            "enumeration": "deterministic exhaustive local fibers",
            "composition_convention": "(pq)(x)=p(q(x)); ordered word t1...tm",
        },
        "calibration_identity_counts": {
            "S3_m4": identity_count(3, 4),
            "S4_m4": identity_count(4, 4),
            "S4_m6": identity_count(4, 6),
        },
        "representative": {
            "N": n,
            "m": m,
            "M": M,
            "separation": separation,
            "colors": "".join(colors),
            "rare_internal": rare_internal,
            "big_internal_edge_repeated": [3, 4],
        },
        "fiber_statistics": {
            str(r): {
                "number_of_products": len(fibers[r]),
                "total_words": sum(map(len, fibers[r].values())),
                "min_fiber": min(map(len, fibers[r].values())),
                "max_fiber": max(map(len, fibers[r].values())),
            }
            for r in (3, 4, 5)
        },
        "window_rare_factor_counts": all_window_color_counts,
        "full_K_update_classification_by_r": by_r,
        "total_exit_probability_from_representative": frac_dict(total),
        "specified_H3_swap": {
            "fiber_size": len(fibers[3][first_product]),
            "exact_full_K_probability": frac_dict(specified_swap_probability),
            "M_squared_lower_bound": frac_dict(theorem_lower_bound),
        },
    }
    Path(args.output).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
