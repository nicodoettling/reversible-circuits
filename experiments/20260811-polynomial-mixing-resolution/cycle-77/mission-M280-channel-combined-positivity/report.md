# M280 report: per-channel recombined positivity

Date: 2026-08-14 UTC.

## 1. Verdict and scope

```text
VERDICT: STRICT EXACT OWNER-CORRELATION REDUCTION; CP UNRESOLVED.

NO EXACT COUNTEREXAMPLE AT THE SOLE NEW FINITE RANK k=11.
CP, OS+, MS, FCL1, EVERY GAP/MIXING CLAIM, AND TERMINALS REMAIN OPEN.
```

Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, odd `k>=3`, and
`n=3k`.  This mission concerns only the first separated fixed cell of the
auxiliary uniform minimal length-`n-1` factorization law of the long cycle
under M73's nonlazy cyclic rank-two quotient kernel.  It is not the global
identity-word law and not the lazy exact same-product `{3,4,5}` heat-bath
chain.

All required M161/M166, M168/M171, M174/M178, M266/M268, and M274/M277
inventories pass.  Their checksum-file digests are retained in
`checkpoint.md`.

## 2. Exact per-channel formula

Let `eta_j=H_(j,B)-H_(j,A)` be the normalized M91 source difference in
literal channel `j=1,2`.  For target lag `ell=y+1`, let the residual owners,
rooted-tree coefficients, and circular correlations be

```text
chi_a^s(r)=1[s(r+1)=r+1 and r in C_a],

kappa_aa=tau(d_a-2)/tau(d_a),
kappa_ab=tau(d_a-1)tau(d_b-1)/[tau(d_a)tau(d_b)]  (a!=b),

C_ab^s(ell)=sum_r chi_a^s(r)chi_b^s(r+ell),
F_ell(s)=sum_(a,b)kappa_ab(s)C_ab^s(ell).
```

Same-owner phases retain their literal `IS/IN` classification and
distinct-owner phases are `X`; the outer channel law retains `T/D`.
M161/M166 and M261/M264 give the exact identity

```text
CP_j(k,y)=Lambda_n/[(n-3)(n-4)] * eta_j(F_ell),
Lambda_n=(n-2)(1-2/n)^(-(n-3)).                    (CP-OCI)
```

`channel_positivity_reduction.md` displays the equivalent complete M91 Abel
gradient-plus-embedding formula and the two direct ordered-factor formulas.
In each representation, Borel normalizations, both lag endpoints, every
cyclic phase, both intermediate kinds, collisions, and all `IS/IN/X`
topologies are combined before the sign is requested.

The positive prefactor makes CP equivalent to the first standalone
owner-correlation inequalities

```text
(OCI) eta_j(F_ell)>=0
      for j=1,2, odd k>=3, 2<=ell<=n-2.
```

Reflection is statewise and channelwise:

```text
F_ell=F_(n-ell),
CP_j(k,y)=CP_j(k,n-2-y).
```

## 3. Exact collision/decorated form and analytic obstruction

With M261's collision profile `I_ell` and exact decorated owner-ratio profile
`Q_ell`, the centered channel identities are

```text
e^2 eta_1(F_ell)=eta_1(I_ell)+eta_1(Q_ell),

e^2 eta_2(F_ell)=2theta_k+eta_2(I_ell)+eta_2(Q_ell),

theta_k=6(k-1)/[k(2k-3)(2k-1)]>0.
```

These are exact; collision and decoration cannot be signed separately.
Channel one has no kind-transfer baseline because it always produces a
double.  Channel two's positive triangle transfer does not dominate its
signed collision/decorated remainder by any proved inequality.

M272/M276's monotone `q`-to-`p` coupling can be applied to `F_ell`, but it
only gives

```text
eta_j(F_ell)=E_j[F_ell(X_T)-F_ell(Y_S)].
```

It gives no pathwise response order.  Frozen M274/M277 already refutes the
stronger adjacent/embedding MON order, scalar-response FOSD, and literal
raw ordered-atom positivity.  Therefore neither the coupling nor the
positive channel-two kind transfer proves OCI.  The analytic sign attempt
stops exactly at the two displayed collision/decorated lower bounds.

## 4. Exact implication hierarchy

The source-independent masses `alpha_1,alpha_2` are positive and

```text
z_k(y)=alpha_1 CP_1(k,y)+alpha_2 CP_2(k,y).
```

Consequently

```text
CP_1,CP_2>=0 pointwise
 => OS+: z_k(y)>=0 pointwise
 => MS: k min(P_k,N_k)=0
 => FCL1, using proved PCS.
```

Only the last arrow uses M266/M268's accepted PCS estimate, through

```text
sum_y|kz_k(y)|
 =k|sum_y z_k(y)|+2k min(P_k,N_k).
```

The weakest retained fallback after CP is the cross-channel negative-mass
bound

```text
k sum_y[-alpha_1 CP_1(k,y)-alpha_2 CP_2(k,y)]_+=O(1),
```

or the symmetric MS statement.  It permits cancellation between the two
channels and is strictly weaker than CP.

## 5. Sole new exact falsifier: k=11

The predeclared checker used exactly `k=11`, `n=33`, all 30 lags
`ell=2,...,31`, and both channels.  It enumerated 11,550 source-accessible
products for `A` and 25,675 for `B`, using exact `Fraction` arithmetic.  It
verified source/channel normalization,

```text
(alpha_0,alpha_1,alpha_2)=(3/29,40/87,38/87),
```

the six-part `T/D` by `IS/IN/X` reconstruction, full-score normalization,
channelwise reflection, and endpoint equality.

All 60 channel-lag values are strictly positive.  The minima are attained
at the reflected pair `y=9,22`:

```text
min_y CP_1(11,y) approximately 0.002786501098849474,
min_y CP_2(11,y) approximately 0.005795799558859083.
```

The weighted full score has minimum approximately `0.003812648588397978`
at the same reflected pair.  The exact phase total gives

```text
11 sum_y z_11(y) approximately 1.977150808658905,
```

agreeing with frozen M168's floating calibration
`1.977150808662763` to its displayed precision.

This positive result is not termwise.  In the retained six-part table:

- channel-one `D_IS` is negative at all 30 lags;
- channel-two `D_IS` is negative at all 30 lags;
- channel-one `D_IN` is negative at 20 lags and positive at 10;
- channel-two `T_IS`, `T_IN`, and `D_IN` also change sign;
- the full response becomes positive only after within-channel
  kind/topology recombination.

Thus `k=11` supplies no counterexample but also no proof mechanism.  No
other new finite rank was run.

## 6. Status and final action

```text
source inventories and M277 corrections                 verified
literal CP raw/Abel/owner-correlation equivalence       proved exact
channelwise reflection and endpoint accounting          proved exact
CP => OS+ => MS => FCL1 given PCS                       proved implication
k=11 channel positivity                                exact finite only
CP / OCI                                                unresolved
OS+, MS, FCL1                                           unresolved
later cells, direct L1/H0, gap, mixing, Terminals       no inference
```

**Final action:** freeze the exact owner-correlation reduction and its
collision/decorated form for a fresh independent audit.  Retain CP as open;
do not promote the finite positivity to OS+, MS, or FCL1.
