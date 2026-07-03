# Sampling Problem Reference

## Core Objects

Work in `S_N` unless the user chooses another reversible-circuit group. A length-`m` transposition circuit is a word

```text
w = (t1, ..., tm)
```

where each `ti` is a transposition. It computes identity when

```text
t1 t2 ... tm = id
```

with the implementation's multiplication convention documented in tests.

The canonical fixed-length target is

```text
Omega(N,m) = { w : all ti transpositions and eval(w) = id }
```

with uniform distribution on `Omega(N,m)`.

## Hurwitz Moves

A right Hurwitz move at position `i` replaces adjacent factors by

```text
(a,b) -> (b, b^-1 a b)
```

and the inverse move replaces

```text
(a,b) -> (a b a^-1, a).
```

For transpositions, conjugates remain transpositions, so these moves preserve length, product, and the transposition gate library.

Pure Hurwitz walks are only orbit samplers. They preserve the weighted connected-component invariant of the transposition graph and therefore generally cannot sample uniformly from all of `Omega(N,m)`. Treat this as a hard constraint, not a numerical accident.

## Breakout Moves

Use one or more orbit-breaking moves when the target is global rather than within-orbit:

- Global conjugation: replace every factor `t` by `sigma^-1 t sigma`. This relabels support but preserves weight profile.
- Square refresh: replace an adjacent `t t` block by `s s`; follow with Hurwitz scrambling.
- Null-block refresh: replace `t1 t1 ... tr tr` by `s1 s1 ... sr sr`.
- Fixed-length block resampling: choose `w = L B R`, compute `h = eval(B)`, and replace `B` by a sampled length-`r` transposition word with product `h`.
- Variable-length birth/death: insert or delete identity relators such as `s s` or `c r c^-1` under a declared Boltzmann/Gibbs target.

Fixed-length block resampling is the cleanest candidate for a stationary uniform identity-word chain when the block conditional is exact.

## Target Discipline

Do not mix targets informally. Decide which target is being tested:

- Uniform on all fixed-length identity words.
- Uniform on a Hurwitz orbit.
- Uniform conditional on an invariant class.
- Stationary law of a specific practical MCMC chain.
- Expected-length Boltzmann/Gibbs identity-word distribution.

If exact conditional sampling is replaced by a heuristic, define the resulting sampler distribution as the object under study.
