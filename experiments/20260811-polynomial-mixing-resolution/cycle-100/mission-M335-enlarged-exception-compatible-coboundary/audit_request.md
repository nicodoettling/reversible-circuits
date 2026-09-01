# M335 request for fresh immutable audit

Date: 2026-08-14 UTC

Please assign a genuinely fresh referee for frozen M335. The audit should:

1. verify the M335 top digest and every payload;
2. verify the ten frontier and fifteen raw-law source gates, using M329's
   append-only correction for M326;
3. independently derive the same-cell residual-support lemma;
4. rerun only the frozen `k=9,H_2` guard and verify the first token's two
   non-Touch checks, two `BadPref=false` checks, unchanged derived cell,
   positive original weight, and zero reverse residual masses;
5. verify the exact tokenwise `J` split and scalar exceptional-mass reduction;
6. enforce that compatible cancellation, exceptional Borel scales, MPCF, and
   every downstream theorem remain open.

The referee must not inspect another rank/row, seek an alternative surgery,
or turn the finite obstruction into an all-rank owner-law claim.

