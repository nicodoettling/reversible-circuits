# M217 Checkpoint

## Start checkpoint

- The owned directory and plan were initialized before substantive work.
- Target: only original signed averaged DE, with literal profiles and
  q_hat weights.
- Pointwise IKBE-b is accepted as refuted; it will not be resurrected.
- M192/M195, M199/M207, and M211/M215 are immutable; complete hash gates are
  next.
- IKBE-a/DV, DE, conditional J=2, and all downstream claims are open at
  start.

## Immutable gate

- Every SHA256SUMS entry in M192/M195, M199/M207, and M211/M215 passed.
- Their checksum-file digests are, in that order:
  4c6cd295cd2a8259d396f8f9218e7f98746e7d005a255cfb4f14dc2d96336c60,
  1f0c398bd92edf37e16880c239e0bf65d63622e1de9c2c9904a26fd560d93f0a,
  1de555bba9affef15b7f2b9585de7955f9d9bd23fc838c76508186d7438c25ed,
  817988cd61ed290b6ce86e90510ee6e1a3358339bff5c8ca757c26acd2e1979d,
  79f3e0f614a6cde4e3e4bd36ce55e217b35416f68470c6deab93598877874225,
  and 59b4bade09ebd0cdaf11265544345ad411d1c482c2353213b3eee8208f938928.
- All six predecessor missions remain unedited.

## Halfway substantive checkpoint and cap

- The exact disjoint A split weight is

      q_hat_s =
        [k/(k-1)] [b_s b_(k-s)/b_k] [1-gamma_F(s)].

  Writing a_L=1-gamma_L and a_F=1-gamma_F, the identity
  q_hat_s=q_s a_F(s) first cancels the A conditional normalizer exactly.
  Inserting the literal M199 profiles then gives

      DE_Z = S_Z + K_Z + N_Z,

  where S_Z is the complete surviving-face B-minus-A block, K_Z is the
  complete Borel fragmentation/fresh-cycle block, and

      N_Z=sum_s q_s[a_F(s)/a_L(s)-1]B_s^Z.

  The exact ratio satisfies

      a_F/a_L-1 =
        2(k-1)/[R(k-s)(D-s)a_L]=O(k^-2)

  uniformly on s<k/2. Since B_s^Z/a_L=Phi_s^D(Z)<=3, this proves
  N_Z=O(k^-2). All terms remain in the original signed sum; no pointwise or
  kindwise absolute bound is used.
- Uniform Stirling bounds give q_hat_s<=C b_s for s<=k/2 and hence

      sum_(s>=m) q_hat_s <= C/sqrt(m).

  Thus the macroscopic region s>=epsilon k has total mass O(k^-1/2).
  This makes M211's O(1) bulk face counterterm harmless at scale l~k,
  since sqrt(l)/k is then Theta(k^-1/2).
- The same tail estimate is too weak for fixed l, whose target scale is
  O(k^-1). Consequently the M211 bulk counterterm does not by itself prove
  signed DE, and no cancellation is inferred from finite signs.
- The exact remaining standalone lemma is the weighted boundary envelope
  for the two unresolved signed blocks:

      |S_Z+K_Z| <= C sqrt(l)/k,

  uniformly for Z=X_l,Y_l. It must retain cancellation between S_Z and K_Z,
  the complementary
  X face, all seams, collision multiplicities, and exact normalizers.
- Formula-only odd k<=15 Y diagnostics remain bounded after target scaling
  (maximum about 0.406); they are calibration only and prove no universal
  bound.
- Verdict at cap: strict exact signed-DE reduction with proved
  macroscopic-mass and normalizer-remainder lemmas. DE, IKBE-a/DV,
  conditional J=2, and all downstream claims remain open.

## Final freeze checkpoint

- The frozen algebra is

      DE_Z=S_Z+K_Z+N_Z,
      N_Z=sum_s q_s[a_F(s)/a_L(s)-1]B_s^Z,

  with S the complete surviving-face B-minus-A block and K the complete
  fragmentation/untouched-cycle B-minus-A block. For X, K retains the
  complementary two-run face, seam indicators, and every collision
  multiplicity.
- The exact ratio

      a_F/a_L-1=2(k-1)/[R(k-s)(D-s)a_L]

  and `a_L>=1/2` prove `N_Z=O(k^-2)`.
- The proved tail

      sum_(s>=m)q_hat_s<=C/sqrt(m)

  controls macroscopic splits at `O(k^-1/2)`. This is target-sized for
  `l~k` but not for fixed `l`.
- The first open lemma is exactly

      |S_Z+K_Z|<=C sqrt(l)/k,   Z=X_l,Y_l.             (WBE)

  WBE would imply DE together with the normalizer bound. It must be proved
  as a signed bound, not by splitting channels or absolute values.
- The deterministic standard-library formula checker regenerated valid JSON
  for odd `k=3,5,...,15`; its maximum scaled Y value is about `0.406`.
  This is calibration only.
- Hygiene check found no `__pycache__` or temporary file. M192/M195,
  M199/M207, and M211/M215 remain immutable. The exact M217 artifact set is
  ready for final checksums.
- Freeze verdict: strict reduction, not a proof or refutation of DE. Request
  a fresh immutable audit of q_hat, the A-normalizer cancellation, block
  signs/completeness, (5.1)--(5.2), the macroscopic tail, and WBE
  sufficiency. No conditional J=2 or downstream inference is made.
