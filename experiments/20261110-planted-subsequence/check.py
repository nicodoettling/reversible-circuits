#!/usr/bin/env python3
"""Exact finite planted-subsequence laws; Python standard library only."""

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import gzip
from itertools import combinations, permutations, product
import json
import math
from pathlib import Path
import platform
import random
import subprocess
import sys
import time


def rational(value):
    value = Fraction(value)
    return {"exact": str(value), "decimal": float(value)}


class Group:
    def __init__(self, n, length):
        self.n = n
        self.edges = list(combinations(range(n), 2))
        self.edge_index = {e: i for i, e in enumerate(self.edges)}
        self.perms = list(permutations(range(n)))
        self.index = {p: i for i, p in enumerate(self.perms)}
        self.identity = self.index[tuple(range(n))]
        self.right = []
        self.inverse = []
        self.conjugations = []
        for p in self.perms:
            row = []
            for a, b in self.edges:
                nxt = list(p)
                nxt[a], nxt[b] = nxt[b], nxt[a]
                row.append(self.index[tuple(nxt)])
            self.right.append(row)
            inv = [0] * n
            for i, x in enumerate(p):
                inv[x] = i
            self.inverse.append(self.index[tuple(inv)])
            self.conjugations.append(tuple(
                self.edge_index[tuple(sorted((p[a], p[b])))]
                for a, b in self.edges))
        base = [0] * len(self.perms)
        base[self.identity] = 1
        self.completions = [base]
        for _ in range(length):
            old = self.completions[-1]
            self.completions.append([
                sum(old[q] for q in row) for row in self.right])

    def evaluate(self, word):
        p = self.identity
        for edge in word:
            p = self.right[p][edge]
        return p

    def literal_evaluate(self, word):
        # Independent point-action evaluator: apply the rightmost gate first.
        answer = []
        for x in range(self.n):
            for e in reversed(word):
                a, b = self.edges[e]
                if x == a:
                    x = b
                elif x == b:
                    x = a
            answer.append(x)
        return tuple(answer)

    def cycle_type(self, p):
        perm = self.perms[p]
        seen, lengths = set(), []
        for x in range(self.n):
            if x in seen:
                continue
            length = 0
            while x not in seen:
                seen.add(x)
                length += 1
                x = perm[x]
            lengths.append(length)
        return tuple(sorted(lengths, reverse=True))

    def orbit_bridges(self, length):
        """Lexicographic orbit representatives under simultaneous relabeling."""
        def visit(word, p, stabilizer):
            remaining = length - len(word)
            if not remaining:
                assert p == self.identity
                yield tuple(word), len(self.perms) // len(stabilizer)
                return
            for e, nxt in enumerate(self.right[p]):
                if not self.completions[remaining - 1][nxt]:
                    continue
                if any(self.conjugations[g][e] < e for g in stabilizer):
                    continue
                fixed = tuple(g for g in stabilizer
                              if self.conjugations[g][e] == e)
                yield from visit(word + [e], nxt, fixed)
        yield from visit([], self.identity, tuple(range(len(self.perms))))

    def draw_bridge(self, length, rng):
        if not self.completions[length][self.identity]:
            raise ValueError("empty identity fiber")
        p, word = self.identity, []
        for remaining in range(length, 0, -1):
            draw = rng.randrange(self.completions[remaining][p])
            for e, nxt in enumerate(self.right[p]):
                weight = self.completions[remaining - 1][nxt]
                if draw < weight:
                    word.append(e)
                    p = nxt
                    break
                draw -= weight
            else:
                raise AssertionError("invalid completion weights")
        assert p == self.identity
        return tuple(word)

    def conjugate_edge(self, by, edge):
        a, b = self.edges[by]
        def move(x):
            return b if x == a else a if x == b else x
        return self.edge_index[tuple(sorted(map(move, self.edges[edge])))]

    def unplant(self, left, right, positions):
        # Reverse the selected-left stable sort (u,s) -> (s,s*u*s).
        length = len(left) + len(right)
        flags = [i in positions for i in range(length)]
        swaps = []
        target = 0
        for i in range(length):
            if flags[i]:
                for j in range(i - 1, target - 1, -1):
                    flags[j], flags[j + 1] = flags[j + 1], flags[j]
                    swaps.append(j)
                target += 1
        word = list(left + right)
        for j in reversed(swaps):
            s, v = word[j:j + 2]
            word[j:j + 2] = [self.conjugate_edge(s, v), s]
        return tuple(word)

    def draw_planted(self, length, k, rng):
        if length % 2 or k % 2 or not 0 <= k <= length:
            raise ValueError("infeasible planting parameters")
        positions = tuple(sorted(rng.sample(range(length), k)))
        word = self.unplant(self.draw_bridge(k, rng),
                            self.draw_bridge(length - k, rng), positions)
        return word, positions

    def transport(self, word):
        p, answer = self.identity, []
        for e in word:
            answer.append(self.conjugations[p][e])
            p = self.right[p][e]
        return tuple(answer)


