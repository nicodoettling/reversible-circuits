# M44 halfway checkpoint — exact rank representation and two failed positive routes

The weighted quartile-shell statement is still open.  The work so far has
nevertheless produced one universal structural identity, an exact full-kernel
boundary reduction, and two sharp falsifications of tempting positive-transfer
shortcuts.  More than half of this work is away from fixed-path canonical
injections.

## 1. Universal prefix graphic-rank identity

Write `n=N-1`, `m=2n`, and let `w=(t_1,...,t_m)` lie in the minimal connected
macro `F_N`.  Let `G_j` be the support multigraph of the first `j` factor
occurrences, let `c_j` count its connected components including isolated
vertices, and put `r_j=N-c_j`.

The join factors form a spanning tree (M34).  At every prefix, the connected
components of `G_j` equal the components of the prefix join forest: a cut
factor has both endpoints in one current prefix cycle and hence in one join
component.  Therefore the number of join steps by time `j` is exactly `r_j`.
Since `j-r_j` steps are cuts,

```text
h_j=N-cycles(t_1...t_j)=2r_j-j=2(N-c_j)-j.             (1.1)
```

Consequently

```text
Area(w)=2 sum_(j=1)^m r_j-m(m+1)/2
       =n(2n+1)-2 sum_(k=1)^n J_k,                    (1.2)
```

where `J_1<...<J_n` are the positions at which Kruskal's greedy scan of the
ordered support multigraph accepts an edge.  Thus the open area law is exactly
an integrated graphic-rank / greedy-basis-position law on uniform increasing
planar maps, not an ordinary Catalan law.

## 2. Exact width-12 and macro-exit reduction

If one same-product block of length `r` is replaced, only the `r-1` internal
prefixes can change.  At internal offset `k`, both old and new prefixes start
at the same permutation and have the same endpoint, so their Cayley ranks
differ by at most `2 min(k,r-k)`.  Hence

```text
|Delta Area| <= delta_r=2 floor(r^2/4),
delta_3=4, delta_4=8, delta_5=12.                     (2.1)
```

For `A_q={w in F_N:Area(w)<=q}`, the literal lazy-kernel formula gives

```text
Q_K(A_q,A_q^c)
 =1/(2|R_m|) sum_r 1/(m-r+1) sum_i
    |Omega|^(-1) sum_(w in A_q) H_(i,r)(w,A_q^c)
 <=Q_K(A_q,F_N^c)
   +pi(F_N)/(2|R_m|) sum_r mu_N(q-delta_r<Area<=q).   (2.2)
```

Moreover, if a chosen block update exits `F_N`, deleting the old block leaves
all outside factors inside blocks of the new disconnected support partition.
Thus `Q_K(A_q,F_N^c)` is controlled by the stationary incidence of consecutive
length-`r` support separators.  A thin area shell alone can never prove
Terminal B: one must also prove this separator incidence superpolynomially
small.

## 3. Lorentzian / complete-log-concavity route is exactly false

For join-position variables define the homogeneous multiaffine polynomial

```text
F_N(z)=sum_P W_N(P) product_(j:P_j=U) z_j.
```

The exact M38 fixed-path coefficients give a decisive `N=4` obstruction.  The
derivative with respect to position zero is quadratic.  On positions
`1,2,3,4`, its Hessian is

```text
[[0,1536,720,264],
 [1536,0,264,96],
 [720,264,0,0],
 [264,96,0,0]].                                      (3.1)
```

The off-diagonal `2 by 2` block
`[[720,264],[264,96]]` has determinant `-576`, so it is nonsingular.  A
nonsingular symmetric saddle matrix `[[A,B],[B^T,0]]` with square nonsingular
`B` has inertia `(2,2)`: the bottom coordinate plane is a maximal totally
isotropic plane, and nonsingularity rules out zero eigenvalues.  A Lorentzian
quadratic may have at most one positive eigenvalue.  Hence `F_4` is not
Lorentzian.  Positive diagonal rescaling cannot repair this because it acts by
congruence and preserves inertia.  The floating eigenvalues in the JSON were
used only to locate the exact witness.

## 4. Endpoint-matched perfect-matching reference

For a Dyck path `P`, let

```text
p(P)=product_(D steps) (height immediately before D).
```

This counts perfect matchings with opener/closer path `P`.  The un-tilted
reference is pointwise exponentially wrong: for the bottom and mountain paths,

```text
(W(top)/p(top))/(W(bottom)/p(bottom))=N^(n-1)/n!.
```

The unique endpoint-matched exponential tilt used here is

```text
q_n=[N^(n-1)/n!]^(1/[n(n-1)]),
reference(P)=p(P)q_n^Area(P).                         (4.1)
```

Its exact un-tilted area coefficients satisfy the positive transfer

```text
(h,a)->(h+1,a+h+1) with multiplicity 1,
(h,a)->(h-1,a+h-1) with multiplicity h.               (4.2)
```

All first reference quartiles through `n=60` have CDF at most `1/2` and a
lower-half nondecreasing coefficient sequence in the floating diagnostic; the
shell ratio at `n=60` is about `0.0149`.  These are finite falsification checks,
not a theorem.  The actual and reference first-quartile areas agree through
`N=12` but differ at `N=13` (`108` versus `106`), exactly refuting equality of
the thresholds.  Normalized area-marginal density distortion is only `1.4086`
through `N=13`, again finite only.

The Duchi--Poulalhon--Schaeffer Cayley-tree/permutation construction pairs the
two labels incident to every inserted black degree-two vertex, producing this
uniform perfect matching.  Their closure algorithm does not identify the
factorization join/cut path with the matching opener/closer path; the unequal
`N=4` coefficients already preclude that identification.

## 5. Current smallest open implication

The exact M44 target would follow from the following weaker-than-unimodality
statement.

> **FIRST-QUARTILE PREFIX-RECORD.**  For every `N>=6`, if `q_N` is the first
> feasible area with `sum_(a<=q_N)H_N(a)>=|F_N|/4`, then
> `sum_(a<=q_N)H_N(a)<=|F_N|/2` and
> `H_N(q_N)>=H_N(a)` for every feasible `a<=q_N`.

Indeed there are at most `L=1+(n^2-n)/2` feasible area layers.  If
`H_N(q_N)>=|F_N|/8`, its shell/CDF ratio is at least `1/4`.  Otherwise the
previous cumulative mass is at least `|F_N|/8`; the prefix-record property
gives `L H_N(q_N)>=|F_N|/8`, hence shell/CDF at least `1/(4L)`.

This proposition holds in the exact `N<=13` tables, but is not implied by the
M38 no-cliff inequality and is not being inferred from finite data.  The next
phase will test whether the positive matching transfer can prove the analogous
reference proposition and whether a polynomial comparison survives structured
path families.  If not, the final report will freeze the exact reductions and
name the connected/reference comparison or separator-incidence estimate as the
first genuine gap.

## Reproduction so far

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-10/mission-M44-weighted-quartile-or-bottleneck/lorentzian_path_falsifier.py \
  --input experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M38-weighted-dyck-shell/results-paths-N8.json \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-10/mission-M44-weighted-quartile-or-bottleneck/lorentzian-results.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-10/mission-M44-weighted-quartile-or-bottleneck/tilted_matching_reference.py \
  --actual experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M38-weighted-dyck-shell/results-N13.json \
  --reference-max-n 60 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-10/mission-M44-weighted-quartile-or-bottleneck/tilted-matching-results.json
```
