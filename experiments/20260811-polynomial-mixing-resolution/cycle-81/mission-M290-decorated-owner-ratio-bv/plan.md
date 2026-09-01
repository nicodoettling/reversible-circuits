# M290 plan: decorated owner-ratio bounded variation

Date: 2026-08-14 UTC.

## Objective and scope

Starting only from the accepted M261/M264 and M276/M279 identities, prove,
strictly reduce, or refute the decorated owner-ratio variation statement

```text
(DOR)  sum_(ell=2)^(n-3) |eta(Delta Q_ell)| = O(1/k),
       n=3k, odd k>=3,
```

where

```text
Q_ell(s)=sum_(a,b)(e^2 kappa_ab(s)-1) C_ab^s(ell),
Delta Q_ell=Q_(ell+1)-Q_ell.
```

Here `eta` is the complete centered first-pair source law.  Both live source
channels, both triangle/double kinds, all `IS/IN/X` topologies, every cyclic
phase, literal owner sizes, and all one-run/two-run seams remain combined
inside the final absolute value.  This mission makes no PBV, FD, FCL1,
spectral-gap, polynomial-mixing, or Terminal inference.

## Target and convention

Permutations compose as `(pq)(x)=p(q(x))`, with displayed factors multiplied
left-to-right.  The audited target is the balanced first fixed cell of the
auxiliary uniform minimal length-`n-1` factorization law of the ambient long
cycle under the nonlazy cyclic rank-two quotient kernel.  It is not the
uniform identity-word law and not the lazy exact same-product `{3,4,5}`
heat-bath chain.

## Source gate

Before using any formula, verify the immutable inventories and controlling
status ledgers for M91/M94, M261/M264, M267/M270, M276/M279, M280/M283, and
M285/M287.  Treat all sign, PBV, minority-mass, and mixing statements as open
unless the frozen source explicitly proves them.

## Analytic workflow

1. Reconstruct the literal interval-owner formula for `Delta Q_ell`, including
   endpoint signs and the outer source coefficients.
2. Expand
   `rho_ab=e^2 kappa_ab-1` without losing the diagonal/off-diagonal
   distinction.  Seek uniform first-order control
   `rho_ab=O(1/d_a+1/d_b)` and the sharper diagonal second-order remainder.
3. Disintegrate by positive cyclic compositions and support anchor, retaining
   all owner intervals and two-run seams.  Perform cancellation before any
   triangle inequality across channels or kinds.
4. Test whether the remaining signed coefficient is a convolution/Abel
   derivative with summable total variation.  State the first standalone
   unresolved coefficient lemma if the sign or `1/k` scale does not close.
5. Only after fixing a candidate universal inequality may one compact exact
   checker be run.  It may falsify a formula or candidate inequality but may
   not be promoted from finite positivity.

## Proof obligations and expected failure modes

- exact lag range `2<=ell<=n-3`, reflection/endpoints, and the definition of
  `Delta`;
- no loss of source masses, raw triangle/double lifts, cyclic stabilizers, or
  owner/run topology;
- no separate absolute values on `J=1,2`, `T/D`, `IS/IN/X`, collision, or
  decoration;
- distinguish small owners, especially `d=1,2`, from bulk ratio expansions;
- guard against a seam term of order one per phase or an Abel coefficient
  mass of order `sqrt(k)`;
- label any finite row exact-finite only;
- freeze a theorem, a strict falsifiable reduction, or a concrete
  obstruction, with its first open lemma and a fresh-audit request.

