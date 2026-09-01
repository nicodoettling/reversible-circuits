# M293 independent proof audit of M290

Date: 2026-08-14 UTC.

## Verdict and scope

```text
ACCEPT M290'S EXACT DEFECT-FIELD AND INVERSE-OWNER THEOREMS.
ACCEPT THE EXACT POSITIVE-COMPOSITION LAW AND DOR <=> BODT REDUCTION.
MATERIAL OBJECTIONS: ZERO.
NONMATERIAL OBJECTIONS: ONE SCOPE-WORDING CLARIFICATION.

BODT, DOR, DSR, DTR, CIBV, SET, PBV, FD, FCL1, EVERY GAP/MIXING
CLAIM, AND BOTH TERMINALS REMAIN UNRESOLVED.
```

The accepted scope is odd `k>=3`, `n=3k`, the complete centered first-pair
law in the auxiliary uniform minimal-factorization model, the convention
`(pq)(x)=p(q(x))`, and target derivative lags `2<=ell<=n-3`. It is not a
theorem about the global identity-word law or the lazy exact same-product
`{3,4,5}` heat-bath chain.

## 1. Exact endpoint formula

With the null-extended owner map, write simply

```text
Q_ell(s)=sum_x rho(o(x),o(x+ell)),
```

where any null incidence has coefficient zero. Reindexing the first copy at
lag `ell+1` by `x <- x-ell` gives

```text
Q_(ell+1)-Q_ell
 =sum_x [rho(o(x-ell),o(x+1))-rho(o(x-ell),o(x))].
```

The sign and all three indices are therefore exact. A summand is zero unless
`o(x)` jumps to `o(x+1)`, including genuine/null transitions. No phase,
owner equality, or one-run/two-run seam has been averaged away.

## 2. Defect-field identity

For genuine owners put

```text
a_i=tau(d_i-1)/tau(d_i),
b_i=tau(d_i-2)/tau(d_i),
delta_i=b_i-a_i^2.
```

Off the owner diagonal, `kappa_ij=a_i a_j`; on it,
`kappa_ii=a_i^2+delta_i`. Hence, with
`A=sum_i a_i chi_i` and `G=sum_i chi_i`,

```text
F_ell=Corr(A,A;ell)+sum_i delta_i Corr(chi_i,chi_i;ell),
Q_ell=e^2 F_ell-Corr(G,G;ell).
```

Now `eA=G+U` and `G=1-B`. Expanding coefficientwise gives exactly

```text
Q_ell
 =2 sum_x U(x)
  -Corr(U,B;ell)-Corr(B,U;ell)+Corr(U,U;ell)
  +e^2 sum_i delta_i Corr(chi_i,chi_i;ell).
```

The first term is lag-independent and disappears after adjacent
differencing. The clean-room guard checked this equality as a polynomial in
`e`—not numerically—at 273,312 state/lag pairs.

Owners of size one have no generic position. At `d=2`, `a_2=1`, `b_2=0`,
and `delta_2=-1`, but that owner has at most one generic position. Its
self-correlation is therefore zero at every nonzero circular lag, including
both `ell` and `ell+1` in every target derivative. This removes only the
size-two diagonal correction; the size-two first-order `U` field is retained.

## 3. Ratio bounds and the statewise variation theorem

For `d>=2`,

```text
a_d=(1-1/d)^(d-2),
b_d=(1-1/d)(1-2/d)^(d-3).
```

The standard logarithmic bounds used by M267/M270 give

```text
0<=lambda_d:=log(e a_d)<=2/d<=1.
```

Convexity of the exponential on `[0,1]` then yields

```text
0<=u_d=e a_d-1<=2 lambda_d<=4/d.
```

The increasing successive ratios of `tau` prove log-convexity and hence
`delta_d>=0` for `d>=3`. Taylor bounds for the displayed exact `a_d,b_d`
formulas, uniformly for `1/d<=1/4` with `d=3` checked separately, give
`delta_d=O(d^-2)`.

Let

```text
S(s)=sum_(i:d_i>=2) 1/d_i.
```

There are exactly three residual owners. Each `chi_i` is a union of at most
two circular intervals, so `TV_circ(chi_i)<=4` and
`||chi_i||_1<=d_i`. Consequently

```text
||U||_1<=12,              TV_circ(U)<=16 S(s),
||B||_1<=4.
```

For arbitrary circular sequences,

```text
TV_circ(Corr(f,g))
 <=min(||f||_1 TV_circ(g),TV_circ(f)||g||_1),
```

by expanding the adjacent difference and summing first over the translated
factor. Applying the appropriate side of this inequality to the two `U/B`
terms and to `U/U` makes their total variation `O(S(s))`. For each `d_i>=3`,

```text
e^2 delta_(d_i) TV_circ(Corr(chi_i,chi_i))
 <=4e^2 C/d_i.
```

