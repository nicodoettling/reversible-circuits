#!/usr/bin/env python3
"""Sole exact k=7 guard for the pre-frozen M334 AOEC_1 candidate.

The script SHA-gates the accepted no-import M311 QBD harness, mechanically
specializes its fixed rank from 11 to 7, and adds only exact active-owner
incidence bookkeeping.  It tests no other rank or grouping.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any


SOURCE_SHA256 = "703f4d8db29c60ee3f1d3f1cd7418aa11782f9a309a310c2a259d8d30d09eb94"


def exact(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else str(x)


def type_key(active: tuple[Any, ...]) -> tuple[Any, ...]:
    return active


def type_name(active: tuple[Any, ...]) -> str:
    if active[0] == "S":
        return f"S_{active[1]}"
    return f"X_{active[1]}_{active[2]}"


def main(source_path: Path) -> dict[str, object]:
    raw = source_path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SOURCE_SHA256
    source = raw.decode()
    assert source.count("K = 11\n") == 1
    assert source.count("assert len(LAGS) == 30") == 1
    source = source.replace("K = 11\n", "K = 7\n", 1)
    source = source.replace("assert len(LAGS) == 30", "assert len(LAGS) == 18", 1)
    namespace: dict[str, Any] = {
        "__name__": "m334_k7_base",
        "__file__": str(source_path),
    }
    exec(compile(source, str(source_path), "exec"), namespace)

    K: int = namespace["K"]
    N: int = namespace["N"]
    D: int = namespace["D"]
    LAGS: tuple[int, ...] = namespace["LAGS"]
    GAMMA: dict[tuple[int, int], Fraction] = namespace["GAMMA"]
    owner_data = namespace["owner_data"]
    response = namespace["response"]
    middle_edge = namespace["middle_edge"]
    v = namespace["v"]
    alpha = namespace["alpha"]
    beta = namespace["beta"]
    edge = namespace["edge"]
    transport_data = namespace["transport_data"]

    assert K == 7 and N == 21 and D == 13 and len(LAGS) == 18
    assert sum(GAMMA.values(), Fraction(0)) == 0

    (
        cut_edges,
        x_mass,
        y_mass,
        _r_mass,
        _R_mass,
        mu,
        pi,
        path,
        blocks,
        M_endpoint,
    ) = transport_data()

    def coefficient(active: tuple[Any, ...]) -> Fraction:
        if active[0] == "S":
            return beta(active[1])
        return alpha(active[1]) * alpha(active[2])

    def active_counts(
        exterior: tuple[int, int], middle: tuple[int, int], ell: int
    ) -> dict[tuple[Any, ...], int]:
        generic, sizes = owner_data(exterior, middle)
        out: defaultdict[tuple[Any, ...], int] = defaultdict(int)
        for x, i in enumerate(generic):
            j = generic[(x + ell) % N]
            if i is None or j is None:
                continue
            if i == j:
                active = ("S", sizes[i])
                assert sizes[i] >= 3
            else:
                d, e = sorted((sizes[i], sizes[j]))
                active = ("X", d, e)
                assert d >= 2
            out[active] += 1
        reconstructed = sum(
            (coefficient(active) * count for active, count in out.items()),
            Fraction(0),
        )
        assert reconstructed == response(exterior, middle, ell)
        return dict(out)

    prefix_table: dict[tuple[int, int, int, tuple[Any, ...]], Fraction] = {}
    endpoint_rows: list[dict[str, object]] = []
    first_negative: dict[str, object] | None = None
    minimum: tuple[Fraction, dict[str, object]] | None = None
    negative_instances = 0
    nonzero_instances = 0
    scalar_prefixes_checked = 0
    all_types: set[tuple[Any, ...]] = set()

    for u in range(1, (K + 1) // 2):
        middle = tuple(middle_edge(a, u) for a in range(K))
        assert len(set(middle)) == K
        for ell in LAGS:
            counts: dict[tuple[int, int], dict[tuple[Any, ...], int]] = {}
            scalar_g: dict[tuple[int, int], Fraction] = {}
            row_types: set[tuple[Any, ...]] = set()
            for exterior in GAMMA:
                total: defaultdict[tuple[Any, ...], int] = defaultdict(int)
                for f in middle:
                    for active, value in active_counts(exterior, f, ell).items():
                        total[active] += value
                counts[exterior] = dict(total)
                row_types.update(total)
                scalar_g[exterior] = sum(
                    (coefficient(active) * value for active, value in total.items()),
                    Fraction(0),
                )
                assert scalar_g[exterior] == sum(
                    (response(exterior, f, ell) for f in middle), Fraction(0)
                )
            all_types.update(row_types)

            xb: dict[int, dict[tuple[Any, ...], Fraction]] = {}
            yb: dict[int, dict[tuple[Any, ...], Fraction]] = {}
            yb_internal: dict[int, dict[tuple[Any, ...], Fraction]] = {}
            yb_seam: dict[int, dict[tuple[Any, ...], Fraction]] = {}
            scalar_xb: dict[int, Fraction] = {}
            scalar_yb: dict[int, Fraction] = {}
            for c in range(1, K):
                cross, internal = cut_edges[c]
                q = v(K, c) / 2 - v(D, c)
                seam = edge(0, c)
                xb[c] = {}
                yb[c] = {}
                yb_internal[c] = {}
                yb_seam[c] = {}
                for active in row_types:
                    pos = Fraction(sum(counts[e].get(active, 0) for e in cross), 2 * c)
                    neg_internal = (
                        q * sum(counts[e].get(active, 0) for e in internal) / y_mass[c]
                    )
                    neg_seam = (
                        v(K, c) * counts[seam].get(active, 0) / (2 * y_mass[c])
                    )
                    xb[c][active] = pos
                    yb_internal[c][active] = neg_internal
                    yb_seam[c][active] = neg_seam
                    yb[c][active] = neg_internal + neg_seam
                scalar_xb[c] = sum(scalar_g[e] for e in cross) / (2 * c)
                scalar_yb[c] = (
                    q * sum(scalar_g[e] for e in internal)
                    + v(K, c) * scalar_g[seam] / 2
                ) / y_mass[c]
                assert scalar_xb[c] == sum(
                    (coefficient(a) * xb[c].get(a, Fraction(0)) for a in row_types),
                    Fraction(0),
                )
                assert scalar_yb[c] == sum(
                    (coefficient(a) * yb[c].get(a, Fraction(0)) for a in row_types),
                    Fraction(0),
                )

            row_endpoints: list[dict[str, object]] = []
            scalar_prefix = Fraction(0)
            active_prefix: defaultdict[tuple[Any, ...], Fraction] = defaultdict(Fraction)
            positive_prefix: defaultdict[tuple[Any, ...], Fraction] = defaultdict(Fraction)
            internal_prefix: defaultdict[tuple[Any, ...], Fraction] = defaultdict(Fraction)
            seam_prefix: defaultdict[tuple[Any, ...], Fraction] = defaultdict(Fraction)
            for block in blocks:
                block_index = int(block["block_index"])
                for c, d in block["cells"]:
                    mass = pi[(c, d)]
                    scalar_prefix += mass * (scalar_xb[c] - scalar_yb[d])
                    for active in row_types:
                        pos = mass * xb[c].get(active, Fraction(0))
                        neg_i = mass * yb_internal[d].get(active, Fraction(0))
                        neg_s = mass * yb_seam[d].get(active, Fraction(0))
                        positive_prefix[active] += pos
                        internal_prefix[active] += neg_i
                        seam_prefix[active] += neg_s
                        active_prefix[active] += pos - neg_i - neg_s
                reconstructed_scalar = sum(
                    (coefficient(a) * active_prefix[a] for a in row_types), Fraction(0)
                )
                assert reconstructed_scalar == scalar_prefix
                scalar_prefixes_checked += 1

                entries: list[dict[str, object]] = []
                for active in sorted(row_types, key=type_key):
                    value = active_prefix[active]
                    prefix_table[(u, ell, block_index, active)] = value
                    if value:
                        nonzero_instances += 1
                        witness = {
                            "u": u,
                            "ell": ell,
                            "block_index": block_index,
                            "endpoint_b": int(block["b"]),
                            "T": exact(M_endpoint[int(block["b"])]),
                            "active_type": type_name(active),
                            "value": exact(value),
                            "value_float": float(value),
                            "positive_nested_mass": exact(positive_prefix[active]),
                            "negative_internal_mass": exact(internal_prefix[active]),
                            "negative_seam_mass": exact(seam_prefix[active]),
                        }
                        entries.append(witness)
                        if value < 0:
                            negative_instances += 1
                            if first_negative is None:
                                first_negative = witness
                        if minimum is None or value < minimum[0]:
                            minimum = (value, witness)
                row_endpoints.append(
                    {
                        "block_index": block_index,
                        "endpoint_b": int(block["b"]),
                        "T": exact(M_endpoint[int(block["b"])]),
                        "scalar_prefix": exact(scalar_prefix),
                        "active_prefixes_nonzero": entries,
                    }
                )
            terminal_direct = sum(
                (
                    GAMMA[e]
                    * sum((response(e, f, ell) for f in middle), Fraction(0))
                    for e in GAMMA
                ),
                Fraction(0),
            )
            assert scalar_prefix == terminal_direct
            endpoint_rows.append({"u": u, "ell": ell, "endpoints": row_endpoints})

    for (u, ell, block_index, active), value in prefix_table.items():
        reflected = N - ell
        assert prefix_table[(u, reflected, block_index, active)] == value

    assert minimum is not None
    return {
        "status": "exact sole k=7 guard of pre-frozen AOEC_1",
        "source": {
            "path": str(source_path),
            "sha256": SOURCE_SHA256,
            "mechanical_changes": ["K = 11 -> K = 7", "30 lags -> 18 lags"],
            "added_bookkeeping": "active owner incidence counts only",
            "other_ranks_tested": False,
            "alternate_groupings_tested": False,
        },
        "scope": {
            "k": K,
            "n": N,
            "middle_cut_classes": list(range(1, (K + 1) // 2)),
            "middle_phases_per_class": K,
            "admissible_lags": list(LAGS),
            "maximal_blocks": len(blocks),
            "rows": len(endpoint_rows),
            "positive_topology": "N (cross exterior)",
            "negative_topology": "S (internal plus seam exterior)",
            "triangle_topology_mass": 0,
        },
        "normalization": {
            "positive_exterior_mass": exact(mu),
            "negative_exterior_mass": exact(mu),
            "transport_mass": exact(sum(pi.values(), Fraction(0))),
            "source_gamma_mass": exact(sum(GAMMA.values(), Fraction(0))),
        },
        "checks": {
            "statewise_AOTI_exact": True,
            "prefix_AOTI_exact": True,
            "scalar_prefixes_checked": scalar_prefixes_checked,
            "all_middle_phases_retained": True,
            "all_target_phases_retained": True,
            "internal_and_seam_negative_parts_retained": True,
            "lag_reflection_exact": True,
        },
        "aoec": {
            "active_types_seen": [type_name(a) for a in sorted(all_types, key=type_key)],
            "nonzero_prefix_instances": nonzero_instances,
            "negative_prefix_instances": negative_instances,
            "survives_k7": negative_instances == 0,
            "first_lexicographic_negative": first_negative,
            "minimum": {
                "exact": exact(minimum[0]),
                "float": float(minimum[0]),
                "witness": minimum[1],
            },
        },
        "rows": endpoint_rows,
        "all_rank_inference": False,
        "gqac_inference": False,
        "downstream_inference": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = main(args.source)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["aoec"], indent=2, sort_keys=True))
