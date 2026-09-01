# M190 independent proof audit of frozen M185

Date: 2026-08-13 UTC.

## 1. Immutable gate, target, and scope

Before reading M185's mathematical conclusions, I ran its complete frozen
ledger.  All seven payloads passed, its directory inventory agreed exactly
with `freeze_manifest.md`, and the ledger digest was

```text
9400d67948c99905bc1ce75081466d737247ed47af3fb42d7b7b5c2ae36b64b1.
```

M185 was not edited.  The complete frozen ledgers for accepted M109/M114,
M115/M116, M117/M121, M147/M151, M157/M160, M162/M165, M173/M177, and
M179/M184 also passed.

The audited object is only the normalized full unweighted reset excursion
`F=H/q` in the auxiliary nonlazy minimal-long-cycle parking projection, and
only fresh retained descendants with last-root height `h=3`.  The project
target remains uniform fixed-length identity transposition words, with
`(pq)(x)=p(q(x))` and displayed factors left-to-right.  No `S<=2`, complete
`h=3` sector bound, total AMV, auxiliary gap, original-chain theorem,
polynomial mixing, or project terminal is under audit.

## 2. Independent three-mode and Bayes derivation

At the fresh parent

```text
xi=(B+L,2,1,B),       mu_parent=Beta(1,1),
```

a height-three degree-`d` root and retained observation `0<=a<d` produce

```text
xi_a=(B+2,d+2,a+1,B),       mu_a=Beta(a+1,d-a+1).       (2.1)
```

The suffix excess is two.  The accepted M162/M165 feature-degree theorem
therefore places the entire Hilbert-valued child feature in the first three
Jacobi modes.  Put

```text
p=E_a U,       v=E_a(U-p)^2,
gamma=E_a(U-p)^3/v,
P_2=(U-p)^2-gamma(U-p)-v,
h_2=E_aP_2^2.
```

Then `(1,(U-p)/sqrt(v),P_2/sqrt(h_2))` is orthonormal.  If its vector
coefficients are `(A_0,A_1,A_2)`, direct Parseval gives the exact child trace

```text
S_a=sum_(i=0)^2 ||A_i||^2.                            (2.2)
```

Let `L_a=binom(d,a)U^a(1-U)^(d-a)` and
`pi_a=E_parent L_a=1/(d+1)`.  For the feature block
`f_a=sqrt(eta/pi_a)L_a Phi_a`, posterior conjugacy gives

```text
E_parent||f_a||^2
 =(eta/pi_a)E_parent[L_a^2||Phi_a||^2]
 =eta E_a[L_a||Phi_a||^2].                           (2.3)
```

There is one remaining likelihood after Bayes, not zero or two.  Since the
quadratic mode is orthogonal to `U-p`,

```text
E_parent[(U-1/2)f_a]
 =sqrt(eta pi_a)[(p-1/2)A_0+sqrt(v)A_1].             (2.4)
```

The parent variance is `1/12`.  Therefore the branch divided by `eta` is
the full Hilbert quadratic form with scalar matrix

```text
G_ij=E_a[L_a e_i e_j]-12pi_a z_i z_j,
z=(p-1/2,sqrt(v),0).                                 (2.5)
```

All three likelihood-weighted off-diagonal entries remain.  Multiplying
`mu_a` by `L_a` yields

```text
hat mu=Beta(2a+1,2d-2a+1),
lambda_0=E_aL_a
 =(d+1)/(2d+1) binom(d,a)^2/binom(2d,2a),            (2.6)
```

so the positive matrix in (2.5) is exactly
`lambda_0 E_hat[e e^T]`.  The attachment value `a=d` is killed before the
history direct sum is taken and is nowhere conditioned back in.  These
identities independently reproduce M185's normalization and every cross
term.

## 3. Exact `2/3` refutation

The standard-library clean-room checker constructs the Jacobi basis from
raw beta moments and obtains

```text
det((2/3)I-G_(20,0))
 =-1731224299/244943654967<0.                         (3.1)
```

This is the determinant in the orthonormal basis; its negative sign proves
that the proposed slack is not positive semidefinite.  A second independent
row gives

```text
det((2/3)I-G_(50,0))
 =-104272204769339/7259860744068816<0.               (3.2)
```

No eigenvalue approximation is needed.  M185's `2/3` refutation is correct.

## 4. Independent universal `3/4` certificate

