#!/usr/bin/env python3
"""Exact algebra audit for nonadjacent pair heat baths on ordered-product bridges.

The finite calculation is a falsifier for universal projection identities.  It
works on the group-increment marginal but retains the exact number of ordered
transposition-pair micro lifts as the single-site weight.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import numpy as np


Perm = tuple[int, ...]
Word = tuple[Perm, ...]


def compose(p: Perm, q: Perm) -> Perm:
    """p after q."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def conjugate(x: Perm, g: Perm) -> Perm:
    """g^{-1} x g."""
    return compose(inverse(g), compose(x, g))


def transpositions(n: int) -> list[Perm]:
    ans: list[Perm] = []
    for i in range(n):
        for j in range(i + 1, n):
            p = list(range(n))
            p[i], p[j] = p[j], p[i]
            ans.append(tuple(p))
    return ans


def parity(p: Perm) -> int:
    inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return inv % 2


def cycles(p: Perm) -> str:
    seen = [False] * len(p)
    parts: list[str] = []
    for i in range(len(p)):
        if seen[i]:
            continue
        cyc: list[int] = []
        x = i
        while not seen[x]:
            seen[x] = True
            cyc.append(x + 1)
            x = p[x]
        if len(cyc) > 1:
            parts.append("(" + " ".join(map(str, cyc)) + ")")
    return "".join(parts) if parts else "e"


def word_product(word: Word, identity: Perm) -> Perm:
    ans = identity
    for g in word:
        ans = compose(ans, g)
    return ans


def segment_product(word: Word, lo: int, hi: int, identity: Perm) -> Perm:
    ans = identity
    for k in range(lo, hi):
        ans = compose(ans, word[k])
    return ans


def setup(n: int):
    ident = tuple(range(n))
    ts = transpositions(n)
    lift_count: dict[Perm, int] = defaultdict(int)
    first_lift: dict[Perm, tuple[Perm, Perm]] = {}
    for a in ts:
        for b in ts:
            g = compose(a, b)
            lift_count[g] += 1
            first_lift.setdefault(g, (a, b))
    group = sorted((p for p in itertools.permutations(range(n)) if parity(p) == 0))
    support = sorted(lift_count)
    return ident, ts, group, support, dict(lift_count), first_lift


def raw_pair_row(
    word: Word,
    pair: tuple[int, int],
    support: list[Perm],
    weights: dict[Perm, int],
    identity: Perm,
) -> dict[Word, Fraction]:
    i, j = pair
    assert i < j
    middle = segment_product(word, i + 1, j, identity)
    target = compose(word[i], compose(middle, word[j]))
    middle_inv = inverse(middle)
    masses: dict[Word, int] = {}
    total = 0
    for x in support:
        # x * middle * y = target
        y = compose(middle_inv, compose(inverse(x), target))
        if y not in weights:
            continue
        new = list(word)
        new[i], new[j] = x, y
        new_t = tuple(new)
        mass = weights[x] * weights[y]
        masses[new_t] = mass
        total += mass
    assert total > 0
    return {new: Fraction(mass, total) for new, mass in masses.items()}


def composed_row(
    word: Word,
    first: tuple[int, int],
    second: tuple[int, int],
    support: list[Perm],
    weights: dict[Perm, int],
    identity: Perm,
) -> dict[Word, Fraction]:
    ans: dict[Word, Fraction] = defaultdict(Fraction)
    for mid, p1 in raw_pair_row(word, first, support, weights, identity).items():
        for out, p2 in raw_pair_row(mid, second, support, weights, identity).items():
            ans[out] += p1 * p2
    return dict(ans)


def hurwitz_at(word: Word, site: int) -> Word:
    a, b = word[site], word[site + 1]
    new = list(word)
    new[site] = b
    new[site + 1] = conjugate(a, b)
    return tuple(new)


def hurwitz_inverse_at(word: Word, site: int) -> Word:
    c, d = word[site], word[site + 1]
    new = list(word)
    new[site] = compose(c, compose(d, inverse(c)))
    new[site + 1] = c
    return tuple(new)


def braid(word: Word, sites: tuple[int, ...]) -> Word:
    ans = word
    for site in sites:
        ans = hurwitz_at(ans, site)
    return ans


def braid_inverse(word: Word, sites: tuple[int, ...]) -> Word:
    ans = word
    for site in reversed(sites):
        ans = hurwitz_inverse_at(ans, site)
    return ans


def shuttle_row(
    word: Word,
    braid_sites: tuple[int, ...],
    adjacent_pair: tuple[int, int],
    support: list[Perm],
    weights: dict[Perm, int],
    identity: Perm,
) -> dict[Word, Fraction]:
    moved = braid(word, braid_sites)
    ans: dict[Word, Fraction] = defaultdict(Fraction)
    for refreshed, prob in raw_pair_row(
        moved, adjacent_pair, support, weights, identity
    ).items():
        ans[braid_inverse(refreshed, braid_sites)] += prob
    return dict(ans)


