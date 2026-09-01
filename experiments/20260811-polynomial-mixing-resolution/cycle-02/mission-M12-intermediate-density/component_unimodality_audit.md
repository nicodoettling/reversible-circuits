# Component-layer unimodality audit

This note records the independent component-polynomial lane and the
coordinator-side checks of its formulas.  It does **not** prove universal
unimodality.

## Exact identities

Let `Q(w)` be the support partition, including isolated labels, and let
`W_c(N,m)=#{w in Omega(N,m): |Q(w)|=c}`.  For `m>0`, its feasible interval is

```text
max(1,N-m/2) <= c <= N-1.                                (1.1)
```

Necessity is `m>=2(N-c)`.  Sufficiency follows by taking one connected
component on `N-c+1` labels and `c-1` isolates and using connected identity
factorization feasibility.  Thus there are no internal zeros.  For `m=0`,
only `c=N` occurs.

If `Z_P(m)` counts identity words confined to the internal transpositions of
a labeled set partition `P`, then

```text
P_{N,m}(u):=sum_c W_c(N,m)u^c
 = sum_{P in Pi_N} (u)_{|P|} Z_P(m).                     (1.2)
```

A word of exact support `Q` occurs in `Z_P` precisely when `Q` refines `P`.
Summing over coarsenings gives
`sum_p S(|Q|,p)(u)_p=u^{|Q|}`, proving (1.2).

With `C_{v,k}` the connected exact-support count, `C_{1,0}=1`, and

```text
H(y,t)=sum_{v,k} C_{v,k} y^v/v! t^k/k!,
```

the labeled component formula is

```text
sum_{N,m} P_{N,m}(u)y^N/N! t^m/m! = exp(uH(y,t)).        (1.3)
```

## Boundary-mass consequence of mere unimodality

If the positive feasible sequence `W_c` is unimodal, then every nontrivial
threshold satisfies

```text
W_{c_0+1} >= (1/N) min{
  sum_{c<=c_0}W_c, sum_{c>=c_0+1}W_c}.                   (2.1)
```

Choose a mode.  If it is at or below `c_0`, then `W_{c_0+1}` is the largest
term of the upper tail.  If it is at or above `c_0+1`, then every term of the
lower tail is at most `W_{c_0+1}`.  Each tail has at most `N` terms.

## Proved low-parameter theorem

The sequence `W_c(N,m)` is log-concave in either of the following regimes:

1. every `N` and `m in {0,2,4,6,8}`;
2. every even `m` and `N<=4`.

For `m=6`, the three possible nonzero layers are

```text
W_{N-3}=(15/8)N(N-1)(N-2)(N-3)(N^2+7N+20),
W_{N-2}=(5/4)N(N-1)(N-2)(3N+23),
W_{N-1}=(1/2)N(N-1),
```

and

```text
W_{N-2}^2-W_{N-3}W_{N-1}
 =(5/8)N^2(N-1)^2(N-2)
   (21N^3+294N^2+634N-2555)>0.
```

For `m=8`, put `A_r=W_{N-r}(N,8)`.  Direct component-profile enumeration
gives

```text
A_1=(1/2)N(N-1),
A_2=(7/4)N(N-1)(N-2)(9N+181),
A_3=(35/4)N(N-1)(N-2)(N-3)(3N^2+53N+364),
A_4=(35/16)N(N-1)(N-2)(N-3)(N-4)
    (3N^3+42N^2+289N+970).
```

The nontrivial differences factor as

```text
A_2^2-A_1A_3
 =(7/16)N^2(N-1)^2(N-2)
   (537N^3+21232N^2+181665N-447734)>0,

A_3^2-A_2A_4
 =(245/64)N^2(N-1)^2(N-2)^2(N-3)Q(N)>0,

Q(N)=153N^5+5007N^4+74261N^3+451873N^2
     +403466N-7247480.
```

Here `Q(4)=7,787,520`, and `Q` is increasing for positive `N`.  The displayed
`m=6,8` layer formulas were independently checked against the exact Frobenius
and component recurrence for `N=3,...,14` and `N=3,...,12`, respectively.
The cases `m<=4` have at most two nonzero layers.

For `N=4` and even `m>=4`,

```text
W_3=6,
W_2=4(3^(m-1)-3)+3(2^(m-1)-2).
```

The Frobenius trace gives

```text
Z_4(m)=6^m/12+3*2^m/4 <= 6^m/6.
```

Since `W_2>=4*3^(m-1)`, one has `W_2^2>=6^m>=6W_1`, proving the only
nontrivial log-concavity inequality.  `N<=3` has at most two nonzero layers.

## Why the natural total-positivity shortcut fails

The exponential identity alone does not force component unimodality.  For
example,

```text
[x^2y^2] exp(u(x+y+b x^2y^2)) = bu + u^4/4
```

has nonnegative connected weights but internal zero coefficients.

More specifically, define the exponential-Riordan triangle

```text
R_{n,c}(t)=n!/c! [y^n]H(y,t)^c.
```

Then

```text
R_{2,1}=cosh(t)-1,  R_{2,2}=1,
R_{3,2}=3(cosh(t)-1),  R_{3,1}=C_3(t),
```

so the natural `2x2` minor

```text
3(cosh(t)-1)^2-C_3(t)
```

has `t^4` coefficient `3/4-1=-1/4`.  It is not coefficientwise TP2 and is
negative for sufficiently small positive `t`.  Therefore the sufficient
criteria in Bao-Xuan Zhu, *Total positivity from the exponential Riordan
arrays*, <https://arxiv.org/abs/2006.14485>, do not apply directly.  This is
an obstruction to that proof route, not a counterexample to fixed-`m`
unimodality.

## Finite falsification status

Exact integer recurrence found no log-concavity failure for `N<=22` and even
`m<=220`.  Exact Sturm counts found only real roots in selected cases
`N=22`, `m=40,42,44,60,100,220`.  These finite checks can falsify the named
claim but cannot prove it.  The durable scripts in this mission reproduce a
smaller checked rectangle (`N<=15,m<=120`) and selected real-root tests; the
larger extension was an independent in-memory audit and is reported as
empirical rather than a durable universal argument.

## Exact remaining proposition

> For every `N>=3` and even `m>=0`, the positive sequence `W_c(N,m)` on the
> feasible interval (1.1) is unimodal.

The DYZ adjacent-genus bound in `checkpoint.md` supplies polynomial local
rates but neither log-concavity nor monotonicity of their increments.  A mere
polynomial adjacent-layer ratio iterated across `N` layers is insufficient.
