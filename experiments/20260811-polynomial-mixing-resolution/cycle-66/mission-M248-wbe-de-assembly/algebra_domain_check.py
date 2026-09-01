#!/usr/bin/env python3
"""Compact no-import falsifier for the M248 assembly arithmetic."""


def main():
    assert 7000 + 160 == 7160
    assert 7000 + 4 == 7004
    assert 7160 + 4 == 7164

    ranks = 0
    split_rows = 0
    cutoff_rows = 0
    minimum_absorption_margin = None

    for k in range(3, 1002, 2):
        ranks += 1
        D = 2 * k - 1
        R = 2 * k - 3
        j = (k - 1) // 2
        L = (3 * k - 1) // 2

        assert R >= k
        assert 2 * (k - j) >= k + 1
        assert 2 * (D - j) >= 3 * k - 1
        assert (k + 1) * (3 * k - 1) - 3 * k * (k - 1) == 5 * k - 1

        for s in range(1, j + 1):
            split_rows += 1
            assert 2 * (k - s) >= k + 1
            assert 2 * (D - s) >= 3 * k - 1
            # With a_L >= 1/2, this is exactly the cross-multiplied
            # rho_s <= 16/(3 k^2) inequality.
            left = 3 * k * (k - 1)
            right = (k + 1) * (3 * k - 1)
            assert left <= right

        for ell in range(2, L + 1):
            cutoff_rows += 1
            margin = k * k * ell - 16
            assert margin >= 0
            if minimum_absorption_margin is None or margin < minimum_absorption_margin:
                minimum_absorption_margin = margin

    assert minimum_absorption_margin == 2
    print(
        '{"status":"pass","imports":0,'
        '"checked_odd_k_max":1001,'
        '"rank_count":%d,"split_rows":%d,"cutoff_rows":%d,'
        '"minimum_k_squared_ell_minus_16":%d,'
        '"wbe_constants":{"Y":7000,"X":7160},'
        '"normalizer_bound":"16/k^2",'
        '"de_constants":{"Y":7004,"X":7164}}'
        % (ranks, split_rows, cutoff_rows, minimum_absorption_margin)
    )


if __name__ == "__main__":
    main()

