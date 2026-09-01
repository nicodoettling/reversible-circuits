# M48 final report: weighted replanting-to-rotation flow

Date: 2026-08-11.  Frozen bundle version 1.  This report concerns the
minimal-sector parking macro represented by rooted plane trees.  The project
permutation convention remains `(pq)(x)=p(q(x))`, with factor tuples
multiplied left-to-right; no new permutation identity is used below.

## 1. Exact claim with all quantifiers and conventions

For a rooted plane tree `t` with `r` edges, let

```text
omega(t)=product_v 1/d_v(t)!,
Z_r=(r+1)^(r-1)/r!,
pi_r(t)=omega(t)/Z_r.
```

For `r>=2`, let `L_r` be the reversible leaf-rotation subchain accepted in
M35/M46.  Its forward move replaces a nonlast leaf child followed by one
sibling subtree by a unary child containing that subtree; in Dyck notation,

```text
UD P -> U P D,
```

where `P` is one primitive excursion.  If the old parent has degree `d_i`,
the forward and reverse rates are exactly

```text
2d_i/[3r(r-1)]  and  2/[3r(r-1)],
```

and unused probability is placed on the diagonal.

Put, for every `r>=3`,

```text
n=r-1,
D_r=2+ceil(log_2 n),
b_r=(r+1)(e/D_r)^D_r.
```

The following is **proved**:

```text
gap(L_r)
 <= b_r/[(e^(-1)-b_r)(3/(8e^2)-b_r)]               (1.1)
```

whenever the two displayed denominator factors are positive.  Therefore,
for every fixed `C>0`,

```text
r^C gap(L_r) -> 0.                                  (1.2)
```

Consequently there is no universal polynomial path or fractional-flow
congestion comparison from the M41 weighted Metropolis leaf-replanting
chain `Y_r` to `L_r`.  This **refutes the assigned comparison target**.
It is an auxiliary result only: `L_r` is a strict subchain of the actual
rank-two parking projection, and neither (1.1) nor (1.2) is Terminal B for
the original identity-word chain.  In fact, the full projection crosses the
same cut at inverse-polynomial flow, as quantified in Section 2.4.

## 2. Full argument

### 2.1 Root branch sizes project into a reversible-pebble graph

Let the root children of `t`, in plane order, have positive branch sizes

```text
a(t)=(a_1,...,a_k),  sum_i a_i=r,
```

where each size includes its edge from the root.  Define

```text
S(t)={a_1,a_1+a_2,...,a_1+...+a_(k-1)} subset [r-1]. (2.1)
```

A leaf rotation below the root preserves every root branch size.  At the
root it maps

```text
(1,q) <-> (q+1).
```

If `s` is the sum of the preceding branch sizes, (2.1) toggles `s+1`, and
`s=0` or `s` is already present.  Thus every `L_r` edge maps into the
reversible-pebble graph whose configurations are subsets of `[n]` and whose
rule is

```text
toggle i only if i=1 or i-1 is present.             (2.2)
```

Surjectivity onto all pebble toggles is neither asserted nor needed; a
reverse tree split additionally requires the relevant branch root to be
unary.

Let

```text
B_r={t:max_v d_v(t)>=D_r}.
```

In `B_r^c`, the root has at most `D_r-1` children, so `S(t)` contains at
most

```text
p=D_r-2=ceil(log_2 n)                               (2.3)
```

pebbles.

The empty configuration and `{n}` are disconnected in (2.2) under the cap
(2.3).  If they were connected, the path would be a persistent reversible
pebbling of the directed `n`-vertex path from the empty configuration to a
single pebble on its sink.  Komarath--Sarma--Sawlani,
arXiv:1604.05510, Theorem 12, gives

```text
R^bullet(P_n)=chi'_e(P_n)+1=ceil(log_2 n)+1.
```

For completeness, the edge-ranking formula has a one-line induction.  If
`M(k)` is the maximum number of edges in a path ranked with `k` colors, its
highest color occurs at most once and its deletion leaves two paths ranked
with `k-1` colors.  Hence
`M(k)<=1+2M(k-1)=2^k-1`; recursive median-edge ranking attains equality.
The required pebble number is therefore one larger than the cap (2.3).

Let `C_0` be the component of the empty pebble configuration under this cap
and set

```text
A_r={t notin B_r:S(t) in C_0}.                       (2.4)
```

Every low-degree `L_r` neighbor of a tree in `A_r` maps to the same pebble
component.  Therefore every `L_r` edge leaving `A_r` enters `B_r`.

### 2.2 Both sides of the cut have constant mass

All root-degree-one trees have `S(t)` empty.  Removing their root and root
edge leaves an arbitrary tree with `r-1` edges, so

```text
pi_r(d_root=1)=Z_(r-1)/Z_r
                 =(r/(r+1))^(r-1)>=e^(-1).          (2.5)
```

After removing `B_r`, (2.5) gives

