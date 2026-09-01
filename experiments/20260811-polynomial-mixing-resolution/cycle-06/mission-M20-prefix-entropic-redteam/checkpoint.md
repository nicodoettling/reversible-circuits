# M20 halfway checkpoint: midpoint-prefix renewal is not a bottleneck

Date: 2026-08-11  
Convention: `(pq)(x)=p(q(x))`, words multiply left-to-right.

## Candidate

For `N>=3`, put `k=2N^3`, `m=2k=4N^3`, and define

```text
A_N^0={w in Omega(N,m):t_1...t_k=id},
A_N={w in A_N^0:the full factorization graph is connected on [N]}.
```

This is a literal connected-full-support, midpoint-prefix renewal cut.  It is
invisible to the support-component macro inside `A_N`, and its stationary
mass is factorially small.

## Exact mass and orientation

Let `C_d(r)` count length-`r` transposition returns in `S_d`.  Then

```text
pi(A_N^0)=C_N(k)^2/C_N(2k).
```

For a set partition `P` of `[N]`, let `R_P(k)` count return words using only
edges internal to blocks of `P`.  Partition-lattice Möbius inversion gives

```text
J_N(k)=sum_P (-1)^(|P|-1)(|P|-1)! R_P(k)^2,
pi(A_N)=J_N(k)/C_N(2k).
```

The even-time character expansion and the exact proper character-ratio bound
`|r_lambda|<=1-2/(N-1)` imply

```text
pi(A_N^0)<= [2/N!](17/16)^2 <1/2.
```

Conditioned on `A_N^0`, its two halves are independent return bridges.  A
union bound over vertex cuts gives

```text
Pr(their union graph is disconnected | A_N^0)
 <=delta_N:=2^(N-3)(N!)^2 exp(-8N^2)<1/2.
```

Thus `A_N` is nonempty, is the smaller side, and

```text
pi(A_N)=(2/N!)(1+exp(-Omega(N^2))).
```

The tiny mass is fully oriented; it is not by itself a bottleneck.

## Exact one-step escape

Take `w in A_N`, set `a=t_k`, `b=t_(k+1)`, `c=t_(k+2)`, and
`P=t_1...t_(k-1)`.  Prefix renewal gives `Pa=id`, hence `P=a`.

- If `a!=b`, the legal right Hurwitz outcome
  `(a,b,c)->(b,bab,c)` preserves the block product and changes the midpoint
  prefix to `ab!=id`.
- If `a=b`, choose any transposition `d!=a` and use
  `(a,a,c)->(d,d,c)`.  Both block products equal `c`, while the new prefix is
  `ad!=id`.

A length-three fiber has at most `M^2`, `M=binom(N,2)`, states.  In the
original lazy kernel, selecting this block and the displayed outcome has
probability at least

```text
q_N=1/[6(m-2)M^2].
```

The output is outside `A_N` whether or not it remains connected.  Therefore

```text
Phi_pm^K(A_N)>=q_N,
```

an inverse polynomial in `N,m`.  This rejects the candidate.

Exactly `r-1` length-`r` windows straddle the midpoint: two for `r=3`, three
for `r=4`, and four for `r=5`.  For the relaxed prefix-only cut this gives
the complementary pointwise upper action rate

```text
K(w,(A_N^0)^c)
 <=(1/6)[2/(m-2)+3/(m-3)+4/(m-4)]=Theta(1/m).
```

For the connected restriction, noncrossing windows can additionally leave by
disconnecting support; that flow only makes the candidate worse and is not
silently omitted from any upper-bound claim.

## Finite falsification checks

The deterministic exact harness reproduces 27, 120, and 3,936 identity words.
At `S_3,m=4`, it finds nine prefix-renewal words, six connected ones, and
exact connected-cut conductance `7/18`.  At `S_4,m=4`, the relaxed cut has 36
states and conductance `7/20`, while the connected restriction is empty.
At `S_4,m=6`, the midpoint prefix length is odd and the renewal cut is empty.
Möbius counts agree with direct enumeration, and connected-pair counts become
positive at `(N,k)=(4,6)` and `(5,8)`.

Smallest remaining implication: establish or refute uniform inverse-
polynomial isoperimetry for **all** dense midpoint-prefix subsets, rather than
the singleton renewal level tested here.

