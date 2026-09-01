# M15 continuation checkpoint: bridge theorems and map transfer

Date: 2026-08-11  
Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`

## Frozen model and normalization

Throughout, `(pq)(x)=p(q(x))`.  Write `m=2n`, pair the letters as
`Y_j=t_{2j-1}t_{2j}`, and let `X_0=e`, `X_j=Y_1...Y_j`, `X_n=e`.  If `P_N`
is uniform on transpositions and `Q_N=P_N*P_N`, the prefix marginal is

```text
mu(x_1,...,x_{n-1}) proportional to
    product_{j=1}^n Q_N(x_{j-1}^{-1}x_j).
```

The aligned chain is the **nonlazy** average

```text
B_{N,n}=(1/(n-1)) sum_{j=1}^{n-1} H_{2j-1,4}.
```

Thus a particular interior prefix site is selected with probability exactly
`1/(n-1)`.  Its update is a one-site prefix heat bath together with exact
refresh of the two adjacent transposition-pair microfactorizations.  The
sibling M15 report proved, with no omitted action-rate normalization,

```text
gap(K_{N,2n}) >= gap(B_{N,n})/12                    (n>=3).
```

`B` is positive semidefinite because it is a convex average of heat-bath
projections; no extra half-hold is included in its definition.

## Primary-source bridge audit

### Fixed-target `H`-colouring theorems do not give uniform constants

Dyer--Goldberg--Jerrum, *Systematic scan for sampling colorings*, Ann.
Appl. Probab. 16 (2006), Theorem 28, proves
`Mix(M_Gl,epsilon)=O_H(L^5 log(epsilon^{-1}))` for the free `L`-vertex path
and a **fixed connected unweighted graph** `H`; the state space is all
`H`-colourings when `H` is nonbipartite, or one compatible class when it is
bipartite.  Their `M_Gl` chooses a site and then one of `h=|V(H)|` colours,
so every accepted elementary proposal has probability `1/(Lh)`.  In Section
8 they take `t=4h-1` or `4h` in the nonbipartite cases.  Reading the encoding
in the proof without suppressing `H` gives the valid explicit congestion
bound

```text
A <= (1/2) L^2 (L+t)^2 h^(2t+1).
```

For the support graph of `Q_N`, `h=|A_N|=N!/2`; this is not polynomial in
`N,L`.  More basically, the theorem is for an unweighted free path and a
Metropolis proposal, while the prefix bridge is `Q_N`-weighted, has both
endpoints pinned to `e`, and `B` also refreshes edge microfactorizations.
Primary source: <https://arxiv.org/pdf/math/0603323> (Section 8, Lemma 27,
Theorem 28; DOI `10.1214/105051605000000683`).

Pedersen, *On systematic scan for sampling H-colourings of the path*,
arXiv:0706.3794, Theorems 4 and 6, also fixes `H`.  With `q=|V(H)|`, it sets
`s=4q+1`, `gamma=2q^s+1`, and its random-update chain selects heat-bath
blocks of size at most `s gamma`; it is not the one-site chain `B`.  Taking
`q=N!/2` makes even the prescribed block size superpolynomial.  The target
is again uniform unweighted `H`-colourings with free endpoints.  Primary
source: <https://arxiv.org/pdf/0706.3794> (Definitions 3 and 5, Theorems 4
and 6).

### The closest weighted theorem is unusable as printed and its natural
### contraction repair is false for `Q_N`

Lyu--Memoli--Sivakoff, *Sampling random graph homomorphisms and applications
to network data analysis*, JMLR 24(9) (2023), equation (30), gives exactly
the weighted one-site conditional law needed for the **prefix marginal**.
However, equation (31) defines `c(d,G)` using a maximum over maps differing
in at most one coordinate.  Equal maps are allowed, so the displayed
quantity is always at least, and in fact at most, `1`; hence it is `1`.
The proof of Lemma B.2 needs a worst-case lower bound, says the relevant
bracket is *at most* `c`, and then uses it as a lower bound.  Equations
(156) and (162) decay as `exp(-ct/k)`, whereas Theorem 2.4, equation (32),
multiplies the mixing bound by `c` rather than dividing by it; equation
(161) also omits the leading `1` in the contraction factor.  No corrigendum
was present on the JMLR article page in the targeted search.  The theorem
therefore cannot be invoked as printed.

The obvious repair (minimum over neighboring boundary configurations and a
`1/c` dependence) still does not apply.  Let

```text
a_N(g)=#{(u,v): u,v transpositions and uv=g}.
```

Then `a_N(e)=binom(N,2)`, it is `3` on 3-cycles, `2` on double
transpositions, and zero elsewhere.  For a fixed 3-cycle `g`, compare the
conditional center laws with leaf pairs `(e,e)` and `(g,e)`; both star maps
are feasible.  Exact exhaustive arithmetic gives at `N=5`

```text
Z_(e,e)=340, Z_(g,e)=207,
TV(mu_(e,e),mu_(g,e)) = 4441/11730.
```

For degree `d=2`, the repaired margin is

```text
1-2d TV = 1-4(4441/11730) = -3017/5865 < 0.
```

Primary source: <https://jmlr.org/papers/volume24/20-449/20-449.pdf>
(equations (30)--(32), Theorem 2.4, Lemma B.2 and equations (156)--(162)).

### Standard Dobrushin and every dependency-matrix norm criterion fail

Dyer--Goldberg--Jerrum, *Dobrushin conditions and systematic scan*, CPC 17
(2008), defines the one-site influences `rho_{i,j}` and records random-update
mixing when a maximum influence sum is below one.  At `N=6`, the same
feasible boundary change has

```text
v = 1627/3060,
2v = 1627/1530 > 1.
```

Thus the usual row/column-sum hypothesis fails at an interior prefix site.
Primary author PDF:
<https://www.cs.ox.ac.uk/people/leslieann.goldberg/papers/dobrushinJournalRevision.pdf>.

The stronger audit uses Dyer--Goldberg--Jerrum, *Matrix norms and rapid
mixing for spin systems*, Ann. Appl. Probab. 19 (2009), Lemma 1: if a
dependency matrix `R` has any matrix norm at most `mu<1`, random-update
Glauber mixes in the displayed `O(L(1-mu)^(-1) log(...))` time.  Lemmas 9
and 10 give monotonicity of the Perron root and `rho(R)<=||R||` for every
matrix norm.  On a path of nine interior sites, every nearest-neighbor
entry of any dependency matrix is at least `v`: use the all-identity prefix
configuration and change the appropriate neighboring prefix to `g`, which
remains feasible because `Q_N(e),Q_N(g),Q_N(g^{-1})>0`.  Therefore

```text
rho(R) >= v rho(A(P_9)) = 2v cos(pi/10)
       > (19/10)(1627/3060) = 30913/30600 > 1.
