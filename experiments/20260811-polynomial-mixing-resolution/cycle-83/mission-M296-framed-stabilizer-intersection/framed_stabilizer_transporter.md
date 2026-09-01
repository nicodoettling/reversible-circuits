# M296 chart-stabilizer transporter and double-coset reduction

Date: 2026-08-14 UTC. Status: **proved exact group-action reduction and
explicit stabilizer structure; polynomial cover remains unresolved**.

## 1. Scope and conventions

For `d>=6`, put `m=2d-2` and

```text
Z_d={w in Transpositions(S_d)^m:
       product(w)=id, support(w) connected}.
```

Permutations compose as `(pq)(x)=p(q(x))`. The chronological signed
right-Hurwitz generators are

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

Write `x;y` for first applying `x`, then `y`, and write `w^x` for the
result. Thus `w^(x;y)=(w^x)^y`. Let

```text
Gamma=B_m,
c=c_d=(1,2)^2(1,3)^2...(1,d)^2,
S=BStab_d={s in Gamma:c^s=c}.                         (1.1)
```

Here `Gamma` and `S` contain literal braid-group elements. They are not the
finite action image, the global relabeling group `G=S_d`, the root
stabilizer `H=Stab_G(d)`, or sets of raw spellings. Length is shortest
signed-generator length unless a displayed representative is explicitly
used.

This note studies only deterministic routing in `Z_d`. It proves no
every-color schedule, voltage correction, congestion, gap, mixing, or
Terminal statement.

## 2. Accepted inputs

The 60 payload rows in M112/M119, M135/M137, M284/M288, and M291/M294 pass
their frozen checksums. M13's two pre-freeze proof hashes also reproduce.
The exact digests and semantic scopes are recorded in
`dependency_audit.md`.

The inputs used in the proof are:

1. M13's constructive bound: every `x in Z_d` has a signed braid route to
   `c` of length at most

   ```text
   L_d=50d(2d-2)^3.                                   (2.1)
   ```

2. M112/M119's exact count

   ```text
   |Z_d|=d^(d-3)(2d-2)!.                              (2.2)
   ```

3. M135/M137's actual `H`-orbit edges selected by an arbitrary
   perfect-matching color.
4. M291/M294's short source and target frames for each selected edge `Q`:

   ```text
   u_Q^alpha_Q=c,       v_Q^delta_Q=c,
   |alpha_Q|,|delta_Q|<=L_d,                          (2.3)
   F_Q={beta:u_Q^beta=v_Q}
      =alpha_Q;S;delta_Q^(-1).                        (2.4)
   ```

M284/M288 is only a type/scope gate. Its rank lift begins after a true
common base schedule exists.

## 3. Concrete structure inside the doubled-star stabilizer

Put `n=d-1`, and write

```text
e_r=(1,r+1),       1<=r<=n,
c=e_1,e_1,e_2,e_2,...,e_n,e_n.                       (3.1)
```

Let `sigma_j=R_j` as an element of `Gamma`.

### Lemma 3.1 (short local chart loops; **PROVED**)

The following braid elements lie in `S`:

```text
sigma_(2r-1),                1<=r<=n,                 (3.2)
sigma_(2r)^3,                1<=r<n.                  (3.3)
```

For `1<=r<n`, also put

```text
q_r=sigma_(2r);sigma_(2r-1);sigma_(2r+1);sigma_(2r).
                                                               (3.4)
```

Then `q_r` exchanges the adjacent square blocks `e_r^2,e_(r+1)^2`, and

```text
q_r^2 in S,        |q_r^2|<=8.                       (3.5)
```

In contrast, `q_r` itself does not fix the literal chart: it maps `c` to
the global conjugate obtained by swapping leaves `r+1,r+2`. Thus a
global-orbit stabilizer must not be substituted for `S`.

#### Proof

For an involution `a`,

```text
R(a,a)=(a,a),
```

which proves (3.2). If distinct transpositions `a,b` share one endpoint and
`z=bab`, then

