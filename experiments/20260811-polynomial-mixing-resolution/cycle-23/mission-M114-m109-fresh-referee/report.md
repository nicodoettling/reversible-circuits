# M114 final fresh referee report on frozen M109

Date: 2026-08-12.  M109 records repository base commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, convention, and scope

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL WORDING CORRECTION: ONE (NM-1 BELOW).
```

The accepted theorem is narrow: for the full nonlazy stationary-flow
parking-degree projection in the minimal long-cycle factorization sector,
the stronger unweighted reset excursion satisfies

```text
H(x)<=q_x(1-q_x)
```

at every active right-heavy context with suffix excess `L=s-B<=2`; hence the
weighted excursion satisfies `G(x)<=U(x)` there.  This is an all-`s`,
all-right-heavy boundary theorem, not an extrapolation from finite ranks.

The project target remains uniform on fixed-length identity words in
`Omega(N,m)`.  Permutations compose as `(pq)(x)=p(q(x))`, and tuple factors
are displayed left-to-right.  The audited object is only an auxiliary
projection.  The global all-`L` excursion, auxiliary `Pbar` gap,
ROOT-MEAN LIFT, original lazy `{3,4,5}` heat-bath gap, polynomial mixing,
Terminal A, and Terminal B remain **unresolved**.

## 2. Frozen provenance and manifest gate

Direct hashes observed before the mathematical audit are:

```text
f68c3211d404d1cf045b101bdea26ccf105f38f708d5bbe0d64f9fb1aa1c6575  report.md
6abb460e61592761bcb9be28095e578e6660138f67bb1ed110772fdca750062b  excursion_reduction.md
5832dedd8ba79d51c93a8e2b2c4cd721851fb73e9e1a9df750c5d6c0296662e3  boundary_exact.py
934fd0d4f87cdb050b5d39c56352ad3d4793a01a43ab671f61f0d1118155fb55  boundary_exact.json
65d0173dbc27df08c6ff653cdbe9e0619f41798a49ec025f3f92a0f0fbc35106  SHA256SUMS
```

They match the assigned frozen values.  The M109 manifest lists every owned
artifact other than itself and verifies without error.  M90/M96's accepted
all-`j` recurrence scope and the accepted M98/M99 and M103/M106 local-route
refutations were read before judging the replacement argument.  No frozen
artifact was edited.

## 3. All-`j` recurrence, reachability, and descent

The Schur transform is exact:

```text
H=A_0+QH,  G=A+QG,
Q(x,y)=rho_s(k,t)nu_(K,R,k)(j),  j=1,...,k.
```

`j=0` and inactive children alone are killed.  Fresh attachment is exactly
uniform, `nu_(1,0,k)(j)=1/(k+1)`.  For every live child
`y=(t-1,K+k,R+j,B)`, positivity of the root group gives

```text
P(x)-P(y)=s-t-k+j+1>=j>=1,
L(x)-L(y)=s-t+1>=1.
```

The reachable closure is preserved and the DAG is finite.  Positivity of the
history expansion also proves `G<=H` because every weighted reset leaf is its
unweighted leaf multiplied by `1-q_leaf in [0,1]`.  These claims are accepted.

## 4. Basin estimate and `L=0,1`

The new estimate

```text
beta_e=rho(B_e)/rho(e)<=degree(e)
```

is correct.  It follows from `c(A,p)/w_A<=p` and the telescoping bound

```text
sum_(p>=1) p ell!/(p+ell)!<=sum_(p>=1)p/(p+1)!=1.
```

At `L=0`, the basin-height expectation gives
`H<=q^2(s-1)/(s+1)<=q(1-q)`.  At `L=1`, the two supported compositions,
the exceptional singleton basin, and the unary terminal descendant reduce
to M109's convex quadratic; both endpoints are nonpositive.  The `s=2`
case is correctly separated: all would-be reset/deep targets are inactive
and `H=0`.

## 5. `L=2` support, basin, and descendant accounting

The four supported compositions and their masses/means are exactly

```text
(2,B)       q/3       2z
(1,1,B)     q/9       3d
(1,s-1)     q/(3v)    v(1-d)
(s)         r         a(1-z).
```

Their mean is `q`.  Their exceptional path-mass accounting is
`5q/9+q/(3v)`, and direct current/capacity calculation gives each of the
three square terms in (6.1).  The only possible deep groups are
`(2,s-1)` and `(1,s)`; retaining both `j=1,2` in the first and `j=1` in the
second gives (6.2) exactly.  Thus the complete recursion is bounded by
`H/q<=E_s(z)` with no omitted attachment rank.

**NM-1 (nonmaterial wording correction).** At the boundary `s=3`, the
nominal `(2,s-1)=(2,2)` target has rank `t-1=1` and is inactive, not live and
suffix-terminal.  Here `v=w_1/w_2=1`, so its corresponding term in (6.2) is

```text
(1-d)(1-v)/3=0.
```

Adding this zero charge leaves every formula and the theorem unchanged.
The prose about both children being terminal should be read for `s>=4`.

## 6. Quartic, endpoints, and Bernstein certificates

Fresh symbolic rational algebra reproduces the derivative identity and all
five coefficients of `N_s`.  Since `N_s''>0` and `N_s(0)<0`, `E_s` has no
interior maximum.  Both endpoint slack identities in (6.4) are exact.

The monotonic reductions to `p(u)`, `j(u)`, and `m(u)` are valid.  In
particular, the two derivative brackets are controlled by the exact margins

```text
4u^3+3u^2 <= 931/1024 < 10,
17u^2       <= 833/256  < 20
```

on `u<=7/16`.  Every listed Bernstein coefficient of `p,j,m` is reproduced
and positive.  All 35 coefficients of the seven exact degree-four
certificates for `s=3,...,9` are also reproduced bit-for-bit and positive.
The analytic `s>=10` proof and finite algebraic certificates therefore cover
every `s>=3`.

## 7. Independent computation and exact comparisons

`independent_exact_audit.py` contains no import statement and reads no
predecessor source or output.  It reconstructs custom exact rationals,
ordered compositions, the root law, contextual means, attachment laws,
literal and grouped basin energies, live children, and full resolvents.
The targeted run has zero failures and checks:

- three literal/grouped basin-energy identities;
- fresh and nonfresh attachment rows with all live ranks;
- decisive `L=0,1` cases, including `s=2`;
- five `L=2` cases including `s=3`, `s=9`, and `s=10`;
- the symbolic derivative and endpoint identities;
- all asymptotic and finite Bernstein coefficients; and
- the four frozen complete-resolvent calibrations.

After the fresh run, a read-only comparison established exact fraction
equality for all four calibration ratios, all asymptotic coefficients, and
all 35 finite coefficients.  The calibration ratios are

```text
weighted   (8,1,0,4)   .43715035400213015...
weighted  (11,1,0,5)   .5391499615007582...
unweighted (8,1,0,3)   .6210042669407680...
unweighted(11,1,0,4)   .6947437905621655...
```

The exact output is `independent_exact_audit.json`; computation is
deterministic with `seed=null` and uses no nonstandard package.

## 8. Dependencies, boundaries, and strongest self-attack

- **Accepted inputs:** the M50/M56/M65/M69 composition, contextual, basin,
  and attachment formulas; M76/M79 reachability and reset geometry;
  M82/M87 split bounds and normalization; M90/M96 all-`j` recurrence.
- **Proved and accepted from M109:** strict `L` descent, fresh uniformity,
  `beta_e<=degree(e)`, and unweighted/weighted contraction for right-heavy
  `L<=2`.
- **Accepted refutations respected:** M98/M99 refute universal nonfresh
  one-step positivity; M103/M106 refute universal global two-layer
  positivity.  M109 assumes neither.
- **Unresolved:** the full excursion for arbitrary `L`, beginning at `L=3`,
  and every downstream gap/mixing obligation.

The strongest self-attack is unchanged: the basin bound can be loose, the
envelope has substantially less slack than the exact resolvent, and the
accepted local defects show that no pointwise one- or two-layer induction may
be inserted.  The `L<=2` proof gives no inference for `L>=3`.

The auxiliary theorem has `s>=2`; original-chain cases with odd `m`, `m=0`,
`m=2`, or `N=2` do not enter it and receive no new conclusion.

## 9. Final verdict, artifacts, numbered objections, and hygiene

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CORRECTION NM-1: s=3 inactive zero-charge child wording only.
```

Owned artifacts are `plan.md`, `checkpoint.md`, `proof_audit.md`,
`independent_exact_audit.py`, `independent_exact_audit.json`, this report,
and `SHA256SUMS`.  The principal command is

```text
python3 -B independent_exact_audit.py
```

run from this directory.  JSON parsing, source execution, whitespace checks,
manifest verification, and owned-directory cache hygiene are required at
freeze.  No M109, predecessor, coordinator note, manuscript, project skill,
or shared source was edited.
