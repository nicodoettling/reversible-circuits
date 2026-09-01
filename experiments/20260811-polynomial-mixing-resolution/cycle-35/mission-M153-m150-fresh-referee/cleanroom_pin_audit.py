#!/usr/bin/env python3
"""Clean-room exact audit of the frozen M150 reduced Pin theorem.

This implementation does not import M150 or its checker.  It builds the
quadratic coefficient field Q(sqrt(2)), Euclidean Clifford multiplication,
the finite Pin preimages in ranks 3 and 5, the split A2 section, and the
localized centralizer witnesses directly.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import platform
from collections import Counter, deque
from fractions import Fraction
from pathlib import Path


Q2 = tuple[Fraction, Fraction]  # rational + sqrt(2) * rational
MV = dict[int, Q2]
Perm = tuple[int, ...]
Edge = tuple[int, int]

ZERO: Q2 = (Fraction(0), Fraction(0))
ONE: Q2 = (Fraction(1), Fraction(0))
NEG_ONE: Q2 = (Fraction(-1), Fraction(0))
INV_SQRT_TWO: Q2 = (Fraction(0), Fraction(1, 2))


def qadd(x: Q2, y: Q2) -> Q2:
    return (x[0] + y[0], x[1] + y[1])


def qneg(x: Q2) -> Q2:
    return (-x[0], -x[1])


def qmul(x: Q2, y: Q2) -> Q2:
    return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def qscale(x: Q2, n: int) -> Q2:
    return (n * x[0], n * x[1])


def mv_key(x: MV) -> tuple:
    return tuple(
        (blade, a.numerator, a.denominator, b.numerator, b.denominator)
        for blade, (a, b) in sorted(x.items())
        if (a, b) != ZERO
    )


def mv_add(x: MV, y: MV) -> MV:
    out = dict(x)
    for blade, coefficient in y.items():
        out[blade] = qadd(out.get(blade, ZERO), coefficient)
        if out[blade] == ZERO:
            del out[blade]
    return out


def mv_neg(x: MV) -> MV:
    return {blade: qneg(coefficient) for blade, coefficient in x.items()}


def crossing_sign(left_blade: int, right_blade: int) -> int:
    inversions = 0
    bits = left_blade
    while bits:
        bit = bits & -bits
        inversions += (right_blade & (bit - 1)).bit_count()
        bits ^= bit
    return -1 if inversions % 2 else 1


def mv_mul(x: MV, y: MV) -> MV:
    out: MV = {}
    for left_blade, left_coefficient in x.items():
        for right_blade, right_coefficient in y.items():
            blade = left_blade ^ right_blade
            coefficient = qmul(left_coefficient, right_coefficient)
            coefficient = qscale(coefficient, crossing_sign(left_blade, right_blade))
            out[blade] = qadd(out.get(blade, ZERO), coefficient)
            if out[blade] == ZERO:
                del out[blade]
    return out


def mv_product(factors) -> MV:
    out: MV = {0: ONE}
    for factor in factors:
        out = mv_mul(out, factor)
    return out


def unit_root(edge: Edge) -> MV:
    i, j = edge
    assert i < j
    return {1 << i: INV_SQRT_TWO, 1 << j: qneg(INV_SQRT_TWO)}


def identity_perm(d: int) -> Perm:
    return tuple(range(d))


def compose(p: Perm, q: Perm) -> Perm:
    """p after q: (p q)(x)=p(q(x))."""
    return tuple(p[q[i]] for i in range(len(p)))


def inverse_perm(p: Perm) -> Perm:
    out = [0] * len(p)
    for i, image in enumerate(p):
        out[image] = i
    return tuple(out)


def edge_perm(d: int, edge: Edge) -> Perm:
    out = list(range(d))
    i, j = edge
    out[i], out[j] = out[j], out[i]
    return tuple(out)


def sign(p: Perm) -> int:
    inversions = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inversions % 2 else 1


def conjugate(g: Perm, x: Perm) -> Perm:
    return compose(compose(g, x), inverse_perm(g))


def evaluate(word: tuple[Edge, ...], d: int) -> Perm:
    out = identity_perm(d)
    for edge in word:
        out = compose(out, edge_perm(d, edge))
    return out


def support_connected(word: tuple[Edge, ...], d: int) -> bool:
    seen = {0}
    changed = True
    while changed:
        changed = False
        for i, j in word:
            if i in seen and j not in seen:
                seen.add(j)
                changed = True
            if j in seen and i not in seen:
                seen.add(i)
                changed = True
    return len(seen) == d


def finite_pin_preimage(d: int) -> dict:
    """Enumerate the root-generated Pin preimage, with central -1 included."""
    ident_p = identity_perm(d)
    ident_mv: MV = {0: ONE}
    minus_mv: MV = {0: NEG_ONE}
    generators = [(edge_perm(d, (i, i + 1)), unit_root((i, i + 1))) for i in range(d - 1)]
    generators.append((ident_p, minus_mv))
    queue = deque([(ident_p, ident_mv)])
    lift_to_perm = {mv_key(ident_mv): ident_p}
    while queue:
        p, lift = queue.popleft()
        for gp, glift in generators:
            new_p = compose(p, gp)
            new_lift = mv_mul(lift, glift)
            key = mv_key(new_lift)
            previous = lift_to_perm.get(key)
            if previous is None:
                lift_to_perm[key] = new_p
                queue.append((new_p, new_lift))
            else:
                assert previous == new_p
    fiber_sizes = Counter(lift_to_perm.values())
    assert len(lift_to_perm) == 2 * math.factorial(d)
    assert set(fiber_sizes.values()) == {2}
    identity_lifts = [key for key, p in lift_to_perm.items() if p == ident_p]
    assert set(identity_lifts) == {mv_key(ident_mv), mv_key(minus_mv)}
    return {
        "d": d,
        "preimage_order": len(lift_to_perm),
        "base_order": len(fiber_sizes),
        "fiber_size_histogram": {str(k): v for k, v in sorted(Counter(fiber_sizes.values()).items())},
        "kernel": ["+1", "-1"],
    }


def d3_split_section() -> tuple[dict[Perm, MV], dict]:
    d = 3
    ident = identity_perm(d)
    generators = [(edge_perm(d, (0, 1)), unit_root((0, 1))), (edge_perm(d, (1, 2)), unit_root((1, 2)))]
    queue = deque([(ident, {0: ONE})])
    section: dict[Perm, MV] = {ident: {0: ONE}}
    while queue:
        p, lift = queue.popleft()
        for gp, glift in generators:
            new_p = compose(p, gp)
            new_lift = mv_mul(lift, glift)
            if new_p not in section:
                section[new_p] = new_lift
                queue.append((new_p, new_lift))
            else:
                assert section[new_p] == new_lift
    assert len(section) == 6
    for p, q in itertools.product(section, repeat=2):
        assert mv_mul(section[p], section[q]) == section[compose(p, q)]
    a = unit_root((0, 1))
    b = unit_root((1, 2))
    c = unit_root((0, 2))
    assert mv_mul(a, a) == {0: ONE}
    assert mv_mul(b, b) == {0: ONE}
    assert mv_product((a, b, a)) == mv_product((b, a, b))
    assert mv_product((a, b, a)) == mv_neg(c)
    for edge in itertools.combinations(range(3), 2):
        assert section[edge_perm(3, edge)] in (unit_root(edge), mv_neg(unit_root(edge)))
    return section, {
        "section_order": len(section),
        "homomorphism_table_entries": len(section) ** 2,
        "a2_braid": True,
        "section_lift_of_02": "-a_(02)",
    }


def d3_even_word_audit(section: dict[Perm, MV]) -> dict:
    edges = tuple(itertools.combinations(range(3), 2))
    rows = []
    for length in (4, 6):
        product_one = 0
        connected = 0
        nonidentity_lifts = 0
        for word in itertools.product(edges, repeat=length):
            if evaluate(word, 3) != identity_perm(3):
                continue
            product_one += 1
            connected += support_connected(word, 3)
            lift = mv_product(section[edge_perm(3, edge)] for edge in word)
            nonidentity_lifts += lift != {0: ONE}
        assert nonidentity_lifts == 0
        translate_masks_checked = 0
        for width in range(1, 5):
            for mask in range(1 << width):
                translated_product_mask = 0
                for _ in range(length):
                    translated_product_mask ^= mask
                assert translated_product_mask == 0
                translate_masks_checked += 1
        rows.append(
            {
                "length": length,
                "product_one_words": product_one,
                "connected_product_one_words": connected,
                "nonidentity_section_products": nonidentity_lifts,
                "central_translate_masks_checked_widths_1_to_4": translate_masks_checked,
            }
        )
    assert rows[0]["product_one_words"] == 27
    assert rows[0]["connected_product_one_words"] == 24
    return {"rows": rows, "even_length_translate_independence": True}


def common_parity_conjugacy_audit(d: int) -> dict:
    perms = tuple(itertools.permutations(range(d)))
    even = tuple(p for p in perms if sign(p) == 1)
    edges = tuple(itertools.combinations(range(d), 2))
    misses = []
    for source, target in itertools.product(edges, repeat=2):
        source_p = edge_perm(d, source)
        target_p = edge_perm(d, target)
        transporter = next((g for g in even if conjugate(g, source_p) == target_p), None)
        if transporter is None:
            misses.append([list(source), list(target)])
    assert not misses
    return {
        "d": d,
        "ordered_transposition_pairs": len(edges) ** 2,
        "even_transporter_failures": misses,
        "tuple_consequence": "coordinatewise even transporters lie in A_d^s <= P_(d,s)",
    }


def localized_kernel_audit(d: int, max_width: int) -> dict:
    edges = tuple(itertools.combinations(range(d), 2))
    ident = identity_perm(d)
    minus = {0: NEG_ONE}
    rows = []
    for width in range(1, max_width + 1):
        failures = []
        witnesses = 0
        for transposition_tuple in itertools.product(edges, repeat=width):
            for q, t in enumerate(transposition_tuple):
                v = next(edge for edge in edges if set(edge).isdisjoint(t))
                t_perm = edge_perm(d, t)
                v_perm = edge_perm(d, v)
                hq = compose(t_perm, v_perm)
                h_tuple = [ident for _ in range(width)]
                h_tuple[q] = hq
                in_common_even = all(sign(h) == 1 for h in h_tuple)
                centralizes = compose(hq, t_perm) == compose(t_perm, hq)
                a = unit_root(t)
                b = unit_root(v)
                ab = mv_mul(a, b)
                commutator = mv_product((a, ab, a, mv_mul(b, a)))
                witnesses += 1
                if not (in_common_even and centralizes and commutator == minus):
                    failures.append({"tuple": transposition_tuple, "coordinate": q, "t": t, "v": v})
        assert not failures
        rows.append(
            {
                "width": width,
                "tuples": len(edges) ** width,
                "localized_witnesses": witnesses,
                "failures": failures,
            }
        )
    return {
        "d": d,
        "rows": rows,
        "deduction": "each z_q occurs as [a_t,a_t a_v], so K_C contains the full kernel",
    }


def signed_hurwitz_section_audit(section: dict[Perm, MV]) -> dict:
    edges = tuple(itertools.combinations(range(3), 2))
    checked = 0
    for a_edge, b_edge in itertools.product(edges, repeat=2):
        a = edge_perm(3, a_edge)
        b = edge_perm(3, b_edge)
        moved_second = compose(compose(inverse_perm(b), a), b)
        old_lift = mv_mul(section[a], section[b])
        new_lift = mv_mul(section[b], section[moved_second])
        assert old_lift == new_lift
        checked += 1
    return {
        "d": 3,
        "ordered_pairs_checked": checked,
        "identity": "ell(b) ell(b^-1 a b) = ell(a) ell(b)",
        "failures": [],
    }


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    section, split = d3_split_section()
    results = {
        "metadata": {
            "mission": "M153",
            "kind": "fresh immutable referee",
            "python": platform.python_version(),
            "dependencies": {},
            "seed": None,
            "command": "python3 -B cleanroom_pin_audit.py",
            "frozen_m150_inputs_imported": False,
        },
        "finite_pin_preimages": [finite_pin_preimage(3), finite_pin_preimage(5)],
        "common_parity_conjugacy": [common_parity_conjugacy_audit(3), common_parity_conjugacy_audit(5)],
        "d3_split_section": split,
        "d3_even_product_one": d3_even_word_audit(section),
        "signed_hurwitz_section": signed_hurwitz_section_audit(section),
        "localized_kernel": [localized_kernel_audit(4, 3), localized_kernel_audit(5, 3)],
    }
    path = Path(__file__).with_name("results.json")
    path.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
