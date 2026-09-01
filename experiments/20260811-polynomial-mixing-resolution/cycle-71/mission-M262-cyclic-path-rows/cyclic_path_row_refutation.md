# M262 cyclic path-row refutation

Date: 2026-08-14 UTC. Status: **the stated CPR ascent/above-`v` transition is
refuted by an arbitrary-rank literal token family; the accepted M257/M260 raw
contexts remain valid**.

## 1. Source, convention, and scope

Every payload in M240/M242, M244/M247, M250/M254, and M257/M260 verifies at
the inventory digests recorded in `checkpoint.md`. The locked DPS PDF
verifies at

```text
98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2.
```

Only M257's M260-accepted CP-1--CP-6 raw contour contexts and M250's
M254-accepted canonical off-path substitution are used. White rotations
increase, black rotations decrease, and a local row is

```text
W_u^q S^e B_b^q -> S,             e in {1,3}.       (1.1)
```

Only `e=3` records the second black endpoint `x_b`. No distribution or
Markov kernel occurs in this note. The object is deterministic DPS closure.
The rank-dependent `a=1` row and final root completion are never entered.

## 2. An admissible family at every rank

Fix `rho>=8`, put `M=2rho-2`, and let `T_rho` have edges

```text
{1,rho}, {1,6}, {6,4},
{1,r} for 2<=r<=rho-1 and r not in {4,6}.            (2.1)
```

This is a tree on `[rho]`, rooted at the leaf `rho`, with `{1,rho}` its root
edge. Its parent data include

```text
p(4)=6,       p(6)=1,       P(4)=(4,6,1).           (2.2)
```

Choose the ordinary odd edit at `v=4`, namely swap labels `5,6`. Vertex `4`
has no rooted child. Since there is no `r>4` with `p(r)=4`, M250's declared
exposed set is

```text
E_4={R_4}={6}.                                      (2.3)
```

The vertex `6` is a strict internal nonroot vertex at both ranks `rho` and
`rho+1`. Thus the following computation lies wholly in CPR's assigned
CP-2--CP-5 path rows, not in RST.

## 3. Literal edited base

At `x_4`,

```text
L_4=5,       R_4=6.
```

There are no child intervals in CP-5. Its exact word is therefore

```text
I_4 =
 B_4^4 B_4^3 B_4^2 B_4^1 B_4^M B_4^(M-1) ... B_4^7
 S^6
 W_4^7 W_4^8 ... W_4^M W_4^1 W_4^2 W_4^3 W_4^4 W_4^5
 S^6 S^5.                                           (3.1)
```

This is the actual token word. In particular, label `6` is carried by the
two tree sides at the reversed slot and has no `W_4^6` or `B_4^6` half-edge.

## 4. The nonroot `4 -> 6` row

At the canonical parent `a=6`,

```text
L_6=9,       R_6=10,       kappa(4)=L_4=5.          (4.1)
```

The last equality is CP-1 and is the essential reversed-child incidence.
There is no other rooted child of `6`. Substituting (3.1) into CP-2 gives

```text
S^9
W_6^10 W_6^11 ... W_6^M W_6^1 W_6^2 W_6^3 W_6^4
S^5

B_4^4 B_4^3 B_4^2 B_4^1 B_4^M ... B_4^7
S^6
W_4^7 W_4^8 ... W_4^M W_4^1 ... W_4^5
S^6 S^5

W_6^6 W_6^7 W_6^8
S^9
B_6^8 B_6^7 B_6^6 B_6^5 B_6^4 ... B_6^1
B_6^M ... B_6^11
S^10.                                                (4.2)
```

Every ellipsis is an explicitly monotone cyclic interval; it may be expanded
at any `M>=14` without changing the following induction.

### 4.1 Left chain

Starting next to the child cut, close labels in the order

```text
4,3,2,1,M,M-1,...,10.
```

The first row is `W_6^4 S^5 B_4^4`; each later row has the side just created
by its predecessor. Hence every row is literally

```text
W_6^t S B_4^t -> S                                  (4.3)
```

at distance one. It leaves `S^9 S_A B_4^9 B_4^8 B_4^7`, where `S_A` is the
last closure side. This is an arbitrary-length induction over the displayed
decreasing interval.

### 4.2 Right chain and the exposed label

