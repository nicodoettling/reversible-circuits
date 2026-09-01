#!/usr/bin/env python3
"""Exact fixed-cell M330 check of the sole M329 obligation N_A > 0.

Scope is frozen to k=7, H_2, cell (s,t)=(1,1), Sigma={0,1,6,14,20},
and M323's fixed B atom e=(6,14), f=(3,5).  The script retains and tests
the A-side raw marked slots.  It reconstructs only the fixed-cell B profile
aggregate needed to define the residual weights; it performs no B search.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


K = 7
DROW = 2
CELL = (1, 1)
SIGMA = {0, 1, 6, 14, 20}
FIXED_B_FIRST_EDGE = (6, 14)
FIXED_B_SECOND_EDGE = (3, 5)

M323_TOP = "0aa6cfccd9d5feaf16ded0c4c5b5bf42d552c1f36ff4f4ce58998c927cbac39c"
M323_SCRIPT = "4a00e3d5e74c7d92ba5f95bdbde447a33f1ef327d9625a40445be101f4f81bc1"
M323_RESULTS = "134de6bd6972654bf3b264ef6dac94744007b735f18bc1955b03061e83cf7821"
M326_TOP = "a1ea699e4086cb967875c9408f586afc0854c85096a278e32eed9697b5ba2a2a"
M329_TOP = "6f3c67dadba4475b70f3372f4b61be575f917f463dd3c62db1afc14813aa11df"
M297_TOP = "a1bfa3684113b84cad5741061fcebb860cc52461ef29f0f02e29752a68dc1792"
M297_SCRIPT = "9809433b8a978831d105f1de71f56f6f63424fa472756c6e3944b87390161b73"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def load_source(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def source_cell_records(m323, primitive, label: str, split_target: int = 1):
    """Reproduce M323 raw_source but retain only the fixed split-one fiber."""
    n = 3 * K
    h = primitive.cyc(n, tuple(range(n)))
    if label == "A":
        source = primitive.cyc(n, (0, K, 2 * K))
    elif label == "B":
        source = primitive.mul(primitive.tr(n, 0, 1), primitive.tr(n, K, 2 * K))
    else:
        raise AssertionError(label)
    residual = primitive.mul(primitive.inv(source), h)
    original = primitive.cycles(residual)
    owner = {x: i for i, component in enumerate(original) for x in component}
    middle = owner[K]
    r0 = primitive.rank(residual)
    denominator = primitive.completion(residual, r0)
    records = []
    for first_owner, component in enumerate(original):
        for first_edge, first in m323.edges(primitive, n, component):
            after_first = primitive.mul(first, residual)
            for child in primitive.cycles(after_first):
                second_owner = owner[child[0]]
                assert all(owner[x] == second_owner for x in child)
                for second_edge, second in m323.edges(primitive, n, child):
                    after_second = primitive.mul(second, after_first)
                    numerator = primitive.completion(after_second, r0 - 2)
                    if not numerator:
                        continue
                    channel = int(first_owner != middle) + int(second_owner != middle)
                    if channel == 0:
                        continue
                    if channel == 1:
                        if first_owner != middle:
                            split = m323.chord_split(original[first_owner], *first_edge)
                        else:
                            split = m323.chord_split(original[second_owner], *second_edge)
                    else:
                        split = m323.chord_split(original[first_owner], *first_edge)
                    if split != split_target:
                        continue
                    records.append(
                        {
                            "channel": channel,
                            "split": split,
                            "first_edge": first_edge,
                            "second_edge": second_edge,
                            "first": first,
                            "second": second,
                            "product": primitive.mul(first, second),
                            "completion_numerator": numerator,
                            "completion_denominator": denominator,
                            "mass": Fraction(numerator, denominator),
                        }
                    )
    return records, residual


def marked_fiber(m323, primitive, records, split_mass: Fraction, retain: bool):
    n = 3 * K
    h = primitive.cyc(n, tuple(range(n)))
    aggregate = defaultdict(Fraction)
    raw_slots = []
    cache = {}
    for record in records:
        product = record["product"]
        cache.setdefault(product, m323.slot_data(primitive, n, h, product))
        conditional_mass = record["mass"] / split_mass
        for slot in cache[product]:
            aggregate[slot["profile"]] += conditional_mass
            if retain:
                raw_slots.append({**record, **slot, "conditional_mass": conditional_mass})
    return aggregate, raw_slots


def main(repo: Path):
    root = repo / "experiments/20260811-polynomial-mixing-resolution"
    m323_dir = root / "cycle-96/mission-M323-source-local-edge-coboundary"
    m326_dir = root / "cycle-97/mission-M326-m323-fresh-referee"
    m329_dir = root / "cycle-98/mission-M329-m326-freeze-salvage"
    m297_dir = root / "cycle-83/mission-M297-bodt-small-owner-tail"
    observed = {
        "M323_top": sha(m323_dir / "SHA256SUMS"),
        "M323_script": sha(m323_dir / "slpf_k7_h2_guard.py"),
        "M323_results": sha(m323_dir / "slpf_k7_h2_results.json"),
        "M326_top": sha(m326_dir / "SHA256SUMS"),
        "M329_top": sha(m329_dir / "SHA256SUMS"),
        "M297_top": sha(m297_dir / "SHA256SUMS"),
        "M297_script": sha(m297_dir / "bodt_k9_probe.py"),
    }
    expected = {
        "M323_top": M323_TOP,
        "M323_script": M323_SCRIPT,
        "M323_results": M323_RESULTS,
        "M326_top": M326_TOP,
        "M329_top": M329_TOP,
        "M297_top": M297_TOP,
        "M297_script": M297_SCRIPT,
    }
    assert observed == expected

    m323 = load_source(m323_dir / "slpf_k7_h2_guard.py", "m330_locked_m323")
    primitive, primitive_hashes = m323.load_primitives(repo)
    assert primitive_hashes == {"manifest": M297_TOP, "script": M297_SCRIPT}
    frozen_b = json.loads((m323_dir / "slpf_k7_h2_results.json").read_text())["first_witness"]
    assert tuple(frozen_b["cell"]) == CELL
    assert tuple(frozen_b["first_edge"]) == FIXED_B_FIRST_EDGE
    assert tuple(frozen_b["second_edge"]) == FIXED_B_SECOND_EDGE
    assert frozen_b["owner_seam_intersection"] == []
    assert frozen_b["head_seam_intersection"] == []

    p, q = m323.split_laws(primitive, K)
    s, t = CELL
    pi = min(q[s], p[t])
    assert pi == Fraction(frozen_b["pi"])

    records_a, residual_a = source_cell_records(m323, primitive, "A", s)
    records_b, _ = source_cell_records(m323, primitive, "B", t)
    marks_a, slots_a = marked_fiber(m323, primitive, records_a, q[s], retain=True)
    marks_b, discarded_b_slots = marked_fiber(m323, primitive, records_b, p[t], retain=False)
    assert discarded_b_slots == []

    m = K - 1
    alpha_sum = Fraction(2 * (4 * m - 1), 3 * (3 * m - 1))
    c_h = 3 * alpha_sum
    assert c_h == Fraction(46, 17)
    assert sum(marks_a.values(), Fraction(0)) == c_h
    assert sum(marks_b.values(), Fraction(0)) == c_h
    profiles = set(marks_a) | set(marks_b)
    g = {profile: mass / c_h for profile, mass in marks_a.items()}
    f = {profile: mass / c_h for profile, mass in marks_b.items()}
    a = {profile: max(g.get(profile, 0) - f.get(profile, 0), 0) for profile in profiles}
    b = {profile: max(f.get(profile, 0) - g.get(profile, 0), 0) for profile in profiles}
    rho_a = sum(a.values(), Fraction(0))
    rho_b = sum(b.values(), Fraction(0))
    rho = Fraction(frozen_b["cell_rho"])
    assert rho_a == rho_b == rho

    positive_a_slots = []
    n_a = Fraction(0)
    for atom in slots_a:
        profile = atom["profile"]
        a_profile = a.get(profile, Fraction(0))
        if not a_profile:
            continue
        profile_mark_mass = marks_a[profile]
        pr_given_profile = atom["conditional_mass"] / profile_mark_mass
        residual_atom_mass = a_profile * pr_given_profile
        touch_owner = sorted(SIGMA.intersection(atom["chi"]))
        touch_heads = sorted(SIGMA.intersection(atom["heads"]))
        non_touch = not touch_owner and not touch_heads
        if non_touch:
            n_a += residual_atom_mass
        positive_a_slots.append(
            {
                **atom,
                "a_profile": a_profile,
                "profile_mark_mass": profile_mark_mass,
                "pr_given_profile": pr_given_profile,
                "residual_atom_mass": residual_atom_mass,
                "touch_owner": touch_owner,
                "touch_heads": touch_heads,
                "non_touch": non_touch,
            }
        )

    positive_a_slots.sort(
        key=lambda atom: (
            atom["first_edge"], atom["second_edge"], atom["slot"], atom["product"]
        )
    )
    non_touch_atoms = [atom for atom in positive_a_slots if atom["non_touch"]]
    first = non_touch_atoms[0] if non_touch_atoms else None

    b_profile = tuple(frozen_b["profile"])
    b_q = b[b_profile]
    assert b_q == Fraction(frozen_b["positive_residual_B_profile_mass"])
    assert g.get(b_profile, Fraction(0)) == 0
    b_atom_conditional_mark_mass = Fraction(frozen_b["raw_conditional_mark_mass_B"])
    pr_eta = b_atom_conditional_mark_mass / marks_b[b_profile]
    assert pr_eta == Fraction(1, 2)

    r0 = primitive.rank(residual_a)
    fixed_first = primitive.tr(3 * K, *FIXED_B_FIRST_EDGE)
    fixed_second = primitive.tr(3 * K, *FIXED_B_SECOND_EDGE)
    after_first = primitive.mul(fixed_first, residual_a)
    after_second = primitive.mul(fixed_second, after_first)
    fixed_b_opposite_ranks = (
        r0,
        primitive.rank(after_first),
        primitive.rank(after_second),
    )
    assert fixed_b_opposite_ranks == tuple(frozen_b["source_A_ranks_before_after_first_after_second"])
    assert fixed_b_opposite_ranks != (r0, r0 - 1, r0 - 2)

    payload = {
        "status": "exact fixed-cell M329 N_A salvage",
        "scope": {
            "k": K,
            "n": 3 * K,
            "row": "H_2",
            "cell": list(CELL),
            "fixed_B_edges": [list(FIXED_B_FIRST_EDGE), list(FIXED_B_SECOND_EDGE)],
            "Sigma": sorted(SIGMA),
            "other_cells": False,
            "other_ranks": False,
            "other_surgeries": False,
        },
        "dependency_hashes": observed,
        "c_H": exact(c_h),
        "pi_11": exact(pi),
        "rho_11": exact(rho),
        "A_split_one_prefix_count": len(records_a),
        "A_raw_marked_slot_count": len(slots_a),
        "A_positive_residual_raw_slot_count": len(positive_a_slots),
        "A_nonTouch_positive_residual_raw_slot_count": len(non_touch_atoms),
        "N_A": exact(n_a),
        "N_A_positive": n_a > 0,
        "fixed_B": {
            "profile": list(b_profile),
            "b_Q": exact(b_q),
            "Pr_eta_given_t_Q": exact(pr_eta),
            "Touch_Sigma": False,
            "opposite_A_ranks": list(fixed_b_opposite_ranks),
            "opposite_A_prefix_valid": False,
        },
        "mpcf_or_downstream_inference": False,
    }

    if first is not None:
        pair_mass = c_h * pi * first["residual_atom_mass"] * b_q * pr_eta / rho
        total_fixed_b_non_touch_mass = c_h * pi * n_a * b_q * pr_eta / rho
        payload["first_nonTouch_A_atom"] = {
            "channel": first["channel"],
            "split": first["split"],
            "first_edge": list(first["first_edge"]),
            "second_edge": list(first["second_edge"]),
            "product": list(first["product"]),
            "slot": first["slot"],
            "owner_size": first["size"],
            "marked_owner_support": list(first["chi"]),
            "support_heads": list(first["heads"]),
            "owner_seam_intersection": first["touch_owner"],
            "head_seam_intersection": first["touch_heads"],
            "Touch_Sigma": False,
            "profile": list(first["profile"]),
            "completion_numerator": first["completion_numerator"],
            "completion_denominator": first["completion_denominator"],
            "raw_unconditional_prefix_mass": exact(first["mass"]),
            "split_probability_q_1": exact(q[s]),
            "raw_conditional_mark_mass": exact(first["conditional_mass"]),
            "A_profile_mark_mass": exact(first["profile_mark_mass"]),
            "a_profile_residual_mass": exact(first["a_profile"]),
            "Pr_xi_given_s_profile": exact(first["pr_given_profile"]),
            "A_residual_atom_mass": exact(first["residual_atom_mass"]),
            "exact_pair_token_mass_with_fixed_B": exact(pair_mass),
        }
        payload["both_token_endpoints_outside_Exc_pf"] = True
        payload["S_pf_defined_on_token"] = False
        payload["exact_total_token_mass_fixed_B_over_all_nonTouch_A"] = exact(
            total_fixed_b_non_touch_mass
        )
    else:
        payload["both_token_endpoints_outside_Exc_pf"] = False
        payload["S_pf_defined_on_token"] = None
    return payload


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(main(args.repo), indent=2, sort_keys=True) + "\n")
