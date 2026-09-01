#!/usr/bin/env python3
"""Exact bounded audit of Adin--Roichman maximal-interval incidence."""

from __future__ import annotations

import argparse
import collections
import json
import platform
import subprocess
import sys
from pathlib import Path

from cyclic_tree_action import Edge, conjugate_edge, minimal_words, transpositions


def phi_map(n: int, word: tuple[int, ...], edges: list[Edge]) -> tuple[int, ...]:
    # Adin--Roichman Observation 3.3 translated to zero-based labels.
    # sigma_(j+1) is the suffix strictly after factor j.
    suffix = tuple(range(n))
    answer = [0] * (n - 1)
    for j in range(n - 2, -1, -1):
        a, b = edges[word[j]]
        if a > b:
            a, b = b, a
        inverse = [0] * n
        for x, image in enumerate(suffix):
            inverse[image] = x
        answer[j] = inverse[a]
        # suffix <- t_j suffix, composition convention p after q.
        changed = list(suffix)
        for x, image in enumerate(suffix):
            changed[x] = b if image == a else a if image == b else image
        suffix = tuple(changed)
    if sorted(answer) != list(range(n - 1)):
        raise AssertionError("phi is not a permutation")
    return tuple(answer)


def inversions(pi: tuple[int, ...]) -> int:
    return sum(pi[i] > pi[j] for i in range(len(pi)) for j in range(i + 1, len(pi)))


def analyze(n: int) -> dict[str, object]:
    edges, gates = transpositions(n)
    edge_index = {edge: i for i, edge in enumerate(edges)}
    words = minimal_words(n, edges, gates)
    word_set = set(words)

    def right(word: tuple[int, ...], i: int) -> tuple[int, ...]:
        changed = list(word)
        # Adin--Roichman R_i slides t_i right: (a,b)->(b^a,a).
        changed[i] = edge_index[conjugate_edge(edges[word[i + 1]], edges[word[i]])]
        changed[i + 1] = word[i]
        target = tuple(changed)
        if target not in word_set:
            raise AssertionError("right Hurwitz move left state space")
        return target

    def left(word: tuple[int, ...], i: int) -> tuple[int, ...]:
        changed = list(word)
        # Adin--Roichman L_i slides t_(i+1) left: (a,b)->(b,b^(-1)ab).
        changed[i] = word[i + 1]
        changed[i + 1] = edge_index[conjugate_edge(edges[word[i]], edges[word[i + 1]])]
        target = tuple(changed)
        if target not in word_set:
            raise AssertionError("left Hurwitz move left state space")
        return target

    phi = {word: phi_map(n, word, edges) for word in words}
    rank = {word: inversions(phi[word]) for word in words}
    maximum_rank = (n - 1) * (n - 2) // 2
    maxima = [word for word in words if rank[word] == maximum_rank]

    down_neighbors: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
    for word in words:
        candidates = set()
        for i in range(n - 2):
            for target in (right(word, i), left(word, i)):
                if rank[target] == rank[word] - 1:
                    candidates.add(target)
        down_neighbors[word] = sorted(candidates)

    incidence = collections.Counter()
    interval_sizes = []
    interval_pair_overlaps = collections.Counter()
    intervals: list[set[tuple[int, ...]]] = []
    for maximum in maxima:
        seen = {maximum}
        stack = [maximum]
        while stack:
            word = stack.pop()
            for target in down_neighbors[word]:
                if target not in seen:
                    seen.add(target)
                    stack.append(target)
        intervals.append(seen)
        interval_sizes.append(len(seen))
        for word in seen:
            incidence[word] += 1
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            interval_pair_overlaps[len(intervals[i] & intervals[j])] += 1

    incidence_by_rank: dict[int, list[int]] = collections.defaultdict(list)
    for word in words:
        incidence_by_rank[rank[word]].append(incidence[word])
    serial_rank = {
        str(k): {
            "states": len(values),
            "min": min(values),
            "max": max(values),
            "mean": sum(values) / len(values),
            "distinct": sorted(set(values)),
        }
        for k, values in sorted(incidence_by_rank.items())
    }
    quotient_incidence = None
    if n % 2 == 1:
        def cyclic_conjugate(word: tuple[int, ...]) -> tuple[int, ...]:
            target = tuple(
                edge_index[
                    tuple(
                        sorted(
                            (
                                (edges[index][0] - 1) % n,
                                (edges[index][1] - 1) % n,
                            )
                        )
                    )
                ]
                for index in word
            )
            if target not in word_set:
                raise AssertionError("cyclic conjugation left state space")
            return target

        quotient_orbit: dict[tuple[int, ...], int] = {}
        orbit_profiles = []
        for word in words:
            if word in quotient_orbit:
                continue
            orbit_id = len(orbit_profiles)
            orbit = []
            current = word
            for _ in range(n):
                if current in quotient_orbit:
                    raise AssertionError("cyclic action was not free")
                quotient_orbit[current] = orbit_id
                orbit.append(current)
                current = cyclic_conjugate(current)
            if current != word:
                raise AssertionError("cyclic action did not have order n")
            orbit_profiles.append(tuple(incidence[state] for state in orbit))
        orbit_sums = [sum(profile) for profile in orbit_profiles]

        translated_block_images_invariant = True
        for interval in intervals:
            base_counts = collections.Counter(quotient_orbit[word] for word in interval)
            shifted_counts = collections.Counter(
                quotient_orbit[cyclic_conjugate(word)] for word in interval
            )
            if base_counts != shifted_counts:
                translated_block_images_invariant = False
                break
        quotient_incidence = {
            "quotient_orbits": len(orbit_sums),
            "orbit_summed_incidence_min": min(orbit_sums),
            "orbit_summed_incidence_max": max(orbit_sums),
            "orbit_summed_incidence_ratio": max(orbit_sums) / min(orbit_sums),
            "orbit_summed_incidence_mean": sum(orbit_sums) / len(orbit_sums),
            "distinct_orbit_summed_incidences": sorted(set(orbit_sums)),
            "first_max_profile": orbit_profiles[orbit_sums.index(max(orbit_sums))],
            "first_min_profile": orbit_profiles[orbit_sums.index(min(orbit_sums))],
            "projected_block_multiset_invariant_under_U_translation": (
                translated_block_images_invariant
            ),
        }
    return {
        "n": n,
        "states": len(words),
        "maximum_rank": maximum_rank,
        "maximal_elements": len(maxima),
        "expected_Catalan": len(maxima),
        "interval_size_set": sorted(set(interval_sizes)),
        "expected_interval_size_factorial": __import__("math").factorial(n - 1),
        "incidence_min": min(incidence.values()),
        "incidence_max": max(incidence.values()),
        "incidence_ratio": max(incidence.values()) / min(incidence.values()),
        "incidence_by_rank": serial_rank,
        "pairwise_interval_overlap_histogram": {
            str(k): interval_pair_overlaps[k] for k in sorted(interval_pair_overlaps)
        },
        "cyclic_quotient_incidence": quotient_incidence,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    parameters = sorted(set(args.n))
    payload = {
        "claim_tested": (
            "The Adin--Roichman maximal weak-order intervals form a uniformly "
            "bounded-overlap block cover suitable for direct spectral decomposition."
        ),
        "scope_warning": "Finite incidence ratios cannot prove asymptotic overlap bounds.",
        "convention": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "parameters": parameters,
        "results": [analyze(n) for n in parameters],
        "python": platform.python_version(),
        "seed": None,
        "deterministic": True,
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": " ".join(sys.argv),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
