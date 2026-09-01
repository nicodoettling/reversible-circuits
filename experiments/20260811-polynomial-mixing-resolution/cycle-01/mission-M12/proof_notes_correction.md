# Correction to `proof_notes.md`

In the proof of Theorem 5.3, replace the parenthetical claim that repeating
one transposition `m` times lies in `A_2`.  That is true only when `m=6`.
For every even `6 <= m <= 2(N-1)`, nonemptiness of `A_2` instead follows by
taking a connected genus-two identity word on `m/2-1 >= 2` labels; its
required length is

```text
2((m/2-1)-1) + 4 = m,
```

and existence follows from the proved feasible-component criterion.  No
inequality or later argument changes.  This correction supersedes only that
parenthetical nonemptiness witness.
