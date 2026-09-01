#!/usr/bin/env python3
"""Polynomial-size audit of an infinite Stanley-basis one-bubble obstruction."""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
M35 = HERE.parents[1] / "cycle-08" / "mission-M35-general-parking-flow"
M27 = HERE.parents[1] / "cycle-06" / "mission-M27-base-exceptional-modes"
sys.path.insert(0, str(M35))
sys.path.insert(0, str(M27))

from adjacent_bypass_probe import compose, factor_word, inverse_chain, partition_perm  # noqa: E402
from stanley_inverse_basis_falsifier import stanley_tree_from_chain  # noqa: E402


Edge = tuple[int, int]


def conjugate_support(support: set[Edge], q: int, n: int) -> set[Edge]:
    return {
        tuple(sorted(((a - q) % n, (b - q) % n)))
        for a, b in support
    }


def evaluate_word(n: int, word: tuple[Edge, ...]) -> tuple[int, ...]:
    product = tuple(range(n))
    for a, b in word:
        gate = list(range(n))
        gate[a], gate[b] = gate[b], gate[a]
        product = compose(product, tuple(gate))
    return product


def row(n: int) -> dict[str, object]:
    if n < 5:
        raise ValueError("family starts at n=5")
    parking_a = (0, 1, 1) + (3,) * (n - 4)
    parking_b = (0, 2, 2, 0) + (4,) * (n - 5)
    chain_a = inverse_chain(parking_a)
    chain_b = inverse_chain(parking_b)
    tree_a = stanley_tree_from_chain(chain_a)
    tree_b = stanley_tree_from_chain(chain_b)
    expected_a = tuple(sorted({(0, 1), (1, 2), (1, 3)} | {(2, j) for j in range(4, n)}))
    expected_b = tuple(sorted((set(expected_a) - {(2, 4)}) | {(0, 4)}))
    if tree_a != expected_a or tree_b != expected_b:
        raise AssertionError("closed-form Stanley tree family failed")
    word_a = factor_word(chain_a)
    word_b = factor_word(chain_b)
    cycle = tuple((x + 1) % n for x in range(n))
    if evaluate_word(n, word_a) != cycle or evaluate_word(n, word_b) != cycle:
        raise AssertionError("inverse words do not multiply to the long cycle")
    support_a, support_b = set(word_a), set(word_b)
    if len(support_a) != n - 1 or len(support_b) != n - 1:
        raise AssertionError("inverse word support is not a tree")
    distances = [
        len(support_a ^ conjugate_support(support_b, q, n)) // 2
        for q in range(n)
    ]
    return {
        "n": n,
        "parking_a": parking_a,
        "parking_b": parking_b,
        "stanley_tree_a": tree_a,
        "stanley_tree_b": tree_b,
        "stanley_tree_basis_distance": len(set(tree_a) ^ set(tree_b)) // 2,
        "factor_word_a": word_a,
        "factor_word_b": word_b,
        "raw_support_a": sorted(support_a),
        "raw_support_b": sorted(support_b),
        "raw_support_basis_distances_to_cyclic_target_phases": distances,
        "minimum_raw_support_basis_distance_mod_U": min(distances),
        "one_contiguous_Hurwitz_bubble_mod_U_impossible": min(distances) > 1,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=20)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "claim_tested": (
            "The one-basis-exchange Stanley family with parking labels "
            "(0,1,1,3^(n-4)) and (0,2,2,0,4^(n-5)) is reachable by one "
            "contiguous Hurwitz bubble after a cyclic endpoint conjugation."
        ),
        "proof_principle": (
            "A contiguous Hurwitz bubble conjugates only the bubbled raw factor; "
            "all crossed factors merely shift positions.  It therefore changes "
            "the raw support tree by at most one basis exchange."
        ),
        "scope_warning": (
            "Finite rows suggest a closed form but prove no universal formula; "
            "the report must separately prove any asymptotic claim."
        ),
        "convention": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "n_max": args.n_max,
        "rows": [row(n) for n in range(5, args.n_max + 1)],
        "python": platform.python_version(),
        "seed": None,
        "deterministic": True,
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": " ".join(sys.argv),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["rows"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

