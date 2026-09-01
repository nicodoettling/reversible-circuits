#!/usr/bin/env python3
"""Exact k=9 separation of self-owner and distinct-owner BODT rows.

This supplements bodt_k9_probe.py at the same single authorized rank.  It
imports only that mission-local clean-room implementation, rebuilds both
source laws, and never treats the finite row as an all-rank estimate.
"""

from __future__ import annotations

import importlib.util
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("m297_bodt_probe", HERE / "bodt_k9_probe.py")
assert SPEC and SPEC.loader
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def main() -> None:
    k = 9
    n = 3 * k
    threshold = (k - 1) // 2
    h = M.cyc(n, tuple(range(n)))
    laws = {label: M.source_law(k, label)[0] for label in ("A", "B")}
    states = {s for law in laws.values() for _, _, s in law}
    omega = {
        s: sum((p for (_, _, t), p in laws["B"].items() if t == s), Fraction(0))
        - sum((p for (_, _, t), p in laws["A"].items() if t == s), Fraction(0))
        for s in states
    }
    profiles = {s: M.owner_profile(n, h, s) for s in states}
    boundary = {s for s in states if min(profiles[s][1]) <= threshold}
    zero = tuple(Fraction(0) for _ in range(n))
    self_rows = defaultdict(lambda: zero)
    off_rows = defaultdict(lambda: zero)

    for s in boundary:
        generic, sizes = profiles[s]
        chis = tuple(tuple(int(x == i) for x in generic) for i in range(3))
        for i, d in enumerate(sizes):
            if d > threshold:
                continue
            for j, e in enumerate(sizes):
                if e > threshold:
                    continue
                delta = M.int_derivative(M.corr01(chis[i], chis[j]))
                term = M.frac_vec_scale(omega[s], delta)
                if i == j:
                    self_rows[d] = M.frac_vec_add(self_rows[d], term)
                else:
                    off_rows[(d, e)] = M.frac_vec_add(off_rows[(d, e)], term)

    lags = range(2, n - 2)
    self_payload = {}
    for d, row in sorted(self_rows.items()):
        norm = M.frac_l1(row, lags)
        bd = math.exp(-d) * float(M.tau(d))
        self_payload[str(d)] = {
            "lag_l1_exact": M.fstr(norm),
            "lag_l1_float": float(norm),
            "normalized_k_over_d2_b_d": k * float(norm) / (d * d * bd),
        }
    off_payload = {}
    for (d, e), row in sorted(off_rows.items()):
        norm = M.frac_l1(row, lags)
        if not norm:
            continue
        bd = math.exp(-d) * float(M.tau(d))
        be = math.exp(-e) * float(M.tau(e))
        off_payload[f"{d},{e}"] = {
            "lag_l1_exact": M.fstr(norm),
            "lag_l1_float": float(norm),
            "normalized_k_over_de_bdb_e": k * float(norm) / (d * e * bd * be),
        }

    print(json.dumps({
        "status": "exact k=9 calibration only",
        "scope": "self/off coefficient rows for the M297 SOCL candidate",
        "imports": "mission-local bodt_k9_probe.py only",
        "complete_boundary_omega_before_norm": True,
        "self_owner_rows": self_payload,
        "distinct_owner_rows": off_payload,
        "BODT_or_downstream_inference": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

