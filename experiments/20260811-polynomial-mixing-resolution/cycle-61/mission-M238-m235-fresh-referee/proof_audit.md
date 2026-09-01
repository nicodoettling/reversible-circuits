# M238 clean-room proof audit of immutable M235

Date: 2026-08-13 UTC.

Verdict: **ACCEPT**.  M235 proves the signed two-run coefficient moment
`(TCM)` with universal constant `160` on its complete stated domain.  This
audit proves no YCM, WBE, DE, conditional J2, downstream response, spectral
gap, mixing bound, or Terminal.

## 1. Immutable gate and accepted interface

All seven files in M235 passed its frozen `SHA256SUMS`; that checksum file has
digest

```text
7e929497029ae0c007d0544d30f0ad3c0198947ce55f946ee7eb0aaa88b19527.
```

Every inventory cited by M235 also passed, with checksum-file digests exactly
matching its manifest: M192/M195, M199/M207, M211/M215, M217/M222, and
M226/M229.  No frozen file was edited.

Use `(pq)(x)=p(q(x))`, odd `k>=3`, and

```text
D=2k-1, R=2k-3, j=(k-1)/2,
b_r=e^(-r)r^(r-1)/r!,
K_R(r,d)=b_d b_(r-d)/(R b_r),
q_s=[k/(k-1)]b_s b_(k-s)/b_k, 1<=s<=j.
```

Oddness makes the half-convolution exact, so `sum_s q_s=1`.  Accepted
M226/M229 supplies the exact signed interface

```text
sum_(y=2)^ell c^T_(k,y)=T_B(k,ell)-T_A(k,ell),       (1.1)
```

where `T_B,T_A` are raw, not conditionally renormalized, q-averaged masses of
the unique two-run face and preserve ordered-tuple and equal-size
multiplicity.  Thus it remains only to audit M235's positive bounds for these
two literal laws.

## 2. B raw normalization and both parent orientations

Write

```text
V=(1,...,k-1,2k,...,3k-1).
```

For a fixed smaller first split `s`, there are exactly `D` unoriented first
chords.  Once its cyclic start `i` is fixed, the two post-first parents have
sizes `r=s` and `r=D-s`.  If the second chord cuts a directed middle child of
length `d`, put `t=r-d`.  Avoiding both first endpoints leaves exactly

```text
a=1,...,r-d-1=t-1
```

second-chord placements.  The two `r` branches identify which post-first
parent contains the second edge; they are not two orientations of the same
ordered pair.  Hence every literal ordered disjoint pair occurs exactly once,
and the first-edge normalization is `1/D`, not `1/(2D)`.  Its per-placement
completion weight is `K_R(r,d)`.  This independently gives

```text
T_B(k,ell)=sum_(s=1)^j q_s (1/D)sum_(i=0)^(D-1)
 sum_(r in {s,D-s}) sum_(d=1)^(r-1)K_R(r,d)
 sum_(a=1)^(r-d-1)1{2<=y_B(i;r,d,a)<=ell}.          (2.1)
```

The clean-room enumeration confirms the count identity before weights: for
each `s`, the number of records is

```text
D sum_(r in {s,D-s}) sum_(t=2)^(r-1)(t-1).
```

## 3. Simultaneous B seams and placement bound

The directed increments of `V` around the ambient `3k`-cycle are `1` except
at two edges.  The large seam has increment `k+1`, hence excess `k`; the
small seam has increment `2`, hence excess `1`.

For a tuple `(i,r,d,a)`, the two-run face is the union of retained source
edge arcs

```text
E=[i,i+a) union [i+a+d,i+r).
```

It has exactly `t=r-d` edges.  Summing their ambient increments gives, with
no exclusion of a simultaneous seam hit,

```text
y_B=t+k 1{beta in E}+1{sigma in E}.                 (3.1)
```

Translation of `i` through all `D` starts puts either fixed seam in `E`
exactly `t` times, regardless of the separation of the two arcs.  If
`t>ell`, no start qualifies.  If `t>ell-k`, a qualifying start must exclude
the large seam.  Therefore, for every fixed `(r,d,a)`,

```text
(1/D)sum_i 1{y_B<=ell}
 <=1{t<=ell-k}+[(D-t)/D]1{t<=ell}.                  (3.2)
```

The first term can make the right side exceed one; it is an upper bound, not
a claimed probability decomposition.  Summing the `t-1` placements and
using `K_R(r,d)=K_R(r,t)` gives exactly M235 (3.6).

