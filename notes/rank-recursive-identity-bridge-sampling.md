# Rank-Recursive Sampling of Transposition Identity Bridges

Date: 2026-09-01

Status: the exact rank disintegration below was the input to the completed
September 2026 goal run.  That run produced a polynomial-time sampler for the
dense schedule `L=2N^3` with fixed negligible total-variation error
`3N exp(-N/12288)`.  See
`experiments/20260901-rank-recursive-identity-bridge-goal/coordinator_report.md`
and the streamlined manuscript proof.  Exact or arbitrarily tunable branch
sampling remains unresolved.

## 1. Target and motivation

Let `T_N` be the set of all transpositions in `S_N` and define the endpoint
fiber

```text
Omega(N,L;g) = { (t_1,...,t_L) in T_N^L : t_1 ... t_L = g }.
```

The project target is the uniform law on `Omega(N,L;e)`.  A proposed recursive
sampler starts at `S_2` and lifts from rank `N-1` to rank `N`, adding
`O(N^2)` factors at rank `N`.  Such overheads sum to `O(N^3)`.

The correct recursive interface is more general than an identity sampler:

```text
Sample(N,L,g): sample uniformly from Omega(N,L;g).
```

The public/top-level call remains `Sample(N,L,e)`.  Arbitrary endpoints arise
only in recursive subproblems.

The fiber is empty unless

```text
sign(g)=(-1)^L
```

and `L` is at least the transposition length of `g`.  Once these conditions
hold, extra pairs can pad any factorization to the requested length.

## 2. Exact rank disintegration

Embed `H=S_(N-1)` as the permutations fixing `N`.  Split the transposition
set into

```text
A_N = { (i j) : 1 <= i < j < N },
B_N = { (i N) : 1 <= i < N }.
```

In the group algebra put

```text
C_N     = sum_(t in T_N) t,
C_(N-1) = sum_(t in A_N) t,
J_N     = sum_(t in B_N) t.
```

Here `J_N` is the `N`th Jucys--Murphy element.  For `h in H`,

```text
h (i N) = (h(i) N) h.
```

Consequently `C_(N-1)` and `J_N` commute and

```text
C_N = C_(N-1) + J_N.
```

This identity has a positive, word-level interpretation.  Record the binary
pattern saying which factors of a word lie in `A_N` and which lie in `B_N`.
Repeatedly apply the displayed relation to stable-sort all old factors to the
left.  The operation preserves the old-factor order, the star-factor count,
and the total product; it only relabels star factors.  For each fixed binary
pattern this gives a bijection

```text
word w  <->  (old word u, star word v),
eval(w) = eval(u) eval(v).
```

Write `[g]X` for the coefficient of `g` in a group-algebra element `X`.
For every `g in S_N`, the resulting exact count is

```text
[g] C_N^L
 = sum_(k=0)^L binom(L,k)
     sum_(h in H)
       [h] C_(N-1)^(L-k) [h^(-1)g] J_N^k.            (2.1)
```

For identity bridges this becomes

```text
|Omega(N,L;e)|
 = sum_(k=0)^L binom(L,k)
     sum_(h in H)
       [h] C_(N-1)^(L-k) [h^(-1)] J_N^k.             (2.2)
```

Equation (2.1) yields an exact sampler if the following choices can be made
efficiently:

1. Draw `(k,h)` with probability proportional to the corresponding summand.
2. Draw `u` uniformly from `Omega(N-1,L-k;h)`.
3. Draw a uniform length-`k` star word `v` with product `h^(-1)g`.
4. Draw a uniform `k`-subset of the `L` positions and invert the stable-sort
   bijection for that binary pattern.

Every target word has a unique preimage under its pattern, so exact choices in
these four steps give the exact uniform law.  This explains why arbitrary
endpoints are needed: even when `g=e`, the lower-rank word normally ends at a
random `h`, not at `e`.

