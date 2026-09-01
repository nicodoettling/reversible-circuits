#!/usr/bin/env python3
"""Run only the bounded d=5,6 embedded-DPS locality audit."""

from __future__ import annotations

import json
import time
from collections import Counter
from pathlib import Path

import locality_probe as core


def main():
    started = time.perf_counter()
    rows = []
    for d in (5, 6):
        block_count = (d - 1) // 3
        patterns = [tuple(0 for _ in range(block_count))]
        patterns.extend(
            tuple(int(index == active) for index in range(block_count))
            for active in range(block_count)
        )
        trees = tuple(core.prufer_trees(d))
        for pattern_id, pattern in enumerate(patterns):
            literal = core.constructed_word(d, pattern)
            for root in range(d):
                source = core.relabel(literal, core.root_swap(d, root))
                tree, ordering, trials = core.inverse_dps(source, trees, d)
                for edit in range(1, 2 * d - 2):
                    target = core.dps_word(tree, core.swap_values(ordering, edit), d)
                    changed = [
                        position
                        for position, (before, after) in enumerate(zip(source, target), 1)
                        if before != after
                    ]
                    adjacent_outside = [
                        position for position in changed
                        if position not in (edit, edit + 1)
                    ]
                    region_start = 6 * ((edit - 1) // 6) + 1
                    region_end = min(region_start + 5, 2 * d - 2)
                    block_outside = [
                        position for position in changed
                        if not region_start <= position <= region_end
                    ]
                    rows.append({
                        "d": d,
                        "pattern_id": pattern_id,
                        "pattern": list(pattern),
                        "root": root,
                        "edit": edit,
                        "inverse_trials": trials,
                        "source": [list(pair) for pair in source],
                        "target": [list(pair) for pair in target],
                        "changed_positions": changed,
                        "outside_adjacent_edit_positions": adjacent_outside,
                        "nominal_factor_region": [region_start, region_end],
                        "outside_nominal_region_positions": block_outside,
                        "literal_adjacent_factor_locality": not adjacent_outside,
                        "literal_six_factor_region_locality": not block_outside,
                        "target_canonical_sha256": core.canonical_digest(target, d),
                    })

    d6_block_to_filler = [
        row for row in rows
        if row["d"] == 6
        and row["edit"] <= 5
        and any(position >= 7 for position in row["changed_positions"])
    ]
    d6_filler_to_block = [
        row for row in rows
        if row["d"] == 6
        and row["edit"] >= 7
        and any(position <= 6 for position in row["changed_positions"])
    ]
    assert d6_block_to_filler
    assert d6_filler_to_block

    payload = {
        "experiment": "M203 bounded d5/d6 embedded-DPS locality audit",
        "scope": "explicit M181 words and all roots/edits; no Q_d enumeration",
        "d_values": [5, 6],
        "rows": len(rows),
        "literal_adjacent_factor_locality_failures": sum(
            not row["literal_adjacent_factor_locality"] for row in rows
        ),
        "literal_six_factor_region_locality_failures": sum(
            not row["literal_six_factor_region_locality"] for row in rows
        ),
        "region_failure_histogram_by_d": dict(sorted(Counter(
            row["d"] for row in rows
            if not row["literal_six_factor_region_locality"]
        ).items())),
        "d6_active_block_edit_changes_filler_count": len(d6_block_to_filler),
        "d6_filler_edit_changes_active_block_count": len(d6_filler_to_block),
        "first_d6_active_block_to_filler_obstruction": d6_block_to_filler[0],
        "first_d6_filler_to_active_block_obstruction": d6_filler_to_block[0],
        "elapsed_seconds": time.perf_counter() - started,
        "rows_detail": rows,
        "interpretation": (
            "DPS adjacent-value edits alter the global closure. Even on the "
            "explicit d=6 one-block/two-filler word, an edit whose two values "
            "lie inside the six-factor block can change filler factors, and a "
            "filler edit can change active-block factors. Thus matched targets "
            "do not factor into independent d5-like block targets."
        ),
    }
    Path("locality_results.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps({key: payload[key] for key in (
        "rows", "literal_adjacent_factor_locality_failures",
        "literal_six_factor_region_locality_failures",
        "region_failure_histogram_by_d",
        "d6_active_block_edit_changes_filler_count",
        "d6_filler_edit_changes_active_block_count",
        "first_d6_active_block_to_filler_obstruction",
        "first_d6_filler_to_active_block_obstruction",
        "elapsed_seconds",
    )}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
