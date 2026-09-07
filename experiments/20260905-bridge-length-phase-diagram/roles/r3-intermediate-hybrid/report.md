# Exact component assembly, sparse approximation, and the connected frontier

Role `r3-intermediate-hybrid`; final report, 2026-09-05.
Target throughout: `U_(N,m)`, uniform on **all** length-`m` transposition
identity words. Conditional connected and minimal-component laws are
explicitly identified below. Products are maps with
`(alpha beta)(x)=alpha(beta(x))`; the rightmost displayed factor acts first.
There is no Markov kernel, local-chain claim, or mixing-time claim here.

**Verdict: promote the positive polynomial count/assembly theorem and the
audited sparse approximation; retain a strict connected-sampling reduction.
All-length polynomial sampling remains unresolved.**

## 1. Exact count and assembly theorem — proved

For a fixed labeled `v`-set, let `C(v,ell)` count connected identity words
using exactly that set, including `C(1,0)=1` solely as the isolated-label
convention. For `v>=2`, it is positive exactly when

```
ell=2(v-1)+2g,  g>=0.
```

Necessity follows by tracking cycle joins and cuts: an identity word has
equally many, and at least `v-1` joins are required to connect `v` initial
support components. Sufficiency follows from a doubled spanning tree and
`g` additional transposition pairs. Neither argument uses Hurwitz
transitivity. All other `C(1,ell)` vanish.

Let `alpha` be an unordered collection of disjoint labeled nontrivial
components `(B,ell_B)` with `sum ell_B=m`. Its exact number of words is

```
W(alpha)=m! product_B C(|B|,ell_B)/ell_B!.                (1)
```

Proof: edges in disjoint components commute; the product is identity iff
every internal ordered word has product identity. Choose those internal
words independently and choose one of the `m!/product ell_B!` color
interleavings. Restricting a resulting word to each support component
recovers all choices uniquely. Isolated labels are implicit in (1).

Consequently the exact global disintegration is:

1. choose labeled component sets and lengths with probability `W(alpha)/Z`;
2. choose independent uniform connected internal words;
3. choose a uniform color interleaving, preserving each internal order.

For unlabeled multiplicities `a_(v,g)` and `s=sum v a_(v,g)<=N`, the exact
weight before normalization is

```
N! m!/(N-s)! * product_(v,g)
  [ C(v,2v-2+2g) / (v! (2v-2+2g)!) ]^a_(v,g) / a_(v,g)! . (2)
```

Equation (2) is subject to `sum (2v-2+2g)a_(v,g)=m`; it retains equal-type
component multiplicities, labeled sets, all component factorials, and all
interleavings. It must not be replaced by uniform selection of partitions,
component sizes, surpluses, or trees.

### Polynomial connected counting

The primary DYZ normalization reconciled by the coordinator is

```
C(d,k)=d! k! h[g,d],     k=2d-2+2g.
```

DYZ Proposition 1 equation (13) therefore becomes the positive integer
recurrence

```
d^2(d-1) C(d,k)
 = 2 sum_(a+b=d) binom(d,a)
       sum_(k1+k2+r=k, r even>=2)
         multinomial(k;k1,k2,r) a^(r+1) b^2
         C(a,k1) C(b,k2),                              (3)
```

with `C(1,0)=1`. The nonzero `k_i` already enforce their degree/genus
constraints. The division on the left is exact. This recurrence computes
all connected counts, for arbitrary surplus, in polynomial bit complexity.

For each ordered degree split, first compute

```
B_(a,b)(s)=sum_j binom(s,j) C(a,j)C(b,s-j).
```

Then the contribution at length `k` is
`2 binom(d,a)b^2 sum_(r even>=2) binom(k,r)a^(r+1)B_(a,b)(k-r)`.
These are two binomial convolutions, giving `O(N^2 m^2)` integer arithmetic
operations for the whole table, with precomputed binomials and powers.
Degrees exceeding `min(N,m/2+1)` can be skipped.
The displayed operation bounds concern `m>=2`; the `m=0` tables and empty
word are filled directly in `O(N)` time. Equivalently replace every `m^2`
factor in the bounds by `(m+1)^2` to cover that boundary uniformly.