At the time this note was drafted, the disintegration was not yet an efficient
sampler: the open tasks were sampling the weighted branch `(k,h)`, sampling
arbitrary-endpoint star factorizations, and making the recursion polynomial
without enumerating `S_(N-1)` or all partitions of `N-1`.  The completed goal
run resolves those tasks for the scheduled dense approximation summarized at
the top of this note.  Exact or arbitrarily tunable branch sampling is still
open.

## 3. Assessment of paired insertion

There are `N-1`, not `N`, new transposition types `(i N)`.

Starting with a lower-rank identity word and inserting only adjacent star
pairs forces, after stable sorting,

```text
eval(u)=e and eval(v)=e.
```

Thus it samples only the `h=e` branch of (2.2).  Random simultaneous
conjugation makes the distinguished omitted label uniform, but it does not
correct the branch weights: identity remains identity after conjugation.

Hurwitz moves may erase this ancestry when the output lies in the relevant
connected Hurwitz orbit.  That turns the proposal into a structured warm
start, not a rank lift already close to uniform.  A guarantee would require a
start-specific Hurwitz mixing theorem, which may be easier than worst-case
mixing but is still unproved.

The project already found a warning against relying on a single removable
square.  At fixed rank and growing genus, the image of one designated pendant
square insertion is exponentially small in the connected identity-word
space; see
`experiments/20260811-polynomial-mixing-resolution/cycle-02/mission-M12-high-surplus/proof_final.md`,
Section 6.  This does not refute a joint dense-rank construction with many
pairs and subsequent mixing, but it rules out treating simple insertion as
automatically measure preserving.

## 4. Exact marginal constraint on a length schedule

Uniform identity words are invariant under simultaneous conjugation.  Hence
the transposition at every fixed position is exactly uniform in `T_N`.  For a
fixed label `v`, if `K_v` is the number of factors incident to `v`, then

```text
E[K_v] = L (N-1)/binom(N,2) = 2L/N.                  (4.1)
```

Suppose a lift retains exactly `L_(N-1)` old factors and adds only factors
incident to the new label.  Matching (4.1) even at the level of the mean
requires

```text
L_N - L_(N-1) = 2L_N/N,
L_(N-1) = L_N (N-2)/N.                              (4.2)
```

The solutions of (4.2) scale as `L_N proportional to N(N-1)`, not `N^3`.
For a cubic schedule, the lift must also add old-label factors, randomize the
old/star classification sufficiently, or use the full rank law (2.1).

## 5. Relation to earlier project work

The long local-mixing run established ingredients adjacent to this proposal:

- Avoiding a fixed label `v` identifies the missing-label fiber exactly with
  `Omega(N-1,m)`.  A same-product length-three square refresh can introduce
  `v`; see
  `experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M19-growing-surplus-redteam/report.md`,
  Sections 2.1 and 2.4.
- A marked adjacent square has an exact insertion/deletion incidence formula,
  but this is a same-rank, length-down/up coordinate.
- The fixed-genus pendant-square construction and the genus-one marked
  deletion investigations showed that simple deletion is not a uniformly
  available rank coordinate; see M12 above and
  `experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M97-genus-one-hurwitz-gap/report.md`,
  Section 9.
- The exact square down-up projection studied in the run changes length by two
  at fixed rank.  It is not the rank recursion (2.1).

No inspected project artifact formulated (2.1) as a recursive sampler or
resolved its branch-sampling complexity.

## 6. Closest literature

- E. Duchi, D. Poulalhon, and G. Schaeffer, *Uniform random sampling of
  simple branched coverings of the sphere by itself*, SODA 2014, give an
  exact linear-time sampler for connected minimal identity factorizations of
  length `2N-2`.  This is a special exact sampler, not a dense rank lift:
  <https://www.irif.fr/~poulalho/Articles/DuPoSc13.pdf>.
- V. Feray, B. Louf, and P. Thevenin, *Random generation and scaling limits
  of fixed genus factorizations into transpositions*, construct an
  asymptotically uniform genus-recursive sampler for factorizations of the
  long cycle.  This is a conceptual precedent for controlled insertion, but
  the endpoint and asymptotic regime differ: <https://arxiv.org/abs/2105.03284>.
