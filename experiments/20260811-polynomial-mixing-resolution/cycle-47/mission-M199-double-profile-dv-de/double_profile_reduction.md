# M199 exact literal double-profile reduction

Date: 2026-08-13 UTC.

Status: Propositions 1--2 below are **proved**. The interval-kernel boundary
edit lemma `(IKBE)`, hence `(DV)`, `(DE)`, the conditional `J=2` prefix
estimate, and every downstream claim remain **unresolved**.

## 1. Setting and notation

Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, `n=3k` with odd
`k>=3`, and M192/M195's immutable disjoint ordered-double laws
`Phi_s^D,Psi_s^D`. Put
```text
b_d=e^-d d^(d-1)/d!,
R_*=2k-3,
K_*(r,d)=b_d b_(r-d)/(R_* b_r),        1<=d<r.       (1.1)
```
Here `R_*` is the **total exterior rank remaining after the first edge**.
It is `2k-3`, not the initial rank `2k-2` and not the post-second rank
`2k-4`. The second-edge per-placement completion ratio in a post-first
component of size `r` is exactly `K_*(r,d)`. Summed over every post-first
component and every internal second edge, these ratios have total one.

Let
```text
V=(v_0,...,v_(D-1))
 =(1,...,k-1,2k,...,3k-1),             D=2k-1.       (1.2)
```
Indices of `V` are cyclic. Define the directed ambient face indicator
```text
I_l(i,x)=1{2 <= (v_(i+x)-v_i mod n) <= l}.           (1.3)
```
For an A-side contiguous `k`-block use
```text
J_l(x)=(k-x)/k * 1{2<=x<=l}.                         (1.4)
```
All indicator formulas below count multiplicity: if two component sizes
coincide, both indicators are added.

For exterior transpositions `e,f`, let `chi_l^X(e,f)` and `chi_l^Y(e,f)`
be the literal values of `X_l,Y_l` on the three cycles of `(ef)^-1 h`.
This is an explicit finite indicator: compute the three cycle supports, count
their cyclic ambient runs, and then apply the cutoff. It retains equal-size
components with multiplicity.

## 2. Exact B one-run profile

Fix a first directed B arc of size `r` beginning at `v_i`, with the other
first piece of size `z=D-r`. A disjoint second chord internal to that piece
has directed subarc size `d` and starting offset
```text
1<=a<=r-d-1.                                         (2.1)
```
The three source pieces are the first complementary piece `z` and the two
subpieces `d,r-d`. Under the ambient long-cycle embedding, the two one-run
faces are precisely the directed gaps
```text
A(i+r,z)=(v_i-v_(i+r) mod n),
A(i+a,d)=(v_(i+a+d)-v_(i+a) mod n).                 (2.2)
```
The remaining face has size `n-A(i+r,z)-A(i+a,d)` and has two runs. This
classification is literal for same-run and cross-run first or second edges.

For a prefix cutoff `l`, define
```text
H_l(i;r,d,a)=I_l(i+r,z)+I_l(i+a,d).                 (2.3)
```

### Proposition 1 (proved: literal B formula)

For `Z=Y_l`,
```text
Phi_s^D(Y_l)
 = 1/[1-gamma_L(s)] * 1/D
   * sum_(i=0)^(D-1) sum_(r in {s,D-s})
       sum_(d=1)^(r-1) K_*(r,d)
       sum_(a=1)^(r-d-1) H_l(i;r,d,a).               (B-Y)
```
Empty inner sums are zero. For `Z=X_l`, replace `H_l` by
```text
H_l(i;r,d,a)
 +1{2 <= n-A(i+r,D-r)-A(i+a,d) <= l},               (B-X)
```
where `A(i,x)=(v_(i+x)-v_i mod n)`.

#### Proof

Condition on a directed representative of the unoriented first chord. For a
fixed smaller split `s`, the two orientations produce `r=s,D-s`, and the
first-chord position is uniform over the `D` starts. Within a marked piece
of length `r`, exactly the offsets (2.1) avoid both first endpoints. The
minimal-factorization completion formula gives each such second edge mass
`K_*(r,d)`. The total disjoint mass conditioned on `s` is
`1-gamma_L(s)`, so division normalizes the literal double law.

Cutting the ambient long cycle by two disjoint chords gives two one-run faces
with the directed gaps (2.2); the third component is the complementary
two-run face. Thus (B-Y) and (B-X) count all three components with their
ambient run types and multiplicities. No kind, color, unit-gap, or collision
stratum is removed. QED.

Averaging (2.3) over `i` removes the placement offset:
```text
F_l(x)=D^-1 sum_i I_l(i,x),
Phi_s^D(Y_l)
 = [sum_(r in {s,D-s}) sum_(d<r)
      (r-d-1)K_*(r,d)(F_l(D-r)+F_l(d))]
   /[1-gamma_L(s)].                                  (2.4)
```
The two-seam word (1.2) gives the closed incidence law. For `1<=x<k`,
```text
#A=x: D-2x,              #A=x+1: x,      #A=x+k: x. (2.5a)
```
For `k<=x<D`, put `c=D-x`; then
```text
#A=n-c: D-2c,            #A=n-c-1: c,    #A=n-c-k: c. (2.5b)
```
Hence every `F_l(x)` is an explicit three-term piecewise-linear function.

## 3. Exact A one-run profile

