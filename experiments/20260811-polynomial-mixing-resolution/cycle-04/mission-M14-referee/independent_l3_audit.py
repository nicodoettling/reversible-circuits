#!/usr/bin/env python3
"""Independent exact referee audit for the frozen M14 l=3 theorem.

This code does not import the author harness. It enumerates the actual
six-transposition state graph for N=3,4, reconstructs the product-incidence
quotient independently, and checks composition, multiplicities, calibration
counts, identity-canonical glue, and the p_min bound.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import subprocess
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


Perm = tuple[int, ...]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for i, value in enumerate(p):
        out[value] = i
    return tuple(out)


def gates(n: int) -> list[Perm]:
    out = []
    for a in range(n):
        for b in range(a + 1, n):
            p = list(range(n))
            p[a], p[b] = p[b], p[a]
            out.append(tuple(p))
    return out


def evaluate(word: tuple[int, ...], trans: list[Perm]) -> Perm:
    value = tuple(range(len(trans[0])))
    for index in word:
        value = compose(value, trans[index])
    return value


def cycle_type(p: Perm) -> tuple[int, ...]:
    seen = [False] * len(p)
    lengths = []
    for start in range(len(p)):
        if seen[start]:
            continue
        current = start
        length = 0
        while not seen[current]:
            seen[current] = True
            current = p[current]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


class UF:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


def actual_components(words: list[tuple[int, ...]]) -> int:
    uf = UF(len(words))
    first_left: dict[tuple[int, int], int] = {}
    first_right: dict[tuple[int, int], int] = {}
    for index, word in enumerate(words):
        fixed_last_pair = (word[4], word[5])
        fixed_first_pair = (word[0], word[1])
        if fixed_last_pair in first_left:
            uf.union(index, first_left[fixed_last_pair])
        else:
            first_left[fixed_last_pair] = index
        if fixed_first_pair in first_right:
            uf.union(index, first_right[fixed_first_pair])
        else:
            first_right[fixed_first_pair] = index
    return len({uf.find(i) for i in range(len(words))})


def quotient_components(endpoint: Perm, trans: list[Perm]) -> tuple[int, int]:
    pair_products: dict[Perm, int] = Counter()
    for i, j in itertools.product(range(len(trans)), repeat=2):
        pair_products[compose(trans[i], trans[j])] += 1
    support = list(pair_products)
    index = {p: i for i, p in enumerate(support)}
    inv = {p: inverse(p) for p in support}
    size = len(support)
    uf = UF(2 * size)
    active: set[int] = set()
    weighted_states = 0
    for a in support:
        for c in support:
            b = compose(compose(inv[a], endpoint), inv[c])
            if b not in index:
                continue
            left = index[a]
            right = size + index[c]
            uf.union(left, right)
            active.add(left)
            active.add(right)
            weighted_states += pair_products[a] * pair_products[b] * pair_products[c]
    return len({uf.find(x) for x in active}), weighted_states


def audit_n(n: int) -> dict[str, object]:
    trans = gates(n)
    m = len(trans)
    identity = tuple(range(n))

    pair_count: Counter[Perm] = Counter()
    for i, j in itertools.product(range(m), repeat=2):
        pair_count[compose(trans[i], trans[j])] += 1
    multiplicity_by_type: dict[str, set[int]] = defaultdict(set)
    for product, count in pair_count.items():
        multiplicity_by_type[str(cycle_type(product))].add(count)

    fibers: dict[Perm, list[tuple[int, ...]]] = defaultdict(list)
    for word in itertools.product(range(m), repeat=6):
        fibers[evaluate(word, trans)].append(word)
    assert sum(map(len, fibers.values())) == m**6

    endpoint_rows = []
    by_type: dict[tuple[int, ...], set[int]] = defaultdict(set)
    for endpoint, words in fibers.items():
        actual = actual_components(words)
        quotient, weighted = quotient_components(endpoint, trans)
        assert len(words) == weighted
        assert actual == quotient
        assert actual == 1
        by_type[cycle_type(endpoint)].add(actual)
        endpoint_rows.append(
            {
                "cycle_type": list(cycle_type(endpoint)),
                "fiber_size": len(words),
                "actual_components": actual,
                "quotient_components": quotient,
            }
        )
    assert all(values == {1} for values in by_type.values())

    identity_four = sum(
        evaluate(word, trans) == identity
        for word in itertools.product(range(m), repeat=4)
    )
    f4: Counter[Perm] = Counter(
        evaluate(word, trans)
        for word in itertools.product(range(m), repeat=4)
    )
    max_f4 = max(f4.values())
    observed_p_min = Fraction(1, 2 * max_f4)
    claimed_floor = Fraction(1, 2 * m**4)
    assert observed_p_min >= claimed_floor

    for s, r in itertools.product(range(m), repeat=2):
        start = (s,) * 6
        middle = (r, r, r, r, s, s)
        finish = (r,) * 6
        assert evaluate(start, trans) == identity
        assert evaluate(middle, trans) == identity
        assert evaluate(finish, trans) == identity
        assert evaluate(start[:4], trans) == evaluate(middle[:4], trans)
        assert evaluate(middle[2:], trans) == evaluate(finish[2:], trans)

    expected = {3: (27, None, None), 4: (120, 3936, None)}
    if n in expected:
        assert identity_four == expected[n][0]
        if expected[n][1] is not None:
            assert len(fibers[identity]) == expected[n][1]

    return {
        "N": n,
        "M": m,
        "six_words": m**6,
        "endpoint_elements": len(fibers),
        "endpoint_cycle_types": len(by_type),
        "all_actual_and_quotient_connected": True,
        "identity_length_four": identity_four,
        "identity_length_six": len(fibers[identity]),
        "pair_product_multiplicities_by_cycle_type": {
            key: sorted(values) for key, values in sorted(multiplicity_by_type.items())
        },
        "max_F4": max_f4,
        "observed_selected_outcome_p_min": str(observed_p_min),
        "claimed_floor": str(claimed_floor),
        "endpoint_rows": sorted(endpoint_rows, key=lambda row: row["cycle_type"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "claim": (
            "Independent exact actual-state and product-quotient audit of "
            "M14 pair-length-three connectivity for N=3,4."
        ),
        "convention": "compose(p,q)=p after q; displayed word is t1...t6",
        "python": platform.python_version(),
        "command": " ".join([sys.executable, *sys.argv]),
        "commit": subprocess.run(
            ["git", "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip(),
        "cases": [audit_n(3), audit_n(4)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
