#!/usr/bin/env python3
"""Deterministic audit of the M122 DPS star-cascade theorem.

The universal proof is in ``star_cascade_obstruction.md``.  This script is a
finite convention/falsification audit.  It imports no predecessor code.
"""

from __future__ import annotations

import argparse
import json
import platform
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


Edge = tuple[int, int]
Word = tuple[Edge, ...]


@dataclass(frozen=True)
class Half:
    color: str
    vertex: int
    label: int


@dataclass(frozen=True)
class Side:
    kind: str


def conjugate(a: Edge, b: Edge) -> Edge:
    """Return b*a*b for transpositions a,b."""
    def image(x: int) -> int:
        if x == b[0]:
            return b[1]
        if x == b[1]:
            return b[0]
        return x

    return tuple(sorted((image(a[0]), image(a[1]))))  # type: ignore[return-value]


def hurwitz(word: Word, pair_position: int, sign: int) -> Word:
    """Apply R_i or R_i^-1; pair_position is one based."""
    i = pair_position - 1
    a, b = word[i], word[i + 1]
    out = list(word)
    if sign == 1:
        out[i], out[i + 1] = b, conjugate(a, b)
    elif sign == -1:
        out[i], out[i + 1] = conjugate(b, a), a
    else:
        raise ValueError(sign)
    return tuple(out)


def evaluate(d: int, word: Word) -> tuple[int, ...]:
    """Factors multiply left-to-right under (pq)(x)=p(q(x))."""
    p = list(range(d))
    for a, b in word:
        p[a], p[b] = p[b], p[a]
    # ``p`` above tracks right multiplication by transpositions in this
    # convention because a transposition swaps the two image entries.
    return tuple(p)


def connected(d: int, word: Word) -> bool:
    adj = [[] for _ in range(d)]
    for a, b in word:
        adj[a].append(b)
        adj[b].append(a)
    seen = {0}
    todo = [0]
    while todo:
        a = todo.pop()
        for b in adj[a]:
            if b not in seen:
                seen.add(b)
                todo.append(b)
    return len(seen) == d


def star_incidence(d: int, swap_first_values: bool):
    """Rooted DPS Hurwitz tree for the star centered at y_1.

    Vertices and labels are one based in this closure routine.  The white root
    is y_d.  Proposition 3 inserts x_i on y_i's first edge toward y_d.
    """
    m = 2 * d - 2
    pi = list(range(1, m + 1))
    if swap_first_values:
        pi[0], pi[1] = pi[1], pi[0]
    incidence = defaultdict(dict)
    original_black = {}
    for i in range(1, d):
        parent = d if i == 1 else 1
        for label, white in ((pi[2 * i - 2], i), (pi[2 * i - 1], parent)):
            bv = ("b", i)
            wv = ("w", white)
            incidence[bv][label] = wv
            incidence[wv][label] = bv
            original_black[label] = i
    return incidence, original_black


def hairy_boundary(incidence, d: int):
    """The accepted + mirror of the DPS hairy-tree outer contour."""
    m = 2 * d - 2
    start = (("w", 1), 1)
    state = start
    tokens = []
    seen = set()
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        clockwise_step = 1 if vertex[0] == "w" else -1
        label = 1 + ((incoming - 1 + clockwise_step) % m)
        if label in incidence[vertex]:
            tokens.append(Side("tree"))
            state = (incidence[vertex][label], label)
        else:
            tokens.append(Half(vertex[0], vertex[1], label))
            state = (vertex, label)
    if state != start or len(tokens) != (2 * d - 1) * m:
        raise AssertionError("bad hairy contour")
    return tokens


def close_hairy(tokens, d: int):
    """DPS LIFO local closure, recording all digon/quadrangle closures."""
    tokens = list(tokens)
    closures = []
    other_black = {}
    while True:
        hp = [i for i, token in enumerate(tokens) if isinstance(token, Half)]
        pair = None
        for k, wi in enumerate(hp):
            w = tokens[wi]
            bj = hp[(k + 1) % len(hp)]
            b = tokens[bj]
            if w.color == "w" and b.color == "b":
                pair = (wi, bj)
                break
        if pair is None:
            break
        wi, bj = pair
        tokens = tokens[wi:] + tokens[:wi]
        bj = (bj - wi) % len(tokens)
        w, b = tokens[0], tokens[bj]
        if w.label != b.label:
            raise AssertionError(("unequal labels", w, b))
        distance = sum(isinstance(x, Side) for x in tokens[1:bj])
        if distance not in (1, 3):
            raise AssertionError(("bad distance", distance, w, b))
        closures.append((w.label, distance, w.vertex, b.vertex))
        if distance == 3:
            if w.label in other_black:
                raise AssertionError("duplicate quadrangle")
            other_black[w.label] = b.vertex
        tokens = [Side("closure")] + tokens[bj + 1 :]
    remaining = [x for x in tokens if isinstance(x, Half)]
    m = 2 * d - 2
    if len(remaining) != m or any(x.color != "w" for x in remaining):
        raise AssertionError("bad unmatched white set")
    if sorted(x.label for x in remaining) != list(range(1, m + 1)):
        raise AssertionError("bad unmatched labels")
    return closures, other_black, remaining


