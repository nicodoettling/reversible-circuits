# M34 halfway checkpoint: shell action is universal; weighted shell mass remains

## Frozen exact action theorem

Use `(pq)(x)=p(q(x))`, let `N>=6`, `m=2N-2`, `M=binom(N,2)`, and let
`F_N` be the connected full-support identity words.  Write

```text
h_j=N-cycles(t_1...t_j),   Area=sum_(j=1)^m h_j.
```

For every `w in F_N` whose height path is not the mountain
`U^(N-1)D^(N-1)`, there is an adjacent valley at factors `(a,b)` and the
right Hurwitz replacement

```text
(a,b) -> (b,bab)
```

has the same product, remains in `F_N`, and raises `Area` by exactly `2`.

### Proof

Mark a factor as a join or cut according as right multiplication raises or
lowers transposition length `N-cycles(.)`.  There are exactly `N-1` joins.
The graph of join factors is connected: inductively every permutation cycle
is contained in a component of the join graph seen so far; cut edges remain
inside such a component, while join edges merge components if needed.  Since
the full factor-support graph is connected, the final join graph is connected.
It has `N-1` edges, hence is a tree.  In particular every join edge connects
two different components of the previous join forest.

At an adjacent valley, put `x` for the prefix before `(a,b)` and `z=xa`.
The cut `a` splits one cycle of `x` into two cycles `A,B` of `z`.  The join
`b` joins two cycles `C,D` of `z`.  The unordered pairs cannot agree: if
`{C,D}={A,B}`, the endpoints of the join edge `b` already lie in the same
previous join-forest component (both lay in one cycle of `x`), contradicting
that the final join graph is a tree.

If `{A,B}` and `{C,D}` are disjoint, `a,b` are disjoint and commute; from
`x`, the first factor `b` joins two cycles, so `(b,a)=(b,bab)` is a peak.  If
the pairs share exactly one cycle, after `a` merges `A,B`, the factor `b`
still joins that merged cycle to the third cycle; again `(b,bab)` begins with
a join.  Since

```text
b(bab)=ab,
```

the block endpoint is unchanged and the sole internal height rises from
`h-1` to `h+1`.  Hurwitz replacement preserves the generated subgroup, so
the outcome stays transitive.  Finally, a nonmountain Dyck path has a `DU`
valley; a Dyck path with no valley consists of all joins followed by all cuts.

## Exact conversion to the original heat bath

Every adjacent pair is contained in a legal length-three window.  Keep the
third factor fixed and make the displayed Hurwitz replacement inside that
window (use the preceding padding factor only when the pair is final).  If
`F_3(g)` is the exact conditional fiber size of that window product, the
specified original-`K` transition has probability

```text
1/[2*3*(m-2)*F_3(g)] >= 1/[6(m-2)M^3].               (C.1)
```

This includes laziness, the uniform choice among `r=3,4,5`, the length-three
window scan, and the exact conditional heat bath.  The `r=4,5` flows remain
present and nonnegative.

For a feasible area value `q<(N-1)^2`, let

```text
A_q={w in F_N:Area(w)<=q},    L_q={w in F_N:Area(w)=q},
mu=Uniform(F_N).
```

Every `w in L_q` has the one-step crossing above.  Therefore

```text
Q_K(A_q,A_q^c)
 >=pi(F_N) mu(L_q)/[6(m-2)M^3].                       (C.2)
```

If `mu(A_q)<=1/2`, then `pi(A_q)=pi(F_N)mu(A_q)<=1/2` is the exact global
smaller side and

```text
Phi_pm^K(A_q)
 >=[mu(L_q)/mu(A_q)]/[6(m-2)M^3].                    (C.3)
```

Thus the width-12 action question from M29 is closed sharply: only the exact
top area layer is needed, and one `H_3` outcome acts from every state in it.

## Fixed-path monotonicity

Let `W_N(P)` count words in `F_N` with a specified Dyck sign path `P`.  If
`P'` is obtained from `P` by one valley-to-peak flip, the same Hurwitz map is
an injection

```text
F_N(P) -> F_N(P'),   so W_N(P)<=W_N(P').              (C.4)
```

This is useful weighted-Dyck structure but does not yet compare the union of
all ranks below a median to the single boundary rank.  A proof using only
unweighted Dyck-rank unimodality would encounter a known open problem: rank
unimodality of the Dyck lattice is itself not established in general.

## Exact falsification and calibration

1. The tempting stronger assertion that every abstract nonmaximum Cayley-rank
   valley has an upper diamond is false already in `S_4`.  For example the
   emitted exact witness has `x=(1 2 3)` with label `0` fixed,
   `a=(1 2),b=(2 3)` (zero-based labels); every two-factorization of `ab`
   stays on `{1,2,3}` and cannot join the fixed label.  Such a valley cannot
   occur as the only obstruction in `F_N`, because its second join would
   create a cycle in the join-factor graph.
2. Complete exact enumeration of all `2880` states in `F_4` and all
   `1,008,000` states in `F_5` confirms the proved adjacent-pair theorem:
   pair gain is `0` exactly on the maximum-area layer and `2` everywhere
   else.  This is calibration, not the proof.
3. At `N=5`, the unique admissible recorded threshold is `q=12`, with
   conditional lower-tail count `427440/1008000`; its exact top layer has
   count `207600`, so (C.3) is polynomial in this finite case.
4. A fixed-seed `F_6` Hurwitz search checked `100001` exact states; it found
   no nonmaximum full-window local maximum.  Nonfinding is empirical only.

## First remaining standalone proposition

> **WEIGHTED DYCK MEDIAN-SHELL MASS.**  Define
> `q_N=min{q:mu(Area<=q)>=1/4}` whenever this threshold also satisfies
> `mu(Area<=q)<=1/2`.  Prove both that such an admissible feasible threshold
> exists for every `N>=6` (or give another explicit admissible choice), and
> that there are universal `c>0,C<infinity` for which
>
> ```text
> mu(Area=q_N)/mu(Area<=q_N) >= c N^(-C).
> ```

Together with (C.3), this exactly proves the requested inverse-polynomial
conductance for the area-median cut.  Conversely, a superpolynomial failure
of this ratio is not yet Terminal B until all other width-12 crossings are
upper-bounded; (C.2) shows it cannot be argued from inactive shell states.
