#!/usr/bin/env python3
"""Finite binary64 discovery scan for M90's weighted reset resolvent.

This imports the frozen M79 grouped Cayley implementation only to select
candidates for independent exact certification.  Values below one are not
proof; values above one are not promoted until reproduced exactly.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import importlib.util
import json
import platform
import time
from pathlib import Path


def load_m79():
    source = Path(__file__).resolve().parents[2] / (
        "cycle-17/mission-M79-m76-referee-resolvent/"
        "grouped_resolvent_attack.py"
    )
    spec = importlib.util.spec_from_file_location("m79_grouped", source)
    if spec is None or spec.loader is None:
        raise RuntimeError(source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M79 = load_m79()


class WeightedScanner:
    def __init__(self, s_max: int):
        self.core = M79.GroupedResolvent(s_max)
        self.contexts = 0

    @functools.lru_cache(maxsize=None)
    def g(
        self, s: int, K: int | None, R: int | None, B: int
    ) -> float:
        """Return ``q_x [(I-D)^-1 J_can W](x)``."""
        if s <= 1:
            return 0.0
        self.contexts += 1
        answer = 0.0
        for child, inverse_q_weight in self.core.jhat(
            s, K, R, B
        ):
            q_child = self.core.q(child[0], child[3])
            # M79 stores energy/q_child.  Undo that transform and apply
            # W(child)=1-q_child (every reset target is right-heavy).
            answer += inverse_q_weight * q_child * (1.0 - q_child)
        for k, t, mass in self.core.groups(s):
            if t <= B or t - 1 < 2:
                continue
            if K is None:
                answer += mass * self.g(t - 1, None, None, B)
            else:
                assert R is not None
                for j in range(1, k + 1):
                    coefficient = self.core.nu(K, R, k, j)
                    if coefficient:
                        answer += mass * coefficient * self.g(
                            t - 1, K + k, R + j, B
                        )
        return answer

    def row(self, s: int, K: int | None, B: int) -> dict[str, object]:
        q = self.core.q(s, B)
        R = None if K is None else K - 1
        g = self.g(s, K, R, B)
        ratio = g / (q * (1.0 - q))
        return {
            "s": s,
            "K": "infinity" if K is None else K,
            "R": "infinity-1" if R is None else R,
            "B": B,
            "q": q,
            "transformed_value": g,
            "ratio": ratio,
        }


def scan(s_values: list[int], K_values: list[int], include_infinite: bool) -> dict:
    scanner = WeightedScanner(max(s_values))
    rows = []
    overall = None
    contexts: list[int | None] = list(K_values)
    if include_infinite:
        contexts.append(None)
    for s in s_values:
        worst = None
        for K in contexts:
            for B in range(1, s + 1):
                row = scanner.row(s, K, B)
                if worst is None or row["ratio"] > worst["ratio"]:
                    worst = row
                if overall is None or row["ratio"] > overall["ratio"]:
                    overall = row
        rows.append(worst)
        print(json.dumps(worst, sort_keys=True), flush=True)
    return {
        "rank_worst_rows": rows,
        "overall_worst": overall,
        "memoized_weighted_contexts": scanner.contexts,
        "core_diagnostics": {
            "max_group_mass_error": scanner.core.max_group_mass_error,
            "max_contextual_mean_error": scanner.core.max_mean_error,
            "max_negative_roundoff": scanner.core.max_negative_roundoff,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-values", type=int, nargs="+", required=True)
    parser.add_argument("--K-values", type=int, nargs="*", default=[1, 2, 4, 16, 256])
    parser.add_argument("--no-infinite", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    result = scan(args.s_values, args.K_values, not args.no_infinite)
    payload = {
        "claim_tested": "right-heavy K_reset W <= W",
        "status_rule": (
            "binary64 is discovery only; any candidate violation requires "
            "independent exact certification; survival proves no theorem"
        ),
        "normalization": (
            "g=q*(I-D)^-1*J_can*W; Dhat=rho*nu over every j>=1; "
            "reset term=(theta^2/Q)*(1-q_child)"
        ),
        "arithmetic": "IEEE-754 binary64 grouped Cayley coefficients",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "parameters": {
            "s_values": args.s_values,
            "K_values": args.K_values,
            "include_infinite": not args.no_infinite,
        },
        "elapsed_seconds": time.time() - started,
        "result": result,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "elapsed_seconds": payload["elapsed_seconds"],
        "overall_worst": result["overall_worst"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
