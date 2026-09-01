# M236 immutable source and formula gate

Date: 2026-08-13 UTC. **SOURCE-ORDER ASSERTION:** this gate is fixed before
any `d=7 -> 8` endpoint is constructed or replayed.

## Frozen predecessor verification

Running `sha256sum -c SHA256SUMS` in each source mission returned `OK` for
every listed payload. The top inventory digests are

```text
M214 cb63ac879b036d096af369fabf02da9abecba786bcf746ba34d809b8ceaada3f
M218 3929f738afcb9834e74eea9610d284ca5cabe2589da05b691bf3b4447b58f656
M220 0b953e9c517cfeb379d32abe04b32ea928dd2a83e67bc1ac40d61f87fccd1316
M223 538eb1e0351a7ff005ca262261a1bd8056d868b98307b79e5948b9f1fd5b929d
M225 e61d77f0765c9aaba177ef0e0bca8b6f7f94758b7814bb7243846dff3f9f0acd
M228 d20259c79d993ef63f8aab8235afeb75792153be6948767a0552d84d70f12237
M231 63b6e790a86f1cfae2db971b28a46c1a173ad9c27560857ac60ce9c7ba0421db
M234 b5b5cb5f5f72be67efe92599a6381e23145eb34567a2ee75431ad087ba1ab903
```

The coordinator ledger accepts M214/M218 at L-0278, accepts the M220/M223
compact-key obstruction at L-0281, accepts the finite M225/M228 full-contour
table at L-0283, and accepts the M231/M234 route-normal quotient at L-0286.
All eight predecessor directories remain immutable.

## Exact M231 formula, with rank changed only to `d=7`

For an ordinary odd edit `i=2v-3`, let

```text
P(v)=(v,p(v),...,1),
lambda = 1 iff an internal vertex of P(v) is greater than v,
alpha  = 1 iff two consecutive internal entries of P(v) ascend,
kappa  = lambda OR alpha.
```

Put `L=d-v-1`. For `0<=t<L`, set

```text
c_t=1 iff p(v+t+1)=v,
epsilon_0=-1 if c_0=1, else +1,
epsilon_t=-1 if c_t=1, else -epsilon_(t-1).
```

The descriptor and assigned chronological signed-Hurwitz word are fixed as

```text
Z2(T,v) = ("closed",)                     if kappa=1,
           ("open",v,epsilon)             if kappa=0,

W(T,v) = identity                         if kappa=1,
         Q(v,epsilon) B_d Q(v,epsilon)^-1 if kappa=0,

Q(v,epsilon)=product_(t=0)^(L-1)
  R_(2(v+t)-2)^epsilon_t R_(2(v+t)-1)^epsilon_t,

B_d=R_(2d-4)^- R_(2d-3) R_(2d-2)^-
    R_(2d-3)^- R_(2d-4)^-.
```

For M236, `d=7`, hence

```text
B_7=R_10^- R_11 R_12^- R_11^- R_10^-.
```

No forward-exception bit, stopped-path remainder, off-path child list,
endpoint factor, mismatch location, target word, or discovered route enters
`Z2` or `W`.

## Predeclared row scopes

The **primary Z2 universe** is every one of the five ordinary odd edits

```text
{1,3,5,7,9}, corresponding to v={2,3,4,5,6},
```

on every tree on `[7]` for which root 7 is a leaf adjacent to 1. There are
exactly `6^4=1,296` such trees and therefore `6,480` primary rows.

The remaining fixed families are checked only as a **secondary full-table
reconciliation**, not as Z2 rows:

```text
internal even edits {2,4,6,8} -> identity,
edit 10 -> (R_9^-)^2,
edit 11 -> R_12^-.
```

Together the secondary and primary scopes comprise all `1,296*11=14,256`
adjacent-label endpoint rows. A secondary failure would refute that fixed
full-table reconciliation but would not by itself be a same-Z2 obstruction.

## Immutable decision rule

The checker must assign `Z2` and `W` before constructing either endpoint and
must perform no endpoint-derived adaptation, quotient/group enumeration,
route search, target lookup, or formula refinement.

- If all 6,480 primary rows pass, freeze only a finite `d=7 -> 8` theorem.
- If a primary row fails, freeze the first deterministic witness. A
  same-Z2 group containing both a pass and a failure proves descriptor
  insufficiency for endpoint behavior; otherwise classify the event only as
  failure of the predeclared word formula on the witness.

No all-rank, every-color, polynomial-length, gap, mixing, or Terminal
conclusion is permitted.

