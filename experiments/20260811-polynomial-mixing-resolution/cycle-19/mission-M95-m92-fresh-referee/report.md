# M95 fresh referee report on frozen M92

Date: 2026-08-12.  Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Decision, accepted claim, and exact scope

```text
ACCEPT M92's scoped reduction and obstruction package.
Material numbered objections: none.
```

The accepted positive result is a **reduction only** for one
two-component minimal exterior macro at `N>=5,m=2N-2`.  For the declared
lazy physical signed-Hurwitz walk

```text
P_Gamma=(1/2)I+[1/(4(m-1))]
                   sum_(i=1)^(m-1)(R_i+R_i^(-1)),
```

M92 correctly proves both of the following.

1. A worst-source probability of hitting M75's marked set by time `T`
   transfers to a source-independent law on fixed bijective signed words,
   endpoint marked probability at least `a/(T+1)`, expected emitted length
   `T/4`, and the stated arbitrary-subset M75 coarea inequality.
2. An inverse-polynomial gap only for connected genus-one identity words on
   `d` fixed labels at length `2d` is sufficient: the genus-zero internal
   word strongly projects out, M05's shuttle comparison survives on the
   quotient, and fixed-time mixing supplies the marked endpoint law.

The accepted negative/topological package is also correctly scoped: a
tree--cotree decomposition leaves two fundamental homology cycles; one
proposed constant metadata encoding is refuted by an exact collision; the
explicit Cayley-tree family gives `d^(d-2)` unmarked sources; exact
canonicalization to one root needs that many distinct transcripts; and a
direct routing through only polynomially many marked roots has exponential
terminal occupation under the hypotheses M92 states.

This acceptance proves no value for `gamma_1(d)`, no uniform marked hitting
bound, no unconditional arbitrary-macro cover, no unrestricted `H4/H5`
statement, no full-`K` spectral gap or mixing bound, and neither Terminal A
nor Terminal B.

## 2. Frozen provenance and package integrity

All three assigned digests independently match:

| frozen M92 artifact | required SHA-256 | observed |
|---|---|---|
| `report.md` | `21662f10c53582e6fbf2fe18cc405ba7d92497948a76e7138d5a46f5a266678f` | match |
| `oblivious_cover_reduction.md` | `6490d4cd0daae58bf0ff68cbdceedb2d432cb27d743e18f02bea05bc4dd2ffd0` | match |
| `freeze_manifest.md` | `e2e6ab274adc9d9cf20a0047196770c14b58681846738af0c919db6196547edc` | match |

Running `sha256sum -c SHA256SUMS` in the M92 directory returned `OK` for all
seven frozen payloads.  The directory contained no `__pycache__` or `.pyc`
file.  The imported reports also match the hashes frozen by M92:

```text
e699e8b54684488ae34a8df87edea5f9a88002939e34d9facc55c549b741ed39  M75 report
ad09b58a061e8b65382a3fff316e846ef291b06de761fbad79711cf9b645fd44  M77 report
d8ec2b835e5169b91977a33ac725680d206d62e9d7f6b944abbc203037d22bf4  M05 report
96c52fdc8f6a07d51869b5bf83415b001a9c7e825e22f041c69836ae3435241d  M68 report
285fca42f7f58a9f45ba63cb163f28566ccd5a30e8da1fb01679200500d90ffa  M74 report
```

No frozen M92, predecessor, coordinator, manuscript, project-skill, or
shared durable file was edited.

## 3. Target, convention, kernel, and dependency boundary

Permutations compose and Hurwitz generators act as

```text
(pq)(x)=p(q(x)),
eval(t_1,...,t_m)=t_1...t_m,
R_i(a,b)=(b,bab),
R_i^(-1)(a,b)=(aba,a).
```

The background target is uniform on

```text
Omega(N,m)={w in Trans(S_N)^m:eval(w)=id}
```

for the literal lazy exact same-product `{3,4,5}` heat-bath kernel.  The
transport walk `P_Gamma` is an auxiliary within-macro signed-Hurwitz walk,
not a global sampler.  Every emitted generator is realized by an inherited
specified padded-`H3` outcome of probability at least

```text
p_H=1/[6(m-2)M^2],       M=binom(N,2).
```

For a two-component minimal exterior macro, the genus balance forces one
component `U` to have genus one and the other `V` genus zero.  If `U` has
`d` labels, its length is `2d`.  Define `gamma_1(d)` as the Poincare gap of
the half-lazy signed-Hurwitz kernel on all connected-support length-`2d`
identity words on that fixed support, with singleton convention one.  If
that kernel is reducible, the gap is zero; hence the proposed lower bound on
`gamma_1` itself supplies the required reachability.