```text
pi_r(A_r)>=e^(-1)-pi_r(B_r).                         (2.6)
```

For the opposite side, use the ordered root branch-size event

```text
a(t)=(r-1,1).
```

Its prefix set is `{n}`, outside `C_0`.  The first child subtree has `r-2`
internal edges, the second child is a leaf, and the root weight is `1/2!`.
Its exact probability is

```text
(1/2)Z_(r-2)/Z_r
 =r(r-1)^(r-2)/[2(r+1)^(r-1)]
 >=3/(8e^2).                                        (2.7)
```

The last inequality uses `r/[2(r+1)]>=3/8` and
`log(1-x)>=-x/(1-x)` with `x=2/(r+1)`.  Excluding `B_r` gives

```text
pi_r(A_r^c)>=3/(8e^2)-pi_r(B_r).                     (2.8)
```

### 2.3 Separator mass, Rayleigh quotient, and the gap

The M41 cycle-lemma/Vervaat representation identifies maximum outdegree
under `pi_r` with maximum occupancy for `r` independent balls in `r+1`
uniform boxes.  A union bound and the standard binomial tail yield

```text
pi_r(B_r)<=(r+1)(e/D_r)^D_r=b_r.                    (2.9)
```

Because `D_r` is asymptotic to `log_2 r`,

```text
log b_r=-Omega(log r log log r),
```

so `b_r=o(r^-C)` for every fixed `C`.

Let `Q_L(x,y)=pi_r(x)L_r(x,y)`.  The support statement after (2.4) and
reversibility give

```text
Q_L(A_r,A_r^c)=Q_L(A_r,B_r)=Q_L(B_r,A_r)<=pi_r(B_r). (2.10)
```

For the indicator of `A_r`, the Dirichlet form is exactly the left side of
(2.10) and the variance is `pi_r(A_r)pi_r(A_r^c)`.  Equations
(2.6)--(2.10) prove (1.1) and (1.2), with no hidden scan or laziness factor.

Finally, any polynomial comparison would give
`E_Y<=r^C E_L` for some fixed `C`.  M41 proves
`gap(Y_r)>=1/[16(r+1)^8]`; hence the comparison would imply
`gap(L_r)>=1/[16r^C(r+1)^8]`, contradicting (1.2).  This excludes arbitrary
fractional polynomial-congestion flows, not merely one canonical path.

### 2.4 The full rank-two projection provably bypasses this cut

Let `bar P_r` be the full nonlazy projected adjacent rank-two heat bath and
let

```text
E_r={t:ordered root branch-size composition is (r-1,1)},
E_r^-={t in E_r:max_v d_v(t)<=D_r-2}.
```

Every source in `E_r^-` lies in `A_r^c`, has `d_0=2`, and has prefix set
`{n}`.  The M35 aggregate-departure identity gives exactly

```text
sum_(j>0) bar P_r(d,d-e_0+e_j)
 =2d_0(d_0-1)/[3r(r-1)]=4/[3r(r-1)].                (2.11)
```

Every positive target in (2.11) has root degree one, empty prefix set, and
maximum degree at most `D_r-1`; hence it belongs to `A_r`.  Put

```text
beta_r=(1/2)Z_(r-2)/Z_r
      =r(r-1)^(r-2)/[2(r+1)^(r-1)],
bprime_r=(r+1)(e/(D_r-1))^(D_r-1).
```

The same occupancy tail bound gives
`pi_r(E_r^-)>=beta_r-bprime_r`.  Reversibility and (2.11) therefore prove

```text
Q_(bar P_r)(A_r,A_r^c)
 >=4(beta_r-bprime_r)/[3r(r-1)].                    (2.12)
```

Since `beta_r>=3/(8e^2)` and `bprime_r` is superpolynomially small, (2.12)
is of order at least `r^-2`.  Thus the new separator is rigorously not a
superpolynomial bottleneck for the full projected chain.

## 3. Probability, runtime, path length, and congestion accounting

- Exact separator mass: `pi_r(B_r)<=b_r`, with constant-mass sides bounded
  by (2.6) and (2.8).
- Exact boundary flow: `Q_L(A_r,A_r^c)<=pi_r(B_r)`; replacing this by a
  one-sided transition estimate is unnecessary.
- Full-projection bypass flow is bounded below by (2.12), asymptotically a
  positive constant times `r^-2`.
- Replanting reference gap: `gap(Y_r)>=1/[16(r+1)^8]`.
- A polynomial comparison congestion is impossible by (1.2).  Equivalently,
  its comparison constant must exceed every fixed power of `r` along a
  subsequence.
- The tree move and the root-prefix map are computable in `O(r)` time from
  parent/child arrays; enumerating all replant proposals takes `O(r^2)`.
- Exact enumeration is Catalan-exponential and is used only as a bounded
  falsifier.  The `r<=10` separator run took about five wall-clock seconds
  on this machine with Python 3.12.3.
