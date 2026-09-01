# M302 Independent Proof Audit of M297

Date: 2026-08-14 UTC

## Verdict and exact scope

```text
ACCEPT M297 AS FROZEN AT STRICT REDUCTION-ONLY SCOPE.
MATERIAL OBJECTIONS: ZERO.
NONMATERIAL OBJECTIONS: TWO NOTATION CLARIFICATIONS.
```

The setting is odd `k>=3`, `n=3k`, the complete centered first-pair law in
the auxiliary uniform minimal-factorization model, and derivatives
`2<=ell<=n-3`, under `(pq)(x)=p(q(x))`.  It is not the uniform identity-word
target or the lazy exact same-product `{3,4,5}` heat-bath chain.

The accepted upstream input is M290/M293's `DOR <=> BODT`.  This audit
accepts only M297's further `BODT <=> SODT <=> SOCT` reduction.  The first
equivalence is modulo a proved `O(1/k)` vector and the second is an exact
scalar expansion.  SOCL is not proved.

## 1. Anchor collapse

M290/M293's accepted positive-composition formula is

```text
(1/3) sum_(r,g) omega(s_T(r,g)) D_T(g,ell)
+(1/4) sum_(r,g) [omega(s_S(r,g)) D_S(g,ell)
                  +omega(s_N(r,g)) D_N(g,ell)].
```

Translation of the support anchor `r` changes neither owner sizes nor a
circular correlation.  The boundary predicate and `D_K(g,ell)` are therefore
independent of `r`, so the `r`-sum may be absorbed into `Omega_K(g)` before
any lag norm.  The factors stay exactly `1/3` for triangles and `1/4` over
the combined `S/N` representations.  No extra factor `n` appears.
Proposition 1 is exact.

## 2. Complete large-owner remainder

Put `h_0=(k-1)/2` and split the three owners as

```text
S={i:d_i<=h_0},       L={i:d_i>=h_0+1},
U=U_S+U_L.
```

After expanding the accepted defect field, the derivative of `Q-Q^S` is the
derivative of

```text
-Corr(U_L,B)-Corr(B,U_L)
+Corr(U_S,U_L)+Corr(U_L,U_S)+Corr(U_L,U_L)
+e^2 sum_(i in L) delta_(d_i) Corr(chi_i,chi_i),
```

up to a lag-constant term.  Both orientations of every
`U_small/U_large` cross-correlation are present; no large-owner term is
discarded.

There are three residual owners.  For each large owner,
`d_i>=(k+1)/2`, while

```text
u_(d_i)<=4/d_i,       TV_circ(chi_i)<=4,
||chi_i||_1<=d_i.
```

Consequently

```text
TV_circ(U_L)=O(1/k),
||U_L||_1<=12,        ||U_S||_1<=12,       ||B||_1<=4.
```

The correlation inequalities

```text
TV Corr(f,g)<=||f||_1 TV(g),
TV Corr(f,g)<=TV(f)||g||_1
```

give `O(1/k)` variation for both `U_L/B` terms, both cross orientations,
and `U_L/U_L`.  If `d_i>=3`, a large diagonal term is at most

```text
C d_i^(-2) TV Corr(chi_i,chi_i)
 <=C d_i^(-2)(4d_i)=O(1/k).
```

For the only exceptional large size, `d_i=2` (possible at `k=3`), the owner
has at most one generic position, so its nonzero-lag self-correlation and
every target derivative vanish.  Restricting circular variation to target
lags cannot increase the estimate.

This statewise bound is applied only to the complete signed coefficient
`omega=P_B-P_A`.  Since `sum_s|omega(s)|<=2`, the combined boundary
remainder is `O(1/k)`.  This proves both directions of
`BODT <=> SODT`, without absolute values between source channels, outer
kinds, or owner incidences.

## 3. Exact scalar expansion

Expanding `U_S=sum_i u_(d_i)chi_i` gives, with ordered `i!=j` pairs,

```text
-sum_d u_d Delta H_d
+sum_(d,e)u_d u_e Delta C^off_(d,e)
+sum_d(u_d^2+e^2 delta_d)Delta A_d.
```

The signs are correct.  `H_d` contains both `chi_i/B` orientations;
`C^off_(d,e)` contains ordered distinct-owner pairs, so no factor two is
missing when `d=e`; and `A_d` is exactly the same-owner diagonal.  Any
indexed small owner already implies the boundary predicate, so a separate
boundary indicator is redundant.  Every row uses the already-collapsed
signed `Omega_K`.  Proposition 3 and `SODT <=> SOCT` are exact.

## 4. Sizes one, two, and three

- `d=1`: no generic position exists, so `chi_i=0`.  Hence `H_1`, `A_1`,
  and every cross row with an index one vanish.
- `d=2`: at most one generic position exists.  Thus `Delta A_2=0` on the
  target range, including the `delta_2=-1` correction.  First-order `H_2`
  and distinct-owner cross rows remain.
- `d=3`: a one-run owner has two consecutive generic positions and a two-run
  owner at most one.  Its autocorrelation is supported at circular lags
  `0,1,n-1`; both entries of a target difference lie in `2,...,n-2`.
  Thus `Delta A_3=0`, while `H_3` and cross rows remain.

These conventions include the minimal rank `k=3`.

## 5. SOCL suffices but is unproved

Let `b_d=e^(-d)d^(d-1)/d!`; `sum_d b_d<infinity`.  Under SOCL:

1. The `H` sum starts effectively at `d=2`, and
   `|u_d|d b_d/k<=4b_d/k`.
2. Cross rows with a size-one index vanish.  For `d,e>=2`,
   `|u_du_e|de b_db_e/k<=16b_db_e/k`.
3. Self rows through `d=3` vanish.  For `d>=4`,
   `|u_d^2+e^2delta_d|d^2b_d/k<=Cb_d/k`.

Summing uses `sum b_d<infinity` and its square, uniformly in the truncated
range `d,e<=h_0`.  SOCL therefore implies `||W||_1=O(1/k)` and hence SOCT,
BODT, and DOR through accepted reductions.  This implication does not prove
SOCL.

## 6. Numbered objections and firewall

1. **Material objections:** none.
2. **Nonmaterial notation clarification:** `u_1=e tau(0)/tau(1)-1` is not
   defined by the generic displayed formula.  All size-one rows are zero, so
   setting `u_1=0` (or any finite formal value) makes the equations literal.
   M297's controlling addendum states this substance.
3. **Nonmaterial bookkeeping clarification:** displayed `Q^S` omits the
   entire lag-constant term `2 sum_x U(x)`.  Thus `Q-Q^S` contains that full
   constant, not merely `2 sum_x U_L(x)`.  Its derivative is zero, so no
   bound or conclusion changes.
4. **Downstream firewall:** this acceptance does not prove SOCL, BODT/DOR,
   PBV/FD, FCL1, any bridge or local-chain gap, polynomial mixing, or a
   Terminal.

No new finite checker was needed.  M297's frozen `k=9` data remain finite
calibration only and were not used to accept an asymptotic claim.