```text
(a,b) --R--> (b,z) --R--> (z,a) --R--> (a,b).         (3.6)
```

Every boundary pair `e_r,e_(r+1)` in (3.1) has this form, proving (3.3).
For arbitrary involutions `a,b`, direct application of the four letters in
(3.4) gives

```text
(a,a,b,b)
 ->(a,b,bab,b)
 ->(b,bab,bab,b)
 ->(b,bab,b,a)
 ->(b,b,a,a).                                         (3.7)
```

Applying the same block exchange once more returns `(a,a,b,b)`, proving
(3.5). For the chart, swapping the blocks is exactly global conjugation by
the leaf transposition `(r+1,r+2)`, but the two displayed literal words are
different. QED.

The elements (3.2)--(3.5) are an explicit short subgroup of `S`; no claim
that they generate all of `S` is made.

### Theorem 3.2 (complete short Schreier inventory; **PROVED**)

For every `x in Z_d`, choose a braid `t_x` such that

```text
c^t_x=x,       |t_x|<=L_d,       t_c=1.              (3.8)
```

For `epsilon in {+1,-1}`, `1<=j<m`, and
`y=x^(sigma_j^epsilon)`, define

```text
h_(x,j,epsilon)=t_x;sigma_j^epsilon;t_y^(-1).         (3.9)
```

Then all elements in (3.9) fix `c`, they generate the full literal subgroup
`S`, and every displayed generator has length at most

```text
2L_d+1=100d(2d-2)^3+1.                               (3.10)
```

There are at most

```text
2(m-1)|Z_d|=2(2d-3)d^(d-3)(2d-2)!                   (3.11)
```

rows in this inventory.

#### Proof

Equation (3.9) follows the state path `c -> x -> y -> c`, so every row is
in `S`, and (3.10) follows from (2.1). Let
`s=g_1;...;g_k in S` be any signed-generator spelling and put
`x_i=c^(g_1;...;g_i)`, with `x_0=x_k=c`. Then the literal braid identity

```text
s=product_(i=1)^k
   (t_(x_(i-1));g_i;t_(x_i)^(-1))                    (3.12)
```

is obtained by cancelling consecutive `t_(x_i)^(-1);t_(x_i)`. Every factor
is a row of (3.9), proving generation. Equations (2.2) and the `2(m-1)`
signed transitions per state give (3.11). QED.

Theorem 3.2 gives polynomial-length generators in an inventory indexed by an
exponentially large state set (duplicate or identity rows are allowed). It
proves neither a polynomial-size generating family nor polynomial diameter
for any `S`-orbit or transporter.

## 4. Exact residualization at one reference edge

Let `I` be any finite family of actual matching-selected `H`-orbit edges,
and fix `Q_0 in I`. Abbreviate its frames by `alpha_0,delta_0`. For every
`Q in I`, define

```text
L_Q=alpha_Q^(-1);alpha_0,
R_Q=delta_0^(-1);delta_Q,                             (4.1)
x_Q=c^(L_Q),
y_Q=c^(R_Q^(-1)),                                    (4.2)
C_Q={s in S:L_Q;s;R_Q in S}.                         (4.3)
```

For the reference edge, `L_0=R_0=1` and `C_0=S`.

### Theorem 4.1 (chart-stabilizer tuple transporter; **PROVED**)

For every `Q`,

```text
C_Q={s in S:x_Q^s=y_Q}=Trans_S(x_Q,y_Q).             (4.4)
```

Moreover the complete common endpoint fiber is

```text
intersection_(Q in I) F_Q
 =alpha_0 ; (intersection_(Q in I) C_Q) ; delta_0^(-1).
                                                               (4.5)
```

Equivalently, after omitting the trivial reference coordinate,
`intersection_Q C_Q` is the transporter under the diagonal `S` action from
the tuple `(x_Q)` to the tuple `(y_Q)`.

#### Proof

Every element of `F_(Q_0)` has a unique expression

```text
beta=alpha_0;s;delta_0^(-1),       s in S.            (4.6)
```

