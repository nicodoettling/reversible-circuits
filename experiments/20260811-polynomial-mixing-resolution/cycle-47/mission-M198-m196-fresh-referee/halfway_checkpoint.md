# M198 halfway checkpoint

Date: 2026-08-13 UTC.

## Completed gate

All thirteen M196 payload entries pass `sha256sum -c`; the immutable
`SHA256SUMS` digest is

```text
7fa987c6c776e55990c00fcfaea85e34c1d7b0e6d3f97d57fdefba8bcb5bd913.
```

No M196 file was edited.

## Exact audit formulation

The independent checker will not import any M196 or M191 Python module. It
will reconstruct the 8,400 canonical `Q_5` states from the physical source
word under signed Hurwitz moves, rebuild and compare all fourteen action rows,
reconstruct the ten rooted DPS descriptions and the resulting 54 named target
pairs, and build its own chronological first-coordinate BFS transversal.

For every adjusted target certificate it will check, literally,

```text
(16,0)^f = meeting,
(16,z)^b = meeting,
h = f reverse_and_negate(b),
(16,0)^h = (16,z).
```

For every original target it will recompute `z=u'^(alpha^-1)`, check
`w=h alpha`, and replay `(16,0)^w=(v',u')`. It will independently rebuild the
radius-eight forward ball and audit all counts, digests, deduplication, and
maximum lengths.

No miss or orbit complement will be interpreted, and no full `Q_5^2` or
stabilizer orbit will be enumerated. No verdict has yet been assigned.
