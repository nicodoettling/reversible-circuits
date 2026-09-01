#!/usr/bin/env python3
"""Directly enumerate length-four transposition words in S_N.

Permutations are tuples p with p[i] equal to the image of i. The word
product t_1 ... t_m uses the right-action convention: apply t_1 first, then
t_2, and so on. Thus compose(p, q)[i] = q[p[i]].
"""

from itertools import product
import json


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return the product p q, applying p first and q second."""
    return tuple(q[p_i] for p_i in p)


def transpositions(n: int) -> tuple[tuple[int, ...], ...]:
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            permutation = list(range(n))
            permutation[i], permutation[j] = permutation[j], permutation[i]
            result.append(tuple(permutation))
    return tuple(result)


def count_identity_words(n: int, length: int = 4) -> int:
    identity = tuple(range(n))
    count = 0
    for word in product(transpositions(n), repeat=length):
        value = identity
        for factor in word:
            value = compose(value, factor)
        if value == identity:
            count += 1
    return count


def main() -> None:
    result = {
        "S3_m4": count_identity_words(3),
        "S4_m4": count_identity_words(4),
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