Vandermonde contains `binom(d,a)^2` as a nonnegative summand of
`binom(2d,2a)`, hence

```text
lambda_0<=lambda_*=(d+1)/(2d+1).                    (4.1)
```

The second-posterior Gram matrix is positive semidefinite, so replacing
`lambda_0` by `lambda_*` increases `G` in Loewner order.  Work in the
unnormalized orthogonal basis `q=(1,U-p,P_2)`.  With `t=2a-d`, exact
beta-moment simplification independently gives

```text
v=[(d+2)^2-t^2]/[4(d+2)^2(d+3)],

h_2=[((d+2)^2-t^2)((d+4)^2-t^2)]
 /[8(d+2)(d+3)^2(d+4)^2(d+5)].                     (4.2)
```

For every `d>=1`, `0<=a<d` implies `|t|<=d`, so both are strictly positive.
The basis change is invertible and Sylvester's criterion applies to

```text
R=(3/4)diag(1,v,h_2)-lambda_*E_hat[qq^T]
  +12/(d+1)(p-1/2,v,0)(p-1/2,v,0)^T.               (4.3)
```

The fresh symbolic derivation obtains the first leading minor

```text
[2d^4+9d^3+11d^2-4+(24d+12)t^2]
/[4(d+1)(d+2)^2(2d+1)]>0.                          (4.4)
```

It obtains for the second leading minor a positive denominator times a
concave quadratic `P_2(x)`, `x=t^2`, whose endpoints are exactly

```text
P_2(0)=(d+2)^3(2d-1)
 (8d^4+40d^3+101d^2+108d+27)>0,

P_2(d^2)=4(d+1)(2d+1)
 (4d^5+108d^4+351d^3+410d^2-27d-54)>0.             (4.5)
```

The last factor is coefficient-positive after `d=1+e`, including the
minimal `d=1` boundary.  Concavity makes this minor positive on the entire
interval `0<=x<=d^2`.

For the determinant, the independent derivation extracts the positive
factor

```text
(d-t+2)(d+t+2)
/[2048(d+1)(d+2)^4(d+3)^4(d+4)^2(d+5)
  (2d+1)^3(2d+3)^3(2d+5)]                          (4.6)
```

and a cubic `P_3(x)`.  Re-expansion in the degree-three Bernstein basis on
`[0,d^2]`, followed by `d=1+e`, regenerates exactly M185's four displayed
lists (with its `3b_1` and `3b_2` scaling).  Their degrees are
`14,14,13,12`, and every coefficient is strictly positive.  This is an
exact symbolic identity from the beta moments, not a degree scan.  Hence the
determinant is positive throughout the interval.

All leading minors are positive.  Thus `R` is positive definite and

```text
G_(d,a)<=(3/4)I_3                                  (4.7)
```

in the normalized basis for every retained branch.  At `d=1,a=0`, the
clean-room normalized determinant is `39/2240>0`; direct diagonalization of
M185's displayed minimal matrix gives top eigenvalue
`(25+sqrt(415))/70<3/4`.  The universal theorem and its boundary cases pass.

## 5. Actual-history suffix-two trace

For the child (2.1), put

```text
k=d+2, D=a+1, U~Beta(D,k-D),
y=w_B/w_(B+1), b=w_B/w_(B+2),
q=(3/2)w_B/w_(B+3),
H_0=(B+1)/(B+3), H_1=B/(B+2).                       (5.1)
```

The accepted suffix-two support has precisely the three exceptional reset
basins `(1,1,B)`, `(2,B)`, and `(1,B+1)`.  Replacing their scalar current
means by the full current polynomials gives

```text
R_2=q(H_0-5q/9-q/(3y))
 +E(3U^2-q)^2/27
 +E(3U^2+6U-4q)^2/54
 +E(y(1-U^2)-q)^2/(6y).                            (5.2)
```

The first term is the accepted ordinary-basin trace bound.  The denominators
in the three squares follow independently from the accepted normalized
capacities `1/3`, `2/3`, and `2/(3y)`.

The sole height-one group is `(1,B+1)`, has exterior `1/3`, degree two, and
retains observations `0,1`.  Its suffix-zero children have constant feature
norm at most `1-y`, hence

```text
D_0=[E(L_(2,0)^2)/E L_(2,0)
    +E(L_(2,1)^2)/E L_(2,1)](1-y)/3.               (5.3)
```

