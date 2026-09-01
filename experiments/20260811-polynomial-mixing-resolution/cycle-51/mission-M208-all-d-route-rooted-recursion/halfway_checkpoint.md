# M208 halfway checkpoint: exact one-leaf correction found at d5->d6

Date: 2026-08-13 UTC.

## Immutable gate

M181/M183, M196/M198, M200/M202, and M203/M205 all passed their full frozen
SHA inventories. No predecessor was edited.

## Exact descriptor extension

For both M181 d=5 patterns at the distinguished root, the recovered rooted
DPS descriptors share the order

```text
pi_5=(7,8 | 1,2 | 3,4 | 5,6).
```

The d=6 source descriptor is obtained exactly by adjoining edge `{1,6}` to
the Cayley tree, changing the root from 5 to 6, and rotating the pair on old
child 1 into the new child-5 slot:

```text
pi_6=(9,10 | 1,2 | 3,4 | 5,6 | 7,8).
```

Thus adjoining `(05)^2` is simple in rooted product coordinates even though
M203/M205 proved it is not simple after physical DPS closure.

## Exact synchronized endpoint corrections

Let `N_i` be the pair of naively stabilized d=5 targets (patterns 0 and 1),
and `A_i` the pair of actual d=6 targets. A targeted diagonal signed-Hurwitz
MITM found and exactly replayed common physical correction words `C_i` with

```text
i        1   2   3   4   5   6   7
|C_i|   13   0   9   0   5   2   1.
```

Using one-based Hurwitz generator indices and signs:

```text
C_1=R2 R3 R4^- R5^- R6^- R7 R8^- R7^- R6^- R5 R4 R3^- R2^-
C_2=id
C_3=R4 R5 R6^- R7 R8^- R7^- R6^- R5^- R4^-
C_4=id
C_5=R6^- R7 R8^- R7^- R6^-
C_6=(R5^-)^2
C_7=R8^-.
```

These are positive certificates, not coverage evidence from search. In
particular `C_1=A C_5 A^-1` with
`A=R2 R3 R4^- R5^-`, and `C_3=(R4 R5) C_5 (R4 R5)^-1`, exhibiting a
contour-transport pattern. The radius misses used before finding `C_1` have
no negative interpretation.

## Remaining bounded audit

Test these schedules against every d=5 Cayley tree compatible with the same
root-extension edge/order template. If they fail, archive the first exact
tree obstruction. If they pass, freeze only the resulting exact finite
template theorem and state the still-unproved general-d contour recurrence.
No `Q_6` enumeration or route-length asymptotic inference is permitted.

