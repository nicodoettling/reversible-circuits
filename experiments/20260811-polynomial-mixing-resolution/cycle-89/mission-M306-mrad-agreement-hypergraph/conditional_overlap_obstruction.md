# M306: Weighted Agreement Dual and Conditional-Overlap Obstruction

Date: 2026-08-14 UTC

Status: exact finite-action theorems proved; actual-M135 MRAD remains
unresolved.

## 1. Scope and immutable inputs

Fix `d>=6`, an adjacent edit index, and one actual M135 perfect matching
`M`.  Let `A_d` be the finite signed-Hurwitz action image on `Z_d`, and use
the accepted fibers

```text
K_Q={a in A_d:a(w_Q)=tau_i(w_Q)},
E_a(M)={Q in M:a in K_Q}.
```

The accepted individual routing/transitivity input makes every `K_Q`
nonempty and of common size

```text
k_d=|A_d|/|Z_d|.
```

The direct source locks pass at top digests

```text
M296 9ab0978c92fee4f92d000604eac4610dbbe6c7aeeaebe3fe86968514990d1f7f
M299 1654bcd6319b3020fe49a34e54a9961b2687ba5daab107baca11873749065b8d
M301 ae7ca4a3089259ac59df8e15ea3ff8d957c01956d842454f2dd1dcf3a881adcd
M304 5518f47facfab896ca1d32d4d3f9626a52c25e05cf970861395d4e19c2a0f4cf
```

Every payload row in those four inventories passes.  M301/M304 supplies the
exact agreement-hyperedge cover formulation and its `d=3` non-Helly guard.
M296/M299 keeps finite-action nonemptiness separate from shortest literal
braid length.

Nothing below proves a literal route, voltage correction, congestion bound,
gap, mixing theorem, or Terminal.

## 2. Exact residual conditional-overlap moment

For nonempty `U subset M`, define

```text
r_U(a)=|E_a(M) intersect U|.
```

### Proposition 2.1 (conditional moment identity; **PROVED**)

For every anchor `P in U`,

```text
(1/k_d) sum_(Q in U)|K_P intersect K_Q|
  =(1/|K_P|)sum_(a in K_P)r_U(a)
  =E[r_U(a) | a in K_P].                            (2.1)
```

Consequently the predeclared condition

```text
max_(P in U) (1/k_d)sum_(Q in U)|K_P intersect K_Q|
  >=|U|/d^C                                           (RCOM)
```

implies MRAD with the same exponent.

#### Proof

Expand the conditional sum and interchange the two finite summations:

```text
sum_(a in K_P)r_U(a)
 =sum_(a in K_P)sum_(Q in U)1[a in K_Q]
 =sum_(Q in U)|K_P intersect K_Q|.
```

An average cannot exceed the maximum of `r_U`, so `(RCOM)` supplies the
required action.  QED.

The average over all anchors is the exact size-biased second moment

```text
(1/(|U|k_d))sum_(P,Q in U)|K_P intersect K_Q|
 =sum_a r_U(a)^2 / sum_a r_U(a).                    (2.2)
```

This is a weighted pair-overlap statistic, not a Helly assertion.

## 3. The actual rank-three Helly guard survives

For M301/M304's actual subfamily `U=[0,2,9]`, every fiber has size nine and

```text
K_0 intersect K_2={45},
K_0 intersect K_9={49},
K_2 intersect K_9={89},
K_0 intersect K_2 intersect K_9=empty.
```

Hence every anchored conditional score in (2.1) is exactly

```text
(9+1+1)/9=11/9,                                     (3.1)
```

while `max_a r_U(a)=2`: each displayed pair action agrees with two edges,
and empty triple intersection forbids agreement with all three.  Thus the
conditional identity is consistent with the hereditary 2-Helly
counterexample.  It neither identifies the three pair actions nor promotes
them to one common action.  Complete `d=3` matching MT2H remains vacuous, as
accepted by M304.

This exact boundary case is not evidence for or against `d>=6` MRAD.

## 4. Correct weighted-orbit target: fractional action cover

Let `N=|M|`.  Define the fractional action-cover number

```text
tau*(M)=min sum_a x_a
subject to x_a>=0 and sum_(a in K_Q)x_a>=1 for every Q in M.  (4.1)
```

For weights `lambda_Q>=0`, write

```text
W_lambda(a)=sum_(Q in E_a(M))lambda_Q,
||lambda||_1=sum_Q lambda_Q.
```

### Theorem 4.1 (weighted agreement dual; **PROVED**)

For every real `q>=1`, the following are equivalent:

```text
tau*(M)<=q,

for every lambda>=0 there is a in A_d with
W_lambda(a)>=||lambda||_1/q.                         (4.2)
```

#### Proof

The LP dual of (4.1) maximizes `sum_Q lambda_Q` subject to
`W_lambda(a)<=1` for every action.  If `tau*<=q`, scale any nonzero weight
vector by `max_a W_lambda(a)` to obtain a dual-feasible vector; duality gives
`||lambda||_1/max_a W_lambda(a)<=q`.  The converse applies (4.2) to every
dual-feasible vector, whose maximum weighted agreement is at most one.
Finite LP duality proves the equivalence.  QED.

