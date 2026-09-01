# M244 DPS stack-pruning reduction

Date: 2026-08-14 UTC. Status: **proved colored-stack pruning; IDL remains
conditional on one exact metric-interface lemma**.

## 1. Source and convention lock

The primary source is E. Duchi, D. Poulalhon, and G. Schaeffer, *Uniform
random sampling of simple branched coverings of the sphere by itself*, SODA
2014, 294--304, DOI `10.1137/1.9781611973402.21`. The author-hosted PDF

```text
https://www.irif.fr/~poulalho/Articles/DuPoSc13.pdf
```

used here has SHA-256

```text
98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2.
```

Proposition 3 roots the Cayley tree at white `y_d`, inserts black `x_a` in
the first edge from `y_a` toward the root, and assigns two labels to the
halves. Lemma 2 proves that consecutive white/black half-edges in a valid
pre-map have the same label and are separated by one or three sides; Theorem
5 proves that the LIFO local closure is the inverse construction.

The paper displays `tau_m ... tau_1=id`. Reversing its factor list gives the
project's left-to-right product display. Equivalently, the accepted
plus-mirror implementation reverses the cyclic white/black rotations and
directly emits that project display. The intrinsic half-edge matching and
physical transpositions are unchanged. In this note white rotations increase,
black rotations decrease, exactly as in the accepted plus-mirror code.

There is no target distribution or Markov kernel here. The object is a
deterministic stack closure.

## 2. Literal contour excursion

Let `m=2r-2` be the current number of boundary labels. For a nonroot white
vertex `y_a`, let `x_a` be the inserted black vertex in its parent edge. Write

```text
L_a = label on x_a--y_a,
R_a = label on x_a--y_{p(a)}.                         (2.1)
```

For labels modulo `m`, `W_a(u up v)` is the increasing open interval of
white half-edges at `y_a` strictly after `u` and before `v`; `B_a(u down v)`
is the analogous decreasing open interval at `x_a`. Let `S^ell` denote a
traversal of an actual tree side carrying label `ell`.

Cut the contour immediately after it crosses from `y_{p(a)}` to `x_a` along
the `R_a` side, and stop after it returns across that side. Because this edge
is a bridge, the resulting word `E_a` is a literal contiguous interval of the
outer contour and contains exactly `x_b,y_b` for descendants `b` of `a`.

Let `c_1,...,c_k` be the children of `a` in the order in which their
parent-side labels `R_{c_j}` occur increasingly after `L_a`. With `q_0=L_a`
and `q_j=R_{c_j}`, direct application of the rotation rule gives

```text
E_a =
  B_a(R_a down L_a) S^L_a
  product_(j=1)^k [
      W_a(q_(j-1) up R_(c_j)) S^R_(c_j) E_(c_j)
  ]
  W_a(q_k up L_a) S^L_a
  B_a(L_a down R_a) S^R_a.                           (2.2)
```

Here `E_{c_j}` starts just after the displayed crossing into `x_{c_j}` and
includes the return crossing to `y_a`. Empty cyclic intervals contribute no
token. Formula (2.2) is the requested generic off-path-subtree factorization;
it is a restatement of the source contour rule, not a finite-rank pattern.

## 3. Excursion-pruning theorem

### Theorem 3.1 (canonical unedited one-open pruning; **PROVED**)

Assume every inserted black vertex in the descendant component of `a` is an
unedited canonical slot, so

```text
R_b=L_b+1 modulo m                                    (3.0)
```

for every descendant `b`, including `a`. Then there is a sequence of DPS
local closures wholly inside the contiguous contour interval `E_a` such
that:

1. every black half-edge in `E_a` is matched;
2. exactly one white half-edge remains, and its label is `R_a`;
3. no token outside `E_a` is changed;
4. after adjoining a formal black half-edge `B^R_a` immediately outside the
   excursion, the augmented half-edge projection is balanced and all its
   matches are internal.

This is exactly the case for a component of `T\P(v)`: the reversed slot
`x_v` lies on `P(v)` and is explicitly excluded. No assertion is made for
`E_v` or for an arbitrarily oriented pair of labels.