On the A side the first edge cuts one exterior `k`-cycle into marked pieces
`s,k-s`; the second exterior `k`-cycle is untouched. The same marked-piece
kernel uses `R_*=2k-3`. A second edge in the untouched cycle has total mass
```text
u_k=(k-1)/(2k-3),                                    (3.1)
```
and its directed face law is (1.4). Put
```text
h_*(r)=(r-1)(r-2)/(rR_*).                              (3.2)
```
This is the total nonincident second-edge mass inside a marked size-`r`
piece.

### Proposition 2 (proved: literal A formula)


Let `E_A(s)` be the `2k` first exterior chords of smaller split `s` in the
two A-side `k`-cycles. For `e in E_A(s)`, let `D(e)` be all internal
second chords after `e` that avoid both endpoints of `e`. Let `r_e(f)` be
the size of the post-first component containing `f`, and let `d_e(f)` be
either post-second child size (the kernel is symmetric). For
`Z in {X_l,Y_l}` the complete literal law is
```text
Psi_s^D(Z)=1/[2k(1-gamma_F(s))]
 * sum_(e in E_A(s)) sum_(f in D(e))
      K_*(r_e(f),d_e(f)) chi_l^Z(e,f).               (A-full)
```
This formula is also the definition of the complementary two-run indicator
used below; it leaves no orientation choice implicit.

Let
```text
C_l=sum_(d=1)^(k-1)(k-d)K_*(k,d) 1{2<=d<=l}.        (3.3)
```
Then
```text
Psi_s^D(Y_l)=1/[1-gamma_F(s)] * {
  h_*(s)J_l(k-s)+h_*(k-s)J_l(s)
 +sum_(r in {s,k-s}) sum_(d=1)^(r-1)
      (r-d-1)K_*(r,d)J_l(d)
 +u_k[J_l(s)+J_l(k-s)] + C_l }.                      (A-Y)
```
For `X_l`, use `(A-full)`; equivalently add its literal complementary
two-run indicator before each marked/untouched placement is averaged.

#### Proof

If the second edge lies in a marked piece of size `r`, its two one-run
faces are the untouched first piece and the new subpiece; summing the first
over all nonincident internal second edges gives (3.2), and summing the second
gives the marked kernel in (A-Y). If the second edge lies in the untouched
cycle, both first pieces survive as one-run faces and the new face has the
usual contiguous chord law, giving (3.1) and (3.3). The third component is
the complementary two-run face. Division by `1-gamma_F(s)` conditions on
disjointness. These cases partition every ordered disjoint pair. QED.

## 4. Exact deletion/merge interpretation

Changing `s` to `s+1` transfers one source boundary point from the long
marked interval `D-s` to the short marked interval `s`. The tuples
`(i,r,d,a)` identify every interior second-chord placement. Under this
identification the exact signed edit has four parts:

1. added placements at the new short-interval boundary;
2. deleted placements at the old long-interval boundary;
3. the Radon--Nikodym edit of `K_*(r,d)` and of the seam indicator when the
   parent endpoint moves by one; and
4. the scalar normalization edit from `[1-gamma_L(s)]^-1` to
   `[1-gamma_L(s+1)]^-1`.

The literal indicator `chi_l^Z` travels with each paired tuple, including
its same/cross kind and any repeated-size collision. Thus this is a signed
deletion/merge map before estimation, not a total-variation split over
kinds. Formulas `(A-full)` and `(A-Y)` give the A/B embedding map: replace
the two-seam exterior word by two contiguous cycles and expose the exact
untouched-cycle term (3.3).

## 5. First open analytic certificate

The exact formulas reduce both M192 lemmas to the following standalone
estimate.

> **INTERVAL-KERNEL BOUNDARY EDIT `(IKBE)` (unresolved).** Let
> `Z_l^B(s)=Phi_s^D(Z)` from `(B-Y)/(B-X)` and
> `Z_l^A(s)=Psi_s^D(Z)` from `(A-full)/(A-Y)`, for `Z=X_l` or `Y_l`.
> Uniformly in odd `k>=3`,
> `2<=l<=(3k-1)/2`,
> ```text
> sum_(s=1)^(k-2)sqrt(s)|Z_l^B(s+1)-Z_l^B(s)|
>      <= C sqrt(l),                                  (IKBE-a)
>
> |Z_l^B(s)-Z_l^A(s)| <= C sqrt(l)/k,
>                  1<=s<k/2.                          (IKBE-b)
> ```

`(IKBE-a)` is exactly `(DV)`. The stronger pointwise `(IKBE-b)` implies
`(DE)` because `sum_s q_hat_s<=1`. Unlike the original abstract profile
lemmas, `(IKBE)` is a finite explicit interval-kernel inequality: its only
ingredients are the Borel kernel (1.1), the three seam incidences (2.5), the
boundary placements (2.1), and the smooth gamma normalizers.

A proof may split the *boundary-edit terms of the same combined formula*
after the literal pairing. It may not separately take absolute values of
unpaired double colors or collision strata. Standard Borel estimates
```text
K_*(r,d)<=C b_min(d,r-d)/R_*,
sum_(d<r)(r-d-1)K_*(r,d)=h_*(r)<=r/R_*,
|gamma_L(s+1)-gamma_L(s)|<=C/(k s^2)
```
show that the normalization edit is summable. What remains unproved is the
uniform combined boundary/seam/kernel edit in `(IKBE-a)` and the cancellation
between the two-seam, marked-piece, and untouched-cycle terms in
`(IKBE-b)`.

Thus M199 supplies a strict literal coefficient reduction but does not prove
`(DV)` or `(DE)`.
