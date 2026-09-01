# M97 final report: exact genus-one handle cuts

Date: 2026-08-12. Repository commit at execution:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Decision and exact scope

```text
PROMOTE the tree--unicycle--tree decomposition as a proved reduction.
REJECT a pointwise birth--death comparison on handle position.
UNRESOLVED: inverse-polynomial gap and worst-source marked hitting.
```

For every `d>=2`, this report gives an everywhere-defined exact-law lift of
the connected genus-one signed adjacent-Hurwitz walk to a cut at which both
sides are componentwise genus zero and the cycle-incidence graph is connected
unicyclic. The lift has exactly the original spectrum plus zero eigenvalues.
It proves no value for `gamma_1(d)`, no uniform M75-marked hitting bound, and
no full-`K` gap or mixing result. There is no Terminal claim.

Claims are labeled **PROVED**, **IMPORTED**, **EMPIRICAL**, **REFUTED**, or
**UNRESOLVED**. No Classification-H result is used; its source/convention
audit is therefore not a dependency. A positive gap itself would imply
irreducibility.

## 2. State law, convention, kernel, and boundary

Fix `[d]`, `d>=2`, and declare

```text
X_d={w=(t_1,...,t_(2d)): t_i transpositions,
                         t_1...t_(2d)=id,
                         support(w) connected},
pi_d=Unif(X_d).
```

Permutations compose as `(pq)(x)=p(q(x))`; tuple factors multiply
left-to-right. For adjacent `(a,b)`,

```text
R_i(a,b)=(b,bab),       R_i^(-1)(a,b)=(aba,a),
P_d=(1/2)I+[1/(4(2d-1))]
             sum_(i=1)^(2d-1)(R_i+R_i^(-1)).       (2.1)
```

The oriented maps are inverse bijections of `X_d`; hence `P_d` is symmetric
and reversible for `pi_d`. The desired statement
`gap(P_d)>=c d^(-C)` remains **UNRESOLVED**.

**PROVED boundary.** At `d=2`,
`X_2={((01),(01),(01),(01))}`. The singleton-gap convention gives
`gap(P_2)=1`; its handles are `h=3,b=2` and `J={2}`. The nontrivial regime
begins at `d=3`.

## 3. Prefix genus and oriented handles

For a word `u` on the fixed labels, isolates included, let `s(u)` be length,
`c(u)` the cycle count of `eval(u)`, and `q(u)` the support-component count.
Set

```text
g(u)=[s(u)-d-c(u)+2q(u)]/2.                        (3.1)
```

**PROVED.** Appending a transposition either (i) joins support components,
with `(Delta q,Delta c)=(-1,-1)`; (ii) cuts a permutation cycle within a
component, with `(0,+1)`; or (iii) joins two permutation cycles within a
component, with `(0,-1)`. Equation (3.1) changes by `0,0,1`, respectively.
Starting at zero, `g` is a nonnegative integer and is prefix-monotone. Since
`g(w)=[2d-d-d+2]/2=1` for `w in X_d`, there is a unique forward genus-creating
factor `h(w)`. Define the backward handle in original coordinates by

```text
b(w)=2d+1-h(reverse(w)).                           (3.2)
```

Reversal inverts the evaluated permutation and preserves cycle count,
support, and length, so suffix genus equals the corresponding reversed-prefix
genus. A Hurwitz move at `i,i+1` changes only prefix data at time `i`, proving
`|Delta h|<=1`; reversal proves `|Delta b|<=1`.

## 4. Tree--unicycle--tree cut theorem

Cut `w=uv` after factor `j` and put `p=eval(u)`, so `eval(v)=p^(-1)`. Let
`Q_L,Q_R` be the support-component partitions. Define a bipartite multigraph
`B_j(w)` whose vertices are their blocks and whose edges are the cycles of
`p`, each joining the unique left and right blocks containing that cycle.

**PROVED connectivity equivalence.** A product of within-block
transpositions preserves each support block, so every `p`-cycle lies in one
block of each partition. A left and right block intersect iff the `p`-cycle
of any label in their intersection supplies an edge between them; conversely
every edge witnesses a nonempty intersection. Thus alternating paths in
`B_j` are exactly chains of intersecting partition blocks. Its connected
components correspond exactly to blocks of `Q_L vee Q_R`; in particular,

