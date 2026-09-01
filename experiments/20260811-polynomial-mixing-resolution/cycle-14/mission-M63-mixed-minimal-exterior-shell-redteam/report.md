# M63 final report: mixed minimal/exterior halos leak polynomially

## 1. Exact claims, quantifiers, and convention

Permutations are maps on `[N]`, `(pq)(x)=p(q(x))`, and words evaluate as
`t_1...t_m`.  Use the literal global chain

```text
K=(1/2)I+(1/(2|R_m|)) sum_(r in R_m)
       (1/(m-r+1)) sum_i H_(i,r),
R_m={r in {3,4,5}:r<=m},
```

with uniform stationary law `pi` on `Omega(N,m)`.  In this report `N>=5`,
`m=2N-2`, `M=binom(N,2)`, and

```text
D_N=(3N^2+N-12)/2,
Lambda_N=binom(m,2)(N-1)^2.                         (1.1)
```

Fix a labeled path join tree `T_N`, its original leaf `v` with neighbor `u`,
and its other original leaf `w`.  Let `Core=Del_{v,w}`.  For any nonempty
proper core set `B`, define

```text
A={x in F_N(T_N):Core(x) in B},
Z=Del_v(A).                                          (1.2)
```

The following three scoped anti-bottleneck theorems are proved.

**Claim A (smallest specified-target halo).** Fix one transposition `s`
avoiding `v` and put

```text
E^(1)={z s s:z in Z},
C^(1)=A union E^(1).                                 (1.3)
```

Then `E^(1) subset F_N^c`, `|E^(1)|=|Z|` exactly, and

```text
pi(C^(1))=(|A|+|Z|)/|Omega(N,m)|,
Phi_pm^K(C^(1))
 >=(N-2)/[6(m-2)D_N(Lambda_N+1)]
 >=1/(144N^6).                                      (1.4)
```

This is the smallest exterior halo that absorbs the single specified M60
H3 target from every deletion-cell hub.

**Claim B (maximal one-step exterior halo).** Let

```text
E^(all)={y in F_N^c:K(x,y)>0 for some x in A},
C^(all)=A union E^(all),
D_out=sum_(r=3)^5 (m-r+1)M^r.                       (1.5)
```

Thus `E^(all)` absorbs every exterior H3/H4/H5 neighbor of every state in
`A`.  Its exact stationary mass is

```text
pi(C^(all))=(|A|+|E^(all)|)/|Omega(N,m)|,
```

and `|E^(all)|<=D_out|A|`, giving

```text
Phi_pm^K(C^(all))
 >=(N-2)/[6(m-2)D_N Lambda_N(1+D_out)]
 >=1/(672N^17).                                     (1.6)
```

The same bound holds for any exterior halo
`E^(1) subseteq E subseteq E^(all)`.  More generally, every exterior
`E subseteq F_N^c` satisfies the alternate-target lower bound

```text
Q_K(A union E,(A union E)^c)/pi(A union E)
 >=(N-2)/[6(m-2)D_N Lambda_N(1+|E|/|A|)].           (1.7)
```

Thus any exterior halo of only polynomial mass relative to `A` is ruled out
as Terminal B.

**Claim C (structurally distinct fixed-missing-label halo).** Let

```text
A_v={x in Omega(N,m):no factor of x contains v},
C^(v)=A union A_v.                                   (1.8)
```

This is a nonlocal exterior phase, not a one-step shell.  Exactly

```text
pi(C^(v))=[|A|+|Omega(N-1,m)|]/|Omega(N,m)|,
```

and

```text
Phi_pm^K(C^(v))
 >=min{
   (N-2)/[6(m-2)D_N Lambda_N],
   1/[3(m-2)(N-1)D_N]
 }
 >=1/(96N^6).                                       (1.9)
```

All three claims split both `F_N` and `F_N^c`; none reduces to M60 or M62 by
complementation.  They are nonterminal scoped results.

## 2. Full argument and construction

### 2.1 Core saturation and deletion-cell count