The `d=1,2` cases contribute no diagonal target derivative, as above.
Restricting full circular variation to the target lags proves exactly

```text
sum_(ell=2)^(n-3)|Delta Q_ell(s)|<=C S(s).
```

No constant depends on `k`, `n`, or the state. The clean-room guard also
verified that every owner has at most two circular intervals and that every
size-two owner has zero nonzero-lag self-overlap throughout the `k=9` source
support.

## 4. Signed density and positive-composition normalization

The coefficient

```text
omega(s)=a(s)[C_B(s)/A_B-C_A(s)/A_A]
```

is exactly `P_B(s)-P_A(s)`, including all raw ordered lifts and both live
source channels. Thus

```text
sum_s omega(s)=0,             sum_s|omega(s)|<=2.
```

For a positive three-composition and support anchor `r`, the unique forward
triangle has one representation for each of its three support vertices.
Equivalently,

```text
n binom(n-1,2)=3 binom(n,3).
```

For four support vertices, the compatible `S/N` encodings alternate with
the chosen anchor. Across their combined sum every supported double has four
representations; equivalently,

```text
2n binom(n-1,3)=4[2 binom(n,4)].
```

Therefore the factors `1/3` and `1/4` are exact. The variable `r` already is
the cyclic support anchor, so multiplying by an additional `n` would be
wrong. Direct tracing of `s^-1h` gives the owner rows

```text
T: I_1,I_2,I_3                    / g_1,g_2,g_3,
S: I_1,I_3,I_2 union I_4          / g_1,g_3,g_2+g_4,
N: I_2,I_4,I_1 union I_3          / g_2,g_4,g_1+g_3.
```

Thus M290's formula retains the combined signed source coefficient, outer
kind, literal phase, owner sizes, seams, and all same-/cross-owner incidences
before the lag absolute value.

## 5. All-macroscopic sector and exact DOR/BODT scope

If every residual owner has size at least `(k+1)/2`, then, because there are
three owners,

```text
S(s)<=6/(k+1)=O(1/k).
```

Let `V_int` be the already-combined signed contribution of those states.
The statewise theorem and the total-variation bound on `omega` give

```text
||V_int||_1
 <=sum_(s interior)|omega(s)| ||Delta Q(s)||_1
 <=O(1/k) sum_s|omega(s)|
 =O(1/k).
```

For odd `k`, the complementary boundary is exactly the set with some owner
size at most `(k-1)/2`. Writing the full DOR vector as
`V_int+V_bd`, the triangle inequality in both directions proves

```text
||V_int+V_bd||_1=O(1/k)  iff  ||V_bd||_1=O(1/k).
```

This is the claimed `DOR <=> BODT` equivalence. It removes a whole explicit
sector but does not establish the boundary estimate. Hence it does not prove
DOR.

## 6. Independent `k=9` guard

`independent_k9_guard.py` imports no M290 or predecessor code/data and was
run at no rank other than `k=9`. It reconstructed:

- source masses `1,1`, raw ordered-pair counts `10,044,22,108`, and `11,388`
  accessible supported products;
- signed channel/kind masses zero except
  `J2_T=32/3519`, `J2_D=-32/3519`;
- 261,924 endpoint identities and 273,312 coefficientwise defect identities;
- all 2,925 triangles with multiplicity three and all 35,100 supported
  doubles with combined `S/N` multiplicity four;
- 5,525 direct `T/S/N` owner-row checks;
- exact reflection, central zero, negative signs at lags `2,...,7`, positive
  signs at `8,...,12`, and zero at `13`; and
- the identical symbolic DOR and DTR values, with
  `DOR(k=9)=0.2784019538957808...` and
  `9 DOR(k=9)=2.5056175850620277...`.

These data match frozen M290 exactly. They are convention and falsification
checks only.

## 7. Numbered objections and scope clarification

1. **Material objections:** none.
2. **Nonmaterial wording clarification:** item 6 of M290's
   `fresh_audit_request.md` asks whether “collision/decorated terms remain
   combined in the BODT statement.” BODT is correctly defined in the proof
   and report as the decorated `Delta Q` obligation alone; `Delta I` is not
   part of DOR or BODT. Collision and decoration must remain combined for the
   OCI sign identity, while the separate sufficient PBV route requires both
   CIBV and DOR. This checklist wording does not alter any theorem statement.
3. **Mandatory interpretation:** “it contributes nothing” in the size-two
   paragraph refers only to the negative diagonal `delta_2` remainder. The
   first-order size-two `U` contribution remains and is included in the
   statewise bound.
4. **Downstream firewall:** BODT, DOR, DSR, DTR, CIBV, SET, PBV, FD, FCL1,
   every bridge/local-chain gap or mixing claim, and both Terminals remain
   unresolved.

Final verdict: **ACCEPT M290 AS FROZEN AT THE STATED REDUCTION SCOPE.**
