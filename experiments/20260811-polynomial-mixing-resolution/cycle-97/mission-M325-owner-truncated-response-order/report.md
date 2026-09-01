# M325 final report: owner-truncated response order

Date: 2026-08-14 UTC
Verdict: **reject `TOEC_1`; keep `AOTI_1`; `GQAC_1` remains unresolved**

## Results

1. **Verified source lock.** All 176 payloads in the sixteen required
   M274--M322 packages and all 76 payloads in the nine direct raw owner-law
   packages pass.  The nine formula files used directly are separately
   SHA-locked.
2. **Proved exact.** The actual truncated positive and negative exterior
   measures have common mass `T`.  Expanding the literal owner response by
   full completion signatures gives
   `Psi(T)=sum_sigma w(sigma)(m_T^+-m_T^-)`, with actual rational Borel
   weights and every middle/target phase retained.
3. **Refuted analytically.** The predeclared same-full-signature rational
   transport `TOEC_1` fails at `k=5,u=2,ell=2,T=mu_5`.  The negative seam
   state `{0,1}{5,7}` contributes positive mass to signature
   `{{(1,0),(2,0),(12,2)}}`, while no positive nested state has any
   singleton owner.
4. **Proved exact, strictly weaker.** Dropping inactive owners yields the
   active-owner identity `(AOTI_1)`, a weighted sum of same-owner and
   cross-owner signed incidence masses.  Active-profile domination
   `(AOEC_1)` would suffice for GQAC, but is unresolved and was not tested.
5. **No computation.** The analytic support obstruction made the optional
   `k=15` guard unnecessary.

## Scope firewall

The obstruction refutes only `TOEC_1`.  It does not refute actual
`GQAC_1`, `MCLP_1`, or any earlier exact QTI/QBD identity.  No inference is
made to GOCI, OCI, CP, MS, FCL1, spectral gap, mixing, or Terminal.

