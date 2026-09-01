#!/usr/bin/env python3
"""Efficient exact Schreier-stabilizer orbit for M191's frozen Q5 action."""

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


def inverse_word(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(-symbol for symbol in reversed(word))


def apply_word(point: int, word: tuple[int, ...], action_by_symbol) -> int:
    for symbol in word:
        point = action_by_symbol[symbol][point]
    return point


def bfs_transversal(start: int, action_by_symbol, n: int):
    parent = array("h", [-2]) * n
    parent_symbol = array("b", [0]) * n
    parent[start] = -1
    order = array("H", [start])
    queue = deque([start])
    while queue:
        x = queue.popleft()
        for symbol in SYMBOLS:
            y = action_by_symbol[symbol][x]
            if parent[y] == -2:
                parent[y] = x
                parent_symbol[y] = symbol
                order.append(y)
                queue.append(y)
    assert len(order) == n
    return parent, parent_symbol, order


def tree_words(parent, parent_symbol):
    """Compute chronological source-to-x words by dynamic programming."""
    words = [None] * len(parent)
    root = next(i for i, value in enumerate(parent) if value == -1)
    words[root] = ()
    unresolved = len(parent) - 1
    while unresolved:
        progressed = 0
        for x in range(len(parent)):
            if words[x] is None and words[parent[x]] is not None:
                words[x] = words[parent[x]] + (parent_symbol[x],)
                unresolved -= 1
                progressed += 1
        assert progressed
    return words


def schreier_image_on_point(point: int, x: int, symbol: int, tree_word, action_by_symbol):
    y = action_by_symbol[symbol][x]
    point = apply_word(point, tree_word[x], action_by_symbol)
    point = action_by_symbol[symbol][point]
    point = apply_word(point, inverse_word(tree_word[y]), action_by_symbol)
    return point


def full_schreier_orbit(source_second, order, tree_word, action_by_symbol, deadline):
    """BFS using all Schreier generators, storing compact generator certificates."""
    n = len(order)
    seen = bytearray(n)
    parent = array("h", [-2]) * n
    parent_x = array("H", [0]) * n
    parent_symbol = array("b", [0]) * n
    seen[source_second] = 1
    parent[source_second] = -1
    queue = deque([source_second])
    expansions = 0
    while queue:
        if time.monotonic() > deadline:
            raise TimeoutError("five-minute cap reached")
        point = queue.popleft()
        for x in order:
            for symbol in SYMBOLS:
                nxt = schreier_image_on_point(
                    point, x, symbol, tree_word, action_by_symbol
                )
                if not seen[nxt]:
                    seen[nxt] = 1
                    parent[nxt] = point
                    parent_x[nxt] = x
                    parent_symbol[nxt] = symbol
                    queue.append(nxt)
        expansions += 1
    return seen, parent, parent_x, parent_symbol, expansions


def orbit_certificate_word(point, parent, parent_x, parent_symbol, tree_word):
    chunks = []
    while parent[point] != -1:
        x = parent_x[point]
        symbol = parent_symbol[point]
        # This edge used s_(x,symbol)=t_x symbol t_(x symbol)^-1.
        y = None
        chunks.append((x, symbol))
        point = parent[point]
    word = ()
    for x, symbol in reversed(chunks):
        # The tree target can be recovered by following symbol on x; caller
        # expands this with the action table in build_certificate_word.
        word += ((x, symbol),)
    return word


def expand_schreier_certificate(certificate, tree_word, action_by_symbol):
    out = []
    for x, symbol in certificate:
        y = action_by_symbol[symbol][x]
        out.extend(tree_word[x])
        out.append(symbol)
        out.extend(inverse_word(tree_word[y]))
    return tuple(out)


def classify(input_path: Path, output_path: Path, cap_seconds: int):
    started = time.monotonic()
    deadline = started + cap_seconds
    frozen = json.loads(input_path.read_text())
    assert frozen["q5_size"] == 8400
    assert frozen["symbols"] == list(SYMBOLS)
    n = frozen["q5_size"]
    action_rows = [array("H", row) for row in frozen["action_rows"]]
    action_by_symbol = dict(zip(SYMBOLS, action_rows))

    action_digest = hashlib.sha256(
        b"".join(action.tobytes() for action in action_rows)
    ).hexdigest()
    assert action_digest == frozen["action_sha256"]
    assert action_digest == "160bcae167e754af4ff55356a2ab25526bf53d03ebc23bd974938fb8370c67ae"
    for action in action_rows:
        assert len(set(action)) == n
    for slot in range(1, 8):
        plus, minus = action_by_symbol[slot], action_by_symbol[-slot]
        assert all(minus[plus[x]] == x and plus[minus[x]] == x for x in range(n))

    source_first, source_second = frozen["source_ids"]
    assert (source_first, source_second) == (16, 0)
    parent, parent_symbol, order = bfs_transversal(source_first, action_by_symbol, n)
    tree_word = tree_words(parent, parent_symbol)
    for x in range(n):
        assert apply_word(source_first, tree_word[x], action_by_symbol) == x

    seen, orbit_parent, parent_x, orbit_parent_symbol, expansions = full_schreier_orbit(
        source_second, order, tree_word, action_by_symbol, deadline
    )
    orbit = [x for x, value in enumerate(seen) if value]

    # Exact closure audit under every Schreier generator.
    closure_checks = 0
    for point in orbit:
        if time.monotonic() > deadline:
            raise TimeoutError("five-minute cap reached during closure audit")
        for x in order:
            for symbol in SYMBOLS:
                nxt = schreier_image_on_point(
                    point, x, symbol, tree_word, action_by_symbol
                )
                assert seen[nxt]
                closure_checks += 1

    rows = []
    positives = negatives = 0
    for target in frozen["target_rows"]:
        target_first, target_second = target["target_ids"]
        alpha = tree_word[target_first]
        adjusted = apply_word(target_second, inverse_word(alpha), action_by_symbol)
        reachable = bool(seen[adjusted])
        if reachable:
            certificate = orbit_certificate_word(
                adjusted, orbit_parent, parent_x, orbit_parent_symbol, tree_word
            )
            stabilizer_word = expand_schreier_certificate(
                certificate, tree_word, action_by_symbol
            )
            route = stabilizer_word + alpha
            assert apply_word(source_first, route, action_by_symbol) == target_first
            assert apply_word(source_second, route, action_by_symbol) == target_second
            positives += 1
        else:
            certificate = ()
            stabilizer_word = ()
            route = ()
            negatives += 1
        rows.append({
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

    orbit_bitmap_digest = hashlib.sha256(bytes(seen)).hexdigest()
    rows_digest = hashlib.sha256(
        json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    elapsed = time.monotonic() - started
    result = {
        "experiment": "M194 efficient exact Q5 Schreier orbit",
        "repository_base_commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
        "command": "python3 -B schreier_orbit.py --input ../mission-M191.../q5_action.json --output exact_results.json",
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "cap_seconds": cap_seconds,
        "elapsed_seconds": elapsed,
        "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "action": {
            "size": n,
            "digest": action_digest,
            "source_ids": [source_first, source_second],
            "bijections_checked": True,
            "inverse_pairs_checked": True,
        },
        "transversal": {
            "visited": len(order),
            "max_word_length": max(map(len, tree_word)),
            "all_words_replayed": True,
        },
        "stabilizer_orbit": {
            "size": len(orbit),
            "bfs_expansions": expansions,
            "schreier_generators_considered_per_expansion": n * len(SYMBOLS),
            "closure_checks": closure_checks,
            "closed_under_all_schreier_generators": True,
            "orbit_ids": orbit,
            "orbit_bitmap_sha256": orbit_bitmap_digest,
        },
        "classification": {
            "target_count": len(rows),
            "reachable": positives,
            "unreachable": negatives,
            "all_positive_routes_replayed": True,
            "negative_certificate": "adjusted ID absent from exact closed orbit_ids",
            "rows_sha256": rows_digest,
            "rows": rows,
        },
        "scope": "exact finite d=5 only",
    }
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "elapsed_seconds": elapsed,
        "peak_rss_kib": result["peak_rss_kib"],
        "transversal": result["transversal"],
        "stabilizer_orbit": {
            key: result["stabilizer_orbit"][key]
            for key in (
                "size", "bfs_expansions", "closure_checks",
                "closed_under_all_schreier_generators", "orbit_bitmap_sha256"
            )
        },
        "classification": {
            key: result["classification"][key]
            for key in (
                "target_count", "reachable", "unreachable",
                "all_positive_routes_replayed", "rows_sha256"
            )
        },
    }, indent=2, sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("exact_results.json"))
    parser.add_argument("--cap-seconds", type=int, default=300)
    args = parser.parse_args()
    classify(args.input, args.output, args.cap_seconds)


if __name__ == "__main__":
    main()
