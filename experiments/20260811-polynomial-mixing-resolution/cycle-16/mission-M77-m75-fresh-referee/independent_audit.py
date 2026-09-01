#!/usr/bin/env python3
"""Independent exact checks for the frozen M75 referee audit.

This file intentionally imports no M75 code.  It uses only the Python
standard library and writes a compact JSON record of finite, deterministic
checks.  The finite calculations audit finite claims and local algebra only;
they are not asymptotic mixing evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
import subprocess
import sys
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path


Permutation = tuple[int, ...]
Edge = tuple[int, int]
Word = tuple[Edge, ...]


def identity(n: int) -> Permutation:
    return tuple(range(n))


def compose(p: Permutation, q: Permutation) -> Permutation:
    """Return pq, so (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Permutation) -> Permutation:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def edge_perm(edge: Edge, n: int) -> Permutation:
    a, b = edge
    out = list(range(n))
    out[a], out[b] = out[b], out[a]
    return tuple(out)


def transpositions(n: int) -> tuple[Edge, ...]:
    return tuple((a, b) for a in range(n) for b in range(a + 1, n))


def eval_word(word: Word, n: int) -> Permutation:
    value = identity(n)
    for edge in word:
        value = compose(value, edge_perm(edge, n))
    return value


def product_perms(perms: tuple[Permutation, ...], n: int) -> Permutation:
    value = identity(n)
    for p in perms:
        value = compose(value, p)
    return value


def conjugate_edge(edge: Edge, by: Edge) -> Edge:
    a, b = edge
    u, v = by

    def act(x: int) -> int:
        if x == u:
            return v
        if x == v:
            return u
        return x

    return tuple(sorted((act(a), act(b))))  # type: ignore[return-value]


def hurwitz(word: Word, position: int, sign: int) -> Word:
    a, b = word[position : position + 2]
    if sign == 1:
        pair = (b, conjugate_edge(a, b))
    elif sign == -1:
        pair = (conjugate_edge(b, a), a)
    else:
        raise ValueError(sign)
    return word[:position] + pair + word[position + 2 :]


def connected_on(word: Word, labels: tuple[int, ...]) -> bool:
    if len(labels) <= 1:
        return True
    parent = {x: x for x in labels}

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    label_set = set(labels)
    for a, b in word:
        if a not in label_set or b not in label_set:
            continue
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    return len({find(x) for x in labels}) == 1


def macro_signature(word: Word, n: int) -> tuple[tuple[tuple[int, ...], int], ...]:
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in word:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    parts: dict[int, list[int]] = {}
    for x in range(n):
        parts.setdefault(find(x), []).append(x)
    answer = []
    for vertices in parts.values():
        vertex_set = set(vertices)
        weight = sum(a in vertex_set and b in vertex_set for a, b in word)
        answer.append((tuple(vertices), weight))
    return tuple(sorted(answer))


def direct_pairs(word: Word, n: int, connected_labels: tuple[int, ...]) -> list[dict]:
    answer = []
    for i, j in itertools.combinations(range(len(word)), 2):
        residual = word[:i] + word[i + 1 : j] + word[j + 1 :]
        if eval_word(residual, n) != identity(n):
            continue
        answer.append(
            {
                "positions": [i, j],
                "connected": connected_on(residual, connected_labels),
            }
        )
    return answer


