#!/usr/bin/env python3
"""Fresh finite referee audit of M122's DPS star cascade.

This checker imports no predecessor experiment code or output.  It rebuilds
the rooted hairy-tree contour, cyclic local closure, signed Hurwitz actions,
full-twist/short routes, compressed-time recovery, and root-capacity ratios
from the definitions.  Finite rows are convention checks and falsifiers, not
proofs of the universal statements.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import subprocess
import time
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


Edge = tuple[int, int]
Word = tuple[Edge, ...]
Vertex = tuple[str, int]
Token = tuple[object, ...]


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return p*q, so (p*q)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def edge_perm(n: int, e: Edge) -> tuple[int, ...]:
    p = list(range(n))
    p[e[0]], p[e[1]] = p[e[1]], p[e[0]]
    return tuple(p)


def evaluate(n: int, word: Word) -> tuple[int, ...]:
    p = tuple(range(n))
    for e in word:
        p = compose(p, edge_perm(n, e))
    return p


def connected(n: int, word: Word) -> bool:
    graph = [[] for _ in range(n)]
    for a, b in word:
        graph[a].append(b)
        graph[b].append(a)
    seen = {0}
    todo = [0]
    while todo:
        a = todo.pop()
        for b in graph[a]:
            if b not in seen:
                seen.add(b)
                todo.append(b)
    return len(seen) == n


def conjugate(a: Edge, b: Edge) -> Edge:
    """Return b*a*b for transpositions a,b."""
    def image(x: int) -> int:
        if x == b[0]:
            return b[1]
        if x == b[1]:
            return b[0]
        return x

    return tuple(sorted((image(a[0]), image(a[1]))))  # type: ignore[return-value]


def hurwitz(word: Word, position: int, sign: int) -> Word:
    """Apply R_position^(sign), with one-based adjacent-pair position."""
    j = position - 1
    a, b = word[j], word[j + 1]
    out = list(word)
    if sign == 1:
        out[j], out[j + 1] = b, conjugate(a, b)
    elif sign == -1:
        out[j], out[j + 1] = conjugate(b, a), a
    else:
        raise ValueError(sign)
    return tuple(out)


def apply_actions(word: Word, actions: tuple[tuple[int, int], ...]) -> Word:
    for position, sign in actions:
        word = hurwitz(word, position, sign)
    return word


def undo_prefix(word: Word, actions: tuple[tuple[int, int], ...]) -> Word:
    for position, sign in reversed(actions):
        word = hurwitz(word, position, -sign)
    return word


def full_actions(length: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        (position, 1)
        for _ in range(length + 1)
        for position in range(2, length + 2)
    )


def short_actions(length: int) -> tuple[tuple[int, int], ...]:
    return (
        tuple((position, 1) for position in range(2, length + 1))
        + ((length + 1, -1),)
        + tuple((position, 1) for position in range(length, 1, -1))
    )


def componentwise_target(source: Word) -> Word:
    h = source[0]
    return source[:2] + tuple(conjugate(u, h) for u in source[2:])


def transpositions(n: int) -> tuple[Edge, ...]:
    return tuple(itertools.combinations(range(n), 2))


def identity_suffix(n: int, suffix: Word) -> bool:
    return evaluate(n, suffix) == tuple(range(n))


def valid_full_source(word: Word) -> bool:
    if len(word) < 4 or word[0] != word[1]:
        return False
    n = 1 + max(max(e) for e in word)
    return identity_suffix(n, word[2:])


def compressed_recovery_counts(
    source: Word, actions: tuple[tuple[int, int], ...]
) -> tuple[list[int], int, int]:
    """Recover sources after deletion of scheduled holding actions.

    For each actual physical edge at compressed time k, try every scheduled
    action time.  Prefix inversion gives at most one source for each such
    scheduled time.  Retain candidates that are legal square-prefix sources
    and for which the proposed time realizes the given edge at compressed
    time k.
    """
    states = [source]
    for action in actions:
        states.append(hurwitz(states[-1], *action))
    events = [
        (scheduled, states[scheduled], states[scheduled + 1])
        for scheduled in range(len(actions))
        if states[scheduled] != states[scheduled + 1]
    ]
    counts = []
    actual_missing = 0
    for compressed, (_actual_t, edge_source, edge_target) in enumerate(events):
        recovered = []
        for scheduled, action in enumerate(actions):
            if hurwitz(edge_source, *action) != edge_target:
                continue
            candidate = undo_prefix(edge_source, actions[:scheduled])
            if not valid_full_source(candidate):
                continue
            candidate_states = [candidate]
            for prefix_action in actions[: scheduled + 1]:
                candidate_states.append(hurwitz(candidate_states[-1], *prefix_action))
            prior_nontrivial = sum(
                candidate_states[j] != candidate_states[j + 1]
                for j in range(scheduled)
            )
            if (
                candidate_states[scheduled] == edge_source
                and candidate_states[scheduled + 1] == edge_target
                and prior_nontrivial == compressed
            ):
                recovered.append(candidate)
        if source not in recovered:
            actual_missing += 1
        counts.append(len(recovered))
    return counts, len(events), actual_missing


def rooted_star_incidence(d: int, swapped: bool):
    """Actual edge incidences of DPS Proposition 3 for the rooted star."""
    m = 2 * d - 2
    labels = list(range(1, m + 1))
    if swapped:
        labels[0], labels[1] = labels[1], labels[0]
    actual: dict[tuple[Vertex, int], Vertex] = {}
    original_black: dict[int, int] = {}
    for i in range(1, d):
        parent = d if i == 1 else 1
        black = ("b", i)
        for label, white_index in zip(labels[2 * i - 2 : 2 * i], (i, parent)):
            white = ("w", white_index)
            actual[(black, label)] = white
            actual[(white, label)] = black
            original_black[label] = i
    return actual, original_black


def outer_contour(actual: dict[tuple[Vertex, int], Vertex], d: int) -> list[Token]:
    """Trace the unique outer contour from vertex rotations.

    White labels increase and black labels decrease in the accepted + mirror.
    A missing incidence emits a loose half-edge; an actual incidence traverses
    one side of the embedded tree edge.
    """
    m = 2 * d - 2
    state: tuple[Vertex, int] = (("w", 1), 1)
    start = state
    seen = set()
    contour: list[Token] = []
    while state not in seen:
        seen.add(state)
        vertex, previous_label = state
        rotation_step = 1 if vertex[0] == "w" else -1
        label = 1 + ((previous_label - 1 + rotation_step) % m)
        neighbor = actual.get((vertex, label))
        if neighbor is None:
            contour.append(("H", vertex[0], vertex[1], label))
            state = (vertex, label)
        else:
            contour.append(("S", "tree"))
            state = (neighbor, label)
    if state != start or len(seen) != (2 * d - 1) * m:
        raise AssertionError(("outer contour", d, len(seen), state))
    return contour


def cyclic_local_closure(contour: list[Token], d: int):
    """Run the DPS local closure directly on a cyclic token ring."""
    ring = list(contour)
    records: list[tuple[int, int, int, int]] = []
    quadrangle_black: dict[int, int] = {}
    while True:
        half_positions = [j for j, token in enumerate(ring) if token[0] == "H"]
        selected = None
        for k, left in enumerate(half_positions):
            right = half_positions[(k + 1) % len(half_positions)]
            if ring[left][1] == "w" and ring[right][1] == "b":
                selected = left, right
                break
        if selected is None:
            break
        left, right = selected
        ring = ring[left:] + ring[:left]
        right = (right - left) % len(ring)
        white, black = ring[0], ring[right]
        if white[3] != black[3]:
            raise AssertionError(("closure label mismatch", white, black))
        if any(token[0] != "S" for token in ring[1:right]):
            raise AssertionError("selected half-edges were not consecutive")
        distance = right - 1
        if distance not in (1, 3):
            raise AssertionError(("closure distance", distance, white, black))
        label = int(white[3])
        records.append((label, distance, int(white[2]), int(black[2])))
        if distance == 3:
            if label in quadrangle_black:
                raise AssertionError(("duplicate quadrangle", label))
            quadrangle_black[label] = int(black[2])
        ring = [("S", "closure")] + ring[right + 1 :]
    unmatched = [token for token in ring if token[0] == "H"]
    m = 2 * d - 2
    if len(unmatched) != m or any(token[1] != "w" for token in unmatched):
        raise AssertionError(("unmatched colors/count", unmatched))
    if sorted(int(token[3]) for token in unmatched) != list(range(1, m + 1)):
        raise AssertionError(("unmatched labels", unmatched))
    return records, quadrangle_black, unmatched


def close_star(d: int, swapped: bool):
    actual, original_black = rooted_star_incidence(d, swapped)
    records, quadrangle_black, unmatched = cyclic_local_closure(
        outer_contour(actual, d), d
    )
    word = tuple(
        tuple(sorted((original_black[label] - 1, quadrangle_black.get(label, d) - 1)))
        for label in range(1, 2 * d - 1)
    )
    return word, records, quadrangle_black, unmatched


def star_formulas(d: int) -> tuple[Word, Word]:
    h = (0, d - 1)
    source = (h, h) + tuple(
        e for k in range(1, d - 1) for e in ((0, k), (0, k))
    )
    target = (h, h) + tuple(
        e for k in range(1, d - 1) for e in ((k, d - 1), (k, d - 1))
    )
    return source, target


def star_row(d: int) -> dict[str, object]:
    source, source_records, source_quads, source_unmatched = close_star(d, False)
    target, target_records, target_quads, target_unmatched = close_star(d, True)
    source_formula, target_formula = star_formulas(d)
    m = 2 * d - 2
    length = m - 2

    source_counts = Counter((label, distance) for label, distance, _, _ in source_records)
    target_counts = Counter((label, distance) for label, distance, _, _ in target_records)
    expected_source = Counter()
    expected_target = Counter()
    for label in range(1, m + 1):
        expected_source[(label, 1)] = d - 2 if label <= 2 else d - 3
        if label >= 3:
            expected_source[(label, 3)] = 1
        expected_target[(label, 1)] = d - 2

    short = short_actions(length)
    full = full_actions(length)
    short_states = [source]
    for action in short:
        short_states.append(hurwitz(short_states[-1], *action))
    full_states = [source]
    for action in full:
        full_states.append(hurwitz(full_states[-1], *action))

    compressed_counts, full_physical_length, compressed_actual_missing = (
        compressed_recovery_counts(source, full)
    )
    hamming = sum(a != b for a, b in zip(source, target))
    stationary = Fraction(1, d)  # coefficient after suppressing |Z_d|^{-1}
    ideal_capacity = stationary * Fraction(1, 4 * (m - 1))
    physical_capacity = ideal_capacity * Fraction(1, d)

    checks = {
        "source_formula": source == source_formula,
        "swapped_formula": target == target_formula,
        "source_closure_table": source_counts == expected_source,
        "swapped_closure_table": target_counts == expected_target,
        "source_quadrangles": source_quads == {label: 1 for label in range(3, m + 1)},
        "swapped_has_no_quadrangle_closure": target_quads == {},
        "unmatched_labels_complete": (
            sorted(int(x[3]) for x in source_unmatched) == list(range(1, m + 1))
            and sorted(int(x[3]) for x in target_unmatched) == list(range(1, m + 1))
        ),
        "endpoints_in_Zd": (
            evaluate(d, source) == tuple(range(d))
            and evaluate(d, target) == tuple(range(d))
            and connected(d, source)
            and connected(d, target)
        ),
        "hamming_2d_minus_4": hamming == 2 * d - 4,
        "lower_bound_d_minus_2": (hamming + 1) // 2 == d - 2,
        "short_endpoint": short_states[-1] == target,
        "short_length_4d_minus_9": len(short) == 4 * d - 9,
        "short_all_off_diagonal": all(a != b for a, b in zip(short_states, short_states[1:])),
        "short_prefix_recovery": all(
            undo_prefix(short_states[t], short[:t]) == source
            for t in range(len(short_states))
        ),
        "short_intermediates_in_Zd": all(
            evaluate(d, state) == tuple(range(d)) and connected(d, state)
            for state in short_states
        ),
        "full_endpoint": full_states[-1] == target,
        "full_scheduled_length": len(full) == length * (length + 1),
        "full_prefix_recovery": all(
            undo_prefix(full_states[t], full[:t]) == source
            for t in range(len(full_states))
        ),
        "full_intermediates_in_Zd": all(
            evaluate(d, state) == tuple(range(d)) and connected(d, state)
            for state in full_states
        ),
        "compressed_recovery_includes_actual": compressed_actual_missing == 0,
        "compressed_recovery_bound": (
            not compressed_counts or max(compressed_counts) <= len(full)
        ),
        "root_capacity_ratio_d": ideal_capacity / physical_capacity == d,
        "short_single_demand_bound": d * len(short) == d * (4 * d - 9),
        "full_single_demand_bound": d * len(full) == d * (2 * d - 4) * (2 * d - 3),
    }
    return {
        "d": d,
        "m": m,
        "checks": checks,
        "failures": [name for name, ok in checks.items() if not ok],
        "factor_hamming_distance": hamming,
        "hurwitz_hamming_lower_bound": (hamming + 1) // 2,
        "short_route_length": len(short),
        "full_scheduled_length": len(full),
        "full_physical_length_after_holds_deleted": full_physical_length,
        "full_deleted_self_loops": len(full) - full_physical_length,
        "compressed_recovery_max_candidates": max(compressed_counts, default=0),
        "compressed_recovery_candidate_histogram": {
            str(k): v for k, v in sorted(Counter(compressed_counts).items())
        },
        "ideal_capacity_coefficient_without_Z_inverse": str(ideal_capacity),
        "lifted_physical_capacity_coefficient_without_Z_inverse": str(physical_capacity),
        "capacity_ratio": str(ideal_capacity / physical_capacity),
        "full_scheduled_single_demand_bound": d * len(full),
        "short_single_demand_bound": d * len(short),
        "source_word": [list(e) for e in source] if d <= 5 else None,
        "swapped_word": [list(e) for e in target] if d <= 5 else None,
    }


def exhaustive_small_braids() -> dict[str, object]:
    n = 4
    edges = transpositions(n)
    counts = Counter()
    failures = Counter()
    for length in (2, 4):
        actions_full = full_actions(length)
        actions_short = short_actions(length)
        suffixes = tuple(
            word
            for word in itertools.product(edges, repeat=length)
            if identity_suffix(n, word)
        )
        counts[(length, "identity_suffixes")] = len(suffixes)
        for h in edges:
            for suffix in suffixes:
                source = (h, h) + suffix
                desired = componentwise_target(source)
                counts[(length, "full_sources")] += 1
                if apply_actions(source, actions_full) != desired:
                    failures[(length, "full_endpoint")] += 1
                states = [source]
                for action in actions_full:
                    states.append(hurwitz(states[-1], *action))
                if any(undo_prefix(states[t], actions_full[:t]) != source for t in range(len(states))):
                    failures[(length, "full_prefix_recovery")] += 1
                last = suffix[-1]
                common = len(set(h) & set(last))
                if h == last or common == 1:
                    counts[(length, "short_applicable_sources")] += 1
                    if apply_actions(source, actions_short) != desired:
                        failures[(length, "short_endpoint")] += 1
    return {
        "ambient_group": "S_4",
        "counts": {f"L={length}:{name}": value for (length, name), value in sorted(counts.items())},
        "failures": {f"L={length}:{name}": value for (length, name), value in sorted(failures.items())},
    }


def disjoint_example() -> dict[str, object]:
    h = (0, 3)
    u = (1, 2)
    source = (h, h, u, u)
    desired = componentwise_target(source)
    short = apply_actions(source, short_actions(2))
    full = apply_actions(source, full_actions(2))
    return {
        "source": [list(e) for e in source],
        "desired": [list(e) for e in desired],
        "short_endpoint": [list(e) for e in short],
        "full_endpoint": [list(e) for e in full],
        "short_fails": short != desired,
        "full_succeeds": full == desired,
        "support_connected": connected(4, source),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-d", type=int, default=3)
    parser.add_argument("--max-d", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.min_d < 3 or args.max_d < args.min_d:
        raise SystemExit("require 3 <= min-d <= max-d")
    started = time.perf_counter()
    rows = [star_row(d) for d in range(args.min_d, args.max_d + 1)]
    exhaustive = exhaustive_small_braids()
    disjoint = disjoint_example()
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception:
        commit = None
    payload = {
        "experiment": "M126 independent M122 star-cascade referee audit",
        "claim_tested": (
            "The rooted DPS star/id adjacent-value edit has the two universal endpoint "
            "formulas, factor cascade/lower bound, universal full twist, conditional "
            "short braid, compressed source recovery, and one-root-refresh capacity loss."
        ),
        "metadata": {
            "repository_commit": commit,
            "python": platform.python_version(),
            "dependencies": {},
            "seed": None,
            "deterministic": True,
            "imports_predecessor_code_or_output": False,
            "convention": "(pq)(x)=p(q(x)); displayed factors multiply left-to-right",
            "elapsed_seconds": time.perf_counter() - started,
        },
        "parameters": {"min_d": args.min_d, "max_d": args.max_d},
        "rows": rows,
        "exhaustive_small_braid_audit": exhaustive,
        "disjoint_last_factor_counterexample": disjoint,
        "all_finite_checks_pass": (
            all(not row["failures"] for row in rows)
            and not exhaustive["failures"]
            and disjoint["short_fails"]
            and disjoint["full_succeeds"]
            and not disjoint["support_connected"]
        ),
        "scope_warning": (
            "Exact finite convention/falsification audit only. Universal claims require "
            "the separate symbolic proof. No all-ideal-edge congestion, physical gap, "
            "arbitrary-product Gamma_0 result, or heat-bath mixing result follows."
        ),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

