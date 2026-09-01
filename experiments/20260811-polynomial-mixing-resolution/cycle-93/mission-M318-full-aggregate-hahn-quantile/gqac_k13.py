#!/usr/bin/env python3
"""Sole exact k=13 guard for frozen M318 GQAC_1.

This standard-library wrapper SHA-gates M311's frozen exact QBD checker,
changes only its fixed rank and corresponding lag-count assertion, and then
tests the predeclared canonical sign-block prefixes.  It does not alter the
quantile transport, sign blocks, owner response, or grouping.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


SOURCE_SHA256 = "703f4d8db29c60ee3f1d3f1cd7418aa11782f9a309a310c2a259d8d30d09eb94"


def exact(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else str(x)


def main(source_path: Path) -> dict[str, object]:
    raw = source_path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SOURCE_SHA256
    source = raw.decode()
    assert source.count("K = 11\n") == 1
    assert source.count("assert len(LAGS) == 30") == 1
    source = source.replace("K = 11\n", "K = 13\n", 1)
    source = source.replace("assert len(LAGS) == 30", "assert len(LAGS) == 36", 1)

    namespace: dict[str, object] = {
        "__name__": "m318_k13_guard",
        "__file__": str(source_path),
    }
    exec(compile(source, str(source_path), "exec"), namespace)
    base = namespace["main"]()
    assert isinstance(base, dict)
    assert base["scope"]["k"] == 13
    assert len(base["rows"]) == 6 * 36

    rows = []
    first_negative = None
    minimum = None
    negative_prefixes = 0
    rows_with_negative = 0
    for row in base["rows"]:
        prefix = Fraction(0)
        row_prefixes = []
        row_negative = False
        for block in row["blocks"]:
            prefix += Fraction(block["value"])
            entry = {
                "block_index": block["block_index"],
                "prefix": exact(prefix),
                "prefix_float": float(prefix),
            }
            row_prefixes.append(entry)
            witness = {
                "u": row["u"],
                "ell": row["ell"],
                **entry,
            }
            if minimum is None or prefix < minimum[0]:
                minimum = (prefix, witness)
            if prefix < 0:
                negative_prefixes += 1
                row_negative = True
                if first_negative is None:
                    first_negative = witness
        assert prefix == Fraction(row["mclp_value"])
        if row_negative:
            rows_with_negative += 1
        rows.append(
            {
                "u": row["u"],
                "ell": row["ell"],
                "prefixes": row_prefixes,
                "mclp_value": row["mclp_value"],
            }
        )

    assert minimum is not None
    return {
        "status": "exact sole k=13 guard of pre-frozen GQAC_1",
        "source": {
            "path": str(source_path),
            "sha256": SOURCE_SHA256,
            "mechanical_changes": ["K = 11 -> K = 13", "30 lags -> 36 lags"],
            "alternate_groupings_tested": False,
            "other_ranks_tested": False,
        },
        "scope": {
            "k": 13,
            "n": 39,
            "middle_cut_classes": 6,
            "middle_phases_per_class": 13,
            "admissible_lags": 36,
            "rows": len(rows),
        },
        "abel_coefficients": base["abel_coefficients"],
        "transport_path": base["transport_path"],
        "blocks": base["blocks"],
        "gqac": {
            "prefix_instances": sum(len(row["prefixes"]) for row in rows),
            "negative_prefix_instances": negative_prefixes,
            "rows_with_negative_prefix": rows_with_negative,
            "survives_k13": negative_prefixes == 0,
            "first_lexicographic_negative_prefix": first_negative,
            "minimum_prefix": {
                "exact": exact(minimum[0]),
                "float": float(minimum[0]),
                "witness": minimum[1],
            },
        },
        "mclp": base["mclp"],
        "rows": rows,
        "qti_exact": base["qti_exact"],
        "qbd_exact": base["qbd_exact"],
        "reflection_exact": base["reflection_exact"],
        "all_rank_inference": False,
        "downstream_inference": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(main(args.source), indent=2, sort_keys=True) + "\n")
