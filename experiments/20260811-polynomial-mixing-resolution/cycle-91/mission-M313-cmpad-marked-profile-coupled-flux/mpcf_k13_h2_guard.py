#!/usr/bin/env python3
"""Sole exact k=13 H_2 guard for M313's predeclared common flux.

This script SHA-gates frozen M297 only for permutation/completion primitives.
It constructs split-conditioned laws and the M313 flux locally.  It does not
read M305 code/data and never norms a channel, source, type, or incidence row.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import platform
import subprocess
import sys
import time
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path


K = 13
DROW = 2
M297_TOP = "a1bfa3684113b84cad5741061fcebb860cc52461ef29f0f02e29752a68dc1792"
M297_SCRIPT = "9809433b8a978831d105f1de71f56f6f63424fa472756c6e3944b87390161b73"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_primitives(repo: Path):
    directory = repo / "experiments/20260811-polynomial-mixing-resolution/cycle-83/mission-M297-bodt-small-owner-tail"
    manifest = directory / "SHA256SUMS"
    script = directory / "bodt_k9_probe.py"
    observed = {"manifest": sha(manifest), "script": sha(script)}
    expected = {"manifest": M297_TOP, "script": M297_SCRIPT}
    if observed != expected:
        raise AssertionError(("M297 gate", expected, observed))
    spec = importlib.util.spec_from_file_location("m313_m297_primitives", script)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module, observed


def edge_data(module, n, component):
    for x, y in combinations(sorted(component), 2):
        yield x, y, module.tr(n, x, y)


def chord_split(component, x, y):
    pos = {v: i for i, v in enumerate(component)}
    d = len(component)
    gap = (pos[y] - pos[x]) % d
    return min(gap, d - gap)


def tagged_source_law(module, k, label):
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
    law = defaultdict(Fraction)
    raw = 0
    for first_owner, component in enumerate(original):
        for x1, y1, first in edge_data(module, n, component):
            after_first = module.mul(first, residual)
            for child in module.cycles(after_first):
                second_owner = owner[child[0]]
                assert all(owner[x] == second_owner for x in child)
                for x2, y2, second in edge_data(module, n, child):
                    numerator = module.completion(module.mul(second, after_first), r0 - 2)
                    if not numerator:
                        continue
                    channel = int(first_owner != middle) + int(second_owner != middle)
                    if channel == 0:
                        continue
                    if channel == 1:
                        if first_owner != middle:
                            split = chord_split(original[first_owner], x1, y1)
                        else:
                            split = chord_split(original[second_owner], x2, y2)
                    else:
                        split = chord_split(original[first_owner], x1, y1)
                    product = module.mul(first, second)
                    law[(channel, split, product)] += Fraction(numerator, denominator)
                    raw += 1
    return dict(law), raw


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
    cells = {}
    for s, (qa, qb) in qints.items():
        for t, (pa, pb) in pints.items():
            mass = min(qb, pb) - max(qa, pa)
            if mass > 0:
                assert s <= t
                cells[(s, t)] = mass
    assert sum(cells.values(), Fraction(0)) == 1
    return cells


def add(measure, key, value):
    measure[key] += value
    if not measure[key]:
        del measure[key]


def h2_mark(module, n, h, product):
    generic, sizes = module.owner_profile(n, h, product)
    heads = tuple(int(v is None) for v in generic)
    zero = tuple(0 for _ in range(n - 4))
    ans = []
    for i in range(3):
        if sizes[i] != DROW:
            ans.append(zero)
            continue
        chi = tuple(int(v == i) for v in generic)
        row = tuple(a + b for a, b in zip(module.corr01(chi, heads), module.corr01(heads, chi)))
        delta = module.int_derivative(row)
        ans.append(tuple(delta[ell] for ell in range(2, n - 2)))
    return tuple(ans)


def conditional_marks(module, k, laws, p, q):
    n = 3 * k
    hperm = module.cyc(n, tuple(range(n)))
    m = k - 1
    denom = 3 * m * (3 * m - 1)
    alpha = {1: Fraction(4 * m * m, denom), 2: Fraction(2 * m * (2 * m - 1), denom)}
    out = {"A": defaultdict(lambda: defaultdict(Fraction)), "B": defaultdict(lambda: defaultdict(Fraction))}
    cache = {}
    for label in ("A", "B"):
        base = q if label == "A" else p
        for (j, s, state), mass in laws[label].items():
            if s not in base:
                raise AssertionError((label, j, s))
            cache.setdefault(state, h2_mark(module, n, hperm, state))
            weight = mass / base[s]
            for profile in cache[state]:
                out[label][s][profile] += weight
        for s, measure in out[label].items():
            total = sum(measure.values(), Fraction(0))
            if total != 3 * (alpha[1] + alpha[2]):
                raise AssertionError((label, s, total, alpha))
        for j in (1, 2):
            for s in base:
                joint = sum((mass for (jj, ss, _), mass in laws[label].items() if jj == j and ss == s), Fraction(0))
                if joint != alpha[j] * base[s]:
                    raise AssertionError(("split marginal", label, j, s, joint, alpha[j] * base[s]))
    return out, alpha, len(cache)


def canonical_edge_flux(graw, fraw, scale):
    g = {x: v / scale for x, v in graw.items()}
    f = {x: v / scale for x, v in fraw.items()}
    common = {x: min(g.get(x, 0), f.get(x, 0)) for x in set(g) | set(f)}
    a = {x: g.get(x, 0) - common[x] for x in common if g.get(x, 0) > common[x]}
    b = {x: f.get(x, 0) - common[x] for x in common if f.get(x, 0) > common[x]}
    rho = sum(a.values(), Fraction(0))
    assert rho == sum(b.values(), Fraction(0))
    edges = defaultdict(Fraction)
    if not rho:
        return edges
    for x, ax in a.items():
        for y, by in b.items():
            if x == y:
                raise AssertionError("residual supports overlap")
            lo, hi = (x, y) if x < y else (y, x)
            sign = 1 if (x, y) == (lo, hi) else -1
            edges[(lo, hi)] += sign * ax * by / rho
    return edges


def run(repo):
    module, hashes = load_primitives(repo)
    p, q = split_laws(module, K)
    laws = {}
    raw = {}
    for label in ("A", "B"):
        laws[label], raw[label] = tagged_source_law(module, K, label)
    marks, alpha, state_count = conditional_marks(module, K, laws, p, q)
    cells = quantile_cells(p, q)
    scale = 3 * (alpha[1] + alpha[2])
    net = defaultdict(Fraction)
    cell_edge_counts = {}
    for (s, t), pi in cells.items():
        edges = canonical_edge_flux(marks["A"][s], marks["B"][t], scale)
        cell_edge_counts[f"{s},{t}"] = len(edges)
        for edge, value in edges.items():
            add(net, edge, scale * pi * value)
    divergence = defaultdict(Fraction)
    for (lo, hi), value in net.items():
        divergence[lo] -= value
        divergence[hi] += value
    direct = defaultdict(Fraction)
    for t, mass in p.items():
        for profile, value in marks["B"][t].items():
            add(direct, profile, mass * value)
    for s, mass in q.items():
        for profile, value in marks["A"][s].items():
            add(direct, profile, -mass * value)
    if dict(divergence) != dict(direct):
        raise AssertionError("flux divergence mismatch")
    edge_norm = sum((abs(v) for v in net.values()), Fraction(0))
    div_norm = sum((abs(v) for p, v in direct.items() if any(p)), Fraction(0))
    max_edge, max_value = max(net.items(), key=lambda item: (abs(item[1]), item[0]))
    contributions = {}
    for (s, t), pi in cells.items():
        value = canonical_edge_flux(marks["A"][s], marks["B"][t], scale).get(max_edge, Fraction(0))
        if value:
            contributions[f"{s},{t}"] = scale * pi * value
    b2 = math.exp(-2) * float(module.tau(2))
    return {
        "status": "sole exact k=13 H_2 MPCF guard; finite only",
        "k": K,
        "n": 3 * K,
        "row": "H_2",
        "dependency_hashes": hashes,
        "raw_pairs": raw,
        "physical_state_count": state_count,
        "quantile_cells": {f"{s},{t}": str(v) for (s, t), v in cells.items()},
        "cell_edge_counts": cell_edge_counts,
        "net_edge_count": len(net),
        "net_edge_norm_exact": str(edge_norm),
        "response_divergence_tv_exact": str(div_norm),
        "normalized_mpcf_k_over_2b2": K * float(edge_norm) / (2 * b2),
        "normalized_cmpad_k_over_2b2": K * float(div_norm) / (2 * b2),
        "max_edge": {
            "source_profile": list(max_edge[0]),
            "target_profile": list(max_edge[1]),
            "net_value_exact": str(max_value),
            "combined_cell_contributions": {k: str(v) for k, v in contributions.items()},
        },
        "all_parts_combined_before_edge_absolute_value": True,
        "inference": {"MPCF_all_rank": False, "CMPAD": False, "downstream": False},
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("mpcf_k13_h2_results.json"))
    args = parser.parse_args()
    start = time.perf_counter()
    repo = Path(__file__).resolve().parents[4]
    payload = run(repo)
    payload.update({
        "elapsed_seconds": time.perf_counter() - start,
        "python": platform.python_version(),
        "seed": None,
        "repository_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip(),
        "command": "python3 -B mpcf_k13_h2_guard.py --output mpcf_k13_h2_results.json",
    })
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(args.output), "edge": payload["normalized_mpcf_k_over_2b2"], "div": payload["normalized_cmpad_k_over_2b2"], "elapsed": payload["elapsed_seconds"]}, sort_keys=True))


if __name__ == "__main__":
    main()

