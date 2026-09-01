#!/usr/bin/env python3
"""Independent exact audit of the frozen M97 genus-one cut claims.

The implementation is deliberately self-contained and does not import M97
code.  It exhausts d=2,3,4, checks every cut of every connected identity
word, checks the square-insertion incidence law, and numerically calibrates
the exact lift spectrum at d=2,3.  Universal claims in the referee report have
separate algebraic proofs; finite agreement is not asymptotic gap evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import heapq
import itertools
import json
import platform
import subprocess
import time
from collections import Counter, defaultdict, deque
from pathlib import Path

import numpy as np


Edge = tuple[int, int]
Word = tuple[Edge, ...]
Perm = tuple[int, ...]


def edges(d: int) -> tuple[Edge, ...]:
    return tuple((a, b) for a in range(d) for b in range(a + 1, d))


def mul_right_edge(p: Perm, e: Edge) -> Perm:
    """Return p*e under (pq)(x)=p(q(x)); this swaps p's entries at e."""
    q = list(p)
    a, b = e
    q[a], q[b] = q[b], q[a]
    return tuple(q)


def eval_word(d: int, word: Word) -> Perm:
    p = tuple(range(d))
    for e in word:
        p = mul_right_edge(p, e)
    return p


def cycles(p: Perm) -> tuple[tuple[int, ...], ...]:
    seen: set[int] = set()
    out: list[tuple[int, ...]] = []
    for x in range(len(p)):
        if x in seen:
            continue
        cyc: list[int] = []
        y = x
        while y not in seen:
            seen.add(y)
            cyc.append(y)
            y = p[y]
        out.append(tuple(cyc))
    return tuple(out)


def same_perm_cycle(p: Perm, a: int, b: int) -> bool:
    y = a
    while True:
        if y == b:
            return True
        y = p[y]
        if y == a:
            return False


def support_partition(d: int, word: Word) -> tuple[int, ...]:
    parent = list(range(d))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in word:
        ra, rb = find(a), find(b)
        if ra != rb:
            if ra > rb:
                ra, rb = rb, ra
            parent[rb] = ra
    raw = tuple(find(x) for x in range(d))
    relabel: dict[int, int] = {}
    return tuple(relabel.setdefault(r, len(relabel)) for r in raw)


def q_support(d: int, word: Word) -> int:
    return len(set(support_partition(d, word)))


def genus(d: int, word: Word) -> int:
    p = eval_word(d, word)
    numerator = len(word) - d - len(cycles(p)) + 2 * q_support(d, word)
    assert numerator >= 0 and numerator % 2 == 0
    return numerator // 2


def prefix_data(d: int, word: Word):
    gs = [0]
    ps: list[Perm] = [tuple(range(d))]
    parts: list[tuple[int, ...]] = [tuple(range(d))]
    case_counts: Counter[str] = Counter()
    prefix: list[Edge] = []
    for e in word:
        p0 = ps[-1]
        part0 = parts[-1]
        q0, c0 = len(set(part0)), len(cycles(p0))
        a, b = e
        if part0[a] != part0[b]:
            case = "join_support_components"
            expected = (-1, -1, 0)
        elif same_perm_cycle(p0, a, b):
            case = "cut_permutation_cycle"
            expected = (0, +1, 0)
        else:
            case = "join_cycles_within_support"
            expected = (0, -1, 1)
        prefix.append(e)
        p1 = mul_right_edge(p0, e)
        part1 = support_partition(d, tuple(prefix))
        q1, c1 = len(set(part1)), len(cycles(p1))
        numerator = len(prefix) - d - c1 + 2 * q1
        assert numerator >= 0 and numerator % 2 == 0
        g1 = numerator // 2
        observed = (q1 - q0, c1 - c0, g1 - gs[-1])
        assert observed == expected, (word, e, case, expected, observed)
        case_counts[case] += 1
        gs.append(g1)
        ps.append(p1)
        parts.append(part1)
    return gs, ps, parts, case_counts


def handle(d: int, word: Word) -> int:
    gs, _, _, _ = prefix_data(d, word)
    jumps = [j for j in range(1, len(gs)) if gs[j] - gs[j - 1] == 1]
    assert gs[-1] == 1 and len(jumps) == 1
    return jumps[0]


def conjugate_edge(e: Edge, by: Edge) -> Edge:
    a, b = e
    u, v = by

    def act(x: int) -> int:
        if x == u:
            return v
        if x == v:
            return u
        return x

    return tuple(sorted((act(a), act(b))))  # type: ignore[return-value]


