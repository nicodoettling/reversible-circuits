#!/usr/bin/env python3
"""Clean-room exact M217 formula check at k=3,5.

There are deliberately no imports.  Rational arithmetic and JSON rendering
are implemented locally; no M217 code or data is loaded.
"""


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def Q(n, d=1):
    if d == 0:
        raise ZeroDivisionError
    if d < 0:
        n, d = -n, -d
    g = gcd(n, d)
    return (n // g, d // g)


def add(x, y):
    return Q(x[0] * y[1] + y[0] * x[1], x[1] * y[1])


def sub(x, y):
    return Q(x[0] * y[1] - y[0] * x[1], x[1] * y[1])


def mul(x, y):
    return Q(x[0] * y[0], x[1] * y[1])


def div(x, y):
    return Q(x[0] * y[1], x[1] * y[0])


def total(xs):
    out = Q(0)
    for x in xs:
        out = add(out, x)
    return out


def qstr(x):
    return str(x[0]) if x[1] == 1 else str(x[0]) + "/" + str(x[1])


def factorial(n):
    out = 1
    for j in range(2, n + 1):
        out *= j
    return out


def b(d):
    # e^{-d} cancels in every same-total ratio used below.
    return Q(d ** (d - 1), factorial(d))


def h(k, r):
    return Q((r - 1) * (r - 2), r * (2 * k - 3))


def gamma(k, side, s):
    other = 2 * k - 1 - s if side == "L" else k - s
    bracket = sub(sub(Q(2), Q(1, s)), Q(1, other))
    return mul(Q(2, 2 * k - 3), bracket)


def qsplit(k, s):
    return mul(Q(k, k - 1), div(mul(b(s), b(k - s)), b(k)))


def kernel(k, r, d):
    return div(mul(b(d), b(r - d)), mul(Q(2 * k - 3), b(r)))


def F(k, ell, x):
    D, n = 2 * k - 1, 3 * k
    if x < k:
        atoms = ((x, D - 2 * x), (x + 1, x), (x + k, x))
    else:
        c = D - x
        atoms = ((n - c, D - 2 * c), (n - c - 1, c), (n - c - k, c))
    return Q(sum(mult for size, mult in atoms if 2 <= size <= ell), D)


def J(k, ell, x):
    return Q(k - x, k) if 2 <= x <= ell else Q(0)


def W(k, r, value):
    return total(
        mul(Q(r - d - 1), mul(kernel(k, r, d), value(d)))
        for d in range(1, r)
    )


def y_blocks(k, s, ell):
    D = 2 * k - 1
    bs = add(mul(h(k, s), F(k, ell, D - s)),
             mul(h(k, D - s), F(k, ell, s)))
    bk = add(W(k, s, lambda d: F(k, ell, d)),
             W(k, D - s, lambda d: F(k, ell, d)))
    untouched_surv = mul(Q(k - 1, 2 * k - 3),
                         add(J(k, ell, s), J(k, ell, k - s)))
    ass = total((mul(h(k, s), J(k, ell, k - s)),
                 mul(h(k, k - s), J(k, ell, s)),
                 untouched_surv))
    c_ell = total(
        mul(Q(k - d), kernel(k, k, d))
        for d in range(2, min(ell, k - 1) + 1)
    )
    ak = total((W(k, s, lambda d: J(k, ell, d)),
                W(k, k - s, lambda d: J(k, ell, d)), c_ell))
    return bs, bk, ass, ak


def check_k(k):
    D, R = 2 * k - 1, 2 * k - 3
    ss = range(1, (k - 1) // 2 + 1)
    identities = []
    qweights = []
    qhats = []
    for s in ss:
        q = qsplit(k, s)
        aL = sub(Q(1), gamma(k, "L", s))
        aF = sub(Q(1), gamma(k, "F", s))
        qhat = mul(q, aF)
        exact_ratio = div(Q(2 * (k - 1)),
                          mul(mul(Q(R * (k - s) * (D - s)), aL), Q(1)))
        identities.extend((
            aL == add(h(k, s), h(k, D - s)),
            aF == total((h(k, s), h(k, k - s), Q(k - 1, R))),
            sub(div(aF, aL), Q(1)) == exact_ratio,
            qhat == mul(qsplit(k, s), sub(Q(1), gamma(k, "F", s))),
        ))
        qweights.append(q)
        qhats.append(qhat)

    rows = []
    for ell in range(2, (3 * k - 1) // 2 + 1):
        direct_terms = []
        cancel_terms = []
        s_terms, kernel_terms, normalizer_terms = [], [], []
        for s in ss:
            q = qsplit(k, s)
            aL = sub(Q(1), gamma(k, "L", s))
            aF = sub(Q(1), gamma(k, "F", s))
            qhat = mul(q, aF)
            bs, bk, ass, ak = y_blocks(k, s, ell)
            B, A = add(bs, bk), add(ass, ak)
            direct_terms.append(mul(qhat, sub(div(B, aL), div(A, aF))))
            cancel_terms.append(mul(q, sub(mul(div(aF, aL), B), A)))
            s_terms.append(mul(q, sub(bs, ass)))
            kernel_terms.append(mul(q, sub(bk, ak)))
            normalizer_terms.append(mul(q, mul(sub(div(aF, aL), Q(1)), B)))
        direct = total(direct_terms)
        cancelled = total(cancel_terms)
        decomposed = total((total(s_terms), total(kernel_terms),
                            total(normalizer_terms)))
        identities.extend((direct == cancelled, direct == decomposed))
        rows.append((ell, qstr(direct)))

    return {
        "k": k,
        "sum_q": qstr(total(qweights)),
        "sum_qhat": qstr(total(qhats)),
        "all_exact_identities": all(identities),
        "Y_DE_by_l": rows,
    }


def render_row(row):
    vals = ",".join("[" + str(ell) + ",\"" + value + "\"]"
                    for ell, value in row["Y_DE_by_l"])
    return ("{\"k\":" + str(row["k"]) +
            ",\"sum_q\":\"" + row["sum_q"] + "\"" +
            ",\"sum_qhat\":\"" + row["sum_qhat"] + "\"" +
            ",\"all_exact_identities\":" +
            ("true" if row["all_exact_identities"] else "false") +
            ",\"Y_DE_by_l\":[" + vals + "]}")


rows = [check_k(3), check_k(5)]
ok = all(row["all_exact_identities"] for row in rows)
print("{\"mission\":\"M222\",\"method\":\"clean-room no-import exact rational formulas\","
      "\"parameters\":{\"k\":[3,5],\"seed\":null},"
      "\"imports\":false,\"universal_inference\":false,"
      "\"all_checks_pass\":" + ("true" if ok else "false") +
      ",\"results\":[" + ",".join(render_row(row) for row in rows) + "]}")
