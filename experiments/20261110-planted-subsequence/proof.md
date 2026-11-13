# Exact planting, likelihood, and the first missing hardness obligation

Date: 2026-11-10. Status: **proved by the elementary arguments below, with
finite implementation checks; not independently proof-reviewed**. No novelty
claim or cryptographic security conclusion is made.

## Model and boundaries

Let N>=2, m>=0 even, T the set of all transpositions of S_N, and
Z_r=|Omega(N,r)|. Products act rightmost first. D0 is uniform on the global,
ordered, labeled identity fiber Omega(N,m). For even 0<=k<=m, let M=binom(m,k).
Choose a fresh uniform k-subset I of positions, and draw D1 as D0 conditioned
on E_I: the ordered subsequence at I has product id. I is hidden. There is
one public noiseless word, no persistent key and no oracle. Work is measured
in explicit N,m. This is a direct sampling game, not a Markov chain.

All even fibers here are nonempty, by repeated doubled transpositions.
Odd m gives an empty null fiber; odd k gives an empty conditioning event.
k=0 and k=m give D1=D0. Thus m=0 and m=2 have no nontrivial plant length.
At N=2 every feasible word is the same repeated gate, so D1=D0 for every k.

## 1. Exact planting reduces to two bridges

**Proved.** Fix I. Stably move selected gates to the left, in original order,
by applying (u,s) -> (s,sus) whenever an unselected gate precedes a selected
one. Both new entries are transpositions and their product remains us. This
map is invertible: (s,v) -> (svs,s). Its swap sequence depends only on I;
the selected gates themselves remain unchanged.

It therefore maps Omega(N,m) intersect E_I bijectively to
Omega(N,k) x Omega(N,m-k). Indeed, the first block is the selected identity
word, and the total product is identity exactly when the second block is.
Consequently every allowed set has the same event probability

    p = Pr_D0(E_I) = Z_k Z_(m-k) / Z_m.                         (1)

An exact planted sampler is:

1. Select I uniformly among all k-subsets, independently of later draws.
2. Draw A uniformly from Omega(N,k) and B independently from Omega(N,m-k).
3. Concatenate A,B and reverse the fixed stable-sort moves for I; output
   the resulting word W, keeping I hidden.

Each conditional fiber has the same number of equiprobable inputs, and the
map is a bijection, so this is exactly the stated D1, not a heuristic plant.
Arbitrary ordinary shuffling of A and B would not have this property.

**Conditional efficiency.** If exact samplers for the two shorter bridges
are available with expected costs T(N,k) and T(N,m-k), the additional work is
at most k(m-k) local conjugations plus position sampling. A transposition
conjugation acts on two explicit labels. Thus there is no extra rare-event
rejection cost. This does not prove efficient bridge sampling for all lengths.

The checker uses a full S_N completion table: C_0(g)=1[g=id] and
C_r(g)=sum_(t in T) C_(r-1)(gt). At state g choose t with weight C_(r-1)(gt).
Telescoping gives uniform probability 1/Z_r to every bridge. This exact finite
implementation has factorial dependence on N. Seeded Python PRNG draws test
implementation only; exact-law statements use ideal independent uniform draws.

The earlier projection report contains the same stable-sort ingredient;
the proof here rederives the portion needed for planting and does not import
its external mixing estimates.

## 2. The complete likelihood ratio is a witness count

Define X_k(W)=sum_(|I|=k) 1[E_I(W)] and mu=E_D0 X_k=M p. Then

    D1(W)/D0(W) = X_k(W)/mu,                                  (2)
    TV(D1,D0) = E_D0 |X_k-mu| / (2 mu),                        (3)
    chi_squared(D1 || D0) = Var_D0(X_k)/mu^2.                  (4)

