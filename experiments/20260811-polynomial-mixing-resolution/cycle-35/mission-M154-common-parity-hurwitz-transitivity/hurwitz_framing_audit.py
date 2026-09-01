#!/usr/bin/env python3
"""Exact bounded falsifier for literal versus inner Hurwitz orbits.

This checker is independent of predecessor modules and output.  It closes the
entire signed-Hurwitz action on the 24 connected minimal identity words in
S_3, decomposes that equivariant action over global-conjugacy orbits, and
checks diagonal orbits of generating pairs.  The all-rank statements in the
accompanying proof note are proved symbolically and are not inferred from
these finite rows.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
import subprocess
from collections import Counter, defaultdict, deque
from pathlib import Path

from sympy.combinatorics import Permutation as SympyPermutation
from sympy.combinatorics import PermutationGroup


Permutation = tuple[int, ...]
Edge = tuple[int, int]
Word = tuple[Edge, ...]
Action = tuple[int, ...]


def multiply(p: Permutation, q: Permutation) -> Permutation:
    """Return pq under (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def sign(p: Permutation) -> int:
    inversions = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return inversions & 1


def edge_map(d: int, edge: Edge) -> Permutation:
    out = list(range(d))
    a, b = edge
    out[a], out[b] = out[b], out[a]
    return tuple(out)


def evaluate(d: int, word: Word) -> Permutation:
    out = tuple(range(d))
    for edge in word:
        out = multiply(out, edge_map(d, edge))
    return out


def connected(d: int, word: Word) -> bool:
    adjacency = [set() for _ in range(d)]
    for a, b in word:
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen = {0}
    queue = [0]
    while queue:
        a = queue.pop()
        for b in adjacency[a] - seen:
            seen.add(b)
            queue.append(b)
    return len(seen) == d


def relabel_edge(edge: Edge, rho: Permutation) -> Edge:
    return tuple(sorted((rho[edge[0]], rho[edge[1]])))


def relabel_word(word: Word, rho: Permutation) -> Word:
    return tuple(relabel_edge(edge, rho) for edge in word)


def conjugate_edge(edge: Edge, by: Edge) -> Edge:
    a, b = edge
    x, y = by

    def image(z: int) -> int:
        if z == x:
            return y
        if z == y:
            return x
        return z

    return tuple(sorted((image(a), image(b))))


def hurwitz(word: Word, slot: int, direction: int) -> Word:
    a, b = word[slot : slot + 2]
    out = list(word)
    if direction == 1:
        out[slot : slot + 2] = (b, conjugate_edge(a, b))
    elif direction == -1:
        out[slot : slot + 2] = (conjugate_edge(b, a), a)
    else:
        raise ValueError(direction)
    return tuple(out)


def brute_target(d: int) -> tuple[Word, ...]:
    edges = tuple(itertools.combinations(range(d), 2))
    identity = tuple(range(d))
    m = 2 * d - 2
    return tuple(
        word
        for word in itertools.product(edges, repeat=m)
        if evaluate(d, word) == identity and connected(d, word)
    )


def compose_action(left: Action, right: Action) -> Action:
    return tuple(left[right[j]] for j in range(len(right)))


def close_action(words: tuple[Word, ...]) -> tuple[tuple[Action, ...], tuple[Action, ...]]:
    index = {word: j for j, word in enumerate(words)}
    generators = tuple(
        tuple(index[hurwitz(word, slot, direction)] for word in words)
        for slot in range(len(words[0]) - 1)
        for direction in (1, -1)
    )
    identity = tuple(range(len(words)))
    actions = {identity}
    queue = deque([identity])
    while queue:
        action = queue.popleft()
        for generator in generators:
            nxt = compose_action(generator, action)
            if nxt not in actions:
                actions.add(nxt)
                queue.append(nxt)
    return tuple(sorted(actions)), generators


def global_orbit_data(d: int, words: tuple[Word, ...]):
    permutations = tuple(itertools.permutations(range(d)))
    index = {word: j for j, word in enumerate(words)}
    canonical_word = {word: min(relabel_word(word, rho) for rho in permutations) for word in words}
    reps = tuple(sorted(set(canonical_word.values())))
    rep_number = {word: j for j, word in enumerate(reps)}
    orbit_of = tuple(rep_number[canonical_word[word]] for word in words)
    transporter = {}
    for rep_id, rep in enumerate(reps):
        for rho in permutations:
            target = relabel_word(rep, rho)
            key = (rep_id, index[target])
            assert key not in transporter
            transporter[key] = rho
    return permutations, index, reps, orbit_of, transporter


def action_voltage_rows(
    actions: tuple[Action, ...],
    words: tuple[Word, ...],
    index: dict[Word, int],
    reps: tuple[Word, ...],
    orbit_of: tuple[int, ...],
    transporter: dict[tuple[int, int], Permutation],
):
    quotient_to_voltages: dict[tuple[int, ...], set[tuple[int, ...]]] = defaultdict(set)
    decorated = []
    for action in actions:
        quotient = []
        parity_voltage = []
        full_transporters = []
        for source_orbit, rep in enumerate(reps):
            target_index = action[index[rep]]
            target_orbit = orbit_of[target_index]
            quotient.append(target_orbit)
            rho = transporter[(target_orbit, target_index)]
            parity_voltage.append(sign(rho))
            full_transporters.append(rho)
        q = tuple(quotient)
        voltage = tuple(parity_voltage)
        quotient_to_voltages[q].add(voltage)
        decorated.append((action, q, voltage, tuple(full_transporters)))
    voltage_fibers = Counter(len(v) for v in quotient_to_voltages.values())
    voltage_weight_histogram = Counter(sum(v) for values in quotient_to_voltages.values() for v in values)
    return decorated, quotient_to_voltages, voltage_fibers, voltage_weight_histogram


def diagonal_pair_orbits(actions: tuple[Action, ...], orbit_of: tuple[int, ...]):
    states = tuple(
        (a, b)
        for a in range(len(orbit_of))
        for b in range(len(orbit_of))
        if orbit_of[a] != orbit_of[b]
    )
    unseen = set(states)
    orbits = []
    while unseen:
        seed = min(unseen)
        orbit = {(action[seed[0]], action[seed[1]]) for action in actions}
        unseen.difference_update(orbit)
        orbits.append(tuple(sorted(orbit)))
    return tuple(sorted(orbits, key=lambda orbit: orbit[0]))


def explicit_inner_conjugation_check(d: int, words: tuple[Word, ...]):
    """Verify the universal braid formula on all bounded words/factors.

    Apply R_(m-1),...,R_1 to move the last factor left, then R_1,...,R_(m-1)
    to rotate it back.  For a product-one word the net result is simultaneous
    conjugation by the last factor.
    """
    failures = []
    for word in words:
        moved = word
        for slot in range(len(word) - 2, -1, -1):
            moved = hurwitz(moved, slot, 1)
        for slot in range(len(word) - 1):
            moved = hurwitz(moved, slot, 1)
        expected = tuple(conjugate_edge(edge, word[-1]) for edge in word)
        if moved != expected:
            failures.append({"word": word, "observed": moved, "expected": expected})
    return failures


def canonical_word(word: Word, permutations: tuple[Permutation, ...]) -> Word:
    return min(relabel_word(word, rho) for rho in permutations)


def permutation_cycle_histogram(action: Action) -> Counter:
    unseen = set(range(len(action)))
    histogram = Counter()
    while unseen:
        start = min(unseen)
        point = start
        length = 0
        while point in unseen:
            unseen.remove(point)
            point = action[point]
            length += 1
        histogram[length] += 1
    return histogram


def permutation_parity(action: Action) -> int:
    cycles = sum(permutation_cycle_histogram(action).values())
    return (len(action) - cycles) & 1


def quotient_component_audit(d: int):
    """Close one exact Hurwitz component modulo global S_d conjugacy."""
    permutations = tuple(itertools.permutations(range(d)))
    m = 2 * d - 2
    star = tuple(edge for v in range(1, d) for edge in ((0, v), (0, v)))
    assert len(star) == m and evaluate(d, star) == tuple(range(d)) and connected(d, star)
    start = canonical_word(star, permutations)
    states = {start}
    queue = deque([start])
    while queue:
        word = queue.popleft()
        for slot in range(m - 1):
            for direction in (1, -1):
                nxt = canonical_word(hurwitz(word, slot, direction), permutations)
                if nxt not in states:
                    states.add(nxt)
                    queue.append(nxt)
    ordered = tuple(sorted(states))
    index = {word: j for j, word in enumerate(ordered)}
    generator_rows = []
    actions = []
    for slot in range(m - 1):
        action = tuple(
            index[canonical_word(hurwitz(word, slot, 1), permutations)] for word in ordered
        )
        actions.append(action)
        histogram = permutation_cycle_histogram(action)
        generator_rows.append(
            {
                "slot": slot + 1,
                "parity": permutation_parity(action),
                "cycle_histogram": dict(sorted(histogram.items())),
            }
        )
    expected_quotient_size = d ** (d - 3) * math.factorial(m) // math.factorial(d)
    group = PermutationGroup([SympyPermutation(list(action)) for action in actions])
    return {
        "d": d,
        "m": m,
        "component_size": len(ordered),
        "accepted_DPS_quotient_size": expected_quotient_size,
        "component_exhausts_quotient_using_accepted_DPS_count": len(ordered) == expected_quotient_size,
        "transitive": group.is_transitive(),
        "primitive": group.is_primitive(),
        "positive_generator_rows": generator_rows,
        "all_positive_generators_even": all(row["parity"] == 0 for row in generator_rows),
    }


def pair_conjugation_tests(
    decorated,
    reps: tuple[Word, ...],
    index: dict[Word, int],
    permutations: tuple[Permutation, ...],
):
    even = tuple(rho for rho in permutations if sign(rho) == 0)
    odd = tuple(rho for rho in permutations if sign(rho) == 1)
    source = (index[reps[0]], index[reps[1]])
    targets = {
        "even_even": (index[relabel_word(reps[0], even[0])], index[relabel_word(reps[1], even[0])]),
        "odd_odd": (index[relabel_word(reps[0], odd[0])], index[relabel_word(reps[1], odd[0])]),
        "even_odd": (index[relabel_word(reps[0], even[0])], index[relabel_word(reps[1], odd[0])]),
        "odd_even": (index[relabel_word(reps[0], odd[0])], index[relabel_word(reps[1], even[0])]),
    }
    reached = {(action[source[0]], action[source[1]]) for action, *_ in decorated}
    return {
        name: {"target": target, "reachable_by_literal_braid": target in reached}
        for name, target in targets.items()
    }


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="results.json")
    args = parser.parse_args()
    mission = Path(__file__).resolve().parent

    d = 3
    words = brute_target(d)
    actions, generators = close_action(words)
    permutations, index, reps, orbit_of, transporter = global_orbit_data(d, words)
    decorated, quotient_to_voltages, voltage_fibers, voltage_weights = action_voltage_rows(
        actions, words, index, reps, orbit_of, transporter
    )
    pair_orbits = diagonal_pair_orbits(actions, orbit_of)
    quotient_image = set(q for _a, q, _v, _t in decorated)

    payload = {
        "experiment": "M154 literal/inner Hurwitz framing audit",
        "target": "Hurwitz orbits of product-one generating C_(d,s)-factorizations; not a sampler",
        "composition_convention": "(pq)(x)=p(q(x)); displayed factors multiply left-to-right",
        "hurwitz_convention": "R_j(a,b)=(b,b^-1 a b), with inverse also included",
        "repository_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "python": platform.python_version(),
        "dependencies": {"sympy": __import__("sympy").__version__},
        "seed": None,
        "command": "python3 -B hurwitz_framing_audit.py --output results.json",
        "d3": {
            "physical_words": len(words),
            "global_conjugacy_orbits": len(reps),
            "global_orbit_sizes": dict(sorted(Counter(orbit_of).items())),
            "signed_hurwitz_generators": len(generators),
            "action_image_order": len(actions),
            "quotient_action_image_order": len(quotient_image),
            "quotient_voltage_fiber_size_histogram": dict(sorted(voltage_fibers.items())),
            "parity_voltage_weight_histogram": dict(sorted(voltage_weights.items())),
            "generating_ordered_pair_states": sum(map(len, pair_orbits)),
            "generating_ordered_pair_orbit_count": len(pair_orbits),
            "generating_ordered_pair_orbit_sizes": sorted(map(len, pair_orbits)),
            "representative_conjugation_reachability": pair_conjugation_tests(
                decorated, reps, index, permutations
            ),
            "explicit_inner_conjugation_formula_failures": explicit_inner_conjugation_check(d, words),
        },
        "quotient_components": [quotient_component_audit(rank) for rank in (3, 4, 5)],
        "predecessor_files_read_only": {
            "M137_report_sha256": sha256(
                mission.parents[1] / "cycle-31" / "mission-M137-m135-fresh-referee" / "report.md"
            ),
            "M150_report_sha256": sha256(
                mission.parents[1] / "cycle-34" / "mission-M150-dps-lifting-invariant" / "report.md"
            ),
        },
    }

    assert len(words) == 24
    assert len(actions) == 216
    assert len(reps) == 4
    assert not payload["d3"]["explicit_inner_conjugation_formula_failures"]
    assert all(row["component_exhausts_quotient_using_accepted_DPS_count"] for row in payload["quotient_components"])
    output = mission / args.output
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["d3"], sort_keys=True))


if __name__ == "__main__":
    main()
