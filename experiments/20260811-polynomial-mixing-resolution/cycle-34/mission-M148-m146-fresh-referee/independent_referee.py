#!/usr/bin/env python3
"""Clean-room finite checks for the frozen M146 tuple-conjugacy theorem.

This script imports no predecessor module.  It verifies the immutable M146
bytes, directly tests centralizer parity and common-parity class splitting in
bounded ranks, reconstructs the rank-three rooted DPS involutions, and checks
the aligned factor-class multiset for every deterministic matching subfamily.
The universal theorem is decided by the proof audit, not finite extrapolation.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import platform
import subprocess
from collections import Counter, defaultdict, deque
from pathlib import Path


Perm = tuple[int, ...]
Edge = tuple[int, int]
Word = tuple[Edge, ...]
Product = tuple[Perm, ...]
Node = tuple[str, int]
Token = tuple[str, str | None, int | None, int | None]

FROZEN_HASHES = {
    "report.md": "160bf329699cb4548e6e42652afc1616bb228f8bcf3711c6eae2d0902d2941a1",
    "tuple_conjugacy_theorem.md": "29b2af120b10d72c678cb5a5fbbc4119be6450d37066103be4822057ae5d2228",
    "tuple_conjugacy_audit.py": "2332ea72539a3bc7feefcbd9722fd384a2c67d0ef1acd50bab3f0ecaacb88730",
    "results.json": "7c49849f8ddae03922223c91f7f3414b531f0785d80ff48374bc0dfe3ff8a5aa",
    "freeze_manifest.md": "454fd2de1b73cf7edf0b8b6f6873ef233408e03e947061f84a33f4be2dea4863",
    "SHA256SUMS": "59689cf9e0174436941ed910ab94f121acf8a27ac2af1d1f5115b3e453e63f16",
}


def mul(a: Perm, b: Perm) -> Perm:
    """Return a*b under (ab)(x)=a(b(x))."""
    return tuple(a[b[x]] for x in range(len(a)))


def inv(p: Perm) -> Perm:
    answer = [0] * len(p)
    for x, y in enumerate(p):
        answer[y] = x
    return tuple(answer)


def sign_bit(p: Perm) -> int:
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) & 1


def edge_perm(d: int, edge: Edge) -> Perm:
    p = list(range(d))
    a, b = edge
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def conjugate(h: Perm, x: Perm) -> Perm:
    return mul(mul(h, x), inv(h))


def cycle_type(p: Perm) -> tuple[int, ...]:
    used: set[int] = set()
    lengths = []
    for start in range(len(p)):
        if start in used:
            continue
        x = start
        length = 0
        while x not in used:
            used.add(x)
            length += 1
            x = p[x]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def rigid_type(kind: tuple[int, ...]) -> bool:
    return all(k & 1 for k in kind) and len(kind) == len(set(kind))


def centralizer_audit(max_d: int = 6) -> list[dict]:
    rows = []
    for d in range(2, max_d + 1):
        group = tuple(itertools.permutations(range(d)))
        representatives: dict[tuple[int, ...], Perm] = {}
        for p in group:
            representatives.setdefault(cycle_type(p), p)
        failures = []
        for kind, p in sorted(representatives.items()):
            centralizer = tuple(h for h in group if mul(h, p) == mul(p, h))
            wholly_even = all(sign_bit(h) == 0 for h in centralizer)
            if wholly_even != rigid_type(kind):
                failures.append({"cycle_type": kind, "centralizer_order": len(centralizer)})
        rows.append({"d": d, "cycle_types": len(representatives), "failures": failures})
    return rows


def product_conjugate(h: Product, x: Product) -> Product:
    return tuple(conjugate(a, b) for a, b in zip(h, x))


def product_mul(a: Product, b: Product) -> Product:
    return tuple(mul(x, y) for x, y in zip(a, b))


def common_parity_group(d: int, width: int) -> tuple[Product, ...]:
    group = tuple(itertools.permutations(range(d)))
    return tuple(x for x in itertools.product(group, repeat=width) if len({sign_bit(p) for p in x}) == 1)


def splitting_audit() -> list[dict]:
    """Directly count P-orbits inside coordinatewise ambient classes."""
    rows = []
    for d, width in ((2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (4, 1), (4, 2)):
        pgroup = common_parity_group(d, width)
        unseen = set(pgroup)
        class_counts: Counter[tuple[tuple[int, ...], ...]] = Counter()
        while unseen:
            x = next(iter(unseen))
            orbit = {product_conjugate(h, x) for h in pgroup}
            assert orbit <= unseen | (set(pgroup) - unseen)
            unseen.difference_update(orbit)
            class_counts[tuple(cycle_type(q) for q in x)] += 1
        failures = []
        for ambient, actual in sorted(class_counts.items()):
            r = sum(rigid_type(kind) for kind in ambient)
            expected = 2 ** max(r - 1, 0)
            if actual != expected:
                failures.append({"ambient": ambient, "rigid": r, "actual": actual, "expected": expected})
        transposition_ambient = tuple(((2,) + (1,) * (d - 2)) for _ in range(width))
        rows.append(
            {
                "d": d,
                "width": width,
                "P_order": len(pgroup),
                "ambient_classes": len(class_counts),
                "formula_failures": failures,
                "transposition_tuple_classes": class_counts[transposition_ambient],
            }
        )
    return rows


def word_value(d: int, word: Word) -> Perm:
    value = tuple(range(d))
    for edge in word:
        value = mul(value, edge_perm(d, edge))
    return value


def connected(d: int, word: Word) -> bool:
    graph = [set() for _ in range(d)]
    for a, b in word:
        graph[a].add(b)
        graph[b].add(a)
    seen = {0}
    queue = [0]
    while queue:
        x = queue.pop()
        for y in graph[x] - seen:
            seen.add(y)
            queue.append(y)
    return len(seen) == d


def minimal_words(d: int) -> tuple[Word, ...]:
    edges = tuple(itertools.combinations(range(d), 2))
    identity = tuple(range(d))
    return tuple(
        word
        for word in itertools.product(edges, repeat=2 * d - 2)
        if word_value(d, word) == identity and connected(d, word)
    )


def trees(d: int):
    for code in itertools.product(range(d), repeat=max(d - 2, 0)):
        degree = [1] * d
        for x in code:
            degree[x] += 1
        answer: list[Edge] = []
        for x in code:
            leaf = next(v for v in range(d) if degree[v] == 1)
            answer.append(tuple(sorted((leaf, x))))
            degree[leaf] -= 1
            degree[x] -= 1
        leaves = [v for v in range(d) if degree[v] == 1]
        answer.append(tuple(sorted(leaves)))
        yield frozenset(answer)


def parents(tree: frozenset[Edge], root: int) -> dict[int, int]:
    graph = [[] for _ in range(root + 1)]
    for a, b in tree:
        graph[a].append(b)
        graph[b].append(a)
    answer = {root: -1}
    queue = [root]
    while queue:
        x = queue.pop()
        for y in graph[x]:
            if y not in answer:
                answer[y] = x
                queue.append(y)
    return answer


def incidence(tree: frozenset[Edge], order: tuple[int, ...], d: int):
    parent = parents(tree, d - 1)
    graph: dict[Node, dict[int, Node]] = defaultdict(dict)
    first: dict[int, int] = {}
    for black in range(d - 1):
        for label, white in ((order[2 * black], black), (order[2 * black + 1], parent[black])):
            b = ("b", black)
            w = ("w", white)
            graph[b][label] = w
            graph[w][label] = b
            first[label] = black
    return graph, first


def trace_boundary(graph: dict[Node, dict[int, Node]], d: int) -> list[Token]:
    modulus = 2 * d - 2
    initial = (("w", 0), 0)
    state = initial
    seen = set()
    tokens: list[Token] = []
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        label = (incoming + (1 if vertex[0] == "w" else -1)) % modulus
        if label in graph[vertex]:
            tokens.append(("arc", None, None, label))
            state = (graph[vertex][label], label)
        else:
            tokens.append(("stub", vertex[0], vertex[1], label))
            state = (vertex, label)
    assert state == initial and len(tokens) == (2 * d - 1) * modulus
    return tokens


def close_stubs(tokens: list[Token], d: int) -> dict[int, int]:
    work = list(tokens)
    second: dict[int, int] = {}
    while True:
        stubs = [i for i, token in enumerate(work) if token[0] == "stub"]
        chosen = None
        for pos, white_index in enumerate(stubs):
            black_index = stubs[(pos + 1) % len(stubs)]
            if work[white_index][1] == "w" and work[black_index][1] == "b":
                chosen = white_index, black_index
                break
        if chosen is None:
            break
        white_index, black_index = chosen
        work = work[white_index:] + work[:white_index]
        black_index = (black_index - white_index) % len(work)
        white, black = work[0], work[black_index]
        assert white[3] == black[3]
        distance = sum(token[0] == "arc" for token in work[1:black_index])
        assert distance in (1, 3)
        if distance == 3:
            assert white[3] is not None and black[2] is not None
            second[white[3]] = black[2]
        work = [("arc", None, None, None)] + work[black_index + 1 :]
    survivors = [token for token in work if token[0] == "stub"]
    assert len(survivors) == 2 * d - 2 and all(token[1] == "w" for token in survivors)
    return second


def dps_word(tree: frozenset[Edge], order: tuple[int, ...], d: int) -> Word:
    graph, first = incidence(tree, order, d)
    second = close_stubs(trace_boundary(graph, d), d)
    root = d - 1
    word = tuple(tuple(sorted((first[label], second.get(label, root)))) for label in range(2 * d - 2))
    assert all(a != b for a, b in word)
    return word


def swap_labels(order: tuple[int, ...], j: int) -> tuple[int, ...]:
    return tuple(j + 1 if x == j else j if x == j + 1 else x for x in order)


def dps_actions_rank_three():
    d = 3
    fibers: dict[Word, list[tuple[frozenset[Edge], tuple[int, ...]]]] = defaultdict(list)
    for tree in trees(d):
        for order in itertools.permutations(range(2 * d - 2)):
            fibers[dps_word(tree, order, d)].append((tree, order))
    words = tuple(sorted(minimal_words(d)))
    assert set(words) == set(fibers) and Counter(map(len, fibers.values())) == {3: 24}
    actions = []
    for j in range(2 * d - 3):
        action = {}
        for word in words:
            images = {dps_word(tree, swap_labels(order, j), d) for tree, order in fibers[word]}
            assert len(images) == 1
            action[word] = next(iter(images))
        assert set(action) == set(action.values()) and all(action[action[w]] == w for w in words)
        actions.append(action)
    return words, fibers, actions


def relabel(word: Word, rho: Perm) -> Word:
    return tuple(tuple(sorted((rho[a], rho[b]))) for a, b in word)


def canonical(word: Word, group: tuple[Perm, ...]) -> Word:
    return min(relabel(word, rho) for rho in group)


def blocks(words: tuple[Word, ...], group: tuple[Perm, ...]):
    answer: dict[Word, list[Word]] = defaultdict(list)
    for word in words:
        answer[canonical(word, group)].append(word)
    return answer


def matching_colors(edges: list[tuple[Word, Word]], degree: int) -> list[tuple[int, ...]]:
    left = tuple(sorted({a for a, _ in edges}))
    unused = set(range(len(edges)))
    colors = []
    for _ in range(degree):
        adjacency = {a: [] for a in left}
        for edge_id in sorted(unused):
            a, b = edges[edge_id]
            adjacency[a].append((b, edge_id))
        occupied: dict[Word, tuple[Word, int]] = {}

        def augment(a: Word, visited: set[Word]) -> bool:
            for b, edge_id in adjacency[a]:
                if b in visited:
                    continue
                visited.add(b)
                if b not in occupied or augment(occupied[b][0], visited):
                    occupied[b] = (a, edge_id)
                    return True
            return False

        assert all(augment(a, set()) for a in left)
        chosen = tuple(sorted(edge_id for _, edge_id in occupied.values()))
        assert len(chosen) == len(left)
        colors.append(chosen)
        unused.difference_update(chosen)
    assert not unused
    return colors


def generated_group(d: int, words: tuple[Word, ...]) -> frozenset[Product]:
    width = len(words)
    identity = tuple(range(d))
    one = tuple(identity for _ in range(width))
    generators = tuple(
        tuple(edge_perm(d, word[j]) for word in words) for j in range(len(words[0]))
    )
    reached = {one}
    queue = deque([one])
    while queue:
        x = queue.popleft()
        for g in generators:
            y = product_mul(x, g)
            if y not in reached:
                reached.add(y)
                queue.append(y)
    return frozenset(reached)


def factors(d: int, words: tuple[Word, ...]) -> tuple[Product, ...]:
    return tuple(tuple(edge_perm(d, word[j]) for word in words) for j in range(len(words[0])))


def class_multiset(group: frozenset[Product], sequence: tuple[Product, ...]) -> Counter:
    return Counter(min(product_conjugate(h, x) for h in group) for x in sequence)


def rank_three_calibration() -> dict:
    d = 3
    words, fibers, actions = dps_actions_rank_three()
    full = tuple(itertools.permutations(range(d)))
    root = tuple(p for p in full if p[d - 1] == d - 1)
    global_key = {w: canonical(w, full) for w in words}
    root_key = {w: canonical(w, root) for w in words}
    root_blocks = blocks(words, root)
    aggregate: dict[int, Counter] = {width: Counter() for width in range(1, 5)}
    matching_rows = []
    for adjacent, action in enumerate(actions, 1):
        representatives = []
        edge_rows = []
        for _, block in sorted(root_blocks.items()):
            assert len({root_key[action[w]] for w in block}) == 1
            representative = min(block)
            representatives.append(representative)
            edge_rows.append((global_key[representative], global_key[action[representative]]))
        colors = matching_colors(edge_rows, d)
        for color, ids in enumerate(colors):
            source = tuple(representatives[i] for i in ids)
            target = tuple(action[w] for w in source)
            assert len({global_key[w] for w in source}) == len(source) == 4
            assert len({global_key[w] for w in target}) == len(target) == 4
            row = {"adjacent": adjacent, "color": color, "by_width": {}}
            for width in range(1, 5):
                counter = Counter()
                for subset in itertools.combinations(range(4), width):
                    us = tuple(source[i] for i in subset)
                    vs = tuple(target[i] for i in subset)
                    gu = generated_group(d, us)
                    gv = generated_group(d, vs)
                    if gu != gv:
                        counter["literal_group_changed"] += 1
                    elif class_multiset(gu, factors(d, us)) == class_multiset(gv, factors(d, vs)):
                        counter["class_multiset_equal"] += 1
                    else:
                        counter["class_multiset_changed"] += 1
                aggregate[width].update(counter)
                row["by_width"][str(width)] = dict(sorted(counter.items()))
            matching_rows.append(row)
    compact = {str(width): dict(sorted(counter.items())) for width, counter in aggregate.items()}
    expected = {
        "1": {"class_multiset_equal": 36},
        "2": {"class_multiset_equal": 54},
        "3": {"class_multiset_equal": 3, "literal_group_changed": 33},
        "4": {"literal_group_changed": 9},
    }
    assert compact == expected
    return {
        "target_words": len(words),
        "rooted_coordinates": sum(map(len, fibers.values())),
        "root_fiber_histogram": dict(sorted(Counter(map(len, fibers.values())).items())),
        "matchings": len(matching_rows),
        "aggregate_by_width": compact,
        "class_multiset_changes_when_literal_group_equal": 0,
        "rows": matching_rows,
    }


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    mission = Path(__file__).resolve().parent
    root = Path(__file__).resolve().parents[4]
    frozen = root / "experiments/20260811-polynomial-mixing-resolution/cycle-33/mission-M146-dps-tuple-conjugacy"
    observed = {name: sha256(frozen / name) for name in FROZEN_HASHES}
    assert observed == FROZEN_HASHES
    centralizers = centralizer_audit()
    splitting = splitting_audit()
    d3 = rank_three_calibration()
    assert all(not row["failures"] for row in centralizers)
    assert all(not row["formula_failures"] and row["transposition_tuple_classes"] == 1 for row in splitting)
    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=root, check=True, capture_output=True, text=True
    ).stdout.strip()
    payload = {
        "experiment": "M148 clean-room fresh referee checks for frozen M146",
        "repository_commit": commit,
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "command": "python3 -B independent_referee.py",
        "composition_convention": "(pq)(x)=p(q(x)); displayed factors multiply left-to-right",
        "frozen_hashes_verified": observed,
        "finite_caps": {
            "centralizer_cycle_types": "all cycle types for 2<=d<=6",
            "class_splitting": "(d,s)=(2,1..3),(3,1..3),(4,1..2)",
            "d3_DPS": "all 9 deterministic matchings and all 15 nonempty subfamilies",
        },
        "centralizer_parity_audit": centralizers,
        "common_parity_class_splitting_audit": splitting,
        "d3_matching_calibration": d3,
        "universal_claim_note": "The universal result is decided by proof audit, not finite extrapolation.",
    }
    output = mission / "independent_results.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(output), "d3_matchings": d3["matchings"]}, sort_keys=True))


if __name__ == "__main__":
    main()
