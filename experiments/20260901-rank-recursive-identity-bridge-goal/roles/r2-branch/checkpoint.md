# R2 substantive checkpoint

Date: 2026-09-01 UTC

## Decisive claim

A positive, labeled, polynomial-state **dense approximation** to the exact
`(k,h)` branch law has been derived.  It is uniform over the arbitrary external
endpoint `g`; it does not enumerate `S_(N-1)` or partitions.  The construction
uses complementary old-long and star-long branches, so one endpoint walk is
always pointwise mixed for every `k`.

Let

```text
r=N-1, d=binom(r,2), b=N-1, s=L-k, a=g^(-1)(N).
```

Let `S_k(a)` count star words with endpoint `q` satisfying `q(a)=N`.  It has
the exact positive two-state recurrence

```text
u_0=1, v_0=0,
u_(j+1)=(N-1)v_j,
v_(j+1)=u_j+(N-2)v_j,
S_k(a)=u_k if a=N, and v_k otherwise.
```

After a single common scaling, sample `k` with integer weight

```text
N binom(L,k) d^s S_k(a),   s>=k,
  binom(L,k) d^s b^k,      k>s.                            (Q)
```

- In the old-long case, sample a uniform star word subject to `q(a)=N` by a
  token-bridge backward sampler and return the actual labeled
  `h=gq^(-1)`.
- In the star-long case, draw `s` independent uniform old transpositions and
  return their actual product `h`.

The first case replaces `A_(r,s)(h)` by parity-uniform while retaining the
exact `B_(N,k)(h^(-1)g)` law.  The second retains exact `A` while replacing
`B` by parity-uniform.  Thus this is a positive sampler, not a signed character
calculation.

## Uniform TV theorem at checkpoint

Fourier inversion with the trivial/sign modes separated gives pointwise
relative errors

```text
delta_old(r,s) <= (r!-2)/2 * ((r-3)/(r-1))^s,
delta_star(N,k)<= (N!-2)/2 * ((N-2)/(N-1))^k,
```

with the evident exact low-rank exceptions.  The first eigenvalue bound is the
transposition character-ratio bound.  The second follows because `J_N` acts in
the Young/Gelfand--Tsetlin basis by the content of the box containing `N`; all
nontrivial/nonsign contents have absolute value at most `N-2`.

Put

```text
Delta = max(delta_old(N-1,ceil(L/2)),
            delta_star(N,floor(L/2)+1)).
```

If `Delta<1`, every approximate branch has valid support and normalization
gives

```text
d_TV(Q, exact branch law) <= Delta/(1-Delta),               (TV)
```

uniformly over every feasible `g`.  At `L=2N^3`, for every `N>=4`, elementary
exponential estimates give

```text
Delta <= exp(-N^2/2),
d_TV <= 2 exp(-N^2/2).
```

This is a proved negligible dense-branch guarantee.  It is not yet a sampler
theorem for the full rank recursion: the R4/R5 lane must show that every
internal call stays in a length/error regime where `(TV)` composes.  Also, at
fixed `L` this does not support an arbitrarily smaller user-specified
`epsilon`; it supports `epsilon` whenever the explicit `Delta` is at most
`epsilon/(1+epsilon)`.

## Effect of the final R3 report

The finalized R3 result supplies an exact polynomial-time conditional
`StarSample(N,k,h^(-1)g)`.  In the old-long case `(Q)` already produces the
star word.  In the star-long case R3 can be applied after choosing `h`; when
`Delta<1`, pointwise support equality guarantees the requested star fiber is
nonempty.  Applying the same exact conditional kernel preserves the branch TV
distance.  R3 therefore closes conditional star generation but does not make
the exact `h` law polynomial by itself.

## Exact compression and scoped state obstruction

The exact positive type-cell representation is

```text
M_g(lambda,mu)=#{h in H: type(h)=lambda,
                          pointed_type(h^(-1)g)=mu},
weight=binom(L,k) A_s(lambda) B_k(mu) M_g(lambda,mu).
```

There are `p(N-1)` lower cycle types and
`sum_(u=0)^(N-1)p(u)` pointed types.  An explicit rectangular table therefore
has their product in its declared inventory; even for `g=e`, exactly
`p(N-1)` set-theoretically nonempty cells remain.  Since
`p(n)>=2^Omega(sqrt(n))` by the subset-plus-ones injection, the implementation
that materializes these cells is superpolynomial.  This is not a hardness
claim: a direct positive connection-coefficient sampler remains the exact
surviving alternative.

## Exact computational checkpoint

`branch_audit.py` completed under Python 3.12.3 with no nonstandard package:

```text
/usr/bin/time -v python3 experiments/20260901-rank-recursive-identity-bridge-goal/roles/r2-branch/branch_audit.py --max-small-n 5 --max-small-length 8 --dense-n 4 5 --output experiments/20260901-rank-recursive-identity-bridge-goal/roles/r2-branch/results.json
```

It recorded:

- 1,368 exact `(D)` branch-normalization/feasibility checks;
- 532 exact TV calculations for feasible small fibers;
- 126 exact star-coset/token recurrence checks;
- 1,911 labeled sampler smoke checks;
- every feasible endpoint at `(N,L)=(4,128)` and `(5,250)`.

Maximum exact dense TV was `6.862e-13` at `N=4` and `1.004e-19` at `N=5`,
below the proved pointwise bounds `3.940e-11` and `1.068e-14`.  These finite
values corroborate but do not prove the theorem.

Checkpoint verdict: `promote` for the dense R2 branch theorem; exact R2 at
arbitrary feasible short lengths remains reduced to the positive labeled
connection primitive.
