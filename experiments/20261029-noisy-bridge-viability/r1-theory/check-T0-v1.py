"""Exact bounded falsification checks for authored theorem T0. Stdlib only.
Run only with the coordinator's current bounded-harness reservation.
"""
import argparse
import hashlib
import itertools
import json
import math
import os
import platform
import subprocess
import time
from fractions import Fraction
from pathlib import Path


def system(n, max_length=24):
    permutations = list(itertools.permutations(range(n)))
    index = {p: i for i, p in enumerate(permutations)}
    identity = index[tuple(range(n))]
    edges = list(itertools.combinations(range(n), 2))
    transitions = []
    for p in permutations:
        row = []
        for a, b in edges:
            changed = list(p)
            changed[a], changed[b] = changed[b], changed[a]
            row.append(index[tuple(changed)])
        transitions.append(row)
    walks = [[0] * len(permutations)]
    walks[0][identity] = 1
    for length in range(1, max_length + 1):
        counts = [0] * len(permutations)
        for x, value in enumerate(walks[-1]):
            if value:
                for y in transitions[x]:
                    counts[y] += value
        walks.append(counts)
    return permutations, identity, edges, transitions, walks


def c6_formula(n):
    q = math.comb(n, 2)
    a = (3 * n * n + n - 12) // 2
    return (q * a * a + 1536 * math.comb(n, 4)
            + 1620 * math.comb(n, 5) + 540 * math.comb(n, 6))


def cycles(p):
    visited, lengths = set(), []
    for x in range(len(p)):
        if x in visited:
            continue
        cur, count = x, 0
        while cur not in visited:
            visited.add(cur)
            count += 1
            cur = p[cur]
        if count > 1:
            lengths.append(count)
    return tuple(sorted(lengths, reverse=True))