Every count is at most `binom(N,2)^m`. Every positive accumulated numerator
in (3) is at most `d^2(d-1)C(d,k)`. Thus counts and all relevant intermediate
integers have `L=O((m+1)log(N+1))` bits. Schoolbook multiplication/division
gives the conservative bit bound `O(N^2 m^2 L^2)` for counting, in the
`N,m` input model. No unit-cost assumption for exponentially large counts is
made. The count recurrence alone is **not** a word sampler.

### Positive assembly dynamic program

Let `Z(n,k)` count unrestricted identity words on `n` labels. Set
`Z(0,0)=1`, `Z(0,k>0)=0`. Distinguish the least remaining label; if its
component has size `v` and length `ell`, then

```
Z(n,k)=sum_(1<=v<=n,0<=ell<=k)
 binom(n-1,v-1) binom(k,ell) C(v,ell) Z(n-v,k-ell).       (4)
```

The `v=1,ell=0` branch isolates that label. Equation (4) is positive and
uses `O(N^2m^2)` arithmetic operations and the same `O(L)` count bits.
It avoids enumeration of labeled set partitions.

To sample the macro law, choose `(v,ell)` with the displayed integer
weights; choose its `v-1` other labels uniformly; choose its `ell` positions
uniformly; recurse on the remaining labels and positions. Once a connected
sampler supplies the internal word, each literal word receives probability
`1/Z(n,k)`, by cancellation of the four selection factors. Exact random
integers use unbiased-bit rejection with fewer than two attempts in
expectation. All exact-runtime assertions in this report are **expected
polynomial time** in this standard random-bit model.

## 2. Minimal connected sampler and exact mass certificate — proved

The audited DPS construction gives

```
C_0(v)=C(v,2v-2)=(2v-2)! v^(v-3),   v>=2.               (5)
```

At `v=2`, (5) is exactly one. A uniform Cayley tree on `[v]` (sampled by
a uniform Prüfer sequence), together with an independent uniform
permutation of `2v-2` edge labels, is a uniform rooted input. DPS
Proposition 3 and Theorems 4–5 reconstruct a connected identity word;
forgetting the root is exactly `v`-to-one. Therefore this is an **exact
connected conditional sampler**, not a heuristic tree weighting.

The simple closure implementation retained here takes at most `O(v^4)`
operations on `O(log v)`-bit labels; more efficient closure is not needed
for polynomiality. All rooted inputs are independently exhausted at
`v=2,3,4`. Word reversal/inversion translates DPS's displayed
`tau_m...tau_1=id` convention to the project convention; since the endpoint
is identity, inversion preserves the target fiber and uniform law.

Let `A_0` be the global subset in which **every** nontrivial component is
minimal. Use (4) after setting all nonminimal component counts to zero, and
call the resulting count `Z_0(N,m)`. Combining that exact macro law with
the DPS sampler gives

```
Q_0=U_(N,m)(.|A_0),
d_TV(Q_0,U_(N,m))=1-Z_0(N,m)/Z(N,m).                    (6)
```

Both counts and this rational certificate are computable in polynomial bit
complexity. The sampling itself needs only (5), the restricted assembly
table, and DPS; its conservative bit runtime is

```
O(N^2 m^2 L^2 + N^4 (log(N+1))^2),
```

and does not grow with `1/epsilon`. Comparing the certificate to a requested
rational accuracy uses its input bit length. For every instance passing
`1-Z_0/Z<=epsilon`, this is a proved endpoint-exact epsilon-close global
sampler. The certificate is not an asymptotic extrapolation from small data.

`A_0` is nonempty exactly for even `0<=m<=2N-2` when `N>=2`. At
`m=2N-2`, it is the connected minimal sector only. It is not the complete
global target: at `(N,m)=(3,4),(4,4),(4,6)`, the total/minimal counts are
`27/24`, `120/114`, and `3936/2880`. Exact TV errors are respectively
`1/9`, `1/20`, and `11/41`.

