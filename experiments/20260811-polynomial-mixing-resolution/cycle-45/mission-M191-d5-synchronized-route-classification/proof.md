# Exact reduction and capped d=5 classification attempt

Date: 2026-08-13 UTC.

## 1. Scope

Let `X=Q_5` be the global-conjugacy quotient of connected product-one
eight-transposition words. Let the signed Hurwitz generators act on the right,
chronologically. Fix the ordered source pair

```text
v=[(01)^2(02)^2(13)^2(04)^2],
u=[(01)^2(02)^2(03)^2(04)^2].
```

Only diagonal component membership in `X^2` for the 54 named M188 targets is
at issue. All stale geometric all-`d` claims from M187 are excluded.

## 2. Stabilizer-orbit criterion

### Proposition 2.1 (exact finite reduction; proved)

For a target `(v',u')`, fix any action word `alpha(v')` with
`v^alpha=v'`. Then

```text
(v',u') in Orb_diag(v,u)
iff
u'^(alpha^-1) in Orb_Stab(v)(u).                       (2.1)
```

Here the exponent denotes the right action.

**Proof.** Suppose `b` sends `(v,u)` to `(v',u')`. Then
`b alpha^-1` fixes `v`, and

```text
u^(b alpha^-1)=u'^(alpha^-1).
```

Thus the adjusted second target is in the stabilizer orbit. Conversely, if
some `h in Stab(v)` sends `u` to `u'^(alpha^-1)`, then `h alpha` sends
`v` to `v'` and `u` to `u'`. QED.

Changing `alpha` multiplies the adjusted target by an element of the same
stabilizer, so membership is independent of the tree choice. A positive
certificate consists of words for `h` and `alpha`; their concatenation is the
desired synchronized braid. A negative certificate consists of the exact
stabilizer orbit plus an adjusted target outside it.

## 3. Complete one-coordinate action

The rooted DPS bijection gives

```text
|Z_5|=5^(5-3) 8!=1,008,000.
```

Global `S_5` conjugation is free on connected words, so

```text
|Q_5|=1,008,000/5!=8,400.                              (3.1)
```

The independent script starts at `v` and closes under all fourteen signed
Hurwitz generators, canonically quotienting by all 120 label permutations.
It finds exactly 8,400 states, hence is complete by (3.1). Every generator is
a permutation and each negative generator is the computed inverse of its
positive partner. The action digest is

```text
160bcae167e754af4ff55356a2ab25526bf53d03ebc23bd974938fb8370c67ae.
```

This is one `Q_5` enumeration, not an enumeration of `Q_5^2`.

The DPS target reconstruction is independent and yields ten rooted source
descriptors and exactly 54 target tuples, matching the immutable M188 target
set. All action permutations and target IDs are archived in `q5_action.json`.

## 4. Exact classification attempt and cap

`classify_q5.m` defines the 8,400-point permutation group, asks Magma for the
point stabilizer of `v`, its orbit on `u`, and explicit action words through
`WordGroup`. For each target it implements (2.1), writing a route word in the
positive case and the adjusted orbit point in every case.

Magma V2.29-4 remained in exact point-stabilizer/orbit construction for about
6 minutes 44 seconds, used about 591 MiB RSS at the last observation, and
created no output certificate. It was terminated under the coordinator's
six-minute cap. Accordingly, the stabilizer orbit is not asserted known and
the 54 targets are not classified here.

## 5. Exact conclusion

```text
PROVED: exact stabilizer-orbit membership criterion (2.1).
EXACT: complete 8,400-state Q5 signed action and 54 target IDs.
ACCEPTED INPUT: M188's 14 explicit positive routes.
INCONCLUSIVE: complete membership classification of all 54 targets.
```

No radius-limited miss is negative evidence. No all-`d`, every-color,
polynomial route-length, gap, mixing, or Terminal conclusion follows.
