# M43 halfway checkpoint: canonical returns remove the segmentation loss

## Frozen candidate theorem

Use `(pq)(x)=p(q(x))`, word product `t_1...t_m`, and

```text
M=binom(N,2),               d=N-1,
E=binom(d,2),               m=4N^3+4,
a_*=floor(m/10^8).
```

For all sufficiently large `N` (the final statement will use an explicit
conservative threshold), the argument below combines with the already frozen
M42 prefix-occupation and boundary-surgery lemmas to give, simultaneously for
every `0<=a<=a_*`,

```text
pi(V^(a))<=exp(-4N^2),
Phi_pm^K(V^(a))>=N^(-25).                             (C.1)
```

Thus the literal disconnected-neighbourhood shells remain polynomially leaky
through a fixed positive fraction of the full word length.  In particular this
contains `N^(2+delta)` for every fixed `delta<1`.  This is not Terminal A or
Terminal B.

## 1. Canonical primitive-return coordinates

Fix the isolate `z=N` and `H=Stab(z)`.  For a word `w`, track

```text
X_j=(t_1...t_j)^(-1)(z).
```

Every crossing factor takes `X` from `z` into `[d]` or eventually returns it
to `z`.  Since the full word is the identity, its crossing factors decompose
uniquely into `c` primitive excursions.  Write their lengths as `l_j>=2`,
and write the numbers of internal factors before, between, and after them as
`g_0,...,g_c`.  Put

```text
q_j=ceil((l_j-1)/4),       Q=sum_j q_j,
h=#{j in [c-1]:g_j<=2},    k=c-h,       p=Q-h.        (C.2)
```

Here `k` is the number of maximal clusters separated by gaps of length at
least three.

**Lemma C.1 (exact path lower witness).**  If `w` is reached from an
`H`-internal word in at most `a` original local updates, then

```text
p=Q-h<=a.                                                (C.3)
```

Indeed, the overlap-connected hulls of the update windows have product in
`H` and cover every crossing.  Shrink them to their first and last crossing.
Starting at the globally first uncovered crossing, subgroup product forces
the right endpoint to be a return to `z`; induction therefore partitions the
canonical primitive excursions into consecutive groups.  A group of span
`L` covered by `u` windows satisfies `L<=4u+1`, hence costs at least
`ceil((L-1)/4)`.  Joining two consecutive primitive groups across a gap
`g` obeys

```text
ceil((L_1+g+L_2-1)/4)
 >=ceil((L_1-1)/4)+ceil((L_2-1)/4)-1_{g<=2}.           (C.4)
```

For `g>=3`, use `L_i>=4q_i-2`; for `g<=2`, the same lower bounds lose at
most one.  Iteration of (C.4) gives (C.3).

This is the missing exact segmentation inequality.  It also explains why
forbidding every intermediate return was wasteful: a long post-return gap
creates a new cluster and is not charged as active span.

## 2. Exact renewal cancellation

A primitive excursion of length `l` has exactly

```text
d(M-1)^(l-2)                                             (C.5)
```

realisations.  This is the inherited killed-state count: choose its first
crossing, each middle factor among the `M-1` choices not returning to `z`,
and its unique final return crossing.

Set

```text
A=(M-1)/E=(N+1)/(N-1),
D_A=1+A+A^2+A^3,
y=d/E^2.                                                (C.6)
```

Fix `p,k,h`.  Then `c=k+h` and `Q=p+h`.  Summing the four possible length
residues for each positive budget composition gives

```text
binom(p+h-1,k+h-1) A^(4(p-k))D_A^(k+h).                (C.7)
```

Choose which `h` of the `c-1` inter-excursion gaps are short and choose each
short length in `{0,1,2}`.  This contributes

```text
binom(k+h-1,h)3^h.                                     (C.8)
```

The crucial product is exact:

```text
binom(k+h-1,h)binom(p+h-1,k+h-1)
 =binom(p-1,k-1)(p)^(over h)/h!.                       (C.9)
```

Each extra close return also contributes `yD_A`.  Therefore all possible
numbers of close returns sum to

```text
sum_{h>=0}(3yD_A)^h (p)^(over h)/h!
 =(1-3yD_A)^(-p).                                      (C.10)
```

For `p<=a_*`, `N` sufficiently large, and the exact quantities (C.6),

```text
(1-3yD_A)^(-p)<=exp(2(3yD_A)p)
 <=exp(O(a_*/N^3))<2.                                  (C.11)
```

Thus intermediate returns cost only `exp(O(a/N^3))`, not
`exp(O(a/N^2))`.  The old factor `(M/(M-1))^(4a)` was caused by comparing a
canonical primitive source with the noncanonical arbitrary-middle block
upper bound.