def subset_products(group, word):
    values = [group.identity] * (1 << len(word))
    for mask in range(1, len(values)):
        last = mask.bit_length() - 1
        values[mask] = group.right[values[mask ^ (1 << last)]][word[last]]
    return values


def mitm_counts(group, word):
    halves = []
    middle = len(word) // 2
    for half in (word[:middle], word[middle:]):
        hist = defaultdict(Counter)
        for mask, p in enumerate(subset_products(group, half)):
            hist[mask.bit_count()][p] += 1
        halves.append(hist)
    counts = [0] * (len(word) + 1)
    for a, left in halves[0].items():
        for b, right in halves[1].items():
            counts[a + b] += sum(v * right[group.inverse[p]]
                                 for p, v in left.items())
    return counts


def features(group, word):
    n, length = group.n, len(word)
    multiplicities = tuple(sorted(Counter(word).values(), reverse=True))
    pairs = sum(x * (x - 1) // 2 for x in multiplicities)
    transported_pairs = sum(x * (x - 1) // 2
                            for x in Counter(group.transport(word)).values())
    repeats = sum(a == b for a, b in zip(word, word[1:]))
    parent = list(range(n))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    used = set()
    for e in word:
        a, b = group.edges[e]
        used.update((a, b))
        parent[root(a)] = root(b)
    vertices = Counter(root(x) for x in range(n))
    weights = Counter(root(group.edges[e][0]) for e in word)
    components = tuple(sorted((size, weights[r])
                              for r, size in vertices.items()))
    prefix = group.cycle_type(group.evaluate(word[:length // 2]))
    fixed = prefix.count(1)
    window_types = []
    for size in (2, 3, 4, 6):
        if size <= length:
            histogram = Counter(group.cycle_type(group.evaluate(word[j:j + size]))
                                for j in range(length - size + 1))
            window_types.append((size, tuple(sorted(histogram.items()))))
    values = {
        "repeat_pairs": pairs,
        "transported_repeat_pairs": transported_pairs,
        "distinct_edges": len(multiplicities),
        "edge_multiplicities": multiplicities,
        "adjacent_repeats": repeats,
        "support_vertices": len(used),
        "weighted_components": components,
        "middle_prefix_cycle_type": prefix,
        "middle_prefix_fixed_points": fixed,
        "middle_prefix_standard_character": fixed - 1,
        "window_cycle_histograms": tuple(window_types),
    }
    values["joint_cheap_observables"] = tuple(values.values())
    return values


def threshold_attack(hist, z, total, column):
    best = (Fraction(0), None, None)
    null, plant = 0, 0
    for value, counts in sorted(hist.items()):
        null += counts[0]
        plant += counts[column]
        difference = Fraction(plant, total) - Fraction(null, z)
        if abs(difference) > best[0]:
            best = (abs(difference), value, difference >= 0)
    return {"advantage": rational(best[0]), "threshold": best[1],
            "accept_planted_when": "<= threshold" if best[2] else "> threshold"}


def exact_case(n, length, literal_check=False):
    started = time.monotonic()
    group = Group(n, length)
    ks = list(range(2, length, 2))
    z = group.completions[length][group.identity]
    mask_counts = [0] * (1 << length)
    witness_hist = {k: Counter() for k in ks}
    support_hist = {k: Counter() for k in ks}
    feature_hist = defaultdict(dict)
    orbit_count = represented = 0
    for word, weight in group.orbit_bridges(length):
        orbit_count += 1
        represented += weight
        products = subset_products(group, word)
        witnesses = Counter()
        for mask, p in enumerate(products):
            if p == group.identity:
                mask_counts[mask] += weight
                witnesses[mask.bit_count()] += 1
        for k in ks:
            witness_hist[k][witnesses[k]] += weight
        observed = features(group, word)
        assert observed["transported_repeat_pairs"] == witnesses[length - 2]
        for k in ks:
            v = observed["support_vertices"]
            assert weight % math.comb(n, v) == 0
            support_hist[k][v, witnesses[k]] += weight // math.comb(n, v)
        for name, value in observed.items():
            counts = feature_hist[name].setdefault(value, [0] * (len(ks) + 1))
            counts[0] += weight
            for j, k in enumerate(ks, 1):
                counts[j] += weight * witnesses[k]
        if orbit_count <= 30:
            assert group.literal_evaluate(word) == tuple(range(n))
            assert mitm_counts(group, word) == [witnesses[k] for k in range(length + 1)]
            transported = group.transport(word)
            assert group.transport(transported) == word
            other = subset_products(group, transported)
            for mask, p in enumerate(products):
                assert p == other[((1 << length) - 1) ^ mask]
    assert represented == z
    for mask, count in enumerate(mask_counts):
        k = mask.bit_count()
        assert count == (group.completions[k][group.identity]
                         * group.completions[length - k][group.identity])
    if literal_check:
        independent = [0] * (1 << length)
        count = 0
        for word in product(range(len(group.edges)), repeat=length):
            if group.literal_evaluate(word) != tuple(range(n)):
                continue
            count += 1
            for mask in range(1 << length):
                selected = tuple(word[j] for j in range(length) if mask >> j & 1)
                if group.literal_evaluate(selected) == tuple(range(n)):
                    independent[mask] += 1
        assert count == z and independent == mask_counts
    cases = []
    for j, k in enumerate(ks, 1):
        hist = witness_hist[k]
        total = sum(x * count for x, count in hist.items())
        assert total == math.comb(length, k) * mask_counts[(1 << k) - 1]
        mean = Fraction(total, z)
        variance = sum(count * (Fraction(x) - mean) ** 2
                       for x, count in hist.items()) / z
        tv = Fraction(sum(count * abs(z * x - total) for x, count in hist.items()),
                      2 * z * total)
        attacks = {}
        for name, fh in feature_hist.items():
            assert sum(v[0] for v in fh.values()) == z
            assert sum(v[j] for v in fh.values()) == total
            attack_tv = Fraction(sum(abs(total * v[0] - z * v[j])
                                     for v in fh.values()), 2 * z * total)
            assert attack_tv <= tv
            attacks[name] = rational(attack_tv)
        cases.append({
            "N": n, "m": length, "k": k, "bridge_count": z,
            "orbit_count": orbit_count, "fixed_I_event_count": mask_counts[(1 << k) - 1],
            "fixed_I_probability": rational(Fraction(mask_counts[(1 << k) - 1], z)),
            "null_witness_mean": rational(mean), "null_witness_variance": rational(variance),
            "null_no_witness_probability": rational(Fraction(hist[0], z)),
            "total_variation": rational(tv), "feature_TV": attacks,
            "repeat_pair_threshold": threshold_attack(feature_hist["repeat_pairs"], z, total, j),
            "witness_histogram": [[x, hist[x]] for x in sorted(hist)],
            "support_witness_coefficients": [[v, x, count]
                                              for (v, x), count in sorted(support_hist[k].items())],
        })
    raw_features = {
        name: [{"value": value, "null_count": counts[0],
                "planted_numerators_by_k": dict(zip(ks, counts[1:]))}
               for value, counts in sorted(hist.items())]
        for name, hist in feature_hist.items()
    }
    return {"N": n, "m": length, "seconds": time.monotonic() - started,
            "literal_cross_check": literal_check, "mask_event_counts": mask_counts,
            "feature_histograms": raw_features, "cases": cases}


def extrapolate_fixed_length(row):
    """Exact polynomial evaluation, not statistical extrapolation; requires N=m."""
    length = row["m"]
    assert row["N"] == length
    answer = []
    for n in (8, 10, 20, 50, 100, 1000, 1000000):
        for case in row["cases"]:
            hist = Counter()
            for v, x, count in case["support_witness_coefficients"]:
                hist[x] += math.comb(n, v) * count
            z = sum(hist.values())
            total = sum(x * count for x, count in hist.items())
            tv = Fraction(sum(count * abs(z * x - total) for x, count in hist.items()),
                          2 * z * total)
            answer.append({"N": n, "m": length, "k": case["k"], "bridge_count": z,
                           "TV": rational(tv), "mean_witnesses": rational(Fraction(total, z)),
                           "null_no_witness": rational(Fraction(hist[0], z))})
    # Verify the support coefficient representation against separately enumerated N<8.
    return answer


def sampler_checks():
    result = {"exhaustive": [], "seeded": [], "boundaries": []}
    for n, length in ((3, 4), (4, 4), (4, 6)):
        group = Group(n, length)
        bridges = {}
        for size in range(0, length + 1, 2):
            bridges[size] = [word for word in product(range(len(group.edges)), repeat=size)
                             if group.literal_evaluate(word) == tuple(range(n))]
        for k in range(2, length, 2):
            for positions in combinations(range(length), k):
                constructed = {group.unplant(a, b, positions)
                               for a in bridges[k] for b in bridges[length - k]}
                reference = {word for word in bridges[length]
                             if group.literal_evaluate(tuple(word[i] for i in positions))
                             == tuple(range(n))}
                assert constructed == reference
                assert len(constructed) == len(bridges[k]) * len(bridges[length - k])
            result["exhaustive"].append({"N": n, "m": length, "k": k,
                                         "all_index_sets_pass": True})
    for n, length, k in ((4, 6, 2), (5, 8, 4)):
        group = Group(n, length)
        for seed in (17, 29, 43):
            rng = random.Random(seed)
            counts = {"null": Counter(), "planted": Counter()}
            for _ in range(200):
                null = group.draw_bridge(length, rng)
                planted, positions = group.draw_planted(length, k, rng)
                assert group.literal_evaluate(null) == tuple(range(n))
                assert group.literal_evaluate(planted) == tuple(range(n))
                assert group.literal_evaluate(tuple(planted[i] for i in positions)) == tuple(range(n))
                for name, word in (("null", null), ("planted", planted)):
                    products = subset_products(group, word)
                    witnesses = sum(p == group.identity and mask.bit_count() == k
                                    for mask, p in enumerate(products))
                    assert mitm_counts(group, word)[k] == witnesses
                    counts[name][witnesses] += 1
            result["seeded"].append({"N": n, "m": length, "k": k, "seed": seed,
                                     "draws_per_world": 200, "witness_histograms": counts})
    for n, length, k in ((2, 0, 0), (2, 2, 0), (2, 2, 2), (2, 6, 2),
                          (3, 4, 0), (3, 4, 4)):
        group = Group(n, length)
        word, positions = group.draw_planted(length, k, random.Random(17))
        assert group.literal_evaluate(word) == tuple(range(n))
        assert group.literal_evaluate(tuple(word[i] for i in positions)) == tuple(range(n))
        result["boundaries"].append({"N": n, "m": length, "k": k, "valid": True})
    for length, k in ((3, 2), (4, 1), (4, 5)):
        group = Group(3, length)
        try:
            group.draw_planted(length, k, random.Random(17))
        except ValueError:
            result["boundaries"].append({"N": 3, "m": length, "k": k, "rejected": True})
        else:
            raise AssertionError("infeasible case accepted")
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    started = time.monotonic()
    result = {"metadata": {
        "command": "python3 -B " + " ".join(sys.argv),
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "python": platform.python_version(), "dependencies": "standard library only",
        "seed_purpose": "sampler smoke checks only; conclusions use deterministic exact counts",
        "seeds": [17, 29, 43],
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }, "sampler_checks": sampler_checks(), "sweep": []}
    parameters = ((3, 4), (4, 4), (4, 6), (3, 6), (3, 8), (3, 10),
                  (4, 8), (5, 6), (5, 8), (6, 6), (6, 8), (3, 12), (8, 8))
    raw_features = []
    for n, length in parameters:
        row = exact_case(n, length, literal_check=(n, length) in parameters[:3])
        raw_features.append({"N": n, "m": length,
                             "feature_histograms": row.pop("feature_histograms")})
        result["sweep"].append(row)
        print(json.dumps({"N": n, "m": length, "seconds": round(row["seconds"], 3),
                          "cases": [{"k": c["k"], "TV": c["total_variation"]["decimal"],
                                     "repeat_TV": c["feature_TV"]["repeat_pairs"]["decimal"],
                                     "null_no_witness": c["null_no_witness_probability"]["decimal"]}
                                    for c in row["cases"]]}), flush=True)
        result["metadata"]["elapsed_seconds"] = time.monotonic() - started
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    universal = result["sweep"][-1]
    for row in result["sweep"]:
        if row["m"] != universal["m"]:
            continue
        for case, universal_case in zip(row["cases"], universal["cases"]):
            hist = Counter()
            for v, x, count in universal_case["support_witness_coefficients"]:
                hist[x] += math.comb(row["N"], v) * count
            assert {x: count for x, count in hist.items() if count} == dict(case["witness_histogram"])
    result["fixed_length_polynomial_evaluations"] = extrapolate_fixed_length(universal)
    raw_path = args.output.with_name("feature-histograms.json.gz")
    raw_path.write_bytes(gzip.compress(json.dumps(raw_features, separators=(",", ":")).encode(), mtime=0))
    result["metadata"]["feature_histograms"] = raw_path.name
    result["metadata"]["elapsed_seconds"] = time.monotonic() - started
    args.output.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
