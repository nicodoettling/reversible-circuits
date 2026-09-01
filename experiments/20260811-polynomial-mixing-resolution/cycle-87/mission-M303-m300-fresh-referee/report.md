# M303 fresh immutable referee report on M300

Date: 2026-08-14 UTC.

## Verdict

```text
ACCEPT M300'S DESIGNATED CHANNEL-ONE DISINTEGRATION, ODD-MIDDLE
CUT PARTITION, COMPLETE EXTERIOR HAHN SUPPORT, AND EXACT EHA_1 IDENTITY.

MATERIAL OBJECTIONS: ZERO.
NONMATERIAL OBJECTIONS: ZERO.

MCLP_1, GOCI_1, GOCI_2, OCI/CP, OS+, MS, FCL1, EVERY GAP OR MIXING
CLAIM, AND BOTH TERMINALS REMAIN UNRESOLVED.
```

The accepted result concerns only the first separated fixed cell of the
auxiliary uniform minimal-factorization law of the long cycle under the
nonlazy cyclic rank-two quotient kernel.  It is not a result about the
global fixed-length uniform identity-word law or the lazy exact same-product
`{3,4,5}` heat-bath chain.

## 1. Immutable source gate

M300's supplied checksum-file digest is exactly

```text
24964f0c5c8e8588715a98fc22a80d7b268b8e6abe683bd95772f51acecbebc8.
```

Every one of its fourteen listed payloads passes.  The eight cited
M274/M277, M280/M283, M285/M287, and M295/M298 top digests all match
M300's dependency audit, and every entry in all eight inventories passes.
Inspection of the controlling proof/referee passages confirms that M300
imports only accepted exact formulas and named refutations; no predecessor
sign or downstream conclusion is imported.

## 2. Disintegration and normalization

Direct expansion of the normalized merged and split channel-one laws proves

```text
eta_1(G)=sum_f nu_M(f)sum_e gamma_k(e)G(ef),
gamma_k=nu_L-(nu_C-+nu_C+)/2,
sum_e gamma_k(e)=0.
```

The split-side `1/2` is exactly the fair exterior-component choice.  The
two commuting exterior/middle color orders have already been conditioned
and summed, so no further `1/2` occurs.  On this designated support the
double `ef` uniquely recovers its exterior and middle cycles, making
`beta_1(ef)=gamma_k(e)nu_M(f)` a valid shorthand.  It must not be read as an
unrestricted ordered-lift formula: a generic double has two raw ordered
lifts.  M300 states this qualifier correctly.

## 3. Middle partition and complete Hahn support

For odd `k`, every unordered middle chord has exactly one representation

```text
{m_a,m_(a+u)},  a in Z/kZ, 1<=u<k/2.
```

Each class contains `k` chords of common positive mass `v_k(u)`, and
`sum_u k v_k(u)=1`.  This proves M300's exact phase-class decomposition and
the implication `MCLP_1 => GOCI_1`; it does not prove MCLP_1.

At exterior cut `c`, the odd `D=2k-1` cycle has `2c` cross-block chords and
`D-2c` internal chords, plus the split-only seam chord `{0,c}`.  Their
gamma coefficients are respectively

```text
v_D(c)>0,
v_D(c)-v_k(c)/2<0,
-v_k(c)/2<0.
```

The strict internal sign follows for every `1<=c<=k-1` from the strict
decrease of `tau(d-1)/tau(d)`.  The classification is exhaustive and has
exactly `k(k-1)` chords of each sign.  No support or endpoint is omitted.

## 4. Exact Hahn--Abel identity

Independent collection confirms

```text
x_c=2c v_D(c),
y_c=(D-2c)(v_k(c)/2-v_D(c))+v_k(c)/2>0,
r_c=x_c-y_c=Dv_D(c)-(k-c)v_k(c).
```

Odd-cycle normalization gives `sum_c Dv_D(c)=1`, while pairing `c` with
`k-c` gives `sum_c(k-c)v_k(c)=1`.  Hence `R_(k-1)=0`.  Discrete summation by
parts then gives exactly

```text
P=sum_(c=1)^(k-1)y_c(Xbar_c-Ybar_c)
  +sum_(c=1)^(k-2)R_c(Xbar_c-Xbar_(c+1)).
```

The first and final endpoints, every negative internal/seam mass, and lag
reflection are retained.  This is an identity, not a positivity proof.

## 5. Independent exact `k=7` audit

The sole clean-room reconstruction uses standard-library `Fraction`
arithmetic, imports no project or predecessor code/data, and evaluates only
`k=7`, `n=21`.  It reproduces:

- all 54 middle-class/lag cells strictly positive;
- exactly 44 negative fixed-middle cells among 378;
- the exact class minimum at `u=2`, `ell=6,15`;
- the exact fixed-middle minimum at `u=2`, phase `6`, `f=(8,13)`,
  `ell=8,13`;
- all 18 fully weighted channel-one lags strictly positive, with minimum at
  `ell=8,13` approximately `0.02016735366799382`;
- exact reflection and direct-versus-class reconstruction;
- all 54 exact EHA_1 equalities;
- common denominator `2316987672506143` and the exact reported `r_c,R_c`
  numerators.

The finite cumulative coefficient signs are

```text
R_1,R_2,R_3<0;  R_4,R_5>0;  R_6=0.
```

This mixed sign is a strict `k=7` coefficient fact only.  It rules out a
certificate that requires all `R_c` to share one sign at that rank.  It does
not refute MCLP_1, imply any response order, or establish an all-rank sign
pattern.  Likewise, the 54/378 facts have no all-rank implication.

## 6. Numbered objections and mandatory interpretations

1. **Material objections: none.**
2. **Nonmaterial objections: none.**
3. **Designated-lift interpretation:** retain M300's exterior/middle-role
   qualifier whenever using scalar `beta_1(ef)` shorthand.
4. **Finite-scope interpretation:** retain `k=7` on the mixed-`R_c`, 54/54
   positive class-cell, and 44/378 negative fixed-middle statements.
5. **Identity-only interpretation:** EHA_1 reduces MCLP_1 to one combined
   scalar inequality but supplies no sign for either displayed block.
6. **Downstream firewall:** no MCLP/GOCI/OCI/CP/MS/FCL1, spectral-gap,
   mixing, or Terminal inference is accepted.

Items 3--6 are mandatory readings already present in M300, not defects.

## 7. Final status ledger

```text
M300 inventory and eight cited predecessor inventories       verified
designated atom-summed channel-one disintegration            proved exact
no-extra-1/2 and ordered-lift qualifier                       proved exact
odd-k middle cut-length phase partition                       proved exact
complete exterior gamma Hahn support and equal sign counts    proved exact
x_c,y_c,r_c,R_c formulas and EHA_1 endpoints                 proved exact
k=7 R_c mixed sign                                            exact finite only
k=7 54/54 positive class cells and 44/378 fixed negatives     exact finite only
MCLP_1 / GOCI_1 / GOCI_2                                     unresolved
OCI/CP, OS+, MS, FCL1                                         unresolved
gap, mixing, Terminals                                        no inference
```

Final action: **ACCEPT AND FREEZE M300 with zero substantive objections.**
