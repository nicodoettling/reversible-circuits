# Independent analytic audit of M83 Proposition 3.1

Date: 2026-08-12.  Convention: `(pq)(x)=p(q(x))`; factors multiply
left-to-right.

## 1. Sources, adjacency, and residual cycles

Let `n=3k`, where `k>=3` is odd, and let `h=(0 1 ... 3k-1)`.  Put

```text
A=(0,k,2k),              B=(0,1)(k,2k).
```

The ordered lifts

```text
A=((k,2k),(2k,0)),       B=((k,2k),(0,1))
```

are correct under the stated convention.  They share the first chord, while
the differing chords share exactly endpoint `0`; this is a strict
`Lambda_n` edge.  Direct cycle tracing gives

```text
cycles(A^-1 h) = [0,...,k-1], [k,...,2k-1], [2k,...,3k-1],
cycles(B^-1 h) = {0},
                 (1,...,k-1,2k,...,3k-1),
                 (k,...,2k-1).
```

Thus their residual component sizes are `(k,k,k)` and `(1,2k-1,k)`.

## 2. The full A-side zero event

In a minimal transposition factorization of `A^-1 h`, each factor remains
inside one of its three residual cycles.  Therefore every double target with
positive `K(A,.)` has both underlying chords internal to the three contiguous
length-`k` blocks above.

For two disjoint noncrossing chords, write the four positive cyclic endpoint
gaps as `x,y,z,w`.  In the separated and nested schemas the residual sizes
are, respectively,

```text
(x,z,y+w),       (x+z,y,w).
```

A singleton residual part therefore forces one of the target chords to be a
polygon boundary edge.  The other chord remains internal to one contiguous
length-`k` block.  One cyclic arc between its endpoints has length at most
`k-1`; in the displayed schema this arc is either itself a remaining
residual part or loses the singleton gap, making it still smaller.  Hence at
least one nonsingleton residual part is at most `k-1`.  It cannot belong to

```text
F_k={(1,u,3k-1-u): k<=u<=floor((3k-1)/2)}.
```

The definition of `F_k` uses only residual cycle sizes and is invariant under
conjugation by `h`.  Summing raw targets over quotient orbits consequently
gives the literal quotient identity `bar K(A,F_k)=0`.

## 3. Selected B-side targets and exact multiplicities

In the long residual cycle

```text
L=(1,...,k-1,2k,...,3k-1)
```

choose `e=(i,j)` with

```text
1<=i<=k-1,  2k<=j<=3k-1,  k+1<=j-i<=2k,
```

and in `M=(k,...,2k-1)` choose the boundary chord
`f=(m,m+1)`, `k<=m<=2k-2`.  Their endpoints occur as
`i<m<m+1<j`, so `ef` is a noncrossing nested double.  Direct gap tracing
gives residual sizes

```text
(1,j-i-1,3k-(j-i)),
```

and the imposed range makes both nonsingletons at least `k`.

Put `r=j-i-k`.  In the cyclic order of `L`, the two arc sizes of `e` are
`r` and `2k-1-r`.  For `1<=r<=k-1`, exactly `r` choices of `(i,j)` have that
value.  For `r=k`, there are `k-1` choices and the smaller split is again
`k-1`.  Thus

```text
M_s=s (1<=s<=k-2),       M_(k-1)=2(k-1).
```

Every target product uniquely recovers its two disjoint edges; their residual
components distinguish `e` from `f`.  Hence there are no duplicate raw
targets.  Each double has exactly two ordered lifts, corresponding exactly to
the two color orders already included in

```text
c_k=2(2k-2)(k-1)/[(3k-3)(3k-4)].
```

There is no extra orbit multiplier or divisor: a quotient row is the sum of
the raw row over every raw target in an orbit, and the selected raw set is a
literal subset of the raw union underlying the invariant event `F_k`.

The `k-1` permitted `M` boundary chords each have weight `w_k(1)`.  The
displayed multiplicities give

```text
L_k=sum_(s=1)^(k-2) s w_(2k-1)(s)
       +2(k-1)w_(2k-1)(k-1).
```

Multiplication by `c_k (k-1)w_k(1)` gives M83's exact `p_k`.

