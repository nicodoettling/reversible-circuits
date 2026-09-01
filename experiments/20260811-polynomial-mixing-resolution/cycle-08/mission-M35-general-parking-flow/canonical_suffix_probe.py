#!/usr/bin/env python3
"""Falsify suffix witness lemmas for canonical borrow--move--return routes.

For each right adjacent ideal macro edge i -> i+1, choose h as the deepest
branching ancestor visible at the preorder cut after vertex i.  The proposed
proof uses parking words ending h,h,i for the buffer edges, and either
i,i,i+1 or i,i for the central edge.  This script tests every such word.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict
from pathlib import Path

import adjacent_bypass_probe as base


Macro = tuple[int, ...]


def counts(macro: Macro) -> tuple[int, ...]:
    return tuple(macro.count(i) for i in range(len(macro)))


def macro(vector: tuple[int, ...]) -> Macro:
    return tuple(i for i, multiplicity in enumerate(vector) for _ in range(multiplicity))


def change(vector: tuple[int, ...], source: int, target: int) -> tuple[int, ...]:
    answer = list(vector)
    answer[source] -= 1
    answer[target] += 1
    return tuple(answer)


def canonical_h(vector: tuple[int, ...], i: int) -> int:
    if i == 0:
        return 0
    stack: list[list[int]] = [[0, vector[0]]]
    for vertex in range(1, i + 1):
        while stack and stack[-1][1] == 0:
            stack.pop()
        if not stack:
            raise AssertionError("invalid preorder stack")
        stack[-1][1] -= 1
        stack.append([vertex, vector[vertex]])
    while stack and stack[-1][1] == 0:
        stack.pop()
    for index in range(len(stack) - 1, -1, -1):
        threshold = 2 if index == len(stack) - 1 else 1
        if stack[index][1] >= threshold:
            return stack[index][0]
    raise AssertionError("adjacent feasibility should leave a branching ancestor")


def run(n: int) -> dict:
    r = n - 1
    edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
    edge_index = {edge: i for i, edge in enumerate(edges)}
    perms = [base.transposition(n, edge) for edge in edges]
    fibers = defaultdict(list)
    for first, p in enumerate(perms):
        for second, q in enumerate(perms):
            fibers[base.compose(p, q)].append((first, second))

    macro_words = defaultdict(list)
    for labels in itertools.product(range(r), repeat=r):
        if base.is_parking_word(labels):
            macro_words[tuple(sorted(labels))].append(labels)

    def has_target(labels: tuple[int, ...], pos: int, target: Macro) -> bool:
        word_edges = base.factor_word(base.inverse_chain(labels))
        word = tuple(edge_index[edge] for edge in word_edges)
        product = base.compose(perms[word[pos]], perms[word[pos + 1]])
        favorable = 0
        for first, second in fibers[product]:
            target_word = word[:pos] + (first, second) + word[pos + 2 :]
            actual = tuple(sorted(edges[index][0] for index in target_word))
            favorable += actual == target
        return favorable == 2

    tests = defaultdict(int)
    failures = []
    for x, words in macro_words.items():
        vx = counts(x)
        for i in range(r - 1):
            if vx[i] == 0:
                continue
            vy = change(vx, i, i + 1)
            y = macro(vy)
            if y not in macro_words:
                continue
            h = canonical_h(vx, i)
            vz = change(vx, h, i)
            vw = change(vz, i, i + 1)
            z, w = macro(vz), macro(vw)

            checks: list[tuple[str, Macro, Macro, tuple[int, ...], int]] = []
            if x != z:
                checks.append(("first_hhi", x, z, (h, h, i), r - 3))
            if z != w:
                if vz[i + 1] > 0:
                    checks.append(("middle_ii_next", z, w, (i, i, i + 1), r - 3))
                else:
                    checks.append(("middle_ii", z, w, (i, i), r - 2))
            if y != w:
                if vy[i] > 0:
                    checks.append(("third_hhi", y, w, (h, h, i), r - 3))
                else:
                    checks.append(("third_hh", y, w, (h, h), r - 2))

            for kind, source, target, suffix, pos in checks:
                candidates = [labels for labels in macro_words[source] if labels[-len(suffix) :] == suffix]
                if not candidates:
                    failures.append(
                        {
                            "kind": kind,
                            "reason": "empty suffix family",
                            "x": list(x),
                            "source": list(source),
                            "target": list(target),
                            "i": i,
                            "h": h,
                            "suffix": list(suffix),
                        }
                    )
                    continue
                for labels in candidates:
                    tests[kind] += 1
                    if not has_target(labels, pos, target):
                        failures.append(
                            {
                                "kind": kind,
                                "reason": "suffix word is not a two-outcome witness",
                                "x": list(x),
                                "source": list(source),
                                "target": list(target),
                                "i": i,
                                "h": h,
                                "suffix": list(suffix),
                                "labels": list(labels),
                            }
                        )
                        if len(failures) >= 30:
                            return _result(n, tests, failures)
    return _result(n, tests, failures)


def _result(n: int, tests: dict[str, int], failures: list[dict]) -> dict:
    return {
        "n": n,
        "r": n - 1,
        "claim_tested": (
            "Canonical borrow-route edges contain the stated suffix witness "
            "families, which have inverse-cubic orbit fraction."
        ),
        "universal_scope_warning": "Finite enumeration is a falsifier only.",
        "tests_by_kind": dict(tests),
        "failures": failures,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.n)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
