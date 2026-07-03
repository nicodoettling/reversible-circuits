#!/usr/bin/env python3
"""Exact enumeration and diagnostics for identity transposition words in S_N.

Permutation convention:
    A permutation is a tuple p with p[x] = image of x.
    multiply(p, q) means p*q = p after q, so (p*q)[x] = p[q[x]].
    A word (t1, ..., tm) is evaluated as (((id*t1)*t2)*...*tm).

This convention is documented so sampler candidates can compare products
without relying on implicit left/right action choices. Identity membership is
unchanged by the opposite convention for these smoke cases, but Hurwitz move
validation uses the convention above.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
import time
from collections import Counter, deque
from pathlib import Path
from typing import Iterable


EXPECTED = {
    (3, 4): {"identity_count": 27, "hurwitz_component_count": 4},
    (4, 4): {"identity_count": 120, "hurwitz_component_count": 13},
    (4, 6): {"identity_count": 3936, "hurwitz_component_count": 17},
}


def all_transpositions(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def transposition_label(t: tuple[int, int]) -> str:
    return f"({t[0] + 1} {t[1] + 1})"


def word_labels(word: tuple[int, ...], transpositions: list[tuple[int, int]]) -> list[str]:
    return [transposition_label(transpositions[i]) for i in word]


def right_multiply_transposition(
    p: tuple[int, ...], t: tuple[int, int]
) -> tuple[int, ...]:
    """Return p*t where t is a transposition."""
    i, j = t
    q = list(p)
    q[i], q[j] = p[j], p[i]
    return tuple(q)


def eval_word(
    n: int, transpositions: list[tuple[int, int]], word: Iterable[int]
) -> tuple[int, ...]:
    p = tuple(range(n))
    for idx in word:
        p = right_multiply_transposition(p, transpositions[idx])
    return p


def apply_transposition_to_point(x: int, t: tuple[int, int]) -> int:
    a, b = t
    if x == a:
        return b
    if x == b:
        return a
    return x


def conjugate_transposition_by(
    a: tuple[int, int], b: tuple[int, int]
) -> tuple[int, int]:
    """Return b^-1*a*b. Since b is an involution, map endpoints of a by b."""
    x = apply_transposition_to_point(a[0], b)
    y = apply_transposition_to_point(a[1], b)
    if x == y:
        raise ValueError("conjugation collapsed a transposition")
    return (x, y) if x < y else (y, x)


def cycle_type(p: tuple[int, ...]) -> tuple[int, ...]:
    seen = [False] * len(p)
    lengths: list[int] = []
    for start in range(len(p)):
        if seen[start]:
            continue
        current = start
        length = 0
        while not seen[current]:
            seen[current] = True
            length += 1
            current = p[current]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def cycle_type_label(p: tuple[int, ...]) -> str:
    return ",".join(str(part) for part in cycle_type(p))


class DisjointSet:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1


def support_components(
    n: int, transpositions: list[tuple[int, int]], word: tuple[int, ...]
) -> list[dict[str, object]]:
    dsu = DisjointSet(n)
    for idx in word:
        i, j = transpositions[idx]
        dsu.union(i, j)

    vertices_by_root: dict[int, list[int]] = {}
    for v in range(n):
        vertices_by_root.setdefault(dsu.find(v), []).append(v)

    edge_counts: Counter[int] = Counter()
    for idx in word:
        i, _ = transpositions[idx]
        edge_counts[dsu.find(i)] += 1

    components = []
    for root, vertices in vertices_by_root.items():
        components.append(
            {
                "vertices_1_based": [v + 1 for v in sorted(vertices)],
                "vertex_count": len(vertices),
                "factor_count": edge_counts[root],
            }
        )
    components.sort(key=lambda c: (c["vertices_1_based"][0], c["vertex_count"]))
    return components


def weighted_component_invariant(
    n: int, transpositions: list[tuple[int, int]], word: tuple[int, ...]
) -> str:
    parts = []
    for component in support_components(n, transpositions, word):
        vertices = ".".join(str(v) for v in component["vertices_1_based"])
        parts.append(f"{vertices}:{component['factor_count']}")
    return "|".join(parts)


def component_shape_invariant(
    n: int, transpositions: list[tuple[int, int]], word: tuple[int, ...]
) -> str:
    shape = sorted(
        (
            int(component["vertex_count"]),
            int(component["factor_count"]),
        )
        for component in support_components(n, transpositions, word)
    )
    return "|".join(f"{vertices}:{factors}" for vertices, factors in shape)


def edge_multiplicity_histogram_label(word: tuple[int, ...]) -> str:
    counts = Counter(word)
    hist = Counter(counts.values())
    return "|".join(f"{multiplicity}:{hist[multiplicity]}" for multiplicity in sorted(hist))


def enumerate_identity_words(
    n: int,
    m: int,
    transpositions: list[tuple[int, int]],
    max_total_words: int,
) -> list[tuple[int, ...]]:
    total_words = len(transpositions) ** m
    if total_words > max_total_words:
        raise ValueError(
            f"S_{n}, m={m} has {total_words} words, above --max-total-words={max_total_words}"
        )

    identity = tuple(range(n))
    identity_words: list[tuple[int, ...]] = []
    for word in itertools.product(range(len(transpositions)), repeat=m):
        if eval_word(n, transpositions, word) == identity:
            identity_words.append(word)
    return identity_words


def hurwitz_neighbors(
    word: tuple[int, ...],
    transpositions: list[tuple[int, int]],
    transposition_to_index: dict[tuple[int, int], int],
) -> Iterable[tuple[int, ...]]:
    for i in range(len(word) - 1):
        a_idx = word[i]
        b_idx = word[i + 1]
        a = transpositions[a_idx]
        b = transpositions[b_idx]

        right = list(word)
        right[i] = b_idx
        right[i + 1] = transposition_to_index[conjugate_transposition_by(a, b)]
        yield tuple(right)

        inverse = list(word)
        inverse[i] = transposition_to_index[conjugate_transposition_by(b, a)]
        inverse[i + 1] = a_idx
        yield tuple(inverse)


def hurwitz_components(
    n: int,
    transpositions: list[tuple[int, int]],
    identity_words: list[tuple[int, ...]],
) -> dict[str, object]:
    word_set = set(identity_words)
    unseen = set(identity_words)
    transposition_to_index = {t: i for i, t in enumerate(transpositions)}
    components: list[list[tuple[int, ...]]] = []
    directed_neighbor_checks = 0

    while unseen:
        start = unseen.pop()
        queue: deque[tuple[int, ...]] = deque([start])
        members = [start]
        while queue:
            word = queue.popleft()
            for neighbor in hurwitz_neighbors(word, transpositions, transposition_to_index):
                directed_neighbor_checks += 1
                if neighbor not in word_set:
                    raise AssertionError(
                        f"Hurwitz neighbor left the exact identity set: {word} -> {neighbor}"
                    )
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    queue.append(neighbor)
                    members.append(neighbor)
        components.append(members)

    component_records = []
    for idx, members in enumerate(sorted(components, key=lambda c: (-len(c), c[0]))):
        invariant_counts = Counter(
            weighted_component_invariant(n, transpositions, word) for word in members
        )
        shape_counts = Counter(
            component_shape_invariant(n, transpositions, word) for word in members
        )
        component_records.append(
            {
                "component_id": idx,
                "size": len(members),
                "representative": word_labels(min(members), transpositions),
                "weighted_component_invariants": dict(sorted(invariant_counts.items())),
                "shape_invariants": dict(sorted(shape_counts.items())),
            }
        )

    size_histogram = Counter(str(len(component)) for component in components)
    return {
        "component_count": len(components),
        "component_size_histogram": dict(sorted(size_histogram.items(), key=lambda x: int(x[0]))),
        "components": component_records,
        "directed_neighbor_checks": directed_neighbor_checks,
    }


def counter_to_json(counter: Counter) -> dict[str, int]:
    return {str(k): int(v) for k, v in sorted(counter.items(), key=lambda x: str(x[0]))}


def prefix_cycle_type_counts(
    n: int, transpositions: list[tuple[int, int]], words: list[tuple[int, ...]], m: int
) -> list[dict[str, int]]:
    counts = [Counter() for _ in range(m + 1)]
    for word in words:
        p = tuple(range(n))
        counts[0][cycle_type_label(p)] += 1
        for pos, idx in enumerate(word, start=1):
            p = right_multiply_transposition(p, transpositions[idx])
            counts[pos][cycle_type_label(p)] += 1
    return [counter_to_json(counter) for counter in counts]


def per_position_transposition_counts(
    transpositions: list[tuple[int, int]], words: list[tuple[int, ...]], m: int
) -> list[dict[str, int]]:
    counts = [Counter() for _ in range(m)]
    for word in words:
        for pos, idx in enumerate(word):
            counts[pos][transposition_label(transpositions[idx])] += 1
    return [counter_to_json(counter) for counter in counts]


def window_cycle_type_counts(
    n: int, transpositions: list[tuple[int, int]], words: list[tuple[int, ...]], m: int
) -> dict[str, list[dict[str, int]]]:
    result: dict[str, list[dict[str, int]]] = {}
    for window_len in (2, 3):
        if window_len > m:
            continue
        by_start = [Counter() for _ in range(m - window_len + 1)]
        for word in words:
            for start in range(m - window_len + 1):
                p = eval_word(n, transpositions, word[start : start + window_len])
                by_start[start][cycle_type_label(p)] += 1
        result[str(window_len)] = [counter_to_json(counter) for counter in by_start]
    return result


def word_stat_distributions(
    n: int, transpositions: list[tuple[int, int]], words: list[tuple[int, ...]]
) -> dict[str, object]:
    adjacent_repeat_counts = Counter()
    support_shape_counts = Counter()
    weighted_component_counts = Counter()
    edge_hist_counts = Counter()
    support_edge_count_counts = Counter()

    adjacent_repeat_total = 0
    adjacent_slots = 0
    for word in words:
        adjacent_repeats = sum(1 for i in range(len(word) - 1) if word[i] == word[i + 1])
        adjacent_repeat_total += adjacent_repeats
        adjacent_slots += max(0, len(word) - 1)
        adjacent_repeat_counts[adjacent_repeats] += 1
        support_shape_counts[component_shape_invariant(n, transpositions, word)] += 1
        weighted_component_counts[weighted_component_invariant(n, transpositions, word)] += 1
        edge_hist_counts[edge_multiplicity_histogram_label(word)] += 1
        support_edge_count_counts[len(set(word))] += 1

    return {
        "adjacent_repeat_count_distribution": counter_to_json(adjacent_repeat_counts),
        "adjacent_repeat_rate": (
            adjacent_repeat_total / adjacent_slots if adjacent_slots else None
        ),
        "support_shape_distribution": counter_to_json(support_shape_counts),
        "weighted_component_invariant_distribution": counter_to_json(weighted_component_counts),
        "edge_multiplicity_histogram_distribution": counter_to_json(edge_hist_counts),
        "support_edge_count_distribution": counter_to_json(support_edge_count_counts),
    }


def run_case(n: int, m: int, max_total_words: int) -> dict[str, object]:
    start = time.perf_counter()
    transpositions = all_transpositions(n)
    total_words = len(transpositions) ** m
    identity_words = enumerate_identity_words(n, m, transpositions, max_total_words)
    hurwitz = hurwitz_components(n, transpositions, identity_words)
    elapsed = time.perf_counter() - start

    record: dict[str, object] = {
        "record_type": "case_summary",
        "target_distribution": "fixed-length uniform bridge on identity transposition words",
        "multiplication_convention": "tuple p maps x to p[x]; word product is (((id*t1)*t2)*...*tm) with (p*t)[x]=p[t[x]]",
        "N": n,
        "m": m,
        "transposition_count": len(transpositions),
        "transpositions_1_based": [transposition_label(t) for t in transpositions],
        "total_words": total_words,
        "identity_count": len(identity_words),
        "identity_density": len(identity_words) / total_words if total_words else math.nan,
        "prefix_cycle_type_counts": prefix_cycle_type_counts(
            n, transpositions, identity_words, m
        ),
        "per_position_transposition_counts": per_position_transposition_counts(
            transpositions, identity_words, m
        ),
        "window_cycle_type_counts": window_cycle_type_counts(
            n, transpositions, identity_words, m
        ),
        "word_stat_distributions": word_stat_distributions(
            n, transpositions, identity_words
        ),
        "hurwitz": hurwitz,
        "elapsed_seconds": elapsed,
    }

    expected = EXPECTED.get((n, m))
    if expected:
        record["expected"] = expected
        record["validation"] = {
            "identity_count_matches": len(identity_words) == expected["identity_count"],
            "hurwitz_component_count_matches": (
                hurwitz["component_count"] == expected["hurwitz_component_count"]
            ),
        }
    else:
        record["expected"] = None
        record["validation"] = None

    return record


def parse_case(case: str) -> tuple[int, int]:
    normalized = case.replace(",", ":").replace("x", ":")
    parts = normalized.split(":")
    if len(parts) != 2:
        raise argparse.ArgumentTypeError(f"case must be N:m, got {case!r}")
    n, m = (int(parts[0]), int(parts[1]))
    if n < 2:
        raise argparse.ArgumentTypeError("N must be at least 2")
    if m < 0:
        raise argparse.ArgumentTypeError("m must be nonnegative")
    return n, m


def write_jsonl(path: Path, records: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            json.dump(record, handle, sort_keys=True)
            handle.write("\n")


def format_bool(value: object) -> str:
    if value is True:
        return "yes"
    if value is False:
        return "no"
    return "n/a"


def write_report(path: Path, records: list[dict[str, object]], command: str) -> None:
    lines: list[str] = []
    lines.append("# Worker A Exact Enumeration Harness")
    lines.append("")
    lines.append("## Objective")
    lines.append("")
    lines.append(
        "Build a small exact reference harness for fixed-length identity transposition words in `S_N`, "
        "with diagnostics that sampler candidates can compare against."
    )
    lines.append("")
    lines.append("Target distribution: uniform on")
    lines.append("")
    lines.append("```text")
    lines.append("Omega(N,m) = { (t1, ..., tm) : each ti is a transposition in S_N and t1...tm = id }.")
    lines.append("```")
    lines.append("")
    lines.append("## Implementation Summary")
    lines.append("")
    lines.append(
        "The script `exact_identity_harness.py` is self-contained Python and uses no third-party packages. "
        "It enumerates all transposition words for each requested small case, filters identity words by exact "
        "tuple-permutation arithmetic, and builds the pure Hurwitz graph on the retained identity words."
    )
    lines.append("")
    lines.append(
        "Multiplication convention: permutations are tuples `p[x] = image of x`; a word is evaluated as "
        "`(((id*t1)*t2)*...*tm)`, with `(p*t)[x] = p[t[x]]` for a transposition `t`."
    )
    lines.append("")
    lines.append("## Commands Run")
    lines.append("")
    lines.append("```bash")
    lines.append(command)
    lines.append("```")
    lines.append("")
    lines.append("## Exact Counts")
    lines.append("")
    lines.append("| Case | Total words | Identity words | Expected | Hurwitz components | Expected components | Validated |")
    lines.append("|---|---:|---:|---:|---:|---:|---|")
    for record in records:
        expected = record.get("expected") or {}
        validation = record.get("validation") or {}
        hurwitz = record["hurwitz"]
        identity_ok = format_bool(validation.get("identity_count_matches"))
        component_ok = format_bool(validation.get("hurwitz_component_count_matches"))
        lines.append(
            f"| `S_{record['N']}, m={record['m']}` "
            f"| {record['total_words']} "
            f"| {record['identity_count']} "
            f"| {expected.get('identity_count', 'n/a')} "
            f"| {hurwitz['component_count']} "
            f"| {expected.get('hurwitz_component_count', 'n/a')} "
            f"| count {identity_ok}; components {component_ok} |"
        )
    lines.append("")
    lines.append("## Diagnostics Implemented")
    lines.append("")
    lines.append("- identity-word count and density among all transposition words")
    lines.append("- Hurwitz component count, size histogram, representatives, and invariant checks")
    lines.append("- prefix cycle-type counts at every prefix length")
    lines.append("- per-position transposition frequencies")
    lines.append("- adjacent-repeat count distribution and aggregate adjacent-repeat rate")
    lines.append("- support graph component-shape and weighted labeled component-invariant distributions")
    lines.append("- support-edge count and edge-multiplicity histogram distributions")
    lines.append("- length-2 and length-3 window product cycle-type counts")
    lines.append("")
    lines.append("## Selected Diagnostics")
    lines.append("")
    for record in records:
        hurwitz = record["hurwitz"]
        stats = record["word_stat_distributions"]
        lines.append(f"### `S_{record['N']}, m={record['m']}`")
        lines.append("")
        lines.append(f"- identity density: `{record['identity_density']:.12g}`")
        lines.append(f"- Hurwitz component size histogram: `{hurwitz['component_size_histogram']}`")
        lines.append(
            f"- adjacent repeat distribution: `{stats['adjacent_repeat_count_distribution']}`"
        )
        lines.append(f"- support shape distribution: `{stats['support_shape_distribution']}`")
        lines.append("")
    lines.append("## Limitations")
    lines.append("")
    lines.append(
        "This is direct word enumeration, so it is only intended for small `N,m`. "
        "The default guard refuses cases above `--max-total-words` total words. "
        "No sampler is implemented here, and no mixing-time claim is made from the Hurwitz components."
    )
    lines.append("")
    lines.append("## Next Steps")
    lines.append("")
    lines.append(
        "Use `results.jsonl` as an exact baseline for sampler runs. A sampler comparison script can consume the "
        "prefix cycle-type, per-position, support-shape, edge-multiplicity, and adjacent-repeat distributions as "
        "reference marginals."
    )
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cases",
        nargs="+",
        type=parse_case,
        default=[(3, 4), (4, 4), (4, 6)],
        help="Cases as N:m, for example --cases 3:4 4:4 4:6",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results.jsonl"),
        help="JSONL output path",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("report.md"),
        help="Markdown report path",
    )
    parser.add_argument(
        "--max-total-words",
        type=int,
        default=2_000_000,
        help="Safety guard for direct enumeration",
    )
    args = parser.parse_args(argv)

    records = [run_case(n, m, args.max_total_words) for n, m in args.cases]
    write_jsonl(args.output, records)
    command = "python3 " + " ".join(sys.argv)
    write_report(args.report, records, command)

    failures = []
    for record in records:
        validation = record.get("validation")
        if validation and not all(validation.values()):
            failures.append((record["N"], record["m"], validation))

    if failures:
        print(f"validation failures: {failures}", file=sys.stderr)
        return 1

    for record in records:
        hurwitz = record["hurwitz"]
        print(
            f"S_{record['N']}, m={record['m']}: "
            f"{record['identity_count']} identity words, "
            f"{hurwitz['component_count']} Hurwitz components"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
