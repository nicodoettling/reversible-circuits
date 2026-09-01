#!/usr/bin/env python3
"""Clean-room d=3 check for M301; reads/imports no project artifact."""

from collections import defaultdict, deque
from itertools import combinations, permutations, product


def compose(p, q):
    return tuple(p[q[x]] for x in range(len(p)))


def transposition(edge):
    p = [0, 1, 2]
    p[edge[0]], p[edge[1]] = p[edge[1]], p[edge[0]]
    return tuple(p)


def evaluate(word):
    p = (0, 1, 2)
    for edge in word:
        p = compose(p, transposition(edge))
    return p


def relabel_edge(edge, rho):
    return tuple(sorted((rho[edge[0]], rho[edge[1]])))


def relabel_word(word, rho):
    return tuple(relabel_edge(edge, rho) for edge in word)


def conjugate_edge(edge, by):
    return relabel_edge(edge, transposition(by))


def hurwitz(word, position, sign):
    a, b = word[position : position + 2]
    out = list(word)
    if sign == 1:
        out[position : position + 2] = (b, conjugate_edge(a, b))
    else:
        out[position : position + 2] = (conjugate_edge(b, a), a)
    return tuple(out)


def connected(word):
    vertices = {v for edge in word for v in edge}
    return vertices == {0, 1, 2}


def rooted_parent(tree):
    adjacency = {1: [], 2: [], 3: []}
    for a, b in tree:
        adjacency[a].append(b)
        adjacency[b].append(a)
    parent = {3: 0}
    stack = [3]
    while stack:
        vertex = stack.pop()
        for neighbor in adjacency[vertex]:
            if neighbor not in parent:
                parent[neighbor] = vertex
                stack.append(neighbor)
    return parent


def dps_word(tree, labeling):
    parent = rooted_parent(tree)
    incidence = defaultdict(dict)
    first_black = {}
    for black in (1, 2):
        pair = labeling[2 * black - 2 : 2 * black]
        for label, white in ((pair[0], black), (pair[1], parent[black])):
            bvertex, wvertex = ("b", black), ("w", white)
            incidence[bvertex][label] = wvertex
            incidence[wvertex][label] = bvertex
            first_black[label] = black

    state = (("w", 1), 1)
    start = state
    seen = set()
    tokens = []
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        step = 1 if vertex[0] == "w" else -1
        label = 1 + ((incoming - 1 + step) % 4)
        if label in incidence[vertex]:
            head = incidence[vertex][label]
            tokens.append(("side", label, vertex, head))
            state = (head, label)
        else:
            tokens.append(("half", vertex[0], vertex[1], label))
            state = (vertex, label)
    assert state == start and len(tokens) == 20

    second_black = {}
    while True:
        positions = [j for j, token in enumerate(tokens) if token[0] == "half"]
        pair = None
        for offset, white_position in enumerate(positions):
            black_position = positions[(offset + 1) % len(positions)]
            if tokens[white_position][1] == "w" and tokens[black_position][1] == "b":
                pair = white_position, black_position
                break
        if pair is None:
            break
        white_position, black_position = pair
        tokens = tokens[white_position:] + tokens[:white_position]
        black_position = (black_position - white_position) % len(tokens)
        white, black = tokens[0], tokens[black_position]
        assert white[3] == black[3]
        distance = sum(token[0] == "side" for token in tokens[1:black_position])
        assert distance in (1, 3)
        if distance == 3:
            second_black[white[3]] = black[2]
        tokens = [("side", None, None, None)] + tokens[black_position + 1 :]
    remaining = [token for token in tokens if token[0] == "half"]
    assert len(remaining) == 4 and all(token[1] == "w" for token in remaining)

    word = []
    for label in (1, 2, 3, 4):
        a = first_black[label]
        b = second_black.get(label, 3)
        assert a != b
        word.append(tuple(sorted((a - 1, b - 1))))
    return tuple(word)


def swap_labels(labeling, i):
    return tuple(i + 1 if x == i else i if x == i + 1 else x for x in labeling)


def action_closure(words, index):
    generators = []
    for position in range(3):
        for sign in (1, -1):
            generators.append(tuple(index[hurwitz(word, position, sign)] for word in words))
    identity = tuple(range(len(words)))
    actions = {identity}
    queue = deque([identity])
    while queue:
        action = queue.popleft()
        for generator in generators:
            new = tuple(generator[action[j]] for j in range(len(words)))
            if new not in actions:
                actions.add(new)
                queue.append(new)
    return tuple(sorted(actions))


def canonical(word, relabelings):
    return min(relabel_word(word, rho) for rho in relabelings)