def find_kernel_difference(
    states: list[Word],
    row_a,
    row_b,
):
    for x in states:
        a = row_a(x)
        b = row_b(x)
        for y in sorted(set(a) | set(b)):
            if a.get(y, 0) != b.get(y, 0):
                return x, y, a.get(y, Fraction(0)), b.get(y, Fraction(0))
    return None


def three_coordinate_group_gaps(
    group: list[Perm],
    support: list[Perm],
    weights: dict[Perm, int],
    identity: Perm,
):
    """Diagonalize the complete three-pair chain on group-product functions.

    These numbers are finite diagnostics only.  They can refute a claimed
    endpoint-independent value or a >1/3 threshold if the computed upper
    subspace gap is already <=1/3; they cannot lower-bound the full micro gap.
    """
    records = []
    for endpoint in group:
        states = [
            w for w in itertools.product(support, repeat=3)
            if word_product(w, identity) == endpoint
        ]
        index = {w: i for i, w in enumerate(states)}
        stat = np.array([stationary_weight(w, weights) for w in states], dtype=float)
        stat /= stat.sum()
        kernel = np.zeros((len(states), len(states)), dtype=float)
        for x_i, x in enumerate(states):
            for pair in ((0, 1), (0, 2), (1, 2)):
                for y, prob in raw_pair_row(x, pair, support, weights, identity).items():
                    kernel[x_i, index[y]] += float(prob) / 3.0
        root = np.sqrt(stat)
        sym = root[:, None] * kernel / root[None, :]
        symmetry_error = float(np.max(np.abs(sym - sym.T)))
        eigenvalues = np.linalg.eigvalsh((sym + sym.T) / 2.0)
        gap = float(1.0 - eigenvalues[-2])
        records.append({
            "endpoint_cycles": cycles(endpoint),
            "endpoint_tuple": list(endpoint),
            "group_state_count": len(states),
            "group_function_gap": gap,
            "lambda2": float(eigenvalues[-2]),
            "symmetry_error": symmetry_error,
        })
    return {
        "scope": "group-product subspace only; gives an upper bound on full micro gap",
        "normalization": "(P_12+P_13+P_23)/3",
        "records": records,
        "minimum_group_function_gap": min(r["group_function_gap"] for r in records),
        "maximum_group_function_gap": max(r["group_function_gap"] for r in records),
    }


def stationary_weight(word: Word, weights: dict[Perm, int]) -> int:
    ans = 1
    for g in word:
        ans *= weights[g]
    return ans


def apply_projection(
    f: dict[Word, Fraction],
    states: list[Word],
    pair: tuple[int, int],
    support: list[Perm],
    weights: dict[Perm, int],
    identity: Perm,
) -> dict[Word, Fraction]:
    out: dict[Word, Fraction] = {}
    for x in states:
        out[x] = sum((prob * f.get(y, Fraction(0)) for y, prob in raw_pair_row(
            x, pair, support, weights, identity
        ).items()), Fraction(0))
    return out


def inner(
    f: dict[Word, Fraction],
    g: dict[Word, Fraction],
    states: list[Word],
    weights: dict[Perm, int],
) -> Fraction:
    z = sum(stationary_weight(x, weights) for x in states)
    return sum(
        (Fraction(stationary_weight(x, weights), z) * f.get(x, 0) * g.get(x, 0)
         for x in states),
        Fraction(0),
    )


def subtract(f: dict[Word, Fraction], g: dict[Word, Fraction]) -> dict[Word, Fraction]:
    return {x: f.get(x, Fraction(0)) - g.get(x, Fraction(0)) for x in set(f) | set(g)}


def micro_hurwitz_checks(
    micro: list[tuple[Perm, Perm]], identity: Perm
) -> dict[str, bool]:
    def p(a: tuple[Perm, Perm]) -> Perm:
        return compose(a[0], a[1])

    def conj_micro(a: tuple[Perm, Perm], g: Perm) -> tuple[Perm, Perm]:
        return conjugate(a[0], g), conjugate(a[1], g)

    def r(a, b):
        return b, conj_micro(a, p(b))

    image = set()
    product_ok = True
    for a in micro:
        for b in micro:
            c, d = r(a, b)
            image.add((c, d))
            product_ok &= compose(p(a), p(b)) == compose(p(c), p(d))
    bijective = len(image) == len(micro) ** 2

    braid_ok = True
    # Exhaustive N=4 would use 36^3=46656 triples, still small.
    for a in micro:
        for b in micro:
            for c in micro:
                x1, x2 = r(a, b)
                x2, x3 = r(x2, c)
                x1, x2 = r(x1, x2)
                left = (x1, x2, x3)

                y2, y3 = r(b, c)
                y1, y2 = r(a, y2)
                y2, y3 = r(y2, y3)
                right = (y1, y2, y3)
                if left != right:
                    braid_ok = False
                    return {
                        "bijective": bijective,
                        "product_preserving": product_ok,
                        "braid_relation": braid_ok,
                    }
    return {
        "bijective": bijective,
        "product_preserving": product_ok,
        "braid_relation": braid_ok,
    }