**Proof.** Each conditional law has density 1[E_I]/p with respect to D0.
Average over I, then use the definitions of TV and chi-squared. In particular
the optimal test accepts the planted world when X_k>mu. Cauchy-Schwarz also
gives TV <= sqrt(Var(X_k))/(2 mu). For any observable f,

    E_D1 f - E_D0 f = Cov_D0(f,X_k)/mu.                         (5)

Thus planting biases toward words with more witnesses. Merely having a
witness is a different statistic; conditioning on existence generally gives
a different distribution. Its distinguishing advantage is exactly
Pr_D0[X_k=0], since every planted word has a witness.

Full endpoint sign, cycle type, support and fixed-point count are identical
in both worlds: their endpoint is id. Word support and prefix/window products
can differ. Simultaneous label conjugation preserves both laws, so every
single gate position is exactly uniform on T in both worlds. These exact
symmetries are controls, not evidence of cryptographic hiding.

## 3. Complement symmetry exposes another efficient score

For W=(t_1,...,t_m), write P_j=t_1...t_(j-1) and define

    F(W)_j = B_j = P_j t_j P_j^(-1).

The product B_1...B_j equals (t_1...t_j)^(-1), by induction. Hence F maps
identity words to identity words and F(F(W))=W: the new prefix before j is
P_j^(-1), so conjugating B_j again returns t_j. In particular F preserves D0.

Replacing gates in J by identity and telescoping gives, when eval(W)=id,

    eval(W restricted to [m]\J) = product_(j in J, increasing) B_j.    (6)

One can also derive (6) by multiplying each prefix-conjugated correction
P_j t_j^(-1) P_j^(-1), in index order, into the original total product.
Transpositions are involutions, giving exactly B_j.

Thus X_k(W)=X_(m-k)(F(W)). Equation (1) is symmetric in k,m-k, so F carries
D1 at k to D1 at m-k and the two full TV distances agree exactly.

For k=2, X_2=sum_t binom(multiplicity_W(t),2). For k=m-2,

    X_(m-2)=sum_t binom(multiplicity_F(W)(t),2).                 (7)

Both scores take polynomial time; the latter needs a running permutation
table and transported edge counts, not enumeration of binom(m,m-2) subsets.
More generally a fixed r=min(k,m-k) permits O(binom(m,r) r) product work,
using F when needed. To implement the optimal decision threshold one also
needs mu or a learned threshold; computing the score alone is not a claimed
all-parameter sampler or normalization algorithm.

Split any word into two consecutive halves for a meet-in-the-middle count.
Let H_left[a,g] and H_right[b,g] count subsequences of cardinality a,b and
product g in each half. Then

    X_k = sum_a sum_g H_left[a,g] H_right[k-a,g^(-1)].           (8)

Computing half-products costs O(2^ceil(m/2) poly(N,m)) time and space using
literal permutation keys. This is an exponential attack in general, not a
polynomial algorithm for growing m. The checker validates it against full
subset enumeration. No presumed XOR commutativity is used.

## 4. Why the fixed-length large-N calculation is complete

**Proved.** Every used label in an identity word occurs in at least two
transpositions: if x occurs only in t=(x,y), write the product as A t B.
A and B fix x, while A t B sends x to A(y), which cannot be x. This is a
contradiction. Hence a length-m identity word uses at most m labels.

For each support size v<=m and witness count x, let a_(v,x) count length-m
identity words using every label of one fixed v-element set and having x
witnesses. Relabeling is a bijection, so for every N>=2,

    #{W in Omega(N,m): X_k(W)=x} = sum_(v<=m) binom(N,v) a_(v,x). (9)

The complete enumeration at N=m contains every coefficient. Our conjugation
orbit with weight w contributes w/binom(m,v) words on a fixed support set;
this quotient is an integer. Orbit representatives are generated by taking
the lexicographically smallest next edge under the stabilizer of the already
chosen prefix, then restricting that stabilizer. Induction on prefix length
gives exactly one representative per orbit; its weight is N!/|stabilizer|.
Completion counts only prune prefixes with no possible identity extension.

