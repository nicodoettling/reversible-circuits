#!/usr/bin/env python3
"""Minimal literal replay of the M262 rank-8/rank-9 CPR obstruction.

The universal result is proved by the interval induction in
cyclic_path_row_refutation.md.  This script is only a deterministic
falsification guard for the old/new rank pair; it performs no tree or rank
census.
"""

from __future__ import annotations

import json
import platform
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "literal_row_results.json"


def up(modulus: int, start: int, stop: int) -> list[int]:
    out: list[int] = []
    value = start % modulus + 1
    while value != stop:
        out.append(value)
        value = value % modulus + 1
    return out


def down(modulus: int, start: int, stop: int) -> list[int]:
    out: list[int] = []
    value = (start + modulus - 2) % modulus + 1
    while value != stop:
        out.append(value)
        value = (value + modulus - 2) % modulus + 1
    return out


def side(name: str) -> tuple[str, str]:
    return ("S", name)


def white(vertex: int, label: int) -> tuple[str, int, int]:
    return ("W", vertex, label)


def black(vertex: int, label: int) -> tuple[str, int, int]:
    return ("B", vertex, label)


def edited_base(modulus: int) -> list[tuple]:
    # v=4, L_v=5, R_v=6, and v has no child.
    return [
        *(black(4, q) for q in down(modulus, 5, 6)),
        side("R4"),
        *(white(4, q) for q in up(modulus, 6, 6)),
        side("R4-return"),
        side("L4-return"),
    ]


def parent_six_context(modulus: int) -> list[tuple]:
    # a=6, L_a=9, R_a=10, and kappa(v)=L_v=5.
    return [
        side("L6-enter"),
        *(white(6, q) for q in up(modulus, 9, 5)),
        side("child-5-enter"),
        *edited_base(modulus),
        *(white(6, q) for q in up(modulus, 5, 9)),
        side("L6-return"),
        *(black(6, q) for q in down(modulus, 9, 10)),
        side("R6-return"),
    ]


def reduce_complete(word: list[tuple]) -> tuple[list[tuple], list[dict]]:
    word = list(word)
    rows: list[dict] = []
    while True:
        halves = [i for i, token in enumerate(word) if token[0] != "S"]
        chosen: tuple[int, int] | None = None
        for left, right in zip(halves, halves[1:]):
            if word[left][0] == "W" and word[right][0] == "B":
                chosen = left, right
                break
        if chosen is None:
            return word, rows
        left, right = chosen
        w_token, b_token = word[left], word[right]
        assert w_token[2] == b_token[2]
        interior = word[left + 1 : right]
        assert all(token[0] == "S" for token in interior)
        distance = len(interior)
        assert distance in {1, 3}
        rows.append(
            {
                "label": w_token[2],
                "white": w_token[1],
                "black": b_token[1],
                "distance": distance,
            }
        )
        word[left : right + 1] = [side(f"closure-{w_token[2]}")]


def normalized(word: list[tuple]) -> list[list | str]:
    out: list[list | str] = []
    for token in word:
        if token[0] == "S":
            out.append("S")
        else:
            out.append([token[0], token[1], token[2]])
    return out


def check_rank(rank: int) -> dict:
    modulus = 2 * rank - 2
    residual, rows = reduce_complete(parent_six_context(modulus))
    expected = [
        "S",
        "S",
        ["B", 4, 9],
        ["B", 4, 8],
        ["B", 4, 7],
        "S",
        ["W", 4, 7],
        ["W", 4, 8],
        ["W", 4, 9],
        ["W", 4, 10],
        "S",
        "S",
    ]
    label_six = [row for row in rows if row["label"] == 6]
    assert normalized(residual) == expected
    assert label_six == [
        {"label": 6, "white": 6, "black": 6, "distance": 1}
    ]
    return {
        "rank": rank,
        "modulus": modulus,
        "residual": normalized(residual),
        "label_six_rows": label_six,
        "all_rows": rows,
    }


def main() -> None:
    checks = [check_rank(8), check_rank(9)]
    result = {
        "mission": "M262 literal CPR row falsification guard",
        "status": "exact two-rank replay only; universal proof is analytic",
        "rank_census": False,
        "tree_census": False,
        "checks": checks,
        "holds": True,
        "environment": {
            "python": platform.python_version(),
            "nonstandard_dependencies": {},
            "seed": None,
        },
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
