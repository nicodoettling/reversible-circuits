#!/usr/bin/env python3
"""Compact, no-import exact audit of the frozen M109 boundary theorem.

This file deliberately has no import statements and reads no predecessor
artifact.  It uses a tiny rational/polynomial implementation, reconstructs
the accepted all-j recurrence, and checks only the decisive calibrations and
the complete finite Bernstein certificate required by the analytic proof.
"""


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


class Q:
    __slots__ = ("n", "d")

    def __init__(self, n=0, d=1):
        if isinstance(n, Q):
            self.n, self.d = n.n, n.d
            return
        if d == 0:
            raise ZeroDivisionError
        if d < 0:
            n, d = -n, -d
        g = gcd(n, d)
        self.n, self.d = n // g, d // g

    @staticmethod
    def get(x):
        return x if isinstance(x, Q) else Q(x)

    def __add__(self, other):
        if not isinstance(other, (Q, int)):
            return NotImplemented
        other = Q.get(other)
        return Q(self.n * other.d + other.n * self.d, self.d * other.d)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.n, self.d)

    def __sub__(self, other):
        if not isinstance(other, (Q, int)):
            return NotImplemented
        return self + (-Q.get(other))

    def __rsub__(self, other):
        if not isinstance(other, (Q, int)):
            return NotImplemented
        return Q.get(other) - self

    def __mul__(self, other):
        if not isinstance(other, (Q, int)):
            return NotImplemented
        other = Q.get(other)
        return Q(self.n * other.n, self.d * other.d)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if not isinstance(other, (Q, int)):
            return NotImplemented
        other = Q.get(other)
        return Q(self.n * other.d, self.d * other.n)

    def __rtruediv__(self, other):
        if not isinstance(other, (Q, int)):
            return NotImplemented
        return Q.get(other) / self

    def __pow__(self, power):
        if power < 0:
            return Q(self.d ** (-power), self.n ** (-power))
        return Q(self.n ** power, self.d ** power)

    def __eq__(self, other):
        other = Q.get(other)
        return self.n == other.n and self.d == other.d

    def __lt__(self, other):
        other = Q.get(other)
        return self.n * other.d < other.n * self.d

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return Q.get(other) < self

    def __ge__(self, other):
        return Q.get(other) <= self

    def __bool__(self):
        return self.n != 0

    def __repr__(self):
        return str(self.n) if self.d == 1 else "%d/%d" % (self.n, self.d)


def fact(n):
    ans = 1
    for j in range(2, n + 1):
        ans *= j
    return ans


def comb(n, k):
    if k < 0 or n < 0 or k > n:
        return 0
    k = min(k, n - k)
    ans = 1
    for j in range(1, k + 1):
        ans = ans * (n - k + j) // j
    return ans


W_CACHE = {}
C_CACHE = {}
GROUP_CACHE = {}


def w(a):
    if a not in W_CACHE:
        if a < 1:
            raise ValueError(("w", a))
        W_CACHE[a] = Q(a ** (a - 1), fact(a))
    return W_CACHE[a]


def cayley(total, parts):
    key = (total, parts)
    if key not in C_CACHE:
        if parts == 0:
            C_CACHE[key] = Q(1 if total == 0 else 0)
        elif not 1 <= parts <= total:
            C_CACHE[key] = Q(0)
        else:
            C_CACHE[key] = Q(
                parts * total ** (total - parts),
                total * fact(total - parts),
            )
    return C_CACHE[key]


def qsplit(s, B):
    return w(s + 1 - B) * w(B) / w(s + 1)


def contextual(k, t, K, R, B):
    if t < B:
        return Q(0)
    if t == B:
        return Q(
            K * comb(k + K - R - 2, K - R - 1),
            comb(k + K - 1, K - 1),
        )
    return qsplit(t - 1, B) * (
        1 - Q(comb(K, R + 1), comb(K + k, R + 1))
    )


def attachment(K, R, k, j):
    return Q(
        comb(R + j, j) * comb(K - R - 1 + k - j, k - j),
        comb(K + k, k),
    )


def groups(s):
    if s not in GROUP_CACHE:
        rows = []
        total = Q(0)
        for k in range(1, s + 1):
            for t in range(1, s + 1):
                mass = w(t) * cayley(s - t, k - 1) / (fact(k) * w(s + 1))
                if mass:
                    rows.append((k, t, mass))
                    total += mass
        assert total == 1
        GROUP_CACHE[s] = tuple(rows)
    return GROUP_CACHE[s]


