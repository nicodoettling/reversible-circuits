#!/usr/bin/env python3
"""No-import boundary and exact-rational checker for the M248 audit."""


def main():
    assert 7000 + 160 == 7160
    assert 7000 + 4 == 7004
    assert 7160 + 4 == 7164

    ranks = splits = cutoffs = coefficient_rows = g_calls = 0
    minimum_h_twice_margin = None
    minimum_absorption_margin = None

    for k in range(3, 2002, 2):
        ranks += 1
        D = 2 * k - 1
        R = 2 * k - 3
        j = (k - 1) // 2
        L = (3 * k - 1) // 2
        assert R >= k and D - k == k - 1

        for s in range(1, j + 1):
            splits += 1
            assert 2 * (k - s) >= k + 1
            assert 2 * (D - s) >= 3 * k - 1

            # Exact rational forms a_L=aL_num/aL_den and
            # a_F=aF_num/aF_den, with no Fraction/import dependency.
            aL_den = R * s * (D - s)
            aL_num = aL_den - 2 * (2 * s * (D - s) - (D - s) - s)
            aF_den = R * s * (k - s)
            aF_num = aF_den - 2 * (2 * s * (k - s) - (k - s) - s)
            assert 0 < aL_num <= aL_den
            assert 0 < aF_num <= aF_den

            actual_num = aF_num * aL_den - aL_num * aF_den
            actual_den = aF_den * aL_num
            expected_num = 2 * s * (k - 1)
            expected_den = (k - s) * aL_num
            assert actual_num * expected_den == expected_num * actual_den
            assert 3 * k * k * actual_num <= 16 * actual_den

            r = D - s
            h_twice_margin = 2 * (r - 1) * (r - 2) - r * R
            assert h_twice_margin >= 0
            if minimum_h_twice_margin is None or h_twice_margin < minimum_h_twice_margin:
                minimum_h_twice_margin = h_twice_margin

        for ell in range(2, L + 1):
            cutoffs += 1
            absorption_margin = k * k * ell - 16
            assert absorption_margin >= 0
            if minimum_absorption_margin is None or absorption_margin < minimum_absorption_margin:
                minimum_absorption_margin = absorption_margin

        # The YCM coefficient cases cover the full cutoff and every G call
        # stays in M229's corrected domain 1 <= x <= L-1.
        for y in range(2, L + 1):
            coefficient_rows += 1
            if y < k:
                args = (y, y - 1)
            elif y == k:
                args = (k - 1,)
            else:
                z = y - k
                assert 1 <= z <= j
                args = (k + z - 1, z)
            for x in args:
                g_calls += 1
                assert 1 <= x <= L - 1

    assert minimum_h_twice_margin == 0
    assert minimum_absorption_margin == 2
    print(
        '{"status":"pass","imports":0,"checked_odd_k_max":2001,'
        '"rank_count":%d,"split_rows":%d,"cutoff_rows":%d,'
        '"coefficient_rows":%d,"g_domain_calls":%d,'
        '"minimum_twice_h_margin":%d,'
        '"minimum_k_squared_ell_minus_16":%d,'
        '"wbe_constants":{"Y":7000,"X":7160},'
        '"normalizer_bound":"16/k^2",'
        '"de_constants":{"Y":7004,"X":7164}}'
        % (
            ranks,
            splits,
            cutoffs,
            coefficient_rows,
            g_calls,
            minimum_h_twice_margin,
            minimum_absorption_margin,
        )
    )


if __name__ == "__main__":
    main()