## 4. Borel facts and split-weight bounds

The Stirling bounds used by M235 imply

```text
e^(-1)r^(-3/2)<=b_r<=(2pi)^(-1/2)r^(-3/2),
b_u/b_v<4 whenever v/2<=u<=v.                       (4.1)
```

They also give

```text
M(L):=sum_(r<=L)r b_r<=sqrt(L).                     (4.2)
```

The rooted-tree convolution, with every index nonempty exactly when used, is

```text
sum_(u=1)^(m-1)b_u b_(m-u)=2(m-1)b_m/m<=2b_m.       (4.3)
```

Finally `sum_r b_r=1`, and for `s<=j`, (4.1) yields

```text
q_s/b_s
 <=(3/2)[e/sqrt(2pi)] 2^(3/2)<5,
sum_s q_s s<=5sqrt(k).                              (4.4)
```

Also `R>=k` and `D/R<=5/3`, including `k=3`.

## 5. Every B range and constant

For the short parent `r=s`, the brace from (3.2) is at most
`2 1{t<=ell}`.  Cancelling `b_s`, putting `u=s-t`, and extending the
nonnegative inner sum from `1<=u<=j-t` to the full convolution gives

```text
B_short
 <=(3/R)sum_(t<=ell)t b_t
   [sum_(u=1)^(k-t-1)b_u b_(k-t-u)/b_k].            (5.1)
```

Whenever this sum is nonempty, `t<s<=j`, so `m=k-t>k/2`.  Applying (4.3)
with exactly `m=k-t` and then (4.1) makes the bracket less than `8`.  Thus

```text
B_short<=24 M(ell)/R<=24sqrt(ell)/k.                (5.2)
```

For the long parent `r=D-s`, the first indicator in (3.2) has
`t<=ell-k<=j`, hence `t<=r/2`.  Therefore
`b_(r-t)/b_r<4`, and summing q gives

```text
B_long,free<=4sqrt(ell)/k.                          (5.3)
```

The second indicator with `t<=r/2` has the same ratio bound; dropping its
factor `(D-t)/D<=1` gives

```text
B_long,low<=4sqrt(ell)/k.                           (5.4)
```

For its remaining range `t>r/2`, and only for this long parent, put
`d=r-t`.  Since `r=D-s`, the exact identity is

```text
D-t=s+d.                                            (5.5)
```

Here `b_t/b_r<4`, `(t-1)/R<=D/R<=5/3`, and
`D>=5k/3`; in particular each summand is at most the looser M235 value

```text
7[(s+d)/k]b_d.                                      (5.6)
```

Extending `d<r/2<D/2<k`, (4.2), (4.4), and `sum b_d=1` give

```text
B_long,high<=(7/k)(5sqrt(k)+sqrt(k))=42/sqrt(k).    (5.7)
```

This range is nonempty only if

```text
ell>r/2>=(D-j)/2=(3k-1)/4>=2k/3,
```

where the last inequality is valid exactly for `k>=3`.  Hence (5.7) is at
most `42sqrt(3/2)sqrt(ell)/k<52sqrt(ell)/k`.  The four constants sum to

```text
T_B(k,ell)<=84sqrt(ell)/k.                          (5.8)
```

No use of (5.5) occurs in a short-parent or low-`t` range.

## 6. Exact A marked and untouched laws

There are two contiguous exterior `k`-cycles, each supplying `k` first
chords of split `s`.  Division by `2k` and summation over the two identical
blocks leaves one cyclic average.  For a marked parent
`r in {s,k-s}`, a retained set has `t` source edges and `t-1` second-edge
placements.  It contains the unique block seam at exactly `t` of the `k`
first starts.  Its two-run size is consequently `t` with mass `(k-t)/k`
and `t+2k` with mass `t/k`.  Because `ell<2k`, the marked prefix is exactly

```text
T_A^mark(k,ell)
 =sum_s q_s sum_(r in {s,k-s})
   sum_(t=2)^min(ell,r-1)
    (t-1)K_R(r,t)(k-t)/k.                           (6.1)
```

When the second edge is in the untouched block, the first one-run face is
`x=s` with mass `(k-s)/k` or `x=k-s` with mass `s/k`.  A second one-run
face of size `y` has raw coefficient `(k-y)K_R(k,y)`, and the complementary
two-run size is `3k-x-y`.

