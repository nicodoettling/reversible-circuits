# M234 symbolic audit of the `Z2` literal-word kernel

Date: 2026-08-13 UTC.  Status: **proved for the declared formula at fixed
rank**.

Fix `d` and an ordinary odd edit `i=2v-3`.  Put

```text
L=d-v-1,
kappa=late OR ascent,
Z2=("closed",)                         if kappa=1,
   ("open",v,epsilon)                  if kappa=0.
```

The declared literal formula is

```text
W=identity                             if kappa=1,
  Q(v,epsilon) B_d Q(v,epsilon)^-1     if kappa=0,

Q(v,epsilon)=product_(t=0)^(L-1)
 R_(2(v+t)-2)^epsilon_t R_(2(v+t)-1)^epsilon_t.
```

## Forward implication

Every symbol in `W` is determined by `Z2`: the closed key selects the empty
word, while an open key determines `v`, every transport-generator position,
and every sign.  Thus equal `Z2` values give literally equal words.  The full
stopped path, off-path incidence lists, child bits before the sign automaton,
and forward-exception bit do not appear in the formula.

## Converse implication

The closed word has length zero.  Every open word has length

```text
2L + 5 + 2L = 4L+5 > 0,
```

so no open word equals the closed word.  At fixed `d`, the length `4L+5`
determines `L`, hence determines `v=d-L-1`; therefore open words with distinct
edited vertices cannot be literally equal.

Now fix `v`.  If `epsilon` and `epsilon'` first differ at index `t`, their
literal words agree before the corresponding transport stage and then contain
different signed generators at the first position of the pair

```text
R_(2(v+t)-2)^epsilon_t R_(2(v+t)-1)^epsilon_t.
```

Hence the words differ.  Thus equality of literal open words forces equality
of `epsilon`, and therefore equality of `Z2`.

Combining the two directions proves, on every descriptor value to which the
declared formula applies,

```text
Z2(T,v)=Z2(T',v')  iff  W(T,v)=W(T',v')
```

as literal signed-generator sequences at fixed `d`.

## Boundary

This is a syntax theorem about the displayed formula.  Endpoint correctness
is separate and is checked exhaustively at `d=6 -> 7` by M234.  The argument
does not show that the formula closes DPS endpoints at another rank.