Call (4.2) **weighted residual agreement density** `(WRAD_q)`.

### Proposition 4.2 (MRAD and WRAD differ by one harmonic factor; **PROVED**)

1. `(WRAD_q)` implies residual density `1/q` by taking `lambda=1_U`.
2. If every nonempty `U` has agreement density at least `1/q`, then
   `(WRAD_(q H_N))` holds, where `H_N=sum_(j=1)^N1/j`.

#### Proof

Only (2) needs proof.  Sort the weights
`lambda_1>=...>=lambda_N` and put

```text
B=max_(1<=j<=N) j lambda_j.
```

Then `lambda_j<=B/j`, so `||lambda||_1<=B H_N`.  Choose a maximizing `j`
and apply residual density to the top-`j` set.  Some action agrees with at
least `j/q` of those edges and therefore has weighted agreement at least
`j lambda_j/q=B/q>=||lambda||_1/(qH_N)`.  QED.

Since

```text
N=d^(d-3)(2d-2)!/d!,       H_N=O(log N)=O(d log d),  (4.3)
```

MRAD, polynomial fractional action-cover number, and WRAD are polynomially
equivalent.  This is an exact weighted-orbit formulation on the actual edge
set.  It supplies dual weighted obstructions when MRAD fails and never uses
pairwise Helly.

For completeness, a fractional cover of cost `q` also gives, on every
residual `U`,

```text
sum_a x_a|E_a intersect U|>=|U|,
```

so some action covers at least `|U|/q`.  M301's greedy argument then gives an
integral cover of size at most `ceil(q(1+ln N))`.

## 5. Strict obstruction to the predeclared RCOM route

The conditional moment (2.1) can dilute precisely the rare actions that an
action cover needs.  This is not a technical possibility; it occurs in the
largest standard permutation actions.

### Theorem 5.1 (point-stabilizer dilution; **PROVED**)

Let `X` have `N>=4` points and let `A` be either `Sym(X)` or `Alt(X)` in its
natural action.  Use the identity matching, with one constraint

```text
K_x={a:a(x)=x}
```

for every `x in X`.  Then:

1. the identity action agrees with all `N` constraints, so MRAD holds with
   density one and both integral and fractional cover numbers equal one;
2. for every anchor `x`, the full-family RCOM score is exactly two:

   ```text
   (1/|K_x|)sum_(y in X)|K_x intersect K_y|=2.       (5.1)
   ```

#### Proof

For `Sym(X)`, `|K_x|=(N-1)!`, while for `y!=x`,
`|K_x intersect K_y|=(N-2)!`.  Therefore (5.1) is

```text
1+(N-1)(N-2)!/(N-1)!=2.
```

For `Alt(X)`, the two sizes are `(N-1)!/2` and `(N-2)!/2`; the same ratio
and conclusion hold.  The identity action proves item 1.  QED.

More generally, on a subset `U` of size `s` containing the anchor, the score
is `1+(s-1)/(N-1)<=2`, while the identity agrees with all `s` constraints.
For a uniform symmetric permutation, the number `F` of fixed points even has

```text
E[(F)_j]=1,       1<=j<=N,                           (5.2)
```

because an ordered `j`-tuple is fixed with probability `1/(N)_j`.  The same
identity holds for `Alt(X)` through `j<=N-2`.  Low conditional moments can
therefore stay bounded while one exceptional action has full agreement.

Take `N=N_d` from (4.3).  Since `N_d>=d^(d-3)`, for every fixed `C`,

```text
2 < N_d/d^C
```

for all sufficiently large `d`.  Thus polynomial MRAD and even an exact
one-action cover do not imply polynomial RCOM.  Transitivity, maximal
symmetric/alternating monodromy, and point-fiber uniformity cannot justify
the predeclared conditional-stabilizer averaging route.

This theorem is a formal obstruction to the route, not an actual-M135
counterexample.  Actual RCOM could hold only through a new, special
large-overlap theorem for the M135 fibers; no accepted subgroup, aligned
factor-class, double-coset nonemptiness, or transitivity statement supplies
such intersection masses.

## 6. Exact conclusion and next lemma

```text
RCOM => MRAD                                      proved
RCOM polynomially equivalent to MRAD             refuted in general
MRAD <=> WRAD <=> polynomial fractional cover    proved up to O(d log d)
actual d=3 hereditary 2-Helly                     refuted (accepted guard)
actual d>=6 WRAD/MRAD                             unresolved
```

The first valid weighted-orbit input is now explicit:

> For every actual `d>=6` matching and every nonnegative edge weight vector,
> construct one finite action capturing an inverse-polynomial fraction of
> the total weight.

This is `(WRAD)` and is polynomially equivalent to MRAD.  It requires an
extremal high-agreement action, not an average over a point stabilizer.  Even
if proved, polynomial literal braid representative length would remain a
separate SSTID layer.