The unary height-two group has exterior `2/3`.  Its retained observation
changes the beta law to `mu_1=Beta(D,k-D+1)`, with `p_1=D/(k+1)`.  Applying
the accepted actual suffix-one feature before the outer likelihood gives

```text
W_1<=(1-p_1)b(H_1-b/2)
     +E_mu1[(1-U)(U-b/2)^2]
     +E_mu1[(1-U)^3](1-y)/(1-p_1).                 (5.4)
```

The three terms are respectively the weighted ordinary reset coordinates,
the weighted exceptional coordinate, and the weighted suffix-zero
descendant.  Thus

```text
S_a<=Sbar_(B,d,a)=R_2+D_0+(2/3)W_1.                (5.5)
```

This is a trace envelope for the actual history, not M117's scalar `F`, a
generic operator bound, or a diagonal-mode deletion.

At `(B,d,a)=(3,20,19)`, independent exact integration gives

```text
R_2=24302327/19673280,
D_0=511/14400,
W_1=3257413/34500000,
Sbar=10249528643/7684875000>1.                     (5.6)
```

Therefore this displayed envelope cannot be capped by one.  As M185
correctly emphasizes, (5.6) is not an exact-child counterexample and does
not refute a sharper `S_a<=1` theorem by another method.

At `B=1`, the height-one target is rank one and its displayed term vanishes
because `y=1`; the unary child is the accepted inactive suffix-one history.
Removing inactive coordinates can only reduce the nonnegative nominal
envelope.  The clean-room nominal row is `2957/23040`.  Thus M185's separate
`B=1` wording is valid and is not an application of a generic active-rank
formula.

## 6. Exterior and endpoint audit

Let `n=L-3`, `r=d-1`.  Direct cancellation of the grouped root mass

```text
w_(B+3)c(n,r)/[(r+1)!w_(B+L+1)]
```

against the child/parent split ratio gives

```text
eta^(3)_(n,r)=(3/2)c(n,r)/[(r+1)!w_(n+4)].         (6.1)
```

There is no observation or survival factor in `eta`; those are already in
the branch matrix.  At `n=0`, only `r=0,d=1` occurs and

```text
eta=(3/2)/w_4=9/16.                                (6.2)
```

For `n>=1`, `r=1,...,n`.  Including `r=n` with `c(n,n)=1`, the binomial
composition identity yields

```text
sum_(r=1)^n(r+1)eta^(3)_(n,r)
 =(3/2)(n+1)^n(n+2)(n+3)/(n+4)^(n+2).              (6.3)
```

The independent exact values at `n=1,2,5` are respectively
`36/125`, `5/24`, and `896/6561`.  The `n=0`, `r=n`, and `B=1` boundaries
all pass.  No sector budget is inferred from these moments.

## 7. Numbered objections and disposition

1. **Material objections: none.**  The exact branch, `2/3` refutation,
   universal `3/4` theorem, history trace envelope, exact `>1` obstruction,
   exterior, and stated boundary cases all pass independent derivation.
2. **Nonmaterial reproducibility note:** M185's compact checker audits only
   named rational rows and does not regenerate its universal Bernstein
   lists.  M190's separate clean-room symbolic derivation regenerates the
   determinant from beta moments and matches every displayed list exactly;
   no theorem correction is required.
3. **Scope guard:** `Sbar>1` refutes only the route `Sbar<=1`, not the exact
   child inequality `S_a<=1`.  M185 states this distinction correctly.
4. **Scope guard:** the accepted result is a strict reduction, not an `h=3`
   sector bound.  It gives no parent reset, `h>=4`, total AMV, gap, or
   Terminal conclusion.

```text
FINAL REFEREE VERDICT: ACCEPT FROZEN M185'S STRICT h=3 REDUCTION.
```

## 8. Reproducibility

From this directory run

```text
python3 -B independent_exact.py --output independent_results.json
python3 -B symbolic_certificate.py --output symbolic_results.json
```

The first checker uses only Python standard-library `Fraction`, imports no
M185 code or data, and audits the decisive matrix, trace, exterior, killed,
and boundary rows.  The second uses SymPy 1.12 for an exact symbolic
derivation of the beta moments, all Sylvester minors, and every Bernstein
coefficient.  It imports no M185 artifact.  Both use `seed=null`; neither
enumerates `L=7`, a state graph, or any wider sector.
