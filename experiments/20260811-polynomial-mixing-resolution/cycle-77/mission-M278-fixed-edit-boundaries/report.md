# M278 report: fixed-edit DPS boundaries

Date: 2026-08-14 UTC.

## Verdict

**PROVED ANALYTICALLY; PROMOTE TO FRESH AUDIT.**

For every `d>=5` and every tree on `[d]` rooted at the leaf `d` with
root edge `{1,d}`, the three fixed edit families have the claimed
old-padded-to-new DPS routes:

```text
internal even i<=2d-6 : identity;
i=2d-4                : (R_(2d-5)^(-1))^2;
i=2d-3                : R_(2d-2)^(-1).
```

This verdict is restricted to the local rooted-row DPS comparison.  It is
not an every-color or global routing assembly.

## Immutable gate

Every payload in the frozen inventories M225/M228, M231/M234, M236/M237,
M240/M242, M269/M271, and M273/M275 verified before use.  Their top-level
inventory digests and the locked DPS digest are recorded in
`checkpoint.md`.  The DPS source is
`/tmp/DuPoSc13.pdf`, SHA-256
`98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2`.
No predecessor was edited.

## Exact boundary shapes

Put

```text
m=2d-2, alpha=m-1, beta=m, gamma=m+1, delta=m+2,
g=(0,d-1), k=(0,d).
```

For `i=m-2`, put

```text
j=m-3, h=(d-2,p(d-1)-1), a=ghg, b=aga.
```

All earlier factors agree, and the literal tails are

```text
N_(j,...,delta)=[a,b,a,g,k,k],
A_(j,...,delta)=[h,g,a,g,k,k].
```

The unconditional calculation is

```text
[a,b,a] --R_j^(-1)--> [g,a,a]
        --R_j^(-1)--> [h,g,a].
```

It remains valid when `h,g` are disjoint and does not invoke M240's
overgeneralized tuple simplification rejected by M242.

For `i=m-1`, the exact four-factor seam is

```text
N_(alpha,beta,gamma,delta)=[g,g,k,k],
A_(alpha,beta,gamma,delta)=[g,gkg,g,k],
```

and `R_beta^(-1)` sends the source pair `[g,k]` to `[gkg,g]`.
All signs are negative and all actions are chronological left to right.

For `i=2v-2<=m-4`, put

```text
e=(v-1,p(v)-1), f=(v,p(v+1)-1).
```

The old and new windows at `i-1,...,i+2` coincide:

```text
p(v)=p(v+1): [e,f,fef,f];
p(v+1)=v:    [e,efe,e,f];
p(v)=v+1:    [c,e,c,f], c=fef=efe;
otherwise:   [e,f,e,f].
```

These four incidence classes are exhaustive.  The all-rank proof contracts
complete nested DPS intervals outside the two edited slots and applies the
literal LIFO distance-one/distance-three endpoint scan to the four remaining
incidence skeletons.  Extension changes only `p(1)`, whereas
`2<=v<=d-2`, so the source and target skeletons and every endpoint agree.

`fixed_edit_boundary_theorem.md` gives the full first-/second-black
endpoint tables for both cross-boundary regimes, the old root, the new child
`d`, the new root, final-root defaults, the numeric post-wrap, forward and
inverse chronology, and the minimal rank `d=5`.

## Post-proof guard

The formula was frozen before `guard.py` was written or run.  The guard
imports no predecessor and performs no route search.  It independently
reconstructs RandomQuad Steps 3--4 for exactly `d=5,6`.

```text
d=5: 16 trees; 32 internal, 16 cross-boundary, 16 last rows.
d=6: 125 trees; 375 internal, 125 cross-boundary, 125 last rows.
total: 141 trees; 407 internal, 141 cross-boundary, 141 last rows.
```

All rows pass.  All four internal incidences occur: at `d=5`, each occurs
8 times; at `d=6`, common-parent/disjoint/next-child/previous-child occur
`75/150/75/75` times.  The `p(d-1)=1` versus not-`1` boundary counts
are `8/8` at `d=5` and `50/75` at `d=6`.  This is a
transcription/boundary falsifier, not the arbitrary-rank proof.

Command:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-77/mission-M278-fixed-edit-boundaries/guard.py
```

Python `3.12.3`.

## Formal composition

The currently licensed ordinary chain is:

1. accepted M269/M271 plus accepted standalone DL-RST M273/M275 establish
   the ordinary endpoint output while replacing false M250 (4.2);
2. M250/M254 conditional endpoint exhaustion gives ordinary IDL; and
3. M240/M242 gives the ordinary odd-edit route
   `Q(v,epsilon)B_dQ(v,epsilon)^(-1)` of length
   `4(d-v-1)+5<=4d-7`.

Subject to a fresh acceptance audit of M278, adjoining the fixed route
lengths `0,2,1` formally covers every adjacent edit index in the local
rooted-row table, still with maximum length `4d-7`.

No claim is made here about every-color synchronization, voltage correction,
other routing obligations, congestion, a spectral gap, polynomial mixing,
or Terminal A/B.  Those remain open and require a separate audited assembly.
