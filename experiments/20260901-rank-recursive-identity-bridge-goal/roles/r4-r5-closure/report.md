# R4/R5 final report: arbitrary-endpoint closure and dense error telescope

Date: 2026-09-01 UTC

## Resolution

**Proved, with an explicit fixed-accuracy limitation.**  Combining the R1
stable-sort bijection, the R2 positive two-sided branch sampler, and the R3
exact star sampler gives a polynomial-state recursive sampler for the dense
top-level bridge after one explicit retained-length conditioning.  For all
sufficiently large top ranks `N`, it always outputs a length-`2N^3` word with
the requested endpoint and its law has

```text
d_TV(output, U_(N,2N^3;g))
 <= 3N exp(-N/12288)                                  (R4/R5)
```

uniformly over every feasible external `g in S_N`.  In particular it applies
to the public endpoint `g=e`, and its error is negligible in `N`.

Every recursive child has an arbitrary labeled endpoint and an arbitrary
length above an explicit rank floor; the algorithm does not recurse only on
the scheduled lengths `2r^3`.  Only old-long branches recurse.  Star-long
branches draw the actual old word and terminate the rank recursion.

The accuracy is not arbitrarily tunable at fixed `L=2N^3`.  The proved
sampler meets a requested `epsilon` whenever

```text
epsilon >= 3N exp(-N/12288).
```

No argument here lowers the error beneath that floor merely by spending time
polynomial in `log(1/epsilon)`.  Exact arbitrary-short recursion also remains
reduced to R2's positive stabilizer-connection sampler.  These limitations
must remain visible in the coordinator classification.

## 1. Convention, target, and feasibility

Permutations are maps with

```text
(alpha beta)(x)=alpha(beta(x));
```

the rightmost factor acts first.  A displayed word `t_1...t_L` is generated
by successive right multiplication and has exactly that product.

For `c(g)` the number of cycles including fixed points, put
`ell_T(g)=r-c(g)`.  For `r>=2`,

```text
Omega(r,L;g) is nonempty
iff sign(g)=(-1)^L and L>=ell_T(g).                  (1.1)
```

Necessity follows because a transposition changes the cycle count by one and
has odd sign.  A cycle `(a_1 ... a_j)` has the rightmost-first factorization

```text
(a_1 a_j)(a_1 a_(j-1))...(a_1 a_2),
```

which proves minimal-length sufficiency; append pairs `tt` for every larger
same-parity length.

The target throughout the approximation proof is the global fixed-length
uniform bridge `U_(r,L;g)`, never an unconditioned endpoint law.

## 2. Complete exact Count/Sample recursion

At rank `r`, embed `H=S_(r-1)` as the stabilizer of `r`.  Write

```text
d = binom(r-1,2),
A_s(h) = [h] C_(r-1)^s,
B_k(q) = [q] J_r^k.
```

The R1 inverse audit fixes the orientation.  If the sorted old and star words
have endpoints `h` and `q`, respectively, then

```text
q=h^{-1}g,  equivalently h=gq^{-1}.                 (2.1)
```

Thus the complete exact recursion for every feasible endpoint and length is

```text
Count(r,L,g)
 = sum_(k=0)^L binom(L,k) sum_(h in S_(r-1))
     Count(r-1,L-k,h) StarCount(r,k,h^{-1}g).       (2.2)
```

The exact `Sample` procedure draws `(k,h)` proportionally to the summand,
draws the lower bridge recursively, invokes R3 on the prescribed star
endpoint, draws a uniform binary pattern, and applies R1's inverse map.  The
base `S_2` word is unique at every feasible length.  Equation (2.2), together
with these conditional samplers, is an exact closure specification for
`L=0`, odd or even feasible endpoints, minimal lengths, and pair-padded
lengths.

R3 proves each individual `StarCount/StarSample` query polynomial in `r,k`,
including arbitrary endpoints and nonminimal lengths.  It does not remove the
explicit `h` sum.  A permutation endpoint itself needs only `O(r log r)`
bits, but the literal implementation of (2.2) inspects `(r-1)!` labeled
endpoints.  In the dense regime a parity coset of such branches is positive,
so this explicit branch table has factorial inventory.  The R2 type-cell
compression still has partition-scale inventory.  These are rigorous
obstructions only to the specified enumeration/table implementations, not
sampling-hardness theorems.

## 3. The two-sided positive approximate lift

Let `s=L-k` be the old length, `b=r-1`, and

```text
x=g^{-1}(r).
```

