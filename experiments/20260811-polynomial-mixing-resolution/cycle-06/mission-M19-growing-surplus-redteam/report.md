# Cycle 06 M19 report: isolated-label phase cut rejected at every surplus

## 1. Exact claim, quantifiers, and convention

Permutations satisfy `(pq)(x)=p(q(x))`, and a word evaluates as
`t_1...t_m`.  Put `M=binom(N,2)` and let the global target be uniform on

```text
Omega(N,m)={w in T_N^m:t_1...t_m=id}.
```

The kernel is exactly

```text
K=(1/2)I
 +(1/(2|R_m|)) sum_(r in R_m)
   (1/(m-r+1)) sum_i H_(i,r),
R_m={r in {3,4,5}:r<=m}.                              (1.1)
```

Fix one label `v` and define the isolated-label component-phase refinement

```text
A_v={w in Omega(N,m):no factor of w contains v}.       (1.2)
```

For a cut `A`, write

```text
Phi_pm^K(A)=Q_K(A,A^c)/min{pi(A),pi(A^c)}.
```

The proved growing-surplus theorem is:

> **Isolated-label anti-bottleneck.**  For every `N>=3`, every even `m>=4`,
> and every label `v`, both sides of (1.2) are nonempty and
>
> ```text
> Phi_pm^K(A_v)
> >=1/[3(m-2)(N-2)D_N]
> >=1/(6mN^3),
> D_N=(3N^2+N-12)/2.                                  (1.3)
> ```

In particular, (1.3) holds uniformly for every growing surplus
`g=m/2-(N-1)` in the entire assigned intermediate window.  It rigorously
rejects the fixed-isolated-label phase cut as a Terminal-B candidate.  It
does not resolve the union over missing labels, the connected bottom layer,
or any internal full-support cut.

## 2. Full proof

### 2.1 Exact stationary mass and smaller-side orientation

Let

```text
Z_(d,k)=|Omega(d,k)|.
```

Avoiding `v` identifies `A_v` bijectively with `Omega(N-1,m)`.  Therefore

```text
pi(A_v)=Z_(N-1,m)/Z_(N,m).                             (2.1)
```

This is an exact global stationary mass, not a macro-conditional one.  It is
computable, for example, from the regular-character identity

```text
Z_(d,m)=(1/d!) sum_(lambda partition d)(f^lambda)^2 c_lambda^m,       (2.2)
```

where `c_lambda` is the content-sum eigenvalue of the transposition class
sum.  The correctly oriented smaller side is

```text
A_v       if 2Z_(N-1,m)<=Z_(N,m),
A_v^c     otherwise.                                  (2.3)
```

Its exact mass is

```text
min{Z_(N-1,m),Z_(N,m)-Z_(N-1,m)}/Z_(N,m).             (2.4)
```

No component-count unimodality or asymptotic orientation is assumed.

### 2.2 Exact adjacent-square incidence in the isolated-label fiber

Put `d=N-1` and `M_-=binom(N-1,2)`.  Conditional on `A_v`, the state is
uniform on `Omega(d,m)`.  Let

```text
S(w)=#{i in {1,...,m-1}:t_i=t_(i+1)}.
```

Deleting a marked adjacent square gives a bijection with:

1. a word in `Omega(d,m-2)`;
2. one of the `M_-` transpositions on the remaining labels; and
3. one of the `m-1` insertion gaps.

The marked position makes the deletion bijective even when several squares
overlap.  Hence

```text
E[S]=(m-1)M_- Z_(d,m-2)/Z_(d,m).                      (2.5)
```

Since `S<=m-1`,

```text
Pr[S>=1]>=M_- Z_(d,m-2)/Z_(d,m).                      (2.6)
```

Let `p_d(k)` be the return probability after `k` uniform random
transpositions in `S_d`.  Then

```text
Z_(d,k)=M_-^k p_d(k),
p_d(k)=(1/d!) sum_(lambda partition d)(f^lambda)^2 r_lambda^k,        (2.7)
```

