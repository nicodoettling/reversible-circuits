# C1-v1: distinct-edge relator blocks with bounded Hurwitz scrambling

Frozen authored algorithm, 2026-10-29. This document specifies a candidate, not a security assertion. Target for comparison is M0's complete noisy word against the same Q_k applied to the GLOBAL U(N,L) law. Rightmost-first products throughout.

## Parameters, setup, interfaces

Finite family: N>=4, B>=1, L=6B, s>=0 integer, 0<=k<=L. Setup exposes A=(N,B,s,k) and has no secret K. Each request independently samples all label and scrambling tapes. Reference exposes identical A; no part of its global bridge depends on A except N,L. Reused setup changes nothing: all tapes are fresh. Gates are canonical unordered pairs of distinct integers in [N].

A concrete polynomial schedule is lambda>=2 integer, N=lambda^2, B=lambda^6, L=6lambda^6, s=floor(B/10), k=lambda. Costs are polynomial in lambda,N,L, not in log_2(N). The common semantic error upper bound is min(1,4/lambda), not a negligible-error guarantee.

## Exact sampler

For j=1,...,B choose an ordered tuple (a,b,c,d) uniformly from distinct labels in [N], independently across j. Emit the six gates

    (ac), (cd), (ab), (ad), (bc), (bd).

Concatenate these B blocks. Then repeat s times: choose i uniformly from {1,...,L-1}, choose an independent uniform bit, and apply either

    H_i: (u,v) -> (v, vuv)
    H_i^{-1}: (u,v) -> (uvu, u).

All other positions remain fixed. The candidate sampler outputs this word. M0 then applies its independent hidden uniform-k-subset replacement. No cyclic shift, global conjugation, further walk, secret decoder or unmentioned compiler is included.

## Identity and entropy

The first triple (ac)(cd)(ab) equals the 4-cycle (a b c d). The last triple (ad)(bc)(bd) equals its inverse. Hence every block has identity product, all six gates are distinct, and adjacent repeats do not occur within a fresh block. Both Hurwitz maps preserve the two-factor product, length, and transposition gate library. Identity before noise is therefore exact for every tape.

The label tuple is recoverable from the six-gate block: c is the intersection of gates 1 and 2, a the other endpoint of gate 1, b the other endpoint of gate 3, d the other endpoint of gate 2. Thus pre-scramble Shannon entropy is B log_2((N)_4). Each fixed scrambling tape is a bijection on all words, so conditioning on that independent tape preserves this entropy. Forgetting the tape cannot lower entropy. This is an entropy lower bound, not closeness to the bridge law.

Using pair relabeling, each Hurwitz move takes O(1) label operations. Sampling and output take expected O(L+s) label operations, O((L+s)log N) random bits under exact rejection-bit samplers, and O(L) memory. Runtime bounds count label arithmetic; conventional bit costs add polynomial factors in log N. The exact ideal law uses uniform finite choices, with rejection sampling as an implementation.

## Explicit exclusions and boundary handling

This is not defined for N<4 or lengths not divisible by 6; the general game still allows those cases, to be checked by separate controls. Odd L is never an identity candidate. k=0 and k=L remain valid channel parameters; at k=L both worlds are exactly iid uniform gates. The primary schedule does not cover those endpoints. No computational or statistical indistinguishability claim is asserted. A successful check of one gate or endpoint cannot certify full-word security. Only this frozen algorithm may be called C1-v1.
