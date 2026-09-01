# M303 independent reconstruction of M300

Date: 2026-08-14 UTC.

## 1. Scope and immutable provenance

This audit uses `(pq)(x)=p(q(x))`, odd `k>=3`, `n=3k`, and only the
designated channel-one coefficient of the first separated fixed cell in the
auxiliary minimal long-cycle factorization calculation.  It is not a claim
about the global identity-word law or the lazy exact same-product
`{3,4,5}` heat-bath chain.

M300's top digest is exactly

```text
24964f0c5c8e8588715a98fc22a80d7b268b8e6abe683bd95772f51acecbebc8,
```

and all fourteen inventoried payloads pass.  All entries in the cited frozen
M274/M277, M280/M283, M285/M287, and M295/M298 inventories also pass, with
the exact top digests recorded by M300.  Their controlling reports support
only the inputs M300 imports: normalized channel laws, the owner response and
reflection, the three/four lift multiplicities, the lack of a channel-two
extra half, the designated channel-one disintegration, and the exact
fixed-middle refutation.  No predecessor sign or downstream theorem is
imported.

## 2. Designated channel-one disintegration

The merged channel-one law draws one exterior chord from `L` and one
independent middle chord from `M`.  The split law chooses `C_-` or `C_+`
fairly, then draws its exterior chord and an independent middle chord.
Therefore direct expansion against any test function gives

```text
eta_1(G)=sum_(f in T(M))nu_M(f) sum_e gamma_k(e)G(ef),

gamma_k(e)=nu_L(e)
 -1/2 1[e in T(C_-)]nu_(C_-)(e)
 -1/2 1[e in T(C_+)]nu_(C_+)(e).
```

Every constituent law has mass one, hence `sum_e gamma_k(e)=0`.  The two raw
color orders commute and are already summed in the normalized conditional
law, so there is no extra `1/2`.  On this declared atom support, `ef` is a
double whose middle cycle uniquely identifies `f` and whose other cycle
identifies `e`.  Thus `beta_1(ef)=gamma_k(e)nu_M(f)` is exact only as a
designated-role shorthand.  An unrestricted double still has two ordered
transposition lifts.  The atom-summed identity above is the collision-safe
statement.

## 3. Odd middle cut partition

Write the middle vertices as `m_a`, `a in Z/kZ`.  For an unordered pair,
exactly one of the two directed differences lies in
`{1,...,(k-1)/2}` because `k` is odd.  Hence every middle chord has a unique
form

```text
f_(a,u)={m_a,m_(a+u)},  1<=u<k/2.
```

There are `k` chords in each class, each with mass

```text
w_(k,u)=v_k(u)>0,
```

and odd-cycle chord normalization is `sum_u k w_(k,u)=1`.  Grouping the
atom-summed disintegration therefore proves exactly

```text
eta_1(F_ell)=sum_u w_(k,u)P_(k,ell)(u).
```

Thus MCLP_1 would imply GOCI_1, but no sign has been established.

## 4. Complete exterior Hahn support

Let `D=2k-1`; the `L` cycle consists of contiguous blocks `A,P` of sizes
`k-1,k`.  For canonical cut `c in {1,...,k-1}`, the `D` cycle chords of
that cut comprise exactly `2c` cross-block chords and `D-2c` internal
chords.  The remaining split-only chord of that cut is `z_c={0,c}`.  Their
coefficients are respectively

```text
v_D(c),
v_D(c)-v_k(c)/2,
-v_k(c)/2.
```

For `r_d=tau(d-1)/tau(d)`, strict log-convexity of `tau` makes `r_d`
strictly decreasing, and cancellation of the common factors gives

```text
2v_D(c)/v_k(c)
 =product_(j=0)^(c-1) r_(D-j)/r_(k-j)<1.
```

This covers every `c`, including `k-1`, so the signs are strict.  There are
`k(k-1)` positive cross chords.  The negative count is

