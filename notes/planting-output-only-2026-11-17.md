# Planting functionality with only input/output access

Date: 2026-11-17, Europe/Berlin.

Scope: the user explicitly selected only input/output access to the final
circuit and requested no heavy experiments. This is a bounded mathematical
follow-up to Q4, not a launch of the historical mixing campaign in GOAL_SPEC.
No experiment was run. The elementary proofs below are author arguments,
not independently reviewed results; no novelty claim is made.

## 1. Interface, targets, and the earlier attack

An adversary receives ideal, classical, adaptive oracle access to the final
function, with at most q queries. It receives neither gates, internal wire
values, implementation-dependent timings, nor secret keys. All public
information is identical between the two games. The advantage is the absolute
difference between acceptance probabilities, not success probability minus
one half. Quantum queries are outside this note.

Use security parameter lambda, with circuit sizes and q polynomial in lambda.
For Boolean functions the reference R is a uniformly random function from a
specified finite domain X to Y. For reversible functions the reference is
uniform in a specified permutation group G, or its explicitly stated coset.
Random gate descriptions do not automatically induce either reference law.
Composition is rightmost first: (A o B)(x)=A(B(x)). There is no Markov kernel.

The earlier [scaling report](../experiments/20261110-planted-scaling/report.md)
concerns explicit transposition descriptions, polynomial time in degree N
and length m, and negligible advantage in N. Its inverse-polynomial attacks
inspect pairs of gates. It does not establish an attack on this oracle game.

**Proved.** If both challenge circuits compute identity, their oracle laws
are exactly equal, even for computationally unbounded adversaries. Every
query x receives x in both games. This covers every feasible instance of the
old model, including m=0, m=2 and N=2; odd transposition identity lengths
remain infeasible. This hides the internal planting perfectly, while the
external functionality remains the same known identity.

## 2. A small hidden input region: a direct coupling theorem

Let F:X->Y be any fixed or randomly sampled function. Independently sample a
secret z defining S_z subset X, such that for every x in X,

    Pr_z[x in S_z] <= rho.

There is no auxiliary information correlated with z available to the
adversary. The base F and all public information are independent of z. Define
F'_z to agree with F outside S_z, with arbitrary values on S_z.