def dps_star_word(d: int, swap_first_values: bool):
    incidence, original_black = star_incidence(d, swap_first_values)
    closures, other_black, remaining = close_hairy(hairy_boundary(incidence, d), d)
    word = []
    for label in range(1, 2 * d - 1):
        a = original_black[label]
        b = other_black.get(label, d)
        word.append(tuple(sorted((a - 1, b - 1))))
    return tuple(word), closures, other_black, remaining


def expected_words(d: int) -> tuple[Word, Word]:
    h = (0, d - 1)
    source = (h, h) + tuple(e for k in range(1, d - 1) for e in ((0, k), (0, k)))
    target = (h, h) + tuple(
        e for k in range(1, d - 1) for e in ((k, d - 1), (k, d - 1))
    )
    return source, target


def braid_actions(L: int) -> tuple[tuple[int, int], ...]:
    return (
        tuple((i, 1) for i in range(2, L + 1))
        + ((L + 1, -1),)
        + tuple((i, 1) for i in range(L, 1, -1))
    )


def full_twist_actions(L: int) -> tuple[tuple[int, int], ...]:
    """Full twist on positions 2,...,L+2: (R_2...R_(L+1))^(L+1)."""
    return tuple((i, 1) for _ in range(L + 1) for i in range(2, L + 2))


def invert_prefix(state: Word, actions: tuple[tuple[int, int], ...]) -> Word:
    for position, sign in reversed(actions):
        state = hurwitz(state, position, -sign)
    return state


def audit_row(d: int):
    source_formula, target_formula = expected_words(d)
    source, source_closures, source_other, source_remaining = dps_star_word(d, False)
    target, target_closures, target_other, target_remaining = dps_star_word(d, True)
    m = 2 * d - 2
    L = m - 2

    closure_source = Counter((label, distance) for label, distance, _, _ in source_closures)
    closure_target = Counter((label, distance) for label, distance, _, _ in target_closures)
    expected_source_closure = Counter()
    expected_target_closure = Counter()
    for label in range(1, m + 1):
        expected_source_closure[(label, 1)] = d - 2 if label <= 2 else d - 3
        if label >= 3:
            expected_source_closure[(label, 3)] = 1
        expected_target_closure[(label, 1)] = d - 2

    actions = braid_actions(L)
    state = source
    recovery_failures = 0
    identity_failures = 0
    support_failures = 0
    diagonal_action_failures = 0
    for t, action in enumerate(actions):
        if invert_prefix(state, actions[:t]) != source:
            recovery_failures += 1
        new_state = hurwitz(state, *action)
        if new_state == state:
            diagonal_action_failures += 1
        state = new_state
        if evaluate(d, state) != tuple(range(d)):
            identity_failures += 1
        if not connected(d, state):
            support_failures += 1
        if invert_prefix(state, actions[: t + 1]) != source:
            recovery_failures += 1

    full_actions = full_twist_actions(L)
    full_state = source
    full_recovery_failures = 0
    full_identity_failures = 0
    full_support_failures = 0
    full_nontrivial_actions = 0
    for t, action in enumerate(full_actions):
        if invert_prefix(full_state, full_actions[:t]) != source:
            full_recovery_failures += 1
        new_state = hurwitz(full_state, *action)
        full_nontrivial_actions += new_state != full_state
        full_state = new_state
        if evaluate(d, full_state) != tuple(range(d)):
            full_identity_failures += 1
        if not connected(d, full_state):
            full_support_failures += 1
        if invert_prefix(full_state, full_actions[: t + 1]) != source:
            full_recovery_failures += 1

    differing = [i + 1 for i, (a, b) in enumerate(zip(source, target)) if a != b]
    failures = []
    checks = {
        "source_dps_formula": source == source_formula,
        "target_dps_formula": target == target_formula,
        "source_closure_table": closure_source == expected_source_closure,
        "target_closure_table": closure_target == expected_target_closure,
        "source_quadrangle_black": source_other == {label: 1 for label in range(3, m + 1)},
        "target_has_no_distance_three_closure": target_other == {},
        "unmatched_label_sets": (
            sorted(x.label for x in source_remaining) == list(range(1, m + 1))
            and sorted(x.label for x in target_remaining) == list(range(1, m + 1))
        ),
        "source_identity_connected": evaluate(d, source) == tuple(range(d)) and connected(d, source),
        "target_identity_connected": evaluate(d, target) == tuple(range(d)) and connected(d, target),
        "hamming_formula": len(differing) == 2 * d - 4 and differing == list(range(3, m + 1)),
        "braid_endpoint": state == target,
        "braid_length_formula": len(actions) == 4 * d - 9,
        "all_intermediates_identity": identity_failures == 0,
        "all_intermediates_connected": support_failures == 0,
        "all_actions_off_diagonal": diagonal_action_failures == 0,
        "prefix_recovery_unique": recovery_failures == 0,
        "full_twist_endpoint": full_state == target,
        "full_twist_scheduled_length_formula": len(full_actions) == L * (L + 1),
        "full_twist_intermediates_identity": full_identity_failures == 0,
        "full_twist_intermediates_connected": full_support_failures == 0,
        "full_twist_prefix_recovery_unique": full_recovery_failures == 0,
    }
    failures.extend(name for name, ok in checks.items() if not ok)
    return {
        "d": d,
        "m": m,
        "checks": checks,
        "failures": failures,
        "factor_hamming_distance": len(differing),
        "differing_one_based_positions": differing,
        "universal_hurwitz_path_lower_bound": (len(differing) + 1) // 2,
        "displayed_braid_path_length": len(actions),
        "full_twist_scheduled_length": len(full_actions),
        "full_twist_nontrivial_action_count": full_nontrivial_actions,
        "closure_count": len(source_closures),
        "source_distance_one_closures": sum(v for (lab, dist), v in closure_source.items() if dist == 1),
        "source_distance_three_closures": sum(v for (lab, dist), v in closure_source.items() if dist == 3),
        "target_distance_one_closures": sum(v for (lab, dist), v in closure_target.items() if dist == 1),
        "target_distance_three_closures": sum(v for (lab, dist), v in closure_target.items() if dist == 3),
        "source_word": [list(e) for e in source] if d <= 5 else None,
        "target_word": [list(e) for e in target] if d <= 5 else None,
    }


