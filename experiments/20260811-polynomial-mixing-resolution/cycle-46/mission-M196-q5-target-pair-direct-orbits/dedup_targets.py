#!/usr/bin/env python3
"""Build M191's chronological transversal and deduplicate adjusted targets."""

from __future__ import annotations

import argparse
import hashlib
import json
from array import array
from collections import defaultdict, deque
from pathlib import Path


SYMBOLS = tuple(range(1, 8)) + tuple(range(-1, -8, -1))


def inverse_word(word):
    return tuple(-symbol for symbol in reversed(word))


def apply(point, word, action):
    for symbol in word:
        point = action[symbol][point]
    return point


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("adjusted_targets.json"))
    args = parser.parse_args()
    frozen = json.loads(args.input.read_text())
    rows = [array("H", row) for row in frozen["action_rows"]]
    action = dict(zip(SYMBOLS, rows))
    digest = hashlib.sha256(b"".join(row.tobytes() for row in rows)).hexdigest()
    assert digest == frozen["action_sha256"]
    first, second = frozen["source_ids"]
    parent = array("h", [-2]) * 8400
    parent_symbol = array("b", [0]) * 8400
    parent[first] = -1
    order = [first]
    queue = deque([first])
    while queue:
        x = queue.popleft()
        for symbol in SYMBOLS:
            y = action[symbol][x]
            if parent[y] == -2:
                parent[y] = x
                parent_symbol[y] = symbol
                order.append(y)
                queue.append(y)
    assert len(order) == 8400
    tree_word = [None] * 8400
    tree_word[first] = ()
    for x in order[1:]:
        tree_word[x] = tree_word[parent[x]] + (parent_symbol[x],)
    assert all(apply(first, tree_word[x], action) == x for x in range(8400))

    classes = defaultdict(list)
    target_rows = []
    for target in frozen["target_rows"]:
        target_first, target_second = target["target_ids"]
        alpha = tree_word[target_first]
        adjusted = apply(target_second, inverse_word(alpha), action)
        row = {
            "target_id": target["target_id"],
            "target_ids": target["target_ids"],
            "occurrences": target["occurrences"],
            "first_tree_word": list(alpha),
            "adjusted_second_id": adjusted,
        }
        target_rows.append(row)
        classes[adjusted].append(target["target_id"])
    result = {
        "action_sha256": digest,
        "source_ids": [first, second],
        "transversal_size": len(order),
        "transversal_max_depth": max(map(len, tree_word)),
        "all_transversal_words_replayed": True,
        "target_count": len(target_rows),
        "distinct_adjusted_target_count": len(classes),
        "adjusted_classes": [
            {"adjusted_second_id": adjusted, "target_ids": ids}
            for adjusted, ids in sorted(classes.items())
        ],
        "target_rows": target_rows,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        key: result[key]
        for key in (
            "action_sha256", "source_ids", "transversal_size",
            "transversal_max_depth", "all_transversal_words_replayed",
            "target_count", "distinct_adjusted_target_count"
        )
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