- Through `r<=8`, every replant neighbor was rotation-connected and the
  largest shortest distance was `(r-1)^2`; this is empirical and is not used
  in the separator proof.

## 4. Dependencies, each labeled

- **Proved here:** root-composition projection; capped-pebble separation;
  exact constant-mass witnesses; cut support; Rayleigh quotient; the
  superpolynomial `L_r` gap upper bound; refutation of every polynomial
  `Y_r`-to-`L_r` flow comparison.
- **Proved and accepted in M35/M46:** the universal leaf-rotation edges and
  exact forward/reverse rates, including `3r(r-1)` normalization.
- **Proved in M41:** `gap(Y_r)>=1/[16(r+1)^8]`; the cycle-lemma maximum-degree
  bound (2.9).
- **Proved independently in M46 from the M35 aggregate identity:** the
  full-projection bypass formula (2.11)--(2.12).
- **Cited with hypotheses checked:** Komarath, Sarma, and Sawlani,
  *Pebbling Meets Coloring: Reversible Pebble Game on Trees*,
  arXiv:1604.05510, Theorem 12.  Our configurations use its persistent
  reversible rule on a directed path: empty initially, only the sink
  pebbled finally, and placement/removal both require the predecessor.
- **Empirical only:** all Catalan enumerations and shortest/minimax paths.
  They can falsify the structural lemma at bounded `r` but prove no
  asymptotic statement.

## 5. First unproved standalone proposition

> **FULL ACTUAL PARKING FLOW.**  Let `A_r^ideal` be the accepted
> adjacent-value restriction of the Lorentzian down-up parking chain and let
> `bar P_r` be the full nonlazy adjacent rank-two projection.  There is a
> universal constant `C` and a fractional assignment of every directed
> `A_r^ideal` commodity to `bar P_r` paths of length at most `r^C` such that
> every directed projected edge has total stationary-flow congestion at
> most `r^C`.

The aggregate departure identity (2.11) supplies polynomial total flow out
of every duplicated label, but a global assignment still needs randomized
buffer choices and recoverable source metadata.  The restricted chain
`L_r` cannot be used as the comparison target.

## 6. Strongest self-attack

Adding reversible edges can increase a gap by an arbitrary factor.  Here
this is not merely a logical possibility: (2.12) proves that non-leaf
rank-two moves cross `A_r` with inverse-polynomial stationary flow while
staying below degree `D_r`.  Therefore it would be invalid to use (1.2) as
an upper bound for the full projection, still less for the `{3,4,5}` chain.
The result closes only the proposed replanting-to-`L_r` route.

## 7. Calibration results

- `r=1`: singleton; gap convention one.  The separator is not invoked.
- `r=2`: the two nominal root leaves are shape-indistinguishable; the
  separator theorem starts at `r=3`.
- Exact enumeration for `3<=r<=10` found
  `D_min=2+ceil(log_2(r-1))` for the maximum degree needed to connect the
  leaf/chain test endpoints, disconnected empty and `{r-1}` pebble
  components under cap `D_min-2`, and zero low-degree cut crossings.
- The exact cut masses for `r=3,...,10` were approximately
  `.750,.816,.710,.852,.768,.711,.675,.875`; both sides remained visible.
  These numbers are checks only; constant lower bounds are proved by
  (2.5)--(2.8).
- At `r=3`, the full projection has `d=(2,1,0)` and aggregate destinations
  `d=(1,2,0)` and `d=(1,1,1)`, each at rate `1/9`; this checks (2.11) and
  the fact that the restricted separator is bypassed.
- Star and path denominators are respectively `r!` and `1`.  No direct
  point-mass comparison or fixed star/path hub enters the proof.
- Rare and balanced degree profiles are covered by the occupancy bound;
  the proof uses total separator mass rather than a single low-capacity
  state.
- The original calibrations `S_3,m=4`, `S_4,m=4`, `S_4,m=6`, the whole-word
  `H_4` move, and the odd/`m=2` exclusions are not contradicted because this
  report makes no claim for the original chain.

## 8. Artifacts and reproduction commands

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-11/
  mission-M48-replanting-to-rotation-flow/
```

Proof: `separator_theorem.md`.  Deterministic scripts and outputs:

```text
python3 rotation_replant_probe.py --r-max 8 --output rotation_replant_r8.json
python3 rotation_bottleneck_probe.py --r-max 8 --output rotation_bottleneck_r8.json
python3 chain_swap_path_probe.py --r-max 10 --output chain_swap_paths_r10.json
python3 degree_separator_probe.py --r-max 10 --output degree_separator_r10.json
```

The scripts use only the Python standard library, no randomness, and hence
no seed.  Repository base commit recorded by the cycle is
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

**REFUTED**

The refuted claim is the existence of a universal polynomial-congestion
comparison from the weighted leaf-replanting chain `Y_r` to the exact
leaf-rotation subchain `L_r`.  This verdict is not a global-goal verdict.
