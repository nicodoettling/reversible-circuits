#!/usr/bin/env python3
"""Exact small-case stabilizer-voltage audit for M163.

The checker hash-gates the accepted clean-room M158 primitives, constructs
the parity cocycle directly from canonical representatives, exhausts d=3
through width four, and audits only the accepted d=4 width-two witness.  It
does not close a d=5 permutation group or make an asymptotic inference.
"""

from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import platform
import subprocess
from collections import Counter, defaultdict, deque
from pathlib import Path


M158_SHA256 = "0189310b6108bef9fe3b687e6131d7a70e577d523766680154e0f9b91e8c10e9"


def load_m158(root: Path):
    path = root / (
        "experiments/20260811-polynomial-mixing-resolution/cycle-36/"
        "mission-M158-m154-fresh-referee/independent_referee.py"
    )
    observed = hashlib.sha256(path.read_bytes()).hexdigest()
    assert observed == M158_SHA256
    spec = importlib.util.spec_from_file_location("m158_frozen", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module, path, observed


def component_with_voltage(m158, d: int):
    """Return canonical quotient states and signed generator cocycle arrays."""
    states, positive = m158.quotient_component(d)
    relabelings = tuple(itertools.permutations(range(d)))
    index = {word: i for i, word in enumerate(states)}
    actions = []
    voltages = []
    labels = []
    for slot in range(2 * d - 3):
        for direction in (1, -1):
            action = []
            voltage = []
            for word in states:
                raw = m158.hurwitz_edge(word, slot, direction)
                target = m158.canonical(raw, relabelings)
                action.append(index[target])
                transporters = [
                    rho
                    for rho in relabelings
                    if m158.word_relabel(target, rho) == raw
                ]
                assert len(transporters) == 1
                voltage.append(m158.perm_sign(transporters[0]))
            actions.append(tuple(action))
            voltages.append(tuple(voltage))
            labels.append((slot + 1, direction))
    for slot, action in enumerate(positive):
        assert tuple(actions[2 * slot]) == tuple(action)
    return states, tuple(actions), tuple(voltages), tuple(labels)


def relative_mask(bits: tuple[int, ...]) -> int:
    if not bits:
        return 0
    return sum((bits[i] ^ bits[0]) << (i - 1) for i in range(1, len(bits)))


def step_tuple(qtuple, mask, action, voltage):
    bits = tuple(voltage[q] for q in qtuple)
    return tuple(action[q] for q in qtuple), mask ^ relative_mask(bits)


def augmented_orbit(seed, actions, voltages):
    start = (tuple(seed), 0)
    seen = {start}
    todo = deque([start])
    while todo:
        qtuple, mask = todo.popleft()
        for action, voltage in zip(actions, voltages):
            nxt = step_tuple(qtuple, mask, action, voltage)
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return seen


def equality_pattern(qtuple):
    labels = {}
    return tuple(labels.setdefault(q, len(labels)) for q in qtuple)


def mask_label(mask: int, width: int) -> str:
    return format(mask, f"0{max(width - 1, 1)}b") if width > 1 else "0"


def d3_exhaustive(m158):
    states, actions, voltages, labels = component_with_voltage(m158, 3)
    assert len(states) == 4
    rows = []
    distinct_summary = []
    for width in range(1, 5):
        by_pattern = defaultdict(Counter)
        distinct_vsets = Counter()
        max_augmented = 0
        for qtuple in itertools.product(range(len(states)), repeat=width):
            component = augmented_orbit(qtuple, actions, voltages)
            vst = frozenset(mask for point, mask in component if point == qtuple)
            quotient_size = len({point for point, _ in component})
            augmented_size = len(component)
            assert augmented_size == quotient_size * len(vst)
            max_augmented = max(max_augmented, augmented_size)
            key = ",".join(mask_label(v, width) for v in sorted(vst))
            by_pattern[str(equality_pattern(qtuple))][key] += 1
            if len(set(qtuple)) == width:
                distinct_vsets[key] += 1
        rows.append(
            {
                "width": width,
                "tuples_exhausted": len(states) ** width,
                "max_augmented_orbit": max_augmented,
                "vstab_histogram_by_equality_pattern": {
                    pattern: dict(sorted(hist.items()))
                    for pattern, hist in sorted(by_pattern.items())
                },
            }
        )
        distinct_summary.append(
            {
                "width": width,
                "ordered_distinct_tuples": 0
                if width > len(states)
                else len(tuple(itertools.permutations(range(len(states)), width))),
                "vstab_histogram": dict(sorted(distinct_vsets.items())),
            }
        )
    assert all(set(row["vstab_histogram"]) <= {"0", "00", "000"} for row in distinct_summary)
    assert all(sum(row["vstab_histogram"].values()) == row["ordered_distinct_tuples"] for row in distinct_summary)
    return {
        "quotient_size": len(states),
        "signed_generators": [list(label) for label in labels],
        "positive_generator_odd_transporter_counts": [
            sum(voltages[2 * slot]) for slot in range(3)
        ],
        "all_tuple_rows": rows,
        "ordered_distinct_matching_rows": distinct_summary,
        "proved_finite_conclusion": (
            "V_stab is trivial for every ordered distinct quotient tuple "
            "of every possible width 1..4"
        ),
    }


def d4_witness(m158):
    states, actions, voltages, labels = component_with_voltage(m158, 4)
    relabelings = tuple(itertools.permutations(range(4)))
    index = {word: i for i, word in enumerate(states)}
    A, B, C, D, E = (0, 1), (0, 2), (2, 3), (1, 2), (1, 3)
    sources = ((A, B, B, A, C, C), (A, B, B, C, A, C))
    targets = ((A, D, B, E, D, C), (A, D, B, C, E, C))
    source = tuple(index[m158.canonical(word, relabelings)] for word in sources)
    target = tuple(index[m158.canonical(word, relabelings)] for word in targets)

    source_component = augmented_orbit(source, actions, voltages)
    target_component = augmented_orbit(target, actions, voltages)
    source_v = sorted(mask for point, mask in source_component if point == source)
    target_v = sorted(mask for point, mask in target_component if point == target)
    route_v = sorted(mask for point, mask in source_component if point == target)

    s3 = tuple(itertools.permutations(range(3)))
    source_phi = [m158.canonical(m158.projected_word(word), s3) for word in sources]
    target_phi = [m158.canonical(m158.projected_word(word), s3) for word in targets]
    assert source_v == [0] and target_v == [0]
    assert not route_v
    assert source_phi[0] == source_phi[1] and target_phi[0] != target_phi[1]
    return {
        "quotient_size": len(states),
        "source_indices": list(source),
        "target_indices": list(target),
        "source_quotient_orbit_size": len({point for point, _ in source_component}),
        "source_augmented_orbit_size": len(source_component),
        "source_vstab": [mask_label(v, 2) for v in source_v],
        "target_quotient_orbit_size": len({point for point, _ in target_component}),
        "target_augmented_orbit_size": len(target_component),
        "target_vstab": [mask_label(v, 2) for v in target_v],
        "source_to_target_voltage_set": route_v,
        "s4_over_v4_block_test": {
            "source_same_block": source_phi[0] == source_phi[1],
            "target_same_block": target_phi[0] == target_phi[1],
        },
        "proved_finite_conclusion": (
            "both accepted witness tuple stabilizers have trivial relative "
            "voltage; the source-to-target failure already occurs in the "
            "quotient block system"
        ),
        "signed_generator_count": len(labels),
    }


def main():
    here = Path(__file__).resolve().parent
    root = here.parents[3]
    m158, m158_path, observed = load_m158(root)
    payload = {
        "experiment": "M163 exact stabilizer-voltage audit",
        "target": "Hurwitz quotient-tuple stabilizer voltage; not a sampler or gap",
        "composition_convention": "M158 R_j(a,b)=(b,b^-1*a*b), chronological signed generators",
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True
        ).strip(),
        "python": platform.python_version(),
        "dependencies": {"accepted_M158_checker": str(m158_path.relative_to(root))},
        "seed": None,
        "command": "python3 -B stabilizer_voltage_audit.py",
        "m158_sha256_verified": observed,
        "d3": d3_exhaustive(m158),
        "d4_accepted_witness": d4_witness(m158),
        "scope": "exact d3 exhaustion and accepted d4 witness only; no d>=5 inference",
    }
    (here / "results.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
