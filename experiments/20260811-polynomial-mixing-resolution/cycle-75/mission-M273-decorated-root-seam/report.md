# M273 final report: decorated root seam

## Verdict

```text
PROMOTE THE STANDALONE DL-RST THEOREM ONLY AFTER FRESH IMMUTABLE AUDIT.

THE CANDIDATE PROOF CLOSES THE LITERAL a=1 ROOT ROW, INCLUDING EVERY
PERSISTENT/DISCHARGED PORT AND ALL FOUR ROOT LABELS.

DO NOT YET PROMOTE IDL, THE ORDINARY-EDIT ROUTE, OR ANY DOWNSTREAM CLAIM.
```

## Strongest result

Put `m=2d-2`, `s=m-R_v`, and
`(alpha,beta,gamma,delta)=(m-1,m,m+1,m+2)`. In coordinates cut at
`q_0=R_v`, the old root slot and the new child `d` both occupy
`(q_(s-1),q_s)=(alpha,beta)`, while the new root occupies
`(q_(s+1),q_(s+2))=(gamma,delta)`.

The new-child six-token macro lies wholly on the `x_1` arm for all three
literal incoming forms: direct-root reversed base, decorated lens, and
canonical residual. Its two rows close `beta` then `alpha`, both at distance
three to `x_1`.

For a decreasing-path/open input, the root row contracts to `F_v(s)` old and
`F_v(s+2)` new. The exact root-complement rows are

```text
W_d^alpha     S^beta  S^alpha S_A B_v^alpha -> S,
W_(d+1)^gamma S^delta S^gamma S_A B_v^gamma -> S.
```

They record `x_v`; every lower root-white/lens-black row has distance one.
The remaining individual port whites and `R_v` then attach to the final
root. This gives

```text
open old: b_d(alpha)=v, b_d(beta)=d;
open new: b_(d+1)(alpha)=b_(d+1)(beta)=1,
          b_(d+1)(gamma)=v, b_(d+1)(delta)=d+1.
```

For a canonical input or a lens expanding at the root, both ranks leave
`C_1`. Old `alpha,beta` and new `gamma,delta` reach their final roots, while
new `alpha,beta` already recorded `x_1`. Hence

```text
sealed old: b_d(alpha)=b_d(beta)=d;
sealed new: b_(d+1)(alpha)=b_(d+1)(beta)=1,
            b_(d+1)(gamma)=b_(d+1)(delta)=d+1.
```

## Individual ports and inherited labels

For every inherited nonroot slot,

```text
t^+(h)=t(h)     for h>v,
t^+(h)=t(h)+2   for h<v.
```

This preserves every strict-internal width comparison and every port's first
discharge event. A port above the initialization width discharges there; a
persistent port discharges at the first contraction below its slot or at the
first expansion. The endpoint is that current parent at both ranks. In
particular, a smaller port on a decreasing path can discharge at a nonroot
`x_b`; it is not silently assigned to `x_1`.

At final open width, precisely the direct children `h>v,p(h)=v` remain.
Their two literal whites, and the `R_v` white, attach to roots `d,d+1`.
Every other inherited low label has the same distance-three endpoint at the
two ranks. In the sealed case all inherited low endpoints agree.

The proof separately treats all incoming cases:

1. direct-root reversed base gives the paired contracted lenses;
2. `F_v(r)` with `r>s` contracts, while `r<s` expands to `C_1`;
3. `C_a` propagates to `C_1`.

The inequalities are preserved under the rank map, equality is impossible,
and direct-root `p(v)=1`, `v=d-1`, empty arms, empty port sets, and post-wrap
siblings are explicit.

## Conditional composition after audit

If a fresh referee accepts the frozen theorem, accepted M269/M271 plus DL-RST
give exactly M250's endpoint outputs `(4.3)--(4.5)`, with the refuted one-bit
transition `(4.2)` replaced by the literal cyclic-width transducer.
M250/M254's accepted coordinate exhaustion would then prove the ordinary
odd-edit IDL, and M240/M242 would give the corresponding route-normal closure
of length at most `4d-7`.

This is only a formal dependency implication until the fresh audit accepts
M273. It does not resurrect the false one-bit CPR rule and does not address
fixed edits, every-color synchronization, congestion, a spectral gap,
polynomial mixing, or a Terminal.

## Exact guard

After the formulas were frozen in `checkpoint.md`, the no-import full DPS
replay checked exactly four cases: direct-root `v=d-1`, decreasing multilevel
with a persistent larger port and a smaller port discharging at nonroot
`x_2`, root expansion with a port, and an already-sealed path. All checks
pass. The four-row digest is

```text
922fca4abe3fce67064cb5e5963a69ee222f4fa2fa2c6f89f110a5b0c62e1695.
```

Reproduction:

```text
repository commit        502a6f031c6d5a4bc0064ee5b370a4fa3914f993
command                  python3 -B root_seam_guard.py
Python                   3.12.3
nonstandard dependencies none
seed                     none (deterministic)
raw output               root_seam_guard_results.json
```

The guard is exact finite calibration only. The interval proof in
`decorated_root_seam.md` carries the arbitrary-rank statement.