## 3. Closed sparse approximation bound — proved, freshly audited

The coordinator proposed the following theorem; this role independently
audited its full incidence proof in `sparse_bound_audit.md`.

For every `N>=2`, even `m<=N`,

```
d_TV(Q_0,U_(N,m))
 <= min(1, m^4/[48(N-m+1)^2]).                          (7)
```

The exact endpoint is preserved on every run. Thus a further proved
polynomial-time regime is all feasible even lengths satisfying
`m^4<=48 epsilon (N-m+1)^2`, in particular
`m=O(epsilon^(1/4) sqrt(N))` with a sufficiently small absolute constant.

Here is the proof's essential accounting. Write `m=2k` and divide every
macro weight by `m!`. Let `S_G` be its total weight at total surplus `G`.
The audited DYZ ratio gives
`A_g(v)<=A_0(v)(v^3/12)^g`, with `A_g=C_g/(2v-2+2g)!`.
After erasing all surplus from a macro, its base has cost `k-G`; summing
genus allocations raises its weight by at most `(k^3/12)^G`. A base has at
least `N-2k+2G` isolated labels. Adding `G` fresh pair components has total
normalized weight `(n_iso)_(2G)/(4^G G!)`. Reverse multiplicity is at most
`binom(k,G)`. Therefore

```
S_G/S_0 <= [k^4/(3(N-2k+1)^2)]^G = R^G.
```

For `R<1`, summing gives bad-to-good mass ratio at most `R/(1-R)`, hence
the actual bad mass, and therefore TV, is at most `R`. For `R>=1`, use
the trivial bound. Empty bases carry no positive surplus, handling `G=k`.
The proof records all factorials, isolates, and matching multiplicities;
no local Markov-chain result is used.

## 4. A limitation of this named sampler — proved, not hardness

The finite mass certificate must not be extrapolated to an `m=Theta(N)`
accuracy theorem. In fact the minimal-only sampler's TV error tends to one
already in every fixed power regime

```
m=Theta(N^alpha),     2/3<alpha<=1,
```

along feasible even lengths; if `m>2N-2`, its subset is empty outright.
This is a theorem about **the minimal-only sampler**, not computational
hardness or an obstruction to the full hybrid.

To prove it, (5) identifies normalized minimal counts with weighted labeled
forests, including isolated vertices:

```
Z_0(N,2k)/(2k)! = sum_(forests F with k edges)
                    product_(components B of F) 1/|B|
                <= binom(binom(N,2),k).                 (8)
```

For any `2<=r<=N` and positive even `m`, all words on a fixed `r`-subset
are valid `N`-label words. The midpoint law of the unconditioned
transposition walk on `S_r` is supported on one parity class. Symmetry and
Cauchy–Schwarz give return probability at least `2/r!`. Thus

```
Z(N,m)>=2 binom(r,2)^m/r!,
Z_0/Z <= min(1, m! binom(binom(N,2),m/2) r!
                 /[2 binom(r,2)^m]).                    (9)
```

Choose `r=floor(m/log m)` for large `N`. For the stated power regimes,
this lies between two and `N`. Elementary factorial/binomial bounds give

```
log(Z_0/Z)
 <= m[log N-(3/2)log m+2loglog m+O(1)]
 = -(3alpha/2-1)m log N+O(m loglog N),                   (10)
```

which tends to minus infinity. Constants may depend on the fixed constants
in `m=Theta(N^alpha)`. For linear `m=2floor(theta N)`, `0<theta<1`, this
specializes to `-theta N log N+O_theta(N loglog N)`.

The simple finite upper bound (9) is loose and was vacuous on the stored
exploratory cases through `N=10000`; those negative diagnostics are retained.
The conclusion (10) follows from its asymptotic proof, not from those data.

## 5. Dense connected conversion and the exact hybrid — proved reduction