From the right, labels `8,7,6` close successively against `x_6`. Each sees
only `S^9` or the side produced by the preceding row, so

```text
W_6^8 S B_6^8 -> S,
W_6^7 S B_6^7 -> S,
W_6^6 S B_6^6 -> S.                                 (4.4)
```

All three have distance one. The last row in (4.4) is the unique row for the
exposed label `6` inside this internal context.

Next, `W_4^5` has precisely the two old sides `S^6,S^5` and the side created
by the label-`6` row before `B_6^5`. Thus

```text
W_4^5 S S S B_6^5 -> S                              (4.5)
```

has distance three and records `x_6`, but it concerns label `5`, not the
exposed label `6`. Finally labels

```text
4,3,2,1,M,M-1,...,11
```

close one by one at distance one against `x_6`. This second arbitrary-length
induction leaves one closure side `S_C`.

### 4.3 Exact residual

The complete bottom-up deletion of (4.2) is therefore

```text
S^9 S_A
B_4^9 B_4^8 B_4^7
S^6
W_4^7 W_4^8 W_4^9 W_4^10
S_C S^10.                                            (4.6)
```

Every deletion above is a complete local node: its half-edges are
consecutive among the remaining half-edges and only the displayed one or
three sides lie between them. M250's accepted complete-node commutation
therefore licenses this order.

Formula (4.6) is a second literal open frontier. It is not the sealed
canonical residual

```text
S^9 W_6^10 S S.                                     (4.7)
```

More decisively, (4.4) proves that exposed label `6` has only a distance-one
row at this first ascent/first path vertex above `v`. It acquires no second
black endpoint before the root seam.

## 5. Why the family is all-rank and rank-coupled

The proof uses `M` only as the end of two reverse-ordered chains. Replacing
`rho` by `rho+1` replaces `M` by `M+2`. The new labels `M+1,M+2` occur once
in (4.3) and once in the final distance-one chain; both disappear before
the residual (4.6) is reached. Thus (4.4) and the inherited low-token
residual (4.6) hold identically at both ranks for every `rho>=8`.

This is a symbolic interval induction, not finite-rank interpolation. The
minimal checker accompanying this note replays only the literal rank-eight/
rank-nine instance as a falsification guard; the checker is not evidence for
the universal quantifier.

## 6. Refuted claim and exact repair

M257's CPR required that the first step with current child `c<a`, including
the first path vertex above `v`, give every `e in E_v` a distance-three
endpoint before the root seam and leave state `C`. In (2.2), `c=4<a=6`, but
(4.4) gives distance one for the sole `e=6`, while (4.6) remains open.
Therefore that CPR transition is **REFUTED**.

The raw M257/M260 contexts CP-1--CP-6 are not refuted; they are precisely
what yields the counterfamily. Nor does this refute IDL or the finite
endpoint identities already checked at small ranks: the later `a=1` row may
still make the full endpoints agree.

The first repaired state space must distinguish at least

```text
O^- : a literal open frontier whose current path vertex a satisfies a<v,
O^+ : a literal open frontier whose current path vertex a satisfies a>v.
                                                               (6.1)
```

Entering `O^+` does not necessarily seal an exposed label. A later internal
row can sweep across the exposed cyclic sector, but in the admissible path
`v<a->1`, the actual `O^+` word reaches the root seam. Consequently the old
RST input described only as `O` or `C` is under-specified: its input must be
the literal directional frontier, or a separately proved sufficient
quotient of that word. A refined signed/directional transducer may still
prove the desired endpoint tables.

## 7. Status

```text
PROVED:
  the arbitrary-rank family (2.1)--(2.3);
  exact CP-2/CP-5 deletion (4.2)--(4.6);
  exposed label 6 has a distance-one, not distance-three, internal row;
  the same inherited residual at ranks rho and rho+1.

REFUTED:
  CPR's stated first-ascent/first-above-v O -> C metric transition;
  the sufficiency of its unrefined O/C partition for the subsequent RST.

UNRESOLVED:
  a refined O-/O+ (or stronger) path transducer;
  literal root tables for every refined input;
  hence RSPT, repaired RSMI+, and IDL.

NOT CLAIMED:
  fixed edits; every-color synchronization; route length or congestion;
  a spectral gap; polynomial mixing; Terminal A or Terminal B.
```
