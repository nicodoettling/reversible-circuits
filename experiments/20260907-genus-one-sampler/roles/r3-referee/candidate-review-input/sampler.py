"""Exact final-transposition sampler, proof version R1-T1.

Only the Python standard library is used. Permutations are tuples with
compose(p,q)[i]=p[q[i]]; displayed words multiply left to right, so the
rightmost transposition acts first. Random-bit exactness assumes independent
fair bits from rng.getrandbits; random.Random is used only for seeded tests.
"""

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, factorial, prod
import random


def power(n, e):
    return Fraction(n ** e) if e >= 0 else Fraction(1, n ** (-e))


def cycles(p):
    seen, result = set(), []
    for x in range(len(p)):
        if x in seen:
            continue
        cycle, y = [], x
        while y not in seen:
            seen.add(y)
            cycle.append(y)
            y = p[y]
        result.append(tuple(cycle))
    return tuple(result)


def right_swap(p, edge):
    q = list(p)
    x, y = edge
    q[x], q[y] = q[y], q[x]
    return tuple(q)


def evaluate(n, word):
    p = tuple(range(n))
    for edge in word:
        p = right_swap(p, edge)
    return p


def components(n, word):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for x, y in word:
        parent[find(x)] = find(y)
    groups = {}
    for x in range(n):
        groups.setdefault(find(x), []).append(x)
    return tuple(sorted(tuple(c) for c in groups.values()))


def marked_symmetric(alpha):
    e, s = [1], [0]
    for a in alpha:
        old_e, old_s = e, s
        e, s = old_e + [0], old_s + [0]
        for j in range(1, len(e)):
            e[j] += a * old_e[j - 1]
            s[j] += a * old_s[j - 1] + a * a * old_e[j - 1]
    return e, s


def normalized_count(alpha, genus):
    alpha = tuple(alpha)
    if not alpha or genus not in (0, 1):
        return Fraction(0)
    n, k = sum(alpha), len(alpha)
    common = prod(Fraction(a ** a, factorial(a - 1)) for a in alpha)
    if genus == 0:
        return common * power(n, k - 3)
    _, s = marked_symmetric(alpha)
    q = sum(a * (a - 1) for a in alpha)
    positive = power(n, k - 2) * q
    for j in range(2, k + 1):
        positive += factorial(j - 1) * power(n, k - 1 - j) * s[j]
    return common * positive / 24


@lru_cache(maxsize=8192)
def count(alpha, genus):
    if genus not in (0, 1):
        return 0
    r = sum(alpha) + len(alpha) - 2 + 2 * genus
    z = factorial(r) * normalized_count(alpha, genus)
    assert z.denominator == 1 and z >= 0, (alpha, genus, z)
    return z.numerator


def count_signed(alpha, genus):
    """Separate Corollary 1.5 calculation for exact normalization checks."""
    n, k = sum(alpha), len(alpha)
    r = n + k - 2 + 2 * genus
    common = prod(Fraction(a ** a, factorial(a - 1)) for a in alpha)
    if genus == 0:
        z = factorial(r) * common * power(n, k - 3)
    else:
        e = [1]
        for a in alpha:
            e.append(0)
            for j in range(len(e) - 1, 0, -1):
                e[j] += a * e[j - 1]
        bracket = Fraction(n * n - n)
        for j in range(2, k + 1):
            bracket -= power(n, 2 - j) * factorial(j - 2) * e[j]
        z = factorial(r) * common * power(n, k - 2) * bracket / 24
    assert z.denominator == 1 and z >= 0
    return z.numerator


