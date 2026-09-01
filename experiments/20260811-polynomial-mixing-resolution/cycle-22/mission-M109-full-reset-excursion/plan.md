# M109 plan: full reset excursion

## Objective and scope

Study the surviving exact finite-DAG reset inequalities for the auxiliary
full nonlazy stationary-flow parking-degree projection in the minimal
long-cycle sector:

```text
G=(I-Q)^(-1)A <= U
```

on every reachable active context, or the stronger unweighted inequality
`H=(I-Q)^(-1)A_0 <= q(1-q)K/(R+1)`. This is not the original lazy
same-product `{3,4,5}` identity-word heat-bath kernel and no gap or Terminal
conclusion follows directly.

Permutations compose as `(pq)(x)=p(q(x))`; tuple factors multiply
left-to-right. The global project target remains uniform on fixed-length
identity words, but this mission concerns only the auxiliary reset operator.

## Accepted inputs and forbidden repetitions

Use accepted M90/M96 recurrence and finite-DAG descent, M98/M99's exact
infinite refutation of nonfresh one-step defect positivity, and M103/M106's
exact refutation of the universal two-layer defect condition. Do not retry
either refuted local sign route.

## Method

1. Derive the exact killed/deep/terminal recurrence, including the fresh and
   right-heavy boundary states, all attachment ranks `j=1,...,k`, and strict
   progress `P=s+K-R` descent.
2. Schur-complement or aggregate the DAG by a genuinely excursion-level
   filtration (candidate variables: terminal root group, reset depth,
   remaining progress, or first return to a right-heavy context).
3. State one falsifiable global lemma that implies a complete weighted or
   unweighted resolvent inequality without requiring pointwise one- or
   two-layer defect signs.
4. Attack that lemma analytically. Use exact finite arithmetic only to check
   formulas or discover a counterexample; promote a refutation only with an
   exact witness and a proof only with analytic completeness.
5. If no universal theorem or counterexample closes, record the strictest
   exact reduction and its first unproved scalar/measure inequality.

## Boundary discipline

Check active `s>=2`, `1<=B<=s`, fresh `(K,R)=(1,0)`, nonfresh `K>R>=1`,
right-heavy `R=K-1`, and terminal/killed branches. Original-chain exceptional
cases `m` odd, `m=0`, `m=2`, and `N=2` remain outside this auxiliary lemma.

## Deliverables

- `checkpoint.md`
- a self-contained theorem/reduction note
- exact scripts and JSON only when needed for a named lemma
- final nine-field report with explicit status and strongest self-attack
- final `SHA256SUMS`, source/JSON validation, and cache-clean freeze

