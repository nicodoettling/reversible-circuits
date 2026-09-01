# M118 fresh referee report on frozen M113

Date: 2026-08-12 UTC.  Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Decision and exact scope

```text
ACCEPT M113's exact handle-projection reduction, qualitative incidence
connectivity, Higgs-lift identification, Lorentzian refutation, and balanced
edge-family arithmetic.
Material numbered objections: none.
```

M113 correctly reduces M104's exact handle-cell projection gap to the gap of
an explicit reversible local connected-unicycle incidence chain:

```text
beta(d) >= gap(A_d)/(2d-1)^3.
```

It also correctly leaves `gap(A_d)>=d^{-O(1)}` unresolved.  This acceptance
proves no polynomial value for `beta(d)` or `gamma_1(d)`, no worst-source
marked hitting estimate, no full lazy `{3,4,5}` same-product heat-bath gap or
mixing result, and neither Terminal A nor Terminal B.  The finite `d<=4`
spectra below are exact finite facts followed by numerical diagonalization;
they are not asymptotic evidence.

## 2. Frozen provenance and integrity

The two assigned M113 hashes independently match:

| frozen artifact | required and observed SHA-256 |
|---|---|
| `report.md` | `295c6d50b70117915cc99d9ebe6e1e88cbfab258a404db66a0b1543ea01cfe47` |
| `freeze_manifest.md` | `64cf3bb48baca3022690cb72c5afc458e3fbf8e514b56612c099b7f9b1e0b6bf` |

The observed hash of M113's `SHA256SUMS` is
`45656b8e6e388dc5dc3210c92f45b4741b400108595fa235dbf86e5ae8309d19`.
Running `sha256sum -c SHA256SUMS` in the frozen M113 directory returned `OK`
for all thirteen payload entries.  Every upstream M97/M101/M104/M110 digest
listed in M113's manifest was independently recomputed and matches exactly.
No predecessor, coordinator, manuscript, project-skill, or shared durable
file was edited.

## 3. Target, convention, kernel, and boundary

The audited auxiliary target is

```text
X_d={w=(t_1,...,t_(2d)): eval(w)=id, support(w) connected},
pi_d=Unif(X_d),                                             d>=2.
```

Permutations compose as `(pq)(x)=p(q(x))`, and factors multiply
left-to-right.  With `D=2d-1`, the base signed adjacent-Hurwitz walk is

```text
P_d=I/2+[1/(4D)]sum_i(R_i+R_i^(-1)),
R_i(a,b)=(b,bab),             R_i^(-1)(a,b)=(aba,a).
```

The accepted M97/M101 lift is

```text
A_lift={(w,j):j in J(w)},          ell(w)=|J(w)|,
tilde_pi(w,j)=1/[|X_d|ell(w)],
L((w,j),(w',j'))=P_d(w,w')/ell(w').
```

M104 partitions this lift by keys
`kappa=(j,p,Q_L,Q_R)`, where `p` is the prefix product and the two `Q`'s are
support partitions including isolates.  `beta(d)` is the Poincare gap of the
exact stationary-flow projection `bar L`.  At `d=2`, there is one base word,
one lifted state, and one key; all three relevant gap conventions equal one.

## 4. Exact cut-refresh law and both comparison constants

For a key `kappa`, write `w~kappa` when the unique cut at the key's recorded
position gives that key, and put

```text
S_kappa=sum_(w~kappa) 1/ell(w).
```

Summing `tilde_pi` over the cell gives exactly

```text
bar_pi(kappa)=S_kappa/|X_d|.                            (4.1)
```

The explicit holding half of `P_d` keeps `w` and refreshes the cut uniformly
in `J(w)`.  Doubling this half-subkernel gives a Markov kernel `G_d` with

```text
G_d(kappa,lambda)
 =S_kappa^(-1) sum_(w~kappa,w~lambda) ell(w)^(-2),
Q_G(kappa,lambda)
 =|X_d|^(-1) sum_(w~kappa,w~lambda) ell(w)^(-2).       (4.2)
```