def compositions(n):
    if n == 0:
        return [()]
    rows = []
    for first in range(1, n + 1):
        for tail in compositions(n - first):
            rows.append((first,) + tail)
    return rows


def root_mass(comp):
    s = sum(comp)
    ans = Q(1, fact(len(comp)) * w(s + 1).n)
    # Avoid assuming w(s+1) is integral: divide as a rational operation.
    ans = Q(1, fact(len(comp))) / w(s + 1)
    for part in comp:
        ans *= w(part)
    return ans


RESET_CACHE = {}


def reset_energy(s, K, R, B, weighted=False):
    key = (s, K, R, B, weighted)
    if key in RESET_CACHE:
        return RESET_CACHE[key]
    parent_q = qsplit(s, B)
    answer = Q(0)
    scalars = {}

    def scalar(A, ell, last):
        skey = (A, ell, last)
        if skey not in scalars:
            value = Q(0)
            for p in range(1, A + 1):
                value += (
                    cayley(A, p)
                    * (contextual(p + ell, last, K, R, B) - parent_q)
                    / fact(p + ell)
                )
            scalars[skey] = value
        return scalars[skey]

    for ell in range(1, s):
        tail_parts = ell - 1
        for A in range(1, s + 1):
            for b in range(1, s - A - tail_parts + 1):
                tail_total = s - A - b
                child_rank = A + b - 1
                if child_rank < 2:
                    continue
                tails = []
                if tail_parts == 0:
                    if tail_total == 0:
                        tails.append((b, w(b)))
                else:
                    for last in range(1, tail_total + 1):
                        forest = cayley(tail_total - last, tail_parts - 1)
                        if forest:
                            tails.append((last, w(b) * forest * w(last)))
                for last, suffix_weight in tails:
                    current = scalar(A, ell, last)
                    energy = (
                        suffix_weight * fact(ell) * current * current
                        / (w(A) * w(s + 1))
                    )
                    if weighted:
                        energy *= 1 - qsplit(child_rank, b)
                    answer += energy
    RESET_CACHE[key] = answer
    return answer


def literal_reset_energy(s, K, R, B, include_inactive=False):
    parent_q = qsplit(s, B)
    answer = Q(0)
    for endpoint in compositions(s):
        if len(endpoint) < 2:
            continue
        A, b = endpoint[0], endpoint[1]
        if not include_inactive and A + b - 1 < 2:
            continue
        current = Q(0)
        for refinement in compositions(A):
            source = refinement + endpoint[1:]
            current += root_mass(source) * (
                contextual(len(source), source[-1], K, R, B) - parent_q
            )
        capacity = len(endpoint) * root_mass(endpoint)
        answer += current * current / capacity
    return answer


CHILD_CACHE = {}


def children(x):
    if x in CHILD_CACHE:
        return CHILD_CACHE[x]
    s, K, R, B = x
    rows = []
    for k, t, mass in groups(s):
        law_sum = Q(0)
        for j in range(k + 1):
            law_sum += attachment(K, R, k, j)
        assert law_sum == 1
        if t <= B or t - 1 < 2:
            continue
        for j in range(1, k + 1):
            nu = attachment(K, R, k, j)
            if not nu:
                continue
            child = (t - 1, K + k, R + j, B)
            pdrop = s + K - R - (child[0] + child[1] - child[2])
            ldrop = (s - B) - (child[0] - B)
            assert pdrop >= j >= 1
            assert ldrop == s - t + 1 >= 1
            assert child[1] > child[2] >= 1
            rows.append((mass * nu, child, k, t, j))
    CHILD_CACHE[x] = tuple(rows)
    return CHILD_CACHE[x]


H_CACHE = {}
G_CACHE = {}


def resolvent(x, weighted=False):
    cache = G_CACHE if weighted else H_CACHE
    if x not in cache:
        value = reset_energy(*x, weighted)
        for mass, child, _, _, _ in children(x):
            value += mass * resolvent(child, weighted)
        cache[x] = value
    return cache[x]


def beta(A, ell):
    ans = Q(0)
    for p in range(1, A + 1):
        ans += cayley(A, p) / fact(p + ell)
    return fact(ell + 1) * ans / w(A)


