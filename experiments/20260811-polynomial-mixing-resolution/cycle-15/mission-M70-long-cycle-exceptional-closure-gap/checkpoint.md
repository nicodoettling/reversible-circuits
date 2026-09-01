# M70 halfway checkpoint

Date: 2026-08-12. Convention `(pq)(x)=p(q(x))`; tuple products are
left-to-right. Put `n=2l+1`, `m=2l`, and
`h=(0 1 ... n-1)`. The state law is uniform on minimal length-`m`
transposition factorizations of `h`, grouped into `l` consecutive raw pairs.

## H-001: exact additive Rayleigh identities

Let M67's accepted product feature be

```text
f(g)=E[a(t_1)+a(t_2)|t_1t_2=g],
a((rs))=-(omega^(-r)-omega^(-s))^2,
```

and set `f_i=f(G_i)`, `F=sum_i f_i`. Write

```text
V=E|f_1|^2,  C=Re E[conj(f_1)f_2],  kappa=C/V.
```

Cyclic positional covariance makes these independent of the selected
distinct positions. Therefore, exactly,

```text
||F||^2=lV+l(l-1)C=lV[1+(l-1)kappa].                (H.1)
```

For any conditional expectation `P_ij` resampling coordinates `i,j`,
`(I-P_ij)F=(I-P_ij)(f_i+f_j)`. Conditional-expectation contraction gives

```text
||(I-P_ij)F||^2<=E|f_i+f_j|^2=2(V+C).                (H.2)
```

Hence for the nonlazy complete-pair heat bath
`C_l=binom(l,2)^(-1)sum_(i<j)P_ij`,

```text
R_C(F):=<F,(I-C_l)F>/||F||^2
 <=2(V+C)/[lV(1+(l-1)kappa)]
 =2(1+kappa)/[l(1+(l-1)kappa)].                     (H.3)
```

M67 proves `kappa>=c/sqrt(l)` for a universal `c>0` eventually, so
`R_C(F)=O(l^-3/2)`. This is a rigorous polynomial slow-mode upper bound on
`gap(C_l)`, but it is not superpolynomial and supplies no bottleneck.

For the aligned adjacent-pair heat bath
`B_l=(l-1)^(-1)sum_(j=1)^(l-1)P_(j,j+1)`, the same bound (H.2) gives

```text
R_B(F)<=2(1+kappa)/[l(1+(l-1)kappa)]=O(l^-3/2).      (H.4)
```

For the fixed-endpoint raw local chain

```text
K^h=(1/2)I+(1/6)sum_(r=3)^5 (1/(m-r+1))sum_i H_(i,r),
```

every selected window intersects at most three pair coordinates, and
conditional-expectation contraction gives

```text
||(I-H_(i,r))F||^2
 <=E|sum_(j touched) f_j|^2
 <=3V+6C.
```

Thus, using the `1/6` global coefficient and summing the three normalized
window scans,

```text
R_(K^h)(F)<=(3V+6C)/[2lV(1+(l-1)kappa)]
           =O(l^-3/2).                               (H.5)
```

This chain has endpoint `h`, not identity, and is introduced only to test
whether the mode survives literal local blocks.

## H-002: exact frequency sector and minimal invariant closures

Let simultaneous endpoint-cycle conjugation be

```text
(Uf)(t_1,...,t_m)=f(h^(-1)t_1h,...,h^(-1)t_mh).
```

Every same-product heat bath commutes with `U`: conjugation maps each
conditional fiber bijectively to the conjugate fiber and fixes endpoint `h`.
Thus `C_l`, `B_l`, and `K^h` all reduce the character spaces

```text
H_k={Phi:U Phi=omega^(2k)Phi},  k in Z_n.             (H.6)
```

With the feature convention above, `F` belongs to `H_1` (replacing `omega^2`
by its conjugate merely swaps `H_1,H_(n-1)`). For a self-adjoint chain `P`,
the smallest exact invariant closure is its Krylov space

```text
V_P(F)=closure span{F,PF,P^2F,...} subset H_1.        (H.7)
```

This is the precise closure requested by M70. No smaller explicit
one-coordinate span is invariant in general: a two-coordinate heat bath maps
an additive function to a function of the outside product, producing genuine
multi-coordinate dependence. M67's feature is only a Rayleigh vector for its
one-coordinate correlation block, not an eigenfunction.

## H-003: a full-twist Poincare bound on the entire frequency sector

For adjacent raw positions, the project Hurwitz bijection is

```text
sigma_i(...,t_i,t_(i+1),...)
 =(...,t_(i+1),t_(i+1)t_i t_(i+1),...).              (H.8)
```

It preserves the ordered product and uniform measure. In the braid group,
the full twist

```text
Delta^2=(sigma_1 sigma_2 ... sigma_(m-1))^m           (H.9)
```

acts on every factor by simultaneous conjugation with the total product
`h` (or `h^-1`, depending on generator orientation). The two possibilities
are inverse characters and have the same modulus below. Formula (H.9) has
exact word length

```text
L=m(m-1).                                             (H.10)
```

For every `Phi in H_k`,

```text
||U Phi-Phi||^2=|omega^(2k)-1|^2||Phi||^2
               =4sin^2(2pi k/n)||Phi||^2.            (H.11)
```

Telescoping along (H.9), using invariance of the uniform law under every
Hurwitz prefix, gives