def first_certificate(word: Word, n: int, labels: tuple[int, ...]) -> tuple[int, int] | None:
    for item in direct_pairs(word, n, labels):
        if item["connected"]:
            return tuple(item["positions"])  # type: ignore[return-value]
    return None


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def triple_fiber_audit() -> dict:
    rows = []
    for n in range(2, 9):
        edges = transpositions(n)
        edge_perms = {edge: edge_perm(edge, n) for edge in edges}
        counts: Counter[Permutation] = Counter()
        for a, b, c in itertools.product(edges, repeat=3):
            counts[product_perms((edge_perms[a], edge_perms[b], edge_perms[c]), n)] += 1
        m_edges = len(edges)
        formula = (3 * n * n + n - 12) // 2
        trans_counts = {counts[edge_perms[edge]] for edge in edges}
        assert trans_counts == {formula}
        assert max(counts.values()) <= m_edges * m_edges
        rows.append(
            {
                "N": n,
                "M": m_edges,
                "D_formula": formula,
                "transposition_fiber_counts": sorted(trans_counts),
                "maximum_nonempty_triple_fiber": max(counts.values()),
                "M_squared": m_edges * m_edges,
            }
        )
    return {
        "rows": rows,
        "identity_checked": "D_N=M+6(N-2)+2*binom(N-2,2)=(3N^2+N-12)/2",
        "all_transposition_fibers_match": True,
        "all_fibers_at_most_M_squared": True,
    }


def coarea_zero_length_audit() -> dict:
    # Gamma={0,1}, G={0}; the word law is half empty and half the swap.
    gamma = (0, 1)
    terminal = 2
    p = Fraction(1, 4)
    word_law = (((), Fraction(1, 2)), (("swap",), Fraction(1, 2)))

    def apply_step(x: int, _step: str) -> int:
        return 1 - x

    def apply_word(x: int, word: tuple[str, ...]) -> int:
        for step in word:
            x = apply_step(x, step)
        return x

    dbar = sum(mass * len(word) for word, mass in word_law)
    zero_mass = sum(mass for word, mass in word_law if not word)
    endpoint_success = {
        x: sum(mass for word, mass in word_law if apply_word(x, word) == 0)
        for x in gamma
    }
    prefix_success = {}
    for x in gamma:
        success = Fraction(0)
        for word, mass in word_law:
            cursor = x
            hit = cursor == 0
            for step in word:
                cursor = apply_step(cursor, step)
                hit = hit or cursor == 0
            if hit:
                success += mass
        prefix_success[x] = success
    eta_endpoint = min(endpoint_success.values())
    eta_prefix = min(prefix_success.values())
    kernel = {
        0: {0: Fraction(1, 2), 1: p, terminal: p},
        1: {0: p, 1: Fraction(3, 4), terminal: Fraction(0)},
    }
    subset_rows = []
    minimum_prefix_slack: Fraction | None = None
    minimum_endpoint_slack: Fraction | None = None
    for mask in range(1 << len(gamma)):
        subset = {gamma[i] for i in range(len(gamma)) if mask & (1 << i)}
        boundary = Fraction(0)
        for x in subset:
            for y, probability in kernel[x].items():
                if y == terminal or y not in subset:
                    boundary += probability
        prefix_rhs = p * eta_prefix * len(subset) / (dbar + 1)
        endpoint_rhs = p * eta_endpoint * len(subset) / max(dbar, Fraction(1))
        assert boundary >= prefix_rhs
        assert boundary >= endpoint_rhs
        prefix_slack = boundary - prefix_rhs
        endpoint_slack = boundary - endpoint_rhs
        minimum_prefix_slack = (
            prefix_slack
            if minimum_prefix_slack is None
            else min(minimum_prefix_slack, prefix_slack)
        )
        minimum_endpoint_slack = (
            endpoint_slack
            if minimum_endpoint_slack is None
            else min(minimum_endpoint_slack, endpoint_slack)
        )
        subset_rows.append(
            {
                "subset": sorted(subset),
                "boundary": fraction_text(boundary),
                "prefix_rhs": fraction_text(prefix_rhs),
                "endpoint_rhs": fraction_text(endpoint_rhs),
            }
        )
    return {
        "zero_length_mass": fraction_text(zero_mass),
        "expected_length": fraction_text(dbar),
        "prefix_success_by_source": {str(x): fraction_text(v) for x, v in prefix_success.items()},
        "endpoint_success_by_source": {str(x): fraction_text(v) for x, v in endpoint_success.items()},
        "eta_prefix": fraction_text(eta_prefix),
        "eta_endpoint": fraction_text(eta_endpoint),
        "prefix_denominator": fraction_text(dbar + 1),
        "endpoint_denominator": fraction_text(max(dbar, Fraction(1))),
        "all_subsets_checked": len(subset_rows),
        "minimum_prefix_slack": fraction_text(minimum_prefix_slack or Fraction(0)),
        "minimum_endpoint_slack": fraction_text(minimum_endpoint_slack or Fraction(0)),
        "subsets": subset_rows,
    }