def l1_envelope(s, K):
    if s == 2:
        return Q(0), qsplit(2, 1) * (1 - qsplit(2, 1))
    r = w(s) / w(s + 1)
    u = w(s - 1) / w(s)
    q = r * u
    hbar = Q(s - 1, s + 1)
    z = Q(1, K + 1)
    env = (
        q * q * (hbar - q / 2)
        + q * (2 * z - q) ** 2 / 4
        + q * (1 - z) * (1 - u)
    )
    return env, q * (1 - q)


def l2_envelope(s, K):
    B = s - 2
    r = w(s) / w(s + 1)
    u = w(s - 1) / w(s)
    v = w(B) / w(s - 1)
    a = u * v
    q = Q(3, 2) * r * a
    hbar = Q(s - 1, s + 1)
    z = Q(1, K + 1)
    d = 2 * z * z / (1 + z)
    reset_part = (
        q * (hbar - 5 * q / 9 - q / (3 * v))
        + (3 * d - q) ** 2 / 27
        + (3 * d + 6 * z - 4 * q) ** 2 / 54
        + (v * (1 - d) - q) ** 2 / (6 * v)
    )
    descendant_part = (
        (1 - d) * (1 - v) / 3
        + Q(2, 3) * (1 - z) * (1 - a)
    )
    return q * (reset_part + descendant_part), q * (1 - q), reset_part, descendant_part


class Poly:
    __slots__ = ("nvars", "terms")

    def __init__(self, nvars, terms=None):
        self.nvars = nvars
        self.terms = {}
        if terms:
            for exponent, coefficient in terms.items():
                coefficient = Q.get(coefficient)
                if coefficient:
                    self.terms[tuple(exponent)] = coefficient

    @staticmethod
    def const(nvars, value):
        return Poly(nvars, {(0,) * nvars: Q.get(value)})

    @staticmethod
    def var(nvars, index):
        exponent = [0] * nvars
        exponent[index] = 1
        return Poly(nvars, {tuple(exponent): Q(1)})

    @staticmethod
    def get(nvars, value):
        if isinstance(value, Poly):
            assert value.nvars == nvars
            return value
        return Poly.const(nvars, value)

    def __add__(self, other):
        if isinstance(other, Rat):
            return NotImplemented
        other = Poly.get(self.nvars, other)
        terms = dict(self.terms)
        for exponent, coefficient in other.terms.items():
            terms[exponent] = terms.get(exponent, Q(0)) + coefficient
            if not terms[exponent]:
                del terms[exponent]
        return Poly(self.nvars, terms)

    __radd__ = __add__

    def __neg__(self):
        return Poly(self.nvars, {e: -c for e, c in self.terms.items()})

    def __sub__(self, other):
        if isinstance(other, Rat):
            return NotImplemented
        return self + (-Poly.get(self.nvars, other))

    def __rsub__(self, other):
        if isinstance(other, Rat):
            return NotImplemented
        return Poly.get(self.nvars, other) - self

    def __mul__(self, other):
        if isinstance(other, Rat):
            return NotImplemented
        other = Poly.get(self.nvars, other)
        terms = {}
        for e1, c1 in self.terms.items():
            for e2, c2 in other.terms.items():
                exponent = tuple(e1[j] + e2[j] for j in range(self.nvars))
                terms[exponent] = terms.get(exponent, Q(0)) + c1 * c2
        return Poly(self.nvars, terms)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return Rat(self) / other

    def __rtruediv__(self, other):
        return other / Rat(self)

    def __pow__(self, power):
        answer = Poly.const(self.nvars, 1)
        base = self
        while power:
            if power & 1:
                answer *= base
            base *= base
            power //= 2
        return answer

    def derivative(self, index):
        terms = {}
        for exponent, coefficient in self.terms.items():
            if exponent[index]:
                out = list(exponent)
                factor = out[index]
                out[index] -= 1
                terms[tuple(out)] = coefficient * factor
        return Poly(self.nvars, terms)

    def is_zero(self):
        return not self.terms


