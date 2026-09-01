#!/usr/bin/env python3
"""Compact exact coefficient diagnostics for M226 WBE.

This is a formula checker, not a proof.  It is deliberately capped at odd
k<=15 and uses no random sampling.
"""

from fractions import Fraction
from itertools import combinations
from math import factorial, sqrt


def b(d: int) -> Fraction:
    return Fraction(d ** (d - 1), factorial(d))


def kernel(k: int, r: int, d: int) -> Fraction:
    return b(d) * b(r - d) / ((2 * k - 3) * b(r))


def h(k: int, r: int) -> Fraction:
    return Fraction((r - 1) * (r - 2), r * (2 * k - 3))


def qsplit(k: int, s: int) -> Fraction:
    return Fraction(k, k - 1) * b(s) * b(k - s) / b(k)


def f_atom(k: int, x: int, y: int) -> Fraction:
    """Coefficient of 1{y<=ell} in the two-seam incidence F_ell(x)."""
    D, n = 2 * k - 1, 3 * k
    if x < k:
        atoms = ((x, D - 2 * x), (x + 1, x), (x + k, x))
    else:
        c = D - x
        atoms = ((n - c, D - 2 * c), (n - c - 1, c), (n - c - k, c))
    return Fraction(sum(mult for size, mult in atoms if size == y), D)


def j_atom(k: int, x: int, y: int) -> Fraction:
    return Fraction(k - x, k) if x == y else Fraction()


def w_atom(k: int, r: int, y: int, side: str) -> Fraction:
    atom = f_atom if side == "B" else j_atom
    return sum(
        (r - d - 1) * kernel(k, r, d) * atom(k, d, y)
        for d in range(1, r)
    )


