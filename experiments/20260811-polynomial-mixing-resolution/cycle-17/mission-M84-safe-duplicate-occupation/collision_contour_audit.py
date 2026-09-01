#!/usr/bin/env python3
"""Exact collision-contour diagnostics for the W_L voltage family.

For a selected set S and unselected labels i<j, duplicate equality is

    t_i = h t_j h^{-1},

where h is the chronological product of selected factors strictly between i
and j.  Tracking the two endpoints of t_j through h produces two paths; with
t_i and t_j they form a closed collision contour.  This script computes its
integer voltage/homology and compares it with exact deletion connectivity.
"""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
from pathlib import Path


sys.dont_write_bytecode = True

BASE_WORD = (
    (3, 5), (3, 4), (1, 5), (2, 5),
    (1, 6), (0, 4), (3, 7), (2, 7),
    (0, 5), (3, 6), (1, 4), (1, 7),
    (0, 6), (2, 4), (2, 6), (0, 7),
)
VX = (-1, -1, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
VY = (-1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)


def lifted_word(L: int):
    def label(vertex: int, x: int, y: int) -> int:
        return (vertex * L + x) * L + y

    word = []
    metadata = []
    for base_index, ((a, b), dx, dy) in enumerate(zip(BASE_WORD, VX, VY)):
        for x in range(L):
            for y in range(L):
                word.append(tuple(sorted((
                    label(a, x, y),
                    label(b, (x + dx) % L, (y + dy) % L),
                ))))
                metadata.append((base_index, x, y))
    return tuple(word), tuple(metadata)


def move_token(position: int, edge: tuple[int, int]) -> int:
    a, b = edge
    return b if position == a else a if position == b else position


def directed_voltage(
    start: int,
    end: int,
    label: int,
    metadata: tuple[tuple[int, int, int], ...],
    L: int,
) -> tuple[int, int]:
    base_index, _x, _y = metadata[label]
    low, high = BASE_WORD[base_index]
    start_base = start // (L * L)
    end_base = end // (L * L)
    assert {start_base, end_base} == {low, high}
    sign = 1 if start_base == low else -1
    return sign * VX[base_index], sign * VY[base_index]


def add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]


def negate(a: tuple[int, int]) -> tuple[int, int]:
    return -a[0], -a[1]


def endpoint_path(
    start: int,
    between_labels: tuple[int, ...],
    word: tuple[tuple[int, int], ...],
    metadata: tuple[tuple[int, int, int], ...],
    L: int,
):
    position = start
    voltage = (0, 0)
    traversed = []
    # h=t_1...t_r acts as swaps in reverse chronological order.
    for label in reversed(between_labels):
        edge = word[label]
        new_position = move_token(position, edge)
        if new_position != position:
            voltage = add(
                voltage,
                directed_voltage(position, new_position, label, metadata, L),
            )
            traversed.append((label, position, new_position))
        position = new_position
    return position, voltage, tuple(traversed)


def contour_record(L: int, selected_prefix: tuple[int, ...], pair: tuple[int, int]):
    word, metadata = lifted_word(L)
    selected = frozenset(selected_prefix)
    i, j = sorted(pair)
    assert i not in selected and j not in selected
    between = tuple(label for label in range(i + 1, j) if label in selected)
    c, d = word[j]
    end_c, voltage_c, path_c = endpoint_path(c, between, word, metadata, L)
    end_d, voltage_d, path_d = endpoint_path(d, between, word, metadata, L)
    duplicate = {end_c, end_d} == set(word[i])
    if not duplicate:
        return {
            "L": L,
            "pair": [i, j],
            "selected_count": len(selected),
            "between_count": len(between),
            "duplicate": False,
        }
    # Close c -> end_c -> end_d -> d -> c.  The middle and last traversals
    # use the actual lifted edges i and j.
    vi = directed_voltage(end_c, end_d, i, metadata, L)
    vj = directed_voltage(d, c, j, metadata, L)
    contour_voltage = add(add(add(voltage_c, vi), negate(voltage_d)), vj)
    assert contour_voltage[0] % L == 0 and contour_voltage[1] % L == 0
    return {
        "L": L,
        "pair": [i, j],
        "selected_count": len(selected),
        "between_count": len(between),
        "between_labels": list(between),
        "duplicate": True,
        "endpoint_matching": [[c, end_c], [d, end_d]],
        "path_voltages": [list(voltage_c), list(voltage_d)],
        "contour_integer_voltage": list(contour_voltage),
        "contour_homology": [contour_voltage[0] // L, contour_voltage[1] // L],
        "path_lengths": [len(path_c), len(path_d)],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    examples = [
        {
            "name": "W2-isolates-one",
            "L": 2,
            "order": [
                22, 38, 58, 18, 40, 13, 61, 28, 11, 46, 49, 26, 4,
                45, 34, 19, 35, 33, 15, 52, 0, 39, 31, 48, 37, 44, 9,
                27, 56, 7, 20, 55, 23, 14, 47, 36, 62, 3, 32,
            ],
        },
        {
            "name": "W2-isolates-two",
            "L": 2,
            "order": [
                27, 43, 54, 56, 0, 13, 25, 11, 38, 40, 17, 35, 49,
                61, 39, 24, 30, 12, 8, 46, 2, 58,
            ],
        },
        {
            "name": "base-tail-safe",
            "L": 1,
            "selected": [label for label in range(16) if label not in (0, 1, 2, 7)],
            "pair": [0, 7],
        },
    ]
    records = []
    for example in examples:
        if "order" in example:
            selected = tuple(example["order"][:-2])
            pair = tuple(example["order"][-2:])
        else:
            selected = tuple(example["selected"])
            pair = tuple(example["pair"])
        row = contour_record(example["L"], selected, pair)
        row["name"] = example["name"]
        records.append(row)
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "argv": sys.argv,
        "commit": commit,
        "python": platform.python_version(),
        "seed": None,
        "nonstandard_dependencies": {},
        "scope_warning": (
            "These are exact diagnostics for named witnesses. A homology "
            "pattern here is not an all-state theorem."
        ),
        "records": records,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(records, sort_keys=True))


if __name__ == "__main__":
    main()
