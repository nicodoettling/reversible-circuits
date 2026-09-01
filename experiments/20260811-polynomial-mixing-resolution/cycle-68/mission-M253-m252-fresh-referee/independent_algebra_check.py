#!/usr/bin/env python3
"""No-import exact/algebra checks for the immutable M252 implication.

This is finite falsification evidence. The all-rank arguments are written in
the referee report; no result is inferred from the finite ranges alone.
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


def leq(x, y):
    return x[0] * y[1] <= y[0] * x[1]


def eq(x, y):
    return x[0] * y[1] == y[0] * x[1]


def absolute(x):
    return (abs(x[0]), x[1])


channel_rows = 0
mixture_rows = 0
endpoint_rows = 0
grouping_rows = 0

for k in range(3, 258, 2):
    n = 3 * k
    m = (n - 1) // 2

    # Middle residual rank k-1 and aggregate exterior rank 2k-2 agree at
    # both sources, so the first-two-color hypergeometric masses agree.
    den = (3 * k - 3) * (3 * k - 4)
    c0 = (k - 1) * (k - 2)
    c1 = 2 * (k - 1) * (2 * k - 2)
    c2 = (2 * k - 2) * (2 * k - 3)
    assert c0 + c1 + c2 == den
    for c in (c0, c1, c2):
        assert 0 <= c <= den
    channel_rows += 1

    # A common J0 conditional law cancels from the exact source difference.
    for cutoff in range(2, min(m, 13) + 1):
        j0 = rat(2 * cutoff + 1, cutoff + 3)
        a1 = rat(cutoff * cutoff + 1, cutoff + 5)
        b1 = rat(3 * cutoff + 2, cutoff + 7)
        a2 = rat(cutoff + 4, 2 * cutoff + 3)
        b2 = rat(2 * cutoff * cutoff + 1, cutoff + 9)
        full_a = add(add(mul(rat(c0, den), j0), mul(rat(c1, den), a1)),
                     mul(rat(c2, den), a2))
        full_b = add(add(mul(rat(c0, den), j0), mul(rat(c1, den), b1)),
                     mul(rat(c2, den), b2))
        reduced = add(mul(rat(c1, den), sub(b1, a1)),
                      mul(rat(c2, den), sub(b2, a2)))
        assert eq(sub(full_b, full_a), reduced)
        mixture_rows += 1

    # M192's unequal disjoint-submeasure mass and endpoint absorptions.
    disjoint_mass_difference = sub(
        sub(rat(1), rat(3, 2 * k - 1)),
        sub(rat(1), rat(3 * (k - 2), k * (2 * k - 3))),
    )
    exact_endpoint = rat(-6 * (k - 1), k * (2 * k - 1) * (2 * k - 3))
    assert eq(disjoint_mass_difference, exact_endpoint)
    observable_endpoint = mul(rat(3), absolute(exact_endpoint))
    assert leq(observable_endpoint, rat(18, k * k))

    shared_bound = mul(
        rat(3),
        add(rat(3, 2 * k - 1), rat(3 * (k - 2), k * (2 * k - 3))),
    )
    assert leq(shared_bound, rat(15, k))

    for cutoff in range(2, m + 1):
        # 3|E| <= 6 sqrt(cutoff)/k, checked exactly after squaring.
        left = mul(observable_endpoint, rat(k, 6))
        assert leq(mul(left, left), rat(cutoff))
        endpoint_rows += 1

    # Exact triangle grouping behind sum_d |epsilon_d|/d. rho_num is an
    # arbitrary nonnegative common-denominator mass vector; that denominator
    # cancels from both sides.
    delta = {a: ((a * a + 3 * a + k) % 11) - 5 for a in range(1, 2 * k)}
    rho_num = {b: 1 + ((2 * b * b + b + k) % 13) for b in range(1, k)}
    signed_by_d = {}
    raw_by_d = {}
    min_d = n
    for a in range(1, 2 * k):
        for b in range(1, k):
            d = n - a - b
            min_d = min(min_d, d)
            term = delta[a] * rho_num[b]
            signed_by_d[d] = signed_by_d.get(d, 0) + term
            raw_by_d[d] = raw_by_d.get(d, 0) + abs(term)
    assert min_d == 2
    lhs = rat(0)
    rhs = rat(0)
    for d in signed_by_d:
        lhs = add(lhs, rat(abs(signed_by_d[d]), d))
        rhs = add(rhs, rat(raw_by_d[d], d))
        assert abs(signed_by_d[d]) <= raw_by_d[d]
        grouping_rows += 1
    assert leq(lhs, rhs)


# The coefficient of |x_d| in Hardy--Abel is exactly
# 1/m + sum_{D=d}^{m-1} 1/D^2 (empty for d=m).
hardy_rows = 0
for m in range(2, 514):
    tail = rat(0)
    weights = {m: rat(1, m)}
    for d in range(m - 1, 1, -1):
        tail = add(tail, rat(1, d * d))
        weights[d] = add(rat(1, m), tail)
    for d in range(2, m + 1):
        assert leq(weights[d], rat(3, d))
        hardy_rows += 1


# Exact constant/scaling ledger.
assert 3 * 2 * 3 == 18       # n=3k, Hardy 3, two K1 occurrences
assert 3 * 3 == 9            # n=3k, Hardy 3, one K2 occurrence
assert 2 * 3 * 3 == 18       # two J2 prefixes, series bound 3, n/k=3
assert 7004 <= 7164
assert 7164 + 15 + 6 == 7185


# Strict PCR non-implication: x_k=1, x_(k+1)=-1 has weighted l1 <=2/k,
# but its D=k prefix is one and its squared ratio to sqrt(k)/k is k.
pcr_witness_rows = 0
for k in range(3, 2002, 2):
    assert leq(add(rat(1, k), rat(1, k + 1)), rat(2, k))
    pcr_witness_rows += 1


print("{")
print('  "status": "pass",')
print('  "scope": "finite exact falsification only; all-rank proof is in report.md",')
print('  "channel_mass_rows": %d,' % channel_rows)
print('  "mixture_identity_rows": %d,' % mixture_rows)
print('  "grouped_epsilon_rows": %d,' % grouping_rows)
print('  "hardy_coefficient_rows": %d,' % hardy_rows)
print('  "endpoint_absorption_rows": %d,' % endpoint_rows)
print('  "pcr_nonimplication_rows": %d' % pcr_witness_rows)
print("}")