The positive reductions use only combinatorial macro factorization, the
accepted M68/M74 marked-incidence bound, bijective Hurwitz maps, M05's
explicit shuttles, and elementary finite-state spectral estimates.  They do
not use the still-conditional Classification-H source.  Classification H is
mentioned only when discussing whether every adaptive exact canonicalizer
transcript exists with polynomial length; M92 explicitly keeps that claim
conditional.

## 4. Random-time hitting, endpoint conversion, and M75 coarea audit

Let `X_0,...,X_T` be one trajectory and `G=G_Gamma`.  Choosing
`J` uniformly in `{0,...,T}` gives

```text
Pr_x(X_J in G)
 =[1/(T+1)]sum_(j=0)^T P_Gamma^j(x,G)
 =[1/(T+1)]E_x sum_(j=0)^T 1[X_j in G]
 >=Pr_x(tau_G<=T)/(T+1).
```

This is exactly the claimed hitting-to-endpoint inequality.  Sampling `J`
proposals directly has the same law as taking a random prefix of a common
length-`T` trajectory.  Deleting holding symbols preserves the endpoint.
Each remaining symbol is a fixed positional signed generator, so every word
and every prefix is a bijection of `Gamma`.  Since `EJ=T/2` and a proposal
is nonholding with probability `1/2`,

```text
E ell(beta)=T/4.
```

The endpoint specialization of M75 was re-derived rather than imported by
name.  Give every successful pair `(x,beta)` its word-law mass.  If its
emitted path first exits `S`, charge that actual first directed edge.  If it
does not exit, its marked endpoint lies in `S`, so charge the designated safe
terminal edge.  For a fixed word, stage, and path edge, inverse prefix
recovers at most one source.  The path load is therefore at most
`E ell=Dbar`.  For a fixed terminal edge and fixed whole word, inverse word
recovers at most one source; summing word probabilities gives load at most
one.  Thus the exact common load denominator is `max(Dbar,1)`, with no word-
support-cardinality or first-hit-time factor.

Putting `eta=a/(T+1)` and `Dbar=T/4` gives

```text
sum_(x in S)K(x,(Gamma minus S) union (F_N minus A))
 >=p_H a|S|/[(T+1)max(T/4,1)].
```

If `max_x E_x tau_G<=H`, choose `T=ceil(2H)`.  Markov gives `a>=1/2`; for
`T>=4` the right side becomes exactly

```text
2p_H|S|/[T(T+1)].
```

The fresh checker independently verified the visit-count inequality over
`Fraction` on a four-state lazy bijective-proposal walk.  This finite check
is a calibration; the displayed expectation identity is the proof.

## 5. Strong lump, product law, mark measurability, and shuttle comparison

The coordinate map is the literal bijection

```text
Gamma=I_(k_U,k_V) x X_U x X_V,
psi(sigma,u,v)=(sigma,u).
```

Every projected state has exactly `|X_V|` preimages.  Consequently uniform
measure projects to

```text
pibar=Unif(I_(k_U,k_V)) tensor Unif(X_U).
```

For an oriented physical proposal at positions `i,i+1`, its projection is
pointwise as follows.

- On `U,U`, it is the corresponding internal oriented Hurwitz generator on
  the consecutive `U` factors.
- On mixed colors, disjoint supports make both orientations the same color
  swap, with both internal subsequences unchanged.
- On `V,V`, only the omitted word may change, so the projected proposal is
  the identity.

Every displayed projected map is itself a bijection and none depends on
`v`; summing labeled proposals therefore gives a strong lump, not merely a
stationary-average projection.  A global adjacent connected-deletable `U`
square is determined by the color positions and `u`, so
`G_Gamma=psi^(-1)(Gbar_Gamma)` and marked stationary mass is preserved
exactly.

For the ideal product kernel

```text
P_*=(Q_col+P_U)/2,
```

conditional variance, `gap(Q_col)>=2/m^3`, and `0<=gamma_1(d)<=1` give

```text
gap(P_*) >=(1/2)min(2/m^3,gamma_1(d))
          >=gamma_1(d)/m^3.
```

M05's shuttle survives projection without a hidden omitted-coordinate
multiplicity.  If consecutive internal `U` occurrences are at physical
positions `a<b`, the signed sequence has length

```text
2(b-a)-1<2m.
```

It moves the first occurrence through disjoint `V` factors, applies the
desired internal orientation, and restores the color word.  For a fixed
projected directed edge and metadata `(a,b,epsilon,stage)`, every projected
prefix is bijective, so inverse prefix recovers at most one projected source.
No `V` word is being reconstructed or summed: both comparison flow and edge
capacity live on `barGamma`.  M05's deliberately loose internal congestion
`<m^6`, direct color contribution `<=1`, and total `<=2m^6` therefore apply.
Hence