## 4. Conditioned-Borel identity

Let

```text
tau(d)=d^(d-1)/d!,       b_d=e^(-d)tau(d),
w_d(s)=(d-2)! tau(s)tau(d-s)/d^(d-2).
```

Cancellation of the exponential factors and
`d!=d(d-1)(d-2)!` gives, exactly,

```text
b_s b_(d-s)/[(1-1/d)b_d]
 = d(d-2)!tau(s)tau(d-s)/d^(d-2)
 = d w_d(s).
```

For odd `d`, each smaller split `s<d/2` has exactly `d` chords, so this is
also the complete smaller-fragment probability.  Exact summation returns one.

## 5. Dominated Riemann sum and the constant

Stirling gives `b_j~c j^(-3/2)`, `c=(2pi)^(-1/2)`, together with a uniform
bound `b_j<=Cj^(-3/2)`.  For `s<=d/2`, the same bound above and below gives

```text
b_(d-s)/b_d <= C'(d/(d-s))^(3/2) <= C''.
```

With `x_s=s/d`, the exact Borel identity therefore yields

```text
d sqrt(d) s w_d(s)
 -> c x^(-1/2)(1-x)^(-3/2)
```

for fixed interior `x=s/d`, and its magnitude is bounded by
`C x_s^(-1/2)`.  This is integrable at zero.  More explicitly, the part
`s<=epsilon d` is bounded by

```text
(C/d) sum_(s<=epsilon d) (s/d)^(-1/2) <= 2C sqrt(epsilon),
```

uniformly in `d`; on `[epsilon,1/2]` ordinary uniform Riemann convergence
applies.  Hence, for odd `d`,

```text
sqrt(d) sum_(s<d/2) s w_d(s)
 -> c integral_0^(1/2) x^(-1/2)(1-x)^(-3/2) dx
  = c*2 = sqrt(2/pi).
```

For `d=2k-1`, the central term `(k-1)w_d(k-1)=O(k^-3/2)` and therefore is
negligible even after multiplication by `sqrt(k)`.  Since `d/k->2`,

```text
sqrt(k)L_k -> 1/sqrt(pi).
```

Also `c_k->4/9` and

```text
(k-1)w_k(1)=((k-1)/k)^(k-2) -> e^-1.
```

This proves

```text
p_k ~ 4/[9e sqrt(pi k)].
```

## 6. Explicit all-k lower bound

The ratio

```text
b_(j+1)/b_j=e^-1(1+1/j)^(j-1)<1
```

shows that `b_j` decreases.  Thus the exact Borel identity gives
`d w_d(s)>=b_s` for `s<d/2`.  The elementary Stirling upper bound
`s!<=e sqrt(s)(s/e)^s` gives `b_s>=e^-1 s^-3/2`.  Consequently, with
`d=2k-1`,

```text
L_k >= (ed)^(-1) sum_(s=1)^(k-2) s^(-1/2)
    >= sqrt(k-2)/[e(2k-1)]
    >= 1/[4e sqrt(k)].
```

The last inequality follows after squaring from
`16k(k-2)>=(2k-1)^2`, valid for `k>=3`.

At `s=1`, the same Borel domination gives

```text
(k-1)w_k(1) >= (1-1/k)b_1 >= 2/(3e).
```

Finally

```text
c_k=4(k-1)/[3(3k-4)] >=4/9.
```

Multiplying the three inequalities proves, for every odd `k>=3`,

```text
p_k >= 2/[27e^2 sqrt(k)].
```

## 7. Logical scope

Since total variation dominates the discrepancy on the invariant event,

```text
TV(bar K(A_k,.),bar K(B_k,.)) >= p_k=Omega(k^-1/2)=Omega(n^-1/2).
```

An infinite subsequence suffices to refute a universal `O(1/n)` one-step
edge-influence estimate.  Nothing above estimates `eta_k bar K`; cancellation
after the second kernel can still produce `O(n^-2)`.  Therefore this theorem
does not settle the two-step lemma, an H0 gap, a fixed-endpoint bridge gap,
the identity heat-bath gap, or either terminal outcome.
