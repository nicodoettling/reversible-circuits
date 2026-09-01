# M131 final report: suffix excess five

Date: 2026-08-13 UTC.

## Field 1 — decision and claim status

Verdict: **PROMOTE A CONDITIONAL STRICT REDUCTION**, not a universal `L=5`
theorem.

**PROVED, relative to the accepted M109/M114, M115/M116, and M117/M121
inputs:** for every `6<=s<=99` and `K>=1`, the complete unweighted
right-heavy auxiliary resolvent satisfies

```text
H(s,K,K-1,s-5)<=q(1-q),
q=w_6 w_(s-5)/w_(s+1).
```

**CONDITIONAL:** the same result for every `s>=100` follows from the single
standalone scalar lemma `C_s<=3/4` defined in Field 5.

**REFUTED AS A PROOF TEMPLATE ONLY:** the inherited coarse
`beta_E<=degree(E)` `L=5` envelope exceeds the target at an exact test point.
The actual resolvent remains below the target there, so this is not an `H`
counterexample.

**UNRESOLVED:** the universal scalar lemma, hence the unconditional all-`s`
`L=5` conclusion. No auxiliary gap, ROOT-MEAN LIFT, original-chain gap,
polynomial mixing statement, or project terminal follows.

## Field 2 — target, normalization, and convention

This mission concerns only the auxiliary full nonlazy stationary-flow
parking-degree projection in the minimal-long-cycle sector. Put

```text
w_n=n^(n-1)/n!,
x=(s,K,K-1,B),  B=s-5,  s>=6, K>=1,
H=(I-Q)^(-1)A_0.
```

The accepted finite-DAG recurrence is

```text
H=A_0+QH,
Q(x,y)=rho_s(k,t)nu_(K,R,k)(j),  j=1,...,k.
```

Only `j=0` and targets of auxiliary rank below two are killed. Every root
mass, current, and capacity is first normalized by `q`; the final envelope is
`H/q<=E_5`, so proving `E_5<=1-q` gives the displayed target without changing
the initial normalization. Permutations compose as `(pq)(x)=p(q(x))`, with
factors read left-to-right.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| M131 complete unweighted `L=5` auxiliary resolvent | `H<=q(1-q)` for all right-heavy contexts | N/A: no word sampler is generated | N/A: this is a projection recurrence | literal basins, every `j`, exact resolvents, rational Bernstein certificates | proved for `6<=s<=99`; conditional for `s>=100` |

## Field 3 — exact root structure and smallest boundary

For `h=0,...,5`, every supported root is `(P,B+h)`, where `P` is an ordered
composition of `5-h`. Thus there are exactly

```text
sum_(h=0)^4 2^(4-h)+1=32
```

supported rows. Their normalized mass-times-contextual-mean sum is exactly
one. First-merge cuts produce 31 nominal exceptional endpoint occurrences;
23 are active and the eight endpoints beginning `(1,1)` are inactive. The
refined envelope retains those eight only in conservative upper-bound
bookkeeping.

There are 16 positive `(k,t)` root groups and exactly 11 live deep groups:

```text
h=1: k=2,3,4,5
h=2: k=2,3,4
h=3: k=2,3
h=4: k=2
h=5: k=1.
```

Every attachment `j=1,...,k` is retained before aggregation. A child has
suffix excess `h-1` and deficit `D'=k+1-j`; hence `j=k` uses the accepted
right-heavy `L<=4` theorem, while all other live children need at most the
arbitrary-deficit `L=3` envelope in Field 4.

At the smallest boundary `s=6`, `B=1`. All nominal `t=2` children have local
rank one and are inactive; their bottom ratio is `b_1=1`, so the corresponding
terminal charge vanishes. The literal recurrence retains exactly 17 children:

```text
(k,t,j)=(1,6,1);
(2,t,j), t=3,4,5, j=1,2;
(3,t,j), t=3,4, j=1,2,3;
(4,3,j), j=1,2,3,4.
```

Literal full-basin reconstruction at `(s,K)=(6,1),(6,5),(7,1),(7,5)` agrees
exactly with grouped reset energy. The literal full-state basin counts are 23
at `s=6` and 47 at `s=7`; every one of the 23 active supported exceptional
currents and capacities matches exactly.

## Field 4 — arbitrary-deficit `L=3` child envelope

For a reachable context with excess `ell<=3`, `K+1=(1+az)/z`, and deficit
`D=K-R`, the exact attachment probabilities are implemented in their full
`(a,D,k,j,z)` form. The support and first-prefix basin recurrence are rebuilt
for each `ell`. A retained child has

```text
(a',D',ell')=(a+k,D+k-j,h-1).
```

Induction on the finite auxiliary DAG now gives a structural envelope: use
the exact exceptional reset currents, the valid ordinary-basin upper terms,
and the already accepted lower-excess child envelopes rank by rank. The first
new level has eight supported rows, seven nominal exceptional basins, and four
live groups. No child below it has excess above two.

The same generic implementation reproduces the accepted arbitrary-deficit
`L=1` and `L=2` formulas exactly. Independent finite falsification over

```text
ell=1,2,3; ell+1<=S<=8; 2<=K<=8; 1<=R<K
```

finds zero envelope failures. These finite rows audit the implementation; the
recursive upper bound itself follows from the exact reset decomposition and
the accepted predecessor theorems.

## Field 5 — exact Cayley coefficient and first open lemma

For a canonical endpoint with first total `A` and degree `k`, set
`lambda(A,k)=beta(A,k)/k`. Exact Cayley convolution gives

```text
lambda(A,k)
 =(k-1)! sum_(p=1)^A [p/(p+k-1)!]*(A)_p/A^p,
lambda(A,2)=A/(A+1).
```

