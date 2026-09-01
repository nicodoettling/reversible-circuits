#!/usr/bin/env python3
"""Exact d=5 coverage map from M135/M181 incidences to M196 routes.

M135 freezes no numerical d=5 edge coloring: its colors are arbitrary perfect
matchings.  The invariant finite object is therefore the root-edge table and
all root-pair incidences.  Every actual color selects one row over each of the
two source vertices, hence exactly one of the archived root-pair rows.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from array import array
from collections import Counter, defaultdict
from pathlib import Path


SYMBOLS = tuple(range(1, 8)) + tuple(range(-1, -8, -1))
EXPECTED_MANIFESTS = {
    "M135": "8d7ca3afbab24be7b1552b433e9f0f0260efbbb658af4bd66cccd676452a5358",
    "M137": "47dfb3f81d5e16e88b676f57f0c6fc0237b7993fff5c5c4a071046c597c51af5",
    "M181": "d2ae8d5a2af347eb74943db1221607d46fc706296ac2802d97abc0a024ec20b0",
    "M183": "ddd2bf1d2ce8d22e2228624d8802b38a527fee27819b92f9f06c3393b567fa46",
    "M196": "7fa987c6c776e55990c00fcfaea85e34c1d7b0e6d3f97d57fdefba8bcb5bd913",
    "M198": "1142912065699b883268b16aee8707b1c1e0d7c4b006eb1ca9bb02282ef9bd84",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def apply_pair(pair, word, action):
    first, second = pair
    for symbol in word:
        row = action[symbol]
        first, second = row[first], row[second]
    return [first, second]


def route_digest(word) -> str:
    packed = json.dumps(word, separators=(",", ":")).encode()
    return hashlib.sha256(packed).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--m181-results", type=Path, required=True)
    parser.add_argument("--m196-adjusted", type=Path, required=True)
    parser.add_argument("--m196-results", type=Path, required=True)
    parser.add_argument("--m198-results", type=Path, required=True)
    parser.add_argument("--q5-action", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("incidence_table.json"))
    args = parser.parse_args()

    m181 = json.loads(args.m181_results.read_text())
    adjusted = json.loads(args.m196_adjusted.read_text())
    routed = json.loads(args.m196_results.read_text())
    referee = json.loads(args.m198_results.read_text())
    q5 = json.loads(args.q5_action.read_text())

    # Exact width-two/full-voltage input from M181.
    d5_rows = [row for row in m181["family_rows"] if row["d"] == 5]
    assert len(d5_rows) == 1
    d5_family = d5_rows[0]
    assert d5_family == {
        "all_words_valid": True,
        "blocks": 1,
        "d": 5,
        "literal_shifted_relations_verified": 1,
        "patterns": [[0], [1]],
        "voltage_basis_representatives": [[0, 1]],
        "width": 2,
    }

    # M198 is the accepted independent certificate audit.
    assert referee["verdict"] == "ACCEPT"
    assert referee["numbered_objections"] == []
    assert referee["named_targets"] == {
        "adjusted_distinct": 41,
        "distinct_rows": 54,
        "occurrences": 175,
        "rooted_descriptors": 10,
    }
    assert referee["certificates"]["stabilizer_replays"] == 41
    assert referee["certificates"]["full_replays"] == 54

    # Load and directly replay the immutable finite quotient certificates.
    rows = [array("H", row) for row in q5["action_rows"]]
    assert len(rows) == 14 and all(len(row) == 8400 for row in rows)
    action = dict(zip(SYMBOLS, rows))
    action_digest = hashlib.sha256(b"".join(row.tobytes() for row in rows)).hexdigest()
    assert action_digest == q5["action_sha256"] == routed["action_sha256"]
    assert action_digest == referee["action_sha256"]
    source_ids = q5["source_ids"]
    assert source_ids == adjusted["source_ids"] == routed["source_ids"] == [16, 0]
    assert routed["complete_positive_classification"] is True
    assert routed["positive_original_targets"] == 54
    assert routed["undecided_original_targets"] == 0
    assert routed["negative_membership_claims"] == 0

    certificates = {}
    for certificate in routed["original_target_certificates"]:
        target_id = certificate["target_id"]
        assert target_id not in certificates
        assert certificate["status"] == "positive"
        full_word = certificate["full_word"]
        assert apply_pair(source_ids, full_word, action) == certificate["target_ids"]
        certificates[target_id] = {
            "target_id": target_id,
            "target_ids": certificate["target_ids"],
            "full_word": full_word,
            "route_length": len(full_word),
            "route_word_sha256": route_digest(full_word),
            "direct_pair_replay_ok": True,
        }
    assert set(certificates) == set(range(54))

    # Each of the 7*5*5 root-pair occurrences must occur exactly once among
    # the 54 deduplicated target rows.
    occurrence_lookup = {}
    class_sizes = {}
    for target in adjusted["target_rows"]:
        target_id = target["target_id"]
        assert target["target_ids"] == certificates[target_id]["target_ids"]
        class_sizes[target_id] = len(target["occurrences"])
        for occurrence in target["occurrences"]:
            key = (occurrence["edit"], *occurrence["roots"])
            assert key not in occurrence_lookup
            occurrence_lookup[key] = {
                "target_id": target_id,
                "target_ids": target["target_ids"],
            }
    expected_keys = {
        (edit, first_root, second_root)
        for edit in range(1, 8)
        for first_root in range(5)
        for second_root in range(5)
    }
    assert set(occurrence_lookup) == expected_keys
    assert len(occurrence_lookup) == 175
    assert len(class_sizes) == 54

    # Coordinate target is independent of the root chosen in the other
    # coordinate.  These 70 rows are the intrinsic edge-incidence table.
    root_edge_rows = []
    coordinate_target = {}
    for edit in range(1, 8):
        for coordinate in range(2):
            for root in range(5):
                possible = {
                    occurrence_lookup[(edit, root, other)]["target_ids"][0]
                    if coordinate == 0
                    else occurrence_lookup[(edit, other, root)]["target_ids"][1]
                    for other in range(5)
                }
                assert len(possible) == 1
                target_q5_id = next(iter(possible))
                coordinate_target[edit, coordinate, root] = target_q5_id
                root_edge_rows.append({
                    "edit": edit,
                    "coordinate": coordinate,
                    "left_source_q5_id": source_ids[coordinate],
                    "h_orbit_root": root,
                    "matched_target_q5_id": target_q5_id,
                })
    assert len(root_edge_rows) == 70

    pair_rows = []
    for edit, first_root, second_root in sorted(expected_keys):
        lookup = occurrence_lookup[edit, first_root, second_root]
        target_id = lookup["target_id"]
        target_ids = [
            coordinate_target[edit, 0, first_root],
            coordinate_target[edit, 1, second_root],
        ]
        assert target_ids == lookup["target_ids"]
        assert target_ids[0] != target_ids[1]
        pair_rows.append({
            "edit": edit,
            "source_q5_ids": source_ids,
            "selected_h_orbit_roots": [first_root, second_root],
            "matched_target_q5_ids": target_ids,
            "m196_target_id": target_id,
            "target_class_occurrences": class_sizes[target_id],
            "covered_by_m196_theorem": True,
            "route_certificate_target_id": target_id,
            "route_length": certificates[target_id]["route_length"],
            "route_word_sha256": certificates[target_id]["route_word_sha256"],
        })
    assert len(pair_rows) == 175

    # Numeric M135 color names were never frozen at d=5.  Normalize an
    # arbitrary coloring at each edit by naming a color after its root above
    # the first source vertex.  Above the second vertex the roots form some
    # permutation sigma.  Listing all five sigma(c) possibilities per color
    # makes the universal quantifier exact without inventing a coloring.
    normalized_color_rows = []
    for edit in range(1, 8):
        for color in range(5):
            possibilities = []
            for second_root in range(5):
                pair = occurrence_lookup[edit, color, second_root]
                possibilities.append({
                    "second_source_root": second_root,
                    "matched_target_q5_ids": pair["target_ids"],
                    "m196_target_id": pair["target_id"],
                    "route_length": certificates[pair["target_id"]]["route_length"],
                })
            assert len(possibilities) == 5
            assert all(
                certificates[row["m196_target_id"]]["direct_pair_replay_ok"]
                for row in possibilities
            )
            normalized_color_rows.append({
                "edit": edit,
                "normalized_color": color,
                "first_source_root": color,
                "second_source_root": "sigma_edit(color)",
                "sigma_edit_constraint": "permutation of 0..4",
                "all_possible_matched_targets": possibilities,
                "all_possibilities_covered": True,
                "full_voltage_source": True,
            })
    assert len(normalized_color_rows) == 35

    # Every actual color maps to one of the pair rows; all are positive.  The
    # remaining M181 affine theorem then discharges physical zero-voltage
    # endpoint existence qualitatively, but supplies no quantitative word.
    uncovered = [row for row in pair_rows if not row["covered_by_m196_theorem"]]
    assert uncovered == []
    target_histogram = Counter(row["m196_target_id"] for row in pair_rows)
    assert target_histogram == Counter(class_sizes)

    output = {
        "experiment": "M200 exact d=5 matching-color route coverage",
        "scope": "finite d=5 width-two M181 family only",
        "composition": "chronological signed Hurwitz symbols acting on the right",
        "seed": None,
        "dependencies": {},
        "immutable_manifest_sha256": EXPECTED_MANIFESTS,
        "source": {
            "q5_ids": source_ids,
            "m181_patterns": d5_family["patterns"],
            "width": 2,
            "voltage_basis_representatives": d5_family["voltage_basis_representatives"],
            "v_stab_dimension": 1,
            "v_stab_equals_w2": True,
        },
        "color_semantics": {
            "colors_per_edit": 5,
            "numerical_d5_coloring_frozen_by_m135": False,
            "invariant_parameterization": (
                "each actual color selects one of five H-orbit roots over each "
                "left source; after labeling colors by the first-source root, "
                "the second-source roots form a permutation sigma_edit"
            ),
        },
        "counts": {
            "edits": 7,
            "colors_per_edit": 5,
            "relevant_left_source_orbits": 2,
            "root_edge_rows": len(root_edge_rows),
            "root_pair_incidences": len(pair_rows),
            "distinct_m196_target_classes": len(target_histogram),
            "covered_root_pair_incidences": len(pair_rows) - len(uncovered),
            "uncovered_root_pair_incidences": len(uncovered),
            "normalized_color_rows": len(normalized_color_rows),
        },
        "digests": {
            "q5_action_packed_sha256": action_digest,
            "q5_action_file_sha256": sha256(args.q5_action),
            "m181_results_sha256": sha256(args.m181_results),
            "m196_adjusted_sha256": sha256(args.m196_adjusted),
            "m196_results_sha256": sha256(args.m196_results),
            "m198_results_sha256": sha256(args.m198_results),
        },
        "exact_theorem": {
            "every_d5_matching_color_has_full_voltage_source_pair": True,
            "every_matched_quotient_target_pair_is_m196_reachable": True,
            "m181_conditional_endpoint_hypothesis_discharged": True,
            "qualitative_zero_relative_voltage_endpoint_route_exists": True,
            "explicit_m196_words_are_quotient_route_certificates": True,
            "quantitative_zero_voltage_route_length_claim": False,
        },
        "uncovered_target_classes": [],
        "root_edge_rows": root_edge_rows,
        "root_pair_rows": pair_rows,
        "normalized_color_rows": normalized_color_rows,
        "route_certificates": [certificates[target_id] for target_id in range(54)],
        "limitations": [
            "M135 freezes no numeric d=5 coloring, so no canonical color-to-root permutation exists.",
            "The theorem is finite d=5 and does not imply all-d coverage.",
            "M196 word lengths certify quotient routes only; no polynomial or quantitative corrected physical route bound follows.",
            "No spectral-gap, mixing, or Terminal inference is made.",
        ],
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "counts": output["counts"],
        "digests": output["digests"],
        "exact_theorem": output["exact_theorem"],
        "uncovered_target_classes": output["uncovered_target_classes"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