where `r_lambda` is the real transposition character ratio and
`|r_lambda|<=1`.  Both `m` and `m-2` are even, so every summand is
nonnegative and decreases with the exponent:

```text
p_d(m-2)>=p_d(m).                                     (2.8)
```

Substituting (2.7)--(2.8) into (2.6) proves the uniform bound

```text
Pr[S>=1]>=1/M_-.                                      (2.9)
```

### 2.3 Exact transposition-product H3 fiber

For a transposition `a`, let `F_3(a)` be its length-three transposition
fiber.  Choose the third factor `z` and count the ordered first two factors
whose product is `az`.

- For `z=a`, the product is the identity and there are `M` equal pairs.
- There are `2(N-2)` transpositions `z` sharing one endpoint with `a`;
  `az` is a 3-cycle and has three ordered two-transposition factorizations.
- There are `binom(N-2,2)` transpositions disjoint from `a`; `az` is a
  double transposition and has two ordered factorizations.

Thus the exact conjugacy-invariant fiber size is

```text
|F_3(a)|
 =M+3[2(N-2)]+2 binom(N-2,2)
 =(3N^2+N-12)/2
 =D_N.                                                 (2.10)
```

In particular, `D_N<=2N^2` for `N>=3`.

### 2.4 Boundary-safe H3 exits

Whenever `S(w)>=1`, choose the first adjacent square `e,e`.  If it is not
the final pair, use the `H_3` window beginning at it; if it is final, use the
window ending at position `m`.  Retain the padding transposition `a` and use
one of

```text
(e,e,a)->(f,f,a),       (a,e,e)->(a,f,f),              (2.11)
```

where `f` contains `v`.  Both sides of each display have the same ordered
block product `a`.  Every one of the `N-1` transpositions containing `v`
gives a distinct outcome outside `A_v`.

The exact kernel selects block size three with coefficient
`1/[2|R_m|]`, the chosen window with probability `1/(m-2)`, and an outcome
uniformly from the `D_N` triples in (2.10).  Since `|R_m|<=3`,

```text
K(w,A_v^c)>=(N-1)/[6(m-2)D_N]                         (2.12)
```

on every certified state.  This includes laziness and has no omitted choice
of the replacement transposition.

### 2.5 Full r=3,4,5 flow and oriented conductance

For each available block size, define its exact boundary contribution

```text
Q_r(A_v,A_v^c)
 =pi(A_v)/[2|R_m|(m-r+1)]
   E_(w|A_v)[sum_i H_(i,r)(w,A_v^c)].                 (2.13)
```

Laziness contributes zero and

```text
Q_K(A_v,A_v^c)=sum_(r in R_m) Q_r(A_v,A_v^c).         (2.14)
```

Every term is nonnegative.  Equations (2.9) and (2.12) give the certified
`r=3` contribution

```text
Q_3(A_v,A_v^c)
 >=pi(A_v)(N-1)/[6(m-2)M_-D_N]
 =pi(A_v)/[3(m-2)(N-2)D_N].                          (2.15)
```

The complete `r=4` and `r=5` flows are retained in (2.14) and can only add
to (2.15); no transition type is dropped in an upper-bound bottleneck
argument.  Reversibility gives the identical flow from `A_v^c` to `A_v`.

Divide (2.15) by the exact smaller-side mass (2.4).  Since that mass is at
most `pi(A_v)`,

```text
Phi_pm^K(A_v)>=1/[3(m-2)(N-2)D_N].                   (2.16)
```

Finally, `m-2<=m`, `N-2<=N`, and `D_N<=2N^2` prove (1.3).

## 3. Worst probability, runtime, path, and congestion accounting

- Certified-state probability under `pi(.|A_v)` is at least `1/M_-`.
- Conditional on certification, the summed one-step exit probability is at
  least `(N-1)/[6(m-2)D_N]`.
- Every witness has path length one.  There is no comparison flow or hidden
  congestion.
- Finding the first square costs `O(m)`.  Listing the `N-1` exit outcomes and
  evaluating the exact fiber count costs polynomial time; the witness can be
  implemented in `O(m+N^2)` arithmetic operations.
