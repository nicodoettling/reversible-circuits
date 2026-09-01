# Exact marked-context inheritance

Date: 2026-08-12.  This note concerns only contextual split statistics in
the nonlazy minimal-long-cycle parking projection.  It is not a statement
about the identity-bridge chain `K`.

## 1. Synthetic attachment contexts

Fix a selected root branch and retain only the ordered root-attachment
factors relevant to its positional split weight.  Write

```text
O_1<...<O_K
```

for this external attachment chain, with active factor `O_(R+1)`; thus
`R` attachments precede the active factor.  The other branches may be
taken to be unit branches: multiset-word deletion gives the same local
statistic after the outside orbit and scan factors are divided out.  Denote
the resulting normalized local statistic by `Phi_(K,R;B)`.

Inside the selected branch, condition on root composition

```text
C=(c_1,...,c_k),        t=c_k,
```

and write `I_1<...<I_k` for its attachment chain, with `I_1` the
rightmost/last-branch attachment.  Deleting all other factors from a
uniform parking-multiset word leaves a uniform shuffle of the two chains
`O` and `I`.

## 2. Negative-hypergeometric recursion

Let `J` be the number of `I` factors preceding `O_(R+1)`.  Exactly `j`
inner and `R` outer factors occur before the active outer factor.  Hence

```text
nu_(K,R,k)(j)
 =P(J=j)
 =binom(R+j,j) binom(K-R-1+k-j,k-j)/binom(K+k,k),   (2.1)
```

for `0<=j<=k`.

**Theorem (marked inheritance).**  If `t>B` and `v` is the standardized
macro of the last inner branch, then pointwise in `v`,

```text
Phi_(K,R;B)(u)
 =sum_(j=1)^k nu_(K,R,k)(j)
      Phi_(K+k,R+j;B)(v).                           (2.2)
```

The child statistics on the right are synthetic attachment contexts; they
need not be actual root-composition contexts of the same ambient tree.

### Proof

Expose the two attachment chains in the constrained-shuffle bijection.
Every binary shuffle has the same number of inverse insertions of the
deleted factors.  If `J=0`, the active factor precedes `I_1`; the
right-spine cut factor inside the last branch cannot form the marked
favourable pair, so this class contributes zero.

Fix `J=j>=1`.  Delete every current-level factor outside the last branch,
but retain its attachment factor as a dummy unit-branch attachment.  The
result has `K+k` external attachment factors.  Exactly `R+j` precede the
same active factor.  Conversely, from a marked word in this synthetic
`(K+k,R+j)` context and a two-chain shuffle with `J=j`, insert the deleted
branch words in their recorded gaps.  Chain order, the marked scan site,
and the favourable rank-two outcome recover both the source and the
shuffle uniquely.

Thus deletion and insertion are inverse on marked favourable
word/outcome pairs.  Dividing by source-orbit size, the three-state fibre,
the scan count, and the corresponding `alpha` leaves precisely the binary
shuffle fraction (2.1).  Summing over `j>=1` proves (2.2).  No scalar
replacement by one ordinary child context has been made.

Vandermonde's identity gives

```text
sum_(j=1)^k nu_(K,R,k)(j)
 =1-nu_(K,R,k)(0)
 =1-binom(K,R+1)/binom(K+k,R+1)
 =D_(K,R)(k).                                       (2.3)
```

Every synthetic child context has stationary mean
`w_(t-B)w_B/w_t`, by the exact root-composition split flow.  Averaging
(2.2) and using (2.3) proves the deep line of the closed conditional-mean
formula.

## 3. Why `(k,0)` is false

The tempting replacement

```text
Phi_parent =D_(K,R)(k) Phi_(k,0)
```

is false first at ambient `r=4`.  Take parent context
`K=1,R=0`, coarse `(4)`, refinement `(3,1)`, and inner composition
`C=(3)`.  On the two last-branch macros `(0,0)` and `(0,1)`, the parent
values are both `1/3`.  The ordinary child `(1,0)` values are `1` and
`1/2`, so multiplication by `D=1/2` predicts `1/2` and `1/4`.

Equation (2.2) instead has `j=1`, weight `1/2`, and synthetic child
`(K',R')=(2,1)`.  That child has values `2/3,2/3`, giving the correct
`1/3,1/3`.

`context_map_audit.py` records the scalar failure.  The corrected
`marked_context_inheritance_audit.py` has zero mismatches in all
`898=1+7+36+163+691` nonvacuous exact checks through ambient `r=7`.
These computations are falsifiers only; the proof is the marked
deletion/insertion bijection above.

## 4. Repeated extreme geometry

The update does not force a rightmost (`R=0`) child context.  If
`R=K-1` and `j=k`, then

```text
(K',R')=(K+k,K+k-1),

nu_k=binom(K-1+k,k)/binom(K+k,k)=K/(K+k).           (4.1)
```

Thus the same extreme geometry repeats with probability weight close to
one when `K>>k`.  Along a unary spine (`k=1`) the depth-`d` continuation
weight telescopes exactly:

```text
product_(h=0)^(d-1) (K+h)/(K+h+1)=K/(K+d).         (4.2)
```

It is only polynomially suppressed and is essentially unsuppressed for
`d<<K`.  Hence an arbitrary-context quotient cost cannot be declared a
one-time loss.  Any surviving proof must carry the full marked mixture
and its edge loads, not only conditional means or the pair `(k,0)`.