For a star word `v` with endpoint `q`, (2.1) gives `h=gq^{-1}`.  It fixes the
pivot exactly when

```text
q^{-1}(r)=g^{-1}(r)=x,
```

equivalently `q(x)=r`.  The two forms agree; the latter is the R2 token
orientation.

Put

```text
Z_r(k,x)=#{length-k star words v: eval(v)(x)=r}.
```

If `z=r-1`, the exact two-state recurrence is

```text
u_0=1, v_0=0,
u_(j+1)=z v_j,
v_(j+1)=u_j+(z-1)v_j,
Z_r(k,x)=u_k if x=r, and v_k otherwise.             (3.1)
```

Equivalently,

```text
u_k=(z^k+z(-1)^k)/r,
v_k=(z^k-(-1)^k)/r.                                 (3.2)
```

The recurrence supports a uniform labeled token-bridge sampler in `O(rk)`
integer operations.  It samples factors in their applied order and reverses
them to return the displayed word.

After one common scale, the R2 approximate branch weights are

```text
r binom(L,k)d^s Z_r(k,x),  s>=k,                    (3.3a)
  binom(L,k)d^s b^k,       k>s.                     (3.3b)
```

All weights are nonnegative integers.

### Old-long branch: `s>=k`

Replace `A_s(h)` by its parity-coset value

```text
2d^s/(r-1)!,
```

retain the exact star-coset law using (3.1), set the actual labeled
`h=gq^{-1}`, and recursively sample the lower bridge `(r-1,s,h)`.

### Star-long branch: `k>s`

Draw `s` independent uniform old transpositions.  This samples the actual
old word `u`, its labeled endpoint `h`, and the exact marginal weight
`A_s(h)/d^s` without a completion table.  Replace the star endpoint count by
its parity-flat value, then invoke R3 to sample a uniform star word with
endpoint `h^{-1}g`.  This branch already has its old word and therefore does
**not** recurse.

In either branch, draw a uniform old/star binary pattern and apply the R1
inverse.  The output endpoint is exactly `g`; approximation affects only its
law within that endpoint fiber.

## 4. Audit of the one-rank pointwise error

R2 proves, uniformly over every feasible `g`,

```text
Delta(r,L)=max{
 ((r-1)!-2)/2 * ((r-4)/(r-2))^ceil(L/2),
 (r!-2)/2     * ((r-2)/(r-1))^(floor(L/2)+1)
},                                                     (4.1)
```

with the exact low-rank conventions, and

```text
d_TV(exact branch, two-sided branch)
 <= Delta/(1-Delta)       when Delta<1.              (4.2)
```

This is a pointwise relative completion-weight theorem, not merely endpoint
TV mixing.

The spectral constants have an independent graph audit.  Apply
Caputo--Liggett--Richthammer, Theorem 1.1, to:

- `K_(r-1)` for the old all-transposition walk, whose one-particle
  Laplacian gap is `r-1`;
- the star graph `K_(1,r-1)` for the star walk, whose gap is `1`.

After normalizing by generator degree and using multiplication by `sgn` to
pair negative and positive eigenvalues, the nontrivial absolute radii are
exactly `(r-4)/(r-2)` and `(r-2)/(r-1)`.  This independently confirms both
terms of (4.1) and avoids a left/right convention issue.