```

Hence **no** matrix norm can satisfy the theorem's `<1` hypothesis for the
`N=6`, `n>=10` pinned bridge.  This refutes the criterion, not rapid mixing.
Primary source: <https://arxiv.org/pdf/math/0702744> (Lemmas 1, 9, 10;
DOI `10.1214/08-AAP532`).

The pivot chain in Lyu--Memoli--Sivakoff Theorem 2.5 is a genuinely global,
root-moving/redrawing chain, not `B`; Remark 2.1 gives per-step cost of order
`Delta(G)^ell Delta(F)`, potentially exponential in motif depth `ell`.
It is therefore not a bounded-cost bridge-Glauber transfer.

## Caraceni--Duchi transfer audit

Duchi--Poulalhon--Schaeffer Proposition 1 is a bijection between minimal
transitive identity factorizations of length `2N-2` and `I_N`, the set of
**simple**, face-labelled, black-vertex-indexed increasing quadrangulations
with `N` black and `N` white vertices.  Their convention is
`tau_{2N-2}...tau_1=e`; word reversal translates it to the project
convention.  Corollary 2 gives count `N^(N-3)(2N-2)!` and a uniform linear
sampler.  Primary source:
<https://www.irif.fr/~poulalho/Articles/DuPoSc13.pdf>.

Caraceni Theorem 1 concerns instead all rooted, unlabelled quadrangulations
`Q_f` with `f` faces, including double edges and degenerate faces, with
uniform stationary measure.  Its non-root flip kernel selects one of
`2f-1` nonroot edges and one of three actions, so an elementary choice has
mass `1/[3(2f-1)]`.  It proves

```text
C_1 f^(-5/4) >= gap >= C_2 f^(-11/2).
```

Proposition 4.1 intertwines that flip kernel with edge rotations **through
Tutte's bijection** `M_f <-> Q_f`, not through the Duchi bijection.  Primary
source: <https://arxiv.org/pdf/2001.04166> (equation (1), Lemma 3.1,
Proposition 4.1, Theorem 1; DOI `10.1214/20-EJP519`).

Consequently the literal transfer is false:

1. `I_N` and `Q_{2N-2}` are different state spaces and carry different
   uniform laws.  Caraceni explicitly permits multigraphs, double edges,
   degree-one vertices, and degenerate faces; Duchi requires simplicity and
   increasing face labels and vertex indices.
2. The simple/increasing subset is not closed under Caraceni flips.  Indeed,
   Caraceni's chain is irreducible on all `Q_f`, and both Duchi-type simple
   states and the paper's degenerate states exist.  A proper nonempty subset
   cannot be closed under an irreducible chain.
3. The only proved transition intertwining is Tutte Proposition 4.1.  Duchi
   encodes word position `k` by face label `k`; Caraceni's kernel has no face
   labels or increasing orientation and gives no bounded simulation of a
   consecutive `r=4` word heat bath.

Restricting Caraceni's chain by rejecting exits, lifting it with labels, and
comparing it to `B` would require new action-rate, stationary-flow, path
length, and congestion bounds.  The cited theorem supplies none.  This
rigorously rejects the direct stationary-measure-preserving intertwining; it
does not rule out a newly constructed comparison theorem.

## Exact frontier

No checked primary theorem in this targeted audit yields an
inverse-polynomial gap for `B` uniformly in `N,n`.  This is a source audit,
not a proof that no such theorem exists.  The smallest remaining statement is:

> **Aligned bridge Poincare proposition.** There are universal `c>0` and
> `C<infinity` such that, for every `N>=3` and `n>=3`, `B_{N,n}` is
> irreducible and `gap(B_{N,n}) >= c(Nn)^(-C)`.

The exact influence obstruction says that this proposition needs a method
beyond worst-case one-site contraction; it does not refute the proposition.

