#!/usr/bin/env python3
"""Targeted diagonal-Hurwitz correction probe for the 7 d5->d6 pairs.

This is not a Q6 enumeration.  It searches only two radius-r balls for each
named pair endpoint.  Failure to meet is never interpreted negatively.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import time
from collections import deque
from pathlib import Path


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
M205_CHECKER = (
    HERE.parent.parent / "cycle-49" / "mission-M205-m203-fresh-referee"
    / "fresh_locality_referee.py"
)


def load_m205():
    spec = importlib.util.spec_from_file_location("m205_frozen", M205_CHECKER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def conjugate(edge, by):
    x, y = by
    image = lambda z: y if z == x else x if z == y else z
    return tuple(sorted((image(edge[0]), image(edge[1]))))


def hurwitz(word, position, sign):
    a, b = word[position], word[position + 1]
    out = list(word)
    if sign == 1:
        out[position : position + 2] = (b, conjugate(a, b))
    else:
        out[position : position + 2] = (conjugate(b, a), a)
    return tuple(out)


def act_pair(state, generator):
    position, sign = generator
    return tuple(hurwitz(word, position, sign) for word in state)


def replay(state, action_word):
    for generator in action_word:
        state = act_pair(state, generator)
    return state


def ball(start, radius):
    paths = {start: ()}
    queue = deque([(start, 0)])
    m = len(start[0])
    while queue:
        state, depth = queue.popleft()
        if depth == radius:
            continue
        path = paths[state]
        for position in range(m - 1):
            for sign in (1, -1):
                nxt = act_pair(state, (position, sign))
                if nxt not in paths:
                    paths[nxt] = path + ((position, sign),)
                    queue.append((nxt, depth + 1))
    return paths


def meet(source, target, radius):
    forward = ball(source, radius)
    backward = ball(target, radius)
    common = set(forward).intersection(backward)
    if not common:
        return None, len(forward), len(backward)
    middle = min(common, key=lambda x: (len(forward[x]) + len(backward[x]), x))
    suffix = tuple((position, -sign) for position, sign in reversed(backward[middle]))
    route = forward[middle] + suffix
    assert replay(source, route) == target
    return route, len(forward), len(backward)


def serialize_route(route):
    if route is None:
        return None
    return [[position + 1, sign] for position, sign in route]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--radius", type=int, default=4)
    parser.add_argument("--output", default="correction_mitm_results.json")
    args = parser.parse_args()
    assert 0 <= args.radius <= 5

    core = load_m205()
    rows, descriptors = core.reconstruct_rows()
    started = time.perf_counter()
    results = []
    for edit in range(1, 8):
        naive = []
        actual = []
        for pattern in (0, 1):
            tree5, order5, _ = descriptors[5, pattern, 4]
            target5 = core.decode_dps(
                tree5, core.adjacent_value_edit(order5, edit), 5
            )
            naive.append(target5 + ((0, 5), (0, 5)))
            tree6, order6, _ = descriptors[6, pattern, 5]
            actual.append(core.decode_dps(
                tree6, core.adjacent_value_edit(order6, edit), 6
            ))
        route, forward_states, backward_states = meet(
            tuple(naive), tuple(actual), args.radius
        )
        results.append({
            "edit": edit,
            "route": serialize_route(route),
            "route_length": None if route is None else len(route),
            "forward_states": forward_states,
            "backward_states": backward_states,
            "exact_endpoint_replay": route is not None,
        })

    payload = {
        "experiment": "M208 targeted synchronized correction MITM",
        "scope": "seven named d5->d6 pattern pairs; exact physical endpoints",
        "radius_each_side": args.radius,
        "miss_interpretation": "none; a radius miss is not a negative result",
        "rows": results,
        "positive_count": sum(row["route"] is not None for row in results),
        "elapsed_seconds": time.perf_counter() - started,
    }
    (HERE / args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