def allocation_table(lengths, forced, tracked_side=0):
    """Positive DP; values are (E list, S list, Q sum), E[0]=M.

    forced maps individual cycle indices to 0 (A) or 1 (B). Equal-size
    cycles remain distinct choices. No cycle subsets are enumerated.
    """
    table = {(0, 0): ([1], [0], 0)}
    for i, a in enumerate(lengths):
        next_table = {}
        choices = (forced[i],) if i in forced else (0, 1)
        for (size, number), (e, s, q) in table.items():
            for side in choices:
                if side == tracked_side:
                    key = (size + a, number + 1)
                    ne, ns = e + [0], s + [0]
                    for j in range(1, len(ne)):
                        ne[j] += a * e[j - 1]
                        ns[j] += a * s[j - 1] + a * a * e[j - 1]
                    nq = q + a * (a - 1) * e[0]
                else:
                    key, ne, ns, nq = (size, number), list(e), list(s), q
                if key not in next_table:
                    next_table[key] = (ne, ns, nq)
                else:
                    ee, ss, qq = next_table[key]
                    for j in range(len(ne)):
                        ee[j] += ne[j]
                        ss[j] += ns[j]
                    next_table[key] = (ee, ss, qq + nq)
        table = next_table
    return table


def allocation_mass(lengths, ga, gb, forced=None):
    """Integer number of disconnected predecessors for allowed allocations."""
    assert ga >= 0 and gb >= 0 and ga + gb <= 1
    forced = {0: 0, 1: 1} if forced is None else dict(forced)
    assert forced.get(0) == 0 and forced.get(1) == 1
    n, k = sum(lengths), len(lengths)
    length = n + k - 4 + 2 * (ga + gb)
    common = factorial(length) * prod(
        Fraction(a ** a, factorial(a - 1)) for a in lengths
    )
    tracked = 1 if gb == 1 else 0
    table = allocation_table(lengths, forced, tracked)
    z = Fraction(0)
    for (size, number), (e, s, q) in table.items():
        other_size, other_number = n - size, k - number
        assert size > 0 and other_size > 0
        if ga + gb == 0:
            term = e[0] * power(size, number - 3)
        else:
            term = q * power(size, number - 2)
            for j in range(2, number + 1):
                term += factorial(j - 1) * power(size, number - 1 - j) * s[j]
            term /= 24
        z += term * power(other_size, other_number - 3)
    result = common * z
    assert result.denominator == 1 and result >= 0, (lengths, ga, gb, forced, result)
    return result.numerator


def assignment_weight(lengths, ga, gb, assignment):
    """Direct branch count (2), used by the audit independently of the DP."""
    a = tuple(x for x, side in zip(lengths, assignment) if side == 0)
    b = tuple(x for x, side in zip(lengths, assignment) if side == 1)
    la = sum(a) + len(a) - 2 + 2 * ga
    lb = sum(b) + len(b) - 2 + 2 * gb
    return comb(la + lb, la) * count(a, ga) * count(b, gb)


@dataclass(frozen=True)
class Branch:
    edge: tuple
    endpoint: tuple
    kind: str
    child_genus: int
    ga: int
    gb: int
    cut_cycles: tuple
    weight: int


@lru_cache(maxsize=256)
def branches(p, genus):
    n = len(p)
    initial_cycles = cycles(p)
    cycle_index = {x: i for i, c in enumerate(initial_cycles) for x in c}
    result = []
    for x, y in combinations(range(n), 2):
        edge = (x, y)
        q = right_swap(p, edge)
        cut = cycles(q)
        alpha = tuple(len(c) for c in cut)
        if cycle_index[x] != cycle_index[y]:
            weight = count(alpha, genus)
            if weight:
                result.append(Branch(edge, q, "connected", genus, -1, -1, (), weight))
        else:
            if genus == 1:
                weight = count(alpha, 0)
                if weight:
                    result.append(Branch(edge, q, "connected", 0, -1, -1, (), weight))
            cx = next(c for c in cut if x in c)
            cy = next(c for c in cut if y in c)
            assert cx != cy
            ordered = (cx, cy) + tuple(c for c in cut if c != cx and c != cy)
            lengths = tuple(len(c) for c in ordered)
            for ga in range(genus + 1):
                gb = genus - ga
                weight = allocation_mass(lengths, ga, gb)
                if weight:
                    result.append(Branch(edge, q, "split", -1, ga, gb, ordered, weight))
    expected = count(tuple(len(c) for c in initial_cycles), genus)
    assert sum(b.weight for b in result) == expected, (p, genus, result, expected)
    return tuple(result)


