# M305 complementary-gap Borel divergence and exact stop

Date: 2026-08-14 UTC.

Status: the scalar complementary-gap coefficient lemma below is **proved
all-rank**.  The marked-profile estimate `(CMPAD)`, hence CBPV and SOCL, is
**unresolved**.  No downstream inference is made.

## 1. Exact coefficient interface

Put

```text
D=2k-1,       h=(k-1)/2,       b_j=e^(-j)j^(j-1)/j!,
R_m(q)=b_(m-q)/b_m,             R_m(0)=1.
```

M91's source-locked conditioned-Borel laws are

```text
p_s=[D/(D-1)] b_s R_D(s),       1<=s<=k-1,
q_s=[k/(k-1)] b_s R_k(s),       1<=s<=h,
q_s=0,                          h<s<=k-1.            (1.1)
```

Both are probability laws.  Write `a_s=p_s-q_s`, extend `a_0=a_k=0`, and
let `D_u=sum_(s<=u)a_s`.  The coefficient `a` is already the signed B/A
split coefficient.  The estimates below never norm B and A separately.
They are coefficient facts only; they are not estimates on an H, A, or C
response row.

## 2. Proved complementary-gap lemma

> **Lemma 1 (Borel ratio envelope).**  There is an absolute `C` such that,
> for `m>=2` and `0<=q<=floor(m/2)`,
>
> ```text
> 1<=R_m(q)<=C,
> |R_m(q)-1|<=Cq/m.                                  (2.1)
> ```
>
> If also `q+1<=floor(m/2)`, then
>
> ```text
> |R_m(q+1)-R_m(q)|<=C/m.                            (2.2)
> ```
>
> Whenever both sides are in the half range,
>
> ```text
> |R_(m+1)(q)-R_m(q)|<=Cq/m^2.                       (2.3)
> ```

**Proof.**  The exact adjacent ratio is

```text
r_j=b_(j-1)/b_j=e(1-1/j)^(j-2),       j>=2.
```

The source-locked M276/M279 logarithmic estimate gives

```text
|log r_j|<=C/j,       |r_(j+1)-r_j|<=C/j^2.          (2.4)
```

Since `R_m(q)=product_(t=0)^(q-1)r_(m-t)`, summing `(2.4)` on indices at
least `m/2` proves boundedness and `|log R_m(q)|<=Cq/m`.  The exponential
mean-value theorem gives `(2.1)`.  The identity

```text
R_m(q+1)-R_m(q)=R_m(q)[r_(m-q)-1]
```

gives `(2.2)`.  Finally, take the difference of the two logarithmic
products for ranks `m+1` and `m`; `(2.4)` telescopes to `O(q/m^2)`, and
bounded exponentials give `(2.3)`.  QED.

> **Lemma 2 (complete scalar split divergence).**  For every odd `k>=3`,
> the exact signed sequence in `(1.1)` satisfies
>
> ```text
> sum_(s=0)^(k-1)|a_(s+1)-a_s|<=C/k.                (2.5)
> ```
>
> On `1<=s<=h`, more precisely,
>
> ```text
> a_s=b_s H_k(s),
> |H_k(s)|<=Cs/k,                              1<=s<=h,
> |H_k(s+1)-H_k(s)|<=C/k,                      1<=s<h. (2.6)
> ```

**Proof.**  On the half range,

```text
H_k(s)=[D/(D-1)]R_D(s)-[k/(k-1)]R_k(s).            (2.7)
```

Lemma 1, the `O(1/k)` prefactor difference, and comparison of the rank-`k`
and rank-`D` products give the first bound in `(2.6)`; `(2.2)` gives the
adjacent bound.  Also

```text
|b_(s+1)-b_s|<=C b_s/s.
```

Hence `|a_(s+1)-a_s|<=Cb_s/k` on the internal low range.  Its sum and the
zero-boundary jump are `O(1/k)` because `sum_s b_s<infinity`.

For `h<s<=k-1`, both `s` and `D-s` are comparable to `k`.  Two-sided
Stirling and

```text
p_(s+1)/p_s=r_(D-s)/r_(s+1)
```

give `p_s<=Ck^(-3/2)` and `|p_(s+1)-p_s|<=Ck^(-5/2)`.
The high-range variation and its terminal jump are therefore
`O(k^(-3/2))`.  At the low/high junction the dropped term is
`q_h=O(k^(-3/2))`.  Adding these contributions proves `(2.5)`.  QED.

## 3. Strict obstruction to the scalar-BV shortcut

