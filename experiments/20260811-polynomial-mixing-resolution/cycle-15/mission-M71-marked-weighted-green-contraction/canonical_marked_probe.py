#!/usr/bin/env python3
"""Finite marked recurrence using M41's first-boundary hub flow.

Unlike the electrical optimizer, every quotient residual created here has
right-heavy mark R=K-1.  The canonical basin of an edge

    (A,c2,...,ck) -> (A+c2,c3,...,ck)

is all refinements of A with the displayed suffix fixed.  Sending each
mean-zero charge to the one-part hub gives current equal to the total charge
of that basin.

This is a finite calibration.  It does not itself prove a universal
congestion or actual-edge collision bound.
"""

from __future__ import annotations

import argparse
import functools
import json
import platform
import subprocess
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import scipy

import weighted_green_probe as base
from marked_resolvent_probe import context_grid, negative_hypergeometric


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


class CanonicalResolvent:
    def __init__(self, s_max: int):
        self.rank_data = {}
        self.max_deep_mass_error = 0.0
        for s in range(2, s_max + 1):
            (
                comps,
                rho,
                _,
                keys,
                groups,
                merge_edges,
            ) = base.build_rank(s)
            canonical_edges = []
            for edge in merge_edges:
                (
                    i,
                    j,
                    capacity,
                    child_rank,
                    left,
                    right,
                    child_K,
                    child_R,
                ) = edge
                refined = comps[i]
                if child_R != child_K - 1:
                    continue
                suffix = refined[1:]
                basin = [
                    index
                    for index, comp in enumerate(comps)
                    if len(comp) >= len(suffix) + 1
                    and comp[-len(suffix):] == suffix
                    and sum(comp[:-len(suffix)]) == left
                ]
                canonical_edges.append((edge, basin))
            masses = np.array(
                [sum(rho[index] for index in groups[key]) for key in keys]
            )
            self.rank_data[s] = {
                "comps": comps,
                "rho": rho,
                "keys": keys,
                "groups": groups,
                "masses": masses,
                "canonical_edges": canonical_edges,
            }

    def transitions(self, s: int, K: int, R: int, B: int):
        data = self.rank_data[s]
        rho = data["rho"]
        keys = data["keys"]
        masses = data["masses"]
        group_values = base.contextual_values(keys, K, R, B)
        mean = float(np.dot(masses, group_values))
        value_by_state = np.empty(len(rho))
        for key_index, key in enumerate(keys):
            value_by_state[data["groups"][key]] = group_values[key_index]
        charge = rho * (value_by_state - mean)

        children = defaultdict(float)
        quotient_energy = 0.0
        for edge, basin in data["canonical_edges"]:
            (
                _,
                _,
                capacity,
                child_rank,
                _,
                right,
                child_K,
                child_R,
            ) = edge
            current = float(sum(charge[index] for index in basin))
            energy = current * current / capacity
            quotient_energy += energy
            if child_rank >= 2:
                children[
                    (child_rank, child_K, child_R, right)
                ] += energy / mean

        deep_weight = 0.0
        terminal = 0.0
        for index, (k, last) in enumerate(keys):
            mass = masses[index]
            if last == B:
                terminal += mass * group_values[index]
            if last <= B:
                continue
            child_rank = last - 1
            child_mean = base.w_ratio(last - B, B)
            for mark_j in range(1, k + 1):
                nu = negative_hypergeometric(K, R, k, mark_j)
                weight = mass * child_mean * nu / mean
                deep_weight += weight
                if child_rank >= 2:
                    children[
                        (child_rank, K + k, R + mark_j, B)
                    ] += weight
        delta = (mean - terminal) / mean
        self.max_deep_mass_error = max(
            self.max_deep_mass_error, abs(deep_weight - delta)
        )
        return quotient_energy / mean, delta, dict(children)

    @functools.lru_cache(maxsize=None)
    def value(self, s: int, K: int, R: int, B: int) -> float:
        if s <= 1:
            return 0.0
        a, _, children = self.transitions(s, K, R, B)
        return a + sum(
            weight * self.value(*child)
            for child, weight in children.items()
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=10)
    parser.add_argument("--K-max", type=int, default=16)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 2 <= args.s_max <= 14:
        raise SystemExit("bounded range is 2 <= s-max <= 14")
    started = time.time()
    solver = CanonicalResolvent(args.s_max)
    records = []
    for s in range(2, args.s_max + 1):
        worst = None
        count = 0
        for K, R, B in context_grid(s, args.K_max):
            value = solver.value(s, K, R, B)
            a, delta, children = solver.transitions(s, K, R, B)
            row = {
                "s": s,
                "K": K,
                "R": R,
                "B": B,
                "resolvent_value": value,
                "base_canonical_energy": a,
                "deep_fraction": delta,
                "total_child_weight": sum(children.values()),
                "child_context_count": len(children),
            }
            if worst is None or value > worst["resolvent_value"]:
                worst = row
            count += 1
        record = {
            "s": s,
            "scanned_context_count": count,
            "worst": worst,
        }
        records.append(record)
        print(json.dumps(record, sort_keys=True), flush=True)
    payload = {
        "claim_tested": (
            "The exact marked recurrence built with first-boundary canonical "
            "hub currents has polynomial resolvent and only right-heavy "
            "quotient residual marks."
        ),
        "finite_scope_warning": (
            "Finite values prove no universal bound or actual-edge source "
            "recovery theorem."
        ),
        "normalization": (
            "G_s=R_s/alpha_s; canonical current is total rho(H-EH) charge "
            "of the M41 first-merge basin; energy=current^2/[rho(refined)k]."
        ),
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "seed": None,
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-15/mission-M71-marked-weighted-green-contraction/"
            f"canonical_marked_probe.py --s-max {args.s_max} "
            f"--K-max {args.K_max} --output {args.output}"
        ),
        "parameters": {
            "s_max": args.s_max,
            "K_max": args.K_max,
            "output": str(args.output),
        },
        "deep_mass_identity_max_abs_error": solver.max_deep_mass_error,
        "elapsed_seconds": time.time() - started,
        "records": records,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
