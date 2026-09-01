# M272 fresh immutable audit request

Please audit the frozen M272 bundle without editing it.

Required checks:

1. Verify every payload against `SHA256SUMS` and record the checksum-file
   digest.
2. Re-derive the literal adjacent `Phi_(j,u)/Phi_(j,u+1)` couplings,
   especially the channel-two conditional second-factor normalization.
3. Check the monotone split crossing mass
   `Pr(S<=u<T)=-D_u` and the full path telescoping identity (5.6), including
   the raw-law disintegrations.
4. Re-derive the owner-charge phase normalization and the outside `1/n`
   in (5.8); do not import it from M267.
5. Check that both channels, triangle/double kinds, literal phase, ordered
   lifts, owner-pair `kappa`, and the middle factor survive until the
   displayed scalar.
6. Audit the exact channel-one collision law (2.5) and every range of the
   critical-Borel bounded-variation proof, especially (3.5) and the two
   junction terms.
7. Re-derive the channel-two `gamma_L/gamma_F` laws, their total masses,
   the nonzero disjoint endpoint, and the vector-valued Abel identity (4.3).
8. Confirm that only the triangle submeasure is bounded positively; CSBV and
   CEBV retain their complete signed sums before lag-l1.
9. Re-run both exact checkers and confirm the independent channel-one
   coefficient assertion, reflection, shared-endpoint masses, disjoint
   endpoint, and vector Abel identity.
10. Treat `(CSBV)`, `(CEBV)`, `(CIBV)`, `(DOR)`, SET, PBV, FD,
    SR/TPR, FCL1, direct-L1, gap, mixing, and Terminal as unresolved.

The finite tables may falsify formulas or an exact cancellation claim.  They
must not be used as a uniform estimate, sign proof, or evidence against SET.
