# M253 fresh immutable referee report on M252

Date: 2026-08-14 UTC.

Verdict: **ACCEPT**.

M252 proves the full weighted prefix-component response `(WPCR)` conditional
on M192's disjoint split variation hypothesis `(DV)`, using the accepted
M248/M249 disjoint embedding response `(DE)`. It does not prove `(DV)`, full
pointwise `(PCR)`, `(SCBR)`, or any downstream mixing statement. There are no
material objections.

## 1. Immutable provenance gate

The SHA-256 digest of M252's checksum inventory is exactly

~~~text
896c8a7169ba73a8ae500a350de1d9106cd3a6f81dd4934b078fbdfd2e137556.
~~~

All nine files named in that inventory pass `sha256sum -c SHA256SUMS`. The
eight predecessor checksum-file digests recompute to

~~~text
M180 b362d629eaae627432efb3d6de97a825ed1bb17c0ca17ffb39c342db5c9d76d6
M182 4b5f96b5269f6174102086ce30ed0858537122bdec39b551e2248d843439c9ad
M186 9d5aa5ff628f8bf15051c09fd1537ffa240fba72ad2a9945356c8adfe8ebd7bd
M189 893275dc8e31ffbd2a801415a5c26f3cd0221795d7c22260ec5866781494ce66
M192 4c6cd295cd2a8259d396f8f9218e7f98746e7d005a255cfb4f14dc2d96336c60
M195 1f0c398bd92edf37e16880c239e0bf65d63622e1de9c2c9904a26fd560d93f0a
M248 c3726d05943b696c11f8e984fae9aa0ee342d00c0744bd7bf0a0f665acbe8bd8
M249 9246377285741ba7af0b2eb713f94e32e9aa25a0c00a7278c0cd9e8240b2d3f7.
~~~

Every file in every one of those eight inventories also passes. M252 and all
predecessors were treated as immutable.

## 2. Exact setting and equal-mass channel decomposition

The audited statement is in M186's fixed-cell model: odd `k>=3`, `n=3k`,
`m=(n-1)/2`, uniform minimal length-`n-1` transposition factorizations of the
ambient cycle, and the nonlazy cyclic rank-two coordinate operator. It is not
the global identity-bridge law or the lazy `{3,4,5}` heat-bath chain.

At both sources the common middle residual has transposition rank `k-1` and
the aggregate exterior residual has rank `2k-2`. Therefore the exact masses
of the number `J` of exterior colors among the first two factors are

~~~text
denominator = (3k-3)(3k-4),
alpha_0 = (k-1)(k-2) / denominator,
alpha_1 = 2(k-1)(2k-2) / denominator,
alpha_2 = (2k-2)(2k-3) / denominator.               (2.1)
~~~

They are nonnegative, source-independent, and sum to one. Conditional on
`J=0`, both factors come from the same common middle residual, so the entire
conditional law is identical at A and B and cancels. Hence, coefficientwise,

~~~text
M_r(d)=alpha_1 M_r^(1)(d)+alpha_2 M_r^(2)(d),
~~~

and finite summation gives exactly M252's mixture identities for `A_D,C_D`.
There is no omitted `alpha_0` contribution and no cross-channel cancellation
assumption. Since `0<=alpha_j<=1`, the later separate triangle bounds are
licensed.

## 3. Channel one: the two weighted inputs really suffice

M186/M189 define

~~~text
delta_d=rho_B(d)-rho_A(d),
epsilon_d=sum_(a+b=n-d)delta_a rho_A(b),
M_1^(1)(d)=delta_d,
M_2^(1)(d)=epsilon_d.                               (3.1)
~~~

Their accepted estimates are the unsigned coefficient bounds

~~~text
sum_a |delta_a|/a <=K_1/k,                          (3.2)
sum_(a,b) |delta_a|rho_A(b)/(n-a-b) <=K_2/k.        (3.3)
~~~

The second estimate is not merely a bound on a final signed charge. At each
fixed residual size `d`, ordinary triangle inequality in (3.1) gives

~~~text
|epsilon_d|/d
 <=sum_(a+b=n-d)|delta_a|rho_A(b)/(n-a-b).
~~~

Summing over `d` proves `sum_d |epsilon_d|/d<=K_2/k`. The exact source
domains are `a<=2k-1` and `b<=k-1`, so `d=n-a-b>=2`; every denominator is
positive and belongs to the two-run range. Restricting from the full support
to `2<=d<=m` only decreases the nonnegative sums.

For a finite sequence `x_2,...,x_m` with `X_D=sum_(d=2)^D x_d`, expand
prefixes and interchange finite sums. The exact coefficient of `|x_d|` is

~~~text
1/m+sum_(D=d)^(m-1)1/D^2.                          (3.4)
~~~

For `d<m`, it is at most

~~~text
1/d+1/d^2+integral_d^infinity x^(-2)dx <=3/d,
~~~

and for `d=m` it is `1/m<=3/m`. This independently proves M252's
Hardy--Abel inequality with constant three. Applying it to `delta` and to
`delta+epsilon` gives

~~~text
(|A_m^(1)|+|C_m^(1)|)/m
 +sum_(D=2)^(m-1)(|A_D^(1)|+|C_D^(1)|)/D^2
 <=3(2K_1+K_2)/k.                                  (3.5)
~~~

Multiplication by `n=3k` gives exactly `18K_1+9K_2`.

## 4. Channel two: exact observables and no hidden normalization

