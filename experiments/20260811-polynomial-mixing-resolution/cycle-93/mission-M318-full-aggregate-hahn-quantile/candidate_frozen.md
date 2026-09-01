# M318 frozen analytic candidate: GQAC_1

Date: 2026-08-14 UTC.

Status: frozen before any `k=13` computation.

## Imported exact notation

Let the maximal Abel sign blocks from QBD_1 be ordered along the canonical
quantile staircase as `q=0,...,Q`.  Write

```text
C_q=Phi_(b_q)-Phi_(a_q-1),
Psi_q=sum_(j=0)^q C_j=Phi_(b_q),
Psi_(-1)=0.
```

Every `C_q` and `Psi_q` retains all `k` middle phases and every supported
quantile cell in the stated block or prefix.

## GQAC_1

The predeclared exchange-flow candidate specializes exactly to

```text
(GQAC_1)  Psi_q(k,u,ell)>=0
          for every canonical maximal sign-block endpoint q.     (1)
```

Equivalently, put `C_q^+=max(C_q,0)` and
`C_q^-=max(-C_q,0)`.  There must exist nonnegative causal exchange flows
`pi_(p,q)` with `p<q` and nonnegative leftovers `L_p` such that

```text
sum_(p<q) pi_(p,q)=C_q^-                         for every q,
sum_(q>p) pi_(p,q)+L_p=C_p^+                    for every p.     (2)
```

Thus every negative complete block is paid by earlier positive complete
blocks, and the exact global exchange/coboundary identity is

```text
C_q=L_q+sum_(r>q)pi_(q,r)-sum_(p<q)pi_(p,q),
P_(k,ell)(u)=sum_q C_q=sum_q L_q>=0.                    (3)
```

The equivalence of `(1)` and `(2)` is the finite greedy inventory lemma:
every prefix has enough preceding supply exactly when each demand can be
met causally.  This is not positivity of a cell or block, and it does not
compare `Xbar` and `Ybar` by MON/FOSD, PSD, or one-direction Abel-kernel
monotonicity.  It is a full-aggregate cross-block compensation statement.

Because the terminal maximal block ends at `b_Q=k-1`, QBD_1 gives

```text
Psi_Q=P_(k,ell)(u).
```

Hence GQAC_1 is sufficient for MCLP_1.  This file asserts sufficiency only;
whether GQAC_1 holds is the mission's falsifiable question.