The primary theorem is P. Caputo, T. M. Liggett, and T. Richthammer,
*Proof of Aldous' spectral gap conjecture*, JAMS **23**(3) (2010), 831--851,
Theorem 1.1, DOI
[10.1090/S0894-0347-10-00659-4](https://doi.org/10.1090/S0894-0347-10-00659-4).

## 5. Explicit retained-length floors

The remaining issue is recursive length, not endpoint state.  Fix the global
top rank `N` and define the integers

```text
ell_N = ceil(log_2 N),
z_N   = ceil(sqrt(N ell_N)).
```

For `6<=j<=N`, use the positive rational weights

```text
w_j = 1/(j ceil(sqrt(j))) + 100 z_N/(N j),
W_N = sum_(j=6)^N w_j.                                (5.1)
```

Put

```text
c_5=1,
c_r=1+(sum_(j=6)^r w_j)/W_N,  6<=r<=N,
B_4=0,
B_r=ceil(N r(r-1)c_r),        5<=r<=N.               (5.2)
```

For `N>=6`, `c_N=2`, so

```text
B_N=2N^2(N-1)<2N^3.                                  (5.3)
```

Ranks at most four have exact polynomial-time special samplers: `S_2` has a
unique word; `S_3` has singleton old parity classes; at rank four the old
`S_3` walk is exactly parity-uniform after positive length, while the sole
zero-old branch is handled by R3.  Thus `B_4=0` is valid.

At rank `r>=6`, retain every star-long branch.  Retain an old-long branch
only when

```text
s>=B_(r-1).                                           (5.4)
```

At rank five every child has rank four and is handled exactly, so no
truncation is needed there.  Condition (5.4) guarantees that every recursive
child is in the next retained domain.  It also gives `s>=r-2`, so parity
alone implies feasibility of the actual labeled child `h`.

All quantities in (5.1)--(5.4) are rational/integer and can be computed with
polynomially many bits and operations.  No irrational comparison is used by
the sampler.

## 6. Exact conditioned mass of discarded old-long branches

This section proves the key survival lemma uniformly in the external
endpoint.

Assume the explicit large-`N` conditions

```text
100 z_N(1+log N)/N <= 15/8,
12 z_N <= N,
log N <= N/4,                                         (6.1)
```

where unadorned `log` is natural.  These conditions hold for every
sufficiently large `N`.

The decreasing-series bound

```text
sum_(j=6)^infinity j^(-3/2) <= 9/8
```

and the harmonic bound give `W_N<=3`.  Therefore, for `r>=6`,

```text
c_r-c_(r-1)=w_r/W_N.
```

Let `A` be the number of old transposition types in an unconditioned
length-`L` word at rank `r`.  Since

```text
M_r=binom(r,2), d=binom(r-1,2),
```

we have

```text
A~Bin(L,p),  p=d/M_r=(r-2)/r.                       (6.2)
```

For fixed cutoff `B_(r-1)`, `Pr[A<B_(r-1)]` decreases with `L`, so it is
enough to use `L=B_r`.  If `mu=pL`, ceilings and (5.1)--(5.2) give

```text
mu-B_(r-1)
 >= N(r-1)(r-2)(c_r-c_(r-1))-1
 >= N sqrt(r)/32 + 6 z_N r
 =: t_0.                                               (6.3)
```

Here `(r-1)(r-2)>=3r^2/8` and
`ceil(sqrt(r))<=2sqrt(r)` were used.

Equivalently, the star count `K=L-A` is binomial with mean
`lambda=2L/r`.  At `L=B_r`, `c_r<=2` gives `lambda<=5Nr`.  From (6.1),
`t_0<=33Nr/64`.  The binomial Bernstein bound, and monotonicity of
`t^2/(2(lambda+t/3))` in `t`, now give

```text
Pr[A<B_(r-1)]
 <= exp(-t_0^2/(2(lambda+t_0/3)))
 <= exp(-N/12288-3r log N).                         (6.4)
```

Indeed, the two squared terms in (6.3), divided by `12Nr`, contribute
`N/12288` and at least `3r ell_N>=3r log N`, respectively.

Equation (6.4) is unconditioned only as an intermediate count.  To control
the exact bridge, let `P_r` be the full random-transposition operator.  On the
correct parity class, the same pointwise spectral argument as in Section 4
gives

```text
P_r^L(e,g) >= 2/r! - (1-2/(r-1))^L.                 (6.5)
```

For `L>=B_r>=Nr(r-1)`, (6.1) makes the relative error in (6.5) less than
`1/2`.  Hence

```text
|Omega(r,L;g)| >= M_r^L/r!                           (6.6)
```

uniformly over every feasible `g`.

The number of endpoint-`g` words with old count below `B_(r-1)` is at most
the total number of unconditioned words with that old count, namely
`M_r^L Pr[A<B_(r-1)]`.  Dividing by (6.6) and using `r!<=N^r` proves

```text
Pr_(U_(r,L;g))[discarded old-long branch]
 <= exp(-N/12288-2r log N)
 <= exp(-N/12288).                                   (6.7)
```

This is the required uniform bridge-conditioned survival bound.  It does not
assume that conditioning leaves factor types independent.

For completeness, let `Q` be the untruncated two-sided proposal.  From the
pointwise likelihood-ratio interval in R2, when `Delta<=1/2`,

```text
Q(discarded) <= 3 U_(r,L;g)(discarded).              (6.8)
```

Thus a rejection implementation has expected fewer than two trials for all
sufficiently large `N`.  The preferred implementation does not reject: it
sets the finitely many discarded old-long `k` weights to zero and performs
one exact range draw from the remaining integer weights.

## 7. One-rank error and exact telescope

For every retained call `L>=B_r`, (4.1) and (6.1) give

```text
Delta(r,L) <= exp(-Nr/4).                            (7.1)
```

For the star term, use `k>=L/2`,
`(1-1/(r-1))^k<=exp(-L/(2(r-1)))`; the old term is
smaller because its exponent is at most `-L/(r-2)`.  The factorial prefactors
cost at most `r log r`, absorbed by `log r<=N/4`.

Let `Q_r^G` be the two-sided proposal conditioned on the retained set.  On
that set, every exact/flat unnormalized likelihood ratio remains in
`[1-Delta,1+Delta]`.  If `b_r` is the exact discarded mass, then

```text
d_TV(U_(r,L;g), Q_r^G with an exact lower child)
 <= b_r + Delta/(1-Delta)
 <= exp(-N/12288)+2exp(-Nr/4).                      (7.2)
```

Define `D_r` as the worst TV error of the actual recursive sampler over all
retained rank-`r` calls and feasible endpoints.  Star-long branches have no
child.  Every old-long child obeys (5.4), so Markov-kernel contraction gives

```text
D_r <= exp(-N/12288)+2exp(-Nr/4)+D_(r-1),           (7.3)
D_4=0.
```

This is the exact rank telescope requested in `(E)`, now uniform over all
retained arbitrary endpoints and lengths.  Equivalently allocate

```text
epsilon_r=exp(-N/12288)+2exp(-Nr/4),  5<=r<=N.
```

Summing (7.3), and loosening constants, yields

```text
D_N <= sum_(r=5)^N epsilon_r
    <= 3N exp(-N/12288).                            (7.4)
```

Together with (5.3), this proves the displayed R4/R5 theorem at
`L_N=2N^3`.

## 8. Algorithm and Turing complexity

For a retained call `DenseSample(r,L,g)`:

1. validate (1.1);
2. compute all `L+1` integer weights (3.3), setting an old-long weight to zero
   only when (5.4) fails;
3. draw `k` exactly by a fair-bit range draw;
4. in an old-long branch, use the token sampler, form `h=gq^{-1}`, and recurse;
5. in a star-long branch, draw the actual old word and use R3 for the star
   fiber;
6. draw a uniform binary pattern and apply the R1 inverse.

Ranks at most four use the exact special samplers described after (5.3).

The endpoint state is one labeled permutation, `O(r log r)` bits.  The branch
arrays contain `O(L)` integers of `O(L log r)` bits.  Token sampling and an
unconditioned old word use `O(rL)` elementary work; the R1 inverse uses at
most `O(L^2)` relabeling rewrites per visited rank.  Only one star-long branch
can occur on a recursion path, because it terminates; its R3 call has the
proved conservative `O(r^3L^3)` exact-rational-operation bound on
polynomial-bit integers.  A conservative overall bound is

```text
O(N^4 L^3)
```

exact-arithmetic operations on polynomial-bit integers, polynomial space,
and polynomial expected fair random bits.  Exact range rejection makes the
procedure Las Vegas in runtime; its distributional error is solely (7.4).

The conditions (6.1) fail for only finitely many top ranks.  A formal uniform
asymptotic algorithm can handle those fixed exceptions by the ordinary
finite-state backward bridge DP on `S_N`; since the exceptional set is fixed,
this contributes a fixed (though impractical) constant to the polynomial
bound.  The useful architectural theorem is the explicit large-`N` result,
not that finite-exception fallback.

## 9. Boundary audit

- **`N=2`.**  The unique transposition gives one word at every length, with
  endpoint determined by parity.
- **Ranks three and four.**  The exact low-rank constructions in R2 close the
  recursion without a dense hypothesis.
- **`L=0`.**  Return the empty word exactly when `g=e`; all other fibers are
  empty.
- **Odd `L`.**  The identity fiber is empty.  Arbitrary odd endpoints are
  accepted exactly when (1.1) holds.
- **Minimal endpoint length.**  The exact recursion (2.2) applies, but the
  dense approximation is not claimed.  This is the surviving exact R2
  connection primitive.
- **Pair padding.**  It proves feasibility but not mixing; all dense error
  estimates use the explicit floors rather than padding alone.
- **Generated internal states.**  Old-long children have correct sign by
  (2.1) and `s>=B_(r-1)>=r-2`, so every such arbitrary endpoint is feasible.
  Star-long branches do not generate child calls.
- **Infeasible external input.**  It is rejected before any flat weight is
  used.  For feasible `g`, parity compatibility of every sampled `h` is
  automatic from `sign(h)=sign(g)(-1)^k=(-1)^(L-k)`.

## 10. Exact finite checks and independent audits

The deterministic standard-library script
`check_flat_projection.py` independently checked the old-long half of the R2
architecture.  Exact command:

```text
python3 experiments/20260901-rank-recursive-identity-bridge-goal/roles/r4-r5-closure/check_flat_projection.py
```

at repository commit `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, Python
3.12.3, with no random seed.  Machine-readable selected output is in
`results.json`.  It recorded, with zero failures:

```text
1,064 stabilizer-coset convolution equalities,
29,018 h=gq^{-1} / projection orientation equivalences,
98 projected formula and backward-recurrence equalities,
975 exact pointwise kernel-entry inequalities,
1,050 full disintegration coefficient equalities,
19 exact rank-three flat-lift cases.
```

These finite checks can falsify the orientation, projection collapse, and
finite spectral inequalities, but cannot prove the asymptotic tail.

The finalized R2 artifacts independently check the full two-sided sampler for
every feasible endpoint at `(N,L)=(4,128)` and `(5,250)`.  R6 independently
reimplemented those laws and reproduced their exact rational dense maxima.
The R3 worker independently audited this report's projection orientation and
closed forms against its star tables, finding no mismatch.  In a fresh R6
audit after this report was drafted, the auditor independently rederived the
ceiling loss and cutoff gap, every Bernstein constant in (6.4), the full-walk
bridge denominator (6.6), the proposal bound (6.8), the child-domain
invariant, and the telescope (7.3), and found no counterexample.

## 11. What is resolved and what remains

**Resolved:**

- exact formal arbitrary-endpoint recursion;
- polynomial endpoint representation in the dense approximate architecture;
- positive labeled branch sampling without permutation or partition tables;
- exact star-long completion through R3;
- a uniform bridge-conditioned recursive-length survival bound;
- an explicit summable TV telescope and negligible error at `2N^3`.

**Unresolved:**

1. At fixed `N,L`, the construction has the explicit error floor (7.4).  It
   does not achieve every smaller requested `epsilon` in time polynomial in
   `log(1/epsilon)`.
2. Exact arbitrary-short branch sampling remains the positive
   stabilizer-connection primitive from R2.  The natural labeled and type-cell
   tables are superpolynomial, but this does not prove hardness.

The first standalone open lemma is therefore:

```text
Tunable positive connection lemma.
For every feasible (r,L,g) and 0<epsilon<1, sample the positive labeled
R1 branch law within epsilon in time polynomial in r,L,log(1/epsilon),
without enumerating S_(r-1) or partition-scale type cells; alternatively,
give an exact polynomial sampler for that law.
```

For the scheduled dense identity target, rank recursion should be **promoted
as a negligible-error architecture**, while exact/tunable rank recursion
should remain a strict reduction to this lemma.

role: r4-r5-closure
claim: The retained positive two-sided rank recursion samples every feasible dense top endpoint at L_N=2N^3 within total variation 3N exp(-N/12288), with polynomial endpoint state and polynomial expected Turing time; exact arbitrary-short recursion is specified but its natural h/type tables are superpolynomial.
status: proved
assumptions: The proved R1 stable-sort bijection and orientation; the proved R2 two-sided pointwise branch theorem; the proved R3 exact prescribed-star sampler (including its audited Féray enumerative input); exact fair random bits; the established Caputo--Liggett--Richthammer Theorem 1.1.
evidence: Sections 2--8; the exact bridge-conditioned tail (6.7); telescope (7.3)--(7.4); check_flat_projection.py and results.json; imported R1/R2/R3 exact artifacts.
independent_checks: R6 independently reproduced the R2 two-sided formulas and dense exact cases and, in a fresh post-draft audit, rederived the cutoff gap, Bernstein constants, bridge denominator, proposal conditioning, child invariant, and telescope without a counterexample; R3 independently checked the projection orientation and closed form; this role's exact script checked 32,224 orientation/projection/mixing/disintegration cases with zero failures.
complexity: Conservative O(N^4 L^3) exact-arithmetic operations on polynomial-bit integers, polynomial space and expected fair random bits; endpoint state O(N log N), branch inventory O(L), zero endpoint error, and TV at most 3N exp(-N/12288).
first_unproved_step: Prove the tunable positive connection lemma above; at fixed L the current negligible-error distribution cannot be driven below its explicit floor merely by increasing runtime.
verdict: promote
