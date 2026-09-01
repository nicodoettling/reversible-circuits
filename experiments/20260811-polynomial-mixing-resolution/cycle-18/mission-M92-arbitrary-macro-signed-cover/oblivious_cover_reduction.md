# Oblivious signed cover: exact reductions and arborescence obstructions

All universal statements below are **proved** unless explicitly labeled
conditional or unresolved.  Permutations compose as `(pq)(x)=p(q(x))`, tuple
factors multiply left-to-right, and

```text
R_i(a,b)=(b,bab),             R_i^(-1)(a,b)=(aba,a).
```

Fix `N>=5`, `m=2N-2`, `M=binom(N,2)`, a two-component minimal exterior
Hurwitz macro `Gamma`, and M75's literal marked set `G_Gamma`: a globally
adjacent square in the genus-one component whose deletion leaves that
component connected.  The background target is uniform on `Omega(N,m)` for
the literal lazy `{3,4,5}` heat-bath chain `K`.  Every transport word in this
note uses only signed Hurwitz generators, realized as specified padded `H3`
outcomes; `H4/H5` are not used.

## 1. A marked-hitting theorem strictly weaker than a Hurwitz gap

Declare the lazy physical signed-Hurwitz walk on `Gamma`:

```text
P_Gamma=(1/2)I+[1/(4(m-1))]
                   sum_(i=1)^(m-1)(R_i+R_i^(-1)).       (1.1)
```

The uniform law `pi_Gamma` is reversible for (1.1).  No transitivity input is
needed below: hypothesis (1.2) itself supplies the required worst-source
reachability.  Let `tau_G=inf{j>=0:X_j in G_Gamma}`.

**Theorem 1.1 (random-time hitting-to-cover transfer).**  Suppose that, for
some integer `T>=1` and `a>0`,

```text
inf_(x in Gamma) Pr_x(tau_G<=T)>=a.                    (1.2)
```

There is a state-independent law `mu_T` on fixed positional signed-Hurwitz
words with

```text
inf_x Pr_(beta~mu_T)(beta x in G_Gamma)>=a/(T+1),
E_mu ell(beta)=T/4.                                   (1.3)
```

It is sampled by choosing `J` uniformly from `{0,...,T}`, taking `J`
independent steps of (1.1), and deleting only the holding symbols.  Sampling
and emitting the word takes `O(T)` time.

**Proof.**  Every nonholding symbol is one fixed bijective generator, so the
concatenation is a state-independent bijective word.  Conditional on `J=j`,
its endpoint law is `P_Gamma^j`.  Therefore

```text
Pr(beta x in G_Gamma)
 = [1/(T+1)] sum_(j=0)^T P_Gamma^j(x,G_Gamma)
 >=Pr_x(tau_G<=T)/(T+1),                              (1.4)
```

because a trajectory which hits by time `T` contributes at least one visit
to the sum of visit indicators.  Since `E J=T/2` and a proposal is
nonholding with probability `1/2`, `E ell=T/4`.  QED.

M75/M77's endpoint first-crossing theorem now gives, for every
`S subseteq Gamma`,

```text
sum_(x in S)K(x,(Gamma minus S) union (F_N minus A))
 >= p_H a |S|/[(T+1)max(T/4,1)],                     (1.5)
p_H=1/[6(m-2)M^2].
```

Every used path edge and designated terminal refresh has `K`-probability at
least `p_H`; fixed word, time, and actual directed edge recover at most one
source by inverse prefix.  Thus (1.5) is actual-edge occupation, not a count
of path labels.  For `S=E_k intersect Gamma`, its targets are outside the
accepted exterior cut `C_k`.

A particularly narrow sufficient proposition is therefore

> **UNIFORM MARKED HITTING TIME (unresolved).**  There is a polynomial
> `H(N,m)` such that every two-component minimal exterior macro satisfies
> `max_x E_x tau_(G_Gamma)<=H(N,m)` for (1.1).

Indeed, take `T=ceil(2H)`.  Markov's inequality gives `a>=1/2`, and for
`T>=4`, (1.5) becomes

```text
sum_(x in S)K(x,(Gamma minus S) union (F_N minus A))
 >=2p_H |S|/[T(T+1)].                                (1.6)
```

This marked-set-specific hitting statement is weaker than a Poincare bound
for every mode of every connected Hurwitz orbit.

