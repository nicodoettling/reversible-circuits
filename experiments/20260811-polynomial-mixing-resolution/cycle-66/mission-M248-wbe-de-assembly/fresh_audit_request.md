# M248 fresh immutable audit request

Audit frozen mission M248 from its inventory before accepting any conclusion.

Required checks:

1. Run `sha256sum -c SHA256SUMS` in M248 and in all eight frozen dependency
   missions M217/M222, M226/M229, M235/M238, and M239/M246.
2. Confirm the exact M226/M229 identities
   `S_Y+K_Y=sum c^Y` and
   `(S_X+K_X)-(S_Y+K_Y)=sum c^T` on the complete cutoff domain, including
   M229's corrected `G_k` domain.
3. Confirm that accepted YCM constant `7000` and accepted TCM constant `160`
   imply Y-WBE `7000` and X-WBE `7160`, preserving every literal kind, seam,
   and collision multiplicity.
4. Re-derive from M217/M222
   `DE_Z=S_Z+K_Z+N_Z` and
   `a_F/a_L-1=2(k-1)/[R(k-s)(D-s)a_L]`.
5. Independently verify `a_F/a_L-1<=16/(3k^2)`, `|N_Z|<=16/k^2`, and
   `16/k^2<=4sqrt(ell)/k` for the exact domain, hence DE constants `7004`
   and `7164`.
6. Verify that the M192 Abel endpoint is outside DE and that M248 makes no
   DV, conditional J2, PCR/WPCR/SCBR, gap, mixing, or Terminal inference.

The referee should freeze a numbered objection list and an ACCEPT/REJECT
verdict without editing M248 or any predecessor.

