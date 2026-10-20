#!/usr/bin/env python3
"""Deterministic exact checks. Standard library only; no random sampling."""
from collections import Counter, defaultdict, deque
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json
import platform
import subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name("results.jsonl")


class Group:
    def __init__(self, n):
        self.n = n
        self.perms = list(permutations(range(n)))
        self.index = {p: i for i, p in enumerate(self.perms)}
        self.e = self.index[tuple(range(n))]
        self.gates = []
        for a, b in combinations(range(n), 2):
            p = list(range(n))
            p[a], p[b] = p[b], p[a]
            self.gates.append(self.index[tuple(p)])
        self.M = len(self.gates)
        self.mul = [[self.index[tuple(p[q[i]] for i in range(n))]
                     for q in self.perms] for p in self.perms]
        self.inv = []
        for p in self.perms:
            z = [0] * n
            for i, j in enumerate(p):
                z[j] = i
            self.inv.append(self.index[tuple(z)])
        self.gate_index = {g: i for i, g in enumerate(self.gates)}

    def eval(self, word):
        g = self.e
        for t in word:
            g = self.mul[g][self.gates[t]]
        return g

    def counts(self, m):
        out = [[int(g == self.e) for g in range(len(self.perms))]]
        for _ in range(m):
            out.append([sum(out[-1][self.mul[g][t]] for t in self.gates)
                        for g in range(len(self.perms))])
        return out

    def fibers(self, m):
        out = defaultdict(list)
        for w in product(range(self.M), repeat=m):
            out[self.eval(w)].append(w)
        return out

    def cycle_type(self, g):
        unseen = set(range(self.n))
        lengths = []
        while unseen:
            j = min(unseen)
            k = 0
            while j in unseen:
                unseen.remove(j)
                j = self.perms[g][j]
                k += 1
            lengths.append(k)
        return tuple(sorted(lengths, reverse=True))

    def hurwitz(self, w, j, sign):
        a, b = (self.gates[t] for t in w[j:j+2])
        if sign == 1:
            pair = (b, self.mul[self.mul[b][a]][b])
        else:
            pair = (self.mul[self.mul[a][b]][a], a)
        return w[:j] + tuple(self.gate_index[t] for t in pair) + w[j+2:]


def components(adj):
    unseen = set(adj)
    ans = 0
    while unseen:
        todo = [unseen.pop()]
        ans += 1
        while todo:
            for y in adj[todo.pop()]:
                if y in unseen:
                    unseen.remove(y)
                    todo.append(y)
    return ans


def kernel_checks(G, m, words):
    # Exact common-denominator matrix for K_A=I/2+H/4+R/4.
    D = 8 * (m - 1) * G.M
    rows, hrows = {}, {}
    channels = 0
    for w in words:
        row = Counter({w: 4 * (m - 1) * G.M})
        hrow = set()
        for j in range(m - 1):
            for sign in (-1, 1):
                v = G.hurwitz(w, j, sign)
                assert G.eval(v) == G.eval(w)
                row[v] += G.M
                hrow.add(v)
                channels += 1
            if w[j] == w[j+1]:
                for s in range(G.M):
                    v = w[:j] + (s, s) + w[j+2:]
                    assert G.eval(v) == G.eval(w)
                    row[v] += 2
                    channels += 1
            else:
                row[w] += 2 * G.M
        assert sum(row.values()) == D
        rows[w], hrows[w] = row, hrow
    for w, row in rows.items():
        for v, a in row.items():
            assert rows[v][w] == a
    assert components(rows) == 1
    return {"kind": "actual_kernel", "N": G.n, "m": m,
            "states": len(words), "primitive_channels": channels,
            "row_sum": D, "detailed_balance": True,
            "components": 1, "hurwitz_components": components(hrows)}


def marginal_checks(G, m, fibers):
    counts = G.counts(m)
    reps = {}
    for g in fibers:
        reps.setdefault(G.cycle_type(g), g)
    checks = 0
    max_tv = {}
    for ct, g in reps.items():
        for r in range(1, min(3, m) + 1):
            worst = F(0)
            for positions in combinations(range(m), r):
                marg = Counter(tuple(w[i] for i in positions) for w in fibers[g])
                tv = F(0)
                for u in product(range(G.M), repeat=r):
                    h = G.eval(u)
                    # Z_(m-r)(h^-1 g), even for scattered observed positions.
                    predicted = counts[m-r][G.mul[G.inv[h]][g]]
                    assert marg[u] == predicted
                    tv += abs(F(marg[u], len(fibers[g])) - F(1, G.M**r))
                    checks += 1
                worst = max(worst, tv / 2)
            max_tv[f"{ct}:r{r}"] = str(worst)
    return {"kind": "marginal_identity", "N": G.n, "m": m,
            "endpoint_types": len(reps), "integer_equalities": checks,
            "max_subset_tv_to_iid": max_tv}