The row sum in (4.2) is `S_kappa/|X_d|`, because each incident word supplies
`ell(w)` possible refreshed cuts.  The flow is symmetric.  Equivalently this
is the two-block Gibbs update `K -> W -> K'` under
`Pr(W=w,K=kappa(w,j))=1/[|X_d|ell(w)]`.  The other half of the projected
kernel contributes a nonnegative Dirichlet form, so the normalization is
exactly

```text
beta(d)>=gap(G_d)/2.                                   (4.3)
```

Now let `C_kappa` be the raw fixed-key word cell and define

```text
Z_inc=sum_kappa |C_kappa|=sum_w ell(w),
rho(kappa)=|C_kappa|/Z_inc.
```

For compatible adjacent keys define the off-diagonal stationary flow

```text
Q_A(kappa,lambda)=|C_kappa intersect C_lambda|/(2Z_inc). (4.4)
```

This is a valid Markov chain: for each `w in C_kappa` there are at most two
adjacent central-cut shifts, so the total off-diagonal numerator in a row is
at most `2|C_kappa|`; the unused mass is held.  Equation (4.4) is symmetric,
so `A_d` is reversible for `rho`.  It is equivalently obtained by choosing a
uniform word in the current raw cell and then a left/right direction with
probability one half.

Because `1<=ell<=D` and `|X_d|<=Z_inc<=D|X_d|`, one has pointwise

```text
D^(-1)<=bar_pi(kappa)/rho(kappa)<=D.                   (4.5)
```

On every off-diagonal `A_d` edge, (4.2) and (4.4) give

```text
Q_G>=2D^(-2)Q_A.                                       (4.6)
```

The needed variance direction is
`Var_barpi(f)<=D Var_rho(f)`.  Combining it with (4.6), rather than using the
opposite density inequality, proves

```text
gap(G_d)>=2D^(-3)gap(A_d),
beta(d)>=D^(-3)gap(A_d).                               (4.7)
```

Thus M113's corrected `D^3` loss and both factors two are valid.

## 5. Realizable keys, adjacent overlap, and exact cell weight

Let `Cyc(p)` be the cycle partition.  A key is realizable exactly when:

1. `Q_L,Q_R` coarsen `Cyc(p)`;
2. their bipartite incidence multigraph, with one edge per `p`-cycle, is
   connected and unicyclic;
3. `j=d+|Q_R|-|Q_L|`.

Necessity follows from the accepted M97 incidence theorem and the two
genus-zero side identities.  In particular `c(p)=|Q_L|+|Q_R|`, and the left
identity gives the displayed value of `j`.

The converse construction is complete.  In a block `B`, minimally factor
each cycle of `p_B`, then add square pairs along a tree joining those cycles.
This gives connected support, product `p_B`, and exactly

```text
k_B=|B|+c(p_B)-2
```

factors.  Interleaving the disjoint block words gives side lengths `j` and
`2d-j`; the fixed connected incidence graph makes the total support
connected.  No zero-size endpoint is silently assumed.

For keys `kappa=(j,p,Q_L,Q_R)` and
`lambda=(j+1,p',Q'_L,Q'_R)`, their cells overlap exactly when

```text
t=p^(-1)p' is a transposition,
Q'_L=join(Q_L,t),             Q_R=join(Q'_R,t).        (5.1)
```

In that case every common word is uniquely `u,t,v'`, and

```text
C_kappa intersect C_lambda=U_kappa x {t} x V_lambda.  (5.2)
```

If `t` joins two `p`-cycles, realizability forces their two `Q_L` blocks to
merge and leaves `Q_R` fixed.  If `t` cuts one `p`-cycle, `Q_L` stays fixed
and the corresponding `Q_R` block splits.  These are exactly the asserted
coagulation and fragmentation cases.

Using the classical convention-checked genus-zero transitive-factorization
count

```text
|F(B,p_B,k_B)|
 =k_B! |B|^(c_B-3)
  product_(p-cycle a in B) |a|^|a|/(|a|-1)!,
```

the side interleavings cancel every `k_B!`.  The resulting exact cell count
is therefore

