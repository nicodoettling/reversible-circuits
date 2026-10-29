# Projections and Random Gate Replacements

Verdict: **keep the exact elementary identities and their proved implications**.
Finite checks passed; they are falsification evidence, not an asymptotic proof.
This is a foreground derivation, not a new long-run or independently audited
manuscript theorem. Central maps and completed-run sources remain unchanged.

## Model and status

N>=2, L even, 0<=k<=L. Let T be all q=binom(N,2) transpositions, mu its
uniform probability law, and p_r=mu^{*r}, p_0=delta_id. Products act rightmost
first. Positions1<=i1<...<ik<=L are fixed independently of the sampled word.
Replacements are independent mu draws, also independent of the original word.
The primary word law is uniform on GLOBAL Omega(N,L). Uniform connected-support
words are a different law. An arbitrary identity-word sampler need not satisfy
either distributional conclusion, however large L is.

Exact identities below are proved here by explicit bijections/counts. The
mixing-scale corollary imports classical random-transposition Fourier estimates,
with its nonlazy parity translation given below. No literature novelty claim.
The targeted notes search did not locate these particular projection/replacement
identities; older conditional heat-bath projection algebra is a separate topic.

## 1. Position-independent ordered subsequence law

Move each selected gate left across every earlier unselected gate using

    (u,s) -> (s,sus).

The selected gate s is unchanged. A fixed stable-sort sequence is an invertible
Hurwitz action: every gate stays a transposition, the full product stays id,
and selected gates appear as the first k entries in their original order.
It also preserves support connectivity. Consequently, under either uniform
target every fixed ordered k-subsequence has exactly the first-k law. This is
NOT exchangeability under arbitrary permutations of the selected values.

For the GLOBAL target, if h=a1...ak, direct completion counting therefore gives

    Pr[(t_i1,...,t_ik)=a] = q^(-k) p_(L-k)(h^(-1)) / p_L(id).       (1)

Let nu_I denote this tuple law. Its TV distance from mu^{tensor k} is exactly

    D = (1/2) E_(H~p_k) |p_(L-k)(H^(-1))/p_L(id) - 1|.             (2)

Conditional on H, both tuple laws are uniform on their product fiber, which
explains why only the endpoint H enters. One coordinate is exactly mu by
simultaneous-conjugation symmetry. Full projection k=L has TV1-p_L(id), so
large L alone cannot guarantee independent gates for every k.
Every projected product has transposition distance at most L-k: after stable
sorting it has an inverse completion of that length. Thus

    D >= Pr_(H~p_k)[N-number_of_cycles(H) > L-k].                    (3)

## 2. Exact replacement endpoint law and contraction

