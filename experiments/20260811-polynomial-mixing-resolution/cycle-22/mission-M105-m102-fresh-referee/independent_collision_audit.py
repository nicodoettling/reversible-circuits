#!/usr/bin/env python3
"""Independent exact audit of M102's rational collision face.

This file imports no predecessor code and does not hard-code any residual-cycle
list.  It derives all lists from labeled support positions and permutation
composition.  Positions are affine in two formal infinitesimals: ``delta``
for the colliding intermediate endpoints and ``eps`` for B's adjacent edge.

Convention: (pq)(x)=p(q(x)); tuple factors multiply left-to-right.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


F = Fraction


@dataclass(frozen=True)
class Affine:
    constant: Fraction = F(0)
    delta: Fraction = F(0)
    eps: Fraction = F(0)

    def __add__(self, other: "Affine") -> "Affine":
        return Affine(
            self.constant + other.constant,
            self.delta + other.delta,
            self.eps + other.eps,
        )

    def __sub__(self, other: "Affine") -> "Affine":
        return Affine(
            self.constant - other.constant,
            self.delta - other.delta,
            self.eps - other.eps,
        )


ZERO = Affine()
ONE = Affine(F(1))


def q(value: int | Fraction, delta: int | Fraction = 0, eps: int | Fraction = 0) -> Affine:
    return Affine(F(value), F(delta), F(eps))


def affine_text(value: Affine) -> str:
    pieces: list[str] = []
    for coefficient, symbol in (
        (value.constant, ""),
        (value.delta, "delta"),
        (value.eps, "eps"),
    ):
        if coefficient == 0:
            continue
        sign = "+" if coefficient > 0 and pieces else ""
        if symbol and abs(coefficient) == 1:
            term = symbol if coefficient > 0 else f"-{symbol}"
        elif symbol:
            term = f"{coefficient}*{symbol}"
        else:
            term = str(coefficient)
        pieces.append(sign + term)
    return "0" if not pieces else "".join(pieces)


def transposition_map(prefix: str, kind: str) -> dict[str, str]:
    labels = [f"{prefix}{index}" for index in range(4)]
    if kind == "S":
        pairs = ((0, 1), (2, 3))
    elif kind == "N":
        pairs = ((0, 3), (1, 2))
    elif kind == "X":
        pairs = ((0, 2), (1, 3))
    else:
        raise ValueError(kind)
    answer = {label: label for label in labels}
    for left, right in pairs:
        answer[labels[left]], answer[labels[right]] = labels[right], labels[left]
    return answer


def compose(first: dict[str, str], second: dict[str, str], labels: list[str]) -> dict[str, str]:
    """Return first after second, extending each map by fixed points."""
    return {
        label: first.get(second.get(label, label), second.get(label, label))
        for label in labels
    }


def merge(*parts: dict[str, Affine]) -> dict[str, Affine]:
    answer: dict[str, Affine] = {}
    for part in parts:
        assert not (set(answer) & set(part))
        answer.update(part)
    return answer


def order_key(item: tuple[str, Affine]) -> tuple[Fraction, Fraction, Fraction, str]:
    label, value = item
    # At the two equal constant positions, eps or delta is positive and fixes
    # the intended local order.  Else constants alone determine the order.
    return value.constant, value.eps, value.delta, label


def residual_lengths(
    positions: dict[str, Affine], permutation: dict[str, str]
) -> list[Affine]:
    labels = [label for label, _ in sorted(positions.items(), key=order_key)]
    assert set(permutation) == set(labels) == set(permutation.values())
    inverse = {image: preimage for preimage, image in permutation.items()}
    index = {label: i for i, label in enumerate(labels)}
    gaps = []
    for i, label in enumerate(labels):
        next_label = labels[(i + 1) % len(labels)]
        gap = positions[next_label] - positions[label]
        if i + 1 == len(labels):
            gap = gap + ONE
        gaps.append(gap)
    transition = [
        index[inverse[labels[(i + 1) % len(labels)]]]
        for i in range(len(labels))
    ]
    seen: set[int] = set()
    answer: list[Affine] = []
    for start in range(len(labels)):
        if start in seen:
            continue
        current = start
        total = ZERO
        while current not in seen:
            seen.add(current)
            total = total + gaps[current]
            current = transition[current]
        answer.append(total)
    return sorted(answer, key=lambda x: (x.constant, x.eps, x.delta))


def product_at_face(values: list[Affine], remove_delta: int, remove_eps: int = 0) -> Fraction:
    delta_zeros = [value for value in values if value.constant == 0 and value.delta != 0]
    eps_zeros = [value for value in values if value.constant == 0 and value.eps != 0 and value.delta == 0]
    assert len(delta_zeros) == remove_delta, (values, delta_zeros)
    assert len(eps_zeros) == remove_eps, (values, eps_zeros)
    answer = F(1)
    for value in values:
        if value.constant:
            answer *= value.constant
    return answer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    a_positions = {"a0": q(0), "a1": q(F(1, 3)), "a2": q(F(2, 3))}
    a_permutation = {"a0": "a1", "a1": "a2", "a2": "a0"}
    b_positions = {
        "b0": q(0),
        "be": q(0, eps=1),
        "b1": q(F(1, 3)),
        "b2": q(F(2, 3)),
    }
    b_permutation = {"b0": "be", "be": "b0", "b1": "b2", "b2": "b1"}
    s_positions = {
        "s0": q(F(1, 10)),
        "s1": q(F(1, 9)),
        "s2": q(F(24, 25)),
        "s3": q(F(24, 25), delta=1),
    }
    t_positions = {
        "t0": q(F(1, 7)),
        "t1": q(F(9, 20)),
        "t2": q(F(5, 7)),
        "t3": q(F(15, 16)),
    }

    source_a_residual = residual_lengths(a_positions, a_permutation)
    source_b_residual = residual_lengths(b_positions, b_permutation)
    derived: dict[str, list[Affine]] = {
        "source_A": source_a_residual,
        "source_B": source_b_residual,
    }
    for s_kind in ("S", "N"):
        s_permutation = transposition_map("s", s_kind)
        a_positions_joint = merge(a_positions, s_positions)
        b_positions_joint = merge(b_positions, s_positions)
        derived[f"A_times_s{s_kind}"] = residual_lengths(
            a_positions_joint,
            compose(a_permutation, s_permutation, list(a_positions_joint)),
        )
        derived[f"B_times_s{s_kind}"] = residual_lengths(
            b_positions_joint,
            compose(b_permutation, s_permutation, list(b_positions_joint)),
        )
        derived[f"s{s_kind}"] = residual_lengths(s_positions, s_permutation)
        for t_kind in ("S", "N"):
            positions = merge(s_positions, t_positions)
            derived[f"s{s_kind}_times_t{t_kind}"] = residual_lengths(
                positions,
                compose(
                    s_permutation,
                    transposition_map("t", t_kind),
                    list(positions),
                ),
            )

    # The third matching of four cyclic support points is crossing.  Its
    # residual has one cycle rather than the three required of an admissible
    # rank-two prefix of a minimal long-cycle factorization, so it supplies no
    # omitted generic intermediate or target color.
    crossing_s_residual = residual_lengths(s_positions, transposition_map("s", "X"))
    crossing_t_residual = residual_lengths(t_positions, transposition_map("t", "X"))
    assert len(crossing_s_residual) == len(crossing_t_residual) == 1

    a_num = product_at_face(derived["A_times_sS"], remove_delta=1)
    b_num = product_at_face(derived["B_times_sS"], remove_delta=1, remove_eps=1)
    a_den = product_at_face(source_a_residual, remove_delta=0)
    b_den = product_at_face(source_b_residual, remove_delta=0, remove_eps=1)
    s_regular = product_at_face(derived["sS"], remove_delta=1)
    joint_ss = product_at_face(derived["sS_times_tS"], remove_delta=1)
    joint_sn = product_at_face(derived["sS_times_tN"], remove_delta=1)
    source_base_a = a_den / a_num
    source_base_b = b_den / b_num
    intermediate_base = s_regular
    joint_base_ss = 1 / joint_ss
    joint_base_sn = 1 / joint_sn
    assert source_base_b < source_base_a

    # The S-intermediate term is singular.  Directly derived N lists have no
    # delta-zero residual factor (after B's separate eps singleton), hence the
    # N-intermediate contribution is bounded in this local coordinate.
    for key in ("A_times_sN", "sN", "sN_times_tS", "sN_times_tN"):
        assert not any(value.constant == 0 and value.delta for value in derived[key]), key
    assert not any(
        value.constant == 0 and value.delta
        for value in derived["B_times_sN"]
        if not value.eps
    )

    stripped = (
        float(source_base_b) ** 1.5 - float(source_base_a) ** 1.5
    ) * float(intermediate_base) ** 1.5 * (
        float(joint_base_ss) ** 1.5 + float(joint_base_sn) ** 1.5
    )
    # a(s)=a(t)=2, while four critical-Borel density factors contribute
    # c^4=(2*pi)^-2.  Thus lift_factor*c^4=1/pi^2.  Since n=3k,
    # multiplying Delta by k^2 adds 1/9.  This is the normalized coefficient
    # density in direct support-position coordinates, before any optional
    # change-of-variable Jacobian.
    normalized = stripped / (9 * math.pi * math.pi)

    payload = {
        "status": "independent_exact_collision_topology_audit",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "derived_residuals": {
            key: [affine_text(value) for value in values]
            for key, values in sorted(derived.items())
        },
        "coefficient_bases": {
            "source_A": str(source_base_a),
            "source_B": str(source_base_b),
            "source_B_less_than_A": source_base_b < source_base_a,
            "intermediate": str(intermediate_base),
            "joint_SS": str(joint_base_ss),
            "joint_SN": str(joint_base_sn),
        },
        "stripped_two_target_color_coefficient": stripped,
        "raw_lift_factor_a_s_a_t": 4,
        "critical_borel_density_factor": "(2*pi)^-2",
        "n_equals_3k_factor_for_k2_delta": "1/9",
        "normalized_k2_delta_position_density_coefficient": normalized,
        "nested_intermediate_bounded_on_face": True,
        "crossing_double_matching_residual_cycles": {
            "intermediate": [affine_text(value) for value in crossing_s_residual],
            "target": [affine_text(value) for value in crossing_t_residual],
            "admissible_rank_two_prefix": False,
        },
        "target_support_gaps": [
            "43/140",
            "37/140",
            "25/112",
            "23/112",
        ],
        "target_inside_central_event_limit": True,
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
