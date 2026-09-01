#!/usr/bin/env python3
"""Exact k=9 diagnostic for the M297 BODT coefficient candidate.

This is a clean-room reconstruction.  It imports no predecessor code or data.
It keeps the complete B-A signed product coefficient, verifies the 1/3 and
1/4 positive-composition phase collapse, and takes lag absolute values only
after the requested aggregate has been formed.  The rank is fixed to k=9;
the output is falsification/calibration only.
"""

from __future__ import annotations

import hashlib
import json
import math
import platform
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations


K0 = 9
Perm = tuple[int, ...]
Lin = tuple[Fraction, Fraction]  # e^2 coefficient, constant coefficient


def mul(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inv(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def cyc(n: int, entries: tuple[int, ...]) -> Perm:
    out = list(range(n))
    if len(entries) > 1:
        for x, y in zip(entries, entries[1:] + entries[:1]):
            out[x] = y
    return tuple(out)


def tr(n: int, x: int, y: int) -> Perm:
    return cyc(n, (x, y))


def cycles(p: Perm) -> tuple[tuple[int, ...], ...]:
    unseen = set(range(len(p)))
    ans = []
    while unseen:
        x0 = min(unseen)
        c = []
        x = x0
        while x in unseen:
            unseen.remove(x)
            c.append(x)
            x = p[x]
        ans.append(tuple(c))
    return tuple(ans)


def rank(p: Perm) -> int:
    return len(p) - len(cycles(p))


@lru_cache(maxsize=None)
def tau(d: int) -> Fraction:
    if d < 1:
        return Fraction(0)
    if d == 1:
        return Fraction(1)
    return Fraction(d ** (d - 2), math.factorial(d - 1))


def completion(p: Perm, length: int) -> int:
    if rank(p) != length:
        return 0
    value = Fraction(math.factorial(length))
    for c in cycles(p):
        value *= tau(len(c))
    assert value.denominator == 1
    return value.numerator


def internal_edges(n: int, component: tuple[int, ...]):
    for x, y in combinations(sorted(component), 2):
        yield tr(n, x, y)


def source_law(k: int, label: str):
    """First-two-factor product law with exact J and T/D coordinates."""
    n = 3 * k
    h = cyc(n, tuple(range(n)))
    if label == "A":
        source = cyc(n, (0, k, 2 * k))
    elif label == "B":
        source = mul(tr(n, 0, 1), tr(n, k, 2 * k))
    else:
        raise ValueError(label)
    residual = mul(inv(source), h)
    original = cycles(residual)
    owner = {x: i for i, c in enumerate(original) for x in c}
    middle = owner[k]
    r0 = rank(residual)
    denominator = completion(residual, r0)
    law: dict[tuple[int, str, Perm], Fraction] = defaultdict(Fraction)
    raw = 0
    for first_owner, component in enumerate(original):
        for first in internal_edges(n, component):
            after_first = mul(first, residual)
            for child in cycles(after_first):
                second_owner = owner[child[0]]
                assert all(owner[x] == second_owner for x in child)
                for second in internal_edges(n, child):
                    numerator = completion(mul(second, after_first), r0 - 2)
                    if not numerator:
                        continue
                    product = mul(first, second)
                    moved = tuple(x for x in range(n) if product[x] != x)
                    kind = "T" if len(moved) == 3 else "D"
                    assert len(moved) in (3, 4)
                    channel = int(first_owner != middle) + int(
                        second_owner != middle
                    )
                    law[(channel, kind, product)] += Fraction(numerator, denominator)
                    raw += 1
    assert sum(law.values(), Fraction(0)) == 1
    return dict(law), raw


def owner_profile(n: int, h: Perm, product: Perm):
    residual = mul(inv(product), h)
    comps = cycles(residual)
    assert len(comps) == 3
    owner = {x: i for i, c in enumerate(comps) for x in c}
    generic = tuple(
        owner[x] if product[(x + 1) % n] == (x + 1) % n else None
        for x in range(n)
    )
    sizes = tuple(len(c) for c in comps)
    return generic, sizes


def q_rows(generic, sizes) -> tuple[Lin, ...]:
    n = len(generic)
    a = [tau(d - 1) / tau(d) for d in sizes]
    b = [tau(d - 2) / tau(d) for d in sizes]
    ans = []
    for lag in range(n):
        f = Fraction(0)
        overlap = 0
        for x in range(n):
            i = generic[x]
            j = generic[(x + lag) % n]
            if i is None or j is None:
                continue
            overlap += 1
            f += b[i] if i == j else a[i] * a[j]
        ans.append((f, Fraction(-overlap)))
    return tuple(ans)


def lin_add(x: Lin, y: Lin) -> Lin:
    return x[0] + y[0], x[1] + y[1]


def lin_scale(c: Fraction, x: Lin) -> Lin:
    return c * x[0], c * x[1]


def lin_sub(x: Lin, y: Lin) -> Lin:
    return x[0] - y[0], x[1] - y[1]


def vec_add(x: tuple[Lin, ...], y: tuple[Lin, ...]) -> tuple[Lin, ...]:
    return tuple(lin_add(a, b) for a, b in zip(x, y))


def vec_scale(c: Fraction, x: tuple[Lin, ...]) -> tuple[Lin, ...]:
    return tuple(lin_scale(c, a) for a in x)


def zero_vec(n: int) -> tuple[Lin, ...]:
    return tuple((Fraction(0), Fraction(0)) for _ in range(n))


def derivative(q: tuple[Lin, ...]) -> tuple[Lin, ...]:
    n = len(q)
    return tuple(lin_sub(q[(ell + 1) % n], q[ell]) for ell in range(n))


def corr01(f: tuple[int, ...], g: tuple[int, ...]) -> tuple[int, ...]:
    n = len(f)
    return tuple(sum(f[x] * g[(x + ell) % n] for x in range(n)) for ell in range(n))


def int_derivative(q: tuple[int, ...]) -> tuple[int, ...]:
    n = len(q)
    return tuple(q[(ell + 1) % n] - q[ell] for ell in range(n))


def frac_vec_add(x: tuple[Fraction, ...], y: tuple[Fraction, ...]):
    return tuple(a + b for a, b in zip(x, y))


def frac_vec_scale(c: Fraction, x: tuple[int | Fraction, ...]):
    return tuple(c * a for a in x)


def frac_l1(v: tuple[Fraction, ...], lags: range) -> Fraction:
    return sum((abs(v[ell]) for ell in lags), Fraction(0))


def support(product: Perm) -> tuple[int, ...]:
    return tuple(x for x in range(len(product)) if product[x] != x)


def gaps_from_anchor(n: int, vertices: tuple[int, ...], anchor_index: int):
    ordered = vertices[anchor_index:] + vertices[:anchor_index]
    return tuple((ordered[(i + 1) % len(ordered)] - ordered[i]) % n for i in range(len(ordered)))


def positive_representations(product: Perm):
    """Return all three/four exact (K,g) representations of one product."""
    n = len(product)
    vertices = support(product)
    ans = []
    if len(vertices) == 3:
        for j in range(3):
            ordered = vertices[j:] + vertices[:j]
            candidate = cyc(n, ordered)
            if candidate == product:
                ans.append(("T", gaps_from_anchor(n, vertices, j)))
        assert len(ans) == 3
        return tuple(ans)
    assert len(vertices) == 4
    for j in range(4):
        v = vertices[j:] + vertices[:j]
        s_state = mul(tr(n, v[0], v[1]), tr(n, v[2], v[3]))
        n_state = mul(tr(n, v[0], v[3]), tr(n, v[1], v[2]))
        if product == s_state:
            ans.append(("S", gaps_from_anchor(n, vertices, j)))
        elif product == n_state:
            ans.append(("N", gaps_from_anchor(n, vertices, j)))
        else:
            raise AssertionError("crossing double is not supported")
    assert len(ans) == 4
    return tuple(ans)


def owner_sizes_from_rep(kind: str, gaps: tuple[int, ...]) -> tuple[int, ...]:
    if kind == "T":
        return gaps
    if kind == "S":
        return gaps[0], gaps[2], gaps[1] + gaps[3]
    if kind == "N":
        return gaps[1], gaps[3], gaps[0] + gaps[2]
    raise ValueError(kind)


def e2_bounds(terms: int = 60):
    lo_e = sum((Fraction(1, math.factorial(j)) for j in range(terms + 1)), Fraction(0))
    hi_e = lo_e + Fraction(2, math.factorial(terms + 1))
    return lo_e * lo_e, hi_e * hi_e


def enclosure(x: Lin, bounds):
    lo, hi = bounds
    if x[0] >= 0:
        return x[0] * lo + x[1], x[0] * hi + x[1]
    return x[0] * hi + x[1], x[0] * lo + x[1]


def abs_enclosure(x: Lin, bounds):
    lo, hi = enclosure(x, bounds)
    if lo >= 0:
        return lo, hi
    if hi <= 0:
        return -hi, -lo
    return Fraction(0), max(-lo, hi)


def l1_enclosure(v: tuple[Lin, ...], lags: range, bounds):
    lo = Fraction(0)
    hi = Fraction(0)
    undecided = 0
    for ell in lags:
        a, b = abs_enclosure(v[ell], bounds)
        lo += a
        hi += b
        undecided += int(a == 0 and b != 0)
    return lo, hi, undecided


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else str(x)


def lin_json(x: Lin):
    return {"e2": fstr(x[0]), "constant": fstr(x[1])}


def metric(v, lags, bounds):
    lo, hi, undecided = l1_enclosure(v, lags, bounds)
    return {
        "float": [float(lo), float(hi)],
        "undecided_coordinates": undecided,
    }


def eval_float(x: Lin) -> float:
    return float(x[0]) * math.e**2 + float(x[1])


def vector_digest(v: tuple[Lin, ...]) -> str:
    raw = "\n".join(f"{x[0]}|{x[1]}" for x in v).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    k = K0
    n = 3 * k
    h = cyc(n, tuple(range(n)))
    laws = {}
    raw = {}
    for label in ("A", "B"):
        laws[label], raw[label] = source_law(k, label)

    states = {s for law in laws.values() for _, _, s in law}
    omega = {
        s: sum((p for (_, _, t), p in laws["B"].items() if t == s), Fraction(0))
        - sum((p for (_, _, t), p in laws["A"].items() if t == s), Fraction(0))
        for s in states
    }
    assert sum(omega.values(), Fraction(0)) == 0

    profiles = {s: owner_profile(n, h, s) for s in states}
    rows = {s: q_rows(*profiles[s]) for s in states}
    deriv = {s: derivative(rows[s]) for s in states}
    threshold = (k - 1) // 2
    boundary = {s for s in states if min(profiles[s][1]) <= threshold}
    interior = states - boundary

    direct_bd = zero_vec(n)
    direct_int = zero_vec(n)
    by_min: dict[int, tuple[Lin, ...]] = defaultdict(lambda: zero_vec(n))
    by_kind: dict[str, tuple[Lin, ...]] = defaultdict(lambda: zero_vec(n))
    for s in states:
        term = vec_scale(omega[s], deriv[s])
        if s in boundary:
            direct_bd = vec_add(direct_bd, term)
            d = min(profiles[s][1])
            by_min[d] = vec_add(by_min[d], term)
            by_kind["T" if len(support(s)) == 3 else "D"] = vec_add(by_kind["T" if len(support(s)) == 3 else "D"], term)
        else:
            direct_int = vec_add(direct_int, term)

    # Kernel-free owner-column coefficients for the fixed analytic candidate.
    # They retain the complete signed source coefficient before each profile
    # is grouped.  S1 controls the U/B first-order field; S2 controls ordered
    # owner-owner correlations, including the diagonal correction.
    zfrac = tuple(Fraction(0) for _ in range(n))
    s1: dict[int, tuple[Fraction, ...]] = defaultdict(lambda: zfrac)
    s2: dict[tuple[int, int], tuple[Fraction, ...]] = defaultdict(lambda: zfrac)
    for s in boundary:
        generic, sizes = profiles[s]
        chis = tuple(tuple(int(x == i) for x in generic) for i in range(3))
        heads = tuple(int(x is None) for x in generic)
        for i, d in enumerate(sizes):
            if d <= threshold:
                row = tuple(a + b for a, b in zip(corr01(chis[i], heads), corr01(heads, chis[i])))
                s1[d] = frac_vec_add(s1[d], frac_vec_scale(omega[s], int_derivative(row)))
        for i, d in enumerate(sizes):
            for j, e in enumerate(sizes):
                if d <= threshold and e <= threshold:
                    delta_row = int_derivative(corr01(chis[i], chis[j]))
                    s2[(d, e)] = frac_vec_add(
                        s2[(d, e)], frac_vec_scale(omega[s], delta_row)
                    )

    # Positive-composition phase collapse.  Each state contributes through
    # its three/four representations with coefficient omega/3 or omega/4.
    phase_coeff: dict[tuple[str, tuple[int, ...]], Fraction] = defaultdict(Fraction)
    rep_response: dict[tuple[str, tuple[int, ...]], tuple[Lin, ...]] = {}
    rep_state_count = 0
    for s in states:
        reps = positive_representations(s)
        divisor = len(reps)
        for kind, gaps in reps:
            key = (kind, gaps)
            phase_coeff[key] += omega[s] / divisor
            if key in rep_response:
                assert rep_response[key] == deriv[s]
            else:
                rep_response[key] = deriv[s]
            assert tuple(sorted(owner_sizes_from_rep(kind, gaps))) == tuple(sorted(profiles[s][1]))
            rep_state_count += 1

    collapsed_bd = zero_vec(n)
    coeff_by_min: dict[int, Fraction] = defaultdict(Fraction)
    collapsed_by_min: dict[int, tuple[Lin, ...]] = defaultdict(lambda: zero_vec(n))
    collapsed_by_topology: dict[str, tuple[Lin, ...]] = defaultdict(lambda: zero_vec(n))
    for key, coeff in phase_coeff.items():
        kind, gaps = key
        d = min(owner_sizes_from_rep(kind, gaps))
        if d <= threshold:
            term = vec_scale(coeff, rep_response[key])
            collapsed_bd = vec_add(collapsed_bd, term)
            coeff_by_min[d] += coeff
            collapsed_by_min[d] = vec_add(collapsed_by_min[d], term)
            collapsed_by_topology[kind] = vec_add(collapsed_by_topology[kind], term)
    assert collapsed_bd == direct_bd
    assert all(collapsed_by_min[d] == by_min[d] for d in by_min)

    # Exact channel/kind signed rows, combined across A/B inside each label.
    channel_kind: dict[str, tuple[Lin, ...]] = defaultdict(lambda: zero_vec(n))
    for j in range(3):
        for kind in ("T", "D"):
            v = zero_vec(n)
            for label, sign in (("B", 1), ("A", -1)):
                for (jj, kk, s), p in laws[label].items():
                    if jj == j and kk == kind and s in boundary:
                        v = vec_add(v, vec_scale(sign * p, deriv[s]))
            channel_kind[f"J{j}_{kind}"] = v

    bounds = e2_bounds()
    lags = range(2, n - 2)
    total = vec_add(direct_bd, direct_int)
    cumulative = zero_vec(n)
    cumulative_metrics = {}
    for d in sorted(by_min):
        cumulative = vec_add(cumulative, by_min[d])
        cumulative_metrics[str(d)] = metric(cumulative, lags, bounds)
    s1_metrics = {}
    for d, v in sorted(s1.items()):
        norm = frac_l1(v, lags)
        bd = math.exp(-d) * float(tau(d))
        s1_metrics[str(d)] = {
            "lag_l1_float": float(norm),
            "normalized_k_over_d_b_d": k * float(norm) / (d * bd),
        }
    s2_nonzero = {}
    max_s2_ratio = 0.0
    max_s2_key = None
    for (d, e), v in sorted(s2.items()):
        norm = frac_l1(v, lags)
        if not norm:
            continue
        bd = math.exp(-d) * float(tau(d))
        be = math.exp(-e) * float(tau(e))
        ratio = k * float(norm) / (d * e * bd * be)
        if ratio > max_s2_ratio:
            max_s2_ratio = ratio
            max_s2_key = [d, e]
        s2_nonzero[f"{d},{e}"] = {
            "lag_l1_exact": fstr(norm),
            "lag_l1_float": float(norm),
            "normalized_k_over_de_bdb_e": ratio,
        }
    s2_top = dict(
        sorted(
            s2_nonzero.items(),
            key=lambda item: item[1]["normalized_k_over_de_bdb_e"],
            reverse=True,
        )[:12]
    )
    payload = {
        "status": "exact k=9 falsification/calibration only",
        "scope": "BODT coefficient candidate; no all-rank or downstream inference",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "imports_predecessor_code_or_data": False,
        "k": k,
        "n": n,
        "raw_ordered_pairs": raw,
        "state_count": len(states),
        "boundary_state_count": len(boundary),
        "interior_state_count": len(interior),
        "representation_count": rep_state_count,
        "phase_collapsed_key_count": len(phase_coeff),
        "positive_composition_multiplicity_verified": True,
        "owner_rows_verified_representationwise": True,
        "collapsed_boundary_equals_direct_exact": collapsed_bd == direct_bd,
        "omega_total": fstr(sum(omega.values(), Fraction(0))),
        "boundary_omega_total": fstr(sum((omega[s] for s in boundary), Fraction(0))),
        "boundary_omega_absolute_mass": fstr(sum((abs(omega[s]) for s in boundary), Fraction(0))),
        "metrics": {
            "full_DOR": metric(total, lags, bounds),
            "BODT_boundary": metric(direct_bd, lags, bounds),
            "interior": metric(direct_int, lags, bounds),
            "sum_of_min_owner_stratum_l1_upper": sum(metric(v, lags, bounds)["float"][1] for v in by_min.values()),
            "sum_of_T_D_l1_upper": sum(metric(v, lags, bounds)["float"][1] for v in by_kind.values()),
            "sum_of_T_S_N_l1_upper": sum(metric(v, lags, bounds)["float"][1] for v in collapsed_by_topology.values()),
        },
        "by_min_owner": {
            str(d): {
                "phase_coefficient_mass": fstr(coeff_by_min[d]),
                "lag_l1": metric(collapsed_by_min[d], lags, bounds),
                "lower_half_vector_float": [eval_float(collapsed_by_min[d][ell]) for ell in range(2, (n - 1) // 2 + 1)],
            }
            for d in sorted(collapsed_by_min)
        },
        "cumulative_min_owner_lag_l1": cumulative_metrics,
        "owner_column_candidate": {
            "S1_by_owner_size": s1_metrics,
            "S2_nonzero_pair_count": len(s2_nonzero),
            "S2_max_normalized_ratio": max_s2_ratio,
            "S2_max_pair": max_s2_key,
            "S2_small_owner_rows": s2_top,
            "all_rows_use_complete_boundary_omega_before_norm": True,
            "S1_arithmetic": "exact rational",
            "S2_arithmetic": "exact rational; d,e <= (k-1)/2 only",
        },
        "by_state_kind": {kind: metric(v, lags, bounds) for kind, v in sorted(by_kind.items())},
        "by_positive_composition_topology": {
            kind: metric(v, lags, bounds) for kind, v in sorted(collapsed_by_topology.items())
        },
        "by_channel_kind": {
            key: metric(v, lags, bounds) for key, v in sorted(channel_kind.items())
        },
        "boundary_lower_half_vector_float": [eval_float(direct_bd[ell]) for ell in range(2, (n - 1) // 2 + 1)],
        "boundary_vector_exact_sha256": vector_digest(direct_bd),
        "full_vector_exact_sha256": vector_digest(total),
        "inference": {
            "BODT": False,
            "DOR": False,
            "DSR_or_DTR": False,
            "PBV_FD_FCL1_gap_mixing_terminal": False,
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
