# adjacent-gap-proof

- Created UTC: 2026-10-14T22:04:15.167786+00:00
- Objective: Attempt the K_A gap at full-cycle m=N+1 via exact two-factor comparison and local conditional projection estimates; preserve any failure and prove only justified bounds.
- Target distribution: Uniform fixed-endpoint ordered transposition words; principal target full N-cycle at m=N+1; auxiliary exact length-three endpoint fibers.
- User-facing date: 2026-10-15, Europe/Berlin; started 2026-10-14 UTC.
- Parameters: full-cycle N=3,4,5 at m=N+1; identity regressions S3,m4 and S4,m4,m6; length-three endpoint classification, transposition case N=2,...,12.
- Command: `python3 -B experiments/20261015-adjacent-gap-proof/check.py`
- Raw data: results.json, with commit, command, Python version and import hashes.
- Interpretation: exact two-factor comparison and conditional projection bounds, not asymptotic inference from finite spectra.
- Next changes: prove a polynomial bound only if the local-to-global step closes; otherwise retain its failure and the explicit bounds actually justified.

Kernel: K_A=I/2+H/4+R/4. H chooses a uniform linear adjacent slot and
sign; R chooses a uniform adjacent slot, replaces a,a by uniform s,s,
and otherwise holds. Products act rightmost first. No cyclic boundary.

Named route: compare K_A with half-lazy exact two-factor heat bath Q;
test the angle of overlapping conditional projections on three gates.
The expected failure mode is excessive dependence in a three-gate
transposition-endpoint fiber. Check whether that fiber really embeds
in the full-cycle m=N+1 target. Failure of this route is not failure of
the global mixing conjecture.

Auxiliary deliverables: a uniform-in-N length-three bound if justified by
complete endpoint classification; an explicit growing-N lower bound from
connectivity with any exponential dependence plainly labeled. Never
substitute a different sampler for K_A. Standard library, deterministic
exact arithmetic, no seeds and no installations.

Entry workspace already contains five dirty map files and the nine
untracked artifacts plus receipt from the earlier excess-one run. Preserve
them and distinguish this turn's changes. The earlier proofs and manuscript
remain unchanged.
