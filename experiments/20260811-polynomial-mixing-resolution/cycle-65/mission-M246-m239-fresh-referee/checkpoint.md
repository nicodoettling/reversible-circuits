# M246 checkpoint

Status: initialized; no verdict.

The M246 role directory was created before substantive inspection.  The
planned audit is a fresh, YCM-only review of frozen M239, including independent
algebra and an independent exact/certified checker.  No M239 source file has
been modified or imported.

## Substantive checkpoint

Status: analytic audit complete in substance; provisional verdict `ACCEPT`
with no material objection, pending final artifact freeze.

- M239's advertised top digest is exactly
  `66c78dd3aab40acc6166857f96f3afd90bba64184d7f139783d395667d21f542`;
  all seven files in its inventory pass. The complete M226, M229, M241,
  and M243 inventories also pass, and their checksum-file digests equal the
  values quoted by M239.
- Independent cancellation of the three GG1 sources gives respectively
  `<23b_x`, `<14b_x`, and `<135b_x`. The short source becomes the
  weighted Borel convolution with `m=k-x`; the long source becomes the
  convolution with `M=D-x` after the exact `b_s`/kernel cancellation. All
  positive enlargements and ratio domains include `k=3`.
- In the small-`y` A case, the referee uses only the safe triangle
  `|QP-1| <= Q|P-1|+|Q-1|`, with `Q<=5`, `1-P<=4y/k`, and
  `Q-1<=16y/k`. Therefore `|A-2b_y|<=72y b_y/k`. The proof does not
  depend on the optional sharper `40` aside.
- The small B bound `234(y+1)b_y/k`, the middle bound, and the below/at/above
  seam envelopes `3000,176,70,242` check with their stated domains. Every
  `G` argument is in M229's corrected range `1<=x<=L-1`.
- Summing the four disjoint regions gives exactly
  `6352+70+484=6906<7000`; the analytic partition also covers `k=3,5,7`
  because their SG/small-`y` subrange is empty.
- A clean-room checker, importing no predecessor module or data, recomputes
  the exact rational formulas, uses a rigorous rational Taylor enclosure for
  `e`, and checks all boundaries through odd `k=101`. It passes, including
  explicit coefficient/prefix rows for `k=3,5,7`. This is falsification
  evidence only.

Provisional objections: none material. One anticipated clarity note is that
the optional sharper A-case constant `40` is unnecessary; the accepted
assembly is certified using `72`, as requested. No TCM, WBE, DE, DV, J2,
gap, mixing, or Terminal inference is made.
