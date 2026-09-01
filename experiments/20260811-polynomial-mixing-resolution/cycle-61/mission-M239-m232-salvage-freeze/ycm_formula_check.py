#!/usr/bin/env python3
"""Clean-room odd-k<=21 falsification checks for the M239 YCM formulas.

This evaluates the exact closed formulas numerically.  It is not used to
prove any universal inequality; the proof is ycm_sufficiency_theorem.md.
"""

import json
import math


def borel(n: int) -> float:
    return math.exp(-n) * n ** (n - 1) / math.factorial(n)


def data_for(k: int) -> dict:
    D, R, j, L = 2 * k - 1, 2 * k - 3, (k - 1) // 2, (3 * k - 1) // 2
    b = {n: borel(n) for n in range(1, D + 1)}

    def q(s: int) -> float:
        return k * b[s] * b[k - s] / ((k - 1) * b[k])

    def K(r: int, d: int) -> float:
        assert 1 <= d < r
        return b[d] * b[r - d] / (R * b[r])

    def h(r: int) -> float:
        return (r - 1) * (r - 2) / (r * R)

    def G(x: int) -> float:
        assert 1 <= x <= L - 1
        survivor = q(x) * h(D - x) if x <= j else 0.0
        short = sum(q(s) * (s - x - 1) * K(s, x)
                    for s in range(x + 1, j + 1))
        long = sum(q(s) * (D - s - x - 1) * K(D - s, x)
                   for s in range(1, j + 1))
        return survivor + short + long

    def B(y: int) -> float:
        if y < k:
            return (D - 2 * y) * G(y) / D + (y - 1) * G(y - 1) / D
        if y == k:
            return (k - 1) * G(k - 1) / D
        z = y - k
        return (k - z) * G(k + z - 1) / D + z * G(z) / D

    def A(y: int) -> float:
        if y >= k:
            return 0.0
        m = k - y
        return (2 * b[y] * b[m] / (R * b[k])
                * (m + (m - 1) * (m - 2) / (k - 1)))

    sg = []
    gg1 = []
    gg2 = []
    for x in range(1, L):
        gx = G(x)
        if x <= k / 4:
            sg.append(abs(gx - 2 * b[x]) * k / ((x + 1) * b[x]))
        if x <= j:
            gg1.append(gx / b[x])
        if x >= j:
            gg2.append(gx * k * math.sqrt(D - x))

    coeff = []
    prefix = 0.0
    ycm = []
    envelope_ratios = []
    for y in range(2, L + 1):
        c = B(y) - A(y)
        coeff.append(c)
        prefix += c
        ycm.append(abs(prefix) * k / math.sqrt(y))
        if y <= j:
            envelope_ratios.append(abs(c) * k * math.sqrt(y) / 3000)
        elif y < k:
            envelope_ratios.append(abs(c) * k * math.sqrt(k - y) / 176)
        elif y == k:
            envelope_ratios.append(abs(c) * k ** 1.5 / 70)
        else:
            envelope_ratios.append(abs(c) * k * math.sqrt(y - k) / 242)

    return {
        "k": k,
        "q_sum_error": abs(sum(q(s) for s in range(1, j + 1)) - 1.0),
        "max_sg_constant": max(sg, default=0.0),
        "max_gg1_constant": max(gg1, default=0.0),
        "max_gg2_constant": max(gg2, default=0.0),
        "max_envelope_fraction": max(envelope_ratios),
        "max_ycm_scaled_prefix": max(ycm),
        "formula_domain": {"G_min": 1, "G_max": L - 1, "ell_max": L},
    }


def main() -> None:
    rows = [data_for(k) for k in range(3, 22, 2)]
    checks = {
        "q_normalization": all(r["q_sum_error"] < 1e-12 for r in rows),
        "SG_128": all(r["max_sg_constant"] <= 128 for r in rows),
        "GG1_172": all(r["max_gg1_constant"] <= 172 for r in rows),
        "GG2_70": all(r["max_gg2_constant"] <= 70 for r in rows),
        "coefficient_envelopes": all(r["max_envelope_fraction"] <= 1 for r in rows),
        "YCM_7000": all(r["max_ycm_scaled_prefix"] <= 7000 for r in rows),
    }
    print(json.dumps({
        "status": "pass" if all(checks.values()) else "falsified",
        "role": "falsification only",
        "odd_k": list(range(3, 22, 2)),
        "checks": checks,
        "rows": rows,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
