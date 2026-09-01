#!/usr/bin/env python3
"""Bounded, import-free exact/algebra falsification of the M251 formulas."""


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


class Q:
    def __init__(self, n=0, d=1):
        if d < 0:
            n, d = -n, -d
        g = gcd(abs(n), d)
        self.n, self.d = n // g, d // g

    @staticmethod
    def q(x):
        return x if isinstance(x, Q) else Q(x)

    def __add__(self, x):
        x = Q.q(x)
        return Q(self.n * x.d + x.n * self.d, self.d * x.d)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.n, self.d)

    def __sub__(self, x):
        return self + (-Q.q(x))

    def __rsub__(self, x):
        return Q.q(x) - self

    def __mul__(self, x):
        x = Q.q(x)
        return Q(self.n * x.n, self.d * x.d)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = Q.q(x)
        return Q(self.n * x.d, self.d * x.n)

    def __rtruediv__(self, x):
        return Q.q(x) / self

    def __pow__(self, n):
        return Q(self.n ** n, self.d ** n)

    def __eq__(self, x):
        x = Q.q(x)
        return self.n == x.n and self.d == x.d

    def __le__(self, x):
        x = Q.q(x)
        return self.n * x.d <= x.n * self.d

    def __abs__(self):
        return Q(abs(self.n), self.d)


def fact(n):
    z = 1
    for j in range(2, n + 1):
        z *= j
    return z


def core(d):
    return Q(d ** (d - 1), fact(d))


def ker(R, r, d):
    return core(d) * core(r - d) / core(r) / R


def h(R, r):
    return Q((r - 1) * (r - 2), r * R)


def root_floor(x):
    a = 0
    while (a + 1) * (a + 1) <= x:
        a += 1
    return a


def root_ceil(x):
    a = root_floor(x)
    return a if a * a == x else a + 1


checks = 0


def check(x):
    global checks
    assert x
    checks += 1


def word(k):
    return list(range(1, k)) + list(range(2 * k, 3 * k))


def gap(k, i, x):
    v, n, D = word(k), 3 * k, 2 * k - 1
    return (v[(i + x) % D] - v[i % D]) % n


def F(k, ell, x):
    D = 2 * k - 1
    return Q(sum(2 <= gap(k, i, x) <= ell for i in range(D)), D)


def F_closed(k, ell, x):
    D = 2 * k - 1
    if ell < k:
        if x == 1:
            return Q(1, D)
        if 2 <= x <= ell - 1:
            return Q(D - x, D)
        if x == ell:
            return Q(D - 2 * ell, D)
        return Q()
    if ell == k:
        return Q(1, D) if x == 1 else (Q(D - x, D) if 2 <= x <= k - 1 else Q())
    a = ell - k
    if x == 1:
        return Q(2, D)
    if 2 <= x <= a:
        return Q(1)
    if a + 1 <= x <= ell - 1:
        return Q(D - x, D)
    return Q()


def atom(k, ell, z, r, i, d, a):
    D, n = 2 * k - 1, 3 * k
    ans = int(2 <= gap(k, i + a, d) <= ell)
    if z == "X":
        ans += int(2 <= n - gap(k, i + r, D - r) - gap(k, i + a, d) <= ell)
    return ans


def vpart(k, ell, z, r):
    D, R = 2 * k - 1, 2 * k - 3
    return sum((ker(R, r, d) * atom(k, ell, z, r, i, d, a)
                for i in range(D) for d in range(1, r - 1)
                for a in range(1, r - d)), Q()) / D


def u(k, ell, z, r):
    D, R = 2 * k - 1, 2 * k - 3
    return h(R, r) * F(k, ell, D - r) + vpart(k, ell, z, r)


def phi(k, ell, z, s):
    D, R, q = 2 * k - 1, 2 * k - 3, 2 * k - 1 - s
    return (u(k, ell, z, s) + u(k, ell, z, q)) / (h(R, s) + h(R, q))


def W(k, r, f):
    R = 2 * k - 3
    return sum(((r - d - 1) * ker(R, r, d) * f(d)
                for d in range(1, r - 1)), Q())


