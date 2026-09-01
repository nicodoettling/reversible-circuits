#!/usr/bin/env python3
"""Sole exact k=7,H_2 residual-token guard for frozen M323 S_pf.

The guard SHA-gates frozen M297 for permutation/completion primitives.  It
tests only whether an actual positive-residual source-B raw marked atom lies
outside Exc_pf while its product-fixed opposite-source prefix is invalid.
It does not evaluate MPCF or any other row/rank/surgery.
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
from itertools import combinations
from pathlib import Path


K = 7
DROW = 2
M297_TOP = "a1bfa3684113b84cad5741061fcebb860cc52461ef29f0f02e29752a68dc1792"
M297_SCRIPT = "9809433b8a978831d105f1de71f56f6f63424fa472756c6e3944b87390161b73"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else str(x)


def load_primitives(repo: Path):
    directory = repo / "experiments/20260811-polynomial-mixing-resolution/cycle-83/mission-M297-bodt-small-owner-tail"
    manifest = directory / "SHA256SUMS"
    script = directory / "bodt_k9_probe.py"
    observed = {"manifest": sha(manifest), "script": sha(script)}
    expected = {"manifest": M297_TOP, "script": M297_SCRIPT}
    assert observed == expected
    spec = importlib.util.spec_from_file_location("m323_m297_primitives", script)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module, observed


def edges(module, n, component):
    for x, y in combinations(sorted(component), 2):
        yield (x, y), module.tr(n, x, y)


def chord_split(component, x, y):
    pos = {v: i for i, v in enumerate(component)}
    d = len(component)
    gap = (pos[y] - pos[x]) % d
    return min(gap, d - gap)


def raw_source(module, k, label):
    n = 3 * k
    h = module.cyc(n, tuple(range(n)))
    if label == "A":
        source = module.cyc(n, (0, k, 2 * k))
    else:
        source = module.mul(module.tr(n, 0, 1), module.tr(n, k, 2 * k))
    residual = module.mul(module.inv(source), h)
    original = module.cycles(residual)
    owner = {x: i for i, c in enumerate(original) for x in c}
    middle = owner[k]
    r0 = module.rank(residual)
    denominator = module.completion(residual, r0)
    records = []
    for first_owner, component in enumerate(original):
        for first_edge, first in edges(module, n, component):
            after_first = module.mul(first, residual)
            for child in module.cycles(after_first):
                second_owner = owner[child[0]]
                assert all(owner[x] == second_owner for x in child)
                for second_edge, second in edges(module, n, child):
                    after_second = module.mul(second, after_first)
                    numerator = module.completion(after_second, r0 - 2)
                    if not numerator:
                        continue
                    channel = int(first_owner != middle) + int(second_owner != middle)
                    if channel == 0:
                        continue
                    if channel == 1:
                        if first_owner != middle:
                            split = chord_split(original[first_owner], *first_edge)
                        else:
                            split = chord_split(original[second_owner], *second_edge)
                    else:
                        split = chord_split(original[first_owner], *first_edge)
                    records.append(
                        {
                            "channel": channel,
                            "split": split,
                            "first_edge": first_edge,
                            "second_edge": second_edge,
                            "first": first,
                            "second": second,
                            "product": module.mul(first, second),
                            "mass": Fraction(numerator, denominator),
                        }
                    )
    return records, residual, original


def w(module, d, s):
    return Fraction(math.factorial(d - 2)) * module.tau(s) * module.tau(d - s) / (d ** (d - 2))


def split_laws(module, k):
    p = {s: (2 * k - 1) * w(module, 2 * k - 1, s) for s in range(1, k)}
    q = {s: k * w(module, k, s) for s in range(1, (k - 1) // 2 + 1)}
    assert sum(p.values(), Fraction(0)) == 1
    assert sum(q.values(), Fraction(0)) == 1
    return p, q


def quantile_cells(p, q):
    pcum = Fraction(0)
    pints = {}
    for t in sorted(p):
        pints[t] = (pcum, pcum + p[t])
        pcum += p[t]
    qcum = Fraction(0)
    qints = {}
    for s in sorted(q):
        qints[s] = (qcum, qcum + q[s])
        qcum += q[s]
    ans = {}
    for s, (qa, qb) in qints.items():
        for t, (pa, pb) in pints.items():
            mass = min(qb, pb) - max(qa, pa)
            if mass > 0:
                ans[(s, t)] = mass
    assert sum(ans.values(), Fraction(0)) == 1
    return ans


def slot_data(module, n, h, product):
    generic, sizes = module.owner_profile(n, h, product)
    heads = tuple(i for i, owner in enumerate(generic) if owner is None)
    zero = tuple(0 for _ in range(n - 4))
    ans = []
    for slot in range(3):
        chi = tuple(i for i, owner in enumerate(generic) if owner == slot)
        if sizes[slot] != DROW:
            profile = zero
        else:
            ind = tuple(int(owner == slot) for owner in generic)
            hd = tuple(int(owner is None) for owner in generic)
            row = tuple(a + b for a, b in zip(module.corr01(ind, hd), module.corr01(hd, ind)))
            delta = module.int_derivative(row)
            profile = tuple(delta[ell] for ell in range(2, n - 2))
        ans.append({"slot": slot, "size": sizes[slot], "chi": chi, "heads": heads, "profile": profile})
    return ans


def build_marks(module, k, records, base):
    n = 3 * k
    h = module.cyc(n, tuple(range(n)))
    marks = defaultdict(lambda: defaultdict(Fraction))
    raw_slots = []
    cache = {}
    for record in records:
        split = record["split"]
        product = record["product"]
        cache.setdefault(product, slot_data(module, n, h, product))
        conditional_mass = record["mass"] / base[split]
        for slot in cache[product]:
            marks[split][slot["profile"]] += conditional_mass
            raw_slots.append({**record, **slot, "conditional_mass": conditional_mass})
    return marks, raw_slots


def main(repo: Path):
    module, hashes = load_primitives(repo)
    p, q = split_laws(module, K)
    cells = quantile_cells(p, q)
    raw_a, residual_a, _ = raw_source(module, K, "A")
    raw_b, _, _ = raw_source(module, K, "B")
    marks_a, _ = build_marks(module, K, raw_a, q)
    marks_b, slots_b = build_marks(module, K, raw_b, p)

    m = K - 1
    alpha_sum = Fraction(2 * (4 * m - 1), 3 * (3 * m - 1))
    c_h = 3 * alpha_sum
    for split in q:
        assert sum(marks_a[split].values(), Fraction(0)) == c_h
    for split in p:
        assert sum(marks_b[split].values(), Fraction(0)) == c_h

    sigma = {0, 1, K - 1, 2 * K, 3 * K - 1}
    candidates = []
    for (s, t), pi in sorted(cells.items()):
        g = {profile: mass / c_h for profile, mass in marks_a[s].items()}
        f = {profile: mass / c_h for profile, mass in marks_b[t].items()}
        profiles = set(g) | set(f)
        rho = sum((max(g.get(profile, 0) - f.get(profile, 0), 0) for profile in profiles), Fraction(0))
        assert rho == sum((max(f.get(profile, 0) - g.get(profile, 0), 0) for profile in profiles), Fraction(0))
        if not rho:
            continue
        for atom in slots_b:
            if atom["split"] != t or atom["size"] != DROW:
                continue
            profile = atom["profile"]
            residual_b = max(f.get(profile, 0) - g.get(profile, 0), 0)
            if not residual_b:
                continue
            if sigma.intersection(atom["chi"]) or sigma.intersection(atom["heads"]):
                continue
            after_first_a = module.mul(atom["first"], residual_a)
            after_second_a = module.mul(atom["second"], after_first_a)
            r0 = module.rank(residual_a)
            valid_a = (
                module.rank(after_first_a) == r0 - 1
                and module.rank(after_second_a) == r0 - 2
                and module.completion(after_second_a, r0 - 2) > 0
            )
            if valid_a:
                continue
            f_profile = f[profile]
            token_mass = pi * residual_b * atom["conditional_mass"] / f_profile
            candidates.append(
                {
                    "s": s,
                    "t": t,
                    "pi": pi,
                    "rho": rho,
                    "atom": atom,
                    "g_profile": g.get(profile, Fraction(0)),
                    "f_profile": f_profile,
                    "residual_b": residual_b,
                    "token_mass": token_mass,
                    "rank_a": (r0, module.rank(after_first_a), module.rank(after_second_a)),
                }
            )

    def key(item):
        atom = item["atom"]
        return (item["s"], item["t"], atom["first_edge"], atom["second_edge"], atom["slot"], atom["product"])

    candidates.sort(key=key)
    witness = candidates[0] if candidates else None
    payload = {
        "status": "sole exact k=7,H_2 guard of frozen S_pf/Exc_pf",
        "dependency_hashes": hashes,
        "scope": {"k": K, "n": 3 * K, "row": "H_2", "other_rows": False, "other_ranks": False},
        "c_H": exact(c_h),
        "quantile_cell_count": len(cells),
        "raw_prefix_counts": {"A": len(raw_a), "B": len(raw_b)},
        "nonexceptional_residual_invalid_count": len(candidates),
        "refutes_S_pf": witness is not None,
        "mpcf_inference": False,
    }
    if witness is not None:
        atom = witness["atom"]
        payload["first_witness"] = {
            "cell": [witness["s"], witness["t"]],
            "pi": exact(witness["pi"]),
            "channel_B": atom["channel"],
            "split_B": atom["split"],
            "first_edge": list(atom["first_edge"]),
            "second_edge": list(atom["second_edge"]),
            "product": list(atom["product"]),
            "slot": atom["slot"],
            "owner_size": atom["size"],
            "marked_owner_support": list(atom["chi"]),
            "support_heads": list(atom["heads"]),
            "seam_vertices": sorted(sigma),
            "owner_seam_intersection": sorted(sigma.intersection(atom["chi"])),
            "head_seam_intersection": sorted(sigma.intersection(atom["heads"])),
            "profile": list(atom["profile"]),
            "raw_unconditional_mass_B": exact(atom["mass"]),
            "raw_conditional_mark_mass_B": exact(atom["conditional_mass"]),
            "g_A_profile_mass": exact(witness["g_profile"]),
            "f_B_profile_mass": exact(witness["f_profile"]),
            "positive_residual_B_profile_mass": exact(witness["residual_b"]),
            "cell_rho": exact(witness["rho"]),
            "positive_token_mass_from_raw_atom": exact(witness["token_mass"]),
            "source_A_ranks_before_after_first_after_second": list(witness["rank_a"]),
            "opposite_source_prefix_valid": False,
        }
    return payload


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(main(args.repo), indent=2, sort_keys=True) + "\n")
