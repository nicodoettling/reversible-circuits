#!/usr/bin/env python3
"""Small exact audit of M155's colored double-orbit disintegration.

This is deliberately self-contained: it imports no predecessor or M155 code.
It enumerates only n=9 and n=15 and uses Fraction for every asserted mass.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import subprocess
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
M155 = ROOT / "experiments/20260811-polynomial-mixing-resolution/cycle-35/mission-M155-balanced-direct-l1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return pq, so (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    ans = [0] * len(p)
    for i, x in enumerate(p):
        ans[x] = i
    return tuple(ans)


def transposition(n: int, a: int, b: int) -> tuple[int, ...]:
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def cycle_sizes(p: tuple[int, ...]) -> list[int]:
    seen = [False] * len(p)
    out = []
    for i in range(len(p)):
        if not seen[i]:
            j = i
            size = 0
            while not seen[j]:
                seen[j] = True
                size += 1
                j = p[j]
            out.append(size)
    return sorted(out)


def canon_edges(edges: frozenset[tuple[int, int]]) -> tuple[tuple[int, int], ...]:
    return tuple(sorted(tuple(sorted(e)) for e in edges))


def rotate(edges: frozenset[tuple[int, int]], r: int, n: int) -> frozenset[tuple[int, int]]:
    return frozenset(tuple(sorted(((a + r) % n, (b + r) % n))) for a, b in edges)


def orbit(edges: frozenset[tuple[int, int]], n: int) -> set[tuple[tuple[int, int], ...]]:
    return {canon_edges(rotate(edges, r, n)) for r in range(n)}


def tau(r: int) -> Fraction:
    return Fraction(r ** (r - 1), math.factorial(r))


def orbit_mass(n: int, residual_sizes: list[int]) -> Fraction:
    ans = Fraction(2 * n * math.factorial(n - 3), n ** (n - 2))
    for d in residual_sizes:
        ans *= tau(d)
    return ans


def cell_weight(n: int, a: int, b: int) -> Fraction:
    c = n - a - b
    ans = Fraction((c - 1) * n * math.factorial(n - 3), 2 * n ** (n - 2))
    return ans * tau(a) * tau(b) * tau(c)


def colored_encodings(edges: frozenset[tuple[int, int]], n: int) -> list[tuple[tuple[int, int, int, int], str]]:
    support = set(x for e in edges for x in e)
    ans = []
    for anchor in support:
        vertices = sorted(support, key=lambda x: (x - anchor) % n)
        gaps = tuple((vertices[(i + 1) % 4] - vertices[i]) % n for i in range(4))
        index = {v: i for i, v in enumerate(vertices)}
        matching = {tuple(sorted((index[a], index[b]))) for a, b in edges}
        if matching == {(0, 1), (2, 3)}:
            color = "S"
        elif matching == {(0, 3), (1, 2)}:
            color = "N"
        else:
            raise AssertionError((n, edges, vertices, matching))
        ans.append((gaps, color))
    return ans


def audit_n(n: int) -> dict[str, object]:
    h = tuple((i + 1) % n for i in range(n))
    raw = set()
    for vertices in combinations(range(n), 4):
        a, b, c, d = vertices
        for pairs in (((a, b), (c, d)), ((a, d), (b, c)), ((a, c), (b, d))):
            edges = frozenset(tuple(sorted(e)) for e in pairs)
            g = compose(transposition(n, *pairs[0]), transposition(n, *pairs[1]))
            residual = compose(inverse(g), h)
            if n - len(cycle_sizes(residual)) == n - 3:
                raw.add(canon_edges(edges))

    expected_raw = 2 * math.comb(n, 4)
    assert len(raw) == expected_raw
    remaining = set(raw)
    representatives = []
    while remaining:
        rep = min(remaining)
        orb = orbit(frozenset(rep), n)
        assert len(orb) == n
        assert orb <= raw
        remaining -= orb
        representatives.append(frozenset(rep))

    separated_compositions = Counter()
    nested_compositions = Counter()
    by_cell: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
    total_mass = Fraction(0)
    factor_test_lhs = Fraction(0)
    factor_test_quarter_separated = Fraction(0)
    encoding_counts = Counter()

    for rep in representatives:
        encodings = colored_encodings(rep, n)
        assert len(set(encodings)) == 4
        assert Counter(color for _, color in encodings) == {"S": 2, "N": 2}

        g = tuple(range(n))
        for a, b in rep:
            g = compose(g, transposition(n, a, b))
        residual_sizes = cycle_sizes(compose(inverse(g), h))
        assert len(residual_sizes) == 3
        mass = orbit_mass(n, residual_sizes)
        total_mass += mass

        # An arbitrary nonnegative orbit function tests the multiplicity
        # identity independently of the score z.
        f_value = Fraction(1 + sum(d * d for d in residual_sizes), 1)
        factor_test_lhs += mass * f_value

        for gaps, color in encodings:
            x, y, z, w = gaps
            if color == "S":
                assert sorted((x, z, y + w)) == residual_sizes
                separated_compositions[gaps] += 1
                by_cell[(x, z)] += mass / 4
                factor_test_quarter_separated += mass * f_value / 4
            else:
                assert sorted((x + z, y, w)) == residual_sizes
                nested_compositions[gaps] += 1
            encoding_counts[color] += 1

    all_compositions = {
        (x, y, z, n - x - y - z)
        for x in range(1, n - 2)
        for y in range(1, n - x - 1)
        for z in range(1, n - x - y)
    }
    assert set(separated_compositions) == all_compositions
    assert set(nested_compositions) == all_compositions
    assert set(separated_compositions.values()) == {1}
    assert set(nested_compositions.values()) == {1}

    expected_cells = {
        (a, b): cell_weight(n, a, b)
        for a in range(1, n - 2)
        for b in range(1, n - a - 1)
    }
    assert dict(by_cell) == expected_cells
    expected_double_mass = Fraction(n - 3, n)
    expected_half_mass = Fraction(n - 3, 2 * n)
    assert total_mass == expected_double_mass
    assert sum(by_cell.values(), Fraction(0)) == expected_half_mass
    assert factor_test_lhs == 2 * factor_test_quarter_separated

    fixed_cells = []
    for a, b in ((1, 1), (1, 3), (3, 3)):
        if a + b <= n - 2:
            fixed_cells.append({"a": a, "b": b, "W_exact": str(by_cell[(a, b)])})

    return {
        "n": n,
        "raw_supported_doubles": len(raw),
        "expected_raw_supported_doubles": expected_raw,
        "quotient_double_orbits": len(representatives),
        "all_orbit_sizes_equal_n": True,
        "colored_encodings": dict(sorted(encoding_counts.items())),
        "positive_compositions_per_color": len(all_compositions),
        "each_composition_once_per_color": True,
        "total_double_mass": str(total_mass),
        "total_separated_quarter_mass": str(sum(by_cell.values(), Fraction(0))),
        "factor_two_arbitrary_function_verified": True,
        "all_cell_weights_verified": True,
        "fixed_cells": fixed_cells,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    required = {
        "report.md": "1d8d6061aff3c9dc3f7811dbe15be4deb9c17c0e29ada6fb27fa6e9125ee8d2f",
        "boundary_condensate_reduction.md": "ee0092cbf553a4ed317d409f7c99fbd8850a23ebcc12bd3f836aec4a0821850a",
        "boundary_condensate_check.py": "99262179be2586618165cfcf1ca605d8d18eb6387b728609d5299b4b8fcaadcf",
        "boundary_condensate_results.json": "65104f7890dd6c9f37f73cff256a84d7491b820c1799817084c0f86d5e0d1438",
        "freeze_manifest.md": "3861fb6894e48b7c3481a38164e7d939434ef706469267230e847e7ce5a87e24",
        "SHA256SUMS": "d85240d4a643ae217386403f737eee62f85fe313c97b511da79f6e4993b56383",
    }
    observed = {name: sha256(M155 / name) for name in required}
    assert observed == required

    payload = {
        "status": "independent_exact_colored_orbit_audit",
        "target": "M73 nonlazy cyclic rank-two quotient; balanced family context only",
        "convention": "(pq)(x)=p(q(x)); tuple factors multiply left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": " ".join(sys.argv),
        "frozen_m155_hashes": observed,
        "audits": [audit_n(9), audit_n(15)],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["audits"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
