# M318 exact global staircase-exchange/coboundary identity

Date: 2026-08-14 UTC.

Status: **proved exact from QTI_1/QBD_1; GQAC_1 remains a separate
owner-response inequality.**

## 1. Frozen setup

Fix odd `k>=3`, put `m=k-1`, and retain every middle phase for fixed
`1<=u<k/2` and `2<=ell<=3k-2`.  Use the accepted quantile intervals

```text
I_c=(A_(c-1),A_c],       J_d=(B_(d-1),B_d],
pi_cd=|I_c intersect J_d|,
D_cd=Xbar_c-Ybar_d,
A_m=B_m=mu_k.
```

Let

```text
0=t_0<t_1<...<t_s=mu_k
```

be the sorted union of cumulative endpoints.  On
`(t_(r-1),t_r]`, write `(c_r,d_r)` for the unique supported cell,

```text
omega_r=t_r-t_(r-1),       Z_r=D_(c_r,d_r).
```

QTI_1 is exactly

```text
P_(k,ell)(u)=sum_(r=1)^s omega_r Z_r.                 (1.1)
```

The maximal Abel sign blocks `H_q=[a_q,b_q]` are ordered along this same
staircase, and their terminal mass points are

```text
T_q=M_(b_q)=max(A_(b_q),B_(b_q)).                    (1.2)
```

Every `T_q` is one of the `t_r`, so no cutoff below slices a supported cell.

## 2. Truncated full-aggregate identity

For `0<=T<=mu_k`, define exact truncated marginal masses

```text
lambda_c(T)=|I_c intersect (0,T]|,
rho_d(T)=|J_d intersect (0,T]|.                      (2.1)
```

Both are nonnegative and

```text
sum_c lambda_c(T)=sum_d rho_d(T)=T.                  (2.2)
```

### Proposition 2.1 (global truncated quantile identity; **PROVED**)

At every staircase endpoint `T=t_j`,

```text
Psi(T)
 :=sum_(r=1)^j omega_r Z_r
  =sum_c lambda_c(T)Xbar_c-sum_d rho_d(T)Ybar_d.     (2.3)
```

At the maximal sign-block endpoints,

```text
Psi(T_q)=Phi_(b_q)=sum_(p=0)^q C_p.                 (2.4)
```

At `T=mu_k`, this is the full aggregate `P_(k,ell)(u)`.

#### Proof

Partition `(0,T]` by the intersections with the `I_c` and then by the
`J_d`.  On every resulting interval the integrand is
`Xbar_c-Ybar_d`; collecting first by `c` and then by `d` gives `(2.3)`.
M311/M314's exact rung characterization says the cells through block `q`
occupy `(0,M_(b_q)]`, proving `(2.4)`.  The last block has `b_Q=m` and
`M_m=mu_k`, proving the endpoint statement.  QED.

## 3. Staircase coboundary

### Proposition 3.1 (exact discrete staircase Abel identity; **PROVED**)

For every endpoint `t_j`,

```text
Psi(t_j)
 =t_j Z_j-sum_(r=1)^(j-1)t_r(Z_(r+1)-Z_r).           (3.1)
```

In particular,

```text
P_(k,ell)(u)
 =mu_k Z_s-sum_(r=1)^(s-1)t_r(Z_(r+1)-Z_r).          (3.2)
```

Every difference in `(3.1)` is an exact staircase exchange:

```text
Z_(r+1)-Z_r
 =(Xbar_(c_(r+1))-Xbar_(c_r))
  -(Ybar_(d_(r+1))-Ybar_(d_r)).                      (3.3)
```

The step increments the `c` coordinate, the `d` coordinate, or both, so
`(3.3)` retains the exact horizontal, vertical, and coincident-endpoint
cases.  It crosses maximal Abel sign-block boundaries without assigning a
sign to an individual exchange.

#### Proof

Expand the right side of `(3.1)`.  The coefficient of `Z_1` is `t_1`, the
coefficient of an interior `Z_r` is `t_r-t_(r-1)=omega_r`, and that of
`Z_j` is `t_j-t_(j-1)=omega_j`.  This proves `(3.1)`; `(3.2)` is its final
endpoint and `(3.3)` is the definition of `Z`.  QED.

## 4. Exact inter-block exchange flow

Put

```text
Psi_q=Psi(T_q),       Psi_(-1)=0,
C_q=Psi_q-Psi_(q-1),
C_q^+=max(C_q,0),     C_q^-=max(-C_q,0).             (4.1)
```

### Proposition 4.1 (causal compensation equivalence; **PROVED**)

The following are equivalent:

1. `Psi_q>=0` for every maximal sign-block endpoint;
2. there are nonnegative flows `pi_(p,q)` for `p<q` and leftovers `L_p>=0`
   satisfying

   ```text
   sum_(p<q)pi_(p,q)=C_q^- ,
   sum_(q>p)pi_(p,q)+L_p=C_p^+.                      (4.2)
   ```

Whenever these hold, the exact block coboundary is

```text
C_q=L_q+sum_(r>q)pi_(q,r)-sum_(p<q)pi_(p,q),         (4.3)
```

and summing it gives

```text
P_(k,ell)(u)=Psi_Q=sum_q L_q>=0.                     (4.4)
```

#### Proof

If `(4.2)` holds, summing the supply minus demand through any prefix leaves
the nonnegative unused supply there plus any flow reserved for later
demands.  This is `Psi_q>=0`.

Conversely, process blocks from left to right, storing the unused amounts
of earlier `C_p^+`.  At a negative block, `Psi_q>=0` says that stored supply
is at least its demand, so take greedily from the earliest stored supplies.
At the end, declare every unused supply to be `L_p`.  This constructs
`(4.2)`.  Subtract demand from supply to obtain `(4.3)`; all internal flows
cancel in the full sum, proving `(4.4)`.  QED.

Thus GQAC_1 is an exact cross-block compensation condition.  It does not
claim any `C_q` is nonnegative and does not compare individual quantile
cells.

## 5. First analytic obstruction

The coefficient geometry alone cannot prove GQAC_1.  QTI_1/QBD_1 fixes the
positive masses, staircase path, rungs, and sign blocks, but imposes no sign
constraint on the actual values `D_cd`.  Assigning `D_cd=-1` on the first
block and zero on all later blocks preserves every coefficient, marginal,
staircase, rung, and block identity while making `Psi_0<0`.

For the actual response, `(2.2)--(2.3)` shows that each `Psi(T)/T` is a
difference of two positive normalized owner-response means.  Statewise
nonnegativity supplies no order between those means.  The accepted
fixed-middle, MON/FOSD, PSD, cellwise, and maximal-block obstructions rule
out promoting any of those stronger interfaces to the missing comparison.

Therefore the first actual-specific step is exactly GQAC_1 for the literal
owner response.  This formal obstruction does not refute GQAC_1; it proves
that a proof needs new global owner-response cancellation beyond the frozen
Hahn/quantile coefficients.

No MCLP or downstream conclusion is made here.