```text
binom(k-1,2)+binom(k,2)+(k-1)=k(k-1),
```

and the support classification is exhaustive.

## 5. Hahn--Abel identity and endpoints

After summing every middle phase, let `Xbar_c` be the uniform mean on the
`2c` cross chords and `Ybar_c` the negative-mass-weighted mean on the
`D-2c` internal chords plus `z_c`.  With

```text
q_c=v_k(c)/2-v_D(c)>0,
x_c=2c v_D(c),
y_c=(D-2c)q_c+v_k(c)/2
   =(k-c)v_k(c)-(D-2c)v_D(c)>0,
r_c=x_c-y_c=Dv_D(c)-(k-c)v_k(c),
R_c=sum_(d<=c)r_d,
```

direct collection first gives

```text
P=sum_c[x_c Xbar_c-y_c Ybar_c]
 =sum_c y_c(Xbar_c-Ybar_c)+sum_c r_c Xbar_c.
```

There are `D` chords of every canonical cut in the odd `D`-cycle, hence
`sum_c Dv_D(c)=1`.  Pairing `c` with `k-c` in the odd `k`-cycle gives
`sum_c(k-c)v_k(c)=1`.  Therefore `R_(k-1)=0`.  Discrete summation by parts,
including the first endpoint and using the vanishing final endpoint, yields

```text
P=sum_(c=1)^(k-1)y_c(Xbar_c-Ybar_c)
  +sum_(c=1)^(k-2)R_c(Xbar_c-Xbar_(c+1)).
```

This is exactly EHA_1.  Symmetry of the accepted owner matrix gives
statewise `F_ell=F_(n-ell)`, so the phase sum and EHA identity retain both
lag endpoints and reflect exactly.  None of these equalities signs the
right-hand side.

## 6. Sole clean-room rank

`independent_audit.py` is a standard-library exact reconstruction that
imports no project or predecessor code/data and evaluates only `k=7`.  It
rebuilds the four chord laws, residual cycles, literal owner response,
middle classes, complete exterior support, and both sides of EHA_1.

The exact output confirms:

- all four chord laws have mass one and `gamma` has mass zero;
- 42 positive cross chords and 42 negative internal/seam chords;
- the three classes partition all 21 middle chords;
- every one of 54 class/lag cells is positive;
- exactly 44 of 378 fixed-middle cells are negative;
- all 18 fully weighted `eta_1` lags are positive;
- direct and cut-class full averages agree at all 18 lags;
- EHA_1 agrees exactly in all 54 class/lag cells;
- state, fixed-cell, class, and full reflection hold.

The exact class minimum is at `u=2`, `ell=6,15`:

```text
18391884160007872512505581390057340062886183764340384475832641580678550316483694546164031922299480179423171
/181211325370827177616731812976270118138716435331141156018616780003928170444373248989640785920000000000000000.
```

The exact fixed-middle minimum is at `u=2`, phase `6`, `f=(8,13)`, and
`ell=8,13`:

```text
-47887190399462218030782332438763438434346238035631961416543569973932853169
/920408972596550617862664784704103676980180079269295528017920000000000000000.
```

The common-denominator numerators of `r_c` and `R_c` are exactly those in
M300.  In particular the finite `k=7` cumulative signs are

```text
R_1,R_2,R_3<0;  R_4,R_5>0;  R_6=0.
```

This is a coefficient fact at one rank.  It prevents a certificate that
requires one common sign for every `R_c` at `k=7`; it does not refute MCLP_1,
prove any response ordering, or establish an all-rank sign pattern.

## 7. Exact stop

The designated disintegration, odd middle partition, complete Hahn support,
and EHA_1 are exact.  MCLP_1 is precisely the nonnegativity of the resulting
combined scalar expression and remains unresolved.  Consequently GOCI_1,
GOCI_2, OCI/CP, OS+, MS, FCL1, every spectral-gap or mixing claim, and both
Terminals remain unresolved.
