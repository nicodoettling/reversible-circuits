# M83 halfway checkpoint: endpoint influence still needs signed cancellation

Date: 2026-08-12. Convention throughout: `(pq)(x)=p(q(x))`; factors multiply
left-to-right. Target: the uniform minimal length-`n-1` bridge to the odd long
cycle, compressed to rank-two products and then simultaneous-long-cycle
conjugacy orbits. This is not the identity bridge.

## Status

The endpoint-sharing two-step bound remains **unresolved**. A simpler
one-step-Dobrushin route has been isolated exactly and then challenged by a
specific finite family whose scale is consistent with the known critical
Borel `n^-1/2` loss. The second step recovers the desired `n^-2` scale only
after cancellation between two large signed pieces; bounding either piece
separately fails.

## Proved reduction

Let `Lambda_n` be M80's endpoint-sharing graph and put

```text
alpha_n=max_(O~O') TV(bar K(O,.),bar K(O',.)).
```

M80 proved `diam(Lambda_n)<=4`. Therefore

```text
delta(bar K)<=4 alpha_n,
delta(bar K^2)<=delta(bar K)^2<=16 alpha_n^2.          (C1)
```

Thus `alpha_n<=A/n` would imply the assigned theorem with constant `16A^2`.
This is a rigorous four-schema alternative to a direct sixteen-schema bound.
It currently remains only a reduction, because the proposed `A/n` premise is
not established and appears false.

The equivalent signed-transport statement is also exact. For an edge
`O~O'`, write `eta=bar K(O,.)-bar K(O',.)`. If the Jordan transport of `eta`
is supported on pairs at `Lambda_n` distance at most `r`, then

```text
||eta bar K||_TV <= r alpha_n ||eta||_TV.
```

Generic diameter-four transport just reproduces (C1); the desired extra
power needs a sharper signed decomposition.

## Finite warning family

For `n=3k=3 mod 6`, define the adjacent source orbits

```text
A_k=[k,k,k]_3,
B_k=[1,k-1,k,k]_S.
```

They have residual sizes `(k,k,k)` and `(2k-1,k,1)`. Direct construction of
the quotient one-step rows gives:

```text
n          9       15       21       27       33       39       45       51
TV(K_A,K_B)
       .56818   .37029   .29387   .25098   .22286   .20267   .18728   .17503
sqrt(n) TV
       1.7045   1.4341   1.3467   1.3041   1.2802   1.2657   1.2563   1.2500
```

These are finite floating facts only, not an asymptotic refutation. They do
make the `A/n` route unsafe. Almost all of the discrepancy is on double
targets. The quotient event

```text
E_k={double target with residual sizes (1,u,n-1-u), 1<=u<=k-1}
```

has signed source-probability differences `.21314,.16198,.11619,.08661` at
`n=15,21,33,51`. This is consistent with the critical-Borel boundary tail.

## Signed two-step structure

For this family put `eta_k=K(A_k,.)-K(B_k,.)`. At `n=21`,

```text
||eta_k||_TV                         = .29387,
||eta_k K||_TV                       = .012698,
||eta_k 1_(E_k) K||_TV               = .080991,
||eta_k 1_(E_k^c) K||_TV             = .081413.
```

Thus neither boundary piece is individually smoothed to `n^-2`; their images
cancel. The corresponding values at `n=15` are `.10657,.10770` against a full
`.025045`. Any proof must therefore pair boundary-tail and complementary
schemas before taking absolute values. A simple `u`-layer triangle bound also
fails: its cumulative partial sums remain of order `n^-1/2` after `K`.

Floating optimal transport between the Jordan parts of `eta_k`, with cost
`TV(K_s,K_t)`, gives bounds `.16830` at `n=9` and `.05685` at `n=15`, versus
direct values `.09046,.02505`. The coupling upper bound itself has stable
`n^2` scaling in these two cases, but no simple one-edge support pattern:
only 53% and 35% of transported mass uses literal `Lambda_n` edges.

## Auxiliary exact support theorem (proved, not sufficient for M16)

For every odd `n>=9`, every quotient source and target are connected by an
explicit positive two-hop path through an oriented triangle; crude Cayley
count bounds give a polynomially positive entry. This proves full support and
a polynomial pointwise minorization of `bar K^2`. It does **not** imply the
needed `kappa_+=O(1/n)` and is not promoted as a solution. Likewise, an
`O(log n/n^2)` trace-two bound would give only
`kappa_+=O(sqrt(log n)/n)` and does not close the frozen M16 accumulation.
Both fallback implications were considered and explicitly rejected at the
required sharpness.

## Remaining standalone lemma

It suffices to prove either the original endpoint-sharing estimate or the
following strictly structured boundary cancellation statement:

> For every endpoint-sharing edge, the exact four-schema one-step signed
> measure `eta` admits a decomposition `eta=eta_boundary+eta_bulk` such that
> the two images cancel before absolute value and
> `||eta bar K||_TV<=C/n^2`, uniformly over all positive cyclic source gaps.

For the balanced/singleton family, the explicit boundary index is the smaller
residual part `u`; an Abel transform must keep the paired complementary image,
not bound boundary partial sums separately.

## Artifacts so far

- `influence_diagnostic.py`: exact through `n=9`, floating thereafter;
- `balanced_one_step_family.py`: direct focused family through `n=51`;
- `balanced_two_step_layers.py`: signed boundary/complement image analysis;
- `transport_diagnostic.py`, `optimal_transport_diagnostic.py`: finite flow
  tests;
- `doeblin_path_certificate.py`: exact finite audit of the auxiliary support
  construction.

No terminal, H0-gap, fixed-endpoint-gap, or identity-chain conclusion is made.

## Final-checkpoint addendum: the one-step shortcut is rigorously refuted

For `n=3k` with odd `k>=3`, the strict endpoint-sharing pair

```text
A_k=(0,k,2k),                 B_k=(0,1)(k,2k)
```

has a cyclic-invariant far-singleton target event `F_k` with
`bar K(A_k,F_k)=0`, while one explicit cross-cycle schema under `B_k` has
probability

```text
p_k ~ 4/(9 e sqrt(pi k)).
```

Consequently

```text
TV(bar K(A_k,.),bar K(B_k,.)) >= p_k = Omega(n^(-1/2)).
```

This is a proved asymptotic lower bound, replacing the finite warning above,
and it refutes the proposed one-step premise `alpha_n=O(1/n)`.  It does not
refute the assigned two-step estimate; the full signed sixteen-schema
cancellation remains open.  `balanced_tail_certificate.py` checks the exact
closed formula over the rationals through `n=33`.
