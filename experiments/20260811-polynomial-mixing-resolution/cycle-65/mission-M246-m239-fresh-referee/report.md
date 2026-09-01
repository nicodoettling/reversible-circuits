# M246 report: fresh referee of frozen M239 YCM

Date: 2026-08-14 UTC.

## Verdict

**ACCEPT**, with zero material objection. Frozen M239 proves that, for every
odd `k>=3` and `2<=ell<=(3k-1)/2`, the exact M226/M229 one-run
coefficients obey

    |sum_(y=2)^ell c^Y_(k,y)|<=7000 sqrt(ell)/k.   (YCM)

This is an analytic all-rank result. Finite checking is secondary
falsification evidence only.

## Decisive audit findings

- M239's full inventory passes, with advertised checksum-file digest
  `66c78dd3aab40acc6166857f96f3afd90bba64184d7f139783d395667d21f542`.
  The complete M226, M229, M241, and M243 dependency inventories also pass.
- Fresh cancellation of GG1's survivor, short-parent, and long-parent sources
  gives `<23b_x`, `<14b_x`, and `<135b_x`, hence `G_k(x)<172b_x`.
- The small-A proof is valid with the safe triangle
  `Q|P-1|+|Q-1|`, giving `72y b_y/k`. The theorem does not rely on the
  optional sharper `40` aside.
- The small/middle/below-seam/seam/above-seam domains yield the stated
  envelopes `3000,176,70,242`. Every G call lies in M229's corrected domain
  `1<=x<=L-1`.
- The four prefix contributions total `6352+70+484=6906<7000`.
  The same analytic partition covers `k=3,5,7` because their small-SG range
  is empty.

The clean-room exact/certified checker passes all odd `3<=k<=101`, including
explicit small-rank boundary rows and the sharper `6906` prefix assertion.

## Numbered objections

1. Material objections: none.
2. Nonmaterial clarity note: the optional small-A constant `40` should not be
   needed or cited; the audited proof uses the safe constant `72`.

## Scope

This report accepts **YCM only**. It does not infer or re-audit TCM, WBE, DE,
DV, J2, PCR, any gap or mixing-time claim, or either Terminal.
