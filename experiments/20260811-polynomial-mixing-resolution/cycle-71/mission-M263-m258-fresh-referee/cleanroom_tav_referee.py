#!/usr/bin/env python3
"""Independent bounded falsifier for M258 TAV; intentionally only k=3,5."""

from __future__ import annotations

import argparse
import json
import math
import platform
from fractions import Fraction
from math import factorial
from pathlib import Path


def tree_weight(q: int) -> Fraction:
    # Replacing b_q by exp(q)b_q leaves every bridge ratio below unchanged.
    return Fraction(q ** (q - 1), factorial(q))


def bridge(k: int, parent: int, kept: int) -> Fraction:
    return (
        tree_weight(kept)
        * tree_weight(parent - kept)
        / ((2 * k - 3) * tree_weight(parent))
    )


def norm_piece(k: int, parent: int) -> Fraction:
    if parent < 2:
        return Fraction(0)
    return Fraction((parent - 1) * (parent - 2), parent * (2 * k - 3))


def kept_edges(parent: int, kept: int, cut: int) -> set[int]:
    return set(range(cut)) | set(range(cut + parent - kept, parent))


def joint_hits(k: int, parent: int, kept: int, cut: int) -> int:
    modulus = 2 * k - 1
    edge_set = kept_edges(parent, kept, cut)
    return sum((x + k) % modulus in edge_set for x in edge_set)


def placement_moment(k: int, parent: int, kept: int) -> int:
    if kept < 2 or kept >= parent:
        return 0
    return sum(joint_hits(k, parent, kept, cut) for cut in range(1, kept))


def cutoff(k: int, ell: int, kept: int) -> Fraction:
    modulus = 2 * k - 1
    numerator = (
        (modulus - 2 * kept) * int(kept <= ell)
        + kept * int(kept <= ell - 1)
        + kept * int(kept <= ell - k)
    )
    return Fraction(numerator, modulus)


def literal_average(k: int, ell: int, parent: int, kept: int, cut: int) -> Fraction:
    modulus = 2 * k - 1
    base = kept_edges(parent, kept, cut)
    accepted = 0
    for shift in range(modulus):
        translated = {(x + shift) % modulus for x in base}
        size = kept + k * int(0 in translated) + int(k in translated)
        accepted += int(2 <= size <= ell)
    return Fraction(accepted, modulus)


def predicted_placement_sum(k: int, ell: int, parent: int, kept: int) -> Fraction:
    modulus = 2 * k - 1
    spike_sign = int(kept == ell) - int(kept == ell - k)
    return (kept - 1) * cutoff(k, ell, kept) + Fraction(
        placement_moment(k, parent, kept) * spike_sign, modulus
    )


def reflected(k: int, parent: int, value) -> Fraction:
    return sum(
        (
            (kept - 1) * bridge(k, parent, kept) * value(kept)
            for kept in range(2, parent)
        ),
        Fraction(0),
    )


def spike(k: int, parent: int, kept: int) -> Fraction:
    if kept < 2 or kept >= parent:
        return Fraction(0)
    return bridge(k, parent, kept) * Fraction(
        placement_moment(k, parent, kept), 2 * k - 1
    )


def normalized_spike(k: int, rank: int, kept: int) -> Fraction:
    modulus = 2 * k - 1
    denominator = norm_piece(k, rank) + norm_piece(k, modulus - rank)
    return (spike(k, rank, kept) + spike(k, modulus - rank, kept)) / denominator


def theta_from_decomposition(k: int, ell: int, rank: int) -> Fraction:
    modulus = 2 * k - 1
    denominator = norm_piece(k, rank) + norm_piece(k, modulus - rank)
    base = (
        reflected(k, rank, lambda t: cutoff(k, ell, t))
        + reflected(k, modulus - rank, lambda t: cutoff(k, ell, t))
    ) / denominator
    return (
        base
        + normalized_spike(k, rank, ell)
        - normalized_spike(k, rank, ell - k)
    )