def heatbath_density(words, density, lengths):
    m = len(words[0])
    out = [f / 2 for f in density]
    for r in lengths:
        coefficient = F(1, 2 * len(lengths) * (m-r+1))
        for j in range(m-r+1):
            cells = defaultdict(list)
            for i, w in enumerate(words):
                cells[w[:j] + w[j+r:]].append(i)
            for cell in cells.values():
                mean = sum((density[i] for i in cell), F(0)) / len(cell)
                for i in cell:
                    out[i] += coefficient * mean
    return out


def hidden_mode(G, m, g, words, cut):
    pinned = [G.eval(w[:cut]) == G.e for w in words]
    mass = F(sum(pinned), len(words))
    assert mass == F(1, 3)
    selected = [w for w, pin in zip(words, pinned) if pin]
    # Exact k-wise independence, stronger than short consecutive windows.
    equalities = 0
    k = min(cut, m-cut) - 1
    for r in range(1, k+1):
        for positions in combinations(range(m), r):
            c = Counter(tuple(w[i] for i in positions) for w in selected)
            assert len(c) == 3**r
            assert all(F(v, len(selected)) == F(1, 3**r) for v in c.values())
            equalities += len(c)
    density = [F(3 if pin else 0) for pin in pinned]
    modes = []
    for lengths in ((2,), (3, 4, 5)):
        hit = sum((F(sum(j < cut < j+r for j in range(m-r+1)),
                         2 * len(lengths) * (m-r+1)) for r in lengths), F(0))
        lam = 1 - hit
        advanced = heatbath_density(words, density, lengths)
        assert all(a-1 == lam*(b-1) for a, b in zip(advanced, density))
        current = density
        tvs = []
        for t in range(4):
            tv = sum((abs(v-1) for v in current), F(0)) / (2*len(words))
            assert tv == F(2, 3) * lam**t
            tvs.append(str(tv))
            if t < 3:
                current = heatbath_density(words, current, lengths)
        modes.append({"lengths": lengths, "lambda": str(lam),
                      "tv_t_0_through_3": tvs})
    return {"kind": "hidden_prefix_mode", "N": 3, "m": m,
            "endpoint": list(G.perms[g]), "cut": cut,
            "states": len(words), "pinned_states": len(selected),
            "k_wise_independent": k, "marginal_equalities": equalities,
            "initial_tv": "2/3", "exact_eigenmodes": modes}


def schedule_checks():
    # Exhaustive interval geometry, including boundary cuts and short lengths.
    tests = 0
    for m in range(2, 31):
        for r in range(2, min(5, m)+1):
            for a in range(m):
                for b in range(a, m):
                    crossing = 0
                    for j in range(m-r+1):
                        if j <= b and j+r-1 >= a and (j < a or j+r-1 > b):
                            crossing += 1
                            assert min(a, j) >= a-(r-1)
                            assert max(b, j+r-1) <= b+(r-1)
                            assert max(b, j+r-1)-min(a, j)-(b-a) <= r-1
                    assert crossing <= 2*(r-1)
                    tests += 1
            for cut in range(1, m):
                count = sum(j < cut < j+r for j in range(m-r+1))
                assert count <= r-1
                if r-1 <= cut <= m-r+1:
                    assert count == r-1
    # Probability/moment coupon inequality with exact rationals.
    for q in range(1, 13):
        p = F(1, 2*q+3)
        for t in range(25):
            mean = q*(1-p)**t
            second = mean+q*(q-1)*(1-2*p)**t
            assert second <= mean+mean*mean
    beta = 1-F(15, 17)**2
    assert 1-2*beta >= F(1, 2)
    return {"kind": "schedule_geometry", "interval_cases": tests,
            "macro_beta_at_eta_1_over_16": str(beta),
            "macro_contraction_numerator": str(1-2*beta)}


