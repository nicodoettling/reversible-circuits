#!/usr/bin/env python3
"""Exact coefficient-only guard for M300's exterior Hahn--Abel identity."""

from __future__ import annotations

import importlib.util
import json
import platform
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def main() -> None:
    if len(sys.argv) != 3 or sys.argv[1] != "--output":
        raise SystemExit("usage: exterior_abel_k7.py --output PATH")
    output = Path(sys.argv[2])

    module_path = Path(__file__).with_name("mclp_k7.py")
    spec = importlib.util.spec_from_file_location("m300_mclp", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load mclp_k7.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    tau = module.tau

    k = 7
    d = 2 * k - 1

    def v(size: int, cut: int) -> Fraction:
        return tau(cut) * tau(size - cut) / ((size - 1) * tau(size))

    cumulative = Fraction(0)
    rows = []
    for cut in range(1, k):
        q = Fraction(1, 2) * v(k, cut) - v(d, cut)
        x = 2 * cut * v(d, cut)
        y = (d - 2 * cut) * q + Fraction(1, 2) * v(k, cut)
        r = x - y
        closed_r = d * v(d, cut) - (k - cut) * v(k, cut)
        assert r == closed_r
        assert q > 0 and x > 0 and y > 0
        cumulative += r
        rows.append(
            {
                "c": cut,
                "cross_count": 2 * cut,
                "internal_count": d - 2 * cut,
                "q": qstr(q),
                "x": qstr(x),
                "y": qstr(y),
                "r": qstr(r),
                "R": qstr(cumulative),
            }
        )

    assert cumulative == 0
    assert any(Fraction(row["R"]) < 0 for row in rows[:-1])
    assert any(Fraction(row["R"]) > 0 for row in rows[:-1])

    payload = {
        "status": "exact coefficient-only guard; not a response sign test",
        "scope": "k=7 only, the same sole rank as mclp_k7.py",
        "convention": "v_d(c)=tau(c)tau(d-c)/((d-1)tau(d))",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": "python3 exterior_abel_k7.py --output exterior_abel_k7.json",
        "imports_only_same_mission_tau_definition": True,
        "k": k,
        "D": d,
        "positive_cross_chords": k * (k - 1),
        "negative_internal_and_seam_chords": k * (k - 1),
        "R_final": qstr(cumulative),
        "R_has_both_signs_before_endpoint": True,
        "rows": rows,
        "downstream_inference": False,
    }
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"R_final": qstr(cumulative), "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
