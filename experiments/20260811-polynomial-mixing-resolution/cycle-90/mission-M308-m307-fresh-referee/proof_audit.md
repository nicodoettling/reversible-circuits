# M308 Independent Proof Audit of M307

Date: 2026-08-14 UTC

## 1. Exact scope

This audit accepts from frozen M300/M303 only the channel-one all-middle
identity

```text
P_(k,ell)(u)=sum_c [x_c Xbar_c-y_c Ybar_c],
x_c=2c v_(2k-1)(c)>0,
y_c=(k-c)v_k(c)-(2k-1-2c)v_(2k-1)(c)>0,
sum_c x_c=sum_c y_c=mu_k>0.
```

Here `k>=3` is odd, `n=3k`, `1<=u<k/2`, and `2<=ell<=n-2`.
Every response mean includes all `k` middle phases.  The object is the first
separated fixed cell of an auxiliary minimal long-cycle-factorization model,
not the global identity bridge or the `{3,4,5}` heat-bath chain.

## 2. Quantile marginals and QTI_1

Put

```text
A_c=sum_(i<=c)x_i,   I_c=(A_(c-1),A_c],
B_d=sum_(j<=d)y_j,   J_d=(B_(d-1),B_d],
pi_cd=|I_c intersect J_d|,
A_0=B_0=0.
```

Equal total mass makes each of `(I_c)` and `(J_d)` a disjoint half-open
partition of `(0,mu_k]`.  Therefore, including both terminal endpoints,

```text
sum_d pi_cd=|I_c|=x_c,       sum_c pi_cd=|J_d|=y_d.
```

Consequently

```text
sum_(c,d)pi_cd(Xbar_c-Ybar_d)
 =sum_c x_c Xbar_c-sum_d y_d Ybar_d
 =P_(k,ell)(u).
```

Thus M307's QTI_1 is exact.  It is an algebraic transport identity, not a
sign theorem.

## 3. Orientation and the exact R-support relation

Since `R_c=A_c-B_c`, the half-open conventions give the following exact
orientation (single endpoints have zero transport mass and also obey the
displayed weak side):

```text
R_c<0:  t in (A_c,B_c]  =>  positive index i>c, negative index j<=c;
R_c>0:  t in (B_c,A_c]  =>  positive index i<=c, negative index j>c.
```

Each nonempty interval has positive length and hence supplies positive
transport mass in at least one cell of the stated orientation.  Therefore
mixed signs among the `R_c` force crossings in both directions; they do not
give a common monotone/Abel direction.  At `k=9`, the exact signs are

```text
R_1,R_2,R_3,R_4<0;  R_5,R_6,R_7>0;  R_8=0.
```

This also confirms that M307 has not reversed the roles of the positive cut
index and the negative cut index.

## 4. Sole exact finite replay and QCP_1 obstruction

The frozen checker was inspected before execution.  It is standard-library
only and fixes `k=9` in source.  It reconstructs all four chord laws, the
signed exterior law, residual owners and literal response, all four middle
cut classes with all nine phases, all 24 admissible lags, the cut means, and
the canonical transport.  Its exact `Fraction` assertions check
normalization, transport marginals, direct/cut/transport equality, and
statewise lag reflection.  The loops are ordered by `u`, then `ell`, then
sorted `(c,d)`, so its first-negative field is lexicographic in the claimed
order.

Exactly one successful no-import replay was made.  Its JSON is byte-for-byte
identical to M307's frozen JSON; both have digest

```text
a77083ebf5ec54dcb5f31d434821921e06a274506b2993c6615db0cc4ca7dd61.
```

The canonical transport has 15 supported cells.  The first exact negative
cell is `(u,ell,c,d)=(1,2,2,2)`, with

```text
pi_22 = 414616267940933495214692
        /13690880720256852133629417 > 0,

Xbar_2-Ybar_2
= -20367588311959084409463968537826170073480336286773182238294530615595556134725838821664097726457710848190710593
  /7091821439466753884372240348474182172628859729780516915565162812551386352457307844070336622322568396800000000
<0.
```

This exactly refutes universal QCP_1.  The nested counters inspect
`4*24*15=1440` supported cells and return 778 negatives.  The JSON contains
96 row-level `negative_qcp_cells` fields, all between 3 and 12 and none zero;
the totals by `u` are `204,188,192,194`, which sum to 778.  The minimum cell
difference is approximately `-2.9057956436408245` at `(4,2,2,2)` and at its
reflected lag.

## 5. Aggregate finite values and reflection

The checker forms each aggregate directly from the complete signed exterior
law and independently asserts equality with both the cut form and QTI_1.
Exact rational comparison returns:

```text
96 aggregates tested; 96 strictly positive; 0 nonpositive.
```

The exact minimum is

```text
14101151053051097333056759056804742144461772203719272577819683617467476572306704209237928480928135313847888157058461020246349508272398056891651911762807327308102099300013201159577858797071
/141294421183276274527442727757398210083787494960920114455791313777358178349166511093434429667425768391000676703748526827089105758281008873036785287148044770693899249254400000000000000000000,
```

approximately `0.0997997722412562`, attained exactly at `(u,ell)=(2,8)`
and `(2,19)`.  Since `n=27`, these are a reflected pair.  Exact assertions
also compare every aggregate and every `Xbar_c,Ybar_c` with lag `27-ell`;
the 96 admissible entries form 48 verified reflection pairs.

These are finite facts at `k=9` only.  In particular, positive aggregates do
not repair QCP_1 and do not establish an all-rank MCLP statement.

## 6. Scope firewall

The accepted conclusions are only QTI_1, its mixed-sign support
interpretation, the exact refutation of QCP_1, and the stated finite `k=9`
data.  This audit makes no inference of MCLP, GOCI, OCI, CP, MS, FCL1, a
spectral gap, mixing, or either Terminal.