class Rat:
    __slots__ = ("num", "den")

    def __init__(self, num, den=None):
        if isinstance(num, Rat) and den is None:
            self.num, self.den = num.num, num.den
            return
        if not isinstance(num, Poly):
            raise TypeError(type(num))
        self.num = num
        self.den = Poly.const(num.nvars, 1) if den is None else den

    @staticmethod
    def get(nvars, value):
        if isinstance(value, Rat):
            return value
        return Rat(Poly.get(nvars, value))

    def __add__(self, other):
        other = Rat.get(self.num.nvars, other)
        return Rat(self.num * other.den + other.num * self.den, self.den * other.den)

    __radd__ = __add__

    def __neg__(self):
        return Rat(-self.num, self.den)

    def __sub__(self, other):
        return self + (-Rat.get(self.num.nvars, other))

    def __rsub__(self, other):
        return Rat.get(self.num.nvars, other) - self

    def __mul__(self, other):
        other = Rat.get(self.num.nvars, other)
        return Rat(self.num * other.num, self.den * other.den)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = Rat.get(self.num.nvars, other)
        return Rat(self.num * other.den, self.den * other.num)

    def __rtruediv__(self, other):
        return Rat.get(self.num.nvars, other) / self

    def __pow__(self, power):
        return Rat(self.num ** power, self.den ** power)

    def derivative(self, index):
        return Rat(
            self.num.derivative(index) * self.den
            - self.num * self.den.derivative(index),
            self.den * self.den,
        )


def rat_equal(left, right):
    right = Rat.get(left.num.nvars, right)
    return (left.num * right.den - right.num * left.den).is_zero()


def derivative_identity():
    # Variables are z,a,q,v.  Terms constant in z may be omitted from E.
    n = 4
    z, a, q, v = [Poly.var(n, j) for j in range(n)]
    d = Rat(2 * z ** 2, 1 + z)
    Evar = (
        (3 * d - q) ** 2 / 27
        + (3 * d + 6 * z - 4 * q) ** 2 / 54
        + (v * (1 - d) ** 2 - 2 * q * (1 - d)) / 6
        + (1 - d) * (1 - v) / 3
        + Q(2, 3) * (1 - z) * (1 - a)
    )
    left = 9 * (1 + z) ** 3 * Evar.derivative(0)
    expected = (
        (12 * v + 72) * z ** 4
        + (6 * a - 14 * q + 24 * v + 156) * z ** 3
        + (18 * a - 42 * q + 36) * z ** 2
        + (18 * a - 36 * q - 18) * z
        + (6 * a - 8 * q - 6)
    )
    assert rat_equal(left, expected)
    return True


def endpoint_identities():
    # Variables are r,u,v,h.  Substitute q=(3/2)ruv exactly.
    n = 4
    r, u, v, h = [Poly.var(n, j) for j in range(n)]
    q = Q(3, 2) * r * u * v

    def E_at(z, d):
        return (
            q * (h - 5 * q / 9 - q / (3 * v))
            + (3 * d - q) ** 2 / 27
            + (3 * d + 6 * z - 4 * q) ** 2 / 54
            + (v * (1 - d) - q) ** 2 / (6 * v)
            + (1 - d) * (1 - v) / 3
            + Q(2, 3) * (1 - z) * (1 - u * v)
        )

    P = (
        -36 * h * r * u + 12 * r ** 2 * u ** 2 * v
        + 9 * r ** 2 * u ** 2 - 24 * r * u + 16 * u + 4
    )
    M = (
        -324 * h * r * u * v + 108 * r ** 2 * u ** 2 * v ** 2
        + 81 * r ** 2 * u ** 2 * v - 36 * r * u * v
        + 72 * u * v + 32 * v + 24
    )
    slack0 = 1 - q - E_at(Q(0), Q(0))
    slack_half = 1 - q - E_at(Q(1, 2), Q(1, 3))
    assert rat_equal(slack0, Rat(v * P) / 24)
    assert rat_equal(slack_half, Rat(M) / 216)
    return True


def trim(coefficients):
    coefficients = list(coefficients)
    while len(coefficients) > 1 and not coefficients[-1]:
        coefficients.pop()
    return coefficients


def poly_add(a, b):
    n = max(len(a), len(b))
    out = [Q(0)] * n
    for j in range(n):
        out[j] = (a[j] if j < len(a) else 0) + (b[j] if j < len(b) else 0)
    return trim(out)


