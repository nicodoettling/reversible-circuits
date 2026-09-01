# M42 plan: linear-shell mechanism versus genuine transition

## Exact target

Use `(pq)(x)=p(q(x))`, `m=4N^3+4`, the uniform identity bridge, and the
literal lazy `{3,4,5}` kernel.  Prove inverse-polynomial conductance for the
actual neighborhoods `V^(a)` on a range genuinely larger than `N^2/100`
(preferably `N^(2+delta)` or a constant fraction of `m`), or prove a literal
Terminal-B sequence with exact orientation and complete `H_3/H_4/H_5` flow.

## First structural question

The M40 cut-multiplicity certificate is limited to `Theta(N^2)` because a
length-`4N^3` internal word has only `Theta(N^2)` factors incident to its
least-used vertex.  Determine whether this is merely a certificate failure.

For a cut `P` and a word `w`, track the prefix image of a cut side.  If `w`
is reached from a `P`-internal word by `u` local updates, every time at which
the prefix image differs from the original side lies inside an active-cluster
hull.  Since `u` windows have total hull span at most `5u`,

```text
dist_K(w, Omega_P)>=A_P(w)/5,
```

where `A_P(w)` is the number of prefix times away from the cut stabilizer.
Unlike edge multiplicity, a dense random core should have
`A_P(w)=Theta(m)` for every nontrivial cut.

## Proof route

1. Prove the prefix-occupation lower bound with exact hull conventions.
2. For the isolate-source construction, delete the primitive blocks and view
   their `H=Stab(z)` products as deterministic kicks between uniform internal
   transposition segments.  Prove a uniform large-deviation bound for the
   occupation of every nontrivial subset under this kicked Bernoulli--Laplace
   walk, paying the endpoint-conditioning factor `d!` and all `2^d` cuts.
3. Preserve the exact M37/M40 layout and source entropy.  Refine the outer
   comparison if the pointwise `(M/(M-1))^(4a)` loss becomes superpolynomial;
   canonical first-return decomposition and exact hard-rod layouts are the
   preferred repair.
4. If the kicked occupation or entropy balance reverses, orient the resulting
   literal shell and count every full-kernel boundary transition before
   considering a Terminal-B claim.

## Primary named lemmas

> **PREFIX-HULL LOWER BOUND.**  Every path of `u` updates from a word internal
> to `P` to `w` satisfies `A_P(w)<=5u`.

> **KICKED SUBSET OCCUPATION.**  For `t=Theta(N^3)`, at most
> `exp(-cN^2)E^t` internal transposition words, uniformly over deterministic
> `H`-kicks and every nontrivial subset, spend a fixed positive fraction of
> their prefix times in that subset's stabilizer.

> **ENTROPY-MATCHED FIRST-RETURN SHELL.**  Canonically splitting isolate
> blocks at prefix returns absorbs the former
> `exp(Theta(a/N^2))` primitive entropy loss with only polynomial source/outer
> ratio.

## Resource audit

Search local sources first, then primary literature for concentration of
occupation times for Bernoulli--Laplace/random-transposition walks under
deterministic permutation kicks, Feynman--Kac operator bounds, and
first-return renewal or hard-rod shell enumerations.  Record exact theorem
hypotheses and constants; homogeneous-chain concentration is not automatically
valid with kicks.

## Failure modes

- Prefix occupation at factor times may not be controlled by active-cluster
  hulls under the chosen multiplication convention.
- Deterministic block products may reset the subset process often enough to
  destroy a homogeneous concentration theorem.
- Endpoint conditioning may cost `d!` once or once per segment; only the
  former is affordable.
- A polynomial action theorem still needs a source family comparable to the
  whole shell, not merely typical robust cores.
- Conductance is not monotone, and a slow auxiliary prefix process is not
  Terminal B.

## Deliverables

- `checkpoint.md`
- `resource_audit.md`
- `report.md`
- exact computations only if they falsify a named algebraic or spectral
  statement.