```text
4sin^2(2pi k/n)||Phi||^2
 <=L sum_(s=1)^L ||(U_(sigma_(i_s))-I)Phi||^2.        (H.12)
```

For the adjacent two-raw-factor heat bath `R_i`, the Hurwitz map is a
permutation of each same-product fiber, so

```text
||(U_(sigma_i)-I)Phi||^2<=4||(I-R_i)Phi||^2.          (H.13)
```

Each generator index occurs exactly `m` times in (H.9). Consequently

```text
sum_s ||(U_(sigma_(i_s))-I)Phi||^2
 <=4m sum_(i=1)^(m-1)<Phi,(I-R_i)Phi>.               (H.14)
```

Let `L_n=(m-1)^(-1)sum_i R_i`. Combining (H.10)--(H.14),

```text
<Phi,(I-L_n)Phi>/||Phi||^2
 >=sin^2(2pi k/n)/[m^2(m-1)^2].                      (H.15)
```

M27 stated its spectral theorem only after restriction to a fixed parking
multiset.  Its padding observation extends edgewise to the full minimal
bridge, and here is the needed scope check.  An off-diagonal `L_n` edge changes
a unique adjacent raw pair.  Choose an aligned four-window containing it and
keep the other two factors fixed.  The target is in that exact H4 fiber even
if its parking macro changes.  The aligned scan/fiber bound is
`B_l(x,y)>=1/[(l-1)M^4]`; minimality makes the raw-pair fiber size two or three,
so `L_n(x,y)<=1/[2(m-1)]`.  Since `m=2l`, this proves on the full space

```text
E_(B_l)>=M^-4 E_(L_n),  M=binom(n,2).                 (H.16)
```

Because `n` is odd, multiplication by two permutes the nonzero residues.
Thus every `k!=0` obeys
`|sin(2pi k/n)|>=sin(pi/n)>=2/n`, and hence

```text
R_B(Phi)>=4/[M^4n^6].                                (H.17a)
```

For `H_1`, which contains every M67 exceptional closure, the stronger bound is

```text
R_B(Phi)>=sin^2(2pi/n)/[M^4m^2(m-1)^2]
           >=16/[M^4 n^6]                            (H.17)
```

for `n>=5`, using `sin(2pi/n)>=4/n`, `m,m-1<n`. This is inverse polynomial
(of order `n^-14` after `M^4`), so the M67 mode cannot make aligned `B_l`
superpolynomially slow.

The accepted complete-to-adjacent comparison is

```text
gap(B_l)>=gap(C_l)/(2l^2),                            (H.18)
```

which has the wrong direction for transferring (H.17) back to `C_l`.
However `C_l` directly contains adjacent pair heat baths with coefficient
`1/binom(l,2)`, whereas `B_l` gives them coefficient `1/(l-1)`. Hence

```text
E_(C_l)>=[2/l]E_(B_l).                                (H.19)
```

Every nonzero sector therefore has an inverse-polynomial `C_l` gap. On the
M67 frequency-two sector,

```text
R_C(Phi)>=32/[lM^4 n^6],                              (H.20)
```

also inverse polynomial.

Finally, no padding estimate is needed for `K^h`. Its aligned length-four
windows are exactly the projections in `B_l`. Each has coefficient
`1/[6(m-3)]` in `K^h`, while it has coefficient `1/(l-1)` in `B_l`. Since
`m=2l`,

```text
E_(K^h)>=[(l-1)/(6(2l-3))]E_(B_l)>=(1/12)E_(B_l).   (H.21)
```

This is the accepted original-`K`-to-aligned-`B` comparison, and it applies
verbatim at arbitrary fixed endpoint. Therefore on `H_1`,

```text
R_(K^h)(Phi)>=4/[3M^4n^6].                           (H.22)
```

## Frontier

The M67 additive direction is polynomially slow:

```text
gap(C_l), gap(B_l), gap(K^h) <=O(l^-3/2),
```

but its entire cyclic-frequency closure has an inverse-polynomial Poincare
lower bound by the full twist. Thus it does not yield a superpolynomial
auxiliary obstruction.

The smallest open implication is now:

> **CYCLICALLY INVARIANT SECTOR.** Prove an inverse-polynomial gap for the
> `U`-invariant sector `H_0` of `C_l` or `B_l`. Every nonzero character sector,
> including the entire M67 exceptional closure, is polynomially bounded.

No lift to identity-conditioned original `K` follows. Under prefix closure,
the endpoint `h` is an internal prefix product; boundary H3/H4/H5 moves change
that endpoint, and M67 supplies neither a stationary-mass cut nor a full
boundary-flow estimate.

## H-004: bounded exact-kernel calibration

The deterministic `N=7,l=3` artifact constructs all `7^5=16,807` minimal
factorizations and every conditional fiber exactly, then uses a floating
ARPACK eigensolver inside the explicitly projected M67 cyclic character. The
gaps on the Krylov closure generated by `F` are

```text
C_l: 0.253029741986,
B_l: 0.175348972227,
L_n: 0.015491894343,
K^h: 0.102298295312.
```

An initial unprojected diagnostic leaked roundoff into the constant
eigenvector for `C_l,K^h`; the recorded script enforces the exact cyclic
character after every matrix-vector multiplication. This finite calculation
can falsify scan normalizations or zero-gap claims at `N=7`; it is not an
asymptotic proof.
