"""Exact final-transposition sampler, candidate proof version R1-T2.v1.

Adapted from the audited 20260907 R1-T1 implementation; new positive marker
count/allocation logic covers g<=2. The current extension is PROVISIONAL.

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


# Positive marker specifications: (special weight names, mode, scalar, divisor).
# Each special slot is labeled, including repeated slot weight names.
SPECS = {
    0: (((), "g0", 1, 1),),
    1: ((("q",), "g1q", 1, 24), (("b",), "g1s", 1, 24)),
    2: ((("a",), "g2e2", 1, 5760),
        (("b", "c"), "g2e3", 1, 5760),
        (("b", "b", "b"), "g2e4", 28, 5760)),
}


def special_weight(name, a):
    if name == "q":
        return a * (a - 1)
    if name == "a":
        return a * a * (a - 1) * (5 * a - 7)
    if name == "b":
        return a * a
    if name == "c":
        return a * a * (29 * a - 25)
    raise ValueError(name)


def ordinary_allowed(spec):
    return spec[1] not in ("g0", "g1q")


def coefficient(spec, size, number, j):
    """Scalar multiplying one completed marker coefficient, excluding q-product."""
    special, mode, scalar, divisor = spec
    if size < 1 or number < 1:
        return Fraction(0)
    if mode == "g0":
        return power(size, number - 3) if j == 0 else Fraction(0)
    if mode == "g1q":
        return power(size, number - 2) / 24 if j == 0 else Fraction(0)
    if mode == "g1s":
        if j < 1 or j > number - 1:
            return Fraction(0)
        return factorial(j) * power(size, number - 2 - j) / 24
    d = len(special)
    if j > number - d:
        return Fraction(0)
    e = int(mode[-1])
    rising = factorial(e + j - 1) // factorial(e - 1)
    return Fraction(scalar * rising * size ** (number - d - j), divisor)


def marker_steps(spec, a, j, mask):
    """Nonnegative transitions for one cycle allocated to this side."""
    yield j, mask, 1
    if ordinary_allowed(spec):
        yield j + 1, mask, a
    for slot, name in enumerate(spec[0]):
        bit = 1 << slot
        if not mask & bit:
            weight = special_weight(name, a)
            if weight:
                yield j, mask | bit, weight


def marker_table(lengths, spec):
    table = {(0, 0): 1}
    for a in lengths:
        nxt = {}
        for (j, mask), value in table.items():
            for nj, nm, factor in marker_steps(spec, a, j, mask):
                key = (nj, nm)
                nxt[key] = nxt.get(key, 0) + value * factor
        table = nxt
    return table


def normalized_count(alpha, genus):
    alpha = tuple(alpha)
    if not alpha or genus not in SPECS or any(a < 1 for a in alpha):
        return Fraction(0)
    n, k = sum(alpha), len(alpha)
    common = prod(Fraction(a ** a, factorial(a - 1)) for a in alpha)
    total = Fraction(0)
    for spec in SPECS[genus]:
        full = (1 << len(spec[0])) - 1
        for (j, mask), value in marker_table(alpha, spec).items():
            if mask == full:
                total += value * coefficient(spec, n, k, j)
    return common * total


@lru_cache(maxsize=8192)
def count(alpha, genus):
    if not alpha or genus not in SPECS:
        return 0
    r = sum(alpha) + len(alpha) - 2 + 2 * genus
    z = factorial(r) * normalized_count(alpha, genus)
    assert z.denominator == 1 and z >= 0, (alpha, genus, z)
    return z.numerator


def allocation_table(lengths, forced, spec_a, spec_b):
    """Tensor marker DP, no enumeration of cycle subsets or endpoint types.

    Keys are (A-size,A-cycle-count,jA,maskA,jB,maskB). Distinct cycle
    indices are processed separately even when their lengths agree.
    """
    table = {(0, 0, 0, 0, 0, 0): 1}
    for i, a in enumerate(lengths):
        nxt = {}
        choices = (forced[i],) if i in forced else (0, 1)
        for (size, number, ja, ma, jb, mb), value in table.items():
            for side in choices:
                if side == 0:
                    for nj, nm, factor in marker_steps(spec_a, a, ja, ma):
                        key = (size + a, number + 1, nj, nm, jb, mb)
                        nxt[key] = nxt.get(key, 0) + value * factor
                else:
                    for nj, nm, factor in marker_steps(spec_b, a, jb, mb):
                        key = (size, number, ja, ma, nj, nm)
                        nxt[key] = nxt.get(key, 0) + value * factor
        table = nxt
    return table


def allocation_mass(lengths, ga, gb, forced=None):
    assert ga >= 0 and gb >= 0 and ga + gb <= 2
    forced = {0: 0, 1: 1} if forced is None else dict(forced)
    assert forced.get(0) == 0 and forced.get(1) == 1
    assert set(forced) <= set(range(len(lengths)))
    assert all(side in (0, 1) for side in forced.values())
    n, k = sum(lengths), len(lengths)
    length = n + k - 4 + 2 * (ga + gb)
    common = factorial(length) * prod(Fraction(a ** a, factorial(a - 1)) for a in lengths)
    total = Fraction(0)
    for sa in SPECS[ga]:
        fa = (1 << len(sa[0])) - 1
        for sb in SPECS[gb]:
            fb = (1 << len(sb[0])) - 1
            table = allocation_table(lengths, forced, sa, sb)
            for (size, number, ja, ma, jb, mb), value in table.items():
                if ma == fa and mb == fb:
                    total += value * coefficient(sa, size, number, ja) * coefficient(sb, n-size, k-number, jb)
    z = common * total
    assert z.denominator == 1 and z >= 0, (lengths, ga, gb, forced, z)
    return z.numerator


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
            if genus >= 1:
                weight = count(alpha, genus - 1)
                if weight:
                    result.append(Branch(edge, q, "connected", genus - 1, -1, -1, (), weight))
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
    if genus not in (0, 1, 2) or not p or sorted(p) != list(range(len(p))):
        raise ValueError("requires a nonempty canonical permutation and genus 0,1,2")
    if count(tuple(len(c) for c in cycles(p)), genus) == 0:
        raise ValueError("empty connected fiber")
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


def sample_identity(n, genus=2, rng=None):
    if n < 1:
        raise ValueError("requires positive degree")
    return sample(tuple(range(n)), genus, rng)