- The mass formula (2.1)--(2.2) fixes orientation exactly, but evaluating its
  branch is unnecessary for the lower bound because (2.4) is always at most
  `pi(A_v)`.
- The final lower bound is inverse polynomial jointly in `N,m`, uniformly
  over bounded, growing, and dense surplus.

## 4. Dependencies with status

- **PROVED HERE:** exact mass/orientation, marked-square incidence,
  even-return monotonicity from the character expansion, exact `D_N`, the
  boundary-safe exit, every normalization in `Q_3`, and the two-sided
  conductance bound.
- **INHERITED PROVED:** uniform heat-bath reversibility/stationarity and the
  regular-character formulas for identity-word counts.
- **NOT USED:** component-count unimodality, fixed-genus pendant estimates,
  dense support-partition transfer, pure Hurwitz mixing, finite convergence,
  or a canonical hub.
- **EMPIRICAL/COMPUTATIONAL DEPENDENCIES:** none.

## 5. First unproved standalone proposition

> **MISSING-LABEL UNION CONDUCTANCE.**  Let
>
> ```text
> U_(N,m)=union_(v in [N]) A_v
> ```
>
> be the set of identity words whose factorization graph has at least one
> isolated label.  Prove a universal inverse-polynomial two-sided
> conductance bound for `U_(N,m)` throughout
> `2(N-1)<m<2+4M log(2N)`, or give an explicit superpolynomial-conductance
> counterexample family with exact mass and full `r=3,4,5` flow.

The fixed-label theorem does not control overlaps: an update can leave
`A_v` while remaining in another `A_u`.  Beyond this union lie the growing-
`g` connected bottom-layer cut and full-support disconnected refinements.

## 6. Strongest self-attack and counterexample verdict

The cut `A_v` can have exponentially small stationary mass.  That does not
rescue it as a bottleneck: the correctly oriented conductance divides by the
smaller mass and (2.16) remains polynomial.  However, the theorem says
nothing about the union of many strongly overlapping rare events.  Words
missing several labels may require several updates to enter full support,
so (2.16) cannot be union-bounded into a result for `U_(N,m)`.

Likewise, no inference is made about internal full-support geometry or the
connected bottom layer `F_(N,g)`.  Known large-genus asymptotics prevent a
uniform pendant-leaf proof there.  No explicit infinite family with
superpolynomial full-`K` conductance survived this cycle, and slow auxiliary
`B` or Hurwitz modes would not establish Terminal B for `K`.

## 7. Calibration

- Odd `m` gives an empty identity fiber; `m=0` is singleton; original `m=2`
  is excluded.  The theorem starts at even `m=4`.
- `N=2` is singleton and excluded from (1.3); for `N>=3`, both `A_v` and its
  complement are nonempty by repeated-square words.
- At `(N,m)=(3,4)`, `(4,4)`, and `(4,6)`, respectively,

  ```text
  pi(A_v)=1/27,   27/120=9/40,   243/3936=81/1312.
  ```

- At `m=4`, `R_m={3,4}`.  The use of `|R_m|<=3` is conservative, and the
  whole-word `H_4` flow remains in (2.14).
- Near-minimal doubled-tree words and every surplus are covered by the same
  incidence identity.  Ordered factors and disjoint-component interleavings
  are never collapsed.
- No vertex-degree parity, edge-multiplicity parity, or graph-only dynamics
  is used.  The length-two local-simulation obstruction is irrelevant to the
  actual `H_3` transition (2.11).

## 8. Artifacts and reproduction commands

Owned artifacts:

- `experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M19-growing-surplus-redteam/plan.md`;
- `experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M19-growing-surplus-redteam/checkpoint.md`;
- this `report.md`.

No computation was used.  Reproduction consists of checking the deletion/
insertion bijection, the displayed finite character sum, the elementary
triple-fiber count, and the exact kernel factors in (2.12)--(2.15).  The
repository base commit is `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

PROVED
