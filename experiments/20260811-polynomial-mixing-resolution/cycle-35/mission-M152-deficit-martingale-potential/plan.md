# M152 plan: deficit-martingale potential

Date: 2026-08-13 UTC.

## Objective and scope

Continue the accepted M147/M151 all-suffix reset frontier on the exact
attachment state `(kappa,D)`.  The sole target is one precise global lemma or
one rigorous falsifier for a named deficit-aware amortized-potential family.
This mission concerns only the unweighted full-reset auxiliary recurrence in
the minimal-long-cycle sector.  It will not claim an auxiliary gap,
`ROOT-MEAN LIFT`, an original-chain gap, polynomial mixing, Terminal A, or
Terminal B.

## Accepted inputs

- M140/M144: the corrected one-power reset subtraction and `C_s<3/4` for
  `s>=100`, with the accepted right-heavy theorem through suffix excess five.
- M147/M151: the exact beta-binomial attachment law, child update, nilpotent
  all-suffix recurrence, and reachable refutation of deficit-blind pointwise
  closure.

The project target remains uniform on fixed-length identity transposition
words.  Permutations compose as `(pq)(x)=p(q(x))`, with displayed factors
left-to-right.  No word sampler is changed here.

## Candidate family and proof tests

1. Derive exact killed-subkernel identities from
   `X=d-j ~ BetaBinomial(d,D,kappa-D)` and
   `(kappa,D)->(kappa+d,D+X)`, beginning with affine and quadratic functions
   of `p=D/kappa`.
2. Explicitly subtract the killed `j=0` atom rather than conditioning it
   away.
3. Test the smallest natural nonnegative family whose coefficients may
   depend on suffix data `(B,L)` but not otherwise on the attachment context:
   affine/quadratic combinations of `1`, `p`, and `p(1-p)`, with right-heavy
   boundary constrained by `1-q_(B,L)`.
4. Either prove a global superharmonic inequality compatible with the full
   corrected reset-plus-descendant recurrence, or give an exact reachable
   family showing that this named family cannot satisfy it.

No `L=7` brute enumeration will be performed.  Diagnostics will be capped,
exact, standard-library-only, and used to audit rather than replace an
algebraic proof.

## Expected failure modes

- The reset current term may depend on more context than a low-degree
  function of `p` can dominate.
- Killing may create helpful drift for increasing functions of `p` but the
  available drift may vanish too quickly as `kappa` grows.
- A counterexample may refute only context-independent polynomial
  coefficients, not arbitrary deficit-aware potentials.

## Deliverables

- `checkpoint.md` with the frozen initial target and source reconciliation;
- a proof/obstruction note with exact hypotheses and boundary cases;
- a standalone exact checker plus machine-readable JSON if a finite audit is
  useful;
- `report.md`, `freeze_manifest.md`, and `SHA256SUMS`.

