# M268 proof audit of the M266 full-DV-to-PCS assembly

## 1. Audited statement

Use `(pq)(x)=p(q(x))`, with displayed factors multiplying left-to-right.
Fix odd `k>=3`, set `n=3k`, `m=(n-1)/2`, exterior length
`D=2k-1`, and exterior residual rank `R=2k-3`. This is the auxiliary
first fixed-cell model for uniform minimal factorizations of the ambient
long cycle under the nonlazy cyclic rank-two kernel. It is not the global
identity-word law and not the lazy exact `{3,4,5}` heat-bath chain.

The audited conclusion is: the former full-DV hypothesis is discharged, and
the already accepted response chain is proved through PCS-bound. It stops
before FD-bound/minority-sign and hence before FCL1.

## 2. Exact full-DV assembly

M251/M255 proves for the normalized literal B-side ordered-disjoint-double
law, every `2<=ell<=(3k-1)/2`, and every adjacent edge
`1<=s<=k-2`,

```text
sum_s sqrt(s)|Delta_s Phi^D(Y_ell)| <=18400 sqrt(ell).
```

M258/M263 uses the same `Phi^D`, cutoff, and rank domain and proves the
literal identity

```text
Phi_s^D(X_ell)=Phi_s^D(Y_ell)+Theta_s(ell)
```

together with

```text
sum_s sqrt(s)|Delta_s Theta(ell)| <=500 sqrt(ell).
```

There is no `q` or `qhat` average in either statement. Taking the
adjacent difference of the exact identity before the triangle inequality
gives full DV for `X` with constant `18400+500=18900`; the `Y`
constant may be enlarged to the same value. Thus `K_V=18900`.

## 3. DE normalization and channel-two prefix

M192/M195's disjoint measures are intentionally unnormalized:
`phat_s=p_s(1-gamma_L(s))` and
`qhat_s=q_s(1-gamma_F(s))`. Their Abel identity keeps both the shared
triangle law and the nonzero unequal-mass endpoint. The scalar cumulative
bound is

```text
|E_u|<=K_E sqrt(u)/k.
```

Full DV therefore bounds the Abel variation by
`18900 K_E sqrt(ell)/k`. M248/M249 proves signed averaged DE on the same
domain with common constant `7164`. The complete shared endpoint is at
most `15 sqrt(ell)/k`, and the unequal-mass endpoint is at most
`6 sqrt(ell)/k`. Hence, for each channel-two prefix,

```text
K_J=18900 K_E+7164+15+6=18900 K_E+7185.
```

These are conditional channel quantities before multiplication by
`alpha_2`; no normalization factor is missing.

## 4. Hardy transfer and full WPCR

For `X_D=sum_(d=2)^D x_d`, direct finite interchange gives

```text
|X_m|/m+sum_(D=2)^(m-1)|X_D|/D^2
 <=3 sum_(d=2)^m |x_d|/d.
```

Applying this to M186/M189's exact channel-one coefficients `delta_d` and
`delta_d+epsilon_d` gives `3(2K_1+K_2)/k`. Channel two gives at most
`6K_J/k`. The source-independent masses

```text
alpha_0=(k-1)(k-2)/den,
alpha_1=2(k-1)(2k-2)/den,
alpha_2=(2k-2)(2k-3)/den,
den=(3k-3)(3k-4)
```

are nonnegative and sum to one, while the `J=0` law cancels. Termwise
triangle inequality and `n=3k` therefore give

```text
C_W=18K_1+9K_2+18K_J
   =18K_1+9K_2+340200K_E+129330.
```

This is WPCR, not pointwise PCR. J1-PCR is unused.

## 5. WPCR to SCBR: singleton and both endpoints

M186/M189's exact signed summation by parts is

```text
S_k=M_1(1)u_1(1)+A_m u_2(m)+C_m r_m
 +sum_(d=2)^(m-1){
    A_d[u_2(d)-u_2(d+1)]
   +C_d[r_d-r_(d+1)]}.
```

WPCR contains exactly the endpoint functional
`(|A_m|+|C_m|)/m` and exactly the interior
`sum_(d=2)^(m-1)(|A_d|+|C_d|)/d^2`. The accepted ratio estimates give
`|u_2(d)|+|r_d|=O(d^-1)` and adjacent differences `O(d^-2)`.

The singleton is not inferred from WPCR: M186 separately proves
`M_1(1)=O(1/n)`, while its zero-shift convention makes `u_1(1)` a fixed
finite constant. These three inputs cover every displayed term and prove
`|S_k|=O(1/n)`. There is no omitted endpoint or hidden PCR use.

## 6. Tail, BR/BIR, affine response, and PCS

M180/M182 proves the absolute large-component tail

```text
sum_(d>n/2)|M_1(d)u_1(d)+M_2(d)u_2(d)|=O(1/n).
```

Together with SCBR this gives `eta(Q)=O(1/n)`. The exact bounded-remainder
identity proves

```text
eta(B_k)=O(1) iff n eta(Q)=O(1).
```

The exact incidence identities

```text
eta(Q)=e eta(H)-t_k,
eta(H)=(n-3)/2[(bar K^2W)(O_B)-(bar K^2W)(O_A)],
t_k=12(k-1)/[3k(3k-4)(2k-1)]=O(n^-2)
```

then prove BR iff BIR at scale `n^-2`, in both directions.

M174/M178's affine response keeps the kind term:

```text
Delta_k(C_k)=e^-2/[(n-3)(n-4)]
             [2n eta(T)+eta(B_k)],
eta(T)=t_k.
```

Since `2n eta(T)=O(1)` and
`(n-3)(n-4)` is uniformly comparable with `n^2`, BR is equivalent to
`Delta_k(C_k)=O(n^-2)`. Finally,

```text
sum_y z_k(y)=2Delta_k(C_k)/pi_y,
pi_y=2/(n-2)(1-2/n)^(n-3).
```

Here `pi_y` is uniformly comparable with `1/n` and `k=n/3`.
Consequently

```text
Delta_k(C_k)=O(n^-2)
 iff k|sum_y z_k(y)|=O(1).
```

The Delta/PCS arrow is therefore an exact two-way normalization, not merely
a sufficient implication.

## 7. Minimal boundary

At `k=3`, `n=9`, `m=4`, the adjacent-rank domain is the single edge
`s=1`, and the cutoffs are `ell=2,3,4`. The normalization values are
`H_1=1/2`, `H_2=2/9`; the channel masses are
`(1/15,8/15,2/5)`; and the disjoint Abel endpoint is `-4/15`.
M258's `ell=4>D-2` term is covered by its empty-sum convention. M186's
small sizes are exactly `d=1,2,3,4`, with the singleton separated and
both `m=4` endpoints retained. No proof uses a larger-rank threshold.

## 8. Exact stop

PCS controls only an absolute value of the signed phase total. M168/M171's
deterministic closure retains

```text
(n-3)k sum_y |z_k(y+1)-z_k(y)|.
```

It still requires FD-bound
`k^2 sum_y|Delta z_k(y)|=O(1)`, or the accepted alternative
minority-sign estimate. Nothing audited here proves PCR, FCL1, the first
fixed-cell absolute scalar, another cell, direct L1/all-edge control, H0, a
bridge gap, polynomial mixing, or a Terminal.