Termwise comparison with the `k=2` coefficient is rigorous because

```text
(k-1)!(p+1)!/(p+k-1)! <=2/k,  k>=2,p>=1.
```

Therefore

```text
lambda(A,k)<=2A/[k(A+1)].
```

This is the only universal lambda shortcut retained. The all-endpoint
canonical-basin coefficient is

```text
C_s=sum_(all canonical E) degree(E)rho(E)lambda(E)^2

   =sum_(k=2)^s sum_(A=1)^(s-k+1)
      [w_A c(s-A,k-1)/(k!w_(s+1))] k lambda(A,k)^2,
```

where `c(n,p)=p n^(n-p-1)/(n-p)!`. Inactive endpoints are deliberately
included, which can only enlarge the envelope. The exact endpoint-degree
marginal is

```text
sum_A w_A c(s-A,k-1)/(k!w_(s+1))
 =binom(s-1,k-1)s^(s-k)/(s+1)^(s-1).
```

The first unproved step is precisely:

> **Scalar lemma C.** For every `s>=100`, `C_s<=3/4`.

Exact finite values include `C_100=.7145417887...`; the JSON stores the exact
rational. No monotonicity or asymptotic tail assertion is made. The tempting
`2(3-e)<9/16` bound is false; an exact factorial-tail bound gives
`e<87/32` and hence the reverse strict inequality. The repaired statement

```text
2(3-e)<17/30
```

is true because `e>sum_(n=0)^5 1/n!=163/60`. It does not aggregate to a proof
of lemma C, so the universal conclusion remains conditional.

## Field 6 — refined envelope and retained negative result

For an ordinary basin `B_E`, its current is `-q rho(B_E)`. Its normalized
energy contribution equals

```text
q degree(E)rho(E)lambda(E)^2.
```

Summing `C_s`, subtracting the ordinary terms for all 31 supported exceptional
occurrences, and adding their exact current-squared-over-capacity terms gives
the refined reset envelope `R_5`. Adding every retained child contribution
from the 11 live groups gives

```text
H/q <= E_5=R_5+D_5.
```

At `(s,K)=(7,4096)`, the inherited coarse envelope has normalized value
approximately `1.0194850323`, while the actual exact resolvent ratio is
approximately `.4025103000`. Both comparisons are stored as exact rational
inequalities. This permanently refutes only the coarse certificate route;
it neither refutes the contraction nor supplies asymptotic evidence.

## Field 7 — universal rational certificates

Let `z=1/(K+1)` and

```text
T_s(z)=prod_(a=1)^5(1+az)^2 [1-q-E_5(z)].
```

For every integer `s=6,...,99`, the exact degree-12 Bernstein expansion on
`z in [0,1/2]` has all 13 coefficients positive. Across all 1222 coefficients,
the exact minimum is

```text
5307578203959502651/4736091661711441920000 >0
```

at `s=7`. This proves the unconditional finite-rank range for every `K>=1`,
not merely the sampled `K` values.

For `s>=100`, the six Cayley ratios are in `[4/11,187/500]`. The lower
endpoint is exact: `b_n>1/e` and the geometric factorial-tail estimate gives
`e<11/4`. The ratios decrease, their smallest index is at least 95, and the
upper endpoint follows from the exact integer inequality

```text
500*95^94 <187*96^94.
```

Under scalar lemma C, replacing `C_s` by `3/4` and every path height by one
only enlarges the envelope. The resulting polynomial has multidegree
`(1,1,2,2,2,2,12)`. All 4212 tensor Bernstein coefficients on the ratio box
times `[0,1/2]` are positive, with exact minimum

```text
4360847276079323/50118750000000000000 >0
```

at index `(1,1,2,2,2,0,0)`. An exact off-grid interpolation identity also
passes. This is a universal box certificate once, and only once, lemma C is
supplied.

## Field 8 — reproducibility and dependency audit

Run from this mission directory:

```text
python3 -B l5_exact.py --s-max 12 --certify --output l5_exact.json
```

The run uses Python `3.12.3`, standard-library `fractions.Fraction`, no
nonstandard dependencies, deterministic arithmetic, and `seed=null`. It
reports zero failures, zero nonpositive finite coefficients, and zero
nonpositive conditional-tail coefficients. Exact sampled resolvents cover
`6<=s<=12` and `K in {1,2,5,64,4096}`; the maximum sampled actual ratio is
about `.6719555`, and the maximum refined-envelope ratio about `.9986162`.
These two maxima are diagnostics only.

The frozen checksum inventories for M109, M114, M115, M116, M117, M121,
M123, and M128 all pass independently. The first six supply the accepted
recurrence and `L<=4` contraction inputs. M123/M128 instead record why the
generic unrestricted, centered, and bounded-event basin-frame/Bessel routes
cannot be reused; this proof does not use them. Exact dependency hashes are
recorded in `freeze_manifest.md`.

## Field 9 — limitations, action, and hygiene

The strongest correct scoped result is:

> `L=5` is proved for `6<=s<=99` and reduced for `s>=100` to the standalone
> exact Cayley-coefficient lemma `C_s<=3/4`.

The next action is a proof or counterexample for that scalar lemma alone. A
finite scan, an unproved monotonicity assertion, or either discarded `e`
shortcut must not be promoted. The inherited coarse envelope obstruction is
retained as a proof-template counterexample, not mislabeled as an `H`
counterexample.

No generic basin-frame/Bessel estimate, raw one-step defect sign, or two-layer
sign argument is used. No claim is made about a weighted contraction beyond
the accepted positive-history implication from this auxiliary `H`, and no
gap or Terminal inference is made. No predecessor, coordinator, manuscript,
project-skill, or other worker file was edited. No package was installed and
no stochastic conclusion appears.
