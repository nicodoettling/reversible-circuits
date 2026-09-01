# M299 Fresh Immutable Referee Plan

## Objective

Independently audit the frozen M296 framed-stabilizer-intersection package without editing it or relying on its verdict.  The audit will either `ACCEPT` the exact theorem/reduction package, or `REJECT` it with numbered material objections and the smallest decisive countercheck.

## Scope and target discipline

- Ambient target of the project: the global fixed-length uniform law on
  `Omega(N,m)`, with the lazy exact same-product `{3,4,5}` block heat-bath
  kernel fixed in `GOAL_SPEC.md`.
- Immediate audit object: a braid-word routing reduction inside a fixed
  minimal connected Hurwitz orbit.  It is not itself a Markov-chain mixing
  theorem.
- Multiplication/composition convention: retain M296's written semicolon
  convention only after independently checking the chronological action
  order.  Every left/right coset and transporter equality will be derived
  from definitions rather than inferred from notation.

## Required checks

1. Verify the frozen top `SHA256SUMS` digest
   `9ab0978c92fee4f92d000604eac4610dbbe6c7aeeaebe3fe86968514990d1f7f`
   and exact inventory.
2. Inspect and independently check every cited input from M13, M112/M119,
   M135/M137, M284/M288, and M291/M294.
3. Reconstruct chronological residualization
   `beta = alpha0 ; s ; delta0^{-1}` and the definitions/orientations of
   `L_Q`, `R_Q`, and
   `C_Q = {s in S : L_Q s R_Q in S}`.
4. Prove or refute the stated transporter identity, pairwise criterion
   `S L_Q S = S R_Q^{-1} S`, coset form
   `s_Q [S intersect R_Q S R_Q^{-1}]`, and claimed higher-arity scope.
5. Check the short stabilizer loops `R_(2r-1)` and `R_(2r)^3` directly from
   the Hurwitz action and verify their length accounting.
6. Audit the Reidemeister--Schreier inventory: polynomial word length versus
   exponential indexing, with no compression claim silently imported.
7. Freeze an `ACCEPT`/`REJECT` report, numbered objections, artifact hashes,
   and a complete inventory.

## Firewalls

Even an acceptance leaves SSTID unresolved.  This audit does not establish a
common-prefix construction, an every-color route, a voltage or congestion
bound, a spectral gap, polynomial mixing, or either terminal outcome.

## Deliverables

- `checkpoint.md`: pre-inspection initialization and halfway audit state.
- `proof_audit.md`: line-by-line independent derivations and cited-input audit.
- `report.md`: immutable verdict and numbered objections.
- `freeze_manifest.md` and `SHA256SUMS`: exact frozen inventory and hashes.

