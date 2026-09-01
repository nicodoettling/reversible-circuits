#!/usr/bin/env python3
"""Exact N=5 exterior BFS and K boundary via outside-window signatures.

For fixed (r,i), two identity words are in one heat-bath fiber exactly when
their factors outside positions i,...,i+r-1 agree.  This gives an exact clique
decomposition and avoids iterating over every conditional replacement.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
import platform
import subprocess
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M59 = load(
    "m59_for_m64_signature",
    HERE.parent.parent / "cycle-13" / "mission-M59-fixed-join-tree-internal-redteam" / "fixed_tree_dp_bucket_audit.py",
)
M60 = load(
    "m60_for_m64_signature",
    HERE.parent.parent / "cycle-13" / "mission-M60-fixed-tree-leaf-cell-expansion" / "leaf_cell_audit.py",
)


N = 5
M = math.comb(N, 2)
LENGTH = 8
WINDOWS = tuple((r, i) for r in (3, 4, 5) for i in range(LENGTH - r + 1))
POWERS = tuple(M**j for j in range(LENGTH + 1))


def encode(word):
    return sum(x * POWERS[j] for j, x in enumerate(word))


def outside_key(code: int, r: int, i: int) -> int:
    low = code % POWERS[i]
    high = code // POWERS[i + r]
    return low + high * POWERS[i]


def inverse(p):
    answer = [0] * len(p)
    for x, y in enumerate(p):
        answer[y] = x
    return tuple(answer)


def connected_masks(all_edges):
    answer = [False] * (1 << len(all_edges))
    for mask in range(1 << len(all_edges)):
        dsu = M59.DSU(N)
        for j, (a, b) in enumerate(all_edges):
            if mask & (1 << j):
                dsu.union(a, b)
        answer[mask] = len({dsu.find(v) for v in range(N)}) == 1
    return answer


def identity_words(all_edges):
    """Meet-in-the-middle enumeration of all length-eight identity words."""
    groups = defaultdict(list)
    for block in itertools.product(range(M), repeat=4):
        product = M59.evaluate(N, all_edges, block)
        code = sum(x * M**j for j, x in enumerate(block))
        mask = 0
        for x in block:
            mask |= 1 << x
        groups[product].append((code, mask))
    connected = connected_masks(all_edges)
    all_codes = []
    exterior = []
    for product, lefts in groups.items():
        rights = groups[inverse(product)]
        for left_code, left_mask in lefts:
            for right_code, right_mask in rights:
                code = left_code + right_code * M**4
                all_codes.append(code)
                if not connected[left_mask | right_mask]:
                    exterior.append(code)
    return all_codes, exterior


def balanced_core_A(all_edges):
    tree = M59.tree_shapes()["path"]
    words, _cache = M59.enumerate_fixed_tree(N, tree, all_edges)
    leaves = M59.tree_leaves(N, tree)
    core = {
        word: M60.delete_original_labels(word, N, tuple(sorted(leaves, reverse=True)))
        for word in words
    }
    distribution = Counter(core.values())
    keys = sorted(distribution)
    selected = None
    for subset in itertools.combinations(keys, 4):
        if sum(distribution[key] for key in subset) == len(words) // 2:
            selected = frozenset(subset)
            break
    if selected is None:
        raise AssertionError(distribution)
    A = {encode(word) for word in words if core[word] in selected}
    if len(A) != 3904:
        raise AssertionError(len(A))
    return A, distribution, selected


def signature_sets(codes):
    answer = {(r, i): set() for r, i in WINDOWS}
    for code in codes:
        for r, i in WINDOWS:
            answer[(r, i)].add(outside_key(code, r, i))
    return answer


def extend_signatures(signatures, codes):
    for code in codes:
        for r, i in WINDOWS:
            signatures[(r, i)].add(outside_key(code, r, i))


def touches(signatures, code):
    return any(outside_key(code, r, i) in signatures[(r, i)] for r, i in WINDOWS)


def group_counts(codes):
    answer = {(r, i): Counter() for r, i in WINDOWS}
    for code in codes:
        for r, i in WINDOWS:
            answer[(r, i)][outside_key(code, r, i)] += 1
    return answer


def add_group_counts(target, codes):
    for code in codes:
        for r, i in WINDOWS:
            target[(r, i)][outside_key(code, r, i)] += 1


def boundary_flow(total_counts, cut_counts):
    by_r = {r: Fraction(0) for r in (3, 4, 5)}
    for r, i in WINDOWS:
        numerator_by_size = Counter()
        totals = total_counts[(r, i)]
        for key, inside in cut_counts[(r, i)].items():
            total = totals[key]
            numerator_by_size[total] += inside * (total - inside)
        for fiber_size, numerator in numerator_by_size.items():
            by_r[r] += Fraction(numerator, 6 * (LENGTH - r + 1) * fiber_size)
    return by_r


def between_flow(total_counts, source_counts, target_counts):
    by_r = {r: Fraction(0) for r in (3, 4, 5)}
    for r, i in WINDOWS:
        numerator_by_size = Counter()
        totals = total_counts[(r, i)]
        source = source_counts[(r, i)]
        target = target_counts[(r, i)]
        if len(source) <= len(target):
            iterator = source.items()
            other = target
        else:
            iterator = target.items()
            other = source
        for key, first in iterator:
            second = other.get(key, 0)
            if second:
                fiber_size = totals[key]
                numerator_by_size[fiber_size] += first * second
        for fiber_size, numerator in numerator_by_size.items():
            by_r[r] += Fraction(numerator, 6 * (LENGTH - r + 1) * fiber_size)
    return by_r


def fraction_text(x):
    return f"{x.numerator}/{x.denominator}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-radius", type=int, default=20)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()

    all_edges = M59.edges(N)
    A, core_distribution, selected = balanced_core_A(all_edges)
    all_codes, exterior_codes = identity_words(all_edges)
    if len(all_codes) != 1770940 or len(exterior_codes) != 762940:
        raise AssertionError((len(all_codes), len(exterior_codes)))

    signatures = signature_sets(A)
    remaining = exterior_codes
    layers = []
    for radius in range(args.max_radius + 2):
        layer = [code for code in remaining if touches(signatures, code)]
        if not layer:
            break
        layer_set = set(layer)
        remaining = [code for code in remaining if code not in layer_set]
        layers.append(layer)
        extend_signatures(signatures, layer)
        if not remaining:
            break
    if not layers:
        raise AssertionError("E0 empty")

    total_counts = group_counts(all_codes)
    cut_counts = group_counts(A)
    layer_counts = [group_counts(layer) for layer in layers]
    radii = []
    cumulative_exterior = 0
    omega = len(all_codes)
    for radius in range(min(args.max_radius + 1, len(layers))):
        layer = layers[radius]
        add_group_counts(cut_counts, layer)
        cumulative_exterior += len(layer)
        full_by_r = boundary_flow(total_counts, cut_counts)
        if radius + 1 < len(layers):
            shell_by_r = between_flow(
                total_counts, layer_counts[radius], layer_counts[radius + 1]
            )
            next_size = len(layers[radius + 1])
        else:
            shell_by_r = {r: Fraction(0) for r in (3, 4, 5)}
            next_size = 0
        f_by_r = {r: full_by_r[r] - shell_by_r[r] for r in (3, 4, 5)}
        if any(value < 0 for value in f_by_r.values()):
            raise AssertionError((radius, full_by_r, shell_by_r))
        full = sum(full_by_r.values(), Fraction(0))
        shell = sum(shell_by_r.values(), Fraction(0))
        to_f = sum(f_by_r.values(), Fraction(0))
        cut_size = len(A) + cumulative_exterior
        complement_size = omega - cut_size
        smaller = min(cut_size, complement_size)
        conductance = full / smaller
        radii.append({
            "radius": radius,
            "layer_size": len(layer),
            "next_layer_size": next_size,
            "exterior_cumulative_size": cumulative_exterior,
            "exterior_remaining_size": len(exterior_codes) - cumulative_exterior,
            "cut_size": cut_size,
            "complement_size": complement_size,
            "smaller_side": "cut" if cut_size <= complement_size else "complement",
            "stationary_mass": fraction_text(Fraction(cut_size, omega)),
            "boundary_unnormalized_sum": fraction_text(full),
            "boundary_to_FminusA_sum": fraction_text(to_f),
            "boundary_to_next_exterior_sum": fraction_text(shell),
            "boundary_by_r": {str(r): fraction_text(full_by_r[r]) for r in (3, 4, 5)},
            "to_FminusA_by_r": {str(r): fraction_text(f_by_r[r]) for r in (3, 4, 5)},
            "to_next_exterior_by_r": {str(r): fraction_text(shell_by_r[r]) for r in (3, 4, 5)},
            "conductance": fraction_text(conductance),
            "conductance_float": float(conductance),
        })
        print(json.dumps(radii[-1], sort_keys=True), flush=True)

    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "argv": sys.argv,
        "commit": commit,
        "python": platform.python_version(),
        "seed": None,
        "nonstandard_dependencies": {},
        "convention": "(pq)(x)=p(q(x)); base-10 little-endian word codes",
        "kernel": "literal lazy K; clique pair weight 1/[6(m-r+1)|fiber|]",
        "claim_tested": "The exact N=5 exterior closure layers and two-term full H3/H4/H5 boundary identity; this can falsify pointwise expansion, immediate saturation, or omitted-flow claims.",
        "scope_warning": "Finite N=5 closure and conductance cannot prove an asymptotic bound.",
        "method": "Meet-in-the-middle identity enumeration plus exact outside-window conditional-fiber cliques.",
        "N": N,
        "m": LENGTH,
        "omega": omega,
        "full_minimal_size": omega - len(exterior_codes),
        "exterior_total_size": len(exterior_codes),
        "A_size": len(A),
        "core_distribution": [
            {"core_word": list(key), "count": core_distribution[key], "selected": key in selected}
            for key in sorted(core_distribution)
        ],
        "all_layer_sizes_computed": [len(layer) for layer in layers],
        "unreached_exterior_after_computed_layers": len(remaining),
        "radii": radii,
        "elapsed_seconds_before_write": time.perf_counter() - started,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