Multi-strand erasure commutes, so for a fixed `v`-base `z`, the value
`Core(x)=Del_w(z)` is the same for every lift in the cell.  Hence `A` is a
union of complete `v`-deletion cells.  For every `z in Z`, the adjacent leaf
square word

```text
h_z=z (v,u)(v,u)                                    (2.1)
```

lies in `A`.  The accepted strand-lift multiplicity bound gives

```text
|A|<=Lambda_N |Z|.                                  (2.2)
```

This is a counting inequality, not routing through one global hub: every
base has its own source (2.1).

### 2.2 Alternate full-support outcomes

Let `c` be the final factor of `z`.  The final H3 window of (2.1) is
`c(v,u)(v,u)` and has product `c`.  For every
`a in [N] minus {v,u}`, the block

```text
c(v,a)(v,a)                                         (2.3)
```

has the same ordered product.  The resulting word

```text
z(v,a)(v,a)                                         (2.4)
```

is an identity word with connected full support.  Its join tree is
`T_N-v` with leaf `v` attached at `a`, rather than at `u`, so it is outside
the fixed path sector and outside `A`.  It is also outside every exterior
halo `E subseteq F_N^c`.  The `N-2` choices are distinct.

The exact length-three fiber of a transposition product has size `D_N`.
Including laziness, block-size choice, the final window among `m-2` windows,
and the conditional outcome gives

```text
K(h_z,(A union E)^c)>=(N-2)/[6(m-2)D_N]              (2.5)
```

for every exterior `E`.  Distinct bases give distinct sources and targets.
Therefore

```text
Q_K(A union E,(A union E)^c)
 >=|Z|/|Omega| * (N-2)/[6(m-2)D_N].                 (2.6)
```

Combining (2.2) and the exact mass
`pi(A union E)=(|A|+|E|)/|Omega|` proves (1.7).  Since the two-sided
denominator is at most `pi(A union E)`, no separate mass orientation is
needed.

### 2.3 Smallest halo

Fix `s` on `[N] minus {v}`.  Every word `zss` omits `v`, so it is exterior.
The map `z -> zss` is injective and its image is disjoint from `A`; hence the
mass statement in (1.4) is exact.  It contains the one specified M60 outcome
from every hub (2.1).

With `E=E^(1)`, equation (2.2) gives

```text
|A|+|E^(1)|<= (Lambda_N+1)|Z|.
```

Substitute into (2.6) to prove the first bound in (1.4).  For `N>=5`, use
`N-2>=N/2`, `m-2<=2N`, `D_N<=2N^2`, and
`Lambda_N+1<=3N^4` to obtain `1/(144N^6)`.

### 2.4 Maximal one-step halo and all r=3,4,5 outcomes

For one source word and a fixed `(r,i)`, there are at most `M^r` ordered
replacement blocks.  Therefore the number of distinct exterior neighbors is
at most

```text
D_out=sum_(r=3)^5 (m-r+1)M^r<=3mM^5.                (2.7)
```

Union-bounding over `A` proves `|E^(all)|<=D_out|A|`.  This is a cardinality
bound on the exact set in (1.5), so overlaps only make it stronger.  Insert
it into (1.7) to prove the first bound in (1.6).  Using
`1+D_out<=7N^11` together with the bounds in Section 2.3 gives the safe
`1/(672N^17)` estimate.

By definition, every exterior target of every H3, H4, and H5 update from `A`
is inside `E^(all)`.  The boundary in (2.5) consists instead of fully
supported H3 targets, so it survives the entire exterior closure.  H4 and H5
flow from the halo itself is retained in the literal kernel and can only add
to (2.6).

### 2.5 Nonlocal fixed-missing-label halo

The sets `A` and `A_v` are disjoint because `A` has full support and `A_v`
omits `v`.  Avoiding `v` identifies `A_v` exactly with `Omega(N-1,m)`, proving
the mass formula in (1.9).

Conditional on `A_v`, let `S(x)` count adjacent equal transpositions.  The
marked-square deletion identity and even return-probability monotonicity give

```text
Pr(S>=1 | A_v)>=1/binom(N-1,2).                      (2.8)
```

