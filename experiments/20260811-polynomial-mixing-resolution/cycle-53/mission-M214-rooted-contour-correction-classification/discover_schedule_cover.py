#!/usr/bin/env python3
"""Bounded positive-certificate discovery for M214.

This explores only radius-r balls around one named endpoint pair at a time.
It is not Q6 enumeration.  Misses are never used negatively.  Final claims
must be replayed by a separate deterministic checker.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import deque
from pathlib import Path


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
M212_CHECKER = (
    HERE.parent.parent / "cycle-52" / "mission-M212-m208-fresh-referee"
    / "fresh_rooted_referee.py"
)


def load_core():
    spec = importlib.util.spec_from_file_location("m212_core", M212_CHECKER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def ball(core, start, radius, state_cap):
    paths = {start: ()}
    queue = deque([(start, 0)])
    while queue:
        state, depth = queue.popleft()
        if depth == radius:
            continue
        path = paths[state]
        for position in range(len(state) - 1):
            for sign in (1, -1):
                nxt = core.hurwitz(state, position, sign)
                if nxt not in paths:
                    paths[nxt] = path + ((position, sign),)
                    if len(paths) > state_cap:
                        raise RuntimeError("state cap exceeded")
                    queue.append((nxt, depth + 1))
    return paths


def meet(core, source, target, radius, state_cap):
    forward = ball(core, source, radius, state_cap)
    backward = ball(core, target, radius, state_cap)
    common = set(forward).intersection(backward)
    if not common:
        return None, len(forward), len(backward)
    middle = min(common, key=lambda state: (len(forward[state]) + len(backward[state]), state))
    suffix = tuple((position, -sign) for position, sign in reversed(backward[middle]))
    route = forward[middle] + suffix
    assert core.act(source, route) == target
    return route, len(forward), len(backward)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--radius", type=int, default=7)
    parser.add_argument("--state-cap", type=int, default=500000)
    parser.add_argument("--output", default="schedule_discovery.json")
    args = parser.parse_args()
    assert 0 <= args.radius <= 7

    core = load_core()
    pi5 = (7, 8, 1, 2, 3, 4, 5, 6)
    pi6 = (9, 10, 1, 2, 3, 4, 5, 6, 7, 8)
    trees = [
        tree for tree in core.prufer_trees(5)
        if (1, 5) in tree and sum(5 in edge for edge in tree) == 1
    ]
    endpoints = {}
    for edit in (1, 3, 5):
        for tree_id, tree5 in enumerate(trees):
            endpoints[edit, tree_id] = (
                core.dps_word(tree5, core.swap_values(pi5, edit), 5)
                + ((0, 5), (0, 5)),
                core.dps_word(tree5 | {(1, 6)}, core.swap_values(pi6, edit), 6),
            )

    output = []
    for edit in (1, 3, 5):
        candidates = [core.ROUTES[edit]]
        uncovered = set(range(16))
        while uncovered:
            progress = False
            for route in candidates:
                agreement = {
                    tree_id for tree_id in uncovered
                    if core.act(endpoints[edit, tree_id][0], route)
                    == endpoints[edit, tree_id][1]
                }
                if agreement:
                    output.append({
                        "edit": edit,
                        "seed_tree": None,
                        "route": core.json_route(route),
                        "route_length": len(route),
                        "agreement_tree_ids": sorted(agreement),
                        "forward_states": None,
                        "backward_states": None,
                    })
                    uncovered -= agreement
                    progress = True
            if progress:
                candidates = []
                continue
            seed = min(uncovered)
            route, nf, nb = meet(
                core, endpoints[edit, seed][0], endpoints[edit, seed][1],
                args.radius, args.state_cap,
            )
            if route is None:
                output.append({
                    "edit": edit,
                    "seed_tree": seed,
                    "route": None,
                    "route_length": None,
                    "agreement_tree_ids": [],
                    "forward_states": nf,
                    "backward_states": nb,
                })
                break
            agreement = {
                tree_id for tree_id in uncovered
                if core.act(endpoints[edit, tree_id][0], route)
                == endpoints[edit, tree_id][1]
            }
            assert seed in agreement
            output.append({
                "edit": edit,
                "seed_tree": seed,
                "route": core.json_route(route),
                "route_length": len(route),
                "agreement_tree_ids": sorted(agreement),
                "forward_states": nf,
                "backward_states": nb,
            })
            uncovered -= agreement

    payload = {
        "experiment": "M214 greedy individual-endpoint positive schedule discovery",
        "scope": "48 named odd-edit rows only; no Q6 enumeration",
        "radius_each_side": args.radius,
        "state_cap_per_ball": args.state_cap,
        "miss_interpretation": "none",
        "rows": output,
    }
    (HERE / args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