```text
|C_kappa|=j!(2d-j)!
 product_(B in Q_L union Q_R)|B|^(c_B-3)
 product_(p-cycle a)[|a|^|a|/(|a|-1)!]^2.             (5.3)
```

The algebra and convention are correct.  The independent exhaustive audit
also verifies (5.2)--(5.3) for every `d<=4` cell.

## 6. Qualitative connectivity, including `d=2`

M113's connectivity proof survives direct audit.

For a nontrivial cycle of `p`, choose `x` on it and
`t=(x,p^(-1)(x))`.  Right multiplication `p'=pt` splits off `{x}`.  Keeping
`Q_L` fixed and splitting `{x}` from its old `Q_R` block replaces one
incidence edge by a residual edge plus a leaf.  Connectedness and cyclomatic
number one are preserved.  Iteration reaches `p=id`.

At `p=id`, if `|Q_L|>1`, connectedness forces one right block to meet two
distinct left blocks.  Joining labels on those two incidence edges merges
the left blocks; the next singleton split restores `p=id` and increases
`|Q_R|` by one.  Iteration reaches

```text
kappa_e=(2d-2,id,{[d]},{{endpoints(e)}, all other singletons}).
```

For `d>=3`, extreme keys whose two-subsets differ by one label communicate
through the stated three-label intermediate with one transposition cycle and
one right triple.  The graph of two-subsets under one-label replacement is
connected.  At `d=2`, only one extreme/key exists.  This proves reachability
only; M113 correctly makes no canonical-path congestion claim.

## 7. First Higgs lift and exact Lorentzian refutation

Fix `p` with `c>=2` cycle atoms.  Let `M` be the direct sum of red and blue
graphic matroids on `K_c`, and let `N` be the graphic matroid of the doubled
multigraph after forgetting colors.  Every `N`-flat contains both colored
copies of all edges internal to the blocks of a vertex partition, hence is
an `M`-flat; thus `N` is a quotient of `M`.

The first Higgs lift has

```text
r_H(X)=min(r_M(X),r_N(X)+1)
```

and rank `c`.  A size-`c` set is a basis exactly when each color is a forest
and the uncolored union is connected.  Contracting the two forest component
partitions produces a connected bipartite incidence graph with `c` vertices
and `c` atom-edges, hence a unicycle.  Conversely, spanning trees within all
partition blocks lift every fixed-`p` key.  This proves the claimed fixed-`p`
matroid skeleton, while correctly not identifying variable-`p` moves with a
single fixed-ground-set exchange.

On the `p=id,d=4` slice, a basis with `r` red edges has exact per-witness
coefficient

```text
w(B)=(2r)!(8-2r)! / product_(C in Q_L union Q_R)|C|.  (7.1)
```

Indeed the exact cell weight divided by its
`product_C |C|^(|C|-2)` colored-tree witnesses gives (7.1).  Differentiating
in red `01,02` and restricting the Hessian to red `03` and blue
`01,02,13` gives exactly

```text
[  0 180 180 180 ]
[180   0   0  64 ]
[180   0   0  48 ]
[180  64  48   0 ].                                  (7.2)
```

Its exact determinant is `8294400`; it is nonsingular and has trace zero.
A real symmetric nonsingular `4x4` matrix with positive determinant has an
even number of negative eigenvalues, and trace zero rules out zero or four,
so its inertia is exactly `(2,2)`.  Interlacing gives at least two positive
eigenvalues in the full derivative Hessian, contradicting the Lorentzian
quadratic-derivative signature.  With the factorial tilt removed, the same
matrix entries become `1/8,1/9,1/12` in the asserted positions and its exact
determinant is `1/82944>0`, again with inertia `(2,2)`.

This refutes direct application of the natural exact Lorentzian/SLC
augmentation only.  It does not refute every augmentation, comparison, or a
polynomial gap for `A_d`.

## 8. Balanced pointwise edge and aggregate arithmetic

For even `d>=6`, M113's source

```text
sigma_d=(3,(01),{{0,1,2},{3},...,{d-1}},{[d]})
```

