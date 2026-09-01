# M75 checkpoint: randomized first-crossing removes support size, but radius one fails

## 1. Convention and scope

Permutations compose as `(pq)(x)=p(q(x))`, words evaluate as
`t_1...t_m`, and at minimal ambient length

```text
N>=5,  m=2N-2,  M=binom(N,2),
K=(1/2)I+(1/6) sum_(r=3)^5
       (1/(m-r+1)) sum_i H_(i,r).
```

The target is uniform on `Omega(N,m)`.  This checkpoint concerns the M68/M74
one-radius partial-macrofiber obligation.  It proves a stronger randomized
version of M68's fixed-word implication, verifies that M60 null-pushing
generalizes exactly once a connected deletion certificate is chosen, and
refutes the first universal shallow certificate cover at
`N=6,m=10`.  It proves neither a full exterior-cut bound nor a literal-chain
bottleneck.

## 2. Randomized bijective marked-cover lemma

Let `Gamma` be a finite Hurwitz macrofiber, `G subseteq Gamma` a marked
set, and `mu` a state-independent probability law on finite words in the
signed adjacent Hurwitz generators.  Every word and every prefix acts
bijectively on `Gamma`.  Suppose

```text
inf_(x in Gamma) Pr_(beta~mu)[some prefix of beta sends x into G] >= eta>0,
E_mu length(beta) <= Dbar.
```

Suppose also that for every `g in G` there is a designated literal terminal
edge from `g` out of the target cut, and put

```text
p=min{
  inf literal K probability of a used padded-Hurwitz edge,
  inf literal K probability of a designated terminal edge
}.
```

Then every subset `S subseteq Gamma` satisfies

```text
sum_(x in S) K(x,cut complement)
 >= p eta |S|/(Dbar+1).                              (2.1)
```

Proof: for each successful pair `(x,beta)`, weighted by `mu(beta)`, stop
at its first visit to `G`.  Charge its first earlier path edge out of `S`;
if no prefix exits, charge the designated terminal edge from that first
marked state.  Total routed demand is at least `eta|S|`.  For
a fixed word and prefix time, bijectivity recovers at most one source from a
directed edge.  Hence one path edge receives load at most
`sum_beta mu(beta)length(beta)=Dbar`.  A terminal edge receives load at
most `sum_beta mu(beta)(length(beta)+1)=Dbar+1`, because word and
first-hit time recover the source.  Comparing these loads with `K(e)>=p`
and summing proves (2.1).

The key improvement over the finite M68 theorem is that the cardinality of
the word support does not appear.  A law may have factorial or infinite
countable support; only its worst-source hitting probability and expected
length matter.

For a two-component exterior macro, M74's corrected join-tree argument gives
the terminal edges into `F_N minus A`.  Every padded Hurwitz edge has

```text
p_H>=1/[6(m-2)M^2],
```

and a specified safe square refresh has at least this probability.  Thus a
law with `eta^-1,Dbar` polynomial proves polynomial one-radius boundary for
every partial subset of that two-component macro.

## 3. Exact M60 null-pushing generalization after a certificate

Write a connected positive-genus component occurrence as

```text
w=P x U y S
```

and suppose deleting `x,y` leaves a connected identity word
`z=P U S`.  Product preservation is equivalent to

```text
x=U y U^(-1).
```

Right-bubble `x` through `U`.  The endpoint is

```text
P U y y S,
```

so the two selected factors become an adjacent connected-deletable square.
The generator word depends only on their two positions and has length at most
`m-2`.  Refresh the square to a fixed internal edge and push it through
`S` using exact same-product triples
`f f c -> c f f`; this reaches the cell hub `z f f` in total length at
most `m-1`.  Every step is a specified positive literal `H3` outcome.

For fixed `z`, two positions, and later transposition `y`, the earlier
`x` is forced by the displayed conjugacy identity.  Therefore the direct
certificate cell over `z` has at most

```text
binom(m,2) M
```

sources.  Equivalently, the `binom(m,2)` position-indexed bubbles are fixed
bijective words, so directed edge plus word index and prefix time recovers
the source exactly.  Thus:

- **certificate chosen:** M60-style word-family size, path length, and
  actual-edge recovery are polynomial;
- **certificate absent:** the construction is undefined;
- **state-dependent Classification-H path to a certificate:** polynomial
  length is inherited, but its aggregate actual-edge load is not bounded.

This cleanly locates the failure before the null-pushing stage.

## 4. Exact failure of radius-one certificate domination

On the five labels `0,...,4`, order transpositions lexicographically and
consider

```text
(01),(02),(03),(24),(02),(14),(24),(34),(02),(24).   (4.1)
```

It is a connected identity word of length ten and genus one.  Embed it in
the minimal ambient instance `N=6,m=10=2N-2` by making label 5 isolated.
The ambient word is therefore in a two-component exterior macro.