For a fixed original word, write P_j=t1...t_(j-1), and at selected positionj
set B_j=P_j t_j P_j^(-1), A_j=P_j t'_j P_j^(-1). A telescoping product gives

    product(w') = product_(j selected, increasing) (A_j B_j).       (4)

Conditional on the complete original word, the A_j are independent mu and
their conditional joint law does not depend on the word. Therefore they are
independent of the B tuple. The B_j are NOT assumed independent.

The full map F:t_j -> P_j t_j P_j^(-1) is triangular and invertible. Indeed
the product of its first j factors is (t1...tj)^(-1), and the original prefix
can be recovered recursively from those factors. Hence it preserves the
identity-word space. Each prefix generates the same subgroup as its image,
so full support connectivity is preserved too. It follows that under either
uniform target the selected B tuple has exactly the original selected tuple
law nu_I. This conclusion requires the word-law invariance, not just (4).

Independent mu insertions in (4) define a Markov channel taking mu^{tensor k}
to p_(2k). Data processing proves

    TV(law(product(w')), p_(2k)) <= TV(nu_I, mu^{tensor k}).         (5)

Because mu is conjugation invariant, it commutes under convolution with every
point mass. If rho is the product distribution of the selected original tuple,
there is also an EXACT formula

    law(product(w')) = p_k * rho.                                 (6)

For the global target rho(h)=p_k(h)p_(L-k)(h^(-1))/p_L(id).
Equations(5)/(6) also hold for uniform CONNECTED bridges, with their own rho.
Thus the endpoint requirement can be strictly weaker than tuple independence.
For k1 it is exactly p2 under both uniform targets, for every feasible length.
For an eta-approximate sampler for either target, add at most eta to the
corresponding exact-target errors, by data processing of the full word law.

## 3. Long-bridge sufficient conditions and parity

Let U_r be uniform on permutations of parity(-1)^r, and put

    delta_r = max_(sign(h)=(-1)^r) |p_r(h)/(2/N!) - 1|.

The transposition-only walk is period two: it never approaches uniform S_N
at a fixed time. Since L is even, every H in (2) has the correct completion
parity. If delta_(L-k)<=delta<1, both numerator and denominator in (1), relative
to2/N!, lie in[1-delta,1+delta]. Taking the mean absolute deviation gives

    D <= delta/(1-delta).                                        (7)

Classical bounds imply delta_r<=epsilon for

    r >= C N (log(N+1)+log(1/epsilon)),                           (8)

with a universal sufficiently large C. This is a sufficient condition, not a
sharp characterization. One explicit translation avoids confusing the lazy
and nonlazy walks. If theta_lambda is a pure-transposition character ratio,
the original Diaconis-Shahshahani lazy eigenvalue is

    alpha_lambda = 1/N + (N-1)theta_lambda/N.

Conjugate partitions pair theta and -theta with equal dimensions. For t>=1,

    delta_(2t) = (1/2) sum_(lambda != trivial,sign) d_lambda^2 theta_lambda^(2t)
               <= sum_(lambda != trivial) d_lambda^2 alpha_lambda^(2t)
               = chi_square(lazy_t,uniform_S_N).

The equality for delta_(2t) follows from Fourier inversion and
|character(h)|<=dimension, with the maximum attained at identity. The
classical L2 estimate is O(exp(-c)) at t=(N/2)(log N+c), so its square bounds
the displayed chi-square term. Relative pointwise distance is nonincreasing
across parity classes under another mu step, giving odd r as well. The finitely
many small N can be absorbed in C; N2/N3 have simpler exact parity mixing.

Primary source: Diaconis-Shahshahani, Generating a Random Permutation with
Random Transpositions, Z. Wahrscheinlichkeitstheorie57(1981),159-179,
Theorem1 and Section3's Fourier sum. Their step includes identity mass1/N;
the preceding eigenvalue comparison is necessary for our transposition-only
model. Author survey restatement with explicit L2 bound: Saloff-Coste,
Random Walks on Finite Groups, Theorem9.2, pp326-327.

Sources read:
- https://www.imo.universite-paris-saclay.fr/~pierre-loic.meliot/symmetric/texts/Diaconis,%20Shahshahani%20-%20Generating%20a%20random%20permutation%20with%20random%20transpositions.pdf
- https://pi.math.cornell.edu/~lsc/papers/chap5.pdf

Thus L-k satisfying(8) suffices for both requested errors to be O(epsilon),
uniformly over ALL fixed choices of positions. No spacing condition is needed.
Choose epsilon=N^(-omega(1)) for negligible error; a sufficient regime is
(L-k)/(N log N)->infinity. L=N3 and k<=L/2 comfortably suffices.

There is a different sufficient condition for the ENDPOINT alone. For ANY
original identity word, even deterministic, (4) and centrality show its endpoint
law is p_k convolved with some parity(-1)^k distribution. If
d_k=TV(p_k,U_k), contraction and the triangle inequality give

    TV(law(product(w')), p_(2k)) <= 2 d_k.                         (9)

Here the hidden old product is the conjugated B product, not necessarily the
raw selected tuple product under a non-invariant word law. Standard parity
mixing makes(9) small for k>=C N(log(N+1)+log(1/epsilon)), independently of L
apart from feasibility k<=L. Combining(7)/(9), a global uniform bridge with
L>=2C N(log(N+1)+log(1/epsilon)) has the desired endpoint law for EVERY k,
after enlarging the universal constant. This says nothing equivalent about
all k-tuples, which retain the k=L obstruction.

## 4. Connected near-minimal bridges: explicit negligible-error obstruction

Equation(1) is NOT valid after imposing connected support. A connected-target
transfer from the global law costs the global probability of disconnected
support, which needs its own bound. Our recent efficient connected sampler has
L=2N-2+O(log N), not the long-completion regime in(8).

There is already a precise obstruction at genus0, L=2N-2, N>=3. The inherited
minimal connected count is C0(N)=(2N-2)!N^(N-3). Consider words starting with
(ab),(ab), followed by a minimal connected bridge on all labels except a.
There are N(N-1)C0(N-1) such distinct words: a is the unique label absent from
the remainder. Hence for the uniform connected target,

    Pr[t1=t2] >= p_leaf
      = N/((2N-2)(2N-3)) * (1-1/N)^(N-3)
      ~ 1/(4 e N).

For independent uniform transpositions this probability is1/q=O(N^-2).
Therefore any fixed two-coordinate projection has TV>=p_leaf-1/q=Omega(1/N).
This vanishes, but is NOT negligible. Position independence from Section1
makes the obstruction apply to every fixed pair of distinct indices.

The ENDPOINT is not automatically negligibly close either. For k2, (6) gives
Pr[product(w')=id]>=p_leaf/q=Omega(N^-3), whereas four independent random
transpositions give

    p4(id) = [q^2+18 binom(N,3)+12 binom(N,4)]/q^4 = O(N^-4).

Consequently endpoint TV is at least p_leaf/q-p4(id)=Omega(N^-3).
This does not refute a negligible bound at other lengths/genera; it rules out
a blanket claim covering all of the recent connected sampler's parameter range.
For k1 both quantities remain exact, so the k2 obstruction is substantive.

## Finite validation and next target

Reproduce with:

    timeout 60s python3 -B experiments/20261028-bridge-projections/check.py

Python3.12.3, standard library, deterministic exact counts/Fractions, no random
seed,512MiB RLIMIT_AS. results.json records the actual commit, timing, cases,
all index-set checks and raw distances. Mandatory global S3L4/S4L4/S4L6 counts
27/120/3936 pass; connected counts are distinguished explicitly.
For N4,L4,k2 the tuple distance is2/15 but the endpoint distance is7/540.
All replacement choices and all fixed sets of size<=2 were checked. The
asymptotic conclusions above rely on the separate arguments, not enumeration.

Highest-value next target: sharpen(2) for short/intermediate GLOBAL bridges,
and derive the corresponding connected completion ratios for specified genus.
Separate negligible error from inverse-polynomial error. For the replacement
question, optimize the smoothed distance TV(p_k*rho,p_(2k)), not the stronger
and sometimes unnecessary full tuple-independence requirement.

candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict
---|---|---|---|---|---
Projection/completion identities | declared global/connected laws, not a new sampler | preserved by the proved bijections | not a walk proposal | exact small laws and replacements | keep elementary identities; asymptotic mixing imports explicit