def Lop(k, s, f):
    D, R, q = 2 * k - 1, 2 * k - 3, 2 * k - 1 - s
    H = h(R, s) + h(R, q)
    return (h(R, s) * f(q) + h(R, q) * f(s) + W(k, s, f) + W(k, q, f)) / H


# A rigorous rational enclosure for e, used only in bounded far-remainder checks.
N = 18
ELO = sum((Q(1, fact(j)) for j in range(N + 1)), Q())
EHI = ELO + Q(1, fact(N + 1)) * Q(N + 2, N + 1)

for k in (3, 5, 7):
    D, R = 2 * k - 1, 2 * k - 3
    for ell in range(2, (3 * k - 1) // 2 + 1):
        for x in range(1, D):
            check(F(k, ell, x) == F_closed(k, ell, x))
        seam = sum((root_ceil(t) * abs(F(k, ell, t + 1) - F(k, ell, t))
                    for t in range(1, D - 1)), Q())
        check(seam <= 8 * root_floor(ell))
        for r in range(1, D - 1):
            for z in ("Y", "X"):
                common = sum((
                    (ker(R, r + 1, d) * atom(k, ell, z, r, i, d, a)
                     - ker(R, r, d) * atom(k, ell, z, r, i, d, a)
                     + ker(R, r + 1, d) * (atom(k, ell, z, r + 1, i, d, a)
                                             - atom(k, ell, z, r, i, d, a)))
                    for i in range(D) for d in range(1, r - 1)
                    for a in range(1, r - d)), Q()) / D
                strip = sum((ker(R, r + 1, d) * atom(k, ell, z, r + 1, i, d, r - d)
                             for i in range(D) for d in range(1, r)), Q()) / D
                check(vpart(k, ell, z, r + 1) - vpart(k, ell, z, r) == common + strip)
        for s in range(1, k - 1):
            q = D - s
            Hs, Hn = h(R, s) + h(R, q), h(R, s + 1) + h(R, q - 1)
            for z in ("Y", "X"):
                dN = (u(k, ell, z, s + 1) - u(k, ell, z, s)) - (u(k, ell, z, q) - u(k, ell, z, q - 1))
                check((phi(k, ell, z, s + 1) - phi(k, ell, z, s))
                      == (dN - phi(k, ell, z, s) * (Hn - Hs)) / Hn)
            two = sum((ker(R, r, d) *
                       int(2 <= 3 * k - gap(k, i + r, D - r) - gap(k, i + a, d) <= ell)
                       for r in (s, q) for i in range(D) for d in range(1, r - 1)
                       for a in range(1, r - d)), Q()) / D / Hs
            check(phi(k, ell, "X", s) - phi(k, ell, "Y", s) == two)
        yd = sum((root_ceil(s) * abs(phi(k, ell, "Y", s + 1) - phi(k, ell, "Y", s))
                  for s in range(1, k - 1)), Q())
        check(yd <= 18400 * root_floor(ell))

    for r in range(1, D - 1):
        for t in range(1, D - 1):
            f = lambda d, t=t: Q(int(d <= t))
            inc = W(k, r + 1, f) - W(k, r, f)
            check(abs(inc) <= Q(3, R))
            if r >= 2 * t + 2:
                blo = sum((core(d) / (EHI ** d) for d in range(1, t + 1)), Q())
                bhi = sum((core(d) / (ELO ** d) for d in range(1, t + 1)), Q())
                lo, hi = inc - bhi / R, inc - blo / R
                err = abs(lo) if abs(hi) <= abs(lo) else abs(hi)
                check(err * err <= Q(120 * 120 * t, R * R * r * r))
    for s in range(1, k):
        H = h(R, s) + h(R, D - s)
        check(Q(2, 9) <= H)
        check(Lop(k, s, lambda d: Q(1)) == 2)
    for t in range(1, D - 1):
        p = lambda s, t=t: Lop(k, s, lambda d: Q(int(d <= t)))
        hv = sum((root_ceil(s) * abs(p(s + 1) - p(s)) for s in range(1, k - 1)), Q())
        check(hv <= 2300 * root_floor(t))

print('{"mission":"M255","bounded_k":[3,5,7],"assertions":%d,"status":"pass",'
      '"finite_only":true,"universal_inference":false,"imports":0}' % checks)
