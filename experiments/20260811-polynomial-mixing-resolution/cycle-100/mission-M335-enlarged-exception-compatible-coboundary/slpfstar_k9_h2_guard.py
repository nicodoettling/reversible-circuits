#!/usr/bin/env python3
"""Sole exact k=9,H_2 guard for frozen M335 SLPF* formulas."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


K = 9
DROW = 2
M323_TOP = "0aa6cfccd9d5feaf16ded0c4c5b5bf42d552c1f36ff4f4ce58998c927cbac39c"
M323_SCRIPT = "4a00e3d5e74c7d92ba5f95bdbde447a33f1ef327d9625a40445be101f4f81bc1"
M330_TOP = "623ec4026179c81cc2a1ec49ce3318af470562924d7a34ac5bc6a6ba76547f93"
M297_TOP = "a1bfa3684113b84cad5741061fcebb860cc52461ef29f0f02e29752a68dc1792"
M297_SCRIPT = "9809433b8a978831d105f1de71f56f6f63424fa472756c6e3944b87390161b73"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def atom_key(atom):
    return (atom["first_edge"], atom["second_edge"], atom["slot"], atom["product"])


def touch(atom, sigma):
    return bool(sigma.intersection(atom["chi"]) or sigma.intersection(atom["heads"]))


def endpoint(atom):
    return {
        "channel": atom["channel"],
        "split": atom["split"],
        "first_edge": list(atom["first_edge"]),
        "second_edge": list(atom["second_edge"]),
        "slot": atom["slot"],
        "owner_size": atom["size"],
        "marked_owner_support": list(atom["chi"]),
        "support_heads": list(atom["heads"]),
        "profile": list(atom["profile"]),
        "raw_unconditional_mass": exact(atom["mass"]),
        "raw_conditional_mark_mass": exact(atom["conditional_mass"]),
    }


def main(repo: Path):
    root = repo / "experiments/20260811-polynomial-mixing-resolution"
    m323_dir = root / "cycle-96/mission-M323-source-local-edge-coboundary"
    m330_dir = root / "cycle-99/mission-M330-m323-a-partner-salvage"
    m297_dir = root / "cycle-83/mission-M297-bodt-small-owner-tail"
    observed = {
        "M323_top": sha(m323_dir / "SHA256SUMS"),
        "M323_script": sha(m323_dir / "slpf_k7_h2_guard.py"),
        "M330_top": sha(m330_dir / "SHA256SUMS"),
        "M297_top": sha(m297_dir / "SHA256SUMS"),
        "M297_script": sha(m297_dir / "bodt_k9_probe.py"),
    }
    assert observed == {
        "M323_top": M323_TOP,
        "M323_script": M323_SCRIPT,
        "M330_top": M330_TOP,
        "M297_top": M297_TOP,
        "M297_script": M297_SCRIPT,
    }

    m323 = load_module(m323_dir / "slpf_k7_h2_guard.py", "m335_locked_m323")
    primitive, primitive_hashes = m323.load_primitives(repo)
    assert primitive_hashes == {"manifest": M297_TOP, "script": M297_SCRIPT}

    p, q = m323.split_laws(primitive, K)
    cells = m323.quantile_cells(p, q)
    raw_a, _, _ = m323.raw_source(primitive, K, "A")
    raw_b, _, _ = m323.raw_source(primitive, K, "B")
    marks_a, slots_a = m323.build_marks(primitive, K, raw_a, q)
    marks_b, slots_b = m323.build_marks(primitive, K, raw_b, p)

    m = K - 1
    c_h = Fraction(2 * (4 * m - 1), 3 * m - 1)
    assert c_h == 3 * Fraction(2 * (4 * m - 1), 3 * (3 * m - 1))
    for split in q:
        assert sum(marks_a[split].values(), Fraction(0)) == c_h
    for split in p:
        assert sum(marks_b[split].values(), Fraction(0)) == c_h

    sigma = {0, 1, K - 1, 2 * K, 3 * K - 1}
    index_a = defaultdict(list)
    index_b = defaultdict(list)
    for atom in slots_a:
        index_a[atom_key(atom)].append(atom)
    for atom in slots_b:
        index_b[atom_key(atom)].append(atom)
    assert all(len(items) == 1 for items in index_a.values())
    assert all(len(items) == 1 for items in index_b.values())

    # Exc_pf^* is endpoint-local.  Retain only atoms for which the literal
    # opposite-source prefix exists and the marked owner/head misses Sigma.
    compatible_a = [
        atom for atom in slots_a if atom_key(atom) in index_b and not touch(atom, sigma)
    ]
    compatible_b = [
        atom for atom in slots_b if atom_key(atom) in index_a and not touch(atom, sigma)
    ]

    checked_tokens = 0
    first_failure = None
    for (s, t), pi in sorted(cells.items()):
        g = {profile: mass / c_h for profile, mass in marks_a[s].items()}
        f = {profile: mass / c_h for profile, mass in marks_b[t].items()}
        profiles = set(g) | set(f)
        a = {profile: max(g.get(profile, 0) - f.get(profile, 0), 0) for profile in profiles}
        b = {profile: max(f.get(profile, 0) - g.get(profile, 0), 0) for profile in profiles}
        rho = sum(a.values(), Fraction(0))
        assert rho == sum(b.values(), Fraction(0))
        if not rho:
            continue

        atoms_a = sorted(
            (atom for atom in compatible_a if atom["split"] == s and a.get(atom["profile"], 0) > 0),
            key=atom_key,
        )
        atoms_b = sorted(
            (atom for atom in compatible_b if atom["split"] == t and b.get(atom["profile"], 0) > 0),
            key=atom_key,
        )
        for xi in atoms_a:
            p_profile = xi["profile"]
            u_xi = xi["conditional_mass"] / marks_a[s][p_profile]
            for eta in atoms_b:
                checked_tokens += 1
                q_profile = eta["profile"]
                u_eta = eta["conditional_mass"] / marks_b[t][q_profile]
                sigma_eta = index_a[atom_key(eta)][0]
                sigma_xi = index_b[atom_key(xi)][0]
                s_prime = sigma_eta["split"]
                t_prime = sigma_xi["split"]
                assert sigma_eta["profile"] == q_profile
                assert sigma_xi["profile"] == p_profile
                assert not touch(sigma_eta, sigma)
                assert not touch(sigma_xi, sigma)
                original_weight = c_h * pi * a[p_profile] * b[q_profile] * u_xi * u_eta / rho

                common = {
                    "reason": None,
                    "original_cell": [s, t],
                    "derived_reverse_cell": [s_prime, t_prime],
                    "pi_original": exact(pi),
                    "rho_original": exact(rho),
                    "profile_P": list(p_profile),
                    "profile_Q": list(q_profile),
                    "a_original_P": exact(a[p_profile]),
                    "b_original_Q": exact(b[q_profile]),
                    "u_A_original": exact(u_xi),
                    "u_B_original": exact(u_eta),
                    "original_token_weight": exact(original_weight),
                    "xi_A": endpoint(xi),
                    "eta_B": endpoint(eta),
                    "sigma_eta_A": endpoint(sigma_eta),
                    "sigma_xi_B": endpoint(sigma_xi),
                    "all_four_Touch_Sigma": False,
                    "both_BadPref": False,
                }

                if (s_prime, t_prime) not in cells:
                    common["reason"] = "unsupported_reverse_quantile_cell"
                    common["pi_reverse"] = "0"
                    first_failure = common
                    break

                pi_prime = cells[(s_prime, t_prime)]
                g_prime = {
                    profile: mass / c_h for profile, mass in marks_a[s_prime].items()
                }
                f_prime = {
                    profile: mass / c_h for profile, mass in marks_b[t_prime].items()
                }
                profiles_prime = set(g_prime) | set(f_prime)
                a_prime = {
                    profile: max(g_prime.get(profile, 0) - f_prime.get(profile, 0), 0)
                    for profile in profiles_prime
                }
                b_prime = {
                    profile: max(f_prime.get(profile, 0) - g_prime.get(profile, 0), 0)
                    for profile in profiles_prime
                }
                rho_prime = sum(a_prime.values(), Fraction(0))
                assert rho_prime == sum(b_prime.values(), Fraction(0))
                common["pi_reverse"] = exact(pi_prime)
                common["rho_reverse"] = exact(rho_prime)
                common["a_reverse_Q"] = exact(a_prime.get(q_profile, Fraction(0)))
                common["b_reverse_P"] = exact(b_prime.get(p_profile, Fraction(0)))
                if not a_prime.get(q_profile, 0) or not b_prime.get(p_profile, 0):
                    common["reason"] = "reverse_residual_sign_failure"
                    first_failure = common
                    break

                u_sigma_eta = sigma_eta["conditional_mass"] / marks_a[s_prime][q_profile]
                u_sigma_xi = sigma_xi["conditional_mass"] / marks_b[t_prime][p_profile]
                reverse_weight = (
                    c_h
                    * pi_prime
                    * a_prime[q_profile]
                    * b_prime[p_profile]
                    * u_sigma_eta
                    * u_sigma_xi
                    / rho_prime
                )
                ratio = reverse_weight / original_weight
                common["u_A_reverse"] = exact(u_sigma_eta)
                common["u_B_reverse"] = exact(u_sigma_xi)
                common["reverse_token_weight"] = exact(reverse_weight)
                common["weight_ratio"] = exact(ratio)
                if ratio != 1:
                    common["reason"] = "exact_weight_mismatch"
                    first_failure = common
                    break

                # The second raw switch is literal identity because the key is
                # unchanged and every source index has one entry.
                assert index_b[atom_key(sigma_eta)][0] is eta
                assert index_a[atom_key(sigma_xi)][0] is xi
            if first_failure is not None:
                break
        if first_failure is not None:
            break

    return {
        "status": "sole exact k=9,H_2 guard of frozen M335 SLPF*",
        "dependency_hashes": observed,
        "scope": {
            "k": K,
            "n": 3 * K,
            "row": "H_2",
            "other_rows": False,
            "other_ranks": False,
            "other_surgeries": False,
        },
        "c_H": exact(c_h),
        "quantile_cell_count": len(cells),
        "raw_marked_slot_counts": {"A": len(slots_a), "B": len(slots_b)},
        "compatible_endpoint_counts": {"A": len(compatible_a), "B": len(compatible_b)},
        "tokens_checked_through_first_failure": checked_tokens,
        "compatible_coboundary_survives_guard": first_failure is None,
        "first_failure": first_failure,
        "exceptional_Borel_bound_tested": False,
        "mpcf_or_downstream_inference": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(main(args.repo), indent=2, sort_keys=True) + "\n")
