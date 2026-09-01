# M307 plan: mixed-sign exterior quantile pairing

Date: 2026-08-14 UTC.

## Objective and exact scope

Continue only from the accepted M300/M303 channel-one all-middle identity.
Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, odd `k>=3`,
`n=3k`, `1<=u<k/2`, and `2<=ell<=3k-2`.  The target is the first
separated fixed cell of the auxiliary uniform minimal long-cycle
factorization law under the nonlazy cyclic rank-two quotient kernel.  This
is not the global uniform identity-word law and not the lazy exact
same-product `{3,4,5}` heat-bath chain.

The accepted identity is

```text
P_(k,ell)(u)=sum_c[x_c Xbar_c-y_c Ybar_c],
sum_c x_c=sum_c y_c=:mu_k,
```

where every `Xbar,Ybar` already sums all `k` phases of the fixed middle cut
class.  Equivalently it is M300's mixed-`R_c` EHA_1 formula.  MCLP_1 asks
that this scalar be nonnegative.

## Candidate frozen before computation: `(QCP_1)`

Define cumulative positive and negative cut masses

```text
X_c^*=sum_(i<=c)x_i,       Y_d^*=sum_(j<=d)y_j,
X_0^*=Y_0^*=0,
```

and the canonical increasing quantile transport

```text
pi_cd = length((X_(c-1)^*,X_c^*] intersect
               (Y_(d-1)^*,Y_d^*]).
```

Then `pi_cd>=0`, its row sums are `x_c`, and its column sums are `y_d`,
regardless of the signs of the cumulative imbalances `R_c=X_c^*-Y_c^*`.
The fixed analytic candidate is

```text
(QCP_1)  Xbar_c >= Ybar_d whenever pi_cd>0,
```

for every allowed `(k,u,ell,c,d)`.

This is a mixed-sign-aware mass pairing, not a one-direction Abel
monotonicity statement.  Indeed, when `R_c` changes sign, the support of
`pi` crosses both sides of the cut diagonal.  If `(QCP_1)` holds, then

```text
P_(k,ell)(u)=sum_(c,d)pi_cd(Xbar_c-Ybar_d)>=0,
```

so it proves MCLP_1 and hence GOCI_1.  It is stronger than MCLP_1 because
it signs each nonzero transport cell, but substantially narrower than all
pairwise cross/internal comparisons.

## Analytic-first procedure

1. Verify the frozen M300/M303 and cited dependency inventories.
2. Derive the transport identity, characterize `pi` support directly from
   the mixed cumulative masses, and retain every endpoint/reflection.
3. Attempt a response comparison only on the actual quantile support, using
   the full middle-phase owner-correlation formula.
4. If the comparison does not close analytically, run exactly one new rank:
   `k=9`, `n=27`, all four middle cut classes and all 24 admissible lags.
   Use exact standard-library arithmetic and stop at the first lexicographic
   negative QCP transport cell while still recording whether aggregate MCLP
   cells remain positive.
5. Freeze either a proof or the first exact obstruction and state the next
   weaker combined coefficient lemma.

## Prohibited shortcuts and conclusions

- Do not condition on one fixed middle chord.
- Do not invoke pointwise MON/FOSD, signed PSD, raw-atom positivity, or a
  common-direction Abel monotonicity.
- Preserve the actual mixed signs of `R_c`; do not replace them by absolute
  values in an alleged equality.
- A finite `k=9` result has no all-rank implication.
- Do not infer GOCI_2, OCI/CP, OS+, MS, FCL1, a gap, mixing, or a Terminal
  conclusion without the complete theorem and fresh audit.

## Expected failure modes

- The quantile transport may cross the correct cut marginals while a single
  supported response cell has the wrong sign; that would refute QCP_1 but
  not MCLP_1.
- A response comparison may require cancellation between several transport
  cells, forcing a weaker prefix- or block-compensated inequality.
- Reflection may duplicate a witness; both lags must be reported.
