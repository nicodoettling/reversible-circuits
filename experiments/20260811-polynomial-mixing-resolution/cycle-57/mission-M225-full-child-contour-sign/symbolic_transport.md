# M225 symbolic transport audit

## Carrier calculation

For the four-factor input

```text
(xy),(zx),(zy),(zn)
```

the five chronological actions

```text
R_p^-, R_(p+1), R_(p+2)^-, R_(p+1)^-, R_p^-
```

produce

```text
(xy,zx,zy,zn)
(zy,xy,zy,zn)
(zy,zy,zx,zn)
(zy,zy,xn,zx)
(zy,xn,zy,zx)
(xn,zy,zy,zx).
```

This proves the carrier identity (2.1) of `candidate_descriptors.md`.

## Child-sign transport rule

The local conjugator advances the carrier across a doubled slot by a pair of
same-sign adjacent generators. In the canonical rooted order, an absent
larger child crosses the next contour side and reverses orientation relative
to the preceding stage; a present larger child meets the edited vertex side
and fixes the orientation to inverse. This gives exactly

```text
present -> epsilon=-1,
absent  -> epsilon=-previous epsilon,
```

with initial absent orientation positive. This is the automaton (1.2). It is
a predeclared local transport hypothesis for the DPS closure; the formal braid
calculation proves what its word does once the asserted local factor shape is
present, while the complete finite replay will test whether the descriptor
correctly identifies that shape.

## Contour identity rule

An internal ascent in the stopped path is predeclared to close the edited
boundary pairing before the leaf carrier is engaged, yielding `N=A` and hence
the identity correction. A strictly decreasing internal path is assigned the
carrier correction unless a larger-than-`v` path vertex triggers the already
known late-ancestor closure.

This is a falsifiable local DPS-closure hypothesis, not an all-rank proof. The
finite checker must test both the asserted `N=A` cases and every nonidentity
carrier replay literally.