M192's literal conditional `J=2` observables are

~~~text
X_ell=sum_(2<=d<=ell)[N_1(d)+N_2(d)],
Y_ell=sum_(2<=d<=ell)N_1(d),
2<=ell<=(3k-1)/2.                                  (4.1)
~~~

The conditional coefficient is the component pushforward of
`Lambda_L-Lambda_F`. Therefore, setting `ell=D`, linearity gives exactly

~~~text
A_D^(2)=E_B[X_D|J=2]-E_A[X_D|J=2],
C_D^(2)=E_B[Y_D|J=2]-E_A[Y_D|J=2].                 (4.2)
~~~

These are conditional quantities before multiplication by the full channel
mass `alpha_2`; no additional factor is missing. M192 partitions each
conditional law into shared-endpoint triangles and disjoint ordered pairs.
The disjoint weights `p_hat,q_hat` are intentionally unnormalized, so its
`R_D(Z)` plus the shared contribution is the full conditional difference,
not a renormalized subchannel.

For either `Z=X_D,Y_D`, `0<=Z<=3`. The exact shared masses therefore give

~~~text
3[3/(2k-1)+3(k-2)/(k(2k-3))] <=15/k.               (4.3)
~~~

M192's disjoint Abel identity has the necessary unequal-mass endpoint

~~~text
E_(k-1)=-6(k-1)/[k(2k-1)(2k-3)].                  (4.4)
~~~

Its contribution is at most

~~~text
18(k-1)/[k(2k-1)(2k-3)]
 <=18/k^2 <=6sqrt(D)/k.                             (4.5)
~~~

Thus neither the endpoint nor the shared triangles are omitted. With M192's
proved scalar estimate `|E_u|<=K_E sqrt(u)/k`, the assumed `(DV)` constant
`K_V` bounds the Abel variation by `K_E K_V sqrt(D)/k`. Frozen M248/M249
proves the signed averaged `(DE)` bound with common constant `7164` for both
observables on exactly the range (4.1). Consequently

~~~text
|A_D^(2)|,|C_D^(2)| <=K_J sqrt(D)/k,
K_J=K_E K_V+7164+15+6=K_E K_V+7185.                (4.6)
~~~

This verifies every triangle, the unequal disjoint-mass endpoint, and the
absence of a hidden conditional normalization.

## 5. Channel-two and full WPCR scaling

Since `k>=3`, one has `m=(3k-1)/2>=4`. Also

~~~text
m^(-1/2)+sum_(D=2)^infinity D^(-3/2) <3.           (5.1)
~~~

For completeness, monotonicity gives the series at most
`2^(-3/2)+integral_2^infinity x^(-3/2)dx=5sqrt(2)/4`; together with
`m^(-1/2)<=1/2`, (5.1) follows from `sqrt(2)<2`. Applying (4.6) to both
prefixes gives the channel-two WPCR functional at most `6K_J/k`.
Multiplication by `n=3k` gives `18K_J`.

Finally, positivity of `alpha_1,alpha_2` and triangle inequality at each
prefix and endpoint yield

~~~text
n[(|A_m|+|C_m|)/m
  +sum_(D=2)^(m-1)(|A_D|+|C_D|)/D^2]
 <=18K_1+9K_2+18(K_E K_V+7185).                   (5.2)
~~~

This is precisely the conditional full-WPCR theorem stated by M252.

## 6. Strict PCR limitation

The accepted weighted coefficient estimates do not logically imply the
pointwise scale required by `(PCR)`. The abstract sequence

~~~text
x_k=1, x_(k+1)=-1, x_d=0 otherwise
~~~

is available inside `2<=d<=m` for every odd `k>=3`. Its weighted l1 norm is
at most `2/k`, while its prefix at `D=k` is one; the ratio to
`sqrt(k)/k` is `sqrt(k)` and is unbounded. This is only a logical
non-implication, not a counterexample to the literal `rho` profiles. M252
correctly leaves `(J1-PCR)` and full `(PCR)` unresolved.

## 7. Independent exact checker

`independent_algebra_check.py` has no imports and reads no M252 or predecessor
code or data. It implements its own reduced-rational arithmetic and checks:

- the three exact channel masses and their normalization;
- common-`J=0` cancellation in synthetic exact conditional mixtures;
- fixed-`d` grouping of signed `epsilon_d` and the `d>=2` boundary;
- every exact Hardy coefficient through `m=513`;
- the shared and unequal-mass endpoint inequalities;
- the displayed constant/scaling arithmetic; and
- the abstract PCR non-implication family.

The command

~~~text
python3 independent_algebra_check.py
~~~

passes 128 channel rows, 1,518 mixture rows, 49,536 grouped-epsilon rows,
131,328 Hardy rows, 24,768 endpoint rows, and 1,000 PCR-witness rows. These
are finite exact falsification checks only; Sections 2--6 are the all-rank
proof audit.

## 8. Numbered objections and scope

1. **Material objections:** none.
2. **Nonmaterial objections:** none.
3. **Scope guard:** ACCEPT establishes only M252's full `(WPCR)` theorem
   conditional on `(DV)`, with `(DE)` accepted. `(DV)`, full `(PCR)`, and
   `(J1-PCR)` remain unresolved. This report makes no `(SCBR)`, `(BIR)`,
   `(BR)`, PCS, comparison, spectral-gap, mixing-time, or Terminal inference.

Final verdict: **ACCEPT M252 AS FROZEN.**