Counting is solved for every feasible component. Sampling remains separate.
Let `U_(v,k)` denote the **unrestricted** identity bridge on a fixed `v`-set
and put

```
alpha(v,k)=C(v,k)/Z(v,k).
```

This is the exact probability that the support is connected, and is
polynomial-time computable by (3)–(4). A dense unconditioned bridge sampler
cannot simply be substituted for the connected primitive.

For even `k>0`, a sufficient bound is

```
1-alpha(v,k)
 <= (v!/2)(2^v-2) exp(-2k/v).                           (11)
```

Indeed, the return probability is at least `2/v!` by the same midpoint
argument. If support is disconnected, some nonempty proper cut has no
crossing transposition. Each fixed cut has avoidance probability at most
`exp(-2k/v)`, since its minimum crossing-edge fraction is `2/v`. Union
bound over at most `2^v-2` cuts and divide by the return probability. Hence
`alpha>=1/2` is guaranteed when

```
k >= (v/2)[log(v!)+log(2^v-2)].                          (12)
```

The exact ratio certificate can be better than (12). At `v=2`, every
positive even bridge is already the unique connected word.

Suppose an audited dense algorithm produces only valid identity words and
has TV error `delta<=1/4` from `U_(v,k)`. If `alpha>=1/2`, reject
disconnected outputs. Acceptance is at least `1/4`; the conditional TV
error is at most `4delta` by the standard conditioning bound
`2delta/alpha`. Expected calls are at most four. Every accepted word has
the exact connected support and endpoint. Thus audited dense regimes may
be used internally with their hypotheses, their smaller requested error,
and this acceptance certificate all checked.

For a full hybrid, fix any explicit polynomial work cap
`B(N,m,log(1/epsilon))`, and define an allowed component set containing:

- isolates and `v=2` components (exact trivial sampling);
- `g=0` components (exact DPS sampling);
- small-rank components covered by the exact support-marked DP below,
  with `v^(2v)<=(Nm+2)^c` for a fixed universal constant `c`;
- components where an audited exact unrestricted bridge sampler meets
  work cap `B` **and** `alpha(v,k)>=1/2`, followed by connected rejection;
- components covered by the audited dense algorithm at error
  `delta=epsilon/(8N)`, with `alpha(v,k)>=1/2`.

Use (4) with `C(v,k)` set to zero outside that allowed set, obtaining the
exact count `Z_allowed`. Sample its macro law exactly and each allowed
connected word with error at most `epsilon/(2N)` (zero for exact branches).
There are at most `N` components, so product coupling and averaging give

```
d_TV(Q_hybrid,U_(N,m))
 <= 1-Z_allowed/Z + epsilon/2.                          (13)
```

Therefore `1-Z_allowed/Z<=epsilon/2` is a **polynomial-time checkable,
per-instance sufficient regime** for the hybrid. The final dense and short
eligibility predicates are the coordinator's audited r1/r2 theorems; this
role does not independently promote an unfinalized dense threshold.
Equation (13) is proved for any predicates satisfying the displayed
primitive guarantees. No closed overlap between sparse and dense regimes
has been established here.

The support-marked DP makes the small-component condition explicit. Its
state is `(q,pi)`, where `q` is the exposed prefix permutation and `pi` is
the partition into exposed support components. There are at most
`v! Bell(v)<=v^(2v)` states. Define

```
F_0(q,pi)=1{q=id and pi has one block},
F_r(q,pi)=sum_(t=(a b)) F_(r-1)(q t, pi join {a,b}).     (14)
```

Starting at `(id,discrete partition)`, this is exactly the number of
connected identity completions. Sample a transition with weight equal to
its continuation count. Every connected word has probability
`1/C(v,k)` by telescoping. A table costs
`O(k v^3 v!Bell(v))` integer/label operations, allowing `O(v)` work for
updating a permutation and partition; all counts have `O(k log(v+1))`
bits. This is polynomial for the stated explicit cap, and for every fixed
`v` with arbitrary input length. The implementation tests (14) and every
connected per-word probability in all required small cases.