## 2. Only the genus-one connected-Hurwitz gap is needed

The accepted DYZ/M68/M74 incidence bound gives

```text
pi_Gamma(G_Gamma)>=zeta,
zeta=3/[Nm(m-1)].                                    (2.1)
```

Write the unique genus-one component as `U`.  If it has `d` labels, it has
exactly `2d` factors.  Let

```text
gamma_1(d)=gap(P_H^(d,2d))                           (2.2)
```

for the half-lazy signed-Hurwitz walk on connected identity words on its
fixed labeled support (singleton gap convention one).

Use the accepted component-factorization bijection

```text
Gamma = I_(k_U,k_V) x X_U x X_V,                    (2.2a)
```

where `I_(k_U,k_V)` is the binary color-interleaving fiber and `X_U,X_V`
are the internal connected identity-word fibers.  Uniform measure is the
product of the three uniform laws.  Let

```text
psi(sigma,u,v)=(sigma,u),    barGamma=I_(k_U,k_V) x X_U.
```

Every projection fiber has the same multiplicity `|X_V|`; in particular
`pibar_Gamma=Unif(I_(k_U,k_V)) tensor Unif(X_U)`.

Here is the pointwise strong-lump check.  For `z=(sigma,u)`, fix any
`v in X_V`, put `x=(sigma,u,v)`, and let
`r_i=|{j<=i:sigma_j=U}|`.  For each orientation `epsilon in {+,-}` define

```text
barR_(i,epsilon)(sigma,u)=
  (sigma,R_(r_i)^epsilon u),  if sigma_i=sigma_(i+1)=U;
  (S_i sigma,u),              if sigma_i != sigma_(i+1);
  (sigma,u),                  if sigma_i=sigma_(i+1)=V. (2.2b)
```

The mixed case uses disjoint support, so both Hurwitz orientations are the
same color swap.  The `V,V` move may change `v`, but is a projected
self-loop.  Therefore, for every `z' in barGamma`,

```text
sum_(y:psi(y)=z') P_Gamma(x,y)
 = (1/2)1_{z'=z}
   +[1/(4(m-1))]sum_(i,epsilon)
       1_{z'=barR_(i,epsilon)z},                     (2.2c)
```

which is independent of the omitted word `v`.  This defines the projected
kernel `Pbar_Gamma` pointwise.  Moreover there is a set
`Gbar_Gamma subseteq barGamma` with

```text
G_Gamma=psi^(-1)(Gbar_Gamma),
pibar_Gamma(Gbar_Gamma)=pi_Gamma(G_Gamma)>=zeta,      (2.2d)
```

because global adjacency and connected deletion of a `U` square are
determined by `(sigma,u)`, and the omitted-fiber multiplicity is constant.

Compare the projected chain with the equal mixture of the half-lazy adjacent
color-interchange chain and the internal `U` chain.  Conditional variance
and the accepted color gap `gamma_col>=2/m^3` give the ideal gap

```text
gap(P_*) >=(1/2)min(gamma_col,gamma_1(d))
          >=gamma_1(d)/m^3.                           (2.3)
```

If `V` is absent as a positive-weight coordinate, the color space is a
singleton and its gap is set to one.  The exact imported comparison is M05
Sections 2.3--2.5: its equation (2.8) shuttles two consecutive `U`
occurrences at physical positions `a<b` by a fixed signed word of length
`2(b-a)-1<2m`; equations (2.12)--(2.14) recover the projected source from
`(a,b,epsilon,stage)` and give internal congestion `<m^6`; equations
(2.15)--(2.16) route color swaps directly and give total congestion
`A<=m^6+1<=2m^6`.  Those paths use only `(sigma,u)`, so this proof applies
verbatim to `Pbar_Gamma`.  Hence

```text
gap(Pbar_Gamma)>=gamma_1(d)/(2m^9)
                >=gamma_1(d)/m^10.                    (2.4)
```

Crucially, no gap of the genus-zero component is used.  Set

```text
t_Gamma=ceil[(m^10/gamma_1(d))
              { (m/2)log M+log(1/zeta) }].            (2.5)
```

**Theorem 2.1 (conditional only through `gamma_1(d)`).**  Sample exactly
`t_Gamma` independent proposals of (1.1) and delete holding symbols.  This is
a state-independent law on bijective signed words with expected length
`t_Gamma/2`, and every source has marked endpoint probability at least
`zeta/2`.  Consequently every `S subseteq Gamma` satisfies