The `x=s` alternative cannot qualify: even at `y=k-1` its size is at least

```text
2k+1-s>=2k+1-j=(3k+3)/2>ell.                       (6.2)
```

For `x=k-s`, set `y=k-c`.  Then the raw coefficient is `cK_R(k,c)`, the
two-run size is `k+s+c`, and the exact qualifying range is
`1<=c<=ell-k-s`.  Thus M235 (5.3) is exact:

```text
T_A^unt(k,ell)
 =sum_s q_s(s/k)sum_(c=1)^(ell-k-s)cK_R(k,c),       (6.3)
```

with the conventional empty sum.  Both marked orientations, the untouched
kind, and equal-size multiplicities remain present.

## 7. Every A convolution range and constant

For the short marked parent `r=s`, the calculation in (5.1) loses the
factor two from the B placement brace.  The same full `m=k-t` convolution
therefore gives

```text
A_mark,short<=12sqrt(ell)/k.                        (7.1)
```

For `r=k-s`, put `u=k-t`.  Nonemptiness forces `t<=k-s-1`, so `u>=2`.
After cancelling `b_(k-s)`, the original `s` range is
`1<=s<=min(j,u-1)`.  Extending it to the complete convolution
`1<=s<=u-1` gives

```text
A_mark,long
 <=[2/((k-1)R)]sum_t (t-1)(u-1)b_t b_u/b_k
 <=(3/R)sum_t t b_t(u/k)b_u/b_k.                   (7.2)
```

The last inequality follows from
`2(t-1)(u-1)/(k-1)<=3tu/k`, valid for `k>=3`.

For `t<=k/2`, `b_u/b_k<4`, so (7.2) is at most
`12sqrt(ell)/k`.  For `t>k/2`, instead `b_t/b_k<4` and `t/R<=1`; summing
`u b_u` gives `12/sqrt(k)`.  This high range requires `ell>k/2`, so

```text
12/sqrt(k)<12sqrt(2)sqrt(ell)/k<17sqrt(ell)/k.      (7.3)
```

Together the marked contribution is at most `41sqrt(ell)/k`.

In (6.3), nonemptiness gives `c<=ell-k-s<=j`.  Hence
`b_(k-c)/b_k<4` and `K_R(k,c)<=4b_c/R`.  Extending the dependent c range
to `c<=j`, then using (4.2) and (4.4), gives

```text
T_A^unt
 <=(4/R)[sum_s q_s(s/k)][sum_(c<=j)c b_c]
 <=20/R<=20/k<=20sqrt(ell)/k.                       (7.4)
```

Therefore

```text
T_A(k,ell)<=61sqrt(ell)/k.                          (7.5)
```

## 8. Boundary case and clean-room falsification

At `k=3`, `R=k=3`, `D/R=5/3`, `q_1=1`, and every displayed inequality is
valid.  Both A prefixes are empty for all allowed `ell=2,3,4`; the B long
parent is handled by the same low/high split.  Thus no asymptotic threshold
or omitted smallest rank is hidden in the proof.

`cleanroom_tcm_referee.py` uses only the Python standard library and imports
no M235 code or data.  It:

- enumerates the literal ordered disjoint pairs by permutation composition;
- verifies the exact first-edge normalizers and placement counts;
- compares the complete B and A coefficient laws at `k=3,5,7`;
- derives B sizes once by ambient edge increments and once by simultaneous
  seam incidence;
- checks (3.2) for every tuple and cutoff (1,458 checks total);
- checks both Borel convolutions through `m=31`; and
- finite-falsifies every component constant at all 360 allowed `(k,ell)`
  pairs with odd `3<=k<=31`.

All checks pass.  The exact maximizing signed prefixes at `k=3,5,7` agree
with M235's frozen output.  These finite checks validate formulas and can
falsify claims; they are not used to prove the universal theorem.

## 9. Conclusion and numbered objections

The raw masses are nonnegative, so (5.8) and (7.5) give

```text
|T_B-T_A|<=T_B+T_A<=145sqrt(ell)/k
                     <=160sqrt(ell)/k.
```

Together with accepted identity (1.1), this proves exactly `(TCM)`.

1. **Material objections:** none.
2. **Nonmaterial objections:** none.

Final verdict: **ACCEPT M235 AS FROZEN.**  Keep YCM and every named
downstream obligation open.