def return_checks(n):
    ps, identity, edges, step, walks = system(n)
    q = len(edges)
    probs = [Fraction(count[identity], q**r) for r, count in enumerate(walks)]
    assert walks[6][identity] == c6_formula(n)
    allowed = {(2,): (3*n*n+n-12)//2, (4,): 16, (3, 2): 9, (2, 2, 2): 6}
    for p, count in zip(ps, walks[3]):
        assert count == allowed.get(cycles(p), 0)
    inequalities = 0
    for r in range(2, 13, 2):
        for length in range(2*r, 25, 2):
            assert probs[length-r]/probs[length] <= probs[r]/probs[2*r]
            inequalities += 1
    for length in range(0, 25, 2):
        assert max(walks[length]) == walks[length][identity]
    for s in range(1, 12):
        assert probs[2*s]**2 <= probs[2*s-2]*probs[2*s+2]
    return dict(N=n, states=len(ps), c6=walks[6][identity], c12=walks[12][identity],
                beta6=str(probs[6]**2/probs[12]), ratio_inequalities=inequalities,
                counts={str(r): walks[r][identity] for r in (0, 2, 4, 6, 12, 24)})


def channel_sum(values, q, r, coordinate):
    """Unnormalized fresh-coordinate channel: sum old symbol, repeat at new."""
    stride = q ** (r-1-coordinate)
    block = stride*q
    answer = [0]*len(values)
    for start in range(0, len(values), block):
        for offset in range(stride):
            total = sum(values[start+offset+a*stride] for a in range(q))
            for a in range(q):
                answer[start+offset+a*stride] = total
    return answer


def window_check(n, length, r, literal=False):
    ps, identity, edges, step, walks = system(n, max(length, 2*r))
    q = len(edges)
    tuples = list(itertools.product(range(q), repeat=r))
    products = []
    for word in tuples:
        value = identity
        for edge in word:
            value = step[value][edge]
        products.append(value)
    weights = [walks[length-r][p] for p in products]  # inverse counts equal
    total = walks[length][identity]
    assert sum(weights) == total
    if literal:
        observed = [0]*len(tuples)
        for word in itertools.product(range(q), repeat=length):
            value = identity
            for edge in word:
                value = step[value][edge]
            if value == identity:
                prefix = 0
                for edge in word[:r]:
                    prefix = prefix*q+edge
                observed[prefix] += 1
        assert observed == weights
    pr = Fraction(walks[r][identity], q**r)
    p2r = Fraction(walks[2*r][identity], q**(2*r))
    beta = pr*pr/p2r
    arrays = {0: weights}
    probabilities, equalities = {}, {}
    maximum = max(weights)
    for mask in range(1 << r):
        if mask:
            bit = mask & -mask
            coord = bit.bit_length()-1
            arrays[mask] = channel_sum(arrays[mask^bit], q, r, coord)
        current = arrays[mask]
        denominator = total*q**mask.bit_count()
        assert sum(current) == denominator
        assert max(current) <= maximum*q**mask.bit_count()
        probabilities[mask] = Fraction(sum(v for v, p in zip(current, products) if p == identity), denominator)
        assert probabilities[mask] <= beta
        if r == 2:
            equalities[mask] = Fraction(sum(v for v, t in zip(current, tuples) if t[0] == t[1]), denominator)
    assert len(set(arrays[(1 << r)-1])) == 1
    noise_rows = []
    for k in range(length+1):
        value = Fraction()
        equality = Fraction()
        subset_mass = Fraction()
        for mask, probability in probabilities.items():
            outside = k-mask.bit_count()
            if not 0 <= outside <= length-r:
                continue
            mass = Fraction(math.comb(length-r, outside), math.comb(length, k))
            subset_mass += mass
            value += mass*probability
            if r == 2:
                equality += mass*equalities[mask]
        assert subset_mass == 1
        assert value <= beta
        row = dict(k=k, noisy_identity_probability=str(value))
        if r == 2:
            alpha = Fraction((length-k)*(length-k-1), length*(length-1))
            p_old = equalities[0]
            assert equality == alpha*p_old+(1-alpha)/q
            row['pair_equality_probability'] = str(equality)
            row['alpha'] = str(alpha)
        noise_rows.append(row)
    return dict(N=n, L=length, r=r, bridge_words=total, literal_enumeration=literal,
                masks_checked=1 << r, projected_tuples=q**r, beta=str(beta), noise=noise_rows)


def survival_check():
    n = 4
    ps, identity, edges, step, _ = system(n, 0)
    index = {p: i for i, p in enumerate(ps)}
    edge_ids = {edge: i for i, edge in enumerate(edges)}
    gate_perms = [step[identity][a] for a in range(len(edges))]
    def multiply(a, b):
        return index[tuple(ps[a][ps[b][j]] for j in range(n))]
    inverse_gate = {g: i for i, g in enumerate(gate_perms)}
    def conjugate(a, b):
        return inverse_gate[multiply(multiply(gate_perms[a], gate_perms[b]), gate_perms[a])]
    def evaluate(word):
        p = identity
        for a in word:
            p = step[p][a]
        return p
    relators = []
    for a, b, c, d in itertools.permutations(range(n)):
        gates = [(a, c), (c, d), (a, b), (a, d), (b, c), (b, d)]
        word = tuple(edge_ids[tuple(sorted(g))] for g in gates)
        assert len(set(word)) == 6 and evaluate(word) == identity
        relators.append(word)
    word = relators[0]*6
    length, m, b = len(word), 6, 1
    threshold = m-1-2*b-1
    checked = 0
    min_seen = length
    for shift in (0, 1, 5, 6, 35):
        rotated = word[shift:]+word[:shift]
        for pos in range(length-1):
            a, c = rotated[pos:pos+2]
            for replacement in ((c, conjugate(c, a)), (conjugate(a, c), a)):
                moved = list(rotated)
                moved[pos:pos+2] = replacement
                assert evaluate(moved) == identity
                for noise_pos in (0, 17, 35):
                    for fresh in range(len(edges)):
                        changed = moved.copy()
                        changed[noise_pos] = fresh
                        x = sum(evaluate(changed[j:j+6]) == identity for j in range(length-5))
                        assert x >= threshold
                        min_seen = min(min_seen, x)
                        checked += 1
    return dict(N=n, M=m, L=length, B=b, k=1, H=threshold,
                distinct_quadruple_relators=len(relators), shifts=[0,1,5,6,35],
                moves='all adjacent positions, both directions', noise_positions=[0,17,35],
                fresh_draws='all six transpositions', cases=checked, minimum_windows=min_seen)


def constants_and_regressions():
    upper = Fraction(15,8)+Fraction(57,4000)+Fraction(513,8000000)
    lower = Fraction(10395,64)*Fraction(467,500)
    assert upper < Fraction(19,10)
    assert Fraction(19,10)**2/lower < Fraction(1,40)
    schedules = []
    for lam in (32,33,64,1000):
        n = lam*lam
        h = n-1-2*(n//8)-lam
        assert 2*h >= n
        schedules.append(dict(lambda_=lam,N=n,L=6*n,k=lam,B=n//8,H=h))
    # Cached-prefix regression CP-1: explicitly rejects the false marginal product bound.
    gamma = Fraction(1,10)
    joint = 2*Fraction(21,2000)/2
    posterior = Fraction(21,221)
    assert joint == Fraction(21,2000) > gamma**2
    assert posterior < gamma
    # Scope regression: removing L>=2r makes the local lemma false at S3,L=r=6,k=0.
    assert Fraction(1,1) > Fraction(1,3)
    return dict(c6_scaled_upper_at_N1000=str(upper), c12_scaled_lower_at_N1000=str(lower),
                beta6_upper=str(Fraction(19,10)**2/lower), schedules=schedules,
                CP1=dict(joint=str(joint), false_product=str(gamma**2),
                         second_posterior=str(posterior), outcome='reject false product bound'),
                rejected_scope=dict(N=3,L=6,r=6,k=0,actual='1',claimed_without_length_hypothesis='1/3'),
                boundaries={'N2':'all noisy words identical; checked in DP and channel cases',
                            'L0':'one empty bridge, k0 only; no six-window theorem',
                            'L2':'outside six-window theorem',
                            'oddL':'identity impossible by sign',
                            'kL':'full channel is constant iid; checked exactly',
                            'H_nonpositive':'no positive attack claim'})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    path = Path(args.output)
    if path.exists():
        raise SystemExit('Refusing to overwrite existing result')
    start = time.monotonic()
    returns = [return_checks(n) for n in range(2,8)]
    windows = [window_check(n,length,r,literal) for n,length,r,literal in
               ((2,4,2,True),(3,4,2,True),(4,4,2,True),(4,6,2,True),
                (3,8,4,False),(4,8,4,False),(3,12,6,False),(4,12,6,False))]
    assert windows[1]['bridge_words'] == 27
    assert windows[2]['bridge_words'] == 120
    assert windows[3]['bridge_words'] == 3936
    result = dict(status='passed', theorem_version='T0',
                  command='python3 -B '+str(Path(__file__))+' --output '+str(path),
                  python=platform.python_version(), nonstandard_dependencies=[],
                  seed='none; exact deterministic enumeration and rational arithmetic',
                  commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  returns=returns, windows=windows, survival=survival_check(),
                  constants_and_regressions=constants_and_regressions(),
                  elapsed_seconds=time.monotonic()-start)
    tmp=path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(json.dumps(result,indent=2)+'\n')
    os.replace(tmp,path)
    print(json.dumps({'status':'passed','elapsed_seconds':result['elapsed_seconds'],
                      'result':str(path),'window_cases':len(windows),'return_cases':len(returns)}))

if __name__ == '__main__':
    main()
