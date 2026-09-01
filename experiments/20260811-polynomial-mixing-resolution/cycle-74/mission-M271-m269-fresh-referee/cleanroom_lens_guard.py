#!/usr/bin/env python3
"""Clean-room finite guards for M269's decorated-lens theorem.

The universal claim is audited analytically.  This script checks only the
four symbolic schemas declared by M269, with vertex names forced to agree
with their canonical slots, and the four rank-nine rows underlying the two
direction-insufficiency pairs.  It imports no predecessor code or data.
"""

from __future__ import annotations

import hashlib
import json
import platform
from collections import deque
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "cleanroom_lens_guard_results.json"


def S(name: str) -> tuple[str, str]:
    return ("S", name)


class RowModel:
    def __init__(self, rho: int, v: int) -> None:
        self.rho = rho
        self.M = 2 * rho - 2
        self.v = v
        self.Rv = 2 * v - 2

    def q(self, j: int) -> int:
        return 1 + ((self.Rv - 1 + j) % self.M)

    def pos(self, h: int) -> int:
        ans = ((2 * h - 2) - self.Rv) % self.M
        assert 1 <= ans <= self.M - 1
        assert ans % 2 == 0
        return ans

    def vertex_at(self, t: int) -> int:
        matches = [h for h in range(1, self.rho + 1) if h != self.v and self.pos(h) == t]
        assert len(matches) == 1
        return matches[0]

    def W(self, u: int, j: int) -> tuple[str, int, int]:
        return ("W", u, self.q(j))

    def B(self, u: int, j: int) -> tuple[str, int, int]:
        return ("B", u, self.q(j))

    def up(self, start: int, stop: int) -> list[int]:
        out: list[int] = []
        j = (start + 1) % self.M
        while j != stop:
            out.append(j)
            j = (j + 1) % self.M
        return out

    def down(self, start: int, stop: int) -> list[int]:
        out: list[int] = []
        j = (start - 1) % self.M
        while j != stop:
            out.append(j)
            j = (j - 1) % self.M
        return out

    def canonical_pruned(self, h: int) -> list[tuple]:
        t = self.pos(h)
        return [S(f"L{h}"), self.W(h, t), S(f"mid{h}"), S(f"R{h}")]

    def edited_base(self, direct: set[int]) -> list[tuple]:
        by_t = sorted((self.pos(h), h) for h in direct)
        word: list[tuple] = [
            *(self.B(self.v, j) for j in self.down(self.M - 1, 0)),
            S("Rv-enter"),
        ]
        previous = 0
        for t, h in by_t:
            word.extend(self.W(self.v, j) for j in self.up(previous, t))
            word.append(S(f"cross-{h}"))
            word.extend(self.canonical_pruned(h))
            previous = t
        word.extend(self.W(self.v, j) for j in self.up(previous, 0))
        word.extend([S("Rv-return"), S("Lv-return")])
        return word

    def cp2(
        self,
        parent: int,
        path_q_pos: int,
        path_word: list[tuple],
        siblings: set[int],
    ) -> list[tuple]:
        s = self.pos(parent)
        children = [(path_q_pos, path_word, "path")]
        children.extend((self.pos(h), self.canonical_pruned(h), str(h)) for h in siblings)
        children.sort(key=lambda item: (item[0] - (s - 1)) % self.M)
        word: list[tuple] = [S(f"L{parent}-enter")]
        previous = s - 1
        for qpos, child_word, tag in children:
            word.extend(self.W(parent, j) for j in self.up(previous, qpos))
            word.append(S(f"cross-{tag}"))
            word.extend(child_word)
            previous = qpos
        word.extend(self.W(parent, j) for j in self.up(previous, s - 1))
        word.append(S(f"L{parent}-return"))
        word.extend(self.B(parent, j) for j in self.down(s - 1, s))
        word.append(S(f"R{parent}-return"))
        return word

    def aggregate(self, r: int, direct: set[int]) -> list[tuple]:
        ports = {self.pos(h): h for h in direct if self.pos(h) < r}
        out: list[tuple] = []
        j = 1
        while j <= r:
            if j + 1 in ports:
                h = ports[j + 1]
                out.append(self.W(self.v, j))
                out.append(S(f"cross-{h}"))
                out.extend(self.canonical_pruned(h))
                j += 2
            else:
                out.append(self.W(self.v, j))
                j += 1
        return out

    def lens(self, r: int, direct: set[int]) -> list[tuple]:
        return [
            S(f"q{r - 1}-enter"),
            S("left-chain"),
            *(self.B(self.v, j) for j in range(r - 1, 0, -1)),
            S("Rv"),
            *self.aggregate(r, direct),
            S("right-chain"),
            S(f"q{r}-return"),
        ]

    def canonical(self, h: int) -> list[tuple]:
        t = self.pos(h)
        return [S(f"L{h}"), self.W(h, t), S("canonical-mid"), S(f"R{h}")]