```text
gap(Pbar_Gamma)
 >=gap(P_*)/(2m^6)
 >=gamma_1(d)/(2m^9)
 >=gamma_1(d)/m^10.
```

The independent checker used the smallest case with both omitted-word
variation and nontrivial genus-one dynamics: `N=6,m=10`, with `U` on three
labels at length six and `V` on three disjoint labels at length four.  It
found `|X_U|=240`, `|X_V|=24`, 210 color interleavings, 50,400 projected
states, and 1,209,600 full states.  It verified:

- all 18 labeled projected proposal maps are bijections on all 50,400 states;
- 1,814,400 physical-to-projected proposal identities using two distinct
  omitted words at every projected state;
- 50,400 exact equality checks between the two omitted-word projected rows;
- 100,800 full/projection mark-measurability checks; and
- all 504,000 internal shuttle instances over every projected state,
  internal index, and orientation.

No check failed.  The exact marked projection fraction was `41/60`, above
the inherited bound `zeta=1/180` in this macro.

## 6. Fixed-time TV, marked density, `t_Gamma`, and final normalization

The projected kernel is half-lazy, so its spectrum is nonnegative.  Fixing
one omitted `V` word injects `barGamma` into `Gamma`, hence
`|barGamma|<=M^m`.  For uniform stationary law,

```text
||Pbar_Gamma^t(z,.)-pibar||_TV
 <=(1/2)sqrt(|barGamma|)exp[-gap(Pbar_Gamma)t].
```

With

```text
zeta=3/[Nm(m-1)],
t_Gamma=ceil[(m^10/gamma_1(d))
              {(m/2)log M+log(1/zeta)}],
```

the weakened gap `gamma_1/m^10` makes the exponential at most
`M^(-m/2)zeta`; the displayed TV distance is therefore at most `zeta/2`.
The mark has projected stationary mass at least `zeta`, so every source has
fixed-time marked endpoint probability at least `zeta/2`.  Exactly
`t_Gamma` physical proposals emit expected signed length `t_Gamma/2`.

Applying the endpoint M75 denominator gives

```text
p_H (zeta/2)/(t_Gamma/2)
 =p_H zeta/t_Gamma
 =1/[2Nm(m-1)(m-2)M^2 t_Gamma],
```

which is M92's equation (2.14), including the factor two.  The checker
verified this equality over exact rationals at `N=6,m=10`.

The inherited marked density itself is unconditional on Classification H.
M68/M74 count deletable-square insertions in a uniform connected genus-one
word, apply their audited positive DYZ adjacent-genus recurrence, and then
interleave colors.  They obtain

```text
E_Gamma Z>=6(d-1)/(d^2m),
Z<=m-1,
(d-1)/d^2>=1/(2N),
```

and hence `Pr_Gamma(Z>=1)>=3/[Nm(m-1)]`.  This is a whole-macro average,
exactly what fixed-time projected mixing needs; M92 does not promote it to a
pointwise statement.

Polynomiality remains conditional on

```text
gamma_1(d)>=c d^(-C).
```

If `gamma_1(d)=0`, `t_Gamma` is not finite and the conditional route says
nothing.  This is the intended reduction boundary, not an implicit use of
transitivity.

## 7. Tree--cotree topology, unmarked family, transcripts, and root load

For a connected genus-one identity word on `d` labels with `2d` occurrences,
the chronological capped ribbon surface has

```text
V=d, E=2d, F=d,
```

and is a cellular torus.  For any primal spanning tree `T`, the dual edges
complementary to `T` are connected: a nontrivial dual component cut would
give a nonempty even primal subgraph supported inside a tree, impossible.
Choose a complementary dual spanning tree `T*`.  The number of leftover
occurrences is

```text
2d-(d-1)-(d-1)=2.
```

Contracting `T` and merging faces along `T*` leaves a one-vertex,
one-face, two-loop torus cellulation.  Since `H_1(T^2;Z)=Z^2`, the lone
two-cell has zero abelianized attaching boundary and the loop classes form an
integral basis.  Pullback gives the two leftover edges closed by their unique
tree paths.  Their nonzero primitive homology classes make the embedded
fundamental cycles nonseparating.  As M92 stresses, this does not construct
an equal pair or a braid surgery.

The two frozen `S_4`, length-eight witnesses were recomputed independently.
Both evaluate to identity, are connected, have four chronological faces,
and have

```text
tree positions       (0,3,5)
cotree positions     (1,4,6)
leftover positions   (2,7)
leftover labels      (01),(13).
```

The fundamental path for leftover `(13)` is `(0,3,5)` in the first witness
and `(0,5)` in the second.  This exactly refutes the claimed sufficiency of
those positions and leftover labels, and nothing broader.

