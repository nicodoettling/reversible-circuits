# M289 fresh immutable audit request

Please appoint a genuinely fresh referee who has not participated in M289.
Treat this directory and all required predecessors as immutable, initialize a
new role directory before substantive inspection, verify this mission's exact
inventory and checksum ledger, and import no M289 code into any independent
checker.

## Claim to audit

For every odd `k>=3`, under the frozen M276/M279 collision and normalization
conventions,

```text
||sum_(1<=s<k/2) qhat_s(Phi_s^D-Psi_s^D)||_1=O(1/k),
qhat_s=q_s a_F(s),
```

with literal collision support, cyclic phases, two B seams, the A wrap seam,
ordered factors, product kind, and endpoint normalization retained.

## Required independent reconstruction

1. Derive the B raw coefficient `beta_s`, the A marked and untouched
   coefficients, and the cross-block coefficient `4u M_l/k^2` directly from
   ordered first-two-factor completion counts.  Check raw masses `12a_L` and
   `12a_F`.
2. Reconstruct the exact normalizer collapse (3.2) without renormalizing
   `qhat`, and check the `O(k^-2)` normalizer remainder.
3. Re-derive both phase operators, including both B seams, A wrap, reflection,
   midpoint, and the restricted derivative coordinates.
4. Audit Lemma 1 at `s=1`, `s=j`, `l=j,j+1,k-1,k`, the middle seam, and
   reflection.  Verify the weighted BV hypotheses for `q_s a_L(s)` and
   `b_s`, including the Borel tail and constant tail.
5. Audit Lemma 2 for `r=1,2`, both sides of the active/inactive cutoff, the
   reflected support, midpoint, and both zero endpoints.  Separately verify
   the untouched coefficient (6.4).
6. Check that all error profiles have the stated `l1` guards before applying
   the phase BV operators, and that no adjacent-profile triangle argument or
   M211 pointwise `IKBE-b` claim has entered the proof.
7. Independently falsify the literal boundary formulas at least at `k=3` and
   `k=5`, if desired, but do not use finite scans as an asymptotic proof.

Return **ACCEPT** only if the theorem is complete.  Otherwise return
**REJECT** with numbered objections and the first false or unproved displayed
statement.  Report the checksum-file top digest and exact inventory.

## Scope firewall

Audit CEBV only.  Make no CIBV, DOR, SET, PBV, FD, FCL1, spectral-gap,
polynomial-mixing, or Terminal A/B inference.
