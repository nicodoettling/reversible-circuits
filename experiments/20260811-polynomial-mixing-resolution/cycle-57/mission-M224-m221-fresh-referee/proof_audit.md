# M224 independent proof audit of frozen M221

Date: 2026-08-13 UTC.

## 1. Verdict and strict scope

```text
FINAL VERDICT: ACCEPT.
MATERIAL OBJECTIONS: NONE.
NONMATERIAL OBJECTIONS: NONE.
```

M221 proves least degree-six Bernstein coefficient bandwidth one only at the
exact fresh row `(B,L,kappa,D)=(1,6,2,1)`, and separately proves that the raw
width-one cone is not closed under unsaturated retained lifts. This audit
accepts no recursive width-one envelope, all-state majorant, contraction,
total AMV, gap, mixing, or Terminal result.

## 2. Immutable source gate

The frozen M221 directory contains exactly the eight payloads declared in its
manifest plus `SHA256SUMS`. Its independently computed ledger digest is

```text
ff5315e5930f3d8dc3c959acbb4413e32df4cf1f9870338e94ec892c18ec1983.
```

Every payload passes. Only after that gate were M221's theorem, report,
request, and result values read. M221 remained immutable.

## 3. Clean-room reconstruction and cost matrix

The independent checker imports no project or M221 code and reads no M221
data. It reconstructs the reset/history recursion using literal ordered
compositions rather than grouped Cayley roots, exact basin currents, all
exterior `eta`, one `1/pi_a`, and omission of killed `a=d`. Across 32 reachable
states it records 51 live literal roots, 108 retained observations, and 51
killed observations. The top kernel has 49 nonzero monomial coefficients.

Exact Gaussian inversion of the Bernstein basis, whose determinant is
`162000`, gives `A`. Independently, with degree-six Bernstein features `b_i`,
the checker constructs

```text
G_ij=E[b_i(U)b_j(U)]
     -12 E[(U-1/2)b_i(U)]E[(U-1/2)b_j(U)].
```

It obtains

```text
kernel d2ee4261fd89e712d0649d9cea3c30952256bff82c99134a59fce7b151505152
A      d1dd37fe74b894523b4b049099d194ed34fb64fb36d144b48ff3746a34e1ccae
G      9bd460a8da3fbf2a7f3dd8698eae88116bb1608dc2b1db9746ddfd9b1b2f5c0c
```

exactly matching the frozen values.

## 4. Conic primal/dual indexing

Let `S_w` be the symmetric matrices supported on `|i-j|<=w`. The primal is

```text
min <G,C>  subject to P=C-A>=0 and C in S_w.          (P_w)
```

Equivalently, `P_ij=-A_ij` off the band. Under the full symmetric Frobenius
pairing `<M,N>=sum_ij M_ij N_ij`, introduce a symmetric off-band multiplier
`Y`. The Lagrangian is

```text
<G,A>+<G,P>+<Y,P+A>
=<A,G+Y>+<P,G+Y>.
```

Its infimum over `P>=0` is finite precisely when `X=G+Y>=0`. Because `Y`
vanishes on band, the dual is

```text
max <A,X>  subject to X>=0 and X_ij=G_ij on band.    (D_w)
```

This confirms M221's on-band/off-band indexing. The full symmetric pairing
counts both entries of an off-diagonal pair consistently in both programs; no
factor of two is missing. A sufficiently large `C=tI` is strictly feasible,
although only weak duality is needed for the two certificates.

## 5. Width-zero exact obstruction

The clean-room charge matrix has diagonal

```text
(433/10192,747/28028,3491/112112,100/3003,
 3491/112112,747/28028,433/10192).
```

With M221's signs/radii, `X_0=vv^T+diag(G_jj-r_j^2)`. The seven independently
computed remainders are exactly the displayed strictly positive rationals, so
`X_0>=0`; its diagonal equals `G`, making it feasible for `(D_0)`. Exact
matrix contraction gives

```text
<A,X_0>-(1-q)
=1000948704365931347999936328408157889213
 /48209994003606915089647408250880000000000 > 0.
```

Weak duality therefore rules out every bandwidth-zero feasible budget point.

## 6. Width-one exact primal

The checker independently enters the seven diagonal and six adjacent entries
of M221's tridiagonal `C_1`; its exact matrix digest is
`d0df5f5c2cd436116d711a62b449abff74bcbd7491907590218e96d6b9426dbb`.
The signed-diagonal-dominance margins of `C_1` reproduce as

```text
(253/150,193/300,16/75,143/300,19/25,1/200,113/40).
```

All are positive and every diagonal entry is positive, so the symmetric
matrix `C_1` is positive definite. Subtracting the independently reconstructed
`A` gives digest
`9f5b386200f2921b8a8f63161cc9ca9af94e28efb39962d265a08da3aff3ba64`
and reproduces all seven frozen row margins. Their minimum is

```text
22066085580152050340437577895121
/9632366434287095922007474176000000 > 0.
```

Thus `C_1-A` is also positive definite. Exact cost contraction gives

```text
<G,C_1>=4937603/9172800,
(1-q)-<G,C_1>=485323987/37571788800 > 0.
```

Width zero is infeasible and width one is feasible; since bandwidth is a
nonnegative integer, least feasible bandwidth is exactly one for this row.
This does not compute the optimum `p_1` and says nothing about other rows.

## 7. Lift theorem audit

Exact Bernstein multiplication sends a child index `j` to `a+j`. In a
saturated lift both coefficient indices receive the same shift, so their
difference—and therefore bandwidth—is preserved.

If the combined degree is `n<L`, put `h=L-n`. Degree elevation sends index
`k` into the consecutive interval `{k,...,k+h}`. Thus a pair initially at
distance at most `w` produces only pairs at distance at most `w+h`, capped by
`L`. The exact raw bound is therefore

```text
min(L,w+(L-n)).
```

The checker verifies 287 saturated index pairs and 287 unsaturated support
bounds. For the explicit child rank-one vector `(1,1)`, retained
`d=1,a=0` multiplication gives degree-two vector `(1,1/2,0)`. Exact elevation
to degree six gives

```text
(1,5/6,2/3,1/2,1/3,1/6,0).
```

Its outer product has nonzero extreme pair `(0,5)`, hence bandwidth five.
This refutes raw fixed-width-one closure. It does not refute an envelope;
controlling an envelope's first-Jacobi cost remains unresolved.

## 8. Numbered objections

1. **Material objections:** none.
2. **Conic-duality objections:** none; the symmetric Frobenius factors and
   on-band equalities are consistent.
3. **Exact-certificate objections:** none; all matrices, margins, charges, and
   signs reproduce.
4. **Lift-theorem objections:** none; both the general support bound and the
   width-five example reproduce.
5. **Scope objections:** none; M221 explicitly limits the theorem to one row
   and leaves recursive envelope cost and contraction unresolved.

