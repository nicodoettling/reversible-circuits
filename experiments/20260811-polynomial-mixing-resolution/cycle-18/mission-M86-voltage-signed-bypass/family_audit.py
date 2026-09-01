#!/usr/bin/env python3
"""Exact finite audit of the explicit M86 phase/interleaving cover algebra."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import platform
import random
import subprocess
import time
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("m86_probe", HERE / "signed_bypass_probe.py")
M = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(M)


def canonical_word(d: int) -> M.Word:
    out = []
    for a in range(d - 1):
        out.extend([M.edge(a, a + 1)] * 2)
    out.extend([M.edge(0, 1)] * 2)
    return tuple(out)


def phase_moves(k: int, q: int, sign: int) -> list[M.Move]:
    positive = [(i, 1) for i in range(k - 1)]
    inverse = [(i, -1) for i in reversed(range(k - 1))]
    return (positive if sign == 1 else inverse) * q


def interleave(genus: M.Word, pair: M.Edge, slots: tuple[int, int]) -> M.Word:
    ans = []
    it = iter(genus)
    pair_slots = set(slots)
    for i in range(len(genus) + 2):
        ans.append(pair if i in pair_slots else next(it))
    return tuple(ans)


def stable_sort_moves(k: int, slots: tuple[int, int]) -> list[M.Move]:
    a, b = slots
    assert 0 <= a < b < k + 2
    # Bubble the right pair occurrence to the final slot, then the left one
    # to the penultimate slot.  For a genuinely disjoint pair every move is
    # an ordinary commutation under R.
    return [(i, 1) for i in range(b, k + 1)] + [(i, 1) for i in range(a, k)]


def relabel_word(word: M.Word, sigma: tuple[int, ...]) -> M.Word:
    return tuple(M.edge(sigma[a], sigma[b]) for a, b in word)


def audit_case(L: int, rng: random.Random) -> dict:
    d, k = 8 * L * L, 16 * L * L
    w = M.voltage_word(L)
    c = canonical_word(d)
    identity = tuple(range(d))
    assert len(w) == len(c) == k
    assert M.evaluate(w, d) == identity
    assert M.evaluate(c, d) == identity
    assert M.support_connected(w, d)
    assert M.support_connected(c, d)
    assert c[-2:] == (M.edge(0, 1),) * 2
    assert M.support_connected(c[:-2], d)
    assert M.evaluate(c[:-2], d) == identity

    phase_qs = sorted({0, 1, k // 2, k - 1})
    phase_checks = []
    for q in phase_qs:
        phased = M.apply_moves(w, phase_moves(k, q, 1))
        assert phased == w[q:] + w[:q]
        restored = M.apply_moves(phased, phase_moves(k, q, -1))
        assert restored == w
        phase_checks.append({"q": q, "forward_length": q * (k - 1), "ok": True})

    pair = M.edge(d, d + 1)
    all_slots = [(a, b) for a in range(k + 2) for b in range(a + 1, k + 2)]
    # Exhaust all interleavings for L<=2; the formula is symbolic thereafter.
    checked_slots = all_slots if L <= 2 else [all_slots[i] for i in (0, 1, len(all_slots)//2, -2, -1)]
    lengths = []
    for slots in checked_slots:
        source = interleave(w, pair, slots)
        moves = stable_sort_moves(k, slots)
        endpoint = M.apply_moves(source, moves)
        assert endpoint == w + (pair, pair)
        length_formula = 2 * k + 1 - slots[0] - slots[1]
        assert len(moves) == length_formula
        lengths.append(length_formula)

    # Generator-by-generator global-relabel equivariance, both signs.
    n = d
    sigma_list = list(range(n))
    rng.shuffle(sigma_list)
    sigma = tuple(sigma_list)
    relabel_checks = 0
    state = w
    for _ in range(min(100, 4 * k)):
        i = rng.randrange(k - 1)
        sign = 1 if rng.randrange(2) else -1
        lhs = M.move(relabel_word(state, sigma), i, sign)
        rhs = relabel_word(M.move(state, i, sign), sigma)
        assert lhs == rhs
        state = M.move(state, i, sign)
        relabel_checks += 1

    P = k * math.comb(k + 2, 2)
    mean_sort = sum(2 * k + 1 - a - b for a, b in all_slots) / len(all_slots)
    assert mean_sort == k
    return {
        "L": L,
        "d": d,
        "k": k,
        "W_identity_connected": True,
        "canonical_identity_connected": True,
        "canonical_marked_last_pair": True,
        "phase_checks": phase_checks,
        "interleavings_total": len(all_slots),
        "interleavings_checked": len(checked_slots),
        "stable_sort_length_min_checked": min(lengths),
        "stable_sort_length_max_checked": max(lengths),
        "stable_sort_exact_mean_all": mean_sort,
        "relabel_generator_checks_each_sign_mixed": relabel_checks,
        "indexed_family_size": P,
        "eta_lower_bound": f"1/{P}",
        "beta_length_bound": 50 * d * k**3,
        "mean_length_bound": 50 * d * k**3 + (k - 1) ** 2 / 2 + k,
        "maximum_length_bound": 50 * d * k**3 + (k - 1) ** 2 + 2 * k,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--L", nargs="+", type=int, default=[1, 2])
    parser.add_argument("--seed", type=int, default=860086)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    rng = random.Random(args.seed)
    records = [audit_case(L, rng) for L in args.L]
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "schema": "m86-family-audit-v1",
        "claim_status": "exact finite falsification checks plus symbolic counts",
        "scope_warning": "Classification-H supplies beta_L universally; this audit checks its source/target hypotheses and the phase/interleaving wrapper, not the internal normalizer implementation.",
        "convention": "(pq)(x)=p(q(x)); R(a,b)=(b,bab)",
        "commit": commit,
        "python": platform.python_version(),
        "dependencies": {},
        "seed": args.seed,
        "argv": [str(x) for x in __import__("sys").argv],
        "elapsed_seconds": time.time() - started,
        "records": records,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
