# M218 plan: fresh referee of M214

## Objective

Perform a clean-room, exact finite audit of frozen mission M214.  The audited
claim is restricted to the declared one-leaf extension template: the 16 rooted
labeled trees on vertices `1,...,5` (root/attachment vertex `1`), each extended
by the leaf edge `{1,6}`, and the seven distinguished edits, for 112 rows total.

## Status and scope

- Audited target: a finite deterministic endpoint certificate, not a Markov
  chain or a probability distribution.
- Claim status before audit: **empirical/exact-computational**, pending this
  independent replay.
- In scope: source inventory; descriptor reconstruction from each tree;
  13 nonempty descriptor/edit cases; nine distinct correction words;
  chronological signed-Hurwitz convention; all 112 literal endpoint checks;
  classification and summary digests.
- Out of scope: enumeration/search in `Q_6`; intrinsic completeness outside
  this template; all-`d` locality; every-color routing; voltage-corrected route
  lengths; spectral gaps, polynomial mixing, or a Terminal claim.

## Source lock

Before substantive checking, read the repository source-of-truth documents
required by `AGENTS.md`, then freeze the M214 input by verifying its complete
`SHA256SUMS` inventory and manifest digest
`cb63ac879b036d096af369fabf02da9abecba786bcf746ba34d809b8ceaada3f`.
M214 is immutable.  The checker will not import M214 code or data.

## Method

1. Reconstruct the 16 rooted labeled trees independently from the declared
   graph conditions.
2. Implement permutation arithmetic and chronological signed Hurwitz moves in
   a new standalone checker.
3. Derive the descriptor directly from each tree: the path from the edited
   vertex to attachment vertex `1`, the late-ancestor flag, the initial
   consecutive larger-label direct-child run, and the declared edit-5
   exceptional path.
4. Encode the finite 13-case correction rule from the mathematical report,
   replay every resulting word literally, and independently aggregate the 112
   rows, 13 nonempty cases, and nine distinct words.
5. Canonically serialize classifications and summaries and compare the
   resulting SHA-256 digests with the two frozen expected values.

## Expected failure modes

- source-lock hash or inventory mismatch;
- an implicit use of M214 output rather than tree-derived reconstruction;
- inverse/sign or chronological-order mismatch;
- incorrect tree universe, descriptor, or exceptional-path orientation;
- endpoint mismatch in any one of 112 rows;
- noncanonical digest serialization;
- a finite result being overstated as a general recursion theorem.

## Verdict rule

`ACCEPT` only if the source lock and every exact finite check pass, with all
material objections numbered.  Otherwise `REJECT`, identifying the first
decisive mismatch.  Nonmaterial clarity issues are listed separately.