def padded_h3_same_product(old: Word, new: Word, pair_position: int, n: int) -> bool:
    if len(old) != len(new) or len(old) < 3:
        return False
    start = pair_position if pair_position + 2 < len(old) else pair_position - 1
    if start < 0:
        return False
    if old[:start] != new[:start] or old[start + 3 :] != new[start + 3 :]:
        return False
    return eval_word(old[start : start + 3], n) == eval_word(new[start : start + 3], n)


def null_push_audit() -> dict:
    # Positive-genus component {0,1,2}; minimal component {3,4} is globally
    # interleaved inside U.  The chosen certificate has x != y.
    n = 5
    a, b, c, d = (0, 1), (1, 2), (0, 2), (3, 4)
    word: Word = (a, c, d, b, d, a, b, a)
    i, j = 1, 5
    x, y = word[i], word[j]
    p_part = word[:i]
    u_part = word[i + 1 : j]
    s_part = word[j + 1 :]
    residual = p_part + u_part + s_part
    assert eval_word(word, n) == identity(n)
    assert eval_word(residual, n) == identity(n)
    assert connected_on(residual, (0, 1, 2))
    original_macro = macro_signature(word, n)
    assert original_macro == (((0, 1, 2), 6), ((3, 4), 2))

    u_perm = eval_word(u_part, n)
    y_perm = edge_perm(y, n)
    forced_x = compose(compose(u_perm, y_perm), inverse(u_perm))
    assert forced_x == edge_perm(x, n)

    current = word
    path_rows = []
    for position in range(i, j - 1):
        target = hurwitz(current, position, 1)
        assert padded_h3_same_product(current, target, position, n)
        assert eval_word(target, n) == identity(n)
        assert macro_signature(target, n) == original_macro
        path_rows.append({"kind": "bubble", "pair_position": position})
        current = target
    expected_bubble = p_part + u_part + (y, y) + s_part
    assert current == expected_bubble

    square_position = len(p_part) + len(u_part)
    fixed_internal = c
    # Refresh yy -> ff, padded on the right in this example.
    refreshed = (
        current[:square_position]
        + (fixed_internal, fixed_internal)
        + current[square_position + 2 :]
    )
    assert padded_h3_same_product(current, refreshed, square_position, n)
    assert eval_word(refreshed, n) == identity(n)
    assert macro_signature(refreshed, n) == original_macro
    current = refreshed
    path_rows.append({"kind": "refresh", "pair_position": square_position})

    for _ in range(len(s_part)):
        old = current
        f1, f2, next_factor = old[square_position : square_position + 3]
        assert f1 == fixed_internal and f2 == fixed_internal
        current = (
            old[:square_position]
            + (next_factor, fixed_internal, fixed_internal)
            + old[square_position + 3 :]
        )
        assert padded_h3_same_product(old, current, square_position, n)
        assert eval_word(current, n) == identity(n)
        assert macro_signature(current, n) == original_macro
        path_rows.append({"kind": "slide", "pair_position": square_position})
        square_position += 1
    assert current == residual + (fixed_internal, fixed_internal)
    expected_length = (j - i - 1) + 1 + (len(word) - j - 1)
    assert len(path_rows) == expected_length == len(word) - i - 1

    # Reconstruct every position/y candidate over the fixed residual z.  The
    # equation x=U y U^{-1} gives at most C(m,2) M source descriptions.
    all_edges = transpositions(n)
    reconstructed: set[Word] = set()
    description_count = 0
    for left, right in itertools.combinations(range(len(word)), 2):
        p0 = residual[:left]
        u0 = residual[left : right - 1]
        s0 = residual[right - 1 :]
        u0_perm = eval_word(u0, n)
        for later in all_edges:
            early_perm = compose(
                compose(u0_perm, edge_perm(later, n)), inverse(u0_perm)
            )
            # Identify the unique swapped pair directly from the permutation.
            moved = [q for q in range(n) if early_perm[q] != q]
            assert len(moved) == 2
            early_edge = tuple(moved)  # type: ignore[assignment]
            candidate = p0 + (early_edge,) + u0 + (later,) + s0
            assert eval_word(candidate, n) == identity(n)
            reconstructed.add(candidate)
            description_count += 1
    bound = len(tuple(itertools.combinations(range(len(word)), 2))) * len(all_edges)
    assert description_count == bound
    assert len(reconstructed) <= bound
    return {
        "N": n,
        "m": len(word),
        "word": [list(edge) for edge in word],
        "certificate_positions": [i, j],
        "x": list(x),
        "y": list(y),
        "U": [list(edge) for edge in u_part],
        "residual": [list(edge) for edge in residual],
        "macro_signature": [[list(vertices), weight] for vertices, weight in original_macro],
        "x_equals_U_y_U_inverse": True,
        "bubble_endpoint": [list(edge) for edge in expected_bubble],
        "canonical_endpoint": [list(edge) for edge in current],
        "path_steps": path_rows,
        "path_length": len(path_rows),
        "claimed_length_formula": expected_length,
        "all_steps_literal_same_product_H3": True,
        "all_steps_preserve_identity_and_macro": True,
        "source_description_count": description_count,
        "distinct_reconstructed_sources": len(reconstructed),
        "binom_m_2_times_M_bound": bound,
    }