The unrestricted short cycle-type sampler by itself is **not** a
small-component primitive: at minimal length its connected probability
can be very small. Rejection is allowed here only with the stated exact
acceptance certificate. This distinction prevents a false polynomial
hybrid obtained by silently paying an exponential conditioning cost.

## 6. First standalone missing primitive — unresolved

> **CONNECTED-IDENTITY-WORD-SAMPLE.** Given `v>=3`, surplus `g>=1`, and
> `0<delta<1`, with `k=2v-2+2g`, generate a word with exactly connected
> support `[v]`, exact product identity, and TV error at most `delta` from
> the uniform connected law, in expected time polynomial in
> `v,k,log(1/delta)`, at least for the pairs not covered by the audited
> short and dense predicates.

The first concrete unresolved family is `g=1`, `k=2v`, with unbounded `v`.
All its counts are already polynomial-time computable. No polynomial
connected sampler was obtained here for fixed positive genus; the word
"fixed" does not make an exponential-in-`v` algorithm polynomial.

The first unproved step in a count-to-sample proposal is a constructive,
correctly weighted word-level lifting of (3), or another polynomial
completion-count oracle for the connected law. Ordinary prefix
self-reduction asks for arbitrary-endpoint completions constrained to join
the already exposed support components; the scalar values `C(v,k)` do not
supply that oracle. One cannot sample formal recursive terms of (3) and
assert they decode uniformly to actual words without a proved map and
multiplicity accounting.

This is strictly narrower than the original global problem: the labeled
assembly, surplus distribution, all exact scalar counts, and color
interleavings have been removed. A sampler for the remaining connected
primitive would complete the global sampler through (4). A failure of the
minimal-only route or lack of this primitive proves no computational
hardness result.

## 7. Boundaries, dependencies, and focused literature reconciliation

For `N>=2`, public odd `m` is infeasible; `m=0` is the empty word;
`m=2` is a uniformly selected repeated edge; `N=2` at every even length is
a singleton. For arbitrary internal endpoints, the usual feasibility
condition is parity and `m>=N-cycles(g)`; a minimal transposition
factorization followed by transposition pairs proves sufficiency. Those
arbitrary endpoints are not silently substituted for connected identity
sampling. On `N<=1`, there are no transpositions and only `m=0` is feasible.

External inputs actually used:

- B. Dubrovin, D. Yang, D. Zagier, *Classical Hurwitz numbers and related
  combinatorics*, Proposition 1 equation (13), with normalization from
  Section 1.2 equations (19)–(20). Source:
  <https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf>.
  The coordinator checked that its weighted covering convention yields
  `C=d! k! h`. Permutation inversion/reversal preserves the identity fiber.
- Duchi–Poulalhon–Schaeffer, *Uniform random sampling of simple branched
  coverings of the sphere by itself*, Proposition 3 and Theorems 4–5.
  Source: <https://www.irif.fr/~poulalho/Articles/DuPoSc13.pdf>.
  The exact rooted quotient and identity convention were independently
  audited in the assigned M119 report and rechecked finitely here.

The coordinator's focused search additionally inspected *Bijections for
simple and double Hurwitz numbers*, Theorems 1 and 4,
<https://arxiv.org/pdf/1410.6521>. Its higher-genus coherent-mobile
bijection is a plausible constructive route, but the inspected statements
do not establish the required polynomial sampler for coherent mobiles.
The fixed-genus long-cycle sampling result in arXiv:2105.03284 concerns
endpoint an `n`-cycle and length `n-1+2g`, not connected identity words of
length `2n-2+2g`. These are scope distinctions, not claims of novelty or
nonexistence of another algorithm.

The only historical citation follow-ups were M12's `checkpoint.md`, because
its report omitted the recurrence coefficient, and M112's
`dps_local_audit.py`, to recover the explicit closure implementation. No
historical resolution ledger or old run log was read wholesale.

## 8. Exact tests and reproducibility

Run from this role directory:

```
python3 -B component_audit.py --n-max 48 --m-max 96 --output results.json
```

