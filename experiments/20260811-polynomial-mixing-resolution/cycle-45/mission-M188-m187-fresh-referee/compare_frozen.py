#!/usr/bin/env python3
"""Compare the completed clean-room replay with frozen M187 data.

This is deliberately run only after independent_results.json exists. It
imports the M188 checker, never M187 code, and reads M187's frozen JSON solely
for an equality comparison.
"""

from __future__ import annotations

import json
from pathlib import Path

import independent_replay as fresh


HERE = Path(__file__).resolve().parent
FROZEN = (
    HERE.parent.parent
    / "cycle-44"
    / "mission-M187-full-rank-family-quotient-route"
)


def main() -> None:
    independent_path = HERE / "independent_results.json"
    assert independent_path.exists(), "run the independent replay first"
    independent = json.loads(independent_path.read_text())
    m187 = json.loads((FROZEN / "targeted_results.json").read_text())

    d = 5
    sources = fresh.source_pair()
    source_match = m187["sources_canonical"] == [
        fresh.word_json(fresh.canonical_word(word, d)) for word in sources
    ]

    descriptor_rows = independent["rooted_descriptors"]
    descriptors = {
        (row["coordinate"], row["root"]): (
            frozenset(tuple(edge) for edge in row["tree"]),
            tuple(row["pi"]),
        )
        for row in descriptor_rows
    }
    target_row_failures = []
    for frozen_edit_row in m187["target_rows"]:
        edit = frozen_edit_row["i"]
        for coordinate in range(2):
            for root in range(d):
                tree, pi = descriptors[coordinate, root]
                target = fresh.dps_close(
                    tree, fresh.swap_adjacent_values(pi, edit), d
                )
                actual = fresh.word_json(fresh.canonical_word(target, d))
                expected = frozen_edit_row["coordinate_rows"][coordinate][root][
                    "target_canonical"
                ]
                if actual != expected:
                    target_row_failures.append({
                        "edit": edit,
                        "coordinate": coordinate,
                        "root": root,
                    })

    summary_match = {
        "eligible_distinct_target_count": (
            m187["eligible_distinct_target_tuple_count"]
            == independent["target_construction"]["distinct_eligible_target_tuples"]
        ),
        "visited_states": (
            m187["bounded_quotient_bfs"]["visited_states"]
            == independent["radius_five_ball"]["visited_states"]
        ),
        "positive_target_count": (
            m187["bounded_quotient_bfs"]["targets_found"]
            == independent["radius_five_ball"]["positive_target_count"]
        ),
        "positive_path_lengths": (
            m187["bounded_quotient_bfs"]["found_path_lengths"]
            == sorted(independent["radius_five_ball"]["positive_path_lengths"])
        ),
    }
    result = {
        "comparison": "M188 independent output against frozen M187 JSON",
        "m187_code_imported": False,
        "source_match": source_match,
        "target_rows_compared": 70,
        "target_row_failures": target_row_failures,
        "summary_match": summary_match,
        "all_claim_bearing_data_match": (
            source_match
            and not target_row_failures
            and all(summary_match.values())
        ),
        "m187_archives_explicit_route_sequences": (
            "found_routes" in m187["bounded_quotient_bfs"]
        ),
        "interpretation": (
            "M187 deterministically computes routes but archives only their "
            "count and lengths; M188 archives and directly rechecks all 14 paths."
        ),
    }
    assert result["all_claim_bearing_data_match"]
    (HERE / "comparison_results.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