The theorem is about the colored LIFO stack. It does not yet determine how
many side tokens survive on either side of the residual `W^R_a`, hence it
does not determine whether a later real closure is at distance one or three.

#### Proof

Induct on the number of white vertices below `a`. Formula (2.2) is contiguous
because cutting a bridge separates the ordinary tree contour into one
interval.

For a leaf, (3.0) makes `B_a(R_a down L_a)` empty. Ignoring side tokens, the
half-edge projection is

```text
W_a(L_a up L_a)
B_a(L_a down R_a).                                  (3.1)
```

The middle increasing cycle contains exactly one token of every label except
`L_a`; the trailing decreasing black interval contains exactly one token of
every label except `L_a,R_a`. Since `R_a=L_a+1`, the white block begins with
`W_a^R_a`, followed by the other labels increasingly, while the black block
lists those other labels in reverse. LIFO cancellation stays inside `E_a`,
cancels every black token, and leaves the first token `W_a^R_a`.

For the induction step, first apply the theorem inside every child interval
`E_{c_j}`. Replace that interval in the half-edge projection by its sole
survivor `W^R_(c_j)`. The white gaps in (2.2), together with these child
survivors, now form

```text
one increasing white token of every label except L_a.       (3.2)
```

Indeed a label absent at `y_a` because it is the parent-side incidence of a
child is supplied exactly once by that child's survivor; every other absent
incidence is supplied by the displayed white gap. Again (3.0) makes the
leading black interval empty, while the trailing interval at `x_a` is

```text
one decreasing black token of every label except L_a,R_a.   (3.3)
```

The same nested cancellation as in (3.1) matches every token in (3.3) and
leaves only the initial `R_a` token from (3.2). Whenever a projected
white/black pair
becomes consecutive among half-edges, DPS Lemma 2 says the actual tokens have
the same label, are separated by one or three sides, and admit a legal local
closure. Hence every projected cancellation lifts to the actual pre-map.
All lifted closures lie between the two bridge cuts in (2.2), so no outside
token changes. Equivalently, the deleted tokens are a union of complete nodes
of the unique noncrossing LIFO rewrite-dependency forest: every node contains
both half-edge endpoints and the one-or-three side children it consumes.
Deleting these nodes bottom-up commutes with every retained rewrite. Finally
a formal `B^R_a` matches the unique survivor, proving the balanced augmented
statement. QED.

### Corollary 3.2 (exact compression of off-path data; **PROVED**)

After a fixed postorder pruning, a canonical unedited rooted off-path subtree
affects the remaining closure only through an interface

```text
I_a = (R_a, J_a^-, J_a^+),                           (3.4)
```

where `R_a` labels the sole white half-edge and `J_a^-,J_a^+` are the actual
side-token words left before and after it. Thus the full internal colored
half-edge word can be discarded. The side words cannot be discarded merely
from the color count.

This corrects the tempting but false phrase “balanced subtree”: `E_a` has
white-minus-black excess one. It is its augmentation by the virtual closing
black token that is balanced.

## 4. Exact remaining metric-interface lemma

Theorem 3.1 resolves colored matching but not the distance-one versus
distance-three choice which records the second black endpoint of a factor.
That metric distinction is exactly what IDL needs. The first unproved step is
therefore the following standalone statement.

