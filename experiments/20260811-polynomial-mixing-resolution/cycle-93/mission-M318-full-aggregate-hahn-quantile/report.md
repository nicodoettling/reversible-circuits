# M318 final report: full-aggregate Hahn/quantile compensation

Date: 2026-08-14 UTC.

Verdict: **inconclusive / keep the exact identity; `GQAC_1` remains
unproved.**

## Stable results

1. **PROVED (import-locked).** All fourteen required predecessor packages
   and all 154 cited payloads verify.  Their semantic scope stops before
   MCLP.
2. **PROVED.** At every quantile staircase endpoint,
   ```text
   Psi(T)=sum_c lambda_c(T)Xbar_c-sum_d rho_d(T)Ybar_d,
   ```
   with both truncated marginal masses equal to `T`.  At QBD block endpoints
   this is `Psi_q=Phi_(b_q)=sum_(p<=q)C_p`; at `T=mu_k` it is the complete
   `P_(k,ell)(u)`.
3. **PROVED.** The global staircase exchange is the exact Abel coboundary
   ```text
   Psi(t_j)=t_j Z_j-sum_(r<j)t_r(Z_(r+1)-Z_r),
   ```
   including horizontal, vertical, and coincident-endpoint steps and all
   middle phases.
4. **PROVED.** Frozen `GQAC_1` (all canonical block-endpoint prefixes
   nonnegative) is equivalent to the exact causal compensation-flow law.
   Consequently it is sufficient for the complete aggregate to be
   nonnegative.  Sufficiency is not a proof that the lemma holds.
5. **UNRESOLVED / first proof obstruction.** Frozen Hahn/quantile coefficient
   geometry does not order the two truncated owner-response means.  An
   actual-owner inequality beyond QTI/QBD is required to sign the prefixes.
6. **EXACT FINITE FACT ONLY.** The sole `k=13` guard tests 648 frozen GQAC
   prefixes in 216 full rows: all are positive, as are all 216 complete
   aggregates.  QTI, QBD, and reflection checks pass exactly.  This is no
   all-rank evidence or inference.

## First unproved lemma

For every admissible odd `k`, every allowed `(u,ell)`, and every canonical
maximal Abel sign-block endpoint `q`, prove for the literal all-middle owner
response that

```text
sum_(p=0)^q C_p(k,u,ell)=Phi_(b_q)(k,u,ell)>=0.       (GQAC_1)
```

It may use cancellation across cells, middle phases, and Abel sign blocks,
but not fixed-middle signs, MON/FOSD, PSD, cellwise positivity, maximal-block
positivity, one-direction Abel monotonicity, or a finite trend.

## Firewall

M318 proves no MCLP, GOCI, OCI, CP, MS, FCL1, spectral-gap, mixing, or
Terminal conclusion.  The frozen candidate survived one rank but remains
unproved and requires a genuinely fresh immutable audit.
