# One-cycle factorization walk: local versus coded updates

Date: 2026-10-13 (Europe/Berlin).
Start commit: `9a7ca2119172f87b15e9f85e28cee6dc91af188f`.
User clarified that the requested cycle is the permutation endpoint, not a
cycle of SAT variables. Work is restricted first to minimal length N-1.

Target: uniform ordered transposition factorizations of the fixed full cycle
c=(0 1 ... N-1), with rightmost-first composition. This is an endpoint fiber,
not an identity-word law. Main kernel K=I/2+H/4+R/4, using a uniformly chosen
linear adjacent slot, a uniform sign for H, and a uniform doubled
transposition for R if the selected pair is equal (otherwise hold).

Named obligations and falsification targets:

1. Prove that square refresh is inactive at minimal length, and that K is
   comparable by explicit constants with lazy two-factor heat bath.
2. Check the candidate bijection between factorizations and rooted labeled
   trees obtained by labeling each child vertex with its incoming edge's
   time index. Check both directions independently against enumeration.
3. Test whether a one-coordinate Prüfer refresh is itself a Hurwitz move.
   Retain a negative witness; the coded walk must not be passed off as K.
4. State the first missing comparison needed to prove polynomial mixing of
   K. Literature connectivity or diameter bounds alone do not suffice.

The coded walk is only a benchmark. Efficient exact sampling of minimal
factorizations is already represented by S-MINIMAL in the project map; no
novel sampling theorem is claimed.

Command: `python3 -B experiments/20261013-single-cycle-walk/check.py`.
Python 3.12.3, standard library only. Deterministic exhaustive tests, with
seed 20261013 recorded but unused. Results go to `results.json`.
Boundary cases: N=1 and N=2 singleton words; N=3 minimal fiber; infeasible
lengths m<N-1 or wrong parity. Exact identity-kernel baseline checks are
reused for S3,m4 and S4,m4,m6; they do not change the endpoint target.

Expected failure modes: ordinary support-tree forgetting is not a bijection;
word positions and permutation labels must be distinguished; relabeling must
preserve the distinguished root and map the computed product to c; duplicate
Hurwitz directions on disjoint pairs must retain their transition weights.
