# M298 clean-room proof audit of M295

Date: 2026-08-14 UTC.

Verdict on the mathematical package: **ACCEPT**, subject to the single
nonmaterial notation qualification in Section 7.

## 1. Scope and convention

Use `(pq)(x)=p(q(x))`, with displayed factors multiplied left-to-right.
Fix odd `k>=3`, put `n=3k`, and use lags `2<=ell<=n-2`.  Define

```text
L=(1,...,k-1,2k,...,3k-1),       M=(k,...,2k-1),
C_-=(0,...,k-1),                 C_+=(2k,...,3k-1).
```

For a directed `d`-cycle `C`, its first-chord law is

```text
nu_C(e)=tau(u)tau(d-u)/[(d-1)tau(d)],
tau(d)=d^(d-2)/(d-1)!.
```

Every such law has exact mass one.

## 2. Channel-one factorization and the collision guard

Every channel-one atom has an exterior chord `e` from one of `L,C_-,C_+`
and a middle chord `f` from `M`.  Their vertex supports are disjoint, so
`ef` is a double.  Moreover its two transposition cycles recover the unique
middle chord and the unique exterior chord.  Thus the designated map

```text
(e,f) -> ef
```

is injective on the channel-one atom support.  Combining the three possible
exterior laws first gives

```text
gamma(e)=nu_L(e)
 -1/2 1[e in T(C_-)]nu_(C_-)(e)
 -1/2 1[e in T(C_+)]nu_(C_+)(e),

beta_1(ef)=gamma(e)nu_M(f),        sum_e gamma(e)=0.          (2.1)
```

Unrestricted rank-two products do have multiple ordered lifts: three for a
triangle and two for a double.  That fact does not contradict `(2.1)`,
which is a designated exterior/middle disintegration.  Even without using
injectivity, summing the atoms first proves the always-safe identity

```text
eta_1(F_ell)
 =sum_(f in T(M))nu_M(f) sum_e gamma(e)F_ell(ef).             (2.2)
```

Consequently, if every fixed-middle sum

```text
S_(k,ell)(f)=sum_e gamma(e)F_ell(ef)
```

were nonnegative, then `(GOCI_1)` would follow.  This is precisely the
proposed `FMCP_1` statement.

## 3. Direct residual response and repaired autocorrelation

For `s=ef`, let `q_s=s^-1h` have residual owners of sizes `d_a`.  A cyclic
phase `x` is generic for owner `a` when the head `x+1` is fixed by `s` and
the tail `x` belongs to owner `a`.  Write its indicator as `chi_a(x)` and

```text
a_d=tau(d-1)/tau(d),
b_d=tau(d-2)/tau(d),
delta_d=b_d-a_d^2.
```

The literal completion response is

```text
F_ell(s)=sum_(a,b) kappa_ab sum_x chi_a(x)chi_b(x+ell),
kappa_aa=b_(d_a),  kappa_ab=a_(d_a)a_(d_b) for a!=b.         (3.1)
```

If `A_s(x)=a_(d_a)chi_a(x)`, expanding `(3.1)` gives

```text
F_ell(s)=sum_x A_s(x)A_s(x+ell)
 +sum_a delta_(d_a)sum_x chi_a(x)chi_a(x+ell).               (3.2)
```

Log-convexity of `tau` gives `delta_d>=0` for `d>=3`.  At `d=2`,
`delta_2=-1`, but that owner has at most one generic phase, so its nonzero-lag
autocorrelation vanishes.  Deleting only this term therefore preserves
equality throughout the admissible lag range and leaves a nonnegative
statewise repaired autocorrelation.

The independent checker evaluates `(3.1)` from residual permutation cycles
and `(3.2)` from scalar owner fields.  It verifies 4,800 exact admissible
state/lag equalities at `k=5`.

## 4. Positive cyclic-composition normalization

For an anchor `r` and positive cyclic gaps, the supported forms are

