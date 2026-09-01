# M285 report: owner-correlation coefficient reduction

Date: 2026-08-14 UTC.

## 1. Verdict and scope

```text
VERDICT: KEEP AND FREEZE A STRICT EXACT GOCI REDUCTION.
SIGNED PSD DOMINANCE: REFUTED BY ONE EXACT k=3 WITNESS.
OCI / CP / OS+ / MS / FCL1: UNRESOLVED.
```

Fix odd `k>=3`, put `n=3k`, and use `(pq)(x)=p(q(x))`, with displayed
factors multiplied left-to-right.  The target is only the first separated
fixed cell of the auxiliary uniform minimal long-cycle factorization law
under the nonlazy cyclic rank-two quotient kernel.  It is not the uniform
identity-word target and not the lazy exact same-product `{3,4,5}` heat-bath
chain.

M280/M283's freshly accepted identity is the starting point:

```text
CP_j(k,y)=Lambda_n/[(n-3)(n-4)] eta_j(F_ell),
ell=y+1,  2<=ell<=n-2,  j=1,2.
```

This mission proves an exact positive-composition coefficient law and a
statewise nonnegative autocorrelation representation for `F_ell`.  It does
not sign the remaining centered channel coefficient.  The first unproved
all-rank statement is `(GOCI_j)` below.

## 2. Immutable provenance gate

Every payload in the exact M280/M283, M91/M94, and M261/M264 inventories
passes.  Their checksum-file digests and payload counts are frozen in
`dependency_audit.md`.  In particular, M280 and M283 have respectively

```text
60afef642d945847db0427f388d1219497416a09c4a955818607f71df87ae0a9
156fa5207e088f38ae71b69e48332a8a708bae8f03f1447c77e9710128572cdf.
```

No predecessor artifact was edited.

## 3. Exact normalized signed coefficients

Let `beta_j(s)` be the mass of a supported pair product `s` under the
normalized conditional `B` law minus its mass under the normalized
conditional `A` law.  With `L,M,C_-,C_+,F=C_-C_+` as in the proof note,

```text
beta_1(s)
 =sum_(ef=s; e in T(L), f in T(M))nu_L(e)nu_M(f)
  -1/2 sum_(C in {C_-,C_+})
        sum_(ef=s; e in T(C), f in T(M))nu_C(e)nu_M(f),

beta_2(s)
 =a(s)[F_(2k-4)(s^-1L)/F_(2k-2)(L)
       -F_(2k-4)(s^-1F)/F_(2k-2)(F)],
```

where `a(s)=3` for a triangle and `a(s)=2` for a double.  Both coefficients
have zero total mass and

```text
eta_j(G)=sum_s beta_j(s)G(s).
```

The `1/2` belongs only to channel one's choice between the two equal exterior
cycles.  In channel two,

```text
F_(2k-2)(F)=(2k-2)! tau(k)^2
```

is the full two-cycle completion count.  Its color interleavings already
make the first exterior component fair.  Multiplying by `a(s)` sums all raw
ordered lifts, so inserting another `1/2` would be an error.

## 4. Exact owner-cycle and phase convolution

For a positive cyclic three-composition `g` and support anchor `r`, the
forward triangle is

```text
s_T=(v_0,v_1,v_2),
```

with residual owner sizes `(g_1,g_2,g_3)`.  For a positive cyclic
four-composition, the two supported double forms are

```text
s_S=(v_0,v_1)(v_2,v_3),    sizes (g_1,g_3,g_2+g_4),
s_N=(v_0,v_3)(v_1,v_2),    sizes (g_2,g_4,g_1+g_3).
```

The owner supports are the explicit intervals/unions in
`coefficient_reduction.md`.  Their overlap convolution is `R_K(g,ell)`.
Exactly,

```text
eta_j(F_ell)
 =1/3 sum_(r,g_1+g_2+g_3=n) beta_j(s_T)R_T(g,ell)
  +1/4 sum_(r,g_1+...+g_4=n)
       [beta_j(s_S)R_S(g,ell)+beta_j(s_N)R_N(g,ell)].
```

The division is exact and has no hidden factor `n`.  Here `r` is a support
vertex: a fixed supported forward triangle has three anchor/composition
representations; a fixed supported double has four, with exactly one `S/N`
representation at each anchor.  Each representation carries the same
actual `beta_j(s)F_ell(s)`, so division by three/four recovers one copy.
The independent target-boundary phase is already summed inside `R_K`.

The outer rows retain triangle/double.  Splitting the interval overlaps by
the literal residual-cycle endpoint order retains same-owner `IS/IN` and
different-owner `X` before their final sum.

## 5. Statewise positive autocorrelation, and its limit

For residual owner size `d`, set

```text
a_d=tau(d-1)/tau(d),
b_d=tau(d-2)/tau(d),
delta_d=b_d-a_d^2.
```

