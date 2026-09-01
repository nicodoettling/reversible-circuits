# M276 fresh immutable audit request

Please audit this frozen referee bundle without modifying it or M272.

1. Verify the M276 inventory, M272 digest
   `af54db1f8bf948ee15439aeee5330d5b18ea7101e2dba062c47c8f949262eed3`,
   and every cited dependency inventory.
2. Confirm the material objection: at `a=k-1`,
   `rho_A(k-1)=Theta(1/k)`, contradicting M272's asserted
   `O(k^-3/2)` bulk summand bound, and M272's stated far-tail range does not
   literally cover this term.
3. Audit the append-only repair (7.6)--(7.9) in `proof_audit.md`, especially
   the variation of `g_k(c)=c nu_k(c)`, both junctions, and the long-cycle
   bulk derivative.
4. Independently confirm the raw channel normalizations, channel-two fair
   component choice, `-D_u` crossing law, path telescoping sign, and outside
   phase factor `1/n`.
5. Recheck `gamma_L,gamma_F`, shared masses, the nonzero disjoint endpoint,
   and the vector Abel identity.
6. Run `independent_check.py` and confirm that it has no project import and
   reads no predecessor/M272 artifact.
7. Keep `CSBV`, `CEBV`, `CIBV`, `DOR`, `SET`, `PBV`, `FD`, `FCL1`, every gap,
   mixing claim, and Terminal open.

Requested verdict: reject M272 as a self-contained frozen proof package;
accept the unaffected exact reductions; accept or reject M276's corrected
channel-one theorem separately.

