# cycle-excess-one

- Created UTC: 2026-10-14T13:38:15.152553+00:00
- Objective: Attempt a polynomial gap for the nonlocal/local hybrid on full-cycle words of length N+1; prove small-family bounds and test graph-fiber and square-exposure lemmas.
- Target distribution: Uniform full N-cycle transposition words of length N+1; declared S3 all-length subfamily.
- Parameters: full-cycle endpoint at N=2,...,5, m=N+1; S3 all feasible endpoints for m=2,...,7; star-multigraph obstruction at N=3,...,12; identity regressions S3,m4 and S4,m4,m6.
- Commands: `python3 -B experiments/20261014-133815-cycle-excess-one/check.py`
- Raw data: results.json, recording Git commit, Python version, parameters and imported-code hash.
- Interpretation: exact finite falsification of count/collision formulas, macro reversibility, adaptive square-refresh proposals, fixed-graph restriction connectivity, and the S3 coupling inequality. No finite-spectrum extrapolation.
- Next changes: retain a complete small-family mixing proof and any valid growing-N lemmas; identify the first unresolved step for the full N+1 hybrid.

Kernel: K_A is the prior half-lazy adjacent Hurwitz/square chain; K_G is
the prior half-lazy shuttle/update/unshuttle all-position-pair chain;
P=(K_A+K_G)/2. Products act rightmost first. Target is uniform on the
declared endpoint fiber. Also test a separately declared balanced square
branch R_*: choose an equal position pair uniformly, propose a uniform
replacement transposition, and accept with min(1,Y(w)/Y(w')). Hold if
Y=0. The surrounding hybrid P_* is defined in proof.md.

Named hypotheses under test: exact graph restrictions mix; genus-one
square exposure is inverse-polynomial; graph-selected square refresh can
be corrected without negligible acceptance; S3 prefix coordinates admit
a uniform contraction bound. Preserve failed hypotheses.

All experiments are deterministic exact enumeration (no seeds); Python
standard library only. No installation, numerical spectral inference,
or claim that a direct sampler proves a walk mixes. The full N+1 bound
is the target, not an assumed premise.

Proof-derived extension: test a separately named coarse jump based on a
minimal tree word plus 2h inserted gates, canonical endpoint relabeling,
and rejection with probability 1-1/tau, where tau is the number of
occurrence-distinguished spanning trees of the output multigraph. Named
claim: every output has exactly tau proposal preimages. Test the entire
proposal universe for h=1,N=2,...,5 and h=2,N=3,4. This can yield a fast
macro hybrid but must not be substituted for the original edge-slide
kernel in the verdict. Command: `python3 -B experiments/20261014-133815-cycle-excess-one/tree_jump_check.py`.