```text
sum_(x in S)K(x,(Gamma minus S) union (F_N minus A))
 >= |S|/[2Nm(m-1)(m-2)M^2 t_Gamma].                  (2.6)
```

**Proof.**  The projected walk is half-lazy, so its spectrum is nonnegative.
Its state space injects into `Gamma` by fixing one omitted `V` word, and
therefore has size at most `M^m`.  For its uniform law `pibar_Gamma`,

```text
||Pbar_Gamma^t(z,.)-pibar_Gamma||_TV
 <=(1/2)sqrt(|barGamma|)exp[-gap(Pbar_Gamma)t].        (2.7)
```

Equations (2.4)--(2.5) make (2.7) at most `zeta/2`.  The mark has stationary
mass (2.1), because it is projection-measurable and all projection fibers
have the same number of omitted `V` words.  Thus the full sampled generator
word has marked endpoint probability at least `zeta/2` from every source.
Apply M75's
endpoint theorem with `Dbar=t_Gamma/2` and simplify using `p_H`.  QED.

Thus it is enough to prove the strictly narrower
**GENUS-ONE CONNECTED HURWITZ GAP** proposition

```text
gamma_1(d)>=c d^(-C)   for every d>=2.                (2.8)
```

It would make (2.5) polynomial and prove the arbitrary two-component signed
cover.  Theorem 2.1 does not prove (2.8), and it is not a new gap theorem.
The older uniform connected-Hurwitz gap for every genus and length implies
(2.8), but is unnecessarily strong here.  Conversely, the marked-hitting
proposition of Section 1 could hold even if an unrelated genus-one mode makes
(2.8) false.

## 3. Elementary torus tree--cotree certificate

Let `w` be the genus-one component word, on `d` labels and with `2d`
factors.  Its chronological ribbon surface has

```text
V=d, E=2d, F=d,
```

so it is a cellular torus.  Choose any primal spanning tree `T`.  The dual
edges whose primal occurrences are outside `T` form a connected dual graph:
otherwise the cellular boundary of a nonempty face set would be a nonempty
even subgraph contained in the tree `T`, which is impossible.  Choose a dual
spanning tree `T*` there.  Exactly

```text
E-|T|-|T*|=2d-(d-1)-(d-1)=2                         (3.1)
```

edge occurrences remain.  Contract `T` and merge faces along `T*`.  The
result is a one-vertex, one-face torus cellulation with two loop edges.  Its
single attaching word has zero exponent sum in each loop, so the two loops
form an integral basis of `H_1(T^2;Z)`.  Pulling back says that the two
leftover edges closed along their unique `T`-paths give a nonseparating
homology basis.

This is a topological certificate, not yet a marked-square certificate.
Turning one fundamental cycle into the annular core of an adjacent equal
pair requires literal braid surgery along its full tree path.

The exact owned `S_4`, length-eight audit refutes the first constant-metadata
shortcut.  It finds two chronological tori with identical ascending-Kruskal
tree positions `(0,3,5)`, cotree positions `(1,4,6)`, leftover positions
`(2,7)`, and leftover labels `(01),(13)`, but the `T`-path closing `(13)` is
respectively `(0,3,5)` and `(0,5)`.  Hence even those position sets and
leftover labels do not determine the proposed path surgery.  This finite
collision refutes only that metadata claim; it does not prove that no fixed
braid can work on both words.

## 4. Exponentially many unmarked tree sources

For every labeled tree `T` on `[d]`, `d>=3`, choose deterministically two
incident edges `a_T,b_T`.  List the other tree edges lexicographically and
put

```text
u_T=(a_T b_T)^3 product_(e in T minus {a_T,b_T}) e^2.   (4.1)
```

The two incident transpositions have a three-cycle product, so
`(a_Tb_T)^3=id`; all remaining factors are squares.  Thus `u_T` is an
identity word of length `6+2(d-3)=2d`, with connected support exactly `T`
and genus one.  It is unmarked.  The alternating prefix has no adjacent
square.  Every adjacent tail square is the only occurrence pair of one tree
edge, and deleting it disconnects `T`.

Append a disjoint square on two new labels.  The resulting words all lie in
one two-component minimal exterior macro