def radius_one_audit() -> dict:
    n = 6
    labels = tuple(range(5))
    word: Word = (
        (0, 1),
        (0, 2),
        (0, 3),
        (2, 4),
        (0, 2),
        (1, 4),
        (2, 4),
        (3, 4),
        (0, 2),
        (2, 4),
    )
    assert eval_word(word, n) == identity(n)
    assert connected_on(word, labels)
    signature = macro_signature(word, n)
    assert signature == (((0, 1, 2, 3, 4), 10), ((5,), 0))
    genus = len(word) // 2 - (len(labels) - 1)
    assert genus == 1
    source_pairs = direct_pairs(word, n, labels)
    assert [item["positions"] for item in source_pairs] == [[0, 5], [2, 7]]
    assert not any(item["connected"] for item in source_pairs)

    neighbors = set()
    radius_one_successes = []
    radius_two_successes = []
    for position in range(len(word) - 1):
        for sign in (-1, 1):
            target = hurwitz(word, position, sign)
            assert eval_word(target, n) == identity(n)
            assert macro_signature(target, n) == signature
            neighbors.add(target)
            certificate = first_certificate(target, n, labels)
            if certificate is not None:
                radius_one_successes.append([[position, sign], list(certificate)])
            for position2 in range(len(word) - 1):
                for sign2 in (-1, 1):
                    target2 = hurwitz(target, position2, sign2)
                    assert eval_word(target2, n) == identity(n)
                    certificate2 = first_certificate(target2, n, labels)
                    if certificate2 is not None:
                        radius_two_successes.append(
                            {
                                "moves": [[position, sign], [position2, sign2]],
                                "certificate": list(certificate2),
                            }
                        )
    assert not radius_one_successes
    assert len(radius_two_successes) == 104
    return {
        "ambient_N": n,
        "m": len(word),
        "word": [list(edge) for edge in word],
        "product_identity": True,
        "macro_signature": [[list(vertices), weight] for vertices, weight in signature],
        "positive_component_genus": genus,
        "source_identity_deletion_pairs": source_pairs,
        "signed_radius_one_paths": 2 * (len(word) - 1),
        "distinct_radius_one_endpoints": len(neighbors),
        "radius_one_certificate_paths": len(radius_one_successes),
        "signed_radius_two_paths": (2 * (len(word) - 1)) ** 2,
        "radius_two_certificate_paths": len(radius_two_successes),
        "first_radius_two_success": radius_two_successes[0],
        "exact_distance": 2,
    }