On a certified state, use the first adjacent square, pad it on the available
side, and refresh it to `(v,a)^2`.  There are `N-1` possible labels `a`.
Every outcome leaves `A_v`.  At most `a=u` can enter `A`: if the output had
join tree `T_N`, its only factor incident to `v` would force its leaf edge to
be `(v,a)=(v,u)`.  Thus all `N-2` choices with `a!=u` lie outside
`C^(v)`.  Equations (2.8) and the exact H3 normalization yield

```text
Q_K(C^(v),(C^(v))^c) from A_v sources
 >=pi(A_v)/[3(m-2)(N-1)D_N].                        (2.9)
```

The sources in `A` independently give, by (2.2)--(2.6),

```text
Q_K(C^(v),(C^(v))^c) from A sources
 >=pi(A)(N-2)/[6(m-2)D_N Lambda_N].                 (2.10)
```

The source sets are disjoint, so the flows add.  Dividing by
`pi(A)+pi(A_v)` and taking the smaller coefficient proves (1.9).  The coarse
bound follows from the same estimates as Section 2.3; the second coefficient
is at least `1/(12N^4)`.

### 2.6 Exact N=5 smallest-halo audit

For the representative N=5 path, an exact half-core selection gives

```text
|A|=3904, |Z|=|E^(1)|=87, |C^(1)|=3991,
pi(C^(1))=3991/1770940.                              (2.11)
```

It has exactly `3|Z|=261` alternate full-support targets from (2.4).  Exact
enumeration of every conditional outcome gives

```text
Q(C^(1),(C^(1))^c)/pi(C^(1))
=17932842729275693759/44514228823515360000
=0.4028564169981168....                              (2.12)
```

The complete boundary split is:

| r | minimal full-support targets | exterior targets | total |
|---:|---:|---:|---:|
| 3 | 0.0784850745 | 0.0242990816 | 0.1027841562 |
| 4 | 0.0940909692 | 0.0469977607 | 0.1410887299 |
| 5 | 0.0980816715 | 0.0609018594 | 0.1589835309 |

The exact category fractions down to exterior support size are in the JSON.
The universal bound (1.4) at N=5 is `1/183192`.  This finite computation
could falsify the injection, mass, normalization, or a missing boundary
category; its positive escape is not the universal proof.

For the structurally distinct fixed-label halo,
`|Omega(4,8)|=140160`, so the N=5 mixed cut has exact size
`3904+140160=144064` out of `1770940`.

## 3. Worst probability, runtime, path length, and congestion

- Each alternate leaf target has exact probability
  `1/[6(m-2)D_N]`; summing `N-2` targets gives (2.5).
- The source fraction is at least `1/Lambda_N` by (2.2).  All paths have
  length one; no comparison congestion or canonical routing is used.
- The smallest-halo, all-one-step-halo, and fixed-label bounds are
  respectively at least `1/(144N^6)`, `1/(672N^17)`, and `1/(96N^6)`.
- `D_out` explicitly includes every window and every ordered outcome for
  r=3,4,5.  Laziness contributes no new neighbor.
- The exact N=5 audit enumerates the 3,904 minimal states, 87 halo states,
  every r=3,4,5 window, and every exact conditional block outcome.  It ran in
  129.77724347705953 seconds using Python 3.12.3 and no nonstandard package.

## 4. Dependencies with status

1. **PROVED HERE:** core-cell saturation; exact smallest-halo injection and
   mass; alternate full-support target count; general halo inequality (1.7);
   one-step outdegree bound; fixed-label absorbed-outcome audit; Claims A--C.
2. **PROVED / INHERITED FROM M49/M60:** commuting strand deletion and the
   cell multiplicity bound `Lambda_N`.
3. **PROVED / INHERITED FROM M19:** exact mass of `A_v`, marked-square
   incidence (2.8), and the even return-probability inequality.  The
   `N-2` boundary-safe outcomes after adjoining `A` are re-audited here.
4. **PROVED / INHERITED COMMON CORE:** exact transposition-product H3 fiber
   size `D_N`, uniform stationarity, and reversibility.
