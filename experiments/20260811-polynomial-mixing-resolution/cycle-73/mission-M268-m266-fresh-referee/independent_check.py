#!/usr/bin/env python3
"""No-import exact arithmetic guard for the M268 assembly audit.

This is finite falsification only. Universal estimates are audited from the
frozen symbolic proofs.
"""


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def rat(a, b=1):
    assert b != 0
    if b < 0:
        a, b = -a, -b
    g = gcd(a, b)
    return (a // g, b // g)


def add(x, y):
    return rat(x[0] * y[1] + y[0] * x[1], x[1] * y[1])


def neg(x):
    return (-x[0], x[1])


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    return rat(x[0] * y[0], x[1] * y[1])


def le(x, y):
    return x[0] * y[1] <= y[0] * x[1]


def check_constants():
    assert 18_400 + 500 == 18_900
    assert 7_164 + 15 + 6 == 7_185
    assert 18 * 18_900 == 340_200
    assert 18 * 7_185 == 129_330


def check_channel_and_domain():
    ranks = 0
    cutoffs = 0
    for k in range(3, 2002, 2):
        n = 3 * k
        m = (n - 1) // 2
        den = (3 * k - 3) * (3 * k - 4)
        nums = (
            (k - 1) * (k - 2),
            2 * (k - 1) * (2 * k - 2),
            (2 * k - 2) * (2 * k - 3),
        )
        assert n % 2 == 1 and m == n // 2
        assert all(x >= 0 for x in nums) and sum(nums) == den
        assert len(range(1, k - 1)) == k - 2
        assert len(range(2, m + 1)) == m - 1
        ranks += 1
        cutoffs += m - 1

        if k == 3:
            assert (n, m) == (9, 4)
            assert tuple(range(1, k - 1)) == (1,)
            assert tuple(range(2, m + 1)) == (2, 3, 4)
            assert tuple(rat(x, den) for x in nums) == (
                rat(1, 15), rat(8, 15), rat(2, 5)
            )
            d, r = 2 * k - 1, 2 * k - 3

            def h(s):
                return rat((s - 1) * (s - 2), s * r)

            assert add(h(1), h(d - 1)) == rat(1, 2)
            assert add(h(2), h(d - 2)) == rat(2, 9)
            assert rat(-6 * (k - 1), k * (2 * k - 1) * (2 * k - 3)) == rat(-4, 15)

    return ranks, cutoffs


def check_hardy():
    rows = 0
    for m in range(4, 302):
        for d in range(2, m + 1):
            coefficient = rat(1, m)
            for cutoff in range(d, m):
                coefficient = add(coefficient, rat(1, cutoff * cutoff))
            assert le(coefficient, rat(3, d))
            rows += 1
    return rows


def check_sbp():
    rows = 0
    for k in range(3, 202, 2):
        n = 3 * k
        m = (n - 1) // 2
        singleton = ((5 * k + 1) % 19) - 9
        u11 = rat(-3, 2)
        ncoef = {}
        pcoef = {}
        u2 = {}
        residual = {}
        for d in range(2, m + 1):
            ncoef[d] = ((d * d + 3 * k * d + 1) % 23) - 11
            pcoef[d] = ((2 * d * d + k * d + 7) % 29) - 14
            u2[d] = rat((-1 if d % 2 else 1) * (2 * d + 1), d * (d + 1))
            residual[d] = rat(3 * d - 1, d * (d + 2))

        lhs = mul(rat(singleton), u11)
        for d in range(2, m + 1):
            lhs = add(lhs, mul(rat(ncoef[d]), u2[d]))
            lhs = add(lhs, mul(rat(pcoef[d]), residual[d]))

        aprefix = {}
        cprefix = {}
        a = rat(0)
        c = rat(0)
        for d in range(2, m + 1):
            a = add(a, rat(ncoef[d]))
            c = add(c, rat(pcoef[d]))
            aprefix[d], cprefix[d] = a, c

        rhs = mul(rat(singleton), u11)
        rhs = add(rhs, mul(aprefix[m], u2[m]))
        rhs = add(rhs, mul(cprefix[m], residual[m]))
        for d in range(2, m):
            rhs = add(rhs, mul(aprefix[d], sub(u2[d], u2[d + 1])))
            rhs = add(rhs, mul(cprefix[d], sub(residual[d], residual[d + 1])))
        assert lhs == rhs
        rows += 1
    return rows


def check_response_scaling():
    rows = 0
    target_rows = 0
    for k in range(3, 2002, 2):
        n = 3 * k
        response_den = (n - 3) * (n - 4)
        assert 27 * response_den >= 10 * n * n
        assert response_den < n * n
        t_num = 12 * (k - 1)
        t_den = 3 * k * (3 * k - 4) * (2 * k - 1)
        assert n * n * t_num <= 9 * t_den
        assert 2 * n * t_num <= 2 * t_den
        assert 3 * (n - 3) >= 2 * n
        rows += 1

        if k <= 101:
            # n*pi_y = 2*((n-2)/n)^(n-4), checked exactly.
            top = 2 * pow(n - 2, n - 4)
            bot = pow(n, n - 4)
            assert bot <= 4 * top
            assert top <= 2 * bot
            target_rows += 1
    return rows, target_rows


def main():
    check_constants()
    ranks, cutoffs = check_channel_and_domain()
    hardy_rows = check_hardy()
    sbp_rows = check_sbp()
    response_rows, target_rows = check_response_scaling()
    print("{")
    print('  "status": "pass",')
    print('  "checker_role": "finite exact falsification only",')
    print('  "imports": 0,')
    print('  "constant_checks": 4,')
    print('  "odd_rank_rows": %d,' % ranks)
    print('  "cutoff_rows": %d,' % cutoffs)
    print('  "hardy_rows": %d,' % hardy_rows)
    print('  "sbp_rows": %d,' % sbp_rows)
    print('  "response_scaling_rows": %d,' % response_rows)
    print('  "target_mass_rows": %d,' % target_rows)
    print('  "k3": {"n": 9, "m": 4, "ranks": [1], "cutoffs": [2, 3, 4], "channel_masses": ["1/15", "8/15", "2/5"], "H": ["1/2", "2/9"], "disjoint_endpoint": "-4/15"},')
    print('  "scope_stop": "FD-bound or minority-sign; no PCR/FCL1/gap/mixing/Terminal"')
    print("}")


if __name__ == "__main__":
    main()