```text
T: (v_0,v_1,v_2),
S: (v_0,v_1)(v_2,v_3),
N: (v_0,v_3)(v_1,v_2).
```

An independent full enumeration at `n=15` obtains:

| family | representations | distinct states | multiplicity | normalization |
|---|---:|---:|---:|---:|
| forward triangles | 1,365 | 455 | 3 | `1/3` |
| combined `S/N` doubles | 10,920 | 2,730 | 4 | `1/4` |

At every representation, `r=v_0` is already one of the support vertices.
It is not an independent phase and therefore contributes no extra factor
`n`.  For each of the 400 channel-one states, all four anchored interval
owner reconstructions equal the direct residual-cycle response at every
circular lag; averaging them with `1/4` reproduces one state exactly.

This supplies 24,000 exact anchored response checks.  It also confirms that
the fixed-middle calculation contains doubles only; the `1/3` triangle
normalization is a convention guard for the full accepted formula.

## 5. No extra channel-two half

As an independent convention check, enumerate every ordered rank-two
transposition product in `S_15` and weight a state `s` by

```text
a(s) F_6(s^-1Q)/F_8(Q).
```

There are 5,005 distinct rank-two products with lift count two or three.
For both the merged nine-cycle source and the split pair of five-cycles,
the total normalized mass is exactly one.  On the split source, the first
factor lies in the two exterior components with masses exactly

```text
1/2, 1/2.
```

Thus the full two-cycle denominator already includes the fair component
choice.  Multiplying the split channel by another `1/2` would give mass
`1/2`, so M295 correctly inserts no such factor.

## 6. Exact `k=5` result

The clean-room calculation tests the sole rank `k=5`, all twelve admissible
lags, and all ten middle chords.  Of the 120 fixed-middle cells, exactly 16
are negative.  The minimum is attained exactly at the reflected pair

```text
f=(6,9),  ell=6 and ell=9,
```

with value

```text
-779985545058827083283361063988362608513
/11367752922135489592720891699200000000000.          (6.1)
```

Therefore universal `FMCP_1` is refuted.

For every one of the twelve lags, however, the complete middle-weighted
quantity in `(2.2)` is strictly positive.  Three independent constructions
agree exactly lag by lag:

```text
direct residual cycles
= repaired owner autocorrelations
= 1/4 times the complete anchored S/N composition sum.
```

The fully scaled minimum is

```text
alpha_1 CP_1 minimum
=469380953030255528575240193615921483304253622141733093283
 /62593163860600167157006651607817304625660070187459136716800,
```

using

```text
alpha_1=16/33,
Lambda_15=129746337890625/1792160394037,
R_15=132.
```

It equals the accepted M274/M277 finite value.  Post-hoc comparison with
frozen M295 matches all 120 cells, all twelve unscaled `eta_1` lags, and all
twelve scaled values, not merely the minimum.

Thus `(6.1)` is not a `GOCI_1` or `OCI_1` counterexample.  It shows exactly
that the proposed proof must retain cancellation across middle-chord atoms.

## 7. Numbered objections

### Material objections

1. **None.**  The mathematical result, exact witness, counts,
   normalizations, and scope firewall are correct.

### Nonmaterial objections

1. **Scalar-beta shorthand needs its designated-role qualifier.**  The
   phrase `beta_1(ef)=gamma(e)nu_M(f)` is exact in the declared channel-one
   support because `e` is the unique exterior cycle and `f` the unique
   middle cycle.  Read as a statement about unrestricted rank-two ordered
   lifts, it would suppress the usual double/triangle multiplicities.  M295's
   proof supplies the needed disjoint-support explanation, so this is a
   notation qualification, not a correction to any equation or result.

## 8. Exact stop

**Refuted:** `FMCP_1` only.

**Unresolved:** `GOCI_1`, `GOCI_2`, `OCI`, `CP`, `OS+`, `MS`, `FCL1`, FD,
all bridge and local gaps, polynomial mixing, and both Terminals.  No claim
here changes the status of the main heat-bath chain.