Exact verification gives:

- among all 45 position pairs, exactly two deletions preserve identity,
  positions `(0,5)` and `(2,7)`, and both remaining supports are
  disconnected;
- none of the 18 signed adjacent Hurwitz generators produces a word with a
  connected identity-preserving two-deletion pair;
- there are 15 distinct one-generator targets;
- 104 signed two-generator paths do reach such a certificate; hence the
  exact Hurwitz distance of (4.1) to the direct-certificate set is two.

Consequently the explicit family

```text
{one optional signed Hurwitz generator}
 followed by {one position-indexed direct bubble}
```

is rigorously refuted as a universal cover.  The obstruction is
nonexistence/reachability of the certificate at radius one, not exponential
family size or an actual-edge collision after a certificate exists.

At `N=5,m=8`, by contrast, all 240 frozen M68 direct-certificate failures
acquire one after every one of the 14 signed adjacent generators.  That
finite miracle is therefore nonuniversal.

## 5. The M68 disjoint `w_q` family is a positive calibration here

For

```text
w_q=R_q R_q R_(q-1) R_(q-1),
R_a=e_1...e_a,
```

each positive-genus two-label component `e_i`, `i<q`, contains four
copies of `e_i`.  Deleting any two copies leaves the connected identity
component `e_i^2`.  Hence `w_q` already has a direct certificate even
though M68 proves literal `K`-distance
`Omega(q)` to an *adjacent* square.  A fixed position-indexed bubble exposes
the selected pair in `O(q)=O(m)` Hurwitz moves with polynomial family and
exact recovery.

Thus `w_q` rules out constant literal radius but does not obstruct the
direct-certificate/null-pushing route; it calibrates why polynomial word
length, rather than constant radius, is the right target.

## 6. Surviving explicit law and next step

For `pi in S_m`, let `beta_pi` be its canonical positive permutation
braid.  Uniform `pi` is state independent and has

```text
E length(beta_pi)=m(m-1)/4.
```

Although its support has size `m!`, Section 2 incurs no support-size loss.
The exact remaining two-component statement is:

> **POSITIVE-PERMUTATION-BRAID MARK DOMINATION.**  Uniformly over every
> positive-genus connected identity word at minimal ambient length, some
> prefix of a uniform positive permutation braid reaches an adjacent square
> whose deletion leaves that component connected with inverse-polynomial
> probability.

Whole-macro averaging proves only that the source-average hit probability is
the M68 marked density, at least `3/[Nm(m-1)]`, because every braid is a
bijection.  Arbitrary partial subsets require a worst-source or subset-average
lower bound; the average alone is insufficient.

Exact finite tests give minimum marked probabilities `608/720` over all
240 connected genus-one `S_3` length-six words and at least
`25768/40320` on all 20 displayed frozen `N=5` hard witnesses.  These
are calibrations only.

The exact double count is useful but stops one line short.  Form the
bipartite multigraph with one edge `x -> beta_pi x` for every source and
simple positive braid.  Every row has degree `m!`.  Because each
`beta_pi` is a bijection, every column also has degree exactly `m!`,
including parallel-edge/stabilizer multiplicity.  Hence

```text
sum_x #{pi:beta_pi x in G}=m!|G|.                   (6.1)
```

This recovers the whole-orbit average marked density exactly.  It does not
bound the minimum row sum.  At `S_3,k=6`, columns all have degree 720 but
row marked counts take nine values from 608 through 720; a row has only
15--119 distinct outputs and maximal parallel multiplicity 12,16,24, or 48.
Thus stabilizer collisions do not spoil (6.1), but double regularity does not
flatten source hit probabilities.

Garside complementation also does not close the gap algebraically.  For a
simple braid `beta`, take its left complement `beta^L`, satisfying
`beta^L beta=Delta`.  Therefore `beta x in G` is equivalent to
`Delta x in beta^L G`, which moves the marked set with the complement.
The connected-deletion marked set is not known to be invariant under all
simple braids (indeed the colors-only audit shows deletability is not
preserved by arbitrary Hurwitz transport).  So complementation permutes the
same total incidence but supplies no row-to-column identification for the
fixed `G`.

For three or more support components, even this domination lemma leaves a
second, separate issue: a successful marked refresh merges two components
but may remain inside the exterior ball.  Repeating to two components must
control accumulated demand additively; multiplying a conditional success
loss through up to `N` levels is not allowed.

Checkpoint verdict:

**OPEN AT TWO SHARPER NAMED STEPS: POSITIVE-PERMUTATION-BRAID MARK
DOMINATION (TWO COMPONENTS) AND ADDITIVE MERGER OCCUPATION (THREE OR MORE
COMPONENTS).**
