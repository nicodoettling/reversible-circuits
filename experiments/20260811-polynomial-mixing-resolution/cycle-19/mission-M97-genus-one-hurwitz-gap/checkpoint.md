# M97 halfway checkpoint: the exact tree--unicycle--tree handle cut

Date: 2026-08-12.  Status: genuine decomposition proved; gap and marked
hitting remain open.

## 1. Frozen state law and kernel

On fixed labels `[d]`, let

```text
X_d={w=(t_1,...,t_(2d)): eval(w)=id, support(w) connected}.
```

The target is `pi_d=Unif(X_d)`.  Permutations compose as
`(pq)(x)=p(q(x))`, tuple factors multiply left-to-right, and the exact
auxiliary kernel is

```text
P_d=(1/2)I+[1/(4(2d-1))]
             sum_(i=1)^(2d-1)(R_i+R_i^(-1)),
R_i(a,b)=(b,bab),       R_i^(-1)(a,b)=(aba,a).
```

It is symmetric, hence reversible for `pi_d`.  The desired proposition is
`gap(P_d)>=c d^(-C)`.  If `P_d` is reducible its gap is zero, so a positive
bound itself supplies irreducibility; no Classification-H source is used in
the claims below.  The boundary `d=2` is a singleton (`(01)^4`) and has the
project singleton-gap convention one.  Content begins at `d=3`.

## 2. Proved prefix-genus lemma

For any prefix/subword `u` on the fixed label set (isolates included), write

```text
s(u)=length,  c(u)=number of cycles of eval(u),
q(u)=number of support components including isolates,
g(u)=[s(u)-d-c(u)+2q(u)]/2.                       (2.1)
```

Appending one transposition changes `g` by either zero or one.  It changes
`g` by one exactly when its endpoints already lie in one support component
but in two different cycles of the current prefix permutation.  Indeed:

- joining two support components has `(Delta q,Delta c)=(-1,-1)`;
- cutting one permutation cycle inside a support component has `(0,+1)`;
- joining two permutation cycles inside one support component has `(0,-1)`.

Substitution in (2.1) gives increments `0,0,1`, respectively.  Thus (2.1)
is a nonnegative integer without importing a transitive-factorization lower
bound.

For `w in X_d`, (2.1) at the endpoint is

```text
g(w)=[2d-d-d+2]/2=1.
```

Consequently every word has a **unique forward handle factor** `h(w)`, the
unique prefix time at which `g` jumps from zero to one.  Apply the same rule
to the reversed word and let

```text
b(w)=2d+1-h(reverse(w))                            (2.2)
```

be the corresponding original factor position for the backward handle.

## 3. Proved tree--unicycle--tree cut theorem

At a cut after factor `j`, let `u=(t_1,...,t_j)`,
`v=(t_(j+1),...,t_(2d))`, and `p=eval(u)`, so `eval(v)=p^(-1)`.
Let `Q_L,Q_R` be the support-component partitions of `u,v`.
Construct a bipartite multigraph `B_j(w)`:

- its vertices are the blocks of `Q_L` and `Q_R`;
- every cycle of `p` gives one edge between the unique left and right
  support blocks containing that cycle.

Every permutation cycle is contained in one block of each support partition.
The join of `Q_L,Q_R` is the full support partition of `w`, so `B_j(w)` is
connected.  It has `q(u)+q(v)` vertices and `c(p)` edges.  Directly from
(2.1), using `length(u)+length(v)=2d`,

```text
g(u)+g(v)=q(u)+q(v)-c(p).                          (3.1)
```

Connectedness gives `c(p)>=q(u)+q(v)-1`, so the two nonnegative genera in
(3.1) can never both equal one.

The same factor cannot be both oriented handles.  Just before the forward
handle factor `e`, its endpoints lie in different cycles of `p`; hence `pe`
joins those cycles.  Viewed from the reverse suffix, adding the same `e`
changes `pe` back to `p` and cuts that joined cycle, so it is not a reverse
genus-creating factor.  Therefore

```text
b(w)<h(w).                                         (3.2)
```

It follows that the nonempty central-cut interval

```text
J(w)={j:b(w)<=j<h(w)}                              (3.3)
```

has the following exact profile.

- For `j<b(w)`, `g(u)=0,g(v)=1`, and `B_j(w)` is a tree.
- For `b(w)<=j<h(w)`, `g(u)=g(v)=0`, and `B_j(w)` is connected unicyclic.
- For `j>=h(w)`, `g(u)=1,g(v)=0`, and `B_j(w)` is a tree.

Thus every genus-one word, including every unmarked word, admits at least
one exact cut into **two componentwise genus-zero factorizations glued by one
unicyclic incidence graph**.  This avoids the zero-fiber defect of literal
marked deletion.

