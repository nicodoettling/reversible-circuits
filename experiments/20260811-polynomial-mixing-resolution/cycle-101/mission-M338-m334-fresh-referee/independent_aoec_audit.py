#!/usr/bin/env python3
"""Independent fixed-k=7 reconstruction for the immutable M334 audit.

This checker authenticates and mechanically specializes the accepted M311
no-import owner-law harness.  It does not import M334 code or results and does
not test another rank, grouping, transport, or candidate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any


M311_SOURCE_SHA256 = "703f4d8db29c60ee3f1d3f1cd7418aa11782f9a309a310c2a259d8d30d09eb94"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def label(active: tuple[Any, ...]) -> str:
    if active[0] == "S":
        return f"S_{active[1]}"
    return f"X_{active[1]}_{active[2]}"


def load_k7_base(source_path: Path) -> dict[str, Any]:
    raw = source_path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == M311_SOURCE_SHA256
    source = raw.decode()
    assert source.count("K = 11\n") == 1
    assert source.count("assert len(LAGS) == 30") == 1
    source = source.replace("K = 11\n", "K = 7\n", 1)
    source = source.replace("assert len(LAGS) == 30", "assert len(LAGS) == 18", 1)
    namespace: dict[str, Any] = {
        "__name__": "m338_authenticated_k7_base",
        "__file__": str(source_path),
    }
    exec(compile(source, str(source_path), "exec"), namespace)
    return namespace


def reconstruct(source_path: Path) -> dict[str, object]:
    ns = load_k7_base(source_path)
    K: int = ns["K"]
    N: int = ns["N"]
    D: int = ns["D"]
    LAGS: tuple[int, ...] = ns["LAGS"]
    GAMMA: dict[tuple[int, int], Fraction] = ns["GAMMA"]
    owner_data = ns["owner_data"]
    response = ns["response"]
    middle_edge = ns["middle_edge"]
    v = ns["v"]
    alpha = ns["alpha"]
    beta = ns["beta"]
    edge = ns["edge"]
    transport_data = ns["transport_data"]

    assert (K, N, D, len(LAGS)) == (7, 21, 13, 18)
    assert sum(GAMMA.values(), Fraction(0)) == 0

    cut_edges, _, y_mass, _, _, mu, pi, _, blocks, endpoints = transport_data()

    def coefficient(active: tuple[Any, ...]) -> Fraction:
        return beta(active[1]) if active[0] == "S" else alpha(active[1]) * alpha(active[2])

    def counts_for_state(
        exterior: tuple[int, int], middle: tuple[int, int], ell: int
    ) -> dict[tuple[Any, ...], int]:
        generic, sizes = owner_data(exterior, middle)
        counts: defaultdict[tuple[Any, ...], int] = defaultdict(int)
        for x, first_owner in enumerate(generic):
            second_owner = generic[(x + ell) % N]
            if first_owner is None or second_owner is None:
                continue
            if first_owner == second_owner:
                active = ("S", sizes[first_owner])
                assert sizes[first_owner] >= 3
            else:
                d, e = sorted((sizes[first_owner], sizes[second_owner]))
                active = ("X", d, e)
                assert d >= 2
            counts[active] += 1
        # This is a state-level, coefficient-by-coefficient AOTI reconstruction.
        assert sum(
            (coefficient(active) * count for active, count in counts.items()),
            Fraction(0),
        ) == response(exterior, middle, ell)
        return dict(counts)

    prefix_values: dict[tuple[int, int, int, tuple[Any, ...]], Fraction] = {}
    negative_instances = 0
    nonzero_instances = 0
    statewise_aoti_checks = 0
    prefix_aoti_checks = 0
    first_negative: dict[str, object] | None = None
    minimum: tuple[Fraction, dict[str, object]] | None = None
    rows = 0

    for u in range(1, (K + 1) // 2):
        middle = tuple(middle_edge(phase, u) for phase in range(K))
        assert len(set(middle)) == K
        for ell in LAGS:
            rows += 1
            exterior_counts: dict[tuple[int, int], dict[tuple[Any, ...], int]] = {}
            scalar_response: dict[tuple[int, int], Fraction] = {}
            active_types: set[tuple[Any, ...]] = set()
            for exterior in GAMMA:
                total: defaultdict[tuple[Any, ...], int] = defaultdict(int)
                scalar_response[exterior] = Fraction(0)
                for middle_atom in middle:
                    state_counts = counts_for_state(exterior, middle_atom, ell)
                    statewise_aoti_checks += 1
                    scalar_response[exterior] += response(exterior, middle_atom, ell)
                    for active, count in state_counts.items():
                        total[active] += count
                exterior_counts[exterior] = dict(total)
                active_types.update(total)
                assert sum(
                    (coefficient(active) * count for active, count in total.items()),
                    Fraction(0),
                ) == scalar_response[exterior]

            positive: dict[int, dict[tuple[Any, ...], Fraction]] = {}
            negative_internal: dict[int, dict[tuple[Any, ...], Fraction]] = {}
            negative_seam: dict[int, dict[tuple[Any, ...], Fraction]] = {}
            scalar_positive: dict[int, Fraction] = {}
            scalar_negative: dict[int, Fraction] = {}
            for cut in range(1, K):
                cross, internal = cut_edges[cut]
                q = v(K, cut) / 2 - v(D, cut)
                seam = edge(0, cut)
                positive[cut] = {}
                negative_internal[cut] = {}
                negative_seam[cut] = {}
                for active in active_types:
                    positive[cut][active] = Fraction(
                        sum(exterior_counts[e].get(active, 0) for e in cross), 2 * cut
                    )
                    negative_internal[cut][active] = (
                        q
                        * sum(exterior_counts[e].get(active, 0) for e in internal)
                        / y_mass[cut]
                    )
                    negative_seam[cut][active] = (
                        v(K, cut)
                        * exterior_counts[seam].get(active, 0)
                        / (2 * y_mass[cut])
                    )
                scalar_positive[cut] = sum(scalar_response[e] for e in cross) / (2 * cut)
                scalar_negative[cut] = (
                    q * sum(scalar_response[e] for e in internal)
                    + v(K, cut) * scalar_response[seam] / 2
                ) / y_mass[cut]

            accumulated_positive: defaultdict[tuple[Any, ...], Fraction] = defaultdict(Fraction)
            accumulated_internal: defaultdict[tuple[Any, ...], Fraction] = defaultdict(Fraction)
            accumulated_seam: defaultdict[tuple[Any, ...], Fraction] = defaultdict(Fraction)
            scalar_prefix = Fraction(0)
            for block in blocks:
                block_index = int(block["block_index"])
                for c, d in block["cells"]:
                    mass = pi[(c, d)]
                    scalar_prefix += mass * (scalar_positive[c] - scalar_negative[d])
                    for active in active_types:
                        accumulated_positive[active] += mass * positive[c][active]
                        accumulated_internal[active] += mass * negative_internal[d][active]
                        accumulated_seam[active] += mass * negative_seam[d][active]

                reconstructed = sum(
                    (
                        coefficient(active)
                        * (
                            accumulated_positive[active]
                            - accumulated_internal[active]
                            - accumulated_seam[active]
                        )
                        for active in active_types
                    ),
                    Fraction(0),
                )
                assert reconstructed == scalar_prefix
                prefix_aoti_checks += 1

                for active in sorted(active_types):
                    value = (
                        accumulated_positive[active]
                        - accumulated_internal[active]
                        - accumulated_seam[active]
                    )
                    prefix_values[(u, ell, block_index, active)] = value
                    if value == 0:
                        continue
                    nonzero_instances += 1
                    witness = {
                        "u": u,
                        "ell": ell,
                        "block_index": block_index,
                        "endpoint_b": int(block["b"]),
                        "T": qstr(endpoints[int(block["b"])]),
                        "active_type": label(active),
                        "positive_cross_mass": qstr(accumulated_positive[active]),
                        "negative_internal_mass": qstr(accumulated_internal[active]),
                        "negative_seam_mass": qstr(accumulated_seam[active]),
                        "delta": qstr(value),
                    }
                    if value < 0:
                        negative_instances += 1
                        if first_negative is None:
                            first_negative = witness
                    if minimum is None or value < minimum[0]:
                        minimum = (value, witness)

            direct_terminal = sum(
                (GAMMA[e] * scalar_response[e] for e in GAMMA), Fraction(0)
            )
            assert scalar_prefix == direct_terminal

    for (u, ell, block_index, active), value in prefix_values.items():
        assert prefix_values[(u, N - ell, block_index, active)] == value

    assert first_negative is not None and minimum is not None
    return {
        "status": "independent exact audit; fixed k=7 AOEC guard only",
        "source": {
            "m311_path": str(source_path),
            "m311_sha256": M311_SOURCE_SHA256,
            "m334_code_or_results_imported": False,
        },
        "scope": {
            "k": K,
            "n": N,
            "u_values": list(range(1, (K + 1) // 2)),
            "lags": list(LAGS),
            "rows": rows,
            "blocks": len(blocks),
            "other_ranks": False,
            "new_grouping_transport_or_search": False,
        },
        "normalization": {
            "positive_mass": qstr(mu),
            "negative_mass": qstr(sum(y_mass.values(), Fraction(0))),
            "transport_mass": qstr(sum(pi.values(), Fraction(0))),
        },
        "checks": {
            "statewise_aoti_reconstructions": statewise_aoti_checks,
            "prefix_aoti_reconstructions": prefix_aoti_checks,
            "terminal_signed_law_reconstruction": True,
            "lag_reflection": True,
        },
        "aoec": {
            "negative_prefix_instances": negative_instances,
            "nonzero_prefix_instances": nonzero_instances,
            "first_lexicographic_negative": first_negative,
            "minimum": {"delta": qstr(minimum[0]), "witness": minimum[1]},
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = reconstruct(args.source)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["aoec"], indent=2, sort_keys=True))
