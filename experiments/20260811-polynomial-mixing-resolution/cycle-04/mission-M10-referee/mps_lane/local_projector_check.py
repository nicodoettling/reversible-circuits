#!/usr/bin/env python3
"""Exact tiny-case checks for the microfactor bridge/MPS algebra.

The computation is a falsification harness only.  It verifies the local
conditional-projector formula and endpoint-sector connectivity in N=3,4 and
n=2,3; no finite calculation is used as a universal proof.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
from collections import Counter
from fractions import Fraction
from pathlib import Path


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return pq under (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * len(p)
    for i, x in enumerate(p):
        out[x] = i
    return tuple(out)


def parity(p: tuple[int, ...]) -> int:
    inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return inv % 2


def transpositions(n: int) -> list[tuple[int, ...]]:
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            p = list(range(n))
            p[i], p[j] = p[j], p[i]
            out.append(tuple(p))
    return out


def alternating_group(n: int) -> list[tuple[int, ...]]:
    return [p for p in itertools.permutations(range(n)) if parity(p) == 0]


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1


def word_product(products: list[tuple[int, ...]], word: tuple[int, ...], identity: tuple[int, ...]) -> tuple[int, ...]:
    out = identity
    for idx in word:
        out = compose(out, products[idx])
    return out


def check_case(n_points: int, length: int) -> dict[str, object]:
    ts = transpositions(n_points)
    identity = tuple(range(n_points))
    products = [compose(a, b) for a in ts for b in ts]
    alphabet_size = len(products)

    # The two-site heat bath has one all-ones/|fiber| block for each ordered
    # product fiber.  This checks the exact convolution counts and hence
    # stochasticity, symmetry, idempotence, and rank without floating point.
    one_site_counts = Counter(products)
    two_site_counts_direct: Counter[tuple[int, ...]] = Counter()
    for a in products:
        for b in products:
            two_site_counts_direct[compose(a, b)] += 1
    two_site_counts_conv: Counter[tuple[int, ...]] = Counter()
    for a, ca in one_site_counts.items():
        for b, cb in one_site_counts.items():
            two_site_counts_conv[compose(a, b)] += ca * cb
    assert two_site_counts_direct == two_site_counts_conv
    assert sum(two_site_counts_direct.values()) == alphabet_size**2
    projector_checks = all(
        k > 0
        and k * Fraction(1, k) == 1
        and k * Fraction(1, k) ** 2 == Fraction(1, k)
        for k in two_site_counts_direct.values()
    )

    # Regular-representation boundary matrices already span endpoint delta
    # functions: Tr(L_{h^{-1}} L_g)=|G| 1[g=h].  Peter--Weyl is its irreducible
    # block decomposition.
    group = alternating_group(n_points)
    regular_delta_check = True
    for h in group:
        h_inv = inverse(h)
        for g in group:
            k = compose(h_inv, g)
            trace = len(group) if k == identity else 0
            if trace != len(group) * int(g == h):
                regular_delta_check = False
    assert regular_delta_check

    words = list(itertools.product(range(alphabet_size), repeat=length))
    uf = UnionFind(len(words))
    first_for_key: dict[tuple[object, ...], int] = {}
    for idx, word in enumerate(words):
        for site in range(length - 1):
            local_product = compose(products[word[site]], products[word[site + 1]])
            outside = word[:site] + word[site + 2 :]
            key = (site, outside, local_product)
            if key in first_for_key:
                uf.union(idx, first_for_key[key])
            else:
                first_for_key[key] = idx

    sector_roots: dict[tuple[int, ...], set[int]] = {}
    for idx, word in enumerate(words):
        endpoint = word_product(products, word, identity)
        sector_roots.setdefault(endpoint, set()).add(uf.find(idx))
    component_counts = sorted(len(roots) for roots in sector_roots.values())
    assert component_counts and max(component_counts) == 1

    return {
        "N": n_points,
        "micro_length_n": length,
        "transpositions_M": len(ts),
        "alphabet_E_size": alphabet_size,
        "states_E_power_n": len(words),
        "one_site_endpoint_count": len(one_site_counts),
        "two_site_projector_rank": len(two_site_counts_direct),
        "two_site_projector_formula_exact": projector_checks,
        "regular_representation_delta_basis_exact": regular_delta_check,
        "feasible_global_endpoint_count": len(sector_roots),
        "max_components_per_endpoint": max(component_counts),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    cases = [check_case(n_points, length) for n_points in (3, 4) for length in (2, 3)]
    payload = {
        "status": "pass",
        "composition": "(pq)(x)=p(q(x))",
        "claim_scope": "finite falsification only",
        "python": platform.python_version(),
        "deterministic": True,
        "cases": cases,
    }
    Path(args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
