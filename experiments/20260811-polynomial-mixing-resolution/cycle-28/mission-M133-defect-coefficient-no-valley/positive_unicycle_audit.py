#!/usr/bin/env python3
"""Audit a subtraction-free unique-cycle expansion for M125 incidence weights.

For fixed indexed cycle atoms, an ordered pair of partitions is represented by
its bipartite incidence multigraph.  On the connected diagonal V=E this graph
is unicyclic.  The unique cycle and the planted trees attached to its vertices
give a positive recurrence.  This script implements that recurrence and checks
it against literal ordered pairs of set partitions in exact arithmetic.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import itertools
import json
import platform
import subprocess
import time
from fractions import Fraction
from pathlib import Path


Poly = dict[tuple[int, int], Fraction]


def integer_partitions(n: int, minimum: int = 1):
    if n == 0:
        yield ()
        return
    for first in range(minimum, n + 1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


@functools.cache
def set_partitions(items: tuple[int, ...]) -> tuple[tuple[tuple[int, ...], ...], ...]:
    if not items:
        return ((),)
    first, rest = items[0], items[1:]
    output = []
    for partition in set_partitions(rest):
        output.append(((first,),) + partition)
        for index in range(len(partition)):
            blocks = list(partition)
            blocks[index] = tuple(sorted((first,) + blocks[index]))
            output.append(tuple(sorted(blocks)))
    # The insertion recursion can create identical block orderings; canonical
    # sorting and a set remove only representation duplicates, not objects.
    return tuple(sorted(set(output)))


def multiply(first: Poly, second: Poly) -> Poly:
    output: Poly = {}
    for (l1, r1), x in first.items():
        for (l2, r2), y in second.items():
            key = (l1 + l2, r1 + r2)
            output[key] = output.get(key, Fraction(0)) + x * y
    return output


def scale(poly: Poly, factor: Fraction, shift: tuple[int, int]) -> Poly:
    dl, dr = shift
    return {(l + dl, r + dr): factor * value for (l, r), value in poly.items()}


def add_into(target: Poly, source: Poly) -> None:
    for key, value in source.items():
        target[key] = target.get(key, Fraction(0)) + value


def block_weight(atom_sizes: tuple[int, ...], incident: tuple[int, ...]) -> Fraction:
    label_size = sum(atom_sizes[index] for index in incident)
    return Fraction(label_size, 1) ** (len(incident) - 3)


def positive_unicycle_by_core(atom_sizes: tuple[int, ...]) -> dict[int, Poly]:
    """Connected-unicyclic diagonal, separated by unique core length."""
    edges = tuple(range(len(atom_sizes)))

    @functools.cache
    def planted(
        colour: int, boundaries: tuple[int, ...], internal: tuple[int, ...]
    ) -> tuple[tuple[tuple[int, int], Fraction], ...]:
        """Tree forest below one vertex with one or two boundary edges.

        `colour=0` is left and `colour=1` is right.  Boundary edges meet the
        root vertex but lead outside this planted object.  Every internal edge
        belongs to exactly one child branch.
        """
        output: Poly = {}
        for partition in set_partitions(internal):
            choices = itertools.product(*partition) if partition else [()]
            for child_roots in choices:
                incident = tuple(sorted(boundaries + tuple(child_roots)))
                product: Poly = {(0, 0): Fraction(1)}
                for block, child in zip(partition, child_roots):
                    descendants = tuple(value for value in block if value != child)
                    child_poly = dict(planted(1 - colour, (child,), descendants))
                    product = multiply(product, child_poly)
                root_shift = (1, 0) if colour == 0 else (0, 1)
                add_into(
                    output,
                    scale(product, block_weight(atom_sizes, incident), root_shift),
                )
        return tuple(sorted(output.items()))

    result: dict[int, Poly] = {}
    edge_set = set(edges)
    # A bipartite core cycle has 2k labelled edges.  Fix its least edge first;
    # then require the next edge to share the left core vertex.  The left/right
    # colours distinguish the two orientations, so every ordered pair of
    # partitions has exactly one resulting sequence.
    for core_size in range(2, len(edges) + 1, 2):
        core_result: Poly = {}
        for core in itertools.combinations(edges, core_size):
            first = min(core)
            remainder = tuple(value for value in core if value != first)
            off_core = tuple(sorted(edge_set.difference(core)))
            for tail in itertools.permutations(remainder):
                sequence = (first,) + tail
                left_pairs = [
                    (sequence[index], sequence[index + 1])
                    for index in range(0, core_size, 2)
                ]
                right_pairs = [
                    (sequence[index], sequence[(index + 1) % core_size])
                    for index in range(1, core_size, 2)
                ]
                vertices = [(0, pair) for pair in left_pairs] + [
                    (1, pair) for pair in right_pairs
                ]
                for destinations in itertools.product(
                    range(core_size), repeat=len(off_core)
                ):
                    assigned = [[] for _ in range(core_size)]
                    for edge, destination in zip(off_core, destinations):
                        assigned[destination].append(edge)
                    product: Poly = {(0, 0): Fraction(1)}
                    for index, (colour, boundaries) in enumerate(vertices):
                        vertex_poly = dict(
                            planted(
                                colour,
                                tuple(sorted(boundaries)),
                                tuple(sorted(assigned[index])),
                            )
                        )
                        product = multiply(product, vertex_poly)
                    add_into(core_result, product)
        result[core_size] = core_result
    return result


def positive_unicycle(atom_sizes: tuple[int, ...]) -> Poly:
    """Connected-unicyclic diagonal by a unique core plus planted trees."""
    result: Poly = {}
    for core_poly in positive_unicycle_by_core(atom_sizes).values():
        add_into(result, core_poly)
    return result


def connected_diagonal_direct(atom_sizes: tuple[int, ...]) -> Poly:
    """Literal ordered-pair partition enumeration, independent of core DP."""
    edges = tuple(range(len(atom_sizes)))
    result: Poly = {}
    for left in set_partitions(edges):
        for right in set_partitions(edges):
            if len(left) + len(right) != len(edges):
                continue
            parent = list(range(len(edges)))

            def find(value: int) -> int:
                while parent[value] != value:
                    parent[value] = parent[parent[value]]
                    value = parent[value]
                return value

            def union(a: int, b: int) -> None:
                ra, rb = find(a), find(b)
                if ra != rb:
                    parent[rb] = ra

            for partition in (left, right):
                for block in partition:
                    for value in block[1:]:
                        union(block[0], value)
            if len({find(value) for value in edges}) != 1:
                continue
            weight = Fraction(1)
            for block in left + right:
                weight *= block_weight(atom_sizes, block)
            key = (len(left), len(right))
            result[key] = result.get(key, Fraction(0)) + weight
    return result


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception:
        return "unavailable"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-d", type=int, default=7)
    parser.add_argument("--max-atoms", type=int, default=7)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    cases = []
    failures = []
    for d in range(2, args.max_d + 1):
        for atom_sizes in integer_partitions(d):
            if not 2 <= len(atom_sizes) <= args.max_atoms:
                continue
            direct = connected_diagonal_direct(atom_sizes)
            positive = positive_unicycle(atom_sizes)
            mismatch = direct != positive
            if mismatch:
                failures.append(
                    {
                        "atom_sizes": atom_sizes,
                        "direct": {str(k): str(v) for k, v in direct.items()},
                        "positive": {str(k): str(v) for k, v in positive.items()},
                    }
                )
            cases.append(
                {
                    "atom_sizes": atom_sizes,
                    "atoms": len(atom_sizes),
                    "coefficients": {
                        f"{left},{right}": str(value)
                        for (left, right), value in sorted(positive.items())
                    },
                    "all_coefficients_positive": all(value > 0 for value in positive.values()),
                    "match": not mismatch,
                }
            )
    payload = {
        "claim_scope": (
            "finite exact audit of a universal combinatorial identity; the "
            "proof is the unique-cycle decomposition, not finite verification"
        ),
        "target": (
            "[y^L z^R] C_S on L+R=|S| for M125 weighted pairs of partitions"
        ),
        "method": (
            "subtraction-free unique even core cycle plus recursively planted "
            "opposite-colour trees, compared with literal partition pairs"
        ),
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "arguments": {
            "max_d": args.max_d,
            "max_atoms": args.max_atoms,
            "output": str(args.output),
        },
        "case_count": len(cases),
        "failure_count": len(failures),
        "failures": failures,
        "cases": cases,
        "elapsed_seconds": time.time() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        f"cases={len(cases)} failures={len(failures)} "
        f"elapsed={payload['elapsed_seconds']:.3f}s",
        flush=True,
    )
    print(f"wrote {args.output} sha256={sha256(args.output)}", flush=True)


if __name__ == "__main__":
    main()
