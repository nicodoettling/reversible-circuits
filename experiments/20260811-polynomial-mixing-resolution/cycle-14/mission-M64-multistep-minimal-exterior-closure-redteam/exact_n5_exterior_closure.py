#!/usr/bin/env python3
"""Exact N=5 breadth-first exterior closure for the M63 balanced path-core cut.

The support graph is the literal positive-transition graph of K.  States are
encoded as base-10 integers to keep the exterior layers compact.  The output
records exact rational full-K boundary flow for each completed radius.
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
    "m59_for_m64",
    HERE.parent.parent / "cycle-13" / "mission-M59-fixed-join-tree-internal-redteam" / "fixed_tree_dp_bucket_audit.py",
)
M60 = load(
    "m60_for_m64",
    HERE.parent.parent / "cycle-13" / "mission-M60-fixed-tree-leaf-cell-expansion" / "leaf_cell_audit.py",
)


def fraction_text(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def encode(word, powers):
    return sum(x * powers[j] for j, x in enumerate(word))


def decode(code: int, length: int, alphabet: int):
    out = []
    for _ in range(length):
        code, digit = divmod(code, alphabet)
        out.append(digit)
    return tuple(out)


def connected_masks(n, all_edges):
    result = [False] * (1 << len(all_edges))
    for mask in range(1 << len(all_edges)):
        dsu = M59.DSU(n)
        for j, (a, b) in enumerate(all_edges):
            if mask & (1 << j):
                dsu.union(a, b)
        result[mask] = len({dsu.find(v) for v in range(n)}) == 1
    return result


def block_data(n, all_edges, alphabet):
    answer = {}
    for r in (3, 4, 5):
        grouped = defaultdict(list)
        for block in itertools.product(range(alphabet), repeat=r):
            product = M59.evaluate(n, all_edges, block)
            local_code = sum(x * alphabet**j for j, x in enumerate(block))
            mask = 0
            counts = [0] * alphabet
            for x in block:
                mask |= 1 << x
                counts[x] += 1
            grouped[product].append((local_code, mask, tuple(counts)))
        answer[r] = dict(grouped)
    return answer


def weighted(counter):
    """Counter keys are (r, fiber_size); values are directed outcome counts."""
    total = Fraction(0)
    by_r = {r: Fraction(0) for r in (3, 4, 5)}
    for (r, fiber_size), count in counter.items():
        value = Fraction(count, 6 * (8 - r + 1) * fiber_size)
        total += value
        by_r[r] += value
    return total, by_r


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-radius", type=int, default=1)
    parser.add_argument("--construct-only", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()

    n = 5
    m = 8
    alphabet = math.comb(n, 2)
    powers = tuple(alphabet**j for j in range(m))
    all_edges = M59.edges(n)
    connected = connected_masks(n, all_edges)
    fibers = block_data(n, all_edges, alphabet)

    tree = M59.tree_shapes()["path"]
    words, _cache = M59.enumerate_fixed_tree(n, tree, all_edges)
    leaves = M59.tree_leaves(n, tree)
    core = {
        word: M60.delete_original_labels(word, n, tuple(sorted(leaves, reverse=True)))
        for word in words
    }
    core_counts = Counter(core.values())
    keys = sorted(core_counts)
    selected = None
    for subset in itertools.combinations(keys, 4):
        if sum(core_counts[key] for key in subset) == len(words) // 2:
            selected = frozenset(subset)
            break
    if selected is None:
        raise AssertionError(core_counts)
    A = {encode(word, powers) for word in words if core[word] in selected}
    if len(A) != 3904:
        raise AssertionError(len(A))

    def process_sources(sources, known_exterior):
        new_exterior = set()
        to_fminus_a = Counter()
        to_new_exterior = Counter()
        for source_code in sources:
            word = decode(source_code, m, alphabet)
            total_counts = [0] * alphabet
            for x in word:
                total_counts[x] += 1
            for r in (3, 4, 5):
                windows = m - r + 1
                for position in range(windows):
                    old = word[position : position + r]
                    product = M59.evaluate(n, all_edges, old)
                    options = fibers[r][product]
                    fiber_size = len(options)
                    outside_code = source_code - sum(old[j] * powers[position + j] for j in range(r))
                    outside_counts = total_counts.copy()
                    for x in old:
                        outside_counts[x] -= 1
                    outside_mask = 0
                    for edge_idx, count in enumerate(outside_counts):
                        if count:
                            outside_mask |= 1 << edge_idx
                    for local_code, block_mask, _block_counts in options:
                        target_code = outside_code + local_code * powers[position]
                        if connected[outside_mask | block_mask]:
                            if target_code not in A:
                                to_fminus_a[(r, fiber_size)] += 1
                        elif target_code not in known_exterior:
                            new_exterior.add(target_code)
                            to_new_exterior[(r, fiber_size)] += 1
        return new_exterior, to_fminus_a, to_new_exterior

    # E_0 is every exterior neighbor of A.  Its A->E_0 flow is internal to C_0.
    E0, flow_A_to_F, _flow_A_to_E0 = process_sources(A, frozenset())
    exterior_seen = set(E0)
    layers = [E0]
    cumulative_f_flow = Counter(flow_A_to_F)
    radii = []

    omega = M59.identity_word_count(n, all_edges, m)
    full_minimal = math.factorial(2 * n - 2) * n ** (n - 3)
    exterior_total = omega - full_minimal
    if len(E0) > exterior_total:
        raise AssertionError((len(E0), exterior_total))

    if args.construct_only:
        a_to_f, a_to_f_by_r = weighted(flow_A_to_F)
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
            "convention": "(pq)(x)=p(q(x)); words are base-10 little-endian encoded",
            "kernel": "literal lazy K; each outcome weight 1/[6(m-r+1)|F_r(g)|]",
            "claim_tested": "The N=5 maximal one-step exterior halo E_0 has the exact reported cardinality; this can falsify a proposed small-halo or immediate-saturation claim.",
            "scope_warning": "The construction-only result does not compute flow from E_0 or prove asymptotic expansion.",
            "N": n,
            "m": m,
            "omega": omega,
            "full_minimal_size": full_minimal,
            "exterior_total_size": exterior_total,
            "A_size": len(A),
            "E0_size": len(E0),
            "C0_size": len(A) + len(E0),
            "C0_stationary_mass": fraction_text(Fraction(len(A) + len(E0), omega)),
            "A_to_FminusA_unnormalized_sum": fraction_text(a_to_f),
            "A_to_FminusA_by_r": {
                str(r): fraction_text(a_to_f_by_r[r]) for r in (3, 4, 5)
            },
            "elapsed_seconds_before_write": time.perf_counter() - started,
        }
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        print(json.dumps({
            "A": len(A),
            "E0": len(E0),
            "C0": len(A) + len(E0),
            "exterior_total": exterior_total,
            "elapsed": payload["elapsed_seconds_before_write"],
        }, sort_keys=True), flush=True)
        return

    for radius in range(args.max_radius + 1):
        layer = layers[radius]
        next_layer, flow_layer_to_F, flow_layer_to_next = process_sources(layer, exterior_seen)
        cumulative_f_flow.update(flow_layer_to_F)
        f_value, f_by_r = weighted(cumulative_f_flow)
        shell_value, shell_by_r = weighted(flow_layer_to_next)
        boundary = f_value + shell_value
        c_size = len(A) + len(exterior_seen)
        complement_size = omega - c_size
        oriented_size = min(c_size, complement_size)
        conductance = boundary / oriented_size
        radii.append(
            {
                "radius": radius,
                "layer_size": len(layer),
                "next_layer_size": len(next_layer),
                "exterior_cumulative_size": len(exterior_seen),
                "cut_size": c_size,
                "complement_size": complement_size,
                "smaller_side": "cut" if c_size <= complement_size else "complement",
                "stationary_mass": fraction_text(Fraction(c_size, omega)),
                "boundary_unnormalized_sum": fraction_text(boundary),
                "boundary_to_FminusA_sum": fraction_text(f_value),
                "boundary_to_next_exterior_sum": fraction_text(shell_value),
                "boundary_by_r": {
                    str(r): fraction_text(f_by_r[r] + shell_by_r[r]) for r in (3, 4, 5)
                },
                "conductance": fraction_text(conductance),
                "conductance_float": float(conductance),
            }
        )
        print(json.dumps(radii[-1], sort_keys=True), flush=True)
        if not next_layer:
            break
        exterior_seen.update(next_layer)
        layers.append(next_layer)

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
        "convention": "(pq)(x)=p(q(x)); words are base-10 little-endian encoded",
        "kernel": "literal lazy K; each outcome weight 1/[6(m-r+1)|F_r(g)|]",
        "claim_tested": "For the N=5 M63 balanced path-core cut, the literal exterior BFS layer identity and complete H3/H4/H5 boundary decomposition hold; a zero/small shell would falsify candidate pointwise exterior expansion lemmas.",
        "scope_warning": "Finite N=5 closure data can refute universal shell claims but cannot prove asymptotic expansion or mixing.",
        "N": n,
        "m": m,
        "omega": omega,
        "full_minimal_size": full_minimal,
        "exterior_total_size": exterior_total,
        "A_size": len(A),
        "core_distribution": [
            {"core_word": list(key), "count": core_counts[key], "selected": key in selected}
            for key in keys
        ],
        "radii": radii,
        "elapsed_seconds_before_write": time.perf_counter() - started,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