There is also an exact no-loss lift.  Put

```text
A_d={(w,j):w in X_d, j in J(w)},
tilde_pi(w,j)=pi_d(w)/|J(w)|.                      (3.4)
```

From `(w,j)`, make one `P_d` move `w->w'` and independently sample
`j'` uniformly in `J(w')`.  Detailed balance follows from

```text
tilde_pi(w,j) P_d(w,w')/|J(w')|
 =tilde_pi(w',j') P_d(w',w)/|J(w)|.
```

Conditional cut coordinates are refreshed in one step, while the `w`
marginal is exactly `P_d`; hence the nonzero spectrum, in particular the gap,
is exactly that of `P_d`.  Via (3.3), `A_d` is bijective to pairs of
componentwise genus-zero prefix/suffix factorizations with inverse products
and connected unicyclic cycle-incidence graph, with the exact weight (3.4).

This is the first genuine decomposition.  A proof can now target restricted
genus-zero factor expansion plus a projection/edge-slide inequality for the
single incidence cycle, rather than arbitrary torus surgery.

## 4. Sharp obstruction to a handle-only chain

One signed Hurwitz move at positions `i,i+1` preserves every prefix product
and support partition except possibly at prefix time `i`.  Thus

```text
|h(w')-h(w)|<=1,       |b(w')-b(w)|<=1.            (4.1)
```

However `h` is not a strong lump and has no pointwise nearest-neighbor move
lower bound.  Already at `d=3`, the two states

```text
x=(01)^4(02)^2,
y=(01)^3(02)(01)(12)
```

both have `h=3`.  All ten oriented proposals from `x` retain `h=3`, whereas
two of the ten oriented proposals from `y` move to `h=4`.  More strongly, for
every `d>=3`,

```text
x_d=(01)^4(12)^2(23)^2...((d-2)(d-1))^2           (4.2)
```

has `h=3`, and every one-step signed Hurwitz proposal retains `h=3`: moves
among the first four equal factors are fixed, while all later moves leave the
first three factors `(01)^3`, where the unique genus jump already occurs.

Therefore a proof cannot dominate the handle coordinate pointwise by a lazy
birth--death chain.  It must mix inside handle/seam fibers before obtaining
average projection flow.  This is an infinite, exact obstruction to that
specific proof route, not a slow-mixing result; (4.2) is already marked.

## 5. Exact marked-deletion multiplicity obstruction

Let `Z_d` be the connected genus-zero identity words of length `2d-2`, and
let `M=binom(d,2)`.  The marked incidence space has the exact bijection

```text
(z, insertion gap p, edge e)
 <-> (w, one connected-deletable adjacent square),
z in Z_d,  p in {1,...,2d-1},  e in T_d.           (5.1)
```

If `r(w)` is the number of such squares, the forgetful map in (5.1) has
fiber size exactly `r(w)`, with

```text
0<=r(w)<=2d-1.                                     (5.2)
```

Hence the projection of the uniform incidence law has density proportional
to `r(w)`, not the uniform genus-one law.  More decisively, it has zero mass
on unmarked states.  Such states exist for every `d>=3`: M92's accepted tree
family

```text
u_T=(a_T b_T)^3 product_(e in T minus {a_T,b_T}) e^2
```

is connected genus one and has `r(u_T)=0`.

This is the sharp deletion obstruction.  The many-to-one factor itself is
only polynomial: on `{r>0}`, a Metropolis correction loses at most `2d-1`.
The actual failure is the zero fiber on exponentially many accepted M92
sources, not exponential multiplicity.  Thus a recursive down--up proof must
first establish unmarked-to-marked flow, or use the everywhere-defined
virtual handle cut (3.3).

## 6. Exact next obligation

The positive route is now:

> **PARTIAL-FIBER HANDLE-CYCLE EXPANSION.**  On the exact lifted law (3.4),
> prove inverse-polynomial restricted gaps for the two componentwise
> genus-zero factorization sides and an inverse-polynomial projection/mean-
> lift inequality for seam moves that update the unique incidence cycle.

Only the one physical window straddling a fixed cut can alter its incidence
graph; moves strictly inside either side are literal Hurwitz moves on that
side and preserve cut admissibility.  The cut can be refreshed as in (3.4).
This gives exact state law and moves, but no estimate yet.  In particular,
the old minimal connected Hurwitz gap reappears as a restricted-side input;
it must be proved or bypassed, not silently assumed.

The weaker M92 worst-source marked hitting statement remains unresolved.
No full-`K` gap, conductance, mixing, or Terminal claim follows.