is realizable.  For `A` containing `0` but not `1`, the target with `p'=id`,
the same left partition, and right partition `{A,A^c}` is compatible through
`t=(01)`.  Writing `a=|A|`, `b=d-a`, the source suffix count is

```text
4(2d-3)!d^(d-4),
```

while the target suffix count is

```text
(2d-4)!a^(a-3)b^(b-3).
```

The common prefix cancels and the direction coin supplies the remaining
factor `1/2`, giving exactly

```text
A_d(sigma_d,lambda_A)
 =a^(a-3)b^(b-3)/[8(2d-3)d^(d-4)].                   (8.1)
```

At `a=b=d/2`, this is

```text
2^(-d+3)/[(2d-3)d^2].                                (8.2)
```

There are `binom(d-2,d/2-1)` distinct balanced targets.  The elementary
maximum-binomial bound
`binom(d-2,d/2-1)>=2^(d-2)/(d-1)` therefore yields aggregate probability

```text
at least 2/[(d-1)(2d-3)d^2].                          (8.3)
```

Thus individual-edge lower bounds fail exponentially on this family, while
the multiplicity cancels the exponential loss for this source.  M113
correctly leaves a uniform all-key aggregate bound unresolved.

## 9. Independent finite reconstruction

`independent_audit.py` was written from scratch and imports no predecessor
mission code.  It enumerates connected identity words, derives central cuts
from the genus formula, independently generates all combinatorial keys,
checks every raw Cartesian cell and adjacent overlap, constructs rational
stationary flows for `A_d`, `G_d`, and `bar L`, and then diagonalizes their
reversible symmetrizations numerically.

| d | candidate words | states | lifted incidences | keys | gap(A) | gap(G) | beta |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3 | 729 | 240 | 336 | 9 | 0.1414353635 | 0.0896143806 | 0.1461033961 |
| 4 | 1,679,616 | 131,040 | 234,720 | 101 | 0.1254163084 | 0.0980244430 | 0.1288510552 |

For each `d`, the observed key set equals the independently generated
realizable-key set, the key graph has one component, and there are zero cell
formula, Cartesian product, overlap, coagulation/fragmentation, interval, or
Hurwitz-target failures.  The reported stationary marginals by cut and cycle
type are also reproduced.  The two-sided singleton-split-or-reverse rate has
minimum `1/4` at `d=3` and `1/3` at `d=4`, with no zero-rate key.  The
fixed-`p` basis counts are independently `1,18,378` for `c=2,3,4`.

The reproduction command from repository root is

```text
python3 -B \
  experiments/20260811-polynomial-mixing-resolution/cycle-24/mission-M118-m113-fresh-referee/independent_audit.py \
  --d 2 3 4 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-24/mission-M118-m113-fresh-referee/independent_results.json
```

The run is deterministic (`seed=null`), used Python `3.12.3` and NumPy
`1.26.4`, and took about 16.5 seconds.  Floating row/symmetry residuals are at
most `1.7e-14`.  Exact Hessian and balanced-family values are stored as
rational strings in the raw JSON.

## 10. Final verdict, objections, and first open lemma

**ACCEPT, with zero material numbered objections.**

M113 validly promotes the exact cut-refresh reduction
`beta(d)>=gap(A_d)/(2d-1)^3`, the universal qualitative connectivity of the
explicit incidence chain, and the first-Higgs-lift skeleton.  Its exact
Hessian correctly blocks the natural Lorentzian route, and its balanced
family correctly blocks pointwise edge comparison without producing an
aggregate bottleneck.

The first standalone obligation remains exactly M113's:

> **LOCAL UNICYCLE INCIDENCE GAP.** Prove
> `gap(A_d)>=d^{-O(1)}` for the exact weighted connected-unicycle
> coagulation/fragmentation chain, for every `d>=3`.

This report does not attack that lemma.  `beta(d)`, `Gamma_0(d)`,
`gamma_1(d)`, the full heat-bath gap/mixing time, and both terminal criteria
remain unresolved.
