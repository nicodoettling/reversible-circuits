#!/usr/bin/env python3
"""Exact falsifier for boundary/contiguous duplicate-block witness lemmas.

For every edge in the canonical borrow--move--return route, orient the edge
from its macro with duplicate lower label a toward the macro replacing a by
b>a.  Test whether fixing the two a coordinates at the prefix, suffix, or
some fixed adjacent physical position makes every compatible parking word a
favorable rank-two witness for that target.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from collections import defaultdict
from pathlib import Path

import adjacent_bypass_probe as base
from canonical_suffix_probe import canonical_h, change, counts, macro


Macro = tuple[int, ...]


def orbit_weight(source: Macro) -> int:
    answer = math.factorial(len(source))
    for value in set(source):
        answer //= math.factorial(source.count(value))
    return answer


def run(n: int) -> dict:
    r = n - 1
    edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
    edge_index = {edge: index for index, edge in enumerate(edges)}
    perms = [base.transposition(n, edge) for edge in edges]
    fibers = defaultdict(list)
    for first, p in enumerate(perms):
        for second, q in enumerate(perms):
            fibers[base.compose(p, q)].append((first, second))

    macro_words = defaultdict(list)
    word_data = {}
    for labels in itertools.product(range(r), repeat=r):
        if not base.is_parking_word(labels):
            continue
        source = tuple(sorted(labels))
        macro_words[source].append(labels)
        word_edges = base.factor_word(base.inverse_chain(labels))
        word_data[labels] = tuple(edge_index[edge] for edge in word_edges)

    def favorable(labels: tuple[int, ...], pos: int, target: Macro) -> bool:
        word = word_data[labels]
        product = base.compose(perms[word[pos]], perms[word[pos + 1]])
        count = 0
        for first, second in fibers[product]:
            target_word = word[:pos] + (first, second) + word[pos + 2 :]
            actual = tuple(sorted(edges[index][0] for index in target_word))
            count += actual == target
        return count == 2

    records = []
    seen = set()
    for x in sorted(macro_words):
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
            oriented = []
            if x != z:
                oriented.append(("first", x, z, h, i))
            if z != w:
                oriented.append(("middle", z, w, i, i + 1))
            if y != w:
                oriented.append(("third-reversed", y, w, h, i))
            for stage, source, target, duplicate, raised in oriented:
                key = (source, target, duplicate, raised)
                if key in seen:
                    continue
                seen.add(key)
                position_rows = []
                for pos in range(r - 1):
                    candidates = [
                        labels
                        for labels in macro_words[source]
                        if labels[pos] == labels[pos + 1] == duplicate
                    ]
                    bad = [labels for labels in candidates if not favorable(labels, pos, target)]
                    position_rows.append(
                        {
                            "position": pos,
                            "candidates": len(candidates),
                            "all_favorable": bool(candidates) and not bad,
                            "first_bad": list(bad[0]) if bad else None,
                            "orbit_fraction": (
                                f"{len(candidates)}/{orbit_weight(source)}"
                                if candidates
                                else "0"
                            ),
                        }
                    )
                good_blocks = []
                for block_length in range(3, min(5, r) + 1):
                    for pos in range(r - 1):
                        for start in range(
                            max(0, pos - block_length + 2),
                            min(pos, r - block_length) + 1,
                        ):
                            grouped = defaultdict(list)
                            for labels in macro_words[source]:
                                if labels[pos] != duplicate or labels[pos + 1] != duplicate:
                                    continue
                                pattern = labels[start : start + block_length]
                                grouped[pattern].append(labels)
                            for pattern, candidates in grouped.items():
                                if all(favorable(labels, pos, target) for labels in candidates):
                                    good_blocks.append(
                                        {
                                            "block_length": block_length,
                                            "block_start": start,
                                            "pair_position": pos,
                                            "pattern": list(pattern),
                                            "candidates": len(candidates),
                                            "orbit_fraction": (
                                                f"{len(candidates)}/{orbit_weight(source)}"
                                            ),
                                        }
                                    )
                good_positions = [
                    row["position"] for row in position_rows if row["all_favorable"]
                ]
                records.append(
                    {
                        "stage_first_seen": stage,
                        "source": list(source),
                        "target": list(target),
                        "duplicate": duplicate,
                        "raised": raised,
                        "orbit": orbit_weight(source),
                        "prefix_all_favorable": 0 in good_positions,
                        "suffix_all_favorable": r - 2 in good_positions,
                        "good_fixed_pair_positions": good_positions,
                        "minimum_good_block_length": (
                            min(row["block_length"] for row in good_blocks)
                            if good_blocks
                            else None
                        ),
                        "best_good_block": max(
                            good_blocks, key=lambda row: row["candidates"], default=None
                        ),
                        "positions": position_rows,
                    }
                )

    boundary_failures = [
        row
        for row in records
        if not row["prefix_all_favorable"] and not row["suffix_all_favorable"]
    ]
    no_fixed_pair_position = [row for row in records if not row["good_fixed_pair_positions"]]
    return {
        "n": n,
        "r": r,
        "claim_tested": (
            "Every canonical borrow-route edge has a prefix or suffix duplicate "
            "pair for which all compatible parking words are favorable."
        ),
        "universal_scope_warning": "Finite enumeration is a falsifier only.",
        "distinct_oriented_route_edges": len(records),
        "boundary_failures": boundary_failures,
        "no_fixed_pair_position": no_fixed_pair_position,
        "records": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.n)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "n": result["n"],
                "r": result["r"],
                "distinct_oriented_route_edges": result["distinct_oriented_route_edges"],
                "boundary_failure_count": len(result["boundary_failures"]),
                "no_fixed_pair_position_count": len(result["no_fixed_pair_position"]),
                "first_boundary_failure": result["boundary_failures"][:1],
                "first_no_fixed_pair_position": result["no_fixed_pair_position"][:1],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