```text
B_j connected iff Q_L vee Q_R is the one-block partition.       (4.1)
```

The union of the two supports is the connected support of `w`, so `B_j` is
connected. It has `V=q(u)+q(v)` and `E=c(p)`. Adding (3.1) for the sides gives

```text
g(u)+g(v)=q(u)+q(v)-c(p)=V-E.                     (4.2)
```

Connectedness implies `E>=V-1`, so the two nonnegative genera cannot both be
one. Now `g(u)=1` iff `j>=h`, while `g(v)=1` iff `j<b`, so `b<=h`. Equality
is impossible: if the same factor `e` created both handles, forward exposure
would change `p` to `pe` by joining two cycles, whereas reverse exposure
changes `pe` back to `p`, cutting that cycle and creating no genus. Hence

```text
b(w)<h(w),       J(w)={j:b(w)<=j<h(w)} nonempty.   (4.3)
```

Equations (4.2)--(4.3) give the exact profile

| cut | side genera | incidence graph |
|---|---|---|
| `j<b` | `(0,1)` | tree |
| `b<=j<h` | `(0,0)` | connected unicyclic |
| `j>=h` | `(1,0)` | tree |

Formula (3.1) is additive over support components, with isolates contributing
zero. Thus each genus-zero side is componentwise genus zero. This proves the
everywhere-defined decomposition, including for unmarked words.

## 5. Exact lift, reversibility, and spectrum

Let

```text
A_d={(w,j):w in X_d,j in J(w)},   ell(w)=|J(w)|,
tilde_pi(w,j)=pi_d(w)/ell(w),
L((w,j),(w',j'))=P_d(w,w')/ell(w').               (5.1)
```

**PROVED exact law.** The `w`-marginal is exactly `P_d`, and

```text
tilde_pi(w,j)L((w,j),(w',j'))
=pi_d(w)P_d(w,w')/[ell(w)ell(w')]
=tilde_pi(w',j')L((w',j'),(w,j)),
```

so `L` is reversible for (5.1).

**PROVED exact spectrum.** Let `(Uf)(w,j)=f(w)` and let
`RF(w)=ell(w)^(-1) sum_(j in J(w))F(w,j)`. Then `RU=I` and `L=UP_dR`.
The image is contained in `im(U)`, where `L` is conjugate to `P_d`, and
`ker(R)` is killed. Hence

```text
spec(L)=spec(P_d) plus zeros (with multiplicity).  (5.2)
```

Since half-lazy `P_d` has spectrum in `[0,1]`, `gap(L)=gap(P_d)`, including
the reducible case. The lift loses neither law nor gap, but supplies no
expansion estimate by itself.

## 6. Exact obstructions retained

**REFUTED handle-coordinate route.** At `d=3`,

```text
x=(01)^4(02)^2,             y=(01)^3(02)(01)(12)
```

both have `h=3`. All ten oriented proposals from `x` keep `h=3`, while two
from `y` move it to `4`. For every `d>=3`,

```text
x_d=(01)^4(12)^2(23)^2...((d-2)(d-1))^2           (6.1)
```

has `h=3` and every proposal keeps `h=3`: early moves among the four equal
factors are fixed; later moves leave the first three factors. Thus `h` is not
a strong lump and has no pointwise birth--death mobility bound. This is not a
slow-mixing result; (6.1) is marked.

**PROVED marked-incidence law.** If `Z_d` is the connected genus-zero
identity set of length `2d-2`, insertion/deletion gives the bijection

```text
(z in Z_d, gap p in {1,...,2d-1}, edge e)
 <-> (w, distinguished connected-deletable adjacent square).   (6.2)
```

The forgetful law weights `w` by its mark count `r(w)`, where
`0<=r(w)<=2d-1`. The multiplicity loss on the marked set is only polynomial;
the sharp defect is zero fibers.

**IMPORTED accepted M92 dependency.** For every labeled tree `T` on `[d]`,
`d>=3`, M92 proves, after deterministically choosing incident `a_T,b_T`, that

```text
u_T=(a_T b_T)^3 product_(e in T minus {a_T,b_T}) e^2  (6.3)
```

