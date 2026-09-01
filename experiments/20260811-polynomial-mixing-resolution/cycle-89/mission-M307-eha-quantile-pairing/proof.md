# M307 mixed-sign quantile transport and exact QCP obstruction

Date: 2026-08-14 UTC.

Status: the quantile transport identity `(QTI_1)` is **proved**.  The
predeclared cellwise quantile pairing `(QCP_1)` is **refuted exactly** at the
sole new rank `k=9`.  MCLP_1 and GOCI_1 remain **unresolved**.

## 1. Scope and accepted input

Use `(pq)(x)=p(q(x))`, with displayed factors multiplied left-to-right.  Fix
odd `k>=3`, put `n=3k`, and use `1<=u<k/2` and
`2<=ell<=n-2`.  This concerns only channel one in the first separated fixed
cell of the auxiliary uniform minimal long-cycle factorization law under the
nonlazy cyclic rank-two quotient kernel.  It is not the global identity-word
law or the lazy exact same-product `{3,4,5}` heat-bath chain.

M300/M303 prove, after summing all `k` phases of the fixed middle cut class,

```text
P_(k,ell)(u)=sum_(c=1)^(k-1)[x_c Xbar_c-y_c Ybar_c],        (1.1)
```

where

```text
x_c=2c v_(2k-1)(c)>0,
y_c=(k-c)v_k(c)-(2k-1-2c)v_(2k-1)(c)>0.                    (1.2)
```

The positive and negative exterior Hahn laws have equal total mass, so

```text
sum_c x_c=sum_c y_c=:mu_k>0.                               (1.3)
```

Every `Xbar_c,Ybar_c` in this note retains the complete middle phase orbit.

## 2. Canonical mixed-sign quantile transport

Define cumulative cut masses and their half-open mass intervals by

```text
A_c=sum_(i=1)^c x_i,        I_c=(A_(c-1),A_c],
B_d=sum_(j=1)^d y_j,        J_d=(B_(d-1),B_d],
A_0=B_0=0,
```

and set

```text
pi_cd = |I_c intersect J_d|
      = [min(A_c,B_d)-max(A_(c-1),B_(d-1))]_+.              (2.1)
```

### Proposition 1 (exact quantile marginals)

For every odd `k>=3`,

```text
pi_cd>=0,       sum_d pi_cd=x_c,       sum_c pi_cd=y_d.     (2.2)
```

#### Proof

By `(1.3)`, both interval families partition the same mass interval
`(0,mu_k]`.  Intersecting one `I_c` with the `J_d` partition and adding
lengths gives `|I_c|=x_c`; reversing the roles gives `|J_d|=y_d`.  This is
exact and includes the first and final cut endpoints.  QED.

### Proposition 2 (quantile transport identity `(QTI_1)`)

For every allowed `(k,u,ell)`,

```text
P_(k,ell)(u)=sum_(c,d)pi_cd(Xbar_c-Ybar_d).                  (QTI_1)
```

#### Proof

Use the two marginal identities in `(2.2)`:

```text
sum_(c,d)pi_cd Xbar_c=sum_c x_c Xbar_c,
sum_(c,d)pi_cd Ybar_d=sum_d y_d Ybar_d.
```

Subtract and invoke `(1.1)`.  QED.

This is equivalently an integral identity.  Put `mathsf X(t)=Xbar_c` on
`I_c` and `mathsf Y(t)=Ybar_d` on `J_d`; then

```text
P_(k,ell)(u)=integral_(0,mu_k)[mathsf X(t)-mathsf Y(t)]dt.  (2.3)
```

## 3. Exact retention of mixed Abel signs

The accepted Abel cumulative coefficient is

```text
R_c=A_c-B_c.                                                (3.1)
```

If `R_c<0`, every mass point in `(A_c,B_c]` is assigned a positive cut
index strictly greater than `c` and a negative cut index at most `c`.
Hence the transport has positive mass in cells `(i,j)` with `i>c>=j`.
If `R_c>0`, the interval `(B_c,A_c]` instead forces cells with
`i<=c<j`.  Thus when `R_c` takes both signs, the transport crosses the cut
diagonal in both directions.  No common-direction Abel monotonicity is
assumed or recovered by `(QTI_1)`.

Since the transport weights depend only on `k`, accepted statewise lag
reflection gives cellwise

```text
Xbar_c(k,u,ell)-Ybar_d(k,u,ell)
 =Xbar_c(k,u,n-ell)-Ybar_d(k,u,n-ell).                       (3.2)
```