Equation (9) makes the recorded evaluations for m=8 and N up to 10^6 exact
integer calculations, not an extrapolation from an empirical trend. Values
at N=3,4,5,6 are checked against independent finite enumerations of those
parameters. The separate audit also checks the leading coefficient below.

**Proved, fixed-length limit only.** Let m=2r be fixed and k be fixed even.
At maximum support v=m, every used vertex has degree two. Every connected
component of an identity factorization on v_i vertices requires at least
2(v_i-1) factors: the first edges that join different support components
each merge permutation cycles, there are v_i-1 of them, and returning from
identity to identity needs at least as many cycle-splitting factors. A degree
two connected component has exactly v_i factors, so v_i<=2. Thus the
maximum-support words consist of r disjoint edges used twice each.

There are

    a_(m, binom(r,k/2)) = (m!)^2 / (4^r r!)                    (10)

such words on a fixed m-element label set: choose a perfect matching, then
order the doubled edges. They have exactly binom(r,k/2) witnesses. All other
support terms in (9) have degree at most m-1 in N. Therefore mu tends to
binom(r,k/2), and (3) gives

    TV(D1,D0) = O_(m,k)(1/N),  for fixed even m,k.              (11)

The constants are not controlled uniformly when m,k grow. This is not a
cryptographic negligible-error claim in security parameter N; inverse powers
are not negligible in N. It says that the large-N fixed-length agreement
comes from statistical convergence, not demonstrated computational hardness.
When N=2^n, explicit-N complexity is still exponential in n.

## 5. A conditional search consequence, and what is still missing

**Conditional proposition.** Suppose D0,D1 are computationally
indistinguishable along a specified efficient parameter schedule. If an
algorithm outputs any valid k-subset on a planted input with probability s,
then

    s <= Pr_D0[X_k>0] + negligible(lambda).                    (12)

Indeed, run the search algorithm and verify its proposed indices and ordered
product. This acceptance test runs in polynomial time in N,m. Its planted
acceptance is s and its null acceptance is at most Pr_D0[X_k>0]. If this null
probability is negligible, finding any witness is hard on planted inputs.
This does not require recovering the original planted I; arbitrary accidental
witnesses already satisfy the search goal.

The bound is nearly vacuous in the tested middle-length cases, where null
witness existence exceeds 93%. It does not prove that every possible
cryptographic application requires rare null witnesses. Nor does it produce
encryption, a one-way function or obfuscation without additional arguments.

**First unproved obligation (standalone).** Exhibit a schedule with growing
N,m and min(k,m-k), efficient samplers for D0 and the two shorter bridges,
and nonnegligible TV(D1,D0), for which the specified cheap statistics and
subset-search algorithms do not yield a nonnegligible efficient advantage.
Surviving those attacks would still be evidence, not proof of hardness. The
stronger search route additionally needs a small null witness-existence
probability, or a different precisely defined recovery goal.

## 6. A conditional recursive identity-word sampler

**Conditional theorem; stronger security model than the original template.**
Fix a schedule indexed by lambda with N,m polynomially bounded in lambda,
even m, and an even cutoff B>=2. Suppose:

1. Exact independent uniform bridges at every even length <=B can be sampled
   in expected polynomial time in N,m. A growing B requires an actual short
   bridge algorithm; it is not supplied by our factorial finite-state code.
2. At every internal length ell>B of the recursion below, the Q4 distributions
   U_ell and D1_(ell,k_ell), k_ell=2 floor(ell/4), are indistinguishable by
   **nonuniform probabilistic polynomial-size circuits**. More precisely the
   maximum advantage over the required lengths and any fixed polynomial
   circuit-size bound is negligible in the same lambda. This uniform bound
   across the polynomially many nodes is part of the assumption.

Define R_ell=U_ell at leaves ell<=B. Otherwise independently generate
R_(k_ell), R_(ell-k_ell), choose a fresh uniform index set, and apply the
inverse stable-sort map from section 1. Then R_m always evaluates to identity,
is efficiently samplable, and is computationally indistinguishable from U_m
under these two premises.

