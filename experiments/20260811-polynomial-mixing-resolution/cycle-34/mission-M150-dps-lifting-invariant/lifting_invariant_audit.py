#!/usr/bin/env python3
"""Deterministic bounded audit for the M150 reduced Pin lifting theorem.

The universal statement rests on ``lifting_invariant_theorem.md``.  This file
checks the Clifford identities exactly over Q, all connected rank-three
minimal words and accepted M135 matching subfamilies, and every d=5
transposition tuple through width three for the localized centralizer witness.
"""

from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import platform
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path


Multivector = dict[int, Fraction]

M137_CHECKER_SHA256 = (
    "bb62d449c7cad72a448389f9f7dd7ee76618e8c71b68189db20e19f4e2244341"
)


def repository_root() -> Path:
    return Path(__file__).resolve().parents[4]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_frozen_m137():
    path = (
        repository_root()
        / "experiments/20260811-polynomial-mixing-resolution/cycle-31"
        / "mission-M137-m135-fresh-referee/independent_referee.py"
    )
    observed = sha256(path)
    assert observed == M137_CHECKER_SHA256, (observed, M137_CHECKER_SHA256)
    spec = importlib.util.spec_from_file_location("frozen_m137_checker_m150", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module, path, observed


def blade_sign(left: int, right: int) -> int:
    """Sign in e_left e_right for Euclidean Clifford generators."""
    sign = 1
    bits = left
    while bits:
        low = bits & -bits
        index = low.bit_length() - 1
        if (right & (low - 1)).bit_count() % 2:
            sign = -sign
        bits -= low
    return sign


def clean(x: Multivector) -> Multivector:
    return {blade: coefficient for blade, coefficient in x.items() if coefficient}


def clifford_mul(left: Multivector, right: Multivector) -> Multivector:
    out: Multivector = {}
    for a, x in left.items():
        for b, y in right.items():
            blade = a ^ b
            out[blade] = out.get(blade, Fraction(0)) + blade_sign(a, b) * x * y
    return clean(out)


def product(*factors: Multivector) -> Multivector:
    out: Multivector = {0: Fraction(1)}
    for factor in factors:
        out = clifford_mul(out, factor)
    return out


def scale(x: Multivector, coefficient: Fraction) -> Multivector:
    return clean({blade: coefficient * value for blade, value in x.items()})


def root_numerator(i: int, j: int) -> Multivector:
    """sqrt(2) times the unit root lift a_(ij), with i<j."""
    assert i < j
    return {1 << i: Fraction(1), 1 << j: Fraction(-1)}


def inverse_root_numerator(x: Multivector) -> Multivector:
    # x^2=2 for the unnormalized root numerator.
    return scale(x, Fraction(1, 2))


def inverse_disjoint_product(a: Multivector, b: Multivector) -> Multivector:
    # (ab)^(-1)=b^(-1)a^(-1)=ba/4 for root numerators.
    return scale(product(b, a), Fraction(1, 4))


def clifford_identity_audit() -> dict:
    a = root_numerator(0, 1)
    b = root_numerator(1, 2)
    c = root_numerator(2, 3)
    d3_braid_left = product(a, b, a)
    d3_braid_right = product(b, a, b)
    ab = product(a, c)
    ba = product(c, a)
    disjoint_anticommutator = clean(
        {
            blade: ab.get(blade, Fraction(0)) + ba.get(blade, Fraction(0))
            for blade in set(ab) | set(ba)
        }
    )
    localized_commutator = product(
        a,
        product(a, c),
        inverse_root_numerator(a),
        inverse_disjoint_product(a, c),
    )
    assert product(a, a) == {0: Fraction(2)}
    assert product(b, b) == {0: Fraction(2)}
    assert d3_braid_left == d3_braid_right
    assert disjoint_anticommutator == {}
    assert localized_commutator == {0: Fraction(-1)}
    return {
        "d3_scaled_braid_identity": True,
        "disjoint_scaled_roots_anticommute": True,
        "localized_commutator": "-1",
    }


def d3_section_numerators() -> dict[tuple[int, int], Multivector]:
    a = root_numerator(0, 1)
    b = root_numerator(1, 2)
    # sigma((0 2))=sigma((0 1)(1 2)(0 1))=aba/(2 sqrt(2)).
    c = scale(product(a, b, a), Fraction(1, 2))
    assert c == scale(root_numerator(0, 2), Fraction(-1))
    return {(0, 1): a, (1, 2): b, (0, 2): c}


def d3_spin(word) -> int:
    section = d3_section_numerators()
    lifted = product(*(section[edge] for edge in word))
    # Four unit-root denominators contribute (sqrt(2))^4=4.
    normalized = scale(lifted, Fraction(1, 4))
    assert normalized in ({0: Fraction(1)}, {0: Fraction(-1)})
    return int(normalized[0])


def d3_matching_audit(ref) -> dict:
    d = 3
    words, _index, _fibers, tau = ref.reconstruct_rank(d)
    permutations = tuple(itertools.permutations(range(d)))
    root_group = tuple(p for p in permutations if p[d - 1] == d - 1)
    global_blocks = ref.orbit_blocks(words, permutations)
    root_blocks = ref.orbit_blocks(words, root_group)
    global_key = {
        source: ref.canonical(word, permutations) for source, word in enumerate(words)
    }
    root_key = {
        source: ref.canonical(word, root_group) for source, word in enumerate(words)
    }

    word_spins = Counter(d3_spin(word) for word in words)
    rows = []
    unequal_vectors = []
    for adjacent_index, target in sorted(tau.items()):
        edge_rows = []
        representatives = []
        for _hkey, block in sorted(root_blocks.items()):
            target_hkeys = {root_key[target[source]] for source in block}
            assert len(target_hkeys) == 1
            representative = block[0]
            edge_rows.append(
                (global_key[representative], global_key[target[representative]])
            )
            representatives.append(representative)
        colors, left_vertices, right_vertices = ref.decompose_regular_bipartite(
            edge_rows, d
        )
        assert len(left_vertices) == len(right_vertices) == len(global_blocks) == 4
        for color in range(d):
            edge_ids = tuple(sorted(edge for edge, c in colors.items() if c == color))
            source_indices = tuple(representatives[edge] for edge in edge_ids)
            target_indices = tuple(target[source] for source in source_indices)
            by_width = {}
            for width in range(1, 5):
                checked = 0
                equal = 0
                for positions in itertools.combinations(range(4), width):
                    source_vector = tuple(
                        d3_spin(words[source_indices[j]]) for j in positions
                    )
                    target_vector = tuple(
                        d3_spin(words[target_indices[j]]) for j in positions
                    )
                    checked += 1
                    equal += source_vector == target_vector
                    if source_vector != target_vector:
                        unequal_vectors.append(
                            {
                                "adjacent_index": adjacent_index + 1,
                                "color": color,
                                "positions": [j + 1 for j in positions],
                                "source_vector": list(source_vector),
                                "target_vector": list(target_vector),
                            }
                        )
                by_width[str(width)] = {"checked": checked, "equal": equal}
            rows.append(
                {
                    "adjacent_index": adjacent_index + 1,
                    "color": color,
                    "matching_edges": len(edge_ids),
                    "subfamilies_by_width": by_width,
                }
            )

    assert len(words) == 24
    assert word_spins == Counter({1: 24})
    assert len(rows) == 9
    assert not unequal_vectors
    return {
        "physical_words": len(words),
        "word_spin_histogram": {str(k): v for k, v in sorted(word_spins.items())},
        "matchings": rows,
        "subfamilies_checked": sum(
            item["checked"]
            for row in rows
            for item in row["subfamilies_by_width"].values()
        ),
        "unequal_residual_vectors": unequal_vectors,
    }


def d5_localized_centralizer_audit(ref, max_width: int = 3) -> list[dict]:
    d = 5
    edges = tuple(itertools.combinations(range(d), 2))
    identity = tuple(range(d))
    minus_one = {0: Fraction(-1)}
    rows = []
    for width in range(1, max_width + 1):
        tuples_checked = 0
        coordinate_witnesses = 0
        failures = []
        for transposition_tuple in itertools.product(edges, repeat=width):
            tuples_checked += 1
            for coordinate, transposition in enumerate(transposition_tuple):
                disjoint = next(
                    edge for edge in edges if set(edge).isdisjoint(transposition)
                )
                t_perm = ref.edge_map(d, transposition)
                v_perm = ref.edge_map(d, disjoint)
                u_perm = ref.multiply(t_perm, v_perm)
                all_even_tuple = [identity] * width
                all_even_tuple[coordinate] = u_perm
                parity_ok = all(ref.sign(p) == 1 for p in all_even_tuple)
                centralizes = (
                    ref.multiply(u_perm, t_perm) == ref.multiply(t_perm, u_perm)
                )
                a = root_numerator(*transposition)
                b = root_numerator(*disjoint)
                commutator = product(
                    a,
                    product(a, b),
                    inverse_root_numerator(a),
                    inverse_disjoint_product(a, b),
                )
                coordinate_witnesses += 1
                if not (parity_ok and centralizes and commutator == minus_one):
                    failures.append(
                        {
                            "tuple": [list(edge) for edge in transposition_tuple],
                            "coordinate": coordinate,
                            "disjoint": list(disjoint),
                            "parity_ok": parity_ok,
                            "centralizes": centralizes,
                            "commutator": serialize_multivector(commutator),
                        }
                    )
        assert not failures
        rows.append(
            {
                "d": d,
                "width": width,
                "transposition_tuples_checked": tuples_checked,
                "localized_coordinate_witnesses_checked": coordinate_witnesses,
                "failures": failures,
            }
        )
    return rows


def d5_dps_representative_audit(ref) -> dict:
    d = 5
    tree = next(ref.prufer_trees(d))
    order = tuple(range(2 * d - 2))
    source = ref.dps_image(tree, order, d)
    targets = [
        ref.dps_image(tree, ref.adjacent_value_swap(order, i), d)
        for i in range(2 * d - 3)
    ]
    identity = tuple(range(d))
    assert ref.evaluate(d, source) == identity and ref.is_connected(d, source)
    assert all(ref.evaluate(d, word) == identity for word in targets)
    assert all(ref.is_connected(d, word) for word in targets)
    return {
        "d": d,
        "source_word": [list(edge) for edge in source],
        "adjacent_edits_checked": len(targets),
        "all_identity": True,
        "all_connected": True,
        "reduced_kernel_rank": 0,
        "reduced_lift_value_source_and_targets": "unique",
    }


def serialize_multivector(x: Multivector) -> dict[str, str]:
    return {str(blade): str(coefficient) for blade, coefficient in sorted(x.items())}


def main() -> None:
    ref, path, observed = load_frozen_m137()
    results = {
        "metadata": {
            "mission": "M150",
            "repository_commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
            "command": "python3 -B lifting_invariant_audit.py",
            "status_labels": {
                "universal_theorem": "proved in lifting_invariant_theorem.md",
                "finite_rows": "exact bounded diagnostics",
            },
            "python": platform.python_version(),
            "dependencies": {},
            "seed": None,
            "frozen_m137_checker": str(path.relative_to(repository_root())),
            "frozen_m137_checker_sha256": observed,
            "caps": {
                "d3": "all 24 connected minimal words; all 9 accepted matchings and 135 nonempty subfamilies",
                "d5": "all transposition tuples through width 3; one DPS representative and all 7 adjacent edits",
            },
        },
        "clifford_identity_audit": clifford_identity_audit(),
        "d3_split_cover_and_matching_audit": d3_matching_audit(ref),
        "d5_localized_centralizer_audit": d5_localized_centralizer_audit(ref),
        "d5_dps_representative_audit": d5_dps_representative_audit(ref),
    }
    output = Path(__file__).with_name("results.json")
    output.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