- V. Feray, *Partial Jucys--Murphy elements and star factorizations*, treats
  arbitrary-length star-factorization counts and explains their class
  symmetry.  These formulas are directly relevant to the `J_N` factor in
  (2.1): <https://arxiv.org/abs/0904.4854>.

The targeted search found no general polynomial-time rank-recursive sampler
for dense uniform transposition identity bridges.  This is a search result,
not a theorem of nonexistence.

## 7. Goal-run specification and outcome

The run specified below has been completed.  Its coordinator classified the
result as `strict-reduction`: obligations R1--R5 were resolved sufficiently to
prove the fixed-negligible dense sampler, while the stronger exact or
`epsilon`-parameterized branch sampler remains a standalone open lemma.  The
text is retained as the provenance for the run rather than as a current
recommendation.

### Goal: resolve the algorithmic content of the exact rank disintegration

The next run should not return to unrestricted polynomial-mixing exploration.
Its decision question should be:

```text
Can the positive rank disintegration (2.1) be implemented as an exact or
negligible-error sampler in time polynomial in N, L, and log(1/epsilon),
at least in the dense regime L=Theta(N^3)?
```

The primary deliverable is a theorem-quality reduction identifying the first
genuinely non-polynomial primitive.  The run should attempt the stronger
sampler theorem, but it counts as substantive progress only if it resolves at
least one of the following obligations rather than merely naming it:

```text
R1  Prove and independently audit the stable-sort bijection and (2.1).
R2  Sample the weighted branch (k,h) without enumerating S_(N-1).
R3  Count and sample star words of length k with a prescribed endpoint.
R4  Show that arbitrary-endpoint recursion closes with polynomial state and
    arithmetic complexity, or isolate an explicit superpolynomial state blowup.
R5  Give a dense approximation with a uniform TV error bound that composes
    over all ranks.
R6  Quantify the bias of paired insertion, before and after a specified number
    of Hurwitz moves, against the exact rank statistics.
```

For approximate lifts `Q_r` satisfying

```text
d_TV(U_(r-1) Q_r, U_r) <= epsilon_r,
```

Markov-kernel contraction gives the exact error budget

```text
d_TV(output at rank N, U_N) <= sum_(r=3)^N epsilon_r. (7.1)
```

Thus every claimed negligible-error sampler must allocate and prove a
summable error at each rank.

### Suggested worker allocation

Use six research workers plus one coordinator for a bounded four-to-six-hour
run:

1. **Bijection and conventions:** prove R1 for arbitrary external endpoint
   `g`, including inverse construction and boundary cases.
2. **Star-factorization algorithm:** use the Jucys--Murphy/star literature to
   attack R3 with explicit arithmetic complexity.
3. **Branch-weight algorithm:** attack R2 via conjugacy classes, generating
   functions, or a positive dynamic program; reject signed character sampling
   unless positivity is restored.
4. **Recursive closure:** formulate `Count/Sample(N,L,g)` and determine whether
   endpoint state compression remains polynomial at every rank.
5. **Dense approximation:** use random-transposition and star-shuffle mixing
   estimates to attack R5 with explicit uniform errors.
6. **Exact red team:** enumerate the smallest feasible ranks and measure the
   exact `(k,h)` law, pair-lift TV distance, inverse-fiber multiplicities, and
   failures of proposed recurrences.
7. **Coordinator:** audit claims, rerun the smallest decisive checks, and
   produce one accepted reduction or algorithm rather than merging mutually
   inconsistent proposals.

### Acceptance criteria

Classify the run as successful only if it produces at least one of:

- an exact or negligible-error polynomial-time recursive sampler with a
  complete complexity and TV proof;
- a strict reduction of that sampler to a newly solved polynomial star or
  branch-sampling primitive, leaving one named standalone lemma;
- a rigorous obstruction to the paired lift or to a precisely specified
  rank-recursive architecture, together with the exact first surviving
  alternative;
- an independently audited proof that the natural endpoint-state recursion
  has a specific superpolynomial blowup, not merely an implementation
  difficulty.

Finite experiments alone, a restatement of (2.1), or another broad literature
survey do not meet the acceptance criteria.