def disjoint_counterexample():
    h = (0, 3)
    u = (1, 2)
    source = (h, h, u, u)
    expected = source  # h*u*h=u when h and u are disjoint
    short_state = source
    short_actions = braid_actions(2)
    for action in short_actions:
        short_state = hurwitz(short_state, *action)
    full_state = source
    full_actions = full_twist_actions(2)
    for action in full_actions:
        full_state = hurwitz(full_state, *action)
    return {
        "h": list(h),
        "U": [list(u), list(u)],
        "short_actions": [[position, sign] for position, sign in short_actions],
        "short_actual_endpoint": [list(e) for e in short_state],
        "claimed_conjugated_endpoint": [list(e) for e in expected],
        "short_endpoints_differ": short_state != expected,
        "full_twist_actions": [[position, sign] for position, sign in full_actions],
        "full_twist_endpoint": [list(e) for e in full_state],
        "full_twist_succeeds": full_state == expected,
        "note": (
            "This refutes dropping the last-factor incidence hypothesis from the shorter "
            "2L-1 word only; the universal full twist succeeds. It is not a Z_d counterexample."
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-d", type=int, default=3)
    parser.add_argument("--max-d", type=int, default=24)
    parser.add_argument("--output", type=Path, default=Path("star_cascade_results.json"))
    args = parser.parse_args()
    if args.min_d < 3 or args.max_d < args.min_d:
        raise SystemExit("require 3 <= min-d <= max-d")
    started = time.perf_counter()
    rows = [audit_row(d) for d in range(args.min_d, args.max_d + 1)]
    counterexample = disjoint_counterexample()
    payload = {
        "experiment": "M122 exact DPS star-cascade convention audit",
        "claim_tested": (
            "The rooted DPS star/id adjacent-value edit has the displayed linear cascade, "
            "and square-prefix conjugation has a universal full-twist route plus a shorter "
            "shared-endpoint route."
        ),
        "commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
        "argv": sys.argv,
        "python": platform.python_version(),
        "nonstandard_dependencies": {},
        "deterministic": True,
        "seed": None,
        "elapsed_seconds": time.perf_counter() - started,
        "all_finite_checks_pass": all(not row["failures"] for row in rows),
        "disjoint_last_factor_counterexample": counterexample,
        "scope_warning": (
            "Finite checks only. The universal contour and braid proofs are in the proof note. "
            "No all-ideal-edge congestion or rooted-product comparison is claimed."
        ),
        "rows": rows,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