def poly_mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def poly_divmod(a, b):
    a, b = trim(a), trim(b)
    if len(a) < len(b):
        return [Q(0)], a
    out = [Q(0)] * (len(a) - len(b) + 1)
    while len(a) >= len(b) and any(a):
        shift = len(a) - len(b)
        factor = a[-1] / b[-1]
        out[shift] += factor
        for j in range(len(b)):
            a[shift + j] -= factor * b[j]
        a = trim(a)
    return trim(out), trim(a)


def affine_power_coefficients(coefficients, left, right):
    # Coefficients after x=left+(right-left)y.
    out = [Q(0)]
    width = right - left
    for power, coefficient in enumerate(coefficients):
        term = [Q(0)] * (power + 1)
        for j in range(power + 1):
            term[j] = coefficient * comb(power, j) * left ** (power - j) * width ** j
        out = poly_add(out, term)
    return out


def bernstein_coefficients(coefficients, left, right, degree=None):
    coefficients = trim(coefficients)
    degree = len(coefficients) - 1 if degree is None else degree
    power = affine_power_coefficients(coefficients, left, right)
    power += [Q(0)] * (degree + 1 - len(power))
    answer = []
    for i in range(degree + 1):
        value = Q(0)
        for k in range(i + 1):
            value += power[k] * Q(comb(i, k), comb(degree, k))
        answer.append(value)
    return answer


def asymptotic_bernstein():
    p = [4, 16, -60, 0, 9, 12]
    j = [32, 72, -360, 0, 81, 216]
    m = [24, 32, 72, -360, 0, 81, 108]
    rows = {
        "p": bernstein_coefficients(p, Q(1, 3), Q(7, 16)),
        "j": bernstein_coefficients(j, Q(1, 3), Q(7, 16)),
        "m": bernstein_coefficients(m, Q(1, 3), Q(7, 16)),
    }
    expected = {
        "p": [Q(229,81), Q(64,27), Q(4285,2304), Q(2659,2048),
              Q(135563,196608), Q(9881,262144)],
        "j": [Q(161,9), Q(179,12), Q(2995,256), Q(16949,2048),
              Q(307781,65536), Q(134143,131072)],
        "m": [Q(805,27), Q(8425,288), Q(32855,1152), Q(678385,24576),
              Q(15627965,589824), Q(475484045,18874368),
              Q(99364775,4194304)],
    }
    assert rows == expected
    assert all(value > 0 for row in rows.values() for value in row)
    return rows


def actual_univariate(poly, z_index, values):
    out = {}
    for exponent, coefficient in poly.terms.items():
        value = coefficient
        for index, assigned in values.items():
            value *= assigned ** exponent[index]
        power = exponent[z_index]
        out[power] = out.get(power, Q(0)) + value
    if not out:
        return [Q(0)]
    coefficients = [Q(0)] * (max(out) + 1)
    for power, coefficient in out.items():
        coefficients[power] = coefficient
    return trim(coefficients)


def finite_slack_polynomial(s):
    # Variables r,u,v,h,z, followed by exact rank substitution.
    n = 5
    r, u, v, h, z = [Poly.var(n, j) for j in range(n)]
    q = Q(3, 2) * r * u * v
    d = Rat(2 * z ** 2, 1 + z)
    E = (
        q * (h - 5 * q / 9 - q / (3 * v))
        + (3 * d - q) ** 2 / 27
        + (3 * d + 6 * z - 4 * q) ** 2 / 54
        + (v * (1 - d) - q) ** 2 / (6 * v)
        + (1 - d) * (1 - v) / 3
        + Q(2, 3) * (1 - z) * (1 - u * v)
    )
    T = 18 * v * (1 + z) ** 2 * (1 - q - E)
    values = {
        0: w(s) / w(s + 1),
        1: w(s - 1) / w(s),
        2: w(s - 2) / w(s - 1),
        3: Q(s - 1, s + 1),
    }
    numerator = actual_univariate(T.num, 4, values)
    denominator = actual_univariate(T.den, 4, values)
    quotient, remainder = poly_divmod(numerator, denominator)
    assert all(not x for x in remainder)
    assert len(quotient) <= 5
    quotient += [Q(0)] * (5 - len(quotient))
    return quotient


