# M67 theorem correction 1: Gram numerator normalization

Date: 2026-08-12. This append-only correction supersedes exactly one sentence
in frozen `theorem.md` (SHA-256
`0d54a909df520c12547ea56ae6684f6b93bf6a2b8d8602a41ea4dd4af830dff5`).
No other statement or equation is changed.

In Section 2 immediately before equation (2.5), replace

```text
The Gram numerator is lV_f+l(l-1)Re<f,Kf>,
```

by the correctly normalized statement

```text
Because every block of M16's Gram operator carries the prefactor 1/l,
the aligned Gram numerator is

    V_f+(l-1)Re<f,Kf>.

The direct-sum norm is lV_f, so the Rayleigh quotient is

    [V_f+(l-1)Re<f,Kf>]/[lV_f]
      =1/l+(l-1)kappa_f/l.
```

This agrees with equation (2.5), the M67 report, and the independently checked
M16 scalar normalization. The frozen theorem's preceding displayed numerator
was a transcription error; if it were used literally, it would contradict its
own equation (2.5). The corrected composite theorem is `theorem.md` read with
this replacement.
