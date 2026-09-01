# M277 fresh immutable referee report for M274

Date: 2026-08-14 UTC.

## Verdict

```text
ACCEPT WITH NONMATERIAL CORRECTIONS.
```

M274's mathematical claims are correct at their stated logical strengths.
The PCS--MS equivalence, complete per-lag and channel formulas, finite
MON/FOSD refutations, and arbitrary-odd-rank raw-atom counterfamily survive
independent reconstruction.  CP, OS+, MS, and FCL1 remain open.  There is no
gap, mixing, or Terminal implication.

There are no fatal or major objections.  Two nonmaterial corrections and one
scope firewall must accompany acceptance:

1. The M274 small-rank checker has a transitive NumPy dependency, contrary to
   its `nonstandard_dependencies: null` metadata.
2. The exact `k=9` minimum is attained at both reflected lags `y=7` and
   `y=18`; naming only `y=7` is not uniqueness.
3. Scope firewall: the all-rank atom obstruction refutes positivity of the displayed literal
   raw ordered-atom decomposition.  It does not logically rule out every
   alternative regrouping or positive representation.

None changes an exact coefficient, counterexample, implication, or open
status.

## 1. Scope and source gate

The audited target is the first separated fixed cell of the auxiliary
uniform minimal-factorization law for the long cycle under the nonlazy cyclic
rank-two quotient kernel.  It is not the global identity-word law or the
lazy exact `{3,4,5}` heat-bath sampler.

The supplied M274 ledger digest is exactly

```text
c3bdadca0f95679fed1fbcf461e60cf01bc4d669cc087e90792c29ec4d4a6e4e.
```

All ten M274 payloads pass.  All payloads in M91/M94/M100, M161/M166,
M168/M171, M174/M178, M261/M264, M266/M268, and M267/M270 pass their
inventories.  Exact ledger digests are in `dependency_ledger.md`.

## 2. Exact PCS--MS equivalence

For `P=sum_y(z_y)_+` and `N=sum_y(-z_y)_+`, direct algebra gives

```text
sum_y |k z_y|
 = k(P+N)
 = k|P-N|+2k min(P,N)
 = k|sum_y z_y|+2k min(P,N).
```

Accepted M266/M268 proves PCS, namely `k|sum_y z_y|=O(1)`.  Therefore FCL1
is equivalent to `k min(P,N)=O(1)` in the presence of PCS.  M274 states both
directions correctly and does not infer FCL1 from PCS alone.  OS+ is a
strictly stronger sufficient statement because it sets `N=0`.

## 3. Raw law, normalization, reflection, and phase caveat

Independent substitution into the quotient kernel gives, for odd `k>=3`,
`n=3k`, and `1<=y<=n-3`,

```text
z_k(y)=n^(n-2)/(nF_T) [
  sum_(s in X_T)3 d_k(s)W_(k,y)(s)/A_s
 +sum_(s in X_D)2 d_k(s)W_(k,y)(s)/A_s],

d_k(s)=C_B(s)/A_B-C_A(s)/A_A,
pi_y=2nF_T/n^(n-2).
```

The factors three and two are the literal intermediate triangle/double
lifts.  The target double lift two is present in
`g=2W/(A_s pi_y)`.  The `IS`, `IN`, and `X` target topologies, every cyclic
phase, both intermediate kinds, and both source channels are retained before
any sign or absolute value.

The lags are exactly `ell=y+1 in {2,...,n-2}`.  Both endpoints remain, and

```text
z_k(y)=z_k(n-2-y).
```

Since `n-2` is odd, there is no fixed colored lag; each physical orbit has
two colored appearances.  M274's reflection and endpoint accounting is
correct.

The per-lag affine split

```text
z_k(ell-1)=Lambda_n e^-2/[(n-3)(n-4)]
 [2eta(T)+eta(I_ell)+eta(Q_ell)]
```

has `eta(T)>0`, but the combined signed remainder has no proved lower bound.
Likewise the positive phase-total term `2n eta(T)` remains separate from
`eta(B_k)`.  M274 correctly refuses to infer atomwise or lagwise positivity
from either baseline.

## 4. Literal channel formulas and CP