def reduce_rightmost(word: list[tuple]) -> tuple[list[tuple], list[dict]]:
    """Delete the rightmost complete W--B node, unlike M269's leftmost scan."""
    word = list(word)
    rows: list[dict] = []
    while True:
        halves = [i for i, token in enumerate(word) if token[0] != "S"]
        chosen: tuple[int, int] | None = None
        for left, right in reversed(list(zip(halves, halves[1:]))):
            if word[left][0] == "W" and word[right][0] == "B":
                chosen = (left, right)
                break
        if chosen is None:
            return word, rows
        left, right = chosen
        w, b = word[left], word[right]
        assert w[2] == b[2]
        interior = word[left + 1 : right]
        assert all(token[0] == "S" for token in interior)
        assert len(interior) in {1, 3}
        rows.append(
            {
                "label": w[2],
                "white": w[1],
                "black": b[1],
                "distance": len(interior),
            }
        )
        word[left : right + 1] = [S(f"close-{w[2]}")]


def normalized(word: list[tuple]) -> list:
    return ["S" if token[0] == "S" else list(token) for token in word]


def d3_pairs(rows: list[dict]) -> list[tuple[int, int]]:
    return sorted((row["label"], row["black"]) for row in rows if row["distance"] == 3)


def run_schema(
    name: str,
    raw: list[tuple],
    expected: list[tuple],
    expected_d3: list[tuple[int, int]],
) -> dict:
    residual, rows = reduce_rightmost(raw)
    assert normalized(residual) == normalized(expected)
    assert d3_pairs(rows) == sorted(expected_d3)
    return {
        "name": name,
        "holds": True,
        "row_count": len(rows),
        "distance_three": [row for row in rows if row["distance"] == 3],
        "residual": normalized(residual),
    }


def actual_vertices(model: RowModel, positions: set[int]) -> set[int]:
    return {model.vertex_at(t) for t in positions}