Lemma 2 does not imply a marked response bound by total-variation
contraction.  M91 proves `p_s<q_s` on `s<=h`, `a_s=p_s>0` above `h`, and

```text
sum_s |a_s|=Theta(k^(-1/2)).                         (3.1)
```

Indeed the negative and positive masses are equal and the cumulative
minimum has order `k^(-1/2)`.

This gives a strict abstract counterexample to the tempting multiplier
shortcut.  On a two-point profile space choose a probability kernel
`F_s=delta_-` on the negative range and `F_s=delta_+` on the positive
range.  Then every `||F_s||_TV=1`, while

```text
||sum_s a_s F_s||_TV=sum_s|a_s|=Theta(k^(-1/2)),
```

despite `(2.5)`.  Thus scalar coefficient BV plus uniformly bounded marked
kernels cannot prove `O(1/k)`.  This is an obstruction to that general
shortcut, not a counterexample to the actual CBPV candidate.

## 4. First standalone unresolved lemma

For `X` in `{H,A,C}` and owner-size index `d` or `(d,e)`, let
`M^X_d` or `M^X_(d,e)` be the literal incidence-mark operator: it sends a
physical product state to the finite measure on its **nonzero** response
profiles, summing every relevant actual owner incidence.  The operator
retains the exact triangle `1/3` and side/negative `1/4` representation
averages; equivalently these average back to the state-level incidence
measure because the literal response is anchor invariant.

Let `Phi_(j,s)` and `Psi_(j,s)` be M91's full conditional product laws in
live channel `j=1,2`, including all raw lifts.  Push them through the mark
operator and combine the two live channels before any norm:

```text
F^X_s=alpha_1 (M^X_* Phi_(1,s))+alpha_2 (M^X_* Phi_(2,s)),
G^X_s=alpha_1 (M^X_* Psi_(1,s))+alpha_2 (M^X_* Psi_(2,s)). (4.1)
```

All `T/S/N` kinds, phases, seams, owner incidences, and source counterterms
remain inside `(4.1)`.  Linearity of M91's exact measure-valued Abel
identity gives, with equality of signed profile measures,

```text
mu^X
 =sum_(u=1)^(k-2) D_u(F^X_u-F^X_(u+1))
  +sum_(s=1)^h q_s(F^X_s-G^X_s).                   (4.2)
```

No endpoint term is missing because `D_(k-1)=0`.

> **Combined marked-profile Abel divergence `(CMPAD)` (unresolved).**
> The single fully combined measure in `(4.2)` obeys
>
> ```text
> ||mu^H_(k,d)||_TV<=C d b_d/k,
> ||mu^A_(k,d)||_TV<=C d b_d/k,
> ||mu^C_(k,d,e)||_TV<=C max(d,e)b_d b_e/k.         (4.3)
> ```

Equation `(4.2)` is the exact complementary-gap coefficient formulation of
CBPV.  Lemma 2 controls only its scalar weights.  The first unproved step is
the common-profile cancellation between both terms of `(4.2)` after both
channels and every phase/seam contribution have been combined.  Bounding
the two sums, either channel, or any source/type row separately would lose
the cancellation and is not proposed.

## 5. Exact small-size handling

- Set the formal amplitude `u_1=0`.  Size-one response rows are zero.  A
  literal coefficient pushforward can retain a zero-profile atom; it is
  deleted in `M^X` because it multiplies the zero response.
- `Delta A_2=Delta A_3=0` throughout `2<=ell<=n-3`.
- `H_2,H_3` and off-diagonal rows involving sizes two or three remain in
  `(CMPAD)` and are not declared proved.
- At the minimal rank `k=3`, `h=1`, so every SOCL row in scope is a
  size-one zero row.  The rank-3 instance is therefore exact and trivial.

## 6. Sole finite guard

The predeclared exact guard used only `k=11` (`n=33`).  It reconstructed
`27,060` states, `91,110` positive-composition representations, and the
complete combined coefficient before profile grouping.  The maximum
normalized CBPV values were

```text
H, d>=2           2.3542421864832535
A, d>=4           0.8658065231265041
C, d,e>=2         4.929342656484796.
```

The candidate survives this guard.  The many actual profile classes (up to
`149` in H and `32` in C at this rank) confirm that the scalar mark is not
a single fixed profile; they prove no asymptotic obstruction.  No other
rank was used.

## 7. Exact stop

```text
CBPV => SOCL deterministic implication                 proved exact
Borel ratio envelope and scalar split BV O(1/k)        proved all-rank
generic scalar-BV multiplier shortcut                  refuted
CMPAD / CBPV                                            unresolved
SOCL and every downstream theorem                      unresolved
```