is connected, genus one, and unmarked. M95 independently accepted this.
M97 imports rather than reproves it from M92 `report.md`, SHA-256
`21662f10c53582e6fbf2fe18cc405ba7d92497948a76e7138d5a46f5a266678f`.
Thus literal deletion has zero fibers on at least `d^(d-2)` accepted sources;
the virtual cut (4.3) exists everywhere.

## 7. Finite falsification audit and boundary status

`handle_time_audit.py` exhaustively enumerates only `d=2,3,4`; its output is
`results.json`.

| `d` | candidates | states | unmarked | max `|Delta h|` | strong lump? |
|---:|---:|---:|---:|---:|---|
| 2 | 1 | 1 | 0 | 0 | yes (singleton) |
| 3 | 729 | 240 | 24 | 1 | no |
| 4 | 1,679,616 | 131,040 | 41,472 | 1 | no |

**EMPIRICAL only.** These exact finite facts falsify strong lumping and
calibrate the proved local-motion statement; they are not asymptotic gap
evidence. Reproduction command:

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
 experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M97-genus-one-hurwitz-gap/handle_time_audit.py \
 --d 2 3 4 \
 --output experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M97-genus-one-hurwitz-gap/results.json
```

Python `3.12.3`; seed `null`; nonstandard dependencies `{}`. Output SHA-256:
`5de0c3915658c28e7cacde2aa01c3022d38a272858358b65f4de29e08af80417`.

## 8. Dependencies, strongest self-attack, and hygiene

The positive theorem is elementary and uses no Classification H, M13
diameter, M68/M74 average incidence, or canonical hub. M92/M95 enter only for
the unmarked family. Frozen dependencies:

```text
21662f10c53582e6fbf2fe18cc405ba7d92497948a76e7138d5a46f5a266678f  M92 report.md
6490d4cd0daae58bf0ff68cbdceedb2d432cb27d743e18f02bea05bc4dd2ffd0  M92 oblivious_cover_reduction.md
e2e6ab274adc9d9cf20a0047196770c14b58681846738af0c919db6196547edc  M92 freeze_manifest.md
96c52fdc8f6a07d51869b5bf83415b001a9c7e825e22f041c69836ae3435241d  M68 report.md
285fca42f7f58a9f45ba63cb163f28566ccd5a30e8da1fb01679200500d90ffa  M74 report.md
e699e8b54684488ae34a8df87edea5f9a88002939e34d9facc55c549b741ed39  M75 report.md
ad09b58a061e8b65382a3fff316e846ef291b06de761fbad79711cf9b645fd44  M77 report.md
```

**Strongest self-attack.** Fixing a central cut leaves literal genus-zero
Hurwitz dynamics on both sides. One side can still be a connected identity
factorization on all `d` labels of minimal length `2d-2` while the other is a
square, so label count need not decrease. Only the physical window straddling
a fixed cut changes its incidence graph. Thus (5.2) is a coordinate theorem,
not a Poincare decomposition: it proves no restricted gap, mean-lift bound,
or seam conductance.

Only the owned M97 directory was edited. The manifest records hashes, cache,
and shared-worktree status; unrelated paths were not altered.

## 9. Verdict and first unproved obligation

**PROMOTE:** Every connected genus-one word has a nonempty interval of cuts
into componentwise genus-zero sides joined by one connected unicyclic
cycle-incidence graph. The cut-refreshed lift is reversible for
`pi_d(w)/|J(w)|` and has `spec(P_d)` plus zeros.

**REJECT:** Handle position alone is neither a strong lump nor pointwise
mobile, and marked deletion is not an everywhere-defined recursive coordinate.

**UNRESOLVED first standalone lemma:**

> **Partial-fiber handle-cycle expansion.** For (5.1), prove inverse-
> polynomial restricted expansion for both componentwise genus-zero sides and
> an inverse-polynomial projection/mean-lift inequality for physical seam
> moves updating the unique incidence cycle.

Such a lemma would imply the target through (5.2), but it is not proved here.
The weaker worst-source hitting time to the connected-deletable adjacent-
square set also remains unresolved. No full-`K` or Terminal criterion is met.
