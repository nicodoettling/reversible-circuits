#!/usr/bin/env python3
"""Export the exact single-Q5 action and named targets for Magma.

Completeness is certified by the rooted-DPS cardinality
5^(5-2)*8!/5!/5 = 8400 and an orbit of that exact size.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from array import array
from collections import deque
from pathlib import Path

import exact_classifier as core


SYMBOLS = tuple(range(1, 8)) + tuple(range(-1, -8, -1))


def enumerate_q5_orbit():
    start = core.sources()[0]
    seen = {start}
    queue = deque([start])
    while queue:
        word = queue.popleft()
        for symbol in SYMBOLS:
            nxt = core.canonical_word(core.hurwitz(word, symbol))
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    states = tuple(sorted(seen))
    physical_count = 5 ** (5 - 3) * math.factorial(8)
    expected_q5 = physical_count // math.factorial(5)
    assert len(states) == expected_q5 == 8400
    return states, {word: i for i, word in enumerate(states)}, physical_count


def magma_sequence(values):
    return "[" + ",".join(str(value) for value in values) + "]"


def write_magma(path: Path, action_rows, source_ids, target_rows):
    n = len(action_rows[0])
    lines = [
        "SetSeed(191);",
        f"n := {n};",
        "S := Sym(n);",
        "gens := [",
    ]
    for row_number, action in enumerate(action_rows):
        suffix = "," if row_number + 1 < len(action_rows) else ""
        lines.append("S!" + magma_sequence(value + 1 for value in action) + suffix)
    lines.extend([
        "];",
        "G := sub<S | gens>;",
        f"v := {source_ids[0] + 1};",
        f"u := {source_ids[1] + 1};",
        "H := Stabilizer(G, v);",
        "orb := Orbit(H, u);",
        "W, phi := WordGroup(G);",
        "F := FreeGroup(#gens);",
        "function WordSequence(g)",
        "    slp := g @@ phi;",
        "    fw := Evaluate(slp, [F.i : i in [1..#gens]]);",
        "    return Eltseq(fw);",
        "end function;",
        'out := Open("magma_results.txt", "w");',
        'fprintf out, "ORBIT %o\\n", #orb;',
        'fprintf out, "HGENS %o\\n", Ngens(H);',
        "for j in [1..Ngens(H)] do",
        '    fprintf out, "HGEN %o %o\\n", j, WordSequence(H.j);',
        "end for;",
        'fprintf out, "ORBITSET %o\\n", Sort(Setseq(orb));',
    ])
    for row in target_rows:
        target_id = row["target_id"]
        tv, tu = (value + 1 for value in row["target_ids"])
        lines.extend([
            f"tv := {tv}; tu := {tu};",
            "ok_a, a := IsConjugate(G, v, tv);",
            "assert ok_a;",
            "adjusted := tu^(a^-1);",
            "reachable := adjusted in orb;",
            f'fprintf out, "TARGET {target_id} %o %o\\n", reachable, adjusted;',
            "if reachable then",
            "    ok_h, h := IsConjugate(H, u, adjusted);",
            "    assert ok_h;",
            "    route := h*a;",
            "    assert v^route eq tv and u^route eq tu;",
            f'    fprintf out, "ROUTE {target_id} %o\\n", WordSequence(route);',
            "end if;",
        ])
    lines.extend([
        "delete out;",
        'print "M191_MAGMA_COMPLETE", #orb, Ngens(H);',
        "quit;",
    ])
    path.write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=Path("q5_action.json"))
    parser.add_argument("--magma", type=Path, default=Path("classify_q5.m"))
    args = parser.parse_args()

    states, index, physical_count = enumerate_q5_orbit()
    action_rows = []
    for symbol in SYMBOLS:
        action = array("H", (
            index[core.canonical_word(core.hurwitz(word, symbol))]
            for word in states
        ))
        assert len(set(action)) == len(states)
        action_rows.append(action)
    for slot in range(7):
        plus = action_rows[slot]
        minus = action_rows[7 + slot]
        assert all(minus[plus[i]] == i and plus[minus[i]] == i for i in range(len(states)))

    occurrences, descriptor_rows = core.named_targets()
    target_rows = []
    for target_id, (target, rows) in enumerate(sorted(occurrences.items())):
        target_rows.append({
            "target_id": target_id,
            "target_ids": [index[target[0]], index[target[1]]],
            "occurrences": sorted(rows, key=lambda row: (row["edit"], row["roots"])),
        })
    source_ids = [index[word] for word in core.sources()]
    action_digest = hashlib.sha256(
        b"".join(action.tobytes() for action in action_rows)
    ).hexdigest()
    data = {
        "q5_size": len(states),
        "physical_z5_count": physical_count,
        "completeness_certificate": "orbit size equals rooted-DPS quotient count",
        "symbols": list(SYMBOLS),
        "source_ids": source_ids,
        "action_sha256": action_digest,
        "action_rows": [list(action) for action in action_rows],
        "target_rows": target_rows,
        "rooted_descriptors": descriptor_rows,
    }
    args.json.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    write_magma(args.magma, action_rows, source_ids, target_rows)
    print(json.dumps({
        "q5_size": len(states),
        "physical_z5_count": physical_count,
        "source_ids": source_ids,
        "target_count": len(target_rows),
        "action_sha256": action_digest,
        "magma_script": str(args.magma),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
