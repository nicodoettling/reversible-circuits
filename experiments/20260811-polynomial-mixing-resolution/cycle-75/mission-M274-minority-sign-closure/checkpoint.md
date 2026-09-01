# Mission M274 checkpoint

Status: **final checkpoint; exact hierarchy frozen, universal sign open**.

- Mission directory, plan, and checkpoint were created before substantive
  mathematical work.
- `HANDOFF.md`, `GOAL_SPEC.md`, the complete project skill, and
  `references/sampling-problem.md` have been read.
- Next: locate and verify immutable M161/M166, M168/M171, M174/M178, and
  M266/M268 artifacts, then reconstruct the exact minority-sign
  normalization before attempting any sign argument.

All eight required checksum inventories now pass.  Their `SHA256SUMS`
digests are

```text
M161  17bd62a9b121a10058f87c576275411186e1c3c5039fa07a9cf29c9bea7358d8
M166  344b6c76e538ecc82ac64ace908a21aabfb805330bad8a72c6ba042831e869c3
M168  3f86fc364d1809752d06085eddad8b2e75132ea03c1d27d5a87e9ec3b1cb84bd
M171  c47a095db5925fe69fe1756080943523376b4194b5a4cb3f6d112d8c7306fe2d
M174  fea1f624d6b65fb8404eee0324832aa601e1bf4f202598b60a6608b1a23a51ba
M178  6ca82e9fe821c5a56b4d590dab28b29bf5e4cbc3c0af0a91c0538a53abd51fba
M266  6203ef0dca1e2c46696cec5bc1446da9656ace2b8a3a4ce9b2131267b200c052
M268  62976d7adca32d4ea7819ad36c7623430e26f75eced98a7b88bec58a4d0de2ef
```

M91/M94/M100 were also checked because their literal source-channel and
orbit formulas are cited transitively; their inventory digests are
`0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703`,
`47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562`,
and `bc5a915fc10aef4b546542938e9289e516e97a13553d4888d7b0395acd8965a2`.

The exact remaining sufficient condition, now that PCS is proved, is

```text
P_k=sum_y (z_k(y))_+,   N_k=sum_y (-z_k(y))_+,
k min(P_k,N_k)=O(1)                         (MS)
```

uniformly over odd `k>=3`, with `1<=y<=3k-3`.  The identity

```text
sum_y |k z_k(y)|
 =k|sum_y z_k(y)|+2k min(P_k,N_k)
```

shows that `(MS)` plus accepted PCS is sufficient for FCL1.  Universal
one-sign is stronger and is not required.

Predeclared finite falsifier: after the complete universal sign statement
and its exact formula are written in the proof note, run only the frozen
literal M161 evaluator at `k=9` over the first fixed cell, retaining exact
rational per-lag scores and the full `T/D` by `IS/IN/X` decomposition.  This
can refute universal one-sign but cannot prove it or refute `(MS)`.  No
higher-rank scan will be used unless a new analytic candidate family is
first stated.

The first exact `k=9` run found no zero or negative score.  A second,
strictly smaller-rank falsifier is now predeclared for the universal
termwise monotonicity statement `(MON)` in `minority_sign_reduction.md`:
exactly `k=3,5`, all first-cell lags, both channels, and every legal split.
It will record violations and the four fully weighted gradient/embedding
blocks.  Failure of `(MON)` is only a firewall against a termwise sign
proof; it is not evidence against the combined minority estimate.

`(MON)` is exactly refuted: there are 4 violations at `k=3` and 46 at
`k=5` (32 adjacent and 14 embedding).  The repaired statement is now fixed
before further work as

```text
CP_j(k,y)=(H_(j,B)-H_(j,A))(R_(k,y))>=0,   j=1,2,
```

where `R_(k,y)(s)=2W_(k,y)(s)/(A_s pi_y)` is the exact normalized target
response.  The exact full score is `alpha_1 CP_1+alpha_2 CP_2`.  The
retained `k=3,5` rows have both channel-combined values positive, but this
is finite falsification only.  The analytic attempt will now use the fully
recombined `p Phi-q Psi` laws and will not sign the refuted Abel pieces.

For the requested direct-coupling attempt, the stronger exact scalar order
`(FOSD)` is now fixed in the proof note: every upper tail of the normalized
response under `H_(j,B)` must dominate the corresponding `H_(j,A)` tail.
The same exact `k=3,5` state space and all first-cell lags will be used as a
capped falsifier.  A failure blocks only response-monotone couplings, not
the channel mean inequality `(CP)`.

The direct-coupling/order attempt is complete:

- `(FOSD)` is exactly false already at `k=3`, `j=1`, `y=1`: at response
  threshold `343359/268912`, the B-minus-A upper-tail mass is `-32/375`.
- The fully recombined direct coefficient formulas `(6.1)--(6.2)` are
  recorded for `CP_1,CP_2`, with no Abel-piece sign inference.
- Raw ordered-atom positivity is refuted for every odd rank by explicit
  merged-only atoms beginning with `(1,2k)` and separate-only atoms
  beginning with `(0,1)`, in both channels.
- The exact capped rows still have `CP_1,CP_2>0` at every `k=3,5` lag.
  This is finite calibration only; no universal CP proof was found.
- The exact `k=9` OS+ falsifier has 24 strictly positive rational scores,
  minimum at `y=k-2=7`, approximately `0.00599987231655`.  This does not
  prove OS+ or MS.

Final hierarchy:

```text
CP_1,CP_2 >=0 pointwise => OS+ => MS <=> FCL1 (given proved PCS).
```

`MON` and `FOSD` are refuted.  `CP`, `OS+`, `MS`, and FCL1 remain
unresolved.  No higher-rank scan was run.  No gap, mixing, or terminal claim
is made.

No minority-sign estimate, FCL1 bound, gap, mixing, or terminal claim is made
at this checkpoint.