For another edge, (2.4) gives

```text
beta in F_Q
iff alpha_Q^(-1);beta;delta_Q in S
iff L_Q;s;R_Q in S
iff c^(L_Q;s;R_Q)=c.                                  (4.7)
```

Applying `R_Q^(-1)` to the final equality in (4.7) is equivalent to
`(c^L_Q)^s=c^(R_Q^(-1))`, proving (4.4). Imposing (4.7) for every `Q`
inside the unique parameterization (4.6) proves (4.5). QED.

This theorem uses both endpoint frames. It is not the one-sided
chart-prefix cover refuted by M291/M294.

## 5. Double-coset compatibility and two-point stabilizers

### Corollary 5.1 (exact pairwise test; **PROVED**)

For every `Q`, the following are equivalent:

1. `F_(Q_0) intersect F_Q` is nonempty;
2. `C_Q` is nonempty;
3. `x_Q,y_Q` lie in the same `S`-orbit;
4. the literal double cosets satisfy

   ```text
   S;L_Q;S = S;R_Q^(-1);S.                            (5.1)
   ```

For two arbitrary edges `P,Q`, this becomes the intrinsic criterion

```text
F_P intersect F_Q != empty
iff
S;alpha_Q^(-1);alpha_P;S
 =S;delta_Q^(-1);delta_P;S.                           (5.2)
```

#### Proof

The first three equivalences follow from Theorem 4.1. Double cosets
`S\Gamma/S` are in bijection with `S`-orbits on `Z_d` by

```text
S;g;S  ->  {c^(g;s):s in S}.                          (5.3)
```

Indeed left multiplication does not move `c`, and right multiplication
moves within the displayed orbit. Applying (5.3) to `L_Q,R_Q^(-1)` proves
(5.1). Repeating with `P` as the reference gives (5.2). QED.

### Corollary 5.2 (cosets of two-point stabilizers; **PROVED**)

Suppose `C_Q` is nonempty and choose `s_Q in C_Q`. Then

```text
C_Q=Stab_S(x_Q);s_Q
   =s_Q;Stab_S(y_Q),                                  (5.4)

Stab_S(x_Q)=S intersect L_Q^(-1);S;L_Q,
Stab_S(y_Q)=S intersect R_Q;S;R_Q^(-1).               (5.5)
```

Thus the unresolved higher-arity condition is literally an intersection of
cosets of varying two-point stabilizers inside `S`:

```text
intersection_(Q in I)
 s_Q;(S intersect R_Q;S;R_Q^(-1)) != empty.           (5.6)
```

#### Proof

For a right action, any transporter from `x` to `y` is a left coset of the
source stabilizer and a right coset of the target stabilizer. Also

```text
Stab_Gamma(c^g)=g^(-1);S;g.                           (5.7)
```

Intersect (5.7) with `S`, first with `g=L_Q` and then with
`g=R_Q^(-1)`, to obtain (5.4)--(5.5). Equation (5.6) is Theorem 4.1. QED.

Pairwise equality (5.1) does not by itself prove (5.6): the subgroups in
(5.6) vary with `Q`. No Helly property for these actual stabilizer cosets is
proved here.

## 6. Frame changes, finite actions, and length

### Proposition 6.1 (frame covariance; **PROVED**)

Replace frames by

```text
alpha_Q'=alpha_Q;u_Q,       delta_Q'=delta_Q;v_Q,
u_Q,v_Q in S.                                       (6.1)
```

If `C_Q'` is formed using the new frames and the same reference edge, then

```text
C_Q'=u_0^(-1);C_Q;v_0.                               (6.2)
```

In particular, nonreference frame changes cancel completely, while a
reference-frame change applies one common two-sided translate to every
constraint. Hence (4.5), (5.1), and common nonemptiness are intrinsic.

#### Proof

The new relative elements are

```text
L_Q'=u_Q^(-1);L_Q;u_0,
R_Q'=v_0^(-1);R_Q;v_Q.
```

