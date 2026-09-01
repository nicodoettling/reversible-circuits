# M145 final report: suffix excess six

Date: 2026-08-13 UTC.

## Field 1 — verdict and claim status

```text
FINAL VERDICT: PROMOTE TO FRESH REFEREE.
CLAIM STATUS: PROVED IN M145 RELATIVE TO ACCEPTED INPUTS; NOT YET
INDEPENDENTLY ACCEPTED.
```

M145 proves the auxiliary right-heavy full-excursion inequality

```text
H(s,K,K-1,s-6)<q(1-q),
q=w_7 w_(s-6)/w_(s+1), s>=7, K>=1.
```

The proof uses a new recursive full-basin refined-reset envelope.  Positive
histories give `G<=H`; the seed is right-heavy, so `U=q(1-q)`.

## Field 2 — target, normalization, and convention

The project target remains uniform on fixed-length identity words in
`Omega(N,m)`.  Permutations compose as `(pq)(x)=p(q(x))`, with factors
displayed left-to-right.  The proved claim concerns only the full nonlazy
stationary-flow parking-degree projection in the minimal-long-cycle sector.
It proves no auxiliary gap, ROOT-MEAN LIFT, original-chain gap, polynomial
mixing result, Terminal A, or Terminal B.

## Field 3 — exact support, basins, and all attachment ranks

At suffix excess six, the exact contextual support has 64 rows.  There are
63 exceptional canonical basins, 22 positive `(k,t)` groups, 16 live groups,
and 51 nominal positive ranks.  At the minimum boundary `s=7`, all 20 ranks
with `t=2` have rank-one children, leaving exactly 31.  Every `j=1,...,k` is
represented before that boundary is imposed.  A live `(h,k,j)` child has

```text
suffix excess h-1, offset a+k, deficit D+k-j.
```

The normalized support masses and means sum exactly to one.

## Field 4 — corrected full-basin reset invariant

For endpoint `E`, let

```text
c_E=degree(E)rho(E), b_E=rho(B_E)=c_E lambda_E.
```

Adding inactive edges harmlessly, the reset satisfies

```text
A_0<=q^2[C_S-sum_exceptional b_E lambda_E]
     +sum_exceptional theta_E^2/c_E.
```

This subtracts one `lambda_E` from full basin mass `b_E`.  It is not M131's
rejected `a_E lambda_E^2`.  Propagating this same refined reset through every
child produces an all-deficit recurrence and cancels every quadratic Cayley-
ratio term, making the envelope multiaffine in all consecutive ratios.

## Field 5 — retained obstruction and uniform repair

The simpler induction that charges each right-heavy child its whole
`q_child(1-q_child)` budget is refuted as a proof template.  At
`s=7,K=128`, its exact normalized value is `1.0003190402...>1`, while the
actual finite-DAG ratio is `0.6265122819...<1`.  This is not an `H`
counterexample.

The successful repair recursively uses the refined envelope even for
right-heavy children.  This supplies a genuine uniform-in-suffix-excess
recurrence/invariant, although M145 certifies its sign only at `L=6`.

## Field 6 — complete universal certificate

With `Delta_6=product_(a=1)^6(1+az)`, the cleared slack has multidegree

```text
(1,1,1,1,1,1,1,14)
```

in seven Cayley ratios and `z`.

For `s=7,...,104`, all 1,470 exact degree-14 Bernstein coefficients are
positive.  The minimum is approximately `0.08438881398289777` at `s=104`,
index zero.  The coefficient digest is

```text
12bcb36c2409ede2ae36d8157a10671246c498043e0f6c6a8dc9f081018edde0.
```

For `s>=105`, all active scalar coefficients have index at least 100, so
accepted M140/M144 supplies `C_S<3/4`.  All seven ratios lie in
`[4/11,187/500]`.  Every one of the 1,920 tensor Bernstein coefficients is
positive.  The exact minimum is

```text
11435975715855226131133337/149750370000000000000000000
```

at `(1,1,1,1,1,1,0,0)`.  Its decimal value is
`0.07636692794719123`; the coefficient digest is

```text
b2aafe3c93fc583b7ae7dc32fadaf3a46de97dac0fe8ba46f8ace2a6815dec1d.
```

## Field 7 — literal and arbitrary-deficit audits

Literal ordered-composition basins and independently grouped Cayley-forest
resets/resolvents agree on all six selected roots

```text
s in {7,8}, K in {1,2,5}.
```

All satisfy `exact H <= refined envelope < target`.  The minimum boundary has
exactly 31 retained children.

All 270 arbitrary-deficit audits through `L=4` pass:

```text
L=1,...,4; L+1<=S<=7; K=2,...,6; 1<=R<K.
```

The tightest exact/envelope ratio is `761/763` at `(3,4,2,1)`.

## Field 8 — reproducibility and dependencies

Primary command:

```text
python3 -B l6_exact.py --phase full --output l6_exact.json
```

The checker uses Python 3.12.3 standard-library `Fraction` arithmetic,
`seed=null`, imports no predecessor source or output, constructs literal and
grouped recurrences separately, checks the rejected budget envelope, derives
finite and tensor Bernstein coefficients, and verifies independent off-grid
identities.

Accepted logical inputs are:

- M109/M114: all-rank finite-DAG recurrence, all-deficit terminal theorem,
  and positive-history `G<=H`;
- M140/M144: the proved scalar bound `C_S<3/4` for every `S>=100`.

M115/M116 and M117/M121 supply accepted lower-boundary comparisons used in
reconciliation and diagnostics, but the recursive proof does not collapse
descendants to their contraction statements.

## Field 9 — limitations, action, and hygiene

The result ends at auxiliary suffix excess six.  It does not establish the
sign of the refined recurrence at `L>=7`, an all-`L` contraction, any gap, or
mixing.  The most valuable next action is a fresh independent referee focused
on (i) the full-basin subtraction normalization, (ii) multiaffinity, (iii)
the `s=105` scalar-index cutoff, and (iv) exact regeneration of both
certificate families.

Only the owned M145 directory was changed.  No packages were installed, no
configuration changed, and no commit or push was attempted.  The default
workspace sandbox failed during `bwrap` loopback setup; scoped approved
escalated commands were used inside the owned directory.

