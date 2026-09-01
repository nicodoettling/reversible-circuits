#!/usr/bin/env python3
"""Independent raw fixed-leaf flow check using only M119 definitions."""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
from collections import Counter, defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('m119_core', HERE / 'independent_audit.py')
assert SPEC is not None and SPEC.loader is not None
A = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(A)


def audit(d: int) -> dict[str, object]:
    v = d - 1
    upstairs = A.enumerate_z(d)
    fibers = defaultdict(list)
    for w in upstairs:
        if v in A.tree_leaves(d, A.join_data(d, w)[1]):
            z, _ = A.delete_strand(d, w, v)
            fibers[z].append(w)
    base = A.enumerate_z(d - 1)
    demands = []
    by_pair = defaultdict(list)
    for z in base:
        for site in range(len(z) - 1):
            for sign in (1, -1):
                zp = A.hurwitz(z, site, sign)
                if zp != z:
                    key = (z, site, sign, zp)
                    demands.append(key)
                    by_pair[(z, zp)].append((site, sign))

    counts = Counter()
    mark_lost = 0
    physical = 0
    for z, words in fibers.items():
        for w in words:
            for wp in A.word_neighbors(w):
                physical += 1
                if v not in A.tree_leaves(d, A.join_data(d, wp)[1]):
                    mark_lost += 1
                    continue
                zp, _ = A.delete_strand(d, wp, v)
                for site, sign in by_pair.get((z, zp), ()):
                    counts[(z, site, sign, zp)] += 1

    total_marked = sum(map(len, fibers.values()))
    base_sites = 2 * (d - 1) - 3
    physical_sites = 2 * d - 3
    ratios = []
    per_source_fractions = []
    for z, site, sign, zp in demands:
        count = counts[(z, site, sign, zp)]
        ratios.append(count * len(base) * base_sites / (total_marked * physical_sites))
        per_source_fractions.append(count / len(fibers[z]))
    return {
        'd': d,
        'fixed_missing_label': v,
        'upstairs_states': len(upstairs),
        'marked_states': total_marked,
        'base_states': len(base),
        'oriented_offdiagonal_demands': len(demands),
        'zero_demands': sum(counts[x] == 0 for x in demands),
        'lift_count_histogram': {str(k): n for k, n in sorted(Counter(counts.values()).items())},
        'normalized_ratio_min': min(ratios),
        'normalized_ratio_max': max(ratios),
        'per_source_fraction_min': min(per_source_fractions),
        'per_source_fraction_max': max(per_source_fractions),
        'physical_directed_proposals': physical,
        'mark_lost': mark_lost,
        'mark_loss_fraction': mark_lost / physical,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    payload = {
        'metadata': {
            'python': platform.python_version(),
            'seed': None,
            'dependencies': {},
            'imports_m112': False,
        },
        'row': audit(4),
        'scope': 'exact finite diagnostic only; no universal flow domination follows',
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n')
    print(json.dumps(payload, sort_keys=True))


if __name__ == '__main__':
    main()