For every labeled tree `T` on `[d]`, `d>=3`, choose two incident edges
`a_T,b_T` and set

```text
u_T=(a_Tb_T)^3 product_(e in T minus {a_T,b_T}) e^2.
```

Two incident transpositions have a three-cycle product, so the alternating
prefix is identity.  The word has length `2d`, identity product, and support
exactly `T`.  It has no equal adjacent pair in the prefix; every tail square
is the sole pair of occurrences of a tree bridge, so deleting it disconnects
the support.  Appending a square on two new labels places all words in the
same labeled weighted-component macro.  Pruefer's bijection gives exactly
`d^(d-2)` distinct unmarked sources.  The fresh checker exhausted all
`3,16,125,1296` labeled trees for `d=3,4,5,6` with no failure; the displayed
algebra and bridge argument are the all-`d` proof.

The transcript claim is a direct injectivity lemma.  If fixed signed words
`beta_x` satisfy `beta_x x=c` and two induce the same bijection, that
bijection sends two sources to `c`, impossible.  Therefore exact collapse to
one canonical root needs at least `d^(d-2)` distinct word maps whenever such
routes are supplied.  Uniform replay of the one exact-root word stored for
each source hits that exact root from `x` only for its matching index, with
probability `d^(-(d-2))`; M92 correctly warns that a wrong word may hit some
other marked state.

Finally, a routing that sends success mass at least `eta` from every source
to `q` marked roots and uses at most `b` terminal edges per root has total
terminal demand at least `eta|Gamma|`.  Pigeonhole gives one actual terminal
edge load at least

```text
eta|Gamma|/(bq).
```

Since `|Gamma_d|>=d^(d-2)`, inverse-polynomial `eta` and polynomial `b,q`
give superpolynomial occupation.  This rules out only direct few-root
schemes meeting those hypotheses.  It does not rule out exponentially
distributed marked roots, a reversible random walk, or a fixed word whose
target varies injectively with the source.  The uniform global-tree
guess-and-abort law has the separately valid upper bound `d^(-(d-2))` on
source `u_T`, because its support contains exactly one spanning tree and a
wrong guess does nothing.

## 8. Fresh artifacts, reproduction, strongest self-attack, and hygiene

`independent_audit.py` was written from scratch with only the Python standard
library and imports no M92 or predecessor implementation.  Its principal
command from the repository root was

```text
python3 -B \
  experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M95-m92-fresh-referee/independent_audit.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M95-m92-fresh-referee/independent-results.json
```

It is deterministic (`seed=null`), ran under Python `3.12.3`, and used no
nonstandard dependency.  A separate rerun of M92's frozen checker to `/tmp`
reproduced its `S_4` witness after 1,589 candidate words and all stated
Cayley-tree checks through `d=6` (plus its path family through `d=12`).

The strongest substantive self-attack remains the unresolved one: a
genus-one Hurwitz gap can be zero or superpolynomially small, and a marked
hitting bound can fail even though all finite projection identities are
correct.  The reduction offers no estimate for either.  Likewise, the
topological basis contains no literal equal pair, and the root-load lemma
does not constrain a law with exponentially diffuse endpoints.  These are
the exact limitations M92 records, so they are not objections to its stated
claims.

Boundary scope is explicit.  Odd `m`, `m=0`, `m=2`, `N=2`, and nonminimal
or more-than-two-component exteriors are outside the positive theorem.  The
unmarked family starts at `d=3`, hence `N=5,m=8`.  The genus-one coordinate
can start at `d=2` under the singleton-gap convention.  Finite checks can
falsify formulas but do not establish any asymptotic rate.

Owned artifacts are `plan.md`, `checkpoint.md`, `independent_audit.py`,
`independent-results.json`, this report, the freeze manifest, and the final
`SHA256SUMS`.  Bytecode was disabled and generated cache is removed before
freeze.

## 9. Final verdict and first unproved obligation

**ACCEPT, with zero material numbered objections.**

M92 validly narrows the two-component exterior cover problem to a
distributed-root statement.  The narrowest open positive obligation is

```text
max_(x in Gamma) E_x tau_(G_Gamma) <= poly(N,m)
```

for the declared physical signed-Hurwitz walk.  The stronger but still
narrower-than-all-genera route is

```text
gamma_1(d)>=c d^(-C).
```

Both remain **unresolved**.  So do a distributed-root reversible surgery,
an unconditional arbitrary-macro cover/direct partial-macro flow,
unrestricted `H4/H5` behavior, the full lazy `{3,4,5}` heat-bath gap and
mixing time, and Terminal A/B.  The accepted deliverable is therefore a
strict reduction plus exact scoped obstructions, not a terminal result.
