#!/usr/bin/env python3
"""M240 checker for generic Hurwitz identities only.

This file performs no tree generation, DPS closure, endpoint construction, or
finite-rank census. It checks only the algebraic identities used after IDL.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import platform
from pathlib import Path


OUTPUT = Path(__file__).with_name("symbolic_identity_results.json")


def edge(a, b):
    assert a != b
    return (a, b) if a < b else (b, a)


def conjugate(a, b):
    u, v = b

    def image(x):
        return v if x == u else u if x == v else x

    return edge(image(a[0]), image(a[1]))


def hurwitz(word, signed):
    j = abs(signed) - 1
    a, b = word[j : j + 2]
    out = list(word)
    if signed > 0:
        out[j : j + 2] = (b, conjugate(a, b))
    else:
        out[j : j + 2] = (conjugate(b, a), a)
    return tuple(out)


def act(word, route):
    for signed in route:
        word = hurwitz(word, signed)
    return word


def digest(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode()).hexdigest()


def main():
    labels = tuple(range(7))
    transpositions = tuple(edge(a, b) for a in labels for b in labels if a < b)

    positive_square = 0
    negative_square = 0
    for c in transpositions:
        for h in transpositions:
            assert act((c, h, h), (1, 2)) == (h, h, c)
            chc = conjugate(h, c)
            assert act((c, h, h), (-1, -2)) == (chc, chc, c)
            positive_square += 1
            negative_square += 1

    child_equalization = 0
    carrier = 0
    for x, y, z, n, u in itertools.permutations(labels, 5):
        cy, hy = edge(x, y), edge(u, y)
        cn, hn = edge(x, n), edge(u, n)
        common = edge(u, x)
        assert act((cy, hy, hy), (-1, -2)) == (common, common, cy)
        assert act((cn, hn, hn), (-1, -2)) == (common, common, cn)
        child_equalization += 1

        source = (edge(x, y), edge(z, x), edge(z, y), edge(z, n))
        target = (edge(x, n), edge(z, y), edge(z, y), edge(z, x))
        assert act(source, (-1, 2, -3, -2, -1)) == target
        carrier += 1

    disjoint_square = 0
    for x, y, n, a, b in itertools.permutations(labels, 5):
        h = edge(a, b)
        for c in (edge(x, y), edge(x, n)):
            assert act((c, h, h), (1, 2)) == (h, h, c)
            assert act((c, h, h), (-1, -2)) == (h, h, c)
            disjoint_square += 1

    double_inverse = 0
    for x, y, z in itertools.permutations(labels, 3):
        a, b = edge(x, y), edge(z, x)
        assert act((a, b, a), (-1, -1)) == (b, conjugate(b, a), a)
        double_inverse += 1

    single_inverse = 0
    for a in transpositions:
        for b in transpositions:
            assert act((a, b), (-1,)) == (conjugate(b, a), a)
            single_inverse += 1

    result = {
        "experiment": "M240 symbolic Hurwitz identities",
        "scope": "No DPS/tree/endpoint enumeration; IDL is not checked.",
        "checks": {
            "positive_square_transport": positive_square,
            "negative_square_transport": negative_square,
            "direct_child_equalization": child_equalization,
            "terminal_carrier": carrier,
            "disjoint_square_both_signs": disjoint_square,
            "double_inverse_boundary": double_inverse,
            "single_inverse_boundary": single_inverse,
        },
        "all_pass": True,
        "environment": {
            "python": platform.python_version(),
            "nonstandard_dependencies": {},
            "seed": None,
        },
    }
    result["normalized_digest"] = digest(result["checks"])
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