```text
Gamma_d: N=d+2, m=2d+2=2N-2,
          component weights (2d,2).                  (4.2)
```

Distinct trees give distinct supports.  The elementary Pruefer bijection
therefore gives an unmarked subset `U_d subset Gamma_d` of size

```text
|U_d|=d^(d-2).                                      (4.3)
```

The owned script exhausts all `3,16,125,1296` trees through `d=6`; these are
falsification checks.  The all-`d` proof is the algebra and bridge argument
above, together with the Pruefer bijection.

## 5. Canonical transcripts and root compression

**Lemma 5.1 (canonical transcript entropy).**  Let `X` be a subset of one
Hurwitz macro and `c` one fixed state.  If a signed word `beta_x` is chosen
for every `x in X` with `beta_x x=c`, then all induced bijections `beta_x`
are distinct.  In particular there are at least `|X|` positional
transcripts.

**Proof.**  If the same bijection sent `x` and `y` to `c`, injectivity would
give `x=y`.  QED.

Applied to (4.3), any adaptive normalizer to one fixed labeled canonical
marked word has at least `d^(d-2)` branches.  This rigorously rules out
representing that exact canonicalizer by polynomially many fixed
transcripts.  The separate claim that such routes always exist with
polynomial length is conditional on the project's still-unverified
Classification-H/transitivity dependency and is not used here.  The entropy
lemma does not rule out polynomially many fixed words whose endpoints vary
injectively with the source, as in M86.

Uniformly replaying one stored exact-canonical transcript per source has
exact canonical-root hit probability `1/|U_d|` from every `x in U_d`: for a
stored `beta_y`, `beta_yx=c=beta_yy` holds exactly when `x=y`.  Other
transcripts could land in other members of `G_Gamma`; this calculation
refutes canonical-root replay, not every marked-set law.

There is also a direct occupation obstruction.  Suppose a routing scheme
sends successful demand from every source of `Gamma` through within-macro
paths to a set of `q` marked roots, then through at most `b` designated
terminal edges per root.  For `S=Gamma` there is no earlier within-macro
exit.  If success mass is at least `eta` per source, the terminal edges carry
total demand at least `eta|Gamma|`; some actual directed terminal edge has
load at least

```text
eta|Gamma|/(bq).                                    (5.1)
```

If one terminal edge is designated per marked root then `b=1`; even allowing
every marked position and every cross-square choice gives the crude polynomial
bound `b<=(m-1)M`.  Thus polynomial actual-edge occupation on `Gamma_d`
requires exponentially many actual roots whenever `eta` is inverse-
polynomial.  A fixed-root or polynomial-root random spanning arborescence is
therefore not a valid direct-coarea proof.  Its map also coalesces many
sources and is not a bijection, so inverse-prefix recovery does not apply.

Finally consider the natural **uniform global-tree guess-and-abort law**:
sample one of the `d^(d-2)` labeled trees independently of the source, run a
tree-supported normalizer only if the guessed tree is contained in the
source support, and otherwise do nothing.  On the unmarked source `u_T`, the
support has the unique spanning tree `T`; every wrong guess leaves the source
unmarked.  Its marked-hit probability is at most

```text
d^(-(d-2)),                                         (5.2)
```

which is superpolynomial.  Sampling a spanning tree conditional on the
source repairs (5.2) only by making the law source-dependent; the resulting
adaptive map is not automatically bijective.  Equations (5.1)--(5.2) do not
rule out a reversible arborescence with roots distributed over exponentially
many marked states.  Constructing and analyzing such a distributed-root law
is precisely the marked-hitting/flow problem isolated in Sections 1--2.

## 6. Exact remaining frontier

The arbitrary-macro exterior obligation is reduced to either of two genuinely
distributed statements:

1. prove the uniform marked hitting-time bound for the declared physical
   Hurwitz walk (1.1), which is weaker than a full connected-Hurwitz gap; or
2. construct another state-independent law of fixed bijective local words
   whose successful endpoints occupy exponentially many actual marked roots
   with polynomial inverse-prefix edge load.

The unresolved genus-one connected-Hurwitz gap (2.8) would prove item 1
through Theorem 2.1; the universal all-genus proposition is not needed.  No
`H4/H5` distance, full-`K` gap, full exterior theorem, or Terminal claim
follows here.