def randbelow(rng, bound):
    assert bound > 0
    bits = (bound - 1).bit_length()
    while True:
        value = rng.getrandbits(bits)
        if value < bound:
            return value


def weighted_choice(rng, values, weights):
    value = randbelow(rng, sum(weights))
    for item, weight in zip(values, weights):
        if value < weight:
            return item
        value -= weight
    raise AssertionError("invalid weight total")


def sample_assignment(lengths, ga, gb, rng):
    forced = {0: 0, 1: 1}
    total = allocation_mass(lengths, ga, gb, forced)
    assert total > 0
    for i in range(2, len(lengths)):
        wa = allocation_mass(lengths, ga, gb, forced | {i: 0})
        wb = allocation_mass(lengths, ga, gb, forced | {i: 1})
        assert wa + wb == total
        side = weighted_choice(rng, (0, 1), (wa, wb))
        forced[i] = side
        total = (wa, wb)[side]
    return tuple(forced[i] for i in range(len(lengths)))


def restrict(p, labels):
    index = {x: i for i, x in enumerate(labels)}
    return tuple(index[p[x]] for x in labels)


def unrank_subset(n, k, rank):
    assert 0 <= rank < comb(n, k)
    result = []
    for i in range(n):
        if k == 0:
            break
        including = comb(n - i - 1, k - 1)
        if rank < including:
            result.append(i)
            k -= 1
        else:
            rank -= including
    assert k == 0 and rank == 0
    return tuple(result)


def interleave(a, b, positions):
    aset, ai, bi, result = set(positions), 0, 0, []
    for i in range(len(a) + len(b)):
        if i in aset:
            result.append(a[ai])
            ai += 1
        else:
            result.append(b[bi])
            bi += 1
    assert ai == len(a) and bi == len(b)
    return tuple(result)


def sample(p, genus, rng=None):
    rng = random.SystemRandom() if rng is None else rng
    assert genus in (0, 1) and count(tuple(len(c) for c in cycles(p)), genus) > 0
    # An explicit continuation stack avoids Python's interpreter recursion cap.
    # `values` contains completed child words in the order they were requested.
    tasks, values = [("sample", p, genus)], []
    while tasks:
        task = tasks.pop()
        if task[0] == "append":
            values.append(values.pop() + (task[1],))
            continue
        if task[0] == "merge":
            _, aa, bb, edge = task
            b, a = values.pop(), values.pop()
            a = tuple(tuple(sorted((aa[x], aa[y]))) for x, y in a)
            b = tuple(tuple(sorted((bb[x], bb[y]))) for x, y in b)
            positions = unrank_subset(len(a) + len(b), len(a), randbelow(rng, comb(len(a) + len(b), len(a))))
            values.append(interleave(a, b, positions) + (edge,))
            continue
        _, endpoint, child_genus = task
        if len(endpoint) == 1 and child_genus == 0:
            values.append(())
            continue
        choices = branches(endpoint, child_genus)
        branch = weighted_choice(rng, choices, tuple(b.weight for b in choices))
        if branch.kind == "connected":
            tasks.append(("append", branch.edge))
            tasks.append(("sample", branch.endpoint, branch.child_genus))
        else:
            lengths = tuple(len(c) for c in branch.cut_cycles)
            assignment = sample_assignment(lengths, branch.ga, branch.gb, rng)
            aa = tuple(sorted(x for c, side in zip(branch.cut_cycles, assignment) if side == 0 for x in c))
            bb = tuple(sorted(x for c, side in zip(branch.cut_cycles, assignment) if side == 1 for x in c))
            tasks.append(("merge", aa, bb, branch.edge))
            tasks.append(("sample", restrict(branch.endpoint, bb), branch.gb))
            tasks.append(("sample", restrict(branch.endpoint, aa), branch.ga))
    assert len(values) == 1
    return values[0]


def sample_identity(n, rng=None):
    if n < 2:
        raise ValueError("X_N requires N>=2; X_1 is empty")
    return sample(tuple(range(n)), 1, rng)