Writing `A_s(x)=a_d` on a generic phase owned by that component and zero on
a support-head phase gives exactly

```text
F_ell(s)=sum_x A_s(x)A_s(x+ell)
          +sum_i delta_(d_i) C_ii^s(ell).
```

The ratio `tau(d)/tau(d-1)=(d/(d-1))^(d-2)` increases with `d`, so
`delta_d>=0` for every `d>=3` and `delta_d=O(d^-2)`.  The sole negative
case is `delta_2=-1`.  A size-two residual owner has at most one generic
phase, hence `C_ii(ell)=0` for every nonzero circular lag.  Deleting that
term changes only lag zero.  Therefore, exactly at every admissible
`2<=ell<=n-2`,

```text
F_ell(s)=sum_x A_s(x)A_s(x+ell)
          +sum_(i:d_i>=3)delta_(d_i)C_ii^s(ell),
```

a sum of nonnegative interval autocorrelations.  The corresponding repaired
full circular sequence has nonnegative Fourier spectrum state by state.

This does not prove OCI: `beta_j` is a centered signed coefficient, so its
expectation is a difference of PSD sequences rather than a positive mixture.
The exact collision/decorated version makes the same remaining sign explicit:

```text
e^2 eta_1(F_ell)=eta_1(I_ell)+eta_1(Q_ell),
e^2 eta_2(F_ell)=2theta_k+eta_2(I_ell)+eta_2(Q_ell),
theta_k=6(k-1)/[k(2k-3)(2k-1)].
```

Neither collision nor the decorated term may be deleted or signed alone.

## 6. Sole predeclared exact falsifier

The checker independently reconstructed both normalized channels at exactly
`k=3`, `n=9`, using standard-library `Fraction` arithmetic and importing no
predecessor code or data.  It verified

```text
(alpha_0,alpha_1,alpha_2)=(1/15,8/15,2/5),
eta_1(T)=0,   eta_2(T)=theta_3=4/15,
```

source normalization, both triangle/double mixtures, reflection, and exact
equality of the literal and repaired owner response at all admissible lags.
The six values for `ell=2,...,7` are, in order,

```text
eta_1(F_ell):
  628141943897/8168202000000,
  120685667401/2042050500000,
  1653138745301/24504606000000,
  1653138745301/24504606000000,
  120685667401/2042050500000,
  628141943897/8168202000000;

eta_2(F_ell):
  131857751173/680683500000,
  769552112923/2722734000000,
  3571902519103/7351381800000,
  3571902519103/7351381800000,
  769552112923/2722734000000,
  131857751173/680683500000.
```

All twelve are strictly positive.  This is exact finite-only evidence and
not an all-rank proof.

Signed spectral dominance nevertheless fails in channel two.  Let

```text
D_2(ell)=eta_2(Ftilde_ell),
M_(ab)=D_2((b-a) mod 9),
v=(10,8,2,-5,-9,-9,-5,2,8).
```

The checker gives the exact certificate

```text
v^T M v=-310962953715709/12252303000000<0.
```

Thus the Cayley/PSD route is refuted, not OCI.  No second rank, scan, or
falsifier was run.

## 7. First unproved inequality and weaker target

The narrow all-rank obligation is:

> **Gapped owner-correlation inequality `(GOCI_j)` (unresolved).**  For
> `j=1,2`, odd `k>=3`, and `2<=ell<=3k-2`, the explicit signed positive-
> composition convolution in Section 4, evaluated on the nonnegative
> response in Section 5, is nonnegative.

Equivalently, the collision/decorated thresholds are

```text
eta_1(I_ell+Q_ell)>=0,
eta_2(I_ell+Q_ell)>=-2theta_k.
```

If channelwise GOCI cannot be proved, the weaker retained target is the
cross-channel negative mass

```text
k sum_y[-alpha_1 CP_1(k,y)-alpha_2 CP_2(k,y)]_+=O(1),
```

equivalently the same sum in owner coefficients multiplied by the exact
common factor `k Lambda_n/[(n-3)(n-4)]`.  This permits cancellation between
channels and is the accepted minority-sign target.

## 8. Status ledger and stop

```text
six immutable dependency inventories                         verified
beta_1/beta_2 normalization, including channel-2 fair choice proved exact
positive-composition/owner-phase convolution                 proved exact
T/D and IS/IN/X retention                                   proved exact
delta log-convexity and admissible-lag PSD repair            proved exact
collision/decorated specialization with theta_k              proved exact
k=3 admissible OCI positivity                                exact finite only
signed channel-2 PSD dominance                               refuted exactly
GOCI / OCI / CP                                              unresolved
OS+ / MS / FCL1                                              unresolved
gap / mixing / Terminal                                      no inference
```

**Final action:** freeze the strict GOCI reduction and exact signed-PSD
obstruction; request a fresh immutable audit.  Do not infer OCI false from
the spectral witness, and do not promote the finite positive row.
