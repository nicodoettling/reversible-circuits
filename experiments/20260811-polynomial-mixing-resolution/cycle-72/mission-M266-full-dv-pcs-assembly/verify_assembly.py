#!/usr/bin/env python3
"""Deterministic arithmetic/domain falsifier for the M266 assembly.

This checker verifies only substitutions and exceptional-case bookkeeping.
The universal inequalities are supplied by the frozen proof artifacts.
"""

import json
from fractions import Fraction


Y_DV = 18_400
TAV = 500
FULL_DV = 18_900
DE = 7_164
SHARED_ENDPOINT = 15
ABEL_ENDPOINT = 6


def main() -> None:
    assert Y_DV + TAV == FULL_DV
    assert DE + SHARED_ENDPOINT + ABEL_ENDPOINT == 7_185
    assert 18 * FULL_DV == 340_200
    assert 18 * 7_185 == 129_330

    checked_ranks = 0
    checked_cutoffs = 0
    k3_channel_masses = None
    for k in range(3, 2002, 2):
        n = 3 * k
        m = (n - 1) // 2
        exterior = 2 * k - 1

        assert k % 2 == 1 and n % 2 == 1
        assert m == n // 2 == (3 * k - 1) // 2
        assert list(range(1, k - 1))[0] == 1
        assert list(range(1, k - 1))[-1] == k - 2
        assert len(range(1, k - 1)) == k - 2
        assert Fraction(k, n - 3) >= Fraction(1, 3)
        assert Fraction(k, n - 3) <= Fraction(1, 2)
        assert Fraction(n - 3, k) <= 3

        den = (3 * k - 3) * (3 * k - 4)
        channel_masses = (
            Fraction((k - 1) * (k - 2), den),
            Fraction(2 * (k - 1) * (2 * k - 2), den),
            Fraction((2 * k - 2) * (2 * k - 3), den),
        )
        assert all(mass >= 0 for mass in channel_masses)
        assert sum(channel_masses) == 1

        for ell in range(2, m + 1):
            assert 2 <= ell <= (3 * k - 1) // 2
            checked_cutoffs += 1
        checked_ranks += 1

        if k == 3:
            assert (n, m, exterior) == (9, 4, 5)
            assert list(range(1, k - 1)) == [1]
            assert list(range(2, m + 1)) == [2, 3, 4]
            assert m > exterior - 2
            assert Fraction(1, 2) > 0 and Fraction(2, 9) > 0
            k3_channel_masses = [str(mass) for mass in channel_masses]

    result = {
        "status": "pass",
        "proof_role": "finite arithmetic and domain falsifier only",
        "constants": {
            "Y_DV": Y_DV,
            "TAV": TAV,
            "full_DV": FULL_DV,
            "DE": DE,
            "channel_two_additive": 7_185,
            "K_J": "18900*K_E+7185",
            "C_W": "18*K_1+9*K_2+340200*K_E+129330",
        },
        "domain": {
            "odd_k_min": 3,
            "odd_k_max_checked": 2001,
            "rank_instances": checked_ranks,
            "cutoff_instances": checked_cutoffs,
            "k3": {"n": 9, "m": 4, "adjacent_ranks": [1], "cutoffs": [2, 3, 4]},
            "k3_channel_masses": k3_channel_masses,
        },
        "scope_guards": {
            "PCR": False,
            "FCL1": False,
            "bridge_gap": False,
            "polynomial_mixing": False,
            "terminal": False,
            "remaining_stop": "FD-bound or minority-sign",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