## 3. Exact hard-rod layouts

After fixing all primitive blocks, all remaining factors lie in `H`.  Their
transposition sum is central, so for total internal length `G>=m-5a` the
inherited dense trace estimate gives at most `4E^G/d!` completions for the
required endpoint.

For the outer count with `k-1` long gaps, after fixing the `h` short gaps,
the leading gap, trailing gap, and long-gap excesses give

```text
binom(m-L-R-2k+3,k)<=binom(m-4p+3,k),                  (C.12)
```

where `R` is the sum of the short lengths.  The inequality uses

```text
L>=4Q-2c=4p-2k+2h.
```

For a clean primitive boundary source with `k` blocks, total budget `a`,
interblock gaps at least three, and four reserved trailing factors, the
number of layouts for prescribed total length `L` is exactly

```text
binom(m-L-2k-1,k).
```

Since `L<=4a+k`, it is at least

```text
binom(m-4a-3k-1,k).                                    (C.13)
```

Unlike the old replacement by `(m-8a)^k/k!`, comparing (C.12) and (C.13)
does not pay `exp(O(ak/m))`.

Define

```text
W_(a,k)=binom(a-1,k-1)y^k A^(4(a-k))D_A^k
          binom(m-4a-3k-1,k),
C=ceil(20sqrt(a)),
B_a=(1/2)(E^m/d!)sum_{k=1}^C W_(a,k).                 (C.14)
```

The robust-core argument is uniform in every fixed primitive layout and
endpoint, so `B_a` is a valid injective count of robust boundary sources.

For `p=a-r` and `k<=C`, put `n=m-4a-3k-1`.  The outer/source layout ratio is
bounded by

```text
binom(n+4r+3k+4,k)/binom(n,k)
 <=exp[k(4r+3k+4)/(n-k)].                              (C.15)
```

Here `log A>=1/N`, `4k/(n-k)<=1/N`, and
`k(3k+4)/(n-k)<=1`.  Hence the full fixed-`k` ratio is at most

```text
e exp(-3r/N),
```

and summing `r>=0` costs at most `2N`.  For `k>C`, the exact clean weight
ratio is at most

```text
[m yD_A/A^4]a/[k(k+1)]<=80a/[k(k+1)]<=1/5,            (C.16)
```

so its tail is geometric and is absorbed by the `k=C` term.  Combining
(C.10)--(C.16), the isolate-charged part of the literal shell is at most a
universal constant times `N B_a` for each `z`, and at most `N^3B_a` after a
conservative union over all isolates.

## 4. Remaining inherited pieces, rechecked at `a_*`

- The robust prefix core has length `t>=m-5a_*-4`.  In M42's kicked
  Johnson-walk estimate its away fraction is now
  `10a_*/t<2x10^(-7)`; the endpoint-conditioned failure remains below
  `exp(-0.75N^2)` uniformly in every layout and kick sequence.
- The final genuine `H_5` move pushes the last return crossing through the
  four reserved factors.  Primitive rigidity raises the isolate cost from
  `a` to `a+1`; prefix occupation excludes every alternative cut.
- For non-isolate smaller side `s<=N/4`, the old negative trace term
  `-5.6(s-1)N^2` dominates the enlarged active term
  `20as/N<=9x10^(-7)sN^2`.  For `s>=N/4`, `-0.8N^3`
  dominates the active `O(10^(-8)N^3)` term.  Those cuts contribute less
  than `B_a`.
- Direct division by `|Omega(N,m)|>=2M^m/N!` has leading logarithm
  `m log(E/M)<=-8N^2`; the isolate active term is at most
  `4a_*log A<=4x10^(-7)N^2`, and the layout term is `o(N^2)`.  Thus the
  smaller-side orientation in (C.1) survives.
- The specified heat-bath outcome has exact lower probability
  `1/[6(m-4)M^4]`; all omitted `Q_3,Q_4,Q_5` terms are nonnegative.

## 5. Current frontier and self-attack

The checkpoint now freezes a small but fixed linear radius.  It does not
control all `a=Theta(m)`: as the fraction `a/m` grows, the source layout
constant, non-isolate active entropy, isolate mass orientation, and the
prefix-occupation allowance must all be balanced simultaneously.  Near the
maximum distance the internal core is no longer dense.  Nothing here settles
the remaining large-fraction shells or the global spectral gap.

The strongest audit target is the use of canonical primitive decomposition
inside an arbitrary overlap-cluster path.  Equation (C.3) must be applied to
the globally ordered first uncovered crossing, not to an arbitrary
subinterval starting while `X_j!=z`; otherwise subgroup product would not
force a return to `z`.