def finite_bernstein():
    expected_minima = {
        3: Q(359,256),
        4: Q(19957,46875),
        5: Q(3703,12000),
        6: Q(32277779252224,119169245671875),
        7: Q(2556191652291015625,10103662211651076096),
        8: Q(62954407990539769,259405508972981952),
        9: Q(3945228443496793740269971289,
             16717688340480000000000000000),
    }
    rows = {}
    for s in range(3, 10):
        power = finite_slack_polynomial(s)
        bernstein = bernstein_coefficients(power, Q(0), Q(1, 2), degree=4)
        assert all(value > 0 for value in bernstein)
        assert min(bernstein) == expected_minima[s]
        rows[s] = {"power": power, "bernstein": bernstein}
    return rows


def l2_structure_case(s, K):
    B = s - 2
    r = w(s) / w(s + 1)
    u = w(s - 1) / w(s)
    v = w(B) / w(s - 1)
    a = u * v
    q = Q(3, 2) * r * a
    z = Q(1, K + 1)
    d = 2 * z * z / (1 + z)
    expected = {
        (2, B): (q / 3, 2 * z),
        (1, 1, B): (q / 9, 3 * d),
        (1, s - 1): (q / (3 * v), v * (1 - d)),
        (s,): (r, a * (1 - z)),
    }
    observed = {}
    mean = Q(0)
    for comp in compositions(s):
        value = contextual(len(comp), comp[-1], K, K - 1, B)
        if value:
            observed[comp] = (root_mass(comp), value)
            mean += root_mass(comp) * value
    assert observed == expected
    assert mean == q
    path_mass = sum((mass * (len(comp) - 1) for comp, (mass, _) in observed.items()), Q(0))
    assert path_mass == 5 * q / 9 + q / (3 * v)

    env, target, reset_part, descendant_part = l2_envelope(s, K)
    actual_reset = reset_energy(s, K, K - 1, B, False)
    augmented_reset = literal_reset_energy(s, K, K - 1, B, True)
    actual_literal = literal_reset_energy(s, K, K - 1, B, False)
    assert actual_reset == actual_literal
    assert actual_reset <= augmented_reset <= q * reset_part

    descendant = Q(0)
    live = {}
    for mass, child, k, t, jrank in children((s, K, K - 1, B)):
        descendant += mass * resolvent(child, False)
        live.setdefault((k, t), []).append(jrank)
    if s == 3:
        assert live == {(1, 3): [1]}
        boundary_note = "(2,2) is inactive; its envelope charge is zero because v=1"
    else:
        assert live == {(2, s - 1): [1, 2], (1, s): [1]}
        boundary_note = "both nominal descendant groups are live"
    assert descendant <= q * descendant_part
    actual = actual_reset + descendant
    assert actual == resolvent((s, K, K - 1, B), False)
    assert actual <= env <= target
    return {
        "context": (s, K, K - 1, B),
        "actual": actual,
        "envelope": env,
        "target": target,
        "actual_reset": actual_reset,
        "augmented_reset": augmented_reset,
        "descendant": descendant,
        "live_groups": live,
        "boundary_note": boundary_note,
    }


def qrecord(value):
    return {
        "numerator": str(value.n),
        "denominator": str(value.d),
        "decimal": "%.17g" % (value.n / value.d),
    }


def jsonify(value, indent=0):
    pad = " " * indent
    nextpad = " " * (indent + 2)
    if isinstance(value, Q):
        return jsonify(qrecord(value), indent)
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'
    if isinstance(value, tuple):
        value = list(value)
    if isinstance(value, list):
        if not value:
            return "[]"
        return "[\n" + ",\n".join(nextpad + jsonify(x, indent + 2) for x in value) + "\n" + pad + "]"
    if isinstance(value, dict):
        if not value:
            return "{}"
        rows = []
        for key in sorted(value, key=lambda x: str(x)):
            rows.append(nextpad + jsonify(str(key), 0) + ": " + jsonify(value[key], indent + 2))
        return "{\n" + ",\n".join(rows) + "\n" + pad + "}"
    raise TypeError(type(value))


