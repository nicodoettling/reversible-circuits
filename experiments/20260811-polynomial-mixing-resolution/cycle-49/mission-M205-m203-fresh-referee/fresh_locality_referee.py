#!/usr/bin/env python3
"""Clean-room finite referee for M203's d=5,6 DPS locality claims.

The reconstruction below imports no M203 code and enumerates no quotient
graph.  It generates only the named M181 source words, their rooted DPS
descriptors, and adjacent-value edits.  Frozen JSON is read only after the
independent tables have been completed.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import platform
import time
from collections import Counter, defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
M203 = HERE.parent / "mission-M203-all-d-matching-route-structural"


def undirected(a: int, b: int) -> tuple[int, int]:
    assert a != b
    return (a, b) if a < b else (b, a)


def rename(word, permutation):
    return tuple(undirected(permutation[a], permutation[b]) for a, b in word)


def rooted_trees(d: int):
    """Cayley trees, generated independently by lexicographic Prüfer codes."""
    for code in itertools.product(range(1, d + 1), repeat=d - 2):
        degree = [0] + [1] * d
        for vertex in code:
            degree[vertex] += 1
        edges = []
        for vertex in code:
            leaf = next(x for x in range(1, d + 1) if degree[x] == 1)
            edges.append(undirected(leaf, vertex))
            degree[leaf] -= 1
            degree[vertex] -= 1
        leaves = [x for x in range(1, d + 1) if degree[x] == 1]
        edges.append(undirected(leaves[0], leaves[1]))
        yield frozenset(edges)


def orient_to_root(tree, d: int):
    neighbors = {x: [] for x in range(1, d + 1)}
    for a, b in tree:
        neighbors[a].append(b)
        neighbors[b].append(a)
    parent = {d: None}
    pending = [d]
    while pending:
        current = pending.pop()
        for nxt in neighbors[current]:
            if nxt not in parent:
                parent[nxt] = current
                pending.append(nxt)
    assert len(parent) == d
    return parent


def trace_boundary(tree, ordering, d: int):
    """Trace the hairy-tree boundary used by the DPS correspondence."""
    parent = orient_to_root(tree, d)
    incidence = defaultdict(dict)
    first_black = {}
    for child in range(1, d):
        first_label, second_label = ordering[2 * child - 2 : 2 * child]
        black = ("black", child)
        for label, white_vertex in (
            (first_label, child),
            (second_label, parent[child]),
        ):
            white = ("white", white_vertex)
            incidence[black][label] = white
            incidence[white][label] = black
            first_black[label] = child

    modulus = 2 * d - 2
    initial = (("white", 1), 1)
    state = initial
    visited = set()
    boundary = []
    while state not in visited:
        visited.add(state)
        vertex, incoming = state
        step = 1 if vertex[0] == "white" else -1
        label = 1 + ((incoming - 1 + step) % modulus)
        if label in incidence[vertex]:
            boundary.append(("edge-side",))
            state = (incidence[vertex][label], label)
        else:
            boundary.append(("half-edge", vertex[0], vertex[1], label))
            state = (vertex, label)
    assert state == initial
    assert len(boundary) == (2 * d - 1) * modulus
    return boundary, first_black


def close_boundary(boundary, d: int):
    """Close adjacent white/black half-edges and record distance-three pairs."""
    boundary = list(boundary)
    second_black = {}
    while True:
        half_positions = [
            index for index, item in enumerate(boundary)
            if item[0] == "half-edge"
        ]
        chosen = None
        for offset, white_index in enumerate(half_positions):
            black_index = half_positions[(offset + 1) % len(half_positions)]
            if (
                boundary[white_index][1] == "white"
                and boundary[black_index][1] == "black"
            ):
                chosen = white_index, black_index
                break
        if chosen is None:
            break

        white_index, black_index = chosen
        boundary = boundary[white_index:] + boundary[:white_index]
        black_index = (black_index - white_index) % len(boundary)
        white_half = boundary[0]
        black_half = boundary[black_index]
        assert white_half[3] == black_half[3]
        intervening_sides = sum(
            item[0] == "edge-side" for item in boundary[1:black_index]
        )
        assert intervening_sides in (1, 3)
        if intervening_sides == 3:
            second_black[white_half[3]] = black_half[2]
        boundary = [("edge-side",)] + boundary[black_index + 1 :]

    residue = [item for item in boundary if item[0] == "half-edge"]
    assert len(residue) == 2 * d - 2
    assert all(item[1] == "white" for item in residue)
    return second_black


def decode_dps(tree, ordering, d: int):
    boundary, first_black = trace_boundary(tree, ordering, d)
    second_black = close_boundary(boundary, d)
    return tuple(
        undirected(first_black[label] - 1, second_black.get(label, d) - 1)
        for label in range(1, 2 * d - 1)
    )


def descriptor_orders(word, d: int):
    """All orders compatible with root d-1, in a declared lexicographic order."""
    root = d - 1
    endpoint_choices = [tuple(x for x in edge if x != root) for edge in word]
    for assignment in itertools.product(*endpoint_choices):
        if any(assignment.count(vertex) != 2 for vertex in range(d - 1)):
            continue
        slots = {
            vertex: [i + 1 for i, value in enumerate(assignment) if value == vertex]
            for vertex in range(d - 1)
        }
        for reversed_bits in itertools.product((0, 1), repeat=d - 1):
            order = []
            for vertex in range(d - 1):
                pair = slots[vertex]
                order.extend(pair if reversed_bits[vertex] == 0 else pair[::-1])
            yield tuple(order)


def recover_descriptor(word, d: int, trees):
    trials = 0
    for order in descriptor_orders(word, d):
        for tree in trees:
            trials += 1
            if decode_dps(tree, order, d) == word:
                return tree, order, trials
    raise AssertionError(f"no rooted DPS descriptor at d={d}")


def adjacent_value_edit(ordering, edit: int):
    return tuple(
        edit + 1 if value == edit
        else edit if value == edit + 1
        else value
        for value in ordering
    )


def explicit_source(d: int, pattern_id: int):
    """The two r=1 M181 words; 0 is V and 1 is U."""
    assert d in (5, 6) and pattern_id in (0, 1)
    third = (1, 3) if pattern_id == 0 else (0, 3)
    base_edges = ((0, 1), (0, 2), third)
    word = tuple(edge for edge in base_edges for _ in range(2))
    fillers = tuple(
        (0, label) for label in range(4, d) for _ in range(2)
    )
    result = word + fillers
    assert len(result) == 2 * d - 2
    return result


def root_permutation(d: int, root: int):
    permutation = list(range(d))
    permutation[root], permutation[d - 1] = permutation[d - 1], permutation[root]
    return tuple(permutation)


def quotient_representative(word, d: int):
    return min(rename(word, permutation) for permutation in itertools.permutations(range(d)))


def representative_digest(representative):
    # Match the frozen artifact's public digest encoding exactly.
    return hashlib.sha256(json.dumps(representative).encode()).hexdigest()


def canonical_data(word, d: int):
    representative = quotient_representative(word, d)
    return representative, representative_digest(representative)


def json_word(word):
    return [list(edge) for edge in word]


def reconstruct_rows():
    rows = []
    descriptors = {}
    for d in (5, 6):
        trees = tuple(rooted_trees(d))
        assert len(trees) == d ** (d - 2)
        for pattern_id in (0, 1):
            literal = explicit_source(d, pattern_id)
            for root in range(d):
                source = rename(literal, root_permutation(d, root))
                tree, ordering, trials = recover_descriptor(source, d, trees)
                descriptors[d, pattern_id, root] = (tree, ordering, trials)
                for edit in range(1, 2 * d - 2):
                    target = decode_dps(tree, adjacent_value_edit(ordering, edit), d)
                    changed = [
                        i for i, pair in enumerate(zip(source, target), 1)
                        if pair[0] != pair[1]
                    ]
                    adjacent_outside = [i for i in changed if i not in (edit, edit + 1)]
                    region_start = 6 * ((edit - 1) // 6) + 1
                    region_end = min(region_start + 5, 2 * d - 2)
                    region_outside = [
                        i for i in changed if not region_start <= i <= region_end
                    ]
                    representative, digest = canonical_data(target, d)
                    rows.append({
                        "d": d,
                        "pattern_id": pattern_id,
                        "pattern": [pattern_id],
                        "root": root,
                        "edit": edit,
                        "inverse_trials": trials,
                        "source": json_word(source),
                        "target": json_word(target),
                        "changed_positions": changed,
                        "outside_adjacent_edit_positions": adjacent_outside,
                        "nominal_factor_region": [region_start, region_end],
                        "outside_nominal_region_positions": region_outside,
                        "literal_adjacent_factor_locality": not adjacent_outside,
                        "literal_six_factor_region_locality": not region_outside,
                        "target_canonical_sha256": digest,
                        "target_representative": json_word(representative),
                    })
    return rows, descriptors


ROW_COMPARE_FIELDS = (
    "d", "pattern_id", "pattern", "root", "edit", "inverse_trials",
    "source", "target", "changed_positions", "outside_adjacent_edit_positions",
    "nominal_factor_region", "outside_nominal_region_positions",
    "literal_adjacent_factor_locality", "literal_six_factor_region_locality",
    "target_canonical_sha256",
)


def comparison_projection(rows):
    return [{key: row[key] for key in ROW_COMPARE_FIELDS} for row in rows]


def digest_json(value):
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def summarize_rows(rows):
    block_to_filler = [
        row for row in rows
        if row["d"] == 6 and row["edit"] <= 5
        and any(position >= 7 for position in row["changed_positions"])
    ]
    filler_to_block = [
        row for row in rows
        if row["d"] == 6 and row["edit"] >= 7
        and any(position <= 6 for position in row["changed_positions"])
    ]
    return {
        "rows": len(rows),
        "literal_adjacent_factor_locality_failures": sum(
            not row["literal_adjacent_factor_locality"] for row in rows
        ),
        "literal_six_factor_region_locality_failures": sum(
            not row["literal_six_factor_region_locality"] for row in rows
        ),
        "region_failure_histogram_by_d": {
            str(key): value for key, value in sorted(Counter(
                row["d"] for row in rows
                if not row["literal_six_factor_region_locality"]
            ).items())
        },
        "d6_active_block_edit_changes_filler_count": len(block_to_filler),
        "d6_filler_edit_changes_active_block_count": len(filler_to_block),
        "first_enumerated_d6_active_to_filler": block_to_filler[0],
        "first_enumerated_d6_filler_to_active": filler_to_block[0],
    }


def leaf_comparisons(rows, descriptors):
    actual_d6 = {
        (row["pattern_id"], row["edit"]): row
        for row in rows if row["d"] == 6 and row["root"] == 5
    }
    output = []
    for pattern_id in (0, 1):
        tree, ordering, _ = descriptors[5, pattern_id, 4]
        for edit in range(1, 8):
            target5 = decode_dps(tree, adjacent_value_edit(ordering, edit), 5)
            naive = target5 + ((0, 5), (0, 5))
            naive_rep, naive_digest = canonical_data(naive, 6)
            actual_row = actual_d6[pattern_id, edit]
            actual = tuple(tuple(edge) for edge in actual_row["target"])
            actual_rep, actual_digest = canonical_data(actual, 6)
            exact_equal = naive_rep == actual_rep
            assert exact_equal == (naive_digest == actual_digest)
            output.append({
                "pattern_id": pattern_id,
                "pattern": [pattern_id],
                "edit": edit,
                "d6_root": 5,
                "d5_target": json_word(target5),
                "naively_stabilized_target": json_word(naive),
                "actual_d6_target": json_word(actual),
                "naively_stabilized_canonical_sha256": naive_digest,
                "actual_d6_canonical_sha256": actual_digest,
                "quotient_classes_equal": exact_equal,
            })
    return output


def main():
    started = time.perf_counter()

    # Clean phase: complete the mathematical reconstruction first.
    rows, descriptors = reconstruct_rows()
    summary = summarize_rows(rows)
    comparisons = leaf_comparisons(rows, descriptors)
    unequal = [row for row in comparisons if not row["quotient_classes_equal"]]
    exact_row_projection = comparison_projection(rows)

    # Comparison phase: only now inspect frozen M203 machine-readable output.
    frozen_locality = json.loads((M203 / "locality_results.json").read_text())
    frozen_leaf = json.loads((M203 / "leaf_stabilization_results.json").read_text())
    frozen_projection = comparison_projection(frozen_locality["rows_detail"])
    row_mismatches = [
        index for index, (ours, theirs) in enumerate(
            zip(exact_row_projection, frozen_projection)
        ) if ours != theirs
    ]
    if len(exact_row_projection) != len(frozen_projection):
        row_mismatches.append("length")

    frozen_comparisons = frozen_leaf["comparison_rows"]
    leaf_mismatches = [
        index for index, (ours, theirs) in enumerate(zip(comparisons, frozen_comparisons))
        if ours != theirs
    ]
    if len(comparisons) != len(frozen_comparisons):
        leaf_mismatches.append("length")

    distinguished = next(
        row for row in rows
        if row["d"] == 6 and row["pattern_id"] == 0
        and row["root"] == 5 and row["edit"] == 1
    )
    result = {
        "experiment": "M205 clean-room immutable referee of M203",
        "scope": (
            "exact targeted rooted DPS rows at d=5,6 and fourteen leaf "
            "comparisons only; no Q6 enumeration"
        ),
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "elapsed_seconds": time.perf_counter() - started,
        "independent_summary": {
            key: value for key, value in summary.items()
            if not key.startswith("first_enumerated")
        },
        "rooted_descriptor_counts": {"d5": 10, "d6": 12},
        "row_projection_sha256": digest_json(exact_row_projection),
        "frozen_row_projection_sha256": digest_json(frozen_projection),
        "row_mismatch_indices": row_mismatches,
        "distinguished_physical_witness": {
            key: distinguished[key] for key in (
                "d", "pattern_id", "root", "edit", "inverse_trials", "source",
                "target", "changed_positions", "outside_nominal_region_positions",
                "target_canonical_sha256",
            )
        },
        "first_enumerated_cross_coupling_witnesses": {
            "active_to_filler": {
                key: summary["first_enumerated_d6_active_to_filler"][key]
                for key in ("pattern_id", "root", "edit", "changed_positions")
            },
            "filler_to_active": {
                key: summary["first_enumerated_d6_filler_to_active"][key]
                for key in ("pattern_id", "root", "edit", "changed_positions")
            },
        },
        "leaf_stabilization": {
            "comparisons": len(comparisons),
            "equal_quotient_classes": len(comparisons) - len(unequal),
            "unequal_quotient_classes": len(unequal),
            "comparison_projection_sha256": digest_json(comparisons),
            "frozen_comparison_projection_sha256": digest_json(frozen_comparisons),
            "mismatch_indices": leaf_mismatches,
            "first_unequal": unequal[0],
        },
        "frozen_summary_matches": {
            "rows": summary["rows"] == frozen_locality["rows"],
            "adjacent_failures": summary["literal_adjacent_factor_locality_failures"]
                == frozen_locality["literal_adjacent_factor_locality_failures"],
            "six_factor_failures": summary["literal_six_factor_region_locality_failures"]
                == frozen_locality["literal_six_factor_region_locality_failures"],
            "region_histogram": summary["region_failure_histogram_by_d"]
                == {str(k): v for k, v in frozen_locality["region_failure_histogram_by_d"].items()},
            "active_to_filler_count": summary["d6_active_block_edit_changes_filler_count"]
                == frozen_locality["d6_active_block_edit_changes_filler_count"],
            "filler_to_active_count": summary["d6_filler_edit_changes_active_block_count"]
                == frozen_locality["d6_filler_edit_changes_active_block_count"],
            "leaf_equal_count": len(comparisons) - len(unequal)
                == frozen_leaf["equal_quotient_classes"],
            "leaf_unequal_count": len(unequal)
                == frozen_leaf["unequal_quotient_classes"],
        },
        "scope_conclusion": (
            "Only the automatic independent-d5-block plus fixed-filler proof "
            "premise is refuted. No d6 nonreachability or all-d routing "
            "conclusion follows."
        ),
    }

    checks = [
        result["row_mismatch_indices"] == [],
        result["leaf_stabilization"]["mismatch_indices"] == [],
        all(result["frozen_summary_matches"].values()),
        result["independent_summary"]["rows"] == 178,
        result["independent_summary"]["literal_six_factor_region_locality_failures"] == 106,
        result["independent_summary"]["d6_active_block_edit_changes_filler_count"] == 29,
        result["independent_summary"]["d6_filler_edit_changes_active_block_count"] == 22,
        result["leaf_stabilization"]["equal_quotient_classes"] == 5,
        result["leaf_stabilization"]["unequal_quotient_classes"] == 9,
    ]
    result["all_checks_pass"] = all(checks)
    assert result["all_checks_pass"]

    (HERE / "referee_results.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

