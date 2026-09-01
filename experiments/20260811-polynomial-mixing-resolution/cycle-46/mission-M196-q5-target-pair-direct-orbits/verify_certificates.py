#!/usr/bin/env python3
"""Independent replay audit for M196's explicit positive certificates."""

from __future__ import annotations

import argparse
import hashlib
import json
from array import array
from pathlib import Path


SYMBOLS = tuple(range(1, 8)) + tuple(range(-1, -8, -1))


def inverse(word):
    return [-symbol for symbol in reversed(word)]


def endpoint(start, word, permutations):
    point = start
    for symbol in word:
        if symbol not in permutations:
            raise AssertionError(f"unknown symbol {symbol}")
        point = permutations[symbol][point]
    return point


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", type=Path, required=True)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("verification.json"))
    args = parser.parse_args()

    action_data = json.loads(args.action.read_text())
    result_bytes = args.results.read_bytes()
    results = json.loads(result_bytes)
    rows = [array("H", row) for row in action_data["action_rows"]]
    permutations = dict(zip(SYMBOLS, rows))
    action_digest = hashlib.sha256(
        b"".join(row.tobytes() for row in rows)
    ).hexdigest()
    assert action_digest == action_data["action_sha256"]
    assert action_digest == results["action_sha256"]
    source_first, source_second = results["source_ids"]

    adjusted_seen = set()
    decomposition_checks = 0
    stabilizer_replays = 0
    for search in results["searches"]:
        assert search["status"] == "positive"
        adjusted_second = search["adjusted_second_id"]
        assert adjusted_second not in adjusted_seen
        adjusted_seen.add(adjusted_second)
        forward = search["forward_word"]
        backward = search["backward_word"]
        stabilizer = search["stabilizer_word"]
        meeting_first, meeting_second = search["meeting_state"]
        assert endpoint(source_first, forward, permutations) == meeting_first
        assert endpoint(source_second, forward, permutations) == meeting_second
        assert endpoint(source_first, stabilizer, permutations) == source_first
        assert endpoint(source_second, stabilizer, permutations) == adjusted_second
        assert stabilizer == forward + inverse(backward)
        target_to_meeting_first = endpoint(source_first, backward, permutations)
        target_to_meeting_second = endpoint(
            adjusted_second, backward, permutations
        )
        assert (target_to_meeting_first, target_to_meeting_second) == (
            meeting_first, meeting_second
        )
        decomposition_checks += 1
        stabilizer_replays += 1

    frozen_targets = {
        row["target_id"]: tuple(row["target_ids"])
        for row in action_data["target_rows"]
    }
    assert len(frozen_targets) == 54
    certificate_ids = set()
    original_replays = 0
    adjusted_relation_checks = 0
    for certificate in results["original_target_certificates"]:
        target_id = certificate["target_id"]
        assert target_id not in certificate_ids
        certificate_ids.add(target_id)
        assert certificate["status"] == "positive"
        target_ids = tuple(certificate["target_ids"])
        assert target_ids == frozen_targets[target_id]
        alpha = certificate["first_tree_word"]
        stabilizer = certificate["stabilizer_word"]
        full_word = certificate["full_word"]
        adjusted_second = certificate["adjusted_second_id"]
        assert full_word == stabilizer + alpha
        assert endpoint(source_first, alpha, permutations) == target_ids[0]
        assert endpoint(adjusted_second, alpha, permutations) == target_ids[1]
        adjusted_relation_checks += 1
        assert endpoint(source_first, full_word, permutations) == target_ids[0]
        assert endpoint(source_second, full_word, permutations) == target_ids[1]
        original_replays += 1

    assert certificate_ids == set(frozen_targets)
    assert len(adjusted_seen) == results["distinct_adjusted_targets"] == 41
    assert stabilizer_replays == results["positive_adjusted_targets"] == 41
    assert original_replays == results["positive_original_targets"] == 54
    assert results["undecided_adjusted_targets"] == 0
    assert results["undecided_original_targets"] == 0
    assert results["complete_positive_classification"] is True
    assert results["negative_membership_claims"] == 0

    audit = {
        "verdict": "PASS",
        "action_sha256": action_digest,
        "targeted_results_sha256": hashlib.sha256(result_bytes).hexdigest(),
        "chronological_right_action_checked": True,
        "signed_inverse_convention_checked": True,
        "distinct_adjusted_target_ids": len(adjusted_seen),
        "meeting_decomposition_checks": decomposition_checks,
        "stabilizer_pair_replays": stabilizer_replays,
        "adjusted_relation_checks": adjusted_relation_checks,
        "original_pair_replays": original_replays,
        "target_id_inventory_exact": True,
        "negative_membership_claims": 0,
    }
    args.output.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    print(json.dumps(audit, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
