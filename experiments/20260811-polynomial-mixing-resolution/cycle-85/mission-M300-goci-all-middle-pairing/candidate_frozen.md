# M300 frozen candidate: middle cut-length phase pairing

Date: 2026-08-14 UTC.

Status: frozen before any M300 computation.

## Reconstructed channel-one interface

Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, odd `k>=3`,
`n=3k`, and `2<=ell<=n-2`. With

```text
L=(1,...,k-1,2k,...,3k-1),       M=(k,...,2k-1),
C_-=(0,...,k-1),                 C_+=(2k,...,3k-1),
```

and the accepted first-chord laws `nu_C`, define

```text
gamma_k(e)=nu_L(e)
 -1/2 1[e in T(C_-)]nu_(C_-)(e)
 -1/2 1[e in T(C_+)]nu_(C_+)(e).
```

Direct expansion of the normalized channel-one laws gives the always-safe
atom-summed identity

```text
eta_1(F_ell)
 =sum_(f in T(M)) nu_M(f) sum_e gamma_k(e)F_ell(ef).       (1)
```

Every channel-one `e` is exterior and every `f` is middle, so their supports
are disjoint and `ef` is a double. In this designated role decomposition,
the cycles of `ef` recover `e` and `f`, and one may abbreviate the
corresponding product coefficient as

```text
beta_1(ef)=gamma_k(e)nu_M(f).
```

This is not a statement that an unrestricted rank-two product has one raw
ordered lift: a double has two and a triangle has three. Channel one has
already conditioned/summed its two commuting color orders. Equation (1),
not an unrestricted scalar-beta shorthand, is the controlling identity.

## Named candidate `(MCLP_1)`

Write the middle vertices as `m_a=k+a`, with `a` in `Z/kZ`. Since `k` is
odd, every unordered middle chord has a unique representation

```text
f_(a,u)={m_a,m_(a+u)},       1<=u<k/2.
```

Its chord-law mass depends only on `u`:

```text
w_(k,u)=tau(u)tau(k-u)/[(k-1)tau(k)] > 0.
```

Define the complete middle-phase orbit coefficient

```text
P_(k,ell)(u)
 =sum_(a in Z/kZ) sum_e gamma_k(e)F_ell(e f_(a,u)).          (2)
```

The fixed candidate is

```text
(MCLP_1)  P_(k,ell)(u)>=0
```

for every odd `k>=3`, `1<=u<k/2`, and `2<=ell<=3k-2`.

This retains cancellation across every middle-chord phase of one cut-length
class. It is strictly weaker than the refuted fixed-middle candidate and is
neither raw atomwise positivity, conditioned Borel monotonicity/FOSD, nor a
signed-PSD assertion. The unique chord partition gives exactly

```text
eta_1(F_ell)=sum_(1<=u<k/2) w_(k,u) P_(k,ell)(u).             (3)
```

All weights in (3) are positive, so `(MCLP_1)` would imply `(GOCI_1)`.
Statewise lag reflection gives
`P_(k,ell)(u)=P_(k,n-ell)(u)` and retains both endpoints.

## Sole predeclared exact falsifier

Test exactly `k=7` (`n=21`), its three cut-length classes, and all
admissible lags, using exact rational arithmetic. Check literal residual
cycles against the repaired owner-autocorrelation identity. Do not scan a
second rank. If `(MCLP_1)` fails, freeze the first exact class witness. If it
survives, freeze (2)--(3) as the first exact all-middle coefficient reduction
and keep the all-rank sign unresolved unless a separate proof closes.