def theta_literal(k: int, ell: int, rank: int) -> Fraction:
    modulus = 2 * k - 1
    denominator = norm_piece(k, rank) + norm_piece(k, modulus - rank)
    total = Fraction(0)
    for parent in (rank, modulus - rank):
        for kept in range(2, parent):
            placement_sum = sum(
                (
                    literal_average(k, ell, parent, kept, cut)
                    for cut in range(1, kept)
                ),
                Fraction(0),
            )
            total += bridge(k, parent, kept) * placement_sum
    return total / denominator


def run_checks() -> dict:
    checks = 0
    maxima = {
        "head_tv_fraction_of_bound": 0.0,
        "q_variation_over_sqrt_ell": 0.0,
        "spike_mass_over_sqrt_t_over_k": 0.0,
        "raw_spike_response_over_sqrt_t": 0.0,
        "normalized_spike_response_over_sqrt_t": 0.0,
        "tav_over_sqrt_ell": 0.0,
    }
    rows = []

    def require(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(label)

    for k in (3, 5):
        modulus = 2 * k - 1
        ell_max = (3 * k - 1) // 2

        # Direct translations, exact placement sum, J support, and pair list.
        for parent in range(2, modulus):
            for kept in range(2, parent):
                for cut in range(1, kept):
                    base = kept_edges(parent, kept, cut)
                    patterns = {(False, False): 0, (False, True): 0,
                                (True, False): 0, (True, True): 0}
                    for shift in range(modulus):
                        moved = {(x + shift) % modulus for x in base}
                        patterns[(0 in moved, k in moved)] += 1
                    joint = joint_hits(k, parent, kept, cut)
                    expected = {
                        (False, False): modulus - 2 * kept + joint,
                        (False, True): kept - joint,
                        (True, False): kept - joint,
                        (True, True): joint,
                    }
                    require(patterns == expected, f"seams {k,parent,kept,cut}")
                moment = placement_moment(k, parent, kept)
                require(moment <= kept * (kept - 1), f"J bound {k,parent,kept}")
                if parent <= k - 1:
                    require(moment == 0, f"short support {k,parent,kept}")
                else:
                    c = parent - k
                    direct_pairs = [
                        (x, (x + k) % modulus)
                        for x in range(parent)
                        if (x + k) % modulus < parent
                    ]
                    claimed_pairs = (
                        [(u, u + k) for u in range(c)]
                        + [(u + k - 1, u) for u in range(c + 1)]
                    )
                    require(direct_pairs == claimed_pairs, f"pair list {k,parent}")
                    if kept <= c:
                        require(moment == 0, f"long cutoff {k,parent,kept}")
                for ell in range(2, ell_max + 1):
                    direct = sum(
                        (literal_average(k, ell, parent, kept, cut)
                         for cut in range(1, kept)),
                        Fraction(0),
                    )
                    require(
                        direct == predicted_placement_sum(k, ell, parent, kept),
                        f"two spikes {k,ell,parent,kept}",
                    )

        # Q endpoint profiles, including ell=k and the k=3 ell>D-2 case.
        for ell in range(2, ell_max + 1):
            for kept in range(1, modulus):
                if ell <= k:
                    expected_q = (
                        Fraction(modulus - kept, modulus) if kept <= ell - 1
                        else Fraction(modulus - 2 * ell, modulus) if kept == ell
                        else Fraction(0)
                    )
                else:
                    a = ell - k
                    expected_q = (
                        Fraction(1) if kept <= a
                        else Fraction(modulus - kept, modulus) if kept <= ell - 1
                        else Fraction(modulus - 2 * ell, modulus) if kept == ell
                        else Fraction(0)
                    )
                require(cutoff(k, ell, kept) == expected_q,
                        f"Q endpoint {k,ell,kept}")
            q_variation = sum(
                math.sqrt(u) * abs(float(cutoff(k, ell, u + 1) - cutoff(k, ell, u)))
                for u in range(1, modulus - 2)
            )
            maxima["q_variation_over_sqrt_ell"] = max(
                maxima["q_variation_over_sqrt_ell"], q_variation / math.sqrt(ell)
            )
            require(q_variation <= 4 * math.sqrt(ell) + 1e-12,
                    f"Q variation {k,ell}")

        # Reflected coefficients, constant identity, unimodality, and TV.
        for parent in range(1, modulus):
            require(reflected(k, parent, lambda _t: Fraction(1)) == norm_piece(k, parent),
                    f"constant {k,parent}")
            for kept in range(2, parent):
                if parent + 1 < modulus:
                    require(
                        (kept - 1) * bridge(k, parent + 1, kept)
                        <= (kept - 1) * bridge(k, parent, kept),
                        f"reflected coefficient {k,parent,kept}",
                    )
        for u in range(1, ell_max + 1):
            head = [
                reflected(k, parent, lambda t, u=u: Fraction(t <= u))
                for parent in range(1, modulus)
            ]
            peak_index = min(u, modulus - 2)
            require(all(head[i] >= head[i - 1] for i in range(1, peak_index + 1)),
                    f"head rise {k,u}")
            require(all(head[i] <= head[i - 1] for i in range(peak_index + 1, len(head))),
                    f"head fall {k,u}")
            tv = sum(abs(head[i] - head[i - 1]) for i in range(1, len(head)))
            tv_bound = Fraction(2 * u, 2 * k - 3)
            require(tv <= tv_bound, f"head TV {k,u}")
            maxima["head_tv_fraction_of_bound"] = max(
                maxima["head_tv_fraction_of_bound"], float(tv / tv_bound)
            )

        # Spike mass, exact paired response, normalization, and final TAV.
        for kept in range(2, ell_max + 1):
            mass = sum((spike(k, parent, kept) for parent in range(kept + 1, modulus)),
                       Fraction(0))
            mass_ratio = float(mass) / math.sqrt(kept / k)
            maxima["spike_mass_over_sqrt_t_over_k"] = max(
                maxima["spike_mass_over_sqrt_t_over_k"], mass_ratio
            )
            require(mass_ratio <= 16 + 1e-12, f"spike mass {k,kept}")
            raw_response = 0.0
            normalized_response = 0.0
            for rank in range(1, k - 1):
                long_parent = modulus - rank
                paired = (
                    spike(k, rank + 1, kept) - spike(k, rank, kept)
                    + spike(k, long_parent - 1, kept) - spike(k, long_parent, kept)
                )
                raw_response += math.sqrt(rank) * abs(float(paired))
                normalized_response += math.sqrt(rank) * abs(float(
                    normalized_spike(k, rank + 1, kept)
                    - normalized_spike(k, rank, kept)
                ))
            maxima["raw_spike_response_over_sqrt_t"] = max(
                maxima["raw_spike_response_over_sqrt_t"], raw_response / math.sqrt(kept)
            )
            maxima["normalized_spike_response_over_sqrt_t"] = max(
                maxima["normalized_spike_response_over_sqrt_t"],
                normalized_response / math.sqrt(kept),
            )
            require(raw_response <= 32 * math.sqrt(kept) + 1e-12,
                    f"raw response {k,kept}")
            require(normalized_response <= 160 * math.sqrt(kept) + 1e-12,
                    f"normalized response {k,kept}")

        for ell in range(2, ell_max + 1):
            for rank in range(1, k):
                require(theta_from_decomposition(k, ell, rank) == theta_literal(k, ell, rank),
                        f"theta identity {k,ell,rank}")
            tav = sum(
                math.sqrt(rank) * abs(float(
                    theta_from_decomposition(k, ell, rank + 1)
                    - theta_from_decomposition(k, ell, rank)
                ))
                for rank in range(1, k - 1)
            )
            ratio = tav / math.sqrt(ell)
            maxima["tav_over_sqrt_ell"] = max(maxima["tav_over_sqrt_ell"], ratio)
            require(ratio <= 500 + 1e-12, f"TAV {k,ell}")
            rows.append({"k": k, "ell": ell, "tav_over_sqrt_ell": ratio})

    return {"status": "pass", "assertions": checks, "maxima": maxima, "rows": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    payload = {
        "metadata": {
            "python": platform.python_version(),
            "seed": None,
            "tested_k": [3, 5],
            "scope": "bounded exact falsification only; no M258 imports or data reads",
            "command": "python3 cleanroom_tav_referee.py --output cleanroom_results.json",
        },
        "certificate": run_checks(),
    }
    Path(args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()