def reduced_positive_word(permutation: tuple[int, ...]) -> tuple[int, ...]:
    """A deterministic reduced adjacent-swap word for a permutation."""
    current = list(range(len(permutation)))
    word = []
    for destination, wanted in enumerate(permutation):
        source = current.index(wanted)
        while source > destination:
            word.append(source - 1)
            current[source - 1], current[source] = current[source], current[source - 1]
            source -= 1
    assert tuple(current) == permutation
    return tuple(word)


def inversion_count(permutation: tuple[int, ...]) -> int:
    return sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )


def marked_connected_square(word: Word, n: int) -> bool:
    labels = tuple(range(n))
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            continue
        residual = word[:i] + word[i + 2 :]
        if eval_word(residual, n) == identity(n) and connected_on(residual, labels):
            return True
    return False


def positive_braid_audit() -> dict:
    n, m = 3, 6
    edges = transpositions(n)
    gamma = [
        word
        for word in itertools.product(edges, repeat=m)
        if eval_word(word, n) == identity(n) and connected_on(word, tuple(range(n)))
    ]
    assert len(gamma) == 240
    state_index = {word: index for index, word in enumerate(gamma)}
    marked = {word for word in gamma if marked_connected_square(word, n)}
    permutations = list(itertools.permutations(range(m)))
    braid_words = [reduced_positive_word(p) for p in permutations]
    lengths = [len(word) for word in braid_words]
    assert all(length == inversion_count(p) for length, p in zip(lengths, permutations))
    assert sum(lengths) == len(permutations) * m * (m - 1) // 4

    row_counts = []
    distinct_endpoint_counts = []
    maximum_parallel_multiplicities = []
    column_degrees = [0] * len(gamma)
    noninvariance = None
    for source in gamma:
        endpoint_counter: Counter[Word] = Counter()
        marked_hits = 0
        for permutation, braid in zip(permutations, braid_words):
            target = source
            for generator in braid:
                target = hurwitz(target, generator, 1)
            assert target in state_index
            endpoint_counter[target] += 1
            column_degrees[state_index[target]] += 1
            is_marked = target in marked
            marked_hits += is_marked
            if noninvariance is None and ((source in marked) != is_marked):
                noninvariance = {
                    "source": [list(edge) for edge in source],
                    "target": [list(edge) for edge in target],
                    "source_marked": source in marked,
                    "target_marked": is_marked,
                    "permutation": list(permutation),
                    "positive_word": list(braid),
                }
        row_counts.append(marked_hits)
        distinct_endpoint_counts.append(len(endpoint_counter))
        maximum_parallel_multiplicities.append(max(endpoint_counter.values()))
    assert noninvariance is not None
    assert set(column_degrees) == {len(permutations)}
    assert sum(row_counts) == len(permutations) * len(marked)
    assert min(row_counts) == 608
    assert max(row_counts) == 720
    assert len(set(row_counts)) == 9
    assert min(distinct_endpoint_counts) == 15
    assert max(distinct_endpoint_counts) == 119
    assert set(maximum_parallel_multiplicities) == {12, 16, 24, 48}
    return {
        "N": n,
        "m": m,
        "Gamma_size": len(gamma),
        "marked_size": len(marked),
        "simple_positive_braids": len(permutations),
        "zero_length_braid_mass_numerator": sum(length == 0 for length in lengths),
        "zero_length_braid_mass_denominator": len(lengths),
        "mean_length": fraction_text(Fraction(sum(lengths), len(lengths))),
        "maximum_length": max(lengths),
        "row_marked_count_minimum": min(row_counts),
        "row_marked_count_maximum": max(row_counts),
        "row_marked_count_distinct_values": sorted(set(row_counts)),
        "row_marked_count_histogram": {
            str(key): value for key, value in sorted(Counter(row_counts).items())
        },
        "column_degree_distinct_values": sorted(set(column_degrees)),
        "double_count_left": sum(row_counts),
        "double_count_right": len(permutations) * len(marked),
        "distinct_endpoint_minimum": min(distinct_endpoint_counts),
        "distinct_endpoint_maximum": max(distinct_endpoint_counts),
        "maximum_parallel_multiplicity_values": sorted(set(maximum_parallel_multiplicities)),
        "marked_set_noninvariance_witness": noninvariance,
    }


