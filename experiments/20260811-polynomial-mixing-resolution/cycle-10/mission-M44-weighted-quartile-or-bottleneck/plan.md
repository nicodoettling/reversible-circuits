# M44 plan — weighted quartile or complete bottleneck

## Exact target and convention

Permutations are maps on `[N]`, with `(pq)(x)=p(q(x))`, and words evaluate
as `t_1...t_m`.  Put `n=N-1`, `m=2n`, and let `F_N` be the connected
full-support identity words of length `m`.  With

```text
h_j=N-cycles(t_1...t_j),
Area=sum_(j=1)^m h_j,
H_N(a)=#{w in F_N:Area(w)=a},
```

the proof target is an explicit feasible `q_N` with

```text
1/4 <= sum_(a<=q_N)H_N(a)/|F_N| <= 1/2,
H_N(q_N)/sum_(a<=q_N)H_N(a) >= N^(-C)
```

for a universal `C`.  By M34 this would give inverse-polynomial conductance
for this original-full-`K` cut.  The alternative is a literal Terminal-B
sequence, which requires an upper bound on every `H_3,H_4,H_5` crossing and
every macro exit from `F_N`, with exact global smaller-side orientation.

## Inherited exact inputs

1. M38 gives the literal support-partition Mobius/cut-join recurrence for all
   `H_N(a)` and fixed-path weights, exact coefficients through `N=13`, and
   the universal no-cliff inequality
   `H_N(a+2)>=H_N(a)/(N-1)`.
2. M34 gives one padded-`H_3` crossing from every top-layer state with exact
   full-`K` probability at least `1/[6(m-2)M^3]`; `H_4,H_5` remain present.
3. The exact first-quartile ratios through `N=13` exceed `1/N`, while the
   `N=5` layer sequence is nonunimodal/non-log-concave.  Finite data is only a
   falsifier.
4. The connected/unrestricted bottom-path ratio is exactly
   `2^n n!/[N n^n]`, exponentially small, so a pointwise positive-transfer
   comparison is unavailable.

## Pivoted work plan

At least half of this cycle leaves fixed-path canonical injections.

1. **Moments and functional inequalities.**  Express the area law through
   positive transfer matrices before support Mobius inversion.  Audit whether
   symmetrization, a variance bound, or an auxiliary-label permutation chain
   gives anti-concentration rather than concentration alone.  Keep the gap
   between a variance estimate and a local atom explicit.
2. **Random-map/Hurwitz-tree representation.**  Use the exact
   Cayley-tree-times-permutation sampler of Duchi--Poulalhon--Schaeffer.
   Determine whether adjacent changes of the permutation parameter induce a
   bounded area change while staying in a fixed product fiber; do not assume
   this without proving how the canonical tree changes.
3. **Positive transfer and cancellation audit.**  Write the area-marker
   matrices and quantify the Mobius cancellation.  Seek a connected positive
   state augmentation or a coefficient-ratio recurrence; reject it explicitly
   if state growth or lack of total positivity is fatal.
4. **Complete boundary route.**  Independently write the exact width-12
   boundary inclusion for `K`.  If coefficients become thin, enumerate the
   types of `H_3,H_4,H_5` crossings and macro exits needed for an upper bound;
   a thin `H_N(q)` alone is never called a bottleneck.
5. Use bounded exact calculations only to falsify a named universal lemma.
   Preserve fixed seed, command, environment, and machine-readable output.

## Calibration

Check odd `m`, `m=0`, `N=2`, excluded `m=2`, global sizes `27,120,3936` and
pure-Hurwitz counts `4,13,17`, `m=4` whole-word `H_4`, doubled-tree minima,
ordered factors/interleavings, parity insufficiency, failed `L=2` simulation,
and exact mass orientation.  The final report will use the required nine
fields and will not broaden a scoped result into Terminal A or B.
