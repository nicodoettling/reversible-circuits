"""Exact support marginal and lumpability audit of the actual all-pair walk."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import importlib.util
import json
import platform
import subprocess

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent/'20261014-133815-cycle-excess-one/check.py'
spec = importlib.util.spec_from_file_location('old', SOURCE)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)


def support(w):
    return tuple(sorted(w))


def word_row(w, n):
    gates = tuple(combinations(range(n), 2))
    C = len(w)*(len(w)-1)//2
    M = len(gates)
    # Integer numerator, common denominator 8*C*M.
    row = Counter({w: 4*C*M})
    for i, j in combinations(range(len(w)), 2):
        for sign in (1, -1):
            row[old.core.macro(w, i, j, 'H', sign)] += M
        for s in gates:
            row[old.core.macro(w, i, j, 'R', s)] += 2
    assert sum(row.values()) == 8*C*M
    return row, 8*C*M


def project(row, simple=False):
    result = Counter()
    for z, count in row.items():
        G = tuple(sorted(set(z))) if simple else support(z)
        result[G] += count
    return result


def audit(n, m, g):
    words = sorted(old.bridge_words(n, m, g))
    fibers = defaultdict(list)
    rows = {}
    graph_rows = {}
    simple_rows = {}
    for w in words:
        row, den = word_row(w, n)
        assert all(old.evaluate(z, n) == g for z in row)
        rows[w] = row
        graph_rows[w] = project(row)
        simple_rows[w] = project(row, simple=True)
        fibers[support(w)].append(w)
    for w in words:
        for z, count in rows[w].items():
            assert rows[z][w] == count
    witness = None
    simple_witness = None
    differing_fibers = 0
    flows = defaultdict(Counter)
    for G, fiber in sorted(fibers.items()):
        base = fiber[0]
        different = False
        for w in fiber:
            flows[G].update(graph_rows[w])
            if graph_rows[w] != graph_rows[base]:
                different = True
                if witness is None:
                    H = min(H for H in graph_rows[w].keys() | graph_rows[base].keys()
                            if graph_rows[w][H] != graph_rows[base][H])
                    witness = dict(words=[base, w], common_graph=G, destination_graph=H,
                        probabilities=[str(F(graph_rows[x][H], den)) for x in (base, w)])
            if simple_rows[w] != simple_rows[base] and simple_witness is None:
                H = min(H for H in simple_rows[w].keys() | simple_rows[base].keys()
                        if simple_rows[w][H] != simple_rows[base][H])
                simple_witness = dict(words=[base, w], destination_simple_graph=H,
                    probabilities=[str(F(simple_rows[x][H], den)) for x in (base, w)])
        differing_fibers += different
    for G, row in flows.items():
        assert sum(row.values()) == den*len(fibers[G])
        for H, flow in row.items():
            assert flows[H][G] == flow
    # Difference between the true graph return at time 2 (uniform lift)
    # and two steps of the stationary-flow projection. This equals a
    # positive within-fiber variance, divided by pi_G(G).
    two_step = None
    if witness:
        G = tuple(tuple(e) for e in witness['destination_graph'])
        true = sum(F(graph_rows[w][G], den)**2 for w in words)/len(fibers[G])
        averaged = sum(F(flows[H][G], den)**2/len(fibers[H])
                       for H in fibers)/len(fibers[G])
        assert true > averaged
        variance = sum(sum(F(graph_rows[w][G], den)**2 for w in fiber)
                       - F(flows[H][G], den)**2/len(fiber)
                       for H, fiber in fibers.items())/len(fibers[G])
        assert true-averaged == variance
        two_step = dict(initial_graph=G, actual_return=str(true),
                        averaged_kernel_return=str(averaged), difference=str(variance))
    return dict(N=n, m=m, endpoint=g, states=len(words),
                support_graphs=len(fibers), fiber_size_histogram=dict(sorted(Counter(map(len, fibers.values())).items())),
                nonlumpable_fibers=differing_fibers, witness=witness,
                simple_graph_witness=simple_witness, two_step=two_step,
                exact_endpoint_balance_and_weighted_projection=True)


def explicit_star():
    a, b = (0, 2), (0, 1)
    words = ((a, a, a, b), (a, b, a, a))
    triangle = tuple(combinations(range(3), 2))
    rows = [word_row(w, 3) for w in words]
    all_edges = [F(project(row, simple=True)[triangle], den) for row, den in rows]
    return dict(words=words, endpoint=old.evaluate(words[0], 3),
                same_endpoint=old.evaluate(words[0], 3)==old.evaluate(words[1], 3),
                common_graph=support(words[0]),
                probability_all_three_edges_present=list(map(str, all_edges)))


def slow_projection_counterexample(delta):
    P = [[F(0) for _ in range(4)] for _ in range(4)]
    for i, j, rate in ((0, 1, F(1, 4)), (2, 3, F(1, 4)), (1, 2, delta)):
        P[i][j] = P[j][i] = rate
    for i in range(4):
        P[i][i] = 1-sum(P[i])
        assert P[i][i] >= F(1, 2)
    fibers = ((0, 1, 2), (3,))
    bar = [[sum(P[i][j] for i in A for j in B)/len(A) for B in fibers] for A in fibers]
    assert bar[0][1] == F(1, 12) and bar[1][0] == F(1, 4)
    assert bar[0][1]+bar[1][0] == F(1, 3)
    # Finite check of the analytic union-bound lower bound.
    mu = [F(1), F(0), F(0), F(0)]
    for t in range(33):
        assert mu[3] <= t*delta
        mu = [sum(mu[i]*P[i][j] for i in range(4)) for j in range(4)]
    return dict(delta=str(delta), matrix=[[str(v) for v in r] for r in P],
                projected_matrix=[[str(v) for v in r] for r in bar],
                projected_gap='1/3', marginal_TV_lower_bound='1/4-t*delta')


if __name__ == '__main__':
    cases = [(3, 4, old.cycle(3)), (4, 3, old.cycle(4)), (4, 5, old.cycle(4)),
             (3, 4, tuple(range(3))), (4, 4, tuple(range(4))), (4, 6, tuple(range(4)))]
    result = dict(metadata=dict(commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
        python=platform.python_version(), dependencies='standard library only',
        random_seeds='none: exact deterministic enumeration',
        command='python3 -B experiments/20261015-122824-support-marginal-audit/check.py',
        imported_sources={str(p.relative_to(HERE.parents[1])):hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in (SOURCE, old.CORE)}),
        cases=[audit(*case) for case in cases], explicit_star=explicit_star(),
        slow_projection=slow_projection_counterexample(F(1, 1024)))
    (HERE/'results.jsonl').write_text(json.dumps(result,sort_keys=True)+'\n')
    print(json.dumps(dict(cases=[{k:r[k] for k in ('N','m','states','support_graphs','nonlumpable_fibers','witness')}
                                for r in result['cases']], explicit_star=result['explicit_star']),indent=2))