Commit `9cc740b29eda6dd38adfde5f0aadc4a9c4eeb6fc`; Python 3.12.3;
standard library only. Exact diagnostics use no seed. Seeded smoke draws
use `1729`, `2718`, and `31415`, twenty draws per recorded case and seed.
Those draws check validity, not distributional approximation.

| candidate | claimed target | identity ok | crosses component data | exact diagnostics | verdict |
|---|---|---|---|---|---|
| positive assembly with exact connected oracle | global uniform | yes by proof | yes | per-word probabilities on required cases | keep reduction |
| minimal DPS assembly | conditional all-minimal law | yes | within its declared subset | exact root quotient and per-word normalization | promote |
| minimal DPS assembly under (7) | epsilon-close global law | yes | within subset; omitted mass bounded | independent incidence proof | promote |
| unrestricted dense bridge used without conditioning | connected law | not guaranteed connected | not applicable | target mismatch | reject |

The direct enumeration tests `S_3,m=4`, `S_4,m=4`, and `S_4,m=6`, plus
eight boundary cases. They verify total/connected/minimal counts, every
labeled macro weight, exact per-word probabilities under full and minimal
assembly, the support-marked connected DP and its per-word probabilities,
endpoint convention, and surplus histograms. Exhaustive DPS
inputs are `2`, `72`, and `11520` rooted pairs at `v=2,3,4`, with exactly
`v` preimages per connected word. Every tested assertion passes.

The stored certificate table has 114 rows with `N<=48,m<=96`; its exact
rational probabilities do not establish an asymptotic curve. For example,
at `N=48,m=24`, the minimal sampler's exact TV error is approximately
`0.05103`; at `N=48,m=48`, it is approximately `0.68183`. The asymptotic
failure theorem (10) prevents interpreting the first value as a linear
length guarantee. The loose finite forest bounds are retained separately
in `results.json`.

The coordinator also independently compared the original rational DYZ
recurrence with a full labeled-permutation DP at all 78 cells
`N<=6,m<=12`, matching this integer count and assembly table. Its artifacts
are outside this role directory and are owned by the coordinator.

Most valuable next human-review target: the positive integer DYZ
normalization (3) together with the independently audited sparse incidence
proof (7), since they determine the new proved global sampling regime.
The next constructive research target is the `g=1` connected sampler, not
a local-chain gap theorem.

```text
role: r3-intermediate-hybrid
claim: Polynomial positive connected counting and exact component assembly; exact minimal conditional sampling; sparse global TV bound; strict connected generation reduction.
status: proved
parameter_regime: N>=2; all even m for counting/reduction; m<=N and m^4<=48 epsilon (N-m+1)^2 for the closed sparse approximate regime; exact mass certificates as stated.
target_distribution: Global U_(N,m); conditional connected and all-minimal laws are explicitly separate internal targets.
runtime: Expected polynomial in N,m,log(1/epsilon); counting O(N^2 m^2 L^2) bit operations, L=O((m+1)log(N+1)); simple DPS sampling adds at most O(N^4 log^2(N+1)).
error: Exact conditional law; global TV=1-Z0/Z and <=min(1,m^4/[48(N-m+1)^2]) in the stated range; hybrid bound 1-Z_allowed/Z+epsilon/2.
assumptions: Audited DYZ Prop.1 eq13 normalization and DPS rooted-product bijection; hybrid additionally requires the explicitly eligible connected primitive guarantees. No Hurwitz transitivity or mixing assumption.
evidence: component_audit.py; results.json; sparse_bound_audit.md; named primary formulas and independent incidence/counting proofs.
independent_checks: Exact required/boundary enumeration and all rooted DPS inputs through v=4; coordinator rational-DYZ versus labeled-permutation DP at N<=6,m<=12; this role independently audited the coordinator's sparse theorem and forest obstruction.
first_unproved_step: Polynomial connected-word generation at fixed positive surplus, first concretely g=1,k=2v, or a constructive weighted lifting of the positive count recurrence.
verdict: promote
```