**Proof.** For an arbitrary output distinguisher, replace one child's law by
its exact uniform bridge law, then the other child's. Conditional on any fixed
sibling word, the parent transform followed by the distinguisher is a
polynomial-size distinguisher for that child. Nonuniform advice can contain
the fixed sibling word, whose representation has polynomial length. Averaging
over sibling words and fresh parent randomness cannot exceed the maximum
child advantage. With both children uniform the resulting parent law is
exactly D1_(ell,k_ell), whose distance from U_ell against such circuits is
bounded by the planting assumption. Induction gives a sum of one planting
advantage per internal node; there are fewer than m nodes. A uniform negligible
bound times this polynomial node count is negligible.

All transforms preserve identity. Splits are balanced to within two gates,
so the sum of squared node lengths is O(m^2). Thus the local transformation
cost is O(m^2) edge-conjugation operations, in addition to at most m/2 base
bridge draws and polynomial position-sampling work. This is an expected
polynomial identity-word generator under premise 1, with no call to a
uniform length-m bridge sampler. Computational closeness concerns circuit
descriptions; the endpoint function is the known identity in both worlds.

**Why the security strengthening matters.** The original Q4 note says PPT
adversaries on one word and supplies no general efficient uniform bridge
sampler. A uniform reduction cannot automatically sample an exact sibling
bridge to simulate the second child replacement. Hardwiring it uses
nonuniform advice. The theorem therefore does **not** silently claim a
consequence of the original uniform single-sample statement alone. An
alternative would be an explicitly justified auxiliary-input/composable
assumption, or efficient exact sibling samplers, with their costs stated.
Supplying efficient full-length reference samplers would already remove the
main sampling motivation. No necessity of nonuniformity is proved; the
uniform-only reduction remains unestablished here.

Premise 2 must hold at every internal length, not just the top length. A base
of doubled gates forces it to include length four, where the repeated-pair
attack is explicit. The exact finite recursive experiment shows the danger:
at N3,m8 the TV is 0.223476 with exact base length two, versus 0.067411 with
exact base length four. This is a counterexample to treating a nested plant
as having the single top-level planting law. It does not refute the theorem,
whose short-level indistinguishability premise is absent in that example.

This supplies a concrete potential application of a suitable strengthened
planted assumption: computational sampling of global identity descriptions
from short exact bridges. No surviving schedule meeting premise 2 has been
found, so it remains a conditional construction, not a secure sampler.

## Dependencies, falsification and scope

- **Proved here:** (1)--(12), conditional statements retaining their premises;
  orbit enumeration completeness and the fixed-m support-polynomial argument.
- **Existing input rederived:** stable sorting from
  `experiments/20261028-bridge-projections/report.md`; no literature mixing
  theorem, Hurwitz transitivity classification or local-chain gap is needed.
- **Exact finite facts:** checker and independent literal audit, as recorded
  in results.json and audit-results.json. These do not prove asymptotic hardness.
- **Conditional:** the recursive computational sampler in section 6 uses
  exact short bridges and an explicitly stronger nonuniform planting
  assumption at every internal scale. Its uniform-only reduction is open.
- **Unresolved:** a schedule satisfying the stated security premises,
  efficient all-length exact bridge generation, and a secure instantiation
  or other cryptographic application of the original template.

Boundary checks cover N2, m0,m2, odd m/k, k0/km, all masks in every enumerated
case, and near-minimal connected words inside the global fibers. Literal
counts independently reproduce 27/120/3936 on the mandatory smoke cases.
Sampler bijections are checked exhaustively on all mandatory fixed-I fibers.
Complement equality is checked on every orbit for k=m-2 and on all masks of
the first 30 orbits of each case. No connected/global law is interchanged.

No manuscript paragraph is proposed: this is a first foreground diagnostic,
without an independent proof review or a surviving cryptographic regime.
