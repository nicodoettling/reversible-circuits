# Genus-one connected sampler — frozen target T0

This is a new, user-authorized capped research run. The old local heat-bath
mixing objective in GOAL_SPEC.md and AGENTS.md is superseded for this run.
Their proof, experiment, safety and coordination standards still apply.

For each N>=2 and integer b>=1, return an ordered word of 2N transpositions
on [N] whose product is exactly identity and whose support graph is connected
on all N labels. Its law must be within 2^(-b) in total variation of uniform
on this set X_N, in expected bit time polynomial in N,b. An exact expected
polynomial-time sampler is stronger. Labels and positions are distinguished;
(a b)(x)=a(b(x)), with rightmost factor acting first. N=2 has one word;
N=1 is infeasible. Polynomial in N is not polynomial in log_2(N) wires.

Internal targets may be connected factorizations of a specified permutation
sigma, of length v+cycles(sigma)-2+2g for g=0,1. These are distinct from
unconstrained endpoint bridges and prefix completion laws with exposed support.
No Markov kernel is assumed or sought.

The coordinator integrates proofs, verifies imported inputs and computes the
exact global mass certificate Z_(g<=1)(N,m)/Z(N,m). A sampler for X_N alone
does not sample the global target Omega(N,2N). Assembly must retain labeled
component counts, lengths and uniform position interleavings. With approximate
components, use error at most epsilon/(2N) per component and pay omitted mass.

Parallel roles: r1_recursive develops one endpoint-count-guided recursion;
r2_structural develops one cut/decorated-object construction; r3_referee works
blind from the separate brief before seeing any candidate. Four simultaneous
contexts total, all gpt-6-astra with ultra effort; workers never delegate.
Workers own only their role directories. Only the coordinator writes root
experiment artifacts. No edits outside this new experiment, commits, pushes,
installs, machine changes, other Codex processes, or detached/remote compute.

Decision gates are relative to service activation: intake/checkpoint by 30
minutes; construction and blind report by 120; cross-audit and global
consequences by 180; final checks by 210; synthesis only thereafter. Absolute
deadlines in run_manifest.md control. Write checkpoints at least every 15
minutes and after major results. Individual computations use bounded runtime.

Tests: exact per-word law or reconstruction multiplicities at (N,m)=(2,4),
(3,6), and (4,8) when feasible; independent counts cross-check 1,240,131040.
Shared regressions (3,4),(4,4),(4,6), with totals 27,120,3936, plus m=0,
odd m,m=2 and N<=2. Exhaustive work stays in these bounded domains. Use
standard-library Python3 and exact integer/rational arithmetic. Seeded
validity tests use multiple fixed seeds and are not proofs of uniformity.

Expected failures: scalar counts without a completion oracle; exponential
cycle-subset inventory; wrong cover-to-word factorial; exposed-support loss;
nonconstant decoration multiplicities; zero-fiber insertion; unbounded
rejection; marginal error products used after conditioning. Preserve rejected
versions and witnesses, reopen downstream claims after any repair, and obtain
a fresh nonauthor recheck. Same-model reviews are correlated.

Final classification: sampler-theorem, strict-constructive-reduction,
checked-method-obstruction, or time-limited-unresolved. Failing a construction
does not establish sampling hardness. Completing artifacts is not completing
the theorem objective.