Since all `u_Q,v_Q` lie in `S`, the condition
`L_Q';s';R_Q' in S` is equivalent to
`L_Q;(u_0;s';v_0^(-1));R_Q in S`, which is exactly (6.2). QED.

### Proposition 6.2 (finite-action nonemptiness; **PROVED**)

Let `p:Gamma->A_d` be the finite action image on `Z_d`, and let
`Sbar=Stab_(A_d)(c)`. Then

```text
S=p^(-1)(Sbar),       p(S)=Sbar.                     (6.3)
```

Projecting (4.3)--(4.5) to `A_d` preserves every common-nonemptiness
predicate exactly. In particular, the pairwise double-coset test may be
performed as a point-stabilizer orbit test in the finite action. Projection
does not preserve shortest literal braid length.

#### Proof

A braid lies in the preimage of `Sbar` exactly when its action fixes `c`,
which is the definition of `S`. Conversely every action fixing `c` has a
braid lift, and every such lift fixes `c`. Each `C_Q` is therefore the full
preimage of its finite transporter. A common finite stabilizer action has one
braid lift lying in every literal transporter. QED.

### Proposition 6.3 (polynomial length is exactly retained; **PROVED**)

With the short reference frames (2.3), a common braid `beta` and its unique
residual parameter `s=alpha_0^(-1);beta;delta_0` satisfy

```text
|beta| <= 2L_d+|s|,
|s|    <= 2L_d+|beta|.                               (6.4)
```

Consequently the common endpoint intersection contains a `d^O(1)`-length
literal braid if and only if the residual transporter intersection contains
a `d^O(1)`-length literal element of `S`.

#### Proof

Use (4.6), its inverse expression for `s`, the triangle inequality for
signed-generator length, and (2.3). QED.

## 7. The sharpened first open lemma

For a fixed M135 matching color, define its **chart-stabilizer
incompatibility graph** to have the selected `H`-orbit edges as vertices and
an edge between `P,Q` exactly when the equivalent conditions in (5.2) fail.
This graph is intrinsic despite the displayed frames.

The pairwise graph is an exact necessary diagnostic, but pairwise coloring is
not promoted as a sufficient intermediate theorem. M135/M137's conflict
coloring does not even settle this diagnostic: equality of aligned generated
subgroups is only a necessary Hurwitz invariant, whereas (5.2) is exact
two-source simultaneous realizability.

The first complete standalone obligation is:

> **STAR-STABILIZER TRANSPORTER INTERSECTION AND DIAMETER (SSTID).** There is
> a universal `C` such that, uniformly for `d>=6`, every actual M135
> perfect-matching color can be covered by at most `d^C` subfamilies `I`.
> For each `I`, after choosing a reference `Q_0 in I` and the short frames
> (2.3), the higher-arity transporter-coset intersection
> ```text
> T_I=intersection_(Q in I) C_Q
> ```
> is nonempty and contains a literal `s in S` of signed-generator length at
> most `d^C`.

By Theorem 4.1 and Proposition 6.3, SSTID is exactly the M291/M294
framed-stabilizer common-intersection theorem with its polynomial
representative-diameter bound. It includes the pairwise double-coset tests
and the higher-arity intersection in one correctly sufficient statement.
M284/M288 can be invoked only after this interface is closed.

The explicit loops in Section 3 do not prove SSTID. The complete Schreier
inventory has polynomial-length rows but an exponentially indexed list, and
it supplies no polynomial orbit diameter, coset-Helly property, or matching
cover. No common-prefix paired-chart strategy is used.

## 8. Boundary and scope

The reduction is stated for `d>=6`, matching M291/M294's accepted chart
scope. The group identities themselves apply whenever the sector and frames
are defined. No `d=5` or `d=6` guard is needed because every formula is an
exact action identity; no finite trend is used.

No every-color common schedule, arbitrary-product route, voltage correction,
congestion, spectral gap, mixing-time bound, or Terminal outcome is proved
or refuted.