def matching_rows(endpoints, left_count):
    by_left = defaultdict(list)
    for edge_id, (left, _right) in enumerate(endpoints):
        by_left[left].append(edge_id)
    rows = []
    for selected in product(*(by_left[left] for left in range(left_count))):
        if len({endpoints[edge_id][1] for edge_id in selected}) == left_count:
            rows.append(tuple(selected))
    return tuple(sorted(set(rows)))


def main():
    edges = ((0, 1), (0, 2), (1, 2))
    direct = tuple(sorted(
        word for word in product(edges, repeat=4)
        if evaluate(word) == (0, 1, 2) and connected(word)
    ))
    assert len(direct) == 24

    trees = (
        frozenset(((1, 2), (1, 3))),
        frozenset(((1, 2), (2, 3))),
        frozenset(((1, 3), (2, 3))),
    )
    preimages = defaultdict(list)
    for tree in trees:
        for labeling in permutations((1, 2, 3, 4)):
            preimages[dps_word(tree, labeling)].append((tree, labeling))
    assert tuple(sorted(preimages)) == direct
    assert {len(rows) for rows in preimages.values()} == {3}

    words = direct
    index = {word: j for j, word in enumerate(words)}
    targets = {}
    for i in (1, 2, 3):
        image = []
        for word in words:
            target_words = {
                dps_word(tree, swap_labels(labeling, i))
                for tree, labeling in preimages[word]
            }
            assert len(target_words) == 1
            image.append(index[next(iter(target_words))])
        targets[i] = tuple(image)

    actions = action_closure(words, index)
    assert len(actions) == 216
    all_relabelings = tuple(permutations(range(3)))
    root_relabelings = tuple(rho for rho in all_relabelings if rho[2] == 2)
    global_keys = tuple(canonical(word, all_relabelings) for word in words)
    root_keys = tuple(canonical(word, root_relabelings) for word in words)
    global_order = tuple(sorted(set(global_keys)))
    root_order = tuple(sorted(set(root_keys)))
    assert len(global_order) == 4 and len(root_order) == 12
    global_id = {key: j for j, key in enumerate(global_order)}
    root_blocks = {key: [j for j, value in enumerate(root_keys) if value == key] for key in root_order}

    guard_rows = []
    for i in (1, 2, 3):
        edge_rows = []
        for root_key in root_order:
            source = root_blocks[root_key][0]
            target_keys = {root_keys[targets[i][j]] for j in root_blocks[root_key]}
            assert len(target_keys) == 1
            edge_rows.append((
                global_id[global_keys[source]],
                global_id[global_keys[targets[i][source]]],
                source,
                targets[i][source],
            ))
        endpoints = tuple(row[:2] for row in edge_rows)
        matchings = matching_rows(endpoints, 4)
        fibers = tuple(frozenset(
            action_id for action_id, action in enumerate(actions)
            if action[row[2]] == row[3]
        ) for row in edge_rows)
        assert len(edge_rows) == 12 and len(matchings) == 12
        assert {len(fiber) for fiber in fibers} == {9}
        compatible_full = sum(all(fibers[a] & fibers[b] for a, b in combinations(row, 2)) for row in matchings)
        assert compatible_full == 0
        guard_rows.append((i, len(edge_rows), len(matchings), compatible_full))

        if i == 1:
            assert (0, 1, 2, 9) in matchings
            assert tuple(endpoints[j] for j in (0, 2, 9)) == ((0, 1), (2, 3), (3, 2))
            assert fibers[0] & fibers[2] == {45}
            assert fibers[0] & fibers[9] == {49}
            assert fibers[2] & fibers[9] == {89}
            assert not (fibers[0] & fibers[2] & fibers[9])
            expected = (
                (((0, 1), (0, 1), (0, 2), (0, 2)), ((0, 1), (1, 2), (0, 1), (0, 2))),
                (((0, 1), (0, 2), (0, 2), (0, 1)), ((0, 1), (1, 2), (0, 2), (1, 2))),
                (((0, 2), (1, 2), (0, 1), (1, 2)), ((1, 2), (0, 1), (0, 1), (1, 2))),
            )
            assert tuple((words[edge_rows[j][2]], words[edge_rows[j][3]]) for j in (0, 2, 9)) == expected

    print("Z3=24 A3=216 global=4 H=12")
    print("guards=" + repr(guard_rows))
    print("matching=[0,1,2,9] witness=[0,2,9] pairs={0,2}:{45} {0,9}:{49} {2,9}:{89} triple=empty")


if __name__ == "__main__":
    main()

