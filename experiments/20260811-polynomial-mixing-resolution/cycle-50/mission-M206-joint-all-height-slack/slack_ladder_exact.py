#!/usr/bin/env python3
"""Exact finite audit of M206's two named slack-ladder rows.

This compact wrapper verifies and imports the frozen, accepted M204 literal-
composition history engine. It does not import M201 and does not scan a
parameter range. The universal B=2 annihilation is proved in the theorem
note; here its finite composition structure is asserted directly.
"""

from argparse import ArgumentParser
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
from json import dumps
from pathlib import Path


M204_CHECKER_SHA256 = (
    "c55162114f0f89b1d6f2a0dd2721cce23f8a538bc834c11a84557e3d419be6d3"
)


def load_frozen_history_engine():
    experiment_root = Path(__file__).resolve().parents[2]
    path = (
        experiment_root
        / "cycle-49"
        / "mission-M204-m201-fresh-referee"
        / "independent_exact.py"
    )
    assert sha256(path.read_bytes()).hexdigest() == M204_CHECKER_SHA256
    spec = importlib.util.spec_from_file_location("frozen_m204_history", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def compatible_bounds(engine, bottom, height_limit):
    q = engine.split_probability(bottom + height_limit, bottom)
    q0 = engine.tree_weight(bottom) / engine.tree_weight(bottom + 1)
    _, a1 = engine.h1_operator_average(height_limit - 1)
    u1 = (1 - q0) * a1

    n2 = height_limit - 2
    m2 = F((n2 + 1) ** n2 * (n2 + 2), (n2 + 3) ** (n2 + 1))
    u2 = F(2, 3) * m2

    n3 = height_limit - 3
    m3 = F(3, 2) * F(
        (n3 + 1) ** n3 * (n3 + 2) * (n3 + 3),
        (n3 + 4) ** (n3 + 2),
    )
    u3 = F(3, 4) * m3
    delta = 1 - q - u1 - u2 - u3
    return q, (u1, u2, u3), delta


def row(engine, bottom):
    height_limit = 4
    q, bounds, delta = compatible_bounds(engine, bottom, height_limit)
    charges = engine.parent_height_charges(bottom, height_limit)
    slacks = tuple(bounds[index] - charges[index + 1] for index in range(3))
    high_excess = charges["reset"] + charges[4] - delta
    full_charge = sum(charges.values(), F(0))
    true_slack = 1 - q - full_charge
    assert true_slack == sum(slacks, F(0)) - high_excess
    return {
        "q": q,
        "bounds": bounds,
        "delta": delta,
        "charges": charges,
        "slacks": slacks,
        "X": high_excess,
        "true_slack": true_slack,
    }


def record(value):
    return {"exact": str(value), "decimal": float(value)}


def encode_row(data):
    return {
        "q": record(data["q"]),
        "U": {f"h{h}": record(data["bounds"][h - 1]) for h in range(1, 4)},
        "Delta": record(data["delta"]),
        "T": {
            "reset": record(data["charges"]["reset"]),
            **{f"h{h}": record(data["charges"][h]) for h in range(1, 5)},
        },
        "S": {f"h{h}": record(data["slacks"][h - 1]) for h in range(1, 4)},
        "X_reset_plus_hge4_minus_Delta": record(data["X"]),
        "S1_minus_X": record(data["slacks"][0] - data["X"]),
        "S1_plus_S2_minus_X": record(
            data["slacks"][0] + data["slacks"][1] - data["X"]
        ),
        "full_true_slack": record(data["true_slack"]),
    }


def main():
    parser = ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    engine = load_frozen_history_engine()

    # The two compositions of 2 have no active reset endpoint or live child.
    assert engine.ordered_compositions(2) == ((1, 1), (2,))
    assert engine.reset_basins(2) == ()
    assert all(source[-1] <= 2 for source, _ in engine.literal_roots(2))

    b2 = row(engine, 2)
    b3 = row(engine, 3)

    assert b2["charges"][1] == 0
    assert b2["slacks"][0] - b2["X"] == F(
        9103978211751469889, 8339940489100500000000
    ) > 0

    assert b3["slacks"][0] - b3["X"] == -F(
        58850574391835735352420545363,
        1474064677007114895360000000000,
    ) < 0
    assert b3["slacks"][0] + b3["slacks"][1] - b3["X"] == F(
        183315802718619702462160882861,
        1474064677007114895360000000000,
    ) > 0

    result = {
        "schema": "M206-slack-ladder-v1",
        "arithmetic": "standard-library Fraction",
        "seed": None,
        "frozen_history_engine": {
            "mission": "M204",
            "sha256": M204_CHECKER_SHA256,
            "verified_before_import": True,
            "root_expansion": "literal ordered compositions",
        },
        "universal_B2_structure": {
            "ordered_compositions": [[1, 1], [2]],
            "active_reset_endpoints": 0,
            "live_descendants": 0,
            "conclusion": "Phi_(2,kappa,D,2)=0 for every valid kappa,D",
        },
        "rows": {"B2_L4": encode_row(b2), "B3_L4": encode_row(b3)},
        "logical_scope": {
            "proved": [
                "universal B=2 suffix-zero history annihilation",
                "B=2,L=4 terminal slack alone pays X",
                "B=3,L=4 terminal slack alone fails",
                "B=3,L=4 cumulative h1+h2 slack pays X",
            ],
            "not_claimed": [
                "universal h1-only transfer",
                "universal h1+h2 transfer",
                "universal cumulative slack lemma",
                "all-state contraction or any gap/Terminal conclusion",
            ],
        },
    }
    args.output.write_text(dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
