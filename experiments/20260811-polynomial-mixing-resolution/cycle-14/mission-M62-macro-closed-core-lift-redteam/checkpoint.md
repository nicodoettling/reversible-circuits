# M62 halfway checkpoint: complement-symmetry closure

## Correction to the inherited frontier

The proposed macro-closed loophole is already closed by the exact M60
theorem.  Let `A` be any subset of `F_N`, core-defined or otherwise, and put

```text
S =F_N^c union A,
S'=F_N^c union (F_N minus A).
```

Then exactly

```text
S^c    =F_N minus A subseteq F_N,
(S')^c =A subseteq F_N.                              (C.1)
```

For every Markov chain and stationary law,

```text
Q(S,S^c)=Q(S^c,S),
min{pi(S),pi(S^c)}=min{pi(S^c),pi(S)},
```

so two-sided conductance is complement invariant.  Applying M60 Claim C to
the right sides of (C.1) gives, whenever `A` is nonempty and proper in `F_N`,

```text
Phi_pm^K(S), Phi_pm^K(S')
 >=1/[2|R_m|N(N-1)Lambda_N(m-2)M^3]
 >=1/(24N^13),

Lambda_N=binom(2N-2,2)(N-1)^2,
M=binom(N,2).                                        (C.2)
```

No assumption about which displayed set is the smaller side is needed.  The
M60 proof gives `Q(B,B^c)>=c_N pi(B)` for every `B subseteq F_N`; since
`min{pi(B),pi(B^c)}<=pi(B)`, its two-sided bound holds even when `B` is the
larger side.

This is an append-only correction to the M60 report's named next gap and
self-attack, which incorrectly said absorbing the exits from `A` left the
macro-closed lift open.  Those particular exits are absorbed, but the
opposite minimal-macro side in (C.1) has its own M60 boundary certificate.

## Exact N=5 calibration

For the N=5 path fiber, the eight core-component sizes are

```text
1068,1068,997,997,997,997,842,842.
```

An exactly half-fiber union has

```text
|A|=1068+997+997+842=3904=7808/2.
```

Using `|Omega(5,8)|=1,770,940`, `|F_5|=1,008,000`, and
`|F_5^c|=762,940`, the two placements have exact side sizes

```text
S:   766,844 versus 1,004,096,
S':  1,767,036 versus 3,904.
```

The exact constant in (C.2) at N=5 is

```text
1/[6*20*448*6*1000]=1/322,560,000.
```

The finite component flows are calibration only; (C.2) is universal and
uses the exact lazy H3 normalization, with every H4/H5 contribution retained
as nonnegative.