def permutation_compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[i]] for i in range(len(p)))


def garside_coxeter_audit() -> dict:
    # At the Coxeter/simple-braid level, q=w0 p^{-1} has
    # q p=w0 and l(q)+l(p)=l(w0).  Hence reduced positive lifts concatenate
    # to Delta.  This audits the precise algebra used in the report.
    m = 6
    w0 = tuple(reversed(range(m)))
    longest_length = m * (m - 1) // 2
    checked = 0
    nontrivial_inverse_positive_failures = 0
    for p in itertools.permutations(range(m)):
        q = permutation_compose(w0, inverse(p))
        assert permutation_compose(q, p) == w0
        assert inversion_count(q) + inversion_count(p) == longest_length
        # The exponent sum of a nonidentity positive simple braid is positive,
        # while its inverse has negative exponent sum and is not positive.
        if inversion_count(p) > 0:
            nontrivial_inverse_positive_failures += 1
        checked += 1
    return {
        "strand_count": m,
        "simple_braids_checked": checked,
        "longest_length": longest_length,
        "left_complement_identity": "q=w0*p^{-1}; q*p=w0",
        "length_additivity_checked": True,
        "nonidentity_simple_braids_whose_inverse_is_not_positive_by_exponent_sum": nontrivial_inverse_positive_failures,
    }


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--m75-report", type=Path, required=True)
    parser.add_argument("--m75-manifest", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        commit = "unavailable"
    report_hash = sha256(args.m75_report)
    manifest_hash = sha256(args.m75_manifest)
    assert report_hash == "e699e8b54684488ae34a8df87edea5f9a88002939e34d9facc55c549b741ed39"
    assert manifest_hash == "17bb22b3c041ec1917f206d0a3cf9a8fba2f049fd5a6b61da2eb004699a6b89b"
    payload = {
        "argv": sys.argv,
        "commit": commit,
        "python": platform.python_version(),
        "seed": None,
        "nonstandard_dependencies": {},
        "convention": "(pq)(x)=p(q(x)); left-to-right tuple products; R(a,b)=(b,bab)",
        "scope_warning": "Finite checks audit finite claims and local algebra only; they do not prove an asymptotic row bound, conductance, gap, or mixing theorem.",
        "frozen_hashes": {
            "M75_report": report_hash,
            "M75_freeze_manifest": manifest_hash,
        },
        "triple_fibers": triple_fiber_audit(),
        "coarea_zero_length": coarea_zero_length_audit(),
        "null_push": null_push_audit(),
        "radius_one_obstruction": radius_one_audit(),
        "positive_braid_incidence": positive_braid_audit(),
        "garside_coxeter": garside_coxeter_audit(),
    }
    payload["elapsed_seconds"] = time.perf_counter() - started
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "elapsed_seconds": payload["elapsed_seconds"],
                "radius_two_hits": payload["radius_one_obstruction"]["radius_two_certificate_paths"],
                "braid_row_range": [
                    payload["positive_braid_incidence"]["row_marked_count_minimum"],
                    payload["positive_braid_incidence"]["row_marked_count_maximum"],
                ],
                "status": "all assertions passed",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
