#!/usr/bin/env python3
"""Target-directed exact searches in the frozen M191 diagonal Q5 action.

This deliberately builds only bounded product-action balls.  A hit yields an
explicit, replayed stabilizer word.  A miss is recorded as undecided, never as
nonmembership.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from array import array
from pathlib import Path


SYMBOLS = tuple(range(1, 8)) + tuple(range(-1, -8, -1))
N = 8400


def inverse_word(word):
    return tuple(-symbol for symbol in reversed(word))


def apply(point, word, action):
    for symbol in word:
        point = action[symbol][point]
    return point


def encode(first, second):
    return first * N + second


def decode(state):
    return divmod(state, N)


def step(state, symbol, action):
    first, second = decode(state)
    return encode(action[symbol][first], action[symbol][second])


def reconstruct(parents, root, state):
    """Return the chronological word along a rooted BFS tree."""
    reversed_word = []
    while state != root:
        parent, symbol = parents[state]
        reversed_word.append(symbol)
        state = parent
    return tuple(reversed(reversed_word))


def build_forward_ball(root, action, max_depth, deadline):
    parents = {root: (-1, 0)}
    frontier = [root]
    level_sizes = [1]
    for _depth in range(max_depth):
        next_frontier = []
        for index, state in enumerate(frontier):
            if index % 1024 == 0 and time.monotonic() >= deadline:
                return parents, level_sizes, True
            for symbol in SYMBOLS:
                child = step(state, symbol, action)
                if child not in parents:
                    parents[child] = (state, symbol)
                    next_frontier.append(child)
        frontier = next_frontier
        level_sizes.append(len(frontier))
    return parents, level_sizes, False


def search_from_target(target, forward_parents, forward_root, action,
                       max_depth, deadline, max_visited):
    """Meet a bounded BFS from target with the fixed forward ball."""
    if target in forward_parents:
        meeting = target
        forward_word = reconstruct(forward_parents, forward_root, meeting)
        return {
            "status": "positive",
            "meeting_state": list(decode(meeting)),
            "forward_word": list(forward_word),
            "backward_word": [],
            "stabilizer_word": list(forward_word),
            "backward_level_sizes": [1],
            "backward_visited": 1,
        }

    backward_parents = {target: (-1, 0)}
    frontier = [target]
    level_sizes = [1]
    for _depth in range(max_depth):
        next_frontier = []
        for index, state in enumerate(frontier):
            if index % 1024 == 0 and time.monotonic() >= deadline:
                return {
                    "status": "undecided_timeout",
                    "backward_level_sizes": level_sizes,
                    "backward_visited": len(backward_parents),
                }
            for symbol in SYMBOLS:
                child = step(state, symbol, action)
                if child in backward_parents:
                    continue
                backward_parents[child] = (state, symbol)
                next_frontier.append(child)
                if child in forward_parents:
                    target_to_meeting = reconstruct(
                        backward_parents, target, child
                    )
                    source_to_meeting = reconstruct(
                        forward_parents, forward_root, child
                    )
                    stabilizer_word = (
                        source_to_meeting + inverse_word(target_to_meeting)
                    )
                    return {
                        "status": "positive",
                        "meeting_state": list(decode(child)),
                        "forward_word": list(source_to_meeting),
                        "backward_word": list(target_to_meeting),
                        "stabilizer_word": list(stabilizer_word),
                        "backward_level_sizes": level_sizes + [
                            len(next_frontier)
                        ],
                        "backward_visited": len(backward_parents),
                    }
                if len(backward_parents) >= max_visited:
                    return {
                        "status": "undecided_memory_cap",
                        "backward_level_sizes": level_sizes + [
                            len(next_frontier)
                        ],
                        "backward_visited": len(backward_parents),
                    }
        frontier = next_frontier
        level_sizes.append(len(frontier))
    return {
        "status": "undecided_radius_cap",
        "backward_level_sizes": level_sizes,
        "backward_visited": len(backward_parents),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", type=Path, required=True)
    parser.add_argument("--adjusted", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("targeted_results.json"))
    parser.add_argument("--forward-depth", type=int, default=8)
    parser.add_argument("--backward-depth", type=int, default=8)
    parser.add_argument("--seconds", type=float, default=285.0)
    parser.add_argument("--max-backward-visited", type=int, default=300000)
    args = parser.parse_args()

    started_wall = time.time()
    started = time.monotonic()
    deadline = started + args.seconds

    frozen = json.loads(args.action.read_text())
    adjusted = json.loads(args.adjusted.read_text())
    rows = [array("H", row) for row in frozen["action_rows"]]
    action = dict(zip(SYMBOLS, rows))
    digest = hashlib.sha256(b"".join(row.tobytes() for row in rows)).hexdigest()
    assert digest == frozen["action_sha256"] == adjusted["action_sha256"]
    assert len(rows) == len(SYMBOLS)
    assert all(len(row) == N for row in rows)
    source_first, source_second = adjusted["source_ids"]
    source = encode(source_first, source_second)

    forward_parents, forward_levels, forward_timed_out = build_forward_ball(
        source, action, args.forward_depth, deadline
    )
    searches = []
    positive_words = {}
    global_timeout = forward_timed_out

    for target_class in adjusted["adjusted_classes"]:
        adjusted_second = target_class["adjusted_second_id"]
        if global_timeout or time.monotonic() >= deadline:
            search = {
                "status": "undecided_timeout",
                "backward_level_sizes": [],
                "backward_visited": 0,
            }
            global_timeout = True
        else:
            search = search_from_target(
                encode(source_first, adjusted_second),
                forward_parents,
                source,
                action,
                args.backward_depth,
                deadline,
                args.max_backward_visited,
            )
            if search["status"] == "undecided_timeout":
                global_timeout = True

        replay_ok = False
        if search["status"] == "positive":
            word = tuple(search["stabilizer_word"])
            endpoint = (
                apply(source_first, word, action),
                apply(source_second, word, action),
            )
            assert endpoint == (source_first, adjusted_second)
            replay_ok = True
            positive_words[adjusted_second] = word
        search.update({
            "adjusted_second_id": adjusted_second,
            "target_ids": target_class["target_ids"],
            "direct_pair_replay_ok": replay_ok,
        })
        searches.append(search)

    original_certificates = []
    for target in adjusted["target_rows"]:
        adjusted_second = target["adjusted_second_id"]
        certificate = {
            "target_id": target["target_id"],
            "target_ids": target["target_ids"],
            "adjusted_second_id": adjusted_second,
        }
        if adjusted_second in positive_words:
            stabilizer_word = positive_words[adjusted_second]
            alpha = tuple(target["first_tree_word"])
            full_word = stabilizer_word + alpha
            endpoint = (
                apply(source_first, full_word, action),
                apply(source_second, full_word, action),
            )
            assert endpoint == tuple(target["target_ids"])
            certificate.update({
                "status": "positive",
                "stabilizer_word": list(stabilizer_word),
                "first_tree_word": list(alpha),
                "full_word": list(full_word),
                "direct_target_replay_ok": True,
            })
        else:
            certificate.update({
                "status": "undecided",
                "direct_target_replay_ok": False,
            })
        original_certificates.append(certificate)

    positive_adjusted = sum(
        search["status"] == "positive" for search in searches
    )
    positive_original = sum(
        certificate["status"] == "positive"
        for certificate in original_certificates
    )
    unresolved_statuses = sorted({
        search["status"] for search in searches
        if search["status"] != "positive"
    })
    elapsed = time.monotonic() - started
    result = {
        "method": "bounded_target_directed_bidirectional_product_bfs",
        "right_action_convention": "chronological signed symbols acting on the right",
        "symbols": list(SYMBOLS),
        "action_sha256": digest,
        "source_ids": [source_first, source_second],
        "started_unix": started_wall,
        "elapsed_seconds": elapsed,
        "wall_clock_cap_seconds": args.seconds,
        "forward_depth_cap": args.forward_depth,
        "backward_depth_cap": args.backward_depth,
        "max_backward_visited": args.max_backward_visited,
        "forward_level_sizes": forward_levels,
        "forward_visited": len(forward_parents),
        "forward_timed_out": forward_timed_out,
        "distinct_adjusted_targets": len(searches),
        "positive_adjusted_targets": positive_adjusted,
        "undecided_adjusted_targets": len(searches) - positive_adjusted,
        "original_targets": len(original_certificates),
        "positive_original_targets": positive_original,
        "undecided_original_targets": len(original_certificates) - positive_original,
        "all_positive_words_replayed": all(
            search["direct_pair_replay_ok"]
            for search in searches if search["status"] == "positive"
        ),
        "all_original_words_replayed": all(
            certificate["direct_target_replay_ok"]
            for certificate in original_certificates
            if certificate["status"] == "positive"
        ),
        "complete_positive_classification": positive_original == len(original_certificates),
        "negative_membership_claims": 0,
        "unresolved_statuses": unresolved_statuses,
        "searches": searches,
        "original_target_certificates": original_certificates,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        key: result[key] for key in (
            "action_sha256", "elapsed_seconds", "forward_level_sizes",
            "forward_visited", "distinct_adjusted_targets",
            "positive_adjusted_targets", "undecided_adjusted_targets",
            "original_targets", "positive_original_targets",
            "undecided_original_targets", "complete_positive_classification",
            "negative_membership_claims", "unresolved_statuses",
        )
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