**Proved.** For every classical adaptive q-query adversary A,

    |Pr[A^(F'_z)=1] - Pr[A^F=1]| <= min(1,q rho).             (1)

The probabilities average over the secret z, function sampling and adversary
randomness. This is a statistical transcript guarantee; F need not be random
or pseudorandom, and A need not be computationally bounded.

**Proof.** Couple the games using the same F and adversary random tape. Run
the unmodified game first, producing a query sequence x_1,...,x_q independent
of z. The transcripts in the two games coincide until a query hits S_z.
A union bound on this unmodified sequence gives probability at most q rho
of any hit. If no hit occurs, induction on the queries shows that the
modified game has exactly the same query sequence and replies. Coupling
therefore proves (1). No assumption that queries are nonadaptive is needed.

For a uniformly chosen secret s-element set S in a D-element domain,
rho=s/D. Merely assuming |S|/D is small, with a public or otherwise predictable
S, is insufficient for chosen-input access. The independence and pointwise
probability assumptions do the work.

## 3. Efficiently planting an arbitrary useful function

Let F_K:{0,1}^{t+d}->{0,1}^ell be a secure PRF. Let
h:{0,1}^d->{0,1}^ell be any efficiently computable public function, independent
of the secret key and trigger. Sample z uniformly from {0,1}^t independently
of K and define

    C_(K,z)(a,b) = h(b),          if a=z;
                  F_K(a,b),     otherwise.                  (2)

All t,d,ell and |h| are polynomially bounded in lambda. A circuit implements
this using an equality test and output selection in addition to F_K and h.
Its size is O(|F_K|+|h|+t+ell) in an ordinary Boolean gate model.

**Conditional on PRF security; proved reduction.** For a PPT adversary making
at most q queries,

    Adv(C_(K,z), R) <= epsilon_PRF(A,q) + min(1,q/2^t).       (3)

Here epsilon_PRF(A,q) is A's ordinary PRF distinguishing bound when run on
the unmodified oracle. Equation (1) compares C_(K,z) to F_K directly, and
the triangle inequality compares F_K to R. A hybrid need not expose z.

Taking t=lambda makes the additional error negligible for every polynomial
q. One may also take d=lambda: the planted region then contains 2^lambda
inputs, despite occupying only a 2^(-lambda) fraction of the full domain.
Someone who knows z can evaluate the entire planted functionality by querying
(z,b). Thus the plant need not itself be pseudorandom; its hidden activation
region suffices. If a pseudorandom h is desired, it is a special case, with
its key sampled independently.

For arbitrary polynomial q, t=omega(log lambda) is a sufficient asymptotic
condition. A fixed t=c log_2 lambda does not give negligible error in general:
with a random-function host, query one fixed (a,b) and test whether the answer
equals h(b). Its exact advantage is 2^(-t)(1-2^(-ell)). Revealing z instead
gives a one-query advantage 1-2^(-ell) against R. These are boundary
falsifications of weaker claims about small or public regions.

This is a construction of a Boolean function with hidden behavior, not a
theorem about replacing a small number of gates in an arbitrary random
circuit. Directly overwriting permutation values may destroy bijectivity.
A reversible implementation of the evaluation map
(x,y)->(x,y XOR C_(K,z)(x)) has the corresponding evaluation-oracle reference
(x,y)->(x,y XOR R(x)); that reference is not uniform over all permutations.

## 4. What replacing a random block by a pseudorandom one proves

The PRF definition here is the standard adaptive oracle definition; see
[Barak's PRF lecture](https://intensecrypto.org/public/lec_04_pseudorandom-functions.html),
the definition and its explanation of black-box access. The use of that
definition below is proved directly and does not require another literature
theorem.

Let T be an efficient oracle construction: given oracle access to B, it
answers queries to the larger circuit T^B. Its public data and randomness
can be sampled without learning B's secret key or inspecting its code.
Polynomially many final-circuit queries cause polynomially many B queries.
If B_0 and B_1 are computationally indistinguishable as oracles, then

    T^(B_0) approximately_c T^(B_1).                         (4)

**Proved reduction.** A distinguisher for the larger circuit can be simulated
using a challenge B oracle; forward each internal B query and return the
construction's answers. Its advantage is unchanged. This works even for a
large or publicly located block. Smallness is not necessary.

Equation (4) compares the same construction with different blocks. If R is
random, P pseudorandom and T performs planting, it gives T^P approximately_c
T^R. To conclude T^P approximately_c R one must also prove T^R approximately_c
R. The latter is a separate preservation statement. Equation (1) is one way
to supply it. A construction that replaces every output by zero satisfies
(4) but plainly fails that preservation statement.

For a block whose description is exposed, ordinary PRF security supplies no
such reduction. Likewise, a host completion conditioned on the block's
endpoint is not an independent context: its sampler must be implemented in
the reduction. An exponentially expensive rejection procedure does not give
a PPT reduction. These limitations matter when returning to the older
identity-word sampling problem, but the user's present interface is oracle
access only.

## 5. Reversible circuits: independent masks give another positive theorem

**Proved.** Let G be a finite permutation group. Let U be uniform on G and
let H in G be any fixed permutation, or an independent random permutation.
Then

    U o H has exactly the uniform law on G.                 (5)

For fixed H and g in G, Pr[U H=g]=Pr[U=g H^(-1)]=1/|G|;
averaging over H proves the random-H statement. If the mask law M has total
variation distance at most eta from uniform, then M H has distance at most
eta: right translation preserves TV for fixed H and mixtures contract it.

**Conditional on PRP security; proved reduction.** Suppose P_K is an
efficient PRP for the stated reference group and H is an efficiently
computable independent permutation in that group. Then P_K o H is also
pseudorandom against forward oracle queries: simulate query x by querying
the challenge oracle at H(x); the uniform hybrid is (5). No bound on the
relative size of H is needed. For inverse access, assume strong PRP security
and efficient H^(-1), and simulate C^(-1)=H^(-1) o P_K^(-1).

This statement applies to the actual reference group. A fixed-length
all-transposition walk has fixed sign; its matching ideal mask is uniform
on the corresponding parity coset, and multiplication translates that coset.
One cannot silently compare it to uniform S_N. A local gate library confined
to A_(2^n) similarly requires the declared group reference and its own
efficient mask justification.

Masking hides a contained implementation of H, but the raw external output is
P_K(H(x)), not H(x). An observer with the mask key can undo the mask. The
secret-trigger construction in section 3 instead provides directly
accessible h outputs on secret inputs. These are different applications.

## 6. Small gate count is not the missing theorem

**Refuted as a general implication.** Replacing a small fraction of gates
does not imply that few inputs are affected or that the new oracle is
pseudorandom. In a one-bit-output Boolean implementation, changing the final
output logic to zero makes every answer zero. Padding the rest of the
circuit with irrelevant gates makes the edited fraction arbitrarily small.
Two distinct oracle queries accepting exactly when both answers are zero
have acceptance 1 after this edit and 1/4 for a uniform random function.

The preservation claim also fails for an independent noninjective
preprocessor: R o D has a forced collision whenever D(x)=D(x') for known
distinct x,x'. Testing equality has advantage 1-1/|Y| against a random
function. Invertibility in the group-mask argument is essential.

Conversely, changing a reversible gate can affect many inputs without
creating a distinguishable ensemble; (5) demonstrates this. The affected-input
bound is sufficient, not necessary. Gate count alone settles neither case.

**Unresolved first obligation for literal subcircuit replacement.** Fix a
gate library, host distribution R_m, replacement rule T, public information,
and size schedules polynomial in lambda. Prove, for every PPT q-query A,

    |Pr[A^eval(T(R_m))=1] - Pr[A^eval(R_m)=1]| <= negl(lambda). (6)

A useful narrower sufficient lemma is either a coupling whose modified input
region has negligible query-hit probability, or an independently justified
random/PRP mask across the replacement interface. Neither follows from a
small edited-gate fraction. If a random circuit is the desired baseline,
its closeness to a random function/permutation is an additional obligation.
Once (6) holds, replacing relevant oracle components by secure PRFs/PRPs
uses (4). No claim about arbitrary circuit descriptions is needed.

## 7. Dependencies, checks, and claim ledger

The positive oracle statements are self-contained coupling, simulation and
finite-group arguments. Efficient cryptographic instantiations assume PRF
or appropriately represented PRP security as stated beside each result.
The old spectral attacks are recalled only to identify their different
interface; their spectral theorem is not an input to these new proofs.

Boundary checks are mathematical: q=0 gives zero advantage; rho=0 gives
identical oracles; t=0 allows arbitrary full-domain replacement; public z
admits the direct test above; a nonpermutation H invalidates (5). Old odd
m/identity and short-length boundaries were addressed in section 1. There
is no transposition genus restriction on the separate Boolean constructions.

| Claim | Status | Assumptions | Evidence/artifact | Independent check | Action |
| --- | --- | --- | --- | --- | --- |
| Old identity plants are invisible to I/O | proved | Both final functions identity; ideal oracle | Section 1 | None; direct query induction | Retain interface distinction |
| Hidden-region change costs at most q rho | proved | Independent secret region; pointwise hit bound | Section 2 coupling | None; public-region counterexample checked analytically | Keep |
| Arbitrary h can be planted on a secret prefix | conditional | Secure PRF; secret independent z; polynomial sizes | Section 3 and (1) | None; short/public trigger boundaries checked analytically | Keep as oracle construction |
| Oracle replacement preserves indistinguishability | proved | Efficient oracle context, matching public information | Section 4 simulation | None; constant-output obstruction checked | Keep with exact comparison target |
| Independent uniform mask hides reversible H | proved | H in same group; independent mask | Section 5 counting | None; noninjective counterexample checked | Keep |
| Efficient masked construction is pseudorandom | conditional | Appropriate PRP security and efficient H | Section 5 reduction | None | Keep conditional |
| Few edited gates suffice for oracle hiding | refuted | Universal statement over Boolean circuits | Section 6 output counterexample | None; exact two-query probabilities | Reject universal claim |
| Generic random local-circuit replacement is hidden | unresolved | Host, surgery and parameters still to be specified | Equation (6) | No experiment or proof claimed | First future target |

No manuscript or HANDOFF change is proposed at this review depth. The
existing full-description planting obstruction and unresolved linear-host
regime remain intact. The new affirmative results concern the separately
declared oracle game.