def main():
    # Basin inequality: analytic proof is in the report; these are decisive
    # normalization checks, including equality at the smallest endpoint.
    beta_rows = []
    for A, ell in [(1, 1), (2, 1), (3, 2), (8, 4)]:
        value = beta(A, ell)
        assert value <= ell + 1
        beta_rows.append({"A": A, "ell": ell, "beta": value, "bound": Q(ell + 1)})

    # Fresh attachment is uniform, and selected nonfresh laws retain all j.
    attachment_rows = []
    for K, R, k in [(1, 0, 5), (7, 6, 2), (7, 3, 4)]:
        row = [attachment(K, R, k, j) for j in range(k + 1)]
        assert sum(row, Q(0)) == 1
        if (K, R) == (1, 0):
            assert row == [Q(1, k + 1)] * (k + 1)
        attachment_rows.append({"K": K, "R": R, "k": k, "row": row})

    # Literal versus grouped canonical energy catches every basin/capacity
    # normalization independently at small rank.
    literal_rows = []
    for x in [(3, 1, 0, 1), (4, 2, 1, 2), (5, 4, 2, 3)]:
        grouped = reset_energy(*x, False)
        literal = literal_reset_energy(*x, False)
        assert grouped == literal
        literal_rows.append({"context": x, "energy": grouped})

    # Suffix boundary checks, including the exact s=2 inactivity exception.
    boundary_rows = []
    for x in [(3, 1, 0, 3), (7, 5, 2, 7)]:
        s, K, R, B = x
        actual = resolvent(x, False)
        q = qsplit(s, B)
        env = q * q * Q(s - 1, s + 1)
        target = q * (1 - q)
        assert actual <= env <= target
        boundary_rows.append({"sector": "L0", "context": x, "actual": actual,
                              "envelope": env, "target": target})
    for s, K in [(2, 1), (2, 9), (3, 1), (9, 7)]:
        x = (s, K, K - 1, s - 1)
        actual = resolvent(x, False)
        env, target = l1_envelope(s, K)
        assert actual <= env <= target
        if s == 2:
            assert actual == 0
        boundary_rows.append({"sector": "L1", "context": x, "actual": actual,
                              "envelope": env, "target": target})

    l2_rows = [
        l2_structure_case(3, 1),
        l2_structure_case(3, 7),
        l2_structure_case(4, 2),
        l2_structure_case(9, 7),
        l2_structure_case(10, 7),
    ]

    # Four accepted recurrence calibrations, evaluated from scratch.
    calibrations = []
    for weighted, x in [
        (True, (8, 1, 0, 4)),
        (True, (11, 1, 0, 5)),
        (False, (8, 1, 0, 3)),
        (False, (11, 1, 0, 4)),
    ]:
        value = resolvent(x, weighted)
        q = qsplit(x[0], x[3])
        ratio = value / (q * (1 - q))
        assert ratio < 1
        calibrations.append({"weighted": weighted, "context": x,
                             "value": value, "ratio": ratio})

    assert derivative_identity()
    assert endpoint_identities()
    asymptotic = asymptotic_bernstein()
    finite = finite_bernstein()

    # Exact monotonicity margins used in the two endpoint reductions.
    first_derivative_inner_max = Q(931, 1024)  # 4u^3+3u^2 at u=7/16
    second_derivative_inner_max = Q(833, 256)  # 17u^2 at u=7/16
    assert first_derivative_inner_max < 10
    assert second_derivative_inner_max < 20

    output = {
        "schema": "M114-independent-exact-audit-v1",
        "method": "no imports; custom rational arithmetic; no predecessor read",
        "seed": None,
        "beta_rows": beta_rows,
        "attachment_rows": attachment_rows,
        "literal_grouped_energy_rows": literal_rows,
        "boundary_rows": boundary_rows,
        "l2_structure_rows": l2_rows,
        "frozen_calibration_recomputations": calibrations,
        "derivative_identity": True,
        "endpoint_identities": True,
        "asymptotic_bernstein": asymptotic,
        "finite_bernstein": finite,
        "monotonicity_margins": {
            "first_inner_max": first_derivative_inner_max,
            "first_threshold": Q(10),
            "second_inner_max": second_derivative_inner_max,
            "second_threshold": Q(20),
        },
        "failures": [],
    }
    with open("independent_exact_audit.json", "w", encoding="utf-8") as handle:
        handle.write(jsonify(output) + "\n")
    print("M114 exact audit: PASS")
    for row in calibrations:
        print(row["weighted"], row["context"], qrecord(row["ratio"])["decimal"])
    print("finite Bernstein minima:", [repr(min(finite[s]["bernstein"])) for s in range(3, 10)])


if __name__ == "__main__":
    main()
