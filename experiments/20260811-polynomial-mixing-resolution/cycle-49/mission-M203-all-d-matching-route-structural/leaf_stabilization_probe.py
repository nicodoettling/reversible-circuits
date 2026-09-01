#!/usr/bin/env python3
"""Test quotient-level stabilization of d=5 DPS targets by one fixed leaf."""

from __future__ import annotations

import json
from pathlib import Path

import locality_probe as core


def main():
    bounded = json.loads(Path("locality_results.json").read_text())
    d6_targets = {
        (row["pattern_id"], row["edit"]): row
        for row in bounded["rows_detail"]
        if row["d"] == 6 and row["root"] == 5
    }
    trees = tuple(core.prufer_trees(5))
    comparisons = []
    for pattern_id, pattern in enumerate(((0,), (1,))):
        source = core.constructed_word(5, pattern)
        tree, ordering, _trials = core.inverse_dps(source, trees, 5)
        for edit in range(1, 8):
            target5 = core.dps_word(tree, core.swap_values(ordering, edit), 5)
            stabilized = target5 + ((0, 5), (0, 5))
            expected_digest = core.canonical_digest(stabilized, 6)
            actual = d6_targets[pattern_id, edit]
            actual_digest = actual["target_canonical_sha256"]
            comparisons.append({
                "pattern_id": pattern_id,
                "pattern": list(pattern),
                "edit": edit,
                "d6_root": 5,
                "d5_target": [list(pair) for pair in target5],
                "naively_stabilized_target": [list(pair) for pair in stabilized],
                "actual_d6_target": actual["target"],
                "naively_stabilized_canonical_sha256": expected_digest,
                "actual_d6_canonical_sha256": actual_digest,
                "quotient_classes_equal": expected_digest == actual_digest,
            })
    failures = [row for row in comparisons if not row["quotient_classes_equal"]]
    assert failures
    payload = {
        "experiment": "M203 quotient-level d5-to-d6 leaf-stabilization probe",
        "scope": "distinguished d6 root, two M181 patterns, internal edits 1..7",
        "comparisons": len(comparisons),
        "equal_quotient_classes": len(comparisons) - len(failures),
        "unequal_quotient_classes": len(failures),
        "first_obstruction": failures[0],
        "comparison_rows": comparisons,
        "interpretation": (
            "Adding a fixed doubled leaf after a d5 target does not in general "
            "produce the actual d6 DPS target even modulo global conjugation."
        ),
    }
    Path("leaf_stabilization_results.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps({
        "comparisons": payload["comparisons"],
        "equal_quotient_classes": payload["equal_quotient_classes"],
        "unequal_quotient_classes": payload["unequal_quotient_classes"],
        "first_obstruction": payload["first_obstruction"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
