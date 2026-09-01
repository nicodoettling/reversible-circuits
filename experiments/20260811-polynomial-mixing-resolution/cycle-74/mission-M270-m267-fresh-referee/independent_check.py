#!/usr/bin/env python3
"""Clean-room finite guards for M267's formulas and endpoint ranges.

This file deliberately has no import statements and reads no predecessor
code or data.  It is finite falsification only, never an all-rank proof.
"""


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


class Q:
    def __init__(self, p=0, q=1):
        if q < 0:
            p, q = -p, -q
        g = gcd(p, q)
        self.p, self.q = p // g, q // g

    def __add__(self, other):
        other = other if isinstance(other, Q) else Q(other)
        return Q(self.p * other.q + other.p * self.q, self.q * other.q)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.p, self.q)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return Q(other) - self

    def __mul__(self, other):
        other = other if isinstance(other, Q) else Q(other)
        return Q(self.p * other.p, self.q * other.q)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = other if isinstance(other, Q) else Q(other)
        return Q(self.p * other.q, self.q * other.p)

    def __pow__(self, exponent):
        return Q(self.p ** exponent, self.q ** exponent)

    def __abs__(self):
        return Q(abs(self.p), self.q)

    def __eq__(self, other):
        other = other if isinstance(other, Q) else Q(other)
        return self.p == other.p and self.q == other.q

    def __le__(self, other):
        other = other if isinstance(other, Q) else Q(other)
        return self.p * other.q <= other.p * self.q

    def __lt__(self, other):
        other = other if isinstance(other, Q) else Q(other)
        return self.p * other.q < other.p * self.q

    def __str__(self):
        return str(self.p) if self.q == 1 else str(self.p) + "/" + str(self.q)


def factorial(n):
    out = 1
    for x in range(2, n + 1):
        out *= x
    return out


def tau(d):
    assert d >= 1
    return Q(d ** (d - 1), factorial(d))


def ratio1(d):
    return Q(0) if d < 2 else tau(d - 1) / tau(d)


def ratio2(d):
    return Q(0) if d < 3 else tau(d - 2) / tau(d)


def mul(p, q):
    return tuple(p[q[x]] for x in range(len(p)))


def inv(p):
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def tr(n, a, b):
    out = list(range(n))
    out[a], out[b] = out[b], out[a]
    return tuple(out)


def cycles(p):
    seen = [False] * len(p)
    out = []
    for start in range(len(p)):
        if seen[start]:
            continue
        cycle = []
        x = start
        while not seen[x]:
            seen[x] = True
            cycle.append(x)
            x = p[x]
        out.append(tuple(cycle))
    return tuple(out)


def supported(n):
    h = tuple((x + 1) % n for x in range(n))
    edges = [tr(n, a, b) for a in range(n) for b in range(a + 1, n)]
    products = set()
    for first in edges:
        for second in edges:
            if first == second:
                continue
            s = mul(first, second)
            moved = sum(s[x] != x for x in range(n))
            if moved in (3, 4) and len(cycles(mul(inv(s), h))) == 3:
                products.add(s)
    return h, products


