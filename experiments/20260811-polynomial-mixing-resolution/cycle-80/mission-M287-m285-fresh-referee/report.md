# M287 fresh immutable referee report on M285

Date: 2026-08-14 UTC.

## Verdict

```text
ACCEPT M285'S STRICT EXACT GOCI REDUCTION.
ACCEPT THE EXACT k=3 CHANNEL-TWO SIGNED-PSD OBSTRUCTION.
FATAL OBJECTIONS: ZERO.
MAJOR OBJECTIONS: ZERO.
MINOR OBJECTIONS: ZERO.

GOCI/OCI, CP, OS+, MS, FCL1, FD, GAP, MIXING, AND TERMINALS REMAIN OPEN.
```

The accepted statement concerns only the first separated fixed cell of the
auxiliary uniform minimal long-cycle factorization law under the nonlazy
cyclic rank-two quotient kernel, for odd `k>=3`, `n=3k`, with
`(pq)(x)=p(q(x))`.  It is not a theorem about the global identity-word law or
the lazy exact same-product `{3,4,5}` heat-bath chain.

## 1. Immutable source gate

M285's checksum-file digest is exactly

```text
54eed4258da59ee1b8491815f182f05ac7c57c809e0f002bc2a2a79666098ac8.
```

Its directory contains exactly the ten payloads named by `SHA256SUMS` plus
the checksum file itself.  All ten payloads pass.  The declared M280/M283,
M91/M94, and M261/M264 manifests also have the exact digests and payload
counts stated by M285, and every listed file passes.  Their controlling
status ledgers agree with M285: all imported formulas are exact, while every
sign, variation, gap, and mixing claim remains open.  No source artifact was
edited.

## 2. Normalized product coefficients

Independent completion-count reconstruction confirms

```text
beta_1(s)
 =sum_(ef=s; e in T(L), f in T(M))nu_L(e)nu_M(f)
  -1/2 sum_(C in {C_-,C_+})
        sum_(ef=s; e in T(C), f in T(M))nu_C(e)nu_M(f),

beta_2(s)
 =a(s)[F_(2k-4)(s^-1L)/F_(2k-2)(L)
       -F_(2k-4)(s^-1F)/F_(2k-2)(F)].
```

The `1/2` appears only in channel one's explicit choice of exterior cycle.
For channel two,

```text
F_(2k-2)(F)=(2k-2)!tau(k)^2
```

is the complete two-component factorization count.  Its interleavings make
the first equal-rank component fair; no extra `1/2` is permitted.  The raw
product lift is exactly `a(s)=3` for a supported triangle and `2` for a
double.  Both normalized laws have total mass one and both beta coefficients
have total mass zero.

## 3. Composition multiplicities and owners

For three positively ordered support vertices there is one compatible
forward triangle, and its three possible support anchors give exactly three
positive-composition representations.  For four support vertices the two
compatible double encodings `S,N` alternate as the anchor runs over the four
vertices, giving exactly four representations of each supported double.
The anchor is already summed; no additional factor `n` occurs.

Tracing `s^-1h` independently yields exactly M285's owner blocks and sizes:

```text
T: I_1, I_2, I_3                    / g_1,g_2,g_3,
S: I_1, I_3, I_2 union I_4          / g_1,g_3,g_2+g_4,
N: I_2, I_4, I_1 union I_3          / g_2,g_4,g_1+g_3.
```

The corresponding overlap convolution reproduces `F_ell(s)`.  The outer
triangle/double kind and the inner `IS/IN/X` partition are retained before
the signed sum.

## 4. Autocorrelation repair and GOCI equivalence

With

```text
a_d=tau(d-1)/tau(d),
b_d=tau(d-2)/tau(d),
delta_d=b_d-a_d^2,
```

the off-diagonal owner coefficient factors as `a_(d_i)a_(d_j)`, so direct
expansion proves

```text
F_ell(s)=sum_x A_s(x)A_s(x+ell)
          +sum_i delta_(d_i)C_ii^s(ell).
```

The increasing ratios
`tau(d)/tau(d-1)=(d/(d-1))^(d-2)` prove `delta_d>=0` for `d>=3`;
the explicit ratio formulas give `delta_d=O(d^-2)`.  At `d=2`,
`delta_2=-1`, but that owner has at most one generic phase, so its
autocorrelation vanishes at every nonzero lag.  Deleting the size-two term
changes only lag zero and leaves the literal response unchanged throughout
`2<=ell<=n-2`.

Consequently M285's GOCI expression is exactly equivalent, on its declared
admissible lags, to

```text
eta_j(F_ell)>=0,
```

and hence to `CP_j>=0` through the accepted positive prefactor.  GOCI is a
strict structural reduction to signed explicit positive autocorrelations;
it is not a proof of their signed coefficient sum.

## 5. Clean-room exact falsifier

`independent_k3_audit.py` imports no M285 or predecessor code/data.  At only
the prescribed `k=3`, it independently rebuilds both source laws and both
explicit beta formulas, checks all channel normalizations, verifies 1,260
composition-owner records, and reconstructs every literal and repaired
response.  All twelve admissible channel-lag values are strictly positive,
which is finite-only.

For channel two's repaired circular sequence and

```text
v=(10,8,2,-5,-9,-9,-5,2,8),
```

the exact quadratic form is

```text
v^T M v=-310962953715709/12252303000000<0.
```

This independently confirms the non-PSD witness.  It refutes only positive
semidefiniteness of M285's canonical signed repaired channel-two sequence.
It is not a negative admissible OCI entry and does not refute GOCI/OCI.

## 6. Numbered objections

1. **Fatal objections: none.**
2. **Major objections: none.**
3. **Minor objections: none.**
4. **Mandatory scope interpretation:** the phrase “PSD route obstruction”
   means only the canonical signed repaired-circulant dominance tested here.
   M285 already states this limitation; no claim that every possible PSD or
   completion argument is impossible is accepted.
5. **Mandatory downstream firewall:** finite `k=3` positivity is not an
   all-rank theorem.  GOCI/OCI, CP, OS+, MS, FCL1, FD, every gap/mixing claim,
   and both Terminals remain unresolved.

## 7. Final status ledger

```text
M285 exact inventory and top checksum digest                 verified
six declared predecessor manifests and controlling ledgers  verified
beta_1/beta_2 normalization and channel-2 fair choice        proved exact
three/four composition multiplicities; no extra n            proved exact
owner intervals/sizes and T/D, IS/IN/X retention             proved exact
rooted-owner autocorrelation and delta log-convexity          proved exact
size-two deletion only at lag zero                           proved exact
GOCI <=> OCI on every admissible lag                         proved exact
k=3 admissible positivity                                   exact finite only
channel-two canonical signed PSD dominance                   refuted exactly
GOCI/OCI, CP, OS+, MS, FCL1, FD                              unresolved
gap, mixing, Terminal                                       no inference
```

Final action: **ACCEPT AND FREEZE M285 with zero substantive objections.**
Continue only from GOCI/OCI or the weaker cross-channel negative-mass target.

