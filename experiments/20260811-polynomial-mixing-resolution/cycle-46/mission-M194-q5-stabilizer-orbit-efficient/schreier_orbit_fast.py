#!/usr/bin/env python3
"""Exact streamed Schreier orbit on M191's frozen 8,400-point action."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import resource
import time
from array import array
from collections import deque
from pathlib import Path


SYMBOLS = tuple(range(1, 8)) + tuple(range(-1, -8, -1))


def inv(word):
    return tuple(-x for x in reversed(word))


def act(point, word, actions):
    for symbol in word:
        point = actions[symbol][point]
    return point


def transversal(start, actions, n):
    parent = array("h", [-2]) * n
    edge = array("b", [0]) * n
    parent[start] = -1
    order = [start]
    queue = deque([start])
    while queue:
        x = queue.popleft()
        for symbol in SYMBOLS:
            y = actions[symbol][x]
            if parent[y] == -2:
                parent[y] = x
                edge[y] = symbol
                order.append(y)
                queue.append(y)
    assert len(order) == n
    words = [None] * n
    words[start] = ()
    for x in order[1:]:
        words[x] = words[parent[x]] + (edge[x],)
    assert all(act(start, words[x], actions) == x for x in range(n))
    return order, words


def schreier_image(point, x, symbol, tree_words, actions):
    y = actions[symbol][x]
    return act(actions[symbol][act(point, tree_words[x], actions)], inv(tree_words[y]), actions)


def close_retained(source, retained, tree_words, actions, parent_data=None):
    n = len(tree_words)
    seen = bytearray(n)
    seen[source] = 1
    orbit = [source]
    queue = deque([source])
    if parent_data is None:
        parent = array("h", [-2]) * n
        parent_x = array("H", [0]) * n
        parent_symbol = array("b", [0]) * n
        parent[source] = -1
    else:
        parent, parent_x, parent_symbol = parent_data
    while queue:
        point = queue.popleft()
        for generator_x, generator_symbol in retained:
            for orientation in (1, -1):
                if orientation == 1:
                    x, symbol = generator_x, generator_symbol
                else:
                    x = actions[generator_symbol][generator_x]
                    symbol = -generator_symbol
                nxt = schreier_image(point, x, symbol, tree_words, actions)
                if not seen[nxt]:
                    seen[nxt] = 1
                    orbit.append(nxt)
                    queue.append(nxt)
                    if parent[nxt] == -2:
                        parent[nxt] = point
                        parent_x[nxt] = x
                        parent_symbol[nxt] = symbol
    return seen, orbit, (parent, parent_x, parent_symbol)


def compute_orbit(source, order, tree_words, actions, deadline):
    retained = []
    seen, orbit, parent_data = close_retained(source, retained, tree_words, actions)
    candidates = 0
    for x in order:
        if time.monotonic() > deadline:
            raise TimeoutError
        for symbol in SYMBOLS:
            candidates += 1
            if any(not seen[schreier_image(p, x, symbol, tree_words, actions)] for p in orbit):
                retained.append((x, symbol))
                seen, orbit, parent_data = close_retained(
                    source, retained, tree_words, actions, parent_data
                )
    return seen, orbit, parent_data, retained, candidates


def compact_certificate(point, parent_data):
    parent, parent_x, parent_symbol = parent_data
    chunks = []
    while parent[point] != -1:
        chunks.append((parent_x[point], parent_symbol[point]))
        point = parent[point]
    return tuple(reversed(chunks))


def expand(certificate, tree_words, actions):
    word = []
    for x, symbol in certificate:
        y = actions[symbol][x]
        word.extend(tree_words[x])
        word.append(symbol)
        word.extend(inv(tree_words[y]))
    return tuple(word)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("exact_results.json"))
    parser.add_argument("--cap-seconds", type=int, default=300)
    args = parser.parse_args()
    start_time = time.monotonic()
    deadline = start_time + args.cap_seconds

    frozen = json.loads(args.input.read_text())
    assert frozen["q5_size"] == 8400 and frozen["symbols"] == list(SYMBOLS)
    rows = [array("H", row) for row in frozen["action_rows"]]
    actions = dict(zip(SYMBOLS, rows))
    digest = hashlib.sha256(b"".join(row.tobytes() for row in rows)).hexdigest()
    assert digest == frozen["action_sha256"] == "160bcae167e754af4ff55356a2ab25526bf53d03ebc23bd974938fb8370c67ae"
    for row in rows:
        assert len(set(row)) == 8400
    for slot in range(1, 8):
        assert all(actions[-slot][actions[slot][x]] == x for x in range(8400))

    first, second = frozen["source_ids"]
    assert (first, second) == (16, 0)
    order, tree_words = transversal(first, actions, 8400)
    seen, orbit, parent_data, retained, candidates = compute_orbit(
        second, order, tree_words, actions, deadline
    )

    # Completeness: closure under every literal Schreier generator.
    closure_checks = 0
    for x in order:
        if time.monotonic() > deadline:
            raise TimeoutError
        for symbol in SYMBOLS:
            for point in orbit:
                assert seen[schreier_image(point, x, symbol, tree_words, actions)]
                closure_checks += 1

    classification = []
    positive = negative = 0
    for target in frozen["target_rows"]:
        target_first, target_second = target["target_ids"]
        alpha = tree_words[target_first]
        adjusted = act(target_second, inv(alpha), actions)
        reachable = bool(seen[adjusted])
        if reachable:
            certificate = compact_certificate(adjusted, parent_data)
            stabilizer_word = expand(certificate, tree_words, actions)
            route = stabilizer_word + alpha
            assert act(first, route, actions) == target_first
            assert act(second, route, actions) == target_second
            positive += 1
        else:
            certificate = stabilizer_word = route = ()
            negative += 1
        classification.append({
            "target_id": target["target_id"],
            "target_ids": target["target_ids"],
            "occurrences": target["occurrences"],
            "first_tree_word": list(alpha),
            "adjusted_second_id": adjusted,
            "reachable": reachable,
            "schreier_certificate": [list(pair) for pair in certificate],
            "stabilizer_word": list(stabilizer_word),
            "route": list(route),
            "route_length": len(route) if reachable else None,
        })

    elapsed = time.monotonic() - start_time
    result = {
        "experiment": "M194 exact streamed Schreier stabilizer orbit",
        "repository_base_commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
        "command": "python3 -B schreier_orbit_fast.py --input M191/q5_action.json --output exact_results.json --cap-seconds 300",
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "cap_seconds": args.cap_seconds,
        "elapsed_seconds": elapsed,
        "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "action": {"size": 8400, "digest": digest, "source_ids": [first, second], "bijections_and_inverses_checked": True},
        "transversal": {"size": len(order), "max_word_length": max(map(len, tree_words)), "all_words_replayed": True},
        "stabilizer_orbit": {
            "size": len(orbit),
            "retained_generators": [list(pair) for pair in retained],
            "retained_generator_count": len(retained),
            "schreier_candidates_checked": candidates,
            "closure_checks": closure_checks,
            "closed_under_all_schreier_generators": True,
            "orbit_ids": sorted(orbit),
            "orbit_bitmap_sha256": hashlib.sha256(bytes(seen)).hexdigest(),
        },
        "classification": {
            "target_count": len(classification),
            "reachable": positive,
            "unreachable": negative,
            "all_positive_routes_replayed": True,
            "negative_certificate": "adjusted_second_id absent from exact closed orbit_ids",
            "rows": classification,
            "rows_sha256": hashlib.sha256(json.dumps(classification, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
        },
        "scope": "exact finite d=5 only",
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "elapsed_seconds": elapsed,
        "peak_rss_kib": result["peak_rss_kib"],
        "transversal": result["transversal"],
        "stabilizer_orbit": {k: result["stabilizer_orbit"][k] for k in ("size", "retained_generator_count", "schreier_candidates_checked", "closure_checks", "orbit_bitmap_sha256")},
        "classification": {k: result["classification"][k] for k in ("target_count", "reachable", "unreachable", "all_positive_routes_replayed", "rows_sha256")},
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
