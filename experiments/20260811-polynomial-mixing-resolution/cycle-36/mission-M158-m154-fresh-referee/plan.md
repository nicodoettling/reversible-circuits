# M158 plan: fresh referee of frozen M154

Date: 2026-08-13 UTC.

## Objective

Audit the immutable M154 inner-Nielsen/parity-voltage reduction at exactly
its stated nonterminal scope. Verify the assigned SHA-256 values before
substantive review. Do not modify M154 or coordinator files.

## Claims under review

1. The explicit chronological Hurwitz word realizes simultaneous conjugation
   by a chosen original factor, with the claimed order and length bound.
2. Literal signed-Hurwitz equivalence equals equivalence modulo inner
   conjugation for product-one generating tuples.
3. For accepted `d>=5` M135 matching subfamilies, M141 upgrades this to the
   exact absolute-quotient/zero-relative-parity-voltage criterion, retaining
   the transporter word-length caveat.
4. Exact finite warnings: two framed literal orbits at `d=3`; the
   `S_4/V_4` block system and accepted witness at `d=4`; only transitivity and
   primitivity of the `8,400`-point quotient action at `d=5`.

## Method and limits

- Read the required project skill/core sources and accepted M135/M137 and
  M141/M143 scopes.
- Audit the universal algebra line by line, including action orientation,
  quotient freeness, transporter uniqueness, and length accounting.
- Write a clean-room deterministic checker in this directory. It may use
  bounded Schreier--Sims at degree `120`, but will not enumerate the full
  degree-`8,400` action group or compute its order.
- Record machine-readable results, an explicit ACCEPT/REJECT report with
  numbered objections and claim scope, then freeze owned bytes.

Target: Hurwitz action orbits on product-one generating transposition-class
factorizations; no sampler, gap, or mixing conclusion.

Permutation convention: `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right. Right Hurwitz move:
`R_j(a,b)=(b,b^{-1}ab)`.

Expected failure modes: a chronological-order reversal in the explicit
braid; a transporter orientation error; silently replacing the inner quotient
by independent coordinate conjugation; an invalid connectedness claim after
`S_4/V_4`; or extrapolation from `d=5` finite primitivity.
