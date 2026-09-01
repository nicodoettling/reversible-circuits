# M101 fresh referee report on frozen M97

Date: 2026-08-12.  Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Decision, accepted claim, and exact scope

```text
ACCEPT M97's tree--unicycle--tree decomposition and exact cut lift.
Material numbered objections: none.
```

For every `d>=2`, M97 correctly gives an everywhere-defined interval of cuts
of each connected-support identity transposition word of length `2d` into two
componentwise genus-zero sides whose cycle-incidence graph is connected
unicyclic.  Refreshing the cut after one signed adjacent-Hurwitz step gives a
reversible lift whose spectrum is exactly the base spectrum plus zeros.

M97 also correctly refutes a pointwise birth--death comparison on forward
handle position and shows that literal connected-square deletion has an
`r(w)`-biased forgetful law with zero fibers on an infinite accepted family.

This acceptance proves no inverse-polynomial value for `gamma_1(d)`, no
worst-source marked hitting bound, no partial-fiber expansion, no global lazy
`{3,4,5}` heat-bath gap or mixing bound, and neither Terminal A nor Terminal
B.  The positive deliverable is an exact decomposition/reduction, not a gap
estimate.

## 2. Frozen provenance and package integrity

The assigned hashes independently match:

| frozen M97 artifact | required SHA-256 | observed |
|---|---|---|
| `report.md` | `73ab5bec4d5ba48bb1b4511099df056525fe1f6b6f1b6caa6f79b7964feb3c99` | match |
| `freeze_manifest.md` | `6d0c28f8a4414175a3226b77fb1cff3217599f14ad707eaf5a7d3e3470babc4f` | match |

The individual payload digests in M97's `SHA256SUMS` agree when resolved in
the M97 directory.  The M92 dependencies used only for the unmarked family
also match the frozen boundary:

```text
21662f10c53582e6fbf2fe18cc405ba7d92497948a76e7138d5a46f5a266678f  M92 report.md
6490d4cd0daae58bf0ff68cbdceedb2d432cb27d743e18f02bea05bc4dd2ffd0  M92 oblivious_cover_reduction.md
e2e6ab274adc9d9cf20a0047196770c14b58681846738af0c919db6196547edc  M92 freeze_manifest.md
```

M95's fresh acceptance of M92 has SHA-256
`feeb86aa8fcd18cf0af9342928adb7c4780beaff25fc453f3416d66794bfe237`.
No M97, predecessor, coordinator, manuscript, skill, or shared durable file
was edited.

## 3. Target, convention, kernel, boundary, and dependencies

The audited auxiliary target is

```text
X_d={w=(t_1,...,t_(2d)): eval(w)=id, support(w) connected},
pi_d=Unif(X_d),                                              d>=2.
```

Permutations compose as `(pq)(x)=p(q(x))`, factors multiply left-to-right,
and the exact kernel is

```text
P_d=(1/2)I+[1/(4(2d-1))] sum_(i=1)^(2d-1)(R_i+R_i^(-1)),
R_i(a,b)=(b,bab),              R_i^(-1)(a,b)=(aba,a).
```

The oriented maps are inverse bijections, so `P_d` is symmetric and
reversible for `pi_d`.  It is an auxiliary within-fiber Hurwitz chain, not a
global sampler.  The positive cut theorem is elementary and does not invoke
Classification H.  A positive gap would itself imply irreducibility; M97
does not assume it.

At `d=2`, there is one edge and
`X_2={((01),(01),(01),(01))}`.  Direct computation gives `h=3`, `b=2`, and
`J={2}`.  Both base and lift are singletons, with the declared singleton-gap
convention one.  The unmarked-family obstruction begins at `d=3`.

## 4. Prefix genus, reverse handle, and local-motion audit

For a word `u` on the fixed `d` labels, including isolates, M97 defines

```text
g(u)=[s(u)-d-c(eval(u))+2q(u)]/2.
```

The proof's three cases are exhaustive and were independently re-derived.
Appending transposition `e` gives

