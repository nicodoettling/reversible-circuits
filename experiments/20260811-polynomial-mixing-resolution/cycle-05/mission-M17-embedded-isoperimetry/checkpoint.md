# Halfway checkpoint: balanced two-lobe midpoint pinch

## Exact hidden cut

Let `N=2s+1`, `m=4s=2N-2`, and split a word at its midpoint.
Define `A_N` by requiring:

- the first half to be a minimal connected identity factorization on a set
  `S` of `s+1` labels;
- the second half to be a minimal connected identity factorization on a set
  `T` of `s+1` labels;
- `S union T=[N]` and `|S intersect T|=1`.

This is an internal temporal-articulation statistic inside the one-component
minimal full-support macro, not its component/weight datum.

The supports of the two halves determine `S,T` and their articulation
uniquely.  With

```text
C_(s+1)=(2s)!(s+1)^(s-2),
```

the exact count is

```text
|A_(2s+1)|
 =(2s+1) binom(2s,s) C_(s+1)^2.                        (H.1)
```

Thus, using `|F_(2s+1)|=(4s)!(2s+1)^(2s-2)`,

```text
|A|/|F|
 = [binom(2s,s)/binom(4s,2s)]
   [(s+1)^(2s-4)/(2s+1)^(2s-3)]
 ~ (8 sqrt(2)e/s)16^(-s).                              (H.2)
```

At `s=1` this ratio is `1/4`; for `s>=2` it is at most
`1/(2s+1)<=1/5`.  Since `A subset F subset Omega`, `pi(A)<=1/4`
with exact global mass obtained by dividing (H.1) by the content-character
formula for `|Omega(2s+1,4s)|`.

## Full-K exit

Every state in `A` has midpoint prefix product identity.  Write the last
left factor as `a` and the first right factor as `b`.  The equality
`a=b` is impossible: that edge would put both endpoints in
`S intersect T`, contradicting its singleton size.

Apply the right Hurwitz move at the midpoint:

```text
(a,b)->(b,bab).
```

It is an outcome of the length-three window beginning at the last left
position, retaining the next factor.  The prefix immediately before `a`
equals `a`, whereas the new midpoint prefix is `ab!=id`; hence the output
leaves `A`.  A three-factor conditional fiber has size at most `M^2`, so

```text
K(x,A^c)>=q_s:=1/[2|R_m|(m-2)M^2]  for every x in A,
Q_K(A,A^c)>=pi(A)q_s,
Phi_pm(A)>=q_s=Theta(s^-5).                             (H.3)
```

All `r=4,5` terms are nonnegative and remain part of `K).  At `s=1`,
the whole-word `H_4` term is retained.

## Exact falsification

The verifier proves:

- `N=3,m=4`: six cut states, `pi(A)=2/9), full flow
  `7/162+7/162=7/81` from `r=3,4), and conductance `7/18`;
- `N=5,m=8`: exactly 17,280 distinct cut states, all with valid midpoint
  certificates; `pi(A)=864/88547` and the proved lower bound is `1/3600`;
- the exact 27/120/3936 calibration counts;
- formula values through `N=21`, whose scaled conditional masses approach
  the predicted constant `8 sqrt(2)e`.

No Terminal-B family and no every-subset expansion theorem emerged.  The
remaining proposition is full embedded isoperimetry for arbitrary subsets of
the minimal full-support macro; the present theorem rejects one exponentially
rare temporal-articulation cut.