def check_tree(rho: int, edges: set[tuple[int, int]], expected: dict[int, int]) -> None:
    assert len(edges) == rho - 1
    graph = {u: set() for u in range(1, rho + 1)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    assert len(graph[rho]) == 1
    parent = {rho: 0}
    queue = deque([rho])
    while queue:
        u = queue.popleft()
        for w in graph[u]:
            if w not in parent:
                parent[w] = u
                queue.append(w)
    assert len(parent) == rho
    for u, p in expected.items():
        assert parent[u] == p


def witness_edges(rho: int, v: int, a: int, b: int) -> set[tuple[int, int]]:
    core = {(1, rho), tuple(sorted((1, b))), tuple(sorted((b, a))), tuple(sorted((a, v)))}
    used = {v, a, b}
    core.update((1, u) for u in range(2, rho) if u not in used)
    return {tuple(sorted(edge)) for edge in core}


def main() -> None:
    model = RowModel(rho=15, v=7)
    q = model.q

    init_direct = actual_vertices(model, {4, 20})
    init_siblings = actual_vertices(model, {24, 6})
    parent = model.vertex_at(14)
    init = run_schema(
        "initialization_with_ports_and_postwrap_siblings",
        model.cp2(parent, model.M - 1, model.edited_base(init_direct), init_siblings),
        model.lens(14, actual_vertices(model, {4})),
        [
            (q(model.M - 1), parent),
            (q(19), parent), (q(20), parent),
            (q(23), model.v), (q(24), model.v),
            (q(5), parent), (q(6), parent),
        ],
    )

    contraction_direct = actual_vertices(model, {4, 18})
    contraction_siblings = actual_vertices(model, {20, 6, 26})
    child = model.vertex_at(22)
    contraction = run_schema(
        "contraction_with_ports_and_both_sibling_arms",
        model.cp2(parent, 22, model.lens(22, contraction_direct), contraction_siblings),
        model.lens(14, actual_vertices(model, {4})),
        [
            (q(21), model.v), (q(22), parent),
            (q(17), parent), (q(18), parent),
            (q(19), model.v), (q(20), model.v),
            (q(5), parent), (q(6), parent),
            (q(25), parent), (q(26), parent),
        ],
    )
    assert child == model.vertex_at(22)

    expansion_direct = actual_vertices(model, {4})
    expansion_siblings = actual_vertices(model, {6, 12, 20})
    expansion = run_schema(
        "expansion_with_port_and_postwrap_siblings",
        model.cp2(parent, 8, model.lens(8, expansion_direct), expansion_siblings),
        model.canonical(parent),
        [
            (q(7), model.v), (q(8), parent), (q(0), parent),
            (q(3), parent), (q(4), parent),
            (q(5), model.v), (q(6), model.v),
            (q(11), parent), (q(12), parent),
            (q(19), parent), (q(20), parent),
        ],
    )

    sealed_child = model.vertex_at(8)
    sealed = run_schema(
        "sealed_propagation_with_postwrap_siblings",
        model.cp2(parent, 8, model.canonical(sealed_child), expansion_siblings),
        model.canonical(parent),
        [
            (q(7), parent), (q(8), parent),
            (q(5), parent), (q(6), parent),
            (q(11), parent), (q(12), parent),
            (q(19), parent), (q(20), parent),
        ],
    )

    witnesses: list[dict] = []
    for sign, v, b, choices in [
        ("O+", 4, 6, (5, 7)),
        ("O-", 6, 3, (2, 4)),
    ]:
        outputs: list[str] = []
        for a in choices:
            wm = RowModel(rho=9, v=v)
            r, s = wm.pos(a), wm.pos(b)
            edges = witness_edges(9, v, a, b)
            check_tree(9, edges, {v: a, a: b, b: 1, 1: 9})
            raw = wm.cp2(b, r, wm.lens(r, set()), set())
            expected = wm.lens(s, set()) if s < r else wm.canonical(b)
            residual, rows = reduce_rightmost(raw)
            assert normalized(residual) == normalized(expected)
            output = "lens" if s < r else "sealed"
            outputs.append(output)
            witnesses.append(
                {
                    "sign": sign,
                    "v": v,
                    "a": a,
                    "b": b,
                    "r": r,
                    "s": s,
                    "output": output,
                    "tree_ok": True,
                    "row_ok": True,
                    "distance_three": [row for row in rows if row["distance"] == 3],
                }
            )
        assert outputs == ["sealed", "lens"]

    result = {
        "mission": "M271 clean-room finite decorated-lens guard",
        "status": "finite symbolic calibration only; universal claims audited analytically",
        "rank_census": False,
        "tree_census": False,
        "predecessor_imports": False,
        "slot_vertex_consistency": True,
        "declared_m269_schemas": [init, contraction, expansion, sealed],
        "direction_pair_rank9_guards": witnesses,
        "holds": True,
        "environment": {
            "python": platform.python_version(),
            "nonstandard_dependencies": {},
            "seed": None,
        },
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["normalized_digest"] = hashlib.sha256(canonical.encode()).hexdigest()
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