The normalized channel identity is exactly

```text
z_k(y)=alpha_1 CP_1(k,y)+alpha_2 CP_2(k,y),
CP_j=(H_(j,B)-H_(j,A))(s -> 2W_(k,y)(s)/(A_s pi_y)).
```

Channel one is the full merged exterior first-edge law versus the fair
mixture of the two separate exterior laws, tensored with the common middle
law.  Channel two is the full ordered first-two-factor law on the merged
cycle versus that on the two-cycle residual.  The latter normalized law
already includes the fair first-component choice; M274 correctly inserts no
additional factor `1/2`.

Thus pointwise `CP_1,CP_2>=0` would imply OS+.  This CP statement permits all
split, gradient/embedding, kind, topology, and phase cancellations within
each channel.  It is weaker than MON/FOSD but stronger than the needed
cross-channel inequality.  In that precise sense it is the first plausible
repaired stronger lemma.  CP is not itself a cross-channel recombination:
the cross-channel scalar is `alpha_1 CP_1+alpha_2 CP_2`.

## 5. Exact finite audit

M274's monotonicity checker reruns byte-for-byte.  The independent
standard-library checker reconstructs the quotient and conditional laws
without importing project code and matches every exact score and all four
blocks in all 18 rows:

```text
k=3: MON 4 = 0 adjacent + 4 embedding; FOSD 36,
k=5: MON 46 = 32 adjacent + 14 embedding; FOSD 250.
```

It reproduces

```text
R_(3,2)(Phi_(1,1))-R_(3,2)(Psi_(1,1))
 = -876877452441/14123762450000
```

and the channel-one `k=3,y=1` upper-tail deficit `-32/375` at threshold
`343359/268912`.  Hence MON and response FOSD are genuinely refuted.  Both
channel means are strictly positive at all 36 tested channel-lag pairs, but
that is finite evidence only.

A fresh frozen-M161 `k=9` run reproduces every mathematical JSON field.
All 24 exact scores are strictly positive, reflection and endpoint equality
hold, and every score equals the sum of its six kind/topology pieces.  The
minimum score is approximately `0.005999872316550588` at both `y=7,18`; its
triangle contribution is approximately `0.010948178900420163`, while its
double contribution is approximately `-0.004948306583869576`.

## 6. Arbitrary-rank raw-atom obstruction

The residual components are

```text
C_-=(0,...,k-1),  M=(k,...,2k-1),
C_+=(2k,...,3k-1),
L=(1,...,k-1,2k,...,3k-1).
```

The chord `e_+=(1,2k)` belongs only to the merged exterior cycle, whereas
`e_-=(0,1)` belongs to `C_-` and not `L`.  Pairing either with
`f_M=(k,k+1)` gives positive and negative channel-one raw atoms.  After the
corresponding first cut, `f=(1,2)` lies in a remaining `(k-1)`-cycle in both
cases, so the positive and negative ordered channel-two atoms have positive
completion weights.  This works symbolically for every odd `k>=3`, not by
finite extrapolation.

The conclusion is exactly sign-indefiniteness of the displayed literal raw
atom sums.  Cancellation after grouping is still possible and is exactly
why CP remains open.

## 7. Objections and final status ledger

```text
fatal objections: none
major objections: none

minor O1: frozen nonstandard-dependency metadata omits transitive NumPy 1.26.4
minor O2: k=9 minimum has the reflected tie y=7,18
scope O3: read “no atomwise-positive factorization” as the literal raw
          ordered-atom factorization actually exhibited
```

```text
PCS                                      proved input
PCS + MS <=> FCL1                        proved exact equivalence
raw/channel/topology/reflection formulas proved exact
MON                                      refuted exact
response FOSD                            refuted exact
literal raw atomwise positivity          refuted exact for every odd k>=3
k=9 OS+ and k=3,5 channel positivity     exact finite only
CP, OS+, MS, FCL1                        unresolved
later cells, direct L1/H0                unresolved and out of scope
gap, mixing, Terminal                    no inference
```

Final action: accept M274's mathematical core with the two corrections and
raw-atom scope firewall above, and retain CP as an open,
per-channel-recombined sufficient lemma.
