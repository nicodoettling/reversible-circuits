#!/usr/bin/env python3
"""Exact falsifier for a universal two-hop adjacent-macro bypass.

The script enumerates parking functions, reconstructs their reduced
long-cycle factorization using Stanley's recursive inverse, builds the exact
nonlazy adjacent raw-pair heat-bath projection, and measures the best direct
or two-hop stationary-capacity route for every feasible adjacent unit
exchange of parking multiplicities.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


Partition = tuple[tuple[int, ...], ...]
Perm = tuple[int, ...]
Edge = tuple[int, int]
Macro = tuple[int, ...]


def compose(p: Perm, q: Perm) -> Perm:
    """Return p after q, so (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    answer = [0] * len(p)
    for x, image in enumerate(p):
        answer[image] = x
    return tuple(answer)


def partition_perm(partition: Partition) -> Perm:
    n = sum(len(block) for block in partition)
    p = list(range(n))
    for block in partition:
        if len(block) > 1:
            for x, image in zip(block, block[1:] + block[:1]):
                p[x] = image
    return tuple(p)


def transposition(n: int, edge: Edge) -> Perm:
    a, b = edge
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def normalize(blocks: list[set[int]]) -> Partition:
    return tuple(sorted(tuple(sorted(block)) for block in blocks))


def inverse_chain(a: tuple[int, ...]) -> tuple[Partition, ...]:
    """Stanley's inverse for a zero-based parking function."""
    r = len(a)
    if r == 0:
        return (((0,),),)
    largest = max(a)
    s = max(i for i, value in enumerate(a) if value == largest)
    smaller = inverse_chain(a[:s] + a[s + 1 :])
    new_vertex = largest + 1

    def relabel(partition: Partition) -> list[set[int]]:
        return [
            {x if x <= largest else x + 1 for x in block}
            for block in partition
        ]

    chain = []
    for new_rank in range(r + 1):
        if new_rank <= s:
            blocks = relabel(smaller[new_rank])
            blocks.append({new_vertex})
        else:
            blocks = relabel(smaller[new_rank - 1])
            target = next(i for i, block in enumerate(blocks) if largest in block)
            blocks[target].add(new_vertex)
        chain.append(normalize(blocks))
    return tuple(chain)


def factor_word(chain: tuple[Partition, ...]) -> tuple[Edge, ...]:
    word = []
    for rank in range(1, len(chain)):
        before = [set(block) for block in chain[rank - 1]]
        after = [set(block) for block in chain[rank]]
        merged = next(block for block in after if not any(block == old for old in before))
        pieces = [block for block in before if block < merged]
        if len(pieces) != 2 or pieces[0] | pieces[1] != merged:
            raise AssertionError("inverse chain is not a maximal-chain cover")
        before_perm = partition_perm(chain[rank - 1])
        after_perm = partition_perm(chain[rank])
        factor = compose(inverse(before_perm), after_perm)
        moved = [x for x, image in enumerate(factor) if x != image]
        if len(moved) != 2 or factor[moved[0]] != moved[1]:
            raise AssertionError("cover quotient is not a transposition")
        word.append(tuple(moved))
    return tuple(word)


def is_parking_word(a: tuple[int, ...]) -> bool:
    return all(value <= i for i, value in enumerate(sorted(a)))


def is_macro(macro: Macro) -> bool:
    return all(value <= i for i, value in enumerate(macro))


def orbit_weight(macro: Macro) -> int:
    counts = Counter(macro)
    ans = math.factorial(len(macro))
    for count in counts.values():
        ans //= math.factorial(count)
    return ans


def adjacent_ideal_edges(macros: set[Macro]) -> list[tuple[Macro, Macro]]:
    if not macros:
        return []
    r = len(next(iter(macros)))
    answer = []
    for source in sorted(macros):
        counts = [source.count(i) for i in range(r)]
        for i in range(r - 1):
            if counts[i] == 0:
                continue
            target_counts = counts.copy()
            target_counts[i] -= 1
            target_counts[i + 1] += 1
            target = tuple(
                value
                for value, multiplicity in enumerate(target_counts)
                for _ in range(multiplicity)
            )
            if target in macros:
                answer.append((source, target))
                answer.append((target, source))
    return sorted(set(answer))


def run(n: int, dump_edges: bool = False) -> dict:
    r = n - 1
    identity = tuple(range(n))
    cycle = tuple(list(range(1, n)) + [0])
    edges = [(a, b) for a in range(n) for b in range(a + 1, n)]
    edge_index = {edge: i for i, edge in enumerate(edges)}
    perms = [transposition(n, edge) for edge in edges]

    pair_fibers: dict[Perm, list[tuple[int, int]]] = defaultdict(list)
    for i, p in enumerate(perms):
        for j, q in enumerate(perms):
            pair_fibers[compose(p, q)].append((i, j))

    macro_words: dict[Macro, list[tuple[int, ...]]] = defaultdict(list)
    seen_words = set()
    for labels in itertools.product(range(r), repeat=r):
        if not is_parking_word(labels):
            continue
        word_edges = factor_word(inverse_chain(labels))
        word = tuple(edge_index[edge] for edge in word_edges)
        product = identity
        for index in word:
            product = compose(product, perms[index])
        if product != cycle:
            raise AssertionError("inverse word has wrong endpoint")
        if tuple(edge[0] for edge in word_edges) != labels:
            raise AssertionError("inverse word has wrong Stanley labels")
        if word in seen_words:
            raise AssertionError("inverse parking map is not injective")
        seen_words.add(word)
        macro_words[tuple(sorted(labels))].append(word)

    expected = n ** (n - 2)
    if len(seen_words) != expected:
        raise AssertionError("Dénes/parking count mismatch")
    for macro, words in macro_words.items():
        if len(words) != orbit_weight(macro):
            raise AssertionError("macro orbit size mismatch")

    rates: dict[tuple[Macro, Macro], Fraction] = defaultdict(Fraction)
    for source, words in macro_words.items():
        total: dict[Macro, Fraction] = defaultdict(Fraction)
        for word in words:
            for pos in range(r - 1):
                product = compose(perms[word[pos]], perms[word[pos + 1]])
                fiber = pair_fibers[product]
                increment = Fraction(1, (r - 1) * len(fiber))
                for first, second in fiber:
                    target_word = word[:pos] + (first, second) + word[pos + 2 :]
                    target = tuple(sorted(edges[index][0] for index in target_word))
                    if not is_macro(target):
                        raise AssertionError("heat-bath target macro is infeasible")
                    total[target] += increment
        for target, value in total.items():
            rates[source, target] = value / len(words)

    detailed_balance_failures = []
    for (source, target), rate in rates.items():
        lhs = orbit_weight(source) * rate
        rhs = orbit_weight(target) * rates.get((target, source), Fraction(0))
        if lhs != rhs:
            detailed_balance_failures.append(
                [list(source), list(target), str(lhs), str(rhs)]
            )
    if detailed_balance_failures:
        raise AssertionError("projected detailed balance failed")

    macros = set(macro_words)
    ideal_edges = adjacent_ideal_edges(macros)
    records = []
    no_two_hop = []
    for source, target in ideal_edges:
        source_weight = orbit_weight(source)
        direct = rates.get((source, target), Fraction(0))
        best_strength = direct
        best_path = [source, target] if direct else None
        best_edge_strengths = [direct] if direct else []
        for middle in macros:
            if middle in (source, target):
                continue
            first = rates.get((source, middle), Fraction(0))
            second = rates.get((middle, target), Fraction(0))
            if not first or not second:
                continue
            second_capacity_at_source = (
                Fraction(orbit_weight(middle), source_weight) * second
            )
            strength = min(first, second_capacity_at_source)
            if strength > best_strength:
                best_strength = strength
                best_path = [source, middle, target]
                best_edge_strengths = [first, second_capacity_at_source]
        if best_path is None:
            no_two_hop.append([list(source), list(target)])
        records.append(
            {
                "source": list(source),
                "target": list(target),
                "direct_rate": str(direct),
                "best_capacity_strength": str(best_strength),
                "best_path": [list(m) for m in best_path] if best_path else None,
                "path_edge_strengths": [str(x) for x in best_edge_strengths],
            }
        )

    positive_direct = [
        Fraction(record["direct_rate"])
        for record in records
        if Fraction(record["direct_rate"]) > 0
    ]
    strengths = [Fraction(record["best_capacity_strength"]) for record in records]
    worst_strength = min(strengths) if strengths else Fraction(1)
    worst_records = [
        record
        for record in records
        if Fraction(record["best_capacity_strength"]) == worst_strength
    ]
    result = {
        "n": n,
        "r": r,
        "factorizations": len(seen_words),
        "macros": len(macros),
        "projected_off_diagonal_edges": sum(
            source != target and rate > 0
            for (source, target), rate in rates.items()
        ),
        "directed_adjacent_ideal_edges": len(ideal_edges),
        "zero_direct_adjacent_edges": sum(
            Fraction(record["direct_rate"]) == 0 for record in records
        ),
        "minimum_positive_direct_rate": (
            str(min(positive_direct)) if positive_direct else None
        ),
        "no_direct_or_two_hop_edges": no_two_hop,
        "minimum_best_two_hop_capacity_strength": str(worst_strength),
        "worst_records": worst_records[:20],
    }
    if dump_edges:
        result["projected_rates"] = [
            {
                "source": list(source),
                "target": list(target),
                "rate": str(rate),
                "capacity_count": str(
                    orbit_weight(source) * rate * 3 * (r - 1)
                ),
            }
            for (source, target), rate in sorted(rates.items())
            if source != target and rate > 0
        ]
        result["ideal_edge_records"] = records
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=7)
    parser.add_argument("--dump-edges", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "claim_tested": (
            "Every feasible adjacent parking-macro unit exchange has a "
            "direct or two-hop actual projected path with inverse-polynomial "
            "stationary capacity."
        ),
        "universal_implication": (
            "A missing two-hop route refutes length-two universality; small "
            "positive rates only calibrate and cannot prove an asymptotic bound."
        ),
        "convention": "(pq)(x)=p(q(x)); tuple product left-to-right",
        "seed": None,
        "python": platform.python_version(),
        "records": [
            run(n, dump_edges=args.dump_edges) for n in range(3, args.n_max + 1)
        ],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
