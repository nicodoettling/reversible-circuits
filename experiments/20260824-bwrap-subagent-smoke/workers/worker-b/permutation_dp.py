#!/usr/bin/env python3
"""Exact four-step transposition-walk counts using permutation-state DP.

Permutations are tuples p with p[i] equal to the image of i.  Composition
compose(p, q) means p o q: apply q first, then p.  The DP appends each new
transposition on the right, so a path records the ordered product t1 t2 ... tm.
"""

from collections import Counter
import json


Permutation = tuple[int, ...]


def compose(p: Permutation, q: Permutation) -> Permutation:
    """Return p o q (q acts first)."""
    return tuple(p[q[i]] for i in range(len(p)))


def transpositions(n: int) -> list[Permutation]:
    result: list[Permutation] = []
    for i in range(n):
        for j in range(i + 1, n):
            permutation = list(range(n))
            permutation[i], permutation[j] = permutation[j], permutation[i]
            result.append(tuple(permutation))
    return result


def identity_count(n: int, steps: int = 4) -> int:
    identity = tuple(range(n))
    counts: Counter[Permutation] = Counter({identity: 1})
    generators = transpositions(n)
    for _ in range(steps):
        next_counts: Counter[Permutation] = Counter()
        for state, count in counts.items():
            for transposition in generators:
                next_counts[compose(state, transposition)] += count
        counts = next_counts
    return counts[identity]


def main() -> None:
    print(
        json.dumps(
            {
                "S3_m4": identity_count(3),
                "S4_m4": identity_count(4),
                "method": "permutation_state_dp",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