```text
different support blocks:             (Delta q,Delta c,Delta g)=(-1,-1,0),
same block and same permutation cycle: (0,+1,0),
same block but different cycles:       (0,-1,+1).
```

Thus prefix genus starts at zero, remains a nonnegative integer, and is
monotone with increments zero or one.  At a connected identity endpoint of
length `2d`, it equals one, so there is one forward handle `h`; reversal has
one handle and defines `b=2d+1-h(reverse(w))`.

A Hurwitz move changes the product and support partition only at the single
intermediate prefix between its two factors.  Therefore `|Delta h|<=1`;
reversal gives the same for `b`.

The strictness argument is sound.  If one factor `e` were both handles and
`p` were the product just before it, forward genus creation says that `pe`
joins two `p`-cycles.  The reversed suffix immediately before the same factor
has product `pe`; appending `e` changes it back to `p`, cutting that joined
cycle, so it is not reverse-genus creating.  Once the incidence inequality
below supplies `b<=h`, this proves `b<h`.

## 5. Incidence connectivity, Euler profile, and componentwise genus

At a cut `w=uv`, put `p=eval(u)`, hence `eval(v)=p^(-1)`.  Every cycle of
`p` lies in a unique left support block and a unique right support block, so
it gives an edge of the stated bipartite multigraph.  A left and right block
intersect exactly when at least one such cycle joins them.  Therefore graph
components are precisely blocks of the join of the two support partitions.
The union support of `w` is connected, so the incidence graph is connected.

It has

```text
V=q(u)+q(v),           E=c(p),
g(u)+g(v)=V-E.
```

Connectedness gives `E>=V-1`, so the two side genera cannot both be one;
this gives `b<=h`, and Section 4 makes it strict.  Consequently:

| cut range | side genera | incidence profile |
|---|---|---|
| `j<b` | `(0,1)` | tree |
| `b<=j<h` | `(0,0)` | connected unicyclic |
| `j>=h` | `(1,0)` | tree |

The genus formula splits as a sum over support components, including zero
from every isolate.  Each component contribution is nonnegative by applying
the prefix-increment argument on that component's fixed label set.  Hence a
genus-zero side is componentwise genus zero.  This verifies the claimed
everywhere-defined tree--unicycle--tree decomposition.

## 6. Lifted law, operator factorization, full spectrum, and gap

Write `ell(w)=|J(w)|` and

```text
A_d={(w,j):j in J(w)},
tilde_pi(w,j)=pi_d(w)/ell(w),
L((w,j),(w',j'))=P_d(w,w')/ell(w').
```

Rows sum to one, the `w`-marginal from every lifted state is exactly `P_d`,
and detailed balance is

```text
tilde_pi(w,j)L((w,j),(w',j'))
 =pi_d(w)P_d(w,w')/[ell(w)ell(w')],
```

which is symmetric in the two states.

For `(Uf)(w,j)=f(w)` and
`RF(w)=ell(w)^(-1)sum_(j in J(w))F(w,j)`, one has `RU=I` and direct kernel
evaluation gives `L=UP_dR`.  Thus

```text
functions on A_d = im(U) direct-sum ker(R),
L|im(U) is similar to P_d,       L|ker(R)=0.
```

This proves the complete spectrum formula, including algebraic
multiplicities.  Since half-laziness puts the base spectrum in `[0,1]`, the
added zeros do not change its Poincare gap.  If the base is reducible, its
eigenvalue-one multiplicity is retained and both gaps are zero; no hidden
irreducibility assumption enters.  The `d=2` singleton case is as stated in
Section 3.

## 7. Frozen-handle and marked-deletion obstructions

For

```text
x_d=(01)^4(12)^2(23)^2...((d-2)(d-1))^2,       d>=3,
```

the first genus creation is the third `(01)`.  Proposals among the first four
equal factors are fixed; every later proposal leaves the first three factors
untouched.  Hence all `2(2d-1)` oriented proposals retain `h=3`.  At `d=3`,
M97's comparison state with the same handle has two proposals moving to four,
so handle position is not a strong lump.  This refutes that pointwise proof
route, not mixing.