5. **EXACT FINITE FACT:** the N=5 all-outcome mass and flow calculation.
6. **UNRESOLVED:** recursively thick exterior halos of superpolynomial mass
   relative to the internal core sector.

## 5. First unproved standalone proposition

**MULTISTEP EXTERIOR-CLOSURE LEAKAGE.** Let `E_0=E^(all)` and recursively let

```text
E_(k+1)={y in F_N^c:K(x,y)>0 for some x in E_k} union E_k.
```

For an explicit growing `k=k(N)`, analyze `C_k=A union E_k`.  Prove a
universal inverse-polynomial lower bound on `Phi_pm^K(C_k)` with exact
stationary mass and every H3/H4/H5 boundary, or produce an explicit sequence
for which `|E_k|/|A|` is superpolynomial while the exterior shell flow is
small enough to satisfy Terminal B.  Claims A--C show that a successful halo
must be larger than every one-step closure and cannot be the entire
fixed-missing-label phase.

## 6. Strongest self-attack / failure mode

The key lower bound (1.7) degrades linearly with `|E|/|A|`.  It says nothing
by itself when an exterior halo has superpolynomially larger stationary mass
than the internal core sector.  A multistep closure could have precisely that
property and could absorb its own boundary through correlated surplus
histories.  The fixed-label theorem rejects one large structured halo but
does not cover unions over many missing labels or recursively growing
support-restoration shells.

The exact N=5 escape near 0.403 is finite and not asymptotic evidence.  Also,
Claims A--C control specifically the path-core sector in (1.2); they do not
constitute an arbitrary-cut conductance theorem for global `K`.

## 7. Calibration suite

- Odd `m`: `Omega` is empty.  The claims use even `m=2N-2`.
- `m=0` and `N=2` even are singleton calibrations; `m=2,N>=3` is excluded.
- `N=3,m=4`: 27 words and 4 pure-Hurwitz components; H4 is whole-word and
  `|R_m|=2`.  The nontrivial balanced path core used here starts at `N=5`.
- `S_4,m=4`: 120 words and 13 Hurwitz components; whole-word H4 cannot be
  ignored.  This is below four-label minimal full-support length.
- `S_4,m=6`: 3,936 words and 17 Hurwitz components.  Its pruned path core is
  singleton, consistent with the absence of a balanced core cut.
- N=5 has the eight exact core components; the selected balanced union has
  size 3,904 and all H3/H4/H5 categories are listed in Section 2.6.
- Path/doubled-tree words certify nonempty core fibers, but no fixed global
  hub or doubled-tree routing is used.
- The full ordered word, insertion history, and support are retained.  No
  parity-only, graph-only, or commuting-color quotient is used.
- No length-two simulation is invoked.  Every boundary witness is a literal
  H3 heat-bath outcome with exact global normalization.
- Stationary orientation is explicit: each proof first bounds `Q/pi(C)`, and
  the two-sided denominator is never larger than `pi(C)`.

## 8. Artifacts and reproduction

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/
  cycle-14/mission-M63-mixed-minimal-exterior-shell-redteam/
```

Command from repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -u experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M63-mixed-minimal-exterior-shell-redteam/exact_n5_mixed_halo.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M63-mixed-minimal-exterior-shell-redteam/exact-n5-smallest-halo.json
```

Metadata: commit `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, Python
3.12.3, seed `null`, no nonstandard dependency.

SHA-256:

```text
a9f4d315df1015ab03b7296d8a64c8024bb79aa54502d4c7c01954fb046e3be2  exact_n5_mixed_halo.py
48fa052e9b1eb6d66d06bce69a01482d8acac8e3c10a893895cd272f52b6f422  exact-n5-smallest-halo.json
```

## 9. Verdict

**PROVED.** The smallest canonical-target halo, the maximal one-step exterior
halo containing every H3/H4/H5 exterior neighbor, and the structurally
distinct full fixed-missing-label halo all have explicit universal
inverse-polynomial conductance.  This scoped verdict is nonterminal for the
global goal.