> **RANK-STABLE METRIC INTERFACE LEMMA (RSMI).** Fix `d>=5`, a tree `T` on
> `[d]` rooted at leaf `d` with `{1,d}`, an ordinary edited slot
> `i=2v-3`, and the canonical orders `s_i pi_d,s_i pi_(d+1)`. Prune every
> component of `T\P(v)` by Theorem 3.1 in the same rooted postorder at old
> rank `d` and after adjoining `{1,d+1}`. Then the surviving interfaces
> `(R_a,J_a^-,J_a^+)` have the following exact rank-stability:
>
> 1. For each canonical unedited `E_a`, let `D_a^(d)` and `D_a^(d+1)` be
>    the complete noncrossing rewrite-dependency nodes deleted by Theorem 3.1
>    at the two ranks. Delete them bottom-up. Whenever retained old-label
>    tokens `W^ell,B^ell` next become consecutive half-edges, the number of
>    retained side tokens between them is the same at both ranks and belongs
>    to `{1,3}`. In the distance-three case, `B^ell` names the same black
>    endpoint. This applies to every off-path component not rooted at a
>    larger direct child `a>v,p(a)=v`.
> 2. for a larger direct child `a>v,p(a)=v`, precisely its two slot labels
>    close at distance three against old final black `x_d` at rank `d` and
>    new final black `x_(d+1)` at rank `d+1`; every other closure contributed
>    by that component obeys the retained-pair rule in item 1;
> 3. after these interfaces are substituted into the stopped-path contour,
>    a strict descent transmits the single open interface, while a path
>    vertex greater than `v` or an internal ascent absorbs it; at the root
>    the transmitted interface has exactly the four side distances and black
>    endpoints displayed in `(IDL-d)`.

Every off-path slot in this statement has the literal plus-mirror canonical
ordering `L_a=2a-3,R_a=2a-2`, hence `R_a=L_a+1`. The sole reversed slot has
`a=v`; it is retained on `P(v)` and never passed to Theorem 3.1. All side
counts refer to the actual `S` tokens in (2.2), after deleting complete
rewrite nodes rather than deleting a bare color projection.

RSMI is narrower than rerunning the global DPS closure: Theorem 3.1 has
already eliminated every internal colored half-edge of every off-path
subtree. Its inputs are only the one-open interfaces (3.4) and the stopped
path. It is also directly falsifiable: a counterexample is one subtree, one
old label, and its first differing `1/3` distance or black endpoint.

## 5. Conditional implication to M240 IDL

### Proposition 5.1 (**PROVED CONDITIONAL ON RSMI**)

RSMI implies all of M240's IDL, including the closed equality and
`(IDL-a)--(IDL-d)`.

#### Proof

Prune all off-path components. If the stopped path contains a vertex greater
than `v` or an internal ascent, RSMI(3) absorbs the only open interface.
RSMI(1) then makes all old-label distance-three endpoints equal at the two
ranks, while the canonical root extension supplies the same final doubled
`(0,d)` pair as the naive word. Hence `N=A`.

If the path is strictly decreasing, the interface reaches the root. Its first
exposed edited face gives `(x,y)` versus `(x,n)` at position `2v-2`, which is
`IDL-a`. RSMI(2) gives the two copies `(a-1,y)^2` versus `(a-1,n)^2` for every
larger direct child, which is `IDL-b`. RSMI(1) gives literal equality for
every other pruned component; because a nonchild parent edge avoids
`{v,d,d+1}`, its physical factor is disjoint from `{x,y,n}`, giving `IDL-c`.
Finally RSMI(3) is exactly the root four-block `IDL-d`. The pruning theorem
and the path/root cases exhaust the contour, so every unnamed coordinate is
literal equal. QED.

This proposition preserves M242 objection `N-1`: it never invokes the false
generic `(R^-1)^2` identity.

## 6. Tiny falsifier and strict scope

Only after the recurrence was fixed, `idl_falsifier.py` independently
implemented Proposition 3 and the LIFO closure and tested the complete
allowed calibration ranks:

```text
d=5: 16 trees, 48 ordinary rows, 34 open, 14 closed, 0 failures
d=6: 125 trees, 500 ordinary rows, 307 open, 193 closed, 0 failures.
```

The 548-row digest is

```text
c6f62a955055cbf998e8119acc7dfb7ff1cebfb006fdd7b4c5c5696465f4383c.
```

This is exact finite calibration and does not prove RSMI or IDL.

Final status:

```text
PROVED: literal excursion factorization; one-open colored-stack pruning;
        exact compression to one residual white interface; RSMI => IDL.
UNRESOLVED: RSMI's side-distance/black-endpoint rank stability.
NOT CLAIMED: unconditional IDL or Z2 closure; fixed-edit closure;
             every-color/voltage/length/gap/mixing/Terminal consequences.
```