def macro_conditionals():
    G = Group(4)
    L = 5
    Z = G.counts(L)
    even = [g for g in range(24) if (4-len(G.cycle_type(g))) % 2 == 0]
    odd = [g for g in range(24) if g not in even]
    eta = max(abs(F(12*Z[L][g], G.M**L)-1) for g in odd)
    assert eta <= F(1, 16)
    a = ((1-eta)/(1+eta))**2
    conditionals = []
    for left, right in product(even, repeat=2):
        weights = [Z[L][G.mul[G.inv[left]][x]] *
                   Z[L][G.mul[G.inv[x]][right]] for x in odd]
        norm = sum(weights)
        row = [F(w, norm) for w in weights]
        assert min(row) >= a/12
        conditionals.append(row)
    max_tv = max(sum((abs(x-y) for x, y in zip(p, q)), F(0))/2
                 for p, q in combinations(conditionals, 2))
    assert max_tv <= 1-a
    slots = 0
    for L in range(1, 8):
        for m in range(2*L, 50):
            q = m//L
            lengths = [L]*(q-1)+[m-(q-1)*L]
            cuts = [0]
            for ell in lengths:
                cuts.append(cuts[-1]+ell)
            for j in range(m-1):
                weight = sum((F(1, cuts[i+2]-cuts[i]-1)
                              for i in range(q-1)
                              if cuts[i] <= j and j+1 < cuts[i+2]), F(0))
                assert weight <= F(2, 2*L-1)
                slots += 1
    return {"kind": "macro_conditionals_and_comparison", "N": 4,
            "block_length": 5, "relative_error": str(eta),
            "conditional_laws": len(conditionals),
            "max_conditional_tv": str(max_tv),
            "coupling_bound": str(1-a), "comparison_slots_checked": slots}


def dense_counts():
    rows = []
    for n, m, cut, k in ((3, 20, 10, 3), (4, 64, 32, 4), (5, 126, 62, 5)):
        G = Group(n)
        Z = G.counts(m)
        worst_eta = F(0)
        parity = (1 if (m-cut) % 2 == 0 else -1)
        for h in range(len(G.perms)):
            sign = (-1)**(n-len(G.cycle_type(h)))
            if sign == parity:
                eta = abs(F(len(G.perms)*Z[m-cut][h], 2*G.M**(m-cut))-1)
                worst_eta = max(worst_eta, eta)
        endpoint_mass = F(Z[cut][G.e]*Z[m-cut][G.e], Z[m][G.e])
        rows.append({"N": n, "m": m, "cut": cut,
                     "stationary_pin_probability": str(endpoint_mass),
                     "initial_global_tv": float(1-endpoint_mass),
                     "completion_relative_error": float(worst_eta),
                     "window_k": k})
    return {"kind": "dense_counts", "rows": rows}


def main():
    records = [{"kind": "manifest", "commit": subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "python": platform.python_version(), "dependencies": "stdlib only",
        "seed": None, "randomness": "none; deterministic exhaustive checks",
        "command": f"python3 -B {Path(__file__).relative_to(ROOT)}",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}]
    for n, m in ((3, 4), (4, 4), (4, 6), (3, 5), (4, 5)):
        G = Group(n)
        fibers = G.fibers(m)
        records.append(marginal_checks(G, m, fibers))
        if G.e in fibers:
            records.append(kernel_checks(G, m, fibers[G.e]))
    G = Group(3)
    fibers = G.fibers(8)
    for g, words in fibers.items():
        records.append(hidden_mode(G, 8, g, words, 4))
    # Exceptional cases: N2 singleton; m0 and m2; odd lengths handled above.
    for n in (2, 3, 4):
        G = Group(n)
        for m in (0, 1, 2):
            fibers = G.fibers(m)
            assert all(len(ws) == 1 for ws in fibers.values()) if n == 2 else True
            assert sum(map(len, fibers.values())) == G.M**m
            if m == 2:
                assert len(fibers[G.e]) == G.M
    records.append({"kind": "boundary_cases", "N": [2, 3, 4],
                    "m": [0, 1, 2], "status": "passed"})
    records.append(schedule_checks())
    records.append(macro_conditionals())
    records.append(dense_counts())
    OUT.write_text("".join(json.dumps(r, sort_keys=True)+"\n" for r in records))
    print(json.dumps({"status": "passed", "records": len(records),
                      "output": str(OUT.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