def encode_word(word: Word, first_lift: dict[Perm, tuple[Perm, Perm]]):
    return {
        "group_cycles": [cycles(g) for g in word],
        "group_tuples": [list(g) for g in word],
        "micro_lifts_cycles": [
            [cycles(first_lift[g][0]), cycles(first_lift[g][1])] for g in word
        ],
        "micro_lifts_tuples": [
            [list(first_lift[g][0]), list(first_lift[g][1])] for g in word
        ],
    }


def find_commutator_witness(
    states: list[Word],
    pair_a: tuple[int, int],
    pair_b: tuple[int, int],
    support: list[Perm],
    weights: dict[Perm, int],
    identity: Perm,
):
    for x in states:
        ab = composed_row(x, pair_a, pair_b, support, weights, identity)
        ba = composed_row(x, pair_b, pair_a, support, weights, identity)
        for y in sorted(set(ab) | set(ba)):
            if ab.get(y, 0) != ba.get(y, 0):
                return x, y, ab.get(y, Fraction(0)), ba.get(y, Fraction(0))
    return None


def find_delta_cross_witness(
    states: list[Word],
    pair_a: tuple[int, int],
    pair_b: tuple[int, int],
    support: list[Perm],
    weights: dict[Perm, int],
    identity: Perm,
):
    # For f=1_{y}, self-adjointness gives
    # <(P_a-I)f,(P_b-I)f>
    # =pi(y)[I-P_a-P_b+P_a P_b](y,y).  This avoids constructing dense
    # projection columns while retaining exact rational arithmetic.
    z_stationary = sum(stationary_weight(x, weights) for x in states)
    for y in states:
        ka = raw_pair_row(y, pair_a, support, weights, identity)
        kb = raw_pair_row(y, pair_b, support, weights, identity)
        kab = composed_row(y, pair_a, pair_b, support, weights, identity)
        bracket = Fraction(1) - ka.get(y, 0) - kb.get(y, 0) + kab.get(y, 0)
        val = Fraction(stationary_weight(y, weights), z_stationary) * bracket
        if val < 0:
            return {"terms": [(y, 1)], "cross": val}
    return None