def hurwitz(word: Word, i: int, sign: int) -> Word:
    a, b = word[i], word[i + 1]
    if sign == 1:
        pair = (b, conjugate_edge(a, b))
    else:
        pair = (conjugate_edge(b, a), a)
    return word[:i] + pair + word[i + 2 :]


def component_genera(d: int, word: Word) -> tuple[int, ...]:
    part = support_partition(d, word)
    p = eval_word(d, word)
    blocks = sorted(set(part))
    sizes = Counter(part)
    lengths: Counter[int] = Counter(part[a] for a, _ in word)
    cycle_counts: Counter[int] = Counter()
    for cyc in cycles(p):
        roots = {part[x] for x in cyc}
        assert len(roots) == 1
        cycle_counts[next(iter(roots))] += 1
    ans: list[int] = []
    for block in blocks:
        num = lengths[block] - sizes[block] - cycle_counts[block] + 2
        assert num >= 0 and num % 2 == 0
        ans.append(num // 2)
    assert sum(ans) == genus(d, word)
    return tuple(ans)


def incidence_at_cut(d: int, word: Word, j: int) -> dict[str, int | bool]:
    left, right = word[:j], word[j:]
    p = eval_word(d, left)
    lp, rp = support_partition(d, left), support_partition(d, right)
    lvals, rvals = sorted(set(lp)), sorted(set(rp))
    lmap = {x: i for i, x in enumerate(lvals)}
    rmap = {x: i + len(lvals) for i, x in enumerate(rvals)}
    adj: list[set[int]] = [set() for _ in range(len(lvals) + len(rvals))]
    edge_count = 0
    for cyc in cycles(p):
        lbs, rbs = {lp[x] for x in cyc}, {rp[x] for x in cyc}
        assert len(lbs) == len(rbs) == 1
        a = lmap[next(iter(lbs))]
        b = rmap[next(iter(rbs))]
        adj[a].add(b)
        adj[b].add(a)
        edge_count += 1
    seen = {0}
    queue = deque([0])
    while queue:
        x = queue.popleft()
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                queue.append(y)
    connected = len(seen) == len(adj)
    gl, gr = genus(d, left), genus(d, right)
    vertices = len(adj)
    assert connected
    assert gl + gr == vertices - edge_count
    assert sum(component_genera(d, left)) == gl
    assert sum(component_genera(d, right)) == gr
    if gl == 0:
        assert all(x == 0 for x in component_genera(d, left))
    if gr == 0:
        assert all(x == 0 for x in component_genera(d, right))
    return {
        "left_genus": gl,
        "right_genus": gr,
        "vertices": vertices,
        "edges": edge_count,
        "connected": connected,
        "cyclomatic": edge_count - vertices + 1,
    }


def connected(d: int, word: Word) -> bool:
    return q_support(d, word) == 1


def marks(d: int, word: Word) -> tuple[int, ...]:
    out: list[int] = []
    ident = tuple(range(d))
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            continue
        z = word[:i] + word[i + 2 :]
        if eval_word(d, z) == ident and connected(d, z):
            out.append(i)
    return tuple(out)


def enumerate_states(d: int, length: int) -> tuple[list[Word], int]:
    es = edges(d)
    ident = tuple(range(d))
    states: list[Word] = []
    candidates = 0
    for word in itertools.product(es, repeat=length):
        candidates += 1
        if eval_word(d, word) == ident and connected(d, word):
            states.append(word)
    return states, candidates


def audit_case(d: int) -> tuple[dict, list[Word]]:
    states, candidates = enumerate_states(d, 2 * d)
    state_set = set(states)
    pair_hist: Counter[tuple[int, int]] = Counter()
    handle_hist: Counter[int] = Counter()
    mark_hist: Counter[int] = Counter()
    case_counts: Counter[str] = Counter()
    cut_profiles: Counter[str] = Counter()
    row_signatures: defaultdict[int, set[tuple[tuple[int, int], ...]]] = defaultdict(set)
    max_displacement = 0
    all_cut_count = 0
    for word in states:
        gs, _, _, local_cases = prefix_data(d, word)
        case_counts.update(local_cases)
        jumps = [j for j in range(1, len(gs)) if gs[j] > gs[j - 1]]
        assert len(jumps) == 1 and gs[-1] == 1
        h = jumps[0]
        hr = handle(d, tuple(reversed(word)))
        b = 2 * d + 1 - hr
        assert b < h
        handle_hist[h] += 1
        pair_hist[(h, b)] += 1
        ms = marks(d, word)
        mark_hist[len(ms)] += 1
        sig: Counter[int] = Counter()
        for i in range(2 * d - 1):
            for sign in (-1, 1):
                other = hurwitz(word, i, sign)
                assert other in state_set
                ho = handle(d, other)
                max_displacement = max(max_displacement, abs(ho - h))
                assert abs(ho - h) <= 1
                sig[ho] += 1
        row_signatures[h].add(tuple(sorted(sig.items())))
        for j in range(2 * d + 1):
            prof = incidence_at_cut(d, word, j)
            gl, gr = int(prof["left_genus"]), int(prof["right_genus"])
            if j < b:
                expected = (0, 1, 0)
                label = "left_tree"
            elif j < h:
                expected = (0, 0, 1)
                label = "central_unicycle"
            else:
                expected = (1, 0, 0)
                label = "right_tree"
            assert (gl, gr, int(prof["cyclomatic"])) == expected
            cut_profiles[label] += 1
            all_cut_count += 1

    zstates, zcandidates = enumerate_states(d, 2 * d - 2)
    inserted: Counter[Word] = Counter()
    insertion_checks = 0
    for z in zstates:
        assert genus(d, z) == 0
        for p in range(2 * d - 1):
            for e in edges(d):
                w = z[:p] + (e, e) + z[p:]
                assert w in state_set
                assert p in marks(d, w)
                inserted[w] += 1
                insertion_checks += 1
    for w in states:
        assert inserted[w] == len(marks(d, w))
    total_marks = sum(len(marks(d, w)) for w in states)
    assert total_marks == len(zstates) * (2 * d - 1) * len(edges(d))

    x = ((0, 1),) * 4 + ((0, 2),) * 2 if d == 3 else None
    y = (
        ((0, 1),) * 3 + ((0, 2),) + ((0, 1),) + ((1, 2),)
        if d == 3
        else None
    )
    example = None
    if d == 3:
        assert x in state_set and y in state_set
        hx, hy = handle(d, x), handle(d, y)
        xdest = Counter(handle(d, hurwitz(x, i, s)) for i in range(5) for s in (-1, 1))
        ydest = Counter(handle(d, hurwitz(y, i, s)) for i in range(5) for s in (-1, 1))
        assert hx == hy == 3 and xdest == Counter({3: 10}) and ydest == Counter({3: 8, 4: 2})
        example = {
            "x_handle_destinations": dict(sorted(xdest.items())),
            "y_handle_destinations": dict(sorted(ydest.items())),
        }

    result = {
        "d": d,
        "candidate_words": candidates,
        "states": len(states),
        "prefix_increment_case_counts": dict(sorted(case_counts.items())),
        "handle_histogram": {str(k): v for k, v in sorted(handle_hist.items())},
        "oriented_handle_pair_histogram": {
            f"{h},{b}": v for (h, b), v in sorted(pair_hist.items())
        },
        "mark_count_histogram": {str(k): v for k, v in sorted(mark_hist.items())},
        "unmarked": mark_hist[0],
        "cut_profile_counts": dict(sorted(cut_profiles.items())),
        "all_cuts_checked": all_cut_count,
        "max_handle_displacement": max_displacement,
        "strong_handle_lump": all(len(s) == 1 for s in row_signatures.values()),
        "row_signature_counts_by_handle": {
            str(k): len(v) for k, v in sorted(row_signatures.items())
        },
        "genus_zero_candidates": zcandidates,
        "genus_zero_states": len(zstates),
        "insertion_incidence_checks": insertion_checks,
        "total_deletable_square_marks": total_marks,
        "insertion_deletion_multiplicity_exact": True,
        "m97_handle_examples": example,
    }
    return result, states


def path_frozen_family(d: int) -> Word:
    word: list[Edge] = [(0, 1)] * 4
    for a in range(1, d - 1):
        word.extend(((a, a + 1), (a, a + 1)))
    return tuple(word)


def audit_frozen_family(max_d: int) -> dict:
    rows = []
    for d in range(3, max_d + 1):
        word = path_frozen_family(d)
        assert len(word) == 2 * d and eval_word(d, word) == tuple(range(d)) and connected(d, word)
        h = handle(d, word)
        dest = Counter(
            handle(d, hurwitz(word, i, sign))
            for i in range(2 * d - 1)
            for sign in (-1, 1)
        )
        assert h == 3 and dest == Counter({3: 2 * (2 * d - 1)})
        assert marks(d, word)
        rows.append({"d": d, "h": h, "proposal_handle_histogram": {"3": sum(dest.values())}})
    return {"range": [3, max_d], "cases": rows, "all_passed": True}


def tree_from_prufer(d: int, code: tuple[int, ...]) -> tuple[Edge, ...]:
    degree = [1] * d
    for x in code:
        degree[x] += 1
    leaves = [x for x in range(d) if degree[x] == 1]
    heapq.heapify(leaves)
    out: list[Edge] = []
    for x in code:
        leaf = heapq.heappop(leaves)
        out.append(tuple(sorted((leaf, x))))  # type: ignore[arg-type]
        degree[leaf] -= 1
        degree[x] -= 1
        if degree[x] == 1:
            heapq.heappush(leaves, x)
    a, b = heapq.heappop(leaves), heapq.heappop(leaves)
    out.append(tuple(sorted((a, b))))  # type: ignore[arg-type]
    return tuple(sorted(out))


def m92_word(tree: tuple[Edge, ...], d: int) -> Word:
    incident: defaultdict[int, list[Edge]] = defaultdict(list)
    for e in tree:
        incident[e[0]].append(e)
        incident[e[1]].append(e)
    vertex = min(x for x in incident if len(incident[x]) >= 2)
    a, b = sorted(incident[vertex])[:2]
    word: list[Edge] = [a, b, a, b, a, b]
    for e in sorted(set(tree) - {a, b}):
        word.extend((e, e))
    assert len(word) == 2 * d
    return tuple(word)


def audit_m92_unmarked(max_d: int) -> dict:
    counts: dict[str, int] = {}
    for d in range(3, max_d + 1):
        seen_trees: set[tuple[Edge, ...]] = set()
        seen_words: set[Word] = set()
        for code in itertools.product(range(d), repeat=d - 2):
            tree = tree_from_prufer(d, code)
            assert tree not in seen_trees
            seen_trees.add(tree)
            word = m92_word(tree, d)
            assert eval_word(d, word) == tuple(range(d))
            assert connected(d, word) and genus(d, word) == 1
            assert not marks(d, word)
            assert frozenset(word) == frozenset(tree)
            seen_words.add(word)
        assert len(seen_trees) == d ** (d - 2)
        assert len(seen_words) == len(seen_trees)
        counts[str(d)] = len(seen_words)
    return {"range": [3, max_d], "tree_and_word_counts": counts, "all_unmarked": True}


def transition_matrix(d: int, states: list[Word]) -> np.ndarray:
    n = len(states)
    index = {w: i for i, w in enumerate(states)}
    positions = 2 * d - 1
    denominator = 4 * positions
    counts = np.zeros((n, n), dtype=np.int64)
    for x, word in enumerate(states):
        counts[x, x] += 2 * positions
        for i in range(positions):
            for sign in (-1, 1):
                counts[x, index[hurwitz(word, i, sign)]] += 1
    assert np.all(counts.sum(axis=1) == denominator)
    assert np.array_equal(counts, counts.T)
    return counts.astype(np.float64) / denominator


def audit_lift(d: int, states: list[Word]) -> dict:
    p = transition_matrix(d, states)
    n = len(states)
    intervals: list[tuple[int, ...]] = []
    for w in states:
        h = handle(d, w)
        b = 2 * d + 1 - handle(d, tuple(reversed(w)))
        intervals.append(tuple(range(b, h)))
    lifted = [(x, j) for x, js in enumerate(intervals) for j in js]
    ai = {a: i for i, a in enumerate(lifted)}
    a_size = len(lifted)
    lmat = np.zeros((a_size, a_size), dtype=np.float64)
    for row, (x, _) in enumerate(lifted):
        for y in np.flatnonzero(p[x]):
            val = p[x, y] / len(intervals[y])
            for jy in intervals[y]:
                lmat[row, ai[(int(y), jy)]] = val
    assert np.max(np.abs(lmat.sum(axis=1) - 1.0)) < 1e-14
    stationary = np.array([1.0 / (n * len(intervals[x])) for x, _ in lifted])
    stationarity_residual = float(np.max(np.abs(stationary @ lmat - stationary)))
    db = stationary[:, None] * lmat
    detailed_balance_residual = float(np.max(np.abs(db - db.T)))
    wmarginal_residual = 0.0
    for row, (x, _) in enumerate(lifted):
        for y in range(n):
            got = sum(lmat[row, ai[(y, jy)]] for jy in intervals[y])
            wmarginal_residual = max(wmarginal_residual, abs(got - p[x, y]))

    f = np.array([((17 * k + 3) % 29) - 14 for k in range(a_size)], dtype=np.float64)
    rf = np.array([
        sum(f[ai[(x, j)]] for j in intervals[x]) / len(intervals[x])
        for x in range(n)
    ])
    uprf = np.array([(p @ rf)[x] for x, _ in lifted])
    factorization_residual = float(np.max(np.abs(lmat @ f - uprf)))

    sqrtpi = np.sqrt(stationary)
    sym_l = sqrtpi[:, None] * lmat / sqrtpi[None, :]
    assert np.max(np.abs(sym_l - sym_l.T)) < 1e-14
    ep = np.linalg.eigvalsh(p)
    el = np.linalg.eigvalsh(sym_l)
    expected = np.sort(np.concatenate((ep, np.zeros(a_size - n))))
    spectrum_residual = float(np.max(np.abs(el - expected)))

    def gap(vals: np.ndarray) -> float:
        if len(vals) == 1:
            return 1.0
        return float(1.0 - np.sort(vals)[-2])

    return {
        "d": d,
        "base_states": n,
        "lifted_states": a_size,
        "extra_zero_eigenvalues_expected": a_size - n,
        "base_eigenvalue_one_multiplicity": int(np.sum(np.abs(ep - 1.0) < 1e-10)),
        "lift_eigenvalue_one_multiplicity": int(np.sum(np.abs(el - 1.0) < 1e-10)),
        "base_zero_eigenvalue_multiplicity_numeric": int(np.sum(np.abs(ep) < 1e-10)),
        "lift_zero_eigenvalue_multiplicity_numeric": int(np.sum(np.abs(el) < 1e-10)),
        "base_min_eigenvalue": float(ep[0]),
        "lift_min_eigenvalue": float(el[0]),
        "base_gap": gap(ep),
        "lift_gap": gap(el),
        "stationarity_residual": stationarity_residual,
        "detailed_balance_residual": detailed_balance_residual,
        "w_marginal_residual": wmarginal_residual,
        "operator_L_equals_UPR_residual": factorization_residual,
        "spectrum_union_zero_residual": spectrum_residual,
    }


def git_commit() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unavailable"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", nargs="+", type=int, default=[2, 3, 4])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--frozen-family-max-d", type=int, default=12)
    parser.add_argument("--m92-family-max-d", type=int, default=5)
    args = parser.parse_args()
    start = time.time()
    cases: list[dict] = []
    state_cache: dict[int, list[Word]] = {}
    for d in args.d:
        result, states = audit_case(d)
        cases.append(result)
        state_cache[d] = states
        print(json.dumps({"finished_d": d, "states": len(states)}), flush=True)
    lift_cases = [audit_lift(d, state_cache[d]) for d in args.d if d <= 3]
    payload = {
        "claim_tested": (
            "M97 prefix genus, strict handle ordering, tree-unicycle-tree cuts, "
            "componentwise genus zero, exact cut lift, frozen-handle family, "
            "and marked-deletion incidence law"
        ),
        "scope_warning": (
            "Exact finite checks calibrate universal algebraic proofs and do not "
            "prove any asymptotic spectral-gap or marked-hitting bound."
        ),
        "convention": "(pq)(x)=p(q(x)); tuple factors multiply left-to-right",
        "kernel": (
            "P_d=I/2 + [1/(4(2d-1))] sum_i (R_i+R_i^-1); "
            "R_i(a,b)=(b,bab), R_i^-1(a,b)=(aba,a)"
        ),
        "commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "dependencies": {"numpy": np.__version__},
        "arguments": {
            "d": args.d,
            "output": str(args.output),
            "frozen_family_max_d": args.frozen_family_max_d,
            "m92_family_max_d": args.m92_family_max_d,
        },
        "cases": cases,
        "lift_cases": lift_cases,
        "frozen_handle_family": audit_frozen_family(args.frozen_family_max_d),
        "m92_unmarked_tree_family": audit_m92_unmarked(args.m92_family_max_d),
        "elapsed_seconds": time.time() - start,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    digest = hashlib.sha256(args.output.read_bytes()).hexdigest()
    print(json.dumps({"output": str(args.output), "sha256": digest}), flush=True)


if __name__ == "__main__":
    main()