def y_coefficient(k: int, y: int) -> tuple[Fraction, Fraction, Fraction]:
    """Return (surviving, fragmentation, total) coefficient at size y."""
    D = 2 * k - 1
    surv = Fraction()
    frag = Fraction()
    for s in range(1, (k - 1) // 2 + 1):
        q = qsplit(k, s)
        b_surv = h(k, s) * f_atom(k, D - s, y) + h(k, D - s) * f_atom(k, s, y)
        a_surv = (
            h(k, s) * j_atom(k, k - s, y)
            + h(k, k - s) * j_atom(k, s, y)
            + Fraction(k - 1, 2 * k - 3)
            * (j_atom(k, s, y) + j_atom(k, k - s, y))
        )
        b_frag = w_atom(k, s, y, "B") + w_atom(k, D - s, y, "B")
        c_atom = (k - y) * kernel(k, k, y) if 1 <= y < k else Fraction()
        a_frag = w_atom(k, s, y, "A") + w_atom(k, k - s, y, "A") + c_atom
        surv += q * (b_surv - a_surv)
        frag += q * (b_frag - a_frag)
    return surv, frag, surv + frag


def g_b(k: int, x: int) -> Fraction:
    """q-averaged coefficient multiplying F_ell(x) in the raw B numerator."""
    D = 2 * k - 1
    j = (k - 1) // 2
    ans = qsplit(k, x) * h(k, D - x) if 1 <= x <= j else Fraction()
    ans += sum(
        qsplit(k, s) * (s - x - 1) * kernel(k, s, x)
        for s in range(x + 1, j + 1)
    )
    ans += sum(
        qsplit(k, s) * (D - s - x - 1) * kernel(k, D - s, x)
        for s in range(1, j + 1)
    )
    return ans


def a_y_atom_closed(k: int, y: int) -> Fraction:
    if not 1 <= y < k:
        return Fraction()
    m = k - y
    return (
        2 * b(y) * b(m)
        * (m + Fraction((m - 1) * (m - 2), k - 1))
        / ((2 * k - 3) * b(k))
    )


def b_y_atom_closed(k: int, y: int) -> Fraction:
    D = 2 * k - 1
    if 1 <= y < k:
        return (
            Fraction(D - 2 * y, D) * g_b(k, y)
            + Fraction(y - 1, D) * g_b(k, y - 1)
        )
    if y == k:
        return Fraction(k - 1, D) * g_b(k, k - 1)
    if k < y <= (3 * k - 1) // 2:
        return (
            Fraction(2 * k - y, D) * g_b(k, y - 1)
            + Fraction(y - k, D) * g_b(k, y - k)
        )
    return Fraction()


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    ans = [0] * len(p)
    for x, y in enumerate(p):
        ans[y] = x
    return tuple(ans)


def cycle_perm(n: int, entries: tuple[int, ...]) -> tuple[int, ...]:
    ans = list(range(n))
    for x, y in zip(entries, entries[1:] + entries[:1]):
        ans[x] = y
    return tuple(ans)


def transposition(n: int, x: int, y: int) -> tuple[int, ...]:
    ans = list(range(n))
    ans[x], ans[y] = ans[y], ans[x]
    return tuple(ans)


def cycles(p: tuple[int, ...]) -> list[tuple[int, ...]]:
    seen: set[int] = set()
    out = []
    for start in range(len(p)):
        if start in seen:
            continue
        part = []
        x = start
        while x not in seen:
            seen.add(x)
            part.append(x)
            x = p[x]
        out.append(tuple(part))
    return out


def internal_edges(p: tuple[int, ...]) -> list[tuple[int, ...]]:
    return [
        transposition(len(p), x, y)
        for part in cycles(p)
        for x, y in combinations(part, 2)
    ]


def edge_vertices(e: tuple[int, ...]) -> tuple[int, int]:
    moved = [x for x in range(len(e)) if e[x] != x]
    return moved[0], moved[1]


def source(k: int, side: str):
    n = 3 * k
    if side == "B":
        part = tuple(range(1, k)) + tuple(range(2 * k, 3 * k))
        return cycle_perm(n, part), [part]
    lower = tuple(range(k))
    upper = tuple(range(2 * k, 3 * k))
    return compose(cycle_perm(n, lower), cycle_perm(n, upper)), [lower, upper]


def split_size(e: tuple[int, ...], original: list[tuple[int, ...]]) -> int:
    x, y = edge_vertices(e)
    part = next(c for c in original if x in c)
    ix, iy = part.index(x), part.index(y)
    gap = (iy - ix) % len(part)
    return min(gap, len(part) - gap)


def ambient_runs(component: tuple[int, ...], n: int) -> int:
    support = set(component)
    return sum(1 for x in support if (x - 1) % n not in support)


def raw_atom_profiles(k: int, side: str):
    """Literal raw disjoint numerators by first split and (run,size)."""
    n = 3 * k
    target = cycle_perm(n, tuple(range(n)))
    src, original = source(k, side)
    candidates = {s: [] for s in range(1, (k - 1) // 2 + 1)}
    for e in internal_edges(src):
        s = split_size(e, original)
        if s in candidates:
            candidates[s].append(e)
    out = {}
    for s, first_edges in candidates.items():
        raw: dict[tuple[int, int], Fraction] = {}
        for e in first_edges:
            after_first = compose(e, src)
            first_vertices = set(edge_vertices(e))
            for f in internal_edges(after_first):
                if first_vertices & set(edge_vertices(f)):
                    continue
                parent = next(
                    part for part in cycles(after_first)
                    if set(edge_vertices(f)).issubset(part)
                )
                after_second = compose(f, after_first)
                children = [
                    part for part in cycles(after_second)
                    if set(part).issubset(parent)
                ]
                weight = kernel(k, len(parent), len(children[0]))
                residual = compose(inverse(compose(e, f)), target)
                faces = cycles(residual)
                assert len(faces) == 3
                for face in faces:
                    key = (ambient_runs(face, n), len(face))
                    raw[key] = raw.get(key, Fraction()) + weight
        out[s] = {key: value / len(first_edges) for key, value in raw.items()}
    return out


def literal_wbe_coefficients(k: int, observable: str):
    bprof = raw_atom_profiles(k, "B")
    aprof = raw_atom_profiles(k, "A")
    max_ell = (3 * k - 1) // 2
    coeffs = {}
    for y in range(2, max_ell + 1):
        value = Fraction()
        for s in range(1, (k - 1) // 2 + 1):
            if observable == "Y":
                b_atom = bprof[s].get((1, y), Fraction())
                a_atom = aprof[s].get((1, y), Fraction())
            else:
                b_atom = sum(v for (run, size), v in bprof[s].items() if size == y)
                a_atom = sum(v for (run, size), v in aprof[s].items() if size == y)
            value += qsplit(k, s) * (b_atom - a_atom)
        coeffs[y] = value
    return coeffs


def run_literal(k: int) -> None:
    bprof = raw_atom_profiles(k, "B")
    aprof = raw_atom_profiles(k, "A")
    all_coeffs = {}
    for observable in ("Y", "X"):
        max_ell = (3 * k - 1) // 2
        coeffs = {}
        for y in range(2, max_ell + 1):
            value = Fraction()
            for s in range(1, (k - 1) // 2 + 1):
                if observable == "Y":
                    b_atom = bprof[s].get((1, y), Fraction())
                    a_atom = aprof[s].get((1, y), Fraction())
                else:
                    b_atom = sum(v for (run, size), v in bprof[s].items() if size == y)
                    a_atom = sum(v for (run, size), v in aprof[s].items() if size == y)
                value += qsplit(k, s) * (b_atom - a_atom)
            coeffs[y] = value
        all_coeffs[observable] = coeffs
        prefix = Fraction()
        best = (0.0, 0, Fraction())
        signs = []
        for y, atom in coeffs.items():
            prefix += atom
            ratio = k * abs(float(prefix)) / sqrt(y)
            if ratio > best[0]:
                best = ratio, y, prefix
            signs.append("+" if atom > 0 else "-" if atom < 0 else "0")
        print("literal", observable, "k", k, "max-prefix", *best, "signs", "".join(signs))
        if observable == "Y":
            for y, atom in coeffs.items():
                assert atom == y_coefficient(k, y)[2]
    for side, profiles in (("B", bprof), ("A", aprof)):
        prefix = Fraction()
        best = (0.0, 0, Fraction())
        for y in range(2, (3 * k - 1) // 2 + 1):
            atom = sum(
                qsplit(k, s) * profiles[s].get((2, y), Fraction())
                for s in range(1, (k - 1) // 2 + 1)
            )
            prefix += atom
            ratio = k * float(prefix) / sqrt(y)
            if ratio > best[0]:
                best = ratio, y, prefix
        print("two-run", side, "k", k, "max-mass", *best)
    for y in all_coeffs["X"]:
        assert all_coeffs["X"][y] - all_coeffs["Y"][y] == sum(
            qsplit(k, s)
            * (bprof[s].get((2, y), Fraction()) - aprof[s].get((2, y), Fraction()))
            for s in range(1, (k - 1) // 2 + 1)
        )


def two_run_placement_bound(k: int) -> None:
    """Falsify count <=4 min(ell,a) per fixed first edge/parent/split."""
    n = 3 * k
    target = cycle_perm(n, tuple(range(n)))
    worst = (0.0, None)
    for side in ("B", "A"):
        src, original = source(k, side)
        for e in internal_edges(src):
            s = split_size(e, original)
            if s > (k - 1) // 2:
                continue
            after_first = compose(e, src)
            first_vertices = set(edge_vertices(e))
            records = []
            for f in internal_edges(after_first):
                if first_vertices & set(edge_vertices(f)):
                    continue
                parent = next(part for part in cycles(after_first)
                              if set(edge_vertices(f)).issubset(part))
                after_second = compose(f, after_first)
                children = [part for part in cycles(after_second)
                            if set(part).issubset(parent)]
                a = min(map(len, children))
                faces = cycles(compose(inverse(compose(e, f)), target))
                two = next(len(face) for face in faces if ambient_runs(face, n) == 2)
                records.append((tuple(sorted(parent)), a, two))
            max_ell = (3 * k - 1) // 2
            for ell in range(2, max_ell + 1):
                groups = {}
                for parent, a, two in records:
                    if two <= ell:
                        groups[(parent, a)] = groups.get((parent, a), 0) + 1
                for (parent, a), count in groups.items():
                    ratio = count / min(ell, a)
                    if ratio > worst[0]:
                        worst = ratio, (side, s, len(parent), a, ell, count)
    print("two-run-placement k", k, "worst", worst)
    if k == 5:
        assert worst == (5.0, ("B", 2, 7, 1, 7, 5))


def run(k: int) -> None:
    max_ell = (3 * k - 1) // 2
    coefficients = {y: y_coefficient(k, y) for y in range(2, max_ell + 1)}
    for y, (_, _, atom) in coefficients.items():
        assert atom == b_y_atom_closed(k, y) - a_y_atom_closed(k, y)
    prefix = Fraction()
    max_scaled = (0.0, 0, Fraction())
    max_atom = (0.0, 0, Fraction())
    signs = []
    for y in range(2, max_ell + 1):
        surv, frag, atom = coefficients[y]
        prefix += atom
        scaled = k * abs(float(prefix)) / sqrt(y)
        if scaled > max_scaled[0]:
            max_scaled = (scaled, y, prefix)
        atom_scaled = k * sqrt(y) * abs(float(atom))
        if atom_scaled > max_atom[0]:
            max_atom = (atom_scaled, y, atom)
        signs.append("+" if atom > 0 else "-" if atom < 0 else "0")
    print(
        "k", k,
        "max-prefix", max_scaled[0], max_scaled[1], str(max_scaled[2]),
        "max-atom", max_atom[0], max_atom[1], str(max_atom[2]),
        "signs", "".join(signs),
    )
    for y in range(2, min(max_ell, 8) + 1):
        surv, frag, atom = coefficients[y]
        print("  y", y, "S", surv, "K", frag, "sum", atom)


if __name__ == "__main__":
    for K in (3, 5, 7, 9, 11, 13, 15):
        run(K)
    for K in (3, 5, 7):
        run_literal(K)
        two_run_placement_bound(K)
