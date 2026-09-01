# M290 report: decorated owner-ratio bounded variation

Date: 2026-08-14 UTC.

## Verdict

```text
PROVE THE EXACT DEFECT-FIELD IDENTITY.
PROVE THE STATEWISE INVERSE-OWNER VARIATION THEOREM.
PROVE THE ALL-MACROSCOPIC-OWNER CONTRIBUTION IS O(1/k).
STRICTLY REDUCE DOR TO THE BOUNDARY OWNER-DEFECT TRANSPORT LEMMA (BODT).
DOR REMAINS UNRESOLVED BECAUSE BODT REMAINS UNRESOLVED.
```

The scope is odd `k>=3`, `n=3k`, for the complete centered first-pair law of
the auxiliary uniform minimal long-cycle factorization model under the
nonlazy cyclic rank-two quotient convention `(pq)(x)=p(q(x))`.  It is not a
claim about the global identity-word law or the lazy `{3,4,5}` heat-bath
chain.

## 1. Literal coefficient law

Extend the residual owner map by a null owner at support heads and put
`rho_ij=e^2 kappa_ij-1` on genuine owners, zero on null incidences.  Direct
circular differentiation gives

```text
Delta Q_ell(s)
 =sum_x[rho(o(x-ell),o(x+1))-rho(o(x-ell),o(x))].
```

Thus only literal owner jumps occur.  Every cyclic phase, owner size,
one-run/two-run seam, same-owner term, and cross-owner term remains present.

## 2. Exact defect field and statewise theorem

With

```text
a_d=tau(d-1)/tau(d),  b_d=tau(d-2)/tau(d),
delta_d=b_d-a_d^2,    u_d=e a_d-1,
G=sum_i chi_i,        B=1-G,       U=sum_i u_(d_i)chi_i,
```

exact expansion gives

```text
Q_ell
 =2 sum_x U(x)-Corr(U,B;ell)-Corr(B,U;ell)+Corr(U,U;ell)
  +e^2 sum_i delta_(d_i)Corr(chi_i,chi_i;ell).
```

For `d>=2`, `0<=u_d<=4/d`; for `d>=3`,
`0<=delta_d<=C/d^2`.  A size-two owner has one generic phase at most, so its
negative diagonal correction is zero at every target lag.  Since every owner
indicator is a union of at most two circular intervals,

```text
TV_circ(Corr(f,g))
 <=min(||f||_1 TV_circ(g),TV_circ(f)||g||_1)
```

proves the new uniform statewise theorem

```text
sum_(ell=2)^(n-3)|Delta Q_ell(s)|
 <=C sum_(i:d_i>=2)1/d_i.
```

This uses the first-order owner defect and the diagonal second-order defect;
it does not replace the exact coefficients by an unsigned finite heuristic.

## 3. Complete positive-composition law and strict reduction

Writing the already-combined source coefficient as

```text
omega(s)=a(s)[C_B(s)/A_B-C_A(s)/A_A],
```

the exact positive-composition formula has coefficient `1/3` on the triangle
row and `1/4` on each of the two double encodings `S,N`.  There is no extra
factor `n`.  The owner rows are exactly

```text
T: I_1,I_2,I_3                    / g_1,g_2,g_3,
S: I_1,I_3,I_2 union I_4          / g_1,g_3,g_2+g_4,
N: I_2,I_4,I_1 union I_3          / g_2,g_4,g_1+g_3.
```

The source channels are combined productwise in `omega`; `T/S/N` and all
`IS/IN/X` incidences remain inside the lag coefficient.  The global total
variation `sum_s|omega(s)|<=2`, applied only after the statewise target-scale
bound, proves that states with every owner at least `(k+1)/2` contribute
`O(1/k)` in lag `l1`.

Consequently DOR is equivalent to the first open scalar lemma:

> **BODT.** Restrict the same complete signed positive-composition vector to
> states with a residual owner at most `(k-1)/2`; prove its lag `l1` norm is
> `O(1/k)`.

This is a strict reduction: the full all-macroscopic-owner sector has been
removed at the target scale, and the boundary condition is literal in each
of the `T/S/N` owner rows.

## 4. Sole finite falsifier

The independent checker ran only at `k=9`.  It reconstructed source masses
one in both channels from 10,044 and 22,108 raw ordered pairs, evaluated
11,388 supported products, and retained channel/kind rows until the final
sum.  Exact signs are negative for `ell=2,...,7`, positive for
`ell=8,...,12`, and zero at the center; exact reflection holds.  Thus the
predeclared DSR candidate survives this rank and the full certified absolute
sum equals its three-point telescoping expression.  Numerically,

```text
DOR(k=9)=0.2784019538957808...,
k DOR(k=9)=2.5056175850620277....
```

This is exact finite-only evidence.  It proves neither DSR nor DTR at other
ranks and supplies no estimate on BODT.

## 5. Obstructions and final ledger

1. **First open lemma:** BODT.  The statewise theorem loses the target factor
   on boundary states with a small owner; their complete signed transport has
   not been controlled.
2. **Sign route:** DSR and its three-point estimate DTR remain unresolved.
   Exact `k=9` survival cannot be promoted from finite positivity.
3. **Cancellation firewall:** no absolute value was placed between the two
   source laws, between `T/D`, or between `IS/IN/X` in the claimed BODT
   reduction.  The proved interior sector is bounded using the total
   variation of the already-combined product coefficient.
4. **Downstream firewall:** CIBV, SET, PBV, FD, FCL1, every spectral-gap or
   mixing statement, and both Terminals remain unresolved.

```text
literal decorated endpoint law                         proved exact
defect-field identity and diagonal second order         proved exact
inverse-owner statewise lag variation                   proved
complete 3/4 positive-composition coefficient law       proved exact
all-macroscopic-owner sector at O(1/k)                  proved
DOR <=> BODT                                            proved strict reduction
DSR at k=9; DOR=DTR at k=9                              exact finite only
BODT, DSR, DTR, DOR                                     unresolved
downstream claims                                       no inference
```

Final action: **freeze the proved theorem and BODT reduction; request a fresh
immutable audit.**