def constructed_negative_cross_witness(
    seeds: list[Word],
    states: list[Word],
    pair_a: tuple[int, int],
    pair_b: tuple[int, int],
    support: list[Perm],
    weights: dict[Perm, int],
    identity: Perm,
):
    """Construct the standard negative anticommutator vector exactly.

    Put A=I-P_a and B=I-P_b.  For u=A delta_y and
    v=(I-A)Bu=P_a B u, one has A v=0 and <u,Bv>=||v||^2.
    Thus f=u-t v with t=(<u,Bu>+||v||^2)/||v||^2 has
    <Af,Bf>=-||v||^2 whenever v is nonzero.
    """
    for y in seeds:
        delta = {y: Fraction(1)}
        pa_delta = apply_projection(delta, states, pair_a, support, weights, identity)
        u = subtract(delta, pa_delta)
        pb_u = apply_projection(u, states, pair_b, support, weights, identity)
        bu = subtract(u, pb_u)
        v = apply_projection(bu, states, pair_a, support, weights, identity)
        beta = inner(v, v, states, weights)
        if beta == 0:
            continue
        alpha = inner(u, bu, states, weights)
        t = (alpha + beta) / beta
        f = {x: u.get(x, 0) - t * v.get(x, 0) for x in states}
        pa_f = apply_projection(f, states, pair_a, support, weights, identity)
        pb_f = apply_projection(f, states, pair_b, support, weights, identity)
        af = subtract(f, pa_f)
        bf = subtract(f, pb_f)
        cross = inner(af, bf, states, weights)
        assert cross == -beta < 0
        return {
            "seed": y,
            "alpha": alpha,
            "beta": beta,
            "t": t,
            "cross": cross,
            "formula": "f=(I-P_a)1_seed-t P_a(I-P_b)(I-P_a)1_seed",
        }
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=4)
    parser.add_argument("--length", type=int, default=4)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    ident, ts, group, support, weights, first_lift = setup(args.N)
    micro = [(a, b) for a in ts for b in ts]
    hurwitz = micro_hurwitz_checks(micro, ident)

    all_words = itertools.product(support, repeat=args.length)
    states = [w for w in all_words if word_product(w, ident) == ident]
    pairs = {
        "separated": ((0, 1), (2, 3)),
        "nested": ((0, 3), (1, 2)),
        "crossing": ((0, 2), (1, 3)),
    }
    tests = {}
    for name, (a, b) in pairs.items():
        witness = find_commutator_witness(states, a, b, support, weights, ident)
        if witness is None:
            tests[name] = {"commute_on_identity_sector": True}
        else:
            x, y, ab, ba = witness
            tests[name] = {
                "commute_on_identity_sector": False,
                "input": encode_word(x, first_lift),
                "output": encode_word(y, first_lift),
                "P_a_then_P_b": [ab.numerator, ab.denominator],
                "P_b_then_P_a": [ba.numerator, ba.denominator],
                "pair_a_zero_based": list(a),
                "pair_b_zero_based": list(b),
            }
            delta = find_delta_cross_witness(states, a, b, support, weights, ident)
            if delta is not None:
                tests[name]["negative_delta_cross"] = {
                    "cross": [delta["cross"].numerator, delta["cross"].denominator],
                    "terms": [
                        {"coefficient": c, "word": encode_word(w, first_lift)}
                        for w, c in delta["terms"]
                    ],
                }
            constructed = constructed_negative_cross_witness(
                [x, y] + states[:8], states, a, b, support, weights, ident
            )
            if constructed is not None:
                tests[name]["negative_constructed_cross"] = {
                    "seed": encode_word(constructed["seed"], first_lift),
                    "formula": constructed["formula"],
                    "alpha": [constructed["alpha"].numerator, constructed["alpha"].denominator],
                    "beta": [constructed["beta"].numerator, constructed["beta"].denominator],
                    "t": [constructed["t"].numerator, constructed["t"].denominator],
                    "cross": [constructed["cross"].numerator, constructed["cross"].denominator],
                }

    shuttle_tests = None
    if args.length >= 3:
        states3 = [
            w for w in itertools.product(support, repeat=3)
            if word_product(w, ident) == ident
        ]
        left = lambda w: shuttle_row(
            w, (1,), (0, 1), support, weights, ident
        )
        right = lambda w: shuttle_row(
            w, (0,), (1, 2), support, weights, ident
        )
        raw = lambda w: raw_pair_row(
            w, (0, 2), support, weights, ident
        )
        lr = find_kernel_difference(states3, left, right)
        lraw = find_kernel_difference(states3, left, raw)
        rraw = find_kernel_difference(states3, right, raw)
        shuttle_tests = {
            "identity_sector_group_word_count": len(states3),
            "later_left_equals_earlier_right": lr is None,
            "later_left_equals_raw_pair_conditional": lraw is None,
            "earlier_right_equals_raw_pair_conditional": rraw is None,
        }
        if lr is not None:
            x, y, a, b = lr
            shuttle_tests["orientation_witness"] = {
                "input": encode_word(x, first_lift),
                "output": encode_word(y, first_lift),
                "later_left_probability": [a.numerator, a.denominator],
                "earlier_right_probability": [b.numerator, b.denominator],
            }
        if lraw is not None:
            x, y, a, b = lraw
            shuttle_tests["raw_conditional_witness"] = {
                "input": encode_word(x, first_lift),
                "output": encode_word(y, first_lift),
                "later_left_probability": [a.numerator, a.denominator],
                "raw_pair_probability": [b.numerator, b.denominator],
            }
        if rraw is not None:
            x, y, a, b = rraw
            shuttle_tests["earlier_right_raw_failure_witness"] = {
                "input": encode_word(x, first_lift),
                "output": encode_word(y, first_lift),
                "earlier_right_probability": [a.numerator, a.denominator],
                "raw_pair_probability": [b.numerator, b.denominator],
            }

    payload = {
        "status": "complete",
        "claim_scope": "finite falsification of universal braided projection identities",
        "composition": "(pq)(x)=p(q(x))",
        "deterministic": True,
        "python": platform.python_version(),
        "N": args.N,
        "length": args.length,
        "group_size": len(group),
        "increment_support_size": len(support),
        "micro_alphabet_size": len(micro),
        "identity_sector_group_word_count": len(states),
        "micro_hurwitz": hurwitz,
        "pair_projection_tests": tests,
        "three_coordinate_shuttle_tests": shuttle_tests,
        "three_coordinate_complete_gap_audit": three_coordinate_group_gaps(
            group, support, weights, ident
        ),
    }
    Path(args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
