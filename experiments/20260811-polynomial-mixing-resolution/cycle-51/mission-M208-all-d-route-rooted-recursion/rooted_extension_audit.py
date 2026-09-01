#!/usr/bin/env python3
"""Exact finite audit of M208's d5->d6 rooted correction certificates.

No route search and no quotient graph enumeration occur here.  The script
reconstructs the named rooted DPS endpoints, replays seven archived common
signed-Hurwitz words, and tests (only as a falsifier) whether those same words
extend to every d5 tree in the corresponding leaf-extension template.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
M205_CHECKER = (
    HERE.parent.parent / "cycle-49" / "mission-M205-m203-fresh-referee"
    / "fresh_locality_referee.py"
)


def load_frozen_m205():
    spec = importlib.util.spec_from_file_location("m205_core", M205_CHECKER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def conjugate(edge, by):
    x, y = by
    image = lambda z: y if z == x else x if z == y else z
    return tuple(sorted((image(edge[0]), image(edge[1]))))


def hurwitz(word, position, sign):
    """Apply R_(position+1)^sign; factors and actions are chronological."""
    a, b = word[position], word[position + 1]
    out = list(word)
    if sign == 1:
        out[position : position + 2] = (b, conjugate(a, b))
    else:
        out[position : position + 2] = (conjugate(b, a), a)
    return tuple(out)


def act(word, route):
    for position, sign in route:
        word = hurwitz(word, position, sign)
    return word


def serialize_word(word):
    return [list(edge) for edge in word]


def serialize_route(route):
    return [[position + 1, sign] for position, sign in route]


def digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


# Zero-based generator positions internally; the JSON uses one-based indices.
ROUTES = {
    1: (
        (1, 1), (2, 1), (3, -1), (4, -1),
        (5, -1), (6, 1), (7, -1), (6, -1), (5, -1),
        (4, 1), (3, 1), (2, -1), (1, -1),
    ),
    2: (),
    3: (
        (3, 1), (4, 1),
        (5, -1), (6, 1), (7, -1), (6, -1), (5, -1),
        (4, -1), (3, -1),
    ),
    4: (),
    5: ((5, -1), (6, 1), (7, -1), (6, -1), (5, -1)),
    6: ((4, -1), (4, -1)),
    7: ((7, -1),),
}


def main():
    core = load_frozen_m205()
    rows, descriptors = core.reconstruct_rows()

    pi5 = (7, 8, 1, 2, 3, 4, 5, 6)
    pi6 = (9, 10, 1, 2, 3, 4, 5, 6, 7, 8)
    expected_trees = {
        0: frozenset({(1, 2), (1, 3), (1, 5), (2, 4)}),
        1: frozenset({(1, 2), (1, 3), (1, 4), (1, 5)}),
    }

    # Verify the symbolic source-descriptor extension before endpoint replay.
    descriptor_rows = []
    for pattern in (0, 1):
        tree5, order5, _ = descriptors[5, pattern, 4]
        tree6, order6, _ = descriptors[6, pattern, 5]
        assert tree5 == expected_trees[pattern]
        assert order5 == pi5
        assert tree6 == frozenset(set(tree5) | {(1, 6)})
        assert order6 == pi6
        assert core.decode_dps(tree5, pi5, 5) == core.explicit_source(5, pattern)
        assert core.decode_dps(tree6, pi6, 6) == core.explicit_source(6, pattern)
        descriptor_rows.append({
            "pattern": pattern,
            "tree5": [list(edge) for edge in sorted(tree5)],
            "tree6": [list(edge) for edge in sorted(tree6)],
            "pi5": list(pi5),
            "pi6": list(pi6),
        })

    # Exact positive certificates for the two named M181 patterns.
    certificate_rows = []
    for edit in range(1, 8):
        per_pattern = []
        for pattern in (0, 1):
            tree5, _, _ = descriptors[5, pattern, 4]
            tree6, _, _ = descriptors[6, pattern, 5]
            target5 = core.decode_dps(
                tree5, core.adjacent_value_edit(pi5, edit), 5
            )
            naive = target5 + ((0, 5), (0, 5))
            actual = core.decode_dps(
                tree6, core.adjacent_value_edit(pi6, edit), 6
            )
            replay = act(naive, ROUTES[edit])
            assert replay == actual
            per_pattern.append({
                "pattern": pattern,
                "naive_target": serialize_word(naive),
                "actual_target": serialize_word(actual),
                "exact_replay": replay == actual,
            })
        certificate_rows.append({
            "edit": edit,
            "chronological_route": serialize_route(ROUTES[edit]),
            "route_length": len(ROUTES[edit]),
            "generator_support": sorted({position + 1 for position, _ in ROUTES[edit]}),
            "patterns": per_pattern,
        })

    # Falsification-only template audit.  These are all 16 Cayley trees on
    # [5] in which old root 5 is a leaf attached to vertex 1.  Applying known
    # routes is not a route search and cannot prove that failed rows have no
    # alternative correction word.
    template_trees = [
        tree for tree in core.rooted_trees(5)
        if (1, 5) in tree and sum(5 in edge for edge in tree) == 1
    ]
    assert len(template_trees) == 16
    failures = []
    failures_by_edit = Counter()
    for tree_index, tree5 in enumerate(template_trees):
        tree6 = frozenset(set(tree5) | {(1, 6)})
        for edit in range(1, 8):
            target5 = core.decode_dps(
                tree5, core.adjacent_value_edit(pi5, edit), 5
            )
            naive = target5 + ((0, 5), (0, 5))
            actual = core.decode_dps(
                tree6, core.adjacent_value_edit(pi6, edit), 6
            )
            replay = act(naive, ROUTES[edit])
            if replay != actual:
                failures_by_edit[edit] += 1
                failures.append({
                    "tree_index": tree_index,
                    "tree5": [list(edge) for edge in sorted(tree5)],
                    "edit": edit,
                    "naive_target": serialize_word(naive),
                    "actual_target": serialize_word(actual),
                    "route_output": serialize_word(replay),
                })

    assert failures
    payload = {
        "experiment": "M208 exact rooted d5-to-d6 extension audit",
        "scope": (
            "two named M181 patterns and all old edits 1..7; deterministic "
            "16-tree falsification audit; no Q6 enumeration"
        ),
        "conventions": {
            "action_order": "chronological, rows listed left to right",
            "route_generator_indices": "one-based in JSON",
            "right_hurwitz": "R_j(a,b)=(b,bab)",
            "inverse_hurwitz": "R_j^-1(a,b)=(aba,a)",
        },
        "descriptor_extension": descriptor_rows,
        "named_pattern_certificates": certificate_rows,
        "named_pattern_route_lengths": [
            len(ROUTES[edit]) for edit in range(1, 8)
        ],
        "maximum_correction_length": max(map(len, ROUTES.values())),
        "named_certificate_digest": digest(certificate_rows),
        "template_falsification": {
            "trees": len(template_trees),
            "tree_edit_checks": len(template_trees) * 7,
            "known_route_failures": len(failures),
            "known_route_failures_by_edit": {
                str(key): value for key, value in sorted(failures_by_edit.items())
            },
            "first_failure": failures[0],
            "logical_boundary": (
                "This refutes universality of the archived route table, not "
                "existence of some other tree-dependent or common route."
            ),
        },
        "strongest_result": (
            "Exact finite one-leaf correction theorem for the two named M181 "
            "patterns at d5->d6 and edits 1..7 only."
        ),
        "unresolved": (
            "A uniform general-d contour recurrence and synchronized braid "
            "with controlled length."
        ),
    }
    (HERE / "rooted_extension_results.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps({
        "named_pattern_route_lengths": payload["named_pattern_route_lengths"],
        "maximum_correction_length": payload["maximum_correction_length"],
        "named_certificate_digest": payload["named_certificate_digest"],
        "template_falsification": payload["template_falsification"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