Let `Z_d` be the connected genus-zero identity words of length `2d-2`.
Inserting a specified square `(e,e)` at one of `2d-1` gaps is inverse to
deleting a distinguished connected-deletable adjacent square.  Thus

```text
(z,gap,e) <-> (w,distinguished mark)
```

is bijective, and forgetting the mark weights `w` by exactly its mark count
`r(w)`, with `0<=r(w)<=2d-1`.  Multiplicity on the marked set is polynomial;
zero fibers are the real defect.

The exact frozen M92 family supplies those fibers.  For each labeled tree
`T`, choose distinct incident edges `a_T,b_T` and set

```text
u_T=(a_Tb_T)^3 product_(e in T minus {a_T,b_T}) e^2.
```

The incident product has order three, every tail pair is a square, and the
support is exactly `T`.  The alternating prefix contains no equal pair, while
deleting a tail square removes the only occurrences of a tree bridge and
disconnects support.  Hence all `d^(d-2)` distinct tree-supported words are
unmarked.  M97 correctly imports this accepted dependency rather than
claiming an independent proof provenance.

## 8. Independent computation, reproduction, self-attack, and hygiene

`independent_audit.py` was written from scratch and imports no M97 code.  Its
principal command was

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
 experiments/20260811-polynomial-mixing-resolution/cycle-20/mission-M101-m97-fresh-referee/independent_audit.py \
 --d 2 3 4 --frozen-family-max-d 12 --m92-family-max-d 5 \
 --output experiments/20260811-polynomial-mixing-resolution/cycle-20/mission-M101-m97-fresh-referee/independent_results.json
```

It was deterministic (`seed=null`), ran under Python `3.12.3`, and used
NumPy `1.26.4` only for the small lifted eigensystem.  Exact structural
results were:

| `d` | states | cuts checked | unmarked | insertion incidences |
|---:|---:|---:|---:|---:|
| 2 | 1 | 5 | 0 | 3 |
| 3 | 240 | 1,680 | 24 | 360 |
| 4 | 131,040 | 1,179,360 | 41,472 | 120,960 |

All 1,181,045 cuts passed incidence connectivity, genus additivity, the exact
three-region Euler profile, and componentwise-genus checks.  Every square
insertion incidence matched exactly one deletion mark.  M97's state,
handle-pair, mark, displacement, and row-signature counts were reproduced.

At `d=3`, the base has 240 states and the lift 336.  The lift has exactly 96
additional numerical zero eigenvalues; its gap is
`0.02771319171181541` versus base `0.02771319171181641`.  Residuals were
`1.8e-15` for `L=UPR` and `3.0e-15` for the spectrum union.  The frozen-handle
family passed through `d=12`; all `3,16,125` M92 tree words at `d=3,4,5`
were distinct and unmarked.

These finite checks calibrate the proofs and supply falsifiers only; they are
not asymptotic gap evidence.  The strongest self-attack is exactly M97's:
fixing a cut can leave a full-label minimal connected genus-zero factor on one
side, and only a seam window updates incidence.  The coordinate theorem gives
no restricted-side gap, seam conductance, or mean-lift estimate.  Nothing in
this audit repairs that missing analysis.

All artifacts are confined to M101.  Bytecode caches are removed before
freeze.  Final Git status is recorded in the manifest; the shared worktree's
other untracked mission and note paths are unrelated.

## 9. Final verdict and first unproved obligation

**ACCEPT, with zero material numbered objections.**

M97 validly promotes an everywhere-defined exact genus-one cut coordinate
and a spectrum-preserving lift, while correctly retaining the failure of
handle-only lumping and literal deletion on zero fibers.  The first open
standalone step remains:

> Prove inverse-polynomial restricted expansion for the two componentwise
> genus-zero sides and an inverse-polynomial projection/mean-lift inequality
> for physical seam moves updating the unique incidence cycle.

The alternative worst-source hitting bound to the connected-deletable square
set remains unresolved.  So do `gamma_1(d)>=d^{-O(1)}`, the full local
heat-bath gap and mixing time, and both Terminal criteria.
