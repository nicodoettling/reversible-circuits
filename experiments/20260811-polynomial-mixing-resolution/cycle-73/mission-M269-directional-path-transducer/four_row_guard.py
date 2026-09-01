#!/usr/bin/env python3
"""Four predeclared symbolic guards for M269's analytic interval theorem.

This is not a rank or tree census.  The universal statements are the interval
and gadget inductions in directional_lens_transducer.md.
"""

from __future__ import annotations

import json
import platform
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "four_row_guard_results.json"
M = 28
V = 7


def side(name: str) -> tuple:
    return ("S", name)


def white(vertex: int, position: int) -> tuple:
    return ("W", vertex, position % M)


def black(vertex: int, position: int) -> tuple:
    return ("B", vertex, position % M)


def up(start: int, stop: int) -> list[int]:
    out: list[int] = []
    j = (start + 1) % M
    while j != stop:
        out.append(j)
        j = (j + 1) % M
    return out


def down(start: int, stop: int) -> list[int]:
    out: list[int] = []
    j = (start - 1) % M
    while j != stop:
        out.append(j)
        j = (j - 1) % M
    return out


def canonical_pruned(vertex: int, t: int) -> list[tuple]:
    return [
        side(f"L{vertex}"),
        white(vertex, t),
        side(f"mid-{vertex}"),
        side(f"R{vertex}"),
    ]


def edited_base(direct: dict[int, int]) -> list[tuple]:
    word: list[tuple] = [
        *(black(V, j) for j in down(M - 1, 0)),
        side("Rv-enter"),
    ]
    previous = 0
    for t, vertex in sorted(direct.items()):
        word.extend(white(V, j) for j in up(previous, t))
        word.append(side(f"cross-{vertex}"))
        word.extend(canonical_pruned(vertex, t))
        previous = t
    word.extend(white(V, j) for j in up(previous, 0))
    word.extend([side("Rv-return"), side("Lv-return")])
    return word


def cp2(
    parent: int,
    s: int,
    path_q: int,
    path_word: list[tuple],
    siblings: dict[int, int],
) -> list[tuple]:
    children = [(path_q, path_word)] + [
        (t, canonical_pruned(vertex, t)) for t, vertex in siblings.items()
    ]
    children.sort(key=lambda item: (item[0] - (s - 1)) % M)
    word: list[tuple] = [side(f"L{parent}-enter")]
    previous = s - 1
    for q, child_word in children:
        word.extend(white(parent, j) for j in up(previous, q))
        word.append(side(f"cross-q{q}"))
        word.extend(child_word)
        previous = q
    word.extend(white(parent, j) for j in up(previous, s - 1))
    word.append(side(f"L{parent}-return"))
    word.extend(black(parent, j) for j in down(s - 1, s))
    word.append(side(f"R{parent}-return"))
    return word


def aggregate(r: int, direct: dict[int, int]) -> list[tuple]:
    out: list[tuple] = []
    j = 1
    while j <= r:
        t = j + 1
        if t in direct and t < r:
            vertex = direct[t]
            out.append(white(V, j))
            out.append(side(f"cross-{vertex}"))
            out.extend(canonical_pruned(vertex, t))
            j += 2
        else:
            out.append(white(V, j))
            j += 1
    return out


def lens(r: int, direct: dict[int, int]) -> list[tuple]:
    return [
        side(f"q{r-1}-enter"),
        side("left-chain"),
        *(black(V, j) for j in range(r - 1, 0, -1)),
        side("Rv"),
        *aggregate(r, direct),
        side("right-chain"),
        side(f"q{r}-return"),
    ]


def canonical(vertex: int, s: int) -> list[tuple]:
    return [
        side(f"L{vertex}"),
        white(vertex, s),
        side("canonical-mid"),
        side(f"R{vertex}"),
    ]


def reduce_complete(word: list[tuple]) -> tuple[list[tuple], list[dict]]:
    word = list(word)
    rows: list[dict] = []
    while True:
        halves = [i for i, token in enumerate(word) if token[0] != "S"]
        chosen: tuple[int, int] | None = None
        for left, right in zip(halves, halves[1:]):
            if word[left][0] == "W" and word[right][0] == "B":
                chosen = (left, right)
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
                "position": w_token[2],
                "white": w_token[1],
                "black": b_token[1],
                "distance": distance,
            }
        )
        word[left : right + 1] = [side(f"close-{w_token[2]}")]


def normalize(word: list[tuple]) -> list:
    return ["S" if token[0] == "S" else list(token) for token in word]


def distance_three(rows: list[dict]) -> list[dict]:
    return sorted(
        (row for row in rows if row["distance"] == 3),
        key=lambda row: (row["position"], row["white"], row["black"]),
    )


def run_row(
    name: str,
    raw: list[tuple],
    expected: list[tuple],
    expected_three: list[tuple[int, int]],
) -> dict:
    residual, rows = reduce_complete(raw)
    got_three = [(row["position"], row["black"]) for row in distance_three(rows)]
    want_three = sorted(expected_three)
    assert normalize(residual) == normalize(expected)
    assert got_three == want_three
    return {
        "name": name,
        "residual": normalize(residual),
        "distance_three": distance_three(rows),
        "row_count": len(rows),
        "holds": True,
    }


def main() -> None:
    # Row 1: initialization.  Direct port t=4 persists, t=20 is discharged.
    # Parent siblings t=24 and t=6 exercise the pre-path and post-wrap arms.
    direct_init = {4: 8, 20: 3}
    init = run_row(
        "initialization_with_ports_and_postwrap_siblings",
        cp2(13, 14, M - 1, edited_base(direct_init), {24: 5, 6: 9}),
        lens(14, {4: 8}),
        [
            (M - 1, 13),
            (19, 13), (20, 13),
            (23, V), (24, V),
            (5, 13), (6, 13),
        ],
    )

    # Row 2: width 22 contracts to 14.  Port t=4 persists and t=18 closes.
    contraction = run_row(
        "contraction_with_ports_and_both_sibling_arms",
        cp2(13, 14, 22, lens(22, {4: 8, 18: 2}), {20: 3, 6: 9, 26: 6}),
        lens(14, {4: 8}),
        [
            (21, V), (22, 13),
            (17, 13), (18, 13),
            (19, V), (20, V),
            (5, 13), (6, 13),
            (25, 13), (26, 13),
        ],
    )

    # Row 3: width 8 expands to 14 and seals.  The sole port is discharged.
    expansion = run_row(
        "expansion_with_port_and_postwrap_siblings",
        cp2(13, 14, 8, lens(8, {4: 8}), {6: 9, 12: 12, 20: 3}),
        canonical(13, 14),
        [
            (7, V), (8, 13), (0, 13),
            (3, 13), (4, 13),
            (5, V), (6, V),
            (11, 13), (12, 13),
            (19, 13), (20, 13),
        ],
    )

    # Row 4: a canonical input stays canonical in the same sibling geometry.
    sealed = run_row(
        "sealed_propagation_with_postwrap_siblings",
        cp2(13, 14, 8, canonical(10, 8), {6: 9, 12: 12, 20: 3}),
        canonical(13, 14),
        [
            (7, 13), (8, 13),
            (5, 13), (6, 13),
            (11, 13), (12, 13),
            (19, 13), (20, 13),
        ],
    )

    result = {
        "mission": "M269 directional-lens four-row symbolic guard",
        "status": "finite guard only; universal proof is analytic",
        "rank_census": False,
        "tree_census": False,
        "predeclared_rows": 4,
        "modulus": M,
        "edited_vertex": V,
        "rows": [init, contraction, expansion, sealed],
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