Both admissible lag endpoints remain.

## 4. Predeclared sufficient lemma

The candidate fixed in `plan.md` before computation was

```text
(QCP_1)  Xbar_c(k,u,ell)>=Ybar_d(k,u,ell)
         whenever pi_cd(k)>0.                               (4.1)
```

It is cellwise only after all middle phases have been combined.  It is not
fixed-middle positivity, a pathwise or scalar MON/FOSD statement, signed
PSD, raw-atom positivity, or one-direction Abel monotonicity.  By QTI_1 and
`pi_cd>=0`, QCP_1 would imply MCLP_1 and hence GOCI_1.

The accepted owner-autocorrelation formula does not prove `(4.1)`
termwise: across a supported transport cell, the nested/separated topology,
owner sizes, one-run/two-run owner fields, and interval overlaps all change.
The exact guard below shows this is a genuine obstruction, not just a gap in
that attempted proof.

## 5. Sole exact `k=9` obstruction

The predeclared standard-library checker evaluates exactly `k=9`, `n=27`,
all four middle cut classes, all 24 admissible lags, and the complete
15-cell support of the canonical cut transport.  It imports no project or
predecessor code/data.  Exact guards verify chord-law and gamma
normalization, the middle partition, residual owner counts, literal equals
repaired response, transport row/column marginals, QTI_1, and reflection.

The first lexicographic supported failure is

```text
(u,ell,c,d)=(1,2,2,2),

pi_22 = 414616267940933495214692
        /13690880720256852133629417 > 0,

Xbar_2-Ybar_2
= -20367588311959084409463968537826170073480336286773182238294530615595556134725838821664097726457710848190710593
  /7091821439466753884372240348474182172628859729780516915565162812551386352457307844070336622322568396800000000
<0.                                                              (5.1)
```

The difference is approximately `-2.871982675510025`; its weighted
transport contribution is approximately `-0.08697546657821176`.  Therefore
`(5.1)` exactly refutes universal QCP_1.

This is not an isolated boundary accident.  Of

```text
4 middle classes x 24 lags x 15 supported cells = 1440
```

transport cells, 778 are negative, and every one of the 96 `(u,ell)` rows
has at least one negative cell.  The counts by middle class are

```text
u=1: 204,   u=2: 188,   u=3: 192,   u=4: 194.
```

The minimum difference is approximately `-2.9057956436408245` at
`(u,ell,c,d)=(4,2,2,2)` (and its reflected lag).  The exact value is stored
in `qcp_k9.json`.

The cumulative cut coefficients at this sole rank retain both signs:

```text
R_1,R_2,R_3,R_4<0;  R_5,R_6,R_7>0;  R_8=0.                (5.2)
```

This is finite coefficient data only.

## 6. Aggregate MCLP result and exact logical scope

Despite 778 negative quantile cells, every complete MCLP aggregate at this
rank is strictly positive.  All

```text
4 middle classes x 24 admissible lags = 96
```

values of QTI_1 are positive.  The minimum occurs at `u=2` and the reflected
lags `ell=8,19`:

```text
14101151053051097333056759056804742144461772203719272577819683617467476572306704209237928480928135313847888157058461020246349508272398056891651911762807327308102099300013201159577858797071
/141294421183276274527442727757398210083787494960920114455791313777358178349166511093434429667425768391000676703748526827089105758281008873036785287148044770693899249254400000000000000000000
approximately 0.0997997722412562.                              (6.1)
```

Thus the exact obstruction is cancellation-specific:

```text
QCP_1 is false,
but the sole k=9 guard does not refute MCLP_1.
```

Finite positivity in `(6.1)` has no all-rank implication and does not prove
GOCI_1.  It shows that any successful use of QTI_1 must retain cancellation
across multiple supported quantile cells.  Per coordinator instruction, this
mission stops here and does not search for a weaker row/block pairing.

## 7. Exact stop

**Proved:** QTI_1 and its exact mixed-sign support interpretation.

**Refuted:** universal cellwise QCP_1.

**Exact finite only:** the `k=9` mixed `R_c` signs, 778/1440 negative QCP
cells, and 96/96 positive MCLP aggregates.

**Unresolved:** MCLP_1, GOCI_1, GOCI_2, OCI/CP, OS+, MS, FCL1, every gap and
mixing claim, and both Terminals.  No main-chain exceptional case (`m` odd,
`m=0`, `m=2`, `N=2`) is implicated by this auxiliary calculation.
