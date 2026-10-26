#!/usr/bin/env python3
"""Exact relabeling quotient of the relaxed word graph, with orbit weights.

This quotient is valid because simultaneous relabeling is a symmetry of the
actual transition kernel. It retains the entire ordered word modulo labels;
it is NOT the non-Markovian projection onto an unordered support graph.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import argparse
import hashlib
import json
import math
import platform
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


@lru_cache(maxsize=300000)
def canonical(word):
    """Lexicographic first-appearance labeling, trying both new-edge orientations."""
    candidates = [((), {})]
    for a, b in word:
        extended = []
        for prefix, labels in candidates:
            new = [x for x in (a, b) if x not in labels]
            orders = [new, new[::-1]] if len(new) == 2 else [new]
            for order in orders:
                mapping = labels.copy()
                for x in order:
                    mapping[x] = len(mapping)
                edge = tuple(sorted((mapping[a], mapping[b])))
                extended.append((prefix+(edge,), mapping))
        least = min(prefix for prefix, _ in extended)
        candidates = [(prefix, mapping) for prefix, mapping in extended if prefix == least]
    return candidates[0][0] if candidates else ()


def data(word):
    v = max((x for edge in word for x in edge), default=-1)+1
    p = list(range(v))
    parent = list(range(v))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, b in word:
        p[a], p[b] = p[b], p[a]
        parent[find(a)] = find(b)
    components = Counter(find(x) for x in range(v))
    rank = v-len(components)
    seen = set()
    cycle_count = 0
    for x in range(v):
        if x not in seen:
            cycle_count += 1
            while x not in seen:
                seen.add(x)
                x = p[x]
    return v, rank, v-cycle_count, sum(size == 2 for size in components.values())


def extensions(word, n):
    v = max((x for edge in word for x in edge), default=-1)+1
    for edge in combinations(range(v), 2):
        yield edge, 1
    if v < n:
        for a in range(v):
            yield (a, v), n-v
    if v+1 < n:
        yield (v, v+1), (n-v)*(n-v-1)//2


def states(n, m, k):
    current = {()}
    for r in range(1, m+1):
        nxt = set()
        for word in current:
            for edge, _ in extensions(word, n):
                new = canonical(word+(edge,))
                v, rank, defect, _ = data(new)
                # Each first merge of two support components increases prefix
                # reflection length. Final rank <= (m+final defect)/2.
                if 2*rank <= m+k and defect <= k+m-r:
                    nxt.add(new)
        current = nxt
    return sorted(word for word in current if data(word)[2] <= k)


def run(n, m, k):
    start = time.monotonic()
    words = states(n, m, k)
    index = {w:i for i, w in enumerate(words)}
    attrs = [data(w) for w in words]
    weights = [math.prod(range(n-v+1, n+1))//(2**b) for v, _, _, b in attrs]
    adjacency = []
    channel_count = 0
    for w in words:
        row = Counter()
        for i in range(m):
            for replacement, multiplicity in extensions(w, n):
                new = canonical(w[:i]+(replacement,)+w[i+1:])
                j = index.get(new)
                if j is not None:
                    row[j] += multiplicity
        adjacency.append(row)
    for i, row in enumerate(adjacency):
        assert sum(row.values()) <= m*n*(n-1)//2
        for j, count in row.items():
            assert weights[i]*count == weights[j]*adjacency[j].get(i, 0)
            channel_count += 1
    identities = [i for i, (_, _, d, _) in enumerate(attrs) if d == 0]
    dist = [-1]*len(words)
    queue = deque(identities)
    for i in identities:
        dist[i] = 0
    while queue:
        i = queue.popleft()
        for j in adjacency[i]:
            if dist[j] < 0:
                dist[j] = dist[i]+1
                queue.append(j)
    histogram = Counter()
    for i, d in enumerate(dist):
        histogram[d] += weights[i]
    ans = {'kind':'relabeling_quotient', 'N':n, 'm':m, 'k':k,
           'orbits':len(words), 'allowed_words':sum(weights),
           'identity_words':sum(weights[i] for i in identities),
           'checked_quotient_channels':channel_count,
           'all_orbits_reach_identity':all(d >= 0 for d in dist),
           'distance_to_identity_histogram':dict(histogram),
           'max_support':max((v for v, _, _, _ in attrs), default=0),
           'seconds':time.monotonic()-start}
    # Persist an explicit obstruction if one is found.
    if any(d < 0 for d in dist):
        ans['unreachable_word'] = words[dist.index(-1)]
    return ans


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--case', action='append', required=True)
    parser.add_argument('--output', type=Path, default=HERE/'quotient.jsonl')
    args = parser.parse_args()
    cases = [tuple(map(int, s.split(','))) for s in args.case]
    manifest = {'kind':'manifest', 'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
                'python':platform.python_version(), 'dependencies':'standard library only',
                'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'command':['python3','-B',str(Path(__file__).relative_to(ROOT))]+__import__('sys').argv[1:],
                'seeds':[], 'deterministic':True, 'cases':cases}
    with args.output.open('w') as out:
        out.write(json.dumps(manifest, sort_keys=True)+'\n')
        out.flush()
        for case in cases:
            ans = run(*case)
            out.write(json.dumps(ans, sort_keys=True)+'\n')
            out.flush()
            print(json.dumps(ans, sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