def owner_data(n, h, s):
    components = cycles(mul(inv(s), h))
    assert len(components) == 3
    vertex_owner = {}
    for i, component in enumerate(components):
        for x in component:
            vertex_owner[x] = i
    owner = []
    for r in range(n):
        head = (r + 1) % n
        owner.append(vertex_owner[r] if s[head] == head else -1)
    sizes = [len(component) for component in components]
    kappa = [[Q(0) for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            kappa[i][j] = (
                ratio2(sizes[i])
                if i == j
                else ratio1(sizes[i]) * ratio1(sizes[j])
            )
    return owner, sizes, kappa


def kap(kappa, a, b):
    return Q(0) if a < 0 or b < 0 else kappa[a][b]


def charge(owner, kappa, ell, x):
    n = len(owner)
    c = owner[(x - ell) % n]
    return kap(kappa, c, owner[(x + 1) % n]) - kap(kappa, c, owner[x])


def endpoint(owner, kappa, ell):
    return sum((charge(owner, kappa, ell, x) for x in range(len(owner))), Q(0))


def correlation(owner, kappa, ell):
    n = len(owner)
    return sum(
        (kap(kappa, owner[r], owner[(r + ell) % n]) for r in range(n)), Q(0)
    )


def split_weight(d, s):
    return Q(factorial(d - 2), d ** (d - 2)) * tau(s) * tau(d - s)


def normalization_guard(k):
    long_d = 2 * k - 1
    p = sum((long_d * split_weight(long_d, s) for s in range(1, k)), Q(0))
    q = sum((k * split_weight(k, s) for s in range(1, (k - 1) // 2 + 1)), Q(0))
    rank = k - 1
    den = 3 * rank * (3 * rank - 1)
    alpha = (
        Q(rank * (rank - 1), den),
        Q(4 * rank * rank, den),
        Q(2 * rank * (2 * rank - 1), den),
    )
    assert p == 1 and q == 1 and sum(alpha, Q(0)) == 1


def ratio_guard():
    e2 = 7.38905609893065
    for d in range(1, 301):
        diagonal = 0.0 if d < 3 else ((d - 1) / d) * ((d - 2) / d) ** (d - 3)
        assert abs(e2 * diagonal - 1.0) <= 20.0 / d + 1e-12
    for d in range(1, 81):
        for e in range(1, 81):
            left = 0.0 if d < 2 else ((d - 1) / d) ** (d - 2)
            right = 0.0 if e < 2 else ((e - 1) / e) ** (e - 2)
            assert abs(e2 * left * right - 1.0) <= (
                20.0 * (1.0 / d + 1.0 / e) + 1e-12
            )


def pointwise_guard(k):
    n = 3 * k
    h, products = supported(n)
    kinds = {"T": 0, "D": 0}
    maximum = Q(0)
    for s in products:
        owner, sizes, kappa = owner_data(n, h, s)
        moved_heads = {(v - 1) % n for v in range(n) if s[v] != v}
        nulls = {r for r in range(n) if owner[r] < 0}
        assert nulls == moved_heads
        kind = "T" if len(moved_heads) == 3 else "D"
        kinds[kind] += 1
        owner_sets = [[owner[r] == i for r in range(n)] for i in range(3)]
        owner_sizes = [sum(bits) for bits in owner_sets]
        for bits in owner_sets:
            assert sum(bits[r] != bits[(r + 1) % n] for r in range(n)) <= 4
        for i in range(3):
            for j in range(3):
                corr = [
                    sum(owner_sets[i][r] and owner_sets[j][(r + ell) % n] for r in range(n))
                    for ell in range(n)
                ]
                variation = sum(abs(corr[(ell + 1) % n] - corr[ell]) for ell in range(n))
                assert variation <= 4 * min(owner_sizes[i], owner_sizes[j])
        values = []
        for ell in range(n):
            e = endpoint(owner, kappa, ell)
            assert e == correlation(owner, kappa, ell + 1) - correlation(owner, kappa, ell)
            assert e == -endpoint(owner, kappa, (n - ell - 1) % n)
            phase_average = sum(
                (charge(owner, kappa, ell, x) / n for x in range(n)), Q(0)
            )
            assert e == n * phase_average
            for x in range(n):
                if owner[x] == owner[(x + 1) % n]:
                    assert charge(owner, kappa, ell, x) == 0
            values.append(e)
        assert values[(n - 1) // 2] == 0
        l1 = sum((abs(values[ell]) for ell in range(2, n - 2)), Q(0))
        maximum = maximum if maximum >= l1 else l1
        # 7.39 is a rigorous convenient decimal upper bound for e^2.
        assert Q(739, 100) * l1 <= 1232
        assert sum(sizes) == n
    return len(products), kinds, maximum


def witness_guard():
    n = 9
    h = tuple((x + 1) % n for x in range(n))
    s1 = mul(tr(n, 0, 2), tr(n, 6, 7))
    s2 = mul(tr(n, 1, 8), tr(n, 6, 7))
    o1, _, k1 = owner_data(n, h, s1)
    o2, _, k2 = owner_data(n, h, s2)
    e1, e2 = endpoint(o1, k1, 2), endpoint(o2, k2, 2)
    profiles = []
    for s in (s1, s2):
        profile = []
        for component in cycles(mul(inv(s), h)):
            vertices = set(component)
            runs = sum((x - 1) % n not in vertices for x in vertices)
            profile.append((len(component), runs))
        profiles.append(tuple(sorted(profile)))
    assert profiles[0] == profiles[1] == ((1, 1), (2, 1), (6, 2))
    assert e1 == Q(-625, 1296) and e2 == Q(-20, 81) and e1 != e2
    return profiles[0], e1, e2


def telescoping_guard(k):
    n = 3 * k
    m = (n - 3) // 2
    increments = {}
    for ell in range(2, k - 1):
        increments[ell] = -(ell + 2)
    for ell in range(k - 1, m + 1):
        increments[ell] = ell + 3
    increments[(n - 1) // 2] = 0
    for ell in range(2, m + 1):
        increments[n - ell - 1] = -increments[ell]
    g = {2: 7}
    for ell in range(2, n - 2):
        g[ell + 1] = g[ell] + increments[ell]
    lhs = sum(abs(increments[ell]) for ell in range(2, n - 2))
    rhs = 2 * (g[2] + g[(n - 1) // 2] - 2 * g[k - 1])
    assert lhs == rhs and rhs >= 0


def main():
    ratio_guard()
    for k in (3, 5, 7, 9, 11):
        normalization_guard(k)
        telescoping_guard(k)
    rows = []
    for k in (3, 5):
        count, kinds, maximum = pointwise_guard(k)
        rows.append((k, count, kinds, maximum))
    profile, e1, e2 = witness_guard()
    print("status=PASS; finite formula/boundary falsification only")
    print("imports=0; predecessor_reads=0; deterministic=true; seed=null")
    for k, count, kinds, maximum in rows:
        print(
            "k=" + str(k)
            + "; supported=" + str(count)
            + "; T=" + str(kinds["T"])
            + "; D=" + str(kinds["D"])
            + "; max_target_l1=" + str(maximum)
        )
    print("normalization_and_SR_TPR_boundary_rows=5")
    print("Cayley_ratio_diagonal_rows=300; cross_rows=6400")
    print("M264_profile=" + str(profile) + "; E2=" + str(e1) + "," + str(e2))


if __name__ == "__main__":
    main()
