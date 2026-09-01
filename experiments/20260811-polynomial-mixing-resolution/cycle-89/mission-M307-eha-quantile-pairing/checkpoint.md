# M307 halfway checkpoint: analytic phase complete

Date: 2026-08-14 UTC.

## Source locks

The accepted source digests are exact:

```text
M300  24964f0c5c8e8588715a98fc22a80d7b268b8e6abe683bd95772f51acecbebc8
M303  a3a708c95c72be4d665a47bcfe14196c1bc11bb281c9e26ee3b625b843cf1e72
```

Every listed payload passes.  One nonmaterial frozen-document discrepancy is
retained: M300's checksum file has **15** payload entries, while M303 says
fourteen.  The digest, files, formulas, and mathematical verdict are
unaffected.  Frozen predecessors will not be edited.

## Fixed candidate and exact transport identity

Before any computation, `plan.md` fixed `(QCP_1)`.  Put

```text
A_c=sum_(i<=c)x_i,       B_d=sum_(j<=d)y_j,
I_c=(A_(c-1),A_c],       J_d=(B_(d-1),B_d],
pi_cd=length(I_c intersect J_d).
```

Accepted Hahn mass balance gives `A_(k-1)=B_(k-1)=mu_k`.  Hence the
`I_c` and `J_d` families are two partitions of `(0,mu_k]`, so

```text
pi_cd>=0,
sum_d pi_cd=x_c,
sum_c pi_cd=y_d.
```

For the fully middle-phase cut means, this proves the exact coupling identity

```text
P_(k,ell)(u)
 =sum_(c,d)pi_cd(Xbar_c-Ybar_d).                    (QTI_1)
```

Therefore the predeclared cell inequality

```text
(QCP_1)  Xbar_c>=Ybar_d whenever pi_cd>0
```

is sufficient for MCLP_1 and hence GOCI_1.

## Why this retains mixed `R_c`

The accepted Abel cumulative coefficient is exactly

```text
R_c=A_c-B_c.
```

If `R_c<0`, then on the positive-length quantile interval `(A_c,B_c]` the
positive cut index lies strictly after `c` while the negative cut index lies
at or before `c`.  Thus the transport contains cells `(i,j)` with
`i>c>=j`.  If `R_c>0`, `(B_c,A_c]` forces cells with `i<=c<j`.  Consequently
a sign change in `R_c` makes the canonical transport cross the diagonal in
both directions.  QTI_1 neither assumes nor manufactures one-direction Abel
monotonicity.

Equivalently, define step functions on `(0,mu_k]` by

```text
mathsf X(t)=Xbar_c for t in I_c,
mathsf Y(t)=Ybar_d for t in J_d.
```

Then `P=int(mathsf X-mathsf Y)dt`, while QCP_1 asks for the pointwise
inequality only on this fixed cut-mass quantile pairing.  It allows the two
cut indices to move in either direction.

## Analytic response attempt and exact stop before computation

Substitution of the accepted owner formula gives each cell difference as a
finite difference of complete middle-phase sums of interval
autocorrelations.  Every state response is nonnegative, but the owner sizes,
one-run/two-run blocks, and overlap locations all change across a QCP
transport cell.  The cut-mass coupling alone supplies no termwise matching of
these owner fields.  Fixed-middle ordering cannot be used (it is refuted),
and no pointwise MON/FOSD, signed-PSD, raw-atom, or common-direction Abel
claim is introduced.

The exact first unresolved sharper lemma is now QCP_1 itself, with no hidden
normalization or endpoint.  Since the transport weights depend only on `k`,
accepted statewise lag reflection gives cellwise

```text
Xbar_c(k,u,ell)-Ybar_d(k,u,ell)
 =Xbar_c(k,u,3k-ell)-Ybar_d(k,u,3k-ell).
```

Both endpoints remain.

## Sole predeclared finite action

The analytic route does not close QCP_1.  The only permitted finite action is
now the plan's exact `k=9`, `n=27` falsifier, over four middle cut classes and
24 admissible lags.  It will stop the universal claim on the first exact
negative supported transport cell while also checking the aggregate MCLP
cells.  No other rank will be run.

No MCLP/GOCI/OCI/CP/MS/FCL1, gap, mixing, or Terminal conclusion has been
reached at this checkpoint.
